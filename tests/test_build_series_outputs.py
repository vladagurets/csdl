from pathlib import Path

from PIL import Image

from tools.build_contact_sheet import build_contact_sheet, numeric_png_paths
from tools.build_landscape_previews import build_pilot_previews, build_preview


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


def test_builds_semantic_preview_names_from_incremental_canonical_assets(
    tmp_path: Path,
) -> None:
    root = tmp_path / "02-sample"
    _image(root / "canonical/light/16x9/1.png")
    _image(root / "canonical/light/16x9/2.png")
    (root / "manifest.yaml").write_text(
        "cards:\n"
        "  - {id: '01', slug: first-slide}\n"
        "  - {id: '02', slug: second-slide}\n",
        encoding="utf-8",
    )

    outputs = build_pilot_previews(root)

    assert [path.name for path in outputs] == [
        "01-first-slide.png",
        "02-second-slide.png",
    ]


def test_orders_incremental_png_names_numerically(tmp_path: Path) -> None:
    for name in ["10.png", "2.png", "1.png"]:
        _image(tmp_path / name)

    assert [path.name for path in numeric_png_paths(tmp_path)] == [
        "1.png",
        "2.png",
        "10.png",
    ]


def test_builds_landscape_contact_sheet(tmp_path: Path) -> None:
    inputs = [_image(tmp_path / f"{index}.png") for index in range(7)]
    output = tmp_path / "sheet.png"
    build_contact_sheet(inputs, output)
    with Image.open(output) as image:
        assert image.size == (3840, 2160)
        assert image.mode == "RGB"


def test_builds_eight_slide_landscape_contact_sheet(tmp_path: Path) -> None:
    inputs = [_image(tmp_path / f"{index}.png") for index in range(8)]
    output = tmp_path / "sheet.png"
    build_contact_sheet(inputs, output)
    with Image.open(output) as image:
        assert image.size == (3840, 2160)
        assert image.mode == "RGB"


def test_contact_sheet_requires_at_least_one_slide(tmp_path: Path) -> None:
    try:
        build_contact_sheet([], tmp_path / "sheet.png")
    except ValueError as error:
        assert str(error) == "contact sheet requires at least one slide"
    else:
        raise AssertionError("expected ValueError")
