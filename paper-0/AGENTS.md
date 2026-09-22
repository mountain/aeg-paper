# Paper 0 editing instructions

These instructions apply inside `paper-0/` and supplement the repository root
`AGENTS.md` and the authoritative amendment
`governance/00b-paper-0-geometric-foundation-amendment.md`.

## Scope

Paper 0 is the **geometric foundation** of the series.  Keep it focused on:

- arithmetic expansions: left- and right-expanded combs under the explicit
  operand-slot recursion, one-hole sections, and the distributive law as the
  rewrite relating distinct expansions of one expression;
- arithmetic expression spaces: the regular AES axioms, the canonical
  arithmetic frame, the four operations as motions, the models `E_0` and `E_1`,
  the continuous arithmetic motion and its rectification;
- the dual reading: poles, horocycle pullback, ripple geometry (descriptive
  name only), reciprocals, infinity, fixed points, and the matrix synthesis;
- commutativization: affine cocycles, the relative defect, the ACS, the
  torsion--Stokes theorem, and tearing (a name for the measured defect);
- the contact structure of tearing: contact form, horizontal fields, curvature,
  finite open and closed defects, and the scalar horizontal differential;
- the structural proposals of §10 and the punctured spaces and computed
  witnesses of §11, each at its recorded status.

Do not develop here, as a main theory: the intrinsic sequential-tree
classification, mixed-chirality marked histories as the main object, the Hecke
`q=4` language, regular-zero rigidity or singular-zero classification, function
theory, quotient towers, or a general convergence theory of infinite
expressions.  Those belong to Papers I--IV.

## Left/right terminology

The root repository warns that informal left/right terminology is ambiguous.
Paper 0 may use it only under the recursive convention of
`conv:p0-left-right-convention`:

```text
L_0[z] = z,    L_k[z] = omega_k(L_{k-1}[z], c_k)
R_0[z] = z,    R_k[z] = omega_k(c_k, R_{k-1}[z])
```

The index is chronological.  Every later use of left/right must be reducible to
this operand-slot convention.

## Claim discipline

- Ordinary arithmetic domains and projective continuation must remain distinct.
- An infinite expansion is not a number until formal or analytic convergence is
  stated.
- An algebraic fixed point need not be attracting.
- A projective pole is not an admissible ordinary division by zero.
- `Ripple pencil` and `ripple geometry` are descriptive terminology for standard
  horocycle pullback families, not a claim of a new projective geometry.
- `Tearing` is a structural proposal naming the two-history defect whose value
  is `thm:torsion-stokes` and whose density is `thm:contact-curvature`; it is
  never stated as an independent theorem.
- Punctures are declared singular points of the regular structure, not holes in
  a metric; a punctured AES is the finite-point case of Paper I's singular AES,
  and its classification is not attempted here.
- Items of `Yuan2026AEGHoleRegister` enter only at the status
  `COMPUTATIONALLY VERIFIED EXAMPLE`, and the non-claims of §11 are part of the
  section.
- The model labels follow `conv:p0-model-labels`: `E_0` is the basic regular
  hyperbolic model (identified once with the former `E_{\mathrm{hyp}}`), `E_1`
  is the once-punctured disc, and `E_k` is descriptive only.
- Every substantial new or moved result must appear in
  `governance/05b-paper-0-status-register.md`.

## Build

Build Paper 0 from the repository root with

```bash
./build.sh 0
```

Check the PDF, undefined references, duplicate labels, missing citations, and
figure overflow before reporting completion.  Any change under `paper-0/`,
`paper-1/`, or `bibliography/` also requires `./build.sh 1`, because CI validates
both logs together.
