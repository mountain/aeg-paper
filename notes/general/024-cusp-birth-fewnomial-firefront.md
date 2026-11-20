# 024 — The cusp birth: fewnomial chord sum vs fire-front chord difference

> **Document type**: AEG research note (024: the one-sentence link between the finite-layer exponential polynomial of [notes/algebra/01](../algebra/01-finite-layer-exponential-polynomials.md) §3 and the fire-front twist of [021](021-fire-front-twist-flat-torus.md))
> **Date**: 2026-11-20
> **Note**: companion script `051-fewnomial-firefront-comparison.py`; statuses below.

---

## 1. Two chord conditions

On the unit circle $u=e^{i\theta_1}$, $v=e^{i\theta_2}$.

**(a) Fewnomial.** For $P_\epsilon(V)=V^2+\epsilon V+1$,
$$P_\epsilon(V)-P_\epsilon(W)=(V-W)(V+W+\epsilon),$$
so a self-intersection ($V\neq W$) is exactly the **chord-sum** condition
$$V+W=-\epsilon.$$
It is solvable iff $|\epsilon|\le2$ (as $|V+W|\le2$). Phase portrait: $\epsilon=0$ circle traversed twice; $0<\epsilon<2$ one transverse node at the origin; $\epsilon=2$ a cusp; $\epsilon>2$ a smooth simple closed curve (`PROVED`, [algebra/01 §3](../algebra/01-finite-layer-exponential-polynomials.md)).

**(b) Fire-front (flat torus).** $C_t(\theta)=(t\cos\theta,\,t\sin\theta)\bmod 1$. A crossing labelled by $v\in\mathbb Z^2\setminus\{0\}$ satisfies $t(u-v)=v$, the **chord-difference** condition
$$u-v=\frac{v}{t},$$
solvable iff $t\ge|v|/2$ (as $|u-v|\le2$). At $t=|v|/2$ the two branches are tangent (birth); for $t>|v|/2$ transverse (`PROVED`, [021](021-fire-front-twist-flat-torus.md)).

## 2. Complementarity: the parallelogram law

For unit-circle points,
$$|u-v|^2+|u+v|^2=2(|u|^2+|v|^2)=4.$$
Hence the two birth conditions are **complementary diameters**:

- fire-front birth at $t=|v|/2$ ⟺ $|u-v|=2$ ⟺ $u=-v$ (**antipodal**);
- fewnomial birth at $|\epsilon|=2$ ⟺ $|u+v|=2$ ⟺ $u=v$ (**coincident**).

Both are the same $A_2$ (cusp) perestroika, read once through the chord *difference* and once through the chord *sum*. This is the analytic form of the "untwist = local reconnection" observation in [021 §5](021-fire-front-twist-flat-torus.md).

## 3. The dictionary

| | fewnomial $P_\epsilon$ | fire-front $C_t$ |
|---|---|---|
| parametrising circle | $|V|=1$ | $S^1$ in $T_p\,\mathbb T^2$ |
| spectrum (frequencies) | finite exponent set $\{0,1,2\}$ | lattice $\mathbb Z^2$ (length spectrum) |
| two-point condition | chord **sum** $V+W=-\epsilon$ | chord **difference** $u-v=v/t$ |
| scale parameter | coefficient ratio $\epsilon$ | radius $t$ |
| birth | $\|\epsilon\|=2$ (coincident) | $t=\|v\|/2$ (antipodal) |
| count | 1 node (finite) | $N(t)=r_2(2t)-1$ (infinite) |

So the fewnomial is the **finite-spectrum truncation** of the fire-front: replace the exponent set $\{0,1,2\}$ by the full lattice $\mathbb Z^2$ and one passes from a single node governed by one coefficient to the Gauss-circle count governed by the length spectrum. Both inverse problems ("does the self-intersection pattern determine the spectral data?") are then the same question at finite vs infinite frequency (`STRUCTURAL PROPOSAL`; cf. the marked/unmarked discussion in [023](023-gauss-word-alignment.md)).

## 4. Status

| Result | Status |
|---|---|
| fewnomial self-intersection ⟺ $V+W=-\epsilon$; phase portrait | `PROVED` |
| fire-front crossing ⟺ $t(u-v)=v$; birth at $t=\|v\|/2$ | `PROVED` |
| parallelogram law $|u-v|^2+|u+v|^2=4$; antipodal/coincident duality | `PROVED` |
| fewnomial = finite-spectrum truncation of the fire-front | `STRUCTURAL PROPOSAL` |
| figure `051-fewnomial-firefront-comparison.png` | `COMPUTATIONALLY VERIFIED EXAMPLE` |

## Appendix: script index

`051-fewnomial-firefront-comparison.py` emits `051-fewnomial-firefront-comparison.png`: top row $P_\epsilon(e^{it})$ for $\epsilon=2.5,2.0,1.2$; bottom row the folded distance circle $C_t$ for $t=0.4,0.5,0.6$.
