from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected YAML mapping: {path}")
    return value


def derive_analytical_proof(
    family: str,
    contract: dict[str, Any],
    dataset_document: dict[str, Any],
    dataset_path: str,
) -> dict[str, Any]:
    dataset = dataset_document["dataset"]
    records = dataset["records"]
    derived: dict[str, Any]
    if family == "histogram":
        derived = {
            "total_count": sum(record["count"] for record in records),
            "bins": [
                [record["bin_start"], record["bin_end"], record["count"]]
                for record in records
            ],
        }
    elif family == "boxplot":
        derived = {
            "five_number_summaries": [
                [
                    record["group"],
                    record["minimum"],
                    record["q1"],
                    record["median"],
                    record["q3"],
                    record["maximum"],
                ]
                for record in records
            ]
        }
    elif family == "intervalplot":
        derived = {
            "intervals": [
                [record["label"], record["lower"], record["estimate"], record["upper"]]
                for record in records
            ]
        }
    elif family == "bullet":
        derived = {
            "comparisons": [
                [
                    record["label"],
                    record["actual"],
                    record["target"],
                    record["range_min"],
                    record["range_max"],
                ]
                for record in records
            ]
        }
    elif family == "gantt":
        derived = {
            "intervals": [
                [record["task"], record["start"], record["end"], record["depends_on"]]
                for record in records
            ]
        }
    elif family == "sankey":
        inbound: dict[str, float] = {}
        outbound: dict[str, float] = {}
        for record in records:
            value = float(record["value"])
            outbound[record["source"]] = outbound.get(record["source"], 0.0) + value
            inbound[record["target"]] = inbound.get(record["target"], 0.0) + value
        internal_nodes = sorted(set(inbound) & set(outbound))
        derived = {
            "inbound": inbound,
            "outbound": outbound,
            "internal_balance": {
                node: round(inbound[node] - outbound[node], 10)
                for node in internal_nodes
            },
        }
    else:
        raise ValueError(f"unsupported arsenal analytical family: {family}")

    return {
        "language": "CSDL",
        "version": "0.2-candidate",
        "kind": "analytical-candidate-proof",
        "id": f"proof-{family}",
        "family": family,
        "dataset": {
            "id": dataset["id"],
            "version": dataset["version"],
            "path": dataset_path,
            "status": dataset["status"],
            "source": dataset["provenance"]["source"],
        },
        "intent": contract["intent"],
        "internal_marks": contract["internal_marks"],
        "candidate_components": contract["candidate_components"],
        "encoding_invariants": contract["encoding_invariants"],
        "fields": dataset["fields"],
        "records": records,
        "derived": derived,
        "provenance": {
            "evidence": "synthetic_fixed_data",
            "builder": "tools/build_arsenal_expansion.py",
            "deterministic": True,
        },
    }


def derive_index(root: Path) -> dict[str, Any]:
    manifest = _load(root / "manifest.yaml")
    return {
        "extension": manifest["extension"]["id"],
        "version": manifest["extension"]["version"],
        "status": manifest["extension"]["status"],
        "recipe_candidate_count": len(manifest["recipes"]),
        "component_candidate_count": len(manifest["components"]),
        "relation_candidate_count": len(manifest["relations"]),
        "analytical_family_candidate_count": len(manifest["analytical_families"]),
        "recipes": [
            {"id": entry["id"], "name": entry["name"], "record": entry["record"]}
            for entry in manifest["recipes"]
        ],
        "components": [
            {"name": entry["name"], "record": entry["record"]}
            for entry in manifest["components"]
        ],
        "relations": manifest["relations"],
        "analytical_families": manifest["analytical_families"],
        "targets": manifest["targets"],
    }


def derive_compatibility(root: Path) -> dict[str, Any]:
    manifest = _load(root / "manifest.yaml")
    recipes = []
    for entry in manifest["recipes"]:
        recipe = _load(root / entry["record"])
        ingredients = recipe["ingredients"]["required"] + recipe["ingredients"]["optional"]
        recipes.append(
            {
                "id": recipe["id"],
                "name": recipe["name"],
                "distinguishes_from": recipe["distinguishes_from"],
                "components": [ingredient["component"] for ingredient in ingredients],
                "relations": sorted(
                    {
                        relation["type"]
                        for group in recipe["relations"].values()
                        for relation in group
                    }
                ),
                "expression_modes": recipe["expression_modes"],
            }
        )
    families = _load(root / "analytics/families.yaml")["families"]
    return {
        "extension": manifest["extension"]["id"],
        "baseline": manifest["baseline"],
        "targets": manifest["targets"],
        "recipes": recipes,
        "analytical_families": [
            {
                "family": family,
                "compatible_recipes": contract["compatible_recipes"],
                "candidate_components": contract["candidate_components"],
            }
            for family, contract in families.items()
        ],
    }


def build_arsenal_expansion(root: Path) -> list[Path]:
    manifest = _load(root / "manifest.yaml")
    families = _load(root / "analytics/families.yaml")["families"]
    outputs: list[Path] = []

    proof_root = root / "analytics/proofs"
    proof_root.mkdir(parents=True, exist_ok=True)
    for entry in manifest["analytical_datasets"]:
        family = entry["family"]
        dataset_path = entry["path"]
        proof = derive_analytical_proof(
            family,
            families[family],
            _load(root / dataset_path),
            dataset_path,
        )
        output = proof_root / f"{entry['id']}.yaml"
        output.write_text(
            yaml.safe_dump(proof, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        outputs.append(output)

    generated_root = root / "generated"
    generated_root.mkdir(parents=True, exist_ok=True)
    for filename, document in (
        ("index.yaml", derive_index(root)),
        ("compatibility.yaml", derive_compatibility(root)),
    ):
        output = generated_root / filename
        output.write_text(
            yaml.safe_dump(document, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        outputs.append(output)
    return outputs


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/build_arsenal_expansion.py ROOT")
        return 2
    try:
        outputs = build_arsenal_expansion(Path(sys.argv[1]))
    except (KeyError, OSError, TypeError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print(
        "arsenal expansion built: "
        + ", ".join(str(path.name) for path in outputs)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
