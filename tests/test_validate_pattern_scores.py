from pathlib import Path

from tools.validate_pattern_scores import HEADER, validate_pattern_scores


def test_incomplete_scores_allow_no_rows(tmp_path: Path) -> None:
    path = tmp_path / "scores.csv"
    path.write_text(HEADER + "\n", encoding="utf-8")
    assert validate_pattern_scores(path, require_complete=False) == []


def test_strict_scores_require_all_twenty_families(tmp_path: Path) -> None:
    path = tmp_path / "scores.csv"
    path.write_text(HEADER + "\n", encoding="utf-8")
    assert "scores.csv family ids must equal 01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20" in validate_pattern_scores(path)


def test_rejects_zero_or_placeholder_score(tmp_path: Path) -> None:
    path = tmp_path / "scores.csv"
    path.write_text(HEADER + "\n02,5,5,4,5,0,5,5\n", encoding="utf-8")
    errors = validate_pattern_scores(path, require_complete=False)
    assert "family 02 restraint must be between 1 and 5" in errors
    assert "family 02 restraint must be at least 4" in errors
