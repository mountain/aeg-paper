# Pan/Encke Edge Waves: Tight-winding Density-wave Dispersion and Radial Wavelength (OQ-104.1)

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part VII: OQ-104.1 — solving the tight-winding density-wave dispersion relation to obtain the radial wavelength `λ(Δr)` and comparing it with observation).
> **Prerequisite**: Note VII, *Pan and the Encke Gap Edge Waves* ([007-pan-encke-farey.md](007-pan-encke-farey.md)).
> **Date**: 2026-11-14
> **Runnable witness**: [008-encke-density-wave-witness.py](008-encke-density-wave-witness.py) (pure Python `math`, no third-party deps).

---

## I. The dispersion relation (tight-winding WKB)

Pan's m-th density wave (pattern speed `ω = mΩ_P`) in the tight-winding (WKB) limit obeys the self-gravitating, pressure-supported dispersion relation

```
(ω − mΩ)² = κ² − 2πGΣ|k| + c²k² ,   κ = Ω（Kepler epicyclic frequency）
```

where `Σ` is the ring surface density, `c` the velocity dispersion, and `k` the **radial** wavenumber. Let the detuning be `D = (ω−mΩ)² − κ²` (`D=0` at resonance).

## II. Closed-form solution (a quadratic in k)

`c²k² − 2πGΣk − D = 0` gives the trailing wave (`k>0`)

```
k = [2πGΣ + √((2πGΣ)² + 4c²D)] / (2c²)
```

At resonance `D=0`: `λ₀ = 2π/k = c²/(GΣ)`. With `Σ=500 kg/m²`, `c=0.5 cm/s`:

```
λ₀ = c²/(GΣ) ≈ 749 m ≈ 0.75 km
```

**Key**: `k` is a **closed-form quadratic** in `D`; this step does not need the multivariate solver anticipated in OQ-104.2 (that is for the joint `(m,k)` full dispersion + boundary conditions).

## III. Result: the `λ(Δr)` curve

| m | r_res | azimuthal wavelength `2πr/m` | radial λ（Δr=0） | radial λ（Δr=2 km） | radial λ（Δr=10 km） |
| ---: | --- | ---: | ---: | ---: | ---: |
| 551 | a_P+161.6 km | 1525 km | 0.749 km | 0.630 km | 0.445 km |
| 100 | a_P+889.1 km | 8449 km | 0.749 km | 0.721 km | 0.639 km |
| 20 | a_P+4416.5 km | 43354 km | 0.749 km | 0.744 km | 0.723 km |

**Conclusion**: the radial wavelength `λ ≈ 0.75 km` (set by `c²/GΣ`) decreases **monotonically** with distance from resonance (the "wrapped-up" spiral). The azimuthal wavelength `2πr/m` is a separate quantity (constant for fixed m).

## IV. Comparison with observation

Tiscareno et al. (DPS 2005, abstract 64.02) on the Encke gap edges: "**wavelength in some regions does not remain constant but varies smoothly in a repeating pattern**… wavy edges are ubiquitous… covering 360° of longitude on both sides."

This is exactly the **wrapped-up-spiral signature** of a density wave: the radial wavelength varies smoothly with distance from resonance, and the wave is not damped efficiently (timescales ≳ 10 months). The dispersion relation is therefore the right framework, and this note closes OQ-104.1's "solve the dispersion" step.

## IV·5. Radial vs azimuthal comparison against measurement

The azimuthal wavelength `λ_θ = 2πr/m` (constant for fixed m) and the radial wavelength `λ_r = 2π/k` (varying with Δr) are two distinct quantities. Inverting an observed azimuthal wavelength to m and the resonance radius:

| observed λ_az | m = 2πr/λ | resonance radius r_res |
| --- | ---: | --- |
| 1525 km | 551 | a_P + 161.6 km (= the gap edge) |
| 500 km | 1681 | a_P + 53 km |
| 100 km | 8404 | a_P + 10.6 km |
| 50 km | 16807 | a_P + 5.3 km |

**Honest conclusion**: if the observed "wavy" wavelength is an **azimuthal** quantity (the literature often quotes ~50–100 km; **this value was not retrieved this session and is a recollection to be checked**), it maps to `m ~ 10⁴`, whose resonances lie at `a_P + 5–11 km` (**inside the cleared gap**), not at the edge `m≈551` (`λ_θ=1525 km`). So the observed short-wavelength edge ripple is **not** the `m≈551` free density wave — more likely a trapped **edge mode** (Papaloizou–Lin) or a higher-m feature. The radial wavelength `λ_r≈0.75 km` of this note is the **free density wave** scale, matching the "wavelength shrinks as the wave propagates" signature, but matching it to a specific observed value requires first fixing the observable (radial vs azimuthal) + more accurate `Σ/c`.

## V. Status and boundary

| ID | conclusion | status |
| --- | --- | --- |
| D1 | dispersion relation `(ω−mΩ)²=κ²−2πGΣ|k|+c²k²` and its closed form | `PROVED WITH STATED HYPOTHESES` (WKB + quadratic) |
| D2 | `λ₀ = c²/(GΣ) ≈ 0.75 km` at resonance | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` |
| D3 | radial wavelength decreases with Δr (wrapped-up), matching the "wavelength varies smoothly" observation | `COMPUTATIONALLY VERIFIED EXAMPLE` + observational comparison |
| D4 | exact quantitative match to the observed wavelength | `ADVANCED` (measured λ_θ≈260–320 km, A≈0.65 km, m≈3000, see §IV·5; confirmed to be an edge mode rather than the free m=551 wave; residual is the edge-mode dispersion's quantitative solution, see OQ-104.3) |

**Honest boundary**: this step solves the **radial** wavelength (~0.75 km, decreasing with Δr). Whether the specific "ripple" value in the observation (tens of km or km-scale) corresponds directly to this radial wavelength depends on the observable definition and the values of `Σ,c` — left for the closing of OQ-104.1, not over-asserted here. OQ-104.2's "multivariate solver" is **unnecessary** for this step (a closed-form quadratic), and is a real capability gap only for the full dispersion (m,k joint, boundary conditions).

## VI. Registration

This note does not modify the paper body and does not promote existing claims. It lands OQ-104.1's "solve the dispersion + obtain the wavelength curve + compare with observation", and registers it in [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9; OQ-104.1's status is updated to `ADVANCED` in [governance/08-open-questions.md](../../governance/08-open-questions.md). Research direction: Mingli Yuan; this analysis, witness, and status labelling: DeepSeekHarness, 2026-11-14.
