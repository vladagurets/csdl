from __future__ import annotations

import shutil
from pathlib import Path

import yaml
from PIL import Image

from tools.build_arsenal_expansion import build_arsenal_expansion
from tools.build_arsenal_review import validate_arsenal_candidates
from tools.validate_arsenal_expansion import validate_arsenal_expansion


ROOT = Path(__file__).parents[1]
EXPANSION = ROOT / "extensions/arsenal-expansion-v0.1"


EXPECTED_RECIPES = [
    "Causal Chain",
    "State Machine",
    "Dependency Map",
    "Claim / Evidence",
    "Spectrum",
    "Anatomy",
    "Layer Stack",
    "Roadmap",
]
EXPECTED_COMPONENTS = ["Threshold", "Trace", "Band"]
EXPECTED_RELATIONS = [
    "causes",
    "transitions_to",
    "depends_on",
    "supports",
    "crosses",
]
EXPECTED_ANALYTICAL_FAMILIES = [
    "histogram",
    "boxplot",
    "intervalplot",
    "bullet",
    "gantt",
    "sankey",
]


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _copy_expansion(tmp_path: Path) -> Path:
    target = tmp_path / "extensions/arsenal-expansion-v0.1"
    shutil.copytree(EXPANSION, target)
    for source, destination in (
        (
            ROOT / "components/component-library-v0.1/manifest.yaml",
            tmp_path / "components/component-library-v0.1/manifest.yaml",
        ),
        (
            ROOT / "recipes/recipe-library-v0.5/manifest.yaml",
            tmp_path / "recipes/recipe-library-v0.5/manifest.yaml",
        ),
        (
            ROOT / "analytics/analytical-mode-v0.1/manifest.yaml",
            tmp_path / "analytics/analytical-mode-v0.1/manifest.yaml",
        ),
        (
            ROOT / "accessibility/night-mode-v0.1/evaluation/raster-hashes.yaml",
            tmp_path / "accessibility/night-mode-v0.1/evaluation/raster-hashes.yaml",
        ),
    ):
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return target


def test_expansion_contract_is_complete_and_valid() -> None:
    assert validate_arsenal_expansion(EXPANSION) == []

    manifest = _load(EXPANSION / "manifest.yaml")
    assert manifest["baseline"] == {
        "component_library": "components/component-library-v0.1/manifest.yaml",
        "component_count": 15,
        "recipe_library": "recipes/recipe-library-v0.5/manifest.yaml",
        "recipe_count": 23,
        "analytical_mode": "analytics/analytical-mode-v0.1/manifest.yaml",
        "analytical_family_count": 10,
    }
    assert manifest["targets"] == {
        "component_library": "component-library-v0.2",
        "component_count": 18,
        "recipe_library": "recipe-library-v0.6",
        "recipe_count": 31,
        "analytical_mode": "analytical-mode-v0.2",
        "analytical_family_count": 16,
    }
    assert [entry["name"] for entry in manifest["components"]] == EXPECTED_COMPONENTS
    assert [entry["name"] for entry in manifest["recipes"]] == EXPECTED_RECIPES
    assert manifest["relations"] == EXPECTED_RELATIONS
    assert manifest["analytical_families"] == EXPECTED_ANALYTICAL_FAMILIES


def test_expression_modes_extend_but_do_not_replace_abc() -> None:
    modes = _load(EXPANSION / "expressions/modes.yaml")
    assert modes["expression_levels"] == ["A", "B", "C"]
    assert list(modes["modes"]) == ["editorial", "structural", "analytical"]
    assert modes["rendering_profiles_preserved"] == [
        "light",
        "night",
        "monochrome",
        "projector",
    ]
    assert modes["candidate_rendering_profiles"] == ["high_contrast", "print"]


def test_every_new_component_has_repeated_semantic_evidence() -> None:
    manifest = _load(EXPANSION / "manifest.yaml")
    usage = {name: set() for name in EXPECTED_COMPONENTS}
    for entry in manifest["recipes"]:
        recipe = _load(EXPANSION / entry["record"])
        ingredients = recipe["ingredients"]["required"] + recipe["ingredients"]["optional"]
        for ingredient in ingredients:
            if ingredient["component"] in usage:
                usage[ingredient["component"]].add(recipe["name"])
    analytical = _load(EXPANSION / "analytics/families.yaml")
    for family, contract in analytical["families"].items():
        for component in contract["candidate_components"]:
            if component in usage:
                usage[component].add(f"analytical:{family}")
    assert all(len(evidence) >= 2 for evidence in usage.values()), usage


def test_all_recipe_candidates_define_a_distinct_problem_and_prompt() -> None:
    manifest = _load(EXPANSION / "manifest.yaml")
    distinctions = set()
    for entry in manifest["recipes"]:
        recipe = _load(EXPANSION / entry["record"])
        assert recipe["status"] == "candidate"
        assert recipe["distinguishes_from"]
        assert recipe["problem"]
        assert len(recipe["allowed_scenarios"]) >= 2
        assert (EXPANSION / recipe["prompt"]).is_file()
        distinctions.add((recipe["name"], recipe["distinguishes_from"]))
    assert len(distinctions) == 8


def test_all_six_analytical_proofs_rebuild_deterministically(tmp_path: Path) -> None:
    target = _copy_expansion(tmp_path)

    first = build_arsenal_expansion(target)
    first_bytes = {path.relative_to(target): path.read_bytes() for path in first}
    second = build_arsenal_expansion(target)
    second_bytes = {path.relative_to(target): path.read_bytes() for path in second}

    assert first_bytes == second_bytes
    index = _load(target / "generated/index.yaml")
    assert index["recipe_candidate_count"] == 8
    assert index["component_candidate_count"] == 3
    assert index["analytical_family_candidate_count"] == 6
    assert len(list((target / "analytics/proofs").glob("*.yaml"))) == 6
    assert validate_arsenal_expansion(target) == []


def test_all_recipe_raster_candidates_are_unique_pngs() -> None:
    assert validate_arsenal_candidates(EXPANSION) == []
    inventory = _load(EXPANSION / "selection/candidate-hashes.yaml")
    assert inventory["status"] == "selected_unpromoted"
    assert inventory["file_count"] == 24
    assert inventory["unique_sha256_count"] == 24


def test_selected_recipe_candidates_are_complete_and_identical_to_sources() -> None:
    assert validate_arsenal_candidates(EXPANSION, require_selection=True) == []
    inventory = _load(EXPANSION / "selection/candidate-hashes.yaml")
    assert inventory["status"] == "selected_unpromoted"
    assert len(inventory["selected"]) == 8
    assert {entry["variant"] for entry in inventory["selected"]} == {"v1"}
    for entry in inventory["selected"]:
        source = EXPANSION / entry["source"]
        selected = EXPANSION / entry["selected_path"]
        assert source.read_bytes() == selected.read_bytes()


def test_candidate_validator_rejects_non_png_container(tmp_path: Path) -> None:
    target = _copy_expansion(tmp_path)
    candidate = target / "drafts/light/16x9/024-causal-chain-redesign/v1.png"
    with Image.open(candidate) as source:
        source.convert("RGB").save(candidate, format="JPEG")

    assert "arsenal candidate must be PNG: v1.png" in validate_arsenal_candidates(target)


def test_validator_rejects_semantic_alias_and_dataset_mutation(tmp_path: Path) -> None:
    target = _copy_expansion(tmp_path)

    component = _load(target / "components/threshold.yaml")
    component["name"] = "Gate"
    (target / "components/threshold.yaml").write_text(
        yaml.safe_dump(component, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    dataset = _load(target / "analytics/datasets/04-bullet.yaml")
    dataset["dataset"]["records"][0]["actual"] = 999
    (target / "analytics/datasets/04-bullet.yaml").write_text(
        yaml.safe_dump(dataset, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    errors = validate_arsenal_expansion(target)
    assert "component record name must match manifest: Threshold" in errors
    assert "analytical proof does not match deterministic dataset: bullet" in errors
