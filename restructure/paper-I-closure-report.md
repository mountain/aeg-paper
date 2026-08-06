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

## 1. Acceptance outcome

- **Repository baseline:** closed.  The fixed baseline, alternate manuscript trees,
  historical notes, figures, styles, build scripts, and bibliography were inventoried.
  The unmodified baseline build failure and stale tracked PDF were recorded before the
  build script was changed.
- **Structural migration:** closed.  The active entry point contains ten foundational
  sections and five appendices, and it inputs only the new
  `sections/foundations/` tree.  No legacy source was deleted.
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
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper.tex
bibtex aeg-paper
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper.tex
```

The task runner materializes repeated writes to a generated binary at sandbox exit,
so the final evidence run executed the same four stages as separate process
invocations.  This avoids a runner-specific overlay race and does not change the
repository build procedure.

Final artifact:

| Property | Value |
|---|---:|
| PDF | `aeg-paper.pdf` |
| Pages | 60 |
| Page size | US letter, 612 x 792 pt |
| PDF version | 1.5 |
| File size | 582,862 bytes |
| SHA-256 | `d557279a2e6e244ca29409906f65136bca3e7c298906c86502cdd72271d1f447` |

Static and rendered checks:

- 166 unique active labels; no duplicate labels;
- every active `ref`, `eqref`, and `autoref` target exists;
- every citation key exists in `aeg-paper.bib`;
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
