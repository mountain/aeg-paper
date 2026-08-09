# Arithmetic Expression Geometry

This repository contains the manuscripts, notes, figures, bibliography, and
build tooling for the Arithmetic Expression Geometry (AEG) research programme.
AEG studies arithmetic expressions through their ordered evaluation histories
rather than only through final numerical values.

The active manuscript series is now:

> **Arithmetic Expression Geometry 0: Paths and Ripple Pencils**  
> *Left and Right Expansions, Reciprocals, and Projective Unification*

> **Arithmetic Expression Geometry I: Foundations**  
> *Sequential Histories, Affine Flow, Torsion, and Contact Geometry*

> **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**  
> *Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity*

> **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**  
> *Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

> **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**  
> *From Histories and Quotients to Representation and Cost*

Their canonical entry points are
[`paper-0/aeg-paper-0.tex`](paper-0/aeg-paper-0.tex),
[`paper-1/aeg-paper-1.tex`](paper-1/aeg-paper-1.tex),
[`paper-2/aeg-paper-2.tex`](paper-2/aeg-paper-2.tex),
[`paper-3/aeg-paper-3.tex`](paper-3/aeg-paper-3.tex), and
[`paper-4/aeg-paper-4.tex`](paper-4/aeg-paper-4.tex).
The governing scope, mathematical-status records, migration map, and acceptance
criteria are under [`governance/`](governance/README.md). Paper 0 is introduced
by the authoritative amendment
[`governance/00a-paper-0-amendment.md`](governance/00a-paper-0-amendment.md).

## Draft status

All active manuscripts are drafts in the ordinary editorial and publication
sense. Their conceptual organization, exposition, figures, and text--figure
integration remain under development. This maturity label does not promote or
weaken any theorem, proposition, conjecture, computation, or open problem;
claim-level status is governed separately.

## Version and DOI

[![Earlier DOI version](https://zenodo.org/badge/DOI/10.5281/zenodo.18887455.svg)](https://doi.org/10.5281/zenodo.18887455)

The Zenodo DOI identifies an earlier archived version of the manuscript. It does
not automatically identify any active restructured paper. A future release must
receive explicit author approval before DOI metadata is changed.

## Five-paper architecture

0. **Paper 0 — Paths and Ripple Pencils.** Explicit left- and right-expanded
   combs, the affine point-path picture, the projective ripple-pencil picture,
   reciprocals, poles, infinity, iterative fixed points, continued-fraction
   truncations, and elementary matrix/projective unification. Paper 0 is a
   pedagogical and geometric prelude; it does not replace Paper I's marked
   history formalism.

1. **Paper I — Foundations.** Intrinsic sequential-tree classification, marked
   spinal histories, bilateral projective semantics, the affine sector, the
   `q=4` Hecke arithmetic sublanguage, cocycles, continuous flow, the complete
   basic hyperbolic model, regular-zero rigidity, global torsion, and contact
   curvature.

2. **Paper II — Hyperbolic Real Function Theory.** Horizontal complex and
   analytic structures, operator domains, kernels, boundary problems, planar
   and cylindrical holomorphic pullbacks, and spectral questions.

3. **Paper III — Singular Zero Geometry and Tubes.** Multi-zero constructions,
   branched pullbacks, arithmetic zero networks, relative divisors, sign covers,
   threaded carriers, Lyashko--Looijenga forgetting, proper tubes, monodromy,
   braids, and the conditional knot-invariant programme.

4. **Paper IV — Projective Condensation and Computational Complexity.** The
   projective quotient tower, bivaluations, chronology-sensitive continuation,
   contextual residuals, minimal exact state, operational live configurations,
   fiber and entropy inequalities, rewrite obstructions, and fixed-model
   calibrations.

The dependency architecture is

```text
Paper 0 -> Paper I -> Paper II
                   -> Paper III
                   -> Paper IV
```

## Path--ripple research spine

Paper 0 activates the elementary interface

```text
left-expanded comb
  -> affine one-hole maps
  -> point path in E0
  -> matrices with pole at infinity

right-expanded comb
  -> reciprocal one-hole maps
  -> finite pole and ripple pencil
  -> general Möbius matrices
```

The same prefix matrix determines the propagated point, the operator pole, its
fixed points, and the pullback of standard horocycles. Arithmetic reciprocals
are also related to iteration: finite geometric-series and continued-fraction
truncations are matrix products, while infinite values are asserted only under
explicit formal or analytic convergence hypotheses. Ordinary division by zero
remains inadmissible even when projective continuation reaches infinity.

## Arithmetic--automorphic research spine

The later cross-paper development remains one-way:

```text
Paper I arithmetic histories
  -> q=4 Hecke projective operators
  -> Paper II holomorphic pullback targets
  -> Paper III branched automorphic zero networks
  -> sign-cover geodesic knots and peripheral polynomial threads.
```

Each arrow has a different information level. Literal histories are not
identified with operators, cells, endpoints, geometric sheets, or knots. The
sextic Lyashko--Looijenga laboratory proves that one finite forgetting map can
lose genuine genus-two moduli, but a general functor from marked histories to
arithmetic prime divisors remains open.

## Arithmetic--computational research spine

Paper IV activates a second conditional interface:

```text
Paper I marked histories
  -> PGL2 operator evaluation
  -> projective quotient G/H
  -> future-relative contextual residual
  -> encoded online state
  -> operational live-configuration trace.
```

A quotient is an exact online state only when the future action descends and the
observation factors through it. Residual cardinality gives a fixed-width
state-selection bound; actual work, workspace, memory--time, and communication
require a declared machine model. No hardness result is inferred merely from
noncommutativity, negative curvature, group growth, or raw history-fiber size.

## Building the manuscripts

The local build requires `pdflatex` and `bibtex`:

```bash
./build.sh
```

This builds Papers 0--IV. To build one manuscript only, run

```bash
./build.sh 0
./build.sh 1
./build.sh 2
./build.sh 3
./build.sh 4
```

The expected artifacts are `paper-k/aeg-paper-k.pdf` for `k = 0,1,2,3,4`.

A container build remains available for environments with Docker:

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

Paper IV's finite verification suite is:

```bash
python paper-4/scripts/verify-paper4.py
```

## Repository authority

Not every note in this repository is current mathematics. When sources
conflict, use the order specified in [`AGENTS.md`](AGENTS.md), together with the
Paper 0 amendment named above. In particular, `notes/`, `images/sources/`,
`archive/revision-*`, `archive/arxiv/`, `archive/paper4p/`, and historical knot
or thermal notes retain exploratory material and are not canonical paper
sources unless a migration or source-audit record says otherwise.
