# Rejected initial review archive

These nine comparison/overview PNGs are rejected visual explorations, not
selected or accepted raster evidence. They were removed from active Git
tracking during the 2026-11-08 cleanup. Existing local copies remain here,
ignored, and a second local backup was verified before untracking.

`archive-manifest.json` records each original repository path, byte size,
SHA-256, and the pre-cleanup commit. `candidate-hashes.yaml` and the package's
`evaluation/review.md` retain candidate provenance and rejection reasons.
The archive PNGs are optional for a fresh checkout and are not CI inputs.

The original bytes remain recoverable from the recorded commit while Git
history is retained. For example, from the repository root:

```bash
git show c8056d153dbb3856844b80cdb4138a7f7d8816b2:extensions/arsenal-expansion-v0.1/selection/rejected-initial/overview.png > extensions/arsenal-expansion-v0.1/selection/rejected-initial/overview.png
```

Verify restored bytes against `archive-manifest.json`. Any future history
rewrite must first preserve an independently retrievable archive and update
these instructions. This cleanup does not authorize a history rewrite.
