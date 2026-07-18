from pathlib import Path

from PIL import Image

from tools.validate_pattern_assets import validate_image, validate_pattern_assets


ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "patterns/visual-dna-sprint-01"


def test_incomplete_catalog_accepts_valid_pilot_references() -> None:
    assert validate_pattern_assets(CATALOG, require_complete=False) == []


def test_strict_catalog_reports_missing_generated_assets() -> None:
    errors = validate_pattern_assets(CATALOG)
    assert "missing asset: canonical/light/16x9/02-cover.png" in errors
    assert len([error for error in errors if error.startswith("missing asset:")]) == 17


def test_rejects_wrong_pattern_raster_size(tmp_path: Path) -> None:
    path = tmp_path / "example.png"
    Image.new("RGB", (1280, 720)).save(path)
    assert validate_image(path, "example.png") == ["example.png must be 1920x1080, got 1280x720"]
