from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


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


def _validate_dataset(path: Path, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    data = _load(path, errors, path.name)
    if not data:
        return errors
    if data.get("language") != "CSDL" or str(data.get("version")) != "0.1":
        errors.append(f"{path.name} must use CSDL analytical dataset version 0.1")
    if data.get("kind") != "analytical-dataset":
        errors.append(f"{path.name} kind must equal analytical-dataset")
    dataset = data.get("dataset")
    if not isinstance(dataset, dict):
        return errors + [f"{path.name} dataset must be a mapping"]
    missing = sorted(set(schema.get("required_dataset_fields", [])) - set(dataset))
    if missing:
        errors.append(f"{path.name} dataset missing fields: {','.join(missing)}")
        return errors
    fields = dataset.get("fields")
    records = dataset.get("records")
    if not isinstance(fields, list) or not fields:
        errors.append(f"{path.name} fields must be a non-empty list")
        fields = []
    if not isinstance(records, list) or not records:
        errors.append(f"{path.name} records must be a non-empty list")
        records = []
    field_ids = [field.get("id") for field in fields if isinstance(field, dict)]
    if len(field_ids) != len(set(field_ids)):
        errors.append(f"{path.name} field ids must be unique")
    allowed_types = set(schema.get("field_types", []))
    allowed_roles = set(schema.get("field_roles", []))
    for field in fields:
        if not isinstance(field, dict):
            errors.append(f"{path.name} fields must contain mappings")
            continue
        missing_field = sorted(set(schema.get("field_required", [])) - set(field))
        if missing_field:
            errors.append(f"{path.name} field missing fields: {','.join(missing_field)}")
        if field.get("type") not in allowed_types:
            errors.append(f"{path.name} field type is invalid: {field.get('id')}")
        if field.get("role") not in allowed_roles:
            errors.append(f"{path.name} field role is invalid: {field.get('id')}")
    record_ids = [record.get("id") for record in records if isinstance(record, dict)]
    if len(record_ids) != len(set(record_ids)) or any(not value for value in record_ids):
        errors.append(f"{path.name} record ids must be unique non-empty values")
    provenance = dataset.get("provenance", {})
    missing_provenance = sorted(set(schema.get("provenance_required", [])) - set(provenance))
    if missing_provenance:
        errors.append(f"{path.name} provenance missing fields: {','.join(missing_provenance)}")
    missing_statuses = set(schema.get("missing_statuses", []))
    for item in dataset.get("missing_values", []):
        if item.get("status") not in missing_statuses:
            errors.append(f"{path.name} missing status is invalid")
        if item.get("record_id") not in record_ids or item.get("field") not in field_ids:
            errors.append(f"{path.name} missing value reference is invalid")
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
            dataset_errors = _validate_dataset(path, dataset_schema)
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
