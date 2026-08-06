# Paper III Decision Record

**Paper:** *Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes*

**Subtitle:** *Multi-Zero Constructions, Discriminants, and Topological Transport*

**Decision date:** 2026-08-06

**Baseline:** `24c1df0`

**Status:** integrated manuscript decisions

This record fixes the conventions and claim boundary of the canonical Paper III
manuscript.  It is subordinate to the restructuring authorities and should be read
with `paper-III-source-audit.md` and `paper-III-closure-report.md`.

## D3-01 — Historical names are not imported as theorems

The Git history contains no certifiable general `E_k`, `E_log`, or multi-zero AEG
construction.  Paper III therefore uses descriptive names: parallel multi-zero
model, logarithmic-cover model, cylindrical product tube, and helical zero tube.
The old symbols remain provenance labels only.

## D3-02 — Metric realization and rigidity are separate questions

For any surface submersion `a` and background metric `h`, Paper III uses

```text
g_a = |da|_h^2 / (mu^2 + lambda^2 a^2) h.
```

This proves broad existence.  It also shows that the bare singular-AES category is
too flexible to support an AEG-specific singularity classification.  Completeness,
curvature, asymptotics, homogeneity, a fixed metric, or expression-history
naturality must be added before a rigidity claim is made.

## D3-03 — Seven zero-object levels remain distinct

The canonical order is:

1. total zero set;
2. smooth zero incidence;
3. proper zero tube;
4. embedded zero tube;
5. threaded zero tube;
6. braid closure;
7. knot invariant.

Every transition requires new hypotheses or data.  The manuscript never uses a
later name merely because an earlier object has been drawn.

## D3-04 — Tube means proper submersion

A zero incidence is called a tube only when its projection is a surjective proper
submersion, with neat relative hypotheses at a boundary.  Ehresmann then supplies
local triviality.  The historic disjoint union of ambient AEG slices is called an
ambient family, not a certified zero tube.

## D3-05 — Rank controls transport

A real assignment on a surface has rank one and regular zero curves.  A
complex-valued field has real rank two and isolated roots.  Ordinary Artin braid
monodromy belongs to the second setting.  It is not inferred directly from a real
assignment-zero tube.

## D3-06 — The structural discriminant has several mechanisms

The manuscript separates critical-zero, boundary, singular/metric, domain/category,
and nonproper escape loci.  Ordinary projective poles are recorded separately.
The escape family proves that topology can change at infinity without a critical
zero at a finite point.

## D3-07 — Compact real tubes over a circle are zero tori

For boundaryless surface fibers with a smooth global orientation of the vertical
tangent bundle, a proper regular real zero tube over `S^1` is an orientable mapping
torus of finitely many circles.  Each connected component is a torus.  A merely
fiberwise, discontinuous orientation choice is insufficient and can allow a Klein
bottle.  This classifies the abstract total zero surface under the printed
hypotheses; it does not select a knot inside it or classify its embedding.

## D3-08 — The helical family is the central explicit tube

On `[-L,L] x S^1` over `S^1`, Paper III uses

```text
A(x,y,theta) = exp(n x) sin(n y - m theta).
```

The conformal metric, properness, neat boundary, `2n` zero intervals, label shift
`k -> k+2m mod 2n`, `2 gcd(n,m)` annular components, logarithmic deck shift, and
boundary homology class are all proved.  The torus-link name is used only after the
ordered torus coordinates are declared.

## D3-09 — Real Morse events and complex branching are different

The real models `x^2+y^2-tau` and `x^2-y^2-tau` are singular-AES birth/death and
reconnection examples.  The complex model `w^2=tau` is a branched root filling.
Its boundary is collision-free and carries a half-twist; the collision lies in the
filling.  None of these examples is advertised as a universal AEG metric normal
form.

## D3-10 — Every-braid realization is a function-theory theorem, not an invariant

Paper II's arithmetic-holomorphic coordinate allows any configuration loop in a
small disc of the basic hyperbolic AES to be encoded by a monic square-free
polynomial.  This realizes every braid and, by closure, every link.  Because the
construction is universal and chosen, representability alone has no separating
power.

## D3-11 — Logarithmic labels have lift gauge

For moving nonzero roots, individual logarithmic endpoint integers depend on the
initial lifts.  Their gauge law is

```text
k_i -> k_i + m_i - m_{sigma(i)}.
```

Cycle sums and total winding are gauge invariant; the full noncommutative datum
remains the configuration path or annular braid.

## D3-12 — A thread is a declared finite multisection

A finite zero thread over a one-manifold base is a properly embedded
one-dimensional submanifold inside a real zero tube whose projection is a
finite-sheeted covering, with the corresponding relative-boundary condition.  A
transverse slice such as `x=c` in the helical model is a valid thread only with that
probe choice recorded.  Intrinsic threading requires a functorial selection theorem
and remains open.

## D3-13 — Scalar and affine candidates pass a novelty filter

Every stateless additive scalar on a braid group factors through writhe and becomes
trivial under compatible two-sided Markov stabilization.  Fixed-multiplier affine
conjugation is exactly an Alexander quandle, and its ordinary torsion cocycle is a
coboundary.  Variable-multiplier Reidemeister-III defect is only an anomaly formula,
not an associator or higher invariant.

## D3-14 — Resonant twisted torsion is algebraically nonzero but planar-trivial

Over `F_q`, with `t != 1`, quandle parameter and coefficient action both
`alpha=t^{-1}`, the affine torsion

```text
kappa(x,y) = (t-1)(y-x)
```

is a normalized twisted 2-cocycle and is not a coboundary.  The finite-order
recurrence proves the nonzero cohomology class for arbitrary one-cochains.  However,
it is the obstruction cocycle of an explicit Alexander-module extension.  The
standard state sum of every planar classical link consequently equals the Alexander
quandle coloring count.  Cohomological nontriviality is not relabeled as nontrivial
knot detection.

## D3-15 — Knot and beyond-Burau claims remain gated

No new AEG knot invariant is claimed.  A future candidate must prove braid
relations, conjugation, positive and negative stabilization, and independence of
lift, probe, thread, spine, axis, basepoint, and presentation as applicable.  A
claim beyond Alexander/Burau additionally requires an explicit closure-level
separation pair under a declared baseline.

## D3-16 — The figure-eight computation remains a word calculation

Under the printed affine convention, the free word `abbbaBAAB` has translation
`-(t^2-3t+1)`.  It descends to the corresponding knot-group representation only on
the zero locus of that polynomial.  At generic `t` it is a relator failure, not an
intrinsic knot invariant.
