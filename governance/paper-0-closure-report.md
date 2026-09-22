# Paper 0 Implementation and Build Report

**Status:** Branch closure report  
**Date:** 2026-08-09  
**Branch:** `paper-0-path-ripple-pencil`  
**Draft PR:** `#14`  
**Validated manuscript head:** `7fd8a44719adcab53684ffcdaa6e7b04bb73b130`

## 1. Files changed

The branch adds the canonical Paper 0 source closure, local instructions, an
authoritative architecture amendment, a source audit, and a build workflow. It
also adds a Paper 0 interface to Paper I, transfers the elementary grid and
Baumslag--Solitar exposition from Paper I to Paper 0, updates the root overview,
and extends `build.sh` with target `0`.

The canonical Paper 0 TeX closure is:

```text
paper-0/aeg-paper-0.tex
paper-0/sections/01-introduction.tex
paper-0/sections/02-two-combs.tex
paper-0/sections/03-paths.tex
paper-0/sections/04-ripple-pencils.tex
paper-0/sections/05-reciprocals-fixed-points.tex
paper-0/sections/06-projective-unification.tex
paper-0/sections/07-interface.tex
paper-0/appendices/app-A-calculations.tex
```

Paper I changes are confined to:

```text
paper-1/aeg-paper-1.tex
paper-1/sections/00-paper-zero-interface.tex
paper-1/sections/06-hyperbolic-model.tex
paper-1/appendices/app-C-hyperbolic-calculations.tex
```

The marked spinal history definitions and terminology are unchanged.

## 2. Mathematical claims added

Paper 0 proves, with the hypotheses stated in the manuscript:

1. unique internal evaluation order for the explicit left- and right-expanded
   comb grammars;
2. the opposite-operation correspondence between the two pure combs;
3. the elementary slot-dependent matrix table and the affine/projective break
   caused by second-slot division;
4. the zeroth-kind upper-half-plane assignment identity and the point-path
   realization of affine prefix evaluation;
5. the line/circle formula for Möbius pullbacks of horizontal horocycles, with
   common tangency at the operator pole;
6. the covariant point-path / contravariant ripple-pencil reading of one prefix
   matrix;
7. finite geometric-series formulas, analytic and formal convergence under
   explicit hypotheses, affine fixed-point iteration, and reciprocal
   continued-fraction fixed-point formulas;
8. the relationship between the pole of `1/(1-r)`, escape of a finite fixed
   point, and the parabolic fixed point at infinity;
9. projective unification through `Aff(1,K)=Stab(infinity)` and generation of
   `PGL_2(K)` by translations, nonzero scalings, and inversion.

The geometric-series discussion now distinguishes the degenerate parameter
`r=0`: the update is constant and has a singular matrix, so it has a finite
fixed point but is not an element of `PGL_2`.

No claim of a new projective metric or a completed projective AES is added.

## 3. Material relocated in expository ownership

Paper 0 becomes the canonical source for:

- the elementary pure left/right comb comparison;
- the historical point-path picture in the zeroth-kind grid;
- the assignment-compatible grid maps and their elementary
  Baumslag--Solitar-type relation;
- inversion as a curved horocycle/ripple pencil;
- reciprocal--pole--infinity and elementary fixed-point discussion;
- the introductory matrix synthesis.

Paper I no longer contains the full arithmetic-grid figure or the detailed
metric-pullback and Baumslag--Solitar calculations. It retains the group-derived
metric, the complete basic hyperbolic AES theorem, horocyclic coordinates,
curvature, completeness, Laplacian, zero geometry, and a concise interface back
to Paper 0.

Paper I also retains the marked spinal history terminology and definitions, the
intrinsic sequential-tree classification, mixed chirality, chronological
projective evaluation, the Hecke interface, affine flow, zero rigidity, ACS
torsion, and contact curvature.

## 4. Assumptions made explicit

- division remains partial in ordinary arithmetic;
- projective continuation does not repair an inadmissible intermediate step;
- the ripple-circle theorem uses a real Möbius lift of positive determinant;
- geometric-series convergence uses `|r|<1` over `R` or `C`, while the formal
  identity lives in `K[[r]]`;
- the affine matrix description requires nonzero scale; the zero-scale update
  is treated separately as a degenerate constant map;
- an algebraic fixed point is not asserted to be attracting without a
  multiplier hypothesis;
- infinite continued fractions are assigned values only after convergence is
  established;
- `E_0` is identified with Paper I's canonical homogeneous hyperbolic model,
  not introduced as a competing definition.

## 5. Unresolved mathematical issues

The following remain open:

- an intrinsic projective arithmetic expression space carrying ripple data;
- quotient-stable or history-natural invariants derived from path/ripple
  geometry;
- a multi-wire extension;
- a general theory of formal, analytic, projective, and operational convergence
  for infinite arithmetic expressions;
- incorporation of further PCRG material after that repository is available to
  the connected source index.

## 6. Build result

GitHub Actions workflow **Paper 0 and Paper I build**, run `#13`
(`31301595247`), completed successfully at the validated manuscript head above.

The workflow:

- built `paper-0/aeg-paper-0.pdf`;
- built the revised `paper-1/aeg-paper-1.pdf`;
- found no undefined control sequences, unresolved references or citations, or
  multiply defined labels under its warning check;
- uploaded both PDFs as artifact `aeg-foundational-papers`.

The generated PDFs contain 23 pages for Paper 0 and 61 pages for Paper I. PDF
preflight found both files openable, unencrypted, and text-based. Visual review
covered the Paper 0 title, comb, point-path, ripple-pencil, reciprocal/fixed-point,
and projective-unification pages, together with the revised Paper I title,
Paper 0 prelude, transferred hyperbolic-model section, and final references.
No clipped text, overlap, broken glyphs, or missing figures were observed.

## 7. Remaining warnings

No blocking LaTeX warning remains. Ordinary typography warnings not covered by
the CI grep were not observed to cause clipping or overlap in the rendered
pages. The manuscripts remain drafts and need mathematical review beyond build
correctness.

## 8. Recommended next task

Review Paper 0 section by section for mathematical emphasis, especially:

1. whether the geometric-series example is the best elementary bridge from
   reciprocal to infinity;
2. whether the ripple pencil should be presented first through inversion or
   through a general pole-centered coordinate;
3. how much of Paper I's repeated elementary projective matrix material should
   remain for self-containment after Paper 0 is accepted;
4. whether the missing PCRG source contributes a distinct elementary theorem or
   only parallel terminology once it becomes accessible.

---

## 9. Post-closure amendment (2026-09-22): Paper 0 as the geometric foundation

This dated section is appended; nothing above is edited.

**Authority:** `governance/00b-paper-0-geometric-foundation-amendment.md`
(authoritative amendment, v1.0), issued as an explicit scope-change task under
`00-authoritative-scope.md` §27.  It supersedes `00a-paper-0-amendment.md`
§§2--5 and reassigns the ownership rows of `00-authoritative-scope.md` §20 that
concern affine cocycles, continuous affine flow, the basic hyperbolic model, ACS
torsion, and contact curvature from Paper I to Paper 0.

**What changed.**  Paper 0 was rebuilt from 7 sections and 1 appendix to 12
sections and 4 appendices.  It absorbed Paper I's geometric chapters and
appendices (affine cocycles, affine flow, the hyperbolic model, ACS torsion,
contact curvature, and the affine/hyperbolic/ACS-contact appendices) at the same
labels and statuses, and it gained five new chapters or parts: the
distributive-expansion material, the model-label convention `E_0`/`E_1`/`E_k`,
the tearing definition, the two obstructions to linear language with the
process-geometry proposals, and the punctured-space chapter with its six
computed witnesses.  Paper I was reduced to the history, projective-semantics,
Hecke, and zero-geometry layers, with one imported definition (the regular AES
and its canonical frame) retained for logical self-containment.

**Statuses.**  Every substantial Paper 0 result is registered in the new file
`governance/05b-paper-0-status-register.md`.  No moved result was promoted.  The
new material is registered as `PROVED` for the two distribution identities and
the two §10 obstructions, `PROVED` for the tangent-cone proposition, and
`STRUCTURAL PROPOSAL` for the names *ripple geometry*, *tearing*, and the model
label convention.  The six §11 witnesses are `COMPUTATIONALLY VERIFIED EXAMPLE`,
and the interpretive reading of them is registered as `UNSUPPORTED AND EXCLUDED`
for use as a claim.

**Provenance.**  Migration M-0019 in `governance/migration-log.md` records the
source and destination of every moved file.  The exploration register behind
§11 is retained as
`notes/foundations-and-geometry/06-hole-obstructions-ledger.md` (a tracked copy,
with a non-authoritative header) and cited as `Yuan2026AEGHoleRegister`; the
working original under `temp/` was not edited.  Two precision defects of that
register --- its "five classes" wording against a six-row table, and its
unproved identification of a `Z_3` monodromy with a `Z_4` twist --- are recorded
in Paper 0 §11 and in `08-open-questions.md` rather than silently repaired.

**Build.**  `./build.sh 0` produces a 67-page PDF with a clean final log;
`./build.sh 1` produces a clean Paper I log; the CI warning gate passes on both.
Papers II, III, and IV were rebuilt after their citations of moved objects were
re-pointed to Paper 0, and all three logs are clean.

**Remaining warnings and open items.**  No blocking LaTeX warning remains.  The
mathematical open items are listed in Paper 0 §11.6 and §12.4 and in
`08-open-questions.md` (OQ-079--OQ-082).  Paper 0 remains a draft under
mathematical review.

---

## 10. Post-closure revision (2026-09-22, evening): response to the external review

This dated section is appended; nothing above is edited.

**Input.**  `AEG-Paper-0-review-2026-09-22-v0.1.md` (reviewer: ChatGPT; reviewed
artifact SHA-256 `afeff197…f3f5e5b`, the 68-page version produced earlier the same
day).  The point-by-point disposition is
`AEG-Paper-0-review-2026-09-22-response-v0.1.md`.

**What changed.**  Four defects were repaired and are recorded in migration
M-0020: the punctured-space definition was vacuous for nonempty puncture sets and
now gives an ambient surface and a finite set first; the proof of the
infinite-dimensionality of the arithmetic generators used an invalid step and now
iterates `ad_A` on `P`; the pole chart `1/(z−q)` has negative determinant and was
replaced by `−1/(z−q)` with a warning on negative-determinant prefixes; and the
frame witness mis-counted directed transitions (three per orbit, four times each;
six only over both orbits).  One over-statement was narrowed: the
infinite-dimensional algebra excludes a finite-dimensional Lie-group *action*, not
a finite-dimensional manifold, and the faithful affine matrix representation is
recorded alongside.  One hypothesis was made explicit: tearing is a scalar defect
for scale-compatible pairs and equals the ACS area only for charge-compatible
pairs.  The four-circle tangent cone is no longer coupled to punctures, and the
interpretive claims of §11.3 became registered questions (OQ-085, OQ-086).

**What was added.**  `prop:p0-contact-quotient`: the basic hyperbolic model is the
Reeb quotient of the contact model, by five exact relations, with proofs.  The
comparison was proposed in the review; each relation was re-derived independently
here before being adopted.  Also added: a warning on partial motions in §3, a
remark fixing the Möbius chart `Z = (λ/μ)x + iy`, a remark stating what `μλ` is and
is not, and an explicit statement in §12 that §§10--11 are research reports rather
than stable interfaces.

**What was removed.**  The register's calibration round counts (11 and 56) are no
longer quoted as facts: an independent reimplementation of the same model gave 10
and 55, so the counts depend on an update step the register does not fix.  The
paper now states the residual functions, their exact zero, and the proved halting
bound `|θ−π/2| < 5ε/8 + O(ε²)` instead.

**Build.**  `./build.sh 0` produces a 74-page PDF with a clean final log.  Papers
I--IV were rebuilt against the extended bibliography and their logs are clean.

**Status.**  The register `05b` was updated: `prop:p0-arithmetic-generators` and
`prop:p0-characters-cannot-see-tearing` keep the status `PROVED` with narrowed
statements, `prop:p0-contact-quotient` is `PROVED` for the basic model,
`def:p0-punctured-aes` is `PROVED` after repair, the observer witness is `PROVED`
for the bound with the register's numbers marked as not reproduced, and the
four-circle construction and the history-monoid question are `OPEN PROBLEM`.
