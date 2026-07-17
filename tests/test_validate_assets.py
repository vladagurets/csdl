from pathlib import Path

from PIL import Image

from tools.validate_assets import validate_assets


def create_png(path: Path, size: tuple[int, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, "white").save(path)


def test_accepts_complete_asset_set(tmp_path: Path) -> None:
    for slug in [
        "01-hook",
        "02-problem",
        "03-model",
        "04-comparison",
        "05-synthesis",
        "06-takeaway",
        "07-share-card",
    ]:
        create_png(tmp_path / "canonical/light/4x5" / f"{slug}.png", (1080, 1350))
    for slug in ["01-hook", "04-comparison", "07-share-card"]:
        create_png(tmp_path / "canonical/light/16x9" / f"{slug}.png", (1920, 1080))
    assert validate_assets(tmp_path) == []


def test_rejects_wrong_dimensions(tmp_path: Path) -> None:
    create_png(tmp_path / "canonical/light/4x5/01-hook.png", (1080, 1080))
    errors = validate_assets(tmp_path, require_complete=False)
    assert "01-hook.png must be 1080x1350, got 1080x1080" in errors
