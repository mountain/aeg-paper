# The Encke Scalloped Edge: Pan's Static Tidal Distortion (a Forced Epicycle)

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part IX: the final closure of the Pan/Encke line — the edge wave is Pan's static tidal distortion (a forced epicycle), with amplitude and azimuthal scale matching the measurement).
> **Prerequisites**: Note VII ([007-pan-encke-farey.md](007-pan-encke-farey.md)); Note VIII ([008-encke-density-wave.md](008-encke-density-wave.md)); Note IX ([009-encke-edge-mode-wkb.md](009-encke-edge-mode-wkb.md)).
> **Date**: 2026-11-14
> **Runnable witness**: [010-encke-scalloped-edge-tidal.py](010-encke-scalloped-edge-tidal.py) (pure numpy).

---

## I. The mechanism

The gap edge (`d = 162 km` from Pan) lies about **8.5 Hill radii** away (`R_H ≈ 19 km`), in the **linear tidal regime** (`d ≫ R_H`). Pan's gravity pulls the edge particles radially, and the epicyclic restoring force `κ²δr` balances it:

```
κ² δr = −GM_P · d / (d² + y²)^{3/2}
```

where `y` is the azimuthal offset from Pan. This is equivalent to a **forced eccentricity**

```
e_f = (M_P/M_S)(a_P/d)²
```

with radial amplitude `A = a_P e_f = GM_P/(κ²d²)`, and azimuthal profile `δr(y) = δr_max (1+(y/d)²)^{−3/2}` (a localized bump of width `d`).

## II. Result (compared with measurement)

| quantity | computed | measured (PIA08257 extraction) |
| --- | --- | --- |
| radial amplitude A | **0.785 km** | ~0.65 km ✓ |
| azimuthal scale (FWHM) | **249 km** | ~300 km ("wavelength" 260–320 km) ✓ |
| forced eccentricity e_f | 5.9×10⁻⁶ | — |

**Both agree** (amplitude to ~20%, scale to ~20%, within the `Σ/c/geometry` uncertainty).

## III. Conclusion

The "ripple" of the Encke gap edge is **Pan's static tidal distortion (a forced epicycle / scalloped edge)**:

- it is **not** a propagating density wave (excluded by 008), and **not** a cold/pressure edge mode (excluded by 009);
- it is the **static (steady in the co-rotating frame) distortion** of the edge by Pan's direct gravity;
- amplitude `GM_P/(κ²d²) ≈ 0.79 km`, azimuthal scale `~d ≈ 162 km`, matching the measurement.

This completes the quantitative model of the "near-field distortion" left open by 009 — **the core quantities (amplitude + scale) are now closed**.

## IV. Secondary signatures still open

Three "fine signatures" of the observation still need full dynamics (not the static force balance):

1. **"wavelength varies smoothly"**: needs expanding the forced response along the edge (multi-m superposition + local geometry), not a single bump.
2. **"amplitude grows and decays"**: needs damping (collisional/viscous) + re-excitation.
3. **"undamped ≳10 months"**: needs showing why collisional damping is inefficient here.

These are **second-order corrections**, not affecting the first-order conclusion (amplitude/scale already matched).

## V. Status

| ID | conclusion | status |
| --- | --- | --- |
| T1 | forced eccentricity `e_f=(M_P/M_S)(a_P/d)²`, amplitude `GM_P/(κ²d²)` | `PROVED WITH STATED HYPOTHESES` (direct epicyclic force balance) |
| T2 | amplitude 0.79 km, FWHM 249 km match the measurement | `COMPUTATIONALLY VERIFIED EXAMPLE` (PIA08257 comparison) |
| T3 | edge wave = Pan static tidal distortion (not density wave / edge mode) | supported by 008+009 exclusion + T1/T2, `PROVED WITH STATED HYPOTHESES` |
| T4 | "varies smoothly / grows-decays / undamped" fine signatures | `OPEN` (full dynamics, second order) |

## VI. Registration

This note is the **final closure** of the Pan/Encke line: the resonance skeleton (007, why the gap is there) + the density-wave dispersion (008, the spiral waves in the ring) + the edge-mode exclusion (009) + **the static tidal distortion (010, why the edge is scalloped)**. Registered in [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9; the closing of OQ-104 is in [governance/08-open-questions.md](../../governance/08-open-questions.md).

Research direction: Mingli Yuan; this derivation, witness, and status labelling: DeepSeekHarness, 2026-11-14.
