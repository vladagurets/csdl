from __future__ import annotations

import re
import sys
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


def _missing_fields(value: Any, required: list[str]) -> list[str]:
    if not isinstance(value, dict):
        return list(required)
    return sorted(set(required) - set(value))


def _is_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_range(
    value: Any,
    errors: list[str],
    label: str,
    lower_bound: float | None = None,
    upper_bound: float | None = None,
) -> None:
    if not isinstance(value, dict) or set(value) != {"min", "max"}:
        errors.append(f"{label} must define only min and max")
        return
    minimum = value.get("min")
    maximum = value.get("max")
    if not isinstance(minimum, (int, float)) or isinstance(minimum, bool):
        errors.append(f"{label}.min must be numeric")
        return
    if not isinstance(maximum, (int, float)) or isinstance(maximum, bool):
        errors.append(f"{label}.max must be numeric")
        return
    if minimum > maximum:
        errors.append(f"{label}.min must not exceed max")
    if lower_bound is not None and minimum < lower_bound:
        errors.append(f"{label}.min must be at least {lower_bound:g}")
    if upper_bound is not None and maximum > upper_bound:
        errors.append(f"{label}.max must be at most {upper_bound:g}")


def _resolve_evidence_path(root: Path, repository_root: Path, relative: str) -> Path:
    library_relative = root / relative
    if library_relative.exists():
        return library_relative
    return repository_root / relative


def _validate_evidence_reference(
    value: Any,
    root: Path,
    repository_root: Path,
    required_fields: list[str],
    errors: list[str],
    label: str,
) -> None:
    missing = _missing_fields(value, required_fields)
    if missing:
        errors.append(f"{label} missing fields: {','.join(missing)}")
        return
    for field in required_fields:
        if not _is_text(value.get(field)):
            errors.append(f"{label}.{field} must be non-empty text")
    path = value.get("path")
    if _is_text(path) and not _resolve_evidence_path(root, repository_root, path).exists():
        errors.append(f"{label} path does not exist: {path}")


def _validate_relations(
    component: dict[str, Any],
    schema: dict[str, Any],
    component_names: set[str],
    errors: list[str],
    label: str,
) -> None:
    relations = component.get("relations")
    if not isinstance(relations, dict) or set(relations) != {"allowed", "forbidden"}:
        errors.append(f"{label} relations must define only allowed and forbidden")
        return

    enums = schema.get("enums", {})
    required = schema.get("required_relation_fields", [])
    normalized: dict[str, set[tuple[str, str, str, str]]] = {
        "allowed": set(),
        "forbidden": set(),
    }
    for group in ("allowed", "forbidden"):
        entries = relations.get(group)
        if not isinstance(entries, list):
            errors.append(f"{label} relations.{group} must be a list")
            continue
        for index, entry in enumerate(entries, start=1):
            entry_label = f"{label} relations.{group} entry {index}"
            missing = _missing_fields(entry, required)
            if missing:
                errors.append(f"{entry_label} missing fields: {','.join(missing)}")
                continue
            relation_type = entry.get("type")
            target = entry.get("target")
            direction = entry.get("direction")
            cardinality = entry.get("cardinality")
            condition = entry.get("condition", "always")
            unknown = sorted(set(entry) - set(required) - {"condition"})
            if unknown:
                errors.append(f"{entry_label} contains unknown fields: {','.join(unknown)}")
            if relation_type not in schema.get("relation_types", []):
                errors.append(f"{entry_label} type is invalid")
            if target not in component_names | {"any"}:
                errors.append(f"{entry_label} target is not a declared component")
            if direction not in enums.get("relation_direction", []):
                errors.append(f"{entry_label} direction is invalid")
            if cardinality not in enums.get("relation_cardinality", []):
                errors.append(f"{entry_label} cardinality is invalid")
            if not _is_text(condition):
                errors.append(f"{entry_label} condition must be non-empty text")
                condition = ""
            normalized[group].add((str(relation_type), str(target), str(direction), str(condition)))

    contradictions = normalized["allowed"] & normalized["forbidden"]
    for relation_type, target, direction, condition in sorted(contradictions):
        errors.append(
            f"{label} relation is both allowed and forbidden: "
            f"{relation_type}:{target}:{direction}:{condition}"
        )


def _validate_expression_limits(
    component: dict[str, Any],
    schema: dict[str, Any],
    errors: list[str],
    label: str,
) -> None:
    limits = component.get("expression_limits")
    required_levels = schema.get("required_expression_levels", [])
    if not isinstance(limits, dict) or list(limits) != required_levels:
        errors.append(f"{label} expression_limits must define A, B, and C in order")
        return
    statuses = schema.get("enums", {}).get("expression_status", [])
    required_fields = schema.get("required_expression_fields", [])
    for level in required_levels:
        value = limits.get(level)
        missing = _missing_fields(value, required_fields)
        if missing:
            errors.append(f"{label} expression {level} missing fields: {','.join(missing)}")
            continue
        status = value.get("status")
        max_count = value.get("max_count")
        if status not in statuses:
            errors.append(f"{label} expression {level} status is invalid")
        if not isinstance(max_count, int) or isinstance(max_count, bool) or max_count < 0:
            errors.append(f"{label} expression {level} max_count must be a non-negative integer")
        if status == "conditional" and not _is_text(value.get("condition")):
            errors.append(f"{label} expression {level} conditional status requires condition")
        if status == "forbidden" and not _is_text(value.get("reason")):
            errors.append(f"{label} expression {level} forbidden status requires reason")


def _validate_examples(
    component: dict[str, Any],
    root: Path,
    repository_root: Path,
    schema: dict[str, Any],
    errors: list[str],
    label: str,
) -> None:
    examples = component.get("examples")
    groups = schema.get("required_example_groups", [])
    if not isinstance(examples, dict) or list(examples) != groups:
        errors.append(f"{label} examples must define do and dont in order")
        return
    required = schema.get("required_example_fields", [])
    for group in groups:
        entries = examples.get(group)
        if not isinstance(entries, list) or not entries:
            errors.append(f"{label} examples.{group} must be a non-empty list")
            continue
        for index, entry in enumerate(entries, start=1):
            entry_label = f"{label} examples.{group} entry {index}"
            missing = _missing_fields(entry, required)
            if missing:
                errors.append(f"{entry_label} missing fields: {','.join(missing)}")
                continue
            if not _is_text(entry.get("description")):
                errors.append(f"{entry_label}.description must be non-empty text")
            path = entry.get("evidence")
            if not _is_text(path):
                errors.append(f"{entry_label}.evidence must be non-empty text")
            elif not _resolve_evidence_path(root, repository_root, path).exists():
                errors.append(f"{entry_label} evidence path does not exist: {path}")


def _normalize_component_term(term: str, declared_names: set[str]) -> str:
    if term == "Axes":
        return "Axis"
    if term.endswith("s") and term[:-1] in declared_names:
        return term[:-1]
    return term


def _validate_active_vocabulary(
    repository_root: Path,
    declared_names: set[str],
    errors: list[str],
) -> None:
    foundation = repository_root / "specs/2026-07-17-csdl-v0.1-design.md"
    if foundation.exists():
        foundation_text = foundation.read_text(encoding="utf-8")
        grammar_start = foundation_text.find("### 10.1 Nouns")
        grammar_end = foundation_text.find("### 10.5 Example composition sentence")
        grammar_text = foundation_text[grammar_start:grammar_end]
        foundation_terms = re.findall(r"^\| `([A-Z][A-Za-z]+)` \|", grammar_text, flags=re.MULTILINE)
        for term in foundation_terms:
            normalized = _normalize_component_term(term, declared_names)
            if normalized not in declared_names:
                errors.append(
                    f"undeclared active component name: {normalized} at "
                    f"{foundation.relative_to(repository_root)}"
                )

    pattern_root = repository_root / "patterns/visual-dna-sprint-01"
    manifest_path = pattern_root / "manifest.yaml"
    if manifest_path.exists():
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        for family in manifest.get("families", []):
            for name in family.get("components", []):
                if name not in declared_names:
                    errors.append(
                        f"undeclared active component name: {name} at "
                        f"patterns/visual-dna-sprint-01/manifest.yaml family {family.get('id')}"
                    )
    for prompt in sorted((pattern_root / "prompts").glob("*.yaml")):
        data = yaml.safe_load(prompt.read_text(encoding="utf-8"))
        for name in data.get("composition", {}).get("components", []):
            if name not in declared_names:
                errors.append(
                    f"undeclared active component name: {name} at {prompt.relative_to(repository_root)}"
                )
    for specification in sorted((pattern_root / "specs").glob("*.md")):
        terms = re.findall(r"`([A-Z][A-Za-z]+)`", specification.read_text(encoding="utf-8"))
        for term in terms:
            if not any(character.islower() for character in term):
                continue
            normalized = _normalize_component_term(term, declared_names)
            if normalized not in declared_names:
                errors.append(
                    f"undeclared active component name: {normalized} at "
                    f"{specification.relative_to(repository_root)}"
                )


def validate_component_library(path: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    root = path.parent
    repository_root = root.parents[1]
    schema_path = root / "schema.yaml"
    if not schema_path.exists():
        return ["missing component schema: schema.yaml"]

    data = _load_yaml(path, errors, "manifest.yaml")
    schema = _load_yaml(schema_path, errors, "schema.yaml")
    if errors:
        return errors

    library = data.get("library")
    missing_library = _missing_fields(library, schema.get("required_library_fields", []))
    if missing_library:
        errors.append("library missing fields: " + ",".join(missing_library))
    if not isinstance(library, dict):
        library = {}
    unknown_library = sorted(set(library) - set(schema.get("required_library_fields", [])))
    if unknown_library:
        errors.append("library contains unknown fields: " + ",".join(unknown_library))
    expected_library = {
        "source_milestone": 3,
        "canvas": "1920x1080",
        "orientation": "landscape",
        "markdown_authority": True,
        "component_count": 15,
        "schema": "schema.yaml",
        "index": "index.yaml",
        "compatibility": "compatibility.yaml",
        "proofs_dir": "proofs",
        "evaluation": "evaluation/review.md",
        "visual_authority": "patterns/visual-dna-sprint-01/visual-authority.yaml",
    }
    for field, expected in expected_library.items():
        if library.get(field) != expected:
            errors.append(f"library.{field} must equal {expected}")

    expected_components = schema.get("component_order", [])
    component_names = {entry.get("name") for entry in expected_components}
    component_slugs = [entry.get("slug") for entry in expected_components]
    vocabulary = data.get("vocabulary")
    if not isinstance(vocabulary, dict):
        errors.append("vocabulary must be a mapping")
    else:
        if vocabulary.get("components") != [entry.get("name") for entry in expected_components]:
            errors.append("vocabulary.components must match schema component order")
        if vocabulary.get("relations") != schema.get("relation_types"):
            errors.append("vocabulary.relations must match schema relation types")

    components = data.get("components")
    if not isinstance(components, list):
        return errors + ["components must be a list"]
    if require_complete and len(components) != 15:
        errors.append("components must contain exactly 15 entries")
    if not require_complete and len(components) > 15:
        errors.append("components must not contain more than 15 entries")

    actual_slugs = [component.get("slug") for component in components if isinstance(component, dict)]
    expected_subsequence = [slug for slug in component_slugs if slug in actual_slugs]
    if actual_slugs != expected_subsequence:
        errors.append("component records must follow canonical schema order")
    if require_complete and actual_slugs != component_slugs:
        errors.append("component order must match schema")

    ids = [str(component.get("id")) for component in components if isinstance(component, dict)]
    names = [component.get("name") for component in components if isinstance(component, dict)]
    for field, values in (("ids", ids), ("slugs", actual_slugs), ("names", names)):
        if len(values) != len(set(values)):
            errors.append(f"component {field} must be unique")

    expected_by_slug = {entry["slug"]: entry for entry in expected_components}
    required_fields = schema.get("required_component_fields", [])
    allowed_fields = set(schema.get("allowed_component_fields", []))
    enums = schema.get("enums", {})
    family_order = schema.get("family_order", [])
    forbidden = schema.get("forbidden_placeholders", [])

    for component in components:
        if not isinstance(component, dict):
            errors.append("each component must be a mapping")
            continue
        component_id = str(component.get("id", "??"))
        label = f"component {component_id}"
        missing = _missing_fields(component, required_fields)
        if missing:
            errors.append(f"{label} missing fields: {','.join(missing)}")
        unknown = sorted(set(component) - allowed_fields)
        if unknown:
            errors.append(f"{label} contains unknown fields: {','.join(unknown)}")

        slug = component.get("slug")
        expected = expected_by_slug.get(slug)
        if expected is None:
            errors.append(f"{label} slug is not declared in schema")
        else:
            if component.get("id") != expected.get("id"):
                errors.append(f"{label} id must match schema for {slug}")
            if component.get("name") != expected.get("name"):
                errors.append(f"{label} name must match schema for {slug}")

        if component.get("category") not in enums.get("category", []):
            errors.append(f"{label} category is invalid")
        if component.get("evidence_level") not in enums.get("evidence_level", []):
            errors.append(f"{label} evidence_level is invalid")
        for field in ("purpose", "semantic_meaning"):
            if not _is_text(component.get(field)):
                errors.append(f"{label} {field} must be non-empty text")

        spatial = component.get("spatial_contract")
        if not isinstance(spatial, dict) or "count" not in spatial:
            errors.append(f"{label} spatial_contract must define count")
        else:
            _validate_range(spatial.get("count"), errors, f"{label} spatial_contract.count", 0)

        dimensions = component.get("dimensions")
        if not isinstance(dimensions, dict):
            errors.append(f"{label} dimensions must be a mapping")
        else:
            if dimensions.get("unit") not in enums.get("dimension_unit", []):
                errors.append(f"{label} dimensions.unit is invalid")
            if "area_percent" not in dimensions:
                errors.append(f"{label} dimensions must define area_percent")
            else:
                _validate_range(
                    dimensions.get("area_percent"),
                    errors,
                    f"{label} dimensions.area_percent",
                    0,
                    100,
                )
            for field, value in dimensions.items():
                if field not in {"unit", "area_percent"}:
                    _validate_range(value, errors, f"{label} dimensions.{field}", 0)

        _validate_relations(component, schema, component_names, errors, label)

        compatible = component.get("compatible_families")
        if not isinstance(compatible, list) or not compatible:
            errors.append(f"{label} compatible_families must be a non-empty list")
        else:
            if len(compatible) != len(set(compatible)):
                errors.append(f"{label} compatible_families must be unique")
            for family in compatible:
                if family not in family_order:
                    errors.append(f"{label} compatible family is invalid: {family}")

        _validate_expression_limits(component, schema, errors, label)

        typography = component.get("typography")
        missing_typography = _missing_fields(typography, schema.get("required_typography_fields", []))
        if missing_typography:
            errors.append(f"{label} typography missing fields: {','.join(missing_typography)}")
        elif not _is_text(typography.get("role")) or not isinstance(typography.get("constraints"), list) or not typography.get("constraints"):
            errors.append(f"{label} typography role and constraints must be non-empty")

        semantic_color = component.get("semantic_color")
        missing_color = _missing_fields(
            semantic_color,
            schema.get("required_semantic_color_fields", []),
        )
        if missing_color:
            errors.append(f"{label} semantic_color missing fields: {','.join(missing_color)}")
        elif not _is_text(semantic_color.get("default")) or not isinstance(
            semantic_color.get("signal_target_allowed"), bool
        ):
            errors.append(f"{label} semantic_color values are invalid")

        _validate_examples(component, root, repository_root, schema, errors, label)

        prompt_dsl = component.get("prompt_dsl")
        missing_prompt = _missing_fields(prompt_dsl, schema.get("required_prompt_dsl_fields", []))
        if missing_prompt:
            errors.append(f"{label} prompt_dsl missing fields: {','.join(missing_prompt)}")
        elif not _is_text(prompt_dsl.get("syntax")) or not isinstance(
            prompt_dsl.get("required_fields"), list
        ) or not prompt_dsl.get("required_fields") or not isinstance(
            prompt_dsl.get("optional_fields"), list
        ):
            errors.append(f"{label} prompt_dsl values are invalid")

        invariants = component.get("validation_invariants")
        if not isinstance(invariants, list) or not invariants or not all(_is_text(item) for item in invariants):
            errors.append(f"{label} validation_invariants must be a non-empty text list")

        evidence = component.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{label} evidence must be a non-empty list")
        else:
            for index, entry in enumerate(evidence, start=1):
                _validate_evidence_reference(
                    entry,
                    root,
                    repository_root,
                    schema.get("required_evidence_fields", []),
                    errors,
                    f"{label} evidence entry {index}",
                )

        specification_value = component.get("specification")
        expected_spec = f"specs/{component_id}-{slug}.md"
        if specification_value != expected_spec:
            errors.append(f"{label} specification path must equal {expected_spec}")
        specification = root / str(specification_value)
        if not specification.exists():
            errors.append(f"{label} missing specification: {specification_value}")
        else:
            spec_text = specification.read_text(encoding="utf-8")
            for section in schema.get("required_spec_sections", []):
                if section not in spec_text:
                    errors.append(f"{label} specification missing section: {section}")
            for token in forbidden:
                if _contains_token(spec_text, str(token)):
                    errors.append(f"{label} specification contains forbidden marker: {token}")

        serialized = yaml.safe_dump(component, allow_unicode=True, sort_keys=False)
        for token in forbidden:
            if _contains_token(serialized, str(token)):
                errors.append(f"{label} manifest contains forbidden marker: {token}")

    if components or require_complete:
        _validate_active_vocabulary(repository_root, component_names, errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_component_library.py MANIFEST")
        return 2
    errors = validate_component_library(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("component library valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
