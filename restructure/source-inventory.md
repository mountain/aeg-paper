# Paper I Source Inventory

**Fixed baseline:** `134e70a74ed010024afa7439bd3931402731423a`  
**Inventory date:** 2026-08-06  
**Baseline population:** 207 tracked files, including 107 `.tex` sources  
**Post-migration population:** 122 `.tex` sources (15 new Paper I chapter/appendix files)

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
| `aeg-paper.tex` | REWRITE / CANONICAL | Sole active Paper I entry point |
| `aeg-paper.bib` | KEEP / CLEAN | Shared bibliography; used entries audited |
| `aeg-paper.pdf` | REBUILD | Fresh artifact from the canonical source |
| `build.sh` | STABILIZE | Strict four-pass Paper I build |
| `aeg-lemma.tex` | HOLD | References absent sections 13--17; no Paper I dependency |

The new canonical source tree is exactly:

```text
sections/foundations/
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
  appendices/app-A-conventions.tex
  appendices/app-B-affine-cocycles.tex
  appendices/app-C-hyperbolic-calculations.tex
  appendices/app-D-acs-contact.tex
  appendices/app-E-equality-neutrality.tex
```

The later-paper destination records `paper-II/README.md`, `paper-III/README.md`, and
`paper-IV/README.md` are new.  They define scope and provenance only; they are not
additional build entry points.

## 2. Exhaustive baseline family classification

| Baseline family | Files | Contents | State | Canonical destination |
|---|---:|---|---|---|
| root | 11 | metadata, Paper I entry, bibliography, PDF, build | mixed, itemized above | Paper I / repository |
| `sections/` | 13 | legacy `sec01.tex`--`sec12.tex` | ARCHIVAL | audited portions rederived in `sections/foundations/`; analytic → II; tube → III; quotient → IV |
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

The active `aeg-paper.tex` includes only the 15 files under
`sections/foundations/`, followed by `aeg-paper.bib`.  It includes no legacy
`sections/sec*.tex`, no alternative manuscript, no external image, and no historical
style.  This makes the Paper I build dependency closure explicit and prevents
later-paper material from re-entering through an implicit include.

## 5. Preservation rule

`ARCHIVAL`, `EXPORTED`, and `HOLD` mean “excluded from the canonical Paper I build,”
not “discarded.”  Old paths remain intact so that an author or reviewer can compare
every migrated statement with its provenance before any future archival move.
