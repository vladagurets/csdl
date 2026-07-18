# Milestone 5 — Analytical Mode v0.1 Implementation Plan

**Architecture decision:** D-031 — independent extension; Prompt DSL v0.5 unchanged.  
**Canonical root:** `analytics/analytical-mode-v0.1/`  
**Primary signal:** ten independently recomputed fixed-data proofs pass strict validation without changing accepted rasters.

## Acceptance contract

Milestone 5 is complete only when all of the following are observable:

1. Canonical Markdown and machine-readable contracts cover bars, lines, scatterplots, waterfall, heatmaps, funnels, maps, networks, tables, uncertainty, forecasts, negative values, units, sources, labels, domains, missing states, and transformations.
2. Typed datasets and analytical encodings preserve identity, field types, values, order, domain, units, provenance, source period, missing status, zero/negative semantics, denominators, transformations, uncertainty, forecast status, geography, and network identity.
3. Each of ten required end-to-end proof paths resolves dataset → intent → compatible v0.5 recipe → Analytical Mode v0.1 extension → valid D-029 instances/relations → deterministic specification.
4. Strict validation accepts every canonical proof; incomplete mode is tested; every required negative fixture fails with its exact expected error; focused mutations cover every critical global invariant.
5. Builders reproduce packages and indexes byte-for-byte and a second pass leaves no worktree diff.
6. The full test suite and every Pilot 01, Milestone 2, Component Library, Recipe Library, Prompt DSL, and Analytical Mode validator pass locally and in CI.
7. Documentation states Milestone 5 complete, Milestone 6 deferred, Prompt DSL v0.5 unchanged, exactly fifteen public components and 23 recipes retained, and no accepted raster changed.
8. The final integration PR is green and merged into `main` with a merge commit; local clean `main` equals `origin/main`; post-merge strict validation passes.

## Architecture

### Versioning boundary

`analytical-mode-v0.1` is an additive extension with:

- `language: CSDL`;
- `version: "0.1"`;
- `kind: analytical-package`;
- a reference to exactly one typed dataset contract;
- analytical intent and a compatible Recipe Library v0.5 recipe reference;
- an internal data-encoding contract;
- D-029 public component instances and relations;
- a deterministic analytical specification and provenance.

Prompt DSL v0.5 remains closed and unchanged. Consumers can pair an Analytical Mode package with a normal Prompt DSL v0.5 generation package when a raster-generation workflow is later authorized. No downgrade can preserve new analytical semantics inside v0.5; rollback removes the additive extension and leaves v0.5 inputs untouched.

### Public versus internal vocabulary

- Public components remain exactly the D-029 fifteen.
- Public recipes remain exactly the D-030 twenty-three.
- `bar`, `line`, `point`, `cell`, `waterfall-step`, `funnel-stage`, `region`, `network-node`, `network-edge`, and `interval-band` are versioned internal analytical marks.
- Internal marks describe data encoding only. They cannot appear as public components or introduce pixel/layout coordinates.

### Canonical sources and derived outputs

Canonical authored inputs:

- `SPEC.md`, `manifest.yaml`, schemas, family contracts, compatibility rules;
- fixed typed datasets;
- proof source definitions;
- negative fixtures and review evidence.

Derived deterministic outputs:

- proof packages/specifications;
- `index.yaml`, `dataset-index.yaml`, and `compatibility.yaml`.

## Validation strategy

Validation loads datasets independently of generated packages and checks:

- schema shape and closed vocabulary;
- field typing and record identity;
- exact field bindings and values;
- domain/order/unit/source/provenance fidelity;
- explicit deterministic transformations and recomputed derived values;
- family rules, zero/log/dual-axis behavior, missing semantics, uncertainty/forecast separation, denominators, geographic/network identity;
- D-029 component compatibility and public relations;
- no color-only meaning or undeclared layout/geometry terms;
- deterministic package/index rebuild.

`require_complete=False` validates an individual or partial library without requiring all canonical datasets/proofs/indexes. Strict mode requires the exact manifest inventory and deterministic outputs.

## Dependency-aware packets

### Packet 1 — Evidence, acceptance, and architecture

Branch: `codex/m5-01-architecture`

- repository-grounded evidence audit;
- D-031 independent-extension decision;
- acceptance contract and packet plan;
- milestone state changed from deferred to active.

### Packet 2 — Data and encoding contracts

Branch: `codex/m5-02-contracts` (stacked on Packet 1)

- start with failing schema/contract tests;
- add canonical spec, manifest, typed dataset schema, encoding schema, family contracts, compatibility source, dataset fixtures;
- validate strict/incomplete inventory and contract shape.

### Packet 3 — Validators, transformations, and builders

Branch: `codex/m5-03-tooling` (stacked on Packet 2)

- start with failing mutation and determinism tests;
- implement independent dataset/package validation;
- implement auditable transformations and deterministic builders/indexes;
- reject global and family-specific quantitative violations.

### Packet 4 — Proofs and negative fixtures

Branch: `codex/m5-04-proofs` (stacked on Packet 3)

- author ten proof sources and fixed datasets;
- build ten deterministic packages/specifications;
- add all required negative fixtures with exact expected errors;
- record synthetic-proof review evidence and raster non-mutation audit.

### Packet 5 — Documentation and regression completion

Branch: `codex/m5-05-docs` (stacked on Packet 4)

- align README, STATUS, ROADMAP, CHANGELOG, DECISIONS, AGENTS, library README, migration, rollback, and compatibility notes;
- extend CI with Analytical Mode strict build/validation/drift checks;
- run every Milestone 1–5 validator and deterministic second pass.

### Packet 6 — Final integration

Branch: `codex/m5-integration` (stacked on Packet 5)

- add final completion audit;
- open final PR to `main` containing the complete stack;
- wait for green CI;
- merge only final integration PR through a merge commit;
- comment traceability on and close intermediate PRs without deleting branches;
- sync and revalidate clean `main` against `origin/main`.

## Test-first sequence

For each behavior packet:

1. add the smallest high-value failing boundary test;
2. run it and record the expected failure signal;
3. implement the minimum contract/tooling necessary;
4. run focused tests and mutations;
5. run the complete suite before committing.

Critical mutations include truncated bar baseline, undeclared log scale, unapproved dual axis, reordered time, changed values, missing unit/source, wrong denominator, forecast-as-observed, inverted uncertainty bounds, bad normalization, raw-count map rate claim, semantic network distance, color-only meaning, unsupported mark/component combination, layout vocabulary, and nondeterministic output.

## Migration and rollback

- Migration is additive: bind a v0.5 analytical recipe package or outline to one v0.1 typed dataset and encoding definition; do not rewrite v0.5.
- Existing bounded Chart proof remains valid and becomes compatibility evidence, not an input that is mutated.
- Rollback is a normal revert of `analytics/`, its tools/tests/docs, and CI steps. Prompt DSL v0.5, Component Library v0.1, Recipe Library v0.5, Pilot 01, and all rasters remain usable and byte-identical.

## Explicit non-goals

- raster generation or mutation;
- new public components or recipes;
- Prompt DSL v0.5 breaking changes;
- Night Mode, portrait/mobile formats, Cookbook, public release, license, tags, or GitHub Releases.
