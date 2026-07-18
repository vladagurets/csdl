from pathlib import Path
import shutil

import yaml

from tools.validate_pattern_data import validate_pattern_data


ROOT = Path(__file__).parents[1]
DATASET = ROOT / "patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml"


def test_real_demo_dataset_is_valid() -> None:
    assert validate_pattern_data(DATASET) == []


def test_rejects_changed_analytical_value(tmp_path: Path) -> None:
    data = yaml.safe_load(DATASET.read_text(encoding="utf-8"))
    data["dataset"]["series"]["success_rate"]["values"][3] = 91
    path = tmp_path / "data.yaml"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    assert "success_rate values must equal 72,78,84,90" in validate_pattern_data(path)


def test_rejects_missing_demo_source_label(tmp_path: Path) -> None:
    data = yaml.safe_load(DATASET.read_text(encoding="utf-8"))
    data["constraints"]["source_label_required"] = "SOURCE"
    path = tmp_path / "data.yaml"
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    assert "constraints.source_label_required must equal DEMO DATA" in validate_pattern_data(path)


def test_rejects_prompt_value_drift(tmp_path: Path) -> None:
    catalog = tmp_path / "patterns/visual-dna-sprint-01"
    shutil.copytree(DATASET.parent.parent, catalog)
    prompt = catalog / "prompts/19-chart.yaml"
    prompt.write_text(prompt.read_text(encoding="utf-8").replace("W4 · 90%", "W4 · 91%"), encoding="utf-8")
    assert "prompts/19-chart.yaml content must match the fixed dataset contract" in validate_pattern_data(
        catalog / "data/agent-reliability-demo.yaml"
    )
