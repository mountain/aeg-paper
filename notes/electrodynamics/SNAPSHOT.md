# Snapshot register

This directory is an archived copy, not a canonical source.

- **Copied from:** `/Users/mingli/work/public/electrodynamics/` (workspace copy,
  outside this repository).
- **Copied on:** 2026-11-06.
- **Fidelity:** verbatim, byte for byte (`diff -r`, excluding `.DS_Store`, which
  was not copied because it is ignored by this repository). 56 files, ~1.2 MB.
  This register is the only file added by the copy.
- **Ignored by git:** `inserts/build-paper0-integrated.log` and
  `inserts/build-paper4-integrated.log` match `*.log` in `.gitignore` and are
  therefore on disk but not tracked. 54 of the 56 files are trackable.

## What the copy contains

Three strands of work share the working directory that was copied, and they have
different status.

1. **Electrodynamics manuscript** (`tex/`, `inserts/`, `verify-notes.py`,
   `verification-report.txt`, the five Chinese source notes
   `费曼图.md`/`勒让德形式.md`/`电动力学讨论-0{1,2,3}.md`, and `README.md`).
   The mathematical parts of this strand are already integrated in Papers 0 and
   IV as Subsection 4.4 (`paper-0/sections/04b-pole-covariance.tex`) and
   Subsection 4.8 (`paper-4/sections/04b-transport-density.tex`); the physical
   readings are conditional on five declared dictionary hypotheses and exist
   only in `tex/aeg-electrodynamics.pdf`.  The canonical copies of the two
   inserted subsections are in the papers, not here.
2. **Paper I capping and interface-disk work** (`pants-v2-qed/` ...
   `pants-v7-translation/`, `pant-vs-feynman-01.md`,
   `pants-v2-qed-baseline-v1.json`, `tools/check-aeg-numbering.py`,
   `formal-drift/`).  Partly overlapping material already tracked in this
   repository: `research/pants-interface-disks/`, `research/capping-scope/`,
   `research/formal-inventory-drift/`, and
   `notes/analysis-and-calculus/25-pants-interface-disks-and-substitution.md`.
   The V4--V7 worked examples and the numbering tool are not tracked anywhere
   else.  See the collision note below before reading a `V<k>` label.
3. **`BRANCH-COLLISION-2026-11-01.md`**, a collision report written before the
   merge of PR #21.

## Naming collision: two different `V2`, two different `V3`

The `V<k>` numbers in the copied `pants-v*` directories are **not** the version
numbers used by `research/pants-interface-disks/` in this repository.  The two
sequences are adjacent but distinct pieces of work:

| label | in this copy | tracked upstream |
|---|---|---|
| V2 | `pants-v2-qed/` --- "V2-QED: applying the OQ-096 V1 checker to electron--positron annihilation wiring", 2026-10-31 | `research/pants-interface-disks/v2/` --- "OQ-096 V2: same value, different source, and reopening under finite observation", 2026-11-02 |
| V3 | `pants-v3-marking/` --- "V3: the marking layer --- generating side surfaces from a DAG", 2026-10-31 | `research/pants-interface-disks/v3/` --- "OQ-096 V3: three-block composition, strict domains, and residual counterexamples", 2026-11-05 |
| V4--V7 | `pants-v4-kernel/`, `pants-v5-labels/`, `pants-v6-interface/`, `pants-v7-translation/` | none |

So a statement that reads "V2" in this directory and a statement that reads "V2"
under `research/pants-interface-disks/` are statements about different
experiments.  Neither sequence supersedes the other, and no number here should
be read as an index into that directory.

## Known staleness

The printed statement numbers cited in the `pants-v*` documents and in
`tools/check-aeg-numbering.py` were taken **before** PR #21 (`fc61fbc`,
"tunnel handles, pierced caps and annular Stokes balance") was merged into
`main`.  That merge did land, so Paper I's chapter-10 numbers shifted after the
snapshot: the collision report predicted, for example, Corollary 10.14 becoming
about 10.21.  **Do not read a number in this directory as the current number of
a statement in `paper-1/`.**  The tool's `CITED` table is the single place to
re-derive the mapping (`--shift-table`).

The two `research/oq096-v2-equal-value-sources` and
`research/oq096-v3-three-block-composition` branches that carry the upstream V2
and V3 sequences were fetched on 2026-11-06 and are not part of this copy.

`formal-drift/drift-summary.json` is byte-identical to
`research/formal-inventory-drift/drift-summary.json`, while the `README.md` and
the diagnose script differ between the two locations; the tracked versions under
`research/` should be treated as canonical.

## Status

Historical or exploratory material, under the same rule as the rest of
`notes/`: it is not a canonical paper source, and its presence here does not
promote any statement.  The manuscript PDF in `tex/` is a rendered artefact of
the snapshot, not a released version.
