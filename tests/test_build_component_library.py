from pathlib import Path
import shutil

import yaml

from tools.build_component_library import build_component_library


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "components/component-library-v0.1"


def test_builds_honest_partial_outputs(tmp_path: Path) -> None:
    target = tmp_path / "components/component-library-v0.1"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)

    index_path, compatibility_path = build_component_library(target, require_complete=False)

    index = yaml.safe_load(index_path.read_text(encoding="utf-8"))
    compatibility = yaml.safe_load(compatibility_path.read_text(encoding="utf-8"))
    manifest = yaml.safe_load((target / "manifest.yaml").read_text(encoding="utf-8"))
    expected_slugs = [component["slug"] for component in manifest["components"]]
    assert [component["slug"] for component in index["components"]] == expected_slugs
    assert [component["slug"] for component in compatibility["components"]] == expected_slugs
    assert len(compatibility["families"]) == 20
