# 13 Loop

## Problem

Show a repeating process whose output changes the next cycle.

## Allowed scenarios

Feedback cycle, learning loop, or recurring operation with three–five stages.

## Semantic components

One closed `Loop` connects ordered `Node`s; one `Signal` marks the compounding or current stage.

## Assembly order

1. Place stages in exact cyclic order.
2. Connect them with thin continuous relations.
3. Close the cycle once.
4. Select one compounding Node.

## Expression levels

A, B, and C are allowed. B is canonical. A removes center copy; C is reserved for a culmination with very short text.

## Typography and spacing

Use direct stage labels, bare circular Nodes, open center space, and readable gaps at `1280×720`.

## Signal constraints

Coral marks `COMPOUND` only and occupies no more than 8%.

## Canonical content

Exact Pilot 01 Card 05 headline, supporting sentence, and five ordered stages.

## Hard exclusions

No interface pills, duplicated markers, multiple active nodes, decorative orbit lines, or broken cycle.

## Prompt DSL contract

`prompts/13-loop.yaml` formalizes the Pilot 01 five-stage Loop and cites the source prompt.

## Acceptance criteria

Cycle and order are obvious; exact copy; one selected Node; Pilot score threshold met.

## Canonical evidence

Pilot 01 Card 05 Synthesis, its Prompt DSL, three-candidate review, accepted score, and pinned SHA-256.
