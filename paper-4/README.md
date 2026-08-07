# Arithmetic Expression Geometry IV

## Projective Condensation and Computational Complexity

**Subtitle:** *From Histories and Quotients to Representation and Cost*

**Canonical source:** `aeg-paper-4.tex`  
**Generated manuscript:** `aeg-paper-4.pdf`  
**Status:** mathematical-review manuscript  
**Date:** 2026-08-07

Paper IV studies what is forgotten when an arithmetic history is replaced by
an operator, a projective quotient state, or an endpoint, and determines when
that forgotten information can be related to an exact online state or an
operational resource.

The central chain is

```text
marked history
  -> projective operator
  -> bivaluation / projective quotient
  -> contextual continuation residual
  -> operational realization.
```

These arrows are not identified. The manuscript separates four layers:

1. projective quotient fibers;
2. future-relative contextual residuals;
3. operational live configurations;
4. rewrite fibers of equal semantic realizations.

## Principal proved results

- Regular bivaluations are ordered image--kernel pairs and are equivalent to
  rank-one idempotents on `K^2`.
- For `G = PGL_2(K)` and the ordered-pair stabilizer `H`, the bivaluation space
  is `G/H`, while a third projective point restores an `H`-torsor of frames.
- Over `F_q`, the quotient and fiber sizes are explicit:
  `|G| = q(q^2-1)`, `|G/H| = q(q+1)`, and `|H| = q-1`.
- Left continuation always acts on `G/H`. A single right update by `k`
  descends exactly when `k^{-1} H k` is contained in `H`; a reversible right
  action descends exactly through the normalizer.
- For a typed interface, legal future monoid, partial-domain convention, and
  observation, contextual continuation equivalence gives the canonical
  minimal exact deterministic online state.
- A finite residual space gives a fixed-width or prefix-free maximum state
  lower bound. Summing these bounds gives a fixed-register **capacity--time**
  bound, not an unconditional dynamic memory--time theorem.
- Ever-computed node sets do not determine workspace in models that allow
  erasure or recomputation.
- Exact fiber--image and conditional-entropy inequalities quantify evaluation
  loss without turning word growth into a runtime lower bound.
- Additive potential labels and pure-gauge group labels telescope around every
  rewrite loop, so they cannot alone define nontrivial holonomy.

## Exact calibrations

The manuscript includes four families of computational examples:

- Horner histories: fixed digit histograms have one ACS charge but a
  multinomial number of distinct affine operators in characteristic zero.
- OBDD equality: block order has width at least `2^n`, whereas interleaved order
  has constant width, although variable restrictions commute.
- Butterfly and NTT networks: a local butterfly is a common matrix times a
  diagonal torus label; full transforms require multi-wire linear semantics,
  scalar normalization, and a declared cost model.
- Matrix chains and checkpointing: equal semantic maps can have incomparable
  work, intermediate-size, and live-space coordinates.

## Claim boundary

Paper IV does **not** infer any of the following:

```text
noncommutativity -> negative curvature
negative curvature -> computational hardness
exponential group growth -> exponential runtime
large history fiber -> large shared representation
endpoint cost difference -> process holonomy
```

Multi-wire AEG, non-flat projective transport, approximate residuals, and
machine-robust complexity comparisons remain open programmes.

## Source layout

```text
aeg-paper-4.tex
sections/01-introduction.tex
...
sections/14-conclusion.tex
appendices/app-A-projective-calculations.tex
appendices/app-B-residual-proofs.tex
appendices/app-C-network-counts.tex
appendices/app-D-claim-ledger.tex
aeg-paper-4.bib
scripts/verify-paper4.py
```

## Build

From the repository root:

```bash
./build.sh 4
```

Or from this directory:

```bash
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
bibtex aeg-paper-4
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
```

Run the dependency-free finite verification suite with:

```bash
python scripts/verify-paper4.py
```

## Release boundary

The PDF is a mathematical-review manuscript. Public release, author metadata,
DOI assignment, and merging into the repository's release line require explicit
author approval.
