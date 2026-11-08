from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


def find_forbidden_keys(value: Any, forbidden: set[str]) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in forbidden:
                found.add(str(key).lower())
            found.update(find_forbidden_keys(child, forbidden))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_keys(child, forbidden))
    return found


def contains_token(text: str, token: str) -> bool:
    return re.search(rf"\b{re.escape(token)}\b", text, flags=re.IGNORECASE) is not None


def relation_is_allowed(
    subject: dict[str, Any],
    target: dict[str, Any],
    relation_type: str,
) -> bool:
    subject_name = subject.get("name")
    target_name = target.get("name")
    for entry in subject.get("relations", {}).get("allowed", []):
        if (
            entry.get("type") == relation_type
            and entry.get("direction") in {"outbound", "either"}
            and entry.get("target") in {target_name, "any"}
        ):
            return True
    for entry in target.get("relations", {}).get("allowed", []):
        if (
            entry.get("type") == relation_type
            and entry.get("direction") in {"inbound", "either"}
            and entry.get("target") in {subject_name, "any"}
        ):
            return True
    return False


def load_yaml_mapping(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} must be readable YAML: {error}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return data
