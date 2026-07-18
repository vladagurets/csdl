from pathlib import Path
import shutil

import yaml

from tools.validate_prompt_dsl import validate_prompt_package


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


def test_incomplete_mode_accepts_empty_proof_directory() -> None:
    assert validate_prompt_package(None, LIBRARY, require_complete=False) == []


def test_schema_separates_five_required_concerns() -> None:
    schema = yaml.safe_load(
        (LIBRARY / "prompt-dsl-v0.5.schema.yaml").read_text(encoding="utf-8")
    )
    assert schema["required_package_fields"] == [
        "language",
        "version",
        "kind",
        "id",
        "recipe",
        "semantic_intent",
        "content",
        "component_instances",
        "relations",
        "generation_constraints",
        "provenance",
    ]


def test_rejects_ad_hoc_layout_key(tmp_path: Path) -> None:
    root = copy_library(tmp_path)
    package = {
        "language": "CSDL",
        "version": "0.5",
        "kind": "generation-package",
        "id": "fixture",
        "recipe": {"id": "001", "slug": "hero", "version": "0.5.0"},
        "semantic_intent": {
            "problem": "State one idea.",
            "scenario": "opening thesis",
            "main_idea": "ONE IDEA",
            "mechanism": "anchor-signal",
        },
        "content": {"source": "inline", "bindings": {"headline": "ONE IDEA"}},
        "component_instances": [],
        "relations": [],
        "generation_constraints": {"layout": {"columns": 12}},
        "provenance": {"recipe_evidence": "README.md", "source_outline": "inline"},
    }
    path = root / "fixture.yaml"
    path.write_text(yaml.safe_dump(package, sort_keys=False), encoding="utf-8")

    errors = validate_prompt_package(path, root, require_complete=False)
    assert "package contains forbidden composition key: layout" in errors
