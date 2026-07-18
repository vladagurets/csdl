from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _load_inputs(root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    schema = yaml.safe_load((root / "schema.yaml").read_text(encoding="utf-8"))
    return manifest, schema


def derive_index(manifest: dict[str, Any]) -> dict[str, Any]:
    library = manifest["library"]
    components = []
    for component in manifest.get("components", []):
        components.append(
            {
                "id": component["id"],
                "slug": component["slug"],
                "name": component["name"],
                "category": component["category"],
                "evidence_level": component["evidence_level"],
                "specification": component["specification"],
                "compatible_families": component["compatible_families"],
                "allowed_levels": [
                    level
                    for level, contract in component["expression_limits"].items()
                    if contract["status"] != "forbidden"
                ],
                "prompt_dsl_syntax": component["prompt_dsl"]["syntax"],
            }
        )
    return {
        "library": library["id"],
        "version": library["version"],
        "component_count": len(components),
        "components": components,
    }


def derive_compatibility(
    manifest: dict[str, Any],
    schema: dict[str, Any],
) -> dict[str, Any]:
    library = manifest["library"]
    families = schema["family_order"]
    component_rows: list[dict[str, Any]] = []
    by_family = {family: [] for family in families}
    for component in manifest.get("components", []):
        compatible = set(component["compatible_families"])
        compatible_state = "conditional" if component["evidence_level"] == "constrained" else "direct"
        states = {
            family: compatible_state if family in compatible else "incompatible"
            for family in families
        }
        component_rows.append(
            {
                "id": component["id"],
                "slug": component["slug"],
                "families": states,
            }
        )
        for family in compatible:
            by_family[family].append(
                {"component": component["slug"], "status": compatible_state}
            )
    return {
        "library": library["id"],
        "version": library["version"],
        "families": families,
        "components": component_rows,
        "by_family": [
            {"family": family, "components": by_family[family]}
            for family in families
        ],
    }


def build_component_library(
    root: Path,
    require_complete: bool = True,
) -> tuple[Path, Path]:
    manifest, schema = _load_inputs(root)
    components = manifest.get("components", [])
    if require_complete and len(components) != manifest.get("library", {}).get("component_count"):
        raise ValueError("component library is incomplete")

    index = derive_index(manifest)
    compatibility = derive_compatibility(manifest, schema)
    index_path = root / manifest["library"]["index"]
    compatibility_path = root / manifest["library"]["compatibility"]
    index_path.write_text(
        yaml.safe_dump(index, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    compatibility_path.write_text(
        yaml.safe_dump(compatibility, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return index_path, compatibility_path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/build_component_library.py COMPONENT_LIBRARY_ROOT")
        return 2
    root = Path(sys.argv[1])
    try:
        index_path, compatibility_path = build_component_library(root)
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print(
        "component library built: "
        f"{index_path.relative_to(root)}, {compatibility_path.relative_to(root)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
