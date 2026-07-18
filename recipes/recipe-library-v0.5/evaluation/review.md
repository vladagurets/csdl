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

## Recipe contract packet

- Branch: `codex/m4-recipe-contracts`
- Accepted records/specifications: `001 Hero` through `020 Dashboard`, plus `021 Breakdown`, `022 Checklist`, and `023 Formula`
- Evidence boundary: twenty Visual DNA families plus three distinct accepted Pilot-only needs; no synthetic expansion toward fifty recipes
- Visual DNA coverage: all twenty families have at least one compatible recipe
- Public vocabulary: every ingredient and allowed relation cross-validates against Component Library v0.1
- Raster generation or mutation: none

### Contract review

Every recipe defines stable identity/version, problem, scenarios, required/optional ingredients and cardinality, allowed/forbidden relations, assembly order, A/B/C support, compatible Visual DNA families, canvas/readability/negative-space constraints, typography and semantic color, exact content, Prompt DSL fields/defaults, exclusions, invariants, examples/evidence, migration, and rollback.

The three Pilot extensions remain semantically distinct:

- Breakdown normalizes the legacy incomplete-Loop wording to a closed expected recurrence with one failed-transition Signal, preserving copy while respecting the Milestone 3 Loop invariant.
- Checklist uses a non-sequential Framework-compatible Cluster of interrogative Nodes and discards legacy `2x2` zone terminology.
- Formula preserves exact operand/operator/result order through Collision-compatible Anchors and one result Signal, discarding zone and plane hints.

### TDD and validation evidence

The packet began with the expected failure that the manifest contained zero records instead of IDs `001`–`023`. After the complete records and Markdown contracts were added:

```text
.venv/bin/python tools/validate_recipe_library.py \
  recipes/recipe-library-v0.5/manifest.yaml
recipe library valid

focused recipe, builder, and index tests
10 passed
```

Mutation coverage rejects a recipe/family-incompatible component and an allowed relation absent from Component Library v0.1. Strict Prompt DSL and final index validation remain intentionally red until the three proof packages and migration evidence exist.

Remaining risk: deterministic package construction has not yet exercised recipe cardinality or exact content at runtime, and the bounded analytical contract has no v0.5 package proof. Those are mandatory in the next two packets.
