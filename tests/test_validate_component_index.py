from pathlib import Path
import shutil

import yaml

from tools.build_component_library import build_component_library
from tools.validate_component_index import validate_component_index


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "components/component-library-v0.1"


def test_partial_generated_outputs_validate(tmp_path: Path) -> None:
    target = tmp_path / "components/component-library-v0.1"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    build_component_library(target, require_complete=False)

    assert validate_component_index(target, require_complete=False) == []


def test_rejects_index_drift(tmp_path: Path) -> None:
    target = tmp_path / "components/component-library-v0.1"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    index_path, _ = build_component_library(target, require_complete=False)
    data = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    data["version"] = "wrong"
    index_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    assert "index does not match the manifest-derived output" in validate_component_index(
        target, require_complete=False
    )
