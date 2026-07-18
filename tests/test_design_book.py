from copy import deepcopy
from pathlib import Path
import shutil

import yaml

from tools.build_design_book import build_design_book
from tools.validate_design_book import (
    validate_design_book,
    validate_negative_fixture,
)


ROOT = Path(__file__).parents[1]
BOOK = ROOT / "cookbook/design-book-v1.0"


def load(relative: str) -> dict:
    return yaml.safe_load((BOOK / relative).read_text(encoding="utf-8"))


def test_manifest_locks_bilingual_a4_landscape_32_page_contract() -> None:
    manifest = load("manifest.yaml")
    publication = manifest["publication"]
    assert publication["page_count"] == 32
    assert len(manifest["pages"]) == 32
    assert publication["editorial_language"] == "uk"
    assert publication["terminology_language"] == "en"
    assert publication["format"]["name"] == "ISO A4 landscape"
    assert publication["format"]["width_mm"] == 297
    assert publication["format"]["height_mm"] == 210
    assert publication["public_release"] is False
    assert set(manifest["required_topics"]) == {
        "philosophy",
        "constructive-signal",
        "quiet-modular",
        "expression-levels",
        "semantic-color",
        "typography",
        "visual-grammar",
        "components",
        "recipes",
        "prompt-dsl-v0.5",
        "analytical-mode-v0.1",
        "accessibility",
        "reference-hierarchy",
        "provenance",
        "why-do-dont",
        "publishing-preflight",
    }


def test_terminology_registry_matches_closed_public_contracts() -> None:
    registry = load("terminology.yaml")
    component_manifest = yaml.safe_load(
        (ROOT / "components/component-library-v0.1/manifest.yaml").read_text(encoding="utf-8")
    )
    recipe_manifest = yaml.safe_load(
        (ROOT / "recipes/recipe-library-v0.5/manifest.yaml").read_text(encoding="utf-8")
    )
    assert [item["name"] for item in registry["components"]] == [
        item["name"] for item in component_manifest["components"]
    ]
    assert [(item["id"], item["name"]) for item in registry["recipes"]] == [
        (str(item["id"]).zfill(3), item["name"]) for item in recipe_manifest["recipes"]
    ]
    assert len(registry["components"]) == 15
    assert len(registry["recipes"]) == 23
    assert registry["registry"]["canonical_identifiers_are_translated"] is False
    assert registry["retired_or_forbidden_public_names"] == ["Container"]


def test_source_contract_is_complete_without_outputs() -> None:
    assert validate_design_book(BOOK, require_outputs=False) == []


def test_builder_is_byte_deterministic_and_text_extractable(tmp_path: Path) -> None:
    target = tmp_path / "cookbook/design-book-v1.0"
    shutil.copytree(BOOK, target, ignore=shutil.ignore_patterns("output"))
    for name in [
        "components",
        "recipes",
        "analytics",
        "accessibility",
        "patterns",
        "pilots",
        "references",
        "docs",
        "specs",
    ]:
        shutil.copytree(ROOT / name, tmp_path / name)
    for name in ["DECISIONS.md", "AGENTS.md"]:
        shutil.copy2(ROOT / name, tmp_path / name)

    first = build_design_book(target)
    first_bytes = {path.relative_to(target).as_posix(): path.read_bytes() for path in first}
    second = build_design_book(target)
    second_bytes = {path.relative_to(target).as_posix(): path.read_bytes() for path in second}
    assert first_bytes == second_bytes

    report = yaml.safe_load((target / "output/build-report.yaml").read_text(encoding="utf-8"))
    assert report["page_count"] == 32
    assert report["deterministic"] is True
    assert report["overflow_pages"] == []
    assert report["missing_glyph_pages"] == []
    assert report["accepted_raster_count"] == 60
    assert report["accepted_raster_mismatches"] == []
    assert (target / "output/pdf/csdl-cookbook-design-book-v1.0.pdf").read_bytes().startswith(b"%PDF-1.7")
    extracted = (target / "output/extracted-text.txt").read_text(encoding="utf-8")
    assert "Constructive Signal" in extracted
    assert "Publishing preflight" in extracted
    assert "Аналітич" in extracted or "Analytical Mode" in extracted
    assert validate_design_book(target, require_outputs=True) == []


def test_all_negative_fixtures_return_their_exact_error() -> None:
    expected = load("fixtures/negative/expected-errors.yaml")["fixtures"]
    fixture_dir = BOOK / "fixtures/negative"
    paths = sorted(path for path in fixture_dir.glob("*.yaml") if path.name != "expected-errors.yaml")
    assert len(paths) == 12
    for path in paths:
        assert validate_negative_fixture(path, BOOK) == expected[path.name]
