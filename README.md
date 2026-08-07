# Arithmetic Expression Geometry

This repository contains the manuscripts, notes, figures, and build tooling for
the Arithmetic Expression Geometry (AEG) research programme. AEG studies
arithmetic expressions through their ordered evaluation histories. An unmarked
sequential tree first requires a choice of accumulator; the resulting fully
marked planar tree is equivalent to a bounded marked history. From that
history, operator evaluation and charge/geometric shadows form separate
branches, and only an operator together with an initial value determines an
endpoint. The repository keeps these levels distinct.

The active manuscripts are:

> **Arithmetic Expression Geometry I: Foundations**  
> *Sequential Histories, Affine Flow, Torsion, and Contact Geometry*

> **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**  
> *Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity*

> **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**  
> *Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

> **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**  
> *From Histories and Quotients to Representation and Cost*

Their canonical entry points are
[`paper-1/aeg-paper-1.tex`](paper-1/aeg-paper-1.tex),
[`paper-2/aeg-paper-2.tex`](paper-2/aeg-paper-2.tex),
[`paper-3/aeg-paper-3.tex`](paper-3/aeg-paper-3.tex), and
[`paper-4/aeg-paper-4.tex`](paper-4/aeg-paper-4.tex). The governing scope,
mathematical-status register, migration map, and acceptance criteria are under
[`governance/`](governance/README.md).

## Draft status

All four active manuscripts are **drafts** in the ordinary editorial and
publication sense. Their conceptual organization, exposition, figures, and
text--figure integration remain under development and are not yet presented as
release-quality replacements for the archived legacy manuscript. In particular,
[`archive/legacy-root-manuscript/`](archive/legacy-root-manuscript/) may currently
offer a more polished reading and visual experience even where the active series has
the newer mathematical organization.

Here **draft** is a maturity label for the manuscripts as complete scholarly and
visual works. It is not a mathematical claim-status label in the governance system
and does not weaken or promote any theorem, proposition, conjecture, computation, or
open problem. Claim-level status remains controlled separately by
[`governance/05-mathematical-status.md`](governance/05-mathematical-status.md).

## Version and DOI

[![Earlier DOI version](https://zenodo.org/badge/DOI/10.5281/zenodo.18887455.svg)](https://doi.org/10.5281/zenodo.18887455)

The Zenodo DOI above identifies an **earlier archived version** of the
manuscript. It does not automatically identify any active restructured paper.
The active sources state their own dates and review status; a future release
must receive explicit author approval before DOI metadata is changed.

## Four-paper architecture

1. **Paper I — Foundations.** Sequential histories, bilateral projective
   semantics, the affine sector, the `q = 4` Hecke arithmetic sublanguage,
   cocycles, continuous flow, the basic hyperbolic model, complete regular-zero
   rigidity, global torsion, and contact curvature.
2. **Paper II — Hyperbolic Real Function Theory.** Horizontal complex and
   analytic structures, operator domains, kernels, boundary problems, planar
   and cylindrical holomorphic pullbacks, and spectral questions.
3. **Paper III — Singular Zero Geometry and Tubes.** Multi-zero constructions,
   holomorphic branch singularities, the order-four Hecke zero network,
   arithmetic register correspondences, the sign-cover realization of the
   `T(2,4)` link complement, its marked toric and logarithmic-tangent polynomial
   normal form `u^2=t^4`, polynomially threaded carrier surfaces, a four-strand
   central extension and group-cohomological residue calibration, the sextic
   Lyashko--Looijenga laboratory with full six-braid and genus-two monodromy,
   Hecke periodic-orbit knots, discriminants, proper tubes, monodromy, and the
   conditional knot-invariant programme.
4. **Paper IV — Projective Condensation and Computational Complexity.** The
   projective quotient tower, rank-one bivaluations, chronology-sensitive
   continuation descent, contextual residuals and minimal exact state,
   operational live-configuration geometry, fiber and entropy inequalities,
   rewrite exactness obstructions, and fixed-model calibrations from Horner,
   OBDDs, transforms, matrix chains, and checkpointing.

Papers I--IV are draft manuscripts under mathematical review. Paper III separates proved
regular and conditional topological results from structural proposals and open
problems. Paper IV separates proved quotient/residual results and fixed-model
complexity calibrations from the open multi-wire, approximate, and
machine-robust programmes.

Paper entry points and generated PDFs follow the uniform convention
`paper-k/aeg-paper-k.tex` and `paper-k/aeg-paper-k.pdf`.

## Arithmetic--automorphic research spine

The cross-paper development activates the following one-way interface:

```text
Paper I arithmetic histories
  -> q=4 Hecke projective operators
  -> Paper II holomorphic pullback targets
  -> Paper III branched automorphic zero networks
  -> sign-cover geodesic knots and peripheral toric thread
  -> logarithmic polynomial cone, threaded carrier, and braid-center residue.
```

Each arrow has a different information level. Literal histories are not
identified with projective operators, group elements, cells, endpoints, or
geometric sheets. The exact Hecke example reaches its automorphic zero graph and
geodesic-flow knots at the operator-quotient level. Finite typed registers give
explicit relative divisors, Frobenius actions, and a tagged trace that detects
some domain history lost by the terminal operator. The family `z^2=t^m` gives
an exact cross-slice comparison among arithmetic components, carrier topology,
discriminant winding, braid exponent, and linking, while its coefficient path
is still supplied rather than history-derived. The fixed pencil `x^6-x-t`
upgrades this to nonabelian transport: one event polynomial controls real
carrier walls, all six-braids, all genus-two mapping classes, full symplectic
monodromy, and a finite 1296-sheet LL forgetting problem. Two explicit sheets
in distinct residual source-rotation orbits have the same event polynomial but
different genus-two Igusa moduli at `t=1`; thus this forgetting provably loses
genuine complex geometry. On the 216-sheet quotient cover, the moduli observable
has a single-valued spectral polynomial, trace--norm descent, a canonical
constant/zero-sum splitting, and a monodromy-invariant forgetting variance with
an exact positive lower bound at `Q_0`; it need not be constant along arbitrary
open paths in the event-polynomial base. The two explicit slice pencils have
ratio `((t-beta)/t)^5` and balanced regular-fiber divisor charge
`5[beta]-5[0]`, a logarithmic charge rather than a finite Dirichlet energy. The
full 216-orbit census, arithmetic/period comparison, marked-monodromy
refinement, and Hodge/Siegel-energy interpretation remain open. Neither the LL
sheet nor its parameter loop is yet selected by a general arithmetic history.
A general functor from marked histories to arithmetic prime divisors remains
open. The active synthesis and claim ledger are recorded in
[`governance/discussions/arithmetic-automorphic-zero-networks.md`](governance/discussions/arithmetic-automorphic-zero-networks.md).

## Arithmetic--computational research spine

Paper IV activates a second one-way interface:

```text
Paper I marked histories
  -> PGL2 operator evaluation
  -> projective quotient G/H
  -> future-relative contextual residual
  -> encoded online state
  -> operational live-configuration trace.
```

The arrows are conditional. A quotient is an exact online state only when the
future action descends and the observation factors through it. A residual
cardinality gives a fixed-width state-selection bound, while actual work,
workspace, memory--time, and communication require a declared machine model.
The paper proves left/right continuation criteria, the minimal deterministic
residual theorem, finite fiber and entropy inequalities, and exact case-study
counts. It does not infer hardness from noncommutativity, negative curvature,
exponential group growth, or raw history-fiber size. The detailed decisions,
source audit, red-team report, and closure record are under `governance/`.

## Building the manuscripts

The local build requires `pdflatex` and `bibtex`:

```bash
./build.sh
```

This builds Papers I--IV. To build one manuscript only, run
`./build.sh 1`, `./build.sh 2`, `./build.sh 3`, or `./build.sh 4`. The expected
artifacts are `paper-k/aeg-paper-k.pdf` for `k = 1,2,3,4`.

A container build remains available for environments with Docker:

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

Paper IV's finite verification suite is:

```bash
python paper-4/scripts/verify-paper4.py
```

The restructuring audit records baseline and current build results in
[`governance/audit-report.md`](governance/audit-report.md) and the per-paper
closure reports.

## Repository authority

Not every note in this repository is current mathematics. When sources
conflict, use the order specified in
[`AGENTS.md`](AGENTS.md). In particular, `notes/`,
`images/sources/`, `archive/revision-*`, `archive/arxiv/`, `archive/paper4p/`, and
`notes/knots-and-loops/` retain historical or exploratory material and are not
canonical paper sources unless the migration log or a per-paper source audit says
otherwise.

The subject classification and per-directory filename ordering for research notes
are documented in [`notes/README.md`](notes/README.md).
