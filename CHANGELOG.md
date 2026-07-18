# Changelog

## Unreleased

## 0.1.0 — Pilot 01 Visual DNA 16:9 release — 2026-07-17

- Replaced the portrait-first foundation with a canonical `1920×1080` 16:9 landscape format after explicit user approval.
- Removed Pilot 01 portrait/mobile deliverables, reset the pilot to Task 1, and marked all previous 4:5 raster selections and scores non-canonical.
- Rebuilt the manifest, Prompt DSL package, validators, tests, rubric terminology, implementation plan, and raster handoff for seven direct 16:9 slides.
- Released one selected 16:9 shared style anchor, seven selected 16:9 slides, seven landscape previews, one contact sheet, complete review evidence, and passing scores.
- Historical entries below describe superseded work retained in Git history; they are not active Pilot 01 evidence.
- Locked Constructive Signal / Quiet Modular direction.
- Locked 4:5 canonical canvas and Level A/B/C rhythm.
- Approved Pilot 01 topic, seven-card narrative, and canonical copy.
- Prepared GitHub/Codex handoff with top-level README, AGENTS instructions, decision register, status, roadmap, research notes, CI, PR template, and archived visual provenance.
- Confirmed the initial import to `vladagurets/csdl` and verified repository read/write access.
- Set built-in Codex `$imagegen` as the default raster route for Pilot 01; clarified that it uses `gpt-image-2` through Codex usage limits and does not require `OPENAI_API_KEY`.
- Reserved API-backed image generation for explicitly scoped programmatic or larger-batch work with separate API billing.
- Added persistent candidate-selection, review-evidence, and per-card scoring requirements to the Codex operating instructions.
- Replaced superseded API-helper handoff prompts with the corrected Task 5 `$imagegen` workflow.
- Fixed editable installation in clean CI environments by disabling accidental setuptools discovery of non-package content directories.
- Repaired Pilot 01 Task 4 by restoring `style-anchor-light.png`, documenting its provenance and manual review, verifying its Git blob byte-for-byte, and adding dedicated unit and CI validation.
- Reopened Task 4 after the temporary pixel-font repair was rejected; replaced the active anchor with the exact user-selected GPT Image 2 candidate, switched the calibration copy to Ukrainian, aligned typography with Card 01's Inter-based hierarchy, persisted three-candidate review, and left the old bitmap raster only in Git history.
- Pinned the approved style-anchor SHA-256 in the dedicated validator so CI rejects any silent replacement or restoration of the superseded pixel raster.
- Completed Pilot 01 Task 5 with the approved Card 01 Hook / Level A raster, exact-copy and mobile review evidence, accepted rubric scores, and transparent deterministic fallback provenance after unusable built-in image outputs.
- Closed the final Task 5 promotion gap by replacing the approximate runner re-render with the byte-for-byte user-selected V1 and adding permanent SHA-256 and Git-blob identity enforcement.
- Completed Pilot 01 Task 6 with three built-in GPT Image 2 candidates, explicit user selection of Card 02 V1, exact-copy and phone-width review, persisted rejection evidence, and an accepted `4.71` rubric score.
- Removed superseded reference boards, completed-import and stale Task 5 handoffs, the rejected bitmap-repair plan/spec, and a byte-identical duplicate calibration image from the active tree; retained historical recoverability through Git and refreshed current Task 7 guidance.

## 2026-07-17 — GitHub target confirmed

- selected `vladagurets/csdl` as the canonical GitHub repository;
- documented the public working-repository state and pending license decision;
- added a deterministic initial-import and Codex connection handoff.
