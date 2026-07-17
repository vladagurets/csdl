# Changelog

## Unreleased

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

## 2026-07-17 — GitHub target confirmed

- selected `vladagurets/csdl` as the canonical GitHub repository;
- documented the public working-repository state and pending license decision;
- added a deterministic initial-import and Codex connection handoff.
