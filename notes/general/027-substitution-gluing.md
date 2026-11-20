# 027 — Substitution = gluing: the fire method as the interface of composition

> **Document type**: AEG research note (027: a structural proposal that the fire method turns *substitution* of arithmetic programs into *gluing* of punctured AEG surfaces)
> **Date**: 2026-11-20
> **Status**: the ground fact is `PROVED`; the correspondence itself is a `STRUCTURAL PROPOSAL` with three `OPEN PROBLEM`s; no new computation.

---

## 1. Ground: the fire method is the AES evaluation, not an analogy

Note [018 §6](018-cayley-assignment-duality-eikonal.md) already records that the Eikonal equation
$$|\nabla a|^2=\mu^2+\lambda^2 a^2$$
is the regular-AES axiom, i.e. **the fire method is the geometric form of AES**. Hence the arrival time (the wavefront $C_t$) *is* the value, and the sweep of $C_t$ across the surface *is* the ordered evaluation history. There is nothing extra to "attach": the fire method is the computation.

## 2. The three-level correspondence

| arithmetic / computation | geometry (fire method) |
|---|---|
| expression (with input slots) | punctured (= cusped) AEG surface |
| **substitution** (compose, plug a sub-expression into a slot) | **gluing** along a cusp |
| ordered evaluation history | the wavefront $C_t$ sweeping the surface |
| value (endpoint) | node / where the front arrives |

The reason substitution = gluing is exactly the composition/pullback structure of [algebra/01 §2](../algebra/01-finite-layer-exponential-polynomials.md) — $\operatorname{ev}(D_*\gamma,\varphi)=\operatorname{ev}(\gamma,D^*\varphi)$, $(E\circ D)^*=D^*\circ E^*$ — read geometrically: the wavefront flowing out of one surface's hole is the input flowing into the other's slot. Substitution is the requirement that **the front be continuous across the gluing**.

## 3. The interface data (what the fire method contributes)

The notes 021–026 supply exactly the local data one must match at the gluing:

1. **cut locus = gluing seam** ([018 §7](018-cayley-assignment-duality-eikonal.md), [021](021-fire-front-twist-flat-torus.md)): the walls of the fire-method fundamental domain are the collision locus of the fire with its deck copies (the Voronoi/medial ridge). The collision points are the future "slots".
2. **half/full clock** ([026](026-firefront-trichotomy.md)): the crossing is born at $t=\|\gamma\|/2$ (two fronts tangent) and the front reaches the deck image $\gamma p$ at $t=\|\gamma\|$. A sub-expression's **full-displacement arrival** is the parent slot's **input time**.
3. **direction circle** ([023](023-gauss-word-alignment.md)): the asymptotic direction of a crossing is the boundary endpoint of the perpendicular bisector — the phase/angle that must align at the gluing.

## 4. The proposal

> **Structural proposal (substitution = gluing).** Two punctured AEG surfaces glued along a cusp correspond to two arithmetic programs composed by substitution, provided their **wavefront arrival structures at the gluing cusp match**: arrival time (half/full displacement), direction (bisector endpoint), and collision pattern (cut locus). This matching is the geometric form of the substitution rule — the sub-expression's output flow is the parent slot's input flow.

## 5. Open problems

1. **Exact matching condition.** At a cusp the front approaches along horocycles; the precise alignment of the two horocycle flows (the cusped analogue of the Fenchel–Nielsen twist parameter) that constitutes a legal substitution is not yet written down.
2. **Spectral decomposition.** How do the length spectrum, $N(t)$, and the cut locus of the glued surface assemble from those of the two pieces? This is the substitution rule at the level of spectral data; if it has a clean form, it is the "arithmetic of substitution".
3. **Cusp vs finite boundary.** The machinery here (021–026) is on the *cusped* thrice-punctured sphere $\Gamma(2)$; the finite-boundary pair of pants needs the half/full clock and cut locus ported to finite boundary lengths before the Fenchel–Nielsen picture is fully available.

## 6. Status

| Result | Status |
|---|---|
| fire method = Eikonal = AES axiom | `PROVED` ([018 §6](018-cayley-assignment-duality-eikonal.md)) |
| substitution = gluing, as a geometric form of composition | `STRUCTURAL PROPOSAL` |
| cut locus / half-full clock / direction circle as interface data | `PROVED` (021–026) |
| exact cusp matching condition | `OPEN PROBLEM` |
| spectral decomposition of the glued surface | `OPEN PROBLEM` |
| finite-boundary pair of pants port | `OPEN PROBLEM` |
