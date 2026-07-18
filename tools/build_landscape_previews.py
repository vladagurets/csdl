from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


PREVIEW_SIZE = (1280, 720)


def build_preview(source: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source).convert("RGB") as image:
        image.resize(PREVIEW_SIZE, Image.Resampling.LANCZOS).save(output)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python tools/build_landscape_previews.py INPUT_DIR OUTPUT_DIR")
        return 2
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    for source in sorted(input_dir.glob("*.png")):
        build_preview(source, output_dir / source.name)
    print("landscape previews built")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
