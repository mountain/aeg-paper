# PPCT lattice attribution — verification

Finite computation accompanying
`notes/analysis-and-calculus/28-ppct-lattice-attribution.md` (OQ-098.2).

## What is verified

`verify_lattice.py` distinguishes the two candidate lattices on plane planted
cubic trees (PPCTs):

1. **Tamari / rotation lattice.** PPCTs ordered by the transitive closure of the
   rotation `N(N(a,b),c) -> N(a,N(b,c))`. For `n = 5` leaves (14 trees, Tamari
   `T_4`) the script confirms it **is** a lattice but it is **not distributive**:
   an explicit triple violating `a∧(b∨c) = (a∧b)∨(a∧c)` is recorded in
   `evidence-v1.json`.

2. **Birkhoff down-set lattice of the infinite binary tree.** The number `R(N)`
   of down-sets with `N` vertices satisfies `R(0)=1`,
   `R(N)=sum_{i=0}^{N-1} R(i)R(N-1-i)`, i.e. `R(N)=Catalan(N)`; checked for
   `N = 1..8`. By Birkhoff duality this lattice is distributive and its
   join-irreducibles are the vertices of the infinite cubic tree.

## Conclusion

The Pushkarev–Byzov phrase "distributive lattice whose irreducible elements are
ordered as the vertices of the infinite cubic tree" is the **Birkhoff down-set
lattice**, not the Tamari (rotation) lattice. AEG's `O(P)` (down-sets of a finite
dependency poset) is the same construction over a finite poset; the two are not
isomorphic in general.

## Status

`COMPUTATIONALLY VERIFIED EXAMPLE` for the finite statements above (`n = 5`
Tamari, `N ≤ 8` Catalan count). The general statements (Tamari non-distributive
for all `n`, Birkhoff distributivity) are classical and cited, not re-proved; no
independent human review is asserted.

## Reproduce

```bash
python3 verify_lattice.py evidence-v1.json
```
