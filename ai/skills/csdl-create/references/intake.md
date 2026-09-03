# Intake and clarification

## Goal

Convert unstructured slide context into one user-approved content contract before any raster generation.

## Analyze first

For each proposed slide, identify:

| Field | Meaning |
|---|---|
| Role | Why this slide exists in the sequence |
| Claim | One proposition the viewer should retain |
| Evidence | Source, data, example, quotation, or explicitly user-supplied premise |
| Exact copy | Every string allowed to appear in the raster |
| Recipe | Repository Recipe selected from explanatory intent |
| Visualization objective | The relationship or transformation all candidates must explain, without fixing one shared mechanism or layout skeleton |
| Level | A, B, or C according to the series rhythm |
| Risk | Unverified claim, dense copy, unclear term, or conflicting instruction |

Distinguish facts from user preferences and hypotheses. Do not treat confident wording as verified evidence.

## Present the proposed brief

Use a compact table:

| # | Role and takeaway | Proposed exact copy | Evidence/source | Recipe / level | Open issue |
|---|---|---|---|---|---|

Keep copy publication-ready but label every agent-authored line as proposed until the user approves it.

## Propose count and rhythm

Honor an explicit user slide count. When it is absent, propose the smallest coherent sequence instead of padding the story to seven slides.

Use the expression levels as narrative intensity, not as a length schema:

- `A` — quiet explanation, orientation, or connective tissue;
- `B` — constructive structure, comparison, system, or transformation;
- `C` — rare dominant culmination or final promise.

The canonical seven-slide default remains `A, A, B, A, B, A, C`. For other lengths, design the rhythm around the story and show it for approval. Typical starting proposals are:

- three slides: `A, B, C`;
- five slides: `A, A, B, A, C`;
- seven slides: `A, A, B, A, B, A, C`;
- longer sets: use mostly A/B progression, reserve C for genuine section or final peaks, and avoid mechanically repeating the seven-slide sequence.

These are proposals, not validator invariants. The approved manifest rhythm is authoritative.

## Ask a consolidated round

Ask only questions that change the output. Prefer five or fewer grouped questions. Cover:

1. **Identity:** Confirm the proposed pilot ID and kebab-case topic slug.
2. **Audience:** Who will view the slides, in what setting, and in which editorial language?
3. **Copy authority:** Which wording is immutable, and may the agent edit or shorten the rest?
4. **Evidence:** Which claims, numbers, quotations, brands, or examples need supplied sources? May user-provided premises be labeled as such?
5. **Narrative approval:** Confirm or correct the proposed slide order, transitions, final promise, and exact-copy table.

If the user already answered an item, restate the inferred answer and ask for confirmation rather than asking them to repeat it.

## Approval gate

Do not generate candidates until the user explicitly approves the normalized brief. Approval can be concise, but it must cover:

- sequence and slide count;
- A/B/C rhythm with exactly one level per slide;
- exact visible copy;
- factual/evidence basis;
- language and audience;
- pilot ID and topic slug.

After approval, treat `manifest.yaml` as immutable copy authority. Any later copy change requires a visible manifest edit and a new exact-copy review.
