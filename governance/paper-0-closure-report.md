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

---

## 11. Post-closure extension (2026-09-22, late): OI-4 and OI-1 resolved

This dated section is appended; nothing above is edited.

**What was open.**  The response to the review left two items at the top of its
list: OI-4, replace the "commutativization" heuristic by a history group with
declared relations and verify that the charge map descends; and OI-1, attach AES
data to the four-circle configuration and prove non-extendability at the origin.
Both are now settled, and both are recorded in migration M-0021.

**OI-4 (§8).**  Histories are taken to form the group
`G = (R,+) * (R,+)` generated by the additive and multiplicative step families,
with relations imposed only within each family.  The charge endpoint and the
evaluation are then homomorphisms `c: G -> R^2` and `nu: G -> Aff^+(1,R)`, both
onto; `c` is the abelianization of `G` (so the ACS endpoint *is* `G_ab = R^2`,
using the standard fact `(F*H)_ab = F_ab + H_ab`); and the descent question has an
asymmetric answer: the multiplicative charge factors through `nu`, namely as
`log` of the linear part, while the additive charge provably does not, witnessed
by `h(p,q) = M_q A_p M_{-q} A_{-e^{-q}p}`, which evaluates to the identity motion
and carries additive charge `p(1-e^{-q}) != 0`.  Three consequences are stated in
the paper: the ACS is the commutativization of the *history language* and not of
the motion group; what it retains beyond its abelianized endpoint is the charge
*path*; and the two failure directions (equal motion with different charges, equal
charges with different motions) are dual, each measured in the ACS.

**OI-1 (§11).**  The four-circle configuration is realized as the zero locus of an
explicit punctured AES.  With `P` the union polynomial, the assignment is `a = P`
on a punctured disc of radius `r < rho`, and the metric is the one the eikonal
identity forces, `g = |grad a|^2 (dx^2+dy^2)/(mu^2+lambda^2 a^2)`.  The critical
set of `P` is computed exactly --- on that disc it is only the origin --- so `g`
is a smooth Riemannian metric and the model is regular; the factorization of `P`
shows that its zero locus is exactly the four circles; non-extendability at the
origin follows from the new lemma that a regular AES has no critical point of its
assignment; and the metric is incomplete with the puncture at finite distance
(along the axes the length element is `O(|x|^5)`, so the axis length from `eps` to
the puncture behaves as `4 eps^6`).  The zero locus therefore has four branches
meeting exactly at the puncture, which is the concrete form of the interface
Paper I predicts: branching in the zero set is possible only where the regular
structure or its completeness fails.

**Build.**  `./build.sh 0` produces a 78-page PDF with a clean final log.

**Remaining open items.**  OI-2 (comparison of tearing across a puncture), OI-3
(canonical puncture sets), OI-5 (intrinsic ripple geometry), OI-6 (frame
independence of `mu*lambda` under a declared horizontal metric), and the new
OQ-087 (generalization to `k` punctures and to motion-generated assignments).

---

## 12. Post-closure extension (2026-09-22, third revision): OI-6 and OI-3 resolved

This dated section is appended; nothing above is edited.  Both items are recorded
in migration M-0022.

**OI-6 (§9).**  The question was whether the curvature coefficient `mu*lambda` is
frame-independent once a horizontal metric is declared.  The answer has two
halves, and they concern different invariance groups.  On the contact side, the
bracket defect of the horizontal distribution defines a canonical 2-form `omega`
on the distribution by `[X,Y] = omega(X,Y) d_a mod D`; it is determined by the
distribution and the charge projection, is insensitive to the normalization of
`alpha`, and its value on the `h`-orthonormal oriented frame is `mu*lambda`, with
the explicit rescaling law `rho^{-2}` when `h` is replaced by `rho^2 h`.  On the
arithmetic side the same number is the chart-free expression
`d_a([X_u,X_v]) = mu*lambda`.  So the coefficient is not a contact invariant --- a
general contact transformation need not preserve `h` --- but neither is it a gauge
artifact; the paper now names its exact invariance group and its residual freedom
(the choice of `(mu,lambda)`, which is part of the AES data).

**OI-3 (§11).**  The question was whether the puncture set can be canonical.  For
punctured spaces whose assignment extends smoothly to the ambient surface the
answer is yes, and exactly: `S` is the critical set of the assignment.  One
inclusion uses the template metric to extend the regular structure across any
non-critical point, contradicting local essentiality; the other reads the eikonal
identity at a critical point of the punctured part and obtains `0 >= mu^2 > 0`.
Three consequences are now in the paper: the four-circle model's puncture is
forced rather than stipulated; the number of punctures equals the number of
critical points of the assignment, so the `k`-puncture problem becomes a problem
about functions with `k` critical points; and the disc model imported from
Paper I is a different species, because there the *assignment* is what fails at the
puncture (it is not `C^1`), so the theorem does not apply and that case is
reopened as OQ-088.

**Build.**  `./build.sh 0` produces an 80-page PDF with a clean final log.

**Remaining open items.**  OI-2 (tearing across a puncture), OI-5 (intrinsic
ripple geometry), OQ-087 (generalization of the four-circle model), and the new
OQ-088 (canonical punctures when the assignment does not extend).

---

## 13. Post-closure extension (2026-09-22, fourth revision): OI-2 resolved

This dated section is appended; nothing above is edited.  The work is recorded in
migration M-0023 and closes OQ-089.

**The question.**  On a punctured space a comparison of two motions may have to be
performed around a puncture rather than through it.  Is the relative torsion then
measured by an ACS area, by a holonomy of a loop around the puncture, or by
neither?

**The answer.**  By the ACS area, in every model; there is no canonical holonomy
of a puncture in the AES data; and what puncturing changes is only whether the
comparison can also be performed on the surface.  Three propositions carry this.

* `prop:p0-tearing-puncture-independent`: `tau` is a function of the two words
  alone, so puncturing, changing the model, or changing the realisation leaves it
  unchanged, and the area formula of `thm:torsion-stokes` applies verbatim.
* `prop:p0-surface-does-not-close`: in *any* regular AES the two orderings of a
  rectangle end at points whose assignments differ by
  `mu*h*(e^{lambda k}-1) != 0`; the two flow paths therefore bound no region of
  the surface, so the comparison always has to leave the surface.  The ACS is
  accordingly the canonical comparison rather than a device for avoiding holes.
* `prop:p0-no-puncture-holonomy`: the horizontal structure determined by the
  assignment is the level-set foliation, which is integrable and hence flat; a
  curved connection requires data beyond the AES (the contact model, whose
  curvature form is canonical relative to the added charge projection); and in
  models with canonical punctures the assignment is single-valued, so no loop
  around a puncture can have a monodromy.

**The puncture's local geometry.**  `prop:p0-puncture-local-picture` computes it in
the model of `thm:p0-four-circle-model`: a circle of radius below `rho` meets the
zero locus in exactly eight points and the assignment changes sign at each; the
punctured disc splits into eight sectors, four positive and four negative, the
negative ones being the cusps `|y| < x^2/(2 rho)` and `|x| < y^2/(2 rho)` along
the coordinate axes; `g` is conformal to the Euclidean metric with a factor
vanishing at the puncture, so the conformal class extends although the metric
does not, which is why the angles at the puncture agree with the tangent cone; and
the puncture lies at finite `g`-distance, so the model is incomplete there.

**Correction recorded.**  A draft of that proposition asserted that the four zero
branches merely touch the origin, which is false: the computation shows sign
changes and the negative cusps.  The corrected statement was verified numerically
before being written up.

**Build.**  `./build.sh 0` produces an 82-page PDF with a clean final log.

**Remaining open items.**  OI-5 (intrinsic ripple geometry), OQ-087
(generalization of the four-circle model), and OQ-088 (canonical punctures and
surface comparisons when the assignment does not extend).
