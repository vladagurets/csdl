from __future__ import annotations

import hashlib
import importlib.util
import shutil
from pathlib import Path
from types import ModuleType

import pytest
import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "ai/skills/csdl-create/scripts/validate_pilot.py"
CRITERIA_HEADER = (
    "card,clarity,presentation_readability,memorability,csdl_identity,"
    "restraint,text_fidelity,semantic_integrity\n"
)


def load_validator() -> ModuleType:
    spec = importlib.util.spec_from_file_location("csdl_create_validator", VALIDATOR_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_pilot(tmp_path: Path, rhythm: list[str]) -> Path:
    root = tmp_path / "02-sample-topic"
    for directory in [
        "prompts",
        "references",
        "canonical/light/16x9",
        "previews/landscape",
        "contact-sheets",
        "evaluation",
    ]:
        (root / directory).mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text("# Sample\n", encoding="utf-8")
    (root / "sources.md").write_text("# Sources\n", encoding="utf-8")
    (root / "references/reference-package.md").write_text(
        "# Reference package\n", encoding="utf-8"
    )
    (root / "prompts/00-style-anchor.yaml").write_text(
        "reference: canonical\n", encoding="utf-8"
    )
    (root / "evaluation/rubric.yaml").write_text("version: 1\n", encoding="utf-8")

    card_count = len(rhythm)
    id_width = max(2, len(str(card_count)))
    cards: list[dict[str, object]] = []
    review = ["# Review", ""]
    score_rows: list[str] = []
    canonical_template = root / "canonical-template.png"
    preview_template = root / "preview-template.png"
    Image.new("RGB", (1920, 1080), "#f4f0e9").save(canonical_template)
    Image.new("RGB", (1280, 720), "#f4f0e9").save(preview_template)

    for index, level in enumerate(rhythm, start=1):
        card_id = f"{index:0{id_width}d}"
        slug = f"slide-{card_id}"
        stem = f"{card_id}-{slug}"
        exact_copy = [f"HEADLINE {card_id}", f"Supporting copy {card_id}."]
        asset = root / f"canonical/light/16x9/{index}.png"
        shutil.copy2(canonical_template, asset)
        shutil.copy2(preview_template, root / f"previews/landscape/{stem}.png")

        draft_dir = root / f"drafts/light/16x9/{stem}"
        draft_dir.mkdir(parents=True)
        for version, color in enumerate(
            ["#f4f0e9", "#ebe6dc", "#ddd7cb"], start=1
        ):
            Image.new("RGB", (1920, 1080), color).save(
                draft_dir / f"{stem}-v{version}.png"
            )

        prompt_path = root / f"prompts/{stem}.yaml"
        prompt_path.write_text(
            yaml.safe_dump(
                {
                    "copy": exact_copy,
                    "generation_constraints": {
                        "candidate_directions": [
                            {
                                "id": "v1",
                                "concept": "A single anchored threshold",
                                "composition": "Asymmetric field with a left-edge entry",
                                "visual_mechanism": "One Anchor crossing one Divider",
                            },
                            {
                                "id": "v2",
                                "concept": "A controlled orbit around the claim",
                                "composition": "Open radial field with an off-center focus",
                                "visual_mechanism": "Three Nodes organized by one Axis",
                            },
                            {
                                "id": "v3",
                                "concept": "A progressive compression into evidence",
                                "composition": "Stepped diagonal sequence with a terminal focus",
                                "visual_mechanism": "One Vector compressing a Cluster",
                            },
                        ]
                    },
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        cards.append(
            {
                "id": card_id,
                "slug": slug,
                "recipe": "Hero",
                "level": level,
                "headline": exact_copy[0],
                "supporting_copy": exact_copy[1],
                "visual_mechanism": "One Anchor and one Signal",
                "components": ["Anchor", "Signal"],
                "signal": "coral",
                "max_supporting_elements": 2,
                "asset": f"canonical/light/16x9/{index}.png",
                "prompt": f"prompts/{stem}.yaml",
                "exact_copy": exact_copy,
            }
        )
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()
        review.extend(
            [
                f"## Slide {card_id}",
                f"**Selected:** `{stem}-v2.png`",
                f"Canonical SHA-256: `{digest}`",
                "Exact-copy review: pass.",
                "Candidate-divergence review: pass.",
                "",
            ]
        )
        score_rows.append(f"{card_id},5,5,4,5,5,5,5\n")

    manifest = {
        "pilot": {
            "id": "pilot-02",
            "slug": "sample-topic",
            "title": "Sample",
            "topic": "Validator fixture",
            "language": "en",
            "terminology_language": "en",
            "mode": "light",
            "canonical_canvas": "1920x1080",
            "orientation": "landscape",
            "rhythm": rhythm,
            "card_count": card_count,
        },
        "cards": cards,
    }
    (root / "manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8"
    )
    (root / "evaluation/review.md").write_text("\n".join(review), encoding="utf-8")
    (root / "evaluation/scores.csv").write_text(
        CRITERIA_HEADER + "".join(score_rows), encoding="utf-8"
    )
    Image.new("RGB", (3840, 2160), "#f4f0e9").save(
        root / "contact-sheets/pilot-02-light.png"
    )
    canonical_template.unlink()
    preview_template.unlink()
    return root


@pytest.mark.parametrize(
    "rhythm",
    [
        ["A", "B", "C"],
        ["A", "A", "B", "A", "B", "A", "C"],
        ["A", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "C"],
    ],
    ids=["three-slides", "seven-slides", "fifteen-slides"],
)
def test_accepts_user_approved_slide_counts(tmp_path: Path, rhythm: list[str]) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, rhythm)

    assert validator.validate(root, require_drafts=True, require_divergence=True) == []


def test_rejects_a_fourth_normalized_candidate(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    stem = "01-slide-01"
    source = root / f"drafts/light/16x9/{stem}/{stem}-v3.png"
    shutil.copy2(source, source.with_name(f"{stem}-v4.png"))

    errors = validator.validate(root, require_drafts=True)

    assert any("normalized candidates must equal" in error for error in errors)


def test_rejects_rhythm_length_different_from_card_count(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    manifest_path = root / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["pilot"]["rhythm"] = ["A", "C"]
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")

    errors = validator.validate(root, require_drafts=True)

    assert "pilot.rhythm must contain exactly 3 entries" in errors


def test_rejects_descriptive_canonical_asset_name(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    manifest_path = root / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["cards"][0]["asset"] = "canonical/light/16x9/01-slide-01.png"
    manifest_path.write_text(
        yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8"
    )

    errors = validator.validate(root, require_drafts=True)

    assert "card 01 asset must equal canonical/light/16x9/1.png" in errors


def test_rejects_missing_candidate_directions_when_required(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    prompt_path = root / "prompts/01-slide-01.yaml"
    prompt = yaml.safe_load(prompt_path.read_text(encoding="utf-8"))
    del prompt["generation_constraints"]["candidate_directions"]
    prompt_path.write_text(
        yaml.safe_dump(prompt, sort_keys=False), encoding="utf-8"
    )

    errors = validator.validate(root, require_drafts=True, require_divergence=True)

    assert any(
        "candidate_directions must contain exactly v1,v2,v3" in error
        for error in errors
    )


def test_rejects_duplicate_candidate_direction_dimension(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    prompt_path = root / "prompts/01-slide-01.yaml"
    prompt = yaml.safe_load(prompt_path.read_text(encoding="utf-8"))
    directions = prompt["generation_constraints"]["candidate_directions"]
    directions[2]["composition"] = directions[0]["composition"]
    prompt_path.write_text(
        yaml.safe_dump(prompt, sort_keys=False), encoding="utf-8"
    )

    errors = validator.validate(root, require_drafts=True, require_divergence=True)

    assert any(
        "candidate direction composition values must be unique" in error
        for error in errors
    )


def test_rejects_identical_candidate_bytes_when_divergence_required(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    draft_dir = root / "drafts/light/16x9/01-slide-01"
    shutil.copy2(
        draft_dir / "01-slide-01-v1.png",
        draft_dir / "01-slide-01-v2.png",
    )

    errors = validator.validate(root, require_drafts=True, require_divergence=True)

    assert any(
        "candidates must have three unique SHA-256 values" in error
        for error in errors
    )


def test_rejects_missing_candidate_divergence_review(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    review_path = root / "evaluation/review.md"
    review = review_path.read_text(encoding="utf-8")
    review_path.write_text(
        review.replace("Candidate-divergence review: pass.\n", "", 1),
        encoding="utf-8",
    )

    errors = validator.validate(root, require_drafts=True, require_divergence=True)

    assert any(
        "must record candidate-divergence review for every card" in error
        for error in errors
    )


def test_legacy_validation_does_not_require_divergence_evidence(tmp_path: Path) -> None:
    validator = load_validator()
    root = build_pilot(tmp_path, ["A", "B", "C"])
    for prompt_path in sorted((root / "prompts").glob("[0-9][0-9]-*.yaml")):
        prompt = yaml.safe_load(prompt_path.read_text(encoding="utf-8"))
        prompt.pop("generation_constraints", None)
        prompt_path.write_text(
            yaml.safe_dump(prompt, sort_keys=False), encoding="utf-8"
        )
    review_path = root / "evaluation/review.md"
    review_path.write_text(
        review_path.read_text(encoding="utf-8").replace(
            "Candidate-divergence review: pass.\n", ""
        ),
        encoding="utf-8",
    )

    assert validator.validate(root, require_drafts=True) == []
