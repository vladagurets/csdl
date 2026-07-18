from pathlib import Path
import shutil

import yaml

from tools.validate_component_library import validate_component_library


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "components/component-library-v0.1"


def copy_library_contract(tmp_path: Path) -> Path:
    target = tmp_path / "components/component-library-v0.1"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    return target / "manifest.yaml"


def complete_component() -> dict:
    return {
        "id": "01",
        "slug": "anchor",
        "name": "Anchor",
        "category": "semantic",
        "purpose": "Carry one dominant proposition.",
        "semantic_meaning": "Primary semantic read.",
        "spatial_contract": {"count": {"min": 1, "max": 1}},
        "dimensions": {"unit": "px", "area_percent": {"min": 0, "max": 100}},
        "relations": {
            "allowed": [
                {
                    "type": "highlights",
                    "target": "Signal",
                    "direction": "inbound",
                    "cardinality": "zero_or_one",
                }
            ],
            "forbidden": [],
        },
        "compatible_families": ["hero"],
        "expression_limits": {
            "A": {"status": "allowed", "max_count": 1},
            "B": {"status": "allowed", "max_count": 1},
            "C": {"status": "allowed", "max_count": 1},
        },
        "typography": {"role": "display", "constraints": ["horizontal"]},
        "semantic_color": {"default": "ink.primary", "signal_target_allowed": True},
        "examples": {
            "do": [
                {
                    "description": "One proposition owns the first read.",
                    "evidence": "README.md",
                }
            ],
            "dont": [
                {
                    "description": "Do not add a second peer proposition.",
                    "evidence": "README.md",
                }
            ],
        },
        "prompt_dsl": {
            "syntax": "Anchor(id=thesis, role=primary)",
            "required_fields": ["id", "role"],
            "optional_fields": [],
        },
        "validation_invariants": ["Anchor has one semantic owner."],
        "evidence": [
            {
                "path": "README.md",
                "locator": "Evidence convention",
                "supports": "Fixture evidence.",
            }
        ],
        "specification": "specs/01-anchor.md",
        "evidence_level": "strong",
    }


def add_complete_component(manifest: Path, component: dict) -> None:
    data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    data["components"].append(component)
    manifest.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    specification = manifest.parent / component["specification"]
    specification.parent.mkdir(exist_ok=True)
    specification.write_text(
        (manifest.parent / "TEMPLATE.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )


def test_infrastructure_manifest_is_valid_in_incomplete_mode() -> None:
    errors = validate_component_library(LIBRARY / "manifest.yaml", require_complete=False)
    assert errors == []


def test_foundation_packet_contains_complete_expected_components() -> None:
    data = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    foundation_slugs = ["anchor", "signal", "field", "frame", "label"]

    assert [
        component["slug"]
        for component in data["components"]
        if component["slug"] in foundation_slugs
    ] == foundation_slugs
    assert validate_component_library(LIBRARY / "manifest.yaml", require_complete=False) == []


def test_units_packet_contains_complete_expected_components() -> None:
    data = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    unit_slugs = [
        "anchor",
        "signal",
        "field",
        "frame",
        "cluster",
        "divider",
        "node",
        "axis",
        "label",
    ]

    assert [
        component["slug"]
        for component in data["components"]
        if component["slug"] in unit_slugs
    ] == unit_slugs
    assert validate_component_library(LIBRARY / "manifest.yaml", require_complete=False) == []


def test_relation_packet_contains_complete_expected_components() -> None:
    data = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))

    assert [component["slug"] for component in data["components"]] == [
        "anchor",
        "signal",
        "field",
        "frame",
        "cluster",
        "vector",
        "divider",
        "node",
        "loop",
        "collision",
        "bridge",
        "axis",
        "label",
    ]
    assert validate_component_library(LIBRARY / "manifest.yaml", require_complete=False) == []


def test_active_visual_dna_contract_uses_only_declared_component_names() -> None:
    data = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    assert data["components"]
    assert not any(
        "undeclared active component name" in error
        for error in validate_component_library(LIBRARY / "manifest.yaml", require_complete=False)
    )


def test_strict_mode_requires_exact_component_set() -> None:
    assert "components must contain exactly 15 entries" in validate_component_library(
        LIBRARY / "manifest.yaml"
    )


def test_incomplete_mode_rejects_partial_component_record(tmp_path: Path) -> None:
    manifest = copy_library_contract(tmp_path)
    data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    data["components"].append({"id": "01", "slug": "anchor", "name": "Anchor"})
    manifest.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    errors = validate_component_library(manifest, require_complete=False)

    assert any(error.startswith("component 01 missing fields:") for error in errors)


def test_rejects_unknown_top_level_component_field(tmp_path: Path) -> None:
    manifest = copy_library_contract(tmp_path)
    component = complete_component()
    component["layout"] = "left"
    add_complete_component(manifest, component)

    errors = validate_component_library(manifest, require_complete=False)

    assert "component 01 contains unknown fields: layout" in errors


def test_rejects_allowed_forbidden_relation_contradiction(tmp_path: Path) -> None:
    manifest = copy_library_contract(tmp_path)
    component = complete_component()
    component["relations"]["forbidden"] = [component["relations"]["allowed"][0].copy()]
    add_complete_component(manifest, component)

    errors = validate_component_library(manifest, require_complete=False)

    assert any(error.startswith("component 01 relation is both allowed and forbidden:") for error in errors)


def test_rejects_missing_evidence_path(tmp_path: Path) -> None:
    manifest = copy_library_contract(tmp_path)
    component = complete_component()
    component["evidence"][0]["path"] = "missing-evidence.md"
    add_complete_component(manifest, component)

    errors = validate_component_library(manifest, require_complete=False)

    assert "component 01 evidence entry 1 path does not exist: missing-evidence.md" in errors


def test_rejects_forbidden_marker_in_complete_record(tmp_path: Path) -> None:
    manifest = copy_library_contract(tmp_path)
    component = complete_component()
    component["purpose"] = "TBD"
    add_complete_component(manifest, component)

    errors = validate_component_library(manifest, require_complete=False)

    assert "component 01 manifest contains forbidden marker: TBD" in errors
