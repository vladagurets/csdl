from pathlib import Path

import yaml

from tools.validate_accessibility_mode import (
    contrast_ratio,
    validate_accessibility_library,
)


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "accessibility/night-mode-v0.1"


def load(relative: str) -> dict:
    return yaml.safe_load((LIBRARY / relative).read_text(encoding="utf-8"))


def test_incomplete_mode_accepts_contract_only_library() -> None:
    assert validate_accessibility_library(LIBRARY, require_complete=False) == []


def test_manifest_locks_version_profiles_and_dependency_counts() -> None:
    manifest = load("manifest.yaml")
    library = manifest["library"]
    assert library["id"] == "night-mode-v0.1"
    assert library["version"] == "0.1.0"
    assert library["kind"] == "accessibility-extension"
    assert library["prompt_dsl_compatibility"] == "0.5"
    assert library["public_component_count"] == 15
    assert library["public_recipe_count"] == 23
    assert manifest["profile_order"] == [
        "light",
        "night",
        "monochrome",
        "projector",
    ]
    assert len(manifest["proofs"]) == 10


def test_token_schema_covers_required_semantic_roles() -> None:
    schema = load("token-schema.yaml")
    assert schema["profiles"] == ["light", "night", "monochrome", "projector"]
    assert set(schema["required_token_roles"]) >= {
        "background.base",
        "surface.raised",
        "ink.primary",
        "ink.secondary",
        "neutral.fill",
        "line.subtle",
        "line.strong",
        "signal.primary",
        "signal.data",
        "signal.attention",
        "signal.positive",
        "signal.error",
        "state.focus",
        "state.selection",
        "data.missing",
    }
    assert set(schema["text_roles"]) == {
        "display",
        "body",
        "label",
        "metadata",
        "code",
        "axis",
        "unit",
        "source",
    }


def test_proof_schema_is_layout_free_and_color_independent() -> None:
    schema = load("proof-schema.yaml")
    assert schema["kind"] == "accessibility-proof-schema"
    assert set(schema["forbidden_keys"]) >= {
        "layout",
        "coordinates",
        "x",
        "y",
        "row",
        "column",
        "grid",
    }
    assert set(schema["redundant_carriers"]) >= {
        "direct_label",
        "shape",
        "line_style",
        "pattern",
        "stroke_weight",
        "arrowhead",
        "boundary",
        "position_from_zero",
    }


def test_all_declared_accessible_pairs_meet_exact_profile_thresholds() -> None:
    tokens = load("contracts/tokens.yaml")
    contrast = load("contracts/contrast.yaml")
    for profile_name, profile in tokens["profiles"].items():
        thresholds = contrast["profiles"][profile_name]
        values = profile["tokens"]
        for pairing in profile["allowed_pairings"]:
            ratio = contrast_ratio(values[pairing["foreground"]], values[pairing["background"]])
            minimum = thresholds[
                "minimum_text_contrast"
                if pairing["kind"] == "text"
                else "minimum_non_text_contrast"
            ]
            assert ratio >= minimum, (
                profile_name,
                pairing["foreground"],
                pairing["background"],
                ratio,
                minimum,
            )


def test_contrast_contract_keeps_text_non_text_focus_and_projector_margins() -> None:
    contract = load("contracts/contrast.yaml")
    assert contract["profiles"]["light"]["minimum_text_contrast"] == 4.5
    assert contract["profiles"]["night"]["minimum_non_text_contrast"] == 3.0
    assert contract["profiles"]["projector"]["minimum_text_contrast"] == 7.0
    assert contract["profiles"]["projector"]["minimum_non_text_contrast"] == 4.5
    assert contract["focus"]["minimum_change_contrast"] == 3.0
    assert contract["focus"]["minimum_perimeter_css_px"] == 2


def test_fallback_contract_covers_cvd_monochrome_and_analytical_meaning() -> None:
    contract = load("contracts/fallbacks.yaml")
    assert contract["color_vision"]["profiles"] == [
        "protanopia",
        "deuteranopia",
        "tritanopia",
        "achromatopsia",
    ]
    assert contract["color_vision"]["color_only_meaning_allowed"] is False
    assert set(contract["semantic_states"]) >= {
        "focus",
        "selection",
        "error",
        "positive",
        "attention",
        "data",
        "signal",
        "missing",
        "uncertainty",
        "observed",
        "forecast",
    }
    assert contract["legend"]["direct_labels_precede_legend"] is True
    assert contract["legend"]["maximum_items"] == 4


def test_compatibility_source_preserves_closed_dependencies() -> None:
    contract = load("contracts/compatibility.yaml")
    assert len(contract["components"]) == 15
    assert len(contract["recipes"]) == 23
    assert contract["prompt_dsl"]["version"] == "0.5"
    assert contract["prompt_dsl"]["changed"] is False
    assert len(contract["analytical_mode"]["families"]) == 10
    assert contract["analytical_mode"]["quantitative_invariants_preserved"] is True


def test_architecture_docs_record_d032_and_keep_milestone_7_deferred() -> None:
    assert "D-032" in (ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    milestone_6 = roadmap.split("## Milestone 6", 1)[1].split("## Milestone 7", 1)[0]
    milestone_7 = roadmap.split("## Milestone 7", 1)[1].split("## Milestone 8", 1)[0]
    assert "**State:** active" in milestone_6
    assert "**State:** deferred" in milestone_7


def test_release_candidate_docs_and_ci_cover_milestone_6() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
    assert "## Night Mode and Accessibility v0.1" in readme
    assert "Milestone 6 integration pending" in status
    assert "tools/build_accessibility_mode.py" in workflow
    assert "tools/validate_accessibility_mode.py" in workflow
