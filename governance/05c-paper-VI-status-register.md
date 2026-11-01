# Paper VI Status Register

**File:** `governance/05c-paper-VI-status-register.md`
**Status:** Authoritative for Paper VI
**Version:** 1.1
**Date:** 2026-11-01
**Depends on:**

* `AGENTS.md`
* `governance/00e-paper-VI-process-geometry-scope.md`
* `governance/05-mathematical-status.md` (shared vocabulary; extended below)
* `paper-6/`

**Applies to:** Mathematical and provenance claims of Paper VI.

**Vocabulary.** Paper VI uses the labels of `05` (`PROVED`,
`PROVED WITH STATED HYPOTHESES`, `COMPUTATIONALLY VERIFIED EXAMPLE`,
`STRUCTURAL PROPOSAL`, `CONJECTURE`, `OPEN PROBLEM`) and labels specific to its
imported sources and its definitions:

* `IMPORTED CLASSICAL` — an external theorem used with attribution.
* `IMPORTED TECHNICAL` — a statement of a companion technical report at a
  declared revision, reproducible only as that report states; not a theorem of
  this paper and not `CLASSICAL`.
* `DEFINITION` — an object or construction fixed by the paper, not a claim.
* `CONSTRUCTION` — an explicit construction whose identities are checked.
* `CORRESPONDENCE` — a stated alignment between two structures with cited
  evidence; not a theorem and not an identification.

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
| PVI-6 | `PROVED` (finite obstruction) | No-go 4.3: the normalized Laplacian of the Hasse diagram of the down-set lattice `O(P)` cannot carry the planar statistic `k(t)` = number of left leaves, the statistic the shift note and its verifier compute; with four leaves (three internal vertices) four trees share the normalized spectrum `(0, 0.1464, 0.5, 0.8536)` with different `k`. Whether the source's traversal index equals `k(t)` on every tree is open (`OQ-100.2`). Planarity obstruction. |
| PVI-7 | `COMPUTATIONALLY VERIFIED EXAMPLE` | Calibration 4.6: the relations `C^4 = S`, `J_cl^4 = id`, `[J_cl,S] = 0`, `M^2 = id` are exact identities of the definitions and are replayed on a finite range by `research/iota-carousel/verify_planar.py`, which reproduces `evidence-planar-v1.json`. `S` is a unilateral shift, so `C` is not invertible (semigroup action). The identification of `C` with the source's carousel is a proposal, not part of this row. The doubled screw construction `H_iota = diag(H,H)` is `PROVED` for its block form and replayed by `verify_shift.py`. |
| PVI-8 | `STRUCTURAL PROPOSAL` | The arity-one principle (slot order induced by the carrier) and the reading of the carousel as the planar screw. Named mechanisms with supporting calibrations; not theorems. |
| PVI-9 | `PROVED` | Theorem 5.2 (`thm:sequential-recovery`): the single-spine fragment of the dictionary is an object-level equivalence (a bijection compatible with concatenation of one-hole contexts) between free histories and chain programs, up to the slot convention. Bounded histories keep the initial mark outside the map; the branching case is excluded. |
| PVI-10 | `CONJECTURE` | Conjecture 5.3: a natural general assignment from plane trees with planar schedule structure to open finite programs, restricting to PVI-9 on the sequential fragment. Unproved; see `OQ-100.1`. |
| PVI-11 | `OPEN` | The dictionary rows "one-hole contexts as compiled observations" and "charge as frontier data"; the three full program-side acceptance tests (a first restricted example is PVI-12); presentation and objectification scope (`OQ-100.7`, `OQ-100.8`). |
| PVI-12 | `COMPUTATIONALLY VERIFIED EXAMPLE` | `research/program-side-fixtures/`: one fixed three-context free spine, slots `(1,2,1)`, multiplication by -1 represented by native `neg` with checked call/graft signature data. At `mountain/adva@87a1a6933bca3fdb5c176cbf612729e278d172f7`, one schedule and inversion count 3 agree with the tree. Literal constants instead give six events and fifteen schedules; forgetting constants is a 15-to-1 projection. Native replay, source-bound reception, a separate combinatorial oracle and refusal controls are stored. Only the declared two-context signature is tested; no general assignment, full 193-tree native census, carrier check or theorem promotion. OQ-100.7 remains OPEN. |

**Boundary note.** The paper is a draft whose content is partly programme. A reader
must not infer a general equivalence from PVI-9, a general carrier claim from PVI-7,
or a canonical carousel correspondence from PVI-5.
