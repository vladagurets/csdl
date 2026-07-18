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

Cover is the first newly generated family. Three built-in GPT Image 2 candidates were reviewed; Candidate 3 was promoted because it preserves exact copy, removes the undeclared arrow present in Candidates 1–2, and uses one diagonal coral Signal plane as the catalog’s single canonical Level C peak.

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
21 passed

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

Partially validated: the Milestone 2 semantic and machine-readable contracts pass, and 4/20 families have accepted canonical evidence. Sixteen new family rasters and the completed contact sheets remain. Pilot 01 remains fully met.

## Secondary signal status

Met for the infrastructure packet: tests, catalog/schema validation, fixed-data validation, and incomplete-milestone Pilot reference/score gates pass. Strict asset and score commands intentionally remain final milestone gates.

## Repository state

Infrastructure review is open from `codex/m2-infrastructure`; Pilot evidence and Cover are stacked in subsequent branches. The next family packet generates and reviews Quote from three built-in GPT Image 2 candidates.
