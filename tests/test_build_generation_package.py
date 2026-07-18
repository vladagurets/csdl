from pathlib import Path

import yaml

from tools.build_generation_package import build_generation_package
from tools.validate_prompt_dsl import validate_prompt_package


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def workflow_outline() -> dict:
    return {
        "id": "structural-workflow",
        "scenario": "work procedure",
        "main_idea": "Verification produces evidence.",
        "content": {
            "headline": "РОБОЧИЙ ПОТІК З ДОКАЗАМИ",
            "stages": ["UNDERSTAND", "PLAN", "EXECUTE", "VERIFY"],
        },
        "content_source": "inline",
    }


def test_builds_deterministic_strict_valid_package(tmp_path: Path) -> None:
    first = build_generation_package(workflow_outline(), LIBRARY)
    second = build_generation_package(workflow_outline(), LIBRARY)
    assert first == second

    path = tmp_path / "workflow.yaml"
    path.write_text(
        yaml.safe_dump(first, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    assert validate_prompt_package(path, LIBRARY) == []


def test_builder_uses_recipe_cardinality_defaults() -> None:
    package = build_generation_package(workflow_outline(), LIBRARY)
    components = [instance["component"] for instance in package["component_instances"]]

    assert components.count("Node") == 4
    assert components.count("Vector") == 3
    assert components.count("Label") == 4
    assert components.count("Signal") == 1
