from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_component_library import derive_compatibility, derive_index
from tools.validate_component_library import validate_component_library
from tools.validate_component_proofs import validate_component_proofs


def _load_yaml(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} must be readable YAML: {error}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return data


def validate_component_index(root: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    manifest_path = root / "manifest.yaml"
    manifest = _load_yaml(manifest_path, errors, "component manifest")
    schema = _load_yaml(root / "schema.yaml", errors, "component schema")
    if errors:
        return errors

    errors.extend(validate_component_library(manifest_path, require_complete=require_complete))
    errors.extend(validate_component_proofs(root, require_complete=require_complete))

    library = manifest.get("library", {})
    index = _load_yaml(root / str(library.get("index", "index.yaml")), errors, "component index")
    compatibility = _load_yaml(
        root / str(library.get("compatibility", "compatibility.yaml")),
        errors,
        "component compatibility matrix",
    )
    if errors:
        return errors

    if index != derive_index(manifest):
        errors.append("index does not match the manifest-derived output")
    if compatibility != derive_compatibility(manifest, schema):
        errors.append("compatibility matrix does not match the manifest-derived output")

    if require_complete:
        family_rows = compatibility.get("by_family", [])
        for row in family_rows:
            if not row.get("components"):
                errors.append(f"compatibility family has no declared components: {row.get('family')}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_component_index.py COMPONENT_LIBRARY_ROOT")
        return 2
    errors = validate_component_index(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("component index valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
