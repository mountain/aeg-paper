# The Encke Edge Mode in the Cold-WKB Test: a Negative Closure of OQ-104.3

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part VIII: OQ-104.3 — testing the cold self-gravitating WKB edge mode (Papaloizou–Lin type) via its quantization; the conclusion is a negative closure).
> **Prerequisites**: Note VII ([007-pan-encke-farey.md](007-pan-encke-farey.md)); Note VIII ([008-encke-density-wave.md](008-encke-density-wave.md)).
> **Date**: 2026-11-14
> **Runnable witness**: [008-encke-edge-mode-wkb.py](008-encke-edge-mode-wkb.py) (pure numpy, no third-party deps).

---

## I. The object under test

OQ-104.3's original statement: the cold self-gravitating WKB mode `σ² = κ² − 2πGΣ|k|`, with the reflecting boundary `Σ₁(r_edge)=0` and the Airy turning-point quantization `∫_{r_edge}^{r_L}|k|dr = (n+3/4)π`, giving the discrete edge-mode frequencies `ω_n(m)` and their radial extent.

## II. Result (negative)

For the gap outer edge `r_edge = a_P + 162 km` and pattern speed `ω = mΩ_P` (Pan's m-th component):

| m | turning point r_L (Lindblad resonance) | conclusion |
| ---: | --- | --- |
| 100–500 | a_P + 178–889 km (**outside the edge**) | density wave exists, radial order n ≈ 31–10342 (**high n**, not a confined edge mode) |
| **551** | a_P + 161.6 km (= the edge) | degenerate boundary |
| **≥ 551** (incl. measured m≈2800) | a_P + 5–148 km (**inside the gap**) | **no confined mode** |

**Key**: the turning point `r_L = a_P((m+1)/m)^{2/3}`. `r_L > r_edge` requires `m < 551`; for `m ≥ 551` the Lindblad resonance lies in the **cleared interior of the gap**, and at the edge `σ² > κ²` is an **evanescent** zone — no propagating wave, no confined mode.

For the measured `m ≈ 2800`: `σ ≈ 5.1Ω` (far off-resonance), evanescent radial decay length

```
1/k_ev = (2πGΣ)/(σ²−κ²) ≈ 0.5 m
```

**about half a metre** — in complete contradiction with the observed edge wave (amplitude ~0.65 km, covering 360°, "wavelength varies smoothly").

## III. Conclusion

1. The **cold WKB edge mode does not exist for `m ≥ 551`** (turning point inside the gap); for `m < 551` it degenerates into a **high-n density wave** (not a confined edge mode).
2. The measured `m ≈ 2800` edge wave lies in a **far-off-resonance evanescent zone** (decay length ~0.5 m), so it is **not** a cold WKB edge mode.
3. Hence **OQ-104.3's "cold self-gravitating WKB" formulation is refuted**. The observed edge wave needs another mechanism — pressure (`c>0`, the genuine Papaloizou–Lin confined mode) or **Pan's near-field gravitational distortion (Hill sphere / wake)** — neither of which is OQ-104.3's original cold WKB.

## III·5. Pressure re-check (Q≈6, added 2026-11-14)

Adding the pressure term `σ² = κ² − 2πGΣ|k| + c²k²` (Toomre `Q = cκ/(πGΣ) ≈ 6.02`, `λ_crit = c²/(GΣ) ≈ 0.75 km`) and re-checking (witness [009-encke-edge-mode-pressure.py](009-encke-edge-mode-pressure.py)):

| m | σ/κ (at the edge) | short-wave radial wavelength |
| ---: | ---: | ---: |
| 551 | 1.01 | 210 m |
| 1000 | 1.83 | 125 m |
| **2800** | **5.11** | **47 m** |
| 10000 | 18.25 | 13.5 m |

**Conclusion (still negative)**: the mode-existence condition is **geometric** (the turning point must lie in the ring `r_t > r_edge`, i.e. `ω < 0.99818(m+1)Ω_P`, hence `m < 548` for `ω≈mΩ_P`), **independent of pressure**. At `m=2800` the edge is far off-resonance (`σ≈5.1κ`), and the pressure only gives a short wave of ~47 m — not the observed ~0.65 km radial amplitude. **Pressure cannot turn the m≈2800 edge wave into a confined edge mode.**

## IV. Status

| ID | conclusion | status |
| --- | --- | --- |
| E1 | turning point `r_L = a_P((m+1)/m)^{2/3}`, outside the edge only for `m<551` | `PROVED WITH STATED HYPOTHESES` (direct Kepler computation) |
| E2 | cold WKB edge mode absent for `m≥551` | `STANDARD CONSEQUENCE` (from E1 + the quantization definition) |
| E3 | measured m≈2800 in the evanescent zone, decay ~0.5 m | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| E4 | observed edge wave = pressure-confined mode or near-field distortion (not cold WKB) | `STRUCTURAL PROPOSAL` / `OPEN` (needs the pressure dispersion or a Hill near-field model) |

**Closure**: OQ-104.3's original "cold self-gravitating WKB edge mode" is **refuted**; the genuine open items are the pressure-confined edge mode (`c>0`, dispersion `σ²=κ²−2πGΣ|k|+c²k²` + reflecting boundary) or Pan's near-field distortion. Registered in [governance/08-open-questions.md](../../governance/08-open-questions.md) OQ-104.3.

Research direction: Mingli Yuan; this test, witness, and status labelling: DeepSeekHarness, 2026-11-14.
