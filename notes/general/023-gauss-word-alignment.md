# 023 — Gauss-word alignment: the perpendicular-bisector direction on the flat torus vs the hyperbolic thrice-punctured sphere

> **Document type**: AEG research note (023: answers "is the flat Gauss word — the interlacing of lattice-vector angles — the same combinatorial object as the hyperbolic Gauss word — the order of deck translation axes on the limit circle?")
> **Prerequisites**: Note 021 (flat torus), Note 022 (hyperbolic thrice-punctured sphere)
> **Date**: 2026-11-20
> **Note**: companion script `049-gauss-word-alignment.py`; the conclusion contains a **correction of an earlier formulation** (§4).

---

## 1. The unified object: the perpendicular-bisector direction

In both models a crossing labelled by a deck element $g$ lies on the *perpendicular bisector* of $[p, g^{-1}p]$ (a line on the flat torus, a geodesic on the hyperbolic surface). As $t\to\infty$ the crossing escapes along that bisector, so its asymptotic *direction* is the direction of the bisector:

- **Flat torus** $\mathbb T^2=\mathbb R^2/\mathbb Z^2$, $g=$ translation $z\mapsto z+v$: the bisector is the line $\{x\cdot v=-\tfrac12|v|^2\}$, direction $=\arg v^\perp$, depending only on the *direction* of $v$ (not $|v|$) — `PROVED` ($[p,g^{-1}p]\parallel v$).
- **Hyperbolic** $\mathbb H^2/\Gamma(2)$, $g=\gamma$: the bisector is the geodesic $\{d(p,z)=d(\gamma^{-1}p,z)\}$, direction = its two boundary endpoints $(\xi_1,\xi_2)$, depending on the full $\gamma$ and on $p$ — `PROVED`.

**Convergence check (`COMPUTATIONALLY VERIFIED EXAMPLE`)**:

| flat $v$ | $\arg v^\perp$ | $t=1.2$ | $t=3$ | $t=8$ |
|---|---|---|---|---|
| $(1,0)$ | 1.5708 | 0.430 | 0.167 | 0.063 |
| $(1,1)$ | 2.3562 | 0.630 | 0.238 | 0.089 |
| $(2,1)$ | 2.0344 | 1.199 | 0.382 | 0.140 |

| hyperbolic $\gamma$ | bisector endpoints | $t=1$ | $t=2$ | $t=4$ |
|---|---|---|---|---|
| $A$ | $(-1,\ \infty)$ | 0.516 | 0.039 | 0.001 |
| $B$ | $(-1,\ 0)$ | 0.205 | 0.019 | 0.000 |
| $AB$ | $(-0.631,-0.227)$ | — (unborn) | 0.069 | 0.001 |
| $AbA$ | $(-2,\ -1)$ | — (unborn) | 0.154 | 0.002 |

(entries are the minimum distance from the crossing direction to the limiting direction, decreasing monotonically to 0.)

## 2. The flat torus is the degenerate (abelian) case: antipodal pairs

The flat deck group $\mathbb Z^2$ consists of translations, so $[p,g^{-1}p]\parallel v$, the bisector direction is $\arg v^\perp$, independent of the basepoint and of $|v|$; each $v$ gives an **antipodal pair** $\{\arg v^\perp,\ \arg v^\perp+\pi\}$ (the two chords have opposite asymptotic directions). Hence the flat Gauss word (large $t$) = the circular order of these antipodal pairs on $S^1$.

## 3. The hyperbolic case is non-degenerate: general pairs (`COMPUTATIONALLY VERIFIED EXAMPLE`)

The hyperbolic bisector endpoints $(\xi_1,\xi_2)$ are generally **not antipodal** and depend on the **full** $\gamma$: $AB$ and $ABAB=(AB)^2$ share the same fixed points $(2.414,-0.414)$ but have different bisector endpoints ($AB$: $(-0.631,-0.227)$; $ABAB$: $(-0.449,-0.380)$).

**Parabolic vs loxodromic observation**: for a parabolic $\gamma$ (fixing cusp $c$) one bisector endpoint is **the cusp $c$ itself**, the other a second point $c'$:

| $\gamma$ | fixed cusp $c$ | bisector endpoints |
|---|---|---|
| $A$ | $\infty$ | $(-1,\ \infty)$ |
| $B$ | $0$ | $(-1,\ 0)$ |
| $AA$ | $\infty$ | $(-2,\ \infty)$ |
| $BB$ | $0$ | $(-0.5,\ 0)$ |
| $Ab$ | $1$ | $(\tfrac13,\ 1)$ |

For a loxodromic $\gamma$, the bisector endpoints are **not** its fixed points (e.g. $AB$: fixed $2.414,-0.414$; bisector $-0.631,-0.227$).

## 4. Correction of the earlier formulation (key)

I earlier phrased the question as "lattice-vector angle order ⟷ order of deck translation axes on the limit circle". The computation shows this is **wrong**:

- the flat "lattice-vector angle" lives on the **tangent circle** $S^1=T_p\widetilde M$ (translations of $\mathbb R^2$ act trivially on its boundary at infinity — there is no limit set);
- the hyperbolic "limit circle" is $\partial\mathbb H^2$ (where $\Gamma(2)$ acts nontrivially by Möbius maps);
- and the hyperbolic Gauss word orders **perpendicular-bisector endpoints**, not translation-axis endpoints (the $AB$ counterexample of §3).

**Conclusion**: the two Gauss words are the same *kind* of combinatorial object — the circular order of perpendicular-bisector directions on a direction circle $S^1$ — but "lattice-vector angle" and "translation axis" are **not** the aligned quantities; the aligned quantity is the **perpendicular-bisector direction**. The flat torus degenerates (abelian) to $\arg v^\perp$ (antipodal pairs); the hyperbolic surface keeps the full $(\xi_1,\xi_2)$ (general pairs). That the tangent circle and the limit circle are two avatars of "the direction circle" is a `STRUCTURAL PROPOSAL`, not a literal identity.

## 5. Status summary

| Result | Status |
|---|---|
| Crossing lies on the perpendicular bisector of $[p,g^{-1}p]$; direction tends to the bisector direction | `PROVED` |
| Flat: bisector $\perp v$, direction $\arg v^\perp$, direction-only, antipodal pairs | `PROVED` |
| Hyperbolic: bisector endpoints $(\xi_1,\xi_2)$, generally non-antipodal, depend on full $\gamma$ | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| Parabolic $\gamma$: one bisector endpoint = cusp $c$ | `COMPUTATIONALLY VERIFIED EXAMPLE` (upgradable to a lemma) |
| Loxodromic $\gamma$: bisector endpoints $\neq$ fixed points ($AB$ counterexample) | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| Tangent circle $S^1$ and limit circle $S^1$ are two avatars of "the direction circle" | `STRUCTURAL PROPOSAL` |

## Appendix: script index

`049-gauss-word-alignment.py` prints the two convergence tables (§1) and the parabolic/loxodromic table (§3), and emits `049-gauss-word-alignment.png` (left = flat direction circle with the antipodal pairs $\arg v^\perp$; right = limit circle with the hyperbolic bisector endpoints).
