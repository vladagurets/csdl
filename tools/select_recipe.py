from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _records(root: Path) -> list[dict[str, Any]]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    return [
        yaml.safe_load((root / entry["record"]).read_text(encoding="utf-8"))
        for entry in manifest["recipes"]
    ]


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


def validate_outline(outline: dict[str, Any], root: Path) -> list[str]:
    schema = yaml.safe_load((root / "outline-schema.yaml").read_text(encoding="utf-8"))
    errors: list[str] = []
    missing = sorted(set(schema["required_fields"]) - set(outline))
    unknown = sorted(set(outline) - set(schema["allowed_fields"]))
    if missing:
        errors.append("outline missing fields: " + ",".join(missing))
    if unknown:
        errors.append("outline contains unknown fields: " + ",".join(unknown))
    composition_surface = {key: value for key, value in outline.items() if key != "content"}
    forbidden = {key.lower() for key in schema["forbidden_composition_keys"]}
    for key in sorted(_find_forbidden_keys(composition_surface, forbidden)):
        errors.append(f"outline contains forbidden composition key: {key}")
    if outline.get("expression", "A") not in schema["enums"]["expression"]:
        errors.append("outline expression is invalid")
    if outline.get("density", "low") not in schema["enums"]["density"]:
        errors.append("outline density is invalid")
    if "content" in outline and (
        not isinstance(outline["content"], dict) or not outline["content"]
    ):
        errors.append("outline content must be a non-empty mapping")
    return errors


def select_recipe(outline: dict[str, Any], root: Path) -> dict[str, Any]:
    outline_errors = validate_outline(outline, root)
    if outline_errors:
        raise ValueError(outline_errors[0])
    records = _records(root)
    requested = outline.get("recipe")
    if requested:
        matches = [
            recipe
            for recipe in records
            if requested in {recipe["id"], recipe["slug"], recipe["name"]}
        ]
    else:
        scenario = outline.get("scenario")
        if not isinstance(scenario, str) or not scenario.strip():
            raise ValueError("outline must define a non-empty scenario")
        normalized = scenario.strip().casefold()
        matches = [
            recipe
            for recipe in records
            if normalized
            in {candidate.strip().casefold() for candidate in recipe["allowed_scenarios"]}
        ]
    if not matches:
        raise ValueError(f"no recipe matches scenario: {outline.get('scenario')}")
    if len(matches) != 1:
        raise ValueError(f"scenario is ambiguous across recipes: {outline.get('scenario')}")
    return matches[0]


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python tools/select_recipe.py OUTLINE RECIPE_LIBRARY_ROOT")
        return 2
    try:
        outline = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
        recipe = select_recipe(outline, Path(sys.argv[2]))
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print(f"{recipe['id']} {recipe['slug']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
