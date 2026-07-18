from __future__ import annotations

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


def _missing_fields(value: Any, required: list[str]) -> list[str]:
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


def _reference_path(root: Path, repository_root: Path, value: str) -> Path:
    local = root / value
    if local.exists():
        return local
    return repository_root / value


def _relation_is_allowed(
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


def _validate_analytical_contract(
    proof: dict[str, Any],
    repository_root: Path,
    errors: list[str],
    label: str,
) -> None:
    contract = proof.get("quantitative_contract")
    if not isinstance(contract, dict):
        errors.append(f"{label} analytical proof must define quantitative_contract")
        return
    required = {"dataset", "series", "periods", "domain", "values", "direct_labels"}
    missing = sorted(required - set(contract))
    if missing:
        errors.append(f"{label} quantitative_contract missing fields: {','.join(missing)}")
        return
    dataset_path = repository_root / str(contract.get("dataset"))
    try:
        source = yaml.safe_load(dataset_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        errors.append(f"{label} analytical dataset must be readable YAML: {error}")
        return
    dataset = source.get("dataset", {})
    series_name = contract.get("series")
    series = dataset.get("series", {}).get(series_name)
    if not isinstance(series, dict):
        errors.append(f"{label} quantitative series does not exist: {series_name}")
        return
    if contract.get("periods") != dataset.get("weeks"):
        errors.append(f"{label} quantitative periods must match fixed dataset order")
    if contract.get("values") != series.get("values"):
        errors.append(f"{label} quantitative values must match fixed dataset")
    if series.get("unit") == "percent" and contract.get("domain") != source.get("constraints", {}).get(
        "percent_domain"
    ):
        errors.append(f"{label} percent domain must match fixed dataset")
    labels = contract.get("direct_labels")
    if not isinstance(labels, list) or len(labels) != len(series.get("values", [])):
        errors.append(f"{label} must directly label every quantitative value")
    instance_components = {instance.get("component") for instance in proof.get("instances", [])}
    if "label" not in instance_components:
        errors.append(f"{label} analytical proof must contain a Label instance")
    if "legend" in instance_components:
        errors.append(f"{label} current single-series proof must not contain Legend")


def validate_component_proofs(root: Path, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    repository_root = root.parents[1]
    manifest = _load_yaml(root / "manifest.yaml", errors, "component manifest")
    schema = _load_yaml(root / "schema.yaml", errors, "component schema")
    if errors:
        return errors

    components = manifest.get("components", [])
    components_by_slug = {
        component.get("slug"): component
        for component in components
        if isinstance(component, dict) and component.get("slug")
    }
    family_order = schema.get("family_order", [])
    proof_order = schema.get("proof_order", [])
    proof_dir = root / manifest.get("library", {}).get("proofs_dir", "proofs")
    paths = sorted(proof_dir.glob("*.yaml")) if proof_dir.exists() else []
    proofs = [_load_yaml(path, errors, path.name) for path in paths]
    if errors:
        return errors

    modes = [proof.get("mode") for proof in proofs]
    if require_complete and modes != proof_order:
        errors.append("proofs must contain exactly editorial, structural, and analytical")
    if not require_complete:
        expected_subsequence = [mode for mode in proof_order if mode in modes]
        if modes != expected_subsequence:
            errors.append("proofs must follow canonical mode order")
    if len(modes) != len(set(modes)):
        errors.append("proof modes must be unique")

    required_fields = schema.get("required_proof_fields", [])
    required_instance_fields = schema.get("required_instance_fields", [])
    required_relation_fields = schema.get("required_proof_relation_fields", [])
    forbidden_keys = {str(key).lower() for key in schema.get("forbidden_proof_keys", [])}
    relation_types = schema.get("relation_types", [])
    levels = schema.get("enums", {}).get("level", [])

    for actual_path, proof in zip(paths, proofs, strict=True):
        proof_id = str(proof.get("id", "??"))
        label = f"proof {proof_id}"
        missing = _missing_fields(proof, required_fields)
        if missing:
            errors.append(f"{label} missing fields: {','.join(missing)}")
        unknown = sorted(set(proof) - set(schema.get("allowed_proof_fields", [])))
        if unknown:
            errors.append(f"{label} contains unknown fields: {','.join(unknown)}")
        for key in sorted(_find_forbidden_keys(proof, forbidden_keys)):
            errors.append(f"{label} contains forbidden composition key: {key}")

        mode = proof.get("mode")
        if mode not in proof_order:
            errors.append(f"{label} mode is invalid")
        expected_path = root / f"proofs/{proof_id}-{mode}.yaml"
        if actual_path != expected_path:
            errors.append(f"{label} path must equal proofs/{proof_id}-{mode}.yaml")
        family = proof.get("family")
        if family not in family_order:
            errors.append(f"{label} family is invalid")
        if proof.get("expression") not in levels:
            errors.append(f"{label} expression is invalid")
        evidence = proof.get("evidence")
        if not isinstance(evidence, str) or not evidence:
            errors.append(f"{label} evidence must be non-empty text")
        elif not _reference_path(root, repository_root, evidence).exists():
            errors.append(f"{label} evidence path does not exist: {evidence}")
        if not isinstance(proof.get("content"), dict) or not proof.get("content"):
            errors.append(f"{label} content must be a non-empty mapping")

        instances = proof.get("instances")
        if not isinstance(instances, list) or not instances:
            errors.append(f"{label} instances must be a non-empty list")
            instances = []
        instance_ids: list[str] = []
        instance_components: dict[str, dict[str, Any]] = {}
        for index, instance in enumerate(instances, start=1):
            instance_label = f"{label} instance {index}"
            missing_instance = _missing_fields(instance, required_instance_fields)
            if missing_instance:
                errors.append(f"{instance_label} missing fields: {','.join(missing_instance)}")
                continue
            unknown_instance = sorted(set(instance) - set(schema.get("allowed_instance_fields", [])))
            if unknown_instance:
                errors.append(
                    f"{instance_label} contains unknown fields: {','.join(unknown_instance)}"
                )
            instance_id = instance.get("id")
            component_slug = instance.get("component")
            if not isinstance(instance_id, str) or not instance_id:
                errors.append(f"{instance_label} id must be non-empty text")
                continue
            instance_ids.append(instance_id)
            component = components_by_slug.get(component_slug)
            if component is None:
                errors.append(f"{instance_label} component is undeclared: {component_slug}")
                continue
            instance_components[instance_id] = component
            if family not in component.get("compatible_families", []):
                errors.append(f"{instance_label} component is incompatible with family {family}")
            attributes = instance.get("attributes")
            if not isinstance(attributes, dict):
                errors.append(f"{instance_label} attributes must be a mapping")
            else:
                prompt_dsl = component.get("prompt_dsl", {})
                required_attributes = set(prompt_dsl.get("required_fields", [])) - {"id"}
                allowed_attributes = required_attributes | set(prompt_dsl.get("optional_fields", []))
                missing_attributes = sorted(required_attributes - set(attributes))
                unknown_attributes = sorted(set(attributes) - allowed_attributes)
                if missing_attributes:
                    errors.append(
                        f"{instance_label} attributes missing fields: {','.join(missing_attributes)}"
                    )
                if unknown_attributes:
                    errors.append(
                        f"{instance_label} attributes contain unknown fields: {','.join(unknown_attributes)}"
                    )
        if len(instance_ids) != len(set(instance_ids)):
            errors.append(f"{label} instance ids must be unique")

        counts = Counter(
            instance.get("component")
            for instance in instances
            if isinstance(instance, dict) and instance.get("component")
        )
        for component_slug, count in counts.items():
            component = components_by_slug.get(component_slug)
            if component is None:
                continue
            limit = component.get("expression_limits", {}).get(proof.get("expression"), {})
            if limit.get("status") == "forbidden":
                errors.append(f"{label} uses {component_slug} at a forbidden expression level")
            max_count = limit.get("max_count")
            if isinstance(max_count, int) and count > max_count:
                errors.append(f"{label} exceeds {component_slug} max_count for expression")

        relations = proof.get("relations")
        if not isinstance(relations, list):
            errors.append(f"{label} relations must be a list")
            relations = []
        for index, relation in enumerate(relations, start=1):
            relation_label = f"{label} relation {index}"
            missing_relation = _missing_fields(relation, required_relation_fields)
            if missing_relation:
                errors.append(f"{relation_label} missing fields: {','.join(missing_relation)}")
                continue
            unknown_relation = sorted(
                set(relation) - set(schema.get("allowed_proof_relation_fields", []))
            )
            if unknown_relation:
                errors.append(
                    f"{relation_label} contains unknown fields: {','.join(unknown_relation)}"
                )
            subject_id = relation.get("subject")
            target_id = relation.get("object")
            relation_type = relation.get("type")
            if subject_id not in instance_components:
                errors.append(f"{relation_label} subject is undeclared: {subject_id}")
            if target_id not in instance_components:
                errors.append(f"{relation_label} object is undeclared: {target_id}")
            if relation_type not in relation_types:
                errors.append(f"{relation_label} type is invalid")
            if (
                subject_id in instance_components
                and target_id in instance_components
                and relation_type in relation_types
                and not _relation_is_allowed(
                    instance_components[subject_id],
                    instance_components[target_id],
                    relation_type,
                )
            ):
                errors.append(f"{relation_label} is not allowed by component contracts")

        if mode == "analytical":
            _validate_analytical_contract(proof, repository_root, errors, label)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_component_proofs.py COMPONENT_LIBRARY_ROOT")
        return 2
    errors = validate_component_proofs(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("component proofs valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
