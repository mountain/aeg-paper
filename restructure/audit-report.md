# Papers I--III Restructuring Audit Report

**Baseline commit:** `134e70a74ed010024afa7439bd3931402731423a`  
**Baseline date:** 2026-08-06  
**Audit date:** 2026-08-06  
**Canonical baseline entry point:** `aeg-paper.tex`  
**Canonical target entry point:** `paper-1/aeg-paper-1.tex`

## 1. Scope of the audit

The audit covered all tracked paths in the baseline archive, the root manuscript and
its twelve legacy section files, alternative manuscript trees, bibliography, styles,
figures, build scripts, research notes, and all authoritative files under
`restructure/`.  The detailed path classification is maintained in
`source-inventory.md`; movement and claim treatment are maintained in
`migration-log.md`.

The baseline contains 207 tracked paths and 107 TeX sources.  Several independent
build trees coexist:

- root `aeg-paper.tex`;
- `../archive/revision-1/main.tex`;
- `../archive/revision-2/main.tex`;
- `../archive/arxiv/main.tex`;
- `../archive/paper4p/aeg.tex`;
- legacy `aeg-lemma.tex`;
- standalone material under `misc/`, `notes/`, `knots/`, and `../archive/ideal_glass/`.

The audited root entry point was subsequently moved to `paper-1/aeg-paper-1.tex` after
the structural migration was explicitly authorized.

## 2. Baseline build

The unmodified baseline build command was:

```bash
bash build.sh
```

The script invoked `pdflatex`, `bibtex`, and two further `pdflatex` passes.  On the
available TeX Live 2023 installation it returned status 1 because
`stmaryrd.sty` was unavailable.  Since the script had neither a shebang nor
`set -e`, it continued after the first failure.  The repository already contained a
stale `aeg-paper.pdf`; its presence was therefore not evidence of a successful local
build.

Baseline artifact metadata before the attempted build:

| Property | Value |
|---|---:|
| Pages | 54 |
| Page size | US letter (612 × 792 pt) |
| File size | 495,462 bytes |
| PDF version | 1.7 |

Observed fatal diagnostic:

```text
LaTeX Error: File `stmaryrd.sty' not found.
Fatal error occurred, no output PDF file produced.
```

Docker was not available in the execution environment (`docker: command not found`).
The final task report must therefore distinguish the verified local build from the
unexecuted container path.

## 3. Baseline mathematical conflicts

The following release-relevant conflicts were found before modification:

1. The legacy definition “every left child is a leaf” was orientation-dependent and
   inconsistent with examples; it must be replaced by the dependency-poset/spine
   classification.
2. Operand-slot mirror, temporal reversal, and inverse path were not defined as
   separate operations.
3. The root manuscript did not contain bilateral projective semantics or the
   `PGL_2` generation theorem, although these are required to place the affine theory.
4. Function composition, chronological words, and matrix multiplication were not
   governed by one explicit convention.
5. The legacy regular-AES definition conflated a framed directional law with an
   intrinsic eikonal equation.
6. The hyperbolic model was verified directly but not derived from a normalized
   invariant affine metric; generalized curvature and Laplacian normalizations were
   not fully audited.
7. A regular-zero theorem was absent.  The isolated-zero disc model was described as
   an AES without fully recording its non-differentiable center.
8. ACS torsion was centered on path reversal rather than arbitrary compatible
   two-history comparison, and its direct-path sign convention was not fixed.
9. Open endpoint defect, closed commutator holonomy, and infinitesimal contact
   curvature were related narratively but not kept mathematically distinct.
10. A complete arithmetic-holomorphic section remained in Paper I although the
    contact structure alone does not choose a unique horizontal complex structure.
11. Tube, knot, projective-condensation, and complexity programmes were not fully
    separated from the foundational manuscript.
12. The theorem environment printed examples as “Theorem”.
13. The root README called the upper-half-plane model `E_1`, whereas the manuscript
    used `E_0`; the model index had no invariant definition.
14. The DOI badge did not distinguish the archived DOI version from the active
    restructuring manuscript.

## 4. Baseline editorial and repository findings

- `aeg-lemma.tex` refers to absent `sections/sec13.tex` through `sec17.tex` and uses a
  suspect style path; it is retained for later audit and excluded from Paper I.
- `revision-1`, `revision-2`, `arxiv`, and `paper4p` are retained as historical or
  alternative manuscripts, not parallel canonical sources.
- The root paper loaded `stmaryrd` twice but did not use its distinctive symbols.
- Semantic labels were incomplete and several legacy labels encoded editorial prose
  rather than mathematical objects.
- Generated PDFs are present in the historical tree.  Their provenance is retained,
  but successful compilation must be established from source for the target paper.

## 5. Target audit gates

The target manuscript is accepted for mathematical review only after:

- all required theorem labels in `02-paper-I-outline.md` occur in the active source;
- all P0 decisions are recorded with exact conventions and proof locations;
- analytic, tube, projective-condensation, and complexity developments are absent
  from the Paper I theorem sequence;
- labels, references, citations, and figure paths pass static checks;
- a fresh non-stale PDF is produced by the active build;
- the abstract and conclusion are traceable to proved body results;
- independent mathematical and scope reviews are recorded.

Final evidence is appended to this report after integration and review.

## 6. Final integration evidence

The active ten-section manuscript and five appendices now build to a fresh 60-page
US-letter PDF.  After the directory migration, the final artifact is 575,584 bytes
and has SHA-256
`98a8a9a2f35cbb2252cfc9576d447ca427a27f95815deaab03d3e3c9f7c04911`.

The final active-source audit found 166 unique labels, no duplicate or missing
references, no missing citation keys, and eight reproducible TikZ figures.  The
LaTeX and BibTeX logs contain no warnings, undefined references, overfull boxes, or
underfull boxes.  Poppler rendered all 60 pages; the title, abstract, contents, every
figure page, appendices, and bibliography were visually checked.

All named theorem/definition slots from the Paper I outline are in the active source.
Independent algebra, geometry, torsion/contact, whole-manuscript mathematics, and
scope reviews report zero remaining blocking defects.  The detailed evidence and
theorem inventory are in `paper-I-closure-report.md`.

The result is classified as a **mathematical-review manuscript**, not an
author-approved public release.  Docker was unavailable, and author metadata and the
relationship to the earlier Zenodo DOI still require human approval.

## 7. Paper II integration evidence

Paper II was integrated from the fixed repository baseline `61ff60d` under the
task-specific authority `paper-II-source-audit.md`.  Its active entry point is
`paper-2/aeg-paper-2.tex`; it inputs eight canonical section files, three canonical
appendix files, and the shared bibliography.  It has no TeX dependency on a legacy
section, alternative revision, note, Paper III source, or Paper IV source.

The final cold build used the same strict `pdflatex`, BibTeX, `pdflatex`, `pdflatex`
sequence as Paper I and produced a 39-page US-letter PDF.  The artifact is 463,026
bytes with SHA-256
`489d21841f56e4a84f9c9179b804c4e6d2207d23c8367d98e00215829fb7bab3`.
The active Paper II source contains 198 unique labels, with no duplicate or missing
reference target and no missing citation key.  The final LaTeX and BibTeX logs contain
no warning, undefined reference or citation, fatal diagnostic, overfull box, or
underfull box.  Poppler rendered all 39 pages; the title, contents, analytic-branch
diagram, displayed equations, theorem page breaks, comparison table, appendices, and
bibliography were inspected for clipping and collisions.

Independent reviews separately recomputed the surface adjoints and drift,
Cauchy--Riemann factorizations, contact measure and Reeb twist, balanced-measure
gauge, logarithmic and affine--Appell families, hyperbolic normalization, Poisson
kernel, boundary uniqueness, Dirichlet-to-Neumann scale, energy constant, and
assignment-only classification.  A separate scope/provenance review confirmed the
Paper I to Paper II dependency and absence of Paper III/IV theorem leakage.  All
blocking findings were repaired; the final reviews report no blocking mathematical,
scope, or provenance defect.

Migration M-0003, status change S-0006, the Paper II decision record, and
`paper-II-closure-report.md` provide the detailed claim treatment and closure
evidence.  Paper II is a **mathematical-review manuscript**, not an author-approved
public release.  General Green kernels, spectral completeness, contact-boundary
representations, singular continuation, and clean-container verification remain
outside this closure.

## 8. Paper III integration evidence

Paper III was integrated from baseline
`24c1df0dd1feb38b691a50a6c6dc7a6aa613248a` under the authority of the
restructuring specifications and the task-specific provenance record
`paper-III-source-audit.md`.  Its active entry point is
`paper-3/aeg-paper-3.tex`; it inputs eight canonical section files, three canonical
appendix files, and the shared root bibliography.  It has no TeX dependency on a
legacy section, note, knot file, working discussion, or archived manuscript.

The historical audit covered all 249 commits reachable from the local refs and found
no certifiable general `E_k`, `E_log`, or multi-zero construction.  The active
parallel, logarithmic-cover, helical, Morse, branch, braid, and finite-field models
are new audited derivations rather than silent migrations under unsupported names.
Migration M-0004, status change S-0007, the Paper III decision record, and the
closure report record their exact treatment.

A cold Paper III build from an isolated source copy produced a 32-page US-letter PDF.
The artifact is 453,986 bytes with SHA-256
`a071d447ac751cc95801d60597b6cfc885675fa0de61b8a29e91bfe9ca43d13f`.
An isolated `./build.sh all` invocation produced Papers I--III at 60, 39, and 32
pages.  The Paper III active source has 100 unique labels, no duplicate or missing
reference, and no missing citation key.  Its final LaTeX and BibTeX logs contain no
warning, undefined reference or citation, fatal diagnostic, overfull box, or
underfull box; all fonts are embedded.

Poppler rendered all 32 pages.  Four contact-sheet passes and targeted full-page
inspection covered the title, claim ledger, three TikZ figures, theorem page breaks,
long tables, exact twisted state-sum convention, appendices, and bibliography.  No
clipping, collision, blank content page, or unreadable element was found.

Independent provenance, mathematical, LaTeX/static, and rendered-layout reviews
found and repaired the translation-coordinate notation, root-incidence codimension,
multi-parameter branch wording, vertical-orientation hypothesis, logarithmic deck
terminology, basepoint and relabeling gauges, and exact
Carter--Elhamdadi--Saito group-ring state sum.  Final review reports no blocking or
major defect.

Paper III is a **mathematical-review manuscript**, not an author-approved public
release.  Intrinsic thread selection, AEG Markov descent, a new knot invariant, and
separation beyond Alexander/Burau remain explicitly open.  Author metadata,
DOI/version policy, Docker reproduction, and publication approval remain human
release actions.

## 9. Post-closure arithmetic--automorphic integration evidence

On 2026-08-06, Papers I--III received the coordinated arithmetic--automorphic
extension recorded in Migration M-0005 and in the three post-closure amendments.
The final repository build used `./build.sh all`, whose per-paper sequence is
`pdflatex`, BibTeX, and three resolving `pdflatex` passes.  The extra resolving pass
ensures that a cold Paper III build reaches a stable contents and label state.

| Paper | Pages | File size | SHA-256 | Unique labels | Unique citations |
|---|---:|---:|---|---:|---:|
| I | 63 | 604,976 bytes | `bbcb16fa720c26f837555ff2387ee7205884a8f07963c6f949e19cb636710fd5` | 177 | 6 |
| II | 44 | 497,142 bytes | `a7f76c6c834ac20fb6ee1780366fe819b1a0e0802d6d6facdfd4e49d152d9592` | 227 | 4 |
| III | 43 | 538,915 bytes | `6aeb931203283f44fef2a2a27b30a92c90c0bea8a35a2205e6a8cae0b9db8f0e` | 126 | 17 |

All three final logs are free of LaTeX and package warnings, undefined references
or citations, duplicate labels, overfull or underfull boxes, and fatal diagnostics.
All PDFs are US letter, PDF 1.5, with embedded fonts.  `bash -n build.sh` and
`git diff --check` pass.  The final mathematical red-team review reports zero
blocking and zero major findings after separating the upstairs `4 pi` cone from the
coarse quotient angle `pi`, computing the exact sign character, and proving the
relative-prime normalization statement on the finite-etale locus.

This section supersedes only the active artifact metadata and integration-level QA.
Sections 6--8 remain the preserved evidence for the original Paper I, II, and III
closure snapshots.

## 10. M-0006 q=4 knot and finite-register integration evidence

Migration M-0006 adds two canonical Paper III sections and only downstream
interface wording to Papers I and II.  The final repository build used
`./build.sh all`, with `pdflatex`, BibTeX, and three resolving `pdflatex` passes per
paper.

| Paper | Pages | File size | SHA-256 | Unique labels | Unique refs | Unique citations |
|---|---:|---:|---|---:|---:|---:|
| I | 63 | 604,948 bytes | `9144f603f9452f09ecaf9e9c32e15029b33992cf0837073580a9d3f7188de2d9` | 177 | 88 | 6 |
| II | 44 | 497,273 bytes | `751af9456607741da051e22c39c126cce280c2a4427fe88750d3023e7eb7fc04` | 227 | 97 | 4 |
| III | 58 | 635,784 bytes | `9ceadc767f0edba48a64ead3ba50e6d37022cdbf90ea040c39bf62ee62c42bc0` | 193 | 111 | 19 |

Every reference target and citation key exists; every label is unique within its
paper.  All three canonical LaTeX and BibTeX logs are free of warnings, undefined
references or citations, overfull or underfull boxes, and fatal diagnostics.  The
PDFs are US letter, PDF 1.5, with embedded fonts.  `bash -n build.sh` and
`git diff --check` pass.

Paper III's 58 pages were all rendered and inspected through full contact sheets,
with enlarged review of the title, contents, both new theorem sections, appendices,
bibliography, and claim ledger.  The changed conclusion pages in Papers I and II
were also rendered.  No visual defect was found.  Independent mathematical red-team
review reports zero blocking and zero major findings.  The remaining general
history-to-divisor functor, marked-history knot enhancement, and new knot invariant
are explicitly open.
