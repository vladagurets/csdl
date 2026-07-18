from pathlib import Path
import shutil

import yaml

from tools.build_accessibility_mode import derive_accessibility_package
from tools.validate_accessibility_mode import (
    validate_accessibility_library,
    validate_accessibility_package,
    validate_negative_fixture,
)


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "accessibility/night-mode-v0.1"


def test_strict_accessibility_library_is_complete() -> None:
    assert validate_accessibility_library(LIBRARY) == []


def test_all_ten_proofs_rebuild_deterministically_and_validate() -> None:
    manifest = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    assert len(manifest["proofs"]) == 10
    for proof in manifest["proofs"]:
        source = yaml.safe_load((LIBRARY / proof["source"]).read_text(encoding="utf-8"))
        source["source_path"] = proof["source"]
        package = yaml.safe_load((LIBRARY / proof["package"]).read_text(encoding="utf-8"))
        assert package == derive_accessibility_package(source, LIBRARY)
        assert validate_accessibility_package(package, LIBRARY) == []


def test_required_proof_profiles_and_semantics_are_present() -> None:
    packages = {
        path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted((LIBRARY / "proofs/packages").glob("*.yaml"))
    }
    assert packages["01-editorial-equivalence"]["profiles"] == ["light", "night"]
    assert packages["02-structural-signal"]["profiles"] == [
        "light",
        "night",
        "monochrome",
    ]
    assert packages["09-monochrome-export"]["profiles"] == ["monochrome"]
    assert packages["10-projector-fallback"]["profiles"] == ["projector"]

    bar = packages["04-positive-negative-bar"]
    assert [record["variance"] for record in bar["source_semantics"]["records"]] == [
        12,
        -5,
        8,
        -3,
    ]
    assert next(item for item in bar["semantic_encodings"] if item["meaning"] == "data")[
        "zero_baseline"
    ] is True
    forecast = packages["05-forecast-uncertainty"]
    encodings = {item["meaning"]: item for item in forecast["semantic_encodings"]}
    assert encodings["observed"]["line_style"] == "solid"
    assert encodings["forecast"]["line_style"] == "dashed"
    assert encodings["uncertainty"]["visible"] is True
    assert encodings["uncertainty"]["level"] == 80
    assert forecast["source_semantics"]["encoding"]["forecast"]["boundary"] == "2027-Q1"
    assert packages["06-heatmap-fallback"]["semantic_encodings"][0]["missing_label"] == "N/A"
    assert packages["07-normalized-map"]["semantic_encodings"][0]["normalized_rate"] is True
    network = {item["meaning"]: item for item in packages["08-directed-network"]["semantic_encodings"]}
    assert "arrowhead" in network["direction"]["redundant_carriers"]
    assert "numeric_label" in network["weight"]["redundant_carriers"]


def test_negative_fixtures_fail_for_exact_declared_reason() -> None:
    fixture_root = LIBRARY / "fixtures/negative"
    expected = yaml.safe_load((fixture_root / "expected-errors.yaml").read_text(encoding="utf-8"))
    assert len(expected["fixtures"]) >= 17
    for fixture in expected["fixtures"]:
        errors = validate_negative_fixture(fixture_root / fixture["file"], LIBRARY)
        assert fixture["error"] in errors, (fixture["file"], errors)


def test_strict_library_rejects_drifted_package_and_index(tmp_path: Path) -> None:
    target = tmp_path / "accessibility/night-mode-v0.1"
    shutil.copytree(LIBRARY, target)
    shutil.copytree(ROOT / "components", tmp_path / "components")
    shutil.copytree(ROOT / "recipes", tmp_path / "recipes")
    shutil.copytree(ROOT / "analytics", tmp_path / "analytics")
    package_path = target / "proofs/packages/01-editorial-equivalence.yaml"
    package = yaml.safe_load(package_path.read_text(encoding="utf-8"))
    package["semantic_encodings"][0]["target"] = "mutated"
    package_path.write_text(yaml.safe_dump(package, sort_keys=False), encoding="utf-8")
    index_path = target / "index.yaml"
    index = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    index["proof_count"] = 9
    index_path.write_text(yaml.safe_dump(index, sort_keys=False), encoding="utf-8")

    errors = validate_accessibility_library(target)
    assert any("deterministic rebuild" in error for error in errors)
    assert "accessibility index does not match deterministic derivation" in errors
