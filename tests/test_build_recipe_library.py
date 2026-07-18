from pathlib import Path
import shutil

import yaml

from tools.build_recipe_library import build_recipe_library


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def test_builds_honest_empty_outputs_in_incomplete_mode(tmp_path: Path) -> None:
    target = tmp_path / "recipes/recipe-library-v0.5"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)

    outputs = build_recipe_library(target, require_complete=False)
    index = yaml.safe_load(outputs[0].read_text(encoding="utf-8"))
    compatibility = yaml.safe_load(outputs[1].read_text(encoding="utf-8"))
    selection = yaml.safe_load(outputs[2].read_text(encoding="utf-8"))

    assert index["recipe_count"] == 0
    assert compatibility["recipes"] == []
    assert len(compatibility["families"]) == 20
    assert selection["scenarios"] == []
