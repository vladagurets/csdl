from copy import deepcopy
from pathlib import Path

import yaml

from tools.validate_accessibility_mode import validate_accessibility_package


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "accessibility/night-mode-v0.1"


def package(name: str) -> dict:
    return yaml.safe_load((LIBRARY / "proofs/packages" / name).read_text(encoding="utf-8"))


def assert_error(value: dict, expected: str) -> None:
    assert expected in validate_accessibility_package(value, LIBRARY)


def test_rejects_indistinguishable_forecast_and_observed() -> None:
    value = package("05-forecast-uncertainty.yaml")
    forecast = next(item for item in value["semantic_encodings"] if item["meaning"] == "forecast")
    forecast["line_style"] = "solid"
    assert_error(value, "observed and forecast values require distinct line styles and direct labels")


def test_rejects_invisible_uncertainty() -> None:
    value = package("05-forecast-uncertainty.yaml")
    interval = next(item for item in value["semantic_encodings"] if item["meaning"] == "uncertainty")
    interval["visible"] = False
    assert_error(value, "uncertainty interval requires visible boundaries, label, type, and level")


def test_rejects_missing_heatmap_value_as_zero() -> None:
    value = package("06-heatmap-fallback.yaml")
    value["semantic_encodings"][0]["missing_label"] = "0"
    assert_error(value, "missing-value encoding must remain distinct from zero")


def test_rejects_hue_only_map_regions() -> None:
    value = package("07-normalized-map.yaml")
    value["semantic_encodings"][0]["redundant_carriers"] = ["direct_label"]
    assert_error(value, "map regions require pattern and direct-label fallback")


def test_rejects_color_only_network_direction() -> None:
    value = package("08-directed-network.yaml")
    direction = next(item for item in value["semantic_encodings"] if item["meaning"] == "direction")
    direction["redundant_carriers"] = ["direct_label"]
    assert_error(value, "network direction requires arrowhead and direct-label fallback")


def test_rejects_signal_lost_in_grayscale() -> None:
    value = package("09-monochrome-export.yaml")
    signal = next(item for item in value["semantic_encodings"] if item["meaning"] == "signal")
    signal["grayscale_contrast"] = 2.0
    assert_error(value, "Signal must survive grayscale with form and minimum contrast")


def test_rejects_prohibited_text_pair_and_signal_area_overflow() -> None:
    value = package("01-editorial-equivalence.yaml")
    value["text_elements"][0]["foreground"] = "signal.primary"
    assert_error(value, "prohibited foreground/background combination")

    value = deepcopy(package("01-editorial-equivalence.yaml"))
    value["semantic_encodings"][0]["area_percent"] = 9
    assert_error(value, "accessibility Signal area exceeds its existing semantic ceiling")
