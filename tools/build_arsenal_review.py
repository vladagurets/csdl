from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, ImageDraw, ImageFont


PAPER = "#F7F5F0"
INK = "#1B1B19"
CORAL = "#C96157"
LINE = "#B8B5AE"
FONT_REGULAR = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")


def _font(path: Path, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if path.is_file():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def _load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected YAML mapping: {path}")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _candidate_paths(root: Path, recipe: dict[str, Any]) -> list[Path]:
    record = _load(root / recipe["record"])
    manifest = _load(root / "manifest.yaml")
    candidate_set = manifest.get("evidence_gate", {}).get(
        "active_candidate_set", "initial"
    )
    suffix = "-redesign" if candidate_set == "recalibration" else ""
    candidate_root = (
        root
        / "drafts/light/16x9"
        / f"{record['id']}-{record['slug']}{suffix}"
    )
    return [candidate_root / f"v{index}.png" for index in range(1, 4)]


def build_recipe_board(
    root: Path, recipe: dict[str, Any], selection_root: Path
) -> Path:
    record = _load(root / recipe["record"])
    candidates = _candidate_paths(root, recipe)
    canvas = Image.new("RGB", (1920, 480), PAPER)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((28, 24, 46, 42), fill=CORAL)
    draw.text(
        (62, 17),
        f"{record['id']}  {record['name'].upper()}  |  THREE UNPROMOTED CANDIDATES",
        font=_font(FONT_BOLD, 28),
        fill=INK,
    )
    draw.line((28, 66, 1892, 66), fill=LINE, width=2)
    positions = [18, 650, 1282]
    for index, (path, x) in enumerate(zip(candidates, positions), start=1):
        with Image.open(path) as source:
            image = source.convert("RGB").resize((620, 349), Image.Resampling.LANCZOS)
        canvas.paste(image, (x, 92))
        draw.rectangle((x + 14, 446, x + 68, 474), fill=INK)
        draw.text((x + 27, 448), f"v{index}", font=_font(FONT_BOLD, 18), fill=PAPER)
    output = selection_root / f"{record['id']}-{record['slug']}.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)
    return output


def build_overview(boards: list[Path], output: Path) -> Path:
    canvas = Image.new("RGB", (3840, 2160), INK)
    positions = [
        (0, 0),
        (1920, 0),
        (0, 540),
        (1920, 540),
        (0, 1080),
        (1920, 1080),
        (0, 1620),
        (1920, 1620),
    ]
    for board, position in zip(boards, positions):
        with Image.open(board) as source:
            image = source.convert("RGB")
        canvas.paste(image, position)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)
    return output


def build_hash_inventory(root: Path, manifest: dict[str, Any], output: Path) -> Path:
    files = []
    for recipe in manifest["recipes"]:
        for path in _candidate_paths(root, recipe):
            with Image.open(path) as image:
                files.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "sha256": _sha256(path),
                        "width": image.width,
                        "height": image.height,
                        "mode": image.mode,
                    }
                )
    selection_path = root / "selection/selected.yaml"
    selected = []
    status = "unpromoted"
    if selection_path.is_file():
        selection = _load(selection_path)
        status = str(selection.get("status", "unpromoted"))
        recipes = {str(entry["id"]): entry for entry in manifest["recipes"]}
        for choice in selection.get("selections", []):
            recipe = recipes[str(choice["id"])]
            record = _load(root / recipe["record"])
            variant = str(choice["variant"])
            source = _candidate_paths(root, recipe)[int(variant[1:]) - 1]
            selected_path = (
                root
                / "selection/selected"
                / f"{record['id']}-{record['slug']}.png"
            )
            selected.append(
                {
                    "id": str(record["id"]),
                    "variant": variant,
                    "source": source.relative_to(root).as_posix(),
                    "selected_path": selected_path.relative_to(root).as_posix(),
                    "source_sha256": _sha256(source),
                    "selected_sha256": _sha256(selected_path),
                    "exact_copy_review": choice.get("exact_copy_review"),
                }
            )
    document = {
        "extension": manifest["extension"]["id"],
        "status": status,
        "file_count": len(files),
        "unique_sha256_count": len({entry["sha256"] for entry in files}),
        "files": files,
    }
    if selected:
        document["selected"] = selected
    output.write_text(
        yaml.safe_dump(document, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return output


def build_arsenal_review(root: Path) -> list[Path]:
    manifest = _load(root / "manifest.yaml")
    selection_root = root / "selection"
    boards = [
        build_recipe_board(root, recipe, selection_root)
        for recipe in manifest["recipes"]
    ]
    overview = build_overview(boards, selection_root / "overview.png")
    inventory = build_hash_inventory(
        root, manifest, selection_root / "candidate-hashes.yaml"
    )
    return [*boards, overview, inventory]


def _validate_selected_candidates(
    root: Path, manifest: dict[str, Any], errors: list[str]
) -> None:
    selection_path = root / "selection/selected.yaml"
    if not selection_path.is_file():
        errors.append("arsenal selection metadata is missing")
        return
    selection = _load(selection_path)
    if selection.get("status") != "selected_unpromoted":
        errors.append("arsenal selection status must equal selected_unpromoted")
    choices = selection.get("selections", [])
    if len(choices) != 8:
        errors.append("arsenal selection requires exactly eight choices")
        return
    recipes = {str(entry["id"]): entry for entry in manifest["recipes"]}
    if {str(choice.get("id")) for choice in choices} != set(recipes):
        errors.append("arsenal selection must cover recipe ids 024 through 031")
    for choice in choices:
        recipe_id = str(choice.get("id"))
        recipe = recipes.get(recipe_id)
        if recipe is None:
            continue
        variant = str(choice.get("variant", ""))
        if variant not in {"v1", "v2", "v3"}:
            errors.append(f"arsenal selection has invalid variant: {recipe_id}")
            continue
        if choice.get("exact_copy_review") != "pass":
            errors.append(f"arsenal selection lacks exact-copy review: {recipe_id}")
        record = _load(root / recipe["record"])
        source = _candidate_paths(root, recipe)[int(variant[1:]) - 1]
        selected = (
            root
            / "selection/selected"
            / f"{record['id']}-{record['slug']}.png"
        )
        if not selected.is_file():
            errors.append(f"missing selected arsenal candidate: {selected.name}")
            continue
        if source.read_bytes() != selected.read_bytes():
            errors.append(f"selected arsenal candidate must equal source: {recipe_id}")

    scores_path = root / "evaluation/scores.csv"
    try:
        with scores_path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        errors.append(f"arsenal scores must be readable: {error}")
        return
    if len(rows) != 8 or {row.get("recipe") for row in rows} != set(recipes):
        errors.append("arsenal scores must cover all eight selected recipes")
        return
    criteria = [
        "clarity",
        "presentation_readability",
        "memorability",
        "csdl_identity",
        "restraint",
        "text_fidelity",
        "semantic_integrity",
    ]
    for row in rows:
        recipe_id = str(row.get("recipe"))
        try:
            values = {criterion: int(row[criterion]) for criterion in criteria}
            average = float(row["average"])
        except (KeyError, TypeError, ValueError):
            errors.append(f"arsenal score row is invalid: {recipe_id}")
            continue
        if values["clarity"] != 5 or values["presentation_readability"] != 5:
            errors.append(f"arsenal readability thresholds failed: {recipe_id}")
        if values["text_fidelity"] != 5:
            errors.append(f"arsenal text fidelity threshold failed: {recipe_id}")
        if min(values.values()) < 4 or average < 4.4:
            errors.append(f"arsenal acceptance score threshold failed: {recipe_id}")
        expected_average = round(sum(values.values()) / len(values), 2)
        if average != expected_average:
            errors.append(f"arsenal score average is inconsistent: {recipe_id}")
        if row.get("status") != "accepted":
            errors.append(f"arsenal score status must equal accepted: {recipe_id}")


def validate_arsenal_candidates(
    root: Path, require_selection: bool = False
) -> list[str]:
    errors: list[str] = []
    manifest = _load(root / "manifest.yaml")
    hashes: set[str] = set()
    count = 0
    for recipe in manifest["recipes"]:
        for path in _candidate_paths(root, recipe):
            count += 1
            if not path.is_file():
                errors.append(f"missing arsenal candidate: {path.relative_to(root)}")
                continue
            try:
                with Image.open(path) as image:
                    if image.format != "PNG":
                        errors.append(f"arsenal candidate must be PNG: {path.name}")
                    if image.size != (1920, 1080):
                        errors.append(f"arsenal candidate must be 1920x1080: {path.name}")
                    if image.mode not in {"RGB", "RGBA"}:
                        errors.append(f"arsenal candidate must be RGB or RGBA: {path.name}")
            except OSError as error:
                errors.append(f"arsenal candidate must be readable PNG: {error}")
                continue
            hashes.add(_sha256(path))
    if count != 24:
        errors.append("arsenal candidate contract requires exactly 24 files")
    if len(hashes) != 24:
        errors.append("arsenal candidates must have 24 unique SHA-256 values")
    if require_selection:
        _validate_selected_candidates(root, manifest, errors)
    return errors


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("usage: python tools/build_arsenal_review.py ROOT [--validate]")
        return 2
    root = Path(sys.argv[1])
    if len(sys.argv) == 3:
        if sys.argv[2] != "--validate":
            print("usage: python tools/build_arsenal_review.py ROOT [--validate]")
            return 2
        errors = validate_arsenal_candidates(root, require_selection=True)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("arsenal candidates valid")
        return 0
    try:
        outputs = build_arsenal_review(root)
    except (KeyError, OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print("arsenal review built: " + ", ".join(path.name for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
