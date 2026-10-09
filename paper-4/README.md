# Arithmetic Expression Geometry IV

## Projective Condensation and Computational Complexity

**Subtitle:** *From Histories and Quotients to Representation and Cost*

**Canonical source:** `aeg-paper-4.tex`  
**Generated manuscript:** `aeg-paper-4.pdf`  
**Status:** draft manuscript under mathematical review<br>
**Date:** 2026-10-09

## Draft status

Here **draft** describes editorial and publication maturity: the conceptual
organization, exposition, figures, and text--figure integration remain under
development. It is not a mathematical claim-status label in `governance/` and does
not alter the status of any individual result.

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
- Finite strict typed networks with explicit copy/discard support source- and
  occurrence-preserving substitution and exact composite partial domains.
  Numerical associativity includes domain equality; graph reassociation is an
  explicit isomorphism, while literal call receipts remain distinct.
- Compatible AES collars and complete computational seam records descend
  together when the assembled global event graph is acyclic. This constructs an
  attached program, not a faithful realization of its gates as AES motions.
- Feature observation factorization is equivalent to refinement of contextual
  equivalence. Online feature update additionally requires a right-congruence
  kernel; effective implementation remains a separate obligation.
- Ever-computed node sets do not determine workspace in models that allow
  erasure or recomputation.
- Exact fiber--image and conditional-entropy inequalities quantify evaluation
  loss without turning word growth into a runtime lower bound.
- Additive potential labels and pure-gauge group labels telescope around every
  rewrite loop, so they cannot alone define nontrivial holonomy.

## Exact calibrations

The manuscript includes a ported-network experiment and four families of
computational calibrations:

- Ported AES: a fixed four-puncture carrier with four input programs and explicit
  copying gives three scalar outputs `(9, 15, 5/2)`, retaining sources,
  occurrences, exact domains, and call receipts. These are declared scalar
  projections, not Adva's native three output roles.
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

The finite multi-wire program interface is established with stated hypotheses.
Faithful AES realizations of its actual arithmetic/structural gates, actual
opposite-edge feature witnesses, non-flat projective transport, approximate
residuals, and machine-robust complexity comparisons remain open programmes.
Geometric punctures, computational holes, and input/output ports remain
independent; binding inputs does not change the carrier assignment or cap ends.

## Source layout

```text
aeg-paper-4.tex
sections/01-introduction.tex
...
sections/05-contextual-residuals.tex
sections/05b-ported-aes-programs.tex
sections/06-operational-resource-geometry.tex
...
sections/14-conclusion.tex
appendices/app-A-projective-calculations.tex
appendices/app-B-residual-proofs.tex
appendices/app-C-network-counts.tex
appendices/app-D-claim-ledger.tex
../bibliography/aeg-paper.bib
scripts/verify-paper4.py
scripts/verify-ported-aes.py
scripts/fixtures/ported-aes/integration-evidence.json
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
python scripts/verify-ported-aes.py
```

## Ported-chapter provenance and verification boundary

The ported chapter is adapted from the complete text of the eight-page
`paper4-ported-aes-v0.1.pdf` produced in the 2026-10-09 H² compactification
session. It is placed immediately after contextual residuals and before
operational resource geometry. `Subst` denotes program substitution; the
existing `Fill` notation remains reserved for rewrite filling area.

The candidate session reported 55 exact finite checks, but its original
`aes-ported-paper4-v0.1.zip` could not be retrieved during integration. The new
`verify-ported-aes.py` is an independently authored integration checker, not a
recovered or rerun original suite. Its 14 named check groups cover exact rational
execution; source/occurrence transport; one-use binding, type, and instance
controls; partial-frontier ordering; strict partial domains and discard;
schedule-independent outputs with distinct traces; composition isomorphisms
with distinct receipts; equal-value/different-process controls; two independently
authored seam-packet reconstructions and their negative controls; a global cycle
formed from locally acyclic pieces; feature observation versus online update;
and eight exact rational reciprocal-chart metric/covector/frame samples.
The composition group checks identity laws as well as reassociation, and the
frontier group checks the explicit boundary permutation required for its
open-producer sequential/simultaneous comparison. Source labels in the checker
are immutable syntactic sites; post-binding value ancestry is retained by the
producer DAG and receipt, not by overwriting those source fields.

The checked deterministic evidence is
`scripts/fixtures/ported-aes/integration-evidence.json`. From this directory,
reproduce and compare it without replacing the checked-in evidence:

```bash
python scripts/verify-ported-aes.py > /tmp/ported-aes-evidence.json
cmp /tmp/ported-aes-evidence.json scripts/fixtures/ported-aes/integration-evidence.json
```

These are independent finite fixtures and samples, not recovered original
packets or gate placements. They supplement the in-paper proofs and do not
establish continuous overlap identities, a faithful AES gate-motion realization,
or native opposite-edge feature witnesses.

## Release boundary

The PDF is a mathematical-review manuscript. Public release, author metadata,
DOI assignment, and merging into the repository's release line require explicit
author approval.
