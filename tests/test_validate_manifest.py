from pathlib import Path

import yaml

from tools.validate_manifest import validate_manifest


VALID_MANIFEST = {
    "pilot": {
        "canonical_canvas": "1920x1080",
        "orientation": "landscape",
        "rhythm": ["A", "A", "B", "A", "B", "A", "C"],
        "card_count": 7,
    },
    "cards": [
        {
            "id": f"{index:02d}",
            "slug": f"card-{index}",
            "recipe": "Hero",
            "level": level,
            "headline": "HEADLINE",
            "supporting_copy": "Короткий точний текст.",
            "visual_mechanism": "One mechanism",
            "components": ["Anchor", "Signal"],
            "signal": "coral",
            "max_supporting_elements": 2,
        }
        for index, level in enumerate(["A", "A", "B", "A", "B", "A", "C"], start=1)
    ],
}


def write_manifest(tmp_path: Path, data: dict) -> Path:
    path = tmp_path / "manifest.yaml"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return path


def test_valid_manifest_has_no_errors(tmp_path: Path) -> None:
    path = write_manifest(tmp_path, VALID_MANIFEST)
    assert validate_manifest(path) == []


def test_rejects_wrong_rhythm(tmp_path: Path) -> None:
    data = yaml.safe_load(yaml.safe_dump(VALID_MANIFEST))
    data["pilot"]["rhythm"] = ["A"] * 7
    path = write_manifest(tmp_path, data)
    assert "pilot.rhythm must equal A,A,B,A,B,A,C" in validate_manifest(path)


def test_rejects_non_landscape_canvas(tmp_path: Path) -> None:
    data = yaml.safe_load(yaml.safe_dump(VALID_MANIFEST))
    data["pilot"]["canonical_canvas"] = "1080x1350"
    data["pilot"]["orientation"] = "portrait"
    path = write_manifest(tmp_path, data)
    errors = validate_manifest(path)
    assert "pilot.canonical_canvas must equal 1920x1080" in errors
    assert "pilot.orientation must equal landscape" in errors


def test_rejects_mismatched_card_level(tmp_path: Path) -> None:
    data = yaml.safe_load(yaml.safe_dump(VALID_MANIFEST))
    data["cards"][2]["level"] = "C"
    path = write_manifest(tmp_path, data)
    assert "card 03 level must be B" in validate_manifest(path)


def test_rejects_more_than_40_supporting_words(tmp_path: Path) -> None:
    data = yaml.safe_load(yaml.safe_dump(VALID_MANIFEST))
    data["cards"][0]["supporting_copy"] = " ".join(["слово"] * 41)
    path = write_manifest(tmp_path, data)
    assert "card 01 supporting_copy exceeds 40 words" in validate_manifest(path)
