from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_pattern_catalog import resolve_asset


def validate_pattern_index(
    root: Path,
    require_complete: bool = True,
    index_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    index_path = index_path or root / "index.yaml"
    try:
        manifest: dict[str, Any] = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
        index: dict[str, Any] = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"pattern index inputs must be readable YAML: {error}"]

    if index.get("catalog") != manifest.get("catalog", {}).get("id"):
        errors.append("index.catalog must match manifest catalog id")
    if index.get("version") != manifest.get("catalog", {}).get("version"):
        errors.append("index.version must match manifest catalog version")

    manifest_families = manifest.get("families", [])
    index_families = index.get("families", [])
    expected_pairs = [(str(family.get("id")), family.get("slug")) for family in manifest_families]
    actual_pairs = [(str(family.get("id")), family.get("slug")) for family in index_families]
    if actual_pairs != expected_pairs:
        errors.append("index family ids and slugs must match manifest order")
        return errors

    scores_path = root / "evaluation/scores.csv"
    with scores_path.open(newline="", encoding="utf-8") as handle:
        scores = {row["family"]: row for row in csv.DictReader(handle)}

    for family, entry in zip(manifest_families, index_families, strict=True):
        family_id = str(family["id"])
        source = resolve_asset(root, family)
        row = scores.get(family_id)
        complete_fields = {"sha256", "dimensions", "color_mode", "score_average"}
        complete = source.exists() and row is not None and complete_fields.issubset(entry)
        if require_complete and not complete:
            errors.append(f"family {family_id} index evidence is incomplete")
            continue
        if not complete:
            if entry.get("status") != "awaiting_generation":
                errors.append(f"family {family_id} incomplete index entry must be awaiting_generation")
            continue

        if entry.get("status") == "awaiting_generation":
            errors.append(f"family {family_id} complete index entry cannot be awaiting_generation")
        actual_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        if entry.get("sha256") != actual_hash:
            errors.append(f"family {family_id} index SHA-256 does not match canonical asset")
        with Image.open(source) as image:
            if entry.get("dimensions") != f"{image.size[0]}x{image.size[1]}":
                errors.append(f"family {family_id} index dimensions do not match canonical asset")
            if entry.get("color_mode") != image.mode:
                errors.append(f"family {family_id} index color mode does not match canonical asset")
        values = [int(row[key]) for key in row if key != "family"]
        expected_average = round(sum(values) / len(values), 2)
        if entry.get("score_average") != expected_average:
            errors.append(f"family {family_id} index score average does not match scores.csv")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_pattern_index.py CATALOG_ROOT")
        return 2
    errors = validate_pattern_index(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pattern index valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
