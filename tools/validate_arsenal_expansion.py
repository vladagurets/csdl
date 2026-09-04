from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_arsenal_expansion import (
    derive_analytical_proof,
    derive_compatibility,
    derive_index,
)


EXPECTED_RECIPES = [
    "Causal Chain",
    "State Machine",
    "Dependency Map",
    "Claim / Evidence",
    "Spectrum",
    "Anatomy",
    "Layer Stack",
    "Roadmap",
]
EXPECTED_COMPONENTS = ["Threshold", "Trace", "Band"]
EXPECTED_RELATIONS = [
    "causes",
    "transitions_to",
    "depends_on",
    "supports",
    "crosses",
]
EXPECTED_ANALYTICAL_FAMILIES = [
    "histogram",
    "boxplot",
    "intervalplot",
    "bullet",
    "gantt",
    "sankey",
]
FORBIDDEN_ALIASES = {"Container", "Gate", "Layer", "Marker", "Path"}
FORBIDDEN_LAYOUT_KEYS = {
    "layout",
    "geometry",
    "coordinates",
    "card",
    "panel",
    "container",
    "sidebar",
}


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


def _find_forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_LAYOUT_KEYS:
                found.add(str(key).lower())
            found.update(_find_forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(_find_forbidden_keys(child))
    return found


def _repository_root(root: Path) -> Path:
    if root.parent.name != "extensions":
        raise ValueError("arsenal expansion must live under extensions/")
    return root.parents[1]


def validate_arsenal_expansion(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        repository = _repository_root(root)
    except ValueError as error:
        return [str(error)]
    manifest = _load(root / "manifest.yaml", errors, "arsenal manifest")
    if not manifest:
        return errors

    extension = manifest.get("extension", {})
    if extension != {
        "id": "arsenal-expansion-v0.1",
        "version": "0.1.0",
        "status": "candidate",
        "language": "CSDL",
        "kind": "evidence-gated-extension",
    }:
        errors.append("arsenal extension identity must match v0.1 candidate contract")

    baseline = manifest.get("baseline", {})
    baseline_paths = {
        "component_library": ("component_count", "components"),
        "recipe_library": ("recipe_count", "recipes"),
        "analytical_mode": ("analytical_family_count", "family_order"),
    }
    for path_key, (count_key, collection_key) in baseline_paths.items():
        source = _load(
            repository / str(baseline.get(path_key, "")),
            errors,
            f"baseline {path_key}",
        )
        expected = baseline.get(count_key)
        if source and len(source.get(collection_key, [])) != expected:
            errors.append(f"baseline {path_key} count must remain {expected}")

    inventory_path = repository / str(manifest.get("protected_raster_inventory", ""))
    inventory = _load(inventory_path, errors, "protected raster inventory")
    if inventory and (
        inventory.get("file_count") != 60
        or len(inventory.get("files", [])) != 60
    ):
        errors.append("protected raster inventory must retain exactly 60 files")

    component_entries = manifest.get("components", [])
    recipe_entries = manifest.get("recipes", [])
    if [entry.get("name") for entry in component_entries] != EXPECTED_COMPONENTS:
        errors.append("component candidate order must match approved expansion")
    if [entry.get("name") for entry in recipe_entries] != EXPECTED_RECIPES:
        errors.append("recipe candidate order must match approved expansion")
    if manifest.get("relations") != EXPECTED_RELATIONS:
        errors.append("relation candidate order must match approved expansion")
    if manifest.get("analytical_families") != EXPECTED_ANALYTICAL_FAMILIES:
        errors.append("analytical family candidate order must match approved expansion")

    component_records: dict[str, dict[str, Any]] = {}
    for entry in component_entries:
        record = _load(root / str(entry.get("record", "")), errors, f"component {entry.get('name')}")
        if not record:
            continue
        name = entry.get("name")
        if record.get("name") != name:
            errors.append(f"component record name must match manifest: {name}")
        if record.get("status") != "candidate":
            errors.append(f"component candidate status must equal candidate: {name}")
        if record.get("name") in FORBIDDEN_ALIASES:
            errors.append(f"component candidate is a retired or redundant alias: {record.get('name')}")
        if not record.get("distinct_from") or not record.get("semantic_meaning"):
            errors.append(f"component candidate must declare semantic distinction: {name}")
        specification = root / str(record.get("specification", ""))
        if not specification.is_file():
            errors.append(f"missing component candidate specification: {name}")
        component_records[str(name)] = record

    baseline_components = _load(
        repository / str(baseline.get("component_library", "")),
        errors,
        "baseline component library",
    ).get("vocabulary", {}).get("components", [])
    allowed_components = set(baseline_components) | set(EXPECTED_COMPONENTS)
    baseline_relations = set(
        _load(
            repository / str(baseline.get("component_library", "")),
            errors,
            "baseline component relations",
        ).get("vocabulary", {}).get("relations", [])
    )
    allowed_relations = baseline_relations | set(EXPECTED_RELATIONS)
    component_usage = {name: set() for name in EXPECTED_COMPONENTS}

    for entry in recipe_entries:
        name = entry.get("name")
        record = _load(root / str(entry.get("record", "")), errors, f"recipe {name}")
        if not record:
            continue
        if record.get("name") != name or record.get("id") != entry.get("id"):
            errors.append(f"recipe record identity must match manifest: {name}")
        if record.get("status") != "candidate":
            errors.append(f"recipe candidate status must equal candidate: {name}")
        if not record.get("problem") or not record.get("distinguishes_from"):
            errors.append(f"recipe candidate must declare a distinct problem: {name}")
        if len(record.get("allowed_scenarios", [])) < 2:
            errors.append(f"recipe candidate needs at least two scenarios: {name}")
        if set(record.get("expression_levels", {})) != {"A", "B", "C"}:
            errors.append(f"recipe candidate must preserve A/B/C: {name}")
        if not set(record.get("expression_modes", [])).issubset(
            {"editorial", "structural", "analytical"}
        ):
            errors.append(f"recipe candidate has unknown expression mode: {name}")
        ingredients = record.get("ingredients", {})
        all_ingredients = ingredients.get("required", []) + ingredients.get("optional", [])
        for ingredient in all_ingredients:
            component = ingredient.get("component")
            if component not in allowed_components:
                errors.append(f"recipe candidate uses undeclared component: {name}.{component}")
            if component in component_usage:
                component_usage[component].add(str(name))
        for group in record.get("relations", {}).values():
            for relation in group:
                if relation.get("type") not in allowed_relations:
                    errors.append(
                        f"recipe candidate uses undeclared relation: {name}.{relation.get('type')}"
                    )
        forbidden = _find_forbidden_keys(record)
        for key in sorted(forbidden):
            errors.append(f"recipe candidate contains forbidden layout key: {name}.{key}")
        for key in ("record", "specification", "prompt"):
            path = root / str(record.get(key, ""))
            if not path.is_file():
                errors.append(f"missing recipe candidate {key}: {name}")

    modes = _load(root / "expressions/modes.yaml", errors, "expression modes")
    if modes.get("expression_levels") != ["A", "B", "C"]:
        errors.append("expression modes must preserve A/B/C")
    if list(modes.get("modes", {})) != ["editorial", "structural", "analytical"]:
        errors.append("expression mode order must be editorial, structural, analytical")

    family_document = _load(root / "analytics/families.yaml", errors, "analytical families")
    families = family_document.get("families", {})
    if list(families) != EXPECTED_ANALYTICAL_FAMILIES:
        errors.append("analytical family contracts must match manifest order")
    for family, contract in families.items():
        for component in contract.get("candidate_components", []):
            if component in component_usage:
                component_usage[component].add(f"analytical:{family}")

    for component, usage in component_usage.items():
        if len(usage) < 2:
            errors.append(
                f"component candidate needs repeated semantic evidence: {component}"
            )

    analytical_entries = manifest.get("analytical_datasets", [])
    if [entry.get("family") for entry in analytical_entries] != EXPECTED_ANALYTICAL_FAMILIES:
        errors.append("analytical datasets must cover all six candidate families")
    for entry in analytical_entries:
        family = entry.get("family")
        dataset_path = root / str(entry.get("path", ""))
        dataset_document = _load(dataset_path, errors, f"analytical dataset {family}")
        if not dataset_document or family not in families:
            continue
        dataset = dataset_document.get("dataset", {})
        if dataset_document.get("language") != "CSDL" or dataset_document.get("version") != "0.2-candidate":
            errors.append(f"analytical dataset must use candidate v0.2: {family}")
        if dataset.get("status") != "synthetic_fixed_data":
            errors.append(f"analytical dataset must be synthetic fixed data: {family}")
        if not dataset.get("fields") or not dataset.get("records") or not dataset.get("provenance"):
            errors.append(f"analytical dataset is incomplete: {family}")
            continue
        expected_proof = derive_analytical_proof(
            str(family),
            families[str(family)],
            dataset_document,
            str(entry.get("path")),
        )
        actual_proof = _load(
            root / "analytics/proofs" / f"{entry.get('id')}.yaml",
            errors,
            f"analytical proof {family}",
        )
        if actual_proof and actual_proof != expected_proof:
            errors.append(f"analytical proof does not match deterministic dataset: {family}")

    generated = {
        "index": derive_index(root),
        "compatibility": derive_compatibility(root),
    }
    for name, expected in generated.items():
        actual = _load(root / "generated" / f"{name}.yaml", errors, f"generated {name}")
        if actual and actual != expected:
            errors.append(f"generated arsenal {name} does not match deterministic derivation")

    for document in ("README.md", "SPEC.md", "MIGRATION.md", "ROLLBACK.md", "evaluation/review.md"):
        if not (root / document).is_file():
            errors.append(f"missing arsenal canonical document: {document}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_arsenal_expansion.py ROOT")
        return 2
    errors = validate_arsenal_expansion(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("arsenal expansion valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
