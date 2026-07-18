from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


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


def _find_forbidden_keys(value: Any, forbidden: set[str]) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in forbidden:
                found.add(str(key).lower())
            found.update(_find_forbidden_keys(child, forbidden))
    elif isinstance(value, list):
        for child in value:
            found.update(_find_forbidden_keys(child, forbidden))
    return found


def _canonical_digest(value: Any) -> str:
    import hashlib
    import json

    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _canonical_source_document(
    package: dict[str, Any], root: Path, errors: list[str]
) -> dict[str, Any]:
    reference = package.get("source_reference", {})
    path_value = reference.get("path")
    if not isinstance(path_value, str) or not path_value:
        errors.append("accessibility source reference path is required")
        return {}
    repository_root = root.parents[1].resolve()
    path = (repository_root / path_value).resolve()
    if repository_root not in path.parents:
        errors.append("accessibility source reference must stay inside repository")
        return {}
    document = _load(path, errors, "canonical accessibility source")
    if document and document.get("kind") != reference.get("kind"):
        errors.append("accessibility source reference kind must match canonical source")
    return document


def derive_source_semantics(document: dict[str, Any]) -> dict[str, Any]:
    kind = document.get("kind")
    if kind == "analytical-package":
        specification = document.get("specification", {})
        return {
            "kind": kind,
            "id": document.get("id"),
            "dataset": document.get("dataset"),
            "analytical_intent": document.get("analytical_intent"),
            "recipe": document.get("recipe"),
            "family": specification.get("family"),
            "records": specification.get("records"),
            "ordering": specification.get("ordering"),
            "missing_values": specification.get("missing_values"),
            "encoding": document.get("encoding"),
        }
    if kind == "generation-package":
        return {
            "kind": kind,
            "id": document.get("id"),
            "recipe": document.get("recipe"),
            "semantic_intent": document.get("semantic_intent"),
            "content": document.get("content"),
            "component_instances": document.get("component_instances"),
            "relations": document.get("relations"),
        }
    raise ValueError(f"unsupported accessibility semantic source kind: {kind}")


def validate_accessibility_source(
    source: dict[str, Any], root: Path
) -> list[str]:
    errors: list[str] = []
    schema = _load(root / "proof-schema.yaml", errors, "proof schema")
    if errors:
        return errors
    required = set(schema.get("required_source_fields", []))
    missing = sorted(required - set(source))
    if missing:
        return ["accessibility proof source missing fields: " + ",".join(missing)]
    if source.get("language") != "CSDL" or str(source.get("version")) != "0.1":
        errors.append("accessibility proof source must use CSDL version 0.1")
    if source.get("kind") != schema.get("source_kind"):
        errors.append("accessibility proof source kind is invalid")
    forbidden = {str(key).lower() for key in schema.get("forbidden_keys", [])}
    for key in sorted(_find_forbidden_keys(source, forbidden)):
        errors.append(f"accessibility proof source contains forbidden key: {key}")
    profiles = source.get("profiles")
    if (
        not isinstance(profiles, list)
        or not profiles
        or len(profiles) != len(set(profiles))
        or any(profile not in EXPECTED_PROFILES for profile in profiles)
    ):
        errors.append("accessibility proof source profiles must be unique declared values")
    if not isinstance(source.get("text_elements"), list) or not source.get(
        "text_elements"
    ):
        errors.append("accessibility proof source requires text elements")
    if not isinstance(source.get("graphical_objects"), list) or not source.get(
        "graphical_objects"
    ):
        errors.append("accessibility proof source requires graphical objects")
    if not isinstance(source.get("semantic_encodings"), list) or not source.get(
        "semantic_encodings"
    ):
        errors.append("accessibility proof source requires semantic encodings")
    reference = source.get("source_reference", {})
    if not isinstance(reference, dict) or not reference.get("kind") or not reference.get(
        "path"
    ):
        errors.append("accessibility proof source requires a canonical source reference")
    output = source.get("output", {})
    if output.get("canvas") != "1920x1080" or output.get("orientation") != "landscape":
        errors.append("accessibility proof source output must be 1920x1080 landscape")
    if output.get("colorspace") != "sRGB":
        errors.append("accessibility proof source output must declare sRGB")
    return errors


def validate_accessibility_package(
    package: dict[str, Any], root: Path
) -> list[str]:
    errors: list[str] = []
    schema = _load(root / "proof-schema.yaml", errors, "proof schema")
    tokens = _load(root / "contracts/tokens.yaml", errors, "token contract")
    contrast = _load(root / "contracts/contrast.yaml", errors, "contrast contract")
    fallbacks = _load(root / "contracts/fallbacks.yaml", errors, "fallback contract")
    compatibility = _load(
        root / "contracts/compatibility.yaml", errors, "compatibility source"
    )
    if errors:
        return errors

    required = set(schema.get("required_package_fields", []))
    missing = sorted(required - set(package))
    if missing:
        errors.append("accessibility package missing fields: " + ",".join(missing))
        return errors
    if package.get("language") != "CSDL" or str(package.get("version")) != "0.1":
        errors.append("accessibility package must use CSDL version 0.1")
    if package.get("kind") != "accessibility-package":
        errors.append("accessibility package kind must equal accessibility-package")
    forbidden = {str(key).lower() for key in schema.get("forbidden_keys", [])}
    accessibility_authored_fields = {
        key: value for key, value in package.items() if key != "source_semantics"
    }
    for key in sorted(_find_forbidden_keys(accessibility_authored_fields, forbidden)):
        errors.append(f"accessibility package contains forbidden key: {key}")

    source_document = _canonical_source_document(package, root, errors)
    if source_document and package.get("semantic_source_digest") != _canonical_digest(
        source_document
    ):
        errors.append("accessibility source digest must match canonical source")
    if source_document:
        try:
            expected_source_semantics = derive_source_semantics(source_document)
        except ValueError as error:
            errors.append(str(error))
        else:
            if package.get("source_semantics") != expected_source_semantics:
                errors.append(
                    "accessibility source semantics must match canonical source independently"
                )

    profile_names = package.get("profiles", [])
    if not isinstance(profile_names, list) or not profile_names:
        errors.append("accessibility package requires at least one output profile")
        profile_names = []
    if any(profile not in EXPECTED_PROFILES for profile in profile_names):
        errors.append("accessibility package uses an undeclared output profile")
    results = package.get("profile_results", [])
    if [result.get("profile") for result in results] != profile_names:
        errors.append("accessibility profile results must match declared profiles")

    allowed_text_roles = set(schema.get("text_roles", []))
    text_elements = package.get("text_elements", [])
    for element in text_elements:
        if element.get("role") not in allowed_text_roles:
            errors.append(f"accessibility text role is undeclared: {element.get('role')}")
        for prohibited in contrast.get("prohibited_pairings", []):
            if (
                prohibited.get("use") == "normal_text"
                and element.get("foreground") == prohibited.get("foreground")
                and element.get("background") == prohibited.get("background")
            ):
                errors.append("prohibited foreground/background combination")
    allowed_graphic_roles = set(schema.get("graphical_roles", []))
    graphical_objects = package.get("graphical_objects", [])
    public_components = {
        entry.get("name") for entry in compatibility.get("components", [])
    }
    component_token_rules = {
        "Signal": {"signal.primary", "signal.data", "signal.attention", "signal.positive", "signal.error", "state.selection"},
        "Frame": {"line.strong"},
        "Divider": {"line.strong"},
        "Vector": {"line.strong", "signal.primary", "signal.data"},
        "Bridge": {"line.strong", "signal.primary", "signal.data", "signal.attention"},
        "Axis": {"line.strong", "signal.primary", "signal.data"},
        "Node": {"line.strong", "signal.primary", "signal.data", "signal.attention", "signal.positive", "signal.error", "state.focus", "state.selection", "data.missing"},
        "Loop": {"line.strong", "signal.primary", "signal.data"},
        "Field": {"line.strong"},
        "Collision": {"line.strong", "signal.primary"},
    }
    for item in graphical_objects:
        if item.get("role") not in allowed_graphic_roles:
            errors.append(f"accessibility graphical role is undeclared: {item.get('role')}")
        component = item.get("component")
        if component not in public_components:
            errors.append(f"accessibility component is not public: {component}")
        elif item.get("foreground") not in component_token_rules.get(component, set()):
            errors.append(
                f"token {item.get('foreground')} is incompatible with component {component}"
            )

    allowed_carriers = set(schema.get("redundant_carriers", []))
    allowed_meanings = set(schema.get("semantic_meanings", []))
    semantic_encodings = package.get("semantic_encodings", [])
    for encoding in semantic_encodings:
        if encoding.get("meaning") not in allowed_meanings:
            errors.append(f"accessibility semantic meaning is undeclared: {encoding.get('meaning')}")
        carriers = encoding.get("redundant_carriers", [])
        if not carriers or not set(carriers) <= allowed_carriers:
            errors.append("color cannot be the sole carrier of meaning")
        area = encoding.get("area_percent")
        maximum = encoding.get("max_area_percent")
        if area is not None and maximum is not None and area > maximum:
            errors.append("accessibility Signal area exceeds its existing semantic ceiling")

    by_meaning = {
        encoding.get("meaning"): encoding for encoding in semantic_encodings
    }
    scenario = package.get("scenario")
    if scenario == "editorial-equivalence":
        if package.get("profiles") != ["light", "night"] or "signal" not in by_meaning:
            errors.append("editorial proof requires light/night semantic equivalence")
    elif scenario == "structural-signal":
        if not {"signal", "direction", "focus", "selection"} <= set(by_meaning):
            errors.append("structural proof requires accessible Signal, direction, focus, and selection")
    elif scenario == "exact-table":
        data = by_meaning.get("data", {})
        if not all(
            data.get(key) is True
            for key in (
                "exact_lookup",
                "direct_labels",
                "units_readable",
                "source_readable",
                "missing_distinct_from_zero",
            )
        ):
            errors.append("exact table requires lookup, labels, units, source, and missing semantics")
    elif scenario == "positive-negative-bar":
        data = by_meaning.get("data", {})
        carriers = set(data.get("redundant_carriers", []))
        if (
            data.get("zero_baseline") is not True
            or data.get("signed_values") is not True
            or not {"position_from_zero", "numeric_label"} <= carriers
        ):
            errors.append("positive/negative bars require zero, sign, position, and numeric labels")
    elif scenario == "forecast-uncertainty":
        observed = by_meaning.get("observed", {})
        forecast = by_meaning.get("forecast", {})
        if (
            observed.get("line_style") == forecast.get("line_style")
            or "direct_label" not in observed.get("redundant_carriers", [])
            or "direct_label" not in forecast.get("redundant_carriers", [])
        ):
            errors.append(
                "observed and forecast values require distinct line styles and direct labels"
            )
        uncertainty = by_meaning.get("uncertainty", {})
        if (
            uncertainty.get("visible") is not True
            or uncertainty.get("lower_upper_visible") is not True
            or not uncertainty.get("interval_type")
            or not uncertainty.get("level")
            or "interval_boundary" not in uncertainty.get("redundant_carriers", [])
            or "direct_label" not in uncertainty.get("redundant_carriers", [])
        ):
            errors.append(
                "uncertainty interval requires visible boundaries, label, type, and level"
            )
    elif scenario == "heatmap-fallback":
        data = by_meaning.get("data", {})
        if not {"numeric_label", "pattern"} <= set(data.get("scale_fallback", [])):
            errors.append("heatmap scale requires numeric-label and pattern fallback")
        if (
            data.get("missing_distinct_from_zero") is not True
            or data.get("missing_label") in {None, "", 0, "0"}
        ):
            errors.append("missing-value encoding must remain distinct from zero")
    elif scenario == "normalized-map":
        data = by_meaning.get("data", {})
        if not {"pattern", "direct_label"} <= set(
            data.get("redundant_carriers", [])
        ):
            errors.append("map regions require pattern and direct-label fallback")
        if data.get("normalized_rate") is not True or not data.get("missing_label"):
            errors.append("normalized map requires rate semantics and explicit missing region")
    elif scenario == "directed-network":
        direction = by_meaning.get("direction", {})
        if not {"arrowhead", "direct_label"} <= set(
            direction.get("redundant_carriers", [])
        ):
            errors.append("network direction requires arrowhead and direct-label fallback")
        weight = by_meaning.get("weight", {})
        if not {"stroke_weight", "numeric_label"} <= set(
            weight.get("redundant_carriers", [])
        ):
            errors.append("network weight requires stroke and numeric-label fallback")
    elif scenario == "monochrome-export":
        required_meanings = {
            "signal",
            "focus",
            "selection",
            "error",
            "positive",
            "attention",
            "data",
            "missing",
            "uncertainty",
            "observed",
            "forecast",
        }
        if package.get("profiles") != ["monochrome"] or not required_meanings <= set(
            by_meaning
        ):
            errors.append("monochrome export must cover every required semantic state")
        signal = by_meaning.get("signal", {})
        if (
            signal.get("grayscale_contrast", 0) < 3
            or not {"shape", "stroke_weight"} <= set(
                signal.get("redundant_carriers", [])
            )
        ):
            errors.append("Signal must survive grayscale with form and minimum contrast")
    elif scenario == "projector-fallback":
        if package.get("profiles") != ["projector"]:
            errors.append("projector proof must use only the projector profile")
        if not {"data", "signal"} <= set(by_meaning):
            errors.append("projector proof requires readable data and one accessible Signal")
    else:
        errors.append(f"accessibility scenario is undeclared: {scenario}")

    semantic_signature = _canonical_digest(
        {
            "source_reference": package.get("source_reference"),
            "scenario": package.get("scenario"),
            "semantic_encodings": package.get("semantic_encodings"),
        }
    )
    for result in results:
        profile_name = result.get("profile")
        if profile_name not in EXPECTED_PROFILES:
            continue
        profile = tokens["profiles"][profile_name]
        thresholds = contrast["profiles"][profile_name]
        if result.get("thresholds") != thresholds:
            errors.append("accessibility profile thresholds must match canonical contract")
        if result.get("token_values") != profile["tokens"]:
            errors.append("accessibility profile tokens must match canonical contract")
        if result.get("semantic_signature") != semantic_signature:
            errors.append("light and night semantic signatures must remain equivalent")
        if result.get("color_vision_profiles") != fallbacks["color_vision"]["profiles"]:
            errors.append("accessibility CVD profiles must match fallback contract")

        expected_text_checks = []
        for element in text_elements:
            if profile_name not in element.get("profiles", [profile_name]):
                continue
            foreground = element.get("foreground")
            background = element.get("background")
            values = profile["tokens"]
            if foreground not in values or background not in values:
                errors.append("accessibility text pairing references undeclared token")
                continue
            ratio = contrast_ratio(values[foreground], values[background])
            minimum = thresholds["minimum_text_contrast"]
            expected_text_checks.append(
                {
                    "id": element.get("id"),
                    "role": element.get("role"),
                    "foreground": foreground,
                    "background": background,
                    "ratio": round(ratio, 6),
                    "minimum": minimum,
                    "passes": ratio >= minimum,
                }
            )
            if ratio < minimum:
                errors.append(f"insufficient text contrast: {element.get('id')}")
        if result.get("text_checks") != expected_text_checks:
            errors.append("accessibility text contrast must match independent calculation")

        expected_graphical_checks = []
        for item in graphical_objects:
            if profile_name not in item.get("profiles", [profile_name]):
                continue
            foreground = item.get("foreground")
            background = item.get("background")
            values = profile["tokens"]
            if foreground not in values or background not in values:
                errors.append("accessibility graphical pairing references undeclared token")
                continue
            ratio = contrast_ratio(values[foreground], values[background])
            minimum = thresholds["minimum_non_text_contrast"]
            minimum_stroke = thresholds["critical_stroke_px"]
            passes = ratio >= minimum and (
                not item.get("meaningful", True)
                or item.get("stroke_px", 0) >= minimum_stroke
            )
            expected_graphical_checks.append(
                {
                    "id": item.get("id"),
                    "role": item.get("role"),
                    "component": item.get("component"),
                    "foreground": foreground,
                    "background": background,
                    "ratio": round(ratio, 6),
                    "minimum": minimum,
                    "stroke_px": item.get("stroke_px"),
                    "minimum_stroke_px": minimum_stroke,
                    "passes": passes,
                }
            )
            if ratio < minimum:
                errors.append(f"insufficient non-text contrast: {item.get('id')}")
            if item.get("meaningful", True) and item.get("stroke_px", 0) < minimum_stroke:
                errors.append(f"meaningful rule is too thin: {item.get('id')}")
        if result.get("graphical_checks") != expected_graphical_checks:
            errors.append("accessibility non-text contrast must match independent calculation")

    if "light" in profile_names and "night" in profile_names:
        signatures = {
            result.get("semantic_signature")
            for result in results
            if result.get("profile") in {"light", "night"}
        }
        if signatures != {semantic_signature}:
            errors.append("light and night semantic signatures must remain equivalent")

    output = package.get("output", {})
    if output.get("canvas") != "1920x1080" or output.get("orientation") != "landscape":
        errors.append("accessibility output must use canonical 1920x1080 landscape")
    if output.get("colorspace") != "sRGB":
        errors.append("accessibility output must declare sRGB")
    if output.get("profiles") != profile_names:
        errors.append("accessibility output profiles must match package profiles")
    if package.get("provenance", {}).get("deterministic") is not True:
        errors.append("accessibility package must declare deterministic output")
    if package.get("provenance", {}).get("evidence") != "deterministic_specification":
        errors.append("accessibility package evidence must be deterministic specification")
    return errors


def _apply_fixture_mutation(package: dict[str, Any], mutation: dict[str, Any]) -> None:
    path = mutation.get("path", [])
    target: Any = package
    for key in path[:-1]:
        target = target[key]
    final = path[-1]
    if mutation.get("operation", "set") == "delete":
        del target[final]
    else:
        target[final] = mutation.get("value")


def validate_negative_fixture(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    fixture = _load(path, errors, path.name)
    if errors:
        return errors
    package = _load(
        root / str(fixture.get("base_package", "")),
        errors,
        "negative fixture base package",
    )
    if errors:
        return errors
    mutation = fixture.get("mutation")
    if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), list):
        return ["negative fixture mutation must declare a path"]
    try:
        _apply_fixture_mutation(package, mutation)
    except (KeyError, IndexError, TypeError) as error:
        return [f"negative fixture mutation path is invalid: {error}"]
    return validate_accessibility_package(package, root)


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
        from tools.build_accessibility_mode import (
            derive_accessibility_package,
            derive_compatibility,
            derive_contrast_matrix,
            derive_index,
        )

        for proof in manifest.get("proofs", []):
            source_path = root / str(proof.get("source", ""))
            package_path = root / str(proof.get("package", ""))
            if not source_path.is_file() or not package_path.is_file():
                continue
            source = _load(source_path, errors, source_path.name)
            package = _load(package_path, errors, package_path.name)
            if not source or not package:
                continue
            errors.extend(validate_accessibility_source(source, root))
            errors.extend(validate_accessibility_package(package, root))
            source["source_path"] = proof.get("source")
            try:
                expected_package = derive_accessibility_package(source, root)
            except (KeyError, OSError, TypeError, ValueError, yaml.YAMLError) as error:
                errors.append(
                    f"accessibility package cannot be deterministically rebuilt: {error}"
                )
            else:
                if package != expected_package:
                    errors.append(
                        "accessibility proof package does not match deterministic rebuild: "
                        + package_path.name
                    )
        for key in ("index", "contrast_matrix", "compatibility"):
            path = root / str(library.get(key, ""))
            if not path.is_file():
                errors.append(f"missing accessibility derived output: {library.get(key)}")
        if all(
            (root / str(library.get(key, ""))).is_file()
            for key in ("index", "contrast_matrix", "compatibility")
        ):
            expected_outputs = {
                "index": derive_index(root, manifest),
                "contrast_matrix": derive_contrast_matrix(tokens, contrast),
                "compatibility": derive_compatibility(manifest, compatibility),
            }
            messages = {
                "index": "accessibility index does not match deterministic derivation",
                "contrast_matrix": "accessibility contrast matrix does not match deterministic derivation",
                "compatibility": "accessibility compatibility does not match deterministic derivation",
            }
            for key, expected in expected_outputs.items():
                actual = _load(
                    root / str(library[key]), errors, f"accessibility {key}"
                )
                if actual and actual != expected:
                    errors.append(messages[key])
        fixture_root = root / "fixtures/negative"
        fixture_index = _load(
            fixture_root / "expected-errors.yaml",
            errors,
            "accessibility negative fixture index",
        )
        fixtures = fixture_index.get("fixtures", []) if fixture_index else []
        expected_fixture_files = [entry.get("file") for entry in fixtures]
        actual_fixture_files = sorted(
            path.name
            for path in fixture_root.glob("*.yaml")
            if path.name != "expected-errors.yaml"
        )
        if len(fixtures) < 17 or expected_fixture_files != actual_fixture_files:
            errors.append(
                "strict accessibility validation requires the indexed negative fixtures"
            )
        for fixture in fixtures:
            fixture_errors = validate_negative_fixture(
                fixture_root / str(fixture.get("file", "")), root
            )
            if fixture.get("error") not in fixture_errors:
                errors.append(
                    "negative accessibility fixture does not fail for expected reason: "
                    + str(fixture.get("file"))
                )
        positive_index = _load(
            root / "fixtures/positive/index.yaml",
            errors,
            "accessibility positive fixture index",
        )
        expected_positive = [
            {
                "id": Path(str(proof.get("package", ""))).stem,
                "package": proof.get("package"),
                "scenario": proof.get("scenario"),
            }
            for proof in manifest.get("proofs", [])
        ]
        if positive_index.get("fixtures", []) != expected_positive:
            errors.append(
                "positive fixture index must reference all ten accessibility proofs"
            )
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
