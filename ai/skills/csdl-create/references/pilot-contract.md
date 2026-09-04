# Pilot output contract

## Canonical location

Use exactly:

```text
pilots/{two-digit-ID}-{kebab-topic-name}/
```

Never overwrite an existing pilot. Inspect `pilots/` and propose the next unused ID when the user does not provide one.

## Required tree

```text
pilots/{ID-topic-name}/
├── README.md
├── sources.md
├── manifest.yaml
├── prompts/
│   ├── 00-style-anchor.yaml
│   └── {card-id}-{slug}.yaml × card_count
├── references/
│   └── reference-package.md
├── drafts/light/16x9/
│   └── {card-id}-{slug}/{card-id}-{slug}-v1.png ... -v3.png × card_count
├── canonical/light/16x9/
│   └── 1.png ... {card_count}.png
├── previews/landscape/
│   └── {card-id}-{slug}.png × card_count
├── contact-sheets/
│   └── pilot-{ID}-light.png
└── evaluation/
    ├── rubric.yaml
    ├── scores.csv
    └── review.md
```

Draft PNG files remain ignored by Git. Persist their filenames, rejection evidence, and selected hashes in `evaluation/review.md`.

## Reference hierarchy

Attach all four images to every built-in generation call, in this order:

1. `references/canonical/1.png`
2. `references/canonical/2.png`
3. `references/canonical/3.png`
4. `pilots/01-agentic-discipline/references/style-anchor-light.png`

Treat the first three as primary Visual DNA authority and the Pilot 01 landscape anchor as secondary execution evidence. Record their repository paths and SHA-256 values in `references/reference-package.md`.

Do not generate a replacement style anchor unless the user separately approves that scope.

## Manifest contract

Keep the existing Pilot 01 shape and add these fields to every card:

```yaml
asset: canonical/light/16x9/1.png
prompt: prompts/01-example.yaml
exact_copy:
  - "Every visible line"
```

The pilot header must declare:

- `id`, `slug`, title, topic, language, and terminology language;
- `mode: light`;
- `canonical_canvas: "1920x1080"`;
- `orientation: landscape`;
- `card_count` equal to the approved positive slide count;
- `rhythm` containing exactly `card_count` values from `A`, `B`, and `C`;
- contiguous zero-padded card IDs from `01` through the final card.

Canonical asset filenames are separate from card IDs and slugs. Use the
card's unpadded one-based manifest position, beginning with `1.png` in every
pilot. Do not add zero padding or descriptive text to canonical filenames.

For a standard seven-slide series, propose `rhythm: [A, A, B, A, B, A, C]`. For any other count, persist the content-led rhythm approved during intake. The standard seven-slide rhythm remains a design default, not a validator-enforced length.

Use only declared Recipe and component names from the current repository manifests.
Before candidate selection, a card's `visual_mechanism` states the shared
explanatory objective rather than prescribing one layout skeleton. After
selection, update it to the selected direction's observed dominant mechanism;
the approved `exact_copy`, data, and evidence contract remains unchanged.

## Candidate direction contract

Every per-slide prompt must include this authoring wrapper in addition to its
shared Prompt DSL content:

```yaml
generation_constraints:
  candidate_directions:
    - id: v1
      concept: "Distinct semantic frame for the approved topic"
      composition: "Distinct topology, reading path, and Anchor/Signal relationship"
      visual_mechanism: "Distinct primary interaction of semantic CSDL components"
    - id: v2
      concept: "Second semantic frame"
      composition: "Second composition topology"
      visual_mechanism: "Second dominant mechanism"
    - id: v3
      concept: "Third semantic frame"
      composition: "Third composition topology"
      visual_mechanism: "Third dominant mechanism"
```

The IDs and order are exact. Values for `concept`, `composition`, and
`visual_mechanism` must be non-empty and unique across `v1`, `v2`, and `v3`.
Each candidate is generated from its own direction-specific prompt while topic,
exact copy/data, evidence, expression level, canvas, references, and exclusions
remain shared. This wrapper controls candidate exploration and does not extend
the closed Prompt DSL v0.5 schema.

Repeating one prompt, mirroring or repositioning one layout, changing only
palette/shape/scale/spacing/alignment, or substituting decoration is invalid.
If side-by-side review finds a cosmetic or near-variant pair, regenerate the
collapsed direction before selection.

## Raster and review gates

- Candidate source: built-in GPT Image output, normally `1672×941` RGB PNG.
- Normalized candidate and canonical: exactly `1920×1080`, RGB PNG, resize only.
- Review preview: exactly `1280×720`, RGB PNG.
- Contact sheet: exactly `3840×2160`, RGB PNG, with a centered grid adapted to `card_count`; use one row for a small set and denser rows for larger sets while preserving sequence order and review readability.
- Candidate count: exactly three reviewed candidates per slide, or `3 × card_count` candidates in total, with three unique normalized SHA-256 values.
- Candidate divergence: every pair visibly differs in concept, dominant visual mechanism, and composition topology; `evaluation/review.md` records `Candidate-divergence review: pass` for every slide before selection.
- Copy: every visible character must match `exact_copy`; no extra text.
- Geometry: one main idea, one mechanism, one dominant Signal; no removable decoration.
- Expression: every card level must match the corresponding value in the approved manifest rhythm; only `A`, `B`, and `C` are valid.
- Scores: critical criteria `5/5`, all others at least `4/5`, average at least `4.4`.

## Hard exclusions

No gradients, shadows, glossy surfaces, 3D, decorative coordinate systems, random dot fields, fake charts, fabricated metrics, UI dashboards, card-shell layouts, logos, footers, interface chrome, political imagery, Soviet or revolutionary-poster styling, imitation-1920s styling, or pixel/bitmap/retro-computer lettering.

Do not add generated labels, legends, brands, statistics, citations, or annotations that are absent from `exact_copy`.
