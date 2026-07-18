from pathlib import Path
from collections import Counter

import yaml

from tools.migrate_prompt_v01_to_v05 import migrate_prompt
from tools.validate_prompt_dsl import validate_prompt_package


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"
SOURCE = ROOT / "pilots/01-agentic-discipline/prompts/04-comparison.yaml"


def scalar_leaves(value):
    if isinstance(value, dict):
        return [leaf for child in value.values() for leaf in scalar_leaves(child)]
    if isinstance(value, list):
        return [leaf for child in value for leaf in scalar_leaves(child)]
    return [value]


def test_migrates_pilot_comparison_without_copy_changes(tmp_path: Path) -> None:
    source = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    package = migrate_prompt(SOURCE, LIBRARY)
    path = tmp_path / "comparison-v05.yaml"
    path.write_text(
        yaml.safe_dump(package, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )

    assert package["recipe"] == {"id": "005", "slug": "comparison", "version": "0.5.0"}
    assert scalar_leaves(package["content"]["bindings"]) == scalar_leaves(source["copy"])
    assert package["provenance"]["migration"]["source_version"] == "0.1"
    assert validate_prompt_package(path, LIBRARY) == []


def test_migration_map_covers_all_recipe_prompt_sources() -> None:
    migration = yaml.safe_load(
        (LIBRARY / "migration-v0.1-to-v0.5.yaml").read_text(encoding="utf-8")
    )["migration"]

    assert len(migration["source_files"]) == 27
    assert set(migration["source_files"]) == set(migration["recipe_map"])
    assert migration["reference_only"] == [
        "pilots/01-agentic-discipline/prompts/00-style-anchor.yaml"
    ]


def test_all_declared_legacy_recipe_prompts_migrate_to_valid_v05(tmp_path: Path) -> None:
    migration = yaml.safe_load(
        (LIBRARY / "migration-v0.1-to-v0.5.yaml").read_text(encoding="utf-8")
    )["migration"]

    for index, relative in enumerate(migration["source_files"], start=1):
        source_path = ROOT / relative
        source = yaml.safe_load(source_path.read_text(encoding="utf-8"))
        package = migrate_prompt(source_path, LIBRARY)
        path = tmp_path / f"{index:02d}.yaml"
        path.write_text(
            yaml.safe_dump(package, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        assert validate_prompt_package(path, LIBRARY) == [], relative
        source_content = source.get("copy", source.get("content", {}))
        source_leaves = Counter(map(str, scalar_leaves(source_content)))
        migrated_leaves = Counter(
            map(str, scalar_leaves(package["content"]["bindings"]))
        )
        assert source_leaves <= migrated_leaves, relative
