# 09 Matrix

## Problem

Position a small set of options across two independent dimensions so relative placement carries meaning.

## Allowed scenarios

Prioritization, portfolio view, or risk map with two explicit axes and at most six points.

## Semantic components

Two `Axis` components define the `Field`; four labeled `Node`s occupy it; one `Signal` marks the selected option.

## Assembly order

1. Define and label two independent axes.
2. Keep quadrants open rather than boxed.
3. Place each Node at a deliberate coordinate.
4. Select one high-impact option.

## Expression levels

Levels A and B are allowed. B is canonical because relative placement is the teaching object. C is excluded.

## Typography and spacing

Use readable direct labels, thin neutral axes, a clear origin, and sufficient point separation at `1280×720`.

## Signal constraints

Coral marks `АВТОМАТИЗУВАТИ` only and occupies no more than 6%.

## Canonical content

Exact headline, axes `ВПЛИВ` and `ЗУСИЛЛЯ`, and the four named options.

## Hard exclusions

No unlabeled axes, pseudo-precise ticks, overlapping labels, quadrant card backgrounds, decorative grid, or invented scores.

## Prompt DSL contract

`prompts/09-matrix.yaml` defines the relative positions and direct labeling without numeric claims.

## Acceptance criteria

Axes are independent and readable; every option is distinct; the selected Node is semantic; no fake precision.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
