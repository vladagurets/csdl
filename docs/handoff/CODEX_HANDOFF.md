# Codex Handoff — 2026-07-17

## Why this repository is a good Codex project

CSDL combines structured Markdown, YAML manifests, Python validators, visual references, and staged review gates. Codex is well suited to maintaining these artifacts, executing deterministic checks, creating small branches/PRs, and preserving a traceable decision history.

Raster generation is intentionally separated from design governance. Codex should orchestrate prompts, scripts, validation, packaging, and review evidence. GPT Image 2 should generate the raster candidates when configured.

## Recommended repository setup

- Repository: `vladagurets/csdl`
- Current visibility: public working repository; no public license selected yet
- Default branch: `main`
- Working branch for the current milestone: `pilot-01`
- Protect `main` after the initial import; merge through pull requests
- Require the validation workflow before merge
- Follow `docs/handoff/GITHUB_IMPORT.md` for the initial push
- Connect the repository to a Codex environment after import

## First Codex task

Use this exact task in Ask mode first:

```text
Read AGENTS.md, STATUS.md, DECISIONS.md, specs/2026-07-17-csdl-v0.1-design.md, pilots/01-agentic-discipline/manifest.yaml, and Task 5 in docs/superpowers/plans/2026-07-17-csdl-pilot-01.md. Summarize the locked constraints, the exact output contract for Card 01, and any environment requirement for GPT Image 2. Do not edit files.
```

After reviewing the answer, use this Code-mode task:

```text
Implement only Task 5 of the Pilot 01 plan on a new branch named codex/pilot-01-card-01. Preserve manifest copy exactly. Create the final Card 01 YAML prompt package and any minimal generation helper required by the task. Run pytest and manifest validation. If GPT Image 2 generation is unavailable, stop at the visual review gate and report the exact command and required environment variables rather than claiming the PNG exists. Update STATUS.md only for work actually completed.
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
