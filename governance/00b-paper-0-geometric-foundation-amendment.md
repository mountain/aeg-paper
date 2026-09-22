# Authoritative Amendment: Paper 0 as the Geometric Foundation

**Status:** Authoritative amendment  
**Version:** 1.0  
**Date:** 2026-09-22  
**Applies to:** `governance/00-authoritative-scope.md`, `governance/00a-paper-0-amendment.md`,
`governance/01-paper-series-architecture.md`, `AGENTS.md`, and the Paper 0 / Paper I
manuscripts  
**Precedence:** This amendment supersedes `00a-paper-0-amendment.md` §§2--5 and those
ownership rows of `00-authoritative-scope.md` §20 and
`01-paper-series-architecture.md` that concern the objects reassigned in §1.5 below.
Where `00a` forbids Paper 0 to develop affine cocycles, global torsion, continuous
arithmetic flow, the basic hyperbolic model, or contact geometry, that prohibition is
lifted and ownership is reassigned as stated here. Every other restriction of `00`,
`00a`, and `01` remains in force.

---

## 1. Scope revision statement

`governance/00-authoritative-scope.md` §27 permits revision of that document only by an
explicit scope-change task stating seven items. They are stated here for the revised
boundary between Paper 0 and Paper I.

### 1.1 Previous rule

`00a-paper-0-amendment.md` fixes the following boundary.

* §2 made Paper 0 an *elementary prelude*: the two pure comb conventions, the affine
  point-path picture, the ripple-pencil picture, reciprocals, poles, infinity, iterative
  fixed points, elementary matrices, and `Aff(1,K) = Stab(infinity) < PGL_2(K)`.
* §3 made Paper 0 "must not develop as a main theory": the intrinsic dependency-poset
  classification beyond the pure-comb proof; mixed-chirality marked spinal histories;
  the Hecke `q=4` history language; **affine cocycles and global torsion**; **continuous
  affine flow as a full intrinsic theory**; regular-zero rigidity or singular-zero
  classification; **contact geometry, horizontal calculus, or function theory**;
  projective bivaluations, quotient towers, or computational complexity; and a general
  convergence theory for infinite arithmetic expressions.
* §4 kept Paper I as the canonical owner of, among others, affine cocycles, continuous
  flow, the regular AES definitions, the complete homogeneous hyperbolic model, ACS
  torsion, and contact curvature.
* §5 recorded the status `proved with stated hypotheses` for the eight elementary
  Paper 0 items, and recorded four open programmes: a projective arithmetic expression
  space intrinsic to the ripple geometry; quotient-stable path/ripple invariants;
  multi-wire path/ripple semantics; and a general theory of infinite arithmetic
  expressions.

`00-authoritative-scope.md` §20 therefore carried no Paper 0 column, and
`05-mathematical-status.md`, `06-editorial-rules.md`, `07-acceptance-checklist.md`,
`source-inventory.md`, and `AGENTS.md` described a four-paper series.

### 1.2 Proposed new rule

Paper 0 becomes the **canonical geometric foundation of the series**. It develops, with
its own definitions, proofs, examples, and figures:

1. the expansion algebra of arithmetic expressions: left- and right-expanded combs under
   the explicit operand-slot convention, the distributive law as the rewrite that
   relates distinct expansions of one expression, and the mechanization lineage of
   mechanical expansion;
2. the arithmetic expression space (AES) as the space in which addition, subtraction,
   multiplication, and division act as *motions*: the regular-AES axioms, the canonical
   arithmetic frame, the basic hyperbolic model `E_0`, the continuous arithmetic flow,
   and the family of models `E_k` indexed by their number of punctures;
3. the projective dual reading of AES, called **ripple geometry**;
4. the **commutativization** of AES, the accumulative commutative space (ACS), the
   two-history affine cocycles, and the reinterpretation of arithmetic torsion as a
   *tearing* of AES measured against ACS;
5. the **contact structure** of that tearing: the arithmetic contact form, horizontal
   fields, the curvature bracket, and the finite open/closed defect comparison;
6. structural proposals that step outside linear language (manifolds, tangent spaces,
   Lie groups, modules), recorded as proposals and not as theorems;
7. the **holed (punctured) arithmetic expression spaces** and the vocabulary of tearing,
   recorded at the claim statuses of §1.5 and `05b`.

Paper I retains the history layer: sequential trees and marked spinal histories, mirror /
temporal reversal / path inverse, projective evaluation of chronological histories, the
`q=4` Hecke sublanguage, the regular- and singular-zero theory, and the interfaces to
Papers II--IV. Paper I imports the geometric objects of Paper 0 and states them only as
concise restatements needed for its own theorems.

The series architecture is unchanged at the level of arrows:
`Paper 0 -> Paper I -> {Paper II, Paper III}` and `Paper I -> Paper IV`.

### 1.3 Mathematical reason

The objects withdrawn from Paper 0 by `00a` §3 are not an elementary prelude: they form
one connected geometric theory in which each later object is *defined by* the earlier one.

* Arithmetic torsion is not an invariant of the history language alone. In the two-history
  formulation it is a defect between two evaluations that share a scale, and its exact
  value is an `e^{M_*-M}`-weighted area in the commutative charge plane. The ACS is not a
  bookkeeping device added after the geometry; it is the commutativization of the
  non-commutative AES, and the torsion is the obstruction to descending the AES evaluation
  through that commutativization.
* The contact form `da - mu du - lambda a dv` is the local form of the *same* defect. Its
  curvature `[D_u,D_v] = mu lambda d/d a` is the infinitesimal density of that obstruction,
  and non-integrability of the horizontal distribution is exactly the statement that no
  local calibration can make both arithmetic directions simultaneously straight. That is a
  statement about AES, not about a later analytic theory.
* The hyperbolic model `E_0` is where addition and multiplication first transport each
  other's rulers non-trivially. Its frame, metric, curvature, horocyclic coordinates, and
  assignment Laplacian are the model data on which every later claim about AES is tested.
* Separating the model, the flow, the cocycles, the commutativization, and the contact
  form across two papers forces the reader to hold a half-defined object and produces
  exactly the "competing canonical versions" that `AGENTS.md` forbids.

The move therefore preserves mathematical meaning: it relocates a single theory to the
paper that introduces its elementary cases, and leaves the history layer to Paper I.

### 1.4 Papers affected

| Paper | Effect |
|---|---|
| Paper 0 | Absorbs the geometric chapters and appendices listed in §1.5; gains §§7--10 below. |
| Paper I | Loses those chapters; keeps the history, projective-semantics, Hecke, and zero-geometry chapters; gains a short imported interface. |
| Paper II | Its citations of the regular-AES definition, canonical frame, hyperbolic model, and contact model are re-pointed to Paper 0 where the object moved; its mathematical content is unchanged. |
| Paper III | Its citations of the regular-AES definition, the bilateral elementary operators, and the isolated-zero disc are re-pointed where the object moved; no claim is changed. |
| Paper IV | Its two references to affine torsion are re-pointed to Paper 0; no claim is changed. |
| `AGENTS.md`, `README.md`, `governance/README.md`, `source-inventory.md` | Updated to describe a five-paper series. |

### 1.5 Required migration

Migration states follow `00-authoritative-scope.md` §21: material is moved, not silently
deleted; one canonical destination is chosen; Paper I retains only the minimum statement
needed for continuity.

| Source (Paper I) | Destination (Paper 0) | Migration state | Claim treatment |
|---|---|---|---|
| `sections/04-affine-cocycles.tex` | `sections/07-acs-tearing.tex` | `MOVE` | `PRESERVE` |
| `sections/05-affine-flow.tex` | `sections/03-aes-and-motion.tex` | `MOVE` | `PRESERVE` |
| `sections/06-hyperbolic-model.tex` | `sections/03-aes-and-motion.tex` | `MOVE` | `PRESERVE` |
| `sections/08-acs-torsion.tex` | `sections/07-acs-tearing.tex` | `MOVE` | `PRESERVE` |
| `sections/09-contact-curvature.tex` | `sections/08-contact-of-tearing.tex` | `MOVE` | `PRESERVE` |
| `appendices/app-B-affine-cocycles.tex` | `appendices/app-C-affine-cocycles.tex` | `MOVE` | `PRESERVE` |
| `appendices/app-C-hyperbolic-calculations.tex` | `appendices/app-B-hyperbolic-calculations.tex` | `MOVE` | `PRESERVE` |
| `appendices/app-D-acs-contact.tex` | `appendices/app-D-acs-contact.tex` | `MOVE` | `PRESERVE` |
| `sections/02-sequential-histories.tex` | --- | `KEEP` | `PRESERVE` |
| `sections/03-projective-affine.tex` | --- | `KEEP` | `PRESERVE` |
| `sections/07-zero-geometry.tex` | --- | `KEEP` | `PRESERVE` |
| `sections/10-conclusion.tex` | --- | `REWRITE` | `PRESERVE` |
| `sections/01-introduction.tex`, `sections/00-paper-zero-interface.tex` | --- | `REWRITE` | `PRESERVE` |
| `appendices/app-A-conventions.tex`, `appendices/app-E-equality-neutrality.tex` | --- | `KEEP` | `PRESERVE` |

Paper I keeps exactly one imported definition: `def:regular-aes` with its canonical
arithmetic frame, restated concisely and marked as imported from Paper 0. This is the
intentional interface duplication already sanctioned by `00a` §4 for the elementary
matrix table, and it is required because Paper I's zero theorems are stated in terms of
that definition. No other Paper 0 theorem is duplicated in Paper I.

### 1.6 Effect on theorem dependencies

* No proved statement changes its mathematical content, hypotheses, or label by this
  migration. Labels move with their source files, so the moved labels
  (`def:acs`, `thm:torsion-stokes`, `thm:contact-curvature`, `def:regular-aes`,
  `thm:continuous-affine-flow`, `thm:basic-hyperbolic-aes`, `` `prop:affine-cocycle-formulas` ``,
  and the rest of the list in §1.5) now resolve inside Paper 0.
* Paper I acquires a forward dependency on Paper 0 for: the regular-AES definition, the
  canonical arithmetic frame, the basic hyperbolic model, the arithmetic flow, the affine
  cocycles, the ACS, and the contact structure. This is consistent with the architecture
  arrow `Paper 0 -> Paper I`.
* Paper 0 acquires dependencies in the reverse direction only for the sequential-tree
  classification `thm:sequential-tree-classification` and the marked-history layer, which
  remain in Paper I. Paper 0 therefore cites Paper I prospectively and does not restate
  that classification; its own comb statement `prop:p0-combs-unique-order` is deliberately
  weaker, exactly as before.
* Papers II--IV continue to import from the series rather than redefining geometry; the
  re-pointed citations of §1.4 are editorial, not mathematical.

### 1.7 Effect on current drafts

* Paper 0 is rebuilt from 7 sections to 11 sections and from 1 appendix to 4; its title
  and abstract change to match its new role. The earlier paper-0 result set is preserved
  in place (same labels, same proofs) and extended, not replaced.
* Paper I is rebuilt from 10 sections to 5 and from 5 appendices to 2. Every removed
  mathematical statement is retained in Paper 0 at the same label and status.
* Papers II, III, and IV receive citation re-pointing only.
* `AGENTS.md` is updated to describe five papers; its Paper I scope-discipline section is
  extended by an explicit Paper 0 scope-discipline section. `paper-0/AGENTS.md` is
  rewritten accordingly.
* The statuses of every substantial Paper 0 result, including moved ones, are recorded in
  the new register `governance/05b-paper-0-status-register.md`; migration entries are
  recorded in `governance/migration-log.md` and the source map in
  `governance/04-current-to-target-map.md`.

---

## 2. What Paper 0 owns after this amendment

Paper 0 is the canonical source for:

1. left- and right-expanded comb grammars under the `L_k`/`R_k` operand-slot recursion,
   one-hole sections, the opposite-operation correspondence, and the affine/projective
   break at second-slot division;
2. the distributive law as a rewrite between expansions of one expression, and the
   consequent distinction between an expression, its expansions, its induced operator, and
   its value;
3. the regular arithmetic expression space, its eikonal identity, and the canonical
   arithmetic frame;
4. the four arithmetic operations as motions of an AES, including the affine grid moves,
   the Baumslag--Solitar-type relation, and the projective motion of second-slot division;
5. the basic hyperbolic model `E_0` (identified once with Paper I's former notation
   `E_{\mathrm{hyp}}`), its horocyclic coordinates, curvature, and assignment Laplacian;
6. the continuous arithmetic flow and its rectification;
7. the point-path and ripple-pencil readings of one chronological matrix product;
8. the affine cocycles, the relative affine defect, and the discrete two-history
   comparison;
9. the accumulative commutative space (ACS), the direct ACS evaluation formula, the
   weighted torsion--Stokes theorem, and the interpretation of torsion as tearing;
10. the arithmetic contact form, horizontal fields, curvature bracket, finite open and
    closed defects, and the scalar horizontal differential;
11. structural proposals that replace linear language by explicitly non-linear algebraic
    structure, including the process-geometry interface;
12. the holed arithmetic expression spaces `E_k`, their punctures, and the vocabulary of
    tearing.

## 3. What Paper 0 must still not develop

Paper 0 still must not develop as a main theory:

* the intrinsic dependency-poset classification of arbitrary sequential trees
  (`thm:sequential-tree-classification` remains a Paper I result; Paper 0 cites it);
* mixed-chirality marked spinal histories as its main object;
* the Hecke `q=4` history language;
* regular-zero rigidity, singular-zero classification, zero networks, tubes, braids, or
  knot invariants;
* arithmetic holomorphic function theory, boundary-value theory, or spectral theory;
* projective bivaluations, quotient towers, condensation, or computational complexity;
* a general convergence theory for infinite arithmetic expressions;
* any claim that the projective ripple family is a new isomorphism class of geometry, or
  that the contact form forces a compatible complex structure.

## 4. Claim-status policy

Every substantial Paper 0 result carries one of the nine labels of
`00-authoritative-scope.md` §23. The register
`governance/05b-paper-0-status-register.md` is authoritative for Paper 0 and is
maintained together with `05-mathematical-status.md`. Moved results keep the status they
held in Paper I; no moved result is promoted by the move.

Terminology fixed by this amendment:

* `ripple geometry` is a **descriptive name** for the family of conditions obtained by
  pulling output conditions back through a projective arithmetic operator. Its further
  structure is an open programme, recorded in `08-open-questions.md`.
* `tearing` is a **structural proposal**: a name for the two-history defect of AES
  evaluation read against the commutativized ACS, whose exact value is the proved weighted
  area of `thm:torsion-stokes` and whose infinitesimal density is the proved curvature
  `mu lambda` of `thm:contact-curvature`.
* `holed arithmetic expression space` is a **descriptive definition** for a punctured AES
  whose punctures are its declared singular points; the verified instance remains the
  isolated-zero disc, and the impossibility statements imported from the exploration
  register keep the status `computationally verified example`.

## 5. Required repository changes

1. `paper-0/aeg-paper-0.tex` remains the canonical entry point and `./build.sh 0` the
   canonical build; the artifact remains `paper-0/aeg-paper-0.pdf`.
2. `paper-1/aeg-paper-1.tex` remains the Paper I entry point.
3. `AGENTS.md` describes five papers and carries an explicit Paper 0 scope section.
4. `README.md`, `governance/README.md`, and `source-inventory.md` list Paper 0 first.
5. `governance/migration-log.md` records one migration entry per moved chapter and
   appendix; `governance/04-current-to-target-map.md` records the migration state of every
   listed source block.
6. `governance/paper-0-closure-report.md` receives a dated post-closure section recording
   this amendment; the earlier dated records are not edited.
7. `bibliography/aeg-paper.bib` gains only citations that are actually used, with primary
   references for any historical or technical comparison.

## 6. Recorded conflicts

Following `AGENTS.md` ("Do not reconcile conflicting sources silently"), the following
conflicts exist and are recorded rather than hidden:

* **C-10.** Before this amendment, `AGENTS.md` and `governance/README.md` described a
  four-paper series while `00a` inserted a fifth. This amendment updates those files and
  states the five-paper series once, in one place.
* **C-11.** `00-authoritative-scope.md` §20 allocates "basic hyperbolic model", "torsion",
  and "contact connection" to Paper I. This amendment reassigns those rows to Paper 0 and
  is the higher-priority source for them; the §20 table is not otherwise revised.
* **C-1 (pre-existing).** The historical labels `E_0` and `E_1` are used inconsistently in
  `notes/`. Paper 0 adopts the correspondence table of §7 below and identifies `E_0` with
  the former `E_{\mathrm{hyp}}` exactly once. No note is edited by this amendment.

## 7. Model-name correspondence table

Required by `06-editorial-rules.md` §28 and §89 before any model-name edit.

| Label | Meaning after this amendment | Former names |
|---|---|---|
| `E_0` | basic **regular** hyperbolic model on the upper half-plane, no puncture | `E_0` (Paper 0), `E_{\mathrm{hyp}}(\mu,\lambda)` (Paper I), "zeroth-kind model", `E_1` in `notes/analysis-and-calculus/04-hyperoperation.md` (inverted usage, recorded as C-1) |
| `E_1` | the **once-punctured** disc model: the unit disc with the isolated zero at the centre removed from the regular locus | "isolated-zero disc" (Paper I §7), `E_1` in some `notes/` sources |
| `E_k` | descriptive family label: an AES with `k` declared punctures; **not** a settled classification | historical `E_k` research label (Paper III README) |
| `E_{\log}` | reserved historical label, **not** defined by this amendment | historical `E_{\log}` research label |

`E_k` and `E_{\log}` remain historical research labels. This amendment defines no
classification by `k`; it fixes the meaning of `E_0` and `E_1` only, and uses `E_k`
descriptively.
