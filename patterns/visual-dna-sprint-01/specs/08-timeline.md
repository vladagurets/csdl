# 08 Timeline

## Problem

Show ordered change over time with one unmistakable reading direction.

## Allowed scenarios

History, delivery sequence, staged rollout, or dated evolution with three–seven moments.

## Semantic components

One `Axis` carries ordered `Node`s; a `Signal` marks the consequential transition.

## Assembly order

1. Draw one horizontal Axis.
2. Place Nodes in exact chronological order.
3. Label directly.
4. Signal one transition without changing order.

## Expression levels

Levels A and B are allowed. A is canonical. C is excluded because chronology needs stable repeated structure.

## Typography and spacing

Use label-size stage names, even rhythm, 96 px margins, and enough gap to prevent label collisions at `1280×720`.

## Signal constraints

Coral marks `VERIFY` or its incoming transition and occupies no more than 6%.

## Canonical content

`ВІД BRIEF ДО SHIP` with `BRIEF`, `PLAN`, `BUILD`, `VERIFY`, `SHIP` in that order.

## Hard exclusions

No invented dates, reversed order, alternating decorative cards, roadmap UI, icons, or multiple active stages.

## Prompt DSL contract

`prompts/08-timeline.yaml` defines one left-to-right Axis with five bare Nodes.

## Acceptance criteria

Order is immediate; all five stages are exact; one active transition; no sequence ambiguity.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
