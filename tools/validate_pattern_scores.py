from __future__ import annotations

import csv
import sys
from pathlib import Path


CRITERIA = [
    "clarity",
    "presentation_readability",
    "memorability",
    "csdl_identity",
    "restraint",
    "content_fidelity",
    "semantic_integrity",
]
CRITICAL = ["clarity", "presentation_readability", "content_fidelity"]
HEADER = "family," + ",".join(CRITERIA)
EXPECTED_FAMILIES = {f"{index:02d}" for index in range(1, 21)}


def validate_pattern_scores(path: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            if reader.fieldnames != HEADER.split(","):
                errors.append("scores.csv header must equal " + HEADER)
    except OSError as error:
        return [f"scores.csv must be readable: {error}"]

    family_ids = [row.get("family", "") for row in rows]
    if len(family_ids) != len(set(family_ids)):
        errors.append("scores.csv family ids must be unique")
    actual = set(family_ids)
    if require_complete and actual != EXPECTED_FAMILIES:
        errors.append("scores.csv family ids must equal " + ",".join(sorted(EXPECTED_FAMILIES)))
    elif not require_complete and not actual.issubset(EXPECTED_FAMILIES):
        errors.append("scores.csv contains an unknown family id")

    for row in rows:
        family = row.get("family", "??")
        scores: dict[str, int] = {}
        for criterion in CRITERIA:
            try:
                value = int(row.get(criterion, ""))
            except (TypeError, ValueError):
                errors.append(f"family {family} {criterion} must be an integer from 1 to 5")
                continue
            scores[criterion] = value
            if value < 1 or value > 5:
                errors.append(f"family {family} {criterion} must be between 1 and 5")
            if value < 4:
                errors.append(f"family {family} {criterion} must be at least 4")

        for criterion in CRITICAL:
            if scores.get(criterion) != 5:
                errors.append(f"family {family} {criterion} must equal 5")
        if len(scores) == len(CRITERIA) and sum(scores.values()) / len(scores) < 4.4:
            errors.append(f"family {family} average must be at least 4.4")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_pattern_scores.py SCORES_CSV")
        return 2
    errors = validate_pattern_scores(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pattern scores valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
