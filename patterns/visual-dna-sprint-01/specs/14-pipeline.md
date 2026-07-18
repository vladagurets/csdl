# 14 Pipeline

## Problem

Show material or data transformed through fixed stages from input to output.

## Allowed scenarios

Data processing, content production, build system, or deterministic transformation.

## Semantic components

Stage `Node`s receive one continuous `Vector`; one `Signal` identifies the validation gate.

## Assembly order

1. Place input and output endpoints.
2. Order transform stages between them.
3. Connect one continuous flow.
4. Signal the validation gate before output.

## Expression levels

Levels A and B are allowed. B is canonical because transformation through five stages is the mechanism. C is excluded.

## Typography and spacing

Use uniform technical labels, a clear baseline, 96 px margins, and enough gap to distinguish stages from one wordmark.

## Signal constraints

Dusty data blue carries the flow; `VALIDATE` is the only active gate; total signal area stays below 10%.

## Canonical content

`КОНТЕКСТ СТАЄ РЕЗУЛЬТАТОМ`: `INPUT → PARSE → TRANSFORM → VALIDATE → OUTPUT`.

## Hard exclusions

No branching, feedback arrow, pipe illustration, database icons, code UI, extra stage, or hidden validation.

## Prompt DSL contract

`prompts/14-pipeline.yaml` defines fixed left-to-right transformation and a validation gate.

## Acceptance criteria

Input/output and stage order are exact; transformation differs clearly from Workflow; validation is semantic.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
