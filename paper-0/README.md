# Paper 0 — Arithmetic Expression Spaces

**Provisional title:** *Arithmetic Expression Geometry 0*  
**Subtitle:** *Arithmetic Expression Spaces: Expansion, Motion, Ripple Duals,
Commutativization, and Tearing*

Paper 0 is the geometric foundation of the series.  It develops:

1. arithmetic expansions: left- and right-expanded combs under the explicit
   operand-slot convention, one-hole sections, and the distributive law as the
   rewrite that relates distinct expansions of one expression;
2. arithmetic expression spaces: the regular AES axioms, the canonical
   arithmetic frame, the four operations as motions, the basic hyperbolic model
   `E_0`, the one-puncture model `E_1`, and the continuous arithmetic motion;
3. the projective dual reading — poles, horocycle pullback, reciprocals,
   infinity, fixed points, and the matrix synthesis — whose dual name is
   *ripple geometry* (descriptive and provisional);
4. the commutativization: affine cocycles, the relative defect, the
   accumulative commutative space (ACS), the weighted torsion--Stokes theorem,
   and the reading of that defect as *tearing*;
5. the contact structure of tearing: the contact form, the horizontal fields,
   the curvature bracket, finite open and closed defects, and the scalar
   horizontal differential;
6. two methodological obstructions to linear language and the structural
   proposals imported from process geometry;
7. punctured arithmetic expression spaces, the tangent cone of a puncture, and a
   register of six computed witnesses.

The paper does **not** revise the marked spinal history terminology of Paper I.
Paper I remains responsible for the intrinsic sequential-tree classification,
mixed chirality, chronological marked histories, projective evaluation, the
Hecke `q=4` sublanguage, and the zero geometry.

## Canonical source closure

```text
paper-0/
  aeg-paper-0.tex
  sections/
    01-introduction.tex
    02-expansion.tex
    03-aes-and-motion.tex
    04-ripple-geometry.tex
    05-reciprocals-fixed-points.tex
    06-projective-unification.tex
    07-affine-cocycles.tex
    08-acs-tearing.tex
    09-contact-of-tearing.tex
    10-beyond-linear.tex
    11-holed-aes.tex
    12-interface.tex
  appendices/
    app-A-calculations.tex
    app-B-hyperbolic-calculations.tex
    app-C-affine-cocycles.tex
    app-D-acs-contact.tex
```

Sections 7--9 and appendices B--D were moved from Paper I by the amendment
`governance/00b-paper-0-geometric-foundation-amendment.md`; they keep their
labels, hypotheses, and statuses.  The paper uses the shared bibliography at
`bibliography/aeg-paper.bib`.

## Claim boundary

Proved in the manuscript, at the statuses recorded in
`governance/05b-paper-0-status-register.md`:

- both pure combs have a unique internal evaluation order;
- right combs become left combs after passing to opposite operations;
- distributivity preserves the operator while changing the charge of an
  expansion;
- the basic hyperbolic model is a complete regular AES of constant curvature;
- the four operations act as motions, with the Baumslag--Solitar-type transport
  relation for the additive ruler;
- the pullback of a horizontal horocycle by a real orientation-preserving
  Möbius map is a line or a circle tangent at the operator pole;
- geometric-series and continued-fraction truncations satisfy the stated
  recursions and matrix formulas, with convergence claimed only under explicit
  hypotheses;
- translations, nonzero scalings, and inversion generate `PGL_2(K)`;
- the ACS evaluation formula and the weighted torsion--Stokes theorem;
- the history group is the free product of the two step families, the charge
  endpoint is its abelianization, and of the two charges only the multiplicative
  one descends to the motion (`thm:p0-descent`);
- the contact form is non-degenerate exactly when `mu*lambda != 0`, and the
  horizontal fields satisfy `[D_u,D_v] = mu*lambda*d_a`; the bracket defect is a
  canonical 2-form on the distribution, and `mu*lambda` is its value on the
  orthonormal frame of the declared horizontal metric;
- the basic model is the Reeb quotient of the contact model, with the horizontal
  fields descending to the canonical frame and `d(alpha)` equal to
  `-mu*lambda` times the hyperbolic area form;
- the arithmetic generators do not close into a finite-dimensional Lie algebra
  (so no finite-dimensional Lie-group action carries all three ranks), and no
  observable of the commutativized charges detects tearing;
- in a regular AES the assignment has no critical point, so every level set is a
  smooth curve;
- the four-circle configuration is the zero locus of an explicit punctured AES
  whose metric is forced by the eikonal identity, with the puncture
  non-extendable and at finite distance (`thm:p0-four-circle-model`);
- for a punctured space whose assignment extends smoothly, the puncture set is
  exactly the critical set of the assignment, hence canonical and unique
  (`thm:p0-punctures-are-critical`), and the number of holes equals the number of
  critical points;
- the tangent cone of that zero locus at the puncture is `(xy)^2 = 0`.

Labelled as proposals rather than theorems: the name *ripple geometry*, the
language of *tearing*, the model-label convention `E_k`, and the vocabulary
imported from process geometry.  Open extensions include an intrinsic projective
AES for ripple geometry, quotient-stable path/ripple invariants, a canonical
choice of punctures, multi-wire generalization, and a general theory of infinite
arithmetic expressions.
