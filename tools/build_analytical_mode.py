from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _round(value: float) -> float:
    return round(value, 10)


def apply_transformations(dataset: dict[str, Any]) -> dict[str, list[Any]]:
    records = dataset.get("records", [])
    results: dict[str, list[Any]] = {}
    for transformation in dataset.get("transformations", []):
        operation = transformation["operation"]
        identifier = transformation["id"]
        inputs = transformation["inputs"]
        parameters = transformation.get("parameters", {})
        if operation == "rate":
            numerator, denominator = inputs
            multiplier = parameters.get("multiplier", 1)
            values = []
            for record in records:
                left, right = record.get(numerator), record.get(denominator)
                values.append(None if left is None or right in {None, 0} else _round(left / right * multiplier))
            results[identifier] = values
        elif operation == "conversion_rate":
            field = inputs[0]
            values = [record.get(field) for record in records]
            converted: list[Any] = []
            for index, value in enumerate(values):
                if index == 0:
                    converted.append(float(parameters.get("first_stage", 100)))
                else:
                    denominator = values[index - 1]
                    converted.append(None if value is None or denominator in {None, 0} else _round(value / denominator * 100))
            results[identifier] = converted
        elif operation == "cumulative_sum":
            start_field, delta_field = inputs
            current: float | int | None = None
            cumulative: list[Any] = []
            for record in records:
                kind = record.get("kind")
                if kind == parameters.get("start_kind", "start"):
                    current = record.get(start_field)
                elif kind == parameters.get("total_kind", "total"):
                    pass
                elif current is not None:
                    current += record.get(delta_field, 0)
                cumulative.append(current)
            results[identifier] = cumulative
        elif operation == "normalize":
            field = inputs[0]
            values = [record.get(field) for record in records]
            total = parameters.get("total", sum(value for value in values if value is not None))
            results[identifier] = [None if value is None or total == 0 else _round(value / total * 100) for value in values]
        elif operation == "identity":
            results[identifier] = [record.get(inputs[0]) for record in records]
        else:
            raise ValueError(f"unsupported analytical transformation: {operation}")
    return results


def derive_analytical_package(
    source: dict[str, Any], dataset_document: dict[str, Any], root: Path
) -> dict[str, Any]:
    dataset = dataset_document["dataset"]
    derived = apply_transformations(dataset)
    fields = {field["id"]: field for field in dataset["fields"]}
    bindings = source["encoding"]["bindings"]
    traceability = {
        channel: {
            "field": field_id,
            "type": fields[field_id]["type"],
            "unit": fields[field_id].get("unit"),
        }
        for channel, field_id in bindings.items()
        if isinstance(field_id, str) and field_id in fields
    }
    return {
        "language": "CSDL",
        "version": "0.1",
        "kind": "analytical-package",
        "id": source["id"],
        "dataset": {
            "id": dataset["id"],
            "version": dataset["version"],
            "path": source["dataset"],
            "source": dataset["provenance"]["source"],
        },
        "analytical_intent": source["analytical_intent"],
        "recipe": source["recipe"],
        "encoding": source["encoding"],
        "component_instances": source["component_instances"],
        "relations": source["relations"],
        "specification": {
            "family": source["family"],
            "fields": dataset["fields"],
            "records": dataset["records"],
            "ordering": dataset["ordering"],
            "missing_values": dataset["missing_values"],
            "transformations": dataset["transformations"],
            "derived": derived,
            "traceability": traceability,
        },
        "provenance": {
            "dataset_source": dataset["provenance"],
            "proof_source": source.get("source_path"),
            "evidence": "synthetic_fixed_data",
            "builder": "tools/build_analytical_mode.py",
            "deterministic": True,
        },
    }


def derive_index(manifest: dict[str, Any], contracts: dict[str, Any]) -> dict[str, Any]:
    return {
        "library": manifest["library"]["id"],
        "version": manifest["library"]["version"],
        "family_count": len(manifest["family_order"]),
        "dataset_count": len(manifest["datasets"]),
        "proof_count": len(manifest["proofs"]),
        "families": [
            {
                "family": family,
                "precise_rules": contracts["families"][family]["precise_rules"],
                "hard_exclusions": contracts["families"][family]["hard_exclusions"],
            }
            for family in manifest["family_order"]
        ],
        "proofs": manifest["proofs"],
    }


def derive_dataset_index(root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    datasets = []
    for entry in manifest["datasets"]:
        document = yaml.safe_load((root / entry["path"]).read_text(encoding="utf-8"))
        dataset = document["dataset"]
        datasets.append(
            {
                "id": dataset["id"],
                "version": dataset["version"],
                "title": dataset["title"],
                "status": dataset["status"],
                "path": entry["path"],
                "record_count": len(dataset["records"]),
                "field_count": len(dataset["fields"]),
                "source": dataset["provenance"]["source"],
            }
        )
    return {
        "library": manifest["library"]["id"],
        "version": manifest["library"]["version"],
        "datasets": datasets,
    }


def derive_compatibility(
    manifest: dict[str, Any], source: dict[str, Any]
) -> dict[str, Any]:
    return {
        "library": manifest["library"]["id"],
        "version": manifest["library"]["version"],
        "prompt_dsl": manifest["library"]["prompt_dsl_compatibility"],
        "public_component_count": manifest["library"]["public_component_count"],
        "public_recipe_count": manifest["library"]["public_recipe_count"],
        "families": [
            {"family": family, **source["families"][family]}
            for family in manifest["family_order"]
        ],
    }


def build_analytical_mode(root: Path, require_complete: bool = True) -> list[Path]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    contracts = yaml.safe_load((root / "contracts/families.yaml").read_text(encoding="utf-8"))
    compatibility_source = yaml.safe_load((root / "contracts/compatibility.yaml").read_text(encoding="utf-8"))
    outputs: list[Path] = []
    package_dir = root / "proofs/packages"
    if require_complete:
        package_dir.mkdir(parents=True, exist_ok=True)
    for proof in manifest["proofs"]:
        source_path = root / proof["source"]
        if not source_path.is_file():
            if require_complete:
                raise ValueError(f"missing analytical proof source: {proof['source']}")
            continue
        source = yaml.safe_load(source_path.read_text(encoding="utf-8"))
        source["source_path"] = proof["source"]
        dataset_document = yaml.safe_load((root / source["dataset"]).read_text(encoding="utf-8"))
        package = derive_analytical_package(source, dataset_document, root)
        output = root / proof["package"]
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(yaml.safe_dump(package, allow_unicode=True, sort_keys=False), encoding="utf-8")
        outputs.append(output)
    derived_outputs = [
        (root / manifest["library"]["index"], derive_index(manifest, contracts)),
        (root / manifest["library"]["dataset_index"], derive_dataset_index(root, manifest)),
        (root / manifest["library"]["compatibility"], derive_compatibility(manifest, compatibility_source)),
    ]
    for path, document in derived_outputs:
        path.write_text(yaml.safe_dump(document, allow_unicode=True, sort_keys=False), encoding="utf-8")
        outputs.append(path)
    return outputs


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("usage: python tools/build_analytical_mode.py ROOT [--incomplete]")
        return 2
    require_complete = len(sys.argv) == 2
    if not require_complete and sys.argv[2] != "--incomplete":
        print("usage: python tools/build_analytical_mode.py ROOT [--incomplete]")
        return 2
    try:
        outputs = build_analytical_mode(Path(sys.argv[1]), require_complete=require_complete)
    except (KeyError, OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print("analytical mode built: " + ", ".join(path.name for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
