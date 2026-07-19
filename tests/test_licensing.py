from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LICENSE_HASHES = {
    "PolyForm-Noncommercial-1.0.0.md": (
        "c0ea4a896d2c8c394b29f9427589996db826cd501c512279ff0ed3ef48fabbe5"
    ),
    "CC-BY-NC-SA-4.0.txt": (
        "1349a4b6148492b44f629e64eed676612e234fe9a839e4f3b277c1482c8849f1"
    ),
}


def test_standard_license_texts_are_pinned() -> None:
    for filename, expected_hash in LICENSE_HASHES.items():
        payload = (ROOT / "LICENSES" / filename).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == expected_hash


def test_d034_scope_and_owner_are_consistent() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    decisions = (ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    normalized_license = " ".join(license_text.split())

    for text in (license_text, notice, decisions, readme):
        assert "Vladyslav Ohirenko" in text

    assert "Required Notice: Copyright 2026 Vladyslav Ohirenko" in license_text
    assert "PolyForm Noncommercial License 1.0.0" in normalized_license
    assert (
        "Creative Commons Attribution-NonCommercial-ShareAlike 4.0"
        in normalized_license
    )
    assert "commercial use requires a separate written license" in normalized_license.lower()
    assert "D-034" in decisions
    assert "not OSI open source" in readme


def test_single_owner_contribution_and_trademark_boundaries_exist() -> None:
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    trademarks = (ROOT / "TRADEMARKS.md").read_text(encoding="utf-8")

    assert "written copyright assignment" in contributing
    assert "Unsolicited pull requests will not be merged" in contributing
    assert "No trademark registration is asserted" in trademarks
    assert "do not grant trademark rights" in trademarks
