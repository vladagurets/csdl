from pathlib import Path
import shutil

import yaml

from tools.validate_component_proofs import validate_component_proofs


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "components/component-library-v0.1"


def copy_library_contract(tmp_path: Path) -> Path:
    target = tmp_path / "components/component-library-v0.1"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    return target


def test_infrastructure_has_no_required_proofs_in_incomplete_mode() -> None:
    assert validate_component_proofs(LIBRARY, require_complete=False) == []


def test_strict_mode_requires_three_composition_proofs() -> None:
    assert "proofs must contain exactly editorial, structural, and analytical" in validate_component_proofs(
        LIBRARY
    )


def test_rejects_ad_hoc_layout_primitive(tmp_path: Path) -> None:
    root = copy_library_contract(tmp_path)
    proofs = root / "proofs"
    proofs.mkdir()
    proof = {
        "id": "01",
        "mode": "editorial",
        "family": "hero",
        "expression": "A",
        "evidence": "README.md",
        "content": {"headline": "ONE IDEA"},
        "instances": [],
        "relations": [],
        "layout": {"columns": 12},
    }
    (proofs / "01-editorial.yaml").write_text(
        yaml.safe_dump(proof, sort_keys=False),
        encoding="utf-8",
    )

    errors = validate_component_proofs(root, require_complete=False)

    assert "proof 01 contains forbidden composition key: layout" in errors
