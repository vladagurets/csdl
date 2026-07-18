# 010 Hierarchy

## Problem

Show levels of ownership or decomposition without implying sequence.

## Allowed scenarios

- goal decomposition.
- taxonomy.
- authority.

## Ingredients and cardinality

- Required `Anchor`: 1–1.
- Required `Frame`: 1–4.
- Required `Node`: 2–7.
- Required `Bridge`: 1–4.
- Required `Label`: 2–7.

## Allowed relations

- `Frame contains Node`.
- `Bridge connected_to Node`.
- `Label attached_to Node`.

## Forbidden relations

- `Frame directs Node` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. place root Anchor.
2. nest or branch child Nodes.
3. preserve one top-to-bottom depth cue.

## Expression levels

- Level A: `allowed`.
- Level B: `allowed`.
- Level C: `forbidden` — No accepted evidence supports this recipe at the expression level.

## Compatible Visual DNA families

- `hierarchy`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `top_to_bottom`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `levels`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `hierarchy-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Expression: `A`.
- Density: `low`.
- Reading path: `top_to_bottom`.
- Palette: light Muted Signal on warm paper; output is exact `1920×1080` PNG.

## Hard exclusions

- extra text.
- logos or repeated footers.
- UI chrome or decorative card shells.
- decorative coordinates or random dot fields.
- gradients, shadows, glossy surfaces, or 3D.
- political, Soviet, or revolutionary-poster styling.
- pixel, bitmap, dot-matrix, segmented, or retro-computer lettering.
- workflow arrow chain.
- avatars.
- duplicate parents.
- decorative boxes.
- org-chart UI.
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

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 10 Hierarchy).
- `patterns/visual-dna-sprint-01/specs/10-hierarchy.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `patterns/visual-dna-sprint-01/canonical/light/16x9/10-hierarchy.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Hierarchy`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
