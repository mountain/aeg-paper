# 020 — Add/multiply lines, graph potential, boundary-value satisfiability, and the cusped 4-gon on the Cayley model

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (020: the Cayley model of the F₂/T₄ tree — "frame correction → node potential → boundary-value satisfiability → graph colouring → E₁-like square → cusped 4-gon").
> **Prerequisites**: Note XVII, *Cayley model and the conformal-hyperbolic unification* ([017-cayley-model-conformal-hyperbolic.md](017-cayley-model-conformal-hyperbolic.md)); Note XVIII, *Assignment, duality, add-multiply, Eikonal on the Cayley model* ([018-cayley-assignment-duality-eikonal.md](018-cayley-assignment-duality-eikonal.md)); Note XIX, *The Schwarz–Christoffel square* ([019_sc_square_eikonal.md](019_sc_square_eikonal.md)); `paper-0/sections/03-aes-and-motion.tex` (`prop:canonical-arithmetic-frame`).
> **Date**: 2026-11-15
> **Remark**: this note consolidates 041–046; the "level lines = add lines" claim of `040` is corrected by `041`.

---

## 1. Correction: add lines = horizontal, multiply lines = vertical (041)

In `paper-0`'s `prop:canonical-arithmetic-frame`, `J` is the **`g`-orthogonal rotation** (not the Euclidean 90°). Substituting

$$X_u=\frac{\mu}{q}E_a-\frac{\lambda a}{q}JE_a,\quad X_v=\frac{\lambda a}{q}E_a+\frac{\mu}{q}JE_a$$

with `q=√(μ²+λ²a²)` gives **`X_u=(−μy,0)` (horizontal), `X_v=(0,−λy)` (vertical)** (sympy-verified).

- **add lines** = horizontal `y=const` (along which `a=−x/y` varies linearly);
- **multiply lines** = vertical `x=const` (along which `a` scales as `1/y`);
- **add ⊥ multiply = 90°** (independent of `a`).

**The `040` error**: I had called the level lines (rays) "add lines". The level line `y=kx` (`k=−1/a`) makes with the add line (horizontal) the angle

$$\angle(\text{level},\text{add})=\arctan(1/|a|),$$

which **varies continuously with `a`** (90° at `a=0`, hugging the multiply line; 0° as `|a|→∞`, hugging the add line). This is the reviewer's "the angle depends on `a`".

## 2. Graph potential: node values (042)

**Setup**: tree nodes (4-valent branch points, `∇a` undefined) are singularities, edges are regular (carry the Eikonal flow), the origin is completed with `a=0`.

Along an edge `da/ds=±√(μ²+λ²a²)`, so `β(v)−β(u)=±λℓ_e` (`β=arcsinh(λa/μ)`). **The tree is acyclic ⟹ no cycle obstruction ⟹ a solution exists**:

$$\boxed{a(\text{node})=\frac{\mu}{\lambda}\sinh\big(\lambda\,d(\text{node})\big)},\quad d=\text{$g$-path-length from the root}.$$

Numerics (`μ=1,λ=2`, `g=(dx²+dy²)/L²`): root edge `g`-length `3ln2≈2.079`, node values `0→≈16→≈1023`; `da/ds=√(μ²+λ²a²)` matches to `1e-15`.

## 3. Boundary-value satisfiability criterion (043)

The strict 1D flow condition (the edge must be a characteristic):

$$\boxed{\ell_e=\frac{\big|\operatorname{arcsinh}(\lambda a_v/\mu)-\operatorname{arcsinh}(\lambda a_u/\mu)\big|}{\lambda}}$$

local = global (acyclic tree). Test (`μ=1,λ=2`):

| edge | `g`-length | required (odd ints) | result |
|---|---|---|---|
| **E₀** `ε₄→Jε₄` (`a:1→−1`) | 1.6227 | 1.4436 | **slack +0.179** (edge not characteristic) |
| **Cayley** (`a:0→1`) | 3ln2=2.0794 | 0.7218 | **+1.358** mismatch |
| **Cayley** (`a:1→3`) | 2.0794 | 0.5241 | **+1.555** mismatch |

**Two readings**: (2D Eikonal, no edge-length constraint) E₀ realizes the odd integers (`a=−x/y`), Cayley does not (its Eikonal solution gives `≈16,1023`); (1D flow) neither is strict — E₀ has slack, Cayley is worse; the only strict solution is `a=(μ/λ)sinh(λd)`.

## 4. Graph-potential colouring (044)

Nodes coloured by `a=(μ/λ)sinh(λd)` (log scale), edges by the flow rate `√(μ²+λ²a²)`; the right panel colours by the `g`-distance `d`. 53 nodes, `a:0→6.5×10⁴`, `d:0→6.24`.

## 5. The E₁-like blue square (045)

Blue lines (dual `{4,∞}` perpendicular bisectors) bound closed squares (root square `[−4,4]²`). With **`a=0` on the blue boundary + Eikonal inside**:

$$a_{\text{centre}}=\frac{\mu}{\lambda}\sinh(\lambda\cdot\text{inradius}),\quad \text{inradius}=\int\frac{dx}{L}.$$

Self-similarity gives **`inradius=ln2` for every square**, hence

$$a_{\text{centre}}=\tfrac12\sinh(2\ln2)=\boxed{\tfrac{15}{16}}\quad(\text{all squares}).$$

**Key distinction**: the source-free fill is constant `15/16`; **the differing number is the centre "source strength" `a(node)`** (`0,16,1023,…`, the potential). So "E₁ + centre puncture source" is right, but the "pole value" is the **source strength**.

**± symmetry**: `sinh` is odd, so `a(d)` and `−a(d)` both solve the flow (`0→−16→−1023` is a valid mirror). **Inversion**: `1/a` is **not** an Eikonal solution — `|∇(1/a)|²=λ²b²+μ²b⁴` (quartic dual); only the value **rotation** `a→e^{iθ}a` is a symmetry.

## 6. The cusped 4-gon (046)

The 4 corners of a blue square = the dual `{4,∞}` vertices = the primal `{∞,4}` face centres = the **parabolic cusps `Q√2 ∪ {∞}`**. Making the 4 corners singular changes three things:

1. **Geometry**: `E₁` (one-puncture disc) → **cusped 4-gon** (4 parabolic vertices; `a=0` on the sides, `a=∞` at the corners — a mixed boundary condition);
2. **Potential**: node graph → **node + cusp bipartite graph** (the cusps carry "cusp potentials" / pole residues);
3. **Value function**: one puncture → **4 cusps + centre source** composite profile (the constant `15/16` is replaced by a cusp-dominated profile).

## 7. Status summary

| result | status | verification |
|---|---|---|
| `X_u=(−μy,0)`, `X_v=(0,−λy)`, add ⊥ multiply | `PROVED` | sympy vs `prop:canonical-arithmetic-frame` |
| level-vs-add angle `arctan(1/|a|)` | `COMPUTATIONALLY VERIFIED` | numeric |
| `a(node)=(μ/λ)sinh(λd)`, acyclic consistency | `PROVED` | analytic + `1e-15` |
| criterion `ℓ_e=|β(Δa)|/λ` | `PROVED` | analytic + numeric |
| odd integers unrealizable in Cayley; 2D-realizable in E₀ with 1D slack | `PROVED` | exact numerics |
| graph colouring (potential / flow) | `COMPUTATIONALLY VERIFIED` | `044` |
| blue square `inradius=ln2`, source-free centre `15/16` | `PROVED` | numeric |
| inversion `1/a` not an Eikonal solution (quartic dual) | `PROVED` (refuted) | numeric |
| "E₁ + centre source strength = potential" | `STRUCTURAL PROPOSAL` | geometry exact, arithmetic open |
| 4 corners = cusps, upgrade to cusped 4-gon | `STRUCTURAL PROPOSAL` (corner=cusp exact) | `016/017` + `046` |

## Appendix: script index

`041` add/multiply correction · `042` node values · `043` satisfiability · `044` potential colouring · `045` E₁ square · `046` cusped 4-gon.
