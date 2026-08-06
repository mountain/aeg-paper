# Paper II Source and Theorem Audit

**Paper:** *Arithmetic Expression Geometry II: Hyperbolic Real Function Theory*

**Audited baseline:** `61ff60d`

**Audit date:** 2026-08-06

**Status:** closed for the mathematical-review manuscript

This file records the controlled scope of the Paper II writing task.  It is subordinate
to `AGENTS.md`, `00-authoritative-scope.md`, and
`01-paper-series-architecture.md`, but is the task-specific authority for the files,
theorem nodes, and validation listed below.

## 1. Scope

The task is to create the first complete mathematical-review manuscript of Paper II.
The paper imports the regular-AES, basic-hyperbolic-model, and contact-state-space
interfaces proved in Paper I.  It adds analytic data, distinguishes two-dimensional
surface holomorphicity from three-dimensional contact CR analysis, fixes operator
domains and measures, proves a Poisson--Dirichlet theorem on the basic hyperbolic AES,
and constructs explicit assignment-dependent solution families.

The task does not attempt a general spectral resolution, a Green-function theory on
arbitrary AESs, singular-zero analysis, tube topology, or computational-complexity
consequences.

## 2. Files allowed to change

- `paper-2/**`;
- `build.sh` for an additive multi-paper build interface;
- `README.md` for active-manuscript and build documentation;
- `aeg-paper.bib` for references actually cited by Paper II;
- `restructure/paper-II-source-audit.md`;
- `restructure/decisions-paper-II.md`;
- `restructure/paper-II-closure-report.md`;
- `restructure/audit-report.md`;
- `restructure/05-mathematical-status.md`;
- `restructure/07-acceptance-checklist.md`;
- `restructure/08-open-questions.md`;
- `restructure/migration-log.md` and `restructure/source-inventory.md`.

## 3. Files forbidden to change

- the mathematical source and generated PDF under `paper-1/`;
- legacy `sections/sec*.tex` sources;
- files under `archive/`, `notes/`, `knots/`, and `misc/`;
- Paper III and Paper IV mathematical sources.

Legacy sources remain provenance records.  Canonical Paper II statements are
rederived rather than silently edited in place.

## 4. Source audit

| Source | Reusable content | Required treatment |
|---|---|---|
| `sections/sec07.tex` | horizontal derivatives; natural units; triangular calculations | retain Paper I curvature only by import; rederive analytic operators and move the calculable family to a Paper II appendix |
| `sections/sec08.tex` | formal Cauchy--Riemann system, conformality, factorization, explicit logarithmic field | split surface holomorphicity from contact CR; fix metric, measure, domain, branch, and sign assumptions |
| `sections/sec09.tex` | analytic research interface | replace programme language by proved Paper II results and a delimited frontier |
| `sections/sec11.tex` | extended contact, factorization, logarithmic, and finite-family calculations | audit formulas; reuse only in canonical Paper II proofs or appendices |
| `archive/revision-1/sections/sec06-analytic.tex` and revision 2 counterpart | compact formal operator package | provenance only; no independent theorem authority |
| `notes/analysis_01.tex` | distinction between factorization and variational operators | resolve the distinction through explicit adjoints and the hyperbolic-model calculation |
| Paper I Sections 5, 6, and 9 | regular AES, canonical frame, hyperbolic metric, contact distribution and bracket | imported proved interface; definitions are enriched, not changed |

The audit found four blocking defects in the legacy analytic presentation:

1. the two-dimensional complex analysis of a regular AES and the CR analysis of the
   three-dimensional contact state space were not kept categorically separate;
2. the raw sum of squares was called a Laplacian without its divergence drift or a
   declared measure;
3. the affine--Appell family was called a basis without an ambient completion or
   spanning theorem;
4. no boundary, kernel, spectral, or continuation theorem had yet been proved.

Paper II resolves the first three by definition and exact calculation.  It resolves
the fourth on the basic hyperbolic AES through the Poisson kernel and its
Dirichlet-to-Neumann energy identity.

## 5. Theorem nodes in scope

The following dependency order is fixed for this task.

```text
P2-D1  analytic regular AES and arithmetic frame
  |
  +--> P2-T1  frame adjoints, energy form, and Laplace--Beltrami operator
  |       |
  |       +--> P2-T2  intrinsic CR factorization and holomorphic => harmonic
  |
  +--> P2-D2  normalized contact analytic structure
          |
          +--> P2-T3  contact adjoints, Friedrichs realization, bracket generation
          +--> P2-T4  contact-CR factorization and logarithmic CR field
          +--> P2-T5  finite filtered affine--Appell modules

Paper I basic hyperbolic model
  |
  +--> P2-T6  arithmetic-frame operator equals the hyperbolic Laplacian
          |
          +--> P2-T7  Poisson kernel and C_0 Dirichlet theorem
          +--> P2-T8  Dirichlet-to-Neumann multiplier and energy identity
          +--> P2-T9  explicit assignment-dependent holomorphic families
```

The term `harmonic` is reserved for a named operator.  Surface harmonicity means
`\Delta_g F=0`; contact variational harmonicity means `\Delta_{\mathcal C}F=0`;
contact-CR factorization produces a separately named twisted equation.

## 6. Claim-status changes authorized

- formal frame and factorization identities may become `PROVED` after complete
  in-paper calculations;
- the corrected logarithmic contact-CR field may become `PROVED WITH STATED
  HYPOTHESES` after its branch domain is fixed;
- the affine--Appell material may become `PROVED` only as a finite filtered module,
  not as a Hilbert or Schauder basis;
- the Poisson, Dirichlet-to-Neumann, and explicit solution-family results may become
  `PROVED WITH STATED HYPOTHESES` after their proofs are included;
- no general self-adjointness, spectral-completeness, Green-kernel, or continuation
  claim is authorized.

## 7. Required validation

1. [x] build Paper I and Paper II independently;
2. [x] confirm that both expected PDFs are nonempty;
3. [x] run BibTeX and check undefined citations and references;
4. [x] check duplicate labels and missing assets;
5. [x] verify every formula in P2-T1--P2-T9 independently;
6. [x] render every Paper II page and inspect title, equations, figures, page breaks,
   and bibliography;
7. [x] perform independent mathematical and scope reviews;
8. [x] record remaining limitations rather than promoting them.

## 8. Expected output

- `paper-2/aeg-paper-2.tex`;
- canonical `paper-2/sections/` and `paper-2/appendices/` sources;
- `paper-2/aeg-paper-2.pdf`;
- a Paper II decision record and closure report;
- updated repository build and provenance records.

All expected outputs now exist.  Exact artifact metadata, static checks, rendered
review, independent-review dispositions, and the remaining release actions are
recorded in `paper-II-closure-report.md`.  Migration M-0003 and status change S-0006
close the provenance and claim-status ledgers for this manuscript.
