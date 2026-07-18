from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw


CANVAS_SIZE = (3840, 2160)
THUMB_SIZE = (840, 472)
POSITIONS = [
    (120, 220),
    (1040, 220),
    (1960, 220),
    (2880, 220),
    (580, 1190),
    (1500, 1190),
    (2420, 1190),
]
BACKGROUND = "#F7F5F0"
INK = "#1B1B19"


def build_contact_sheet(inputs: Iterable[Path], output: Path) -> None:
    paths = list(inputs)
    if len(paths) != 7:
        raise ValueError("contact sheet requires exactly seven slides")
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", CANVAS_SIZE, BACKGROUND)
    draw = ImageDraw.Draw(canvas)
    for index, (path, position) in enumerate(zip(paths, POSITIONS, strict=True), start=1):
        with Image.open(path).convert("RGB") as image:
            thumb = image.resize(THUMB_SIZE, Image.Resampling.LANCZOS)
            canvas.paste(thumb, position)
        draw.text((position[0], position[1] - 52), f"{index:02d}", fill=INK)
    canvas.save(output)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python tools/build_contact_sheet.py INPUT_DIR OUTPUT_FILE")
        return 2
    input_dir = Path(sys.argv[1])
    build_contact_sheet(sorted(input_dir.glob("*.png")), Path(sys.argv[2]))
    print("contact sheet built")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
