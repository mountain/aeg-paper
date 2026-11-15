# 019 — The Schwarz–Christoffel "Heaven-Round Earth-Square" Conformal Hyperbolic Model on $\mathcal{Q}_e = [-e, e]^2$, `{∞,4}` Embedding, and Smooth Orthogonal Eikonal Fills

**Date**: 2026-11-15  
**Related notes & scripts**: [016-c2c4-tearing-belyi-f7.en.md](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/016-c2c4-tearing-belyi-f7.en.md), [017-cayley-model-conformal-hyperbolic.en.md](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.en.md), [018-cayley-assignment-duality-eikonal.en.md](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/018-cayley-assignment-duality-eikonal.en.md) · Companion script: `039-sc-square-eikonal.py`

## 1. Motivation: From the Fractal Cayley Union $D_\infty$ to the Canonical Square $\mathcal{Q}_e = [-e, e]^2$

In [Note 017](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.en.md) and [Note 018](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/018-cayley-assignment-duality-eikonal.en.md), the $F_2$ 4-regular tree $T_4$ is embedded in $\mathbb{R}^2$ as a recursive union $D_\infty$ of $L^1$-diamonds equipped with the piecewise-linear Manhattan depth metric $g = (dx^2+dy^2)/L^2$ ($K = -2$ on smooth facets). Rotating [035-gradient-cayley.py](https://github.com/mountain/aeg-paper/blob/main/notes/general/035-gradient-cayley.py) by $45^\circ$ aligns the four primary $T_4$ trunks along the diagonals $Y = \pm X$ so that the entire infinite fractal is tightly inscribed inside a single axis-aligned bounding square, while near the origin the gradient and level lines form orthogonal concentric circles and rays.

Constructing a global Eikonal fill directly via Euclidean circles or the piecewise-$L^1$ formula of [038-eikonal-cayley.py](https://github.com/mountain/aeg-paper/blob/main/notes/general/038-eikonal-cayley.py) faces two structural obstacles:

1. **Axial fractal fjords and medial shock ridges**: The self-similar Euclidean union $D_\infty$ leaves countable re-entrant fjords along the coordinate axes and produces gradient discontinuities along medial ridges; moreover, `030/038` evaluated $L_{\mathrm{bug}} = \min_i \big|\|p-c_i\|_1 - R_i\big|$, which vanishes along internal parent-square seams and leaks into the exterior.
2. **Symmetry mismatch between $SO(2)$ circles and the $D_4$ square boundary**: Pure Euclidean circles $\rho = \text{const}$ cannot align simultaneously with the edge midpoints and corners of a bounding square.

The **Gauss lemniscatic Schwarz–Christoffel conformal map** resolves both tensions canonically: its hyperbolic wavefronts are concentric Euclidean circles up to fourth order near the origin and morph smoothly into squircles hugging $\partial\mathcal{Q}_e = \partial[-e, e]^2$, equipping $(-e, e)^2$ with a **real-analytic, constant-curvature ($K = -1$), shock-free** hyperbolic metric and exact orthogonal Eikonal fills.

## 2. The Lemniscatic Map $\mathcal{S}: \mathbb{D}_w \xrightarrow{\sim} \mathcal{Q}_e$ and Boundary Phase-Locking

Let $\mathcal{Q}_e := [-e, e]^2 \subset \mathbb{C}_Z$ ($Z = X + iY$, $e = \exp(1)$). Define the conformal biholomorphism from the Poincaré disk $\mathbb{D}_w = \{|w| < 1\}$ onto $\mathcal{Q}_e$:
$$Z = \mathcal{S}(w) := \frac{e}{K_+} \int_0^w \frac{d\zeta}{\sqrt{1 + \zeta^4}}, \qquad K_+ := \int_0^1 \frac{dt}{\sqrt{1 + t^4}} = \frac{\Gamma(1/4)^2}{8\sqrt{\pi}} = \frac{\varpi}{2\sqrt{2}} \approx 0.927037338650686,$$
where $\varpi = 2\int_0^1 (1-t^4)^{-1/2}dt \approx 2.62205755429212$ is Gauss's lemniscate constant and the diagonal integral satisfies $\int_0^1 (1-t^4)^{-1/2}dt = \sqrt{2}\,K_+ \approx 1.31102877714606$.

Composing the $\varepsilon_4$-centered Cayley transform from the Hecke upper half-plane $\mathbb{H}^2_\tau$ ($\Gamma_4 = \langle J, T \rangle \cong C_2 * C_4$, $\varepsilon_4 = \frac{-1+i}{\sqrt{2}}$),
$$w(\tau) = \frac{\tau - \varepsilon_4}{\tau - \overline{\varepsilon}_4},$$
with $\mathcal{S}$ establishes exact geometric phase-locking (`PROVED`):

* **Central order-4 vertex**: $\tau = \varepsilon_4 \mapsto w = 0 \mapsto Z = (0, 0)$. Because $\mathcal{S}(w) = \frac{e}{K_+}\big(w - \frac{w^5}{10} + \frac{3 w^9}{72} - \cdots\big)$ has no $w^2, w^3, w^4$ terms, inner wavefronts are isotropic to $O(|w|^5)$.
* **Edge midpoints = the four fundamental parabolic cusps of $\{4,\infty\}$**:
  $$\tau \in \left\{\infty,\ 0,\ -\frac{1}{\sqrt{2}},\ -\sqrt{2}\right\} \longmapsto w \in \{+1,\ -i,\ -1,\ +i\} \longmapsto Z \in \{(+e,0),\ (0,-e),\ (-e,0),\ (0,+e)\}.$$
  The coordinate segments $[-e, e]_X$ and $[-e, e]_Y$ are exact complete hyperbolic geodesics of $g_{\mathrm{SC}}$.
* **Square corners = the four hyperbolic Pell axis endpoints**:
  The first-generation vertex $J(\varepsilon_4) = \frac{1+i}{\sqrt{2}}$ maps to $w = \frac{1-i}{2} = \frac{1}{\sqrt{2}}e^{-i\pi/4}$, launching the four $\{\infty,4\}$ trunks along $\pm 45^\circ, \pm 135^\circ$; the hyperbolic Pell fixed points $\tau = \pm 1$ and $U(\pm 1)$ map to $w = e^{\pm i\pi/4}, e^{\pm 3\pi i/4}$ and land **at the four square corners $(\pm e, \pm e)$**, with the Euclidean diagonals $Y = \pm X$ serving as exact hyperbolic geodesics.

## 3. Conformal Depth $f_{\mathrm{SC}}$ and a Four-Line Wirtinger Proof of $K = -1$

Pushing forward $g_{\mathbb{D}} = \frac{4|dw|^2}{(1-|w|^2)^2}$ via $w'(Z) = \frac{K_+}{e}\sqrt{1+w^4}$ yields the conformal depth form of [Note 017](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.en.md):
$$g_{\mathrm{SC}} = \frac{dX^2 + dY^2}{f_{\mathrm{SC}}(X, Y)^2}, \qquad f_{\mathrm{SC}}(X, Y) := \frac{e}{2 K_+} \frac{1 - |w(Z)|^2}{\big|1 + w(Z)^4\big|^{1/2}}.$$

* **Unit-slope boundary asymptotics**: Along any open side $|X| \to e^-$ ($|Y| < e$) or $|Y| \to e^-$ ($|X| < e$), $e - |X| \simeq |\mathcal{S}'(w)|(1-|w|)$, hence $f_{\mathrm{SC}}(X,Y) \simeq \mathrm{dist}_{\mathrm{Eucl}}\big((X,Y), \partial\mathcal{Q}_e\big)$ with slope $1$.
* **Exact Wirtinger proof of $K \equiv -1$** (`PROVED`): Set $c = \frac{e}{2K_+}$, $A = 1 - |w|^2$, $g(w) = (1+w^4)^{-1/4}$, and $\eta = \frac{g'(w)}{g(w)} = -\frac{w^3}{1+w^4}$, so $f_{\mathrm{SC}} = c A |g|^2$ and $4 c^2 |g|^4 |w'(Z)|^2 \equiv 1$. Since $|\nabla f|^2 = 4|w'|^2 |\partial_w f|^2$ and $\Delta f = 4|w'|^2 \partial_w\partial_{\bar w} f$:
  $$|\nabla f_{\mathrm{SC}}|^2 = |-\bar w + A\eta|^2 = |w|^2 - 2A\operatorname{Re}(w\eta) + A^2|\eta|^2,$$
  $$f_{\mathrm{SC}}\,\Delta f_{\mathrm{SC}} = A\big(-1 - 2\operatorname{Re}(w\eta) + A|\eta|^2\big).$$
  Subtracting cancels every fourth-order branch term $\eta$ identically:
  $$K = f_{\mathrm{SC}}\,\Delta f_{\mathrm{SC}} - |\nabla f_{\mathrm{SC}}|^2 = -A - |w|^2 = -(1 - |w|^2) - |w|^2 \equiv -1.$$
  (Rescaling $\tilde f_{\mathrm{SC}} = \sqrt{2}\,f_{\mathrm{SC}}$ gives $K \equiv -2$, matching the normalization of $D_\infty$.)

This extends Section 4 of [Note 017](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.en.md) to **four canonical $\{\infty,4\}$ realizations**:

| Model | Domain | Conformal depth $f$ | $\Delta f$ | $\|\nabla f\|^2$ | $K = f\Delta f - \|\nabla f\|^2$ | Boundary & singularity profile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Poincaré** $\mathbb{H}^2$ | $\{y > 0\}$ | $y$ | $0$ | $1$ | **$-1$** | Unbounded line $\mathbb{R}\cup\{\infty\}$, smooth |
| **Cayley** $D_\infty$ | Fractal square union | $L_{\mathrm{true}}$ ($L^1$ depth) | $0$ (facet) | $2$ (facet) | **$-2$** (facet) | Axial fjords + countable tree/neck ridges |
| **SC Square** $\mathcal{Q}_e$ | $[-e, e]^2$ | $\frac{e(1-\|w\|^2)}{2K_+\|1+w^4\|^{1/2}}$ | $\neq 0$ (analytic) | Analytic | **$-1$** (global) | Compact square sides, **0 shocks, 0 fjords** |
| **Hecke** $W$-plane | $\mathbb{C}_W^\times$ (branched) | $\|W\| = e^s$ | $1/\|W\|$ | $1$ | **$0$** (flat) | $4\pi$ cone saddles at $\varepsilon_4$, rectified zero locus |

## 4. Two Shock-Free Orthogonal Eikonal Fills on $[-e, e]^2$

With respect to $g_{\mathrm{SC}}$, the intrinsic regular AES Eikonal equation ([Note 018](https://www.google.com/search?q=https://github.com/mountain/aeg-paper/blob/main/notes/general/018-cayley-assignment-duality-eikonal.en.md) §6) reads:
$$|\nabla_{g_{\mathrm{SC}}} a|_{g_{\mathrm{SC}}}^2 = f_{\mathrm{SC}}(X, Y)^2 \left[\left(\frac{\partial a}{\partial X}\right)^2 + \left(\frac{\partial a}{\partial Y}\right)^2\right] = \mu^2 + \lambda^2 a^2.$$

Script `039-sc-square-eikonal.py` constructs and verifies two shock-free orthogonal solutions to machine precision ($< 10^{-14}$):

1. **Radial "Heaven-Round Earth-Square" squircle fill (origin source $\varepsilon_4 \to \partial\mathcal{Q}_e$)**:
   Setting $s_{\mathrm{rad}}(Z) = 2\operatorname{artanh}|w(Z)| = \ln\frac{1+|w(Z)|}{1-|w(Z)|}$ gives
   $$a_{\mathrm{rad}}(X, Y) = \frac{\mu}{\lambda}\sinh\big(\lambda s_{\mathrm{rad}}(X, Y)\big),$$
   whose level curves interpolate smoothly from Euclidean circles around $(0,0)$ to squircles hugging $\partial[-e,e]^2$, orthogonal to the constant-argument streamlines $\arg w(Z) = \text{const}$ (straight along the 8 symmetry rays).
2. **Globally singularity-free cusp-to-cusp fill ($E_0$ pushforward)**:
   Taking the signed hyperbolic distance to the horizontal cusp-to-cusp geodesic $[-e, e]_X$,
   $$s_\perp(Z) = \operatorname{arsinh}\left(\frac{2\operatorname{Im} w(Z)}{1 - |w(Z)|^2}\right), \qquad a_\perp(X, Y) = \frac{\mu}{\lambda}\sinh\big(\lambda s_\perp(Z)\big),$$
   yields a real-analytic Eikonal solution across **all of $(-e, e)^2$ including $(0,0)$**, paired with orthogonal trajectories connecting $Y = -e$ to $Y = +e$.

## 5. Addendum: Upper-Envelope Penetration $L_{\mathrm{true}}$ for `030/038`

When retaining the rotated Euclidean square union $D_N = \bigcup_i Q_i \subset [-e, e]^2$, the upper envelope
$$L_{\mathrm{true}}(X, Y) = \frac{16}{e} \max_i \Big(h_i - \max\big(|X - c_{X,i}|,\ |Y - c_{Y,i}|\big)\Big)_+,$$
heals the internal parent-seam fractures and exterior leakage of [038-eikonal-cayley.py](https://github.com/mountain/aeg-paper/blob/main/notes/general/038-eikonal-cayley.py) and isolates the countable shock locus onto $T_4$ plus parent-child neck gates (`039`, panel d).

**Caveat: $L_{\mathrm{true}}$ is the $L^\infty$ penetration depth, not in general the exact distance to the complement.**

- **Star-shaped / penetration hypothesis (equality)**: $L_{\mathrm{true}}$ equals the exact $L^1$ distance to $\partial D_N$ iff "the deepest square is also the outermost", i.e. every $L^\infty$ ray from the root exits the union exactly once ($L^\infty$-orthogonal convexity / directional star-shapedness). The Cayley tree union satisfies this along the main axes and diagonals (numerical cross-check agrees).
- **Lower bound in general**: near fjords and parent-child necks the union extends beyond the deepest square, so the penetration depth is $<$ the nearest-exit distance; $L_{\mathrm{true}}$ is then only a **lower bound** (random cross-check shows deviations up to $\sim0.85$ for the Cayley union and $\sim1.5$ for arbitrary unions).
- **Purpose and ground truth**: the concrete value of $L_{\mathrm{true}}$ is removing the internal pseudo-zero lines of `038` (unlike $\min_i|d_i-R_i|$, it takes the parent's positive penetration on interior seams and vanishes only in the exterior complement). For an exact distance one should use a **chessboard distance transform (CDT)** or the complement distance transform as ground truth; $L_{\mathrm{true}}$ is a fast lower bound / visualization.


## 6. Epistemic Status Summary

| Claim / Construction | Status | Verification |
| :--- | :--- | :--- |
| $\mathcal{S}: \mathbb{D}_w \xrightarrow{\sim} [-e, e]^2$ locks the 4 cusps to edge midpoints and 4 Pell axes to corners | **PROVED** | Exact integral identities + `039` ($10^{-15}$) |
| Conformal depth $f_{\mathrm{SC}}$ satisfies $K = f_{\mathrm{SC}}\Delta f_{\mathrm{SC}} - \|\nabla f_{\mathrm{SC}}\|^2 \equiv -1$ | **PROVED** | 4-line Wirtinger proof + `039` verification |
| Radial squircle fill $a_{\mathrm{rad}}$ and smooth cusp-to-cusp fill $a_\perp$ satisfy the intrinsic Eikonal PDE | **PROVED** | Analytic chain rule + `039` residual $< 10^{-14}$ |
| $L_{\mathrm{true}} = \max_i (R_i - d_i)_+$: fixes the `038` internal pseudo-zeros; equals the exact $L^1$ distance to the exterior **under the star-shaped/penetration hypothesis**, lower bound in general | **PROVED under star-shaped hypothesis** | Analytic + `039` panel (d) + main-axis cross-check; arbitrary unions deviate $\sim1.5$, exact value needs CDT |
| Interpreting the squircle-ray coordinates on $\mathcal{Q}_e$ directly as continuous add-multiply renormalization coordinates | **STRUCTURAL PROPOSAL** | Geometrically exact; arithmetic coupling open |
