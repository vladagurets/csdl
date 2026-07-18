from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _load_inputs(root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    schema = yaml.safe_load((root / "schema.yaml").read_text(encoding="utf-8"))
    return manifest, schema


def _load_records(root: Path, manifest: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for entry in manifest.get("recipes", []):
        if not isinstance(entry, dict) or not entry.get("record"):
            continue
        records.append(
            yaml.safe_load((root / str(entry["record"])).read_text(encoding="utf-8"))
        )
    return records


def derive_index(manifest: dict[str, Any], records: list[dict[str, Any]]) -> dict[str, Any]:
    library = manifest["library"]
    recipes = []
    for recipe in records:
        recipes.append(
            {
                "id": recipe["id"],
                "slug": recipe["slug"],
                "name": recipe["name"],
                "version": recipe["version"],
                "source_family": recipe["source_family"],
                "allowed_scenarios": recipe["allowed_scenarios"],
                "required_components": [
                    ingredient["component"]
                    for ingredient in recipe["ingredients"]["required"]
                ],
                "optional_components": [
                    ingredient["component"]
                    for ingredient in recipe["ingredients"]["optional"]
                ],
                "allowed_levels": [
                    level
                    for level, contract in recipe["expression_levels"].items()
                    if contract["status"] != "forbidden"
                ],
                "compatible_visual_dna_families": recipe[
                    "compatible_visual_dna_families"
                ],
                "specification": recipe["specification"],
                "record": recipe["record"],
            }
        )
    return {
        "library": library["id"],
        "version": library["version"],
        "recipe_count": len(recipes),
        "recipes": recipes,
    }


def derive_compatibility(
    manifest: dict[str, Any], schema: dict[str, Any], records: list[dict[str, Any]]
) -> dict[str, Any]:
    library = manifest["library"]
    families = schema["family_order"]
    recipe_rows = []
    by_family: dict[str, list[dict[str, str]]] = {family: [] for family in families}
    for recipe in records:
        compatible = set(recipe["compatible_visual_dna_families"])
        states = {
            family: "direct" if family in compatible else "incompatible"
            for family in families
        }
        recipe_rows.append(
            {"id": recipe["id"], "slug": recipe["slug"], "families": states}
        )
        for family in families:
            if family in compatible:
                by_family[family].append({"recipe": recipe["slug"], "status": "direct"})
    return {
        "library": library["id"],
        "version": library["version"],
        "families": families,
        "recipes": recipe_rows,
        "by_family": [
            {"family": family, "recipes": by_family[family]} for family in families
        ],
    }


def derive_selection_index(
    manifest: dict[str, Any], records: list[dict[str, Any]]
) -> dict[str, Any]:
    library = manifest["library"]
    scenarios = []
    for recipe in records:
        for scenario in recipe["allowed_scenarios"]:
            scenarios.append(
                {
                    "scenario": scenario,
                    "recipe_id": recipe["id"],
                    "recipe_slug": recipe["slug"],
                }
            )
    return {
        "library": library["id"],
        "version": library["version"],
        "scenarios": scenarios,
    }


def build_recipe_library(
    root: Path, require_complete: bool = True
) -> tuple[Path, Path, Path]:
    manifest, schema = _load_inputs(root)
    records = _load_records(root, manifest)
    expected_count = manifest.get("library", {}).get("recipe_count")
    if require_complete and len(records) != expected_count:
        raise ValueError("recipe library is incomplete")

    outputs = (
        (root / manifest["library"]["index"], derive_index(manifest, records)),
        (
            root / manifest["library"]["compatibility"],
            derive_compatibility(manifest, schema, records),
        ),
        (
            root / manifest["library"]["selection_index"],
            derive_selection_index(manifest, records),
        ),
    )
    for path, data in outputs:
        path.write_text(
            yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )
    return outputs[0][0], outputs[1][0], outputs[2][0]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/build_recipe_library.py RECIPE_LIBRARY_ROOT")
        return 2
    root = Path(sys.argv[1])
    try:
        paths = build_recipe_library(root)
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print("recipe library built: " + ", ".join(path.name for path in paths))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
