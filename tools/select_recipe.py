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


def select_recipe(outline: dict[str, Any], root: Path) -> dict[str, Any]:
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
