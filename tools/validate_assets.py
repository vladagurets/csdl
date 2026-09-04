from __future__ import annotations

import re
import sys
from pathlib import Path

from PIL import Image


CARD_FILENAMES = [f"{index}.png" for index in range(1, 8)]
INCREMENTAL_FILENAME = re.compile(r"^[1-9][0-9]*\.png$")


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
    card_dir = root / "canonical/light/16x9"
    actual_paths = sorted(card_dir.glob("*.png")) if card_dir.exists() else []

    for path in actual_paths:
        if not INCREMENTAL_FILENAME.fullmatch(path.name):
            errors.append(f"unexpected canonical filename: {path.name}")

    filenames = (
        CARD_FILENAMES
        if require_complete
        else [path.name for path in actual_paths]
    )
    if require_complete:
        actual_names = {path.name for path in actual_paths}
        expected_names = set(CARD_FILENAMES)
        for extra in sorted(actual_names - expected_names):
            errors.append(f"unexpected canonical asset: {extra}")

    for filename in filenames:
        _check_image(card_dir / filename, (1920, 1080), errors)
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
