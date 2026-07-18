# 15 Decision Tree

## Problem

Make a small branching rule and its consequences explicit.

## Allowed scenarios

Routing rule, escalation, or eligibility with one–three questions and explicit branch labels.

## Semantic components

One question `Node` branches through labeled `Bridge`s to terminal action Nodes; one branch is the `Signal`.

## Assembly order

1. Place the question Node.
2. Branch on explicit mutually exclusive answers.
3. Terminate each branch in one action.
4. Signal the risk/escalation path.

## Expression levels

Levels A and B are allowed. A is canonical. C is excluded because branch labels and outcomes must remain readable.

## Typography and spacing

Use a strong question, label-size answers, clear separation between outcomes, and no connector crossing.

## Signal constraints

Ochre marks the high-risk `ТАК → HUMAN REVIEW` branch only and occupies no more than 7%.

## Canonical content

Exact headline, `РИЗИК ВИСОКИЙ?`, `ТАК → HUMAN REVIEW`, and `НІ → AUTOMATE`.

## Hard exclusions

No unlabeled branch, third outcome, circular return, decision-diamond cliché, icons, or implied bypass of verification.

## Prompt DSL contract

`prompts/15-decision-tree.yaml` defines one binary decision and two terminal actions.

## Acceptance criteria

Question, answers, and outcomes are unambiguous; exact copy; high-risk route is the only signal.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
