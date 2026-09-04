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


def copy_library_with_proof_evidence(tmp_path: Path) -> Path:
    target = copy_library_contract(tmp_path)
    repository_root = target.parents[1]
    for relative in [
        "patterns/visual-dna-sprint-01/canonical/light/16x9/3.png",
        "patterns/visual-dna-sprint-01/canonical/light/16x9/9.png",
        "patterns/visual-dna-sprint-01/canonical/light/16x9/16.png",
        "patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml",
    ]:
        destination = repository_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, destination)
    return target


def test_complete_composition_proofs_validate() -> None:
    assert validate_component_proofs(LIBRARY) == []

    modes = [
        yaml.safe_load(path.read_text(encoding="utf-8"))["mode"]
        for path in sorted((LIBRARY / "proofs").glob("*.yaml"))
    ]
    assert modes == ["editorial", "structural", "analytical"]


def test_strict_mode_requires_three_composition_proofs(tmp_path: Path) -> None:
    root = copy_library_with_proof_evidence(tmp_path)
    (root / "proofs/03-analytical.yaml").unlink()

    assert "proofs must contain exactly editorial, structural, and analytical" in validate_component_proofs(root)


def test_rejects_ad_hoc_layout_primitive(tmp_path: Path) -> None:
    root = copy_library_contract(tmp_path)
    proofs = root / "proofs"
    shutil.rmtree(proofs)
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


def test_rejects_relation_not_allowed_by_component_contracts(tmp_path: Path) -> None:
    root = copy_library_with_proof_evidence(tmp_path)
    path = root / "proofs/03-analytical.yaml"
    proof = yaml.safe_load(path.read_text(encoding="utf-8"))
    proof["relations"][0]["type"] = "repeats"
    path.write_text(yaml.safe_dump(proof, allow_unicode=True, sort_keys=False), encoding="utf-8")

    errors = validate_component_proofs(root)

    assert "proof 03 relation 1 is not allowed by component contracts" in errors


def test_rejects_quantitative_value_distortion(tmp_path: Path) -> None:
    root = copy_library_with_proof_evidence(tmp_path)
    path = root / "proofs/03-analytical.yaml"
    proof = yaml.safe_load(path.read_text(encoding="utf-8"))
    proof["quantitative_contract"]["values"][-1] = 91
    path.write_text(yaml.safe_dump(proof, allow_unicode=True, sort_keys=False), encoding="utf-8")

    errors = validate_component_proofs(root)

    assert "proof 03 quantitative values must match fixed dataset" in errors
