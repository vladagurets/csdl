from pathlib import Path

import yaml

from tools.validate_pattern_index import validate_pattern_index


ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "patterns/visual-dna-sprint-01"


def test_incomplete_index_accepts_three_pilot_evidence_entries() -> None:
    assert validate_pattern_index(CATALOG, require_complete=False) == []


def test_strict_index_reports_seventeen_awaiting_families() -> None:
    errors = validate_pattern_index(CATALOG)
    assert "family 02 index evidence is incomplete" in errors
    assert len([error for error in errors if error.endswith("index evidence is incomplete")]) == 17


def test_rejects_hash_drift(tmp_path: Path) -> None:
    index = yaml.safe_load((CATALOG / "index.yaml").read_text(encoding="utf-8"))
    index["families"][0]["sha256"] = "0" * 64
    path = tmp_path / "index.yaml"
    path.write_text(yaml.safe_dump(index, allow_unicode=True, sort_keys=False), encoding="utf-8")
    errors = validate_pattern_index(CATALOG, require_complete=False, index_path=path)
    assert "family 01 index SHA-256 does not match canonical asset" in errors
