from copy import deepcopy
from pathlib import Path
import shutil

import yaml

from tools.build_accessibility_mode import (
    build_accessibility_mode,
    derive_accessibility_package,
    derive_contrast_matrix,
)
from tools.validate_accessibility_mode import (
    validate_accessibility_package,
    validate_accessibility_source,
    validate_negative_fixture,
)


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "accessibility/night-mode-v0.1"


def valid_source() -> dict:
    return {
        "language": "CSDL",
        "version": "0.1",
        "kind": "accessibility-proof-source",
        "id": "proof-tooling",
        "scenario": "editorial-equivalence",
        "source_reference": {
            "kind": "generation-package",
            "path": "recipes/recipe-library-v0.5/proofs/packages/01-editorial.yaml",
        },
        "profiles": ["light", "night"],
        "text_elements": [
            {
                "id": "title",
                "role": "display",
                "foreground": "ink.primary",
                "background": "background.base",
            },
            {
                "id": "source",
                "role": "source",
                "foreground": "ink.secondary",
                "background": "background.base",
            },
        ],
        "graphical_objects": [
            {
                "id": "signal",
                "role": "signal",
                "component": "Signal",
                "foreground": "signal.primary",
                "background": "background.base",
                "stroke_px": 2,
                "meaningful": True,
            },
            {
                "id": "boundary",
                "role": "surface_boundary",
                "component": "Frame",
                "foreground": "line.strong",
                "background": "background.base",
                "stroke_px": 2,
                "meaningful": True,
            },
        ],
        "semantic_encodings": [
            {
                "meaning": "signal",
                "color_token": "signal.primary",
                "redundant_carriers": ["shape", "direct_label"],
                "target": "pulse",
                "area_percent": 4,
                "max_area_percent": 8,
            }
        ],
        "output": {
            "canvas": "1920x1080",
            "orientation": "landscape",
            "colorspace": "sRGB",
            "format": "deterministic-specification",
        },
    }


def test_accessibility_package_is_deterministic_and_preserves_source_digest() -> None:
    source = valid_source()
    assert validate_accessibility_source(source, LIBRARY) == []
    first = derive_accessibility_package(source, LIBRARY)
    second = derive_accessibility_package(deepcopy(source), LIBRARY)
    assert first == second
    assert first["semantic_source_digest"].startswith("sha256:")
    assert first["profile_results"][0]["semantic_signature"] == first["profile_results"][1]["semantic_signature"]
    assert validate_accessibility_package(first, LIBRARY) == []


def test_contrast_matrix_recomputes_exact_allowed_pairings() -> None:
    tokens = yaml.safe_load((LIBRARY / "contracts/tokens.yaml").read_text(encoding="utf-8"))
    contrast = yaml.safe_load((LIBRARY / "contracts/contrast.yaml").read_text(encoding="utf-8"))
    matrix = derive_contrast_matrix(tokens, contrast)
    assert [profile["profile"] for profile in matrix["profiles"]] == [
        "light",
        "night",
        "monochrome",
        "projector",
    ]
    assert all(pair["passes"] for profile in matrix["profiles"] for pair in profile["pairings"])


def test_partial_builder_outputs_are_byte_deterministic(tmp_path: Path) -> None:
    target = tmp_path / "accessibility/night-mode-v0.1"
    shutil.copytree(LIBRARY, target)
    repository = tmp_path
    shutil.copytree(ROOT / "components", repository / "components")
    shutil.copytree(ROOT / "recipes", repository / "recipes")
    shutil.copytree(ROOT / "analytics", repository / "analytics")
    outputs = build_accessibility_mode(target, require_complete=False)
    first = {path.name: path.read_bytes() for path in outputs}
    outputs = build_accessibility_mode(target, require_complete=False)
    second = {path.name: path.read_bytes() for path in outputs}
    assert first == second
    assert {
        "index.yaml",
        "contrast-matrix.yaml",
        "compatibility.yaml",
        "raster-hashes.yaml",
    } <= set(first)


def test_package_validator_rejects_global_accessibility_mutations() -> None:
    package = derive_accessibility_package(valid_source(), LIBRARY)

    mutated = deepcopy(package)
    mutated["profile_results"][0]["text_checks"][0]["ratio"] = 1.0
    assert "accessibility text contrast must match independent calculation" in validate_accessibility_package(mutated, LIBRARY)

    mutated = deepcopy(package)
    mutated["semantic_encodings"][0]["redundant_carriers"] = []
    assert "color cannot be the sole carrier of meaning" in validate_accessibility_package(mutated, LIBRARY)

    mutated = deepcopy(package)
    mutated["profile_results"][1]["semantic_signature"] = "sha256:mutated"
    assert "light and night semantic signatures must remain equivalent" in validate_accessibility_package(mutated, LIBRARY)

    mutated = deepcopy(package)
    mutated["semantic_source_digest"] = "sha256:mutated"
    assert "accessibility source digest must match canonical source" in validate_accessibility_package(mutated, LIBRARY)

    mutated = deepcopy(package)
    mutated["provenance"]["deterministic"] = False
    assert "accessibility package must declare deterministic output" in validate_accessibility_package(mutated, LIBRARY)

    mutated = deepcopy(package)
    mutated["layout"] = {"columns": 4}
    assert "accessibility package contains forbidden key: layout" in validate_accessibility_package(mutated, LIBRARY)


def test_negative_fixture_mutation_engine_uses_package_validator(tmp_path: Path) -> None:
    target = tmp_path / "accessibility/night-mode-v0.1"
    shutil.copytree(LIBRARY, target)
    shutil.copytree(ROOT / "components", tmp_path / "components")
    shutil.copytree(ROOT / "recipes", tmp_path / "recipes")
    shutil.copytree(ROOT / "analytics", tmp_path / "analytics")
    package = derive_accessibility_package(valid_source(), target)
    package_path = target / "proofs/packages/tooling.yaml"
    package_path.parent.mkdir(parents=True, exist_ok=True)
    package_path.write_text(yaml.safe_dump(package, sort_keys=False), encoding="utf-8")
    fixture_path = target / "fixture.yaml"
    fixture_path.write_text(
        yaml.safe_dump(
            {
                "base_package": "proofs/packages/tooling.yaml",
                "mutation": {
                    "path": ["provenance", "deterministic"],
                    "value": False,
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    assert "accessibility package must declare deterministic output" in validate_negative_fixture(
        fixture_path, target
    )
