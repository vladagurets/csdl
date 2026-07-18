from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_analytical_mode import apply_transformations


EXPECTED_FAMILIES = [
    "bar",
    "line",
    "scatterplot",
    "waterfall",
    "heatmap",
    "funnel",
    "map",
    "network",
    "table",
    "dashboard",
]
EXPECTED_COMPONENTS = [
    "Anchor",
    "Signal",
    "Field",
    "Frame",
    "Cluster",
    "Vector",
    "Divider",
    "Node",
    "Loop",
    "Collision",
    "Bridge",
    "Axis",
    "Pulse",
    "Label",
    "Legend",
]


def _load(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} must be readable YAML: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return value


def _find_forbidden_keys(value: Any, forbidden: set[str]) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in forbidden:
                found.add(str(key).lower())
            found.update(_find_forbidden_keys(child, forbidden))
    elif isinstance(value, list):
        for child in value:
            found.update(_find_forbidden_keys(child, forbidden))
    return found


def validate_analytical_dataset(
    data: dict[str, Any], root: Path, label: str = "dataset"
) -> list[str]:
    errors: list[str] = []
    schema = _load(root / "dataset-schema.yaml", errors, "dataset schema")
    if data.get("language") != "CSDL" or str(data.get("version")) != "0.1":
        errors.append(f"{label} must use CSDL analytical dataset version 0.1")
    if data.get("kind") != "analytical-dataset":
        errors.append(f"{label} kind must equal analytical-dataset")
    dataset = data.get("dataset")
    if not isinstance(dataset, dict):
        return errors + [f"{label} dataset must be a mapping"]
    missing = sorted(set(schema.get("required_dataset_fields", [])) - set(dataset))
    if missing:
        errors.append(f"{label} dataset missing fields: {','.join(missing)}")
        return errors
    fields = dataset.get("fields")
    records = dataset.get("records")
    if not isinstance(fields, list) or not fields:
        errors.append(f"{label} fields must be a non-empty list")
        fields = []
    if not isinstance(records, list) or not records:
        errors.append(f"{label} records must be a non-empty list")
        records = []
    field_ids = [field.get("id") for field in fields if isinstance(field, dict)]
    if len(field_ids) != len(set(field_ids)):
        errors.append(f"{label} field ids must be unique")
    allowed_types = set(schema.get("field_types", []))
    allowed_roles = set(schema.get("field_roles", []))
    for field in fields:
        if not isinstance(field, dict):
            errors.append(f"{label} fields must contain mappings")
            continue
        missing_field = sorted(set(schema.get("field_required", [])) - set(field))
        if missing_field:
            errors.append(f"{label} field missing fields: {','.join(missing_field)}")
        if field.get("type") not in allowed_types:
            errors.append(f"{label} field type is invalid: {field.get('id')}")
        if field.get("role") not in allowed_roles:
            errors.append(f"{label} field role is invalid: {field.get('id')}")
        if field.get("type") == "quantitative" and field.get("role") == "measure" and not field.get("unit"):
            errors.append(f"quantitative measure must declare unit: {field.get('id')}")
    record_ids = [record.get("id") for record in records if isinstance(record, dict)]
    if len(record_ids) != len(set(record_ids)) or any(not value for value in record_ids):
        errors.append(f"{label} record ids must be unique non-empty values")
    provenance = dataset.get("provenance", {})
    missing_provenance = sorted(set(schema.get("provenance_required", [])) - set(provenance))
    if missing_provenance:
        errors.append(f"{label} provenance missing fields: {','.join(missing_provenance)}")
    missing_statuses = set(schema.get("missing_statuses", []))
    for item in dataset.get("missing_values", []):
        if item.get("status") not in missing_statuses:
            errors.append(f"{label} missing status is invalid")
        if item.get("record_id") not in record_ids or item.get("field") not in field_ids:
            errors.append(f"{label} missing value reference is invalid")
    missing_pairs = {
        (item.get("record_id"), item.get("field"))
        for item in dataset.get("missing_values", [])
        if isinstance(item, dict)
    }
    for record in records:
        for field_id in field_ids:
            if field_id == "id":
                continue
            if record.get(field_id) is None and (record.get("id"), field_id) not in missing_pairs:
                errors.append(
                    f"dataset null requires one missing declaration: {record.get('id')}.{field_id}"
                )
    transformations = dataset.get("transformations", [])
    allowed_operations = set(schema.get("transformation_operations", []))
    required_transform = set(schema.get("transformation_required", []))
    for transformation in transformations:
        missing_transform = sorted(required_transform - set(transformation))
        if missing_transform:
            errors.append(f"transformation missing fields: {','.join(missing_transform)}")
        if transformation.get("operation") not in allowed_operations:
            errors.append(f"transformation operation is invalid: {transformation.get('id')}")
        if not transformation.get("reversible") and not transformation.get("auditable"):
            errors.append(f"transformation must be reversible or auditable: {transformation.get('id')}")
    return errors


def _validate_dataset(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    data = _load(path, errors, path.name)
    if errors:
        return errors
    return validate_analytical_dataset(data, root, path.name)


def validate_analytical_package(
    package: dict[str, Any], root: Path
) -> list[str]:
    errors: list[str] = []
    manifest = _load(root / "manifest.yaml", errors, "analytical manifest")
    schema = _load(root / "encoding-schema.yaml", errors, "encoding schema")
    compatibility = _load(
        root / "contracts/compatibility.yaml", errors, "compatibility source"
    )
    if errors:
        return errors
    required = set(schema.get("required_package_fields", []))
    missing = sorted(required - set(package))
    if missing:
        errors.append("analytical package missing fields: " + ",".join(missing))
        return errors
    unknown = sorted(set(package) - set(schema.get("allowed_package_fields", [])))
    if unknown:
        errors.append("analytical package contains unknown fields: " + ",".join(unknown))
    if package.get("language") != "CSDL" or str(package.get("version")) != "0.1":
        errors.append("analytical package must use CSDL version 0.1")
    if package.get("kind") != "analytical-package":
        errors.append("analytical package kind must equal analytical-package")
    forbidden = {str(key).lower() for key in schema.get("forbidden_keys", [])}
    for key in sorted(_find_forbidden_keys(package, forbidden)):
        errors.append(f"analytical package contains forbidden key: {key}")

    dataset_ref = package.get("dataset", {})
    dataset_path = root / str(dataset_ref.get("path", ""))
    dataset_document = _load(dataset_path, errors, "canonical analytical dataset")
    if not dataset_document:
        return errors
    errors.extend(validate_analytical_dataset(dataset_document, root, dataset_path.name))
    dataset = dataset_document.get("dataset", {})
    if dataset_ref.get("id") != dataset.get("id"):
        errors.append("analytical package dataset identity must match canonical dataset")
    if dataset_ref.get("version") != dataset.get("version"):
        errors.append("analytical package dataset version must match canonical dataset")
    if dataset_ref.get("source") != dataset.get("provenance", {}).get("source"):
        errors.append("analytical package source must match canonical dataset")

    specification = package.get("specification", {})
    for field, message in (
        ("records", "analytical specification records must match canonical dataset"),
        ("fields", "analytical specification fields must match canonical dataset"),
        ("ordering", "analytical specification ordering must match canonical dataset"),
        ("missing_values", "analytical specification missing values must match canonical dataset"),
        ("transformations", "analytical specification transformations must match canonical dataset"),
    ):
        if specification.get(field) != dataset.get(field):
            errors.append(message)
    try:
        derived = apply_transformations(dataset)
    except (KeyError, TypeError, ValueError) as error:
        errors.append(f"analytical transformations cannot be recomputed: {error}")
        derived = None
    if derived is not None and specification.get("derived") != derived:
        errors.append("analytical specification derived values must match canonical dataset")

    family = specification.get("family")
    if family not in manifest.get("family_order", []):
        errors.append(f"analytical family is undeclared: {family}")
        family_contract = {}
    else:
        family_contract = compatibility.get("families", {}).get(family, {})
    encoding = package.get("encoding", {})
    fields = {field["id"]: field for field in dataset.get("fields", [])}
    bindings = encoding.get("bindings", {})
    if not isinstance(bindings, dict) or not bindings:
        errors.append("analytical encoding requires field bindings")
        bindings = {}
    for channel, field_id in bindings.items():
        if isinstance(field_id, str) and field_id not in fields:
            errors.append(f"analytical binding references undeclared field: {channel}")
        elif isinstance(field_id, list):
            for value in field_id:
                if value not in fields:
                    errors.append(f"analytical binding references undeclared field: {channel}")
    marks = encoding.get("marks", [])
    allowed_marks = set(family_contract.get("marks", []))
    internal_marks = set(schema.get("internal_marks", []))
    for mark in marks:
        mark_type = mark.get("type") if isinstance(mark, dict) else None
        if mark_type not in internal_marks:
            errors.append(f"analytical mark is undeclared: {mark_type}")
        elif mark_type not in allowed_marks:
            errors.append(f"analytical mark {mark_type} is incompatible with family {family}")

    allowed_components = set(family_contract.get("components", []))
    public_components = set(manifest.get("public_components", []))
    instances = package.get("component_instances", [])
    instance_ids: set[str] = set()
    for instance in instances:
        identifier = instance.get("id")
        component = instance.get("component")
        if identifier in instance_ids or not identifier:
            errors.append("analytical component instance ids must be unique non-empty values")
        instance_ids.add(identifier)
        if component not in public_components:
            errors.append(f"analytical component is not public: {component}")
        elif component not in allowed_components:
            errors.append(f"component {component} is incompatible with analytical family {family}")
    component_manifest_path = root.parents[1] / manifest["library"]["component_library"]
    component_manifest = _load(component_manifest_path, errors, "component manifest")
    relation_types = set(component_manifest.get("vocabulary", {}).get("relations", []))
    for relation in package.get("relations", []):
        if relation.get("subject") not in instance_ids or relation.get("object") not in instance_ids:
            errors.append("analytical relation endpoint is undeclared")
        if relation.get("type") not in relation_types:
            errors.append(f"analytical relation is not public: {relation.get('type')}")

    recipe = package.get("recipe", {})
    if str(recipe.get("id")) not in set(family_contract.get("recipes", [])):
        errors.append(f"recipe {recipe.get('id')} is incompatible with analytical family {family}")
    recipe_root = root.parents[1] / "recipes/recipe-library-v0.5"
    recipe_record_path = next(
        (
            recipe_root / entry["record"]
            for entry in _load(recipe_root / "manifest.yaml", errors, "recipe manifest").get("recipes", [])
            if str(entry.get("id")) == str(recipe.get("id"))
        ),
        None,
    )
    if recipe_record_path is None:
        errors.append(f"analytical recipe is undeclared: {recipe.get('id')}")
    else:
        recipe_record = _load(recipe_record_path, errors, "analytical recipe record")
        if recipe.get("slug") != recipe_record.get("slug") or recipe.get("version") != recipe_record.get("version"):
            errors.append("analytical recipe reference must match Recipe Library v0.5")

    if encoding.get("color_only_meaning") is not False or not encoding.get("redundant_encodings"):
        errors.append("color cannot be the sole carrier of meaning")
    if encoding.get("decorative_field_area_percent", 0) > 5:
        errors.append("decorative Field area cannot exceed 5 percent")
    if encoding.get("dual_axis") is True:
        exception = encoding.get("dual_axis_exception", {})
        if not all(exception.get(key) for key in ("rationale", "independent_units", "non_misleading_review")):
            errors.append("dual axis requires an explicit exception")
    scales = encoding.get("scales", {})
    if any(scale == "log" for scale in scales.values()):
        if encoding.get("log_scale_declared") is not True:
            errors.append("log scale requires explicit declaration")
        else:
            for field_id in bindings.values():
                if isinstance(field_id, str) and fields.get(field_id, {}).get("type") == "quantitative":
                    if any(record.get(field_id) is not None and record.get(field_id) <= 0 for record in dataset.get("records", [])):
                        errors.append("log scale requires positive-only quantitative values")
    if package.get("provenance", {}).get("deterministic") is not True:
        errors.append("analytical package must declare deterministic output")

    if family == "bar":
        if encoding.get("zero_baseline") is not True:
            errors.append("bar encoding requires a zero baseline")
        value_domain = encoding.get("domains", {}).get("value", [])
        if not isinstance(value_domain, list) or len(value_domain) != 2 or not (value_domain[0] <= 0 <= value_domain[1]):
            errors.append("bar value domain must include zero")
        expected_order = dataset.get("ordering", {}).get("values")
        if encoding.get("order") != expected_order:
            errors.append("bar category order must match canonical dataset")
    return errors


def validate_analytical_library(root: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    manifest = _load(root / "manifest.yaml", errors, "analytical manifest")
    dataset_schema = _load(root / "dataset-schema.yaml", errors, "dataset schema")
    encoding_schema = _load(root / "encoding-schema.yaml", errors, "encoding schema")
    global_contract = _load(root / "contracts/global.yaml", errors, "global contract")
    family_contracts = _load(root / "contracts/families.yaml", errors, "family contracts")
    compatibility = _load(root / "contracts/compatibility.yaml", errors, "compatibility source")
    if errors:
        return errors
    library = manifest.get("library", {})
    if library.get("id") != "analytical-mode-v0.1" or library.get("version") != "0.1.0":
        errors.append("analytical manifest identity/version is invalid")
    if library.get("prompt_dsl_compatibility") != "0.5":
        errors.append("analytical manifest must preserve Prompt DSL v0.5 compatibility")
    if manifest.get("family_order") != EXPECTED_FAMILIES:
        errors.append("analytical family order must match the ten-family contract")
    if manifest.get("public_components") != EXPECTED_COMPONENTS:
        errors.append("analytical public components must equal D-029")
    if list(family_contracts.get("families", {})) != EXPECTED_FAMILIES:
        errors.append("family contracts must cover all families in canonical order")
    if list(compatibility.get("families", {})) != EXPECTED_FAMILIES:
        errors.append("compatibility source must cover all families in canonical order")
    if encoding_schema.get("mark_scope") != "internal_data_encoding_only":
        errors.append("analytical marks must remain internal data encodings")
    if global_contract.get("fidelity", {}).get("quantitative_relationships_override_style") is not True:
        errors.append("global contract must prioritize quantitative fidelity")
    for entry in manifest.get("datasets", []):
        path = root / str(entry.get("path", ""))
        if path.exists():
            dataset_errors = _validate_dataset(path, root)
            errors.extend(dataset_errors)
            if not dataset_errors:
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                if data.get("dataset", {}).get("id") != entry.get("id"):
                    errors.append(f"{path.name} identity must match manifest")
        elif require_complete:
            errors.append(f"missing analytical dataset: {entry.get('path')}")
    if require_complete:
        for proof in manifest.get("proofs", []):
            if not (root / str(proof.get("source", ""))).is_file():
                errors.append(f"missing analytical proof source: {proof.get('source')}")
            if not (root / str(proof.get("package", ""))).is_file():
                errors.append(f"missing analytical proof package: {proof.get('package')}")
        for key in ("index", "dataset_index", "compatibility"):
            if not (root / str(library.get(key, ""))).is_file():
                errors.append(f"missing analytical derived output: {library.get(key)}")
    return errors


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("usage: python tools/validate_analytical_mode.py ROOT [--incomplete]")
        return 2
    root = Path(sys.argv[1])
    require_complete = len(sys.argv) == 2
    if not require_complete and sys.argv[2] != "--incomplete":
        print("usage: python tools/validate_analytical_mode.py ROOT [--incomplete]")
        return 2
    errors = validate_analytical_library(root, require_complete=require_complete)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("analytical mode valid" if require_complete else "analytical mode incomplete contract valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
