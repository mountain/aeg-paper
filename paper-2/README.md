# Arithmetic Expression Geometry II — Hyperbolic Real Function Theory

This directory contains a draft manuscript under mathematical review:

> **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
> *Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity*

The canonical source and generated artifact are [`aeg-paper-2.tex`](aeg-paper-2.tex)
and `aeg-paper-2.pdf`.

## Draft status

Here **draft** describes editorial and publication maturity: the conceptual
organization, exposition, figures, and text--figure integration remain under
development. It is not a mathematical claim-status label in `governance/` and does
not alter the status of any individual result.

## Main results

- a measure-sensitive Laplace--Beltrami formula in the canonical arithmetic frame;
- exact surface Cauchy--Riemann factorizations and holomorphic-to-harmonic
  implication;
- a locally biholomorphic pullback theorem for a planar harmonic AES, with an
  explicit curvature law;
- a complete flat cylindrical AES whose pullbacks have zero set
  `W^{-1}(S^1)`, together with the regular automorphic descent criterion;
- a separate contact-CR normalization, variational sub-Laplacian, and Friedrichs
  realization;
- a Poisson kernel and well-posed ideal-boundary `C_0` Dirichlet problem on the
  complete basic hyperbolic AES;
- an exact boundary energy identity and Dirichlet-to-Neumann multiplier;
- explicit assignment-dependent holomorphic, harmonic, and contact-CR families.

Build this manuscript from the repository root with:

```bash
./build.sh 2
```

## Imports from Paper I

- the regular-AES definition and arithmetic frame;
- the basic hyperbolic model;
- the arithmetic contact model, horizontal lifts, and bracket curvature.

## Migrated source families

- legacy `sections/sec08.tex`;
- analytic portions of `sections/sec07.tex`, `sec09.tex`, and `sec11.tex`;
- corresponding material under `../archive/revision-1/`, `../archive/revision-2/`, and `notes/`.

## Status boundary

The manuscript proves a Poisson--Dirichlet theorem and an exact boundary energy
identity on the basic hyperbolic model.  It does not claim general Green kernels,
spectral completeness, contact-boundary representation, or continuation across
singular AES points.  Critical points, poles, and algebraic branch points of the
pullback constructions are reserved for Paper III.  The two-dimensional regular-AES
complex theory and three-dimensional contact-CR theory are kept strictly separate.
