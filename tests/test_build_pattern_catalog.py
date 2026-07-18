from pathlib import Path

from PIL import Image

from tools.build_pattern_catalog import build_contact_sheet


def make_inputs(tmp_path: Path, count: int) -> list[Path]:
    paths: list[Path] = []
    for index in range(count):
        path = tmp_path / f"{index:02d}.png"
        Image.new("RGB", (1280, 720), (247, 245, 240)).save(path)
        paths.append(path)
    return paths


def test_builds_twenty_family_contact_sheet(tmp_path: Path) -> None:
    output = tmp_path / "sheet.png"
    build_contact_sheet(make_inputs(tmp_path, 20), output)
    with Image.open(output) as image:
        assert image.size == (3840, 2160)
        assert image.mode == "RGB"


def test_contact_sheet_requires_an_image(tmp_path: Path) -> None:
    try:
        build_contact_sheet([], tmp_path / "sheet.png")
    except ValueError as error:
        assert str(error) == "contact sheet requires at least one image"
    else:
        raise AssertionError("expected ValueError")
