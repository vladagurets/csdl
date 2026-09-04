from pathlib import Path

from PIL import Image

from tools.validate_assets import validate_assets


def create_png(path: Path, size: tuple[int, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, "white").save(path)


def test_accepts_complete_asset_set(tmp_path: Path) -> None:
    for index in range(1, 8):
        create_png(tmp_path / "canonical/light/16x9" / f"{index}.png", (1920, 1080))
    assert validate_assets(tmp_path) == []


def test_rejects_wrong_dimensions(tmp_path: Path) -> None:
    create_png(tmp_path / "canonical/light/16x9/1.png", (1080, 1080))
    errors = validate_assets(tmp_path, require_complete=False)
    assert "1.png must be 1920x1080, got 1080x1080" in errors
