# Paper I — Foundations

**Provisional title:** *Arithmetic Expression Geometry I: Foundations*  
**Subtitle:** *Sequential Histories, Projective Semantics, and Zero Geometry*

**MSC 2020:** 20H10 (primary); 05C05, 58K05; 20G15, 68Q42, 53C21

Paper I develops the layer that the geometry of Paper 0 presupposes: the syntax
of process and the projective semantics of arithmetic words.  It contains:

1. the classification of finite binary expression trees with a unique legal
   internal evaluation order, and the marked spinal histories of such trees;
2. operand-slot chirality, kept distinct from temporal reversal and from
   functional inversion;
3. projective evaluation of non-degenerate bilateral histories, generation of
   `PGL_2(K)`, the affine/Borel sector, and the rank-one Bruhat decomposition;
4. the `q=4` Hecke sublanguage over `Q(sqrt2)` and its history-level relations;
5. the zero theory of regular arithmetic expression spaces: the regular zero
   locus, the complete splitting theorem and its no-go consequence, the
   definition of a singular arithmetic expression space, a verified
   isolated-zero model, and the parameter-family zero-set lemma with its
   properness warning.

The paper imports exactly one geometric definition from Paper 0 — the regular
AES and its canonical arithmetic frame — because its zero theorems are stated in
those terms.  Everything else that earlier versions of this paper developed
(arithmetic expression spaces, motions, the hyperbolic and punctured models,
affine cocycles, the accumulative commutative space, tearing, and the contact
structure) is now proved in Paper 0 under the amendment
`governance/00b-paper-0-geometric-foundation-amendment.md`, and is cited here
rather than repeated.

## Revision of 2026-10-29

Two review findings were acted on.  First, the generation theorem
`thm:bilateral-pgl2-generation` was proved here and in Paper 0 with the same
factorization computation; the proof of the deletion route chosen by the series
rule "one canonical source per result" now stands only in Paper 0 (its chapter on
matrix and projective unification), and this paper keeps the history-level
statement, its three-line derivation, the affine-sector corollary
`cor:affine-borel-sector` (which is not in Paper 0), and the `q=4` Hecke
sublanguage.  Second, notation that belonged to Paper 0 was removed from the
appendices: the accumulated-scale and cocycle rows of the Appendix A notation
table, and Appendix B's two examples built on the accumulative commutative space
and on the open/closed torsion pair, which are already proved in Paper 0's
chapters on commutativization and on the contact model and computed in its
appendices C and D.  Appendix B now defines the two step families `A_p`, `M_q`
that it uses, and records their two totals as bookkeeping only.  The reported
"ace" typo in the abstract was not present in the source or the built PDF of
this version; no correction was needed.

## Canonical source closure

```text
paper-1/
  aeg-paper-1.tex
  sections/
    00-paper-zero-interface.tex
    01-introduction.tex
    02-sequential-histories.tex
    03-projective-affine.tex
    04-regular-aes-interface.tex
    05-zero-geometry.tex
    06-conclusion.tex
  appendices/
    app-A-conventions.tex
    app-B-equality-neutrality.tex
```

## Claim boundary

Proved here, at the statuses recorded in `governance/05-mathematical-status.md`:

- the four equivalent characterizations of a sequential tree, and the
  marked-tree/history correspondence;
- the separation of mirror, temporal reversal, and path inverse;
- projective evaluation compatibility with chronology, generation of
  `PGL_2(K)` (derived from Paper 0's generation theorem), and the affine/Borel
  placement;
- the order-four Hecke relation realized by an explicit marked history;
- the regular zero locus and its local rigidity; the complete regular splitting
  `M = Z(a) x R` for connected complete boundaryless regular spaces; the
  submersive total zero set of a spatially regular family; and the verified
  isolated-zero singular model.

Open problems are listed in the concluding chapter; they concern the Hecke
history fibers, singular multi-zero models, properness upgrades, history
complexity, and the relation between ordinary admissibility and projective
non-degeneracy.

Build from the repository root with `./build.sh 1`.
