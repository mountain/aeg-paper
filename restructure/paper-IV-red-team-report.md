# Paper IV Mathematical Red-Team Report

**Date:** 2026-08-07  
**Manuscript:** *Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity*  
**Status after repair:** no known blocking mathematical or claim-boundary finding

## Findings repaired before closure

1. **Right continuation was initially stated too strongly.**  A single right
   update descends under `k^{-1}Hk ⊆ H`; only reversible right continuation or a
   right group action forces the normalizer condition.
2. **Residual action required a total state space.**  Partial arithmetic is now
   totalized with an absorbing invalid state, and the residual quotient includes
   every reachable totalized state.
3. **Online realization needed equivariance.**  The exact-machine definition now
   requires state transitions to update from the encoded state rather than from
   a hidden copy of the full past.
4. **Variable-length bit counting lacked a decoding convention.**  The theorem
   now uses fixed-width states or prefix-free encodings with bounded maximum
   length.
5. **The summed state bound was overinterpreted.**  It is now named
   fixed-register capacity--time and is related to actual memory--time only under
   an explicit snapshot-charging rule.
6. **Completed-node sets were used beyond their valid model.**  General
   workspace is now defined from live configurations; a frontier formula is
   retained only in a no-recomputation, last-use-retention model.
7. **Horner injectivity needed a characteristic hypothesis.**  The theorem is
   now characteristic-zero, with modular collisions stated separately.
8. **OBDD width could be mistaken for a universal lower bound.**  The manuscript
   now states the fixed representation and variable-order boundary and emphasizes
   that the restriction operators commute.
9. **Projective butterflies lost exact scalar data.**  The local quotient lemma
   is separated from full multi-wire `GL` semantics and inverse normalization.
10. **Static twiddle storage was conflated with dynamic state.**  The two are now
    assigned to description and live-state coordinates, respectively.
11. **Endpoint cost differences were called process residue too freely.**  Exact
    additive and group-valued labels are proved to telescope; nontrivial holonomy
    remains open.
12. **Matrix intermediate entries were close to being read as peak space.**  The
    text now records allocation, retention, overwrite, blocking, and temporaries
    as additional hypotheses.

## Independent finite checks

The dependency-free verification script checks seven groups:

- rank-one projector idempotence;
- `PGL_2(F_q)` counts, cosets, and right-descent/normalizer equality for
  `q = 3,5,7`;
- radix injectivity and histogram counts;
- block/interleaved equality residual widths for `n <= 5`;
- butterfly factorization and primitive NTT roots in `F_257`;
- matrix-chain and reverse-chain arithmetic counts;
- the finite fiber--image inequality.

All groups pass in the closure build.

## Remaining open boundary

No red-team repair turns the manuscript into a proof that noncommutativity,
negative curvature, hyperbolic growth, or quotient-fiber size implies
computational hardness. Those implications remain explicitly excluded.
