# Project Status

**Project:** Constructive Signal Design Language
**Version:** Visual DNA Sprint 1 catalog
**Current milestone:** Milestone 2 — complete
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

Milestone 2 is complete as a twenty-family Visual DNA catalog. Its infrastructure defines:

- the exact 20-family catalog order and 13 A / 6 B / 1 C canonical distribution;
- complete per-family semantic, assembly, expression-level, typography, spacing, signal, content, exclusion, Prompt DSL, and acceptance contracts;
- Pilot 01 reference evidence routes for Hero, Comparison, and Loop;
- one fixed demo dataset shared by KPI, Table, Chart, and Dashboard prototypes;
- strict catalog, analytical-data, raster, score, preview, contact-sheet, and machine-index tooling;
- a stacked one-packet/one-family pull-request sequence with no automatic merges.

Pilot-backed catalog evidence is audited and accepted for Hero, Comparison, and Loop. Their actual canonical bytes, RGB `1920×1080` metadata, exact Prompt DSL content, three-candidate selection records, hashes, `1280×720` readability evidence, and Pilot rubric rows all pass the Milestone 2 contract. No regeneration is justified.

The user-approved D-028 rebaseline makes all three boards in `references/canonical/` primary Visual DNA authority and keeps the Pilot landscape anchor as secondary execution evidence. A series-level contact-sheet audit found that the first generated passes for Cover, Quote, Big Number, Collision, Before / After, Timeline, Matrix, Hierarchy, Architecture, Workflow, and Pipeline satisfy copy and semantic checks but collapse toward generic centered infographics. Those approvals are superseded, their active rasters/scores/index evidence are removed, and all affected families require new candidate passes with the complete four-image reference package. Cover, Quote, Big Number, Collision, Before / After, Timeline, Matrix, Hierarchy, Architecture, Workflow, and Pipeline now pass that regeneration gate and restore the primary boards' expression contrast, Modular Technical cadence, numeric Pulse, active-plane synthesis, semantic trace language, quiet chronological Axis, square relative-position grammar, nested ownership-depth grammar, open system-boundary topology, finite operational route grammar, and continuous carrier-through-gates transformation; Decision Tree adds a binary branch mechanism, Framework adds an equal-concept open Cluster, and the bounded analytical set is complete with a fixed-data KPI Pulse, exact-lookup Table, audited 0–100% Chart, and open composite Dashboard. Historical first passes remain in review notes, ignored drafts, and Git history.

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
patterns/visual-dna-sprint-01/canonical/light/16x9/04-cover.png through 20-dashboard.png
patterns/visual-dna-sprint-01/previews/landscape/01-hero.png through 20-dashboard.png
patterns/visual-dna-sprint-01/contact-sheets/visual-dna-01-all.png
patterns/visual-dna-sprint-01/contact-sheets/visual-dna-01-editorial.png
patterns/visual-dna-sprint-01/contact-sheets/visual-dna-01-structural.png
patterns/visual-dna-sprint-01/contact-sheets/visual-dna-01-analytical.png
```

## Validation state

```text
.venv/bin/python -m pytest -q
49 passed

.venv/bin/python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
manifest valid

.venv/bin/python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
style anchor valid

.venv/bin/python tools/validate_assets.py pilots/01-agentic-discipline
assets valid

.venv/bin/python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv
scores valid

.venv/bin/python tools/validate_pattern_catalog.py patterns/visual-dna-sprint-01/manifest.yaml
pattern catalog valid

.venv/bin/python tools/validate_pattern_data.py patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml
pattern analytical data valid

.venv/bin/python tools/validate_pattern_assets.py patterns/visual-dna-sprint-01
pattern assets valid

.venv/bin/python tools/validate_pattern_scores.py patterns/visual-dna-sprint-01/evaluation/scores.csv
pattern scores valid

.venv/bin/python tools/validate_pattern_review.py patterns/visual-dna-sprint-01
pattern review valid

.venv/bin/python tools/build_pattern_catalog.py patterns/visual-dna-sprint-01
pattern catalog built: 20 previews, 4 contact sheets

.venv/bin/python tools/validate_pattern_index.py patterns/visual-dna-sprint-01
pattern index valid
```

## Primary signal status

Met: all 20 families have accepted canonical evidence — three audited Pilot references, the complete D-028 corrective sequence through Pipeline, and newly generated Decision Tree, Framework, KPI, Table, Chart, and Dashboard. The full, editorial, structural, and analytical contact sheets pass visual review, and all strict milestone validators pass. Pilot 01 remains fully met.

## Secondary signal status

Met: all twenty families pass their individual primary-authority, Prompt DSL, exact-copy/data, raster, flat-signal, and series-contact-sheet gates. Complete-mode asset, score, review, machine-index, preview, and contact-sheet gates pass for the built catalog.

## Repository state

Infrastructure review and the stacked family sequence remain open without merges. All twenty family evidence packets are complete through Dashboard; the final catalog build and strict validation packet is ready on `codex/m2-catalog-completion` above `codex/m2-dashboard`.
