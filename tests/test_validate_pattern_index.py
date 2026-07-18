import subprocess
import sys
from pathlib import Path

import yaml

from tools.validate_pattern_index import validate_pattern_index


ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "patterns/visual-dna-sprint-01"


def test_cli_entrypoint_runs_from_repository_root() -> None:
    result = subprocess.run(
        [sys.executable, "tools/validate_pattern_index.py", str(CATALOG)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.strip() == "pattern index valid"


def test_incomplete_index_accepts_three_pilot_evidence_entries() -> None:
    assert validate_pattern_index(CATALOG, require_complete=False) == []


def test_strict_index_reports_current_awaiting_families() -> None:
    errors = validate_pattern_index(CATALOG)
    index = yaml.safe_load((CATALOG / "index.yaml").read_text(encoding="utf-8"))
    expected = {
        f"family {str(family['id']).zfill(2)} index evidence is incomplete"
        for family in index["families"]
        if family.get("status") == "awaiting_generation"
    }
    assert set(errors) == expected


def test_rejects_hash_drift(tmp_path: Path) -> None:
    index = yaml.safe_load((CATALOG / "index.yaml").read_text(encoding="utf-8"))
    index["families"][0]["sha256"] = "0" * 64
    path = tmp_path / "index.yaml"
    path.write_text(yaml.safe_dump(index, allow_unicode=True, sort_keys=False), encoding="utf-8")
    errors = validate_pattern_index(CATALOG, require_complete=False, index_path=path)
    assert "family 01 index SHA-256 does not match canonical asset" in errors
