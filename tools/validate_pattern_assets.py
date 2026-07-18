from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, UnidentifiedImageError


def validate_image(path: Path, label: str) -> list[str]:
    if not path.exists():
        return [f"missing asset: {label}"]
    try:
        with Image.open(path) as image:
            if image.format != "PNG":
                return [f"{label} must be PNG, got {image.format or 'unknown'}"]
            errors: list[str] = []
            if image.size != (1920, 1080):
                errors.append(f"{label} must be 1920x1080, got {image.size[0]}x{image.size[1]}")
            if image.mode not in {"RGB", "RGBA"}:
                errors.append(f"{label} must use RGB or RGBA mode, got {image.mode}")
            return errors
    except (OSError, UnidentifiedImageError):
        return [f"{label} must be a readable PNG"]


def validate_pattern_assets(root: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    manifest_path = root / "manifest.yaml"
    try:
        data: dict[str, Any] = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"manifest must be readable YAML: {error}"]

    repo_root = root.parents[1]
    expected_generated: set[Path] = set()
    for family in data.get("families", []):
        evidence = family.get("evidence", {})
        canonical = Path(str(evidence.get("canonical_example", "")))
        mode = evidence.get("mode")
        if mode == "generated":
            path = root / canonical
            expected_generated.add(path)
            if require_complete or path.exists():
                errors.extend(validate_image(path, canonical.as_posix()))
        elif mode == "pilot_reference":
            path = repo_root / canonical
            errors.extend(validate_image(path, canonical.as_posix()))
            if path.exists():
                actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
                if actual_hash != evidence.get("sha256"):
                    errors.append(f"{canonical.as_posix()} SHA-256 does not match manifest evidence")

    canonical_dir = root / "canonical/light/16x9"
    actual_generated = set(canonical_dir.glob("*.png")) if canonical_dir.exists() else set()
    extras = sorted(actual_generated - expected_generated)
    for extra in extras:
        errors.append(f"unexpected canonical asset: {extra.relative_to(root).as_posix()}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_pattern_assets.py CATALOG_ROOT")
        return 2
    errors = validate_pattern_assets(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pattern assets valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
