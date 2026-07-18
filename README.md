# Constructive Signal Design Language (CSDL)

A geometric visual language for explaining complex ideas clearly, memorably, and consistently with humans and generative models.

**Status:** Foundation v0.1, Pilot 01 v0.1.0, and Milestone 2 — Visual DNA Sprint 1 are complete; Milestone 3 — Component Library is in progress.

**GitHub:** `vladagurets/csdl` is the selected public working repository. A public license has not yet been selected.

## Start here

1. Read [`AGENTS.md`](AGENTS.md) before assigning work to Codex.
2. Review the locked choices in [`DECISIONS.md`](DECISIONS.md).
3. Check current progress and the exact next task in [`STATUS.md`](STATUS.md).
4. Follow the staged work in [`ROADMAP.md`](ROADMAP.md).
5. Treat [`specs/2026-07-17-csdl-v0.1-design.md`](specs/2026-07-17-csdl-v0.1-design.md) as the design source of truth.
6. Execute Milestone 3 from [`docs/plans/2026-07-18-csdl-milestone-3.md`](docs/plans/2026-07-18-csdl-milestone-3.md) and its evidence audit.
7. Use [`docs/plans/2026-07-18-csdl-milestone-2.md`](docs/plans/2026-07-18-csdl-milestone-2.md) for the completed Visual DNA contract.
8. Use [`docs/handoff/CODEX_IMAGE_GENERATION.md`](docs/handoff/CODEX_IMAGE_GENERATION.md) for the approved Codex raster workflow.

## Current foundation

- Direction: **Constructive Signal**
- Default mode: **Quiet Modular**
- Display voice: **Modular Technical**, with rare condensed editorial emphasis
- Palette: **Muted Signal** on warm paper; full night mode deferred
- Canonical canvas: **16:9, 1920 × 1080 px, landscape**
- Portrait masters and mobile-preview deliverables: **not required**
- Density rhythm: **A → A → B → A → B → A → C**
- Core rule: **one idea + one visual mechanism + one signal per screen**
- Canonical documentation: Markdown; images calibrate the written system
- Shared Pilot 01 reference: [`style-anchor-light.png`](pilots/01-agentic-discipline/references/style-anchor-light.png), with adjacent provenance and review evidence

## Repository map

```text
AGENTS.md                         Codex operating instructions
DECISIONS.md                      locked and provisional design decisions
STATUS.md                         completed, active, blocked, and next work
ROADMAP.md                        milestones after Pilot 01
specs/                            approved design specifications
docs/superpowers/plans/           task-by-task implementation plans
docs/handoff/                     current Codex raster workflow
pilots/01-agentic-discipline/     canonical copy, prompts, evaluation, assets
patterns/visual-dna-sprint-01/    20-family contracts, prompts, evidence, assets
components/component-library-v0.1/ 15-component contracts, proofs, indexes
references/canonical/             approved visual anchors
research/                         source analysis without redistributing source PDFs
tools/ and tests/                 validation and assembly tooling
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
python tools/validate_pattern_catalog.py patterns/visual-dna-sprint-01/manifest.yaml
python tools/validate_pattern_data.py patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml
```

The baseline test suite, manifest validator, and shared-reference validator must pass before raster promotion.

## Image workflow

The repository separates **design governance** from **raster generation**:

- Codex owns specifications, Prompt DSL, validation, versioning, issue/PR workflow, and release packaging.
- For normal card work, Codex explicitly invokes built-in `$imagegen`, which uses `gpt-image-2` and counts toward Codex usage limits. This route does not require `OPENAI_API_KEY`.
- An external ChatGPT Images session may be used as a human-operated fallback with the same prompt and review contract.
- An API-backed script is optional for larger or programmatic batches and requires separately billed API access; it is not implicit scope for a card task.
- Only approved references and canonical exports belong in Git. Intermediate candidates live under `pilots/**/drafts/` and are ignored.
- Pilot 01 uses a newly selected 16:9 Ukrainian/Inter style anchor; all superseded portrait and pixel-font references remain only in Git history.
- AI-rendered copy must match `manifest.yaml` exactly before publication.

## Pilot 01

Pilot 01 explains how disciplined workflows and retained learning make agentic development more reliable over time. Its source of truth is [`pilots/01-agentic-discipline/manifest.yaml`](pilots/01-agentic-discipline/manifest.yaml).

Pilot 01 is released as the first CSDL Visual DNA set. See [`RELEASE.md`](pilots/01-agentic-discipline/RELEASE.md).

## Visual DNA Sprint 1

The Milestone 2 catalog formalizes Hero, Cover, Quote, Big Number, Comparison, Collision, Before / After, Timeline, Matrix, Hierarchy, Architecture, Workflow, Loop, Pipeline, Decision Tree, Framework, KPI, Table, Chart, and Dashboard. Its source of truth is [`patterns/visual-dna-sprint-01/manifest.yaml`](patterns/visual-dna-sprint-01/manifest.yaml), with the mandatory reference hierarchy in [`visual-authority.yaml`](patterns/visual-dna-sprint-01/visual-authority.yaml). KPI/Table/Chart/Dashboard use fixed demo data and remain bounded prototypes rather than a premature full Analytical Mode.

## Component Library

Milestone 3 formalizes Anchor, Signal, Field, Frame, Cluster, Vector, Divider, Node, Loop, Collision, Bridge, Axis, Pulse, Label, and constrained Legend from accepted Visual DNA evidence. All fifteen component contracts now pass strict library validation. Markdown specifications remain canonical; composition proofs and deterministic index/compatibility outputs are the remaining milestone gates. No new raster generation is part of the component library.
