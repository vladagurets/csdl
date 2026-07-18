from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


EXPECTED_RHYTHM = ["A", "A", "B", "A", "B", "A", "C"]
EXPECTED_IDS = [f"{index:02d}" for index in range(1, 8)]
REQUIRED_CARD_FIELDS = {
    "id",
    "slug",
    "recipe",
    "level",
    "headline",
    "supporting_copy",
    "visual_mechanism",
    "components",
    "signal",
    "max_supporting_elements",
}


def _word_count(text: str) -> int:
    return len([part for part in text.replace("\n", " ").split(" ") if part.strip()])


def validate_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    pilot = data.get("pilot", {})
    cards = data.get("cards", [])

    if pilot.get("canonical_canvas") != "1920x1080":
        errors.append("pilot.canonical_canvas must equal 1920x1080")
    if pilot.get("orientation") != "landscape":
        errors.append("pilot.orientation must equal landscape")
    if pilot.get("rhythm") != EXPECTED_RHYTHM:
        errors.append("pilot.rhythm must equal A,A,B,A,B,A,C")
    if pilot.get("card_count") != 7:
        errors.append("pilot.card_count must equal 7")
    if len(cards) != 7:
        errors.append("cards must contain exactly 7 entries")
        return errors

    actual_ids = [str(card.get("id", "")) for card in cards]
    if actual_ids != EXPECTED_IDS:
        errors.append("card ids must equal 01,02,03,04,05,06,07")

    for index, (card, expected_level) in enumerate(zip(cards, EXPECTED_RHYTHM, strict=True), start=1):
        card_id = f"{index:02d}"
        missing = sorted(REQUIRED_CARD_FIELDS - set(card))
        if missing:
            errors.append(f"card {card_id} missing fields: {','.join(missing)}")
        if card.get("level") != expected_level:
            errors.append(f"card {card_id} level must be {expected_level}")
        if _word_count(str(card.get("supporting_copy", ""))) > 40:
            errors.append(f"card {card_id} supporting_copy exceeds 40 words")
        components = card.get("components", [])
        if not isinstance(components, list) or not components:
            errors.append(f"card {card_id} components must be a non-empty list")
        max_elements = card.get("max_supporting_elements")
        if not isinstance(max_elements, int) or max_elements < 1 or max_elements > 4:
            errors.append(f"card {card_id} max_supporting_elements must be between 1 and 4")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_manifest.py PATH")
        return 2
    errors = validate_manifest(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("manifest valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
