# 07 Before / After

## Problem

Make a meaningful state transition legible without treating “after” as a cosmetic restyle.

## Allowed scenarios

Transformation, migration, process improvement, or recovery with one changed property.

## Semantic components

Two `Field`s hold the states, one `Divider` preserves the comparison, and one `Vector` plus `Signal` identifies the change.

## Assembly order

1. Define the before Field and its failure state.
2. Define the after Field and retained property.
3. Connect them with one directional Vector.
4. Signal only the changed property.

## Expression levels

Levels A and B are allowed. A is canonical. C is excluded because the paired states require equal readability.

## Typography and spacing

Use matching title/body roles across both states, 96 px margins, and a major gap around the Vector.

## Signal constraints

Mineral green marks retained context after the transition and occupies no more than 8%.

## Canonical content

Exact headline plus `AD HOC / РІШЕННЯ ГУБЛЯТЬСЯ` and `SYSTEM / КОНТЕКСТ ЗАЛИШАЄТЬСЯ`.

## Hard exclusions

No makeover photography, generic check/cross icons, unequal copy hierarchy, decorative split screen, or invented benefit.

## Prompt DSL contract

`prompts/07-before-after.yaml` defines equal open Fields and one left-to-right transformation.

## Acceptance criteria

Both states read equally; the semantic change is obvious; exact copy; no implied quantitative improvement.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
