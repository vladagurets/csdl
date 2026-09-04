from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.validate_accessibility_mode import contrast_ratio, derive_source_semantics


def _natural_path_key(path: Path) -> tuple[tuple[int, int | str], ...]:
    return tuple(
        (0, int(part)) if part.isdecimal() else (1, part.casefold())
        for part in re.split(r"([0-9]+)", path.as_posix())
        if part
    )


def _digest(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def load_source_reference(source: dict[str, Any], root: Path) -> dict[str, Any]:
    repository_root = root.parents[1]
    reference = source["source_reference"]
    path = repository_root / reference["path"]
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError("accessibility source reference must contain a YAML mapping")
    if document.get("kind") != reference.get("kind"):
        raise ValueError("accessibility source reference kind must match canonical source")
    return document


def _text_checks(
    elements: list[dict[str, Any]],
    profile_name: str,
    profile: dict[str, Any],
    thresholds: dict[str, Any],
) -> list[dict[str, Any]]:
    values = profile["tokens"]
    checks = []
    for element in elements:
        if profile_name not in element.get("profiles", [profile_name]):
            continue
        ratio = contrast_ratio(
            values[element["foreground"]], values[element["background"]]
        )
        minimum = thresholds["minimum_text_contrast"]
        checks.append(
            {
                "id": element["id"],
                "role": element["role"],
                "foreground": element["foreground"],
                "background": element["background"],
                "ratio": round(ratio, 6),
                "minimum": minimum,
                "passes": ratio >= minimum,
            }
        )
    return checks


def _graphic_checks(
    objects: list[dict[str, Any]],
    profile_name: str,
    profile: dict[str, Any],
    thresholds: dict[str, Any],
) -> list[dict[str, Any]]:
    values = profile["tokens"]
    checks = []
    for item in objects:
        if profile_name not in item.get("profiles", [profile_name]):
            continue
        ratio = contrast_ratio(
            values[item["foreground"]], values[item["background"]]
        )
        minimum = thresholds["minimum_non_text_contrast"]
        minimum_stroke = thresholds["critical_stroke_px"]
        checks.append(
            {
                "id": item["id"],
                "role": item["role"],
                "component": item.get("component"),
                "foreground": item["foreground"],
                "background": item["background"],
                "ratio": round(ratio, 6),
                "minimum": minimum,
                "stroke_px": item.get("stroke_px"),
                "minimum_stroke_px": minimum_stroke,
                "passes": ratio >= minimum
                and (
                    not item.get("meaningful", True)
                    or item.get("stroke_px", 0) >= minimum_stroke
                ),
            }
        )
    return checks


def derive_accessibility_package(
    source: dict[str, Any], root: Path
) -> dict[str, Any]:
    tokens = yaml.safe_load((root / "contracts/tokens.yaml").read_text(encoding="utf-8"))
    contrast = yaml.safe_load((root / "contracts/contrast.yaml").read_text(encoding="utf-8"))
    fallbacks = yaml.safe_load((root / "contracts/fallbacks.yaml").read_text(encoding="utf-8"))
    source_document = load_source_reference(source, root)
    semantic_signature = _digest(
        {
            "source_reference": source["source_reference"],
            "scenario": source["scenario"],
            "semantic_encodings": source["semantic_encodings"],
        }
    )
    profile_results = []
    for profile_name in source["profiles"]:
        profile = tokens["profiles"][profile_name]
        thresholds = contrast["profiles"][profile_name]
        profile_results.append(
            {
                "profile": profile_name,
                "semantic_signature": semantic_signature,
                "thresholds": thresholds,
                "stroke_widths": profile["stroke_widths"],
                "token_values": profile["tokens"],
                "text_checks": _text_checks(
                    source["text_elements"], profile_name, profile, thresholds
                ),
                "graphical_checks": _graphic_checks(
                    source["graphical_objects"], profile_name, profile, thresholds
                ),
                "color_vision_profiles": fallbacks["color_vision"]["profiles"],
            }
        )
    return {
        "language": "CSDL",
        "version": "0.1",
        "kind": "accessibility-package",
        "id": source["id"],
        "scenario": source["scenario"],
        "source_reference": source["source_reference"],
        "semantic_source_digest": _digest(source_document),
        "source_semantics": derive_source_semantics(source_document),
        "profiles": source["profiles"],
        "profile_results": profile_results,
        "text_elements": source["text_elements"],
        "graphical_objects": source["graphical_objects"],
        "semantic_encodings": source["semantic_encodings"],
        "output": {**source["output"], "profiles": source["profiles"]},
        "provenance": {
            "proof_source": source.get("source_path"),
            "semantic_source": source["source_reference"]["path"],
            "accessibility_contract": "night-mode-v0.1@0.1.0",
            "builder": "tools/build_accessibility_mode.py",
            "evidence": "deterministic_specification",
            "deterministic": True,
        },
    }


def derive_contrast_matrix(
    tokens: dict[str, Any], contrast: dict[str, Any]
) -> dict[str, Any]:
    profiles = []
    for profile_name, profile in tokens["profiles"].items():
        values = profile["tokens"]
        thresholds = contrast["profiles"][profile_name]
        pairings = []
        for pairing in profile["allowed_pairings"]:
            ratio = contrast_ratio(
                values[pairing["foreground"]], values[pairing["background"]]
            )
            minimum = thresholds[
                "minimum_text_contrast"
                if pairing["kind"] == "text"
                else "minimum_non_text_contrast"
            ]
            pairings.append(
                {
                    **pairing,
                    "ratio": round(ratio, 6),
                    "minimum": minimum,
                    "passes": ratio >= minimum,
                }
            )
        profiles.append(
            {
                "profile": profile_name,
                "thresholds": thresholds,
                "pairings": pairings,
            }
        )
    return {
        "library": "night-mode-v0.1",
        "version": "0.1.0",
        "calculation": contrast["calculation"],
        "profiles": profiles,
    }


def derive_index(root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    proofs = []
    for proof in manifest["proofs"]:
        source_path = root / proof["source"]
        profiles: list[str] = []
        if source_path.is_file():
            source = yaml.safe_load(source_path.read_text(encoding="utf-8"))
            profiles = source.get("profiles", [])
        proofs.append({**proof, "profiles": profiles})
    return {
        "library": manifest["library"]["id"],
        "version": manifest["library"]["version"],
        "profile_count": len(manifest["profile_order"]),
        "proof_count": len(manifest["proofs"]),
        "profiles": manifest["profile_order"],
        "proofs": proofs,
    }


def derive_compatibility(
    manifest: dict[str, Any], source: dict[str, Any]
) -> dict[str, Any]:
    return {
        "library": manifest["library"]["id"],
        "version": manifest["library"]["version"],
        "profiles": manifest["profile_order"],
        "prompt_dsl": source["prompt_dsl"],
        "public_component_count": len(source["components"]),
        "public_recipe_count": len(source["recipes"]),
        "analytical_family_count": len(source["analytical_mode"]["families"]),
        "components": source["components"],
        "recipes": source["recipes"],
        "analytical_mode": source["analytical_mode"],
    }


def derive_raster_hashes(
    repository_root: Path, accepted_paths: list[str] | None = None
) -> dict[str, Any]:
    if accepted_paths is None:
        accepted_roots = [
            repository_root / "pilots",
            repository_root / "patterns",
            repository_root / "references/canonical",
        ]
        paths = sorted(
            [
                path
                for accepted_root in accepted_roots
                for path in accepted_root.rglob("*.png")
                if path.is_file() and "drafts" not in path.parts
            ],
            key=_natural_path_key,
        )
    else:
        paths = [
            repository_root / path
            for path in accepted_paths
            if (repository_root / path).is_file()
        ]
    files = [
        {
            "path": path.relative_to(repository_root).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        for path in paths
    ]
    return {
        "library": "night-mode-v0.1",
        "version": "0.1.0",
        "purpose": "Pin every tracked accepted raster byte before and after Milestone 6.",
        "file_count": len(files),
        "files": files,
    }


def build_accessibility_mode(
    root: Path, require_complete: bool = True
) -> list[Path]:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    tokens = yaml.safe_load((root / "contracts/tokens.yaml").read_text(encoding="utf-8"))
    contrast = yaml.safe_load((root / "contracts/contrast.yaml").read_text(encoding="utf-8"))
    compatibility_source = yaml.safe_load(
        (root / "contracts/compatibility.yaml").read_text(encoding="utf-8")
    )
    outputs: list[Path] = []
    for proof in manifest["proofs"]:
        source_path = root / proof["source"]
        if not source_path.is_file():
            if require_complete:
                raise ValueError(f"missing accessibility proof source: {proof['source']}")
            continue
        source = yaml.safe_load(source_path.read_text(encoding="utf-8"))
        source["source_path"] = proof["source"]
        package = derive_accessibility_package(source, root)
        output = root / proof["package"]
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            yaml.safe_dump(package, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        outputs.append(output)
    raster_hash_path = root / manifest["library"]["raster_hashes"]
    accepted_paths = None
    if require_complete and raster_hash_path.is_file():
        baseline = yaml.safe_load(raster_hash_path.read_text(encoding="utf-8"))
        accepted_paths = [entry["path"] for entry in baseline.get("files", [])]

    derived = [
        (root / manifest["library"]["index"], derive_index(root, manifest)),
        (
            root / manifest["library"]["contrast_matrix"],
            derive_contrast_matrix(tokens, contrast),
        ),
        (
            root / manifest["library"]["compatibility"],
            derive_compatibility(manifest, compatibility_source),
        ),
        (
            raster_hash_path,
            derive_raster_hashes(root.parents[1], accepted_paths),
        ),
    ]
    for path, document in derived:
        path.write_text(
            yaml.safe_dump(document, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        outputs.append(path)
    return outputs


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("usage: python tools/build_accessibility_mode.py ROOT [--incomplete]")
        return 2
    require_complete = len(sys.argv) == 2
    if not require_complete and sys.argv[2] != "--incomplete":
        print("usage: python tools/build_accessibility_mode.py ROOT [--incomplete]")
        return 2
    try:
        outputs = build_accessibility_mode(
            Path(sys.argv[1]), require_complete=require_complete
        )
    except (KeyError, OSError, TypeError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print("accessibility mode built: " + ", ".join(path.name for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
