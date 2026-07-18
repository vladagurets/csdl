from pathlib import Path
import shutil

from tools.build_recipe_proofs import build_recipe_proofs


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def test_proof_builder_reproduces_committed_packages(tmp_path: Path) -> None:
    target = tmp_path / "recipes/recipe-library-v0.5"
    target.parent.mkdir(parents=True)
    shutil.copytree(LIBRARY, target)
    pilot_target = tmp_path / "pilots/01-agentic-discipline/prompts"
    pilot_target.mkdir(parents=True)
    shutil.copy2(
        ROOT / "pilots/01-agentic-discipline/prompts/04-comparison.yaml",
        pilot_target / "04-comparison.yaml",
    )
    expected = {
        path.relative_to(LIBRARY): path.read_bytes()
        for path in [
            *sorted((LIBRARY / "proofs/packages").glob("*.yaml")),
            LIBRARY / "proofs/migration/01-pilot-comparison.yaml",
        ]
    }

    outputs = build_recipe_proofs(target)

    assert {path.relative_to(target): path.read_bytes() for path in outputs} == expected
