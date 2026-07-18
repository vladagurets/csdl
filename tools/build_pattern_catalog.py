from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml
from PIL import Image


PAPER = (247, 245, 240)
PREVIEW_SIZE = (1280, 720)
SHEET_SIZE = (3840, 2160)


def _load_manifest(root: Path) -> dict[str, Any]:
    return yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))


def resolve_asset(root: Path, family: dict[str, Any]) -> Path:
    canonical = Path(family["evidence"]["canonical_example"])
    if family["evidence"]["mode"] == "pilot_reference":
        return root.parents[1] / canonical
    return root / canonical


def build_previews(root: Path, require_complete: bool = True) -> list[Path]:
    output_dir = root / "previews/landscape"
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for family in _load_manifest(root)["families"]:
        source = resolve_asset(root, family)
        if not source.exists():
            if require_complete:
                raise FileNotFoundError(source)
            continue
        output = output_dir / f"{family['id']}-{family['slug']}.png"
        with Image.open(source) as image:
            image.convert("RGB").resize(PREVIEW_SIZE, Image.Resampling.LANCZOS).save(output)
        outputs.append(output)
    return outputs


def build_contact_sheet(inputs: Iterable[Path], output: Path, columns: int = 5) -> None:
    paths = list(inputs)
    if not paths:
        raise ValueError("contact sheet requires at least one image")
    rows = (len(paths) + columns - 1) // columns
    gutter = 32
    max_cell_width = (SHEET_SIZE[0] - (columns + 1) * gutter) // columns
    max_cell_height = (SHEET_SIZE[1] - (rows + 1) * gutter) // rows
    scale = min(max_cell_width / PREVIEW_SIZE[0], max_cell_height / PREVIEW_SIZE[1])
    cell = (round(PREVIEW_SIZE[0] * scale), round(PREVIEW_SIZE[1] * scale))
    sheet = Image.new("RGB", SHEET_SIZE, PAPER)
    total_height = rows * cell[1] + (rows - 1) * gutter
    start_y = (SHEET_SIZE[1] - total_height) // 2
    for row in range(rows):
        row_paths = paths[row * columns : (row + 1) * columns]
        total_width = len(row_paths) * cell[0] + (len(row_paths) - 1) * gutter
        start_x = (SHEET_SIZE[0] - total_width) // 2
        for column, path in enumerate(row_paths):
            with Image.open(path) as image:
                preview = image.convert("RGB").resize(cell, Image.Resampling.LANCZOS)
            sheet.paste(preview, (start_x + column * (cell[0] + gutter), start_y + row * (cell[1] + gutter)))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def build_catalog_contact_sheets(root: Path, require_complete: bool = True) -> list[Path]:
    previews = build_previews(root, require_complete=require_complete)
    by_id = {path.name[:2]: path for path in previews}
    groups = {
        "visual-dna-01-editorial.png": [f"{index:02d}" for index in range(1, 8)],
        "visual-dna-01-structural.png": [f"{index:02d}" for index in range(8, 17)],
        "visual-dna-01-analytical.png": [f"{index:02d}" for index in range(17, 21)],
        "visual-dna-01-all.png": [f"{index:02d}" for index in range(1, 21)],
    }
    outputs: list[Path] = []
    for filename, ids in groups.items():
        inputs = [by_id[family_id] for family_id in ids if family_id in by_id]
        if require_complete and len(inputs) != len(ids):
            raise ValueError(f"{filename} requires {len(ids)} family previews")
        if not inputs:
            continue
        output = root / "contact-sheets" / filename
        build_contact_sheet(inputs, output, columns=5)
        outputs.append(output)
    return outputs


def build_index(root: Path, require_complete: bool = True) -> Path:
    data = _load_manifest(root)
    scores_path = root / "evaluation/scores.csv"
    with scores_path.open(newline="", encoding="utf-8") as handle:
        score_rows = {row["family"]: row for row in csv.DictReader(handle)}
    entries: list[dict[str, Any]] = []
    for family in data["families"]:
        source = resolve_asset(root, family)
        row = score_rows.get(family["id"])
        if require_complete and (not source.exists() or row is None):
            raise ValueError(f"family {family['id']} lacks complete asset or score evidence")
        entry: dict[str, Any] = {
            "id": family["id"],
            "slug": family["slug"],
            "name": family["name"],
            "canonical_level": family["canonical_level"],
            "allowed_levels": family["allowed_levels"],
            "evidence_mode": family["evidence"]["mode"],
            "canonical_example": family["evidence"]["canonical_example"],
        }
        if source.exists():
            with Image.open(source) as image:
                entry.update(
                    sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                    dimensions=f"{image.size[0]}x{image.size[1]}",
                    color_mode=image.mode,
                )
        else:
            entry["status"] = "awaiting_generation"
        if row is not None:
            values = [int(row[key]) for key in row if key != "family"]
            entry["score_average"] = round(sum(values) / len(values), 2)
        entries.append(entry)
    output = root / "index.yaml"
    output.write_text(
        yaml.safe_dump(
            {"catalog": data["catalog"]["id"], "version": data["catalog"]["version"], "families": entries},
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return output


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/build_pattern_catalog.py CATALOG_ROOT")
        return 2
    root = Path(sys.argv[1])
    previews = build_previews(root)
    sheets = build_catalog_contact_sheets(root)
    index = build_index(root)
    print(f"pattern catalog built: {len(previews)} previews, {len(sheets)} contact sheets, {index.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
