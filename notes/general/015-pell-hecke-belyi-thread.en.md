# 015 — Pell, the {∞,4} tiling, the Hecke Hauptmodul, and Belyi maps: non-trivial zero sets and the threading polynomial

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (015: consolidation of the Pell thread — the unifying constant, the Hecke zero network, dual grids, the flat structure, Belyi/dessins, and the threading polynomial).
> **Prerequisites**: Note I, *The HTWR Core* ([001-htwr-core.md](001-htwr-core.md)); Note II, *The Exact Spacetime Pareto Frontier* ([002-htwr-example.md](002-htwr-example.md)); Note IV, *Test Sequences* ([004-test-sequences.md](004-test-sequences.md)); Note XIV, *The Pell master figure* ([014-pell-master-figure.md](014-pell-master-figure.md)).
> **Date**: 2026-11-15
> **Remark**: this note consolidates the visualization/computation scripts 011–027 (each with its `.py`/`.png`); every statement is status-labelled (`PROVED` / `COMPUTATIONALLY VERIFIED EXAMPLE` / `STRUCTURAL PROPOSAL` / `OPEN`).

---

## 1. The unifying constant k

$$k := 3-2\sqrt2 = (\sqrt2-1)^2 = \lambda^{-2} = \left|\frac{\mu}{\lambda}\right|,\qquad \lambda=1+\sqrt2,\ \mu=1-\sqrt2.$$

`k` is simultaneously: the Pell contraction factor `|μ/λ|`; the inverse square `λ⁻²` of the silver ratio; the fundamental constant of the `{∞,4}` tiling (the Math.SE construction); and the convergence rate `|x_n − √2| = 2√2·kⁿ(1+o(1))`. **Status**: exact identities (`COMPUTATIONALLY VERIFIED EXAMPLE`).

## 2. The {∞,4} tiling = the Hecke zero network

The Hecke triangle group `Γ₄ = ⟨J, T⟩` (`q=4`, `λ₄=√2`): `J: z→−1/z` (order 2), `T: z→z+√2` (parabolic), `J²=(JT)⁴=1`. Elliptic points `ε₂=i` (order 2) and `ε₄=(−1+i)/√2` (order 4). The Hauptmodul `β` normalized by `β(ε₂)=0, β(ε₄)=1, β(cusp)=∞`. **paper-3 `thm:q4-hecke-zero-network` (PROVED)**:

- the zero network `Z(a₄) = β⁻¹([0,1])` is the `{∞,4}` Hecke graph;
- `ε₄` is a four-valent singular zero (cone angle `4π`), `ε₂` a bivalent regular zero;
- `a₄=(μ/λ)sinh(λs)`, `g₄=|dW/W|²`, `F²=β/(1−β)`, `W=(F−i)/(F+i)`, `s=log|W|`.

## 3. Dual grids {∞,4} vs {4,∞}

- **`{∞,4}` (primal)** = the `Γ₄`-orbit of the `ε₂–ε₄` arc (the zero network);
- **`{4,∞}` (dual)** = the `Γ₄`-orbit of the line `a=0` (the imaginary axis, the E₀ zero line), crossing `{∞,4}` **perpendicularly at `ε₂`**.

Hence `a=0` (E₀'s trivial zero line) is a `{4,∞}` dual edge; add/multiply branching `1→2→4→8→20→…` spreads it into the whole dual grid. **Status**: the branching and perpendicular crossing are exact computations; "`{4,∞}` = orbit of `a=0`" is a `STRUCTURAL PROPOSAL`.

## 4. The flat metric and the assignment (the simple arithmetic reading)

**paper-3 (PROVED)**: `g₄ = |dW/W|² = |dζ|²` is **flat** (`ζ = log W = s + iθ`). Hence

- the zero set `a₄=0` ⟺ `s=0` (a radial level); the dual = `θ=const` (angular levels);
- `a₄=(μ/λ)sinh(λs)` depends on the radial coordinate `s` alone (same form as the E₁ disc `a_D=(μ/λ)sinh(λ·dist)`);
- the two perpendicular families are the radial/angular coordinate families of the flat structure.

This is the geometric ground of "two perpendicular geodesic families advanced by add/multiply": add/multiply are the two coordinate directions of the flat structure.

## 5. Vertex a-values (the Z[√2] structure)

`a = −x/y` (the E₀ assignment) on the Hecke vertices (`COMPUTATIONALLY VERIFIED EXAMPLE`; matrix formula `a(g(i)) = −(ac+bd)`, `g=[[a,b],[c,d]]`):

$$a(\varepsilon_2\text{-orbit}) = \mathbb Z\sqrt2,\qquad a(\varepsilon_4\text{-orbit}) = 2\mathbb Z+1.$$

In particular `a(ε₂)=0, a(ε₄)=1` (the Hauptmodul branch values); `w(ε₄)=|μ|i`; the fundamental units `λ,μ = 1±√2` = "odd integer ± √2".

## 6. Regular vs non-trivial zero sets

- **A regular AES always has a trivial zero set** (`thm:regular-zero-locus`, PROVED): `μ≠0` forces the zero set to be smooth — no branching, no crossings, no multiple lines. `a=(μ/λ)sinh(λs)` is the universal post-rectification local form, so `μ=1, λ=2,3,4,5` all degenerate to a single zero line.
- **Non-trivial zero sets (several lines, 4-valent) require the singular category**: `thm:branched-pullback-zero-germ` (PROVED) — a holomorphic map `Φ` of local degree `m` gives `2m` prongs and cone angle `2πm`.

## 7. The family = Belyi maps / dessins d'enfants

Non-trivial AES zero sets are **dessins of Belyi maps**: for `β: X→P¹` ramified only over `{0,1,∞}`, set `a=Im β`, `g=|dβ|²/(μ²+λ²a²)`; the zero set is `β⁻¹(ℝ)`, the dessin `β⁻¹([0,1])`.

- `β=zⁿ`: zero set = `n` lines through the origin (`2n` prongs); `n=2` (4 prongs, cone `4π`) is the `ε₄` local germ of `{∞,4}`;
- `β=T_n` (Chebyshev): zero set = the nodal set `T_n⁻¹(ℝ)`, roots `u=cos((2k+1)π/2n)` **algebraic**;
- **LMFDB** ([Belyi maps](https://www.lmfdb.org/Belyi/)) holds 1111 Belyi maps (degree ≤9), searchable by ramification triple `[a,b,c]` and base field (including `Q(√2)`) — the arithmetic catalogue of "the family".

**Belyi's theorem + Grothendieck's programme**: Belyi maps ⟺ arithmetic curves; `Gal(Q̄/Q)` acts faithfully on dessins. Non-trivial zero sets (dessins) are the geometric expression of number theory. **Status**: dessin = zero set is a proved mechanism; "countably many rational-parameter geometries ↔ number theory" is the structural picture.

## 8. The threading polynomial

**Aligned definition**: a path `P` is a word in the four operations. Transport of `a`: `+ : a↦a+μ`, `− : a↦a−μ`, `× : a↦a·u`, `÷ : a↦a/u`, with `u=e^λ`. Starting from `a=0`, `P_λ(0) = p(u)` — a (Laurent) polynomial in `u=e^λ`. For `μ=1` and `λ=ln n`, `u=n`.

Examples (`μ=1`): `+x`→`u`; `+x+`→`u+1`; `+xx`→`u²`; `++x`→`2u`; `+x+x`→`u(u+1)`; `+x−x`→`u(u−1)` (giving `2,6,12` pronic numbers at `u=2,3,4`).

**The Chebyshev `T_n` unifies the threading polynomial and the Belyi map**: `T_n(u)` is a polynomial in `u` (threading) and simultaneously a Belyi map (dessin), with roots `cos((2k+1)π/2n)` algebraic (`T_2`'s roots `±√2/2 ∈ Q(√2)`). **"Polynomial roots ↔ geometry"** = the roots mark the special `λ` where the threading vanishes (`a` returns to 0).

## 9. The big picture

$$\lambda = \ln n \ \Longrightarrow\ u = e^{\lambda} = n \in \mathbb Q \ \Longrightarrow\ \text{countably many geometries, threaded by } p(u);$$

the roots of `p(u)` are the `λ` where the threading returns to zero (degenerate/resonant geometries). `λ=ln2,ln3,ln4` lie in `u>1` (non-degenerate); the roots all lie in `u≤1` (`λ≤0`).

## 10. Status summary

| result | status |
|---|---|
| unifying constant `k`, rate `2√2kⁿ` | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| `g₄=|dζ|²` flat, `a₄` radial, `thm:q4-hecke-zero-network` | `PROVED` (paper-3) |
| branched pullback, `thm:regular-zero-locus` | `PROVED` (paper-3/paper-1) |
| vertex a-values `Z√2 ∪ (2Z+1)`, `w(ε₄)=|μ|i`, dual perpendicularity, figures | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| `{4,∞}` = orbit of `a=0`, `A₀=Z(a)`, the single `k` through all | `STRUCTURAL PROPOSAL` |
| history-to-divisor functor, canonical origin, non-tautological decoration | `OPEN` (OQ-073/074/076) |

## Appendix: script/figure index (011–027)

`011` wormhole-acceleration witness · `012` Pell four-panel · `013` Poincaré disk + Ford wormhole · `014` master figure · `015/016` E₀ assignment distribution (+skeleton) · `017` Hecke zero network vs IFS · `018` vertex a-values + level sets · `019` 0-line branching · `020` dual grids + assignment · `021` flat Hecke grid · `022` a₄ distribution (Schwarz map) · `023` λ-family + threading · `024` zⁿ Belyi zero sets · `025` threading polynomial + grid · `026` big-picture threading · `027` Chebyshev dessins.
