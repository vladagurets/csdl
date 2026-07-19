---
name: csdl-create
description: Create a complete Constructive Signal Design Language infographic slide set in Codex from slide context. Use when a user asks to build, generate, translate, extend, or regenerate a CSDL infoslide series or a pilot under `pilots/{ID-topic-name}`. Analyze the material, resolve slide count, rhythm, copy, and evidence through a consolidated clarification round, generate three candidates per slide with Codex image generation and the canonical CSDL reference hierarchy, select and validate the final 16:9 set, and persist prompts, rasters, previews, contact sheet, sources, scores, and review evidence.
---

# CSDL Create

Turn slide-by-slide context into a complete, reviewable CSDL pilot at `pilots/{ID-topic-name}`. Run the workflow through Codex and its built-in image generation. Keep product interpretation and exact copy under user control; perform the mechanical generation, evaluation, promotion, and validation autonomously after approval.

## Load the contracts

1. Confirm the repository root and read the applicable `AGENTS.md` completely.
2. Read the repository files in the mandatory order stated by `AGENTS.md`.
3. Read [references/intake.md](references/intake.md) before questioning the user.
4. Read [references/pilot-contract.md](references/pilot-contract.md) before creating files or generating images.
5. Inspect `git status`, existing `pilots/` IDs, the Recipe Library manifest, the Component Library manifest, and the closest accepted pilot.

Do not begin Milestone 8, alter locked design decisions, change accepted raster evidence, or invent public components, Recipes, facts, statistics, sources, or capabilities.

## Run the workflow

### 1. Analyze the request

Extract the supplied context into a proposed narrative. Separate:

- user-approved exact copy;
- editable draft copy;
- factual claims requiring sources;
- canonical CSDL identifiers that must remain English;
- requested slide roles or mechanisms;
- inferred choices that still need approval.

Use the slide count requested by the user. When no count is given, propose the smallest count that produces a coherent narrative; use seven only as the default for a full standard CSDL arc. Treat `A, A, B, A, B, A, C` as the standard seven-slide rhythm, not as a universal length constraint. For any other count, propose a content-led A/B/C rhythm of the same length and obtain user approval. Update `DECISIONS.md` only when changing the standard itself, not merely when creating a shorter or longer series.

### 2. Ask one consolidated clarification round

Always ask clarification questions before generation. Ask only consequential questions, but do not skip the round even when the input looks complete. Present a compact proposed slide table first, then ask the user to confirm or correct it.

Resolve at minimum:

- pilot ID and kebab-case topic slug;
- audience, use context, and language;
- exact versus editable wording for every slide;
- claim, evidence/source, and intended takeaway for every slide;
- missing narrative transitions, final promise, and call to action;
- explicit approval of the normalized brief, slide count, and proposed A/B/C rhythm.

If the user supplied a complete brief, ask for confirmation of the synthesized brief instead of manufacturing additional questions. Do not generate raster candidates until the user approves the brief and exact-copy contract.

### 3. Create the pilot contract

Create `pilots/{ID-topic-name}` only after brief approval. Use a zero-padded two-digit pilot ID unless the repository already establishes another convention. Do not overwrite an existing pilot.

Persist:

- `manifest.yaml` as the source of truth for sequence, exact visible copy, Recipe, expression level, visual mechanism, components, signal role, and asset filename;
- `sources.md` mapping every factual claim, dataset, quote, and user-supplied statement to its provenance;
- one Prompt DSL YAML per slide plus `prompts/00-style-anchor.yaml` describing the shared reference package;
- the output tree and evidence files defined in `references/pilot-contract.md`.

For each card, include an `exact_copy` list containing every string permitted to appear in its raster. No other visible text is allowed.

### 4. Select Recipes and components

Start from the explanatory problem, not a preferred layout. Read the selected Recipe records/specifications and the relevant component contracts before writing prompts.

Use only the 23 public Recipes and exactly fifteen public components already declared by the repository. Give every geometric element a semantic role. Keep one main idea, one visual mechanism, and one dominant Signal per slide.

### 5. Build prompts and generate candidates

Use the repository's built-in image-generation route and follow the `imagegen` skill. Attach the complete reference hierarchy defined in `references/pilot-contract.md`.

For every slide:

1. Write a Prompt DSL package that repeats the exact-copy contract and hard exclusions.
2. Generate exactly three candidates.
3. Store source and normalized candidates under `drafts/light/16x9/{card-id}-{slug}/`.
4. Normalize without cropping, redrawing, recoloring, or editing text to `1920×1080` RGB PNG.
5. Stop and report `built-in Codex image generation unavailable` if the built-in route is unavailable. Do not substitute placeholders or claim completion.

Never silently promote the first candidate. A complete draft set contains exactly `3 × card_count` normalized candidates.

### 6. Evaluate and promote

Review all three candidates together at full resolution and at `1280×720`. Reject candidates with copy mutations, extra text, clipping, weak hierarchy, non-semantic decoration, incorrect expression level, inaccessible contrast, or family drift.

Persist in `evaluation/review.md`:

- all candidate filenames;
- rejection reasons;
- selected filename and selection rationale;
- exact-copy, dimensions, color-mode, clipping, contrast, and reading-order checks;
- visual mechanism and removable-element check;
- canonical SHA-256 and remaining risk.

Record rubric scores in `evaluation/scores.csv`. Require clarity, presentation readability, and text fidelity at `5/5`; every other criterion at least `4/5`; average at least `4.4`.

Copy only selected assets to `canonical/light/16x9/`. Build one `1280×720` preview per slide and one `3840×2160` contact sheet with a grid adapted to the approved slide count. Review the sequence as a family, not only as independent slides.

### 7. Validate

Run:

```bash
.venv/bin/python ai/skills/csdl-create/scripts/validate_pilot.py pilots/{ID-topic-name} --require-drafts
.venv/bin/python -m pytest -q
.venv/bin/python tools/validate_accessibility_mode.py accessibility/night-mode-v0.1
.venv/bin/python tools/validate_design_book.py cookbook/design-book-v1.0
```

Also run any pilot-specific or boundary validator affected by the work. Inspect the full contact sheet and every selected slide at original resolution. Update `STATUS.md` and `CHANGELOG.md` when the pilot is complete.

Do not stage, commit, push, publish, or release unless the user explicitly requests it.

### 8. Report completion

Lead with the final pilot directory and contact sheet. List canonical slide files, prompts, manifest, sources, and review evidence. Report exact validation results, `Primary signal status`, `Secondary signal status`, documentation status, unresolved risks, and a suggested commit message.

If only prompts were completed because generation was unavailable, state that the primary signal is not met and name the exact blocker.

## Stop conditions

Pause and ask the user when:

- exact copy or a consequential claim remains ambiguous;
- a factual statement lacks acceptable provenance;
- the requested count, rhythm, direction, palette, canvas, or expression conflicts with locked decisions;
- the user must choose between materially different narratives;
- generation would replace accepted raster evidence;
- a destructive, release, licensing, permission, or external-publication action would be required.
