# Paper I Migration Log

**Baseline:** `134e70a74ed010024afa7439bd3931402731423a`  
**Canonical active manuscript:** `aeg-paper.tex` and `sections/foundations/`  
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
| `aeg-paper.tex` | CANONICAL | Rewritten as the ten-section Paper I entry point | Claims limited to proved foundational results |
| `sections/sec01.tex`–`sec12.tex` | ARCHIVAL | Replaced in the active build by `sections/foundations/` | Reused only after formula-level audit |
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
