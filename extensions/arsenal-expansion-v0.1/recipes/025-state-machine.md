# Recipe 025: State Machine

## Problem

Explain a finite set of states and the conditions that permit transitions.

## Distinction

`Decision Tree` owns a branching rule and its consequences. `State Machine`
owns persistent states, guarded transitions, and optional return behavior.

## Ingredients

Three to six state `Node` instances, explicit `Vector` transitions, one or more
`Threshold` conditions, one `Signal`, and an optional observed `Trace`.

## Acceptance

Every transition has a source, target, and condition. Current, terminal, and
recurrent states are not inferred from color alone.
