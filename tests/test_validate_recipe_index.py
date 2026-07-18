from pathlib import Path
import shutil

import yaml

from tools.build_recipe_library import build_recipe_library
from tools.validate_recipe_index import validate_recipe_index


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def copy_library(tmp_path: Path) -> Path:
    target = tmp_path / "recipes/recipe-library-v0.5"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    component_target = tmp_path / "components/component-library-v0.1"
    component_target.mkdir(parents=True)
    shutil.copy2(
        ROOT / "components/component-library-v0.1/manifest.yaml",
        component_target / "manifest.yaml",
    )
    manifest = yaml.safe_load((target / "manifest.yaml").read_text(encoding="utf-8"))
    for entry in manifest["recipes"]:
        record = yaml.safe_load((target / entry["record"]).read_text(encoding="utf-8"))
        for evidence in record["evidence"]:
            source = ROOT / evidence["path"]
            destination = tmp_path / evidence["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    return target


def test_partial_generated_outputs_validate(tmp_path: Path) -> None:
    target = copy_library(tmp_path)
    build_recipe_library(target, require_complete=False)
    assert validate_recipe_index(target, require_complete=False) == []


def test_rejects_index_drift(tmp_path: Path) -> None:
    target = copy_library(tmp_path)
    index_path, _, _ = build_recipe_library(target, require_complete=False)
    index = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    index["version"] = "wrong"
    index_path.write_text(yaml.safe_dump(index, sort_keys=False), encoding="utf-8")

    assert "index does not match the manifest-derived output" in validate_recipe_index(
        target, require_complete=False
    )
