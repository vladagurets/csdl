# Project Status

**Project:** Constructive Signal Design Language  
**Version:** Foundation v0.1  
**Current milestone:** Pilot 01 — Agentic Discipline  
**Last updated:** 2026-07-17

## Summary

Foundation choices are approved and encoded in Markdown. Pilot 01 has canonical content, validation tooling, a scoring rubric, and a shared Quiet Modular style anchor. The previously missing Task 4 raster has been restored with provenance, byte-level identity evidence, and an independent validation gate. The repository has been imported to `vladagurets/csdl`, Codex can read it, and GitHub write access has been verified. Raster production of the seven-card series has not yet begun in the canonical asset tree.

## Completed

| Plan task | State | Evidence |
|---|---|---|
| Task 1 — repository and canonical content manifest | Complete | commit `c046d2c` |
| Task 2 — manifest validation with tests | Complete | commit `875994a` |
| Task 3 — raster-asset and rubric validation | Complete | commit `15efea1` |
| Task 4 — shared light-mode style anchor and generation boilerplate | Complete (repaired) | `style-anchor-light.png`, provenance sidecar, dedicated tests, and CI validator |

Additional completed foundation work:

- Constructive Signal direction selected;
- Modular Technical selected as display direction;
- Muted Signal palette selected;
- Quiet Modular adopted after density review;
- Level A/B/C system calibrated;
- 4:5 master format approved;
- Foundation spec and full implementation plan approved;
- initial and superseded references archived with status labels;
- full Git history imported to `https://github.com/vladagurets/csdl`;
- Codex Ask-mode repository reading verified;
- GitHub branch/write permissions verified.

## Active next task

### Task 5 — Generate and approve Card 01: Hook / Level A

Canonical content:

- headline: `СИЛЬНИЙ АГЕНТ ≠ СТІЙКИЙ РЕЗУЛЬТАТ`
- supporting copy: `Стабільність з’являється, коли робота має процес, перевірки й пам’ять.`
- mechanism: one large Anchor opposed by one small stable Signal block
- components: Anchor, Signal
- expression: Level A / Quiet
- output: `pilots/01-agentic-discipline/canonical/light/4x5/01-hook.png`

Follow the exact Task 5 steps in `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md` and the execution rules in `docs/handoff/CODEX_IMAGE_GENERATION.md`.

## Image-generation execution route

The default Task 5 route is built-in Codex image generation:

- invoke `$imagegen` explicitly;
- use `gpt-image-2` through the user's Codex plan/usage limits;
- attach `pilots/01-agentic-discipline/references/style-anchor-light.png` as the primary visual reference;
- generate three independent candidates;
- no `OPENAI_API_KEY` or Python API helper is required for this route.

An API-backed helper is optional future work for larger or programmatic batches. It is not part of Task 5 unless explicitly requested.

If `$imagegen` is unavailable on the active Codex surface or disabled by workspace settings, stop at the visual review gate and report that capability blocker. Do not treat an unset `OPENAI_API_KEY` as a blocker for built-in image generation.

## Remaining Pilot 01 work

- [ ] Task 5 — Card 01 Hook / Level A
- [ ] Task 6 — Card 02 Problem / Level A
- [ ] Task 7 — Card 03 Four-layer model / Level B
- [ ] Task 8 — Card 04 Complementary comparison / Level A
- [ ] Task 9 — Card 05 Synthesis loop / Level B
- [ ] Task 10 — Card 06 Operational takeaway / Level A
- [ ] Task 11 — Card 07 Share formula / Level C
- [ ] Task 12 — Mobile previews and contact sheet
- [ ] Task 13 — Score and revise all seven cards
- [ ] Task 14 — Rebuild Cards 01, 04, and 07 for 16:9
- [ ] Task 15 — Promote Pilot 01 to the canonical Visual DNA set

## Current validation state

```text
python -m pytest -q
................ [100%]

python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
manifest valid

python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
style anchor valid
```

Full asset and score validation is expected to fail until Tasks 5–14 create the required files and completed scores.

## Open constraints, not Task 5 blockers

1. Final font families remain deferred; prompts use role descriptions rather than licensed font binaries.
2. The repository has no public license yet. Do not assume reuse rights for generated assets or documentation until a license decision is recorded.
3. API-backed batch generation would require separately configured API access and billing, but built-in Codex `$imagegen` does not.

## Resume prompt

```text
Read AGENTS.md, STATUS.md, DECISIONS.md, the Foundation v0.1 spec, Pilot 01 manifest, Task 5 of the implementation plan, and docs/handoff/CODEX_IMAGE_GENERATION.md.

Continue only Task 5 on a new branch named codex/pilot-01-card-01. Preserve canonical copy exactly. Create prompts/01-hook.yaml first, run the tests, manifest validation, and dedicated style-anchor validation, then explicitly invoke $imagegen three times using the approved style-anchor image as visual guidance. Do not inspect or require OPENAI_API_KEY for built-in image generation, and do not create an API helper in this task.

Save and review three candidates, persist selection evidence in evaluation/review.md, record the accepted score in scores.csv, promote only the human-approved candidate to the canonical path, update STATUS.md and CHANGELOG.md, rerun validation, and open a pull request.

If the $imagegen capability itself is unavailable on this Codex surface, stop at the visual review gate and report that exact capability blocker. Do not create a placeholder PNG.
```
