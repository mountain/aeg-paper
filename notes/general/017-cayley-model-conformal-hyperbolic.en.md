# 017 — The Cayley model and the conformal-hyperbolic unification of {∞,4}: g = (dx²+dy²)/L² and the three realizations

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (017: the Cayley model of the F₂ 4-regular tree, its hyperbolic metric `g=(dx²+dy²)/L²`, and the conformal unification of the Poincaré / Cayley / Hecke realizations of `{∞,4}`).
> **Prerequisites**: Note XVI, *The C₂*C₄ normal form* ([016-c2c4-tearing-belyi-f7.md](016-c2c4-tearing-belyi-f7.md)); the earlier *Cayley model* note ([01-cayley-hyperbolic-model.tex](../../notes/foundations-and-geometry/01-cayley-hyperbolic-model.tex)); the TikZ source ([cayley-tree-4-border.tex](../../images/sources/cayley-tree-4-border.tex)).
> **Date**: 2026-11-15
> **Remark**: this note merges the 2025-07 "Cayley model" with the 2025-11 `{∞,4}` thread; reproduction script [030-cayley-model-hyperbolic.py](030-cayley-model-hyperbolic.py), proof script [031-conformal-hyperbolic-proof.py](031-conformal-hyperbolic-proof.py).

---

## 1. The Cayley tree 4-border construction = the F₂ 4-regular tree = T₄

The TikZ source `cayley-tree-4-border.tex` constructs, recursively: at each node a **square (= an L¹ ball `|x|+|y|≤R`, radius `R=2^step` halving with depth)**, whose two diagonals are the embedded F₂ 4-regular tree; each node sprouts 3 children at its top vertex (rotations `−90°, 0, +90°`), the root has 4 branches (`0°, 90°, 180°, −90°`). Edge lengths halve as `s_n = L_0/2^n`, and the boundary `B_n` of the union of squares is **fractal** in the limit.

**Key**: this tree is the 1-skeleton `T₄` of the `{∞,4}` tiling (the `C₂*C₄` tree of Note 016), embedded in the Euclidean plane. The left panel of `030` reproduces it: 53 squares, 156 edges.

## 2. The hyperbolic metric `g=(dx²+dy²)/L²` and `K=−2`

The metric proposed in the earlier note 01 (computed and verified in `030`):

$$g = \frac{dx^2+dy^2}{L^2},\qquad L(x,y)=\text{Manhattan distance to the border (depth)}.$$

`L` is piecewise-linear (`L=±x±y+C`), so `ΔL=0`, `|∇L|²=2`, and the curvature `K=LΔL−|∇L|²=−2` (numerically `−2.000`). Hence `g` is a constant-negative-curvature (`−2`) hyperbolic metric: **the fractal border sits at infinite intrinsic distance**.

## 3. Lemma: harmonic depth ⟹ constant curvature (proved symbolically in `031`)

For `g=(dx²+dy²)/f²` (`f>0`), the Gaussian curvature is

$$K = f\,\Delta f - |\nabla f|^2.$$

**Proof**: a conformal metric `g=e^{2φ}(dx²+dy²)` has curvature `K=−e^{−2φ}Δφ`. With `φ=−ln f`: `e^{−2φ}=f²`, `Δφ=−Δ(ln f)=−(fΔf−|∇f|²)/f²`, so `K=fΔf−|∇f|²`. **Corollary**: if `Δf=0` (harmonic) and `|∇f|=c` (constant speed), then `K=−c²`. ∎

## 4. The three `{∞,4}` realizations and the depth correspondence

| model | depth `f` | `Δf` | `|∇f|²` | `K` | type |
|---|---|---|---|---|---|
| **Poincaré** `H²` | `f=y` (height) | `0` | `1` | **−1** | hyperbolic |
| **Cayley** `D∞` | `f=L` (Manhattan depth) | `0` (piecewise) | `2` | **−2** | hyperbolic |
| **Hecke** `W`-plane | `f=\|W\|=e^s` (radial) | `1/\|W\|` | `1` | **0** | **flat** |

**Conclusions**:

1. **Poincaré ≅ Cayley**: the same hyperbolic plane, differing only by the homothety `g_C = ½ g_P` (`K=−2 = −1·2`). The Cayley model is not a new space but `H²` in the "Euclidean plane + conformal factor `1/L²`" guise.
2. **The Hecke flat `g₄=|dζ|²` (`K=0`) is the developing map**: it straightens the zero set into the `s=0` line (a rectification), not a hyperbolic model itself.
3. **Depth correspondence**: the "distance-to-boundary" functions of the three models play the same role

$$y\ \sim\ L\ \sim\ e^s = |W|,$$

being the conformal factors that push the boundary to infinity, differing only in curvature normalization (`1, 2, 0` ↔ `K=−1,−2,0`).

In one line:

> **The three realizations of `{∞,4}` form one conformal-hyperbolic structure: Poincaré and Cayley are the same hyperbolic plane (up to a homothety), the Hecke flat metric is its developing map / rectification; the depth function `y ∼ L ∼ e^s` is an invariant of this conformal class.**

## 5. Status summary

| result | status |
|---|---|
| F₂ 4-regular tree = `T₄` (Euclidean embedding of the Cayley tree 4-border) | `PROVED` (construction + `030`) |
| curvature identity `K=fΔf−|∇f|²` | `PROVED` (standard, `031` symbolic) |
| Poincaré `K=−1`, Cayley `K=−2`, Hecke `K=0` | `PROVED` (symbolic; Cayley piecewise + `030` numeric) |
| `g_C = ½ g_P` (homothety) | `PROVED` |
| Hecke flat = developing map | `STRUCTURAL PROPOSAL` (reading of `paper-3 thm:q4-hecke-zero-network`) |
| depth correspondence `y ∼ L ∼ e^s` as a conformal invariant | `STRUCTURAL PROPOSAL` |

## Appendix: script index

`028` C₂*C₄ tree (collision-free) · `029` a-formula + distribution · `030` Cayley reproduction + `K=−2` · `031` conformal-hyperbolic lemma.
