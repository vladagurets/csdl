# Arsenal Expansion Selection

The selection gate is complete. On 2026-09-03 the user selected the first
recalibrated direction for every recipe:

- `024:v1`
- `025:v1`
- `026:v1`
- `027:v1`
- `028:v1`
- `029:v1`
- `030:v1`
- `031:v1`

`selected.yaml` is the machine-readable decision record. Files under
`selected/` are byte-identical copies of the chosen sources, and
`candidate-hashes.yaml` records both hashes. The selected evidence remains
package-local and unpromoted. Public promotion into new version packages, plus
the final vocabulary decision for `Threshold`, `Trace`, and `Band`, requires a
separate approved objective.

## Review and archive paths

The eight active comparison boards live only in `recalibration/`; the active
overview is `overview.png`. The review builder writes this single set rather
than recreating duplicate root boards or a second overview.

Rejected initial board PNGs are ignored local archive files, with a verified
external local backup. Their committed hashes, prior commit, and retrieval
instructions live in `rejected-initial/`. Selection metadata, review notes,
scores, and all eight selected PNGs remain tracked.
