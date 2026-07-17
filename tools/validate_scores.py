from __future__ import annotations

import csv
import sys
from pathlib import Path


CRITERIA = [
    "clarity",
    "mobile_readability",
    "memorability",
    "csdl_identity",
    "restraint",
    "text_fidelity",
    "semantic_integrity",
]
CRITICAL = ["clarity", "mobile_readability", "text_fidelity"]


def validate_scores(path: Path, expected_cards: set[str] | None = None) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if expected_cards is None:
        expected_cards = {f"{index:02d}" for index in range(1, 8)}
    actual_cards = {row.get("card", "") for row in rows}
    if actual_cards != expected_cards:
        errors.append(
            "scores.csv card ids must equal " + ",".join(sorted(expected_cards))
        )

    for row in rows:
        card = row.get("card", "??")
        scores: dict[str, int] = {}
        for criterion in CRITERIA:
            try:
                value = int(row[criterion])
            except (KeyError, TypeError, ValueError):
                errors.append(f"card {card} {criterion} must be an integer from 1 to 5")
                continue
            scores[criterion] = value
            if value < 1 or value > 5:
                errors.append(f"card {card} {criterion} must be between 1 and 5")
            elif value < 4:
                errors.append(f"card {card} {criterion} must be at least 4")

        for criterion in CRITICAL:
            if scores.get(criterion) != 5:
                errors.append(f"card {card} {criterion} must equal 5")

        if len(scores) == len(CRITERIA):
            average = sum(scores.values()) / len(CRITERIA)
            if average < 4.4:
                errors.append(f"card {card} average must be at least 4.4")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_scores.py SCORES_CSV")
        return 2
    errors = validate_scores(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("scores valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
