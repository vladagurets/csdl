from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image


EXPRESSION_LEVELS = {"A", "B", "C"}
CRITERIA = [
    "clarity",
    "presentation_readability",
    "memorability",
    "csdl_identity",
    "restraint",
    "text_fidelity",
    "semantic_integrity",
]
CRITICAL = {"clarity", "presentation_readability", "text_fidelity"}
REQUIRED_CARD_FIELDS = {
    "id",
    "slug",
    "recipe",
    "level",
    "headline",
    "supporting_copy",
    "visual_mechanism",
    "components",
    "signal",
    "max_supporting_elements",
    "asset",
    "prompt",
    "exact_copy",
}
CANDIDATE_DIRECTION_IDS = ["v1", "v2", "v3"]
CANDIDATE_DIRECTION_FIELDS = ["concept", "composition", "visual_mechanism"]


def load_yaml(path: Path, errors: list[str]) -> Any:
    if not path.exists():
        errors.append(f"missing file: {path.as_posix()}")
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"invalid YAML {path.as_posix()}: {exc}")
        return {}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def declared_names(path: Path, key: str, errors: list[str]) -> set[str]:
    data = load_yaml(path, errors)
    records = data.get(key, []) if isinstance(data, dict) else []
    names: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            continue
        name = record.get("name")
        if isinstance(name, str):
            names.add(name)
    return names


def all_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        result: list[str] = []
        for item in value.values():
            result.extend(all_strings(item))
        return result
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(all_strings(item))
        return result
    return []


def check_image(
    path: Path,
    size: tuple[int, int],
    errors: list[str],
) -> None:
    if not path.exists():
        errors.append(f"missing image: {path.as_posix()}")
        return
    try:
        with Image.open(path) as image:
            if image.format != "PNG":
                errors.append(f"{path.as_posix()} must be PNG, got {image.format}")
            if image.size != size:
                errors.append(
                    f"{path.as_posix()} must be {size[0]}x{size[1]}, "
                    f"got {image.size[0]}x{image.size[1]}"
                )
            if image.mode != "RGB":
                errors.append(f"{path.as_posix()} must be RGB, got {image.mode}")
    except OSError as exc:
        errors.append(f"invalid image {path.as_posix()}: {exc}")


def check_scores(path: Path, expected_ids: list[str], errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing file: {path.as_posix()}")
        return
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as exc:
        errors.append(f"cannot read {path.as_posix()}: {exc}")
        return

    actual_ids = [row.get("card") for row in rows]
    if actual_ids != expected_ids:
        errors.append(
            "scores.csv card ids must equal " + ",".join(expected_ids)
        )
    for row in rows:
        card = row.get("card", "??")
        values: list[int] = []
        for criterion in CRITERIA:
            try:
                value = int(row[criterion])
            except (KeyError, TypeError, ValueError):
                errors.append(f"card {card} {criterion} must be an integer")
                continue
            values.append(value)
            minimum = 5 if criterion in CRITICAL else 4
            if value < minimum or value > 5:
                errors.append(f"card {card} {criterion} must be between {minimum} and 5")
        if len(values) == len(CRITERIA) and sum(values) / len(values) < 4.4:
            errors.append(f"card {card} average must be at least 4.4")


def check_candidate_directions(
    prompt: Any,
    card_id: str,
    errors: list[str],
) -> None:
    constraints = (
        prompt.get("generation_constraints", {})
        if isinstance(prompt, dict)
        else {}
    )
    directions = (
        constraints.get("candidate_directions", {})
        if isinstance(constraints, dict)
        else {}
    )
    if not isinstance(directions, list) or [
        direction.get("id") if isinstance(direction, dict) else None
        for direction in directions
    ] != CANDIDATE_DIRECTION_IDS:
        errors.append(
            f"card {card_id} candidate_directions must contain exactly v1,v2,v3"
        )
        return

    for field in CANDIDATE_DIRECTION_FIELDS:
        values: list[str] = []
        for direction in directions:
            value = direction.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"card {card_id} candidate direction {direction['id']} "
                    f"{field} must be a non-empty string"
                )
                continue
            values.append(value.strip().casefold())
        if len(values) == 3 and len(set(values)) != 3:
            errors.append(
                f"card {card_id} candidate direction {field} values must be unique"
            )


def validate(
    root: Path,
    require_drafts: bool,
    require_divergence: bool = False,
) -> list[str]:
    errors: list[str] = []
    require_drafts = require_drafts or require_divergence
    repository = repo_root()
    recipes = declared_names(
        repository / "recipes/recipe-library-v0.5/manifest.yaml",
        "recipes",
        errors,
    )
    components = declared_names(
        repository / "components/component-library-v0.1/manifest.yaml",
        "components",
        errors,
    )

    manifest = load_yaml(root / "manifest.yaml", errors)
    pilot = manifest.get("pilot", {}) if isinstance(manifest, dict) else {}
    cards = manifest.get("cards", []) if isinstance(manifest, dict) else []

    expected_dir = re.compile(r"^\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
    if not expected_dir.fullmatch(root.name):
        errors.append("pilot directory must match NN-kebab-topic-name")
    if pilot.get("canonical_canvas") != "1920x1080":
        errors.append("pilot.canonical_canvas must equal 1920x1080")
    if pilot.get("orientation") != "landscape":
        errors.append("pilot.orientation must equal landscape")
    if pilot.get("mode") != "light":
        errors.append("pilot.mode must equal light")
    card_count = pilot.get("card_count")
    if not isinstance(card_count, int) or isinstance(card_count, bool) or card_count < 1:
        errors.append("pilot.card_count must be a positive integer")
        return errors
    if not isinstance(cards, list) or len(cards) != card_count:
        errors.append(f"cards must contain exactly pilot.card_count ({card_count}) entries")
        return errors

    rhythm = pilot.get("rhythm")
    if not isinstance(rhythm, list) or len(rhythm) != card_count:
        errors.append(f"pilot.rhythm must contain exactly {card_count} entries")
        return errors
    invalid_levels = sorted({str(level) for level in rhythm} - EXPRESSION_LEVELS)
    if invalid_levels:
        errors.append(
            "pilot.rhythm contains invalid levels: " + ",".join(invalid_levels)
        )

    id_width = max(2, len(str(card_count)))
    expected_ids = [f"{index:0{id_width}d}" for index in range(1, card_count + 1)]
    if [str(card.get("id", "")) for card in cards] != expected_ids:
        errors.append("card ids must equal " + ",".join(expected_ids))

    for card, expected_id, expected_level in zip(
        cards, expected_ids, rhythm, strict=True
    ):
        missing = REQUIRED_CARD_FIELDS - set(card)
        if missing:
            errors.append(f"card {expected_id} missing fields: {','.join(sorted(missing))}")
            continue
        slug = card["slug"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(slug)):
            errors.append(f"card {expected_id} slug must be kebab-case")
        if card["level"] != expected_level:
            errors.append(f"card {expected_id} level must equal {expected_level}")
        if card["recipe"] not in recipes:
            errors.append(f"card {expected_id} uses undeclared Recipe: {card['recipe']}")
        if not isinstance(card["components"], list) or not card["components"]:
            errors.append(f"card {expected_id} components must be a non-empty list")
        else:
            unknown = sorted(set(card["components"]) - components)
            if unknown:
                errors.append(
                    f"card {expected_id} uses undeclared components: {','.join(unknown)}"
                )
        exact_copy = card["exact_copy"]
        if not isinstance(exact_copy, list) or not exact_copy or not all(
            isinstance(item, str) and item.strip() for item in exact_copy
        ):
            errors.append(f"card {expected_id} exact_copy must be a non-empty string list")

        expected_stem = f"{expected_id}-{slug}"
        expected_asset = f"canonical/light/16x9/{expected_stem}.png"
        expected_prompt = f"prompts/{expected_stem}.yaml"
        if card["asset"] != expected_asset:
            errors.append(f"card {expected_id} asset must equal {expected_asset}")
        if card["prompt"] != expected_prompt:
            errors.append(f"card {expected_id} prompt must equal {expected_prompt}")

        prompt_path = root / expected_prompt
        prompt = load_yaml(prompt_path, errors)
        prompt_strings = all_strings(prompt)
        for line in exact_copy if isinstance(exact_copy, list) else []:
            if line not in prompt_strings:
                errors.append(
                    f"card {expected_id} exact copy absent from prompt: {line!r}"
                )
        if require_divergence:
            check_candidate_directions(prompt, expected_id, errors)

        check_image(root / expected_asset, (1920, 1080), errors)
        check_image(root / "previews/landscape" / f"{expected_stem}.png", (1280, 720), errors)

        if require_drafts:
            draft_dir = root / "drafts/light/16x9" / expected_stem
            expected_candidates = {
                f"{expected_stem}-v{version}.png" for version in range(1, 4)
            }
            candidate_pattern = re.compile(
                rf"^{re.escape(expected_stem)}-v\d+\.png$"
            )
            actual_candidates = {
                path.name
                for path in draft_dir.glob(f"{expected_stem}-v*.png")
                if candidate_pattern.fullmatch(path.name)
            }
            if actual_candidates != expected_candidates:
                errors.append(
                    f"card {expected_id} normalized candidates must equal "
                    + ",".join(sorted(expected_candidates))
                )
            for version in range(1, 4):
                check_image(
                    draft_dir / f"{expected_stem}-v{version}.png",
                    (1920, 1080),
                    errors,
                )
            if require_divergence:
                candidate_paths = [
                    draft_dir / f"{expected_stem}-v{version}.png"
                    for version in range(1, 4)
                ]
                if all(path.exists() for path in candidate_paths):
                    digests = {
                        hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in candidate_paths
                    }
                    if len(digests) != 3:
                        errors.append(
                            f"card {expected_id} candidates must have three unique "
                            "SHA-256 values"
                        )

    load_yaml(root / "prompts/00-style-anchor.yaml", errors)
    for required in ["README.md", "sources.md"]:
        if not (root / required).exists():
            errors.append(f"missing file: {(root / required).as_posix()}")
    reference_files = list((root / "references").glob("*.md"))
    if not reference_files:
        errors.append("references/ must contain a reference-package Markdown file")

    contact_sheets = sorted((root / "contact-sheets").glob("*.png"))
    if len(contact_sheets) != 1:
        errors.append("contact-sheets/ must contain exactly one PNG")
    else:
        check_image(contact_sheets[0], (3840, 2160), errors)

    review_path = root / "evaluation/review.md"
    if not review_path.exists():
        errors.append(f"missing file: {review_path.as_posix()}")
    else:
        review = review_path.read_text(encoding="utf-8")
        if review.count("**Selected:**") < card_count:
            errors.append("evaluation/review.md must record a selected candidate for every card")
        if review.count("Exact-copy review:") < card_count:
            errors.append("evaluation/review.md must record exact-copy review for every card")
        if review.count("Canonical SHA-256:") < card_count:
            errors.append("evaluation/review.md must record canonical hashes for every card")
        if (
            require_divergence
            and review.count("Candidate-divergence review:") < card_count
        ):
            errors.append(
                "evaluation/review.md must record candidate-divergence review "
                "for every card"
            )
        for card in cards:
            asset = root / card.get("asset", "")
            if asset.exists():
                digest = hashlib.sha256(asset.read_bytes()).hexdigest()
                if digest not in review:
                    errors.append(f"review.md missing SHA-256 for {asset.name}")

    if not (root / "evaluation/rubric.yaml").exists():
        errors.append("missing file: evaluation/rubric.yaml")
    check_scores(root / "evaluation/scores.csv", expected_ids, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a csdl-create pilot")
    parser.add_argument("pilot_root", type=Path)
    parser.add_argument(
        "--require-drafts",
        action="store_true",
        help="require all three normalized candidates for every slide",
    )
    parser.add_argument(
        "--require-divergence",
        action="store_true",
        help=(
            "require v1-v3 direction briefs, unique candidate bytes, and "
            "candidate-divergence review evidence"
        ),
    )
    args = parser.parse_args()
    errors = validate(
        args.pilot_root.resolve(),
        args.require_drafts,
        args.require_divergence,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("csdl-create pilot valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
