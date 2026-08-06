# Arithmetic Expression Geometry

This repository contains the manuscripts, notes, figures, and build tooling for the
Arithmetic Expression Geometry (AEG) research programme.  AEG studies arithmetic
expressions through their ordered evaluation histories.  An unmarked sequential tree
first requires a choice of accumulator; the resulting fully marked planar tree is
equivalent to a bounded marked history.  From that history, operator evaluation and
charge/geometric shadows form separate branches, and only an operator together with
an initial value determines an endpoint.  The repository keeps these levels distinct.

The active manuscript is:

> **Arithmetic Expression Geometry I: Foundations**  
> *Sequential Histories, Affine Flow, Torsion, and Contact Geometry*

Its canonical entry point is [`aeg-paper.tex`](aeg-paper.tex).  The governing scope,
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
   the affine sector, cocycles, continuous flow, the basic hyperbolic model, regular
   and singular zero foundations, global torsion, and contact curvature.
2. **Paper II — Hyperbolic Real Function Theory.** Horizontal complex and analytic
   structures, operator domains, kernels, boundary problems, and spectral questions.
3. **Paper III — Singular Zero Geometry and Tubes.** Multi-zero constructions,
   singularities, discriminants, proper tube families, monodromy, and the conditional
   braid/knot programme.
4. **Paper IV — Projective Condensation and Computational Complexity.** Projective
   quotient structures, information loss under condensation, and complexity only
   after explicit state, metric, encoding, and cost models have been supplied.

The later-paper directories currently record scope and provenance; they are not yet
claims of completed papers.

## Building Paper I

The local build requires `pdflatex` and `bibtex`:

```bash
./build.sh
```

The expected artifact is `aeg-paper.pdf`.  A container build remains available for
environments with Docker:

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
