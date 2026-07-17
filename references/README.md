# Reference policy

## Canonical

`canonical/` contains approved visual anchors that may guide future generation. They still contain AI-rendered specimen text and are not publication assets unless explicitly promoted under a pilot release.

## Archive

`archive/` preserves earlier explorations, rejected density levels, typography comparisons, and superseded directions. These files explain how decisions were reached but **must not** be used as the primary style reference by Codex or GPT Image 2.

## Rules

- Use the Foundation v0.1 spec and canonical references together.
- Never infer canonical copy from an image; use the relevant YAML manifest.
- Treat AI-rendered wording inside reference boards as illustrative and potentially inaccurate.
- Do not add every candidate generation to Git. Keep candidates under an ignored `drafts/` path and commit only approved references or release assets.
