# Pan and the Encke Gap Edge Waves: the Farey/Ford Structure of the Lindblad Resonance Ladder (an AEG application)

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part VI: reading the Lindblad resonance ladder of the Pan/Encke gap edge waves as a Farey/Ford structure, with aeglib certifying the core algebraic numbers).
> **Prerequisites**: Note I, *The HTWR Core*, Axioms I–IV ([001-htwr-core.md](001-htwr-core.md)); Note IV, *Fanout Cost and Interval Wrapping* ([005-fanout-wrapping.md](005-fanout-wrapping.md)).
> **Date**: 2026-11-14
> **Runnable witnesses** (aeglib 0.0.2, both certifying algebraic numbers with `ArbBall`):
> - [pan_encke_resonance_ladder.py](../../../aeglib/python/examples/pan_encke_resonance_ladder.py) (the resonance ladder)
> - [pan_encke_gap_criterion.py](../../../aeglib/python/examples/pan_encke_gap_criterion.py) (Hill radius + resonance overlap)

---

## I. The physical object

Pan is the moon orbiting inside Saturn's Encke gap (mass `M_P≈4.95×10¹⁵ kg`, `GM_P≈3.3×10⁻⁴ km³/s²`, semi-major axis `a_P=133,584 km`). Its gravity excites **edge waves** at the gap edges, observed as a scalloped pattern. This note uses linear epicyclic celestial mechanics to locate those resonances, and reads their **frequency structure** as the Farey/Ford structure of AEG/HTWR.

## II. The Lindblad resonance ladder = a Farey sequence

Pan's m-th gravitational component, with pattern speed `Ω_P`, excites a ring particle at the **Lindblad resonance**

```
m(Ω − Ω_P) = ±κ ,   Ω = κ = Ω_P (r/a_P)^{−3/2}
```

Writing `x := Ω/Ω_P` gives `m(x−1)=±x`, i.e.

```
inner resonance (r<a_P)：x = m/(m−1)      outer resonance (r>a_P)：x = m/(m+1)
resonance radius：r/a_P = x^{−2/3}
```

**Core observation**: the resonance frequency ratios `x = m/(m±1)` are exactly the **Farey neighbours** of the corotation point `x=1`, with `x→1` as `m→∞`. aeglib `ArbBall`-certified resonance radii (excerpt):

| m | outer resonance x | r_outer/a_P (Arb) | Ford radius 1/(2q²) |
| ---: | --- | --- | --- |
| 1 | 1/2 | 1.58740 | 1.25e-1 |
| 2 | 2/3 | 1.31037 | 5.56e-2 |
| 10 | 10/11 | 1.06560 | 4.13e-3 |
| 100 | 100/101 | 1.00666 | 4.90e-5 |
| **551** | 551/552 | **1.00121** | 1.64e-6 |

**Core result**: the `m=551` outer resonance radius is `a_P + 161.6 km`, precisely the Encke outer edge (`+162 km`). That is, the gap edge is where Pan's high-m resonances begin to pile up densely.

## III. The gap-opening criterion (Chirikov resonance overlap)

Two algebraic numbers and one exact rational spacing, certified by aeglib:

| quantity | formula | value (Arb-certified) |
| --- | --- | --- |
| Hill radius | `R_H = a_P (μ/3)^{1/3}` | **19.05 km** |
| resonance width | `dr ~ a_P √μ` (O(1) coefficient suppressed) | **0.394 km** |
| resonance spacing (m=551) | `dR_m = 2a_P/(3m²)` | **0.293 km** (exact rational `89056/303601`) |
| overlap m | `dr = dR_m ⇒ m ≈ √(2/(3√μ))` | **≈ 475** |

**Conclusion**: `dr ≈ dR_m` (0.394 km ≈ 0.293 km) holds at `m≈500–550` — the gap edge is where Pan's high-m resonances **begin to overlap** (the Chirikov criterion). The gap half-width `≈ 8.5 R_H` shows the gap is opened by the **resonance forest** overlap, not by direct Hill-sphere clearing (the Hill radius is only 19 km). `m_overlap≈475` and the edge `m≈551` agree to the O(1) coefficient.

## IV. The AEG/HTWR reading

1. **Farey structure (exact)**: the resonance frequency ratios `x=m/(m±1)` are the Farey neighbours of corotation `x=1`, accumulating at `1` as `m→∞`. This is the **same rational approximation** as the HTWR `P¹(Q)` model (Ford circles, continued fractions) — **not an analogy**.
2. **Ford-circle geometry (`STRUCTURAL PROPOSAL`)**: each resonance `x=p/q` carries a Ford circle of radius `1/(2q²)`; for `x=m/(m±1)` the radius is `≈1/(2m²)`, shrinking with m and piling up at the corotation cusp `x=1`. This is the geometry of the "resonance forest"; the resonance spacing `d(r/a_P)/dm≈−2/(3m²)` matches the Ford-circle `~1/m²` pile-up law.
3. **HTWR depth (`STRUCTURAL PROPOSAL`)**: the "information height" of the m-th resonance `I = ln max(|p|,|q|) = ln(m+1)` is the logarithm of the azimuthal wavenumber m — the satellite's **single** driving frequency is "fanned out" into m azimuthal harmonics, and m is exactly the HTWR fanout count.

## V. Status and boundary

| ID | conclusion | status |
| --- | --- | --- |
| P1 | resonance ladder `x=m/(m±1)` and radius `r/a_P=x^{−2/3}` | `PROVED WITH STATED HYPOTHESES` (direct Kepler/epicyclic computation + Arb certification) |
| P2 | outer edge `m≈551` coincidence (`a_P+161.6 km`) | `COMPUTATIONALLY VERIFIED EXAMPLE` (Arb certification + comparison to the observed edge radius) |
| P3 | resonance-overlap criterion `dr≈dR_m`, `m_overlap≈475`, `gap≈8.5 R_H` | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` (standard scaling of the Chirikov criterion) + `COMPUTATIONALLY VERIFIED` |
| P4 | Farey/Ford reading (resonance forest = corotation-cusp pile-up) | `STRUCTURAL PROPOSAL` |
| P5 | HTWR depth `I=ln(m+1)` reading | `STRUCTURAL PROPOSAL` |

**Boundary**: this note establishes the **skeleton** of the resonance ladder (frequencies/radii/overlap criterion). The **specific wavelength and amplitude** of the edge wave need the density-wave dispersion relation (self-gravity `2πGΣ|k|` + edge modes); the observed wavelength of tens of km (m~10⁴) is not the m≈551 resonance itself — this exceeds the current scope and is registered as OQ-104.

## VI. Registration

This note does not modify Axioms I–IV, does not modify the paper body, and does not promote existing claims. It turns the Pan/Encke phenomenon into two reproducible aeglib certified computations, and registers the Farey/Ford reading in [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9; the open item is registered as [governance/08-open-questions.md](../../governance/08-open-questions.md) OQ-104. Research direction: Mingli Yuan; this analysis, certification, and status labelling: DeepSeekHarness, 2026-11-14.
