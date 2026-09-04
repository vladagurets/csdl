# 023 Formula

## Problem

State an exact ordered symbolic relationship and its exact result as one culmination.

## Allowed scenarios

- summary equation.
- multiplicative model.
- culminating formula.

## Ingredients and cardinality

- Required `Anchor`: 2–2.
- Required `Collision`: 1–1.
- Required `Signal`: 1–1.
- Optional `Label`: 0–2.

## Allowed relations

- `Collision overlaps Anchor`.
- `Collision produces Signal`.
- `Label attached_to Anchor`.

## Forbidden relations

- `Collision groups Anchor` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. bind operands and operators in exact order.
2. bind the exact result as the second Anchor.
3. use one Collision and one Signal to connect formula and result.

## Expression levels

- Level A: `forbidden` — Accepted evidence is a culmination with a strong symbolic relationship.
- Level B: `conditional` — The equation and result stay short and the signal remains restrained.
- Level C: `allowed`.

## Compatible Visual DNA families

- `collision`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `left_to_right`, `split_to_result`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `formula`, `result`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `ordered-symbolic-formula-to-result`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Anchor`=2, `Collision`=1, `Signal`=1, `Label`=0.
- Expression: `C`.
- Density: `low`.
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
- this is the only Level C slide.
- text is short, large, horizontal, and exact.
- no extra slogan, footer, logo, icons, shards, or propaganda cues.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `pilots/01-agentic-discipline/prompts/07-share-card.yaml` — Canonical content and legacy mechanism. (accepted legacy Prompt DSL package).
- `pilots/01-agentic-discipline/evaluation/review.md` — Three-candidate selection, exact-copy, readability, and score evidence. (Slide 07 — Share formula / Level C).
- `pilots/01-agentic-discipline/canonical/light/16x9/7.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Formula`.
- Migration: Legacy zone and Signal-plane hints are discarded; exact operand/operator order and Collision relations carry the formula.
- Rollback: Revert the additive recipe record and derived outputs; accepted Pilot prompt and raster bytes remain unchanged.
