from __future__ import annotations

import sys
from pathlib import Path

import yaml
from PIL import Image


PREVIEW_SIZE = (1280, 720)


def build_preview(source: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source).convert("RGB") as image:
        image.resize(PREVIEW_SIZE, Image.Resampling.LANCZOS).save(output)


def numeric_png_paths(directory: Path) -> list[Path]:
    paths = list(directory.glob("*.png"))
    if all(path.stem.isdecimal() for path in paths):
        return sorted(paths, key=lambda path: int(path.stem))
    return sorted(paths)


def build_pilot_previews(root: Path) -> list[Path]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    outputs: list[Path] = []
    for position, card in enumerate(manifest["cards"], start=1):
        source = root / f"canonical/light/16x9/{position}.png"
        stem = f"{card['id']}-{card['slug']}"
        output = root / f"previews/landscape/{stem}.png"
        build_preview(source, output)
        outputs.append(output)
    return outputs


def main() -> int:
    if len(sys.argv) == 2:
        build_pilot_previews(Path(sys.argv[1]))
        print("pilot landscape previews built")
        return 0
    if len(sys.argv) != 3:
        print(
            "usage: python tools/build_landscape_previews.py PILOT_ROOT\n"
            "   or: python tools/build_landscape_previews.py INPUT_DIR OUTPUT_DIR"
        )
        return 2
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    for source in numeric_png_paths(input_dir):
        build_preview(source, output_dir / source.name)
    print("landscape previews built")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
