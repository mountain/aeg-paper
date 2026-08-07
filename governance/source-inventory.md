# AEG Source Inventory

**Fixed baseline:** `134e70a74ed010024afa7439bd3931402731423a`  
**Inventory date:** 2026-08-06  
**Baseline population:** 207 tracked files, including 107 `.tex` sources  
**Paper I post-migration population:** 123 `.tex` sources

**Current active source closures:** Paper I: 16 canonical `.tex` files; Paper II:
13; Paper III: 17; Paper IV: 19

This inventory classifies every top-level path family in the fixed baseline.  A
family classification applies to every file beneath the named directory; exceptions
are listed explicitly.  The migration does not delete or silently overwrite any
legacy source.  Claim-level provenance is recorded in `migration-log.md`.

## 1. Canonical and root-level files

| Path | Baseline treatment | Paper I treatment |
|---|---|---|
| `.dockerignore`, `.gitignore` | KEEP | Repository hygiene; unchanged |
| `Dockerfile` | KEEP / VERIFY | Container recipe retained; Docker unavailable in the task environment |
| `LICENSE` | KEEP | Unchanged |
| `README.md` | REWRITE | Four-paper entry point and DOI distinction |
| `restructure/AGENTS.md` | KEEP / AUTHORITATIVE | Currently consolidated as the repository-wide root `AGENTS.md` |
| `aeg-paper.tex` | REWRITE / CANONICALIZE | Replaced by the sole active Paper I entry point `paper-1/aeg-paper-1.tex` |
| `aeg-paper.bib` | KEEP / CLEAN | Currently the shared bibliography at `bibliography/aeg-paper.bib` |
| `aeg-paper.pdf` | REBUILD | Replaced by the canonical artifact `paper-1/aeg-paper-1.pdf` |
| `build.sh` | STABILIZE | Canonical multi-paper build for Papers I--IV |
| `aeg-lemma.tex` | HOLD | References absent sections 13--17; no Paper I dependency |

The new canonical source tree is exactly:

```text
paper-1/
  aeg-paper-1.tex
  sections/
    01-introduction.tex
    02-sequential-histories.tex
    03-projective-affine.tex
    04-affine-cocycles.tex
    05-affine-flow.tex
    06-hyperbolic-model.tex
    07-zero-geometry.tex
    08-acs-torsion.tex
    09-contact-curvature.tex
    10-conclusion.tex
  appendices/
    app-A-conventions.tex
    app-B-affine-cocycles.tex
    app-C-hyperbolic-calculations.tex
    app-D-acs-contact.tex
    app-E-equality-neutrality.tex
```

The later-paper destination records `paper-2/README.md`, `paper-3/README.md`, and
`paper-4/README.md` are new relative to the fixed baseline.  Papers II--IV have
since advanced to canonical active source closures. Paper II is recorded in Section
6, Paper III in Section 7, and Paper IV in Section 8 below.

## 2. Exhaustive baseline family classification

| Baseline family | Files | Contents | State | Canonical destination |
|---|---:|---|---|---|
| root | 11 | metadata, Paper I entry, bibliography, PDF, build | mixed, itemized above | Paper I / repository |
| `sections/` | 13 | legacy `sec01.tex`--`sec12.tex` source family | ARCHIVAL | preserved with the baseline root manuscript under `archive/legacy-root-manuscript/`; audited portions rederived in `paper-1/sections/`; analytic → II; tube → III; quotient → IV |
| `restructure/` | 13 | authority, scope, dependency, status, editorial, acceptance, discussions | KEEP / AUTHORITATIVE | currently `governance/`; repository governance control plane |
| `revision-1/` | 13 | alternate eight-section TeX build | ARCHIVAL | currently `archive/revision-1/`; no active theorem authority |
| `revision-2/` | 26 | alternate TeX build, PDF, Lean experiment and reports | ARCHIVAL / HOLD | currently `archive/revision-2/`; formalization may be audited separately |
| `arxiv/` | 14 | prior distribution snapshot, styles, figures, bibliography | ARCHIVAL | currently `archive/arxiv/`; DOI/version provenance |
| `paper4p/` | 2 | short alternative manuscript and build | ARCHIVAL | currently `archive/paper4p/`; no active theorem authority |
| `notes/` | 32 | bilateral, analytic, loop, thermal, ring, resource notes | HOLD / PARTIAL EXPORT | audited algebra → I; analysis → II; singularity → III; quotient/complexity → IV; currently classified under topical subdirectories of `notes/` |
| `misc/` | 28 | standalone diagram/model TeX and image experiments | HOLD / ARCHIVAL | currently preserved under `images/sources/`; reuse only after formula and asset audit |
| `images/` | 26 | 21 PDF and 5 PNG rendered assets | HOLD / SHARED ASSET ARCHIVE | none is required by the active Paper I build |
| `knots/` | 6 | knot/problem TeX plus one PDF | EXPORTED / ARCHIVAL | currently preserved under `notes/knots-and-loops/`; Paper III research archive; no invariant claim |
| `ideal_glass/` | 18 | independent PDF, TeX, Python package, experiment tooling | HOLD / INDEPENDENT | currently `archive/ideal_glass/`; not a Paper I dependency |
| `plans/` | 2 | historical principles and study plan | ARCHIVAL | currently `archive/plans/`; active plans live in `governance/` |
| `styles/` | 2 | arXiv and quiver styles | ARCHIVAL | currently preserved under `archive/legacy-latex-styles/`; not loaded by any canonical paper |
| `peddle/` | 1 | standalone HTML laboratory | HOLD / INDEPENDENT | currently `archive/peddle/`; not a Paper I dependency |

The fixed baseline contains no tracked `gpt/` directory.  References to `gpt/` in
planning documents are therefore treated as a general archival rule, not evidence of
missing tracked files.

## 3. Extension audit

| Extension or type | Baseline count | Treatment |
|---|---:|---|
| `.tex` | 107 | 1 canonical root entry, 13 legacy sections, remaining sources archival/HOLD as classified above |
| `.pdf` | 33 | rendered/historical assets; root PDF rebuilt from source |
| `.png` | 7 | historical/shared image assets; none loaded by active Paper I |
| `.md` | 19 | repository, restructuring, reports, and formalization notes |
| `.py` | 11 | independent ideal-glass experiment; no Paper I build dependency |
| `.lean` | 6 | experimental formalization under `revision-2`; not proof authority for Paper I |
| `.sh` | 6 | root and alternative build scripts; only root `build.sh` is canonical |
| `.sty` | 4 | historical styles; active Paper I uses installed packages only |
| `.bib` / `.bbl` | 2 / 1 | baseline root `aeg-paper.bib` plus arXiv snapshot; shared bibliography now under `bibliography/` |
| other repository/config files | 11 | license, ignores, Docker, HTML, JSON, TOML, text, toolchain, and one `.DS_Store` in the historical ideal-glass tree |

## 4. Active dependency closure

The active `paper-1/aeg-paper-1.tex` includes only the 15 files under
`paper-1/sections/` and `paper-1/appendices/`, followed by the shared
`bibliography/aeg-paper.bib`.  It includes no legacy
`sections/sec*.tex`, no alternative manuscript, no external image, and no historical
style.  This makes the Paper I build dependency closure explicit and prevents
later-paper material from re-entering through an implicit include.

## 5. Preservation rule

`ARCHIVAL`, `EXPORTED`, and `HOLD` mean “excluded from the canonical Paper I build,”
not “discarded.”  Every migrated statement remains available at its recorded current
destination, and path-only archival moves are logged so that provenance remains
recoverable.

The current noncanonical research-material layout is:

```text
images/
  sources/                         # former misc/ figure and model sources
archive/
  legacy-latex-styles/             # former styles/ third-party TeX styles
notes/
  analysis-and-calculus/
  computation-and-resources/
  foundations-and-geometry/
  knots-and-loops/                 # includes the former knots/ tree
  projective-condensation/
  thermodynamics-and-renormalization/
```

This classification changes paths only.  It does not promote any note or figure
source to theorem authority, and it does not add any file to a canonical paper build
closure.

## 6. Canonical Paper II source tree

The controlled Paper II migration adds exactly the following active source closure:

```text
paper-2/
  aeg-paper-2.tex
  sections/
    01-introduction.tex
    02-analytic-data.tex
    03-surface-operators.tex
    04-contact-analysis.tex
    05-pullback-cylinder.tex
    05-hyperbolic-analysis.tex
    06-poisson-dirichlet.tex
    07-boundary-energy.tex
    08-conclusion.tex
  appendices/
    app-A-frame-calculations.tex
    app-B-contact-calculations.tex
    app-C-poisson-fourier.tex
```

The Paper II entry point inputs only these twelve section/appendix files and the
shared bibliography at `bibliography/aeg-paper.bib`.  It imports Paper I statements by citation and restatement,
not by TeX inclusion.  No legacy `sections/sec*.tex`, archive, note, Paper III, or
Paper IV source belongs to its build dependency closure.  Formula-level provenance
and claim treatment are recorded in `paper-II-source-audit.md` and
`decisions-paper-II.md`.  The `05-pullback-cylinder.tex` file is a post-closure
addition activating the regular analytic bridge: the planar harmonic AES,
local-biholomorphic pullback, the complete cylindrical AES, and its unitary/inversion
descent.  Its branch and critical loci are expressly excluded and passed to Paper
III.

## 7. Paper III integration addendum

The current Paper III source closure is:

```text
paper-3/
  aeg-paper-3.tex
  sections/
    01-singular-aes.tex
    02-local-zero-models.tex
    03-multi-zero-constructions.tex
    04-arithmetic-zero-networks.tex
    04-parameter-discriminants.tex
    05-q4-geodesic-knots.tex
    05-polynomial-threaded-carriers.tex
    05-sextic-ll-laboratory.tex
    05-history-divisor-naturality.tex
    05-regular-tubes.tex
    06-singular-fibers.tex
    07-monodromy-and-braids.tex
    08-threading-and-knot-questions.tex
  appendices/
    app-A-regularity-and-properness.tex
    app-B-configuration-and-braid-background.tex
    app-C-affine-quandle-calculations.tex
```

The entry point inputs only these sixteen section/appendix files and the shared
bibliography at `bibliography/aeg-paper.bib`.  It imports Papers I and II by cited interfaces rather than by TeX
inclusion.  No legacy `sections/sec*.tex`, note, knot file, miscellaneous figure
source, archived manuscript, or restructuring discussion belongs to the active
Paper III TeX dependency closure.

The historical-source and Git-history audit is recorded in
`paper-III-source-audit.md`.  Its central provenance finding is that no verifiable
general multi-zero construction, defined general `E_k`, or explicit historical AEG
`E_log` construction occurs in the 249 reachable commits.  The parallel
multi-zero, logarithmic-cover, helical-tube, Morse, branch, braid-realization, and
finite-field constructions in the active manuscript are therefore
`REDERIVED HERE`; legacy files remain `ARCHIVAL` or `HOLD`.

The post-closure file `04-arithmetic-zero-networks.tex` adds a separately audited
arithmetic--automorphic layer.  It contains the exact (q=4) Hecke--Hauptmodul
singular AES, sign-character descent, and the standard relative-divisor
decomposition for a supplied monic generically square-free polynomial.  The
triangle-group uniformization and number-theoretic background are cited external
inputs; the AEG pullback and zero-network formulas are `REDERIVED HERE`.  No general
history-to-divisor functor is added to the proof closure: that arrow remains an open
problem.  This addition does not change the negative historical finding for `E_k`
or `E_log`.

The subsequent `05-q4-geodesic-knots.tex` and
`05-history-divisor-naturality.tex` additions form the sign-cover/register
extension.  The first identifies the same sign-character cover with a complete
coarse cylinder and, after retaining the hyperbolic orbifold and applying the
declared cusp filling, with the complement of `T(2,4)` in `S^3`; it also records
the operator-level periodic-orbit map and the cited zero-spine/template coding.
The second proves the quadratic and quartic supplied-register models, tagged trace,
pole cocycle, collapse kernel, and Frobenius dictionary.  Dehornoy and
Dehornoy--Pinsky supply the classical geodesic-flow inputs; the AEG cover
identification and register synthesis are rederived in the active manuscript.
Neither file changes the negative historical finding or closes the general
history-to-prime-divisor and knot-invariant problems.

The later `05-polynomial-threaded-carriers.tex` addition is a new derivation, not
a recovered historical source.  It proves the supplied family
`Im(z^2-t^m)=0` with intrinsic root thread `z^2=t^m`, its carrier topology,
discriminant/framing/braid identity, the q=4 marked toric specialization, and the
logarithmic-tangent weighted cone.  It also gives a supplied four-strand
central-extension calibration while leaving the unrestricted marked-history
coefficient-path functor open.  The arithmetic quadratic twist, radial carrier,
and path-selection choices remain explicit claim boundaries.

The subsequent `05-sextic-ll-laboratory.tex` addition is an explicit laboratory,
not a recovered historical source and not a general theory of polynomial families.
It starts from the supplied sparse sextic `P_0(x)=x^6-x`, computes its critical-value
quintic, carrier walls, six-root thread, genus-two double covers, mixed braid exact
sequence, and one arithmetic fiber.  The finite-etale Lyashko--Looijenga covering,
its degree, transposition-factorization count, Birman--Hilden lifting,
Picard--Lefschetz and symplectic monodromy, and the arithmetic Galois/endomorphism
criteria are cited classical inputs.  The `1296` points in a regular LL fiber are
coordinate-normalized monic-centered sextics; the free residual `mu_6` source
rotation has `216` orbits.  Neither number is asserted to count nonisomorphic
genus-two curves.  An exact second sheet now proves that the moduli image contains
at least two points: it has the same event polynomial as (x^6-x) but a different
genus-two Igusa reading at (t=1).  The same source gives the quotient-cover
spectral polynomial and trace--norm descent, the canonical average/zero-sum
sequence, and a monodromy-invariant forgetting variance with an exact positive
lower bound.  It does not assert constancy along arbitrary open LL paths.  Along
the two explicit slice pencils the invariant ratio is ((t-\beta)/t)^5 with
balanced regular-fiber divisor (5[\beta]-5[0]); this is a logarithmic charge, not
a finite Dirichlet energy.  The full (216)-orbit census, arithmetic/period
comparison, marked-monodromy and Hodge/Siegel-energy refinements, and every
functor from unrestricted AEG histories to the LL pullback or its Hurwitz
groupoid remain open.

The exact certificate for the displayed pair is tracked separately from the TeX
closure at
`paper-3/computations/ll-igusa-twin/verify-explicit-twin.py`, with its invocation
and claim boundary in the adjacent `README.md`.  This reproducibility artifact
does not alter the count of canonical Paper III TeX inputs.

This addendum supersedes the earlier inventory statement that Paper III consisted
only of a scope/provenance README.  It does not alter the fixed Paper I baseline
counts above.

## 8. Canonical Paper IV source tree

The current Paper IV source closure contains `paper-4/aeg-paper-4.tex`, fourteen
numbered section files under `paper-4/sections/`, and four technical appendices under
`paper-4/appendices/`, for nineteen canonical TeX files in total. It uses the shared
bibliography at `bibliography/aeg-paper.bib` and the independent finite verification
script `paper-4/scripts/verify-paper4.py`.

No legacy section, research note, archived manuscript, or governance discussion is
an active TeX dependency. The source audit, mathematical decisions, red-team review,
and closure boundary are recorded in `paper-IV-source-audit.md`,
`decisions-paper-IV.md`, `paper-IV-red-team-report.md`, and
`paper-IV-closure-report.md`.
