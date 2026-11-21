# 054 — Eisenstein base points: bringing √3 into the {∞,4} assignment with Γ₄ discrete

> **Document nature**: research note (AEG). Subject: in the Cayley/{∞,4} model and
> the `a=−x/y` assignment layer, **keep Γ₄ = H(√2) discrete and change the base
> point rather than the ratios**, and use the Eisenstein integers `ℤ[ω]` as the
> base-point lattice to bring √3 in. This note changes no paper source and no
> mathematical-status register.
>
> **Prerequisites**: [015 — Pell/{∞,4}/Hecke/Belyi](015-pell-hecke-belyi-thread.md)
> (§2, §5), [016 — C₂*C₄ normal form](016-c2c4-tearing-belyi-f7.md),
> [017 — Cayley model](017-cayley-model-conformal-hyperbolic.md),
> [018 — assignment/duality/Eikonal](018-cayley-assignment-duality-eikonal.md)
> (§2), [020 — add/multiply lines, potential, HTWR restart](020-cayley-add-multiply-potential-boundary.md)
> (§8), `paper-0/sections/03-aes-and-motion.tex` (`a=−x/y`, `X_s`, `Y_k`).
>
> **Date**: 2026-11-21.
>
> **Status**: (F), (E1), (E2), (O1), (O2) are `PROVED` (direct computation; the
> exact script [055](055-eisenstein-base-points-check.py) passes all checks); the
> three-orbit generation of `ℤ[√2,√3]` is `PROVED` (on top of the value sets of
> 015 §5); whether the orbit fills `√3·ℚ(√2)` is an `OPEN PROBLEM`; the geometric
> readings are `STRUCTURAL PROPOSAL`.

---

## 0. Problem and decision

The original problem needs √3 in the assignment layer. The two previous routes
are both unsatisfactory:

1. **Represent ℚ(√3) inside ℚ(√2)**: impossible, `ℚ(√3) ⊄ ℚ(√2)`
   (`ℚ(√2)∩ℚ(√3)=ℚ`).
2. **Change the coefficient ratios of the assignment formula**: changing ratios
   inside `ℚ(√2)` is ineffective (the value stays in `ℚ(√2)`); raising the
   coefficient field to `ℚ(√2,√3)` can produce `a=√3`, but the translation
   subgroup of `PSL₂(ℚ(√2,√3))` is dense in ℝ, which destroys the discrete
   structure of Γ₄/{∞,4}.

This note takes the third route: **keep Γ₄ discrete and change the base point**.
The base point is taken from the Eisenstein-integer lattice `ℤ[ω] ⊂ ℂ`
(`ω=(−1+i√3)/2`). Γ₄ and the {∞,4} tiling are preserved as they are, while √3
enters the assignment layer through the height of the base point.

## 1. General assignment formula

Continue with the upper half-plane `ℍ²`, `a=−x/y`, and the Hecke group

$$
\Gamma_4=\langle J,T\rangle,\qquad J:z\mapsto-\tfrac1z,\qquad T:z\mapsto z+\sqrt2,
$$

with elliptic points `ε₂=i` and `ε₄=(−1+i)/√2`. For a general base point
`z₀=x₀+iy₀` and `g=[[A,B],[C,D]]`, write `Δ=AD−BC≠0`. From
`z=(Az₀+B)/(Cz₀+D)`, multiplying by the conjugate and taking `−Re/Im` gives

$$
\boxed{\;a(gz_0)=-\frac{AC(x_0^2+y_0^2)+BD+(AD+BC)\,x_0}{y_0\,(AD-BC)}\;}
\qquad\text{(F)}
$$

**`PROVED`** (direct computation; script 055 symbolically checks several `z₀`
and `g`).

Two special cases:

- `z₀=ε₄` (`x₀=−1/√2`, `y₀=1/√2`, `x₀²+y₀²=1`):

$$
a(g\varepsilon_4)=\frac{(AD+BC)-\sqrt2\,(AC+BD)}{AD-BC}.
$$

  018/029 used the `det=1` version; the formula above extends it to `Δ≠0`.
- `z₀=ω−1` (see §3): `a(g(ω−1))` is (O1).

Note that (F) is homogeneous of degree 0 in `(A,B,C,D)`: **the assignment
depends only on the ratios `[A:B:C:D]`**, which is the precise object of the
phrase "changing the ratios".

## 2. Why the ratio route does not suffice (recap)

Let `A,B,C,D ∈ K` (coefficient field). By (F), numerator and denominator both
lie in `K(√2)`, hence `a ∈ K(√2)` (`PROVED`). Thus `a=√3` requires at least
`√3 ∈ K(√2)`. Proceeding step by step (the last row is for contrast):

| K | `a=√3` possible? | Reason |
|---|---|---|
| ℚ(√2) | no | `a∈ℚ(√2)` |
| ℚ(√3) | no | `(*)` forces `B²=(1−√3)A²` (C≠0), or `A/B=−(√2+√6)/2` (C=0); no real solution |
| ℚ(√6) | no | `(*)` forces `A²−B²=√6·AB`, i.e. `t²−√6t−1=0`, `t=(√6±√10)/2∉ℚ(√6)` |
| ℚ(√2,√3) | yes | the translation `b=(√2−√6)/2=(1−√3)/√2` gives `a=1−√2b=√3` |

Here `(*)` is the equivalent form of `a=√3`:

$$
AD(1-\sqrt3)+BC(1+\sqrt3)=\sqrt2\,(AC+BD). \qquad\text{(*)}
$$

The derivation is: for `C≠0`, `(*)` solves for `D=C·P/Q` with
`P=√2A−(1+√3)B` and `Q=(1−√3)A−√2B`; taking the fixed-field condition of `K`
inside `ℚ(√2,√3)` (`σ₂` for `ℚ(√3)`, `σ₂σ₃` for `ℚ(√6)`) gives the two
formulas in the table.

For a general quadratic field `K=ℚ(√d)`: if `d=2`, `K(√2)=ℚ(√2)` does not
contain √3; if `d≠2`, `K(√2)=ℚ(√2,√d)` is biquadratic and contains `ℚ(√3)` iff
`d≡3` or `6` (mod squares), so only the rows `ℚ(√3)`, `ℚ(√6)` remain, and they
are already excluded. Hence **no quadratic coefficient field can give `a=√3`**
(`PROVED`, elementary).

These exclusions are elementary computations (`PROVED`); they show that
**introducing √3 in the coefficient field costs discreteness: the translation
subgroup `ℤ+ℤ√2+ℤ√3` of `ℚ(√2,√3)` is dense in ℝ, so `PSL₂(ℚ(√2,√3))` is no
longer discrete**. To preserve Γ₄/{∞,4}, √3 must not enter the
coefficients/generators; it can only enter the base point.

## 3. The Eisenstein lattice and the ℚ√3 line

Take

$$
\omega=\frac{-1+i\sqrt3}{2},\qquad \omega^2+\omega+1=0,
$$

`ℤ[ω]` is the ring of integers of `ℚ(√−3)`, with norm form
`N(m+nω)=m²−mn+n²` and unit group `μ₆`. For `w=m+nω` (`n≠0`), the coordinates
are

$$
x=m-\tfrac n2,\qquad y=n\tfrac{\sqrt3}{2},
$$

hence

$$
a(w)=-\frac{x}{y}=\frac{n-2m}{n\sqrt3}
=\sqrt3\cdot\frac{n-2m}{3n}\in\mathbb Q\sqrt3 .
\qquad\text{(E1)}
$$

**`PROVED`** (direct computation; 055 symbolically checked). In particular:

| Eisenstein integer | `a` value | Meaning |
|---|---|---|
| `ω−1` | `√3` | positive √3 level |
| `2+ω` | `−√3` | negative √3 level |
| `2ω+1 = i√3` | `0` | height √3 on the zero line `{a=0}` |

**`PROVED`** (055). That is, the assignment of the whole Eisenstein lattice lies
on the **ℚ-line `ℚ√3`**; this is completely symmetric to the `ε₂`-orbit giving
`ℤ√2 ⊂ ℚ√2` (015 §5).

`2ω+1=i√3` is the most telling row: in `ℤ[ω]`, √3 is a **height**, and the
assignment `a=−x/y` is precisely the operation that turns height into value.

## 4. Keeping Γ₄ discrete: the orbit of the base point `ω−1`

Take the base point `w₀=ω−1` (`a=√3`); **Γ₄ is unchanged**. For
`g=[[A,B],[C,D]] ∈ SL₂(ℚ(√2))`, (F) with `x₀=−3/2`, `y₀=√3/2`,
`x₀²+y₀²=3` gives

$$
a\bigl(g(\omega-1)\bigr)
=\sqrt3\cdot
\frac{3(AD+BC)-6AC-2BD}{3(AD-BC)}
=\sqrt3\,R(g),\qquad R(g)\in\mathbb Q(\sqrt2).
\qquad\text{(O1)}
$$

**`PROVED`** (055 checks the identity, `T`, `T²`, `J`, and 40 random Γ₄ words).
Hence

$$
a\bigl(\Gamma_4\cdot(\omega-1)\bigr)\;\subset\;
\sqrt3\,\mathbb Q(\sqrt2)=\mathbb Q\sqrt3+\mathbb Q\sqrt6 .
$$

Some explicit values:

| `g` | `a(g(ω−1))` |
|---|---|
| `id` | `√3` |
| `T` | `√3 − (2/3)√6` |
| `T²` | `√3 − (4/3)√6` |
| `J` | `−√3` |

The translation orbit has the closed form

$$
a\bigl(\omega-1+m\sqrt2\bigr)=\sqrt3-\tfrac{2m}{3}\sqrt6,\qquad m\in\mathbb Z,
\qquad\text{(O2)}
$$

**`PROVED`** (055).

The orbit points have coordinates in `ℚ(√2,√3)`: the coefficients of `g` lie in
`ℚ(√2)`, the coordinates of `ω−1` in `ℚ(√3)`, and after the Möbius action
`Re,Im ∈ ℚ(√2,√3)`. So this is **one orbit of the same discrete Γ₄ over the
compositum**, not an enlarged group.

## 5. Three orbits and the ring they generate

| base point | value set | ℚ-line | evidence |
|---|---|---|---|
| `ε₂=i` | `ℤ√2` | `ℚ√2` | 015 §5 |
| `ε₄=(−1+i)/√2` | `2ℤ+1` | `ℚ` | 015 §5; 029 |
| `ω−1` | `⊂ √3·ℚ(√2)` | `ℚ√3 + ℚ√6` | this note (O1) |

The value sets contain `1` (odd integers), `√2` (the `ε₂`-orbit, e.g.
`a(Tε₂)=−√2`), and `√3` (`ω−1` itself). Hence the ring generated by these three
value families is

$$
\mathbb Z[\sqrt2,\sqrt3]=\mathbb Z+\mathbb Z\sqrt2+\mathbb Z\sqrt3+\mathbb Z\sqrt6,
$$

whose fraction field is the biquadratic compositum `ℚ(√2,√3)` (the splitting
field of `x⁴−10x²+1`, Galois group `V₄`). **`PROVED`** (on top of the value sets
of 015 §5; 055 checks representatives).

It is worth emphasizing: the orbit of `ω−1` alone gives only the two-dimensional
ℚ-space `√3ℚ(√2)` and **does not** give the whole compositum; to get `1` and
`√2` one must also use the `ε₄`/`ε₂` orbits. Only the three orbits together give
`ℤ[√2,√3]`.

## 6. Why ℤ[ω] can only be a "base-point lattice"

This is what decides why the whole route does not destroy discreteness:

1. `ℚ(√−3)` is an **imaginary** quadratic field, while `ℚ(√2,√3)` is totally
   real. `ℚ(√−3)` has no embedding into ℝ, so `ℤ[ω]` cannot be a subring of the
   value field, and hence cannot enter as "arithmetic of values".
2. `PSL₂(ℤ[ω])` is a Bianchi group acting on `ℍ³`, not in the two-dimensional
   model.
3. The units `μ₆` of `ℤ[ω]` are Euclidean rotations (multiplication by `ω`
   rotates by 120°), which do not preserve `ℍ²`, so they give no Möbius motion
   of `ℍ²`.

Therefore the only legitimate role of `ℤ[ω]` is: **a lattice of base points in
the coordinate plane ℂ**. It provides points, heights, and √3, but no motions;
Γ₄ and {∞,4} are therefore preserved as they are.

## 7. Readings (`STRUCTURAL PROPOSAL`)

- **Two ℚ-lines**: `ℚ√2` (Hecke side: `ℤ√2`, odd integers, cusps) and `ℚ√3`
  (Eisenstein side: the levels `a=±√3`, the zero-line height `2ω+1=i√3`). The
  assignment `a=−x/y` couples the vertical √3 into the values; the union of the
  two lines generates the biquadratic field.
- **Half-step reading**: `a(ω−1)=√3` is precisely the value of the ×3
  multiplicative half-step from `1` (`Y_{√3}` multiplies `a` by √3); `ε₄` sits
  at the ×2 half-step height `1/√2`. `2ω+1=i√3` puts √3 directly at the height
  of the zero line `{a=0}`.
- These are readings, not theorems; they connect the Cayley/Hecke thread of
  017–020 with the Eisenstein base points of this note on one `√2/√3`
  half-step trunk.

## 8. Status

| claim | status | evidence |
|---|---|---|
| (F) general assignment formula | `PROVED` | direct computation; 055 |
| (E1) `a(m+nω)=√3(n−2m)/(3n)`, values in `ℚ√3` | `PROVED` | 055 |
| `a(ω−1)=√3`, `a(2+ω)=−√3`, `a(2ω+1)=0`, `2ω+1=i√3` | `PROVED` | 055 |
| (O1) `a(g(ω−1))=√3R(g)`, `R(g)∈ℚ(√2)` | `PROVED` | 055 (including random words) |
| (O2) `T`-orbit `√3−(2m/3)√6` | `PROVED` | 055 |
| three orbits generate `ℤ[√2,√3]` | `PROVED` (on top of 015 §5) | 015; 055 |
| whether `Γ₄·(ω−1)` fills `√3ℚ(√2)` | `OPEN PROBLEM` | — |
| the "two ℚ-lines / half-step" reading | `STRUCTURAL PROPOSAL` | — |
| history→assignment functor, properness, tube interface | `OPEN PROBLEM` | OQ-072–077 |

## 9. Open questions and next steps

1. **Filling**: is the value set of `Γ₄·(ω−1)` all of `√3ℚ(√2)`, or a proper
   subset? Script 055 can already enumerate words and compute values; the next
   step is to extend it to sampling/visualization and test whether the value set
   is exactly a `ℤ[√2]`-lattice.
2. **Other Eisenstein base points**: `1+ω` (the order-3 elliptic point of the
   modular group, `a=−1/√3`), `2ω+1=i√3` (on the zero line), `k(1+2ω)` (the
   points `ik√3` on the zero line) — what orbits/value sets do they give?
3. **Interface with 015/020**: the core compatibility relation of 020 §8,
   `s_γ(u)∈M_u`, `a_u(s_γ(u))=p_γ(u)`, has no counterpart yet on the base-point
   side; whether the base-point choice gives a well-defined "history→assignment"
   functor remains part of OQ-072–077.
4. **Script/figure**: extend 055 into a version with a figure (Γ₄ orbit points
   plus `a`-value colouring), and align it with the drawing conventions of `030`
   (Cayley reproduction) and `032` (`a` on Cayley).

## Appendix A — key identities and checks

The script [055-eisenstein-base-points-check.py](055-eisenstein-base-points-check.py)
checks the following with exact sympy (all PASS):

```text
(F)   a(g z0) = -[AC(x0²+y0²)+BD+(AD+BC)x0] / (y0 (AD-BC))
(E1)  a(m+nω) = √3 (n-2m)/(3n) ∈ ℚ√3
(E2)  a(ω-1)=√3, a(2+ω)=-√3, a(2ω+1)=0, 2ω+1=i√3
(O1)  a(g(ω-1)) = √3 [3(AD+BC)-6AC-2BD]/(3(AD-BC)),  R ∈ ℚ(√2)
(O2)  a(ω-1+m√2) = √3 - (2m/3)√6
(R1)  Q(√2)-ratios ⇒ a ∈ Q(√2); b=(√2-√6)/2 gives a=√3, but deg_Q(b)=4
(R2)  a(ε₂)=0, a(Tε₂)=-√2, a(ε₄)=1, a(Tε₄)=-1
```
