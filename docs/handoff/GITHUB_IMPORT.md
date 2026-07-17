# GitHub Initial Import — `vladagurets/csdl`

## Status: completed

The repository import is complete.

- Repository: `https://github.com/vladagurets/csdl`
- Owner: `vladagurets`
- Default branch: `main`
- Visibility: public
- Imported history head: `21992631862fd84fcca26e07983f4efc0ed16c26`
- Codex repository reading: verified
- GitHub write/branch access: verified

No public license has been selected. Publishing the working repository does not grant reuse rights beyond the defaults of applicable copyright law.

The commands below are retained only for disaster recovery or a fresh mirror. They are no longer an active project blocker.

## Historical import: preserve the existing Git history

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

## Historical alternative: source archive

Use `csdl-source-export.zip` only when preserving commit history is not important:

```bash
git clone https://github.com/vladagurets/csdl.git
cd csdl
unzip ../csdl-source-export.zip
# Copy the archive contents into the repository root if the unzip created a wrapper directory.
git add .
git commit -m "chore: import CSDL foundation and Codex handoff"
git push -u origin main
```

## Active repository policy

1. Keep `main` as the default branch.
2. Protect `main` and merge through pull requests.
3. Require `.github/workflows/validate.yml` before merging.
4. Prefer squash merge for one-task pull requests.
5. Do not add font binaries, the uploaded *Two Squares* PDF, API keys, or unreviewed raster drafts.
6. Use built-in Codex `$imagegen` for normal card work; no `OPENAI_API_KEY` is required.
7. Reserve API-backed image generation for a separately scoped batch-automation task.

## Next Codex session

Use the current prompt from `docs/handoff/CODEX_IMAGE_GENERATION.md` rather than the superseded API-helper prompt from the original handoff package.
