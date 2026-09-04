# Recipe 026: Dependency Map

## Problem

Show what depends on what and which prerequisite blocks the declared target.

## Distinction

`Architecture` explains boundaries and permitted interactions. `Hierarchy`
explains ownership. `Dependency Map` explains prerequisite semantics only.

## Ingredients

Three to seven `Node` instances, explicit `Bridge` connections, one `Signal`,
and an optional observed critical `Trace`.

## Acceptance

Every dependency has a declared direction. Distance and angle carry no meaning.
The critical dependency is not presented as a chronological step.
