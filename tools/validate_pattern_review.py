from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml


GENERATED_REQUIREMENTS = [
    "**Selected:**",
    "**Source SHA-256:**",
    "**Canonical SHA-256:**",
    "Primary-authority comparison: pass",
    "Series contact-sheet review: pass",
]


def _sections(review: str) -> dict[str, tuple[str, str]]:
    matches = list(re.finditer(r"^### (?P<id>\d{2}) (?P<title>.+)$", review, flags=re.MULTILINE))
    sections: dict[str, tuple[str, str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(review)
        sections[match.group("id")] = (match.group("title"), review[match.start() : end])
    return sections


def validate_pattern_review(root: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    try:
        manifest: dict[str, Any] = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
        review = (root / "evaluation/review.md").read_text(encoding="utf-8")
        with (root / "evaluation/scores.csv").open(newline="", encoding="utf-8") as handle:
            accepted = {row["family"] for row in csv.DictReader(handle)}
    except (OSError, yaml.YAMLError, KeyError) as error:
        return [f"pattern review inputs must be readable: {error}"]

    sections = _sections(review)
    expected = {str(family["id"]) for family in manifest.get("families", [])}
    if require_complete and accepted != expected:
        errors.append("review validation requires accepted scores for all 20 families")

    for family in manifest.get("families", []):
        family_id = str(family["id"])
        if family_id not in accepted:
            continue
        if family_id not in sections:
            errors.append(f"family {family_id} accepted score requires a review section")
            continue
        title, section = sections[family_id]
        if "superseded" in title.lower():
            errors.append(f"family {family_id} superseded review cannot have an accepted score")
            continue
        if family.get("evidence", {}).get("mode") != "generated":
            continue
        if "accepted" not in title.lower():
            errors.append(f"family {family_id} generated review heading must say accepted")
        for requirement in GENERATED_REQUIREMENTS:
            if requirement not in section:
                errors.append(f"family {family_id} generated review missing: {requirement}")
        slug = family["slug"]
        for candidate in range(1, 4):
            filename = f"{family_id}-{slug}-v{candidate}.png"
            if filename not in section:
                errors.append(f"family {family_id} generated review missing candidate: {filename}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_pattern_review.py CATALOG_ROOT")
        return 2
    errors = validate_pattern_review(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pattern review valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
