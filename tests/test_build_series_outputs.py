from pathlib import Path

from PIL import Image

from tools.build_contact_sheet import build_contact_sheet
from tools.build_landscape_previews import build_preview


def _image(path: Path, size: tuple[int, int] = (1920, 1080)) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, "white").save(path)
    return path


def test_builds_landscape_preview(tmp_path: Path) -> None:
    source = _image(tmp_path / "source.png")
    output = tmp_path / "preview.png"
    build_preview(source, output)
    with Image.open(output) as image:
        assert image.size == (1280, 720)
        assert image.mode == "RGB"


def test_builds_landscape_contact_sheet(tmp_path: Path) -> None:
    inputs = [_image(tmp_path / f"{index}.png") for index in range(7)]
    output = tmp_path / "sheet.png"
    build_contact_sheet(inputs, output)
    with Image.open(output) as image:
        assert image.size == (3840, 2160)
        assert image.mode == "RGB"


def test_contact_sheet_requires_seven_slides(tmp_path: Path) -> None:
    inputs = [_image(tmp_path / f"{index}.png") for index in range(6)]
    try:
        build_contact_sheet(inputs, tmp_path / "sheet.png")
    except ValueError as error:
        assert str(error) == "contact sheet requires exactly seven slides"
    else:
        raise AssertionError("expected ValueError")
