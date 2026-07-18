from pathlib import Path
import shutil

import yaml

from tools.validate_recipe_library import validate_recipe_library


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def copy_library(tmp_path: Path) -> Path:
    target = tmp_path / "recipes/recipe-library-v0.5"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    component_target = tmp_path / "components/component-library-v0.1"
    component_target.mkdir(parents=True)
    shutil.copy2(
        ROOT / "components/component-library-v0.1/manifest.yaml",
        component_target / "manifest.yaml",
    )
    return target


def test_infrastructure_validates_in_incomplete_mode() -> None:
    assert validate_recipe_library(LIBRARY / "manifest.yaml", require_complete=False) == []


def test_strict_mode_rejects_incomplete_recipe_set(tmp_path: Path) -> None:
    root = copy_library(tmp_path)
    path = root / "manifest.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["recipes"].pop()
    path.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )

    errors = validate_recipe_library(path)
    assert "recipes must contain exactly 23 entries" in errors


def test_complete_recipe_set_is_evidence_bounded_and_strict_valid() -> None:
    data = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    entries = data["recipes"]

    assert [entry["id"] for entry in entries] == [f"{index:03d}" for index in range(1, 24)]
    assert [entry["source_family"] for entry in entries[:20]] == [
        "hero",
        "cover",
        "quote",
        "big-number",
        "comparison",
        "collision",
        "before-after",
        "timeline",
        "matrix",
        "hierarchy",
        "architecture",
        "workflow",
        "loop",
        "pipeline",
        "decision-tree",
        "framework",
        "kpi",
        "table",
        "chart",
        "dashboard",
    ]
    assert [entry["slug"] for entry in entries[20:]] == [
        "breakdown",
        "checklist",
        "formula",
    ]
    assert validate_recipe_library(LIBRARY / "manifest.yaml") == []


def test_rejects_unknown_library_field(tmp_path: Path) -> None:
    root = copy_library(tmp_path)
    path = root / "manifest.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["library"]["layout"] = "grid"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    assert "library contains unknown fields: layout" in validate_recipe_library(
        path, require_complete=False
    )


def test_rejects_undeclared_public_component(tmp_path: Path) -> None:
    root = copy_library(tmp_path)
    path = root / "schema.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["public_components"].append("Container")
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    errors = validate_recipe_library(root / "manifest.yaml", require_complete=False)
    assert "schema public_components must match Component Library v0.1" in errors


def test_rejects_component_incompatible_with_recipe_family(tmp_path: Path) -> None:
    root = copy_library(tmp_path)
    path = root / "records/001-hero.yaml"
    recipe = yaml.safe_load(path.read_text(encoding="utf-8"))
    recipe["ingredients"]["optional"].append(
        {"component": "Vector", "min": 0, "max": 1}
    )
    path.write_text(
        yaml.safe_dump(recipe, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )

    errors = validate_recipe_library(root / "manifest.yaml", require_complete=False)
    assert "recipe 001 ingredient Vector is incompatible with a declared Visual DNA family" in errors


def test_rejects_relation_not_allowed_by_component_contracts(tmp_path: Path) -> None:
    root = copy_library(tmp_path)
    path = root / "records/001-hero.yaml"
    recipe = yaml.safe_load(path.read_text(encoding="utf-8"))
    recipe["relations"]["allowed"][0]["type"] = "groups"
    path.write_text(
        yaml.safe_dump(recipe, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )

    errors = validate_recipe_library(root / "manifest.yaml", require_complete=False)
    assert "recipe 001 allowed relation 1 is not allowed by component contracts" in errors
