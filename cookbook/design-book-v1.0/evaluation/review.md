# Cookbook and Design Book v1.0 — Publication Review

**State:** complete through integration PR #69 and merge commit `4c20829f4923c164b48985d06a49247ff372ed4f`
**Format:** ISO A4 landscape, 32 pages  
**Canonical sources:** `pages/01-cover.md` through `pages/32-preflight.md`  
**Generated artifact:** `output/pdf/csdl-cookbook-design-book-v1.0.pdf` (ignored, deterministic)

## Evidence audit and architecture

The Milestone 7 evidence audit classified direct canonical rules, multi-source editorial synthesis, deferred boundaries, and prohibited claims before implementation. D-033 records the additive publication boundary and selects A4 landscape after comparing it with 16:9 landscape and A4 portrait. No production dependency, font binary, license decision, public-release claim, or new CSDL raster evidence was added.

## Content and bilingual review

- page count and order: 32/32, pass;
- Ukrainian editorial-language declaration and Ukrainian content: 32/32, pass;
- English terminology registry: exact D-029 fifteen-component sequence and D-030 23-recipe sequence, pass;
- Prompt DSL package fields: exact v0.5 allowed-field sequence, pass;
- complete editorial Prompt DSL proof example: validates against v0.5, pass;
- required topics: all sixteen manifest topics have page coverage, pass;
- provenance: every page maps to existing repository sources and a declared claim class, pass;
- Analytical Mode and Accessibility dependency counts/versions/profiles: unchanged, pass.

## Visual review

Reviewed the `3840×2160` contact sheet and representative full-size pages 01, 05, 07, 16, 20, 24, 26, 29, and 32. The overview preserves a quiet opening, denser component/recipe middle, technical Prompt DSL/Analytical section, and quiet practice/preflight close. Full-size review found no clipped body text, missing glyphs, overlapping blocks, cropped evidence, or broken page numbers. A first-pass evidence caption could exceed its frame; the builder was corrected to use a bounded `accepted evidence · source SHA-256 pinned` label and the publication was rebuilt.

Minimum adaptive body size is recorded in `output/build-report.yaml`; the complete Prompt DSL page is the densest page and remains readable at full size. Evidence thumbnails are subordinate, uncropped, and labeled as accepted evidence. Publication renders are derived review outputs and explicitly do not become raster authority.

## Accessibility and PDF review

- declared page text contrast, secondary text contrast, and Signal non-text contrast: pass;
- all 32 grayscale pages generated; representative page 29 retains hierarchy and readable evidence boundaries: pass;
- PDF metadata: 32 pages, A4 `841.89×595.276 pt`, PDF 1.7: pass;
- Unicode text layer: `pypdf` extracted 30,848 characters including Ukrainian and English in page order: pass;
- PDF pages 24 and 29 rendered independently with Poppler and match the deterministic page renders: pass;
- reading-order sidecar contains `PAGE 01` through `PAGE 32` in manifest order: pass.

The PDF has an extractable Unicode reading layer and canonical Markdown remains the primary accessible source. It is not claimed as PDF/UA-tagged; exact final font licensing remains deferred.

## Determinism and raster integrity

The focused test builds the complete publication twice in an isolated repository copy and requires byte-identical generated and output files. Local source build/validation passes. The report pins fixed metadata, page/text/PDF/contact-sheet hashes, font path/digest, and all embedded evidence hashes. The Accessibility v0.1 inventory remains exactly sixty files with zero SHA-256 mismatches.

## Remaining boundaries

- global licensed-font selection remains unresolved;
- PDF is text-extractable but not claimed as PDF/UA-tagged;
- night/projector/monochrome/CVD visual calibration remains deterministic specification evidence only;
- Legend retains constrained status and no positive accepted family raster;
- license, tags, GitHub Releases, public-release positioning, and Milestone 8 remain untouched.
