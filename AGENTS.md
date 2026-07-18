# AGENTS.md — CSDL operating instructions

These instructions apply to the entire repository. The canonical GitHub target is `vladagurets/csdl`.

## Mission

Develop Constructive Signal Design Language as a versioned, machine-readable visual language for educational presentation slides about AI, software engineering, and economics. Optimize for clarity, landscape presentation readability, memorability, and reproducibility with GPT Image 2.

## Mandatory reading order

Before changing anything, read:

1. `STATUS.md`
2. `DECISIONS.md`
3. `specs/2026-07-17-csdl-v0.1-design.md`
4. `pilots/01-agentic-discipline/manifest.yaml`
5. the relevant task in `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`
6. `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`
7. `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md`
8. `docs/handoff/CODEX_IMAGE_GENERATION.md` for raster tasks

Do not rely on memory or infer a new direction when these files are explicit.

## Locked design constraints

Do not change these without explicit user approval and a corresponding update to `DECISIONS.md`:

- direction: Constructive Signal;
- default expression: Quiet Modular;
- display direction: Modular Technical, with rare condensed editorial emphasis only;
- palette character: warm, muted, mineral, restrained;
- canonical canvas: 1920×1080, ratio 16:9, landscape;
- portrait masters and mobile-preview deliverables are out of scope;
- standard series rhythm: A, A, B, A, B, A, C;
- one main idea, one visual mechanism, one dominant signal per screen;
- 50–75% negative space depending on expression level;
- no political, Soviet, revolutionary-poster, or imitation-1920s styling;
- Markdown is the canonical specification.

## Current objective

Milestone 5 — Analytical Mode v0.1 is complete. Preserve the independent additive contract under `analytics/analytical-mode-v0.1/`, ten typed fixed datasets, ten deterministic proofs, seventeen negative fixtures, strict/incomplete validation, deterministic builders/indexes, Prompt DSL v0.5 compatibility, exactly fifteen public components, exactly 23 recipes, and all accepted Milestone 1–4 rasters. Milestone 6 Night Mode must not begin without a new explicit objective. Cookbook, public release, licensing, tags, and GitHub Releases remain out of scope.

## Work protocol

1. Use one branch and one pull request per independently reviewable task.
2. Preferred branch names: `codex/pilot-01-card-01`, `codex/pilot-01-card-02`, and so on.
3. Preserve canonical copy from `manifest.yaml` exactly. A copy change requires user approval before editing the manifest.
4. Generate three candidates for each card, then select one through the evaluation rubric. Do not silently promote the first candidate.
5. Keep drafts under `pilots/01-agentic-discipline/drafts/`; they are intentionally ignored by Git.
6. Commit approved card files only under `pilots/01-agentic-discipline/canonical/`.
7. Update `STATUS.md` and `CHANGELOG.md` whenever a task is completed or a decision changes.
8. Record all candidate filenames, rejection reasons, the selected filename, exact-copy review, dimensions/color-mode review, and selection rationale in `pilots/01-agentic-discipline/evaluation/review.md`. Draft-local `approved.txt` is only a convenience marker and is not persistent project evidence.
9. Record the accepted card score in `pilots/01-agentic-discipline/evaluation/scores.csv`.
10. Do not add decorative geometry that has no semantic role.
11. Do not add generated labels, interface chrome, logos, footers, or text that is absent from the prompt and manifest.
12. For Milestone 2 generated families, keep candidates under `patterns/visual-dna-sprint-01/drafts/`, promote only selected assets under `canonical/`, and persist evidence in the catalog evaluation files.

## Image-generation routes

### Default: built-in Codex image generation

For interactive Codex raster work, explicitly invoke `$imagegen` and attach the approved reference image with `-i` or `--image` when supported by the current surface.

- Built-in generation uses `gpt-image-2`.
- It counts toward the user's general Codex usage limits.
- It does **not** require `OPENAI_API_KEY`.
- Do not gate built-in generation on checking the `OPENAI_API_KEY` environment variable or the Python `openai` package.
- For Tasks 5–11, this is the preferred generation route.

### Optional: programmatic API generation

Use an API-backed helper only when the user explicitly requests a reproducible programmatic or larger-batch workflow.

- This route requires `OPENAI_API_KEY`, API billing/access, the appropriate SDK, and network access.
- ChatGPT/Codex subscription access and API billing are separate.
- Never print, log, or commit secrets.
- Do not create an API helper as incidental scope inside a single-card task.

### Fallbacks and blockers

If built-in `$imagegen` is unavailable on the current Codex surface or disabled by workspace settings:

- produce the complete YAML prompt package;
- report the exact capability blocker as `built-in Codex image generation unavailable`;
- state the expected output paths and dimensions;
- stop at the human generation/review gate;
- do not misreport a missing API key as the blocker for the built-in route;
- do not substitute placeholder raster assets and claim completion.

An external ChatGPT Images session is an acceptable human-operated fallback when it uses the same Prompt DSL, style reference, output contract, and review gate.

For generated images:

- exact output is PNG;
- canonical slide size is 1920×1080;
- text must be publication-ready and match the manifest exactly;
- no gradients, shadows, 3D, glossy surfaces, decorative coordinate systems, or random dot fields;
- the approved card-specific reference is `pilots/01-agentic-discipline/references/style-anchor-light.png`;
- preserve its smooth Ukrainian-capable Inter display/body relationship; do not introduce pixel, bitmap, dot-matrix, segmented, or retro-computer lettering;
- the reference's GPT generation, candidate selection, hashes, and review evidence are recorded in `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md`;
- the broader calibration references are under `references/canonical/`, including `quiet-modular-a-b-c-calibration.png`.

## Validation commands

Run before every commit:

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
```

After all seven canonical 16:9 slides exist, also run:

```bash
python tools/validate_assets.py pilots/01-agentic-discipline
python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv
```

For Milestone 2 infrastructure and analytical data, also run:

```bash
python tools/validate_pattern_catalog.py patterns/visual-dna-sprint-01/manifest.yaml
python tools/validate_pattern_data.py patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml
```

At Milestone 2 completion, also run:

```bash
python tools/validate_pattern_assets.py patterns/visual-dna-sprint-01
python tools/validate_pattern_scores.py patterns/visual-dna-sprint-01/evaluation/scores.csv
python tools/build_pattern_catalog.py patterns/visual-dna-sprint-01
python tools/validate_pattern_index.py patterns/visual-dna-sprint-01
```

For Component Library v0.1, also run:

```bash
python tools/validate_component_library.py components/component-library-v0.1/manifest.yaml
python tools/validate_component_proofs.py components/component-library-v0.1
python tools/build_component_library.py components/component-library-v0.1
python tools/validate_component_index.py components/component-library-v0.1
```

For Recipe Library and Prompt DSL v0.5, also run:

```bash
python tools/validate_recipe_library.py recipes/recipe-library-v0.5/manifest.yaml
python tools/build_recipe_proofs.py recipes/recipe-library-v0.5
python tools/validate_prompt_dsl.py recipes/recipe-library-v0.5
python tools/build_recipe_library.py recipes/recipe-library-v0.5
python tools/validate_recipe_index.py recipes/recipe-library-v0.5
```

For Analytical Mode v0.1, also run:

```bash
python tools/build_analytical_mode.py analytics/analytical-mode-v0.1
python tools/validate_analytical_mode.py analytics/analytical-mode-v0.1
```

Pilot 01 and Milestones 2–5 are complete, so all strict validators for those milestones are expected to pass. Use tested `require_complete=False` modes only when reviewing historical intermediate branches, and record only evidence actually reviewed.

## Definition of done for one card

A card task is complete only when:

- three candidates were generated and reviewed;
- one candidate is selected and copied to the canonical path;
- candidate selection and rejection evidence is persisted in `evaluation/review.md`;
- dimensions and color mode validate;
- the card matches canonical copy exactly;
- clarity, presentation readability, and text fidelity score 5/5;
- every other rubric criterion is at least 4/5;
- the average score is at least 4.4;
- the accepted score is recorded in `evaluation/scores.csv`;
- review notes explain why the selected candidate is canonical;
- tests, manifest validation, and style-anchor validation pass;
- `STATUS.md` and `CHANGELOG.md` are updated.

## Source and copyright policy

Do not commit the uploaded El Lissitzky PDF or font binaries. Preserve the analytical notes in `research/` and use them only as methodological reference. Approved generated reference images may be committed. Do not expose API keys or private user data.

## Communication

When blocked, report the exact blocker and the last passing command. Do not guess. When a visual choice is ambiguous, present a small number of options and request user approval before changing locked direction.
