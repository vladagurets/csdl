# Project Status

**Project:** Constructive Signal Design Language  
**Version:** Foundation v0.1  
**Current milestone:** Pilot 01 — Agentic Discipline  
**Last updated:** 2026-07-17

## Summary

Foundation choices are approved and encoded in Markdown. Pilot 01 has canonical content, validation tooling, a scoring rubric, and a shared Quiet Modular style anchor. The previously missing Task 4 raster has been restored with provenance, byte-level identity evidence, and an independent validation gate. Card 01 — Hook / Level A is now approved in the canonical asset tree with exact-copy review, mobile review, score evidence, and deterministic fallback provenance. The repository has been imported to `vladagurets/csdl`, Codex can read it, and GitHub write access has been verified.

## Completed

| Plan task | State | Evidence |
|---|---|---|
| Task 1 — repository and canonical content manifest | Complete | commit `c046d2c` |
| Task 2 — manifest validation with tests | Complete | commit `875994a` |
| Task 3 — raster-asset and rubric validation | Complete | commit `15efea1` |
| Task 4 — shared light-mode style anchor and generation boilerplate | Complete (repaired) | `style-anchor-light.png`, provenance sidecar, dedicated tests, and CI validator |
| Task 5 — Card 01 Hook / Level A | Complete | `01-hook.png`, `01-hook.provenance.md`, `evaluation/review.md`, and Card 01 score row |

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

### Task 6 — Generate and approve Card 02: Problem / Level A

Canonical content:

- headline: `AD-HOC РОБОТА РОЗПАДАЄТЬСЯ МІЖ СЕСІЯМИ`
- supporting copy: `Рішення губляться. Перевірки повторюються. Помилки повертаються.`
- mechanism: one broken Loop with three detached Nodes
- components: Loop, Node, Signal
- expression: Level A / Quiet
- output: `pilots/01-agentic-discipline/canonical/light/4x5/02-problem.png`

Follow the exact Task 6 steps in `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md` and the execution rules in `docs/handoff/CODEX_IMAGE_GENERATION.md`.

## Image-generation execution route

The default Task 6 route remains built-in Codex image generation:

- invoke `$imagegen` explicitly;
- use `gpt-image-2` through the user's Codex plan/usage limits;
- attach `pilots/01-agentic-discipline/references/style-anchor-light.png` as the primary visual reference;
- generate three independent candidates;
- no `OPENAI_API_KEY` or Python API helper is required for this route.

Task 5 used an explicitly approved deterministic Pillow fallback only after three built-in generations returned unrelated interface screenshots. That exception and its typography correction are recorded in `canonical/light/4x5/01-hook.provenance.md`; it does not silently change the default route for later cards.

If `$imagegen` is unavailable or produces unusable output on the active surface, stop at the visual review gate, report the exact failure, and request approval before changing generation route. Do not substitute a placeholder raster.

## Remaining Pilot 01 work

- [x] Task 5 — Card 01 Hook / Level A
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

Card 01 raster validation:

- PNG, `1080×1350`, RGB;
- exact canonical copy manually verified;
- full-resolution and `216×270` phone-width review passed;
- SHA-256 `cf97312ae89b7f03bf6c2f5c5e028b29c518b1d4146a0a24871cedf633ff2d9d`;
- accepted score average `4.71`, with clarity, mobile readability, and text fidelity at `5/5`.

Full asset validation remains incomplete until Cards 02–07 and the three 16:9 adaptations exist. The series-level score validator is expected to fail while unfinished rows `02`–`07` retain zero placeholders.

## Open constraints, not Task 6 blockers

1. Final font families remain deferred; prompts use role descriptions rather than licensed font binaries.
2. The repository has no public license yet. Do not assume reuse rights for generated assets or documentation until a license decision is recorded.
3. API-backed batch generation would require separately configured API access and billing, but built-in Codex `$imagegen` does not.

## Resume prompt

```text
Read AGENTS.md, STATUS.md, DECISIONS.md, the Foundation v0.1 spec, Pilot 01 manifest, Task 6 of the implementation plan, the approved style-anchor provenance, and docs/handoff/CODEX_IMAGE_GENERATION.md.

Continue only Task 6 on a new branch named codex/pilot-01-card-02. Preserve canonical copy exactly. Create prompts/02-problem.yaml first, run the tests, manifest validation, style-anchor validation, and validation of existing canonical assets, then explicitly invoke $imagegen three times using the approved style-anchor image as visual guidance. Do not inspect or require OPENAI_API_KEY for built-in image generation, and do not create an API helper in this task.

Save and review three candidates, persist selection and rejection evidence in evaluation/review.md, record the accepted Card 02 score in scores.csv, promote only the human-approved candidate to canonical/light/4x5/02-problem.png, update STATUS.md and CHANGELOG.md, rerun validation, and open a pull request.

If built-in image generation is unavailable or returns unusable non-CSDL output, stop at the visual review gate and report that exact failure. Do not create a placeholder PNG or silently switch generation routes.
```
