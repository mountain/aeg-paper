# Fanout Cost and Interval Wrapping: an Interval-Arithmetic Reading of the HTWR Transverse Catalytic Flux (Level C witness)

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part IV: Level C — reading the HTWR core's "fanout cost / transverse catalytic flux" as the dependency-inflation (wrapping) cost of interval arithmetic).
> **Prerequisites**: Note I, *The HTWR Core*, Axioms I–IV ([001-htwr-core.md](001-htwr-core.md)); Note II, *The Exact Spacetime Pareto Frontier* ([002-htwr-example.md](002-htwr-example.md)).
> **Date**: 2026-11-14
> **Runnable witness**: [005-fanout-wrapping-witness.py](005-fanout-wrapping-witness.py) (Python stdlib `fractions.Fraction`, **exact rational arithmetic, no floats, no rounding**).
> **aeglib witness** (2026-11-14): [aeglib/python/examples/level_c_fanout_wrapping.py](../../../aeglib/python/examples/level_c_fanout_wrapping.py) (reproduces the same "fanout → wrapping" phenomenon on aeglib 0.0.2's `ArbBall`, the interval type used for VdP C11 certification).

---

## I. The problem

Note II §II gives a precise geometric fact: the Pell doubling map `k(x_n) = x_{2n} = (x_n² + 2)/(2x_n)` has two **semantically equal** but **worldsheet-metrically different** expressions:

| form | expression | Δ fan-outs | cross-section | peak transverse catalytic flux Σ_aux |
| --- | --- | ---: | --- | ---: |
| naive | `(x² + 2)/(2x)` | 2 | `(x, x, x)` | `3I_*/2` |
| Heron (partial fraction) | `(x + 2/x)/2` | 1 | `(x, 2/x)` | `I_*` |

Question: can this "difference in fanout count" be reproduced **exactly** in interval arithmetic as a **difference in wrapping width**? If so, the HTWR "fanout cost `c_Δ` / transverse catalytic flux `Σ_aux`" acquires an arithmetic witness independent of the worldsheet picture, and connects directly to the hardest blocker of VdP C11 certification — the **dependency inflation** of interval/affine Taylor tubes ([aeglib docs 17 §10–12](../../../aeglib/docs/17-vdp-c11-certification.md), [18](../../../aeglib/docs/18-vdp-tube-replay-audit.md), [19](../../../aeglib/docs/19-c11-independent-review.md)).

## II. Status labels

Following the authoritative labels of [governance/05-mathematical-status.md](../../governance/05-mathematical-status.md):

- identity `k_naive = k_Heron` (partial-fraction decomposition): `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`.
- interval-wrapping monotonicity (more fanouts → wider wrapping): `COMPUTATIONALLY VERIFIED EXAMPLE` (finite-δ exact verification + exact δ→0 leading coefficient).
- the general "fanout cost = wrapping" correspondence (interval-width ↔ information-height): `STRUCTURAL PROPOSAL`, `OPEN PROBLEM`.

Per AGENTS.md: the HTWR Axioms I–IV are themselves `STRUCTURAL PROPOSAL`; the "wrapping witness" of this note is an independent arithmetic fact **outside** the axiomatic framework, but its **correspondence** to the HTWR is a structural proposal, not a theorem.

## III. Exact computation

Let `c = x_4 = 17/12`, `c² = 289/144`. Take `δ < √2 − 17/12 ≈ 0.002453`, ensuring `k` is monotone increasing on `[c−δ, c+δ]` (`k'(x) = (x²−2)/(2x²) > 0`), so the true-image width is exactly `W_true = k(c+δ) − k(c−δ)`.

Using exact rational interval arithmetic (`±×÷` closed on rational endpoints), compute three widths:

| δ | `W_true` | `W_naive` | `W_heron` |
| ---: | ---: | ---: | ---: |
| `1/10³` | `62491/18062491000` | `72187509/18062491000` | `36062491/18062491000` |
| `1/10⁴` | `6249991/18062499910000` | `379934211/950657890000` | `3606249991/18062499910000` |
| `1/10⁵` | `624999991/18062499999100000` | `721875000009/18062499999100000` | `360624999991/18062499999100000` |

**Conclusion (exact)**:

1. Both forms are exactly equal at the centre: `k_naive(17/12) = k_Heron(17/12) = 577/408`.
2. For every small δ: `W_true < W_heron < W_naive`.
3. δ→0 leading terms (exact rationals):
   - `W_true/δ = 1 − 2/c² = 1/289`;
   - `W_heron/δ = 1 + 2/c² = 577/289`;
   - `W_naive/δ = 3 + 2/c² = 1155/289`.
4. Hence the wrapping excess (width − true-image width):
   - `excess_heron/δ = 4/c² = 576/289`;
   - `excess_naive/δ = 2 + 4/c² = 1154/289`;
   - **`excess_naive / excess_heron = (c²+2)/2 = 577/288 ≈ 2.0035`**.

## IV. Interpretation: why this is "fanout cost"

In the naive form `x` occurs **3 times** (twice in `x·x`, once in `2x`) = 2 Δ fan-outs; in the Heron form `x` occurs **2 times** (`x` and `2/x`) = 1 Δ fan-out. In interval arithmetic, "variable reuse" is precisely "fan-out": each fanned-out copy is treated as an **independent** interval, losing the correlation and producing wrapping width. Hence the wrapping excess grows **monotonically** with the fanout count — the arithmetic shadow of the HTWR decision to make Δ a "generator carrying positive action cost" (Axiom II.3).

**Precision (do not mislead)**: the wrapping excess here is **first-order** (∝ δ), not second-order. Its leading coefficient is monotone in the fanout count, but is **not** a simple multiple of the fanout count — `excess_naive/excess_heron = 577/288`, not exactly `2`. The reason is that the fanout **location** (numerator vs denominator vs mixed) affects the coefficient. So the safe assertion is the **monotone correspondence** (more fanout → more wrapping), not a "wrapping ∝ fanout" linear law; the latter needs extra structural hypotheses and is open.

## V. Connection to VdP C11 (the real target of Level C)

In the VdP variational equation `Φ' = J(x,y)Φ`, the state `(x,y)` is fanned out into the four entries of the Jacobian `J` **and** into the propagation of `Φ` itself; this is the arithmetic source of the "dependency inflation / wrapping" recorded in [docs 17/18/19](../../../aeglib/docs/17-vdp-c11-certification.md). The manual **split-tube** of doc 17 §12 (phase/action vs variational φ) is, in HTWR language, **separating the main carrier wire from the fanout-auxiliary wires**: phase/action is the "main wire", the variational φ is the "fanout-auxiliary wire", and only after separating them does the main wire stop being charged twice.

The Pell witness of this note is the **minimal toy version** of that chain: it proves "same value, different expression → different fanout → different wrapping" can be reproduced **exactly-rationally** (not in floats, not by analogy), reducing Level C from a conceptual bridge to a **reproducible arithmetic fact**. 2026-11-14: the same witness was ported to aeglib 0.0.2 (`aeglib/python/examples/level_c_fanout_wrapping.py`) using `ArbBall` (the very interval type of VdP C11 certification), reproducing `width_naive > width_heron` (ratio ≈ 2.002, consistent with the exact-rational leading term); the `fractions` part verifies the centre identity `577/408`. But the state-space gap remains: the HTWR `I(u) = ln max(|p|,|q|)` is a rational **size** (Weil height), whereas the VdP wrapping width is a real **interval width**. The correspondence "interval-width ↔ information-height" is not yet established — the core open item of Level C (see §VI W4).

## VI. Status table and open problems

| ID | conclusion | status | note |
| --- | --- | --- | --- |
| W1 | `k_naive = k_Heron` (partial-fraction identity) | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | classical; verified exactly here |
| W2 | `W_true < W_heron < W_naive`, excess monotone in fanout | `COMPUTATIONALLY VERIFIED EXAMPLE` | finite δ + exact δ→0 leading term |
| W3 | `excess_naive/excess_heron = 577/288` (at `c=17/12`) | `COMPUTATIONALLY VERIFIED EXAMPLE` | exact rational; not a simple multiple of fanout |
| W4 | "fanout cost = wrapping", interval-width ↔ information-height | `STRUCTURAL PROPOSAL` / `OPEN PROBLEM` | state-space gap unfilled |

**Open problems**:

1. **(open)** establish the exact `interval-width ↔ information-height` correspondence: can the HTWR `I(u)` (logarithmic Weil height) be replaced by a precision log `log(1/width)`, so that `c_Δ = α·I(u)` becomes the leading wrapping coefficient? This decides whether Level C is a "monotone correspondence" or a "quantitative law".
2. **(open)** derive from HTWR Theorem 1 (spacetime-uncertainty lower bound) a "certify-to-precision-ε tube-width / work lower bound". Currently only the Pell monotone witness exists; a VdP wrapping lower bound is `STRUCTURAL PROPOSAL`, the fiberwise proof not yet done (per AGENTS.md, computational lower bounds must not be inferred from geometric growth alone).
3. **(open)** formalise doc 17 §12's split-tube as the HTWR "main wire + fanout-auxiliary wire" decomposition, and check whether it reduces the wrapping of `Φ'=JΦ` term by term.

## VII. Relation to existing governance

This note does not modify Axioms I–IV, does not modify any paper body, and does not promote any existing claim status. It lands Note II §II's "different fanout" independently as an exact arithmetic witness, and registers the Level-C open items in [governance/08-open-questions.md](../../governance/08-open-questions.md) (OQ-103) and [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9. Research direction: Mingli Yuan; this witness, status labelling, and open items: DeepSeekHarness, 2026-11-14.
