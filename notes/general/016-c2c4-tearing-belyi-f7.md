# 016 — The C₂*C₄ normal form, F₂⋊C₄ tearing, the even-order Belyi criterion, and the {7,4} compactification

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (016: four construction interfaces of the order-4 apeirogonal tiling {∞,4} — the precise tree normal form, the tearing commutator, the even-order sign criterion, and the finite modular compactification).
> **Prerequisites**: Note XIV, *The Pell master figure* ([014](014-pell-master-figure.md)); Note XV, *The Pell–Hecke–Belyi thread* ([015-pell-hecke-belyi-thread.md](015-pell-hecke-belyi-thread.md)); [paper-0/sections/08-acs-tearing.tex](../../paper-0/sections/08-acs-tearing.tex); [paper-0/sections/04-ripple-geometry.tex](../../paper-0/sections/04-ripple-geometry.tex).
> **Date**: 2026-11-15
> **Remark**: this note answers the reviewer's four construction problems about `013`; the §1 `C₂*C₄` constructor is [028-c2c4-tree.py](028-c2c4-tree.py) (fixing `013`'s non-free IFS). All claims are numerically verified.

---

## 1. Discrete generators: the C₂*C₄ normal form (fixing 013's non-free IFS)

### 1.1 The hidden torsion of 013

The four maps of `013` satisfy (in PSL(2,ℝ)):

$$F_3 = F_2^{-1},\qquad F_4 = F_1^{-1}\qquad(\text{since } F_3F_2 = (6-4\sqrt2)\,I,\ F_4F_1 = (6-4\sqrt2)\,I).$$

Hence `013`'s "4-ary tree" was actually a 2-generator Cayley graph with word collisions and re-drawing. **Status**: `PROVED` (direct matrix computation).

### 1.2 The precise tree normal form

Take

$$\Gamma_4 = \langle J, U \mid J^2 = U^4 = 1 \rangle \cong C_2 * C_4,\qquad U = JT\ (\text{fixes }\varepsilon_4),\ J\ (\text{fixes }\varepsilon_2=i).$$

The 1-skeleton of `{∞,4}` inside `H²` is, as an abstract graph, **isomorphic to the 4-regular Bass–Serre tree `T₄`**: root edge `e₀=[ε₄, J(ε₄)]`, and the four neighbours of `g(ε₄)` are `g U^r J(ε₄)` (`r=0,1,2,3`). Expanding by the reduced words `U^{r₀} J U^{r₁} J ⋯ J U^{r_d}` (`r₀∈{0,1,2,3}`, `r_i∈{1,2,3}`) generates `1 + 2(3^d − 1)` vertices **collision-free** (`028` gives 161 at `d=4`, exact). **Status**: `PROVED` (free product + Bass–Serre; the count is verified).

### 1.3 Distinguishing the two kinds of ideal boundary points

- **face centres (parabolic cusps)**: `Γ₄·∞ = Q√2 ∪ {∞}` (e.g. `±(√2−1)`), the tangency points of the ripple pencils `R(F)`;
- **straight-axis endpoints (hyperbolic fixed points)**: `Γ₄·{±1} ∉ Q√2`. The `r_i≡2` word `(U²J)^d` gives the Pell axis; `028` shows its endpoints converge to `−1` (a hyperbolic fixed point), **not** to a cusp. **Status**: `COMPUTATIONALLY VERIFIED EXAMPLE`.

## 2. Tearing: F₂⋊C₄ and the commutator [α̃, β̃_⊥] = T⁴

Define `φ: Γ₄ → Z/4Z` by `φ(U)=1, φ(J)=2`. By Kurosh, `ker φ` is torsion-free, of index 4, isomorphic to the free group `F₂` of rank 2; and `ker φ ∩ ⟨U⟩ = {1}`, `φ(⟨U⟩) = Z/4Z`, so `ker φ` acts **freely and transitively** on the `ε₄` vertex set.

Take the hyperbolic generators (translation length `2 ln λ` each):

$$\tilde\alpha = J U^2,\qquad \tilde\beta_\perp = U^3 J U^3.$$

**Commutator** (verified in `028`, in PSL):

$$[\tilde\alpha, \tilde\beta_\perp] = (JU)^4 = T^4 = \begin{pmatrix}1 & 4\sqrt2\\ 0 & 1\end{pmatrix}.$$

In the commutative quotient (the ACS Euclidean square grid `{4,4}`) `[\bar\alpha,\bar\beta_\perp]=1` (four steps close a square); in the non-commutative lift the four steps trace `ε₄ → Tε₄ → T²ε₄ → T³ε₄ → T⁴ε₄` along `y=1/√2` (with `Tε₄ = J(ε₄)`). Repeating `[α̃,β̃_⊥]^∞` tears the closed `{4,4}` square open into a cusp-width-4 apeirogon. **Status**: the commutator identity `PROVED` (matrix computation); the "tearing" geometric reading `STRUCTURAL PROPOSAL`.

**The key tension**: the affine actions `A_p(x)=x+p, M_q(x)=e^q x` lie in the solvable Borel `B_∞` (`[[M,A],A]=id`, activating only the cusp `∞`), which is why `015 §8`'s threading polynomial `P_λ(0)` collapses the exponentially-growing `F₂` vertices many-to-one onto `Z[√2]`. To spread `{∞,4}` open inside the arithmetic language one must introduce projective gates leaving `B_∞` (e.g. `z↦±1/z`). **Status**: `STRUCTURAL PROPOSAL`.

## 3. The even-order Belyi criterion (the q=4 sign protection)

Under `F² = β/(1−β)`, `W=(F−i)/(F+i)`, `g₄ = |d log W|² = ds² + dθ²`:

1. **each apeirogon face is isometric to a flat Euclidean half-plane under `g₄`**: at `ε₄`, `1−β` has a 4th-order zero, so `W−1 ∼ c(w−ε₄)²` and the cone angle is `4π`; exactly 4 apeirogons meet at `ε₄`, so each face gets interior angle `4π/4 = π` (a straight angle). Along an edge, crossing `ε₂` rotates `θ=arg W` by `2π`; infinitely many edges around a cusp universally cover the punctured disk `{|W|<1}` into the unbounded half-plane `{s<0, θ∈ℝ}`. **Status**: `PROVED` (paper-3 branched pullback + flat metric).

2. **even ramification order = global single-valued sign**: a tessellation of `H²` is 2-colourable iff every interior vertex valence is even. `q=4` has even ramification at `ε₂`(2) and `ε₄`(4), so `F=√(β/(1−β))` is globally single-valued on `H²`; `q=3` (the modular group `{∞,3}`) has `1−β ∼ (w−ε₃)³`, whose square root retains a half-integral branch point, so no global sign. **This is the primary criterion for OQ-073/074/076 filtering admissible Belyi maps: the local multiplicities of `β⁻¹(0)` and `β⁻¹(1)` are all even.** **Status**: `PROVED` (standard square-root single-valuedness: the divisor of `F²` must be even).

## 4. The finite modular compactification: Γ₄ ↠ PSL₂(F₇) and the {7,4} surface

`7` splits in `Z[√2]` (`3²≡2 mod 7`). Projecting by `√2 ↦ 3 mod 7`:

$$J \mapsto \begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad T_+ = \begin{pmatrix}1&3\\0&1\end{pmatrix}\ (7),\quad U_+ = JT_+ = \begin{pmatrix}0&-1\\1&3\end{pmatrix}\ (4),$$

surjects onto `PSL₂(F₇)` (`028` verified `|⟨J,T₊⟩| = 168`). The torsion-free normal core `ker π₊` has cusp width 7 (`T⁷ ∈ ker`), rolling each order-4 apeirogon into a **right-angled heptagon**, compactifying to a genus-10 modular surface `X̄(3−√2)`:

$$F = 168/7 = 24,\quad E = 168/2 = 84,\quad V = 168/4 = 42,\quad g = 1 + 84\cdot\tfrac{3}{28} = 10,$$

with `336` `(2,4,7)` fundamental triangles, Gauss–Bonnet `336 × 3π/28 = 36π = 4π(10−1)`. This places `015`'s Hecke geometry and Paper IV / PR #39's `F₇` count in one commutative diagram. **Status**: `PROVED` (congruence projection + orbit–stabilizer + Riemann–Hurwitz; count verified).

---

## Status summary

| result | status |
|---|---|
| `F₃=F₂⁻¹, F₄=F₁⁻¹`; `C₂*C₄` normal form; `T₄` tree count | `PROVED` |
| commutator `[α̃,β̃_⊥]=T⁴` | `PROVED` |
| tearing reading; Borel collapse vs hyperbolic spread | `STRUCTURAL PROPOSAL` |
| single face = flat half-plane; even-order criterion | `PROVED` |
| `Γ₄↠PSL₂(F₇)`; `{7,4}` count | `PROVED` |

## Appendix: 028 output (collision-free tree + commutator)

`d=4`: 161 vertices, 160 edges; `[α̃,β̃_⊥] = −T⁴ = T⁴` (PSL); Pell axis `(U²J)^d ε₄` converges to `−1`; commutator path `ε₄ → (1+i)/√2 → … → ε₄+4√2`.
