# 018 — Assignment, duality, add-multiply decomposition and the Eikonal fill on the Cayley model

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (018: unifying the distribution of `a`, the `{∞,4}`/`{4,∞}` duality, level/gradient orthogonality, the add-multiply decomposition, and the Eikonal fill on the Cayley model).
> **Prerequisites**: Note XVII, *Cayley model and the conformal-hyperbolic unification* ([017-cayley-model-conformal-hyperbolic.md](017-cayley-model-conformal-hyperbolic.md)); Note XVI, *The C₂*C₄ normal form* ([016-c2c4-tearing-belyi-f7.md](016-c2c4-tearing-belyi-f7.md)).
> **Date**: 2026-11-15
> **Remark**: this note consolidates scripts 032–038; every statement is status-labelled (`PROVED` / `COMPUTATIONALLY VERIFIED EXAMPLE` / `STRUCTURAL PROPOSAL`).

---

## 1. The Cayley model in brief

The Cayley model `D∞` is the **Euclidean embedding** of the F₂ 4-regular tree `T₄`: recursive squares (L¹ balls `|x|+|y|≤R`, radius `2^step` halving with depth), the diagonals = the tree, the boundary `B∞` = the fractal border of the union. The metric is `g=(dx²+dy²)/L²` (`L` = Manhattan depth to the border, `K=−2`; Note 017). `T₄` is also the 1-skeleton of `{∞,4}`.

## 2. The assignment `a` on the Cayley tree (odd integers, collapse)

`a=−x/y` takes **odd-integer** values `2m+1` on the `ε₄` orbit. Carried to the Cayley tree nodes (square centres), it has the explicit formula (`g=[[A,B],[C,D]]`):

$$a(g\,\varepsilon_4)=(AD+BC)-\sqrt2(AC+BD).$$

**Oddness**: in both parity classes of `H(√2)`, `a≡1 (mod 2)` (`PROVED`, `029`). On the tree `a` is **not injective**: root `a=1`, four children `a=−1,3,7,3` (two share `a=3`) — `a` **collapses** the exponential tree many-to-one onto the odd integers of `Z[√2]` (`COMPUTATIONALLY VERIFIED`). Along the `U²J` axis `a=P_{2d+3}` (Pell numerators).

## 3. Primal `{∞,4}` and dual `{4,∞}`

- **primal `{∞,4}`** (black): the F₂ diagonal tree, nodes coloured by `a`;
- **dual `{4,∞}`** (blue): the **perpendicular bisector** of each primal edge, crossing at the `ε₂` midpoint. Each `ε₄` vertex is surrounded by a **dual 4-gon face**; the dual vertices (blue-line corners) are the cusps (`∞`-valent).

**Blue lines = zero lines**: the dual `{4,∞}` is the `Γ₄`-orbit of the `a=0` line (the imaginary axis; Notes 015/016 §3), i.e. the zero sets of the transported `a∘g⁻¹` (`STRUCTURAL PROPOSAL`, geometric realisation).

## 4. Level lines (rays) and gradient lines (circles) are orthogonal

For `a=−x/y`: level lines `a=const` are **rays** `y=kx` through the origin; the Euclidean gradient lines of `∇a=(−1/y,x/y²)` satisfy `dy/dx=−x/y` ⇒ **concentric circles** `x²+y²=const` (which are also `H²` geodesics). They are **orthogonal everywhere** (`COMPUTATIONALLY VERIFIED`). In the AES metric `g` (`μ=1,λ=2`) the gradient lines are **ellipses** `4x²+y²=const` (`g`-orthogonal).

## 5. The add-multiply decomposition (`μ=1,λ=2`)

Polar coordinates `a=−cot θ` split `(ρ,θ)` into add/multiply:

| object | reading |
|---|---|
| blue lines (`a=0`) | the **add-zero** line |
| origin | the `a=0/0` singularity, the **multiply-zero** (completed `a=0`) |
| green circles `ρ=4,2,1,0.5,…` | the **multiply scale** `1, 1/2, 1/4, 1/8,…` (halving) |
| 45°/135° diagonals | the **add axes**: `a=−1` (45°), `a=1` (135°), one `a↦a+1` step apart |

The four fit together: add runs along the rays, multiply along the circles, orthogonally; the add-zero (blue) and multiply-zero (origin) are the respective zero elements (`STRUCTURAL PROPOSAL`, built on the exact facts of `036`).

## 6. The Eikonal equation = the AES axiom

$$|\nabla a|^2=\mu^2+\lambda^2a^2\quad(\text{def:regular-aes}),\qquad a=\frac{\mu}{\lambda}\sinh(\lambda s),\ |\nabla s|=1.$$

Both faces satisfy it (numerically `1.1×10⁻¹³`):

- **angular face (E₀)** `a=−x/y`: level lines = rays;
- **radial face (flat/Hecke)** `a=(μ/λ)sinh(λs)`: level lines = concentric circles (`e^s`).

"Fill the space + agree with the skeleton" is `PROVED` for these two known solutions; "unique reconstruction from the skeleton alone" is a `STRUCTURAL PROPOSAL` (needs well-posedness conditions).

## 7. Eikonal on the Cayley model: countably many ridge singularities

On the Cayley model `L` is piecewise-linear with `|∇L|=√2`, so `a=(μ/λ)sinh(λL)` satisfies

$$|\nabla a|^2=2(\mu^2+\lambda^2a^2).$$

The gradient of `L` jumps along the **ridges** (where the nearest square changes — the medial axis / Voronoi ridges). The squares are **countable** ⇒ the ridges are **countable** ⇒ the Eikonal solution is **piecewise smooth with shocks along countably many ridges**. This is the correct form of "drawing the Eikonal interior points on the Cayley model" (`038`, `COMPUTATIONALLY VERIFIED`).

## 8. Status summary

| result | status |
|---|---|
| `a(g ε₄)=(AD+BC)−√2(AC+BD)∈2Z+1` | `PROVED` |
| `a` is not injective on the tree (collapse) | `COMPUTATIONALLY VERIFIED` |
| primal/dual orthogonality, dual 4-gon faces | `COMPUTATIONALLY VERIFIED` |
| level lines (rays) ⊥ gradient lines (circles) | `COMPUTATIONALLY VERIFIED` |
| add-multiply decomposition (blue=add-zero, origin=multiply-zero, green=multiply scale, 45°/135°=add axes) | `STRUCTURAL PROPOSAL` |
| Eikonal = AES axiom, both faces satisfy | `PROVED` (`1e-13`) |
| Cayley Eikonal: piecewise fill with countably many ridge singularities | `COMPUTATIONALLY VERIFIED` |

## Appendix: script index

`032` a on the Cayley model · `033` primal/dual overlay · `034` level/gradient orthogonality · `035` gradient lines on Cayley · `036` add-multiply decomposition · `037` Eikonal two faces · `038` Eikonal on Cayley + countable ridges.
