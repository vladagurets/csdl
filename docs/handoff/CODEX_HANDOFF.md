# Codex Handoff — 2026-07-17

## Current state

CSDL combines structured Markdown, YAML manifests, Python validators, visual references, and staged review gates. Codex is well suited to maintaining these artifacts, executing deterministic checks, generating raster candidates through its built-in image capability, creating small branches/PRs, and preserving a traceable decision history.

The repository is imported at `vladagurets/csdl`. Codex repository reading has been verified, and GitHub write access has been verified. Task 5 is the next unfinished implementation item.

## Repository setup

- Repository: `vladagurets/csdl`
- Current visibility: public working repository; no public license selected yet
- Default branch: `main`
- Protect `main`; merge through pull requests
- Require the validation workflow before merge
- Prefer one reviewable task per branch and PR

The initial-import procedure is retained only as historical recovery documentation in `docs/handoff/GITHUB_IMPORT.md`.

## Image generation

The default card-production route is built-in Codex image generation:

- explicitly invoke `$imagegen`;
- use the approved reference image;
- built-in generation uses `gpt-image-2` and consumes Codex usage limits;
- no `OPENAI_API_KEY` is required;
- do not create an API helper inside Task 5.

An API-backed helper is optional future work for programmatic or larger batches and requires separate API access and billing. See `docs/handoff/CODEX_IMAGE_GENERATION.md`.

## Verified Ask-mode task

The repository-context read was completed successfully with:

```text
Read AGENTS.md, STATUS.md, DECISIONS.md, specs/2026-07-17-csdl-v0.1-design.md, pilots/01-agentic-discipline/manifest.yaml, and Task 5 in docs/superpowers/plans/2026-07-17-csdl-pilot-01.md. Summarize the locked constraints, the exact output contract for Card 01, and any environment requirement for GPT Image 2. Do not edit files.
```

## Next Code-mode task

Use this corrected prompt:

```text
Implement only Task 5 of the Pilot 01 plan on a new branch named codex/pilot-01-card-01.

Read AGENTS.md, STATUS.md, DECISIONS.md, the Foundation v0.1 spec, pilots/01-agentic-discipline/manifest.yaml, Task 5 in the implementation plan, and docs/handoff/CODEX_IMAGE_GENERATION.md.

Preserve manifest copy exactly. Create prompts/01-hook.yaml first and run the baseline tests and manifest validation.

Then explicitly invoke $imagegen three times, using pilots/01-agentic-discipline/references/style-anchor-light.png as the primary visual reference. Built-in Codex image generation uses gpt-image-2 and does not require OPENAI_API_KEY. Do not inspect API credentials, install an API SDK, or create an API helper in this task.

Save three candidates under drafts/light/4x5/01-hook/ using the required filenames. Present all three for human selection and do not promote a candidate until approval is explicit.

After approval, persist candidate and selection evidence in evaluation/review.md, record the accepted Card 01 score in scores.csv, copy the selected candidate to canonical/light/4x5/01-hook.png, update STATUS.md and CHANGELOG.md, rerun validation, commit, push, and open a pull request.

If the $imagegen capability itself is unavailable on this Codex surface or disabled by workspace settings, stop at the visual review gate. Report the exact capability blocker and the last passing validation command. Do not treat an unset OPENAI_API_KEY as a blocker for the built-in route, and do not create a placeholder PNG.
```

## PR sequence

1. Card 01 Hook
2. Card 02 Problem
3. Card 03 Model
4. Card 04 Comparison
5. Card 05 Loop
6. Card 06 Checklist
7. Card 07 Share card
8. Preview and contact-sheet tooling
9. Evaluation/revision pass
10. 16:9 adaptations
11. Pilot 01 release

Do not combine several visual cards in one initial PR. The first two cards calibrate the production workflow.

## Human review checkpoints

A human approves:

- final visual candidate;
- exact Ukrainian text rendering;
- whether geometry carries the intended meaning;
- whether the card remains Quiet Modular rather than decorative;
- any change to locked decisions or canonical copy.

Codex verifies:

- file paths and dimensions;
- manifests and Prompt DSL;
- tests and rubric thresholds;
- branch/commit/PR hygiene;
- release packaging and documentation consistency.
