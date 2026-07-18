from pathlib import Path

import yaml

from tools.build_generation_package import build_generation_package
from tools.migrate_prompt_v01_to_v05 import migrate_prompt
from tools.select_recipe import select_recipe
from tools.validate_prompt_dsl import validate_prompt_package


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def test_outline_selection_and_packages_are_deterministic_and_strict_valid() -> None:
    outline_paths = sorted((LIBRARY / "proofs/outlines").glob("*.yaml"))
    package_paths = sorted((LIBRARY / "proofs/packages").glob("*.yaml"))

    assert len(outline_paths) == len(package_paths) == 3
    for outline_path, package_path in zip(outline_paths, package_paths, strict=True):
        outline = yaml.safe_load(outline_path.read_text(encoding="utf-8"))
        package = yaml.safe_load(package_path.read_text(encoding="utf-8"))
        selected = select_recipe(outline, LIBRARY)

        assert package["recipe"]["id"] == selected["id"]
        assert package == build_generation_package(outline, LIBRARY)
        assert validate_prompt_package(package_path, LIBRARY) == []


def test_bounded_analytical_proof_preserves_fixed_dataset_contract() -> None:
    package = yaml.safe_load(
        (LIBRARY / "proofs/packages/03-analytical.yaml").read_text(encoding="utf-8")
    )
    contract = package["content"]["bindings"]["quantitative_contract"]
    dataset = yaml.safe_load(
        (ROOT / "patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml").read_text(
            encoding="utf-8"
        )
    )

    assert contract["domain"] == dataset["constraints"]["percent_domain"]
    assert contract["order"] == dataset["dataset"]["weeks"]
    assert contract["values"] == dataset["dataset"]["series"]["success_rate"]["values"]
    assert contract["unit"] == dataset["dataset"]["series"]["success_rate"]["unit"]
    assert contract["source"] == dataset["constraints"]["source_label_required"]


def test_persisted_migration_proof_matches_mechanical_rebuild() -> None:
    path = LIBRARY / "proofs/migration/01-pilot-comparison.yaml"
    package = yaml.safe_load(path.read_text(encoding="utf-8"))
    rebuilt = migrate_prompt(
        ROOT / "pilots/01-agentic-discipline/prompts/04-comparison.yaml", LIBRARY
    )

    assert package == rebuilt
    assert validate_prompt_package(path, LIBRARY) == []
