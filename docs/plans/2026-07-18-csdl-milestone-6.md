# Milestone 6 — Night Mode and Accessibility v0.1 Implementation Plan

**Architecture decision:** D-032 — independent additive extension; Prompt DSL v0.5 unchanged.  
**Canonical root:** `accessibility/night-mode-v0.1/`  
**Primary signal:** ten deterministic proofs preserve one semantic signature across required output profiles while independently meeting contrast, fallback, and provenance contracts.

## Acceptance contract

Milestone 6 is complete only when all of the following are observable:

1. Canonical Markdown and versioned machine contracts cover light, night, monochrome, and projector profiles; base/raised/ink/neutral/line/signal tokens; text and non-text contrast; typography roles; focus/selection/error/positive/attention/data semantics; CVD robustness; and output provenance.
2. Every informative display, body, label, metadata, code, axis, unit, and source pairing meets at least 4.5:1. Every meaningful graphical object/state meets at least 3:1. Projector proofs meet 7:1 text and 4.5:1 non-text.
3. Color is never the sole carrier for Signal, status, category, uncertainty, forecast, missing data, direction, weight, magnitude, selection, or focus. Monochrome output retains direct labels and deterministic form/pattern distinctions.
4. Light/night packages preserve identical semantic roles, component/recipe references, analytical values, units, order, missing states, uncertainty, forecast boundaries, direction, and weight.
5. Compatibility matrices cover exactly fifteen D-029 components, exactly 23 D-030 recipes, unchanged Prompt DSL v0.5, and all ten Analytical Mode families without weakening D-031.
6. Ten required end-to-end proofs rebuild deterministically: editorial equivalence; structural accessible Signal/relations; exact table; positive/negative bars; forecast/uncertainty line; heatmap fallback; normalized map with missing region; directed/weighted network fallback; monochrome export; projector fallback.
7. Strict validation accepts every canonical proof; incomplete mode is tested; every indexed negative fixture fails for its exact reason; focused mutation tests cover global and scenario-specific invariants.
8. Builders reproduce packages, contrast/compatibility/index outputs byte-for-byte; repeated builders leave no worktree diff.
9. The full Milestone 1–6 test/validator matrix and CI are green. Prompt DSL v0.5, 15 components, 23 recipes, Analytical Mode values, and all accepted raster hashes remain unchanged.
10. Documentation, migration, compatibility, rollback, evidence review, and completion audit are aligned. The final integration PR is merged to `main` with a merge commit, local clean `main` equals `origin/main`, and post-merge strict validation passes. Milestone 7 remains unstarted.

## Architecture

### Versioning boundary

`accessibility/night-mode-v0.1` is an additive extension with:

- `language: CSDL`;
- `version: "0.1"`;
- `kind: accessibility-package`;
- a reference to one existing recipe/proof/analytical source without rewriting it;
- one or more output profiles chosen from light, night, monochrome, and projector;
- semantic token mappings and allowed pairings;
- text, graphical-object, redundant-encoding, fallback, CVD, and output contracts;
- a deterministic semantic-source digest and derived proof package.

Prompt DSL v0.5 remains closed. D-029 components and D-030 recipes remain closed. Analytical Mode v0.1 remains the quantitative authority. Accessibility terms are internal extension vocabulary, not public components or recipes.

### Canonical sources and derived outputs

Canonical authored inputs:

- `SPEC.md`, `manifest.yaml`, versioned token/proof schemas;
- token, contrast, fallback, and compatibility source contracts;
- ten proof sources;
- negative fixtures, migration/rollback docs, and review evidence.

Derived deterministic outputs:

- ten proof packages;
- `index.yaml`;
- `contrast-matrix.yaml`;
- `compatibility.yaml`.

### Accessibility profiles

- **light:** accessible mapping over the warm-paper Muted Signal intent; no accepted light raster is recolored.
- **night:** semantic role mapping over a warm graphite field; not mechanical inversion.
- **monochrome:** one-channel tonal mapping plus deterministic forms/patterns/direct labels.
- **projector:** high-margin profile with 7:1 informative text, 4.5:1 meaningful graphics, thicker critical rules, no semantic dependence on raised-surface fill.

### Evidence boundary

Accepted light rasters calibrate CSDL identity and presentation hierarchy. WCAG thresholds support contrast and color-independent rules. Projector, CVD, monochrome, and new night values are deterministic synthetic proofs. No package may label itself accepted raster evidence.

## Validation strategy

Validation independently:

- parses sRGB tokens and recomputes relative luminance/contrast without trusting generated matrices;
- checks every declared text and graphical pairing against its profile threshold;
- checks foreground/background eligibility and prohibited combinations;
- verifies raised surfaces have a valid semantic boundary when required;
- enforces minimum critical line weights and focus-indicator area/contrast;
- rejects color-only meaning and missing redundant form/text/pattern carriers;
- verifies light/night semantic digest equivalence;
- reloads referenced recipe/analytical packages and recomputes source digests;
- checks observed/forecast/uncertainty/missing/zero/Signal/category/direction/weight fallbacks;
- rejects undeclared layout/geometry vocabulary and unsupported token/component combinations;
- verifies deterministic provenance and exact generated outputs.

`require_complete=False` validates a partial contract without requiring all ten proofs, fixtures, or derived outputs. Strict mode requires exact inventory and deterministic equality.

## Dependency-aware packets

### Packet 1 — Evidence, acceptance, and architecture

Branch: `codex/m6-01-architecture`

- repository/evidence audit and baseline hashes;
- D-032 independent-extension decision;
- acceptance contract and packet plan;
- Milestone 6 state changed from deferred to active.

### Packet 2 — Token and compatibility contracts

Branch: `codex/m6-02-contracts` (stacked on Packet 1)

- begin with failing schema/contract/contrast tests;
- add canonical specification, manifest, token/proof schemas, semantic profiles, contrast/fallback rules, and compatibility source;
- test strict/incomplete inventory, token eligibility, WCAG calculation, profile thresholds, and exact 15/23/0.5/ten-family boundaries.

### Packet 3 — Validator, builder, and mutation engine

Branch: `codex/m6-03-tooling` (stacked on Packet 2)

- begin with failing validator/determinism/mutation tests;
- implement independent contrast/source-digest validation;
- build deterministic proof packages, contrast matrix, compatibility matrix, and index;
- reject prohibited pairings, color-only semantics, profile mutation, inaccessible signal area, layout vocabulary, and nondeterminism.

### Packet 4 — Proofs and negative fixtures

Branch: `codex/m6-04-proofs` (stacked on Packet 3)

- author ten required proof sources and build ten deterministic packages;
- add at least seventeen indexed negative fixtures, including every objective-listed failure;
- persist proof review, evidence class, raster deferral, and baseline/final raster hash comparison.

### Packet 5 — Documentation and regression completion

Branch: `codex/m6-05-docs` (stacked on Packet 4)

- align README, STATUS, ROADMAP, CHANGELOG, DECISIONS, AGENTS, accessibility README, migration, rollback, compatibility, and CI;
- run full Milestone 1–6 matrix, mutation suite, repeated builders, clean-diff check, and raster-hash audit.

### Packet 6 — Final integration

Branch: `codex/m6-integration` (stacked on Packet 5)

- add the final completion audit;
- open a final PR to `main` containing the complete stack;
- wait for green CI and merge only the integration PR through a merge commit;
- comment traceability on and close intermediate PRs without deleting their branches;
- sync clean local `main` to `origin/main` and repeat strict validation.

## Test-first sequence

For each behavior packet:

1. add the smallest failing boundary test;
2. run it and record the expected failure signal;
3. implement the minimum contract/tooling;
4. run focused tests and exact-error mutations;
5. run the complete suite before committing.

Required negative fixtures reject:

- insufficient text contrast;
- insufficient non-text contrast;
- color-only meaning;
- observed and forecast values with indistinguishable treatment;
- invisible uncertainty interval;
- missing value confused with zero;
- inaccessible heatmap scale;
- hue-only map regions;
- color-only network direction;
- Signal lost in grayscale;
- unreadable source or units;
- light/night semantic-role mutation;
- unsupported token/component combination;
- undeclared layout or geometry vocabulary;
- nondeterministic output;
- prohibited foreground/background combination;
- inaccessible signal-area behavior.

## Migration and rollback

- Migration is additive: attach an Accessibility v0.1 package to an unchanged existing source package and choose an output profile.
- Existing Prompt DSL, component, recipe, analytical, Pilot, and Visual DNA documents remain valid without migration.
- Rollback removes the additive `accessibility/` contract, tools/tests, CI steps, and documentation state. No source package, raster, dependency, secret, permission, database, or deployment needs conversion.

## Explicit non-goals

- raster generation, recoloring, or mutation without a separate explicit approval;
- Prompt DSL v0.5 changes;
- public component or recipe additions;
- Analytical Mode quantitative changes;
- portrait/mobile formats;
- Milestone 7 Cookbook/Design Book;
- licensing, tags, GitHub Releases, deployment, or other public-release work.
