from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


CARD_SLUGS = [
    "01-hook",
    "02-problem",
    "03-model",
    "04-comparison",
    "05-synthesis",
    "06-takeaway",
    "07-share-card",
]
def _check_image(path: Path, expected_size: tuple[int, int], errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing asset: {path.as_posix()}")
        return
    with Image.open(path) as image:
        if image.size != expected_size:
            errors.append(
                f"{path.name} must be {expected_size[0]}x{expected_size[1]}, "
                f"got {image.size[0]}x{image.size[1]}"
            )
        if image.mode not in {"RGB", "RGBA"}:
            errors.append(f"{path.name} must use RGB or RGBA mode, got {image.mode}")


def validate_assets(root: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    card_slugs = CARD_SLUGS if require_complete else []

    if not require_complete:
        card_dir = root / "canonical/light/16x9"
        card_slugs = [path.stem for path in card_dir.glob("*.png")] if card_dir.exists() else []

    for slug in card_slugs:
        _check_image(root / "canonical/light/16x9" / f"{slug}.png", (1920, 1080), errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_assets.py PILOT_ROOT")
        return 2
    errors = validate_assets(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("assets valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
