# Codex Image Generation Workflow

This document defines the reusable raster-production route for CSDL card tasks. The active card and exact output contract always come from `STATUS.md`, the relevant implementation-plan task, and `manifest.yaml`.

## Default route: built-in `$imagegen`

Use built-in Codex image generation for normal Pilot 01 card work.

- Invoke the capability explicitly with `$imagegen`.
- Built-in generation uses `gpt-image-2` and counts toward the user's Codex usage limits.
- It does not require `OPENAI_API_KEY`.
- Attach the approved style reference when the active Codex surface supports image inputs.
- Do not inspect API environment variables or install the OpenAI SDK before attempting the built-in route.

Official reference: [Image generation in Codex](https://learn.chatgpt.com/docs/image-generation).

## Approved shared reference

Use this file as the primary visual reference for Pilot 01 card generation:

```text
pilots/01-agentic-discipline/references/style-anchor-light.png
```

Its generation route, exact hashes, candidate selection, metadata, and manual review are recorded in:

```text
pilots/01-agentic-discipline/references/style-anchor-light.provenance.md
```

The active reference is the exact user-selected GPT Image 2 composition, mechanically normalized to `1080×1350`. Its typography follows the Ukrainian-capable Inter Display / Inter relationship approved on Card 01. The earlier custom 5×7 pixel raster is superseded and exists only in Git history.

Validate the reference before generation. The dedicated validator checks format, dimensions, color mode, complete PNG data, and the approved SHA-256. Do not replace it silently or use a superseded exploration as a card-specific reference.

## Optional routes

### External ChatGPT Images

A human may generate or edit candidates in ChatGPT Images when Codex's built-in image capability is unavailable. The same YAML prompt, reference image, filenames, dimensions, and review criteria still apply.

### Programmatic API

Use the Image Generation API only for an explicitly scoped reproducible or larger-batch workflow. This route requires `OPENAI_API_KEY`, separately configured API billing/access, network access, and an approved helper implementation with tests. Do not add an API helper incidentally while implementing one card.

## Per-card execution contract

### 1. Resolve the active task

Read:

- `STATUS.md` for the current task;
- the matching task in `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`;
- the matching card entry in `pilots/01-agentic-discipline/manifest.yaml`;
- `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`;
- the approved style-anchor provenance sidecar.

Treat manifest copy as immutable unless the user explicitly approves a copy change.

### 2. Prepare the prompt package

Create the per-card YAML file at the path specified by the implementation plan. It must declare the recipe, expression level, semantic components, visual mechanism, palette roles, negative-space target, exact visible copy, and hard exclusions.

### 3. Run deterministic baseline checks

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
```

Expected baseline before card-asset completion:

```text
17 passed
manifest valid
style anchor valid
```

If the style-anchor command fails, stop before image generation. Do not substitute another reference without explicit approval and updated provenance.

### 4. Generate three independent candidates

Use the same card prompt and primary reference for all three candidates. Save them under the task-specific ignored draft directory and use the filenames defined by the implementation plan.

Do not silently promote the first candidate. Reject any candidate with incorrect text, unrelated UI chrome, extra labels, non-semantic decoration, an incorrect expression level, or unreadable phone-size copy.

### 5. Stop for human selection

Present all three candidates with enough visual evidence to compare full-resolution composition and phone-width readability. A candidate becomes canonical only after explicit human approval.

### 6. Persist review evidence

Record in `pilots/01-agentic-discipline/evaluation/review.md`:

- all candidate filenames;
- rejection reason for every rejected candidate;
- selected candidate filename;
- exact-copy review result;
- dimensions and color-mode result;
- full-resolution and phone-width review results;
- why the selected image is canonical.

Update the card row in `pilots/01-agentic-discipline/evaluation/scores.csv`. Required thresholds are:

- clarity = 5;
- mobile readability = 5;
- text fidelity = 5;
- every other criterion >= 4;
- average >= 4.4.

`validate_scores.py` remains a series-level gate and is expected to fail until all seven card rows are complete.

### 7. Promote and validate

Copy only the human-approved candidate to the canonical path specified by the implementation plan. Then update `STATUS.md` and `CHANGELOG.md` and rerun the baseline validations.

After all seven 4:5 cards and three 16:9 adaptations exist, also run:

```bash
python tools/validate_assets.py pilots/01-agentic-discipline
python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv
```

## Capability blocker

If built-in image generation is unavailable or disabled by workspace settings:

1. finish the complete YAML prompt package;
2. report `built-in Codex image generation unavailable` and the last passing validation;
3. state the expected draft filenames, canonical path, and dimensions;
4. stop at the human generation/review gate.

Do not treat an unset `OPENAI_API_KEY` as a blocker for the built-in route, silently switch generation routes, or create placeholder raster assets.
