# Recipe Library v0.5 Review

## Review protocol

Every packet records focused failing tests, implemented contracts, strict or incomplete validation status, regression results, deterministic-output checks, compatibility implications, rollback behavior, and remaining risk. Partial recipe records and placeholder evidence are never accepted.

## Infrastructure packet

- Branch: `codex/m4-infrastructure`
- Manifest state: zero accepted recipe records; exact 23-recipe order declared
- Public vocabulary: exact fifteen components and fourteen relations imported from Component Library v0.1
- Schemas: complete recipe-record, Markdown-section, path/order, Prompt DSL concern-separation, default, exclusion, and proof-package infrastructure
- Tooling: strict/incomplete recipe and Prompt DSL validators plus deterministic index, compatibility, and selection-index builder/validator
- Raster generation or mutation: none

### TDD evidence

The initial focused run failed during collection with the expected four `ModuleNotFoundError` results for the not-yet-created recipe validator, Prompt DSL validator, builder, and index validator.

After implementation:

```text
.venv/bin/python -m pytest -q \
  tests/test_validate_recipe_library.py \
  tests/test_validate_prompt_dsl.py \
  tests/test_build_recipe_library.py \
  tests/test_validate_recipe_index.py
10 passed

programmatic incomplete-mode recipe/Prompt DSL/index validation
recipe infrastructure partial contracts valid
```

Strict-mode stop signals are intentional at this packet boundary:

- recipe validator: exactly 23 complete records are absent;
- Prompt DSL validator: exactly three proof packages are absent;
- builder: `recipe library is incomplete`.

The focused mutation tests reject an unknown library field, a public-vocabulary change that restores `Container`, an ad hoc `layout` key, and deterministic index drift.

Remaining risk: record-level ingredient compatibility, component relation permission, migration behavior, proof content fidelity, and analytical preservation cannot receive positive coverage until recipes and packages exist. Later packets must exercise those gates before strict validation passes.
