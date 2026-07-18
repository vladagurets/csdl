# 10 Hierarchy

## Problem

Show levels of decomposition, ownership, or containment without implying a time sequence.

## Allowed scenarios

Goal decomposition, taxonomy, authority, or nested scope with three–five levels.

## Semantic components

The root `Anchor` owns child `Node`s; nested open `Frame`s or `Bridge` relations express depth.

## Assembly order

1. Place the root Anchor.
2. Add each deeper Node with consistent indentation or branching.
3. Preserve one top-to-bottom depth cue.
4. Signal the terminal verification Node.

## Expression levels

Levels A and B are allowed. A is canonical. C is excluded because hierarchy requires repeated depth cues.

## Typography and spacing

Decrease type scale or indentation by depth, keep labels horizontal, and use `space.4–space.6` between levels.

## Signal constraints

Coral selects `CHECK` only and occupies no more than 6%.

## Canonical content

`ВІД ЦІЛІ ДО ПЕРЕВІРКИ` with `OBJECTIVE`, `MILESTONE`, `TASK`, `CHECK` in descending depth.

## Hard exclusions

No arrow chain that reads as workflow, org-chart avatars, duplicate parents, decorative boxes, or extra levels.

## Prompt DSL contract

`prompts/10-hierarchy.yaml` defines four nested/decomposed levels and one selected leaf.

## Acceptance criteria

Depth is immediate; sequence is not implied; exact labels; every connector expresses ownership.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
