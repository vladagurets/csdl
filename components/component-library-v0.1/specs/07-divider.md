# 07 Divider

## Purpose

Separate peer states, positions, or scopes without establishing scale, direction, or moral priority.

## Semantic meaning

A Divider is a subordinate distinction boundary between two comparable regions. It says “different scopes,” not “before/after order,” “greater/lesser,” or “move this way.”

## Visual and spatial contract

Use exactly one thin Divider for exactly two peer subjects. Keep it subordinate to their Labels and Anchors. Orientation follows the two subjects but does not itself create a reading path.

## Dimensions and ranges

- thickness: `1–4 px`;
- width: `1–1728 px`;
- height: `1–936 px`;
- area: `0.01–2%`;
- count: zero or one.

## Allowed relations

- `separates → Field | Anchor | Frame` with two peer subjects.

## Forbidden relations

- `orders → any`: use Axis;
- `directs → any`: use Vector;
- `connected_to → any`: use Bridge;
- a decorative split-screen plane or unequal moral boundary.

## Compatible Visual DNA families

Direct evidence: Comparison and Before / After.

## Expression levels

- **A:** one, area below `2%`;
- **B:** one, area below `2%`;
- **C:** conditional one only when peer distinction remains essential inside the single Signal peak.

## Typography and semantic color

Divider carries no text. Labels belong to the separated subjects. Use `neutral.line`; a Divider is not a Signal target in v0.1.

## Do examples

- Comparison: one thin line preserves equal open Fields.
- Before / After: one restrained boundary preserves peer state readability while Vector owns transformation.

## Don't examples

- Do not use the Divider as a quantitative Axis.
- Do not thicken it into decorative split-screen geometry.

## Prompt DSL syntax

```text
Divider(id=<id>, subjects=<instance-ids>)
```

Required fields: `id`, `subjects`. Optional fields: `orientation`, `tone`, `gap`.

## Validation invariants

- exactly two peer subjects;
- no order, direction, scale, or connectivity semantics;
- maximum one Divider;
- area remains below `2%`.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.4 and Comparison recipe;
- `patterns/visual-dna-sprint-01/specs/05-comparison.md`: equal Fields and thin distinction;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Comparison and Before / After: accepted subordinate Divider behavior.
