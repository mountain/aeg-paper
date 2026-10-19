# Experiment 6 — narrowed successor v1.1

This report supersedes the v1 interpretation at
`1556eaedaee0946b2e395320739234dc59ec846c`. The exact old report, evidence and
fixtures are indexed by full Git identity in
`../reviews/2026-10-19-repair-history.json`. The original rejection review is
retained in `../reviews/2026-10-14-independent-review.md`.

## Motion certification

Positive self-embedding certification now requires a checked simple initial
polygon and a rigid translation on every affine time segment. Closed polygons
require at least three nodes. The primary static check covers distinct nodes,
nonzero edges, nonadjacent intersections and adjacent overlap. Equal node
displacements at every breakpoint imply equal displacement throughout each
PL interval. Translation preserves all static incidence relations.

The second route independently checks static squared segment distances;
adjacent rays overlap precisely when their Gram determinant vanishes and their
dot product is positive. It checks that every node vector relative to node 0
is constant. Both routes therefore preserve simplicity through translation
without relying on omitted adjacent-edge interval conditions.

Nontranslations may return an exact invalidity witness, or `not-certified`.
They cannot return `valid` from the whole-interval checker. The optional
keyframe-only procedure remains an explicitly unsound distortion control, not
a certificate. General deformations are an open extension, not a solved case.

The original 20 moving-obstacle interval certificates still verify. The
certified margin is 3/4; the independently calculated minimum squared distance
is 400/101, attained at t=301/808. The second path collides at t=3/8. Its time
map includes a waiting interval; no strictly increasing reparameterisation or
physical speed-constrained rope claim follows.

## Signed-word calculations

The functions named R1/R2 retain their historical API names but act only on
abstract signed words. The committed R2 witness violates necessary planar
Gauss parity at labels 3 and 4. Round-trip and sign-sum checks remain exact
syntactic statements. They are not evidence of planar realisability, a local
disk move, Reidemeister soundness, or a faithful knot-process interface.
Gauss parity alone would not be a sufficient planar realisability certificate.

## Environments and encoding gates

A tame simple curve on a tame embedded sphere bounds a disk. A torus has a
different boundary: a primitive (2,3) curve on the standard embedded torus is a
trefoil. Meridian/longitude comparisons with free R3 use the standard unknotted
torus and fixed framing. A surface basis swap changes the equivalence contract;
it is not assumed isotopic to identity or extendible in a specified ambient
space. Writhe is a diagram statistic. Nonzero linking obstructs splitting;
zero linking does not certify splitting.

| Gate | Current status |
|---|---|
| A | Finite literal encode/decode checks; no arithmetic-geometric simulation |
| B | Literal code equality is finer than the declared topological equivalence; this refutes that equality, not every possible faithful arithmetic representation |
| C | Literal action sequence, concatenation and endpoint replay only; knot-process faithfulness not certified |
| D | Terminating bounded checks with unknown/not-certified outcomes; no general knot or dynamic-obstacle decision procedure |

## Verification

`python3 tools/ci_check.py` checks an explicit inventory, immutable old contract
pins, fresh main and raw outputs, derived fixtures, and normal/optimized/hash
seed agreement in temporary directories. It does not rewrite recorded evidence
or refresh contract digests. `reviews/verify_repairs_2026_10_19.py` checks the
collapsing triangles (including t=1/3), adjacent overlap, edge collapse,
undersized polygons, nontranslations, and integrity mutations. It also repeats
the independent 5461-row braid check and the 20 timing certificates.

All results are restricted to these profiles. Paper IV, process-geometry and
Adva may receive documentary references; no native execution, continuation or
learning authority is granted.
