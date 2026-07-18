from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


def _load_yaml(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} must be readable YAML: {error}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return data


def _contains_token(text: str, token: str) -> bool:
    return re.search(rf"\b{re.escape(token)}\b", text, flags=re.IGNORECASE) is not None


def _reference_paths(entries: Any, errors: list[str], label: str) -> list[str]:
    if not isinstance(entries, list):
        errors.append(f"{label} must be a list")
        return []
    paths: list[str] = []
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"{label} entry {index} must be a mapping")
            continue
        path = entry.get("path")
        role = entry.get("role")
        if not isinstance(path, str) or not path:
            errors.append(f"{label} entry {index} must define path")
            continue
        if not isinstance(role, str) or not role:
            errors.append(f"{label} entry {index} must define role")
        paths.append(path)
    return paths


def _validate_visual_authority(
    root: Path,
    catalog: dict[str, Any],
    schema: dict[str, Any],
    errors: list[str],
) -> dict[str, Any]:
    rules = schema.get("reference_authority_rules", {})
    expected_catalog_path = rules.get("catalog_path")
    authority_relative = catalog.get("visual_authority")
    if authority_relative != expected_catalog_path:
        errors.append(f"catalog.visual_authority must equal {expected_catalog_path}")
        return {}

    authority_path = root / str(authority_relative)
    if not authority_path.exists():
        errors.append(f"missing visual authority package: {authority_relative}")
        return {}
    authority = _load_yaml(authority_path, errors, "visual-authority.yaml")
    if not authority:
        return {}

    primary = _reference_paths(authority.get("primary_visual_authority"), errors, "primary_visual_authority")
    secondary = _reference_paths(
        authority.get("secondary_execution_reference"),
        errors,
        "secondary_execution_reference",
    )
    expected_primary = rules.get("primary", [])
    expected_secondary = rules.get("secondary", [])
    if primary != expected_primary:
        errors.append("primary visual authority paths must match schema order")
    if secondary != expected_secondary:
        errors.append("secondary execution reference paths must match schema order")
    if catalog.get("style_anchor") not in secondary:
        errors.append("catalog.style_anchor must be the secondary execution reference")

    repository_root = root.parents[1]
    for reference in primary + secondary:
        if not (repository_root / reference).exists():
            errors.append(f"missing visual authority reference: {reference}")

    generation = authority.get("generation_contract", {})
    if generation.get("attachment_order") != primary + secondary:
        errors.append("visual authority attachment_order must equal primary then secondary references")
    if generation.get("candidate_count") != 3 or generation.get("independent_calls") is not True:
        errors.append("visual authority generation contract must require three independent calls")

    actual_gates = authority.get("review_contract", {}).get("required_gates")
    if actual_gates != rules.get("required_review_gates"):
        errors.append("visual authority review gates must match schema")
    return authority


def validate_pattern_catalog(path: Path) -> list[str]:
    errors: list[str] = []
    root = path.parent
    schema_path = root / "schema.yaml"
    if not schema_path.exists():
        return ["missing catalog schema: schema.yaml"]

    data = _load_yaml(path, errors, "manifest.yaml")
    schema = _load_yaml(schema_path, errors, "schema.yaml")
    if errors:
        return errors

    catalog = data.get("catalog", {})
    families = data.get("families", [])
    required_catalog = set(schema.get("required_catalog_fields", []))
    missing_catalog = sorted(required_catalog - set(catalog)) if isinstance(catalog, dict) else sorted(required_catalog)
    if missing_catalog:
        errors.append("catalog missing fields: " + ",".join(missing_catalog))

    if catalog.get("canvas") != "1920x1080":
        errors.append("catalog.canvas must equal 1920x1080")
    if catalog.get("orientation") != "landscape":
        errors.append("catalog.orientation must equal landscape")
    if catalog.get("family_count") != 20:
        errors.append("catalog.family_count must equal 20")
    _validate_visual_authority(root, catalog, schema, errors)
    if not isinstance(families, list) or len(families) != 20:
        errors.append("families must contain exactly 20 entries")
        return errors

    expected_order = schema.get("family_order", [])
    if [family.get("slug") for family in families] != expected_order:
        errors.append("family order must match schema")
    expected_ids = [f"{index:02d}" for index in range(1, 21)]
    if [str(family.get("id", "")) for family in families] != expected_ids:
        errors.append("family ids must equal 01 through 20 in order")

    actual_distribution = Counter(family.get("canonical_level") for family in families)
    expected_distribution = catalog.get("canonical_distribution", {})
    if dict(actual_distribution) != expected_distribution:
        errors.append("canonical level distribution must match catalog.canonical_distribution")
    if expected_distribution != {"A": 13, "B": 6, "C": 1}:
        errors.append("catalog.canonical_distribution must equal A:13,B:6,C:1")

    required_family = set(schema.get("required_family_fields", []))
    enums = schema.get("enums", {})
    required_sections = schema.get("required_spec_sections", [])
    forbidden = schema.get("forbidden_placeholders", [])
    evidence_rules = schema.get("evidence_rules", {})

    for family in families:
        family_id = str(family.get("id", "??"))
        slug = str(family.get("slug", ""))
        missing = sorted(required_family - set(family))
        if missing:
            errors.append(f"family {family_id} missing fields: {','.join(missing)}")

        if family.get("wave") not in enums.get("wave", []):
            errors.append(f"family {family_id} wave is invalid")
        allowed_levels = family.get("allowed_levels", [])
        if not isinstance(allowed_levels, list) or not allowed_levels:
            errors.append(f"family {family_id} allowed_levels must be a non-empty list")
        elif any(level not in enums.get("level", []) for level in allowed_levels):
            errors.append(f"family {family_id} allowed_levels contains an invalid level")
        if family.get("canonical_level") not in allowed_levels:
            errors.append(f"family {family_id} canonical_level must be included in allowed_levels")
        if family.get("density") not in enums.get("density", []):
            errors.append(f"family {family_id} density is invalid")

        components = family.get("components", [])
        assembly = family.get("assembly_order", [])
        scenarios = family.get("scenarios", [])
        if not isinstance(components, list) or not components:
            errors.append(f"family {family_id} components must be a non-empty list")
        if not isinstance(assembly, list) or len(assembly) < 3:
            errors.append(f"family {family_id} assembly_order must contain at least 3 steps")
        if not isinstance(scenarios, list) or not scenarios:
            errors.append(f"family {family_id} scenarios must be a non-empty list")

        specification = root / str(family.get("specification", ""))
        prompt = root / str(family.get("prompt", ""))
        expected_spec = root / f"specs/{family_id}-{slug}.md"
        expected_prompt = root / f"prompts/{family_id}-{slug}.yaml"
        if specification != expected_spec:
            errors.append(f"family {family_id} specification path must follow schema")
        if prompt != expected_prompt:
            errors.append(f"family {family_id} prompt path must follow schema")

        if not specification.exists():
            errors.append(f"family {family_id} missing specification: {family.get('specification')}")
        else:
            spec_text = specification.read_text(encoding="utf-8")
            for section in required_sections:
                if section not in spec_text:
                    errors.append(f"family {family_id} specification missing section: {section}")
            for token in forbidden:
                if _contains_token(spec_text, str(token)):
                    errors.append(f"family {family_id} specification contains forbidden placeholder: {token}")

        if not prompt.exists():
            errors.append(f"family {family_id} missing prompt: {family.get('prompt')}")
        else:
            prompt_text = prompt.read_text(encoding="utf-8")
            prompt_data = _load_yaml(prompt, errors, f"family {family_id} prompt")
            if prompt_data.get("recipe") != family.get("name"):
                errors.append(f"family {family_id} prompt recipe must equal family name")
            canvas = prompt_data.get("canvas", {})
            if canvas.get("size") != "1920x1080" or canvas.get("orientation") != "landscape":
                errors.append(f"family {family_id} prompt canvas must be 1920x1080 landscape")
            expected_authority = schema.get("reference_authority_rules", {}).get("prompt_path")
            if prompt_data.get("visual_authority") != expected_authority:
                errors.append(f"family {family_id} prompt must use the catalog visual authority package")
            if "reference" in prompt_data:
                errors.append(f"family {family_id} prompt must not use a single legacy reference")
            for token in forbidden:
                if _contains_token(prompt_text, str(token)):
                    errors.append(f"family {family_id} prompt contains forbidden placeholder: {token}")

        evidence = family.get("evidence", {})
        mode = evidence.get("mode") if isinstance(evidence, dict) else None
        if mode not in enums.get("evidence_mode", []):
            errors.append(f"family {family_id} evidence mode is invalid")
        else:
            rule = evidence_rules.get(mode, {})
            missing_evidence = sorted(set(rule.get("required_fields", [])) - set(evidence))
            if missing_evidence:
                errors.append(f"family {family_id} evidence missing fields: {','.join(missing_evidence)}")
            expected_generation = rule.get("candidate_generation_required")
            if evidence.get("candidate_generation_required") is not expected_generation:
                errors.append(f"family {family_id} candidate_generation_required must be {str(expected_generation).lower()}")
            canonical = str(evidence.get("canonical_example", ""))
            if mode == "generated" and canonical != f"canonical/light/16x9/{family_id}-{slug}.png":
                errors.append(f"family {family_id} generated canonical path must follow schema")
            if mode == "pilot_reference" and not re.fullmatch(r"[0-9a-f]{64}", str(evidence.get("sha256", ""))):
                errors.append(f"family {family_id} pilot SHA-256 must contain 64 lowercase hex characters")

        acceptance = family.get("acceptance", {})
        for field in schema.get("acceptance_rules", {}).get("required_fields", []):
            if field not in acceptance:
                errors.append(f"family {family_id} acceptance missing field: {field}")
        if acceptance.get("candidate_count") != 3:
            errors.append(f"family {family_id} acceptance candidate_count must equal 3")

        serialized = yaml.safe_dump(family, allow_unicode=True, sort_keys=False)
        for token in forbidden:
            if _contains_token(serialized, str(token)):
                errors.append(f"family {family_id} manifest contains forbidden placeholder: {token}")

    analytical = [family for family in families if family.get("wave") == "analytical"]
    if [family.get("slug") for family in analytical] != ["kpi", "table", "chart", "dashboard"]:
        errors.append("analytical wave must contain KPI, Table, Chart, and Dashboard")
    for family in analytical:
        family_id = family["id"]
        if family.get("canonical_level") != "A" or family.get("allowed_levels") != ["A"]:
            errors.append(f"family {family_id} analytical prototype must be Level A only")
        if family.get("content", {}).get("dataset") != "data/agent-reliability-demo.yaml":
            errors.append(f"family {family_id} must reference the fixed analytical dataset")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_pattern_catalog.py MANIFEST")
        return 2
    errors = validate_pattern_catalog(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pattern catalog valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
