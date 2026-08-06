# Paper I Migration Log

**Baseline:** `134e70a74ed010024afa7439bd3931402731423a`  
**Canonical active manuscript:** `paper-1/aeg-paper-1.tex`, `paper-1/sections/`, and
`paper-1/appendices/`
**Rule:** legacy sources are retained until human review; exclusion from the active
build is not deletion.

## Migration states

- `CANONICAL`: active source of the restructured Paper I.
- `EXPORTED`: material assigned to a later paper with provenance recorded.
- `ARCHIVAL`: retained historical source, not an active theorem dependency.
- `HOLD`: status requires a separate audit before reuse.

## Root and alternative manuscripts

| Source | State | Destination / treatment | Claim treatment |
|---|---|---|---|
| `paper-1/aeg-paper-1.tex` | CANONICAL | Rewritten as the ten-section Paper I entry point | Claims limited to proved foundational results |
| `sections/sec01.tex`–`sec12.tex` | ARCHIVAL | Replaced in the active build by `paper-1/sections/` | Reused only after formula-level audit |
| `../archive/revision-1/` | ARCHIVAL | Historical eight-section draft | Analytic material assigned to Paper II |
| `../archive/revision-2/` | ARCHIVAL | Historical eight-section and Lean-support draft | Not a canonical Paper I source |
| `../archive/arxiv/` | ARCHIVAL | Earlier distribution snapshot | DOI/release provenance retained |
| `../archive/paper4p/` | ARCHIVAL | Earlier short manuscript | Tube claims not imported |
| `aeg-lemma.tex` | HOLD | Separate source/proof audit required | No Paper I dependency |

## Legacy section disposition

| Legacy source | Paper I destination | Exported or excluded material |
|---|---|---|
| `sections/sec01.tex` | `01-introduction.tex` | Holomorphic programme → Paper II |
| `sections/sec02-00.tex` | `02-sequential-histories.tex`; Chapter 6 examples | Orientation-dependent threadlike definition superseded |
| `sections/sec02-01.tex` | Chapters 2 and 4; Appendix E | Full relation/neutrality theory → Paper IV/HOLD |
| `sections/sec03.tex` | Chapters 4 and 5 | Analytic operator interpretation → Paper II |
| `sections/sec04.tex` | Chapters 6 and 7; Appendix C | Tube and general model hierarchy → Paper III |
| `sections/sec05.tex` | Chapter 8; Appendix D | Condensation interpretation → Paper IV |
| `sections/sec06.tex` | Chapter 9; Appendix D | Long standard contact calculations reduced |
| `sections/sec07.tex` | Chapter 9 only where foundational | Appell/function theory → Paper II |
| `sections/sec08.tex` | No active Paper I input | Entire analytic development → Paper II |
| `sections/sec09.tex` | `10-conclusion.tex` | Interfaces split among Papers II–IV |
| `sections/sec10.tex` | Appendices C and D | Historical model numbering removed |
| `sections/sec11.tex` | Appendix D only where contact-foundational | Holomorphic calculations → Paper II |
| `sections/sec12.tex` | Appendix E, minimal examples | General neutrality/relations → Paper IV/HOLD |

## Working-note provenance

| Source class | State | Canonical destination |
|---|---|---|
| `notes/bilateral_projective_condensation.tex` | EXPORTED/PARTIAL IMPORT | Sequential/projective/affine proofs → Paper I Chapters 2–4; quotient and condensation theory → Paper IV |
| Analysis, horizontal-CR, Appell, and operator notes | EXPORTED | Paper II |
| Multi-zero, `E_k`, `E_log`, singularity, and tube notes | EXPORTED | Paper III |
| `knots/` and knot-related `misc/` | EXPORTED | Paper III research archive; no invariant claim yet |
| `notes/rg_*` and complexity/resource notes | EXPORTED | Paper IV |
| Remaining `notes/`, `misc/`, and `../archive/plans/` | HOLD/ARCHIVAL | Retain provenance; no automatic theorem authority |

## New canonical source map

| Target | Status | Principal claims |
|---|---|---|
| `01-introduction.tex` | CANONICAL | Process hierarchy, contributions, scope |
| `02-sequential-histories.tex` | CANONICAL | Sequential-tree classification; marked histories |
| `03-projective-affine.tex` | CANONICAL | Bilateral projective semantics; `PGL_2`; Borel sector |
| `04-affine-cocycles.tex` | CANONICAL | Target/source cocycles; relative affine defect |
| `05-affine-flow.tex` | CANONICAL | Lie flow; regular AES; eikonal/frame equivalence |
| `06-hyperbolic-model.tex` | CANONICAL | Invariant metric; complete homogeneous model |
| `07-zero-geometry.tex` | CANONICAL | Regular-zero theorem; singular AES; parameter family |
| `08-acs-torsion.tex` | CANONICAL | Direct ACS evaluation; generalized weighted Stokes |
| `09-contact-curvature.tex` | CANONICAL | Contact form; finite defects; horizontal curvature |
| `10-conclusion.tex` | CANONICAL | Proved conclusion and Papers II–IV interfaces |
| `appendices/app-A`–`app-E` | CANONICAL | Convention checks and supporting calculations only |

## Build record

| Stage | Result |
|---|---|
| Baseline, fixed commit | Failed: missing `stmaryrd.sty`; tracked PDF was stale |
| Ten-section skeleton | Passed integration parse; all target inputs present |
| Algebraic chapters | Passed integration build and independent algebra review |
| Geometric chapters | Passed integration build and independent geometry review |
| ACS/contact chapters | Passed integration build and independent sign/convention review |
| Final local build | Passed: 60 pages, clean LaTeX/BibTeX logs |
| Rendered PDF review | Passed: all pages rendered; all eight figures inspected |
| Docker build | Not run: Docker unavailable in current environment |

No legacy mathematical source has been deleted.  Git history and the retained paths
preserve every superseded formulation pending author review.

The final artifact and all closure evidence are recorded in
`paper-I-closure-report.md`.  Paper II--IV material remains in the legacy tree or its
explicit destination record and is not imported through the active Paper I input
closure.

## Migration M-0002

- Date: 2026-08-06
- Source: `aeg-paper.tex`, `sections/foundations/`, and
  `paper-II/`--`paper-IV/`
- Destination: `paper-1/`--`paper-4/`
- Migration state: CANONICAL / EXPORTED
- Claim treatment: no mathematical claims changed
- Theorem nodes affected: none
- Notation changes: none
- Content retained in source: legacy root `sections/sec*.tex` files remain archival
- Content removed from source: none; canonical files were moved without mathematical edits
- Build result: passed; `paper-1/aeg-paper-1.pdf` produced (60 pages)
- Reviewer notes: Arabic-numbered top-level directories are now canonical

## Naming convention N-0001

- Source entry point: `paper-k/aeg-paper-k.tex`
- Generated artifact: `paper-k/aeg-paper-k.pdf`
- Current implementation: Papers I and II
- Reserved future names: `paper-3/aeg-paper-3.tex` and
  `paper-4/aeg-paper-4.tex`; no empty manuscript files are created before their
  theorem sets stabilize

## Migration M-0003

- **Date:** 2026-08-06
- **Source:** analytic portions of `sections/sec07.tex`, `sections/sec08.tex`,
  `sections/sec09.tex`, and `sections/sec11.tex`; corresponding revision-1 and
  revision-2 analytic sections; `notes/analysis_01.tex`; the regular-AES,
  hyperbolic-model, and contact interfaces in Paper I Sections 5, 6, and 9
- **Destination:** `paper-2/aeg-paper-2.tex`, eight files under
  `paper-2/sections/`, and three files under `paper-2/appendices/`
- **Migration state:** CANONICAL / REDERIVED; legacy and alternative sources remain
  ARCHIVAL or HOLD and are not active TeX dependencies
- **Claim treatment:** surface and contact analysis are separated; raw sums of
  squares are distinguished from measure-selected variational Laplacians; formal,
  pointwise, and closed-operator statements receive separate domains; the legacy
  affine--Appell “basis” is corrected to a filtered `C^infty(u,v)`-module; the
  Poisson--Dirichlet and Dirichlet-to-Neumann theorems are newly proved on the basic
  model with classical provenance stated explicitly
- **Formula/source-family destinations:** general surface adjoints and CR
  factorization → Sections 2--3 and Appendix A; contact adjoints, twisted
  factorization, logarithmic fields, and affine--Appell calculations → Section 4 and
  Appendix B; hyperbolic normalization, Poisson kernel, boundary uniqueness,
  Fourier energy, and assignment-dependent fields → Sections 5--7 and Appendix C;
  limitations and Papers III--IV boundary → Sections 1 and 8
- **Theorem nodes affected:** P2-D1--P2-D2 and P2-T1--P2-T9
- **Notation changes:** `X_u,X_v` are reserved for the regular-AES tangent frame;
  `D_u,D_v` for contact lifts; `Delta_g` and `Delta_C` name the variational
  operators; `Q_C` names the raw contact sum of squares; the contact Appell scale is
  `r=e^{lambda v}`, distinct from the surface eikonal norm `q`
- **Citations:** Paper I provenance plus Ahlfors, H\"ormander, and
  Caffarelli--Silvestre; no legacy source is treated as external proof authority
- **Content retained in source:** every legacy, revision, and note file remains
  unchanged for comparison
- **Content removed from source:** none
- **Build result:** passed locally; Paper II produces a 39-page US-letter PDF with
  clean LaTeX and BibTeX logs; exact artifact metadata and hash are recorded in
  `paper-II-closure-report.md`
- **Reviewer notes:** independent cross-branch mathematical reviews found no
  blocking formula or theorem defect after the trace-space summary was narrowed;
  the scope review confirmed the Paper I → Paper II dependency and no Paper III/IV
  leakage
