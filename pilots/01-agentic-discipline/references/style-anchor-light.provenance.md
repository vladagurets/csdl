# Style Anchor Light — 16:9 Provenance

**Status:** Approved canonical reference for the 16:9 Pilot 01 restart
**Generation route:** built-in Codex `$imagegen`, GPT Image 2
**Selected candidate:** `style-anchor-light-v2.png`
**Source dimensions/mode:** `1672×941`, RGB
**Canonical dimensions/mode:** `1920×1080`, RGB
**Source SHA-256:** `85afc72a0d556fb84b4296db8e1c07e8dc1043fa685a3834a789bf613e4fa9e6`
**Canonical SHA-256:** `6c8504246745d77efe19749e77d51d2cd1d1db26b004975298215bd395311c2a`

## Candidate review

- `style-anchor-light-v1.png` — rejected: the oversized headline and supporting copy make the calibration feel denser and more poster-like than the Quiet Modular default.
- `style-anchor-light-v2.png` — selected: strongest balance of restrained Inter-style hierarchy, generous landscape space, one clear left-to-right Vector, and one semantic coral Signal.
- `style-anchor-light-v3.png` — rejected: heavier condensed display treatment creates unnecessary visual pressure and weakens the quiet default.

## Exact-copy review

Observed text matches the prompt exactly:

```text
ТИХА МОДУЛЬНІСТЬ
ОДНА ІДЕЯ.
ОДИН СИГНАЛ.
```

No additional labels, logo, footer, or UI chrome are visible.

## Normalization

All three GPT Image 2 sources were `1672×941` RGB PNGs composed directly for landscape. Each was resized mechanically with macOS `sips` to `1920×1080`; no crop, redraw, recolor, text edit, or compositional change was applied. The source/canonical aspect-ratio difference is below 0.1%.

## Review result

- full-resolution `1920×1080`: pass;
- `1280×720` landscape readability: pass;
- exact Ukrainian Unicode text: pass;
- one coral Signal and one functional Vector: pass;
- ≥65% perceived negative space: pass;
- prohibited typography and decoration: absent.
