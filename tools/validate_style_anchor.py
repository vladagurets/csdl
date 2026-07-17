from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

EXPECTED_SIZE = (1080, 1350)
ALLOWED_MODES = {"RGB", "RGBA"}


def validate_style_anchor(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing style anchor: {path.as_posix()}"]

    errors: list[str] = []
    try:
        with Image.open(path) as image:
            if image.format != "PNG":
                errors.append(
                    f"{path.name} must be PNG, got {image.format or 'unknown'}"
                )
            if image.size != EXPECTED_SIZE:
                errors.append(
                    f"{path.name} must be 1080x1350, "
                    f"got {image.size[0]}x{image.size[1]}"
                )
            if image.mode not in ALLOWED_MODES:
                errors.append(
                    f"{path.name} must use RGB or RGBA mode, got {image.mode}"
                )
    except OSError:
        errors.append(f"{path.name} must be a readable PNG")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_style_anchor.py STYLE_ANCHOR_PNG")
        return 2

    errors = validate_style_anchor(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("style anchor valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
