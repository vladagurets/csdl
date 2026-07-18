from pathlib import Path

import yaml

from tools.validate_prompt_dsl import validate_prompt_package


ROOT = Path(__file__).parents[1]
LIBRARY = ROOT / "recipes/recipe-library-v0.5"


def test_negative_fixtures_fail_for_the_declared_contract_reason() -> None:
    fixture_root = LIBRARY / "fixtures/negative"
    index = yaml.safe_load((fixture_root / "expected-errors.yaml").read_text(encoding="utf-8"))

    assert len(index["fixtures"]) == 6
    for fixture in index["fixtures"]:
        errors = validate_prompt_package(fixture_root / fixture["file"], LIBRARY)
        assert fixture["error"] in errors, fixture["file"]
