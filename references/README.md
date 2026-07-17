# Reference policy

## Canonical

`canonical/` contains approved visual anchors that may guide future generation. They still contain AI-rendered specimen text and are not publication assets unless explicitly promoted under a pilot release.

## Superseded references

Rejected explorations are not kept in the active tree. Their decision history is summarized in `DECISIONS.md`, the Foundation specification, and relevant provenance sidecars; original files remain recoverable from Git history.

## Rules

- Use the Foundation v0.1 spec and canonical references together.
- Never infer canonical copy from an image; use the relevant YAML manifest.
- Treat AI-rendered wording inside reference boards as illustrative and potentially inaccurate.
- Do not add every candidate generation to Git. Keep candidates under an ignored `drafts/` path and commit only approved references or release assets.
