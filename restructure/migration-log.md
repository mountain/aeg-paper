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
- Current implementation: Papers I--III
- Reserved future name: `paper-4/aeg-paper-4.tex`; no empty manuscript file is
  created before its theorem set stabilizes

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

## Migration M-0004

- **Date:** 2026-08-06
- **Source:** the singular-zero and family interfaces in Paper I; the
  arithmetic-holomorphic coordinate in Paper II; historical tube material in
  `archive/paper4p/aeg.tex`; audited portions of `notes/note_02.tex`,
  `notes/note_03.tex`, `notes/note_04.tex`, `notes/note_05.tex`,
  `notes/note_08.tex`, `notes/note_11.tex`, `notes/loop_01.tex`, and
  `notes/loop_02.tex`; knot calculations under `knots/` and
  `misc/knot_4_1.tex`; the two subordinate Paper III discussions; and 249 commits
  reachable from all refs in the local checkout
- **Destination:** `paper-3/aeg-paper-3.tex`, eight files under
  `paper-3/sections/`, three files under `paper-3/appendices/`, and the provenance
  audit `restructure/paper-III-source-audit.md`
- **Migration state:** CANONICAL / REDERIVED HERE; legacy, archived, knot, visual,
  and discussion sources remain ARCHIVAL, HOLD, or MOTIVATION and are not active
  TeX dependencies
- **Negative provenance finding:** no verifiable general multi-zero AEG
  construction, defined general `E_k`, or explicit historical AEG `E_log`
  construction was found in the 249 reachable commit trees; current explicit
  models are new derivations, not recovered theorems under those labels
- **Claim treatment:** Paper I's regular-zero, singular-AES, incidence, and
  properness interfaces are preserved; ambient families, zero incidences, proper
  tubes, embedded tubes, threads, braid closures, and knot invariants are separated;
  topology change includes nonproper and boundary mechanisms; knot claims stop at
  the explicit Markov and choice-independence gate
- **New constructions, all REDERIVED HERE:** conformal realization; cylindrical
  and parallel multi-zero models; logarithmic zero lift; structural discriminant
  and nonproper escape; proper real-zero and helical tubes; definite and indefinite
  Morse families; the simple branch model; finite-root and logarithmic braid
  transport; realization of every braid in the Paper II coordinate; finite zero
  threads; the stateless-scalar, ordinary-exactness, resonant finite-field, planar
  state-sum, and variable-multiplier obstruction calculations
- **Historical calculations retained:** the HNN/Alexander linear system, selected
  Fox and affine cocycle formulas, the figure-eight free-word computation, and the
  6_2/6_3/7_6 tables, each only with the limitations and reproducibility fields
  recorded in `paper-III-source-audit.md`
- **Claims rejected or held:** canonical meaning for the old `E_k` index;
  historical explicit status for `E_log`; smooth-incidence-implies-tube; irrational
  lattice density in the plane; knot-group embedding into the displayed solvable
  affine targets; presentation-independent raw torsion; automatic invariance from a
  tube, thread, stronger braid representation, or nonflat defect
- **Notation changes:** the old `E_k` and `E_log` symbols are not canonical model
  names; descriptive names identify the proved constructions; `tube` is reserved
  for the proper zero-incidence level; logarithmic sheet integers are distinguished
  from gauge-invariant cycle sums
- **Content retained in source:** all legacy sections, notes, knot files, figures,
  archived manuscripts, and working discussions remain unchanged for comparison
- **Content removed from source:** none
- **Build result:** not certified by this provenance-only migration entry; build and
  rendered-artifact evidence belong in the Paper III closure report
- **Reviewer notes:** the active proof closure excludes every historical note and
  discussion; any future external source for `E_k` or `E_log` must be added by
  immutable revision and formula-level comparison before the provenance status can
  change

## Migration M-0005

- **Date:** 2026-08-06
- **Name:** arithmetic--automorphic zero-network integration across Papers I--III
- **Source:** Paper I's bilateral projective contexts and regular-AES equation;
  Paper II's oriented-surface complex structure; Paper III's singular-pullback,
  discriminant, tube, and braid interfaces; the new synthesis record
  `restructure/discussions/arithmetic-automorphic-zero-networks.md`; and the cited
  standard literature on Hecke groups, Rosen continued fractions, triangle-group
  Hauptmoduls, relative divisors, and algebraic number theory
- **Active manuscript destinations:** `paper-1/aeg-paper-1.tex` and Paper I
  Sections 1, 3, 7, and 10; `paper-2/aeg-paper-2.tex`, Paper II Sections 1 and 8,
  and the new `paper-2/sections/05-pullback-cylinder.tex`;
  `paper-3/aeg-paper-3.tex`, Paper III Sections 1--3, the new
  `paper-3/sections/04-arithmetic-zero-networks.tex`, the existing parameter,
  singular-fiber, braid, and threading sections, and Appendix A; the Paper II and
  III README files; the root `README.md`; and `aeg-paper.bib`
- **Governance destinations:** `00-authoritative-scope.md`,
  `01-paper-series-architecture.md`, `02-paper-I-outline.md`,
  `03-theorem-dependency-graph.md`, `05-mathematical-status.md`,
  `07-acceptance-checklist.md`, `08-open-questions.md`, the three paper decision
  records, `paper-III-source-audit.md`, `source-inventory.md`, this migration log,
  the three closure reports, and the new synthesis discussion under `restructure/`
- **Migration state:** CANONICAL / REDERIVED HERE / STANDARD EXTERNAL INPUT / OPEN
  FRONTIER.  Legacy notes and discussions remain provenance or motivation and are
  not active proof dependencies.
- **Paper I claim treatment:** the arithmetic contexts
  `T_sqrt(2)(z)=z+sqrt(2)` and `J(z)=-1/z` are evaluated projectively; their matrix
  relations identify the generated operator group with the `q=4` Hecke triangle
  group.  Literal words, marked histories, projective operators, stabilizer cosets,
  and endpoints remain distinct.  A connected complete boundaryless regular scalar
  AES is globally diffeomorphic to `Z(a) x R`; this is a smooth, not Riemannian,
  splitting and excludes a multi-component or branching zero network only under
  those exact hypotheses.
- **Paper II claim treatment:** the rotated-imaginary-part planar target is a
  harmonic regular AES with the printed curvature law; the logarithmic cylinder is
  a complete flat regular AES; and holomorphic local biholomorphisms pull these
  targets back functorially.  Critical points, algebraic branch points, zeros or
  poles of the cylindrical coordinate, degenerate metrics, and cone completion are
  outside the theorem and pass to Paper III.  Analytic pullback naturality is not a
  history-to-function functor.
- **Paper III claim treatment:** a holomorphic local degree `m` over the target zero
  line gives a locally essential `2m`-prong zero and cone angle `2 pi m`.  Conditional
  on the cited normalized `(2,4,infinity)` Hauptmodul, the square-root/Cayley/
  cylindrical construction has zero set `beta^{-1}([0,1])`; order-four points are
  four-valent `4 pi` cone zeros, order-two points are bivalent edge midpoints, and
  the assignment descends either on the sign-character kernel or as a real sign-line
  section.  The relative-divisor theorem applies only after a monic generically
  square-free polynomial over a declared integral domain is supplied.
- **Arithmetic boundary:** factorization over the coefficient field, geometric
  sheets, analytic monodromy, and Galois/Frobenius data are different layers.  The
  `q=4` construction supplies operator arithmetic and automorphic uniformization,
  not nonunique factorization in `Z[sqrt(2)]`.  A general functor from marked
  histories to arithmetic relative zero divisors remains open.
- **Theorem nodes affected:** P1-H1, P1-H2, P1-Z9; P2-A1--P2-A3;
  P3-S1--P3-S4; P3-R1--P3-R3, with P3-S3 a cited standard input and P3-R3 still an
  open structural proposal
- **Provenance:** the AEG matrix, splitting, pullback, branch, Cayley, sign-descent,
  and zero-network calculations are proved or rederived in the active papers.  The
  Hecke-group and Hauptmodul geometry and the algebraic/arithmetic background are
  externally cited inputs.  The negative historical finding for general `E_k` and
  explicit AEG `E_log` is unchanged.
- **Content removed from source:** none
- **Unified build result:** `./build.sh all` completed the current four-LaTeX-pass
  per-paper sequence (`pdflatex`, BibTeX, and three resolving `pdflatex` passes).
  Papers I--III contain 63, 44, and 43 pages.  The final sizes, SHA-256 values,
  label counts, citation counts, and clean-log evidence are recorded in
  `audit-report.md` Section 9 and in the three post-closure amendments.
