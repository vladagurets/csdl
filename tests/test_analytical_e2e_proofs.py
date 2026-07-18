from pathlib import Path
import shutil

import yaml

from tools.build_analytical_mode import derive_analytical_package
from tools.validate_analytical_mode import (
    validate_analytical_library,
    validate_negative_fixture,
    validate_analytical_package,
)


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "analytics/analytical-mode-v0.1"


def test_strict_analytical_library_is_complete() -> None:
    assert validate_analytical_library(LIBRARY) == []


def test_all_ten_proofs_rebuild_deterministically_and_validate() -> None:
    manifest = yaml.safe_load((LIBRARY / "manifest.yaml").read_text(encoding="utf-8"))
    assert len(manifest["proofs"]) == 10
    for proof in manifest["proofs"]:
        source = yaml.safe_load((LIBRARY / proof["source"]).read_text(encoding="utf-8"))
        source["source_path"] = proof["source"]
        dataset = yaml.safe_load((LIBRARY / source["dataset"]).read_text(encoding="utf-8"))
        package = yaml.safe_load((LIBRARY / proof["package"]).read_text(encoding="utf-8"))
        assert package == derive_analytical_package(source, dataset, LIBRARY)
        assert validate_analytical_package(package, LIBRARY) == []


def test_family_proofs_preserve_critical_derived_values() -> None:
    packages = {
        path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted((LIBRARY / "proofs/packages").glob("*.yaml"))
    }
    assert packages["01-bar-positive-negative"]["encoding"]["zero_baseline"] is True
    line = packages["02-line-forecast"]
    assert line["encoding"]["forecast"]["boundary"] == "2027-Q1"
    assert line["encoding"]["uncertainty"]["type"] == "prediction_interval"
    assert line["encoding"]["uncertainty"]["level"] == 80
    assert packages["04-waterfall"]["specification"]["derived"]["cumulative"] == [100, 125, 115, 130, 130]
    assert packages["06-funnel"]["specification"]["derived"]["previous_stage_conversion"] == [100.0, 65.0, 60.0, 50.0]
    assert packages["07-map"]["specification"]["derived"]["rate_per_100000"] == [4.0, 6.0, None]
    dashboard = packages["10-dashboard"]
    assert {view["dataset"] for view in dashboard["encoding"]["views"]} == {"dashboard-agent-reliability-v1@1.0.0"}


def test_negative_fixtures_fail_for_exact_declared_reason() -> None:
    fixture_root = LIBRARY / "fixtures/negative"
    expected = yaml.safe_load((fixture_root / "expected-errors.yaml").read_text(encoding="utf-8"))
    assert len(expected["fixtures"]) >= 15
    for fixture in expected["fixtures"]:
        errors = validate_negative_fixture(fixture_root / fixture["file"], LIBRARY)
        assert fixture["error"] in errors, fixture["file"]


def test_strict_library_rejects_drifted_package_and_index(tmp_path: Path) -> None:
    target = tmp_path / "analytics/analytical-mode-v0.1"
    shutil.copytree(LIBRARY, target)
    shutil.copytree(
        ROOT / "components/component-library-v0.1",
        tmp_path / "components/component-library-v0.1",
    )
    shutil.copytree(
        ROOT / "recipes/recipe-library-v0.5",
        tmp_path / "recipes/recipe-library-v0.5",
    )
    package_path = target / "proofs/packages/01-bar-positive-negative.yaml"
    package = yaml.safe_load(package_path.read_text(encoding="utf-8"))
    package["specification"]["records"][0]["variance"] = 999
    package_path.write_text(yaml.safe_dump(package, sort_keys=False), encoding="utf-8")
    index_path = target / "index.yaml"
    index = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    index["family_count"] = 9
    index_path.write_text(yaml.safe_dump(index, sort_keys=False), encoding="utf-8")

    errors = validate_analytical_library(target)
    assert "analytical specification records must match canonical dataset" in errors
    assert "analytical index does not match deterministic derivation" in errors
