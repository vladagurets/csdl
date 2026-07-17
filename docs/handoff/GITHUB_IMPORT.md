# GitHub Initial Import — `vladagurets/csdl`

## Verified target

- Repository: `https://github.com/vladagurets/csdl`
- Owner: `vladagurets`
- Default branch: `main`
- Visibility at handoff: public
- Repository state at handoff: empty
- Intended working branch: `pilot-01`
- Local source of truth: the full-history Git bundle delivered with the handoff package

No public license has been selected. Publishing the working repository does not grant reuse rights beyond the defaults of applicable copyright law.

## Preferred import: preserve the existing Git history

Download `csdl-initial-import.bundle`, then run:

```bash
git clone -b main csdl-initial-import.bundle csdl
cd csdl
# The bundle exposes pilot-01 as a remote-tracking ref; materialize it locally before replacing origin.
git branch pilot-01 refs/remotes/origin/pilot-01
git remote set-url origin https://github.com/vladagurets/csdl.git
git push -u origin main
git push -u origin pilot-01
```

Verify:

```bash
git remote -v
git branch -a
git log --oneline --decorate -8
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
```

Expected baseline:

```text
9 passed
manifest valid
```

## Alternative import: source archive

Use `csdl-source-export.zip` only when preserving local commit history is not important:

```bash
git clone https://github.com/vladagurets/csdl.git
cd csdl
unzip ../csdl-source-export.zip
# Copy the archive contents into the repository root if the unzip created a wrapper directory.
git add .
git commit -m "chore: import CSDL foundation and Codex handoff"
git push -u origin main
```

## GitHub setup after the first push

1. Keep `main` as the default branch.
2. Push `pilot-01` as the current milestone branch.
3. Enable branch protection on `main` after the import.
4. Require `.github/workflows/validate.yml` before merging.
5. Prefer squash merge for one-task pull requests.
6. Connect `vladagurets/csdl` to Codex.
7. Do not add font binaries, the uploaded *Two Squares* PDF, API keys, or unreviewed raster drafts.

## First Codex session

Start in Ask mode:

```text
Read AGENTS.md, STATUS.md, DECISIONS.md, specs/2026-07-17-csdl-v0.1-design.md, pilots/01-agentic-discipline/manifest.yaml, and Task 5 in docs/superpowers/plans/2026-07-17-csdl-pilot-01.md. Summarize the locked constraints, the exact output contract for Card 01, and any environment requirement for GPT Image 2. Do not edit files.
```

Then create a Code-mode task:

```text
Implement only Task 5 of the Pilot 01 plan on branch codex/pilot-01-card-01. Preserve manifest copy exactly. Create the Card 01 prompt package and the minimal generation helper required by the plan. Run pytest and manifest validation. If GPT Image 2 generation is unavailable, stop at the visual review gate and report the exact command and environment requirements. Update STATUS.md only for work actually completed.
```
