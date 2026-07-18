from pathlib import Path
import shutil

import yaml

from tools.validate_pattern_catalog import validate_pattern_catalog


ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "patterns/visual-dna-sprint-01"


def copy_catalog_contract(tmp_path: Path) -> Path:
    target = tmp_path / "patterns/visual-dna-sprint-01"
    target.parent.mkdir(parents=True)
    shutil.copytree(CATALOG, target)
    return target / "manifest.yaml"


def test_real_pattern_catalog_contract_is_valid() -> None:
    assert validate_pattern_catalog(CATALOG / "manifest.yaml") == []


def test_rejects_wrong_family_order(tmp_path: Path) -> None:
    manifest = copy_catalog_contract(tmp_path)
    data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    data["families"][0], data["families"][1] = data["families"][1], data["families"][0]
    manifest.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    assert "family order must match schema" in validate_pattern_catalog(manifest)


def test_rejects_canonical_level_outside_allowed_levels(tmp_path: Path) -> None:
    manifest = copy_catalog_contract(tmp_path)
    data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    data["families"][1]["canonical_level"] = "B"
    manifest.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    assert "family 02 canonical_level must be included in allowed_levels" in validate_pattern_catalog(manifest)


def test_rejects_missing_required_spec_section(tmp_path: Path) -> None:
    manifest = copy_catalog_contract(tmp_path)
    spec = manifest.parent / "specs/02-cover.md"
    spec.write_text(spec.read_text(encoding="utf-8").replace("## Canonical evidence", "## Evidence"), encoding="utf-8")
    assert "family 02 specification missing section: ## Canonical evidence" in validate_pattern_catalog(manifest)


def test_rejects_placeholder_in_prompt(tmp_path: Path) -> None:
    manifest = copy_catalog_contract(tmp_path)
    prompt = manifest.parent / "prompts/02-cover.yaml"
    prompt.write_text(prompt.read_text(encoding="utf-8") + "\nnotes: TBD\n", encoding="utf-8")
    assert "family 02 prompt contains forbidden placeholder: TBD" in validate_pattern_catalog(manifest)
