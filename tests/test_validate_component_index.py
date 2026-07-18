from pathlib import Path
import shutil

import yaml

from tools.build_component_library import build_component_library
from tools.validate_component_index import validate_component_index


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "components/component-library-v0.1"


def copy_library_with_evidence(tmp_path: Path) -> Path:
    target = tmp_path / "components/component-library-v0.1"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    for relative in ["DECISIONS.md", "specs/2026-07-17-csdl-v0.1-design.md"]:
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, destination)
    pattern_target = tmp_path / "patterns/visual-dna-sprint-01"
    pattern_target.mkdir(parents=True)
    shutil.copy2(ROOT / "patterns/visual-dna-sprint-01/manifest.yaml", pattern_target / "manifest.yaml")
    for directory in ["prompts", "specs", "evaluation"]:
        shutil.copytree(
            ROOT / f"patterns/visual-dna-sprint-01/{directory}",
            pattern_target / directory,
        )
    authority = tmp_path / "references/canonical/foundation-patterns-v0.1.png"
    authority.parent.mkdir(parents=True)
    shutil.copy2(ROOT / "references/canonical/foundation-patterns-v0.1.png", authority)
    return target


def test_partial_generated_outputs_validate(tmp_path: Path) -> None:
    target = copy_library_with_evidence(tmp_path)
    build_component_library(target, require_complete=False)

    assert validate_component_index(target, require_complete=False) == []


def test_rejects_index_drift(tmp_path: Path) -> None:
    target = copy_library_with_evidence(tmp_path)
    index_path, _ = build_component_library(target, require_complete=False)
    data = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    data["version"] = "wrong"
    index_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    assert "index does not match the manifest-derived output" in validate_component_index(
        target, require_complete=False
    )
