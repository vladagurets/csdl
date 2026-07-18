from copy import deepcopy
from pathlib import Path
import shutil

import yaml

from tools.build_analytical_mode import (
    apply_transformations,
    build_analytical_mode,
    derive_analytical_package,
)
from tools.validate_analytical_mode import validate_analytical_dataset


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "analytics/analytical-mode-v0.1"


def load_dataset(name: str) -> dict:
    return yaml.safe_load((LIBRARY / "datasets" / name).read_text(encoding="utf-8"))


def test_cumulative_and_rate_transformations_are_recomputed() -> None:
    waterfall = load_dataset("04-waterfall.yaml")["dataset"]
    derived = apply_transformations(waterfall)
    assert derived["cumulative"] == [100, 125, 115, 130, 130]

    map_data = load_dataset("07-map.yaml")["dataset"]
    derived = apply_transformations(map_data)
    assert derived["rate_per_100000"] == [4.0, 6.0, None]


def test_conversion_rate_uses_declared_previous_stage_denominator() -> None:
    dataset = load_dataset("06-funnel.yaml")["dataset"]
    derived = apply_transformations(dataset)
    assert derived["previous_stage_conversion"] == [100.0, 65.0, 60.0, 50.0]


def test_dataset_validator_rejects_null_without_missing_status() -> None:
    data = load_dataset("05-heatmap.yaml")
    data["dataset"]["missing_values"] = []
    errors = validate_analytical_dataset(data, LIBRARY)
    assert "dataset null requires one missing declaration: h5.success_rate" in errors


def test_dataset_validator_rejects_measure_without_unit() -> None:
    data = load_dataset("01-bar-positive-negative.yaml")
    del data["dataset"]["fields"][1]["unit"]
    errors = validate_analytical_dataset(data, LIBRARY)
    assert "quantitative measure must declare unit: variance" in errors


def test_derived_package_is_deterministic_and_preserves_dataset_identity() -> None:
    dataset = load_dataset("01-bar-positive-negative.yaml")
    source = {
        "id": "proof-bar",
        "family": "bar",
        "dataset": "datasets/01-bar-positive-negative.yaml",
        "analytical_intent": {
            "question": "Which categories changed positively or negatively?",
            "claim": "Signed variance crosses zero.",
        },
        "recipe": {"id": "019", "slug": "chart", "version": "0.5.0"},
        "encoding": {
            "marks": [{"type": "bar", "orientation": "vertical"}],
            "bindings": {"category": "category", "value": "variance"},
            "order": ["Reliability", "Review time", "Coverage", "Escaped defects"],
            "domains": {"value": [-10, 15]},
            "scales": {"value": "linear"},
            "zero_baseline": True,
            "direct_labels": True,
            "color_only_meaning": False,
            "redundant_encodings": ["label", "direction_from_zero"],
            "dual_axis": False,
            "decorative_field_area_percent": 0,
        },
        "component_instances": [
            {"id": "value-axis", "component": "Axis", "role": "quantitative"},
            {"id": "labels", "component": "Label", "role": "direct-label"},
        ],
        "relations": [
            {"subject": "labels", "type": "attached_to", "object": "value-axis"}
        ],
    }
    first = derive_analytical_package(source, dataset, LIBRARY)
    second = derive_analytical_package(deepcopy(source), deepcopy(dataset), LIBRARY)
    assert first == second
    assert first["dataset"]["id"] == "bar-variance-v1"
    assert first["dataset"]["version"] == "1.0.0"
    assert first["specification"]["records"] == dataset["dataset"]["records"]


def test_partial_builder_emits_deterministic_indexes(tmp_path: Path) -> None:
    target = tmp_path / "analytics/analytical-mode-v0.1"
    shutil.copytree(LIBRARY, target)
    outputs = build_analytical_mode(target, require_complete=False)
    first = {path.name: path.read_bytes() for path in outputs}
    outputs = build_analytical_mode(target, require_complete=False)
    second = {path.name: path.read_bytes() for path in outputs}
    assert first == second
    index = yaml.safe_load((target / "index.yaml").read_text(encoding="utf-8"))
    assert index["family_count"] == 10
    assert index["dataset_count"] == 10

