# Arithmetic Expression Geometry

This repository contains the manuscripts, notes, figures, and build tooling for the
Arithmetic Expression Geometry (AEG) research programme.  AEG studies arithmetic
expressions through their ordered evaluation histories.  An unmarked sequential tree
first requires a choice of accumulator; the resulting fully marked planar tree is
equivalent to a bounded marked history.  From that history, operator evaluation and
charge/geometric shadows form separate branches, and only an operator together with
an initial value determines an endpoint.  The repository keeps these levels distinct.

The active manuscripts are:

> **Arithmetic Expression Geometry I: Foundations**  
> *Sequential Histories, Affine Flow, Torsion, and Contact Geometry*

> **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
> *Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity*

> **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
> *Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

Their canonical entry points are [`paper-1/aeg-paper-1.tex`](paper-1/aeg-paper-1.tex),
[`paper-2/aeg-paper-2.tex`](paper-2/aeg-paper-2.tex), and
[`paper-3/aeg-paper-3.tex`](paper-3/aeg-paper-3.tex).  All four papers have top-level
directories: [`paper-1/`](paper-1/), [`paper-2/`](paper-2/),
[`paper-3/`](paper-3/), and [`paper-4/`](paper-4/).  The governing scope,
mathematical-status register, migration map, and acceptance criteria are under
[`restructure/`](restructure/README.md).

## Version and DOI

[![Earlier DOI version](https://zenodo.org/badge/DOI/10.5281/zenodo.18887455.svg)](https://doi.org/10.5281/zenodo.18887455)

The Zenodo DOI above identifies an **earlier archived version** of the manuscript.  It
does not automatically identify the active restructured Paper I.  The active source
states its own date and review status; a future release must receive explicit author
approval before its DOI metadata is changed.

## Four-paper architecture

1. **Paper I — Foundations.** Sequential histories, bilateral projective semantics,
   the affine sector, the (q=4) Hecke arithmetic sublanguage, cocycles, continuous
   flow, the basic hyperbolic model, complete regular-zero rigidity, global torsion,
   and contact curvature.
2. **Paper II — Hyperbolic Real Function Theory.** Horizontal complex and analytic
   structures, operator domains, kernels, boundary problems, planar and cylindrical
   holomorphic pullbacks, and spectral questions.
3. **Paper III — Singular Zero Geometry and Tubes.** Multi-zero constructions,
   holomorphic branch singularities, the order-four Hecke zero network, arithmetic
   register correspondences, the sign-cover realization of the `T(2,4)` link
   complement, Hecke periodic-orbit knots, discriminants, proper tubes, monodromy,
   and the conditional knot-invariant programme.
4. **Paper IV — Projective Condensation and Computational Complexity.** Projective
   quotient structures, information loss under condensation, and complexity only
   after explicit state, metric, encoding, and cost models have been supplied.

Papers I--III are mathematical-review manuscripts.  Paper III separates proved
regular and conditional topological results from structural proposals and open
problems.  Paper IV remains a scope and provenance record, not a claim of a
completed paper.

Paper entry points and generated PDFs follow the uniform convention
`paper-k/aeg-paper-k.tex` and `paper-k/aeg-paper-k.pdf`, respectively.

## Arithmetic--automorphic research spine

The current cross-paper development activates the following one-way interface:

```text
Paper I arithmetic histories
  -> q=4 Hecke projective operators
  -> Paper II holomorphic pullback targets
  -> Paper III branched automorphic zero networks
  -> sign-cover geodesic knots and register-decorated relative divisors.
```

Each arrow has a different information level.  Literal histories are not identified
with projective operators, group elements, cells, endpoints, or geometric sheets.
The exact Hecke example now reaches its automorphic zero graph and geodesic-flow
knots at the operator-quotient level.  Finite typed registers give explicit
relative divisors, Frobenius actions, and a tagged trace that detects some domain
history lost by the terminal operator.  A general functor from marked histories to
arithmetic prime divisors remains open.  The active synthesis and claim ledger are
recorded in
[`restructure/discussions/arithmetic-automorphic-zero-networks.md`](restructure/discussions/arithmetic-automorphic-zero-networks.md).

## Building the manuscripts

The local build requires `pdflatex` and `bibtex`:

```bash
./build.sh
```

This builds Papers I--III.  To build one manuscript only, run `./build.sh 1`,
`./build.sh 2`, or `./build.sh 3`.  The expected artifacts are
`paper-1/aeg-paper-1.pdf`, `paper-2/aeg-paper-2.pdf`, and
`paper-3/aeg-paper-3.pdf`.  A container build remains available for environments
with Docker:

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

The restructuring audit records baseline and current build results in
[`restructure/audit-report.md`](restructure/audit-report.md).

## Repository authority

Not every note in this repository is current mathematics.  When sources conflict,
use the order specified in [`restructure/AGENTS.md`](restructure/AGENTS.md).  In
particular, `notes/`, `misc/`, `revision-*`, `archive/arxiv/`, `archive/paper4p/`, and `knots/` retain
historical or exploratory material and are not canonical Paper I sources unless the
migration log says otherwise.
