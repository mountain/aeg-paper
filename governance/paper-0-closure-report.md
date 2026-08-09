# Paper 0 Implementation and Build Report

**Status:** Branch closure report  
**Date:** 2026-08-09  
**Branch:** `paper-0-path-ripple-pencil`  
**Draft PR:** `#14`  
**Validated manuscript head:** `7fd8a44719adcab53684ffcdaa6e7b04bb73b130`

## 1. Files changed

The branch adds the canonical Paper 0 source closure, local instructions, an
authoritative architecture amendment, a source audit, and a build workflow. It
also adds a Paper 0 interface to Paper I, transfers the elementary grid and
Baumslag--Solitar exposition from Paper I to Paper 0, updates the root overview,
and extends `build.sh` with target `0`.

The canonical Paper 0 TeX closure is:

```text
paper-0/aeg-paper-0.tex
paper-0/sections/01-introduction.tex
paper-0/sections/02-two-combs.tex
paper-0/sections/03-paths.tex
paper-0/sections/04-ripple-pencils.tex
paper-0/sections/05-reciprocals-fixed-points.tex
paper-0/sections/06-projective-unification.tex
paper-0/sections/07-interface.tex
paper-0/appendices/app-A-calculations.tex
```

Paper I changes are confined to:

```text
paper-1/aeg-paper-1.tex
paper-1/sections/00-paper-zero-interface.tex
paper-1/sections/06-hyperbolic-model.tex
paper-1/appendices/app-C-hyperbolic-calculations.tex
```

The marked spinal history definitions and terminology are unchanged.

## 2. Mathematical claims added

Paper 0 proves, with the hypotheses stated in the manuscript:

1. unique internal evaluation order for the explicit left- and right-expanded
   comb grammars;
2. the opposite-operation correspondence between the two pure combs;
3. the elementary slot-dependent matrix table and the affine/projective break
   caused by second-slot division;
4. the zeroth-kind upper-half-plane assignment identity and the point-path
   realization of affine prefix evaluation;
5. the line/circle formula for Möbius pullbacks of horizontal horocycles, with
   common tangency at the operator pole;
6. the covariant point-path / contravariant ripple-pencil reading of one prefix
   matrix;
7. finite geometric-series formulas, analytic and formal convergence under
   explicit hypotheses, affine fixed-point iteration, and reciprocal
   continued-fraction fixed-point formulas;
8. the relationship between the pole of `1/(1-r)`, escape of a finite fixed
   point, and the parabolic fixed point at infinity;
9. projective unification through `Aff(1,K)=Stab(infinity)` and generation of
   `PGL_2(K)` by translations, nonzero scalings, and inversion.

The geometric-series discussion now distinguishes the degenerate parameter
`r=0`: the update is constant and has a singular matrix, so it has a finite
fixed point but is not an element of `PGL_2`.

No claim of a new projective metric or a completed projective AES is added.

## 3. Material relocated in expository ownership

Paper 0 becomes the canonical source for:

- the elementary pure left/right comb comparison;
- the historical point-path picture in the zeroth-kind grid;
- the assignment-compatible grid maps and their elementary
  Baumslag--Solitar-type relation;
- inversion as a curved horocycle/ripple pencil;
- reciprocal--pole--infinity and elementary fixed-point discussion;
- the introductory matrix synthesis.

Paper I no longer contains the full arithmetic-grid figure or the detailed
metric-pullback and Baumslag--Solitar calculations. It retains the group-derived
metric, the complete basic hyperbolic AES theorem, horocyclic coordinates,
curvature, completeness, Laplacian, zero geometry, and a concise interface back
to Paper 0.

Paper I also retains the marked spinal history terminology and definitions, the
intrinsic sequential-tree classification, mixed chirality, chronological
projective evaluation, the Hecke interface, affine flow, zero rigidity, ACS
torsion, and contact curvature.

## 4. Assumptions made explicit

- division remains partial in ordinary arithmetic;
- projective continuation does not repair an inadmissible intermediate step;
- the ripple-circle theorem uses a real Möbius lift of positive determinant;
- geometric-series convergence uses `|r|<1` over `R` or `C`, while the formal
  identity lives in `K[[r]]`;
- the affine matrix description requires nonzero scale; the zero-scale update
  is treated separately as a degenerate constant map;
- an algebraic fixed point is not asserted to be attracting without a
  multiplier hypothesis;
- infinite continued fractions are assigned values only after convergence is
  established;
- `E_0` is identified with Paper I's canonical homogeneous hyperbolic model,
  not introduced as a competing definition.

## 5. Unresolved mathematical issues

The following remain open:

- an intrinsic projective arithmetic expression space carrying ripple data;
- quotient-stable or history-natural invariants derived from path/ripple
  geometry;
- a multi-wire extension;
- a general theory of formal, analytic, projective, and operational convergence
  for infinite arithmetic expressions;
- incorporation of further PCRG material after that repository is available to
  the connected source index.

## 6. Build result

GitHub Actions workflow **Paper 0 and Paper I build**, run `#13`
(`31301595247`), completed successfully at the validated manuscript head above.

The workflow:

- built `paper-0/aeg-paper-0.pdf`;
- built the revised `paper-1/aeg-paper-1.pdf`;
- found no undefined control sequences, unresolved references or citations, or
  multiply defined labels under its warning check;
- uploaded both PDFs as artifact `aeg-foundational-papers`.

The generated PDFs contain 23 pages for Paper 0 and 61 pages for Paper I. PDF
preflight found both files openable, unencrypted, and text-based. Visual review
covered the Paper 0 title, comb, point-path, ripple-pencil, reciprocal/fixed-point,
and projective-unification pages, together with the revised Paper I title,
Paper 0 prelude, transferred hyperbolic-model section, and final references.
No clipped text, overlap, broken glyphs, or missing figures were observed.

## 7. Remaining warnings

No blocking LaTeX warning remains. Ordinary typography warnings not covered by
the CI grep were not observed to cause clipping or overlap in the rendered
pages. The manuscripts remain drafts and need mathematical review beyond build
correctness.

## 8. Recommended next task

Review Paper 0 section by section for mathematical emphasis, especially:

1. whether the geometric-series example is the best elementary bridge from
   reciprocal to infinity;
2. whether the ripple pencil should be presented first through inversion or
   through a general pole-centered coordinate;
3. how much of Paper I's repeated elementary projective matrix material should
   remain for self-containment after Paper 0 is accepted;
4. whether the missing PCRG source contributes a distinct elementary theorem or
   only parallel terminology once it becomes accessible.
