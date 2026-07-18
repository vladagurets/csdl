from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


EXPECTED = {
    "runs": [40, 45, 50, 55],
    "success_rate": [72, 78, 84, 90],
    "median_review_minutes": [18, 16, 13, 10],
    "escaped_defects": [8, 6, 4, 2],
}

EXPECTED_PROMPT_CONTENT = {
    "17-kpi.yaml": {
        "headline": "НАДІЙНІСТЬ АГЕНТА · W4",
        "primary": "90% УСПІШНІСТЬ",
        "supporting": ["55 ЗАПУСКІВ", "10 ХВ МЕДІАНА РЕВ’Ю", "2 ПРОПУЩЕНІ ДЕФЕКТИ"],
        "source_label": "DEMO DATA",
    },
    "18-table.yaml": {
        "headline": "4 ТИЖНІ НАДІЙНОСТІ",
        "header": ["METRIC", "W1", "W2", "W3", "W4"],
        "rows": [
            ["ЗАПУСКИ", 40, 45, 50, 55],
            ["УСПІШНІСТЬ", "72%", "78%", "84%", "90%"],
            ["МЕДІАНА РЕВ’Ю", "18 ХВ", "16 ХВ", "13 ХВ", "10 ХВ"],
            ["ПРОПУЩЕНІ ДЕФЕКТИ", 8, 6, 4, 2],
        ],
        "source_label": "DEMO DATA",
    },
    "19-chart.yaml": {
        "headline": "УСПІШНІСТЬ ЗРОСТАЄ ЩОТИЖНЯ",
        "points": ["W1 · 72%", "W2 · 78%", "W3 · 84%", "W4 · 90%"],
        "source_label": "DEMO DATA",
    },
    "20-dashboard.yaml": {
        "headline": "AGENT RELIABILITY · W4",
        "metrics": ["90% УСПІШНІСТЬ", "55 ЗАПУСКІВ", "10 ХВ МЕДІАНА РЕВ’Ю", "2 ПРОПУЩЕНІ ДЕФЕКТИ"],
        "trend": ["W1 · 72%", "W2 · 78%", "W3 · 84%", "W4 · 90%"],
        "source_label": "DEMO DATA",
    },
}


def _validate_prompt_contracts(catalog_root: Path) -> list[str]:
    errors: list[str] = []
    for filename, expected_content in EXPECTED_PROMPT_CONTENT.items():
        path = catalog_root / "prompts" / filename
        if not path.exists():
            errors.append(f"missing analytical prompt: prompts/{filename}")
            continue
        try:
            prompt: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as error:
            errors.append(f"prompts/{filename} must be readable YAML: {error}")
            continue
        if prompt.get("content") != expected_content:
            errors.append(f"prompts/{filename} content must match the fixed dataset contract")
        if prompt.get("dataset") != "patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml":
            errors.append(f"prompts/{filename} must reference the fixed dataset")

    chart_path = catalog_root / "prompts/19-chart.yaml"
    if chart_path.exists():
        chart = yaml.safe_load(chart_path.read_text(encoding="utf-8"))
        quantitative = chart.get("composition", {}).get("quantitative_contract", {})
        if quantitative != {
            "x_order": ["W1", "W2", "W3", "W4"],
            "y_domain": [0, 100],
            "values": [72, 78, 84, 90],
            "interpolation": False,
        }:
            errors.append("prompts/19-chart.yaml quantitative_contract must preserve exact order, domain, and values")
    return errors


def validate_pattern_data(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"dataset must be readable YAML: {error}"]

    dataset = data.get("dataset", {})
    if dataset.get("id") != "agent-reliability-demo":
        errors.append("dataset.id must equal agent-reliability-demo")
    if dataset.get("status") != "fixed_demo_data":
        errors.append("dataset.status must equal fixed_demo_data")
    if dataset.get("weeks") != ["W1", "W2", "W3", "W4"]:
        errors.append("dataset.weeks must equal W1,W2,W3,W4")

    series = dataset.get("series", {})
    for name, values in EXPECTED.items():
        actual = series.get(name, {}).get("values")
        if actual != values:
            errors.append(f"{name} values must equal {','.join(str(value) for value in values)}")

    snapshot = dataset.get("canonical_snapshot", {})
    expected_snapshot = {
        "week": "W4",
        "runs": 55,
        "success_rate": 90,
        "median_review_minutes": 10,
        "escaped_defects": 2,
    }
    if snapshot != expected_snapshot:
        errors.append("dataset.canonical_snapshot must equal the W4 series values")

    constraints = data.get("constraints", {})
    if constraints.get("preserve_order") is not True:
        errors.append("constraints.preserve_order must be true")
    if constraints.get("zero_baseline_for_counts") is not True:
        errors.append("constraints.zero_baseline_for_counts must be true")
    if constraints.get("percent_domain") != [0, 100]:
        errors.append("constraints.percent_domain must equal 0,100")
    if constraints.get("interpolation") is not False:
        errors.append("constraints.interpolation must be false")
    if constraints.get("invented_values") is not False:
        errors.append("constraints.invented_values must be false")
    if constraints.get("source_label_required") != "DEMO DATA":
        errors.append("constraints.source_label_required must equal DEMO DATA")
    catalog_root = path.parent.parent
    if (catalog_root / "prompts").is_dir():
        errors.extend(_validate_prompt_contracts(catalog_root))
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_pattern_data.py DATASET")
        return 2
    errors = validate_pattern_data(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pattern data valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
