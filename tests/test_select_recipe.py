from pathlib import Path

import pytest

from tools.select_recipe import select_recipe


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def test_selects_recipe_from_exact_evidence_backed_scenario() -> None:
    recipe = select_recipe(
        {
            "id": "workflow-proof",
            "scenario": "work procedure",
            "main_idea": "Evidence follows every action.",
            "content": {"headline": "FLOW", "stages": ["PLAN", "BUILD", "VERIFY"]},
        },
        LIBRARY,
    )

    assert recipe["id"] == "012"
    assert recipe["slug"] == "workflow"


def test_rejects_scenario_without_recipe_evidence() -> None:
    with pytest.raises(ValueError, match="no recipe matches scenario"):
        select_recipe(
            {
                "id": "unsupported",
                "scenario": "multiseries uncertainty fan",
                "main_idea": "Deferred analytical behavior.",
                "content": {"headline": "DEFERRED"},
            },
            LIBRARY,
        )


def test_rejects_outline_layout_terminology() -> None:
    with pytest.raises(ValueError, match="outline contains unknown fields: layout"):
        select_recipe(
            {
                "id": "layout-outline",
                "scenario": "count",
                "main_idea": "One value.",
                "content": {"value": "1"},
                "layout": {"columns": 12},
            },
            LIBRARY,
        )
