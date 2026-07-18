from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


def _load_yaml(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} must be readable YAML: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return value


def _missing(value: Any, required: list[str]) -> list[str]:
    if not isinstance(value, dict):
        return list(required)
    return sorted(set(required) - set(value))


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _contains_token(text: str, token: str) -> bool:
    return re.search(rf"\b{re.escape(token)}\b", text, flags=re.IGNORECASE) is not None


def _component_contract(repository_root: Path) -> dict[str, Any]:
    return yaml.safe_load(
        (repository_root / "components/component-library-v0.1/manifest.yaml").read_text(
            encoding="utf-8"
        )
    )


def _relation_is_allowed(
    subject: dict[str, Any], target: dict[str, Any], relation_type: str
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


def _validate_ingredients(
    recipe: dict[str, Any], schema: dict[str, Any], errors: list[str], label: str
) -> None:
    ingredients = recipe.get("ingredients")
    groups = schema.get("required_ingredient_groups", [])
    if not isinstance(ingredients, dict) or list(ingredients) != groups:
        errors.append(f"{label} ingredients must define required and optional in order")
        return
    components: list[str] = []
    for group in groups:
        entries = ingredients.get(group)
        if not isinstance(entries, list):
            errors.append(f"{label} ingredients.{group} must be a list")
            continue
        for index, entry in enumerate(entries, start=1):
            entry_label = f"{label} ingredients.{group} entry {index}"
            missing = _missing(entry, schema.get("required_ingredient_fields", []))
            if missing:
                errors.append(f"{entry_label} missing fields: {','.join(missing)}")
                continue
            component = entry.get("component")
            components.append(component)
            if component not in schema.get("public_components", []):
                errors.append(f"{entry_label} component is not public: {component}")
            minimum = entry.get("min")
            maximum = entry.get("max")
            default = entry.get("default")
            if (
                not isinstance(minimum, int)
                or isinstance(minimum, bool)
                or not isinstance(maximum, int)
                or isinstance(maximum, bool)
                or minimum < 0
                or minimum > maximum
            ):
                errors.append(f"{entry_label} min/max cardinality is invalid")
            elif (
                not isinstance(default, int)
                or isinstance(default, bool)
                or default < minimum
                or default > maximum
            ):
                errors.append(f"{entry_label} default cardinality is invalid")
            if group == "required" and minimum < 1:
                errors.append(f"{entry_label} required minimum must be at least one")
            if group == "optional" and minimum != 0:
                errors.append(f"{entry_label} optional minimum must equal zero")
    if len(components) != len(set(components)):
        errors.append(f"{label} ingredient components must be unique")


def _validate_relations(
    recipe: dict[str, Any], schema: dict[str, Any], errors: list[str], label: str
) -> None:
    relations = recipe.get("relations")
    groups = schema.get("required_relation_groups", [])
    if not isinstance(relations, dict) or list(relations) != groups:
        errors.append(f"{label} relations must define allowed and forbidden in order")
        return
    for group in groups:
        entries = relations.get(group)
        if not isinstance(entries, list):
            errors.append(f"{label} relations.{group} must be a list")
            continue
        for index, entry in enumerate(entries, start=1):
            entry_label = f"{label} relations.{group} entry {index}"
            missing = _missing(entry, schema.get("required_relation_fields", []))
            if missing:
                errors.append(f"{entry_label} missing fields: {','.join(missing)}")
                continue
            if entry.get("type") not in schema.get("public_relations", []):
                errors.append(f"{entry_label} type is not public")
            for field in ("subject", "object"):
                if not _text(entry.get(field)):
                    errors.append(f"{entry_label}.{field} must be non-empty text")


def _validate_record(
    recipe: dict[str, Any],
    entry: dict[str, Any],
    root: Path,
    repository_root: Path,
    schema: dict[str, Any],
    components_by_name: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    recipe_id = str(recipe.get("id", "???"))
    label = f"recipe {recipe_id}"
    missing = _missing(recipe, schema.get("required_recipe_fields", []))
    if missing:
        errors.append(f"{label} missing fields: {','.join(missing)}")
    unknown = sorted(set(recipe) - set(schema.get("allowed_recipe_fields", [])))
    if unknown:
        errors.append(f"{label} contains unknown fields: {','.join(unknown)}")

    for field in ("id", "slug", "name", "version", "problem", "specification", "record"):
        if not _text(recipe.get(field)):
            errors.append(f"{label} {field} must be non-empty text")
    for field in ("id", "slug", "name", "source_family", "specification", "record"):
        if recipe.get(field) != entry.get(field):
            errors.append(f"{label} {field} must match manifest entry")

    scenarios = recipe.get("allowed_scenarios")
    if not isinstance(scenarios, list) or not scenarios or not all(_text(item) for item in scenarios):
        errors.append(f"{label} allowed_scenarios must be non-empty text entries")
    assembly = recipe.get("assembly_order")
    if not isinstance(assembly, list) or len(assembly) < 3 or not all(_text(item) for item in assembly):
        errors.append(f"{label} assembly_order must contain at least three steps")

    _validate_ingredients(recipe, schema, errors, label)
    _validate_relations(recipe, schema, errors, label)

    families_for_contract = set(recipe.get("compatible_visual_dna_families", []))
    for group in ("required", "optional"):
        for ingredient in recipe.get("ingredients", {}).get(group, []):
            component = components_by_name.get(ingredient.get("component"))
            if component is None:
                continue
            compatible = set(component.get("compatible_families", []))
            if families_for_contract and not families_for_contract <= compatible:
                errors.append(
                    f"{label} ingredient {component['name']} is incompatible with "
                    "a declared Visual DNA family"
                )
    for index, relation in enumerate(
        recipe.get("relations", {}).get("allowed", []), start=1
    ):
        subject = components_by_name.get(relation.get("subject"))
        target = components_by_name.get(relation.get("object"))
        if subject is None or target is None:
            continue
        if not _relation_is_allowed(subject, target, relation.get("type")):
            errors.append(
                f"{label} allowed relation {index} is not allowed by component contracts"
            )

    levels = recipe.get("expression_levels")
    required_levels = schema.get("required_expression_levels", [])
    if not isinstance(levels, dict) or list(levels) != required_levels:
        errors.append(f"{label} expression_levels must define A, B, and C in order")
    else:
        for level, contract in levels.items():
            missing_level = _missing(contract, schema.get("required_expression_fields", []))
            if missing_level:
                errors.append(f"{label} expression {level} missing status")
                continue
            status = contract.get("status")
            if status not in schema.get("enums", {}).get("expression_status", []):
                errors.append(f"{label} expression {level} status is invalid")
            if status == "conditional" and not _text(contract.get("condition")):
                errors.append(f"{label} expression {level} conditional status requires condition")
            if status == "forbidden" and not _text(contract.get("reason")):
                errors.append(f"{label} expression {level} forbidden status requires reason")

    families = recipe.get("compatible_visual_dna_families")
    if not isinstance(families, list) or not families:
        errors.append(f"{label} compatible_visual_dna_families must be non-empty")
    else:
        if len(families) != len(set(families)):
            errors.append(f"{label} compatible_visual_dna_families must be unique")
        for family in families:
            if family not in schema.get("family_order", []):
                errors.append(f"{label} compatible family is invalid: {family}")

    for field, required in (
        ("presentation", "required_presentation_fields"),
        ("typography", "required_typography_fields"),
        ("semantic_color", "required_semantic_color_fields"),
        ("content_contract", "required_content_contract_fields"),
        ("prompt_dsl", "required_prompt_dsl_fields"),
        ("compatibility", "required_compatibility_fields"),
    ):
        missing_fields = _missing(recipe.get(field), schema.get(required, []))
        if missing_fields:
            errors.append(f"{label} {field} missing fields: {','.join(missing_fields)}")

    presentation = recipe.get("presentation", {})
    if presentation.get("canvas") != "1920x1080" or presentation.get("orientation") != "landscape":
        errors.append(f"{label} presentation must use 1920x1080 landscape")
    negative_space = presentation.get("negative_space_percent")
    if (
        not isinstance(negative_space, dict)
        or set(negative_space) != {"min", "max"}
        or not all(isinstance(value, int) and not isinstance(value, bool) for value in negative_space.values())
        or negative_space.get("min", 101) > negative_space.get("max", -1)
        or negative_space.get("min", -1) < 0
        or negative_space.get("max", 101) > 100
    ):
        errors.append(f"{label} negative_space_percent must define a valid min/max range")

    for field in ("hard_exclusions", "validation_invariants", "canonical_examples", "evidence"):
        value = recipe.get(field)
        if not isinstance(value, list) or not value:
            errors.append(f"{label} {field} must be a non-empty list")

    for index, evidence in enumerate(recipe.get("evidence", []), start=1):
        evidence_label = f"{label} evidence entry {index}"
        missing_evidence = _missing(evidence, schema.get("required_evidence_fields", []))
        if missing_evidence:
            errors.append(f"{evidence_label} missing fields: {','.join(missing_evidence)}")
            continue
        path = evidence.get("path")
        if not _text(path):
            errors.append(f"{evidence_label}.path must be non-empty text")
        elif not (repository_root / path).exists() and not (root / path).exists():
            errors.append(f"{evidence_label} path does not exist: {path}")

    expected_spec = root / f"specs/{recipe_id}-{recipe.get('slug')}.md"
    specification = root / str(recipe.get("specification", ""))
    if specification != expected_spec:
        errors.append(f"{label} specification path must follow schema")
    elif not specification.exists():
        errors.append(f"{label} missing specification")
    else:
        text = specification.read_text(encoding="utf-8")
        for section in schema.get("required_spec_sections", []):
            if section not in text:
                errors.append(f"{label} specification missing section: {section}")
        for token in schema.get("forbidden_placeholders", []):
            if _contains_token(text, str(token)):
                errors.append(f"{label} specification contains forbidden marker: {token}")

    serialized = yaml.safe_dump(recipe, allow_unicode=True, sort_keys=False)
    for token in schema.get("forbidden_placeholders", []):
        if _contains_token(serialized, str(token)):
            errors.append(f"{label} record contains forbidden marker: {token}")


def _validate_migration(
    root: Path,
    repository_root: Path,
    manifest: dict[str, Any],
    schema: dict[str, Any],
    errors: list[str],
) -> None:
    migration_path = root / str(manifest.get("library", {}).get("migration", ""))
    data = _load_yaml(migration_path, errors, "migration contract")
    migration = data.get("migration")
    missing = _missing(migration, schema.get("required_migration_fields", []))
    if missing:
        errors.append("migration missing fields: " + ",".join(missing))
        return
    if migration.get("source_versions") != [0.1]:
        errors.append("migration source_versions must equal [0.1]")
    if str(migration.get("target_version")) != "0.5":
        errors.append("migration target_version must equal 0.5")
    source_files = migration.get("source_files")
    recipe_map = migration.get("recipe_map")
    if not isinstance(source_files, list) or len(source_files) != 27:
        errors.append("migration must declare exactly 27 recipe source files")
        source_files = []
    if len(source_files) != len(set(source_files)):
        errors.append("migration source_files must be unique")
    if not isinstance(recipe_map, dict) or set(recipe_map) != set(source_files):
        errors.append("migration recipe_map keys must equal source_files")
        recipe_map = {}
    declared_ids = {str(entry.get("id")) for entry in manifest.get("recipes", [])}
    for relative in source_files:
        path = repository_root / relative
        if not path.exists():
            errors.append(f"migration source path does not exist: {relative}")
        if str(recipe_map.get(relative)) not in declared_ids:
            errors.append(f"migration source maps to undeclared recipe: {relative}")
    if migration.get("reference_only") != [
        "pilots/01-agentic-discipline/prompts/00-style-anchor.yaml"
    ]:
        errors.append("migration reference_only must preserve the Pilot style anchor")
    elif not (
        repository_root / "pilots/01-agentic-discipline/prompts/00-style-anchor.yaml"
    ).exists():
        errors.append("migration reference-only style anchor path does not exist")
    rules = migration.get("normalization_rules")
    if not isinstance(rules, list) or len(rules) < 5 or not all(_text(rule) for rule in rules):
        errors.append("migration normalization_rules must be complete non-empty text")


def validate_recipe_library(path: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    root = path.parent
    repository_root = root.parents[1]
    manifest = _load_yaml(path, errors, "manifest.yaml")
    schema = _load_yaml(root / "schema.yaml", errors, "schema.yaml")
    if errors:
        return errors

    library = manifest.get("library")
    required_library = schema.get("required_library_fields", [])
    missing_library = _missing(library, required_library)
    if missing_library:
        errors.append("library missing fields: " + ",".join(missing_library))
    if not isinstance(library, dict):
        library = {}
    unknown_library = sorted(set(library) - set(required_library))
    if unknown_library:
        errors.append("library contains unknown fields: " + ",".join(unknown_library))

    expected_library = {
        "version": "0.5.0",
        "source_milestone": 4,
        "canvas": "1920x1080",
        "orientation": "landscape",
        "markdown_authority": True,
        "recipe_count": 23,
        "schema": "schema.yaml",
        "prompt_dsl_schema": "prompt-dsl-v0.5.schema.yaml",
        "migration": "migration-v0.1-to-v0.5.yaml",
        "index": "index.yaml",
        "compatibility": "compatibility.yaml",
        "selection_index": "selection-index.yaml",
        "proofs_dir": "proofs",
        "evaluation": "evaluation/review.md",
        "component_library": "components/component-library-v0.1/manifest.yaml",
        "visual_dna_manifest": "patterns/visual-dna-sprint-01/manifest.yaml",
    }
    for field, expected in expected_library.items():
        if library.get(field) != expected:
            errors.append(f"library.{field} must equal {expected}")

    try:
        component_contract = _component_contract(repository_root)
    except (OSError, KeyError, yaml.YAMLError) as error:
        errors.append(f"Component Library v0.1 must be readable: {error}")
        return errors
    component_names = component_contract["vocabulary"]["components"]
    relation_names = component_contract["vocabulary"]["relations"]
    components_by_name = {
        component["name"]: component for component in component_contract["components"]
    }
    if schema.get("public_components") != component_names:
        errors.append("schema public_components must match Component Library v0.1")
    if schema.get("public_relations") != relation_names:
        errors.append("schema public_relations must match Component Library v0.1")

    recipe_entries = manifest.get("recipes")
    if not isinstance(recipe_entries, list):
        return errors + ["recipes must be a list"]
    if require_complete and len(recipe_entries) != 23:
        errors.append("recipes must contain exactly 23 entries")
    if not require_complete and len(recipe_entries) > 23:
        errors.append("recipes must not contain more than 23 entries")

    order = schema.get("recipe_order", [])
    expected_by_slug = {entry["slug"]: entry for entry in order}
    slugs = [entry.get("slug") for entry in recipe_entries if isinstance(entry, dict)]
    expected_subsequence = [entry["slug"] for entry in order if entry["slug"] in slugs]
    if slugs != expected_subsequence:
        errors.append("recipe entries must follow canonical schema order")
    if require_complete and slugs != [entry["slug"] for entry in order]:
        errors.append("recipe order must match schema")
    if len(slugs) != len(set(slugs)):
        errors.append("recipe slugs must be unique")

    for entry in recipe_entries:
        if not isinstance(entry, dict):
            errors.append("each recipe manifest entry must be a mapping")
            continue
        expected = expected_by_slug.get(entry.get("slug"))
        if expected is None:
            errors.append(f"recipe slug is not declared in schema: {entry.get('slug')}")
            continue
        for field in ("id", "name", "family"):
            manifest_field = "source_family" if field == "family" else field
            if entry.get(manifest_field) != expected.get(field):
                errors.append(
                    f"recipe {entry.get('slug')} {manifest_field} must match schema"
                )
        expected_record = f"records/{expected['id']}-{expected['slug']}.yaml"
        expected_spec = f"specs/{expected['id']}-{expected['slug']}.md"
        if entry.get("record") != expected_record or entry.get("specification") != expected_spec:
            errors.append(f"recipe {expected['id']} paths must follow schema")
            continue
        record_path = root / expected_record
        if not record_path.exists():
            errors.append(f"recipe {expected['id']} missing record: {expected_record}")
            continue
        recipe = _load_yaml(record_path, errors, expected_record)
        _validate_record(
            recipe,
            entry,
            root,
            repository_root,
            schema,
            components_by_name,
            errors,
        )
    if require_complete:
        _validate_migration(root, repository_root, manifest, schema, errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_recipe_library.py MANIFEST")
        return 2
    errors = validate_recipe_library(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("recipe library valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
