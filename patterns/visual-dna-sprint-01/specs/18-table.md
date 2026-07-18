# 18 Table

## Problem

Support exact lookup and comparison across a small fixed dataset.

## Allowed scenarios

Compact report, value audit, or weekly comparison where exact values matter more than visual trend.

## Semantic components

One restrained `Frame` aligns row/column `Axis` roles; a `Signal` identifies the current period without hiding values.

## Assembly order

1. Place the title and source label.
2. Align headers and all sixteen dataset values.
3. Use rules only where they improve lookup.
4. Signal the W4 column without filling every cell.

## Expression levels

Only Level A is allowed in Milestone 2. Full table grammar remains part of deferred Analytical Mode.

## Typography and spacing

Use neutral sans labels, tabular numeric alignment, minimum label size at `1280×720`, and sparse neutral rules.

## Signal constraints

Dusty data blue identifies W4 through one rule or label and occupies no more than 5%.

## Canonical content

All W1–W4 values for runs, success rate, median review minutes, and escaped defects from the fixed dataset, plus `DEMO DATA`.

## Hard exclusions

No zebra decoration, rounded cell cards, omitted units, reordered weeks, heatmap color, invented totals, or truncated values.

## Prompt DSL contract

`prompts/18-table.yaml` enumerates the full exact table and forbids any additional summary.

## Acceptance criteria

Every header and value exact; lookup works at `1280×720`; W4 emphasis does not distort or conceal data.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates and verified cell by cell.
