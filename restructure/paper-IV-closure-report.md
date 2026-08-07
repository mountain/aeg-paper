# Paper IV Closure Report

**Paper:** *Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity*  
**Subtitle:** *From Histories and Quotients to Representation and Cost*  
**Closure date:** 2026-08-07  
**Repository baseline:** `264b7edeade754b706b575929fbbe3c8df72b5c3`  
**Status:** mathematical-review manuscript complete; publication approval pending

## 1. Canonical closure

Canonical entry point:

```text
paper-4/aeg-paper-4.tex
```

The recursive source closure contains:

- 19 canonical TeX files;
- 14 numbered sections;
- 4 technical appendices;
- 3,015 TeX source lines;
- 118,209 TeX source bytes;
- one 12-entry bibliography;
- one dependency-free finite verification script.

The manuscript compiles to:

```text
paper-4/aeg-paper-4.pdf
```

Final PDF audit:

- pages: **45**;
- bytes: **512,567**;
- SHA-256:
  `2c8c794c3e96469cad690f8ea62960b3bd24fb1b662c29fc45ddd88ca81cd1d0`;
- page size: US Letter;
- all fonts embedded;
- title, author, subject, and keyword metadata present;
- no encryption, JavaScript, or forms.

## 2. Build audit

The canonical build sequence was:

```text
pdflatex
bibtex
pdflatex
pdflatex
pdflatex
```

The final build log contains no:

- LaTeX or package warnings;
- undefined references or citations;
- duplicate labels;
- overfull or underfull boxes;
- fatal diagnostics;
- unclosed TeX groups.

The repository build interface was extended to accept `1|2|3|4|all`, with a
portable fallback from `bibtex` to `bibtex.original` in the task environment.
`bash -n build.sh` passes.

## 3. Static source audit

The canonical closure contains:

- 87 labels, all unique;
- 59 reference occurrences to 43 unique targets;
- zero missing reference targets;
- 12 bibliography keys;
- all 12 keys cited;
- zero missing or unused bibliography keys;
- no nonprinting control bytes;
- balanced theorem, proof, equation, list, table, and array environments.

The verification script passes Python byte-code compilation.

## 4. Mathematical verification

`paper-4/scripts/verify-paper4.py` passes all seven independent finite check
groups:

1. rank-one projector idempotence, trace, and determinant;
2. `PGL_2(F_q)` cardinalities, quotient fibers, and finite
   right-descent/normalizer equality for `q = 3,5,7`;
3. radix injectivity, histogram counts, and the binary length-four constants;
4. block/interleaved equality residual widths for `n <= 5`;
5. butterfly factorization and primitive NTT roots over `F_257`;
6. matrix-chain and reverse-chain arithmetic counts;
7. the finite fiber--image inequality.

The proof authority remains the manuscript. The script is a reproducibility and
regression check.

## 5. Mathematical red-team result

The red-team pass repaired the following potentially blocking boundaries before
closure:

- single right-update descent versus reversible normalizer action;
- totalization of partial arithmetic;
- equivariance of an online state encoding;
- fixed-width/prefix-free hypotheses in the bit bound;
- capacity--time versus actual dynamic memory--time;
- live configurations versus ever-computed node sets;
- characteristic-zero Horner injectivity;
- OBDD representation and order dependence;
- `GL` scalar data versus local projective butterfly quotients;
- static twiddle labels versus dynamic states;
- exact potential/pure-gauge telescoping;
- principal matrix intermediate size versus peak memory.

After repair there is no known blocking mathematical or claim-boundary finding.
The detailed record is `restructure/paper-IV-red-team-report.md`.

## 6. Visual audit

All 45 pages were rendered at 140 dpi. Five contact sheets covering every page
were inspected. Dense pages containing the principal-results table, open
problems, finite-count tables, claim ledger, cost checklist, case-study matrix,
and bibliography were inspected at enlarged resolution.

No clipped formulas, overlapping text, broken tables, missing glyphs, blank
pages, or malformed references were found.

## 7. Claim closure

Promoted to proved status under printed hypotheses:

- the bivaluation--projector and homogeneous-space theorems;
- frame-torsor and finite-field count/entropy results;
- left/right continuation descent criteria;
- contextual residual congruence and minimal exact-state theorem;
- fixed-width state and fixed-register capacity--time bounds;
- completed-set insufficiency and restricted frontier result;
- fiber--image, entropy, and word-metric comparison results;
- additive and pure-gauge exactness obstructions;
- Horner, OBDD, butterfly/NTT, matrix-chain, and reverse-chain calibrations.

Retained as frameworks or open problems:

- model-relative Pareto resource geometry;
- non-flat projective torsion and rewrite holonomy;
- multi-wire AEG;
- costed AEG-native representation changes;
- approximate residuals;
- machine-robust complexity invariants.

Explicitly excluded:

- noncommutativity implies negative curvature;
- negative curvature or hyperbolic growth implies hardness;
- exponential group growth implies exponential runtime;
- large raw history fibers imply large shared representations;
- endpoint cost differences define holonomy.

## 8. Release boundary

This closure establishes a complete mathematical-review manuscript and an
auditable repository overlay. It does not constitute author approval for public
release, DOI assignment, affiliation changes, or archival replacement. Those
steps remain explicit author decisions.
