from pathlib import Path
import shutil

from tools.validate_pattern_review import validate_pattern_review


ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "patterns/visual-dna-sprint-01"


def copy_catalog(tmp_path: Path) -> Path:
    target = tmp_path / "visual-dna-sprint-01"
    shutil.copytree(CATALOG, target)
    return target


def test_incomplete_rebaselined_review_accepts_pilot_evidence() -> None:
    assert validate_pattern_review(CATALOG, require_complete=False) == []


def test_rejects_score_for_superseded_generated_review(tmp_path: Path) -> None:
    catalog = copy_catalog(tmp_path)
    scores = catalog / "evaluation/scores.csv"
    scores.write_text(scores.read_text(encoding="utf-8") + "02,5,5,5,5,5,5,5\n", encoding="utf-8")
    assert "family 02 superseded review cannot have an accepted score" in validate_pattern_review(
        catalog,
        require_complete=False,
    )


def test_rejects_generated_review_without_authority_gates(tmp_path: Path) -> None:
    catalog = copy_catalog(tmp_path)
    scores = catalog / "evaluation/scores.csv"
    scores.write_text(scores.read_text(encoding="utf-8") + "02,5,5,5,5,5,5,5\n", encoding="utf-8")
    review = catalog / "evaluation/review.md"
    review.write_text(
        review.read_text(encoding="utf-8").replace(
            "### 02 Cover — first generated pass superseded",
            "### 02 Cover — regenerated example accepted",
        ),
        encoding="utf-8",
    )
    errors = validate_pattern_review(catalog, require_complete=False)
    assert "family 02 generated review missing: Primary-authority comparison: pass" in errors
    assert "family 02 generated review missing: Series contact-sheet review: pass" in errors
