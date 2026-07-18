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

## Prompt DSL and migration packet

- Branch: `codex/m4-prompt-dsl`
- Selection: exact evidence-backed scenario or explicit stable recipe identity; unsupported and ambiguous scenarios fail
- Package building: deterministic instances, component-owned attributes, relations, canvas/output defaults, reading path, negative-space range, palette semantics, exclusions, content bindings, and provenance
- Migration coverage: seven Pilot 01 recipe prompts plus twenty Visual DNA prompt packages; the shared style anchor remains immutable reference-only calibration evidence
- Raster generation or mutation: none

### Contract behavior

The builder keeps semantic intent, content bindings, component instances, relations, generation constraints, and provenance in separate top-level concerns. Component cardinality defaults are explicit in every recipe ingredient. Generated component attributes satisfy the per-component Prompt DSL contract from Milestone 3; package relations are checked against both endpoint contracts.

The migration tool normalizes `level`/`expression`, `copy`/`content`, component count maps, canvas/output, visual-authority/dataset provenance, and exclusions. Legacy zone, row, column, side, coordinate, Container, and other layout hints are discarded instead of entering v0.5 vocabulary. Every scalar copy/data value from each declared source prompt remains present in the migrated content bindings. Pilot Comparison receives the persisted migration proof in the next packet.

### TDD and validation evidence

The packet began with three expected import failures for selection, package building, and migration modules. After implementation:

```text
focused selection, package, migration, Prompt DSL, and recipe tests
17 passed

all 27 declared legacy recipe prompts
migrate to strict-valid Prompt DSL v0.5 packages
source scalar copy/data retained

.venv/bin/python tools/validate_recipe_library.py \
  recipes/recipe-library-v0.5/manifest.yaml
recipe library valid
```

Focused tests also prove deterministic repeated package construction, Workflow cardinality defaults (`4 Node`, `3 Vector`, `4 Label`, `1 Signal`), exact Pilot Comparison copy preservation, a 27-source migration map, rejection of an unsupported scenario, and rejection of ad hoc layout keys.

Remaining risk: strict library-wide Prompt DSL and index validation still require the three persisted end-to-end packages, migration proof, negative fixtures, and bounded analytical fidelity checks.

## Proof, negative-fixture, and index packet

- Branch: `codex/m4-proofs-indexes`
- End-to-end proofs: editorial Big Number, structural Workflow, bounded analytical Chart
- Migration proof: accepted Pilot 01 Comparison v0.1 to v0.5
- Negative fixtures: layout primitive, unknown component, forbidden relation, unsupported recipe/component combination, copy mutation, and analytical distortion
- Deterministic outputs: package/migration proof builder plus recipe index, 23×20 compatibility matrix, and selection index
- Raster generation or mutation: none

### Proof review

- Editorial outline scenario `count` selects `004 Big Number`; the package binds exact `3`, `РІВНІ ВИРАЗНОСТІ`, and `QUIET · CONSTRUCTIVE · SIGNAL` content to Anchor/Pulse/Label/Signal instances.
- Structural outline scenario `work procedure` selects `012 Workflow`; four Nodes, three Vectors, four Labels, and one Signal preserve UNDERSTAND → PLAN → EXECUTE → VERIFY without row/column/zone terminology.
- Analytical outline scenario `trend` selects `019 Chart`; two Axes, four Nodes, five Labels, and one Signal preserve W1–W4 order, `[72, 78, 84, 90]`, percent unit, `[0, 100]` domain, four direct Labels, and `DEMO DATA` source.
- Pilot migration proof selects `005 Comparison`, preserves every scalar copy value, records normalized/discarded fields, and contains only Component Library v0.1 instances and relations.

### TDD and validation evidence

The first focused run produced five expected failures: no canonical proof packages, no proof outlines, no migration proof, no analytical contract, and no negative-fixture index. After implementation:

```text
focused Prompt DSL, end-to-end, negative-fixture, and proof-builder tests
12 passed

.venv/bin/python tools/build_recipe_proofs.py recipes/recipe-library-v0.5
recipe proofs built: 01-editorial.yaml, 02-structural.yaml,
03-analytical.yaml, 01-pilot-comparison.yaml

.venv/bin/python tools/validate_prompt_dsl.py recipes/recipe-library-v0.5
Prompt DSL v0.5 valid

.venv/bin/python tools/validate_recipe_index.py recipes/recipe-library-v0.5
recipe index valid
```

The strict validator rebuilds all four persisted packages and compares the parsed documents. The analytical gate independently checks dataset path, series, order, domain, values, unit, direct labels, source, Node attributes, and Axis attributes. The source-outline gate rejects any content mutation.

Remaining risk: final documentation alignment, complete regression matrix, two-pass clean-tree rebuild, CI, PR integration, and post-merge main audit remain for release completion.

## Release documentation and CI packet

- Branch: `codex/m4-release`
- Active documentation: `AGENTS.md`, `README.md`, `ROADMAP.md`, `STATUS.md`, `DECISIONS.md`, `CHANGELOG.md`, and the foundation specification aligned to Milestone 4 complete / Milestone 5 deferred
- CI: complete Pilot 01, Visual DNA, Component Library, Recipe Library, Prompt DSL, deterministic builder, and clean-diff matrix
- Raster generation or mutation: none

### Completion validation

```text
.venv/bin/python -m pytest -q
98 passed

Pilot 01 manifest, style-anchor, asset, and score validators
all passed

Visual DNA catalog, data, asset, score, review, builder, and index validators
all passed

Component Library contract, proof, builder, and index validators
all passed

Recipe Library contract, proof builder, Prompt DSL, library builder, and index validators
all passed

git diff --check
passed
```

The catalog, component, proof-package, migration-proof, compatibility, and index builders produced no unrecorded output drift. The active-document scan found no stale statement that Milestone 4 is planned or unstarted; historical Milestone 3 review and plan records retain their original point-in-time wording.

Remaining risk: GitHub CI, final integration review, merge-commit completion, and post-merge validation on `main` remain external to this packet.
