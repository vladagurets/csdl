# CSDL Decision Register

**Last reviewed:** 2026-07-18
**Change rule:** a locked decision changes only after explicit user approval. Update this file, the foundation spec, and the changelog in the same pull request.

## Locked decisions

| ID | Decision | Rationale |
|---|---|---|
| D-001 | The system is named **Constructive Signal Design Language (CSDL)**. | It is a language for thinking and composing, not merely a template library. |
| D-002 | Primary direction is **Constructive Signal**. | Best balance of editorial clarity, authorial identity, and geometric narrative. |
| D-003 | Default expression is **Quiet Modular**. | Early references were overloaded; the quieter mode preserves distinctiveness without sacrificing comprehension. |
| D-004 | Level distribution is approximately **60–70% A / 20–30% B / 5–10% C**. | Quiet cards carry information; Constructive cards explain relationships; Signal cards create rare peaks. |
| D-005 | Standard seven-card rhythm is **A → A → B → A → B → A → C**. | Prevents a carousel from becoming seven competing posters. |
| D-006 | Display typography is **Modular Technical**. | It supports AI/software topics, square engineering proportions, and mixed Ukrainian/English text. |
| D-007 | A rare condensed editorial voice may provide emphasis, but never becomes the default. | Keeps some vertical energy without returning to a poster-heavy system. |
| D-008 | Reading text uses a neutral high-legibility sans; code and technical sequences use monospace. | Separates editorial, explanatory, and technical voices. |
| D-009 | Color direction is **Muted Signal**: warm paper, warm graphite, mineral coral, dusty data blue, soft ochre, and mineral green. | Reduces saturation while retaining semantic weight and adult technical character. |
| D-010 | One normal card uses one dominant signal color. | Color communicates meaning rather than decoration. |
| D-011 | Canonical master is **16:9, 1920×1080 px, landscape**. | The primary output is a presentation slide; vertical mobile masters are no longer required. |
| D-012 | Pilot 01 has no portrait or mobile adaptation deliverable. | Every slide is composed directly for 16:9 rather than derived from a vertical master. |
| D-013 | Every screen contains **one main idea + one visual mechanism + one dominant signal**. | This is the primary anti-overload rule. |
| D-014 | Default cards preserve **50–75% negative space**, depending on level. | Space carries hierarchy and makes a few forms memorable. |
| D-015 | Geometry is semantic. | Scale, direction, distance, overlap, and containment explain relationships. |
| D-016 | The library uses named components and recipes rather than fixed templates. | Components such as Anchor, Signal, Vector, Cluster, Frame, Node, Loop, Collision, and Pulse form a reusable visual grammar. |
| D-017 | The Prompt DSL is declarative and machine-readable. | Humans and generative agents should describe the same composition using stable vocabulary. |
| D-018 | Markdown is the source of truth; images calibrate the specification. | Rules remain searchable, reviewable, versioned, and suitable for Codex. |
| D-019 | Documentation is bilingual in spirit: Ukrainian explanatory copy with English token/component names. | Matches the publishing audience and technical vocabulary. |
| D-020 | Historical influence is methodological, not stylistic imitation. | Adopt active space, asymmetry, scale, geometric narrative, and semantic color from *Two Squares* without political or propaganda associations. |
| D-021 | No animations or transitions in v0.1. | Current scope is static social and presentation graphics. |
| D-022 | GPT Image 2 uses a **reference-first workflow**. | Reference anchors reduce visual drift across generations. |
| D-023 | Pilot 01 topic is **Agentic Discipline: Superpowers × Compound Engineering**. | It tests comparison, process, framework, checklist, and share-card recipes in one real series. |
| D-024 | Pilot 01 canonical copy lives in `manifest.yaml`. | Raster text must not become the source of truth. |
| D-025 | Only approved references and final assets are committed; drafts are ignored. | Keeps the repository useful to Codex without turning Git history into an uncontrolled image dump. |
| D-026 | Pilot 01 uses the newly selected 16:9 GPT Image 2 Ukrainian/Inter style anchor; all portrait and pixel-font anchors are superseded. | Aligns the shared reference with the landscape-first contract and verified Ukrainian rendering without prematurely locking the final licensed font family. |
| D-027 | Pilot 01 restarts from Task 1 under the 16:9-first contract; previous 4:5 rasters and their review evidence are non-canonical. | The canvas change affects composition, validation, review scale, and release scope, so the pilot must be evaluated as a new landscape series. |
| D-028 | Visual DNA generation uses the three boards in `references/canonical/` as the **primary visual authority**; the Pilot 01 `style-anchor-light.png` is a **secondary execution reference** for 16:9 composition, Ukrainian text fidelity, warm paper, and Quiet spacing. | The user-approved rebaseline restores Modular Technical typography, semantic component grammar, asymmetry, strong Anchor/Plane relationships, and calibrated A/B/C identity that a single quiet slide anchor cannot carry alone. Primary authority governs visual language when the references conflict; the `1920×1080` output contract and the ban on restoring superseded 4:5 Pilot rasters remain locked. |

## Deferred decisions

These remain intentionally open until Pilot 01 validates the foundation:

- exact licensed font families;
- final night-mode token values;
- Analytical Mode for dense charts and tables;
- final icon construction grid;
- full component constraints and compatibility matrix;
- full 50-recipe cookbook;
- long-term storage policy for high-resolution exports and rejected candidates;
- public license and release strategy.
