# 17 KPI

## Problem

Expose one primary operational measure with only the context needed to interpret it.

## Allowed scenarios

Status measure, target tracking, or weekly snapshot over a small controlled dataset.

## Semantic components

The primary value is a `Pulse`; period and label establish scope; restrained supporting values form a subordinate `Axis`.

## Assembly order

1. Place the W4 success-rate Pulse.
2. Attach its label and period.
3. Add the three exact W4 supporting values.
4. Add the required demo-data source label.

## Expression levels

Only Level A is allowed in Milestone 2. Brand expression recedes behind quantitative fidelity.

## Typography and spacing

Use strong numeric typography, explicit units, tabular alignment for supporting values, 96 px margins, and no dense card grid.

## Signal constraints

Dusty data blue marks `90%` only and occupies no more than 6%. Color is not the only carrier of primacy.

## Canonical content

The W4 snapshot in `data/agent-reliability-demo.yaml`: 55 runs, 90% success, 10 review minutes, 2 escaped defects, and `DEMO DATA`.

## Hard exclusions

No gauge, donut, fake target, invented delta, hidden unit, status icon, green-for-good shortcut, or decorative card shell.

## Prompt DSL contract

`prompts/17-kpi.yaml` pins every W4 value and identifies the work as a Visual DNA prototype.

## Acceptance criteria

All values and units exact; 90% reads first; supporting metrics remain readable; no unsupported interpretation.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates and verified against the fixed dataset.
