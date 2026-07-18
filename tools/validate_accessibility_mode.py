from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


EXPECTED_PROFILES = ["light", "night", "monochrome", "projector"]
EXPECTED_COMPONENTS = [
    "Anchor",
    "Signal",
    "Field",
    "Frame",
    "Cluster",
    "Vector",
    "Divider",
    "Node",
    "Loop",
    "Collision",
    "Bridge",
    "Axis",
    "Pulse",
    "Label",
    "Legend",
]
EXPECTED_ANALYTICAL_FAMILIES = [
    "bar",
    "line",
    "scatterplot",
    "waterfall",
    "heatmap",
    "funnel",
    "map",
    "network",
    "table",
    "dashboard",
]


def _channel(value: int) -> float:
    normalized = value / 255
    return (
        normalized / 12.92
        if normalized <= 0.04045
        else ((normalized + 0.055) / 1.055) ** 2.4
    )


def relative_luminance(value: str) -> float:
    if not re.fullmatch(r"#[0-9A-F]{6}", value):
        raise ValueError(f"invalid sRGB token: {value}")
    red, green, blue = (_channel(int(value[index : index + 2], 16)) for index in (1, 3, 5))
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(first: str, second: str) -> float:
    lighter, darker = sorted(
        (relative_luminance(first), relative_luminance(second)), reverse=True
    )
    return (lighter + 0.05) / (darker + 0.05)


def _load(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} must be readable YAML: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return value


def validate_accessibility_library(
    root: Path, require_complete: bool = True
) -> list[str]:
    errors: list[str] = []
    manifest = _load(root / "manifest.yaml", errors, "accessibility manifest")
    token_schema = _load(root / "token-schema.yaml", errors, "token schema")
    proof_schema = _load(root / "proof-schema.yaml", errors, "proof schema")
    tokens = _load(root / "contracts/tokens.yaml", errors, "token contract")
    contrast = _load(root / "contracts/contrast.yaml", errors, "contrast contract")
    fallbacks = _load(root / "contracts/fallbacks.yaml", errors, "fallback contract")
    compatibility = _load(
        root / "contracts/compatibility.yaml", errors, "compatibility source"
    )
    if errors:
        return errors

    library = manifest.get("library", {})
    if library.get("id") != "night-mode-v0.1" or library.get("version") != "0.1.0":
        errors.append("accessibility manifest identity/version is invalid")
    if library.get("kind") != "accessibility-extension":
        errors.append("accessibility manifest kind is invalid")
    if library.get("prompt_dsl_compatibility") != "0.5":
        errors.append("accessibility manifest must preserve Prompt DSL v0.5")
    if library.get("public_component_count") != 15:
        errors.append("accessibility manifest must preserve fifteen public components")
    if library.get("public_recipe_count") != 23:
        errors.append("accessibility manifest must preserve 23 public recipes")
    if library.get("analytical_family_count") != 10:
        errors.append("accessibility manifest must preserve ten analytical families")
    if manifest.get("profile_order") != EXPECTED_PROFILES:
        errors.append("accessibility profile order must match the four-profile contract")
    if manifest.get("public_components") != EXPECTED_COMPONENTS:
        errors.append("accessibility public components must equal D-029")

    if token_schema.get("profiles") != EXPECTED_PROFILES:
        errors.append("token schema profiles must match the manifest")
    required_tokens = set(token_schema.get("required_token_roles", []))
    profile_documents = tokens.get("profiles", {})
    if list(profile_documents) != EXPECTED_PROFILES:
        errors.append("token contract profiles must use canonical order")
    contrast_profiles = contrast.get("profiles", {})
    if list(contrast_profiles) != EXPECTED_PROFILES:
        errors.append("contrast profiles must use canonical order")

    for profile_name in EXPECTED_PROFILES:
        profile = profile_documents.get(profile_name, {})
        values = profile.get("tokens", {})
        missing = sorted(required_tokens - set(values))
        if missing:
            errors.append(
                f"{profile_name} token profile missing roles: {','.join(missing)}"
            )
        unknown = sorted(set(values) - required_tokens)
        if unknown:
            errors.append(
                f"{profile_name} token profile has unknown roles: {','.join(unknown)}"
            )
        for role, value in values.items():
            try:
                relative_luminance(value)
            except (TypeError, ValueError):
                errors.append(f"{profile_name} token is not canonical sRGB: {role}")
        thresholds = contrast_profiles.get(profile_name, {})
        for pairing in profile.get("allowed_pairings", []):
            foreground = pairing.get("foreground")
            background = pairing.get("background")
            if foreground not in values or background not in values:
                errors.append(f"{profile_name} pairing references undeclared token")
                continue
            minimum_key = (
                "minimum_text_contrast"
                if pairing.get("kind") == "text"
                else "minimum_non_text_contrast"
            )
            minimum = thresholds.get(minimum_key)
            if minimum is None:
                errors.append(f"{profile_name} contrast threshold is missing")
                continue
            if contrast_ratio(values[foreground], values[background]) < minimum:
                errors.append(
                    f"{profile_name} allowed pairing fails {minimum_key}: "
                    f"{foreground}/{background}"
                )
        expected_critical = thresholds.get("critical_stroke_px")
        if profile.get("stroke_widths", {}).get("critical_px") != expected_critical:
            errors.append(f"{profile_name} critical stroke width must match contrast contract")

    if proof_schema.get("kind") != "accessibility-proof-schema":
        errors.append("proof schema identity is invalid")
    if fallbacks.get("color_vision", {}).get("color_only_meaning_allowed") is not False:
        errors.append("fallback contract must forbid color-only meaning")
    if fallbacks.get("monochrome", {}).get("tone_only_meaning_allowed") is not False:
        errors.append("monochrome contract must forbid tone-only meaning")

    component_names = [entry.get("name") for entry in compatibility.get("components", [])]
    if component_names != EXPECTED_COMPONENTS:
        errors.append("compatibility source components must equal D-029")
    recipes = compatibility.get("recipes", [])
    if len(recipes) != 23 or [entry.get("id") for entry in recipes] != [
        f"{index:03d}" for index in range(1, 24)
    ]:
        errors.append("compatibility source recipes must equal D-030")
    prompt = compatibility.get("prompt_dsl", {})
    if prompt.get("version") != "0.5" or prompt.get("changed") is not False:
        errors.append("compatibility source must keep Prompt DSL v0.5 unchanged")
    analytical = compatibility.get("analytical_mode", {})
    family_names = [entry.get("name") for entry in analytical.get("families", [])]
    if family_names != EXPECTED_ANALYTICAL_FAMILIES:
        errors.append("compatibility source must cover all Analytical Mode families")
    if analytical.get("quantitative_invariants_preserved") is not True:
        errors.append("compatibility source must preserve quantitative invariants")

    repository_root = root.parents[1]
    component_manifest = _load(
        repository_root / str(library.get("component_library", "")),
        errors,
        "component dependency manifest",
    )
    recipe_manifest = _load(
        repository_root / str(library.get("recipe_library", "")),
        errors,
        "recipe dependency manifest",
    )
    analytical_manifest = _load(
        repository_root / str(library.get("analytical_mode", "")),
        errors,
        "analytical dependency manifest",
    )
    prompt_schema = _load(
        repository_root / "recipes/recipe-library-v0.5/prompt-dsl-v0.5.schema.yaml",
        errors,
        "Prompt DSL dependency schema",
    )
    dependency_components = component_manifest.get("vocabulary", {}).get(
        "components", []
    )
    if dependency_components != EXPECTED_COMPONENTS:
        errors.append("component dependency must remain exactly D-029")
    if len(recipe_manifest.get("recipes", [])) != 23:
        errors.append("recipe dependency must remain exactly D-030")
    if str(prompt_schema.get("version")) != "0.5":
        errors.append("Prompt DSL dependency must remain version 0.5")
    if analytical_manifest.get("family_order") != EXPECTED_ANALYTICAL_FAMILIES:
        errors.append("Analytical Mode dependency families must remain unchanged")

    if require_complete:
        for key in ("canonical_specification", "evaluation", "migration", "rollback"):
            path = root / str(library.get(key, ""))
            if not path.is_file():
                errors.append(f"missing accessibility canonical document: {library.get(key)}")
        expected_sources = [Path(proof["source"]).name for proof in manifest.get("proofs", [])]
        actual_sources = sorted(path.name for path in (root / "proofs/sources").glob("*.yaml"))
        if expected_sources != actual_sources:
            errors.append("strict accessibility validation requires exactly ten proof sources")
        expected_packages = [Path(proof["package"]).name for proof in manifest.get("proofs", [])]
        actual_packages = sorted(path.name for path in (root / "proofs/packages").glob("*.yaml"))
        if expected_packages != actual_packages:
            errors.append("strict accessibility validation requires exactly ten proof packages")
        for key in ("index", "contrast_matrix", "compatibility"):
            path = root / str(library.get(key, ""))
            if not path.is_file():
                errors.append(f"missing accessibility derived output: {library.get(key)}")
    return errors


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("usage: python tools/validate_accessibility_mode.py ROOT [--incomplete]")
        return 2
    root = Path(sys.argv[1])
    require_complete = len(sys.argv) == 2
    if not require_complete and sys.argv[2] != "--incomplete":
        print("usage: python tools/validate_accessibility_mode.py ROOT [--incomplete]")
        return 2
    errors = validate_accessibility_library(root, require_complete=require_complete)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "accessibility mode valid"
        if require_complete
        else "accessibility mode incomplete contract valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
