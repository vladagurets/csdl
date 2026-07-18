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


def test_complete_outputs_cover_fifteen_components_by_twenty_families() -> None:
    index = yaml.safe_load((LIBRARY / "index.yaml").read_text(encoding="utf-8"))
    compatibility = yaml.safe_load((LIBRARY / "compatibility.yaml").read_text(encoding="utf-8"))

    assert index["component_count"] == 15
    assert len(compatibility["components"]) == 15
    assert all(len(row["families"]) == 20 for row in compatibility["components"])
    legend = next(row for row in compatibility["components"] if row["slug"] == "legend")
    assert legend["families"]["chart"] == "conditional"
    assert legend["families"]["dashboard"] == "conditional"
    assert set(legend["families"].values()) == {"conditional", "incompatible"}
