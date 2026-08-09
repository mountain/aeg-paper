# Paper 0 Source and Claim Audit

**Status:** Audit record  
**Date:** 2026-08-09  
**Canonical entry point:** `paper-0/aeg-paper-0.tex`

## 1. Purpose

Paper 0 was introduced to place the earliest path-based AEG exposition and the
later bilateral/projective completion into one elementary prelude. It does not
change the marked-history definitions of Paper I.

## 2. Provenance

The source families used are:

| Material | Historical source | Paper 0 treatment |
|---|---|---|
| right- and left-expanded examples | archived legacy root manuscript, Basic Concepts | repaired conventions and parallel recursive definitions |
| path notation and bounded/free paths | archived legacy root manuscript | rederived as chronological pure-comb evaluation |
| `E_0` grid and assignment `a=-x/y` | archived legacy root manuscript and canonical Paper I hyperbolic model | concise proved elementary model |
| curved grid under inversion | archived legacy remark | expanded into the ripple-pencil theorem |
| one-hole bilateral sections and matrix table | `notes/projective-condensation/01-bilateral-projective-condensation.tex` and Paper I | retained in elementary self-contained form |
| affine fixed-point closure | legacy Paper I appendix and projective-condensation notes | separated from attraction and operator identity |
| reciprocal as geometric-series closure | projective-condensation/PAL notes | rewritten with finite, analytic, and formal convergence hypotheses |
| continued-fraction recursion | bilateral projective notes and standard matrix calculus | rederived with explicit ordinary-domain warning |
| pole/infinity and affine gauge | projective-condensation notes | restricted to elementary projective-coordinate claims |

The `mountain/pcrg-paper` repository was named as a possible comparison source,
but it was not available through the connected repository index during this
edit. No unsupported PCRG claim has therefore been imported.

## 3. New derivations in Paper 0

The following formulations are new to the canonical series and are proved in
Paper 0:

1. the explicit chronological pair of pure-comb recursions `L_k` and `R_k`;
2. the opposite-operation proposition under that indexing convention;
3. the path/condition-pullback distinction;
4. the ripple-pencil line/circle formula
   for `F^{-1}(Im w=t)` and its tangency at `F^{-1}(infinity)`;
5. the four-readings theorem for one prefix matrix: point, pole, fixed points,
   and ripple pencil;
6. the explicit link between the pole of `1/(1-r)`, disappearance of the finite
   fixed point of `s -> 1+rs`, and the parabolic fixed point at infinity;
7. the ownership/interface statement separating Paper 0 from Paper I.

## 4. Claim ledger

| Claim | Status |
|---|---|
| unique internal order for explicitly defined pure combs | proved |
| comb opposition through `omega^op` | proved |
| `E_0` assignment/eikonal identity | proved |
| arithmetic compatibility of the grid moves | proved |
| horocycle pullback line/circle formula | proved for real positive-determinant Möbius maps |
| Apollonius zero--pole level-set formula | proved where the displayed zero/pole coordinates are finite |
| geometric-series finite formula | proved |
| geometric-series analytic limit | proved under `|r|<1` |
| formal series identity | proved in `K[[r]]` |
| affine iteration and convergence | proved with stated hypotheses |
| reciprocal fixed-point equation and local multiplier test | proved |
| `PGL_2(K)` generation | proved |
| projective AES intrinsic to ripple pencils | open |
| general convergence theory for infinite arithmetic expressions | open |
| history-quotient invariant derived from ripple data | open |

## 5. Canonical source closure

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

The build uses `bibliography/aeg-paper.bib`. No archived source is included by
TeX input.

## 6. Paper I migration boundary

Moved in expository ownership:

- elementary pure left/right comb comparison;
- path geometry of the basic grid;
- inversion as a curved/ripple grid;
- reciprocal--pole--infinity and elementary fixed-point discussion;
- elementary matrix synthesis.

Retained in Paper I:

- marked spinal history terminology and definitions;
- intrinsic sequential-tree classification;
- mixed chirality and reversal/inverse distinctions;
- theorem-level projective history evaluation and Hecke interface;
- affine flow, full hyperbolic theorem, zero rigidity, torsion, and contact
  geometry.

Paper I repeats some matrix statements for logical self-containment; this is an
intentional interface duplication, not divergent ownership.
