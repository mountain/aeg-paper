# Paper VI Status Register

**File:** `governance/05c-paper-VI-status-register.md`
**Status:** Authoritative for Paper VI
**Version:** 1.0
**Date:** 2026-11-01
**Depends on:**

* `AGENTS.md`
* `governance/00e-paper-VI-process-geometry-scope.md`
* `governance/05-mathematical-status.md` (shared vocabulary; extended below)
* `paper-6/`

**Applies to:** Mathematical and provenance claims of Paper VI.

**Vocabulary.** Paper VI uses the labels of `05` (`PROVED`,
`PROVED WITH STATED HYPOTHESES`, `COMPUTATIONALLY VERIFIED EXAMPLE`,
`STRUCTURAL PROPOSAL`, `CONJECTURE`, `OPEN PROBLEM`) and two labels specific to
its imported sources:

* `IMPORTED CLASSICAL` — an external theorem used with attribution.
* `IMPORTED TECHNICAL` — a statement of a companion technical report at a
  declared revision, reproducible only as that report states; not a theorem of
  this paper and not `CLASSICAL`.

---

## Paper VI process-geometry integration (2026-11-01)

Canonical source: `paper-6/`. Scope:
`governance/00e-paper-VI-process-geometry-scope.md`. Open questions: `OQ-100`.
This section registers the claim statuses of the new paper. It does not promote,
weaken, or redefine any claim of Papers 0--V, and no proved node of those papers
may depend on it.

| ID | Status | Statement and boundary |
|---|---|---|
| PVI-1 | `IMPORTED TECHNICAL` | The native open program, the three readings K/C/F, and the exact slice laws are imported from the Adva technical report `docs/TECHNICAL_REPORT_PROGRAM_PROCESS_CORE.md` at `mountain/adva` commit `1b9bd090`, with the mathematical core of `mountain/process-geometry` at commit `c47c96fa`; both are pinned in `research/process-representation-gap/reports/manifest-baseline.md`. Import is not proof of a new theorem and is not `CLASSICAL`. |
| PVI-2 | `PROVED` | Proposition 2.7 (`prop:sequential-leaf`): free marked spinal histories are exactly open finite programs with one hole and a chain body, up to the declared slot convention. A bounded history keeps its initial mark `x_0` as an extra datum outside the correspondence. Sequential-only; no branching claim. |
| PVI-3 | `PROVED` | Theorem 3.6 (`thm:canonical-order`): for every plane binary tree, the left-first postorder is the unique linear extension of the dependency order minimizing inversions against the corner order. Proof: induction on the tree with the parent/block decomposition. |
| PVI-4 | `COMPUTATIONALLY VERIFIED EXAMPLE` | Calibration 3.9: the canonical order is checked on all plane binary trees with 3–6 internal vertices, equivalently 4–7 leaves (193 trees) by `research/iota-carousel/verify_canonical_choice.py`. Evidence for the implementation, not for the theorem. |
| PVI-5 | `PROVED` (correspondence record) | Proposition 4.2: the strong form "carousel class-cycle = J" is false; the surviving alignment is non-canonical (3 planes × 2 orientations) and the `SR` entry with the index shift have no `J` counterpart. The plane/sign part is imported from Paper V; the carrier identities are replayed by `research/iota-carousel/verify_omega.py`, while the six plane/orientation candidates are enumerated by hand in the alignment note, not by that script. Negative calibration, not a positivity claim. |
| PVI-6 | `PROVED` (finite obstruction) | No-go 4.3: the cut Laplacian cannot carry the planar statistic `k(t)` = number of left leaves, the statistic the shift note and its verifier compute; four trees at `n = 4` share one cut-graph spectrum with different `k`. Whether the source's traversal index equals `k(t)` on every tree is open (`OQ-100.2`). Planarity obstruction. |
| PVI-7 | `COMPUTATIONALLY VERIFIED EXAMPLE` | Calibration 4.6: the planar screw module satisfies `C^4 = S`, `J^4 = id`, `[J,S] = 0`, `M^2 = id` on the declared finite range (`research/iota-carousel/verify_planar.py`). The reading of the module as *the* carrier is a proposal, not part of this row. |
| PVI-8 | `STRUCTURAL PROPOSAL` | The arity-one principle (slot order induced by the carrier) and the reading of the carousel as the planar screw. Named mechanisms with supporting calibrations; not theorems. |
| PVI-9 | `PROVED` | Theorem 5.2 (`thm:sequential-recovery`): the single-spine fragment of the dictionary is an object-level equivalence (a bijection compatible with concatenation of one-hole contexts) between free histories and chain programs, up to the slot convention. Bounded histories keep the initial mark outside the map; the branching case is excluded. |
| PVI-10 | `CONJECTURE` | Conjecture 5.3: a natural general assignment from plane trees with planar schedule structure to open finite programs, restricting to PVI-9 on the sequential fragment. Unproved; see `OQ-100.1`. |
| PVI-11 | `OPEN` | The dictionary rows "one-hole contexts as compiled observations" and "charge as frontier data"; the three program-side acceptance fixtures; presentation and objectification scope (`OQ-100.7`, `OQ-100.8`). |

**Boundary note.** The paper is a draft whose content is partly programme. A reader
must not infer a general equivalence from PVI-9, a general carrier claim from PVI-7,
or a canonical carousel correspondence from PVI-5.
