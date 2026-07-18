# 20 Dashboard

## Problem

Summarize a small operational state while preserving one primary signal and clear lookup.

## Allowed scenarios

Weekly status, compact operating review, or bounded monitoring of three–five measures.

## Semantic components

One primary `Pulse`, a subordinate metric `Cluster`, one small trend `Axis`, and one `Signal` create the summary.

## Assembly order

1. Place the W4 success-rate Pulse.
2. Group the three supporting W4 measures without card chrome.
3. Add the exact four-week success trend.
4. Place the demo-data source label.

## Expression levels

Only Level A is allowed in Milestone 2. This is a Visual DNA prototype, not a full dashboard system.

## Typography and spacing

Use one dominant number, consistent direct labels, tabular figures, 96 px margins, and open alignment rather than widget cards.

## Signal constraints

Dusty data blue identifies success rate and its trend, occupying no more than 7%. Other metrics stay graphite.

## Canonical content

Exact W4 snapshot, exact success-rate trend `[72%, 78%, 84%, 90%]`, headline, and `DEMO DATA` from the fixed dataset.

## Hard exclusions

No navigation, filters, buttons, status icons, rounded widgets, invented deltas, gauges, extra chart, or hidden source.

## Prompt DSL contract

`prompts/20-dashboard.yaml` enumerates every visible metric and forbids interface chrome.

## Acceptance criteria

90% reads first; every value is exact; chart and metrics agree; no UI imitation; readable at `1280×720`.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates and verified across all views.
