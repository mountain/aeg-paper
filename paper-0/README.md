# Paper 0 — Paths and Ripple Pencils

**Provisional title:** *Arithmetic Expression Geometry 0: Paths and Ripple Pencils*  
**Subtitle:** *Left and Right Expansions, Reciprocals, and Projective Unification*

Paper 0 is the elementary prelude to Paper I. It develops, in parallel:

1. left-expanded and right-expanded comb expressions under an explicit operand-slot convention;
2. the point-path geometry of the affine/zeroth-kind upper-half-plane model;
3. the ripple-pencil geometry obtained by pulling horocycles back through Möbius maps;
4. arithmetic reciprocals, finite and infinite expansions, poles, the projective point at infinity, and iterative fixed points;
5. the matrix representation that unifies point paths, poles, fixed points, and ripple pencils.

The paper does **not** revise the marked spinal history terminology of Paper I. Paper I remains responsible for the intrinsic sequential-tree classification, mixed chirality, chronological marked histories, projective evaluation, affine flow, torsion, zero geometry, and contact curvature.

## Canonical source closure

```text
paper-0/
  aeg-paper-0.tex
  sections/
    01-introduction.tex
    02-two-combs.tex
    03-paths.tex
    04-ripple-pencils.tex
    05-reciprocals-fixed-points.tex
    06-projective-unification.tex
    07-interface.tex
  appendices/
    app-A-calculations.tex
```

The paper uses the shared bibliography at `bibliography/aeg-paper.bib`.

## Claim boundary

The core claims are elementary and proved in the manuscript:

- both pure combs have a unique internal evaluation order;
- right combs become left combs after passing to opposite operations;
- pure slot-(1) arithmetic is affine, while slot-(2) division introduces inversion;
- the pullback of a horizontal horocycle by a real orientation-preserving Möbius map is a line or a circle tangent at the operator pole;
- geometric-series and continued-fraction truncations satisfy the stated recursions and matrix formulas;
- convergence is claimed only under explicit analytic or formal hypotheses;
- translations, nonzero scalings, and inversion generate `PGL_2(K)`.

Open extensions include a projective AES, intrinsic ripple geometry independent of a chosen chart, history-quotient descent, multi-wire generalization, and a general theory of infinite arithmetic expressions.
