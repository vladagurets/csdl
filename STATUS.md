# Project Status

**Project:** Constructive Signal Design Language
**Version:** Visual DNA Sprint 1 infrastructure
**Current milestone:** Milestone 2 — in progress
**Last updated:** 2026-07-18

## Outcome

Pilot 01 was restarted and completed under the user-approved 16:9-first contract. The canonical canvas is `1920×1080`, landscape. Portrait masters, 4:5 assets, and mobile previews are not deliverables. Previous Pilot 01 rasters and review evidence are superseded and remain only in Git history.

The completed release contains:

- one approved 16:9 shared style anchor selected from three GPT Image 2 candidates;
- seven approved 16:9 slides, each selected from three candidates;
- eight machine-readable Prompt DSL files;
- seven `1280×720` landscape review previews;
- one `3840×2160` contact sheet;
- complete candidate, exact-copy, raster, selection, and rubric evidence;
- passing automated validation.

Milestone 2 has started from a synchronized clean `main`. Its infrastructure packet defines:

- the exact 20-family catalog order and 13 A / 6 B / 1 C canonical distribution;
- complete per-family semantic, assembly, expression-level, typography, spacing, signal, content, exclusion, Prompt DSL, and acceptance contracts;
- Pilot 01 reference evidence routes for Hero, Comparison, and Loop;
- one fixed demo dataset shared by KPI, Table, Chart, and Dashboard prototypes;
- strict catalog, analytical-data, raster, score, preview, contact-sheet, and machine-index tooling;
- a stacked one-packet/one-family pull-request sequence with no automatic merges.

Pilot-backed catalog evidence is audited and accepted for Hero, Comparison, and Loop. Their actual canonical bytes, RGB `1920×1080` metadata, exact Prompt DSL content, three-candidate selection records, hashes, `1280×720` readability evidence, and Pilot rubric rows all pass the Milestone 2 contract. No regeneration is justified.

The user-approved D-028 rebaseline makes all three boards in `references/canonical/` primary Visual DNA authority and keeps the Pilot landscape anchor as secondary execution evidence. A series-level contact-sheet audit found that the first generated passes for Cover, Quote, Big Number, Collision, Before / After, Timeline, Matrix, Hierarchy, Architecture, Workflow, and Pipeline satisfy copy and semantic checks but collapse toward generic centered infographics. Those approvals are superseded, their active rasters/scores/index evidence are removed, and all affected families require new candidate passes with the complete four-image reference package. Cover and Quote now pass that regeneration gate and restore the primary boards' Modular Technical Level C/Level A contrast; historical first passes remain in review notes, ignored drafts, and Git history.

## Canonical outputs

```text
pilots/01-agentic-discipline/references/style-anchor-light.png
pilots/01-agentic-discipline/canonical/light/16x9/01-hook.png
pilots/01-agentic-discipline/canonical/light/16x9/02-problem.png
pilots/01-agentic-discipline/canonical/light/16x9/03-model.png
pilots/01-agentic-discipline/canonical/light/16x9/04-comparison.png
pilots/01-agentic-discipline/canonical/light/16x9/05-synthesis.png
pilots/01-agentic-discipline/canonical/light/16x9/06-takeaway.png
pilots/01-agentic-discipline/canonical/light/16x9/07-share-card.png
pilots/01-agentic-discipline/contact-sheets/pilot-01-light.png
```

## Validation state

```text
.venv/bin/python -m pytest -q
47 passed

.venv/bin/python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
manifest valid

.venv/bin/python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
style anchor valid

.venv/bin/python tools/validate_assets.py pilots/01-agentic-discipline
assets valid

.venv/bin/python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv
scores valid
```

## Primary signal status

Partially validated: 5/20 families have accepted canonical evidence — three audited Pilot references plus D-028-regenerated Cover and Quote. Fifteen generated families, complete contact sheets, and strict series validation remain. Pilot 01 remains fully met.

## Secondary signal status

In correction: the semantic catalog and fixed-data contracts remain valid. Cover and Quote pass the new D-028 primary-authority, Prompt DSL, exact-copy, raster, flat-signal, and series-contact-sheet gates; the remaining generated families still await equivalent evidence.

## Repository state

Infrastructure review is open from `codex/m2-infrastructure`; the first generated family stack through Pipeline is superseded by the D-028 corrective packet. Rebaselined Cover and Quote packets are complete, and regeneration proceeds next to Big Number.
