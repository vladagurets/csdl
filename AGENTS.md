# AGENTS.md — CSDL operating instructions

These instructions apply to the entire repository. The canonical GitHub target is `vladagurets/csdl`.

## Mission

Develop Constructive Signal Design Language as a versioned, machine-readable visual language for educational infographics about AI, software engineering, and economics. Optimize for clarity, mobile readability, memorability, and reproducibility with GPT Image 2.

## Mandatory reading order

Before changing anything, read:

1. `STATUS.md`
2. `DECISIONS.md`
3. `specs/2026-07-17-csdl-v0.1-design.md`
4. `pilots/01-agentic-discipline/manifest.yaml`
5. the relevant task in `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`
6. `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`

Do not rely on memory or infer a new direction when these files are explicit.

## Locked design constraints

Do not change these without explicit user approval and a corresponding update to `DECISIONS.md`:

- direction: Constructive Signal;
- default expression: Quiet Modular;
- display direction: Modular Technical, with rare condensed editorial emphasis only;
- palette character: warm, muted, mineral, restrained;
- canonical canvas: 1080×1350, ratio 4:5;
- 16:9 is rebuilt, never cropped;
- standard series rhythm: A, A, B, A, B, A, C;
- one main idea, one visual mechanism, one dominant signal per screen;
- 50–75% negative space depending on expression level;
- no political, Soviet, revolutionary-poster, or imitation-1920s styling;
- Markdown is the canonical specification.

## Current objective

Resume Pilot 01 from Task 5 in the implementation plan. Tasks 1–4 are complete. Do not restart or rewrite them unless a failing test or explicit user request requires it.

## Work protocol

1. Use one branch and one pull request per independently reviewable task.
2. Preferred branch names: `codex/pilot-01-card-01`, `codex/pilot-01-card-02`, and so on.
3. Preserve canonical copy from `manifest.yaml` exactly. A copy change requires user approval before editing the manifest.
4. Generate three candidates for each card, then select one through the evaluation rubric. Do not silently promote the first candidate.
5. Keep drafts under `pilots/01-agentic-discipline/drafts/`; they are intentionally ignored by Git.
6. Commit approved card files only under `pilots/01-agentic-discipline/canonical/`.
7. Update `STATUS.md` and `CHANGELOG.md` whenever a task is completed or a decision changes.
8. Record visual-review evidence in `pilots/01-agentic-discipline/evaluation/review.md` and scores in `scores.csv`.
9. Do not add decorative geometry that has no semantic role.
10. Do not add generated labels, interface chrome, logos, footers, or text that is absent from the prompt and manifest.

## Image-generation boundary

Codex may create and run an image-generation script only when an OpenAI API key and network access are explicitly configured. Use model `gpt-image-2` and the repository Prompt DSL. Never print or commit secrets.

When image generation is unavailable:

- produce the complete YAML prompt package;
- state the exact expected output path and dimensions;
- stop at the human generation/review gate;
- do not substitute placeholder raster assets and claim completion.

For generated images:

- exact output is PNG;
- canonical card size is 1080×1350;
- text must be publication-ready and match the manifest exactly;
- no gradients, shadows, 3D, glossy surfaces, decorative coordinate systems, or random dot fields;
- the approved style anchor is `references/quiet-modular-density-calibration.png` plus the current canonical references.

## Validation commands

Run before every commit:

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
```

After all seven canonical 4:5 cards and three 16:9 adaptations exist, also run:

```bash
python tools/validate_assets.py pilots/01-agentic-discipline
python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv
```

Expected baseline before asset completion: nine tests pass and the manifest reports `manifest valid`.

## Definition of done for one card

A card task is complete only when:

- three candidates were generated or explicitly reviewed;
- one candidate is selected and copied to the canonical path;
- dimensions and color mode validate;
- the card matches canonical copy exactly;
- clarity, mobile readability, and text fidelity score 5/5;
- every other rubric criterion is at least 4/5;
- the average score is at least 4.4;
- review notes explain why the selected candidate is canonical;
- tests and manifest validation pass;
- `STATUS.md` is updated.

## Source and copyright policy

Do not commit the uploaded El Lissitzky PDF or font binaries. Preserve the analytical notes in `research/` and use them only as methodological reference. Approved generated reference images may be committed. Do not expose API keys or private user data.

## Communication

When blocked, report the exact blocker and the last passing command. Do not guess. When a visual choice is ambiguous, present a small number of options and request user approval before changing locked direction.
