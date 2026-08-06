# Paper III Closure Report

**Manuscript:** *Arithmetic Expression Geometry III: Singular Zero Geometry and
Tubes*

**Subtitle at original closure:** *Multi-Zero Constructions, Discriminants, and
Topological Transport*

**Current subtitle after post-closure integration:** *Branched Pullbacks,
Arithmetic Zero Networks, and Topological Transport*

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

**Post-closure notice:** Section 10 records the later arithmetic zero-network
integration and Section 11 records the q=4 knot/register extension.  Sections 1--9
retain the original eight-section, 32-page closure evidence.

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

## 10. Post-closure arithmetic zero-network amendment (2026-08-06)

This amendment records the Paper III part of the cross-paper integration.  It
supersedes the original active-section count and current subtitle, but it preserves
the 32-page artifact table and rendered review above as evidence for the original
closure run.  The active source closure now contains nine sections and three
appendices, with the new
`sections/04-arithmetic-zero-networks.tex` inserted between the multi-zero and
parameter/discriminant sections.

| Extension node | Active statement | Status and proof boundary |
|---|---|---|
| P3-S1 / P3-S2 | A holomorphic local degree `m` whose critical value lies on the target zero line gives a locally essential `2m`-prong zero and cone angle `2 pi m` | proved by local normal form and metric calculation; a controlled pullback subclass, not a classification of all singular AES germs |
| P3-S3 | A normalized `(2,4,infinity)` Hauptmodul has the printed branch data | standard external triangle-group uniformization input; normalization and citations are explicit |
| P3-S4 | The displayed square-root/Cayley/cylindrical data give the exact zero set `beta^{-1}([0,1])`, with bivalent order-two points and four-valent `4 pi` cone points over the order-four orbit | proved conditional on P3-S3; the metric and zero graph descend, while the assignment is scalar only on the sign-character cover or is a sign-line section on the full quotient |
| P3-R1 / P3-R2 | A supplied monic polynomial with nonzero discriminant defines a finite flat relative divisor; its field-prime components, geometric sheets, Galois orbits, etale locus, analytic monodromy, and good-reduction data occupy distinct layers | standard algebraic and arithmetic consequences with the printed finiteness, domain, characteristic, and integral-model hypotheses |
| P3-R3 | A functor from general marked histories to arithmetic relative zero divisors | open structural proposal; not used to prove the Hecke example |

After bivalent vertices are suppressed, the Hecke zero graph is the
`{infinity,4}` network.  Its regular locus is incomplete at the order-four points.
Upstairs completion adjoins finite-distance `4 pi` cone points; the coarse full
quotient has angle `pi` at each elliptic image and is a complete length space with
an infinite-distance cusp.  This is singular length-metric completeness, not a
smooth complete regular-AES theorem and not automatically a proper zero tube.

The local section also adds two controls on scope.  Finite Blaschke products link a
finite divisor, a real zero network, and root braids without making any of them
canonical arithmetic history data.  The example `sin(1/z)` shows that an essential
singularity can support countably many four-valent nodes and zero circles
accumulating at the puncture; it proves analytic capacity, not arithmetic
naturality or a recovered `E_log` construction.

The exact AEG branch, Cayley, metric, zero-set, cone, and sign-descent calculations
are `REDERIVED HERE`.  Hecke-group geometry, the normalized Hauptmodul, relative
divisor background, and the arithmetic reduction dictionary are cited standard
inputs.  The negative historical findings for general `E_k`, explicit AEG `E_log`,
and a recovered general multi-zero theorem remain unchanged.  Moreover,
`Z[sqrt(2)]` is a unique-factorization domain, so the `q=4` model represents
noncommuting operator paths and automorphic uniformization rather than nonunique
factorization; any factorization-theoretic version requires a separate arithmetic
family.

The final unified repository build produced the amended Paper III artifact with the
following current evidence:

| Property | Current integration artifact |
|---|---:|
| Pages | 43 |
| File size | 538,915 bytes |
| SHA-256 | `6aeb931203283f44fef2a2a27b30a92c90c0bea8a35a2205e6a8cae0b9db8f0e` |
| Active labels | 126 unique |
| Citation keys used | 17 unique |

The final log has no LaTeX or package warning, undefined reference or citation,
overfull or underfull box, duplicate label, or fatal diagnostic.  This table
supersedes only the artifact metadata for the active integration snapshot; the
original 32-page closure evidence above remains a historical record.

## 11. M-0006 q=4 knot and register amendment (2026-08-06)

The active Paper III closure now consists of eleven sections and three appendices.
Two new canonical sections are inserted after the arithmetic zero-network section:
`05-q4-geodesic-knots.tex` and `05-history-divisor-naturality.tex`.

The first proves the sign-cover signature and coarse-cylinder uniformization,
identifies the corresponding hyperbolic unit-tangent cover with
`S^3 minus T(2,4)` under the declared filling, and specializes the classical
Hecke geodesic-flow coding to the q=4 zero dessin.  The slope calculation and
covering character are internal; the lens-space compactification and flow template
are cited classical inputs.  A local four-prong cone is not identified with the
global torus link, and no new knot invariant is claimed.

The second supplies typed quadratic and quartic register towers and proves their
endpoint divisors, equivariance, trace/pole data, collapse kernel, discriminants,
arithmetic/geometric splitting, monodromy, and Frobenius cycle types.  These
registers are declared input.  The terminal endpoint divisor factors through the
projective operator and therefore does not solve the general marked-history
naturality problem.

The final M-0006 artifact evidence is:

| Property | M-0006 integration artifact |
|---|---:|
| Pages | 58 |
| File size | 635,784 bytes |
| SHA-256 | `9ceadc767f0edba48a64ead3ba50e6d37022cdbf90ea040c39bf62ee62c42bc0` |
| Canonical TeX files | 15: entry point, 11 sections, 3 appendices |
| Active labels | 193 unique |
| Reference targets | 111 unique, all present |
| Citation keys used | 19 unique, all present |

The full `pdflatex`--BibTeX resolution sequence is clean: no LaTeX, package, or
BibTeX warning; no undefined reference or citation; no duplicate label; no overfull
or underfull box; and no fatal diagnostic.  All 58 pages were rendered in contact
sheets.  The title, three-page contents, both new sections, long equations and
tables, appendices, bibliography, and final claim ledger received enlarged visual
inspection; no clipping, collision, broken glyph, blank content page, or unreadable
element was found.  Independent red-team review reports zero blocking and zero
major mathematical findings after repair.

## 12. M-0007 polynomial threaded-carrier amendment (2026-08-06)

The active Paper III closure now consists of twelve sections and three appendices,
or sixteen canonical TeX files including the entry point.  The new section
`05-polynomial-threaded-carriers.tex` is inserted between the q=4 geodesic-knot
section and the supplied-register section.

The section proves that one supplied polynomial may simultaneously define a real
carrier by `Im(P)=0` and an embedded finite root thread by `P=0`.  For
`P_m(z,t)=z^2-t^m`, the carrier is a compact connected neat surface with four
boundary components, `2m` Morse saddles, Euler characteristic `-2m`, and genus
`m-1`; it is not called a proper zero tube.  The root thread closes to `T(2,m)`,
and discriminant order, logarithmic period, braid exponent, negative carrier
framing, and negative half Euler characteristic agree with the printed
orientation conventions.

At q=4, the marked peripheral lattice and deck involution recover the two-coset
toric divisor `u^2=t^4`.  The marked compactified sign cover further recovers the
same binomial as the cusp section in its logarithmic-tangent graded ring, while
its weighted Hopf circle bundle recovers the filled `T(2,4)` cusp link.  The
arithmetic split/nonsplit descent and radial carrier remain declared choices.

A separate supplied four-root calibration identifies the q=4 unit-tangent
central extension with the pullback of the four-braid center extension.  Its
invariant integer relation character satisfies the normalized discriminant-period
identity and, in the Lyndon--Hochschild--Serre five-term sequence, transgresses to
the unit-tangent Euler extension class.  This is a group-extension transgression,
not a Serre transgression over the circle, and the character is not Paper I's
affine torsion.  The coefficient paths are supplied rather than history-natural;
the inverse full-twist closure `T(4,-4)` is not identified with the cusp link
`T(2,4)`, and no new knot invariant is claimed.

The final unified repository build produced the following active artifact:

| Property | M-0007 integration artifact |
|---|---:|
| Pages | 69 |
| File size | 704,239 bytes |
| SHA-256 | `f094bc5e70739fc0144fcefff78a877f03d420f39f2475be12aed6d938a9dd9e` |
| Canonical TeX files | 16: entry point, 12 sections, 3 appendices |
| Active labels | 266 unique |
| Reference targets | 144 unique, all present |
| Citation keys used | 20 unique, all present |

The final `pdflatex`--BibTeX resolution sequence is clean: no LaTeX, package, or
BibTeX warning; no undefined reference or citation; no duplicate label; no
overfull or underfull box; and no fatal diagnostic.  All 69 pages were rendered
in contact sheets.  Enlarged review covered the title and abstract, the complete
threaded-carrier section, the logarithmic-tangent and LHS proofs, the conclusion,
bibliography, and final claim ledger; no clipping, collision, broken glyph, blank
content page, or unreadable element was found.  Independent mathematical and
claim-boundary reviews report zero blocking and zero major findings after repair.

## 13. M-0008 sextic LL laboratory amendment (2026-08-06)

Migration M-0008 inserts `05-sextic-ll-laboratory.tex` after the polynomial
threaded-carrier section.  The canonical Paper III closure is therefore now 17
TeX files: the entry point, 13 sections, and 3 appendices.

The new section directly computes the event polynomial for (P_0=x^6-x), proves
the spanning-star (B_6) monodromy for the displayed pencil, and constructs its
compatible real carrier, six-root thread, mixed-braid pullback, and genus-two
mapping tori.  LL finiteness and degree, the (1296)-sheet normalized fiber and
(216) residual source-rotation orbits, caustic/Maxwell multiplicities,
Birman--Hilden and symplectic results, and the arithmetic Galois/endomorphism
criteria are explicitly classical inputs.  Neither (1296) nor (216) is a count
of nonisomorphic curves.

The mixed exact sequence replaces any putative canonical (B_5\to B_6) map.
Carrier wall crossings, root collisions, and spectral degenerations are not
identified.  The isomorphism (\operatorname{Sp}_4(\mathbb F_2)\cong S_6) is a
common finite target, not an elementwise identification of arithmetic and
topological monodromy.  The LL--Igusa twin test and selection of an LL sheet or
coefficient path by an unrestricted AEG history remain open.

The canonical `./build.sh 3` release build and visual audit give:

| Property | M-0008 integration artifact |
|---|---:|
| Pages | 78 |
| File size | 809,341 bytes |
| SHA-256 | `d5bf667041dc6ce52189f840a5a691c4d8c6eed1126705911937a907fb74f816` |
| Canonical TeX files | 17: entry point, 13 sections, 3 appendices |
| Active labels | 322, all unique |
| Reference targets | 157, all resolved |
| Citation keys used | 30, all present in the 48-key shared bibliography |
| Build-log status | Clean: no warning, undefined reference/citation, or over/underfull box diagnostic |
| Visual-review status | All 78 pages rendered; the repaginated manuscript, new figure, exact diagrams, claim ledger, and bibliography were inspected with no clipping, collision, blank content page, or broken glyph found |

This amendment does not supersede the verified M-0007 artifact above.  It records
the later M-0008 release snapshot and its stricter mathematical and provenance
boundary.

## 14. M-0009 explicit LL--Igusa twin source amendment (2026-08-06)

The source now contains an exact second LL sheet over (Q_0) whose common (t=1)
slice is separated from that of (P_0) by an absolute ratio built from the
quadratic Igusa--Clebsch invariant and the discriminant.
Accordingly, P3-L9 is proved: the genus-two moduli reading does not factor through
the event polynomial on this finite fiber.

The same source theorem package records the degree-(216) sheet observable's norm
spectral polynomial and trace--norm descent, the canonically split averaging
sequence, and its permutation-monodromy-invariant finite-fiber variance.  The
explicit pair gives an exact positive lower bound at (Q_0), without implying
constancy along arbitrary open LL paths.  For the two explicit slice pencils the
ratio is ((t-\beta)/t)^5, supported by the balanced divisor
(5[\beta]-5[0]) at regular fibers.  This is a logarithmic charge, not a finite
Dirichlet energy.

The closure boundary is deliberately narrower than a census.  P3-L10 remains
open for enumeration of all (216) source-rotation orbits, same-field Frobenius
comparison, reduced Siegel periods, and marked-monodromy/Hurwitz grouping.  The
Hodge- or Siegel-metric energy comparison and the unrestricted
history-to-LL-sheet arrow also remain open.  Neither (1296) nor
(216) is promoted to a count of nonisomorphic curves.

The table in Section 13 remains the historical M-0008 artifact.  The completed
M-0009 release closure is:

| Property | M-0009 integration artifact |
|---|---:|
| Pages | 83 |
| File size | 859,662 bytes |
| SHA-256 | `f9cf579734cbf2a5c70794470ba3baf3b79c2fc1144926513f291b7a2462c858` |
| Canonical TeX files | 17: entry point, 13 sections, 3 appendices |
| Active labels | 351, all unique |
| Reference targets | 175, all resolved |
| Citation keys used | 36, all present in the 53-entry shared bibliography |
| Build-log status | Clean: no warning, undefined reference/citation, or over/underfull box diagnostic |
| Exact-computation status | Dependency-free verification script passes all printed resultant, scaling, Clebsch, discriminant, and moving-divisor checks |
| Visual-review status | All 83 pages rendered; higher-resolution checks covered the new twin/energy pages and bibliography, with no clipping, collision, blank content page, unreadable element, or broken glyph found |

This closes the M-0009 source, computation, static, build, and visual gates while
leaving P3-L10 and the unrestricted history-naturality questions open.
