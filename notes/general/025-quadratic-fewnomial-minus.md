# 025 — Quadratic fewnomials on the unit circle: the node is at $c-a$

> **Document type**: AEG research note (025: the general rule behind [021](021-fire-front-twist-flat-torus.md)/[024](024-cusp-birth-fewnomial-firefront.md), applied to the new example $P_\epsilon(V)=V^2-\epsilon V-1$)
> **Date**: 2026-11-20
> **Note**: companion script `052-quadratic-fewnomial-minus.py`; statuses below.

---

## 1. The general rule for $f(V)=aV^2+bV+c$ on $|V|=1$

A self-intersection $f(V)=f(W)$ with $V\neq W$ factors:

$$f(V)-f(W)=(V-W)\bigl(a(V+W)+b\bigr),$$

so the crossing is the **chord-sum** condition $V+W=-b/a$, solvable iff $|b/a|\le2$ (birth as a cusp at $|b/a|=2$, where $V=W$). At the crossing $V+\overline V=-b/a$, hence

$$f(V)=aV^2-a(V+\overline V)V+c=-a|V|^2+c=c-a.$$

So (`PROVED`, three lines):

1. **node position** $=c-a$, **independent of $b$**;
2. **birth** at $|b/a|=2$ (the only place $b$ enters);
3. **root product** $=c/a$ (roots of $f(V)=0$).

The three coefficients have three separate roles: $b/a$ = birth threshold, $c/a$ = zero structure, $c-a$ = value at the node.

## 2. The new example $P_\epsilon(V)=V^2-\epsilon V-1$

Here $a=1$, $b=-\epsilon$, $c=-1$, so the node is at $c-a=-2$ for all $\epsilon$, born at $|\epsilon|=2$, and the roots satisfy $r_+r_-=-1$. Phase portrait (cf. [algebra/01 §3](../algebra/01-finite-layer-exponential-polynomials.md)):

| $\epsilon$ | image of $|V|=1$ under $P_\epsilon$ |
|---|---|
| $0$ | $e^{2it}-1$: circle centre $-1$ radius $1$, traversed twice |
| $0<\epsilon<2$ | one transverse node at $-2$ |
| $\epsilon=2$ | cusp at $-2$ |
| $\epsilon>2$ | smooth simple closed curve |

Concretely, $P_\epsilon(e^{it})=e^{it}(2i\sin t-\epsilon)$; the node preimages are $V=e^{\pm it}$ with $2\cos t=\epsilon$. Roots: $r_\pm=\frac{\epsilon\pm\sqrt{\epsilon^2+4}}{2}$, real, $r_+r_-=-1$ (anti-reciprocal); at $\epsilon=1$ they are the golden ratio $\varphi$ and $-1/\varphi$; at $\epsilon=2$, $1\pm\sqrt2$.

## 3. Contrast with the $+1$ family, and the identity

| | $Q_\epsilon=V^2+\epsilon V+1$ ([024](024-cusp-birth-fewnomial-firefront.md)) | $P_\epsilon=V^2-\epsilon V-1$ (here) |
|---|---|---|
| chord-sum condition | $V+W=-\epsilon$ | $V+W=+\epsilon$ |
| node | $0=c-a$ | $-2=c-a$ |
| roots $r_+r_-$ | $+1$ (conjugate, on unit circle for $\epsilon<2$) | $-1$ (anti-reciprocal, always real) |
| node vs zero locus | node is a zero (at $0$) | node is not a zero (at $-2$) |

The two families are linked by the exact identity

$$P_\epsilon(V)+2=V^2-\epsilon V+1=Q_{-\epsilon}(V).$$

So the node of $P_\epsilon$ is the image, shifted by $-2$, of the zero locus of $Q_{-\epsilon}$: the self-intersection locus of one family is the (shifted) zero locus of the sign-flipped family.

## 4. Back to the fire front

Both families share the birth mechanism of [024](024-cusp-birth-fewnomial-firefront.md): the chord-sum $V+W=-b/a$ reaches the diameter at $|b/a|=2$, dually to the fire-front chord-difference $u-v=v/t$ reaching the diameter at $t=|v|/2$ (parallelogram law $|u-v|^2+|u+v|^2=4$). The new content here is **value-level**: the node position $c-a$ and the root product $c/a$ are fixed under the one-parameter family, while only the birth threshold $b/a$ varies — a clean separation of "where the curve crosses itself / hits zero" (value) from "when the crossing is born" (history/scale), in the sense of AEG's value/history distinction (`STRUCTURAL PROPOSAL`).

## 5. Status

| Result | Status |
|---|---|
| $f(V)-f(W)=(V-W)(a(V+W)+b)$; node at $c-a$; birth at $\|b/a\|=2$; roots product $c/a$ | `PROVED` |
| $P_\epsilon$ phase portrait; node at $-2$; roots product $-1$ | `PROVED` |
| $P_\epsilon+2=Q_{-\epsilon}$ | `PROVED` |
| node/root = value-level, birth = history-level | `STRUCTURAL PROPOSAL` |
| figure `052-quadratic-fewnomial-minus.png` | `COMPUTATIONALLY VERIFIED EXAMPLE` |

## Appendix: script index

`052-quadratic-fewnomial-minus.py` prints the general rule and the $P_\epsilon$ table, and emits `052-quadratic-fewnomial-minus.png` ($P_\epsilon(e^{it})$ for $\epsilon=0,1,2,2.5$).
