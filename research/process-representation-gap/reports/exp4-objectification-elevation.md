# Experiment 4 — objectification and elevation (对象化与升阶)

Contract: `research/process-representation-gap/contracts/exp4-objectification-elevation.v1.json`
(sha256 `a092fcd470d5cee5a750bb47f73ef9065ab71a69f2460f99ba60dca37658bed6`, frozen before implementation).
Evidence: `evidence/exp4-objectification-elevation.json`,
`evidence/exp4-objectification-elevation-independent.json`.
Plan reference: `AEG-process-representation-work-plan.md` §6 实验四, §4.4, §5, §7, §9.

## 1. The question

Is equality of a **single evaluation** enough to form a stable object? And is a stable
object enough to form a **higher-order computation**? Both halves are answered on three
exact declared models:

* **baseline control** — the pinned addition→multiplication rank transition of
  `mountain/process-geometry` at commit `c47c96fa79123c677172278be59d67ca1cc891b1`
  (`docs/51-…`, `docs/44 §7–§8`, `tests/research/test_aeg_addition_multiplication_rank_transition.py`,
  `src/process_geometry/process/history.py`);
* **attempt 2** — objectify the experiment‑2 loop/accumulator structure;
* **attempt 5** — objectify the experiment‑5 crossing process onto `Aut(F_3)`.

No `Objectification`, `ProcessRank`, `RankLowering` or generic rank API is written or
proposed: the pinned package deliberately omits them and the plan forbids building one.

## 2. Declared convention (the composition-order trap)

| clause | declaration |
|---|---|
| word order | `(g₁,…,gₙ)` is chronological: `g₁` acts first (this is `ProcessWord` order) |
| algebraic juxtaposition | `XY` applies `Y` first, then `X`; this is why the note computes `D_k T_a` as `k(x+a)` |
| dictionary (quoted from the pinned essay) | "the chronological word `(T_a, D_k)` denotes the algebraic composite `D_k T_a`, while `(D_k, T_ka)` denotes `T_ka D_k`" |
| pair | `(b,k)` means `x ↦ k·x + b`; declared product `(b,k)*(c,l) = (b + k·c, k·l)` (right factor acts first) |
| consequence | `pair(w ++ (g,)) = pair(g) * pair(w)`; chronologically appending multiplies in **reverse** algebraic order |

The trap is real and is a negative control: on `D_2 T_1` then `T_3` the chronological
product is `(7,2)` while the declared product is `(4,2)`. For the braid attempt the same
trap appears: the pinned law `Φ(w·σ) = Φ(w)∘φ_σ` equals `O(reverse(w))` in this file's
chronological convention — verified on all 341 words of length ≤ 4 (`EXP4-CONVENTION-DICTIONARY`).

## 3. Headline results (exact numbers)

Sweep: all **3906** words of length ≤ 5 over `{T_-2, T_1, T_3, D_2, D_3}` (1,5,25,125,625,3125 per length), declared states `{-3,-1,0,2,5}`.

| Check | Count | Result |
|---|---|---|
| `T_a T_b = T_(a+b)`, `a,b ∈ [-6,6]` | 169 | all equal |
| `D_k D_l = D_(k·l)`, `k,l ∈ [1,6]` | 36 | all equal |
| `D_k T_a = T_(ka) D_k`, `a ∈ [-6,6]`, `k ∈ [1,6]` | 78 | both sides `= (ka,k)`, all equal |
| `pair(w ++ (g,)) = pair(g)*pair(w)` (induction step) | 19530 | all equal |
| `pair(w1 ++ w2) = pair(w2)*pair(w1)` (all splits, |w| ≤ 4) | 3711 | all equal |
| `lower(star(P,Q),x) = lower(P,lower(Q,x))` | 3125 | all equal |
| associativity of `*` on the depth‑2 reachable layer (25 objects) | 15625 | all equal |
| **gate (iii) descent**: object-layer composite then lower vs bottom step-by-step | **19530** | **0 mismatches** |
| gate (ii) closed update (same object ⇒ same successor, per generator) | 19530 | all equal |

`*` is the declared product; `lower((b,k))(x) = kx+b`.

**Repetition vs objectification (§4.4 of the plan).** 78 schemas `(a,n)` with `a ∈ [-6,6]`,
`n ∈ [1,6]` produce only **37** distinct outputs. The fibre of `T_6` is
`{(1,6),(2,3),(3,2),(6,1)}` — the pinned `T_2³ = T_6 = T_3²` (and `(T_1)⁶`); the fibre of
`T_0` has 6 schemas. So **the output does not determine the schema**. The uniform
endomorphism `R_k : T_a ↦ T_{ka}` is an endomorphism of the translation family (1014 exact
checks), the 6 factors `k ∈ [1,6]` induce 6 pairwise different actions, and `R_2(T_1)=T_2 ≠ R_3(T_1)=T_3`.

**Growth of the object layer (bounded, deduplicated BFS).** Full sweep alphabet:
1, 6, 25, 83, 238, **626** objects at depths 0…5 versus **3906** words. Translation-only
alphabet `{T_-2,T_1}`: 1, 3, 6, 9, 12, **15** (linear in the length). This is the declared
complexity-advantage channel (docs/44 §7.7): the object layer needs 626 states where the
free word language has 3906 words.

**Experiment‑2 attempt.** Domains reproduced exactly: all words 364 (1,3,9,27,81,243),
legal words **115** (1,1,2,4,10,26,71 — the frozen experiment‑2 domain). `A(w)` equals the
object's value at 0 on all **479** declared words (`EXP4-EXP2-ACCUMULATOR-ACTION`); descent
checks 4790 (all words + legal words × 10 declared states), 0 mismatches. On the legal
domain the 115 words fall into **63** objects (**27** colliding fibres, largest 5).

**Experiment‑5 attempt.** Reproduced exactly: 5461 crossing words (1,4,16,64,256,1024,4096),
**1457** freely reduced classes, **577** Artin-object classes, **6** endpoint-permutation
classes; merges 4004 + 880 = **4884** words fused. The pinned probe collisions are
reproduced (`x1`: 101 collision groups, largest 13, 213 distinct signatures) and the
minimal separating subfamily is `{commutator}` (size 1, separating all 577 classes).
Descent: 1593 split checks + 2728 probe checks, 0 mismatches.

## 4. Witnesses with concrete values

1. **Single evaluation is not enough (minimal).** `epsilon` and `D_2` both evaluate to **0**
   at the declared initial state `x₀ = 0`; their objects are `(0,1)` and `(0,2)`, i.e.
   `x ↦ x` versus `x ↦ 2x`. At the declared states they give `[-3,-1,0,2,5]` versus
   `[-6,-2,0,4,10]`. Minimal witness with both words non‑empty: **`D_2` and `D_3`**
   (both `0` at `x₀`, objects `(0,2)` vs `(0,3)`). Over the sweep the summary has 107
   classes, 93 colliding fibres, largest fibre 252.
2. **Output does not determine the schema.** `T_2³ = T_3² = T_6 = (6,1)`; the fibre of
   `T_6` contains 4 schemas; the named object `T_2³` **is** the lower-layer translation
   `T_6` and therefore fails elevation criterion E1.
3. **Uniform action distinguishes what the output cannot.** `R_2(T_1) = T_2 = (2,1)` vs
   `R_3(T_1) = T_3 = (3,1)`; `R_k` is an endomorphism of the translation family.
4. **Descent counterexample for the wrong lowering.** Lowering `D_k` to `T_k` gives `(3,1)`
   on the word `D_2 T_1`; bottom execution gives `1` at state `0` → `EXP4-DESCENT-DISAGREEMENT`.
5. **Experiment‑2 gate (i) failure, inside experiment‑2's own legal domain.**
   `cvc` and `ccvcv` have the same object **`(2,2)`** (`x ↦ 2x+2`, accumulator `2` both), but
   the declared readout is `(3, 1, 2)` for `cvc` — the frozen PR‑16 triple — and
   `(5, 1, 12/5)` for `ccvcv`; minimal in-domain witness (total length 8).
   Legality-channel witness (`vc` vs `l`, both object `(1,1)`): legal signatures `[c,l]` vs `[c]`.
   Largest fibre (object `(3,2)`, 5 words): readouts `(3,1,9/4)`, `(5,1,12/5)`, `(5,1,5/2)`.
6. **Experiment‑5 history witness.** `s1 s2 s1` and `s2 s1 s2` share the object
   `(xyzy⁻¹x⁻¹, xyx⁻¹, x)` and the permutation `(2,1,0)` while their generator counts differ,
   `{s1:2, s2:1}` vs `{s1:1, s2:2}`. Second witness: `epsilon` and `s1 s1` share the
   permutation `(0,1,2)` but not the object.
7. **Hand-derived literal table** (contract `independent_check.hand_literal_tables`), derived
   here by hand with the declared rule `P ↦ pair(g)*P`:
   `(D_1,T_-4)→(-4,1)`; `(D_2,D_3)→(0,6)`; `(D_2,T_1)→(1,2)`; `(D_3,T_2,D_2)→(4,6)`
   [0,3 → 3x+2 → 6x+4]; `(D_3,T_6)→(6,3)`; `(T_-2,T_1)→(-1,1)`; `(T_0,D_5)→(0,5)`;
   `(T_1,D_2)→(2,2)` [2(x+1)]; `(T_2,D_3)→(6,3)` [3(x+2)]; `(T_2,T_2,T_2)→(6,1)`;
   `(T_3,D_2)→(6,2)` [2(x+3)]; `(T_3,T_3)→(6,1)`.
   Experiment‑2: `c=(1,2)`, `v=(0,1/2)`, `l=(1,1)`; `cc→(3,4)`; `cv→(1/2,1)`; `cvc→(2,2)`;
   `ccvcv→(2,2)` [`ccvcv`: (3,4) → (3/2,2) → (4,4) → (2,2)]; `vc→(1,1)`; `vv→(0,1/4)`.
   Experiment‑5: `O(s1)=(xyx⁻¹, x, z)`;
   `O(s1s2s1) = φ_{s1}∘φ_{s2}∘φ_{s1} = (xyzy⁻¹x⁻¹, xyx⁻¹, x)` — the `x` image is
   `(xyx⁻¹)·x·z·x⁻¹·(xyx⁻¹)⁻¹ = x y (x⁻¹x) z (x⁻¹x) y⁻¹x⁻¹ = xyzy⁻¹x⁻¹`, the `y` image is
   `φ_{s1}(x) = xyx⁻¹`, and the `z` image is `φ_{s1}(y) = x`.

## 5. Gate-by-gate verdict

Declared gates (frozen in the contract): (i) task sufficiency, (ii) stable/callable/composable
interface, (iii) exact descent. Declared elevation criterion: E1 generator novelty,
E2 strict inclusion, E3 uniformity, E4 generative novelty, E5 not-by-naming/caching/history.

| Model | gate (i) | gate (ii) | gate (iii) | elevation | label |
|---|---|---|---|---|---|
| baseline object layer `pi_obj` | **PASS** | **PASS** (19530) | **PASS** (19530, 0 mismatch) | **ELEVATION** (E1–E5 hold) | proved |
| baseline single evaluation `pi_out` | **FAIL** — witness `epsilon`/`D_2` | n/a (no closed update: a dilation has no image) | n/a | n/a | proved (counterexample) |
| experiment‑2 accumulator object | **FAIL** — `cvc`/`ccvcv`, `vc`/`l` | **PASS** (assoc 1728, update 1092) | **PASS** (4790, 0 mismatch) | **ELEVATION** (E1–E5 hold) | proved |
| experiment‑5 Artin object | **PASS** for the declared group-level task (Artin faithfulness, stated hypothesis); **FAIL** for a history-valued task (counts `{s1:2,s2:1}` vs `{s1:1,s2:2}`) | **PASS** (assoc 103823, update 21844) | **PASS** (1593 + 2728, 0 mismatch) | **NO ELEVATION** — E1, E2, E4 fail | proved / proved-with-stated-hypotheses |

**Answers.** (1) No — one equal evaluation does not determine the object (`epsilon` vs `D_2`),
so it cannot form one. (2) In the arithmetic calibration a stable object *is* enough for a
higher-order computation (`D_2*D_3 = (0,6)` is expressible at the object layer and nowhere in
the lower language), but this does not generalise: the experiment‑2 object is stable, elevated
and still fails gate (i); the experiment‑5 object passes all three gates and is **not** an
elevation at all — it is a quotient (5461 → 577 on the declared bound, surjective by
construction, so E1/E2/E4 fail). **A stable object is therefore neither sufficient nor
necessary for elevation, and neither property implies task sufficiency.**

## 6. Three comparison tiers (cost, per channel, no collapsing)

Base model over the 3906-word sweep (contract tier 1 = existing summary, tier 2 = pre-declared
bounded enhancement, tier 3 = full history / exact semantics):

| tier | storage bytes | fields | build steps | answer steps | observations | verification | answers task |
|---|---|---|---|---|---|---|---|
| `pi_out` (one integer) | 10418 | 3906 | 18555 | 3906 | 3906 | 3906 | **no** |
| `pi_obj` (pair `(b,k)`) | 54409 | 15624 | 18555 | 19530 | 19530 | 3906 | yes |
| `pi_hist` (literal word) | 109187 | 7812 | 18555 | 92775 | 19530 | 18555 | yes |

`structural_size` counts retained fields (2 per word for `pi_obj`, 1 for `pi_hist`) and does
**not** measure word length; the channels that grow with the history are `storage_bytes`
(109187 vs 54409) and `answer_steps` (92775 vs 19530). Mean storage: `5209/1953` (≈2.67 B),
`54409/3906` (≈13.9 B), `109187/3906` (≈27.9 B) per word; maxima 5, 17, 33 bytes.
Attempt costs: exp2 scalar 1772 B / object 6800 B / history 4924 B;
exp5 permutation 98298 B / Artin object 320614 B / literal 292179 B.

## 7. Independent route and its agreement

`experiments/exp4_objectification_elevation_independent.py` — **87 comparisons, all agreeing,
0 disagreements**. It shares no code with the primary (neither imports the other; the primary's
JSON is read as data only; the only shared module is `gapkit` serialisation):

* affine actions as exact 2×2 upper-triangular matrices `[[k,b],[0,1]]` over `Q` multiplied
  explicitly, versus the primary's pair formula `(b,k)*(c,l) = (b+kc,kl)`;
* object layer enumerated by **BFS with deduplication** instead of by word enumeration
  (all four alphabets reproduced, including the translation-only row 1,3,6,9,12,15);
* the contract's hand tables parsed and checked against this route (independent literal input);
* word counts recomputed combinatorially (`5^n`, `3^n`, `4^n`) rather than enumerated;
* the braid part: a **separate re-implementation** of the free-group model plus a genuinely
  different counting route (577 object classes counted by **probe signatures** rather than by
  automorphism-triple equality). The braid part is only a re-implementation, not a second
  algebra, and is labelled as such — its independence is weaker than the affine part's;
* a **detector self-test**: two manufactured disagreements (a mutated primary scalar and a
  mutated matrix product) both raise `EXP4-ROUTE-DISAGREEMENT`; the honest comparison passes.
  A checker that can never fail is not a checker.

Determinism: `python3 <primary> | cmp -` with the recorded evidence passes; `python3` and
`python3 -O` outputs are byte-identical for both scripts; `tools/check_determinism.py --only`
reports `identical_across_runs`, `identical_across_modes` and `matches_recorded_evidence` all
true for both.

## 8. Negative controls (each declares a code and actually raises it)

| id | expected code | observed code |
|---|---|---|
| contract-drift | EXP-CONTRACT-DRIFT | EXP-CONTRACT-DRIFT |
| endpoint-value-insufficiency | EXP4-SUMMARY-INSUFFICIENT | EXP4-SUMMARY-INSUFFICIENT |
| naive-dilation-lowering | EXP4-DESCENT-DISAGREEMENT | EXP4-DESCENT-DISAGREEMENT |
| composition-order-flip | EXP4-COMPOSITION-ORDER | EXP4-COMPOSITION-ORDER |
| cross-relation-without-scaling | EXP4-CROSS-RELATION | EXP4-CROSS-RELATION |
| dilation-domain-zero | EXP4-DILATION-DOMAIN | EXP4-DILATION-DOMAIN |
| matrix-route-disagreement | EXP4-ROUTE-DISAGREEMENT | EXP4-ROUTE-DISAGREEMENT |
| enumerated-count-mismatch | EXP4-ENUMERATION-MISMATCH | EXP4-ENUMERATION-MISMATCH |
| named-power-as-elevation | EXP4-NAMING-NOT-ELEVATION | EXP4-NAMING-NOT-ELEVATION |
| exp2-object-sufficiency | EXP4-EXP2-SUFFICIENCY-CLAIM | EXP4-EXP2-SUFFICIENCY-CLAIM |
| exp5-elevation-claim | EXP4-ELEVATION-NOT-ESTABLISHED | EXP4-ELEVATION-NOT-ESTABLISHED |
| hand-table-mutated | EXP4-HAND-TABLE-MISMATCH | EXP4-HAND-TABLE-MISMATCH |
| exp5-braid-relation-mutated | EXP4-RELATION-SOUNDNESS | EXP4-RELATION-SOUNDNESS |
| free-reduction-wrong | EXP4-REDUCTION-NOT-ADJACENT | EXP4-REDUCTION-NOT-ADJACENT |
| illegal-exp2-action | EXP4-ILLEGAL-ACTION | EXP4-ILLEGAL-ACTION |

Polarities are the "checker overclaims, so the `require` fails" form used by experiment 2: each
control body asserts the **false** claim (e.g. that the single evaluation separated
`T_2 D_3` from `T_3 D_2`, that `T_2³` lies outside the lower layer, that `cvc`/`ccvcv` are
separated) and must therefore raise its declared code. `D_0`, `D_-1`, `D_1/2` are additionally
refused directly by the constructor (`dilation_domain_refusals` in the evidence), and
`exp2_step((), "v")` is refused directly.

## 9. Scope boundary and what is NOT claimed

* The laws claimed as **proved** are proved by exact algebra, not by the sweep: `star` is
  composition of the lowered maps, the pair is determined by its values at 0 and 1
  (injectivity lemma, case-checked over the 25-object reachable set), and the fold is a left fold
  of `star`, so descent holds for **every** word over the alphabet and every integer state.
  The 19530/1593/2728 check sweeps are **calibrations**, not the proof.
* Everything counted per length, per reachable object, per layer, per merge and per probe is
  labelled **bounded-domain-compatible**; no closed-form growth law is claimed.
* No generic objectification/rank/lowering API is proposed or implemented; no repository file
  outside `research/process-representation-gap/` was touched.
* `k ∈ N_{>0}` only. `D_0`, negative and non-integer dilations are outside the declared domain
  and are not analysed.
* The experiment‑5 argument uses Artin's faithfulness as a **stated, cited hypothesis**
  (`proved-with-stated-hypotheses`); faithfulness is claimed only at the braid-element layer.
* The experiment‑5 quotient is **not** claimed useless: it is a decision-complete, composable
  stabilisation of literal histories (decidable equality by triple comparison, 577 classes for
  5461 words) — a compression and a cost benefit, not an elevation.
* No unbounded recursion, no adaptive observation, no spectrum/matrix claim (the 2×2 matrices
  are only an exact encoding of the affine pair), no knot/braid-closure claim.

## 10. Blockers and open items

No blockers: every declared bound completed, so `outcomes.budget_exhausted` is instantiated and
empty. Open: (a) whether the experiment‑2 accumulator object is sufficient for some *other*
declared task that observes only the accumulator; (b) the closed-form growth of the reachable
object layer beyond the declared lengths; (c) whether any non-arithmetic model in this programme
admits a genuine elevation rather than a quotient — on this evidence the braid model does not.
