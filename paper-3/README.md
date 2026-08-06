# Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes

*Multi-Zero Constructions, Discriminants, and Topological Transport*

This directory contains the mathematical-review manuscript

> **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
> *Multi-Zero Constructions, Discriminants, and Topological Transport*

Its canonical source and generated artifact are `aeg-paper-3.tex` and
`aeg-paper-3.pdf`.

The manuscript studies the boundary of the regular-zero theory established in
Paper I.  Its central distinction is between a total zero set, a smooth zero
surface, a locally trivial proper tube, an embedded or threaded tube, a braid
closure, and a knot invariant.  These are different levels of structure; no later
level is inferred merely from an earlier one.

## Imports from Paper I

- the regular and singular AES definitions;
- the regular-zero theorem;
- the smooth total-zero-set and projection-submersion proposition;
- the properness warning.

## Proved results and strict boundary

The manuscript proves:

- an explicit conformal realization theorem and finite/countable multi-zero models;
- a rank-`r` parameterized zero-section and proper-tube theorem;
- a torus-structure theorem for compact boundaryless real zero tubes over a circle
  with globally oriented vertical tangent bundle;
- a compact helical tube with computed component, deck, and boundary transport;
- singular AEG Morse bifurcations and the separate complex branch model `w^2=tau`;
- proper finite-root braid monodromy and realization of every braid by the
  arithmetic-holomorphic fields of Paper II;
- logarithmic root-lift gauge laws;
- scalar/affine novelty filters, including a nonzero resonant twisted cohomology
  class whose planar classical-link state sum nevertheless collapses to the
  Alexander-quandle coloring count.

It does **not** claim a global classification of multi-zero models, a general
singularity normal-form theorem compatible with the AEG flow, properness of every
family, an intrinsic real-zero-to-braid functor, functorial thread selection, a new
Markov-normalized AEG knot invariant, or separation beyond Alexander/Burau.  In
particular:

- a smooth total zero set is not automatically a tube;
- a tube is not automatically an embedded or threaded tube;
- braid-level data are not automatically knot invariants;
- visual tube constructions do not establish isotopy or Markov invariance.

## Building

Build this manuscript from the repository root with:

```bash
./build.sh 3
```

The all-manuscript command is:

```bash
./build.sh
```

## Source layout

```text
paper-3/
├── aeg-paper-3.tex
├── sections/
│   ├── 01-singular-aes.tex
│   ├── 02-local-zero-models.tex
│   ├── 03-multi-zero-constructions.tex
│   ├── 04-parameter-discriminants.tex
│   ├── 05-regular-tubes.tex
│   ├── 06-singular-fibers.tex
│   ├── 07-monodromy-and-braids.tex
│   └── 08-threading-and-knot-questions.tex
└── appendices/
    ├── app-A-regularity-and-properness.tex
    ├── app-B-configuration-and-braid-background.tex
    └── app-C-affine-quandle-calculations.tex
```

## Historical source families and provenance warning

- multi-zero, `E_k`, `E_log`, and tube notes (historical motivation only);
- tube-related parts of legacy `sections/sec04.tex` and `sec09.tex`;
- `knots/` and knot-related files under `misc/`;
- restructuring discussions on tubes, braid monodromy, and Markov invariance.

The `E_k` and `E_log` notations are historical research labels, not settled model
classes.  A scan of the current tree and 249 Git commits found no verifiable general
construction under either name.  The formulas in this manuscript are newly
rederived and audited rather than silently attributed to those labels.  The
authoritative scope and status records under `../restructure/` take precedence over
all legacy provenance sources.

## Integration records

- [`../restructure/paper-III-source-audit.md`](../restructure/paper-III-source-audit.md)
- [`../restructure/decisions-paper-III.md`](../restructure/decisions-paper-III.md)
- [`../restructure/paper-III-closure-report.md`](../restructure/paper-III-closure-report.md)
