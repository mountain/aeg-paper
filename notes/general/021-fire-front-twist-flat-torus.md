# 021 — The fire-front twist on the flat torus: $C_t$, self-intersection count = Gauss circle problem, Gauss words, and the twist/untwist movie

> **Document type**: Arithmetic Expression Geometry (AEG) research note (021: the *twist pattern* of the fire-method wavefront, made precise, provable, and reproducible on $\mathbb T^2$)
> **Prerequisites**: Note 018 [*Cayley model: assignment, duality, add–multiply decomposition and Eikonal fill*](018-cayley-assignment-duality-eikonal.en.md) (its §6–7 locate the Eikonal equation and the "medial / Voronoi ridge / cut locus" as the correct form of the fire method); Note 019 [*SC-square conformal hyperbolic model*](019_sc_square_eikonal_en.md) (radial Eikonal fill = the ordinary circles in the cover)
> **Date**: 2026-11-20
> **Note**: companion script `047-fire-front-twist.py`; every claim carries a status (`PROVED` / `COMPUTATIONALLY VERIFIED EXAMPLE` / `STRUCTURAL PROPOSAL`).

---

## 1. The object: circles in the cover, twisting on the quotient

Let $M=\mathbb T^2=\mathbb R^2/\mathbb Z^2$ (unit square torus), basepoint $p=0$, universal cover $\widetilde M=\mathbb R^2$, deck group $\Gamma=\mathbb Z^2$. The fire spreads from $\tilde p=0$; at time $t$ the front in the cover is the ordinary circle

$$\Sigma_t=\{x\in\mathbb R^2:\|x\|=t\},$$

and on the quotient the **distance circle**

$$C_t=\pi(\Sigma_t)=\big\{\big(t\cos\theta\bmod 1,\ t\sin\theta\bmod 1\big):\theta\in[0,2\pi)\big\}.$$

- for $t<\tfrac12$, $C_t$ is a smooth embedded circle ($\mathrm{inj}(0)=\tfrac12$, half the systole);
- at $t=\tfrac12$ the first self-tangency occurs;
- for $t>\tfrac12$, $C_t$ is an immersed circle with transverse self-intersections.

"Plain circle in the cover, repeatedly twisting and untwisting on the surface" is exactly the *parametrized movie* of $C_t$ (`047` emits `047-fire-front-twist.gif`, 120 frames, $t\in[0.05,2.5]$).

## 2. Self-intersections = chords whose displacement is a lattice vector; event times = half lattice lengths (`PROVED`)

$C_t$ self-intersects at $q$ iff two distinct circle points satisfy $x'\equiv x\pmod{\mathbb Z^2}$, i.e. $x'-x=v\in\mathbb Z^2\setminus\{0\}$. A radius-$t$ circle admits a chord of displacement $v$ iff $\|v\|<2t$. Hence:

1. every crossing is labelled by a nonzero lattice vector $v=(m,n)$;
2. it is born at the **event time**

$$t=\frac{\|v\|}{2}=\frac12\sqrt{m^2+n^2};$$

3. event times = half lattice lengths = half the **based geodesic-loop length spectrum** of $(M,p)$ (for $\mathbb T^2$ the lattice lengths $\sqrt{m^2+n^2}$, systole $=1$, first event $t=\tfrac12$).

Each **unoriented** lattice vector $\{v,-v\}$ contributes exactly two parallel chords for $t>\|v\|/2$ (two midpoints $\pm\sqrt{t^2-\|v\|^2/4}\cdot\hat v^\perp$), collapsing to one diameter self-tangency at $t=\|v\|/2$. So each event increases $N(t)$ by $2\times(\text{number of unoriented vectors of that length})$.

**Check** (`COMPUTATIONALLY VERIFIED EXAMPLE`, script self-check `len(crossings_at(t)) == N_exact(t)` passes): $N(0.49)=0\to N(0.51)=4$ (event $t=\tfrac12$, $+4$); $N(0.70)=4\to N(0.71)=8$ ($t=\tfrac{\sqrt2}{2}$, $+4$); $N(0.99)=8\to N(1.01)=12$ ($t=1$, $+4$).

## 3. Main result: $N(t)=r_2(2t)-1$ (`PROVED`)

Since crossings are in bijection with nonzero lattice vectors $v$ ($\|v\|<2t$), the self-intersection count is

$$N(t)=\#\{v\in\mathbb Z^2\setminus\{0\}:\|v\|<2t\}=r_2(2t)-1,$$

where $r_2(R)$ is the **Gauss circle problem** counting function. Thus $N(t)\sim 4\pi t^2$ (area argument, exact leading term). Numerically (script printout): $N(2)=44$, $N(3)=108$, matching $4\pi t^2$ ($\approx 113.1$ at $t=3$) to leading order.

**Conclusion (provable)**: on the unit square torus the "twist self-intersection count of the diffusion circle" *is* the Gauss circle problem; each crossing is labelled by a lattice vector $v$ with birth time $t=\|v\|/2$. This is the zero-curvature, cleanest exposure of "the twist pattern sweeps out the based length spectrum in time order".

## 4. Gauss words (`COMPUTATIONALLY VERIFIED EXAMPLE`)

The cyclic order in which the crossings are met along $C_t$ (as $\theta$ increases) is its Gauss word. The script prints, for $t=0.60,0.78,1.10$:

| $t$ | $N(t)$ | Gauss word (cyclic; each label appears twice) |
|---|---|---|
| 0.60 | 4 | `2 1 0 2 3 0 1 3` |
| 0.78 | 8 | `7 1 4 6 2 4 0 3 6 0 5 7 3 5 1 2` |
| 1.10 | 12 | `4 10 1 6 3 4 8 2 6 0 10 8 5 11 0 7 2 5 9 3 7 1 11 9` |

Each label appears exactly twice (a valid Gauss code of one immersed circle with transverse double points). The Gauss word records how the lattice vectors interlace in angular order — a finer invariant than $N(t)$.

## 5. Sharpening "twist / untwist" and its interfaces

1. **$N(t)$ is a monotone staircase (`PROVED`)**: $N(t)=r_2(2t)-1$ never decreases — on a closed surface $C_t$ never "unties" back to a simple circle; global complexity rises monotonically, jumping only at $t=\|v\|/2$.
2. **"Untwisting" is a local perestroika (`STRUCTURAL PROPOSAL`)**: at each event the front undergoes an A/D-type reconnection (self-tangency $\to$ two transverse crossings), locally smoothing out before the next event — an explicit flat instance of Arnold wavefront perestroikas.
3. **Cut-locus consistency (`PROVED`)**: the cut locus of $0$ on $\mathbb T^2$ is $\{x=\tfrac12\}\cup\{y=\tfrac12\}$ (the first self-tangency locus), matching Note 018 §7's "medial / Voronoi ridge".
4. **Interface to Paper 3's writhe (`STRUCTURAL PROPOSAL`)**: $C_t$ lifts to the unit tangent bundle $ST\,\mathbb T^2\simeq\mathbb T^3$ (contact structure) as a Legendrian curve; its self-linking (Thurston–Bennequin) is the rigorous twist number, connecting to Paper 3 §08's $w:B_n\to\mathbb Z$ and the Markov obstruction. **Not yet computed on the torus**; left as next step.

## 6. Status summary

| Result | Status |
|---|---|
| Self-intersection ⟺ chord displacement a nonzero lattice vector; event time $t=\|v\|/2$ | `PROVED` |
| $N(t)=r_2(2t)-1$, $N(t)\sim 4\pi t^2$ | `PROVED` |
| Each unoriented vector gives two chords; each event jumps by $2\times$ (#unoriented vectors) | `PROVED` |
| $N(0.49)=0,0.51=4,0.71=8,1.01=12,2=44,3=108$ | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| Gauss words ($t=0.60,0.78,1.10$) | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| Flat-torus cut locus $=\{x=\tfrac12\}\cup\{y=\tfrac12\}$ | `PROVED` |
| "Untwist" = A/D perestroika; Legendrian / self-linking interface | `STRUCTURAL PROPOSAL` |

## Appendix: script index

`047-fire-front-twist.py` emits: `047-fire-front-twist-t0_35/0_60/0_78/1_10.png` (cover circle vs quotient fold, four snapshots), `047-fire-front-twist-nt.png` ($N(t)$ staircase with event labels), `047-fire-front-twist.gif` (120-frame movie). Event table, Gauss words, and $N(t)$ samples are printed by the script (quoted in §2–§4 above).
