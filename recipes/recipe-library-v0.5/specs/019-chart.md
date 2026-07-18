# 019 Chart

## Problem

Reveal one quantitative trend without distorting its scale or adding decorative geometry.

## Allowed scenarios

- trend.
- comparison over time.
- progress.

## Ingredients and cardinality

- Required `Axis`: 2–2.
- Required `Node`: 2–7.
- Required `Label`: 3–12.
- Required `Signal`: 1–1.
- Optional `Legend`: 0–1.

## Allowed relations

- `Axis orders Node`.
- `Label attached_to Node`.
- `Signal highlights Node`.
- `Legend maps_to Node`.

## Forbidden relations

- `Axis repeats Node` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. define honest Axes.
2. plot ordered values.
3. label directly.
4. signal final point.

## Expression levels

- Level A: `allowed`.
- Level B: `forbidden` — No accepted evidence supports this recipe at the expression level.
- Level C: `forbidden` — No accepted evidence supports this recipe at the expression level.

## Compatible Visual DNA families

- `chart`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `left_to_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `data_blue`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `series`, `points`, `source_label`.
- Optional bindings: `quantitative_contract`.
- Copy/data is exact, order-preserving, and limited to 140 words or atomic values.
- Data contract: `patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml`.

## Prompt DSL v0.5

- Semantic mechanism: `chart-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Axis`=2, `Node`=4, `Label`=5, `Signal`=1, `Legend`=0.
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
- truncated unlabeled axis.
- smoothed curve.
- missing point label.
- extra series.
- decorative grid.
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

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 19 Chart).
- `patterns/visual-dna-sprint-01/specs/19-chart.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `patterns/visual-dna-sprint-01/canonical/light/16x9/19-chart.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Chart`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
