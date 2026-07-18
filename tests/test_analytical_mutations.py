from copy import deepcopy
from pathlib import Path

import yaml

from tools.build_analytical_mode import derive_analytical_package
from tools.validate_analytical_mode import validate_analytical_package


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "analytics/analytical-mode-v0.1"


def valid_bar_package() -> dict:
    dataset = yaml.safe_load(
        (LIBRARY / "datasets/01-bar-positive-negative.yaml").read_text(encoding="utf-8")
    )
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
            {"id": "category-axis", "component": "Axis", "role": "sequence"},
            {"id": "value-axis", "component": "Axis", "role": "quantitative"},
            {"id": "labels", "component": "Label", "role": "direct-label"},
            {"id": "signal", "component": "Signal", "role": "positive-focus"},
        ],
        "relations": [
            {"subject": "labels", "type": "attached_to", "object": "value-axis"},
            {"subject": "signal", "type": "highlights", "object": "value-axis"},
        ],
    }
    return derive_analytical_package(source, dataset, LIBRARY)


def assert_error(package: dict, expected: str) -> None:
    assert expected in validate_analytical_package(package, LIBRARY)


def test_valid_bar_package_passes() -> None:
    assert validate_analytical_package(valid_bar_package(), LIBRARY) == []


def test_rejects_truncated_bar_baseline() -> None:
    package = valid_bar_package()
    package["encoding"]["zero_baseline"] = False
    assert_error(package, "bar encoding requires a zero baseline")


def test_rejects_undeclared_log_scale() -> None:
    package = valid_bar_package()
    package["encoding"]["scales"]["value"] = "log"
    assert_error(package, "log scale requires explicit declaration")


def test_rejects_dual_axis_without_exception() -> None:
    package = valid_bar_package()
    package["encoding"]["dual_axis"] = True
    assert_error(package, "dual axis requires an explicit exception")


def test_rejects_color_only_meaning() -> None:
    package = valid_bar_package()
    package["encoding"]["color_only_meaning"] = True
    package["encoding"]["redundant_encodings"] = []
    assert_error(package, "color cannot be the sole carrier of meaning")


def test_rejects_undeclared_layout_key() -> None:
    package = valid_bar_package()
    package["encoding"]["layout"] = {"columns": 4}
    assert_error(package, "analytical package contains forbidden key: layout")


def test_rejects_mutated_specification_value() -> None:
    package = valid_bar_package()
    package["specification"]["records"][0]["variance"] = 999
    assert_error(package, "analytical specification records must match canonical dataset")


def test_rejects_unsupported_mark_component_combination() -> None:
    package = valid_bar_package()
    package["component_instances"][0]["component"] = "Bridge"
    assert_error(package, "component Bridge is incompatible with analytical family bar")


def test_rejects_nondeterministic_provenance() -> None:
    package = deepcopy(valid_bar_package())
    package["provenance"]["deterministic"] = False
    assert_error(package, "analytical package must declare deterministic output")

