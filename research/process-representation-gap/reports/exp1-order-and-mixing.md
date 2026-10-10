# exp1 — 顺序与混合作用 (order and mixing)

Work plan: `AEG-process-representation-work-plan.md` section 6, 实验一; shared frozen
template in section 5; gap classification in section 9.

Contract: `contracts/exp1-order-and-mixing.v1.json`, sha256
`d1ab186a2fefc0f803e293a0742a03c2fa96f89ca8eae266cef1c24de81d8c77`, frozen in
`contracts/FROZEN.sha256` before the implementation was written. The primary
implementation re-reads and re-hashes it and raises `EXP-CONTRACT-DRIFT` on any
mismatch.

## 1. The question

Do the same endpoint, the same action count, or the same single-action spectral
summary preserve order and mixing?

## 2. Frozen contract in one page

| Field | Declaration |
|---|---|
| native object (Instance N) | a two-vessel exact-rational mixing plant; the literal ordered history is carried by `process_geometry.process.history.ProcessWord` from the pinned checkout `/Users/mingli/AEG/process-geometry/src/process_geometry/process/history.py`, sha256 `93e9dc46…2cc45`, git blob `0d1f1895744fb87d1fbed141cc20c1812bb1dfac`, commit `c47c96fa7912…` (a drift raises `EXP1-PG-DRIFT`) |
| state | `(u, v)`, exact rational contents of vessels U and V, `0 <= u, v <= 1`; initial state `(1, 1)` |
| actions | total, no legality restriction, no INVALID outcome: `P(u,v)`: `t = min(u/2, 1-v)`, successor `(u/2, v+t)`, spilled `u/2 - t`; `R(u,v)`: `t = min(v/2, 1-u)`, successor `(u+t, v/2)`, spilled `v/2 - t` |
| task Q | the mixing task: report the mixture state `(u, v)` at the endpoint of the history and after every action of every continuation in `M_C` (depth ≤ 3, 15 continuations); non-adaptive |
| secondary task | `Q_prov`: report the transferred and spilled volume of every step; used only to compare enhancement candidates |
| existing summary `pi0` | `(count_P, count_R, u)` — endpoint readout plus action counts; declared variants `pi0_counts` and `pi0_endpoint` |
| bounded enhancements | ordered word; finite mixing-response table (probe families `{P,R}`, depth 2, depth 3); provenance/incidence relation |
| upper-bound control | full literal history with occurrence identity, explicitly **not** a recommended repair |
| budget | native: all 127 words of length ≤ 6 (1,2,4,8,16,32,64); continuations depth ≤ 3 (15); downstream: all 31 words of length ≤ 4 |
| outcomes | success / expected_negative / implementation_error / budget_exhausted / unknown, kept distinct |
| rewrites | allowed: append one action; ProcessWord notation; the vessel-swap relabelling. Forbidden: commuting `P` and `R`, removing the capacity bound inside Instance N, identifying occurrences, treating the plant as linear |

Instance D (declared **downstream observation only**) is the linear case: `A = [[1,1],[0,2]]`,
`B = [[0,2],[-1,3]]`, both invertible with `det = 2`, both with characteristic polynomial
`t² − 3t + 2`; matrices act on row vectors on the right, so the composite of a word is the
matrix product in word order; the frozen vector is `v = (2, 1)`.

## 3. Exact headline results

1. **The declared summary is insufficient — bounded-domain-compatible, all 127 native
   words of length ≤ 6 and continuations of depth ≤ 3.** `pi0` has 95 classes on the
   domain (49 distinct reachable states) and 46 pairs that share the summary while
   reaching different states. It does not refine the task equivalence: its kernel merges
   two task-inequivalent histories.
2. **The witness pair is `PRR` versus `RPR`**, both with counts `(1, 2)` and
   `pi0 = (1, 2, 1)`, reaching `(1, 1/4)` versus `(1, 1/2)`. Proved for these two words by
   exact arithmetic; the minimality statement is bounded-domain.
3. **The same action count alone is insufficient**: `PR` and `RP` both have counts
   `(1, 1)` and reach `(1, 1/2)` versus `(1/2, 1)`. **The endpoint readout alone is
   insufficient**: the empty word and `R` both have `u = 1` and reach `(1, 1)` versus
   `(1, 1/2)`.
4. **The chosen spectral summary is insufficient — proved.** `σ(A) = σ(B) = (3, 2)` yet
   `v·A = (2, 4)` and `v·B = (-1, 7)`. For the two-action words, `σ(AB) = σ(BA) = (5, 4)`,
   both composites have characteristic polynomial `t² − 5t + 4`, and `BA = A⁻¹(AB)A`, so
   **every conjugation invariant of the composite agrees**; yet `v·AB = (-4, 16)` and
   `v·BA = (-1, 13)`. The commutator `A⁻¹B⁻¹AB = [[3/4,1/4],[-1/4,5/4]] ≠ I`.
5. **On the declared downstream domain the spectral summary is only a re-encoding of the
   word length**: `σ(w) = (2^|w| + 1, 2^|w|)` — lengths 0…4 give `(2,1) (3,2) (5,4) (9,8)
   (17,16)`; a labelled exploratory range extends this to lengths 5 and 6
   (`(33,32)`, `(65,64)`) and is excluded from every verdict. The determinant part is
   proved by multiplicativity; the trace part is not proved in general. Consequently the
   declared spectral summary carries exactly as much information as the action count, and
   no more.
6. **Minimality (bounded-domain-compatible).** Exhaustive enumeration of all 8001 pairs of
   the declared domain: the minimal `pi0`-colliding, task-separated pair is
   `(PRR, RPR)` with maximum length 3 and total length 6; **no such pair exists with both
   words of length ≤ 2** (0 pairs), and there are 46 gap pairs in total.
7. **Non-linearity is load-bearing — proved-with-stated-hypotheses.** In the separately
   declared uncapped variant (`P(u,v) = (u/2, v+u/2)`, `R(u,v) = (u+v/2, v/2)`) total
   volume is invariant, so `v = 2 − u` and the endpoint readout determines the state:
   0 summary collisions with distinct states on the declared domain. The declared witness
   therefore depends on the capacity bound: `PRR` spills 1/4 and ends at total `5/4`
   against the initial `2`. The declared actions are also **not injective** on the 49
   reachable states (distinct states `(1/4,7/8)` and `(1/4,1)` both map to `(1/8,1)`
   under `P`), so the instance is not a group action and is not a linearisation.
8. **Minimal repair (bounded-domain-compatible).** The two-probe mixing-response pair is
   sufficient and **equal to the task equivalence**: 49 classes on the domain, exactly the
   49 reachable states, with the declared closed update (recover the state by
   `u = 2·(response to P).u`, `v = 2·(response to R).v`, apply the pour law, re-probe).
   The recovery law was verified on all 127 histories.
9. **Over-refinement is real**: the ordered word and the provenance relation are also
   sufficient but strictly finer than the task (127 classes against 49): they separate
   histories the declared task declares equivalent.

## 4. Witnesses with concrete values

**Minimal counterexample** — `PRR` and `RPR`, same declared summary `(1, 2, 1)`:

| word | transfers and spills | state | total |
|---|---|---|---|
| `PRR` | `P: 0 / spill 1/2`, `R: 1/2 / spill 0`, `R: 0 / spill 1/4` | `(1, 1/4)` | `5/4` |
| `RPR` | `R: 0 / spill 1/2`, `P: 1/2 / spill 0`, `R: 1/2 / spill 0` | `(1, 1/2)` | `3/2` |

Separated at depth 0 (the endpoint readout is an observation point of the task) and also
by both depth-1 probes: `P` gives `(1/2, 3/4)` versus `(1/2, 1)`, `R` gives `(1, 1/8)`
versus `(1, 1/4)`.

**Positive control (required by the plan)** — `PPRR` and `RPRR`: different literal
histories of the same length, both with counts `(2, 2)` and summary `(2, 2, 1)`, both
reaching `(1, 1/4)`, hence genuinely indistinguishable under the whole frozen continuation
family. Without this control, any syntactic difference would look like a gap; here an
enhancement that separated them would be over-refined.

**Secondary control** — `PR` and `RPR` have *different* summaries (`(1, 1, 1)` against
`(1, 2, 1)`) yet both reach `(1, 1/2)` and are task-equivalent: summary inequality is not a
semantic difference either.

**Downstream witness** — `A = [[1,1],[0,2]]`, `B = [[0,2],[-1,3]]`, `v = (2, 1)`;
path for the word `AB`: `(2,1) → (2,4) → (−4,16)`; path for `BA`: `(2,1) → (−1,7) →
(−1,13)`. `AB = [[-1,5],[-2,6]]`, `BA = [[0,4],[-1,5]]`, both trace 5, determinant 4,
polynomial `t² − 5t + 4`.

## 5. The gap and its exact scope

The gap is **summary versus state**: the declared summary either merges two
task-inequivalent histories (`pi0`, `pi0_counts`, `pi0_endpoint`) or is blind to the
composite order (`σ`). It is not a claim that no summary works — the two-probe
mixing-response pair works, exactly and cheaply, on the declared domain. In the
downstream instance the failure is sharper: `AB` and `BA` are *conjugate*, so **no**
conjugation-invariant function of the composite, spectral or otherwise, can separate
them, while the declared observation separates them.

Scope: 127 native words of length ≤ 6, continuations of depth ≤ 3, 31 downstream words of
length ≤ 4, exact rational arithmetic only. No statement is made about longer words, other
plants, other spectra, or other observation tasks.

## 6. Independent route and its agreement

`experiments/exp1_order_and_mixing_independent.py` shares no semantic helper with the
primary; it imports only `gapkit` (canonical JSON, diagnostics, hashing) and reads the
primary evidence as data. It recomputes everything by different algorithms:

* the plant by an explicit **flux ledger** — the state is never carried forward, it is
  reconstructed from the recorded transferred/spilled volumes at each step, and the
  capacity branch uses a cross-multiplied comparison instead of `min`;
* the summaries from that ledger, with sufficiency decided by a **partition criterion**
  (every summary class inside one task class) instead of by searching continuations;
* the linear instance by **basis images** only — maps are composed by applying one map to
  the images of the other, so no two matrices are multiplied; characteristic polynomials
  are checked through the Cayley–Hamilton relation and the inverse by exact Gaussian
  elimination;
* hand-computed literal tables of plant states, spectra and frozen-vector actions.

Result: **163 of 163 compared fields agree, 0 disagreements** (including every
representation's class counts, colliding fibres, largest colliding fibre, sufficiency,
refinement, closed-update verdict, witness pairs, storage channels, the minimality data,
the reserved verification family, and the exploratory length law). The independent checker
raises `EXP1-ROUTE-DISAGREEMENT` whenever any compared field differs; its own control
demonstrates that this comparison is sensitive.

Two development-time disagreements were reported by this route and are recorded here
rather than hidden: (i) `largest_fiber` was computed over all classes in one route and over
colliding classes only in the other, and (ii) the provenance update in the independent
route rebuilt the record list from a different representative word instead of appending
the new record. Both were definitional/implementation artifacts; the underlying
mathematics never disagreed, and the definitions were fixed and documented. The
independent route also recomputes the storage channels (`mean`, `max` bytes per history)
from its own payloads; the declared `computation_steps`, `observations` and
`verification_cost` are accounting rules of the declared construction and are explicitly
**not** independently re-derived.

## 7. Negative-control table

Primary implementation (`EXP1-*`), each control body fails as required:

| id | expected diagnostic | observed |
|---|---|---|
| `contract-drift` | `EXP-CONTRACT-DRIFT` | `EXP-CONTRACT-DRIFT` |
| `pinned-processword-drift` | `EXP1-PG-DRIFT` | `EXP1-PG-DRIFT` |
| `hand-table-mutated` | `EXP1-HAND-TABLE-MISMATCH` | `EXP1-HAND-TABLE-MISMATCH` |
| `summary-collision-claim` | `EXP1-SUMMARY-COLLISION-MISSING` | `EXP1-SUMMARY-COLLISION-MISSING` |
| `pi0-sufficiency-claim` | `EXP1-SUMMARY-SUFFICIENCY-REFUTED` | `EXP1-SUMMARY-SUFFICIENCY-REFUTED` |
| `spectral-separation-claim` | `EXP1-SPECTRAL-SEPARATION-MISSING` | `EXP1-SPECTRAL-SEPARATION-MISSING` |
| `spectral-sufficiency-claim` | `EXP1-SPECTRAL-SUFFICIENCY-REFUTED` | `EXP1-SPECTRAL-SUFFICIENCY-REFUTED` |
| `uncapped-collision-claim` | `EXP1-CONSERVATION-CLAIM-REFUTED` | `EXP1-CONSERVATION-CLAIM-REFUTED` |
| `positive-control-claim` | `EXP1-POSITIVE-CONTROL-REFUTED` | `EXP1-POSITIVE-CONTROL-REFUTED` |
| `minimality-claim` | `EXP1-MINIMALITY-REFUTED` | `EXP1-MINIMALITY-REFUTED` |
| `plant-injectivity-claim` | `EXP1-PLANT-INJECTIVITY-CLAIM-REFUTED` | `EXP1-PLANT-INJECTIVITY-CLAIM-REFUTED` |
| `response-recovery-mutation` | `EXP1-RESPONSE-RECOVERY-FAILED` | `EXP1-RESPONSE-RECOVERY-FAILED` |
| `primary-independent-disagreement` | `EXP1-ROUTE-DISAGREEMENT` | `EXP1-ROUTE-DISAGREEMENT` |
| `enumerated-count-mismatch` | `EXP1-ENUMERATION-MISMATCH` | `EXP1-ENUMERATION-MISMATCH` |

Independent route: `oracle-drift` → `EXP1I-PIN-DRIFT`, `hand-table-mutated` →
`EXP1I-HAND-TABLE-MISMATCH`, `route-disagreement-detected` → `EXP1-ROUTE-DISAGREEMENT`
(all observed as declared). No control passes silently; a control that passed would raise
`GAPKIT-NO-DIAGNOSTIC` or `GAPKIT-WRONG-DIAGNOSTIC` and fail the run.

## 8. Costs (declared domain: 127 native words, 15 continuations)

| candidate | tier | storage bytes (mean / max) | structural size | steps | observations | verification | sufficient | closed update | refinement |
|---|---|---|---|---|---|---|---|---|---|
| `pi0` counts+endpoint | existing | `2774/127` ≈ 21.84 / 24 | 762 | 127 | 6350 | 1905 | **no** | **no** | does not refine task |
| `pi0_counts` | existing | 13 / 13 | 508 | 127 | 6223 | 1905 | **no** | yes | does not refine task |
| `pi0_endpoint` | existing | `1504/127` ≈ 11.84 / 14 | 254 | 127 | 6350 | 1905 | **no** | **no** | does not refine task |
| `pi1_word` ordered word | enhancement | `4875/127` ≈ 38.39 / 45 | 1284 | 769 | 6865 | 1905 | yes | yes | strictly finer (127 classes) |
| `pi2_resp` response pair | enhancement | `8089/127` ≈ 63.69 / 71 | 1270 | 254 | 6477 | 1905 | yes | yes | **equal to task (49)** |
| `pi2_resp_d2` (7 probes) | enhancement | `27643/127` ≈ 217.7 / 248 | 4445 | 889 | 7112 | 1905 | yes | yes | equal to task |
| `pi2_resp_d3` (15 probes) | enhancement | `60031/127` ≈ 472.7 / 539 | 9525 | 1905 | 8128 | 1905 | yes | yes | equal to task |
| `pi3_prov` provenance | enhancement | `28727/127` ≈ 226.2 / 272 | 5778 | 1411 | 7507 | 1905 | yes | yes | strictly finer (127 classes) |
| `hist` full history | upper-bound control | `15789/127` ≈ 124.3 / 147 | 3210 | 1284 | 7507 | 1905 | yes | yes | strictly finer (127 classes) |
| `pi_spectral` (downstream, 31 words) | existing | `559/31` ≈ 18.03 / 19 | 124 | 98 | 0 | 31 | **no** | yes (length law) | does not refine task (5 classes vs 31) |

Which task each candidate improves, and where it fails:

| candidate | improves | still fails |
|---|---|---|
| `pi0`, `pi0_counts`, `pi0_endpoint` | nothing on the declared tasks | fail `Q_mix` (witness above) and `Q_prov` (witnesses recorded, e.g. `PPRRRR`/`PRPRRR`) |
| `pi1_word` ordered word | answers `Q_mix` and `Q_prov` (replay, `\|w\|` steps) | fails no declared task; it is strictly finer than `Q_mix` (over-refined) and is budget-exhausted beyond length 6; its structural size grows with the history |
| `pi2_resp` (2 probes) | cheapest **information** repair: exactly the task equivalence, constant structural size, closed update | fails `Q_prov`: the mixture state does not determine the past (witness `PP`/`RPP`); on this small domain its byte cost is higher than the plain word because every payload carries four exact rationals |
| `pi2_resp_d2`/`d3` | same sufficiency with deeper probe families | same `Q_prov` failure at 7×/15× the storage; no sufficiency gain (the 2-probe pair already recovers the state) |
| `pi3_prov` provenance | `Q_prov` in one record lookup, no replay; answers `Q_mix` | over-refined for `Q_mix` and the most expensive per step |
| `hist` | nothing beyond `pi1_word` on the declared tasks | upper-bound control only; unbounded and over-refined, **not** a recommended repair |

Minimal repair, stated with its trade-off: the *coarsest sufficient* summary on the
declared domain is the mixture state itself, realized by the two-probe response pair
(equal to the task equivalence, 49 classes). Measured bytes do not force a unique winner
at this small size — the ordered word is smaller per history (`38.39` against `63.69`
bytes mean) because its payload grows by one symbol per step while the response payload
always carries four exact rationals whose dyadic denominators grow — so the recommendation
is argued from information (equal to the task, not finer) and from the growth of the
structural size, not from a single byte number.

## 9. Status of every result

`proved`: the witness pair's values; the spectral blindness of `AB` versus `BA` (conjugacy
argument); the equality of the two single-action spectra with different frozen-vector
actions. `proved-with-stated-hypotheses`: the uncapped variant's conservation and hence its
lack of a gap. `computationally-verified-example`: counts-only and endpoint-only failure;
non-injectivity of the actions. `bounded-domain-compatible`: the sufficiency and
minimality verdicts, the minimal repair, the over-refinement statement, the spectral
length law. `open`: everything listed below. Every claim is registered with its status in
`evidence.exp1.claims`.

## 10. What is explicitly NOT claimed

* The declared spectral summary is what fails. No claim is made that richer spectral
  systems, or any spectral system outside 2×2 rational matrices with this observation,
  are insufficient.
* No general theorem is inferred from the finite enumeration: not for words longer than 6,
  not for other plants, not for other summaries.
* The trace law `trace = 2^n + 1` is verified, not proved.
* No claim that the plant action semigroup admits no linear representation; only that the
  actions are non-injective and that nothing here is derived from a linearisation.
* No claim that the plant is native Adva execution or a faithful process-geometry process;
  the pinned `ProcessWord` is used only as the carrier of the literal ordered history.
* No claim that order/mixing is unrecoverable in general — a two-rational response pair
  recovers it exactly on the declared domain.
* `hist` is an upper-bound control, not a recommended repair.
* The declared `pi0` uses a scalar endpoint readout because the PR-16 snapshot policy
  does; the experiment does not assume a finite observer must be scalar or finite-state.

## 11. Open items

1. Whether any richer spectral or operator-level system is sufficient for the declared
   observation task (the experiment only refutes the chosen summary).
2. A plant whose own readout is strictly coarser than its state: a finite mixing-response
   table could then be sufficient without determining the state — a genuinely different
   bounded-domain-compatible result. Not declared in this contract version.
3. A general proof of `trace(composite of n actions) = 2^n + 1` on the downstream
   alphabet, and a structural reason for it.
4. Whether a linear representation of the declared plant action semigroup exists at all.
5. Adaptive selection of the next observation is out of scope for version 1.
6. Beyond the declared length budget nothing is decided; longer words are
   `budget-exhausted`, not negative results.

## 12. Reproduction

```
python3 research/process-representation-gap/experiments/exp1_order_and_mixing.py > /tmp/exp1.json
cmp /tmp/exp1.json research/process-representation-gap/evidence/exp1-order-and-mixing.json
python3 -O research/process-representation-gap/experiments/exp1_order_and_mixing.py > /tmp/exp1-O.json
cmp /tmp/exp1.json /tmp/exp1-O.json
python3 research/process-representation-gap/experiments/exp1_order_and_mixing_independent.py
python3 research/process-representation-gap/experiments/exp1_order_and_mixing_independent.py --out research/process-representation-gap/evidence/exp1-order-and-mixing-independent.json
python3 research/process-representation-gap/tools/freeze_contracts.py
```

Both programs were verified byte-identical under `python3` and `python3 -O` with `cmp`.
No `assert` is used anywhere: every obligation is `gapkit.require(condition, "CODE", …)`.
No floating point appears in any witness, comparison or cost — `0.1` occurs nowhere in
either program.
