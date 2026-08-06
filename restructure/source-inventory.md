# Paper I Source Inventory

**Fixed baseline:** `134e70a74ed010024afa7439bd3931402731423a`  
**Inventory date:** 2026-08-06  
**Baseline population:** 207 tracked files, including 107 `.tex` sources  
**Paper I post-migration population:** 123 `.tex` sources

**Current active source closures:** Paper I: 16 canonical `.tex` files; Paper II:
13; Paper III: 13

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
| `AGENTS.md` | NEW | Discovery pointer to `restructure/AGENTS.md` |
| `paper-1/aeg-paper-1.tex` | REWRITE / CANONICAL | Sole active Paper I entry point |
| `aeg-paper.bib` | KEEP / CLEAN | Shared bibliography; used entries audited |
| `paper-1/aeg-paper-1.pdf` | REBUILD | Fresh artifact from the canonical source |
| `build.sh` | STABILIZE | Strict four-pass Paper I build |
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
`paper-4/README.md` are new relative to the fixed baseline.  Paper II has since
advanced to the canonical active source closure recorded in Section 6 below.
Paper III has likewise advanced to the active source closure recorded in Section 7.
Paper IV remains a scope and provenance record and is not an additional build entry
point.

## 2. Exhaustive baseline family classification

| Baseline family | Files | Contents | State | Canonical destination |
|---|---:|---|---|---|
| root | 11 | metadata, Paper I entry, bibliography, PDF, build | mixed, itemized above | Paper I / repository |
| `sections/` | 13 | legacy `sec01.tex`--`sec12.tex` | ARCHIVAL | audited portions rederived in `paper-1/sections/`; analytic → II; tube → III; quotient → IV |
| `restructure/` | 13 | authority, scope, dependency, status, editorial, acceptance, discussions | KEEP / AUTHORITATIVE | restructuring control plane |
| `../archive/revision-1/` | 13 | alternate eight-section TeX build | ARCHIVAL | no active theorem authority |
| `../archive/revision-2/` | 26 | alternate TeX build, PDF, Lean experiment and reports | ARCHIVAL / HOLD | formalization may be audited separately |
| `../archive/arxiv/` | 14 | prior distribution snapshot, styles, figures, bibliography | ARCHIVAL | DOI/version provenance |
| `../archive/paper4p/` | 2 | short alternative manuscript and build | ARCHIVAL | no active theorem authority |
| `notes/` | 32 | bilateral, analytic, loop, thermal, ring, resource notes | HOLD / PARTIAL EXPORT | audited algebra → I; analysis → II; singularity → III; quotient/complexity → IV |
| `misc/` | 28 | standalone diagram/model TeX and image experiments | HOLD / ARCHIVAL | reuse only after formula and asset audit |
| `images/` | 26 | 21 PDF and 5 PNG rendered assets | HOLD / SHARED ASSET ARCHIVE | none is required by the active Paper I build |
| `knots/` | 6 | knot/problem TeX plus one PDF | EXPORTED / ARCHIVAL | Paper III research archive; no invariant claim |
| `../archive/ideal_glass/` | 18 | independent PDF, TeX, Python package, experiment tooling | HOLD / INDEPENDENT | not a Paper I dependency |
| `../archive/plans/` | 2 | historical principles and study plan | ARCHIVAL | active plans live in `restructure/` |
| `styles/` | 2 | arXiv and quiver styles | KEEP / ARCHIVAL | not loaded by active Paper I |
| `../archive/peddle/` | 1 | standalone HTML laboratory | HOLD / INDEPENDENT | not a Paper I dependency |

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
| `.bib` / `.bbl` | 2 / 1 | root shared bibliography plus arXiv snapshot |
| other repository/config files | 11 | license, ignores, Docker, HTML, JSON, TOML, text, toolchain, and one `.DS_Store` in the historical ideal-glass tree |

## 4. Active dependency closure

The active `paper-1/aeg-paper-1.tex` includes only the 15 files under
`paper-1/sections/` and `paper-1/appendices/`, followed by the shared root
`aeg-paper.bib`.  It includes no legacy
`sections/sec*.tex`, no alternative manuscript, no external image, and no historical
style.  This makes the Paper I build dependency closure explicit and prevents
later-paper material from re-entering through an implicit include.

## 5. Preservation rule

`ARCHIVAL`, `EXPORTED`, and `HOLD` mean “excluded from the canonical Paper I build,”
not “discarded.”  Old paths remain intact so that an author or reviewer can compare
every migrated statement with its provenance before any future archival move.

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
shared root bibliography.  It imports Paper I statements by citation and restatement,
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
    05-regular-tubes.tex
    06-singular-fibers.tex
    07-monodromy-and-braids.tex
    08-threading-and-knot-questions.tex
  appendices/
    app-A-regularity-and-properness.tex
    app-B-configuration-and-braid-background.tex
    app-C-affine-quandle-calculations.tex
```

The entry point inputs only these twelve section/appendix files and the shared root
bibliography.  It imports Papers I and II by cited interfaces rather than by TeX
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

This addendum supersedes the earlier inventory statement that Paper III consisted
only of a scope/provenance README.  It does not alter the fixed Paper I baseline
counts above.
