import hashlib
from pathlib import Path

from PIL import Image

from tools.validate_style_anchor import validate_style_anchor


def create_image(
    path: Path,
    *,
    size: tuple[int, int] = (1080, 1350),
    mode: str = "RGB",
    image_format: str = "PNG",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new(mode, size).save(path, format=image_format)


def test_accepts_valid_style_anchor(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    assert validate_style_anchor(path) == []


def test_rejects_unapproved_style_anchor_hash(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    expected = "0" * 64
    actual = hashlib.sha256(path.read_bytes()).hexdigest()

    assert validate_style_anchor(path, expected_sha256=expected) == [
        f"style-anchor-light.png SHA-256 must be {expected}, got {actual}"
    ]


def test_rejects_missing_style_anchor(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    assert validate_style_anchor(path) == [
        f"missing style anchor: {path.as_posix()}"
    ]


def test_rejects_non_png_content(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, image_format="JPEG")
    assert "style-anchor-light.png must be PNG, got JPEG" in validate_style_anchor(path)


def test_rejects_truncated_png(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    path.write_bytes(path.read_bytes()[:-12])
    assert "style-anchor-light.png must be a readable PNG" in validate_style_anchor(path)


def test_rejects_corrupt_png_checksum(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    data = bytearray(path.read_bytes())
    idat = data.index(b"IDAT")
    data[idat + 8] ^= 0x01
    path.write_bytes(data)
    assert "style-anchor-light.png must be a readable PNG" in validate_style_anchor(path)


def test_rejects_wrong_dimensions(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, size=(1080, 1080))
    assert "style-anchor-light.png must be 1080x1350, got 1080x1080" in validate_style_anchor(path)


def test_rejects_unsupported_color_mode(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, mode="L")
    assert "style-anchor-light.png must use RGB or RGBA mode, got L" in validate_style_anchor(path)
