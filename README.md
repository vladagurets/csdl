# Constructive Signal Design Language (CSDL)

A geometric visual language for explaining complex ideas clearly, memorably, and consistently with humans and generative models.

**Status:** Foundation v0.1 approved; Pilot 01 — Agentic Discipline is in progress.

## Start here

1. Read [`AGENTS.md`](AGENTS.md) before assigning work to Codex.
2. Review the locked choices in [`DECISIONS.md`](DECISIONS.md).
3. Check current progress and the exact next task in [`STATUS.md`](STATUS.md).
4. Follow the staged work in [`ROADMAP.md`](ROADMAP.md).
5. Treat [`specs/2026-07-17-csdl-v0.1-design.md`](specs/2026-07-17-csdl-v0.1-design.md) as the design source of truth.
6. Execute Pilot 01 from [`docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`](docs/superpowers/plans/2026-07-17-csdl-pilot-01.md).

## Current foundation

- Direction: **Constructive Signal**
- Default mode: **Quiet Modular**
- Display voice: **Modular Technical**, with rare condensed editorial emphasis
- Palette: **Muted Signal** on warm paper; full night mode deferred
- Canonical canvas: **4:5, 1080 × 1350 px**
- Secondary canvas: **16:9, 1920 × 1080 px**, rebuilt rather than cropped
- Density rhythm: **A → A → B → A → B → A → C**
- Core rule: **one idea + one visual mechanism + one signal per screen**
- Canonical documentation: Markdown; images calibrate the written system

## Repository map

```text
AGENTS.md                         Codex operating instructions
DECISIONS.md                      locked and provisional design decisions
STATUS.md                         completed, active, blocked, and next work
ROADMAP.md                        milestones after Pilot 01
specs/                            approved design specifications
docs/superpowers/plans/           task-by-task implementation plans
docs/handoff/                     Codex handoff and resume prompts
pilots/01-agentic-discipline/     canonical copy, prompts, evaluation, assets
references/canonical/             approved visual anchors
references/archive/               superseded explorations; never use as canon
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
```

The baseline currently contains nine passing tests.

## Image workflow

The repository separates **design reasoning** from **raster generation**:

- Codex owns specifications, Prompt DSL, scripts, validation, versioning, issue/PR workflow, and release packaging.
- GPT Image 2 produces or edits raster candidates through an API-backed script or an external ChatGPT image session.
- Only approved references and canonical exports belong in Git. Intermediate candidates live under `pilots/**/drafts/` and are ignored.
- AI-rendered copy must match `manifest.yaml` exactly before publication.

## Pilot 01

Pilot 01 explains how disciplined workflows and retained learning make agentic development more reliable over time. Its source of truth is [`pilots/01-agentic-discipline/manifest.yaml`](pilots/01-agentic-discipline/manifest.yaml).

The first unfinished implementation item is **Task 5: generate and approve Card 01 — Hook / Level A**.
