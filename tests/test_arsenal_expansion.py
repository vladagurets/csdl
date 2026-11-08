from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

import yaml
from PIL import Image

from tools.build_arsenal_expansion import build_arsenal_expansion
from tools.build_arsenal_review import (
    build_arsenal_review,
    build_hash_inventory,
    validate_arsenal_candidates,
    validate_arsenal_selection,
)
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
    shutil.copytree(EXPANSION, target, ignore=shutil.ignore_patterns("drafts"))
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


def test_all_recipe_raster_candidates_have_unique_persisted_hashes() -> None:
    inventory = _load(EXPANSION / "selection/candidate-hashes.yaml")
    assert inventory["status"] == "selected_unpromoted"
    assert inventory["file_count"] == 24
    assert inventory["unique_sha256_count"] == 24
    assert len(inventory["files"]) == 24
    assert len({entry["sha256"] for entry in inventory["files"]}) == 24


def test_selected_recipe_candidates_match_persisted_source_hashes() -> None:
    assert validate_arsenal_selection(EXPANSION) == []
    inventory = _load(EXPANSION / "selection/candidate-hashes.yaml")
    assert inventory["status"] == "selected_unpromoted"
    assert len(inventory["selected"]) == 8
    assert {entry["variant"] for entry in inventory["selected"]} == {"v1"}
    for entry in inventory["selected"]:
        selected = EXPANSION / entry["selected_path"]
        assert hashlib.sha256(selected.read_bytes()).hexdigest() == entry["source_sha256"]


def _candidate_fixture(tmp_path: Path) -> Path:
    target = _copy_expansion(tmp_path)
    manifest = _load(target / "manifest.yaml")
    for index, recipe in enumerate(manifest["recipes"]):
        record = _load(target / recipe["record"])
        directory = target / f"drafts/light/16x9/{record['id']}-{record['slug']}-redesign"
        directory.mkdir(parents=True)
        for variant in range(1, 4):
            image = Image.new("RGB", (1920, 1080), (index, variant, 0))
            source = directory / f"v{variant}.png"
            image.save(source)
            if variant == 1:
                selected = target / f"selection/selected/{record['id']}-{record['slug']}.png"
                shutil.copy2(source, selected)
    build_hash_inventory(target, manifest, target / "selection/candidate-hashes.yaml")
    return target


def test_candidate_validator_rejects_non_png_container(tmp_path: Path) -> None:
    target = _candidate_fixture(tmp_path)
    candidate = target / "drafts/light/16x9/024-causal-chain-redesign/v1.png"
    with Image.open(candidate) as source:
        source.convert("RGB").save(candidate, format="JPEG")

    assert "arsenal candidate must be PNG: v1.png" in validate_arsenal_candidates(target)


def test_full_candidate_validation_checks_local_drafts(tmp_path: Path) -> None:
    target = _candidate_fixture(tmp_path)
    assert validate_arsenal_candidates(target, require_selection=True) == []
    candidate = target / "drafts/light/16x9/024-causal-chain-redesign/v1.png"
    Image.new("RGB", (1920, 1080), "white").save(candidate)
    errors = validate_arsenal_candidates(target, require_selection=True)
    assert any("does not match recorded hash" in error for error in errors)


def test_selection_validation_works_without_drafts_and_rejects_changed_raster(tmp_path: Path) -> None:
    target = _copy_expansion(tmp_path)
    assert not (target / "drafts").exists()
    assert validate_arsenal_selection(target) == []
    selected = target / "selection/selected/024-causal-chain.png"
    Image.new("RGB", (1920, 1080), "white").save(selected)
    assert "selected arsenal candidate must equal source: 024" in validate_arsenal_selection(target)


def test_selection_validation_rejects_changed_inventory_binding(tmp_path: Path) -> None:
    target = _copy_expansion(tmp_path)
    path = target / "selection/candidate-hashes.yaml"
    inventory = _load(path)
    inventory["selected"][0]["source"] = inventory["files"][1]["path"]
    path.write_text(yaml.safe_dump(inventory), encoding="utf-8")
    assert "arsenal selected inventory does not match choice: 024" in validate_arsenal_selection(target)


def test_selection_validation_rejects_unreadable_selected_raster(tmp_path: Path) -> None:
    target = _copy_expansion(tmp_path)
    selected = target / "selection/selected/024-causal-chain.png"
    selected.write_bytes(b"invalid PNG")
    errors = validate_arsenal_selection(target)
    assert any("must be readable PNG" in error for error in errors)


def test_review_builder_writes_only_one_board_set(tmp_path: Path) -> None:
    target = _candidate_fixture(tmp_path)
    selection = target / "selection"
    for path in selection.glob("*.png"):
        path.unlink()
    for path in (selection / "recalibration").glob("*.png"):
        path.unlink()
    outputs = build_arsenal_review(target)
    assert len(list((selection / "recalibration").glob("[0-9]*.png"))) == 8
    assert list(selection.glob("*.png")) == [selection / "overview.png"]
    assert not (selection / "recalibration/overview.png").exists()
    assert all(path.is_file() for path in outputs)
    assert validate_arsenal_candidates(target, require_selection=True) == []


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
