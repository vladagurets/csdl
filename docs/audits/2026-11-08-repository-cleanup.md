# Repository cleanup — 2026-11-08

## Scope and result

The user authorized the recommended cleanup sequence after the repository
audit of `c8056d153dbb3856844b80cdb4138a7f7d8816b2`. This task changes the
active repository tree and disposable local state; it does not rewrite Git
history, publish a release, change licensing, promote candidate vocabulary,
or generate/replace accepted CSDL raster evidence.

The working branch is `codex/repository-cleanup`.

## Clean-checkout tests

Previously, three Arsenal tests opened ignored draft PNGs and failed on a
clean Git snapshot. The tests now validate tracked selected PNGs against the
persisted candidate inventory, selected-choice bindings, raster metadata,
and rubric scores. The inventory still covers twenty-four distinct candidates;
it records evidence without claiming that absent local drafts were decoded.

`tools/build_arsenal_review.py ROOT --validate-selection` performs this
tracked-package check and is included in CI. The existing `--validate` command
still requires all twenty-four local drafts and additionally compares their
actual hashes to the persisted inventory. Synthetic temporary PNG fixtures
exercise invalid containers, changed candidate bytes, and builder behavior.
Additional tests reject changed selected bytes, changed source bindings, and
unreadable selected images without depending on local draft availability.

## Code cleanup

- Removed unused `sys`, `math`, `yaml`, and `deepcopy` imports and the unused
  `FONT_REGULAR` constant identified in the audit.
- Added `tools/validation_common.py` for YAML-mapping loading, forbidden-key
  discovery, token matching, and allowed semantic relations. Existing private
  names remain import aliases; validator messages and version boundaries are
  preserved. Removed imports made unused by this extraction.
- Preserved all existing executable tools: the audit did not establish that
  any complete script was dead. Pair-only helpers were left in place.

## Raster storage cleanup

All paths below are relative to
`extensions/arsenal-expansion-v0.1/selection/`.

1. Removed eight duplicate root recipe boards, `024-causal-chain.png` through
   `031-roadmap.png`, while preserving their byte-identical review-linked
   counterparts in `recalibration/`.
2. Removed the duplicate `recalibration/overview.png`, preserving the active
   root `overview.png`. These nine duplicate paths total **10,650,784 bytes**.
3. Updated the review builder to write the single board set under the active
   candidate-set directory and one root overview. A regression test checks
   the resulting file tree so the duplicate paths are not recreated.
4. Removed nine rejected initial board/overview PNGs from active Git tracking,
   totaling **8,880,697 bytes**. Local copies remain under `rejected-initial/`
   and are ignored; an external local copy was independently hash-verified
   before untracking. The directory retains its candidate hashes, a per-file
   `archive-manifest.json`, and recovery instructions pinned to the pre-cleanup
   commit. Review notes describe the storage change.

The prospective fresh checkout contains **18 fewer PNG paths / 19,531,481
fewer bytes (18.63 MiB)**. Existing local rejected copies remain on disk;
only the duplicate group was physically removed. This is not a claim of
equivalent Git-pack savings: Git already deduplicates identical blobs and
history remains reachable.

All sixty accepted raster paths/hashes, all eight selected Arsenal PNGs,
remaining review boards, manifests, choice records, scores, and provenance
remain unchanged. The three shared Pilot/Visual DNA preview pairs remain
because their paths belong to protected evidence contracts.

## Local-only cleanup and ignore rules

- Removed 45 untracked disposable cache entries (`__pycache__`, `.pytest_cache`,
  and `.DS_Store`), totaling **1,348,526 bytes**, excluding `.git` and `.venv`.
- After a dry-run identified the missing-worktree registration, pruned only
  the stale `csdl-worktree-session-brazen-bunting-zout` registration. No live
  worktree or branch was removed.
- Preserved stash `18cd8ef7d6801d65e7a67d6380db62a336efb7a6`, all other refs,
  ignored presentation packages, local draft candidates, `.scratch` production
  scripts and review PNGs, and the Python environment.
- Added narrow ignore rules for JPG/JPEG/WEBP draft media, draft-local
  `approved.txt`, and rejected-initial board PNGs. Text prompts, manifests,
  hashes, and archive instructions remain trackable.

## Verification

Tests ran in a separate candidate snapshot containing only prospective
tracked files, without ignored draft or rejected-archive PNGs. The existing
Python 3.12/macOS environment was used; the Ubuntu/Python 3.11 GitHub runner
was not invoked.

- **190 tests passed**, including all existing negative/error-contract fixtures.
- **27 validation/build steps** from the updated CI workflow passed when
  replayed locally, including the new tracked Arsenal selection gate.
- Two additional Arsenal contract/proof build and validation commands passed.
- Two Design Book builds passed their deterministic report comparison.
- All tracked source/output hashes in the candidate snapshot remained
  unchanged after builders; no tracked build drift was observed.
- The full local Arsenal `--validate` check also passed against the preserved
  twenty-four drafts and selected source hashes.
- All retained repository PNGs match their pre-cleanup SHA-256 values;
  protected raster inventory validation passes for all sixty accepted files.
- `git diff --check` passes.

Local execution logs and XML/JSON receipts are stored outside the repository
in the dated cleanup audit folder; generated logs and temporary test fixtures
are not added to Git.

## History decision

History rewriting is deferred. The ordinary tree cleanup resolves the
confirmed tracking issues without breaking historical provenance. Older
references and accepted/rejected transitions are explicitly archived in Git;
some large historical blobs are held by side refs and stash rather than main.
A separate history-purge task would require a complete independent archive,
an exact object/path selection, and a review of all retained refs. This task
performs no force-push, branch deletion, stash drop, or object-store pruning.
