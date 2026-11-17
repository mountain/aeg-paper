# The Split-tube as an HTWR Decomposition: VdP C11's "Main Wire + Fanout-Auxiliary Wire" (OQ-103.4)

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part V: OQ-103.4 — formalising the VdP C11 split-tube as the HTWR "main wire + fanout-auxiliary wire" decomposition, and checking its term-by-term wrapping reduction).
> **Prerequisites**: Note I, *The HTWR Core*, Axioms I–IV ([001-htwr-core.md](001-htwr-core.md)); Note IV, *Fanout Cost and Interval Wrapping* ([005-fanout-wrapping.md](005-fanout-wrapping.md)); [aeglib docs 17](../../../aeglib/docs/17-vdp-c11-certification.md) §11–12.
> **Date**: 2026-11-14
> **Runnable witness**: [006-split-tube-witness.py](006-split-tube-witness.py) (pure Python RK4 + RHS magnitude check, no third-party deps).
> **Implementation reference**: `aeglib/crates/aeg-hilbert16/src/vdp_certified/{model,taylor}.rs` (0.0.2, `f93947f`).

---

## I. The VdP augmented 8-dimensional system and its block-triangular structure

The VdP C11 certification merges the periodic orbit, the variational matrix, and the horizontal action into one 8-dimensional augmented state

```
z = (x, y, φ11, φ12, φ21, φ22, A_hor, I)
```

whose vector field (`model.rs::rhs_interval`, `ε=1`) is

```
x'   = y                                    (phase)
y'   = ε(1−x²)y − x                          (phase)
φ11' = φ21
φ12' = φ22
φ21' = j21·φ11 + j22·φ21                     (variational, j21 = −1−2εxy, j22 = ε(1−x²))
φ22' = j21·φ12 + j22·φ22                     (variational)
A_hor' = ε(1−x²)y − x − y²                    (horizontal action)
I'   = y²                                    (action)
```

**Block-triangularity (definitional fact)**: the phase/action components `(x', y', A_hor', I')` depend **only** on `(x, y)`, not on the variational `φ`; the variational components `φ'` depend on `(x, y)` **and** `φ`. That is,

```
F₁(x, y)   = (x', y', A_hor', I')            depends on (x,y) — the main wire
F₂(x, y, φ) = (φ11', …, φ22')                depends on (x,y) and φ — the auxiliary wire
```

`φ` does **not** feed back into the phase/action. This is exactly the comment in `taylor.rs`'s split-tube: "phi does not feed back into the phase/action components, so its much larger RHS must not inflate the x/y tube."

## II. The HTWR decomposition

Applying Note IV's (005) "fanout cost" reading to this system:

| HTWR object | VdP C11 components | meaning |
| --- | --- | --- |
| **main wire (main carrier)** | `(x, y)` phase + `(A_hor, I)` action | the depth-1 main carrier advancing the actual state and accumulating the horizontal action `A_hor=∫(Q−yP)dt`, `I=∫y²dt` |
| **fanout-auxiliary wire** | `φ = ∂z/∂z₀` variational matrix | the linearised tangent response of the phase state: the Jacobian `J(x,y)=[[0,1],[−1−2εxy, ε(1−x²)]]` **fans out** `(x,y)` into its entries, then propagates by `Φ'=JΦ` |
| **transverse catalytic flux Σ_aux** | the four `φ` components | the linearised "auxiliary wires" that must run parallel to the main carrier — the HTWR fanout copies |

Key: `J(x,y)` is exactly Note IV's "`x` fanned out multiple times", in VdP form — the phase `(x,y)` is fanned out into `j21=−1−2εxy` (reads `x,y` twice) and `j22=ε(1−x²)` (reads `x` twice), then multiplied into `φ`. So the variational block is the **Δ fan-out** of the phase state, and its cost (wrapping width) is the transverse catalytic flux.

## III. The split-tube's term-by-term wrapping reduction

`taylor.rs` splits the Picard tube into two groups:

```
phase = [0,1,6,7]      r_phase = 0.5·h·max_{i∈phase}|F_i|
phi   = [2,3,4,5]      r_phi   = 0.5·h·max_{i∈phi}|F_i|
```

The unsplit (single-radius) tube is `r = 0.5·h·max_{0≤i≤7}|F_i|`. By block-triangularity, `F₁` does not read `φ`, so `r_phase` is determined entirely by the main wire's own RHS — it does **not** carry the fanout's cost. Hence

```
r_phase ≤ r （strict when some variational component's |F| exceeds all phase/action components）
```

**Term-by-term conclusion**: the split-tube's main-wire radius is **never wider** than the unsplit one; it is the operationalisation of the HTWR principle "the main wire does not pay for the fanout-auxiliary wire" (Axiom II.3: Δ carries an independent positive action cost) in interval arithmetic. The variational tube `r_phi` is charged separately (the auxiliary wire's transverse flux).

## IV. Computational check (006 witness)

1. **Block-triangularity**: setting `φ` to zero and recomputing the RHS leaves the phase/action components unchanged → `True` (a numerical check of the definitional fact).
2. **Radius reduction**: along the C11 periodic orbit (`y₀=2.1727126964`, RK4), pointwise `max|F_phase|`, `max|F_phi|` and `r_phase/r_unsplit`:

| t | max\|F_phase\| | max\|F_phi\| | r_phase / r_unsplit |
| ---: | ---: | ---: | ---: |
| 0.00 | 4.7207 | 1.0000 | 1.0000 |
| 1.00 | 3.3237 | 3.2191 | 1.0000 |
| 2.00 | 0.9540 | 0.2807 | 1.0000 |
| 3.00 | 3.9221 | 1.5825 | 1.0000 |
| 3.62 | 7.7175 | **8.4773** | **0.9104** |
| 4.00 | 4.6078 | 3.2744 | 1.0000 |

**Honest finding**: on the **converged C11 periodic orbit**, the variational RHS is not consistently dominant (`r_phase/r_unsplit` is mostly 1, dropping to 0.91 only at `t≈3.62`). Hence the split-tube's term-by-term wrapping reduction is **weak** (`r_phase ≤ r`, at most ~9% on this orbit). Its **decisive value is in the shooting phase**: doc 17 §11 records that pre-fix `φ21'≈29.5` (`t≈3.62`), when the variational RHS far exceeds the phase RHS, the single radius is pulled up by the variational term, which in turn amplifies the `x,y` nonlinear terms and diverges; only the split pins the main wire. This is consistent with "φ is bounded on the periodic orbit but can blow up during shooting".

## V. Status and boundary

| ID | conclusion | status |
| --- | --- | --- |
| S1 | block-triangularity of the VdP augmented RHS (phase/action does not read φ) | `PROVED WITH STATED HYPOTHESES` (explicit from the defining equations + numeric check) |
| S2 | `r_phase ≤ r_unsplit` (the split never widens the main-wire tube) | `STANDARD CONSEQUENCE` (max over subset ≤ max over set; made meaningful by S1) |
| S3 | split-tube = HTWR "main wire + fanout-auxiliary wire" decomposition | `STRUCTURAL PROPOSAL` (interpretive reading, not a theorem) |
| S4 | term-by-term reduction "weak" on the periodic orbit, "strong" during shooting | `COMPUTATIONALLY VERIFIED EXAMPLE` (finite RK4 sampling, not a general theorem) |

**Boundary**: this note formalises the **mechanism** (block-triangularity + the radius inequality + the HTWR reading), **not** the optimality of the split-tube, nor a claim that "the variational RHS always exceeds the phase RHS" (S4 makes explicit that this is data-dependent). OQ-103.4 is thereby advanced from `OPEN` to "formalised + weak reduction confirmed" (see [governance/08-open-questions.md](../../governance/08-open-questions.md) OQ-103.4).

## VI. Relation to existing governance

This note does not modify Axioms I–IV, does not modify any paper body, and does not promote any existing claim. It lands OQ-103.4's "formalisation + term-by-term check" as a reproducible witness ([006-split-tube-witness.py](006-split-tube-witness.py)), and registers it in [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9. Research direction: Mingli Yuan; this formalisation, witness, and status labelling: DeepSeekHarness, 2026-11-14.
