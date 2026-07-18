from __future__ import annotations

import sys
from pathlib import Path

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.build_generation_package import build_generation_package
from tools.migrate_prompt_v01_to_v05 import migrate_prompt


PROOF_NAMES = ["01-editorial", "02-structural", "03-analytical"]


def build_recipe_proofs(root: Path) -> list[Path]:
    repository_root = root.parents[1]
    package_dir = root / "proofs/packages"
    migration_dir = root / "proofs/migration"
    package_dir.mkdir(parents=True, exist_ok=True)
    migration_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for name in PROOF_NAMES:
        outline = yaml.safe_load(
            (root / f"proofs/outlines/{name}.yaml").read_text(encoding="utf-8")
        )
        package = build_generation_package(outline, root)
        output = package_dir / f"{name}.yaml"
        output.write_text(
            yaml.safe_dump(package, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        outputs.append(output)
    migration = migrate_prompt(
        repository_root / "pilots/01-agentic-discipline/prompts/04-comparison.yaml",
        root,
    )
    migration_output = migration_dir / "01-pilot-comparison.yaml"
    migration_output.write_text(
        yaml.safe_dump(migration, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    outputs.append(migration_output)
    return outputs


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/build_recipe_proofs.py RECIPE_LIBRARY_ROOT")
        return 2
    try:
        outputs = build_recipe_proofs(Path(sys.argv[1]))
    except (KeyError, OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print("recipe proofs built: " + ", ".join(path.name for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
