from __future__ import annotations

import sys
from math import ceil, sqrt
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw


CANVAS_SIZE = (3840, 2160)
THUMB_SIZE = (840, 472)
BACKGROUND = "#F7F5F0"
INK = "#1B1B19"
HORIZONTAL_MARGIN = 120
VERTICAL_MARGIN = 120
HORIZONTAL_GAP = 80
VERTICAL_GAP = 80
LABEL_SPACE = 52


def _layout(count: int) -> tuple[tuple[int, int], list[tuple[int, int]]]:
    columns = min(5, ceil(sqrt(count * 16 / 9)))
    rows = ceil(count / columns)
    available_width = (
        CANVAS_SIZE[0] - 2 * HORIZONTAL_MARGIN - (columns - 1) * HORIZONTAL_GAP
    )
    available_height = (
        CANVAS_SIZE[1]
        - 2 * VERTICAL_MARGIN
        - rows * LABEL_SPACE
        - (rows - 1) * VERTICAL_GAP
    )
    cell_width = available_width // columns
    cell_height = available_height // rows
    thumb_width = min(THUMB_SIZE[0], cell_width, cell_height * 16 // 9)
    thumb_height = thumb_width * 9 // 16
    row_height = thumb_height + LABEL_SPACE
    grid_height = rows * row_height + (rows - 1) * VERTICAL_GAP
    grid_start_y = (CANVAS_SIZE[1] - grid_height) // 2

    positions: list[tuple[int, int]] = []
    for row in range(rows):
        row_start = row * columns
        items_in_row = min(columns, count - row_start)
        row_width = items_in_row * thumb_width + (items_in_row - 1) * HORIZONTAL_GAP
        start_x = (CANVAS_SIZE[0] - row_width) // 2
        start_y = grid_start_y + row * (row_height + VERTICAL_GAP) + LABEL_SPACE
        positions.extend(
            (start_x + column * (thumb_width + HORIZONTAL_GAP), start_y)
            for column in range(items_in_row)
        )
    return (thumb_width, thumb_height), positions


def build_contact_sheet(inputs: Iterable[Path], output: Path) -> None:
    paths = list(inputs)
    if not paths:
        raise ValueError("contact sheet requires at least one slide")
    thumb_size, positions = _layout(len(paths))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", CANVAS_SIZE, BACKGROUND)
    draw = ImageDraw.Draw(canvas)
    for index, (path, position) in enumerate(zip(paths, positions, strict=True), start=1):
        with Image.open(path).convert("RGB") as image:
            thumb = image.resize(thumb_size, Image.Resampling.LANCZOS)
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
