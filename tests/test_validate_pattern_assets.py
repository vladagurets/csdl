from pathlib import Path

from PIL import Image
import yaml

from tools.validate_pattern_assets import validate_image, validate_pattern_assets


ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "patterns/visual-dna-sprint-01"


def test_incomplete_catalog_accepts_valid_pilot_references() -> None:
    assert validate_pattern_assets(CATALOG, require_complete=False) == []


def test_strict_catalog_reports_current_missing_generated_assets() -> None:
    errors = validate_pattern_assets(CATALOG)
    manifest = yaml.safe_load((CATALOG / "manifest.yaml").read_text(encoding="utf-8"))
    expected = {
        f"missing asset: {family['evidence']['canonical_example']}"
        for family in manifest["families"]
        if family["evidence"]["mode"] == "generated"
        and not (CATALOG / family["evidence"]["canonical_example"]).exists()
    }
    assert set(errors) == expected


def test_rejects_wrong_pattern_raster_size(tmp_path: Path) -> None:
    path = tmp_path / "example.png"
    Image.new("RGB", (1280, 720)).save(path)
    assert validate_image(path, "example.png") == ["example.png must be 1920x1080, got 1280x720"]
