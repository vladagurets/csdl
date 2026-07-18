# 04 Big Number

## Problem

Make one exact quantity the explanatory object while retaining its label and context.

## Allowed scenarios

Count, percentage, ratio, milestone, or bounded system fact.

## Semantic components

The value is a `Pulse`; its label is the `Anchor`; one `Signal` ties value to meaning.

## Assembly order

1. Place the Pulse at dominant scale.
2. Attach a concise label without separating units.
3. Add one supporting line and one Signal marker.

## Expression levels

A, B, and C are allowed. A is canonical. B may add one explanatory relation; C requires a single short value with minimal copy.

## Typography and spacing

Use the strongest numeric display role, a neutral label, aligned baselines, and at least 65% negative space at Level A.

## Signal constraints

Coral marks the value or its baseline and occupies no more than 8%. It cannot encode a second quantity.

## Canonical content

`3`, `РІВНІ ВИРАЗНОСТІ`, and `QUIET · CONSTRUCTIVE · SIGNAL`, exactly.

## Hard exclusions

No unsupported statistic, gauge, donut, fake trend, superscript ambiguity, decorative digits, or extra metric.

## Prompt DSL contract

`prompts/04-big-number.yaml` treats the number as a Pulse and the three named levels as context.

## Acceptance criteria

The value reads first; the label stays attached; all three level names are exact; no implied empirical claim.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
