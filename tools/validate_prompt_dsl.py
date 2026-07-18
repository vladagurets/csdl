from __future__ import annotations

import re
import sys
from collections import Counter
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


def _contains_token(text: str, token: str) -> bool:
    return re.search(rf"\b{re.escape(token)}\b", text, flags=re.IGNORECASE) is not None


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


def _load_records(root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for entry in manifest.get("recipes", []):
        record_path = root / str(entry.get("record", ""))
        if record_path.exists():
            record = yaml.safe_load(record_path.read_text(encoding="utf-8"))
            records[str(record.get("id"))] = record
    return records


def validate_prompt_package(
    path: Path | None, root: Path, require_complete: bool = True
) -> list[str]:
    errors: list[str] = []
    schema = _load_yaml(root / "prompt-dsl-v0.5.schema.yaml", errors, "Prompt DSL schema")
    manifest = _load_yaml(root / "manifest.yaml", errors, "recipe manifest")
    repository_root = root.parents[1]
    component_manifest = _load_yaml(
        repository_root / "components/component-library-v0.1/manifest.yaml",
        errors,
        "component manifest",
    )
    if errors:
        return errors
    if path is None:
        if require_complete:
            proof_dir = root / str(manifest.get("library", {}).get("proofs_dir", "proofs")) / "packages"
            paths = sorted(proof_dir.glob("*.yaml")) if proof_dir.exists() else []
            if len(paths) != 3:
                return ["strict Prompt DSL validation requires exactly three proof packages"]
            for proof_path in paths:
                errors.extend(validate_prompt_package(proof_path, root, require_complete=False))
        return errors

    package = _load_yaml(path, errors, path.name)
    if errors:
        return errors
    missing = _missing(package, schema.get("required_package_fields", []))
    if missing:
        errors.append("package missing fields: " + ",".join(missing))
    unknown = sorted(set(package) - set(schema.get("allowed_package_fields", [])))
    if unknown:
        errors.append("package contains unknown fields: " + ",".join(unknown))
    forbidden = {str(key).lower() for key in schema.get("forbidden_composition_keys", [])}
    composition_surface = dict(package)
    if isinstance(package.get("content"), dict):
        composition_surface["content"] = {
            key: value
            for key, value in package["content"].items()
            if key != "bindings"
        }
    for key in sorted(_find_forbidden_keys(composition_surface, forbidden)):
        errors.append(f"package contains forbidden composition key: {key}")

    if package.get("language") != "CSDL":
        errors.append("package language must equal CSDL")
    if str(package.get("version")) != "0.5":
        errors.append("package version must equal 0.5")
    if package.get("kind") != "generation-package":
        errors.append("package kind must equal generation-package")
    if not isinstance(package.get("id"), str) or not package.get("id"):
        errors.append("package id must be non-empty text")

    recipe_ref = package.get("recipe")
    missing_recipe = _missing(recipe_ref, schema.get("required_recipe_fields", []))
    if missing_recipe:
        errors.append("package recipe missing fields: " + ",".join(missing_recipe))
        recipe = None
    else:
        recipes = _load_records(root, manifest)
        recipe = recipes.get(str(recipe_ref.get("id")))
        if recipe is None:
            if require_complete or manifest.get("recipes"):
                errors.append(f"package recipe is undeclared: {recipe_ref.get('id')}")
        else:
            if recipe_ref.get("slug") != recipe.get("slug"):
                errors.append("package recipe slug must match recipe record")
            if recipe_ref.get("version") != recipe.get("version"):
                errors.append("package recipe version must match recipe record")

    for field, schema_field in (
        ("semantic_intent", "required_semantic_intent_fields"),
        ("content", "required_content_fields"),
        ("generation_constraints", "required_generation_constraint_fields"),
        ("provenance", "required_provenance_fields"),
    ):
        missing_fields = _missing(package.get(field), schema.get(schema_field, []))
        if missing_fields:
            errors.append(f"package {field} missing fields: {','.join(missing_fields)}")

    content = package.get("content")
    if isinstance(content, dict) and not isinstance(content.get("bindings"), dict):
        errors.append("package content.bindings must be a mapping")
    elif isinstance(content, dict) and recipe is not None:
        bindings = content.get("bindings", {})
        required_bindings = set(recipe.get("content_contract", {}).get("required", []))
        optional_bindings = set(recipe.get("content_contract", {}).get("optional", []))
        missing_bindings = sorted(required_bindings - set(bindings))
        unknown_bindings = sorted(set(bindings) - required_bindings - optional_bindings)
        if missing_bindings:
            errors.append(
                "package content bindings missing recipe fields: "
                + ",".join(missing_bindings)
            )
        if unknown_bindings:
            errors.append(
                "package content bindings contain unknown recipe fields: "
                + ",".join(unknown_bindings)
            )

    semantic_intent = package.get("semantic_intent")
    if isinstance(semantic_intent, dict) and recipe is not None:
        if semantic_intent.get("scenario") not in recipe.get("allowed_scenarios", []):
            errors.append("package scenario is not allowed by recipe")
        if semantic_intent.get("mechanism") != recipe.get("prompt_dsl", {}).get(
            "semantic_intent"
        ):
            errors.append("package mechanism must match recipe semantic intent")

    components_by_name = {
        component["name"]: component for component in component_manifest.get("components", [])
    }
    instances = package.get("component_instances")
    if not isinstance(instances, list):
        errors.append("package component_instances must be a list")
        instances = []
    instance_ids: list[str] = []
    instance_contracts: dict[str, dict[str, Any]] = {}
    for index, instance in enumerate(instances, start=1):
        label = f"package instance {index}"
        missing_instance = _missing(instance, schema.get("required_instance_fields", []))
        if missing_instance:
            errors.append(f"{label} missing fields: {','.join(missing_instance)}")
            continue
        unknown_instance = sorted(set(instance) - set(schema.get("allowed_instance_fields", [])))
        if unknown_instance:
            errors.append(f"{label} contains unknown fields: {','.join(unknown_instance)}")
        instance_id = instance.get("id")
        if not isinstance(instance_id, str) or not instance_id:
            errors.append(f"{label} id must be non-empty text")
            continue
        instance_ids.append(instance_id)
        component = components_by_name.get(instance.get("component"))
        if component is None:
            errors.append(f"{label} component is not public: {instance.get('component')}")
            continue
        instance_contracts[instance_id] = component
        attributes = instance.get("attributes", {})
        if not isinstance(attributes, dict):
            errors.append(f"{label} attributes must be a mapping")
            attributes = {}
        component_dsl = component.get("prompt_dsl", {})
        required_component_fields = set(component_dsl.get("required_fields", []))
        optional_component_fields = set(component_dsl.get("optional_fields", []))
        provided_component_fields = {"id", "role"} | set(attributes)
        missing_component_fields = sorted(
            required_component_fields - provided_component_fields
        )
        unknown_component_attributes = sorted(
            set(attributes)
            - required_component_fields
            - optional_component_fields
        )
        if missing_component_fields:
            errors.append(
                f"{label} component contract missing fields: "
                + ",".join(missing_component_fields)
            )
        if unknown_component_attributes:
            errors.append(
                f"{label} component attributes contain unknown fields: "
                + ",".join(unknown_component_attributes)
            )
        if recipe is not None:
            ingredients = recipe.get("ingredients", {})
            recipe_components = {
                ingredient["component"]
                for group in ("required", "optional")
                for ingredient in ingredients.get(group, [])
            }
            if instance.get("component") not in recipe_components:
                errors.append(
                    f"{label} component is unsupported by recipe {recipe.get('slug')}"
                )
    if len(instance_ids) != len(set(instance_ids)):
        errors.append("package instance ids must be unique")

    if recipe is not None:
        counts = Counter(instance.get("component") for instance in instances)
        for group in ("required", "optional"):
            for ingredient in recipe.get("ingredients", {}).get(group, []):
                count = counts.get(ingredient["component"], 0)
                if count < ingredient["min"] or count > ingredient["max"]:
                    errors.append(
                        f"package {ingredient['component']} count must be between "
                        f"{ingredient['min']} and {ingredient['max']}"
                    )

    relations = package.get("relations")
    if not isinstance(relations, list):
        errors.append("package relations must be a list")
        relations = []
    relation_types = component_manifest.get("vocabulary", {}).get("relations", [])
    for index, relation in enumerate(relations, start=1):
        label = f"package relation {index}"
        missing_relation = _missing(relation, schema.get("required_relation_fields", []))
        if missing_relation:
            errors.append(f"{label} missing fields: {','.join(missing_relation)}")
            continue
        subject = relation.get("subject")
        target = relation.get("object")
        relation_type = relation.get("type")
        if subject not in instance_contracts:
            errors.append(f"{label} subject is undeclared: {subject}")
        if target not in instance_contracts:
            errors.append(f"{label} object is undeclared: {target}")
        if relation_type not in relation_types:
            errors.append(f"{label} type is not public: {relation_type}")
        if (
            subject in instance_contracts
            and target in instance_contracts
            and relation_type in relation_types
            and not _relation_is_allowed(
                instance_contracts[subject], instance_contracts[target], relation_type
            )
        ):
            errors.append(f"{label} is not allowed by component contracts")

    generation = package.get("generation_constraints", {})
    expression = generation.get("expression")
    if expression not in schema.get("enums", {}).get("expression", []):
        errors.append("package generation expression is invalid")
    if recipe is not None:
        level = recipe.get("expression_levels", {}).get(expression, {})
        if level.get("status") == "forbidden":
            errors.append(f"package expression {expression} is forbidden by recipe")
        if generation.get("hard_exclusions") != recipe.get("hard_exclusions"):
            errors.append("package hard_exclusions must match the recipe contract")
    canvas = generation.get("canvas")
    expected_canvas = schema.get("defaults", {}).get("canvas")
    if isinstance(canvas, dict) and canvas != expected_canvas:
        errors.append("package canvas must equal the canonical DSL default")
    presentation = generation.get("presentation")
    if isinstance(presentation, dict):
        reading_path = presentation.get("reading_path")
        if reading_path not in schema.get("enums", {}).get("reading_path", []):
            errors.append("package reading_path is invalid")
        if recipe is not None and presentation.get(
            "negative_space_percent"
        ) != recipe.get("presentation", {}).get("negative_space_percent"):
            errors.append("package negative-space range must match recipe")
    output = generation.get("output")
    if isinstance(output, dict) and output != schema.get("defaults", {}).get("output"):
        errors.append("package output must equal the canonical DSL default")

    serialized = yaml.safe_dump(package, allow_unicode=True, sort_keys=False)
    for token in schema.get("forbidden_placeholders", []):
        if _contains_token(serialized, str(token)):
            errors.append(f"package contains forbidden marker: {token}")
    return errors


def validate_prompt_library(root: Path, require_complete: bool = True) -> list[str]:
    return validate_prompt_package(None, root, require_complete=require_complete)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_prompt_dsl.py PACKAGE_OR_LIBRARY_ROOT")
        return 2
    path = Path(sys.argv[1])
    if path.is_dir():
        errors = validate_prompt_library(path)
    else:
        root = path.parents[2] if "proofs" in path.parts else path.parent
        errors = validate_prompt_package(path, root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Prompt DSL v0.5 valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
