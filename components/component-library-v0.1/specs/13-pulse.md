# 13 Pulse

## Purpose

Make one exact number or measure the dominant explanatory object.

## Semantic meaning

A Pulse is a bounded value whose attached label, unit, period, and provenance establish what the number means. It is not a generic large numeral, a gauge, or an unsupported performance claim.

## Visual and spatial contract

Use at most one Pulse in a composition. Keep its label and any required unit attached. When the value comes from a dataset, retain the exact period and source. Supporting metrics remain subordinate and cannot become peer Pulses.

## Dimensions and ranges

- width: `122–980 px`;
- height: `44–520 px`;
- area: `1–18%`;
- count: zero or one;
- context fields when supplied: unit, period, and source.

## Allowed relations

- inbound direct `Label attached_to Pulse`;
- `inside → Field | Frame`;
- inbound `Axis orders Pulse` for restrained supporting comparison;
- inbound `Cluster groups Pulse` when the Pulse leads a bounded summary;
- inbound one `Signal highlights Pulse`.

## Forbidden relations

- `repeats → Loop`: one value does not establish recurrence;
- `produces → Collision`: a value does not cause synthesis;
- `directs → Vector`: numeric prominence does not establish action;
- `maps_to → Legend`: the Pulse remains directly labeled;
- detached units, invented targets, deltas, trends, or interpretations.

## Compatible Visual DNA families

Direct evidence: Big Number, KPI, and Dashboard.

## Expression levels

- **A:** maximum one and 18% area;
- **B:** maximum one and 18% area;
- **C:** conditional maximum one when the value and essential context remain short enough for one unambiguous Signal peak.

## Typography and semantic color

Use Modular Technical numeric display with tabular figures. Keep units attached and the direct Label legible. Default color is `ink.primary`; the value or its baseline may carry the one Signal, but color cannot introduce a second quantity.

## Do examples

- Big Number: use the exact `3` with its attached level label and named context.
- KPI: use exact W4 `90%` with period, success label, supporting context, and `DEMO DATA` provenance.
- Dashboard: make one exact Pulse primary while all supporting metrics remain subordinate.

## Don't examples

- Do not add a gauge, donut, fake target, invented delta, detached unit, or second peer metric.
- Do not infer a trend from a single snapshot value.

## Prompt DSL syntax

```text
Pulse(id=<id>, value=<value-ref>, label=<label-ref>)
```

Required fields: `id`, `value`, `label`. Optional fields: `unit`, `period`, `source`, `signal_state`.

## Validation invariants

- at most one Pulse per composition;
- exact value, label, unit, period, and source when supplied by evidence;
- no unsupported target, trend, delta, or interpretation;
- supporting values remain subordinate;
- color is never the only carrier of quantitative meaning.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.1: one key number or measure;
- `patterns/visual-dna-sprint-01/specs/04-big-number.md`: one exact editorial value and attached context;
- `patterns/visual-dna-sprint-01/specs/17-kpi.md`: one exact operational snapshot with unit, period, and source;
- `patterns/visual-dna-sprint-01/specs/20-dashboard.md`: one primary Pulse in a bounded analytical summary;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Big Number, KPI, and Dashboard: accepted Pulse behavior.
