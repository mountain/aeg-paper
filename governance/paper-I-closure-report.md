# Paper I Closure Report

**Manuscript:** *Arithmetic Expression Geometry I: Foundations*  
**Status:** Mathematical-review manuscript  
**Closure date:** 2026-08-06  
**Audited baseline:** `134e70a74ed010024afa7439bd3931402731423a`

This report records the result of the Paper I restructuring task.  It should be read
with `audit-report.md`, `source-inventory.md`, `migration-log.md`, and
`decisions-paper-I.md`.  “Closed” below means closed for the mathematical-review
manuscript at the hypotheses actually printed in the paper.  It does not mean that
Papers II--IV, author release approval, or DOI publication work is complete.

**Post-closure notice:** Section 8 records the later arithmetic--automorphic
integration and Section 9 records the M-0006 interface rebuild; Sections 1--7 retain
the original 60-page closure evidence.

## 1. Acceptance outcome

- **Repository baseline:** closed.  The fixed baseline, alternate manuscript trees,
  historical notes, figures, styles, build scripts, and bibliography were inventoried.
  The unmodified baseline build failure and stale tracked PDF were recorded before the
  build script was changed.
- **Structural migration:** closed.  The active entry point contains ten foundational
  sections and five appendices, and it inputs only the new
  `paper-1/sections/` and `paper-1/appendices/` trees.  No legacy source was deleted.
- **Mathematical closure:** closed for Paper I.  Every named foundational theorem and
  definition slot is present with exact hypotheses; theorem-like results have proofs
  in the active manuscript or a supporting appendix.
- **Editorial closure:** closed for mathematical review.  The 258-word abstract and
  the conclusion were checked against the proved body results; all eight planned
  conceptual figures are present as reproducible TikZ.
- **Release status:** not yet an author-approved release.  Docker was unavailable in
  the task environment, and the author must still approve the affiliation, date,
  version declaration, and relationship to the earlier Zenodo DOI.

## 2. Foundational theorem inventory

| Area | Stable labels | Active source | Closure |
|---|---|---|---|
| Sequential classification and histories | `thm:sequential-tree-classification`, `def:marked-spinal-history` | Section 2 | proved / defined |
| Projective evaluation and generation | `def:projective-evaluation`, `thm:bilateral-pgl2-generation`, `cor:affine-borel-sector` | Section 3; Appendix A | proved / defined |
| Affine cocycles and differentials | `prop:affine-cocycle-formulas`, `prop:target-affine-cocycle`, `prop:source-normalized-cocycle`, `prop:left-right-affine-differentials` | Section 4; Appendices A--B | proved |
| Continuous affine flow and regular AES | `def:regular-aes`, `thm:continuous-affine-flow` | Section 5 | proved / defined |
| Basic hyperbolic model | `thm:basic-hyperbolic-aes`, `prop:laplace-eigenfunction` | Section 6; Appendix C | proved |
| Regular and singular zeros | `thm:regular-zero-locus`, `def:singular-aes`, `prop:regular-total-zero-set` | Section 7; Appendix C | proved / defined |
| ACS and global torsion | `def:acs`, `def:relative-torsion`, `thm:torsion-stokes` | Section 8; Appendix D | proved / defined for positive add--scale histories |
| Contact and horizontal curvature | `prop:contact-form`, `thm:contact-curvature`, `prop:horizontal-differential-curvature` | Section 9; Appendix D | proved |

The dependency-graph aliases for the target-frame and source-normalized cocycles are
attached to the combined cocycle proposition.  Ordinary arithmetic evaluation,
projective evaluation, charge evaluation, endpoint equality, mirror, temporal
reversal, and path inverse remain distinct throughout.

## 3. Mathematical decisions closed

The Part XIV ledger in `08-open-questions.md` closes every Paper I P0 item and the
chapter-blocking P1 items used in this manuscript.  In particular:

1. histories are chronological words, with
   `rho(gamma delta)=rho(delta)rho(gamma)` under column-vector Möbius action;
2. bilateral non-degenerate contexts generate `PGL_2(K)` over every field, while the
   infinity stabilizer is the affine Borel sector;
3. regular AES data are intrinsic eikonal data with a derived arithmetic frame;
4. the hyperbolic model is derived from a normalized left-invariant metric, without a
   uniqueness claim;
5. regular zeros and singular zeros are categorically separated;
6. relative torsion is defined for scale-compatible positive add--scale histories,
   while weighted Stokes requires charge compatibility and the orientation
   `dA wedge dM`;
7. finite target-frame open defect, source-normalized closed drift, and their common
   infinitesimal contact curvature are not identified at finite scale.

## 4. Build and static validation

The strict command sequence encoded by `build.sh` was executed with TeX Live 2023:

```text
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-1.tex
bibtex aeg-paper-1
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-1.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-1.tex
```

The task runner materializes repeated writes to a generated binary at sandbox exit,
so the final evidence run executed the same four stages as separate process
invocations.  This avoids a runner-specific overlay race and does not change the
repository build procedure.

Final artifact:

| Property | Value |
|---|---:|
| PDF | `paper-1/aeg-paper-1.pdf` |
| Pages | 60 |
| Page size | US letter, 612 x 792 pt |
| PDF version | 1.5 |
| File size | 575,584 bytes |
| SHA-256 | `98a8a9a2f35cbb2252cfc9576d447ca427a27f95815deaab03d3e3c9f7c04911` |

Static and rendered checks:

- 166 unique active labels; no duplicate labels;
- every active `ref`, `eqref`, and `autoref` target exists;
- every citation key exists in the shared `bibliography/aeg-paper.bib`;
- every named stable theorem/definition slot is present;
- 8 figure environments, all inline TikZ, with no missing assets;
- no LaTeX or BibTeX warnings, undefined references, undefined citations,
  overfull boxes, or underfull boxes in the final logs;
- no unresolved TODO/FIXME marker in the active manuscript;
- all 60 pages rendered with Poppler; the title/abstract, contents, all eight figure
  pages, appendices, and bibliography were visually inspected for clipping,
  collisions, and unreadable labels.

Docker was not installed in the task environment.  The existing `Dockerfile` was
retained unchanged; container verification remains a release check rather than an
unreported success.

## 5. Independent review record

The integrated manuscript received separate read-only reviews of:

- algebraic chapters and composition/matrix conventions;
- flow, metric, hyperbolic, zero-locus, and singular-model calculations;
- ACS orientation, weighted Stokes, finite defects, and contact curvature;
- whole-manuscript mathematical consistency;
- Paper I scope, abstract/conclusion traceability, and later-paper boundaries;
- rendered PDF layout and conceptual figures.

All blocking findings from those reviews were repaired and rechecked.  The final
mathematical and scope reviews report zero blocking defects.

## 6. Scope preserved for later papers

Paper I does not claim a complete arithmetic-holomorphic function theory, a general
multi-zero or tube classification, braid/knot invariants, the full projective
condensation quotient tower, or computational lower bounds.  Those materials retain
their provenance and are assigned respectively to the Paper II, III, and IV scope
records.  The current manuscript proves only the interfaces needed by those later
programmes.

## 7. Remaining human release actions

Before calling this manuscript a public release candidate, an author should:

1. build the submitted commit in a clean checkout and with the retained Dockerfile;
2. approve author, affiliation, email, date, and version metadata;
3. decide whether and how the prior Zenodo record should point to the new version;
4. review the draft pull request and authorize a non-draft release state.

## 8. Post-closure arithmetic--automorphic amendment (2026-08-06)

This amendment records a later integration checkpoint and does not rewrite the
60-page artifact evidence in Section 4, which remains the evidence for the original
closure run.  The active dependency shape is still ten sections and five appendices;
no additional Paper I source file was introduced.  The entry point and Sections 1,
3, 7, and 10 now make the arithmetic--automorphic export explicit.

| Extension node | Active statement | Source and status |
|---|---|---|
| P1-H1 / P1-H2 | The projective contexts `T_sqrt(2)` and `J=-1/z` generate the `q=4` Hecke operator subgroup, with exact projective order four | `prop:hecke-four-arithmetic-relation`, Section 3; matrix calculation plus cited standard group identification |
| P1-Z9 | Every connected, complete, boundaryless regular AES is diffeomorphic to `Z(a) x R`; its assignment is surjective and its zero set is nonempty and connected | `thm:complete-regular-aes-splitting`, Section 7; proved by rectification and complete unit-gradient flow |

The equality levels remain part of the theorem boundary: literal words, marked
histories, induced projective operators, Hecke relations, cell-stabilizer cosets, and
endpoints are not identified.  Projective continuation through `0` or infinity does
not certify an ordinary arithmetic computation.  The splitting is smooth rather
than isometric and does not apply to incomplete metrics or manifolds with boundary.
It therefore supplies the precise global no-go result needed downstream: a
branching Hecke zero network cannot be the zero set of one connected, complete,
boundaryless regular scalar AES, but it may occur after a declared singular,
incomplete, boundary, or higher-rank mechanism.

The specialization to `sqrt(2)`, the matrix relation, and the splitting proof are
internal active-manuscript results.  The conventional Hecke-group identification
and continued-fraction background use the new cited primary sources.  Paper I does
not claim a Hauptmodul, a dessin, a branched metric, or a history-to-divisor functor;
those are downstream interfaces.

The final unified repository build produced the amended Paper I artifact with the
following current evidence:

| Property | Current integration artifact |
|---|---:|
| Pages | 63 |
| File size | 604,976 bytes |
| SHA-256 | `bbcb16fa720c26f837555ff2387ee7205884a8f07963c6f949e19cb636710fd5` |
| Active labels | 177 unique |
| Citation keys used | 6 unique |

The final log has no LaTeX or package warning, undefined reference or citation,
overfull or underfull box, duplicate label, or fatal diagnostic.  This table
supersedes only the artifact metadata for the active integration snapshot; the
original 60-page closure evidence above remains a historical record.

## 9. M-0006 interface rebuild (2026-08-06)

Paper I receives no new theorem or source file in M-0006.  Section 10 now names the
proved downstream use of its q=4 operator export: Paper III passes from primitive
hyperbolic operator classes to classical periodic-orbit knots, while retaining the
distinction between marked histories, operators, conjugacy classes, and knots.  This
does not turn Paper I into a knot-theoretic paper and does not close the
history-to-divisor problem.

The unified repository build after that interface edit produced:

| Property | M-0006 integration artifact |
|---|---:|
| Pages | 63 |
| File size | 604,948 bytes |
| SHA-256 | `9144f603f9452f09ecaf9e9c32e15029b33992cf0837073580a9d3f7188de2d9` |
| Active labels | 177 unique |
| Reference targets | 88 unique, all present |
| Citation keys used | 6 unique, all present |

The canonical log and BibTeX log contain no warning, undefined reference or
citation, overfull or underfull box, or fatal diagnostic.  The three changed
conclusion pages were rendered and visually checked without a layout defect.
