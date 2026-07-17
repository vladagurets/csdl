from pathlib import Path

from tools.validate_scores import validate_scores


HEADER = "card,clarity,mobile_readability,memorability,csdl_identity,restraint,text_fidelity,semantic_integrity\n"


def test_accepts_publishable_scores(tmp_path: Path) -> None:
    path = tmp_path / "scores.csv"
    row = "01,5,5,4,4,5,5,4\n"
    path.write_text(HEADER + row, encoding="utf-8")
    assert validate_scores(path, expected_cards={"01"}) == []


def test_rejects_critical_score_below_five(tmp_path: Path) -> None:
    path = tmp_path / "scores.csv"
    row = "01,4,5,5,5,5,5,5\n"
    path.write_text(HEADER + row, encoding="utf-8")
    assert "card 01 clarity must equal 5" in validate_scores(path, expected_cards={"01"})


def test_rejects_average_below_threshold(tmp_path: Path) -> None:
    path = tmp_path / "scores.csv"
    row = "01,5,5,3,4,4,5,4\n"
    path.write_text(HEADER + row, encoding="utf-8")
    assert "card 01 average must be at least 4.4" in validate_scores(path, expected_cards={"01"})
