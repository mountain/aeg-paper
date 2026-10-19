# P-AEG-1 — draft governance record (aeg-paper)

**Status: PROPOSAL. Not applied. Requires governance review.**

Target: `governance/process-representation-gap-2026-10-10.md`
Precedent: `governance/opposite-feature-witness-2026-10-09.md` (PR 16)

Every number below is reproduced from `research/process-representation-gap/`;
the citations are re-checked on every run by
`tools/build_interface_promotion.py` and the SHA-256 of each cited evidence file
is recorded in `evidence/interface-promotion.json`.

---

## Draft

```markdown
# Process-representation gap: six declared experiments and a pinned-source
# continuation gap

Date: 2026-10-10.  Status: independent finite research record and mathematical
boundary record.  Baseline: aeg-paper `735695cbc7ce512a1cd5e188577613eda4b3083c`.
No existing frozen evidence or manuscript theorem is changed.

## Sources and authority

Pinned repositories: `mountain/adva` at `cce73004c2b4fbfb87d9ba1ccc66820423273cf6`
and `1b9bd090b2c4710916b6a0ccca0ad88fb7d323bd`; `mountain/process-geometry` at
`c47c96fa79123c677172278be59d67ca1cc891b1`.  Six commits and thirty files are
frozen by Git blob and SHA-256 in `research/process-representation-gap/evidence/manifest.json`,
read from object stores rather than working trees.

Full research record: `research/process-representation-gap/`.

## Status rows

| ID | Status | Statement and boundary |
|---|---|---|
| PRG-S1 | `COMPUTATIONALLY VERIFIED EXAMPLE` | On 115 reachable words of a declared three-mechanism typed model, the PR-16 three-scalar readout `(c+v, f-h, 3h/f)` has 17 classes with a largest fibre of 26, and is neither task-sufficient nor closed-update. The readout of a word over `{compute, verify}` is a function of the event count alone. |
| PRG-S2 | `PROVED WITH STATED HYPOTHESES` | On the declared domain, the shortest continuation distinguishing `ccv` from `cvc` has length 1; the two share the readout `(3,1,2)`, the counts `(2,1,0)` and the legal-action set. Proof in the canonical research record. |
| PRG-S3 | `COMPUTATIONALLY VERIFIED EXAMPLE` | Of 63 declared one-field extensions of the incidence summary, exactly one -- the exact accumulator -- is both sufficient and closed-update, at 26.0 mean bytes per history against 40.3 for the literal word, and it survives a reserved held-out family of 751 words not used to select it. |
| PRG-S4 | `COMPUTATIONALLY VERIFIED EXAMPLE` | On 16648 typed open bodies, the initial-filling summary has 341 classes and 232 separating fibres, and 0 of 63 declared bounded candidates are sufficient. |
| PRG-S5 | `COMPUTATIONALLY VERIFIED EXAMPLE` | Across four observation layers of the 5461 crossing words of length at most 6, free reduction merges 4004 and the Artin quotient a further 880, leaving 577 braid elements and 6 endpoint permutations. |
| PRG-S6 | `COMPUTATIONALLY VERIFIED EXAMPLE` | A stable object can pass the interface and exact-descent gates and still fail task sufficiency; the Artin object passes all three gates and is a quotient, not a new rank. |
| PRG-S7 | `PROVED WITH STATED HYPOTHESES` | The pinned Adva source supplies no native legal-continuation interface for a `FrameRelationPathV0` or a `RelationCellV0`: the cell exposes only `new`, `check` and `transport`; `transport` refuses an open filling; `check_braid` fixes exactly three steps; ADR 0022 rejects frame-id reuse for iteration; PSC0 excludes recursion, cyclic substitution and stable feedback. |
| PRG-F1 | `OPEN PROBLEM` | No general theorem follows from any row above. Every count is inside a declared domain and budget. |

## Attribution corrections

The three-scalar body `y1 = c+v`, `y2 = f-h`, `y3 = 3h/f` is defined by this
repository's PR-16 script `paper-4/scripts/verify-opposite-features.py`. It is a
declared scalar adapter and is **not** an Adva output and **not** a research-0114
output; 0114's own coordinates are time, space and construction. The string
occurs zero times in the pinned Adva tree, verified directly.

`PR-16` is an aeg-paper identifier; it does not occur in the pinned Adva tree.

Neither correction weakens PR-16 or PIV-S8/PIV-S9.

## Relation to existing status

This record adds rows and closes nothing.  In particular PIV-F2 is unchanged:
`chi_T` and `chi_S` still have only two-record sample consistency, and no
spectral operator closure, truth-fiber or cyclic-update semantics is supplied.
No theorem, label, notation or frozen audit is altered.
```

---

## Why this is the minimal change

It is a new file plus additive status rows. It follows the PR-16 precedent
exactly, changes no LaTeX source, and therefore triggers no build obligation
beyond what already runs. It does not update
`governance/05-mathematical-status.md` in place; if the maintainer prefers the
rows there instead, the same content moves without change of meaning.

## Regression condition

`tools/build_interface_promotion.py` re-reads every cited verdict and compares
it with the value this proposal depends on, and records the SHA-256 of each
cited evidence file. A changed verdict or a changed hash fails the build.
