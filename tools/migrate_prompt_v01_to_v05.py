from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_generation_package import build_generation_package


def _recipe_records(root: Path) -> dict[str, dict[str, Any]]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    return {
        entry["id"]: yaml.safe_load(
            (root / entry["record"]).read_text(encoding="utf-8")
        )
        for entry in manifest["recipes"]
    }


def _normalize_bindings(slug: str, legacy: dict[str, Any]) -> dict[str, Any]:
    source = copy.deepcopy(legacy.get("copy", legacy.get("content", {})))
    if not isinstance(source, dict):
        raise ValueError("legacy prompt copy/content must be a mapping")
    if slug == "hero" and "supporting" in source:
        source["supporting_copy"] = source.pop("supporting")
    elif slug == "comparison" and "left_title" in source:
        normalized = {
            "headline": source["headline"],
            "supporting_copy": source["supporting"],
            "left": [source["left_title"], *source["left_points"]],
            "right": [source["right_title"], *source["right_points"]],
        }
        source = normalized
    elif slug == "framework" and "supporting" in source and "pillars" not in source:
        source["pillars"] = [source.pop("supporting")]
    elif slug == "loop" and "supporting" in source:
        source["supporting_copy"] = source.pop("supporting")
    elif slug == "table" and "header" in source:
        source["columns"] = source.pop("header")
    elif slug == "chart" and "series" not in source:
        source["series"] = "success_rate"
    return source


def migrate_prompt(source_path: Path, root: Path) -> dict[str, Any]:
    repository_root = root.parents[1]
    relative = source_path.resolve().relative_to(repository_root.resolve()).as_posix()
    migration = yaml.safe_load(
        (root / "migration-v0.1-to-v0.5.yaml").read_text(encoding="utf-8")
    )["migration"]
    recipe_id = migration["recipe_map"].get(relative)
    if recipe_id is None:
        raise ValueError(f"legacy prompt is not declared by migration map: {relative}")
    legacy = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    if str(legacy.get("version")) != "0.1":
        raise ValueError("legacy prompt version must equal 0.1")
    recipe = _recipe_records(root)[recipe_id]
    bindings = _normalize_bindings(recipe["slug"], legacy)
    main_idea = next(
        (
            bindings[key]
            for key in ("headline", "formula", "quote", "primary")
            if key in bindings
        ),
        recipe["name"],
    )
    outline = {
        "id": f"migration-{recipe['slug']}",
        "recipe": recipe["id"],
        "scenario": recipe["allowed_scenarios"][0],
        "main_idea": main_idea,
        "content": bindings,
        "content_source": relative,
        "source_outline": relative,
        "expression": legacy.get(
            "level",
            legacy.get(
                "expression", recipe["prompt_dsl"]["deterministic_defaults"]["expression"]
            ),
        ),
        "density": legacy.get(
            "density", recipe["prompt_dsl"]["deterministic_defaults"]["density"]
        ),
    }
    package = build_generation_package(outline, root)
    package["provenance"]["source_prompt"] = relative
    if legacy.get("dataset"):
        package["provenance"]["dataset"] = legacy["dataset"]
    package["provenance"]["migration"] = {
        "id": migration["id"],
        "source_version": "0.1",
        "target_version": "0.5",
        "normalized_fields": [
            "recipe",
            "copy_or_content",
            "component_instances",
            "relations",
            "generation_constraints",
        ],
        "discarded_legacy_fields": [
            field
            for field in ("reference", "composition", "components", "palette", "constraints")
            if field in legacy
        ],
    }
    return package


def main() -> int:
    if len(sys.argv) != 4:
        print(
            "usage: python tools/migrate_prompt_v01_to_v05.py "
            "SOURCE RECIPE_LIBRARY_ROOT OUTPUT"
        )
        return 2
    try:
        package = migrate_prompt(Path(sys.argv[1]), Path(sys.argv[2]))
        Path(sys.argv[3]).write_text(
            yaml.safe_dump(package, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
    except (KeyError, OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print(f"Prompt DSL migrated: {sys.argv[3]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
