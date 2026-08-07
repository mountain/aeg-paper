# Paper II Closure Report

**Manuscript:** *Arithmetic Expression Geometry II: Hyperbolic Real Function Theory*

**Status:** Mathematical-review manuscript

**Closure date:** 2026-08-06

**Audited baseline:** `61ff60d`

This report records the result of the Paper II writing and restructuring task.  It
should be read with `paper-II-source-audit.md`, `decisions-paper-II.md`,
`source-inventory.md`, `migration-log.md`, and `audit-report.md`.  “Closed” below
means closed at the hypotheses and operator domains printed in the mathematical-review
manuscript.  It does not mean that the remaining analytic programme or public-release
work is complete.

**Post-closure notice:** Section 9 records the later regular-pullback integration
and Section 10 records the M-0006 interface rebuild.  Sections 1--8 retain the
original eight-section, 39-page closure evidence.

## 1. Acceptance outcome

- **Source and dependency closure:** closed.  The active entry point contains eight
  sections and three appendices and imports Paper I by citation and restatement.  No
  legacy, alternative-revision, note, Paper III, or Paper IV source is an active TeX
  dependency.
- **Mathematical closure:** closed for P2-D1--P2-D2 and P2-T1--P2-T9.  The manuscript
  separates the intrinsic surface theory from the normalized contact-CR theory,
  declares measures and domains, and proves the basic-model boundary results it
  advertises.
- **Claim-status and provenance closure:** closed.  Migration M-0003 records every
  migrated source family and treatment; status change S-0006 records the authorized
  theorem promotion; the remaining questions are explicitly retained as open.
- **Editorial and rendered closure:** closed for mathematical review.  The abstract,
  introduction, theorem statements, comparison table, conclusion, appendices, and
  bibliography are traceable to the proved body results and were visually inspected.
- **Release status:** not an author-approved public release.  Author metadata,
  clean-container verification, DOI/version policy, and final publication judgment
  remain human release actions.

## 2. Theorem inventory

| Node | Result | Active location | Closure |
|---|---|---|---|
| P2-D1 / P2-T1 | regular-AES analytic data, frame adjoints, energy, and Laplace--Beltrami drift | Section 2; Appendix A | defined / proved |
| P2-T2 | intrinsic arithmetic CR operator, gauge law, exact factorizations, and holomorphic implies harmonic | Section 3; Appendix A | proved |
| P2-D2 / P2-T3 | normalized contact analytic data, contact adjoints, variational sub-Laplacian, Friedrichs realization, and bracket generation | Section 4; Appendix B | defined / proved |
| P2-T4 | raw and adjoint/Reeb contact-CR twists and logarithmic CR fields | Section 4; Appendix B | proved with branch hypotheses |
| P2-T5 | finite filtered affine--Appell modules and finite upward sweep | Section 4; Appendix B | proved; no basis or completeness claim |
| P2-T6 | exact arithmetic-frame and hyperbolic Laplacian comparison | Section 5; Appendices A and C | proved |
| P2-T7 | transported Poisson kernel and compactified `C_0` Dirichlet theorem | Section 6; Appendix C | proved with stated boundary class |
| P2-T8 | Fourier multiplier, variational conormal, energy identity, and minimization | Section 7; Appendix C | proved on the stated Schwartz/Sobolev classes |
| P2-T9 | rational, Fourier, assignment-only harmonic, harmonic-measure, and contact-CR families | Sections 4 and 7; Appendices B and C | proved with stated domains |

The paper does not identify the raw contact sum of squares with the variational
sub-Laplacian, or the contact-CR twisted equation with surface harmonicity.  It does
not promote the affine--Appell family to a Hilbert or Schauder basis.

## 3. Mathematical decisions closed

The Paper II decision record fixes the following release-relevant distinctions:

1. surface fields `X_u,X_v` and contact lifts `D_u,D_v` live on different analytic
   carriers;
2. the divergence-of-gradient sign makes `-Delta_g` and `-Delta_C` the nonnegative
   energy operators;
3. Riemannian area and positive contact volume force the displayed first-order drift
   terms;
4. formal test-function identities, pointwise differential consequences, and closed
   Friedrichs operators are stated on separate domains;
5. surface arithmetic holomorphicity is a unitary gauge of ordinary oriented-surface
   holomorphicity, while contact CR factorization has a Reeb/curvature twist;
6. the global model uses `X=(lambda/mu)x`, with every original-coordinate Poisson and
   conormal scale shown explicitly;
7. the decisive uniqueness class is continuous data on the conformal compactification,
   with `C_0(R)` denoting zero value at its ideal point;
8. explicit solution families are claims of construction, not mode completeness.

## 4. Build and static validation

The repository command `./build.sh 2` executes the strict sequence

```text
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-2.tex
bibtex aeg-paper-2
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-2.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-2.tex
```

A cold build after deleting Paper II's generated auxiliaries succeeded.  The task
runner can expose an overlay race when repeatedly replacing the same generated
binary, so the verified complete PDF was promoted by an atomic rename after the
four stages completed.  This affects only artifact materialization, not the source or
the repository build procedure.

Final artifact:

| Property | Value |
|---|---:|
| PDF | `paper-2/aeg-paper-2.pdf` |
| Pages | 39 |
| Page size | US letter, 612 x 792 pt |
| PDF version | 1.5 |
| File size | 463,026 bytes |
| SHA-256 | `489d21841f56e4a84f9c9179b804c4e6d2207d23c8367d98e00215829fb7bab3` |

Static checks:

- 198 labels and 198 unique labels;
- 83 unique `ref`, `eqref`, `pageref`, or `autoref` targets, all present;
- 4 citation keys, all present in the then-root shared bibliography;
- no control character or unresolved TODO/FIXME marker in the active TeX source;
- no LaTeX or BibTeX warning, undefined reference or citation, fatal diagnostic,
  overfull box, or underfull box in the final logs;
- `git diff --check` passes.

## 5. Rendered review

The final 39-page artifact was rendered with Poppler.  Every page was included in
four contact-sheet passes, followed by full-page inspection of the title and abstract,
introduction and analytic-branch figure, surface/contact transition, contact gauge,
hyperbolic coordinate transition, Poisson uniqueness proof, explicit assignment
families, conclusion, both calculation appendices, and bibliography.  No clipping,
collision, unreadable figure label, malformed equation, blank content page, or broken
page transition was found.

## 6. Independent review record

Three separate read-only review tracks covered:

- surface-frame divergence, adjoints, Laplace drift, unitary gauge, raw/exact/adjoint
  CR factorizations, and the closed Dirichlet realization;
- contact volume and divergences, raw and Reeb-twisted products, balanced measure,
  logarithmic first integrals, affine--Appell filtration, Poisson and Fourier scales,
  energy constants, and explicit assignment-dependent fields;
- whole-manuscript mathematical consistency, source provenance, Paper I dependency,
  required-topic coverage, and exclusion of Paper III/IV theorem claims.

The reviews initially found one blocking overstatement: the conclusion described a
complete finite-energy trace-space identification although the body proves the exact
identity for Poisson extensions and completion from Schwartz data.  The conclusion
was narrowed to that proved statement.  All other findings concerned domain wording,
normalization transparency, terminology, or provenance and were repaired.  Final
review disposition: no blocking mathematical, scope, or provenance defect.

## 7. Deliberately open frontier

The closure does not include general Green kernels on regular AESs, spectral
completeness, a contact-boundary representation theorem, continuation across singular
AES points, multi-zero/tube topology, projective condensation, or computational
complexity.  These remain open or assigned to Papers III--IV exactly as recorded in
the status and architecture files.

## 8. Remaining human release actions

Before treating Paper II as a public release candidate, an author should:

1. build the submitted commit in a clean checkout and with the retained Dockerfile;
2. approve author, affiliation, date, title, subtitle, and version metadata;
3. decide the DOI/version relationship between Papers I and II and earlier archives;
4. review the draft pull request and authorize any non-draft release state.

## 9. Post-closure regular-pullback amendment (2026-08-06)

This amendment records the analytic part of the arithmetic--automorphic integration.
It supersedes only the original active-section count and artifact metadata: Paper II
now has nine sections and three appendices because
`sections/05-pullback-cylinder.tex` has been added between the contact layer and the
basic hyperbolic model.  The 39-page table in Section 4 remains the evidence for the
original closure run and is not silently relabelled as the current artifact.

| Extension node | Active statement | Status and boundary |
|---|---|---|
| P2-A1 | The planar assignment `A_phi(w)=Im(e^{-i phi}w)` with its printed conformal metric is a harmonic regular AES and satisfies the stated curvature law | proved by direct calculation; `mu != 0` |
| P2-A2 | The logarithmic cylinder with metric `|dW/W|^2` and the hyperbolic-sine assignment is a complete flat regular AES with zero circle `|W|=1` | proved, including the linear `lambda=0` limit |
| P2-A3 | A holomorphic local biholomorphism pulls either regular target back to a regular AES | proved only where the derivative is nonzero and all required branches are chosen |

The same section proves unitary and inversion descent for the cylindrical metric and
zero circle.  Inversion reverses the assignment, so quotient descent is either to an
index-two scalar cover or to the associated real sign line bundle.  The printed
square-root/Cayley formula converts an automorphic interval into the unit-circle
preimage, but Paper II does not infer a global graph type from that formula.

Critical points, degenerate pullback metrics, algebraic branch points, cone
completion, zeros or poles of the cylindrical coordinate, Hauptmodul ramification,
and singular zero networks remain outside the Paper II theorem.  They are passed in
one direction to Paper III.  Likewise, functorial analytic pullback does not prove
that the pulling map is generated naturally by an arithmetic history.

The planar, cylindrical, pullback, and descent calculations are `REDERIVED HERE`;
no historical `E_log` formula is promoted.  The final unified repository build
produced the amended Paper II artifact with the following current evidence:

| Property | Current integration artifact |
|---|---:|
| Pages | 44 |
| File size | 497,142 bytes |
| SHA-256 | `a7f76c6c834ac20fb6ee1780366fe819b1a0e0802d6d6facdfd4e49d152d9592` |
| Active labels | 227 unique |
| Citation keys used | 4 unique |

The final log has no LaTeX or package warning, undefined reference or citation,
overfull or underfull box, duplicate label, or fatal diagnostic.  This table
supersedes only the artifact metadata for the active integration snapshot; the
original 39-page closure evidence above remains a historical record.

## 10. M-0006 interface rebuild (2026-08-06)

Paper II receives no new theorem or source file in M-0006.  Its conclusion now
states the realized downstream boundary more precisely: Paper III uses the
cylindrical pullback and sign descent to build the singular q=4 carrier, but the
hyperbolic unit-tangent knot theory is a separate three-dimensional construction.
Paper II still proves neither cone completion nor a knot theorem.

The unified repository build after that interface edit produced:

| Property | M-0006 integration artifact |
|---|---:|
| Pages | 44 |
| File size | 497,273 bytes |
| SHA-256 | `751af9456607741da051e22c39c126cce280c2a4427fe88750d3023e7eb7fc04` |
| Active labels | 227 unique |
| Reference targets | 97 unique, all present |
| Citation keys used | 4 unique, all present |

The canonical log and BibTeX log contain no warning, undefined reference or
citation, overfull or underfull box, or fatal diagnostic.  The three conclusion
pages were rendered and visually checked without a layout defect.
