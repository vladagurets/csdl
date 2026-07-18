# CSDL Milestone 4 — Recipe Library and Prompt DSL v0.5 Implementation Plan

**Goal:** Convert the accepted CSDL evidence into a versioned 23-recipe library and Prompt DSL v0.5 that deterministically turns an outline into a valid generation package without ad hoc layout rules.

**Evidence basis:** `docs/audits/2026-07-18-csdl-milestone-4-recipe-evidence.md`.

## Acceptance contract

### Primary signal

Given each canonical proof outline, the selector chooses the declared recipe and the package builder emits a strict-valid Prompt DSL v0.5 package using only the Milestone 3 public vocabulary. Rebuilding produces no diff.

### Observable pass/fail criteria

1. The library contains exactly 23 evidence-backed recipes in canonical order, each with a complete Markdown specification and per-recipe YAML record containing no placeholders.
2. The first twenty recipes cover all twenty Visual DNA families exactly once; Breakdown, Checklist, and Formula retain the three additional accepted Pilot 01 needs without adding unsupported families.
3. Every proof instance and relation is permitted by Component Library v0.1, and validators reject undeclared layout terminology and unsupported recipe/component or relation combinations.
4. Editorial, structural/process, and bounded analytical outlines select recipes and build strict-valid v0.5 packages; analytical values, domain, order, units, labels, and source remain exact.
5. A Pilot 01 v0.1 prompt migrates mechanically to v0.5 without copy changes; the migration report records normalized legacy fields.
6. Recipe index, compatibility output, selection index, and proof packages are deterministic and builders leave the worktree unchanged on a second run.
7. The full Pilot 01, Milestone 2, Milestone 3, and Milestone 4 test/validator matrix passes locally and in the final integration PR.
8. README, STATUS, ROADMAP, CHANGELOG, DECISIONS, and AGENTS agree that Milestone 4 is complete and Milestone 5 remains deferred.

### Secondary signals

- strict and `require_complete=False` modes are covered by focused tests;
- schema allowlists, path/order rules, cardinality, required/optional DSL fields, defaults, hard exclusions, evidence provenance, migration mapping, and rollback metadata validate;
- negative fixtures fail for layout primitives, unknown components, forbidden relations, unsupported recipes/components, changed copy, and distorted analytical data;
- no raster bytes, production dependencies, secrets, permissions, deployments, tags, releases, or PR #7 are changed.

## Canonical tree

```text
recipes/recipe-library-v0.5/
├── README.md
├── TEMPLATE.md
├── manifest.yaml
├── schema.yaml
├── prompt-dsl-v0.5.schema.yaml
├── migration-v0.1-to-v0.5.yaml
├── records/001-hero.yaml … 023-formula.yaml
├── specs/001-hero.md … 023-formula.md
├── proofs/
│   ├── outlines/01-editorial.yaml … 03-analytical.yaml
│   ├── packages/01-editorial.yaml … 03-analytical.yaml
│   └── migration/01-pilot-comparison.yaml
├── fixtures/negative/
├── evaluation/review.md
├── index.yaml
├── compatibility.yaml
└── selection-index.yaml

tools/
├── validate_recipe_library.py
├── validate_prompt_dsl.py
├── select_recipe.py
├── build_generation_package.py
├── migrate_prompt_v01_to_v05.py
├── build_recipe_library.py
└── validate_recipe_index.py
```

## Prompt DSL v0.5 contract

Required top-level concerns are kept separate:

- `semantic_intent`: problem, scenario, main idea, mechanism;
- `content`: source path/identity and exact bindings;
- `component_instances`: explicit IDs, public component names, and component-owned attributes;
- `relations`: explicit subject/type/object triples from public relation vocabulary;
- `generation_constraints`: canonical canvas, expression, controlled reading path, negative-space range/value, typography roles, semantic palette, exact-content flags, hard exclusions, and output contract;
- `provenance`: recipe/version, evidence, source outline, and optional migration source/report.

Deterministic defaults are declared centrally in the DSL schema and repeated in recipe records only when narrowed. Absence of an optional field produces the declared default; it never authorizes model invention.

## Recipe groups

### Group 1 — Editorial and Foundation (`001`–`007`)

Hero, Cover, Quote, Big Number, Comparison, Collision, Before / After.

### Group 2 — Structural and process (`008`–`016`)

Timeline, Matrix, Hierarchy, Architecture, Workflow, Loop, Pipeline, Decision Tree, Framework.

### Group 3 — Bounded analytical (`017`–`020`)

KPI, Table, Chart, Dashboard. These reuse the fixed Milestone 2 data contract and do not generalize into full Analytical Mode.

### Group 4 — Pilot extensions (`021`–`023`)

Breakdown, Checklist, Formula.

## Dependency-aware packet plan

No intermediate pull request is merged. Every packet branch is created from the preceding packet, its PR targets that preceding branch, and the final integration branch targets `main` with the complete commit chain. Intermediate PRs receive traceability comments and are closed as integrated only after the final merge. Branches are preserved.

### Packet 1 — Audit and plan

Branch: `codex/m4-audit-plan`

- persist the evidence audit, 23-recipe boundary, acceptance contract, and this plan;
- validate repository baseline and documentation formatting;
- open a PR to `main` but do not merge it.

### Packet 2 — Contract infrastructure

Branch: `codex/m4-infrastructure`, based on Packet 1.

- write failing tests for schema, strict/incomplete validation, unknown keys, placeholder/path/order checks, DSL separation, public vocabulary, and deterministic output contracts;
- add the library schema, DSL v0.5 schema, template, empty/incomplete manifest infrastructure, validators, builders, and CLI behavior;
- stop strict mode honestly until recipe records and proofs exist.

### Packet 3 — Recipe contracts

Branch: `codex/m4-recipe-contracts`, based on Packet 2.

- write failing coverage/order/cardinality assertions;
- add all 23 Markdown specifications and per-recipe YAML records;
- validate ingredients, relations, A/B/C support, family compatibility, canvas/presentation rules, typography/color/negative-space constraints, content contracts, DSL fields/defaults, exclusions, invariants, evidence, compatibility, and rollback notes;
- pass strict recipe-record validation without proofs/indexes.

### Packet 4 — Prompt DSL and migration

Branch: `codex/m4-prompt-dsl`, based on Packet 3.

- write failing package and migration tests;
- implement deterministic recipe selection, package building, v0.5 validation, and v0.1-to-v0.5 migration;
- map all accepted Pilot 01 slide recipes and the twenty Visual DNA recipe prompts; retain the style anchor as immutable reference-only calibration evidence;
- prove exact-copy preservation and reject legacy layout vocabulary instead of promoting it.

### Packet 5 — Proofs, negative fixtures, and indexes

Branch: `codex/m4-proofs-indexes`, based on Packet 4.

- write failing end-to-end, analytical-fidelity, negative-fixture, and drift tests;
- add editorial, structural/process, and bounded analytical outlines/packages plus a Pilot comparison migration proof;
- add negative fixtures for undeclared layout, unsupported component, forbidden relation, unsupported combination, copy mutation, and analytical distortion;
- derive deterministic recipe index, 23×20 compatibility output, and selection index;
- persist evaluation/review evidence.

### Packet 6 — Release alignment

Branch: `codex/m4-release`, based on Packet 5.

- update README, STATUS, ROADMAP, CHANGELOG, DECISIONS, AGENTS, and recipe README;
- extend CI with Milestone 2, Milestone 3, and Milestone 4 strict validators so the final PR checks the complete contract;
- run the full local matrix and a two-pass builder no-drift check;
- record exact results and compatibility/rollback notes.

### Packet 7 — Final integration

Branch: `codex/m4-integration`, based on Packet 6.

- perform an adversarial repository-grounded completion audit without starting Milestone 5;
- add only final evidence corrections required by that audit;
- open the final integration PR to `main`, wait for green CI, and merge through a merge commit;
- comment on and close intermediate PRs as integrated without deleting branches;
- fetch `origin/main`, switch local `main`, verify local `main == origin/main`, rerun strict validation, and confirm a clean worktree.

## TDD sequence

For each behavior packet:

1. add the smallest high-value failing test or mutation fixture at the contract boundary;
2. confirm the expected failure is caused by the missing/incorrect behavior;
3. implement the minimum contract or tool behavior;
4. run the focused test file;
5. run the full suite and all earlier milestone validators;
6. rebuild generated outputs twice and verify no diff before commit.

## Validation matrix

```bash
.venv/bin/python -m pytest -q

.venv/bin/python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
.venv/bin/python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
.venv/bin/python tools/validate_assets.py pilots/01-agentic-discipline
.venv/bin/python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv

.venv/bin/python tools/validate_pattern_catalog.py patterns/visual-dna-sprint-01/manifest.yaml
.venv/bin/python tools/validate_pattern_data.py patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml
.venv/bin/python tools/validate_pattern_assets.py patterns/visual-dna-sprint-01
.venv/bin/python tools/validate_pattern_scores.py patterns/visual-dna-sprint-01/evaluation/scores.csv
.venv/bin/python tools/validate_pattern_review.py patterns/visual-dna-sprint-01
.venv/bin/python tools/build_pattern_catalog.py patterns/visual-dna-sprint-01
.venv/bin/python tools/validate_pattern_index.py patterns/visual-dna-sprint-01

.venv/bin/python tools/validate_component_library.py components/component-library-v0.1/manifest.yaml
.venv/bin/python tools/validate_component_proofs.py components/component-library-v0.1
.venv/bin/python tools/build_component_library.py components/component-library-v0.1
.venv/bin/python tools/validate_component_index.py components/component-library-v0.1

.venv/bin/python tools/validate_recipe_library.py recipes/recipe-library-v0.5/manifest.yaml
.venv/bin/python tools/validate_prompt_dsl.py recipes/recipe-library-v0.5
.venv/bin/python tools/build_recipe_library.py recipes/recipe-library-v0.5
.venv/bin/python tools/validate_recipe_index.py recipes/recipe-library-v0.5
```

After both catalog/library builders run, `git status --short` must be empty.

## Compatibility, rollout, and rollback

- v0.5 is additive and versioned; legacy v0.1 prompt files and canonical assets remain byte-identical.
- Migration output records its source and normalized fields; no source file is rewritten.
- Package selection/building is a local deterministic toolchain with no deployment or data migration.
- Rollback is a normal revert of Milestone 4 commits. Existing milestones remain valid because Milestone 4 consumes their public contracts and does not mutate them.
- Any future recipe addition requires new usage evidence, its own versioned contract, tests, compatibility update, and review record.

## Explicit non-goals

- full Analytical Mode or new chart families;
- Container or any ad hoc layout/geometry primitive;
- raster generation or mutation;
- dark mode, portrait/mobile outputs, animation, public release, licensing, tags, or GitHub Releases;
- production dependencies, CI/CD redesign, or changes to PR #7.
