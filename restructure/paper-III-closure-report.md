# Paper III Closure Report

**Manuscript:** *Arithmetic Expression Geometry III: Singular Zero Geometry and
Tubes*

**Subtitle:** *Multi-Zero Constructions, Discriminants, and Topological Transport*

**Status:** Mathematical-review manuscript

**Closure date:** 2026-08-06

**Audited baseline:** `24c1df0dd1feb38b691a50a6c6dc7a6aa613248a`

This report records the result of the Paper III writing and restructuring task.  It
should be read with `paper-III-source-audit.md`, `decisions-paper-III.md`,
`source-inventory.md`, `migration-log.md`, `05-mathematical-status.md`, and
`audit-report.md`.  “Closed” below means closed at the hypotheses and interfaces
printed in the mathematical-review manuscript.  It does not mean that the open
thread-selection, Markov-descent, or beyond-Alexander/Burau programmes have been
solved, or that a public release has been authorized.

## 1. Acceptance outcome

- **Source and dependency closure:** closed.  The active entry point contains eight
  sections and three appendices, imports Papers I and II by explicit interfaces, and
  uses only the shared root bibliography beyond its own source tree.  No legacy
  section, note, knot file, working discussion, or archived manuscript is an active
  TeX dependency.
- **Mathematical closure:** closed for the stated conformal, multi-zero, incidence,
  proper-tube, helical, singular-event, finite-root, logarithmic-gauge, and affine
  novelty-filter results.  Every global statement displays the needed
  transversality, properness, boundary, orientation, rank, square-free, or finite-field
  hypothesis.
- **Claim-status and provenance closure:** closed.  Migration M-0004, status change
  S-0007, the Paper III decision record, and the source audit record all imports,
  new derivations, rejected promotions, and retained open questions.
- **Editorial and rendered closure:** closed for mathematical review.  The abstract,
  claim ledger, eight-section argument, three calculation appendices, figures, and
  bibliography were checked against the proved body results and visually inspected.
- **Release status:** not an author-approved public release.  Author metadata,
  DOI/version policy, clean-checkout reproduction of the eventual commit, and final
  publication judgment remain human release actions.

## 2. Theorem and construction inventory

| Result | Active location | Closure |
|---|---|---|
| zero-object hierarchy and ambient AEG family | Sections 1 and 4 | defined; seven levels kept distinct |
| conformal and singular realization | Section 2; Appendix A | proved with `mu != 0` |
| parallel finite/countable and logarithmic-cover zero models | Section 3; Appendix A | proved; no historical `E_k` or `E_log` classification claim |
| rank-`r` parameterized zero-section theorem | Section 4; Appendix A | proved; properness and relative boundary hypotheses explicit |
| structural discriminant and escape to infinity | Section 4; Appendix A | defined and proved example; general stratification open |
| proper real-zero tube theorem | Section 5 | proved; global vertical orientation required for the torus conclusion |
| compact helical zero tube | Section 5; Appendices A--B | proved; component permutation, annuli, deck shift, and boundary class computed |
| real Morse events and complex simple branch | Section 6; Appendix B | proved examples/local model; no universal AEG metric normal form claimed |
| finite-root covering and braid monodromy | Section 7; Appendix B | proved for square-free monic complex fields; rank-one real zeros excluded |
| realization of every braid on the Paper II model | Section 7 | proved for the complete basic hyperbolic AES with `mu,lambda > 0`; universality is not an invariant |
| logarithmic root transport | Section 7; Appendix B | proved as a principal cover; lift gauge and relabeling laws explicit |
| finite threads and Markov gate | Section 8; Appendix B | definition and necessary conditions fixed; intrinsic selection and descent open |
| affine/Alexander novelty filters | Section 8; Appendix C | stateless scalar collapse and ordinary exactness proved |
| resonant twisted affine class | Section 8; Appendix C | nonzero finite-field cohomology class proved for arbitrary one-cochains |
| planar twisted state-sum collapse | Section 8; Appendix C | exact CES weights printed; value is the coloring count times `[0]` |
| variable-multiplier anomaly and figure-eight word | Section 8; Appendix C | explicit computations only; no associator or generic knot-invariant claim |

## 3. Mathematical decisions closed

The Paper III decision record fixes the following release-relevant distinctions:

1. historical `E_k` and `E_log` names do not supply theorem authority;
2. conformal existence is separated from completeness, rigidity, and naturality;
3. total zero set, smooth incidence, proper tube, embedded tube, threaded tube,
   braid closure, and knot invariant are seven different objects;
4. tube means a surjective proper submersion, with neat relative boundary data;
5. rank-one real assignments have curve zeros, while rank-two complex fields have
   finite roots and Artin braid monodromy;
6. critical, boundary, singular/metric, domain/category, and nonproper escape are
   separate discriminant mechanisms;
7. the real-tube torus theorem requires a smooth orientation of the vertical tangent
   bundle; without it a Klein-bottle zero tube is possible;
8. the helical family is the central explicit proper tube, with all transport
   conventions declared;
9. real Morse changes and complex branching are not conflated;
10. every-braid realization is a function-theory universality theorem, not a knot
    invariant;
11. logarithmic integers carry lift gauge, and cycle data carry relabeling gauge;
12. a thread is a declared finite-sheeted one-dimensional multisection, not a
    canonical consequence of a curve tube;
13. fixed affine conjugation is exactly Alexander-quandle data;
14. the resonant twisted class is cohomologically nonzero but planar-state-sum
    trivial beyond coloring count;
15. Markov descent and any separation beyond Alexander/Burau remain gated open
    problems;
16. the figure-eight polynomial is a specified free-word/relator calculation, not a
    generic invariant.

## 4. Build and static validation

The repository command `./build.sh 3` executes the strict sequence

```text
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-3.tex
bibtex aeg-paper-3
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-3.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-3.tex
```

A cold build in an isolated source copy, with all Paper III auxiliary and generated
files excluded before the first pass, succeeded.  A second isolated invocation of
`./build.sh all` built Papers I--III to 60, 39, and 32 pages respectively.

Final Paper III artifact:

| Property | Value |
|---|---:|
| PDF | `paper-3/aeg-paper-3.pdf` |
| Pages | 32 |
| Page size | US letter, 612 x 792 pt |
| PDF version | 1.5 |
| File size | 453,986 bytes |
| SHA-256 | `a071d447ac751cc95801d60597b6cfc885675fa0de61b8a29e91bfe9ca43d13f` |

Static checks:

- 100 labels and 100 unique labels;
- 58 unique `ref`, `eqref`, `pageref`, or `autoref` targets, all present;
- 10 citation keys, all present in the shared root bibliography;
- no control character, non-ASCII byte, or unresolved TODO/FIXME marker in the
  active TeX source;
- no LaTeX or BibTeX warning, undefined reference or citation, fatal diagnostic,
  overfull box, or underfull box in the final logs;
- all PDF fonts embedded;
- `bash -n build.sh` and `git diff --check` pass.

## 5. Rendered review

The final 32-page artifact was rendered with Poppler at 110 dpi.  Every page was
included in four contact-sheet passes.  Full-page review covered the title and
abstract, claim ledger, conformal and multi-zero formulas, discriminant table,
proper-tube theorem and Klein-bottle counterexample, helical and Morse diagrams,
finite-root theorem, logarithmic gauge calculation, exact twisted state-sum
convention, Markov gate, all three appendices, the figure-eight calculation table,
and the bibliography.  No clipping, collision, unreadable figure label, malformed
equation, blank content page, or broken page transition was found.

## 6. Independent review record

Three separate review tracks covered:

- the full current tree and all 249 commits reachable from the local refs, including
  negative provenance findings for `E_k`, `E_log`, and a historical general
  multi-zero theorem;
- every principal formula and theorem hypothesis, including conformal realization,
  Ehresmann properness, vertical orientability, helical orbit counts, Morse and branch
  models, finite-root properness, braid realization, logarithmic gauge, affine
  conjugation, resonant cohomology, and the Carter--Elhamdadi--Saito state sum;
- LaTeX structure, labels, references, citations, typography, fonts, figures,
  bibliography, isolated cold build, and rendered-page layout.

The reviews initially found two high-severity wording/notation errors: the affine
translation coordinate was denoted by the standard matrix-trace symbol, and a
real-parameter root incidence was called complex codimension one.  They also found
one genuinely false theorem under a weak orientation reading: a family with
orientation-reversing monodromy can have a Klein-bottle zero tube.  The manuscript
now uses an explicit translation projection, states real codimension two, requires a
smooth global vertical orientation, and prints the Klein-bottle counterexample.

Further repairs made the multi-parameter branch coordinates, basepoint conjugacy,
principal logarithmic action, cycle-sum relabeling, interval return map, relative
thread definition, field/nonunit distinction, figure-eight presentation, and exact
Alexander-numbered twisted weights explicit.  Final review disposition: no blocking
or major mathematical, scope, provenance, build, or layout defect.

## 7. Provenance closure

The historical audit found no certifiable general `E_k`, `E_log`, or multi-zero AEG
construction in the current tree or the 249 reachable commit trees.  The earliest
tube materials propose ambient families or pictures but do not supply a smooth
zero-incidence topology, properness, threading, or knot theorem.  The active
parallel, logarithmic-cover, helical, Morse, branch, braid, and finite-field results
are therefore marked `REDERIVED HERE`.  All legacy notes, knot files, figures,
archives, and working discussions remain preserved but outside the active TeX
dependency closure.

## 8. Deliberately open frontier

The closure does not include a canonical classification of singular AEG germs,
complete or history-natural multi-zero metrics, a canonical Whitney stratification
of the structural discriminant, intrinsic or functorial thread selection, a general
real-assignment-to-braid functor, a Markov-normalized history decoration, a new
classical knot invariant, or a closure-level separation beyond Alexander/Burau.
These are stated as open problems rather than inferred from the explicit tubes.

## 9. Remaining human release actions

Before treating Paper III as a public release candidate, an author should:

1. build the submitted commit in a clean checkout and with the retained Dockerfile;
2. approve author, affiliation, date, title, subtitle, and version metadata;
3. approve the corrected provenance status of the historical `E_k` and `E_log`
   labels;
4. decide the DOI/version relationship among Papers I--III and earlier archives;
5. review the final branch or pull request and authorize any public release state.
