# Pan and the Encke Gap Edge Waves: a Farey–Ford Reading of a Resonance Ladder

**An application example of the Hyperbolic Tropical Wavefront-Residual (HTWR) framework**

Mingli Yuan (research direction); computation and drafting: DeepSeekHarness
2026-11-14 · v1.0

---

## Abstract

The scalloped edges of Saturn's Encke gap are the gravitational signature of the
shepherd moon Pan. We give a two-layer account. The *arithmetic layer* reads Pan's
Lindblad resonance ladder `x = m/(m±1)` as the Farey neighbourhood of corotation
(`x = 1`), realized as Ford circles piling up on the hyperbolic upper half-plane —
a concrete physical instance of the rational-approximation structure at the core
of the HTWR framework. The *dynamical layer* then resolves the observed wave: it is
neither a propagating density wave nor a (cold or pressure) edge mode, but Pan's
**static tidal distortion** (a forced epicycle), with radial amplitude
`GM_P/(κ²d²) ≈ 0.79 km` and azimuthal scale `≈ 250 km`, matching the values
extracted from a Cassini image (`≈ 0.65 km`, `≈ 300 km`). The two layers are
complementary: the arithmetic skeleton locates the gap (resonance overlap), while
the tidal distortion shapes its edge.

**Status.** §2–§3 (the Farey ladder and the gap-opening criterion) are the HTWR
reading; they are *structural proposals* plus elementary celestial mechanics.
§4–§6 are standard linear celestial mechanics, labelled `PROVED WITH STATED
HYPOTHESES` or `COMPUTATIONALLY VERIFIED EXAMPLE` as appropriate. The paper does
not claim a new theorem of AEG; it exhibits a physical realization of the
HTWR rational-approximation structure.

---

## 1. Introduction

Pan (mass `M_P ≈ 4.95×10¹⁵ kg`, semi-major axis `a_P = 133,584 km`) orbits inside
the Encke gap, a 325-km-wide division in Saturn's A ring. Its gravity excites a
scalloped ("wavy") pattern on both gap edges, observed by Voyager and Cassini and
ubiquitous over 360° of longitude (Tiscareno et al., DPS 2005). The aim of this
note is twofold:

1. to exhibit the **arithmetic structure** of Pan's resonances — a Farey ladder
   accumulating at corotation — as a concrete instance of the HTWR framework's
   rational-approximation geometry; and
2. to resolve the **dynamical mechanism** of the observed edge wave by
   elimination, ending at Pan's static tidal distortion.

The two parts are *complementary*, not the same phenomenon: the resonance ladder
explains *why the gap is there*, the tidal distortion explains *why its edge is
scalloped*.

---

## 2. The resonance ladder is a Farey sequence (the arithmetic layer)

In the linear epicyclic theory, the m-th gravitational component of Pan (pattern
speed `Ω_P`) excites a ring particle at the Lindblad resonance

```
m (Ω − Ω_P) = ±κ ,   Ω = κ = Ω_P (r/a_P)^{−3/2} .
```

Writing `x := Ω/Ω_P`, this is `m(x − 1) = ±x`, i.e.

```
inner (r < a_P):  x = m/(m−1)        outer (r > a_P):  x = m/(m+1) ,
resonance radius: r/a_P = x^{−2/3} .
```

Hence the resonance *frequencies* are exactly the **Farey neighbours** of
corotation:

```
x = m/(m±1)  →  1   as  m → ∞ .
```

| m | outer `x = m/(m+1)` | `r/a_P` (Arb-certified) | Ford radius `1/(2q²)` |
| ---: | --- | --- | --- |
| 1 | 1/2 | 1.58740 | 1.25×10⁻¹ |
| 10 | 10/11 | 1.06560 | 4.13×10⁻³ |
| 100 | 100/101 | 1.00666 | 4.90×10⁻⁵ |
| **551** | 551/552 | **1.00121** | 1.64×10⁻⁶ |

At `m = 551` the outer resonance sits at `r = a_P + 161.6 km`, i.e. at the Encke
outer edge (`+162 km`). This is the HTWR reading in one line: the resonance ladder
is a sequence of rational points `p/q ∈ P¹(Q)`, each carrying a Ford circle of
radius `1/(2q²)` tangent to the real axis at `p/q`, piling up at the corotation
cusp `x = 1`; the m-th resonance has "information height" `I = ln max(p,q) = ln(m+1)`
(the logarithm of the azimuthal wavenumber). **Status:** the ladder identity is
`PROVED` (elementary); the Ford-circle/hyperbolic reading is `STRUCTURAL PROPOSAL`.

---

## 3. Gap opening: the Chirikov resonance-overlap criterion

The gap edge is where the high-m resonances *overlap*. The relevant scales are

```
Hill radius      R_H = a_P (μ/3)^{1/3} ≈ 19.0 km      (μ = M_P/M_S = 8.7×10⁻¹²)
resonance width  δr  ≈ a_P √μ         ≈ 0.39 km
resonance spacing dR_m = 2 a_P/(3 m²)  = 0.293 km   (m = 551)
```

Overlap (Chirikov) requires `δr ≳ dR_m`, i.e. `m ≳ √(2/(3√μ)) ≈ 475`. The observed
edge (`m ≈ 551`) agrees with this to the O(1) coefficient of the resonance width.
Since `gap/R_H ≈ 8.5`, the gap is opened by the **resonance forest** (the dense
high-m ladder), not by direct Hill-sphere clearing. **Status:** `STANDARD
CONSEQUENCE` (Chirikov criterion) + `COMPUTATIONALLY VERIFIED EXAMPLE`.

---

## 4. The density-wave dispersion (the free wave, eliminated)

The tight-winding (WKB) dispersion for a self-gravitating, pressure-supported
disk is

```
(ω − mΩ)² = κ² − 2πGΣ|k| + c²k² ,
```

a closed-form quadratic in the radial wavenumber `k`. At resonance the radial
wavelength is `λ₀ = c²/(GΣ) ≈ 0.75 km` (`Σ = 500 kg/m²`, `c = 0.5 cm/s`),
*decreasing* away from resonance (the "wrapped-up" spiral). This matches the
observed "wavelength varies smoothly" signature qualitatively, but the free wave
lives at `m < 551` (resonance in the ring); the measured edge wave is `m ≈ 2800`,
whose resonance lies *inside* the cleared gap. Hence the observed edge wave is
**not** the free density wave. **Status:** `PROVED WITH STATED HYPOTHESES`
(dispersion) + `COMPUTATIONALLY VERIFIED EXAMPLE` (wavelength curve).

---

## 5. Edge-mode elimination (cold and pressure)

We test the Papaloizou–Lin edge mode in the cold WKB limit and with pressure.

*Cold WKB* (`σ² = κ² − 2πGΣ|k|`, reflecting edge, Airy quantization
`∫|k|dr = (n+3/4)π`): the turning point `r_L = a_P((m+1)/m)^{2/3}` lies outside the
edge only for `m < 551`; for `m ≥ 551` the resonance is inside the gap and the edge
is far off-resonance (evanescent decay length `≈ 0.5 m`).

*Pressure* (`Q = cκ/(πGΣ) ≈ 6`): the existence condition is geometric
(`m < 548`), independent of `c`; at `m = 2800` the pressure only yields a short
wave of radial wavelength `≈ 47 m`.

So the observed edge wave is **neither** a density wave **nor** an edge mode
(cold or pressure). **Status:** `PROVED WITH STATED HYPOTHESES` (turning-point
geometry) + `COMPUTATIONALLY VERIFIED EXAMPLE`.

---

## 6. The static tidal distortion (the resolution)

The edge lies `d ≈ 162 km ≈ 8.5 R_H` from Pan — the linear tidal regime
(`d ≫ R_H`). Pan's gravity pulls the edge radially, balanced by the epicyclic
restoring force `κ²δr`:

```
κ² δr = − GM_P · d / (d² + y²)^{3/2} ,
```

where `y` is the azimuthal offset from Pan. This is a **forced epicycle** with
eccentricity

```
e_f = (M_P/M_S)(a_P/d)² ≈ 5.9×10⁻⁶ ,
```

radial amplitude `A = a_P e_f = GM_P/(κ²d²)`, and azimuthal profile
`δr(y) = δr_max (1+(y/d)²)^{−3/2}` (a localized bump of width `d`).

| quantity | computed | observed (PIA08257) |
| --- | --- | --- |
| radial amplitude A | **0.785 km** | ≈ 0.65 km |
| azimuthal FWHM | **249 km** | ≈ 300 km |

Both agree to ~20%, inside the `Σ/c/geometry` uncertainty. **Status:** `PROVED
WITH STATED HYPOTHESES` (force balance) + `COMPUTATIONALLY VERIFIED EXAMPLE`
(match to the image).

---

## 7. Observation: extraction from a Cassini image

We extracted the edge-wave parameters directly from NASA's public-domain image
PIA08257 ("Encke Waves", 1 km/px original, stretched 4× in the radial direction),
detecting the gap edges and fitting the strongest sinusoid: azimuthal wavelength
`λ_θ ≈ 260–320 km` and radial amplitude `A ≈ 0.65 km`, hence `m = 2πr/λ_θ ≈ 2800`.
Reproducible in `aeglib`/numpy scripts (`008-encke-edge-wave-image.py`). **Status:**
`COMPUTATIONALLY VERIFIED EXAMPLE`.

---

## 8. Discussion: what the HTWR framework does and does not contribute

The HTWR framework contributes the **arithmetic skeleton**: the resonance ladder
is a Farey sequence realized as Ford circles on `H²`, with the corotation point as
the cusp. This is a *physical realization* of the rational-approximation structure
that the HTWR axioms (state space `P¹(Q)`, logarithmic-Weil-height calibration)
abstract — not a new theorem, and not the mechanism of the edge wave itself.

The edge-wave *mechanism* is standard linear celestial mechanics (forced
epicycle), where the HTWR framework has no role. The two layers answer different
questions: *where* the gap is (resonance overlap, the Farey pile-up), and *what
shape* its edge has (static tidal distortion).

**Honest boundary.** The secondary signatures — "wavelength varies smoothly",
"amplitude grows and decays", "undamped over ≳ 10 months" — are not captured by
the static force balance; they require the full dynamics (collisional damping and
multi-m superposition). These remain open (see `governance/08-open-questions.md`,
OQ-104).

---

## 9. Conclusion

The Encke gap's scalloped edges are a two-layer phenomenon: an **arithmetic
skeleton** (Pan's Lindblad resonances form the Farey ladder `x = m/(m±1)`,
accumulating at corotation as Ford circles — a concrete instance of the HTWR
rational-approximation structure), and a **dynamical layer** (the observed edge
wave is Pan's static tidal distortion, a forced epicycle of amplitude
`GM_P/(κ²d²) ≈ 0.79 km`, matching the observed ≈ 0.65 km). The framework's value
here is exemplary: it turns a resonance catalogue into a geometric object on
`P¹(Q)`, while the physics that shapes the edge remains classical.

---

## References

- Cuzzi, J. N., & Scargle, J. D. 1985, ApJ, 292, 276 — "Wavy edges suggest moonlet in Encke's gap".
- Tiscareno, M. S., Burns, J. A., Hedman, M. M., et al. 2005, BAAS, 37, 64.02 — "Wavy Edges and Other Disturbances in Saturn's Encke and Keeler Gaps".
- Goldreich, P., & Tremaine, S. 1979, ApJ, 233, 857 — density wave theory.
- Papaloizou, J. C. B., & Lin, D. N. C. 1988, ApJ, 331, 838 — edge modes.
- NASA/JPL/Space Science Institute, PIA08257 "Encke Waves" (public domain).
- Companion notes: `notes/general/007–010`; governance `OQ-103/OQ-104`.

---

## Mathematical status register

| ID | Claim | Status |
| --- | --- | --- |
| R1 | resonance ladder `x = m/(m±1)`, radius `r/a_P = x^{−2/3}` | `PROVED WITH STATED HYPOTHESES` |
| R2 | Ford-circle / hyperbolic reading (HTWR) | `STRUCTURAL PROPOSAL` |
| R3 | Chirikov overlap → gap edge `m ≈ 551` | `STANDARD CONSEQUENCE` + `COMPUTATIONALLY VERIFIED` |
| R4 | density-wave dispersion, `λ₀ = c²/(GΣ)` | `PROVED WITH STATED HYPOTHESES` |
| R5 | edge mode absent for `m ≥ 551` (cold & pressure) | `PROVED WITH STATED HYPOTHESES` |
| R6 | static tidal distortion `A = GM_P/(κ²d²)` | `PROVED WITH STATED HYPOTHESES` |
| R7 | image extraction `λ_θ ≈ 300 km`, `A ≈ 0.65 km` | `COMPUTATIONALLY VERIFIED EXAMPLE` |
