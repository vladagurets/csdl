# 020 Dashboard

## Problem

Summarize a small operational state while preserving one clear primary signal.

## Allowed scenarios

- weekly status.
- operating review.
- compact monitoring.

## Ingredients and cardinality

- Required `Pulse`: 1–1.
- Required `Cluster`: 1–1.
- Required `Axis`: 1–2.
- Required `Label`: 4–12.
- Required `Signal`: 1–1.
- Optional `Legend`: 0–1.

## Allowed relations

- `Cluster groups Pulse`.
- `Axis orders Pulse`.
- `Label attached_to Pulse`.
- `Signal highlights Pulse`.
- `Legend maps_to Signal`.

## Forbidden relations

- `Cluster orders Pulse` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. place primary Pulse.
2. group three supporting measures.
3. add one restrained trend.
4. preserve direct labels.

## Expression levels

- Level A: `allowed`.
- Level B: `forbidden` — No accepted evidence supports this recipe at the expression level.
- Level C: `forbidden` — No accepted evidence supports this recipe at the expression level.

## Compatible Visual DNA families

- `dashboard`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `left_to_right`, `top_left_to_bottom_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `data_blue`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `metrics`, `trend`, `source_label`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 140 words or atomic values.
- Data contract: `patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml`.

## Prompt DSL v0.5

- Semantic mechanism: `dashboard-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Pulse`=1, `Cluster`=1, `Axis`=1, `Label`=10, `Signal`=1, `Legend`=0.
- Expression: `A`.
- Density: `analytical`.
- Reading path: `left_to_right`.
- Palette: light Muted Signal on warm paper; output is exact `1920×1080` PNG.

## Hard exclusions

- extra text.
- logos or repeated footers.
- UI chrome or decorative card shells.
- decorative coordinates or random dot fields.
- gradients, shadows, glossy surfaces, or 3D.
- political, Soviet, or revolutionary-poster styling.
- pixel, bitmap, dot-matrix, segmented, or retro-computer lettering.
- navigation.
- filters.
- buttons.
- status icons.
- rounded widgets.
- invented deltas.
- gauges.
- extra chart.
- gradients.
- shadows.
- 3D.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 20 Dashboard).
- `patterns/visual-dna-sprint-01/specs/20-dashboard.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `patterns/visual-dna-sprint-01/canonical/light/16x9/17.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Dashboard`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
