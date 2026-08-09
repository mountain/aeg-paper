# Authoritative Amendment: Paper 0 Prelude

**Status:** Authoritative amendment  
**Version:** 1.0  
**Date:** 2026-08-09  
**Applies to:** The AEG paper-series architecture and the Paper I restructuring

This file explicitly amends `governance/00-authoritative-scope.md` and
`governance/01-paper-series-architecture.md`. Where those files describe a
four-paper series beginning with Paper I, this amendment takes precedence and
inserts the elementary Paper 0 specified below. All other scope restrictions of
the existing governance files remain in force.

## 1. Revised series architecture

The active manuscript series is:

0. **Arithmetic Expression Geometry 0: Paths and Ripple Pencils**  
   *Left and Right Expansions, Reciprocals, and Projective Unification*
1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
3. **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
4. **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

The dependency architecture is

```text
Paper 0 -> Paper I -> Paper II
                   -> Paper III
                   -> Paper IV
```

Paper 0 is an elementary prelude. It does not replace Paper I as the theorem-level
foundation of the later papers.

## 2. Paper 0 role

Paper 0 must develop the following material in a self-contained and elementary
form:

- explicit left-expanded and right-expanded comb conventions;
- parallel one-hole evaluation of the two pure combs;
- the affine point-path picture in the zeroth-kind upper-half-plane model;
- the projective ripple-pencil picture obtained by pulling horocycles back through
  Möbius maps;
- arithmetic reciprocals, denominator poles, the point at infinity, finite and
  infinite reciprocal expansions, and iterative fixed points;
- matrix representations of elementary arithmetic sections;
- projective unification of paths, poles, fixed points, and ripple pencils;
- the placement `Aff(1,K) = Stab(infinity) < PGL_2(K)` and elementary generation
  of `PGL_2(K)` by translation, nonzero scaling, and inversion.

Paper 0 may use the historical notation `E_0` provided that it explicitly
identifies the model with Paper I's canonical homogeneous hyperbolic model and
does not introduce a conflicting second definition.

## 3. Paper 0 exclusions

Paper 0 must not develop as a main theory:

- the intrinsic dependency-poset classification beyond the pure-comb proof;
- mixed-chirality marked spinal histories;
- the Hecke `q=4` history language;
- affine cocycles and global torsion;
- continuous affine flow as a full intrinsic theory;
- regular-zero rigidity or singular-zero classification;
- contact geometry, horizontal calculus, or function theory;
- projective bivaluations, quotient towers, or computational complexity;
- a general convergence theory for infinite arithmetic expressions.

Convergence claims for geometric series, continued fractions, or iteration must
state their field, topology, ordinary-domain, and attraction hypotheses.

## 4. Paper I after the transfer

Paper I retains the current marked-history terminology and formalism. This
amendment does not authorize a marked-history redesign.

Paper I remains the canonical owner of:

- intrinsic sequential-tree classification;
- marked planar sequential trees and bounded/free marked spinal histories;
- operand-slot chirality, mirror, reversal, and path inverse;
- projective evaluation of chronological histories;
- the `q=4` Hecke sublanguage;
- affine cocycles, continuous flow, and regular AES definitions;
- the complete homogeneous hyperbolic model and zero-set theorems;
- ACS torsion, contact curvature, and later-paper interfaces.

Paper I may repeat concise elementary matrix formulas and projective-generation
proofs for logical self-containment. Paper 0 is the canonical source for the
pedagogical path/ripple exposition and the reciprocal--pole--infinity discussion.

## 5. Claim status for Paper 0

The following are `proved with stated hypotheses`:

- unique internal evaluation order for each explicitly defined pure comb;
- the opposite-operation correspondence between right and left combs;
- the elementary matrix table for nondegenerate one-hole arithmetic sections;
- the upper-half-plane assignment identity for the zeroth-kind model;
- the line/circle formula for a pulled-back horocycle under a real
  orientation-preserving Möbius map;
- finite geometric-series and continued-fraction matrix recursions;
- affine and reciprocal fixed-point formulas;
- `PGL_2(K)` generation and rank-one Bruhat placement.

The terms `point path` and `ripple pencil` are descriptive definitions. They do
not assert a new isomorphism class of hyperbolic or projective geometry.

The following remain open programmes:

- a projective arithmetic expression space intrinsic to the ripple geometry;
- quotient-stable path/ripple invariants;
- multi-wire path/ripple semantics;
- a general theory of infinite arithmetic expressions.

## 6. Required repository changes

The canonical Paper 0 entry point is
`paper-0/aeg-paper-0.tex`. The root build script must accept target `0`, and the
repository overview must list Paper 0 before Papers I--IV. Paper I must include a
short interface statement identifying the transferred elementary material without
changing its marked-history definitions.
