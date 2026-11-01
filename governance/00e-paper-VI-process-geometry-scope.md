# Authoritative Scope: Paper VI — Process Geometry

**Status:** Authoritative scope specification (new paper, not an amendment of
Papers 0--V)
**Version:** 1.0
**Date:** 2026-11-01
**Applies to:** `paper-6/`; and the rows of `README.md` and
`01-paper-series-architecture.md` that describe the series after Paper V. Those
files are authoritative for Papers 0--IV (and `00c` for Paper V), so this file
governs Paper VI until they are extended.
**Precedence:** Within the territory listed in §2 this file outranks research
notes. It does not supersede any statement of `00`, `00a`, `00b`, `00c` or `01`
about Papers 0--V, and it grants Paper VI no right to redefine their objects.

---

## 1. Why a seventh paper exists

Papers 0--V develop arithmetic expression geometry from syntax to geometry,
analysis, singularity, condensation, and triadic characteristics. Every one of
them treats a *sequence of operations* as the primitive history: Paper I restricts
its histories to sequential trees, and Paper V's carrier is the endpoint of that
line rather than a theory of programs.

Current research has produced a second native formalism that none of Papers 0--V
owns:

* **Process Geometry** (`mountain/process-geometry`, `docs/MATHEMATICAL_CORE.md`,
  `docs/THEORY_MAP.md`): a process-first library whose native object is an open,
  finite, typed program with ordered holes, retained construction history, and
  three coupled readings (construction, causality, frontier), together with
  presentations, quotients and objectification.
* The **carousel/iota thread** (`notes/analysis-and-calculus/26`--`40`,
  `research/iota-carousel/`, `research/donaghey-orbits/`): the arity-one iota
  carrier, the planar screw module `C^4 = S`, the carousel correspondence, and the
  canonical evaluation order for arbitrary plane binary trees.
* The **process-representation gap** experiments
  (`research/process-representation-gap/`), which compare declared process
  representations with task-sufficient presentations at pinned source revisions.

The unifying observation is that the arity-one iota induces an order on slots, so
the spine and the left/right comb orders of an arithmetic expression are a special
case of a process order on an open program. The programme of this paper is to state
that general theory and to make the equivalence with arithmetic expression geometry
precise.

Paper VI is therefore a **new slot**, not an amendment: it imports the objects of
Papers I and V and the process corpus, and it owns the general theory that neither
paper claims.

## 2. What Paper VI owns

Paper VI may define and develop the following as its own main theory.

### 2.1 Native program processes

* open finite programs: typed expression DAGs with ordered holes, explicit source
  and occurrence identity, explicit copy and discard, retained construction
  history;
* the three readings K (construction and substitution), C (causal development),
  F (cut and frontier), and the statement that they are readings of one process;
* evaluation schedules as linear extensions of the construction order, as opposed
  to the order itself;
* slices, cut linkage, and the invariance of an outer slice under schedule choice.

### 2.2 The arity-one carrier and evaluation order

* the arity-one principle: the iota carrier acts at one slot and therefore induces
  a slot order, from which the spine and the left/right comb orders are recovered;
* plane binary trees and their corner order, dependency posets, and linear
  extensions;
* the canonical evaluation order: the unique linear extension minimizing
  inversions against the corner order (left-first postorder), with its proof for
  arbitrary trees and its finite calibration;
* the relation of this order to mark histories, mirror/reversal, and Donaghey-type
  tree transforms, as bounded statements only.

### 2.3 The carousel correspondence

* the carousel's class-level four-cycle and its order-two count shadow;
* the iota complex unit `J`, the three aspect--opposite-relation planes, and the
  chirality sign law imported from Paper V;
* the planar screw module `V = V_class ⊗ V_index` with `C^4 = S`, its status as a
  finite calibration, and the obstruction that the cut Laplacian does not carry the
  index;
* the alignment and its limits: the strong form "carousel = J" is refuted, and the
  surviving correspondence is stated at exactly the strength established.

### 2.4 The arithmetic--process dictionary and the equivalence

* a typed dictionary between arithmetic expression objects (expression tree,
  marked spinal history, operator, charge) and process objects (program body,
  schedule, reading, frontier);
* the equivalence statements that the dictionary supports, each with its claim
  status: proved, conditionally proved, computationally verified example,
  structural proposal, or open;
* the exact scope of the equivalence: which AEG statements are recovered as the
  sequential (single-spine) special case, and which process statements have no AEG
  counterpart yet.

## 3. What Paper VI must not develop

* the foundational objects of Papers 0--V: arithmetic expression spaces, motions,
  cocycles, contact structure, projective semantics, zero geometry, hyperbolic
  function theory, condensation, triadic characteristics, or apertures;
* a claim that the equivalence is proved beyond the status registered for it;
* the engineering corpus of Process Geometry as mathematics: the Rust kernel,
  CLI, packages, fixtures and API commitments are cited sources, not theorems;
* a general complexity, hardness, or decidability claim derived from the
  correspondence;
* promotion of Pushkarev--Byzov, Donaghey or any other external result beyond its
  classical status;
* redefinition of Paper I's sequential histories or Paper V's carrier; the paper
  imports them by citation.

## 4. Relation to the earlier papers

The dependency is one-way:

```text
Paper 0 (expression-space and charge vocabulary) --+
Paper I (marked spinal histories, mirror/reversal) --+--> Paper VI
Paper V (six-state carrier, iota, chirality sign law) -+    (program processes, evaluation order,
                                                             carousel correspondence, equivalence)
```

Paper VI may state results about the sequential case by citing Paper I, about the
carrier by citing Paper V, and about the expression spaces and charge vocabulary by
citing Paper 0. It may not prove new claims inside their scope,
and it may not be used as a dependency of any proved node in Papers 0--V.

## 5. Source corpus and status

Admitted sources, in the order of precedence:

1. this scope file and the governance records;
2. `paper-6/` itself;
3. AEG research notes `notes/analysis-and-calculus/26`--`40`
   (Donaghey, mirror/reversal, PPCT lattice, carousel and iota, canonical choice);
4. `research/iota-carousel/` and `research/donaghey-orbits/` evidence and
   verifiers;
5. `research/process-representation-gap/` reports and proposals, at their pinned
   revisions;
6. Process Geometry's `docs/MATHEMATICAL_CORE.md`, `docs/THEORY_MAP.md` and
   `docs/RESEARCH_STATUS.md` at a declared revision;
7. the Adva research notes admitted by `00c` (0001--0127) and, for the process
   material only, later notes cited by hash;
8. external classical sources: Donaghey (1980), Pushkarev--Byzov (2014), and
   standard order/lattice references.

Notes and pinned checkouts are evidence, not authority. A statement enters the
manuscript only with a status label, and every imported external theorem keeps its
classical attribution.

## 6. Claim status and honesty requirements

Paper VI uses the vocabulary of `governance/05c-paper-VI-status-register.md`:
`PROVED`, `PROVED WITH STATED HYPOTHESES`, `COMPUTATIONALLY VERIFIED EXAMPLE`,
`STRUCTURAL PROPOSAL`, `CONJECTURE`, `OPEN PROBLEM`, and the imported-source
labels `IMPORTED CLASSICAL` and `IMPORTED TECHNICAL`.

* A finite calibration is never promoted to a theorem.
* An alignment that is non-canonical is stated as non-canonical.
* The equivalence is stated at the strength currently supported; its open
  directions are listed as open problems, not as consequences.
* Every imported Process Geometry statement names its revision; a drift is a
  boundary, not a licence.

## 7. Deliverables and acceptance

Paper VI is a manuscript at `paper-6/aeg-paper-6.tex`, built by
`./build.sh 6`, with:

* an introduction and programme;
* the native process carrier and the arity-one principle;
* evaluation orders and the canonical order theorem;
* the carousel correspondence and the screw carrier;
* the arithmetic--process dictionary and the equivalence statement;
* a boundaries section listing the open problems with their dependencies;
* a bibliography and a claim ledger.

A draft may state sections as programme rather than as proved theory, provided
every claim carries its status. Acceptance as a reviewable manuscript requires
that no open problem is presented as solved and that every finite claim names its
verifier.
