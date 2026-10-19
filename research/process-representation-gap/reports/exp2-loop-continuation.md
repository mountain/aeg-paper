# Experiment 2 — loop continuation and anytime observation

Work-plan section 6, 实验二 (declared primary). Contract
`contracts/exp2-loop-continuation.v1.1.json`, sha256
`e0b9d493d79af5140993bf72c0e75d0f6455ffaa4473cd6ce89a886dfc96a0fe`.

Evidence: `evidence/exp2-loop-continuation.json` and
`evidence/exp2-loop-continuation-independent.json`.

## 1. The question, stated exactly

Do two histories with the same current observation stay indistinguishable under
the same future interaction? The work plan asks for the shortest distinguishing
continuation, a verification or counterexample of the update commuting square,
and a clear boundary between finite closure and the unbounded case — with the
two failure modes of section 4.3 kept apart:

* same summary, different observations in the future → **task-sufficiency
  failure**;
* same summary, same action, different summary → **closed-update failure**.

## 2. The gap in the pinned source, reported rather than papered over

The plan says: if the two PR-16 records have no common legal native
continuation interface, report the gap and build a small model conforming to
the core contract instead. That is what happened.

| Item | Value |
|---|---|
| PR-16 left event word | `compute, verify, compute` |
| PR-16 right event word | `verify, compute, verify` |
| Left reachable under the declared legality | **yes** |
| Right reachable under the declared legality | **no** — its first action is `verify` with `count_c = 0 > count_v = 0` false |
| Frozen scalar triple, both records | `(3, 1, 2)` |

The two records are equal under the pinned scalar projection and unequal in
reachability under any declared compute–verify legality rule of the form used
here. So this experiment does **not** manufacture a continuation interface for
them. It builds the declared model below, as the plan instructs.

## 3. The declared model (not native Adva execution)

Alphabet `Σ = {c, v, l}` with `c` = compute, `v` = verify, `l` = learn.
A state is a trace word. Declared partial legality:

* `c` legal always;
* `v` legal iff `count_c(w) > count_v(w)`;
* `l` legal iff `count_v(w) ≥ 1`.

Exact accumulator, over `Q`:

```
A(ε) = 0,  A(u·c) = 2·A(u) + 1,  A(u·v) = A(u)/2,  A(u·l) = A(u) + 1
```

Declared observation (a Moore observation of the state, matching Paper IV's
`O_C(p)`):

* `R(w) = (count_c + count_v, frames − handoffs, 3·handoffs/frames)` with
  `frames = |w|`, `handoffs = max(|w| − 1, 0)`;
* a state ending in `l` instead exposes `A(w) − 1 = A(w⁻)`, the accumulator
  before the learn; `A(u·l) − 1 = A(u)`, so the two presentations induce the
  same equivalence.

This is a declared small typed model under PIV-S5/PIV-S6. It is **not** native
Adva execution and **not** a faithful AES gate motion.

## 4. A structural fact about the frozen projection

On the declared class of words over `{c, v}`, the PR-16 readout satisfies
`y2 = 1` and `y3 = 3(|w|−1)/|w|`, and `y1 = |w| − count_l`.  Hence:

> **The PR-16 three-scalar readout of a word over `{c, v}` is a function of the
> event count alone.** It is blind to the entire order and to the `c`/`v`
> split.

That is the mechanism behind the collision below, and it is why the
`(T, S, C)` projection obstruction of PR-16 survives projection to scalars.

## 5. Results on the declared domain

Domain: 115 reachable words, `|w| ≤ 6` (`1, 1, 2, 4, 10, 26, 71` by length).
Continuation family `M_C`: all 40 words over `Σ` of length at most 3.

| id | tier | classes on 115 words | task-sufficient | closed update | largest fibre |
|---|---|---|---|---|---|
| `pi0` | existing summary (PR-16 three scalars) | 17 | **no** | **no** | 26 |
| `pi1` | enhancement: mechanism counts | 29 | **no** | yes | 16 |
| `pi2` | enhancement: counts + phase tag | 45 | **no** | yes | 6 |
| `pi3` | enhancement: counts + phase + 2-suffix + `A` | 115 | yes | yes | 1 |
| `hist` | upper-bound control: the literal word | 115 | yes | yes | 1 |

The exact independent oracle (section 7) counts **71** classes of the
legality-and-budget-augmented relation on 117 machine states; the primary's
counts above are classes of the declared representations, a different object.

## 6. The witnesses, with exact values

### 6.1 Order gap — shortest distinguishing continuation is length 1

| | |
|---|---|
| histories | `ccv` and `cvc` |
| readout | both `(3, 1, 2)` — the frozen PR-16 triple |
| counts | both `(2, 1, 0)` |
| legal actions | both `{c, v, l}` |
| accumulators | `A(ccv) = 3/2`, `A(cvc) = 2` |
| continuation `l` | legal for both; observations `("learned","3/2")` vs `("learned","2")` |
| shortest distinguishing continuation | `["l"]`, depth 1, kind `observation` |
| minimality | depth 0 cannot distinguish: the readout and legality agree; enumerated exhaustively |

### 6.2 Legality gap

| | |
|---|---|
| histories | `ccc` and `ccv` |
| readout | both `(3, 1, 2)` |
| legal actions | `{c, v}` vs `{c, v, l}` |
| `l` | illegal at `ccc` (nothing verified), legal at `ccv` |
| base-equivalent (jointly legal continuations only) | **false**, via the legality difference visible at depth 1 |
| shortest distinguishing continuation | `["l"]`, depth 1, kind `legality` |

Per work-plan section 4.2 this pair separates the two equivalence notions: under
the base relation only continuations *jointly legal* are compared, and legality
itself is what differs. The experiment reports both relations and never
conflates them.

### 6.3 The two failure modes are genuinely different

* `pi0` **fails closed update**: `cccvl` and `ccvlv` share the readout
  `(4, 1, 12/5)`; applying `v` is legal at the first and illegal at the second.
  Under the declared absorbing-invalid totalisation the digests after the same
  action are `(5, 1, 5/2)` and `INVALID`. Same digest, same action, different
  digest.
* `pi1` and `pi2` **pass closed update but fail task sufficiency**:
  * `pi1`: `cccvlv` and `cccvvl` both have counts `(3, 2, 1)`; `l` gives `9/4`
    vs `11/4`.
  * `pi2`: `cccvlc` and `ccvclc` both have counts `(4, 1, 1)` and phase `c`; `l`
    gives `10` vs `11`.

So "closed online state" and "observation sufficiency" are demonstrably
independent here — exactly Paper IV's Example `ex:feature-not-online` shape,
realised with a feedback loop rather than a two-element monoid.

### 6.4 Positive control — an equivalence, not a gap

| | |
|---|---|
| histories | `ccvlc` and `cvccl` |
| readout | both `(4, 1, 12/5)` |
| accumulator | both `6` |
| legality | both `{c, v, l}` |
| base- and augmented-equivalent | **yes**, under every common continuation |

Two literally different histories that the declared task genuinely cannot
separate. Without this control any syntactic difference could be mistaken for a
semantic gap; an enhancement that separated this pair would be over-refined.

### 6.5 Boundary: finite closure versus unbounded

Closed for: all reachable words of length ≤ 6, and all continuations of depth
≤ 3. Open: nothing is claimed beyond the declared bound. No unbounded
recursion, infinite loop, or fixpoint semantics is implemented or claimed. The
contract fixes `adaptive: false`; selecting continuations from observations is
declared out of scope for version 1.

## 7. Independent verification

Two independent routes, neither sharing a semantic helper with the primary
(only deterministic JSON serialisation is common):

1. **Exact quotient oracle, from another repository.**
   `process-geometry` at `c47c96fa`, module
   `src/process_geometry/experimental/finite_task_quotient.py`, git blob
   `a381c47822ba00f54530d774446a77b2d48c5a7d`, sha256
   `1b2bf6a4510fd4f9831f0fa721f63deb19a61c4a658c32c7b138b70b4e38fd66`.  It
   decides the task equivalence by **stable partition refinement** on a
   totalised Moore machine, exactly and with **no continuation-depth cutoff**,
   and returns its own breadth-first distinguishing continuations.
   Cross-check over 117 machine states: *every primary verdict on all five
   representations agrees*, and both declared shortest continuations
   (`ccv`/`cvc` → `l`, `ccc`/`ccv` → `l`) match the oracle's own witnesses.
2. **Affine-map algebra for the accumulator.** Each mechanism is the exact
   affine map `c: x ↦ 2x+1`, `v: x ↦ x/2`, `l: x ↦ x+1`; the checker composes
   them right to left and reads the constant term, instead of folding the
   recurrence left to right. It reproduces the frozen hand table
   `A(ccv) = 3/2`, `A(cvc) = 2`, `A(ccvcl) = 5` exactly.

A defect the second route found in itself is retained in the record as
negative control `reversed-composition-route`, in the sibling experiment:
composing in the wrong order silently reverses the composite and the two
routes disagree on the first word of length two. That is the mechanism by
which the independence requirement does real work.

Determinism: both primary and independent emit byte-identical output across
repeated runs and across `python3` / `python3 -O`
(`tools/check_determinism.py`, `failures: []`).

## 8. Cost, per channel, and the declared enhancement grid

Per history, over the 115-word domain; observation count is 11 845 for every
representation because the same continuation family is run against each.

| id | mean storage bytes | max storage bytes | structural size (total) | computation steps | observations | verification cost |
|---|---|---|---|---|---|---|
| `pi0` | 3016/115 ≈ 26.2 | 36 | 690 | 115 | 11 845 | 4 600 |
| `pi1` | 18.0 | 18 | 690 | 115 | 11 845 | 4 600 |
| `pi2` | 2878/115 ≈ 25.0 | 28 | 920 | 115 | 11 845 | 4 600 |
| `pi3` | 6759/115 ≈ 58.8 | 61 | 1 719 | 115 | 11 845 | 4 600 |
| `hist` | 4636/115 ≈ 40.3 | 45 | 1 226 | 115 | 11 845 | 4 600 |

`pi1` is the cheapest candidate and is still not sufficient; `pi3` is the most
expensive non-history candidate and is sufficient, but its structural size
(1 719) exceeds full history's (1 226) on this domain. On the four candidates
declared in contract v1.0, the cheapest sufficient candidate would therefore
have been the literal word — i.e. **no cheap compression at all**.

### 8.1 The declared one-field grid (contract v1.1)

Contract version 1.1 added a *systematic* family so that the minimal-repair
recommendation is argued from a declared grid rather than an ad-hoc list:
`counts` plus exactly one of seven declared fields.

| candidate | classes / 115 | sufficient | closed update | structural size | mean bytes/history |
|---|---|---|---|---|---|
| `counts + accum` | **94** | **yes** | **yes** | 920 | 26 |
| `counts + alternations` | 62 | no | **no** | 920 | 23 |
| `counts + suffix2` | 68 | no | yes | 1 259 | 5031/115 ≈ 43.7 |
| `counts + last_learn_position` | 46 | no | yes | 920 | 572/23 ≈ 24.9 |
| `counts + phase` | 45 | no | yes | 920 | 2878/115 ≈ 25.0 |
| `counts + first` | 29 | no | yes | 920 | 2878/115 ≈ 25.0 |
| `counts + verified_fraction` | 29 | no | yes | 920 | 3043/115 ≈ 26.5 |

**This overturned the ad-hoc conclusion.** Exactly one declared field repairs
both failures: the exact accumulator `A(w)`. `counts + accum` is
task-sufficient and closed-update at **26 mean bytes per history**, against
**40.3** for the literal word — so on this domain a genuine compression does
exist, and it is the *cheapest* candidate that works.

Two facts worth keeping:

* `counts + accum` has **94** classes, not 115, and is still sufficient. The 21
  collisions it leaves are between histories the declared task genuinely cannot
  separate — a sufficiency theorem does not require injectivity, and a repair
  that chased injectivity would be over-refined.
* `counts + alternations` fails **closed update**, not just sufficiency: two
  words with equal counts and equal alternations but different last mechanisms
  stay equal after appending the same action only if their last mechanisms
  agree, which is not implied. It is a concrete example of an enhancement that
  looks informative and is not stable.

The selection rule is applied mechanically, and the grid scan is a *declared*
family fixed before the scan ran — not a field added after seeing a failure.


## 9. Negative controls

| id | expected diagnostic | observed |
|---|---|---|
| `illegal-action-accepted` | `EXP2-ILLEGAL-ACTION` | `EXP2-ILLEGAL-ACTION` |
| `accumulator-law-mutated` | `EXP2-HAND-TABLE-MISMATCH` | `EXP2-HAND-TABLE-MISMATCH` |
| `readout-order-blindness` | `EXP2-READOUT-COLLISION-MISSING` | `EXP2-READOUT-COLLISION-MISSING` |
| `pi1-sufficiency-claim` | `EXP2-SUFFICIENCY-CLAIM-REFUTED` | `EXP2-SUFFICIENCY-CLAIM-REFUTED` |
| `pi2-sufficiency-claim` | `EXP2-SUFFICIENCY-CLAIM-REFUTED` | `EXP2-SUFFICIENCY-CLAIM-REFUTED` |
| `route-disagreement` | `EXP2-ROUTE-DISAGREEMENT` | `EXP2-ROUTE-DISAGREEMENT` |
| `enumerated-count-mismatch` | `EXP2-ENUMERATION-MISMATCH` | `EXP2-ENUMERATION-MISMATCH` |
| `oracle-drift` (independent route) | `EXP2I-ORACLE-DRIFT` | `EXP2I-ORACLE-DRIFT` |
| `carrier-escape` (independent route) | `EXP2I-CARRIER-ESCAPE` | `EXP2I-CARRIER-ESCAPE` |

Every control expects a *specific* code and the message is matched, not merely
"some exception".

## 10. What is explicitly NOT claimed

* No unbounded recursion, infinite-loop, or fixpoint semantics.
* No matrix, operator or spectrum: Paper IV section 05b requires the
  endomorphism closure, operator domain, marking and residual to be declared
  before a spectral feature is used, and none is declared here.
* No general theorem from a finite enumeration. Sufficiency is asserted on the
  declared domain and declared continuation family only.
* No claim that the mechanism monoid is anything but free; introducing a
  relation between mechanisms changes the native object and needs a new
  contract version.
* No claim that `pi3` is a recommended repair: it is sufficient but its
  structural size exceeds full history on this domain. The recommended
  candidate from the declared grid is `counts + accum`, and the recommendation
  is bounded to this domain.
* No claim that `counts + accum` is minimal in any absolute sense. It is the
  cheapest candidate inside the seven-field grid declared in contract v1.1 and
  nothing else.
* No claim about the PR-16 records' continuations. They are not reachable
  words of this model.

## 11. Open items carried forward

* The two PR-16 records still have no common legal native continuation
  interface. Whether the pinned Adva core supplies one is the subject of the
  separate source reading recorded in the repository reading notes.
* Adaptive continuation selection (choosing the next action from observations)
  is not permitted by contract version 1.1 and is untouched.
* Whether a *cheaper* sufficient representation exists on a larger domain is
  open. On the declared domain the answer found by the declared grid is
  `counts + accum` at 26 mean bytes per history, and the grid is not claimed
  to be exhaustive over all possible enhancements.
* Why the accumulator — and not the phase, the suffix or the alternation count
  — is the field that carries the missing information is observed, not
  explained. A structural explanation would be a genuine next step.
