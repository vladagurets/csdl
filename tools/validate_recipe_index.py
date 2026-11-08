from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_recipe_library import (
    _load_records,
    derive_compatibility,
    derive_index,
    derive_selection_index,
)
from tools.validate_prompt_dsl import validate_prompt_library
from tools.validate_recipe_library import validate_recipe_library
from tools.validation_common import load_yaml_mapping as _load_yaml


def validate_recipe_index(root: Path, require_complete: bool = True) -> list[str]:
    errors = validate_recipe_library(
        root / "manifest.yaml", require_complete=require_complete
    )
    errors.extend(validate_prompt_library(root, require_complete=require_complete))
    if errors:
        return errors
    manifest = _load_yaml(root / "manifest.yaml", errors, "recipe manifest")
    schema = _load_yaml(root / "schema.yaml", errors, "recipe schema")
    records = _load_records(root, manifest)
    library = manifest.get("library", {})
    index = _load_yaml(root / str(library.get("index", "index.yaml")), errors, "recipe index")
    compatibility = _load_yaml(
        root / str(library.get("compatibility", "compatibility.yaml")),
        errors,
        "recipe compatibility",
    )
    selection = _load_yaml(
        root / str(library.get("selection_index", "selection-index.yaml")),
        errors,
        "recipe selection index",
    )
    if errors:
        return errors
    if index != derive_index(manifest, records):
        errors.append("index does not match the manifest-derived output")
    if compatibility != derive_compatibility(manifest, schema, records):
        errors.append("compatibility does not match the manifest-derived output")
    if selection != derive_selection_index(manifest, records):
        errors.append("selection index does not match the manifest-derived output")
    if require_complete:
        for row in compatibility.get("by_family", []):
            if not row.get("recipes"):
                errors.append(f"Visual DNA family has no compatible recipe: {row.get('family')}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_recipe_index.py RECIPE_LIBRARY_ROOT")
        return 2
    errors = validate_recipe_index(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("recipe index valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
