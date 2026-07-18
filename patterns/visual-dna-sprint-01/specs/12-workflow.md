# 12 Workflow

## Problem

Show what action happens next in a bounded operational procedure.

## Allowed scenarios

Work procedure, handoff, review flow, or four–six ordered actions.

## Semantic components

Action `Node`s are connected by `Vector`s; one `Signal` marks the evidence-producing action.

## Assembly order

1. Place action Nodes in execution order.
2. Connect them with one directional path.
3. Select the action that produces evidence.

## Expression levels

Levels A and B are allowed. A is canonical. C is excluded because repeated actions must remain equally readable.

## Typography and spacing

Use uniform labels, bare Nodes rather than cards, 96 px margins, and `space.5–space.7` between actions.

## Signal constraints

Coral marks `VERIFY` only and occupies no more than 7%.

## Canonical content

`РОБОЧИЙ ПОТІК З ДОКАЗАМИ`: `UNDERSTAND → PLAN → EXECUTE → VERIFY`.

## Hard exclusions

No swimlane UI, status pills, icons, branching, cyclic return arrow, or extra completion state.

## Prompt DSL contract

`prompts/12-workflow.yaml` defines a simple left-to-right operational route.

## Acceptance criteria

Action order is immediate; `VERIFY` is the only signal; exact labels; no confusion with Pipeline or Loop.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
