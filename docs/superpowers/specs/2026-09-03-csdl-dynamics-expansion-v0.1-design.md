# CSDL Dynamics Expansion v0.1

**Status:** Proposed design, approved for specification
**Date:** 2026-09-03
**Language:** Ukrainian explanation with canonical English identifiers
**Package:** `extensions/dynamics-expansion-v0.1/`
**Dependency:** public promotion of D-035 Arsenal Expansion v0.1
**Canonical canvas:** `1920x1080`, 16:9, landscape

## 1. Summary

Dynamics Expansion v0.1 is an additive, evidence-gated CSDL incubation package
for explaining how systems behave over time.

The package adds four composition recipes, two candidate components, six
candidate relations, and three analytical families:

```text
INTERACTION
+ FEEDBACK
+ ACCUMULATION
+ SCENARIOS
```

The package is not an in-place edit of Component Library, Recipe Library,
Analytical Mode, Prompt DSL, Foundation, or accepted raster evidence. Candidate
vocabulary remains local until every promotion gate passes.

## 2. Context

### 2.1 Canonical baseline before D-035 promotion

- Component Library v0.1: 15 public components.
- Recipe Library v0.5: 23 public recipes.
- Analytical Mode v0.1: 10 analytical families.
- Prompt DSL v0.5: closed declarative composition contract.
- Foundation v0.1: static `1920x1080` landscape visual language.
- Accessibility v0.1: semantic light, night, monochrome, and projector profiles.

### 2.2 D-035 dependency

D-035 Arsenal Expansion v0.1 proposes:

- three components: `Threshold`, `Trace`, `Band`;
- eight recipes, IDs `024` through `031`;
- five relations;
- six analytical families.

Dynamics Expansion starts only after D-035 user selection, rubric review,
compatibility review, deterministic validation, and public promotion.

The expected promoted baseline is:

- Component Library v0.2: 18 public components;
- Recipe Library v0.6: 31 public recipes;
- Analytical Mode v0.2: 16 analytical families;
- Prompt DSL v0.6 only if D-035 promotion requires it.

If D-035 promotion changes these version numbers, Dynamics Expansion must bind
to the actual promoted versions without changing its semantic scope.

## 3. Problem

After D-035, CSDL can explain propositions, comparisons, static structures,
operational order, state transitions, causal chains, dependencies, roadmaps,
and a broad set of analytical views.

Four semantic gaps remain:

1. Interaction between multiple actors over time.
2. Closed-loop control around a target and measured deviation.
3. Accumulation and depletion through inflows and outflows.
4. Multiple plausible future trajectories under uncertainty.

Existing recipes can approximate these ideas, but doing so overloads their
contracts:

- `Workflow` owns operational order, not actor-to-actor messages.
- `Architecture` owns stable system boundaries, not temporal interaction.
- `Loop` owns recurrence, not target, measurement, deviation, and correction.
- `Pipeline` owns staged transformation, not conservation or accumulation.
- `Sankey` owns flow distribution, not stored state.
- `Decision Tree` owns branching rules, not uncertain future trajectories.
- `Roadmap` owns planned work, not scenario outcomes.
- `Line` owns a declared series and forecast, not several scenario identities.

## 4. Goals

1. Add four evidence-backed recipes:
   - `032 Interaction Sequence`;
   - `033 Feedback Control`;
   - `034 Stock / Flow`;
   - `035 Scenario Fan`.
2. Incubate two reusable public-component candidates:
   - `Lane`;
   - `Stock`.
3. Incubate six explicit semantic relations:
   - `sends_to`;
   - `measures`;
   - `corrects`;
   - `flows_into`;
   - `flows_out_of`;
   - `diverges_to`.
4. Add three deterministic analytical families:
   - `controlchart`;
   - `slopegraph`, with `dumbbell` as a rendering form;
   - `dotplot`.
5. Create three materially different `1920x1080` visual candidates for each
   recipe.
6. Preserve all accepted contracts and raster hashes until explicit promotion.
7. Keep user selection as the visual promotion gate.

## 5. Non-goals

- No animation, video, slide transition, or interactive presentation format.
- No new expression level beyond A, B, and C.
- No change to the locked `1920x1080` landscape canvas.
- No change to Quiet Modular, Constructive Signal, or Muted Signal direction.
- No automatic promotion of candidates.
- No recipe quota.
- No UI-shell, widget, gauge, radar, generic mind-map, or decorative graph
  vocabulary.
- No Wave 2 or Wave 3 recipes.
- No `Service Blueprint`, `Risk Bow-Tie`, `Guardrail Map`, `Causal Loop`,
  `Incident Reconstruction`, `Cumulative Flow`, or `Event Strip` in this
  package.
- No mutation, recoloring, or regeneration of accepted Milestone 1-7 rasters.

## 6. Version boundary

The package lives at:

```text
extensions/dynamics-expansion-v0.1/
```

Candidate terms may be used only inside this directory and its validators.
Baseline manifests remain unchanged.

Promotion targets are expected to be:

- Component Library v0.3: 20 public components;
- Recipe Library v0.7: 35 public recipes;
- Analytical Mode v0.3: 19 analytical families;
- Prompt DSL next version only if accepted components or relations require a
  public schema change.

Version numbers are promotion targets, not pre-approved canonical releases.

## 7. Package architecture

```text
extensions/dynamics-expansion-v0.1/
├── README.md
├── SPEC.md
├── MIGRATION.md
├── ROLLBACK.md
├── manifest.yaml
├── schema.yaml
├── components/
│   ├── lane.md
│   ├── lane.yaml
│   ├── stock.md
│   └── stock.yaml
├── relations/
│   └── relations.yaml
├── recipes/
│   ├── 032-interaction-sequence.md
│   ├── 032-interaction-sequence.yaml
│   ├── 033-feedback-control.md
│   ├── 033-feedback-control.yaml
│   ├── 034-stock-flow.md
│   ├── 034-stock-flow.yaml
│   ├── 035-scenario-fan.md
│   └── 035-scenario-fan.yaml
├── prompts/
│   ├── 032-interaction-sequence.yaml
│   ├── 033-feedback-control.yaml
│   ├── 034-stock-flow.yaml
│   └── 035-scenario-fan.yaml
├── analytics/
│   ├── families.yaml
│   ├── datasets/
│   │   ├── 01-controlchart.yaml
│   │   ├── 02-slopegraph.yaml
│   │   └── 03-dotplot.yaml
│   └── proofs/
│       ├── 01-controlchart.yaml
│       ├── 02-slopegraph.yaml
│       └── 03-dotplot.yaml
├── drafts/
│   └── 16x9/
├── selection/
│   ├── README.md
│   ├── candidate-hashes.yaml
│   ├── overview.png
│   └── boards/
├── evaluation/
│   ├── rubric.yaml
│   ├── scores.csv
│   └── review.md
└── generated/
    ├── index.yaml
    └── compatibility.yaml
```

Draft and selected candidate rasters remain local or ignored until the user
selects a variant and explicitly approves promotion.

## 8. Candidate components

### 8.1 Lane

**Category:** structural

**Meaning:** A stable channel of responsibility owned by one actor, controller,
system, or workstream across an ordered interaction.

**Distinct from:**

- `Field`: context or environment without ordered responsibility.
- `Cluster`: grouping without a temporal route.
- `Band`: a bounded interval on an Axis.
- `Frame`: a functional boundary or lookup scope.

**Required evidence inside Wave 1:**

1. `Interaction Sequence`: actor ownership across ordered messages.
2. `Feedback Control`: separation of controller and controlled-system actions.

**Allowed relations:**

- contains `Node`;
- contains `Trace`;
- attached_to `Label`;
- is ordered by `Axis` through the existing `orders` relation when the promoted
  vocabulary permits that target;
- participates in `sends_to`, `measures`, or `corrects` through contained
  instances.

**Invariants:**

- One Lane has exactly one declared owner.
- Lane order is not semantic unless the recipe declares it.
- Lane width or color never implies priority by itself.
- A Lane is not a decorative card or UI panel.

### 8.2 Stock

**Category:** semantic-analytical

**Meaning:** A declared quantity or state that changes through measured inflows
and outflows while preserving conservation semantics.

**Distinct from:**

- `Node`: a generic entity, state, actor, or stage.
- `Pulse`: one exact highlighted value without accumulation semantics.
- `Cluster`: a group without conservation.
- `Band`: an interval rather than a stored state.

**Required evidence inside Wave 1:**

1. `Stock / Flow`: explicit starting stock, inflow, outflow, and ending stock.
2. `Feedback Control`: measured stock state compared with a target and changed
   through a correction.

**Allowed relations:**

- receives `flows_into`;
- emits `flows_out_of`;
- is targeted by `measures`;
- is highlighted by `Signal`;
- is labeled by `Label`;
- is bounded by `Threshold` or `Band` when quantitative conditions require it.

**Invariants:**

- Stock identity and unit are explicit.
- Starting value, inflows, outflows, and ending value reconcile.
- Area is not proportional to value unless declared by an analytical encoding.
- Color is not the only carrier of stock state.

## 9. Candidate relations

### 9.1 `sends_to`

One declared actor transmits a named message, request, result, or response to
another declared actor.

It does not imply causation, ownership, or successful delivery.

### 9.2 `measures`

A controller, observer, or analytical mark reads a named property of a target.

The measured field, unit, and observation point must be explicit.

### 9.3 `corrects`

A declared action changes a measured system state in response to a declared
deviation from target.

It must identify the target state and direction of correction.

### 9.4 `flows_into`

A declared rate or quantity increases a `Stock` over an interval.

### 9.5 `flows_out_of`

A declared rate or quantity decreases a `Stock` over an interval.

### 9.6 `diverges_to`

One shared observed state separates into two or more explicitly named future
scenario paths.

It does not mean a decision was made. Scenario probability is included only
when the source provides it.

### 9.7 Relation promotion rule

A candidate relation may remain package-local even when its recipe is accepted.
Public promotion requires:

- a semantic meaning not expressible through an existing relation;
- compatibility review across every target component;
- deterministic validation;
- no ambiguity with existing `directs`, `connected_to`, `produces`, `orders`,
  `transitions_to`, `causes`, `crosses`, or `depends_on` semantics.

## 10. Recipe contracts

### 10.1 `032 Interaction Sequence`

**Problem:** Explain ordered message exchange between multiple actors, including
waits, returns, errors, or retries.

**Distinct from:**

- `Workflow`: action order without actor-to-actor message ownership.
- `Architecture`: stable topology without an ordered temporal route.
- `State Machine`: guarded state transition without message chronology.

**Required components:**

- `Lane`: 2-4;
- `Node`: 2-8;
- `Trace`: 1-3;
- `Vector`: 2-8;
- `Label`: 4-12;
- `Signal`: exactly 1.

**Relations:**

- `sends_to`;
- `directs`;
- `orders`;
- `attached_to`;
- `highlights`.

**Expression:** A or B; C forbidden.

**Default mode:** Structural.

**Reading path:** top-to-bottom time within left-to-right actor ownership.

**Demo visible copy:**

```text
ДЕ АГЕНТ ЧЕКАЄ
USER
AGENT
TOOL
ЗАПИТ
ВИКЛИК
РЕЗУЛЬТАТ
ВІДПОВІДЬ
ОЧІКУВАННЯ
RETRY
```

**Visual variants must differ by mechanism:**

1. Parallel actor Lanes with a vertical time route.
2. Central Agent Lane with mirrored request and response Traces.
3. Compact stepped interaction with one explicit wait interval and retry path.

### 10.2 `033 Feedback Control`

**Problem:** Explain how a system measures deviation from a target and applies a
corrective action.

**Distinct from:**

- `Loop`: recurrence without a control target.
- `Causal Chain`: one-way consequence without closed correction.
- `State Machine`: guarded states without measured deviation.

**Required components:**

- `Lane`: 2;
- `Stock`: 1;
- `Loop`: 1;
- `Threshold`: 1-2;
- `Trace`: 1;
- `Pulse`: 1-2;
- `Signal`: exactly 1;
- `Label`: 4-10.

**Relations:**

- `measures`;
- `corrects`;
- `crosses`;
- `repeats`;
- `highlights`;
- `attached_to`.

**Expression:** A or B; C forbidden.

**Default mode:** Structural with bounded Analytical evidence.

**Demo visible copy:**

```text
АВТОНОМНІСТЬ ПОТРЕБУЄ FEEDBACK
TARGET
MEASURE
COMPARE
CORRECT
BACKLOG
ВІДХИЛЕННЯ
```

**Visual variants must differ by mechanism:**

1. Closed control Loop around one measured Stock.
2. Controller and system Lanes with one returning Trace.
3. Target-to-deviation Axis with an explicit corrective return path.

### 10.3 `034 Stock / Flow`

**Problem:** Explain how inflows and outflows change a stored state over a
declared interval.

**Distinct from:**

- `Pipeline`: transformation through stages.
- `Sankey`: distribution between nodes.
- `Waterfall`: reconciliation of signed contributions without persistent stock
  semantics.

**Required components:**

- `Stock`: exactly 1;
- `Vector`: 2-4;
- `Pulse`: 3-6;
- `Label`: 4-10;
- `Signal`: exactly 1.

**Optional components:**

- `Axis`: 0-1;
- `Band`: 0-1;
- `Threshold`: 0-1.

**Relations:**

- `flows_into`;
- `flows_out_of`;
- `attached_to`;
- `highlights`;
- `bounds` when an interval is declared.

**Expression:** A or B; C forbidden.

**Default mode:** Structural with exact quantitative reconciliation.

**Demo visible copy and values:**

```text
BACKLOG ЗМІНЮЄТЬСЯ ПОТОКАМИ
ПОЧАТОК 24
НОВІ ЗАДАЧІ +12
BACKLOG 28
ЗАВЕРШЕНО -8
```

Required reconciliation:

```text
24 + 12 - 8 = 28
```

**Visual variants must differ by mechanism:**

1. Horizontal inflow-stock-outflow composition.
2. Central Stock with opposed signed Vectors and direct reconciliation.
3. Interval-based change with start and end stock states connected by flows.

### 10.4 `035 Scenario Fan`

**Problem:** Explain several plausible future trajectories that share one
observed state and diverge under declared assumptions.

**Distinct from:**

- `Decision Tree`: rules and decisions.
- `Roadmap`: planned workstreams and milestones.
- `Line`: one or more observed series with a forecast contract.

**Required components:**

- `Axis`: 1-2;
- `Trace`: 3-5;
- `Band`: 1-3;
- `Threshold`: 0-2;
- `Label`: 5-12;
- `Signal`: exactly 1.

**Relations:**

- `diverges_to`;
- `orders`;
- `bounds`;
- `crosses` when a declared condition is crossed;
- `highlights`.

**Expression:** A or B; C forbidden.

**Default mode:** Analytical.

**Demo visible copy:**

```text
ОДНЕ РІШЕННЯ. ТРИ ТРАЄКТОРІЇ.
NOW
NEXT
LATER
BASELINE
GUARDED
AUTONOMOUS
НЕВИЗНАЧЕНІСТЬ
```

No probabilities are shown because the demo source does not provide them.

**Visual variants must differ by mechanism:**

1. Shared origin with three directly labeled Traces and one uncertainty Band.
2. Baseline Axis with guarded and autonomous divergence around it.
3. Three scenario corridors with common NOW state and separated LATER outcomes.

## 11. Analytical family contracts

### 11.1 `controlchart`

**Purpose:** Determine whether an ordered process is stable or contains declared
special-cause variation.

**Required data:**

- ordered observation identity;
- time or declared sequence;
- exact observed value;
- unit;
- centerline;
- upper control limit;
- lower control limit;
- limit derivation method;
- source and transformation provenance.

**Rules:**

- Limits are computed deterministically from the declared method or supplied as
  source values.
- Observations are not silently reordered.
- Control limits are not target or specification limits unless explicitly
  declared as such.
- Special-cause markers identify the exact triggering rule.
- Missing observations remain visible as gaps.
- Color is not the only anomaly carrier.

**Hard exclusions:**

- undeclared limits;
- target presented as control limit;
- decorative smoothing;
- hidden missing values;
- silent aggregation;
- dual axes;
- gauge rendering.

### 11.2 `slopegraph`

`dumbbell` is an allowed rendering form of the same paired-change family, not a
separate public family.

**Purpose:** Compare the same entities across exactly two declared states.

**Required data:**

- unique entity identity;
- state A identity and value;
- state B identity and value;
- shared unit;
- shared quantitative domain;
- signed delta;
- source and transformation provenance.

**Rules:**

- Every visible connector binds one entity across both states.
- State ordering is explicit and stable.
- Values share one scale.
- Direct labels identify entities and endpoints.
- Delta is derived deterministically.
- Missing endpoints are declared and never connected as complete pairs.

**Hard exclusions:**

- unrelated entities connected as pairs;
- independent scales;
- silent entity omission;
- slope angle presented as an independent metric;
- invented intermediate values;
- decorative crossing reduction through hidden reordering.

### 11.3 `dotplot`

**Purpose:** Compare many categorical values compactly through position on one
declared quantitative domain.

**Required data:**

- unique category identity;
- exact value;
- unit;
- declared domain;
- category order;
- source and transformation provenance.

**Rules:**

- Position is the primary quantitative encoding.
- Zero inclusion is declared according to the analytical question.
- Category order is source order or a declared deterministic sort.
- Selected points receive direct labels.
- Multiple series require shape, label, or another non-color carrier.
- Overlapping points use a declared strategy.

**Hard exclusions:**

- decorative jitter;
- silent sorting;
- area encoding without a declared size field;
- color-only categories;
- hidden domain truncation;
- unlabeled highlighted points.

## 12. Static dynamics contract

Dynamics Expansion represents motion through static semantic evidence:

- `Axis` for ordered time or quantitative domain;
- `Lane` for responsibility;
- `Trace` for observed or scenario route;
- `Vector` for directed action;
- `Loop` for recurrence;
- `Band` for interval or uncertainty;
- `Threshold` for state-changing conditions;
- direct labels for actor, state, value, unit, and route identity.

Animation, transitions, autoplay, and frame sequences are prohibited. A still
slide must communicate the mechanism without narration or hover.

## 13. Expression and density

- A/B/C continue to control amplitude only.
- Structural and Analytical remain orthogonal modes.
- All four recipes forbid Level C because their semantics depend on multiple
  ordered elements.
- Level A uses the minimum complete mechanism.
- Level B permits one additional state, branch, interval, or return path.
- Analytical density is allowed only when exact scales, labels, units, and
  sources remain readable at `1280x720`.
- One dominant Signal remains mandatory.

## 14. Visual evidence contract

Each recipe receives exactly three independent candidates:

```text
032:v1, v2, v3
033:v1, v2, v3
034:v1, v2, v3
035:v1, v2, v3
```

Candidates must differ materially in:

1. composition topology;
2. visual mechanism;
3. reading path;
4. use of scale, space, containment, or direction.

Changing only color, alignment, typography scale, or minor geometry does not
count as a separate candidate.

Every active candidate must:

- be PNG;
- be exactly `1920x1080`;
- use RGB or RGBA mode;
- have a unique SHA-256 hash;
- preserve exact visible copy;
- pass prohibited-element review;
- remain readable at `1280x720`;
- use the complete canonical reference hierarchy;
- remain unpromoted until user selection.

Selection syntax:

```text
032:v_, 033:v_, 034:v_, 035:v_
```

## 15. Candidate component evidence matrix

| Component | Use 1 | Use 2 | Promotion condition |
|---|---|---|---|
| `Lane` | Interaction Sequence actor ownership | Feedback Control controller/system ownership | Both selected recipe proofs require Lane semantics and cannot use Field or Cluster without loss |
| `Stock` | Stock / Flow conservation | Feedback Control measured controlled state | Both deterministic proofs reconcile identity, unit, and state change |

A component remains package-local if either use can be represented faithfully by
the existing public vocabulary.

## 16. Prompt DSL boundary

The package must not edit the baseline Prompt DSL schema.

Candidate packages include local extension fields for:

- `Lane` and `Stock` instances;
- six candidate relations;
- analytical family bindings;
- dataset provenance;
- rendering-specific constraints.

Promotion review decides whether to:

1. add accepted vocabulary to the next Prompt DSL version;
2. keep analytical terms inside Analytical Mode;
3. retain one or more relations as package-local recipe semantics.

No candidate term may silently appear in a baseline package.

## 17. Deterministic analytical proofs

The three analytical families use typed synthetic fixed datasets.

Each proof contains:

- canonical dataset;
- source package;
- deterministic derived package;
- exact values and units;
- provenance digest;
- expected compatibility output;
- one or more negative mutations.

Rebuilding twice from identical inputs must produce byte-identical generated
YAML.

Raster evidence is not required for analytical family acceptance in this
package. Visual raster generation for analytical families requires a separate
explicit objective.

## 18. Validation architecture

### 18.1 Main validator

```text
tools/validate_dynamics_expansion.py
```

It validates:

- package version and dependency boundary;
- exact counts: 4 recipes, 2 components, 6 relations, 3 families;
- recipe IDs `032-035`;
- candidate-only status;
- component evidence matrix;
- relation compatibility;
- exact demo copy;
- recipe ingredient cardinality;
- analytical dataset and encoding contracts;
- deterministic proof derivation;
- protected raster inventory;
- generated index and compatibility drift.

### 18.2 Review builder

```text
tools/build_dynamics_review.py
```

It builds and validates:

- four three-candidate comparison boards;
- one review overview;
- candidate hash inventory;
- selected-candidate placeholders only after user selection;
- no automatic promotion.

### 18.3 Negative fixtures

The package must reject at least:

1. message without sender or receiver;
2. Lane without owner;
3. correction without measured deviation;
4. Stock without unit;
5. unreconciled stock equation;
6. outflow encoded as inflow;
7. scenario path without shared origin;
8. invented scenario probability;
9. control limit used as target without declaration;
10. reordered paired entity;
11. mismatched slopegraph scales;
12. dotplot category silently sorted;
13. candidate term used in baseline Prompt DSL;
14. Level C used for a Dynamics recipe;
15. accepted raster hash mutation;
16. duplicate visual candidate hash;
17. superficial variant with identical declared mechanism and composition.

## 19. Testing

### Primary signal

The package is successful when all four semantic gaps have distinct,
publication-readable, user-selected visual evidence and all three analytical
families rebuild from typed data without distortion.

### Secondary signals

- focused validator tests pass;
- negative fixtures fail with exact expected errors;
- generated outputs are deterministic;
- component and relation compatibility is complete;
- existing component, recipe, analytical, accessibility, and Design Book
  validators remain green;
- accepted raster hashes remain byte-identical;
- `git diff --check` passes.

### Expected commands

```bash
.venv/bin/python -m pytest -q
.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1
.venv/bin/python tools/build_dynamics_review.py extensions/dynamics-expansion-v0.1 --validate
.venv/bin/python tools/validate_component_library.py components/component-library-v0.1/manifest.yaml
.venv/bin/python tools/validate_recipe_library.py recipes/recipe-library-v0.5/manifest.yaml
.venv/bin/python tools/validate_analytical_mode.py analytics/analytical-mode-v0.1
.venv/bin/python tools/validate_accessibility_mode.py accessibility/night-mode-v0.1
.venv/bin/python tools/validate_design_book.py cookbook/design-book-v1.0
git diff --check
```

When D-035 has been promoted, the commands must point to the actual promoted
component, recipe, and analytical package versions.

## 20. Error handling

- Builders stop before writing derived outputs when source validation fails.
- Validation errors identify the file, record ID, field, and violated invariant.
- Candidate raster failures do not delete or overwrite earlier evidence.
- Regenerated candidates receive new hashes while rejected passes remain review
  evidence.
- A failed promotion review leaves the entire baseline unchanged.
- Missing built-in image generation stops at the complete prompt package and
  reports `built-in Codex image generation unavailable`.

## 21. Migration

The package has no automatic migration into canonical libraries.

Promotion is additive:

1. Select one candidate per recipe.
2. Complete exact-copy and rubric review.
3. Decide component and relation promotion individually.
4. Generate new versioned component, recipe, analytical, and DSL packages.
5. Rebuild compatibility and indexes.
6. Revalidate protected raster hashes.
7. Keep prior versions available for rollback.

Existing Prompt DSL packages, source prompts, datasets, and rasters remain valid.

## 22. Rollback

Before promotion, rollback means removing or ignoring the additive incubation
package. No canonical consumer changes.

After promotion, rollback means restoring consumers to the previous versioned
manifests. Previous package versions and accepted raster evidence remain
available and unchanged.

No rollback requires raster regeneration.

## 23. Documentation

Implementation must create or update only Dynamics-specific documentation until
promotion:

- package README and SPEC;
- migration and rollback guides;
- component and recipe Markdown contracts;
- analytical family contracts;
- evaluation review;
- generated index and compatibility outputs.

Root `STATUS.md`, `DECISIONS.md`, `CHANGELOG.md`, Foundation spec, Cookbook, and
public library manifests change only when the package is completed or a public
promotion decision is approved.

## 24. Implementation sequence

1. Create package skeleton, schema, manifest, and validator tests.
2. Define `Lane`, `Stock`, and candidate relations.
3. Define four recipe Markdown and YAML contracts.
4. Implement three analytical datasets, proofs, negative fixtures, builder, and
   validator.
5. Build generated index and compatibility outputs.
6. Produce exact Prompt DSL packages for the four visual demos.
7. Generate three materially different candidates per recipe.
8. Build comparison boards and review overview.
9. Wait for user selection.
10. Complete rubric, compatibility, and promotion review.

## 25. Acceptance criteria

Dynamics Expansion v0.1 is specification-complete when:

- the package contains exactly 4 recipes, 2 component candidates, 6 relation
  candidates, and 3 analytical families;
- every term has a distinct nearest-neighbor statement;
- both components have two independent evidenced uses;
- every recipe has three materially different `1920x1080` candidates;
- every active candidate preserves exact copy and has a unique hash;
- all analytical datasets and proofs are typed, fixed, and deterministic;
- all negative fixtures fail for their intended reason;
- no baseline schema, manifest, or accepted raster has changed;
- selection remains with the user;
- no promotion occurs before review completion.

The package is not publicly complete until the user selects one candidate per
recipe and explicitly approves promotion.

## 26. Approved design decisions

- Scope is Wave 1 only.
- Architecture is one unified Dynamics Expansion package.
- The package is evidence-gated and additive.
- D-035 promotion is a prerequisite.
- Visual evidence is three materially different candidates per recipe.
- Analytical evidence is deterministic and raster-free.
- `Lane` and `Stock` require two independent uses.
- Six candidate relations are allowed locally.
- Dynamics remains static; animation and transitions are non-goals.
- User selection controls visual promotion.

## 27. Spec self-review

- Placeholder scan: no unresolved placeholder markers or incomplete required
  decision.
- Internal consistency: counts, IDs, vocabulary, package boundary, and promotion
  targets agree across sections.
- Scope check: the spec contains Wave 1 only and is suitable for one phased
  implementation plan.
- Ambiguity check: recipe ownership, component meanings, relation semantics,
  exact demo copy, evidence, validation, migration, rollback, and promotion are
  explicit.
- Compatibility check: canonical contracts remain immutable until promotion.
