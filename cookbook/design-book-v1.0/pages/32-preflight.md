---
id: '32'
title_uk: Publishing preflight
editorial_language: uk
terminology_language: en
---
# Publishing preflight

Фінальна перевірка з’єднує зміст, visual quality, accessibility, provenance і governance в один release-independent gate.

## Content

- [ ] one main idea, one mechanism, one dominant `Signal` per screen/example;
- [ ] Ukrainian editorial content complete; English identifiers exact;
- [ ] all references resolve and claim class is honest;
- [ ] exact copy/data, units, sources, missing states, forecast and uncertainty preserved.

## Visual and accessibility

- [ ] full-size pages and contact sheet reviewed;
- [ ] no clipping, overflow, missing glyphs or broken reading order;
- [ ] contrast thresholds and color-independent carriers pass;
- [ ] grayscale and projector behavior remain interpretable;
- [ ] accepted rasters embedded without mutation.

## Build and governance

- [ ] page count is 25–40 and order matches manifest;
- [ ] build runs twice with identical hashes;
- [ ] tests, Milestone 1–7 validators and CI pass;
- [ ] generated files are not hand-edited; `git diff --exit-code` passes;
- [ ] license, tags, GitHub Releases, Milestone 8 and public-release claims remain untouched.
