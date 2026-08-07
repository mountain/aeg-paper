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
| `archive/legacy-root-manuscript/` | ARCHIVAL | Recovered legacy `aeg-paper.tex` with its `sections/sec01.tex`–`sec12.tex`; replaced in the active build by `paper-1/sections/` | Reused only after formula-level audit |
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
| `notes/projective-condensation/01-bilateral-projective-condensation.tex` | EXPORTED/PARTIAL IMPORT | Sequential/projective/affine proofs → Paper I Chapters 2–4; quotient and condensation theory → Paper IV |
| Analysis, horizontal-CR, Appell, and operator notes | EXPORTED | Paper II |
| Multi-zero, `E_k`, `E_log`, singularity, and tube notes | EXPORTED | Paper III |
| `notes/knots-and-loops/` and knot-related `images/sources/` | EXPORTED | Paper III research archive; no invariant claim yet |
| `notes/thermodynamics-and-renormalization/rg_*` and complexity/resource notes | EXPORTED | Paper IV |
| Remaining `notes/`, `images/sources/`, and `../archive/plans/` | HOLD/ARCHIVAL | Retain provenance; no automatic theorem authority |

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
  revision-2 analytic sections; `notes/analysis-and-calculus/01-horizontal-analysis-program.tex`; the regular-AES,
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
  `archive/paper4p/aeg.tex`; audited portions of `notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex`,
  `notes/knots-and-loops/03-figure-eight-aeg-summary.tex`, `notes/knots-and-loops/04-figure-eight-hnn-arithmetization.tex`, `notes/knots-and-loops/05-figure-eight-modulo-arithmetization.tex`,
  `notes/foundations-and-geometry/03-single-zero-diffusion-model.tex`, `notes/knots-and-loops/06-fox-calculus-and-alexander-modules.tex`, `notes/knots-and-loops/01-figure-eight-arithmetic-loop.tex`, and
  `notes/knots-and-loops/02-zero-taxonomy-and-arithmetic-loops.tex`; knot calculations under `notes/knots-and-loops/` and
  `images/sources/knot_4_1.tex`; the two subordinate Paper III discussions; and 249 commits
  reachable from all refs in the local checkout
- **Destination:** `paper-3/aeg-paper-3.tex`, eight files under
  `paper-3/sections/`, three files under `paper-3/appendices/`, and the provenance
  audit `governance/paper-III-source-audit.md`
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
  `governance/discussions/arithmetic-automorphic-zero-networks.md`; and the cited
  standard literature on Hecke groups, Rosen continued fractions, triangle-group
  Hauptmoduls, relative divisors, and algebraic number theory
- **Active manuscript destinations:** `paper-1/aeg-paper-1.tex` and Paper I
  Sections 1, 3, 7, and 10; `paper-2/aeg-paper-2.tex`, Paper II Sections 1 and 8,
  and the new `paper-2/sections/05-pullback-cylinder.tex`;
  `paper-3/aeg-paper-3.tex`, Paper III Sections 1--3, the new
  `paper-3/sections/04-arithmetic-zero-networks.tex`, the existing parameter,
  singular-fiber, braid, and threading sections, and Appendix A; the Paper II and
  III README files; the root `README.md`; and `bibliography/aeg-paper.bib`
- **Governance destinations:** `00-authoritative-scope.md`,
  `01-paper-series-architecture.md`, `02-paper-I-outline.md`,
  `03-theorem-dependency-graph.md`, `05-mathematical-status.md`,
  `07-acceptance-checklist.md`, `08-open-questions.md`, the three paper decision
  records, `paper-III-source-audit.md`, `source-inventory.md`, this migration log,
  the three closure reports, and the new synthesis discussion under `governance/`
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

## Migration M-0006

- **Date:** 2026-08-06
- **Name:** q=4 sign-cover knots and finite-register divisor naturality
- **Source:** the active q=4 Hauptmodul/sign construction; Paper I's chronological
  projective evaluation and neutral word `omega_4`; the cited geodesic-flow,
  lens-space, template, finite-etale, and arithmetic-Frobenius literature; and the
  two-priority mathematical red-team record
- **Active manuscript destinations:** new
  `paper-3/sections/05-q4-geodesic-knots.tex` and
  `paper-3/sections/05-history-divisor-naturality.tex`; the Paper III entry point,
  abstract, introduction, README, and PDF; Paper I and II conclusion interfaces;
  root README; and the shared bibliography
- **Governance destinations:** `00-authoritative-scope.md`,
  `05-mathematical-status.md`, `07-acceptance-checklist.md`,
  `08-open-questions.md`, `decisions-paper-III.md`, `source-inventory.md`, this
  migration log, the arithmetic--automorphic synthesis discussion, audit report,
  and closure amendments
- **Migration state:** CANONICAL / REDERIVED HERE / CLASSICAL EXTERNAL INPUT /
  RESTRICTED NATURALITY MODEL / OPEN GENERAL FRONTIER
- **q=4 topology treatment:** the sign kernel has signature
  `(0;2;infinity,infinity)`; its completed coarse AEG carrier is `C*`.  Retaining
  the hyperbolic orbifold, its unit tangent bundle is identified by peripheral
  cover and slope calculation with `S^3 minus T(2,4)` under the declared filling.
  The local four-prong germ is not identified with this global link.
- **Knot treatment:** primitive hyperbolic operator classes give classical
  geodesic-flow periodic-orbit knots.  Cyclic word shift acts by operator
  conjugacy; path inverse gives the time-reversed orbit; the map is surjective but
  collapses marked-history fibers.  The zero dessin is a coding spine, not the
  three-dimensional template.  No new isotopy or Markov invariant is claimed.
- **Register treatment:** `u^2=t` forces an equivariant projective quadratic
  endpoint divisor and explicit Frobenius.  A tagged prefix trace and ordinary
  pole cocycle distinguish `omega_4` from the empty history at `t=2` and `t=1/2`.
  The tower `v^2=3`, `u^2=t+v` forces an arithmetically irreducible quartic with
  two constant-geometric components, explicit discriminant, monodromy, and
  Frobenius cycle types.
- **Boundary:** both registers are supplied typed inputs.  Their terminal endpoint
  data factor through projective evaluation and do not solve the general
  history-to-prime-divisor functor, factorization-history problem, or knot
  decoration descent.
- **Theorem nodes affected:** P3-K1--P3-K4 and P3-R3--P3-R5; OQ-072--OQ-074 are
  partially resolved as recorded, OQ-075 remains open, and OQ-076 records the new
  marked-history knot-enhancement frontier
- **Content removed from source:** none
- **Unified build result:** `./build.sh all` completed the current
  `pdflatex`--BibTeX--three-`pdflatex` sequence for all three manuscripts.  Papers
  I--III contain 63, 44, and 58 pages.  Their final sizes, SHA-256 values, label,
  reference, and citation counts, clean-log evidence, and visual audit are recorded
  in `audit-report.md` Section 10 and in the M-0006 closure amendments.

## Migration M-0007

- **Date:** 2026-08-06
- **Name:** polynomial relations across slices and threaded carriers
- **Source:** the user-specified tube intuition; the active q=4 sign-cover lattice
  and cusp-slope calculation; the supplied family `P_m(z,t)=z^2-t^m`; Paper III's
  existing singular-AES, relative-divisor, finite-root, and braid interfaces; and
  independent carrier, exact-sequence, q4 naturality, and mathematical red-team
  calculations
- **Active manuscript destinations:** new
  `paper-3/sections/05-polynomial-threaded-carriers.tex`; Paper III entry point,
  abstract, introduction, conclusion, README, and generated PDF; root README
- **Governance destinations:** `00-authoritative-scope.md`,
  `05-mathematical-status.md`, `07-acceptance-checklist.md`,
  `08-open-questions.md`, `decisions-paper-III.md`, `source-inventory.md`, this
  migration log, audit report, and Paper III closure amendment
- **Migration state:** PROVED EXPLICIT HORIZONTAL MODEL / MARKED TORIC q=4
  SPECIALIZATION / OPEN HISTORY-NATURAL LIFT
- **Carrier treatment:** `Im(P_m)=0` is a compact connected neat smooth incidence
  with four boundary circles and `2m` circle-valued Morse saddles; it has genus
  `m-1` and singular-AES slice metrics.  It is not called a proper zero tube.
- **Thread treatment:** `P_m=0` is an embedded finite root thread with braid
  `sigma_1^m` and closure `T(2,m)`.  Its arithmetic prime components, geometric
  components, and link components agree in this family, but the embedded braid
  retains the full integer `m` beyond the permutation parity.
- **Horizontal identity:** discriminant order, logarithmic period, braid exponent,
  carrier-framing period, and negative half Euler characteristic agree.  At
  `m=4`, the pure-braid coordinate and mutual linking number are two although the
  polynomial splits and its sheet permutation is trivial.
- **q=4 treatment:** the ordered filling meridians, index-two lattice, deck
  translation, and cusp slope derive the two-coset toric divisor `u^2=t^4` up to
  toric gauge.  The compactified marked sign cover further recovers the binomial
  as its logarithmic-tangent cusp section and realizes its link in the weighted
  Hopf circle bundle.  Arithmetic quadratic descent and radial extension to the
  genus-three carrier remain separate declared choices.
- **Extension calibration:** supplied four-root Garside and rotation paths pull the
  braid-center extension back to the q=4 unit-tangent extension; their common
  full-twist residue and normalized discriminant period are proved.  The induced
  invariant kernel character has LHS transgression equal to the unit-tangent Euler
  extension class, but is not Paper I affine torsion and has no history-natural
  origin yet.
- **Boundary:** the pure-braid exact sequence is not the unit-tangent central
  extension, no Paper I torsion transgression is claimed, and the neutral history
  `omega_4` remains the hard coefficient-path naturality test.
- **Theorem nodes affected:** P3-H1--P3-H7; OQ-072 receives a marked peripheral
  refinement; OQ-073 and OQ-076 remain open; OQ-077 records the mixed
  slice--tube naturality problem.
- **Content removed from source:** none
- **Unified build result:** Papers I--III build cleanly at 63, 44, and 69 pages.
  The final Paper III artifact is 704,239 bytes with SHA-256
  `f094bc5e70739fc0144fcefff78a877f03d420f39f2475be12aed6d938a9dd9e`;
  static, mathematical, and all-page visual audits report no blocking or major
  finding after repair.  Full unified evidence is recorded in `audit-report.md`
  and `paper-III-closure-report.md`.

## Migration M-0008

- **Date:** 2026-08-06
- **Name:** sextic Lyashko--Looijenga forgetting laboratory
- **Source:** the supplied sparse sextic `P_0(x)=x^6-x`; the active
  polynomial-carrier/thread interface; the classical Lyashko--Looijenga,
  transposition-factorization, Birman--Hilden, Picard--Lefschetz, symplectic
  monodromy, and hyperelliptic arithmetic literature; and independent
  root/critical-value braid and claim-boundary red teams
- **Active manuscript destinations:** new
  `paper-3/sections/05-sextic-ll-laboratory.tex`; Paper III entry point,
  introduction/claim ledger, conclusion, README, and generated PDF; root README
- **Governance destinations:** `05-mathematical-status.md`,
  `07-acceptance-checklist.md`, `decisions-paper-III.md`, `source-inventory.md`,
  this migration log, audit report, and Paper III closure amendment
- **Migration state:** PROVED EXPLICIT SEXTIC LABORATORY / CLASSICAL LL AND
  GENUS-TWO INPUTS / OPEN LL--IGUSA TWIN TEST / OPEN AEG-HISTORY NATURALITY
- **Event-polynomial treatment:** for a monic centered sextic `P`,
  `Q_P(t)=6^{-6} disc_x(P(x)-t)` is the monic quintic of critical values.  The
  regular LL map is a finite etale cover of degree `6^4=1296`.  These are
  coordinate-normalized sheets; the free residual source rotation by `mu_6`
  gives `216` orbits, not `1296` or `216` pairwise nonisomorphic curves.
- **Explicit-pencil treatment:** `P_0=x^6-x` has five simple critical values and
  event polynomial `Q_0=t^5+5^5/6^6`.  Meridians about those values lift to
  half-twists along a six-vertex spanning star, generating `B_6`.  The associated
  real carrier has saddle walls, its complex zeros give the intrinsic six-sheet
  thread, and its double branched cover gives genus-two mapping tori.  Real wall
  crossings, root collisions, and spectral degenerations remain distinct strata.
- **Two-braid treatment:** critical-value transport acts through the LL
  `1296`-sheet cover, while the moving test value gives a separate vertical
  `F_5` and six-root braid.  The manuscript uses the mixed braid extension and
  its LL pullback; it does not assert a canonical homomorphism `B_5 -> B_6` after
  forgetting the LL sheet.
- **Genus-two and arithmetic treatment:** the displayed pencil surjects onto the
  genus-two mapping class group and has full integral symplectic monodromy through
  cited classical lifting and monodromy theorems.  The fiber
  `y^2=x^6-x-1` has the printed `S_6` Galois and geometric-endomorphism conclusions
  by cited classical criteria.  The common finite target
  `Sp_4(F_2) isomorphic to S_6` does not canonically identify Frobenius elements
  with topological loops.
- **Open boundary:** the LL--Igusa twin test has not established two
  nonisomorphic genus-two curves in one LL fiber.  No unrestricted arithmetic
  history canonically selects a sextic, an LL sheet, a mixed-braid path, or a
  six-root braid.  No new knot invariant or Markov descent is claimed.
- **Theorem nodes affected:** P3-L1--P3-L9; P3-H7 and P3-R3 remain open.
- **Content removed from source:** none
- **Canonical build result:** `./build.sh 3` produced a clean 78-page,
  809,341-byte PDF with SHA-256
  `d5bf667041dc6ce52189f840a5a691c4d8c6eed1126705911937a907fb74f816`.
  Static closure has 17 TeX files, 322 unique labels, 157 resolved reference
  targets, and 30 resolved citation keys.  All 78 pages were rendered and
  visually inspected without a blocking layout defect.

## Migration M-0009

- **Date:** 2026-08-06
- **Name:** explicit geometric LL--Igusa twin and fiberwise nonfactorization
- **Source:** exact elimination in the sparse even-coefficient sextic ansatz;
  scaling of critical values; the quadratic Igusa--Clebsch invariant and binary
  sextic discriminant; and the surrounding sextic-moduli comparison with recent
  work of Farb and collaborators
- **Active manuscript destinations:** Paper III abstract, introduction, sextic
  LL laboratory, conclusion, README, and root README
- **Governance destinations:** `00-authoritative-scope.md`,
  `01-paper-series-architecture.md`, `03-theorem-dependency-graph.md`,
  `05-mathematical-status.md`, `07-acceptance-checklist.md`,
  `decisions-paper-III.md`, `source-inventory.md`, this migration log,
  `audit-report.md`, and `paper-III-closure-report.md`
- **Migration state:** EXPLICIT GEOMETRIC TWIN PROVED / FULL 216-ORBIT CENSUS,
  ARITHMETIC-PERIOD COMPARISON, MARKED-MONODROMY REFINEMENT, HODGE/SIEGEL
  ENERGY, AND HISTORY NATURALITY OPEN
- **Exact pair:** (P_0=x^6-x) and the displayed algebraic monic-centered (P_1)
  have identical event quintic (Q_0=t^5+5^5/6^6) and lie in distinct residual
  source-rotation orbits.
- **Geometric separation:** at the common regular slice (t=1), both sextics have
  discriminant (6^6+5^5), but their exact quadratic Clebsch values give distinct
  absolute Igusa--Clebsch ratios.  Their genus-two curves are nonisomorphic over
  (\mathbb C), so the slice-moduli reading does not factor through the LL event
  polynomial.
- **Computation provenance:** the same-event identity is proved from a printed
  exact Sylvester-resultant identity and scaling law; the moduli separation is
  an exact symbolic invariant comparison.  The repository script reproduces the
  two calculations and is verification evidence rather than a substitute for
  the proof.
- **Finite-sheet descent:** over (Q(1)\ne0), the residual-rotation quotient is a
  degree-(216) finite etale cover.  The moduli sheet observable has a norm
  spectral polynomial with descended trace, norm, and higher symmetric
  coefficients.  Canonical averaging splits constants from the zero-sum
  permutation representation; its squared norm is a monodromy-invariant
  forgetting variance.  The explicit twin supplies the printed exact positive
  lower bound at (Q_0).  No constancy along arbitrary open LL paths is asserted.
- **Moving-slice charge:** for the two explicit pencils,
  (\mathcal J_1/\mathcal J_0)=((t-\beta)/t)^5), both (0) and (\beta) are regular,
  and the divisor is (5[\beta]-5[0]).  Its logarithmic residues balance, but this
  is not a finite Dirichlet energy.
- **Farb boundary:** recent Farb--Kisin--Wolfson, Farb--Wolfson,
  Farb--Looijenga, and rigidity work supplies closely related sextic,
  configuration-space, modular, monodromy, arithmetic, and period frameworks.
  It does not supply this LL-fiber pair; Paper III claims only the explicit
  upper fiberwise nonfactorization.
- **Open boundary / P3-L10:** no full solution of all (1296) sheets or (216)
  rotation orbits; no assertion that either number counts curves; no certified
  Frobenius or reduced Siegel-period distinction for the pair; no result after
  grouping by marked local (\operatorname{Sp}_4(\mathbb Z)) transvections and
  Hurwitz action; no Hodge- or Siegel-metric energy; no history-natural sheet
  selection.
- **Theorem nodes affected:** P3-L9 is promoted from open to proved; P3-L10 is
  introduced as the remaining finite census and deeper-twin problem.
- **Content removed from source:** none
- **Canonical build result:** `./build.sh 3` produced a clean 83-page,
  859,662-byte PDF with SHA-256
  `f9cf579734cbf2a5c70794470ba3baf3b79c2fc1144926513f291b7a2462c858`.
  Static closure has 17 canonical TeX files, 351 unique labels, 175 resolved
  reference targets, and 36 resolved citation keys in a 53-entry shared
  bibliography.  All 83 pages were rendered and visually inspected without a
  blocking layout or glyph defect.

## Migration M-0010

- Date: 2026-08-07
- Source: root `sections/sec01.tex`--`sections/sec12.tex` and historical
  `aeg-paper.tex` from revision `095ae4b28cb645ea43e18aa2560d227830cc3a14`
- Destination: `archive/legacy-root-manuscript/`
- Migration state: ARCHIVAL
- Claim treatment: no mathematical claims changed; an archival provenance comment
  was added to each section source
- Content removed from source: the legacy root `sections/` path; all files were
  retained under the destination
- Build result: all four canonical papers passed `./build.sh`; the archived bundle
  itself retains its historical repository-relative dependency paths and is not a
  standalone build package

## Migration M-0011

- Date: 2026-08-07
- Source: `misc/`, `knots/`, and the previously flat `notes/` directory
- Destinations: figure/model sources to `images/sources/`; knot sources and related
  loop notes to `notes/knots-and-loops/`; remaining notes to the five other topical
  subdirectories recorded in `source-inventory.md`
- Migration state: ARCHIVAL RECLASSIFICATION
- Claim treatment: no mathematical claims, statuses, assumptions, or build closures
  changed; tracked rendered artifacts and local compilation companions moved with
  their source documents
- Reference treatment: repository references to the moved source paths were updated
  to their current destinations
- Content removed from source: none; the old `misc/` and `knots/` directory names
  were retired after all contents were preserved under their destinations
- Build result: no canonical LaTeX source or build dependency changed; static path
  checks found no remaining references to the retired locations

## Migration M-0012

- Date: 2026-08-07
- Source: top-level `styles/`
- Destination: `archive/legacy-latex-styles/`
- Migration state: ARCHIVAL
- Claim treatment: no mathematical claims, statuses, assumptions, or canonical
  build closures changed
- Reference treatment: the historical revision drafts, archived root manuscript,
  and thermal note now reference both archived style paths
- Content removed from source: none; both third-party style files were preserved
  byte-for-byte and the empty top-level directory was retired
- Build result: canonical papers do not load either style; static path checks found
  no remaining references to the retired top-level location

## Migration M-0013

- Date: 2026-08-07
- Source: root `aeg-paper.bib`
- Destination: `bibliography/aeg-paper.bib`
- Migration state: SHARED RESOURCE RELOCATION
- Claim treatment: no mathematical claims, citation entries, assumptions, or
  canonical TeX membership changed; only the shared-database path changed
- Reference treatment: all four canonical papers and the historical manuscripts
  that use the shared database now reference its dedicated directory
- Content removed from source: none; the bibliography was moved without rewriting
  its entries
- Build result: `./build.sh` rebuilt all four canonical PDFs successfully; each
  BibTeX log reads `../bibliography/aeg-paper.bib`, with no undefined references,
  undefined citations, or duplicate labels

## Migration M-0014

- Date: 2026-08-07
- Source: top-level `restructure/`
- Destination: top-level `governance/`
- Migration state: GOVERNANCE CONTROL-PLANE RENAME
- Claim treatment: no mathematical claims, statuses, assumptions, source contents,
  or canonical build closures changed
- Reference treatment: repository guidance, governance documents, paper READMEs,
  source audits, discussions, and local workspace path history now use the new name
- Content removed from source: none; all 30 files were moved with their directory
  structure intact
- Build result: `./build.sh` rebuilt all four canonical PDFs successfully, with no
  undefined references, undefined citations, or duplicate labels; the only remaining
  `restructure/` strings are the historical source-path records in this migration and
  `source-inventory.md`

## Migration M-0015

- Date: 2026-08-07
- Source: `governance/AGENTS.md` and the root discovery-pointer `AGENTS.md`
- Destination: root `AGENTS.md`
- Migration state: AUTHORITATIVE INSTRUCTION CONSOLIDATION
- Claim treatment: no mathematical claims, statuses, assumptions, or canonical
  build closures changed
- Reference treatment: repository README, governance overview, source inventory,
  source audits, and discussion provenance now point to the root instruction file
- Content removed from source: only the superseded root pointer text; the complete
  authoritative instruction content is preserved at the destination
- Build result: the authoritative content matches the former governance copy after
  the `governance/` path migration; all AGENTS links resolve, and `./build.sh`
  rebuilt all four canonical PDFs with no undefined references, undefined citations,
  or duplicate labels

## Migration M-0016

- Date: 2026-08-07
- Name: explicit manuscript-level draft notices
- Destinations: root README, existing per-paper READMEs, and the title matter of all
  four canonical manuscripts
- Migration state: EDITORIAL MATURITY DISCLOSURE
- Claim treatment: no mathematical claim or governance status changed; `draft` is
  expressly an editorial, visual, conceptual-integration, and publication-maturity
  description rather than a claim-status label
- Legacy comparison: the notices record that the archived root manuscript may
  currently be more polished in exposition, figures, and text--figure integration
- Build result: `./build.sh` rebuilt all four canonical PDFs with no undefined
  references, undefined citations, or duplicate labels; every first page was rendered
  and checked to confirm that the notice is visible before the abstract without
  clipping or overlap

## Migration M-0017

- Date: 2026-08-07
- Source: the six categorized subdirectories under `notes/`
- Destination: the same subject directories with normalized filenames
- Migration state: NOTE NAMING AND ORDER NORMALIZATION
- Naming rule: `NN-descriptive-topic-slug`, with an independent two-digit reading
  order inside each subject; companion artifacts share the source basename
- Claim treatment: no note content or mathematical status was promoted; the numeric
  code is explicitly not an authority, chronology, or theorem-status code
- Reference treatment: governance records and note-to-note references were updated to
  the descriptive filenames; former names survive only where explicitly marked as
  historical provenance
- Content removed from source: none
- Build result: all 39 note sources satisfy the naming rule with no duplicate
  per-directory code; 27 unique repository note-path references and all companion
  basenames resolve; `./build.sh` rebuilt all four canonical PDFs successfully
