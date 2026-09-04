# 15 Legend

## Purpose

Provide a subordinate indirect key for two to four analytical categories only when direct labels cannot fit without collision or ambiguity.

## Semantic meaning

A Legend is a conditional mapping from repeated text-and-form keys to analytical categories. It is never a primary Signal, visual mechanism, decorative palette strip, or substitute for direct Labels.

## Visual and spatial contract

Use at most one Legend with two to four items. Every item combines readable text with a distinct semantic form, so color is never the only carrier. The composition must record why direct Labels collide or remain ambiguous. Current accepted single-series Chart and Dashboard evidence does not satisfy that exception and therefore uses no Legend.

## Dimensions and ranges

- width: `122–612 px`;
- height: `44–320 px`;
- area: `0.5–8%`;
- count: zero or one;
- items: two to four.

## Allowed relations

- `maps_to → Signal | Label | Node` for one or more declared analytical categories;
- `inside → Field | Frame` when the analytical scope requires it.

## Forbidden relations

- `highlights → Signal`: the Legend cannot become the dominant emphasis;
- `orders → Axis`: the Legend does not establish quantitative order;
- `directs → Vector`: key placement does not establish action;
- `produces → Collision`: a mapping key does not create synthesis;
- `repeats → Loop`: repeated key forms do not establish recurrence;
- any use that color alone must explain.

## Compatible Visual DNA families

Conditional only: Chart and Dashboard. The accepted Milestone 2 examples use direct Labels and do not constitute canonical Legend use.

## Expression levels

- **A:** conditional maximum one with two to four items, after a proof records why direct Labels fail;
- **B:** forbidden because Milestone 2 contains no accepted Level B analytical evidence for an indirect key;
- **C:** forbidden because a multi-item key conflicts with a short single-peak Signal composition.

## Typography and semantic color

Use horizontal Foundation Label typography in direct reading order. Pair every text label with a semantic form. Use only semantic palette values; the Legend remains subordinate and cannot itself carry Signal color as an attention device.

## Do examples

- Conditionally map two to four analytical categories after documenting a direct-label collision or ambiguity.
- Use the primary-authority palette key strip only to calibrate repeated text-and-form construction, not as evidence that a Visual DNA family needs a Legend.

## Don't examples

- Do not add a Legend to the accepted single-series Chart; all four points are directly labeled.
- Do not turn a palette strip, row of swatches, or UI key into a primary visual mechanism.

## Prompt DSL syntax

```text
Legend(id=<id>, items=<mapping-items>, reason_direct_labels_fail=<reason>)
```

Required fields: `id`, `items`, `reason_direct_labels_fail`. Optional fields: `placement`, `order`.

## Validation invariants

- exactly two to four category mappings when present;
- every item combines readable text with a distinct semantic form;
- an explicit direct-label failure reason is recorded;
- color is never the only carrier of meaning;
- Legend remains subordinate and cannot carry the dominant Signal;
- no current canonical family use is claimed.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, Analytical Mode: direct Labels are preferred over a Legend;
- `patterns/visual-dna-sprint-01/specs/19-chart.md`: accepted single-series evidence requires direct point Labels;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Chart: no Legend or extra series is present;
- `references/canonical/1.png`: construction calibration for a text-and-form key only, not family-use evidence.
