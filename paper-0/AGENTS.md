# Paper 0 editing instructions

These instructions apply inside `paper-0/` and supplement the repository root
`AGENTS.md` and `governance/00a-paper-0-amendment.md`.

## Scope

Paper 0 is the elementary path/ripple prelude. Keep it focused on:

- explicitly defined left-expanded and right-expanded pure combs;
- point paths in the zeroth-kind upper-half-plane model;
- ripple pencils as Möbius pullbacks of standard horocycles;
- reciprocals, poles, infinity, geometric-series and continued-fraction
  truncations, and iterative fixed points;
- elementary `2 x 2` matrix and projective unification.

Do not import Paper I's full marked-history, torsion, contact, zero-rigidity, or
Hecke theories into this paper.

## Left/right terminology

The root repository warns that informal left/right terminology is ambiguous.
Paper 0 may use it only under the recursive convention

```text
L_0[z] = z,    L_k[z] = omega_k(L_{k-1}[z], c_k)
R_0[z] = z,    R_k[z] = omega_k(c_k, R_{k-1}[z])
```

The index is chronological. Every later use of left/right must be reducible to
this operand-slot convention.

## Claim discipline

- Ordinary arithmetic domains and projective continuation must remain distinct.
- An infinite expansion is not a number until formal or analytic convergence is
  stated.
- An algebraic fixed point need not be attracting.
- A projective pole is not an admissible ordinary division by zero.
- `Ripple pencil` is descriptive terminology for a standard horocycle pullback
  family, not a claim of a new projective geometry.
- The historical notation `E_0` must be identified with Paper I's canonical
  homogeneous hyperbolic model.

## Build

Build Paper 0 from the repository root with

```bash
./build.sh 0
```

Check the PDF, undefined references, duplicate labels, missing citations, and
figure overflow before reporting completion.
