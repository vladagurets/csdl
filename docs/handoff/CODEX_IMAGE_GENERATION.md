# Codex Image Generation Workflow

This document defines the approved raster-production route for CSDL tasks.

## Default route: built-in `$imagegen`

Use built-in Codex image generation for normal Pilot 01 card work.

- Invoke the capability explicitly with `$imagegen`.
- Built-in generation uses `gpt-image-2`.
- It counts toward the user's general Codex usage limits.
- It does not require `OPENAI_API_KEY`.
- Attach the approved style reference with `-i` or `--image` when the active Codex surface supports that syntax.
- Do not inspect API environment variables or install the OpenAI SDK before attempting the built-in route.

Official reference: [Image generation in Codex](https://learn.chatgpt.com/docs/image-generation).

## Approved shared reference

Use this file as the primary visual reference for Pilot 01 Tasks 5–11:

```text
pilots/01-agentic-discipline/references/style-anchor-light.png
```

Its GPT generation route, exact hashes, candidate selection, metadata, and manual review are recorded in:

```text
pilots/01-agentic-discipline/references/style-anchor-light.provenance.md
```

The active reference is the exact user-selected GPT Image 2 composition, mechanically normalized to `1080×1350`. Its typography follows the Ukrainian-capable Inter Display / Inter relationship already approved on Card 01. The earlier custom 5×7 pixel raster is superseded and exists only in Git history. Do not use pixel, bitmap, dot-matrix, segmented, or retro-computer lettering for later cards.

Validate the file before attempting generation. The dedicated validator checks format, dimensions, color mode, and complete PNG data; it rejects both truncated files with readable headers and files with corrupt PNG chunk checksums. Do not replace the reference silently or use a superseded exploratory image as the card-specific reference.

## Optional routes

### External ChatGPT Images

A human may generate or edit candidates in ChatGPT Images when Codex's built-in image capability is unavailable. The same YAML prompt, reference image, filenames, dimensions, and review criteria still apply.

### Programmatic API

Use the Image Generation API only for an explicitly scoped reproducible or larger-batch workflow.

This route requires:

- `OPENAI_API_KEY`;
- separately configured API billing/access;
- network access;
- an approved helper implementation and tests.

A ChatGPT or Codex subscription does not automatically fund API calls. Do not add an API helper incidentally while implementing one card.

## Task 5 execution contract

### 1. Prepare the prompt package

Create:

```text
pilots/01-agentic-discipline/prompts/01-hook.yaml
```

The visible copy must match `manifest.yaml` character-for-character.

### 2. Run deterministic baseline checks

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
```

Expected:

```text
17 passed
manifest valid
style anchor valid
```

If the style-anchor command fails, stop before image generation and repair or restore the shared reference. Do not substitute another file without explicit approval and updated provenance.

### 3. Generate three independent candidates

Use the same prompt and the same primary reference each time:

```text
pilots/01-agentic-discipline/references/style-anchor-light.png
```

Explicitly invoke `$imagegen` for each candidate and request 4:5 portrait output at 1080×1350.

Save drafts as:

```text
pilots/01-agentic-discipline/drafts/light/4x5/01-hook/01-hook-v1.png
pilots/01-agentic-discipline/drafts/light/4x5/01-hook/01-hook-v2.png
pilots/01-agentic-discipline/drafts/light/4x5/01-hook/01-hook-v3.png
```

Drafts are ignored by Git.

### 4. Stop for human visual selection

Do not silently promote the first candidate. Present all three candidates for review.

Reject a candidate when it has any of the following:

- incorrect Ukrainian text;
- more than one coral object;
- less than approximately 60% perceived negative space;
- extra labels, grid marks, logos, footer, frame, or UI chrome;
- a Level C poster character instead of Level A Quiet;
- unreadable body text at phone size.

### 5. Persist selection evidence

Record in:

```text
pilots/01-agentic-discipline/evaluation/review.md
```

Required evidence:

- all three candidate filenames;
- rejection reason for every rejected candidate;
- selected candidate filename;
- exact-copy review result;
- dimensions and color-mode result;
- explanation of why the selected image is canonical.

Update Card 01 in:

```text
pilots/01-agentic-discipline/evaluation/scores.csv
```

Thresholds:

- clarity = 5;
- mobile_readability = 5;
- text_fidelity = 5;
- all other criteria >= 4;
- average >= 4.4.

`validate_scores.py` remains a series-level gate and is expected to fail until all seven rows are complete.

### 6. Promote the approved candidate

Copy only the human-approved draft to:

```text
pilots/01-agentic-discipline/canonical/light/4x5/01-hook.png
```

Then update `STATUS.md` and `CHANGELOG.md`, run all three baseline validations again, and open a pull request.

## Corrected Codex task prompt

```text
Implement only Task 5 of the Pilot 01 plan on a new branch named codex/pilot-01-card-01.

Read AGENTS.md, STATUS.md, DECISIONS.md, the Foundation v0.1 spec, pilots/01-agentic-discipline/manifest.yaml, Task 5 in the implementation plan, pilots/01-agentic-discipline/references/style-anchor-light.provenance.md, and docs/handoff/CODEX_IMAGE_GENERATION.md.

Preserve manifest copy exactly. Create prompts/01-hook.yaml first and run the tests, manifest validation, and dedicated style-anchor validation. Expected baseline: 17 tests pass, the manifest is valid, and the style anchor is valid.

Then explicitly invoke $imagegen three times, using pilots/01-agentic-discipline/references/style-anchor-light.png as the primary visual reference. Built-in Codex image generation uses gpt-image-2 and does not require OPENAI_API_KEY. Do not inspect API credentials, install an API SDK, or create an API helper in this task.

Save three candidates under drafts/light/4x5/01-hook/ using the required filenames. Present all three for human selection and do not promote a candidate until approval is explicit.

After approval, persist candidate and selection evidence in evaluation/review.md, record the accepted Card 01 score in scores.csv, copy the selected candidate to canonical/light/4x5/01-hook.png, update STATUS.md and CHANGELOG.md, rerun validation, commit, push, and open a pull request.

If the $imagegen capability itself is unavailable on this Codex surface or disabled by workspace settings, stop at the visual review gate. Report the exact capability blocker and the last passing validation command. Do not treat an unset OPENAI_API_KEY as a blocker for the built-in route, and do not create a placeholder PNG.
```
