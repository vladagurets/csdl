from pathlib import Path

import yaml

from tools.validate_analytical_mode import validate_analytical_library


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "analytics/analytical-mode-v0.1"


def test_incomplete_mode_accepts_contract_only_library() -> None:
    assert validate_analytical_library(LIBRARY, require_complete=False) == []


def test_manifest_declares_all_required_families_and_proof_slots() -> None:
    manifest = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    assert manifest["library"]["id"] == "analytical-mode-v0.1"
    assert manifest["library"]["version"] == "0.1.0"
    assert manifest["library"]["prompt_dsl_compatibility"] == "0.5"
    assert manifest["library"]["public_component_count"] == 15
    assert manifest["library"]["public_recipe_count"] == 23
    assert manifest["family_order"] == [
        "bar",
        "line",
        "scatterplot",
        "waterfall",
        "heatmap",
        "funnel",
        "map",
        "network",
        "table",
        "dashboard",
    ]
    assert len(manifest["proofs"]) == 10


def test_dataset_schema_covers_required_data_semantics() -> None:
    schema = yaml.safe_load((LIBRARY / "dataset-schema.yaml").read_text(encoding="utf-8"))
    assert schema["field_types"] == [
        "categorical",
        "ordinal",
        "temporal",
        "quantitative",
        "geographic",
        "identifier",
    ]
    assert schema["field_roles"] == ["dimension", "measure", "identifier"]
    assert schema["missing_statuses"] == [
        "missing",
        "null",
        "suppressed",
        "not_applicable",
        "unavailable",
    ]
    assert set(schema["required_dataset_fields"]) >= {
        "id",
        "version",
        "fields",
        "records",
        "ordering",
        "missing_values",
        "provenance",
    }


def test_encoding_schema_keeps_marks_internal_and_layout_free() -> None:
    schema = yaml.safe_load((LIBRARY / "encoding-schema.yaml").read_text(encoding="utf-8"))
    assert schema["mark_scope"] == "internal_data_encoding_only"
    assert set(schema["internal_marks"]) >= {
        "bar",
        "line",
        "point",
        "cell",
        "waterfall-step",
        "funnel-stage",
        "region",
        "network-node",
        "network-edge",
        "interval-band",
    }
    assert "layout" in schema["forbidden_keys"]
    assert "coordinates" in schema["forbidden_keys"]
    assert "row_order" not in schema["forbidden_keys"]
    assert "column_order" not in schema["forbidden_keys"]


def test_family_contracts_define_rules_and_hard_exclusions() -> None:
    contracts = yaml.safe_load(
        (LIBRARY / "contracts/families.yaml").read_text(encoding="utf-8")
    )
    assert list(contracts["families"]) == [
        "bar",
        "line",
        "scatterplot",
        "waterfall",
        "heatmap",
        "funnel",
        "map",
        "network",
        "table",
        "dashboard",
    ]
    for contract in contracts["families"].values():
        assert contract["precise_rules"]
        assert contract["hard_exclusions"]


def test_global_contract_records_quantitative_invariants() -> None:
    contracts = yaml.safe_load(
        (LIBRARY / "contracts/global.yaml").read_text(encoding="utf-8")
    )
    assert contracts["zero_baseline"]["bar_like"] == "required"
    assert contracts["log_scale"]["default"] == "forbidden"
    assert contracts["dual_axis"]["default"] == "forbidden"
    assert contracts["decorative_field"]["max_area_percent"] == 5
    assert contracts["direct_labels"]["precedence"] == "preferred"
    assert contracts["color"]["sole_carrier_allowed"] is False


def test_completion_docs_preserve_dependency_boundaries() -> None:
    assert "Analytical Mode v0.1 are complete" in (ROOT / "README.md").read_text(
        encoding="utf-8"
    )
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    milestone = roadmap.split("## Milestone 5 — Analytical Mode", 1)[1].split(
        "## Milestone 6", 1
    )[0]
    assert "**State:** complete" in milestone
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    assert "Milestone 5 is complete" in status
    assert "Milestone 6 is active" in status

    component_manifest = yaml.safe_load(
        (ROOT / "components/component-library-v0.1/manifest.yaml").read_text(
            encoding="utf-8"
        )
    )
    recipe_manifest = yaml.safe_load(
        (ROOT / "recipes/recipe-library-v0.5/manifest.yaml").read_text(encoding="utf-8")
    )
    prompt_schema = yaml.safe_load(
        (ROOT / "recipes/recipe-library-v0.5/prompt-dsl-v0.5.schema.yaml").read_text(
            encoding="utf-8"
        )
    )
    assert len(component_manifest["components"]) == 15
    assert len(recipe_manifest["recipes"]) == 23
    assert prompt_schema["version"] == "0.5"
