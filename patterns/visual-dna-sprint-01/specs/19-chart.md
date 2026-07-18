# 19 Chart

## Problem

Reveal one quantitative trend without distorting scale or turning chart furniture into decoration.

## Allowed scenarios

Single-series trend, ordered comparison, or bounded progress over a fixed small dataset.

## Semantic components

Honest `Axis` components establish domain; four `Node`s carry exact values; one `Signal` highlights the final point.

## Assembly order

1. Define W1–W4 in order and a 0–100% value domain.
2. Plot 72, 78, 84, and 90 exactly.
3. Label points directly.
4. Signal W4 without changing scale.

## Expression levels

Only Level A is allowed in Milestone 2. Complete chart rules remain deferred to Milestone 5.

## Typography and spacing

Use direct labels, neutral axes, 96 px margins, and enough plot area to distinguish the four values honestly.

## Signal constraints

Dusty data blue carries the series; coral is not added. The W4 point may be heavier but not displaced.

## Canonical content

`УСПІШНІСТЬ ЗРОСТАЄ ЩОТИЖНЯ`, W1 72%, W2 78%, W3 84%, W4 90%, and `DEMO DATA`.

## Hard exclusions

No truncated unlabeled axis, smoothed invented curve, missing point label, 3D, area gradient, decorative grid, or extra series.

## Prompt DSL contract

`prompts/19-chart.yaml` pins the percent domain, point order, exact labels, and direct-label requirement.

## Acceptance criteria

All four values exact and ordered; geometry preserves proportions; trend is clear; no visual exaggeration.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates and verified against the fixed dataset.
