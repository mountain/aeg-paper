# Paper I Calculus and Capping Amendment

**File:** `governance/00d-paper-I-calculus-and-capping-amendment.md`
**Status:** Authoritative scope amendment (revises `00-authoritative-scope.md` §27
procedure; supersedes the Paper I / Paper 0 boundary where stated)
**Version:** 1.0
**Date:** 2026-10-31
**Depends on:** `governance/00-authoritative-scope.md`, `governance/00b-paper-0-geometric-foundation-amendment.md`, `governance/02-paper-I-outline.md`

---

## 1. Previous rule

Per `00-authoritative-scope.md` (and `AGENTS.md` Paper I / Paper 0 scope
discipline):

* **Paper 0** owns the geometric foundation: arithmetic expression spaces and
  their motions, the basic hyperbolic model `E_0`, the punctured model `E_1`,
  the accumulative commutative space (ACS), the affine cocycles and
  torsion–Stokes theorem, the contact structure with curvature `μλ`, and the
  punctured/compactification chapters (§§11–12).
* **Paper I** owns the sequential syntax, marked spinal histories, projective
  semantics, the affine/Borel sector, the Hecke `q=4` sublanguage, and the
  regular/singular zero geometry. It must **not** develop the analysis
  (differential/integral/series), the order topology, or the hole–cap geometry.

---

## 2. Proposed new rule

**Paper I is upgraded to a self-contained combined volume**, titled
*AEG I: Foundations of History Calculus and Hole–Cap Geometry*, with nine
sections and four appendices. It absorbs, as its own theorems (at the statuses
recorded in the Integration Audit Matrix of
`temp/paper_1_detailed_writing_plan.md` §4):

1. the Scott–Lawson order topology of sequential and branching histories
   (notes `09`–`16`, OQ-091–094);
2. the analysis three pillars — differential (smoothing Lie functor, minimal
   DAG defects, graded horizontal calculus), integral (mixed affine
   integration, dual adjoint pairing, 1-cocycles, holographic Stokes), and
   series (free Lie algebra Magnus expansion, arity–cell correspondence,
   PBW abelianization) — built on the history/DAG layer (notes `02`–`03`,
   `17`–`24`, OQ-095);
3. the hole–cap fine geometry (fivefold hole taxonomy, ball-and-tube
   thickening, hole–disk complementarity, constant-boundary capping
   obstruction, certified sealing) (note `25`, OQ-096);
4. a **self-contained restatement** of Paper 0's §8 (ACS, torsion–Stokes),
   §9 (contact form, horizontal fields, curvature `μλ`), §11 (punctured AES),
   and §12 (compactification/collar descent), so that Paper I is readable
   without Paper 0's later half.

**Paper 0** retains its §§1–7 (expression expansions, arithmetic motions,
hyperbolic/punctured models, the four operations as motions, the dual reading,
commutativization, tearing) as the geometric source; its §§8–9, §§11–12 become
the canonical upstream whose results Paper I restates with the same labels.

---

## 3. Mathematical reason

The analysis pillars are built on the **history/DAG layer** (the down-set
dcpo, the linear-extension graph, the free Lie algebra of the generators) —
which is Paper I's core object — rather than on the geometric foundation
alone. The Scott–Lawson order topology supplies the domain theory without
which "continuity of evaluation" has no carrier; the contact curvature `μλ`
is the order defect of the minimal branching DAG `{add, multiply}`; and the
hole–cap geometry is the geometric companion of the down-set lattice
`O(P)` (its maximal chains are the spinal histories). Splitting these across
two papers fragments one logical spine.

---

## 4. Papers affected

* **Paper 0** — §§8–9, §§11–12 become cited upstream; §§1–7 unchanged.
* **Paper I** — expands from 6 sections + 2 appendices to 9 sections + 4
  appendices.

---

## 5. Required migration

* Paper 0's `thm:torsion-stokes`, `eq:arithmetic-contact-form`,
  `eq:horizontal-arithmetic-fields`, `thm:contact-curvature`,
  `def:p0-punctured-aes`, `def:p0-collar-contract`, `prop:p0-aes-collar-descent`
  are **restated in Paper I** with the same labels (one canonical source per
  result moves to Paper I; Paper 0 cites forward).
* Notes `02`–`03`, `09`–`25` are promoted into Paper I at the grades recorded
  in the Integration Audit Matrix; no `STRUCTURAL PROPOSAL` or
  `COMPUTATIONALLY VERIFIED EXAMPLE` is promoted to `PROVED` without the
  §4 integration audits.

---

## 6. Effect on theorem dependencies

* The contact curvature `μλ`, ACS area formula, and torsion–Stokes now sit in
  Paper I (their downstream consumers are Paper II's harmonic analysis and
  Paper III's tube geometry).
* Paper 0's zero-geometry chapters (§§11–12) keep their dependency on Paper
  I's regular-AES splitting; the arrow reverses for the contact/ACS content.

---

## 7. Effect on current drafts

* `paper-0/aeg-paper-0.tex`: §§8–9, §§11–12 gain a forward pointer "restated
  in Paper I"; source retained but no longer the sole canonical home.
* `paper-1/aeg-paper-1.tex`: `\input` list grows to 9 sections
  (`00`–`09`) + 4 appendices (`app-A`–`app-D`); new files
  `04-differential-theory.tex`, `05-integral-theory.tex`,
  `06-series-theory.tex`, `07-holes-and-zero-geometry.tex`,
  `08-caps-and-interface-disks.tex`, `09-conclusion.tex`, and
  `appendices/app-C-magnus-sympy-verification.tex`,
  `appendices/app-D-pants-cellulation-verification.tex`.

---

**Prepared:** 2026-10-31. This amendment revises the Paper I / Paper 0
boundary; it does not by itself promote any claim. Promotion follows the
Integration Audit Matrix of the writing plan.
