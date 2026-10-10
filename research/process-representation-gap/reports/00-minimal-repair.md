# 00 — Minimal repair design

Work-plan section 9. Every proposal below is tied to a concrete witness, a
declared repair, a stated cost, the task it improves, the tasks in which it
still fails, and a **regression condition** that would falsify it. Proposals are
ordered by the strength of the evidence behind them, strongest first.

Nothing here has been applied to any repository. Work-plan section 10 requires
research evidence first and interface promotion afterwards, through each
repository's own governance.

## 1. The rule the work plan sets, and how it was followed

> 改进须尽量小且经济，不能以"全部记录都保留"替代研究。

Three consequences were enforced mechanically rather than promised:

* Each experiment declared an **enhancement grid** — a systematic family of
  candidate repairs — *before* running the scan. exp2 declared seven one-field
  extensions of its incidence counts; exp3 declared all 63 non-empty subsets of
  six fields; exp1 declared a response-table family; exp4 declared a gate
  criterion.
* The recommendation is chosen by a **declared selection rule**, not by taste.
* exp1 declared a **reserved verification family** in its contract and did not
  use it to select anything. exp2 acquired the same discipline in this round
  (section 7).

Full history was carried in every experiment as an **upper-bound control**
only. In no experiment did it turn out to be the recommended repair.

## 2. R1 — exp2: add the exact accumulator to the incidence counts

**Gap.** exp2's `pi0` (the PR-16 three-scalar readout) has 17 classes over 115
reachable words with a largest fibre of 26, is not task-sufficient, and fails
closed update. `pi1` (incidence counts) is closed-update but still not
sufficient: `cccvlv` and `cccvvl` share counts `(3,2,1)` and `l` returns `9/4`
vs `11/4`.

**Change.** `pi1 + A(w)`, where `A` is the exact rational accumulator already
carried by the state. One exact rational, no new machinery.

**Evidence.** Contract v1.1's seven-field grid, scanned mechanically:

| candidate | classes / 115 | sufficient | closed | mean bytes |
|---|---|---|---|---|
| **counts + accum** | 94 | **yes** | **yes** | **26.0** |
| counts + alternations | 62 | no | no | 23 |
| counts + suffix2 | 68 | no | yes | 43.7 |
| counts + last_learn_position | 46 | no | yes | 24.9 |
| counts + phase | 45 | no | yes | 25.0 |
| counts + first | 29 | no | yes | 25.0 |
| counts + verified_fraction | 29 | no | yes | 26.5 |

**Cost.** 26.0 mean bytes per history against 40.3 for the literal word — a
genuine compression, not a renaming.

**Task improved.** The declared anytime-observation task, on `|w| ≤ 6` with
continuations of depth ≤ 3.

**Still fails.** Any task that observes construction history: 94 classes is not
115, and the collisions left are between histories the declared task cannot
separate but a history task could.

**Regression condition.** A declared reachable word pair with equal
`(counts, accumulator)` and a legal continuation on which the declared
observation differs. Finding one falsifies R1.

**Held-out check.** See section 7: it survives.

## 3. R2 — exp1: a bounded two-probe response pair

**Gap.** exp1's `pi0 = (count_P, count_R, u)` has 95 classes over 127 words with
46 summary-colliding pairs; counts alone fail (`PR` vs `RP`, states `(1,1/2)` vs
`(1/2,1)`), and the endpoint alone fails (`ε` vs `R`, states `(1,1)` vs
`(1,1/2)`).

**Change.** Replace the endpoint coordinate with a **two-probe response pair**:
the plant state after two fixed, pre-declared probe words.

**Evidence.** The result is exact and unusually clean: 49 classes over 127 words,
and the declared domain has exactly **49 reachable states**. The response pair is
therefore *equal to the task equivalence* — neither too coarse nor over-refined.

**Cost.** 63.69 mean bytes per history against 124.3 for the literal word.

**Still fails.** The provenance task: `pi2_resp` fails with witness `PP` vs `RPP`.
That is a *different* declared task, and it is reported separately rather than
folded in.

**Regression condition.** A declared reachable word pair with equal two-probe
response and different behaviour at depth 0 or 1. The experiment exhibits **0**
such pairs among all 8001 word pairs, so this is currently a strong negative
claim inside the declared budget.

**Note on honesty in the cost report.** exp1's own report states that on this
small domain the plain literal word is *smaller in bytes per history* than some
sufficient candidates. The recommendation rests on the response pair being
**exactly the task equivalence** — an information argument — not on it being the
cheapest encoding. The trade-off is stated rather than hidden.

## 4. R3 — exp3: no bounded residual works; move the context into the interface

**Gap.** exp3's `pi0` has 341 classes over 16 648 bodies and 232 separating
fibres. `const(2)` and `h1` both give `DEFINED (2)` at the frozen filling
`beta0 = (2,7,3,5)` and `2` vs `4` at the legal filling `beta3 = (4,7,3,5)`.
Stronger: `div(const(2),h1)` and `div(h1,const(2))` agree on **all six** declared
residues — support, use counts, literals, operators, operator count, domain
profile — and differ only in operand order.

**The honest negative.** Of **63** declared grid candidates, **0 are
sufficient**. The best single field (`dom_profile`) still leaves 242 classes; the
union of all six still leaves 281. This is the opposite of exp2's outcome and it
is the single most important repair-design finding in the programme:

> **In the typed-context setting there is no cheap bounded residual.**
> Six apparently informative structural fields, and every combination of them,
> all fail.

**Change (proposed, not applied).** Do not add fields. Declare the **context
family itself** as part of the interface, and make the observation explicit:
`pi_F` = the behaviour vector over the declared filling family `F`. That is
sufficient and closed-update by construction, because the update is a projection.

**Cost.** `pi_F` at 398.8 mean bytes per history against full history's 2 483 —
so the behaviour vector is 6.2× cheaper than history while being exactly what
the task needs, and history is *strictly finer* than the task (it separates the
positive control `const(-1)` vs `add(const(-1),const(0))`, which are
contextually equal — over-refinement).

**Still fails.** `F` is not claimed complete; refilling outside `F` is a
composition of contexts and needs its own contract version.

**Regression condition.** A sufficient candidate inside the declared 63-candidate
grid would falsify the negative. None was found.

## 5. R4 — exp4: do not call a quotient an elevation

**Gap.** The plan asks whether one equal evaluation is enough to form an object,
and whether a stable object is enough to form a higher-order computation.

**Evidence, gate by gate.**

| model | gate (i) sufficiency | gate (ii) interface | gate (iii) descent | verdict |
|---|---|---|---|---|
| baseline `pi_obj` (`T_a`, `D_k`) | PASS | PASS (19 530) | PASS (19 530 / **0** mismatches) | **ELEVATION** |
| baseline `pi_out` (one endpoint) | **FAIL** (`ε` vs `D_2`) | — | — | — |
| exp2 accumulator object | **FAIL** (`cvc` vs `ccvcv`) | PASS (1 728 / 1 092) | PASS (4 790 / 0) | ELEVATION |
| exp5 Artin object | PASS for the group task, FAIL for a history task | PASS (103 823 / 21 844) | PASS (1 593 + 2 728 / 0) | **NO ELEVATION** |

**Change.** Adopt the criterion the evidence supports: an object is an
**elevation** only when it passes all three gates *and* adds expressiveness the
lower layer cannot express. The exp5 Artin object passes all three gates and is
still a quotient (5461 literal words → 577 objects, surjective by construction);
labelling it an elevation would be exactly the naming fallacy the plan forbids.

**Cost.** `pi_out` 10 418 B / 3 906 answer steps; `pi_obj` 54 409 B / 19 530;
`pi_hist` 109 187 B / 92 775.

**Still fails.** Gate (i) for the exp2 accumulator object: it determines `A(w)`
exactly and retains nothing of the incidence counts, yet the exp2 observation and
legality are functions of those counts. An object can be stable, composable and
exactly lowerable and still be observation-insufficient.

**Regression condition.** Exhibit a composite expressible only at the object
layer for the exp5 model; that would falsify the "no elevation" verdict.

## 6. R5 / R6 / R7 — the three remaining repairs

### R5 — exp5: keep the two layers explicitly, and merge nothing

5461 literal words → 1457 freely reduced → **577** braid elements → 6 endpoint
permutations. The Artin triple is a genuine compression: 58.7 mean bytes per word
against 67.7 for the literal word, while determining the braid element exactly
by Artin's theorem. It is also exactly the layer at which `σ₁σ₂σ₁` and
`σ₂σ₁σ₂` become one object while their generator counts stay `(2,1)` and `(1,2)`.

**Change.** Never serve a construction-history task from the group quotient.
Keep both layers and state which equivalence each serves.

**Negative finding worth as much as the repair.** A single probe is not the
action: `x₁x₂x₃` is **constant** across all 577 classes (576 collisions, largest
577), while the commutator `x₁x₂x₃x₁⁻¹x₂⁻¹x₃⁻¹` separates all 577. That is a
finite-domain finding and is labelled as one.

**Regression condition.** A class pair separated by no free-group probe.

### R6 — Adva: report the gap; do not invent native semantics

The pinned source supplies **no** native legal-continuation interface for the two
PR-16 records, established by 23 re-checked facts: `RelationCellV0` exposes only
`{new, check, transport}`; `transport()` refuses the open filling; `check_braid`
fixes exactly three steps; ADR 0022 rejects frame-id reuse for iteration; PSC0
excludes recursion, cyclic substitution and stable feedback.

**Change (proposal to that repository, not applied).** If a continuation notion
is wanted, it belongs in a **new declared profile** with its own legality
predicate, append operation, boundary-agreement rule, identity policy and filler
decision — not in PSC0 and not as a silent extension. Experiment 2's model is
exactly such a profile, and it declares itself as one.

**Regression condition.** A pinned Adva operation that appends a step to a
`FrameRelationPathV0`, or composes two `RelationCellV0`. None exists today.

### R7 — exp6: the environment goes in the contract, not the encoding

Gate B is **refuted for topological semantics**: an injective integer encoding
does not decide topological equivalence. Meridian and longitude differ on the
strict torus and are both unknots in free R³; a basis swap of determinant `−1`
changes the contract again.

**Change.** State the environment (embedding, basis, thickening, obstacle
timetable) as part of the task contract. Never let an encoder's injectivity stand
in for an equivalence test.

**Also material.** Time parameterisation changes legality: one parameterisation
is certified clear with margin `3/4` (hand-checked minimum squared distance
`40400/10201` at `t = 301/808`), the other collides at `t = 3/8`. Both share
start, end and knot type. **Continuous interval certificates, not keyframes, are
what make that a proof** — the keyframe-only negative control detects the
blindness at `t = 1/4`.

**Regression condition.** A task in which two encodings that are equal decide a
topological question differently, with no environment difference.

## 7. The reserved verification family

Work-plan section 9: *至少保留一个未用于选择修补的后续验证族*.

* **exp1** declared one in its contract before running: downstream words of
  length 3 and 4, whose spectral fibres are enumerated and reported separately,
  not used to select the recommendation.
* **exp2** acquired one in this round. The repair `counts + accum` was selected
  on the exhaustive layer `|w| ≤ 6`; the reserved family is `|w| ∈ {7, 8}` — 751
  reachable legal words (197 at length 7, 554 at length 8), inside the contract's
  declared domain but outside the enumeration layer that produced the choice.

  **Result: `counts + accum` remains task-sufficient and closed-update on the
  reserved family**, with 344 classes on 751 words, and the full-history control
  remains sufficient. The verdict recorded in the evidence is
  *"the selected repair still holds outside the selection family"*.

  This is a genuine held-out confirmation, and it is still only a bounded-domain
  result: it is not a theorem, and the report says so.

* **exp3** has no reserved family — its recommendation is the *negative* (0 of
  63 candidates sufficient), and a negative cannot be "confirmed on held-out
  data" the same way. What would falsify it is a sufficient grid candidate,
  which the declared grid does not contain.

## 8. What the programme recommends *not* doing

1. **Do not retain full history by default.** It was never the recommended
   repair: it is 40.3 vs 26.0 in exp2, 124.3 vs 63.69 in exp1, and 2 483 vs
   398.8 in exp3, and in exp3 it is 6.2× the sufficient candidate while being
   strictly finer than the task.
2. **Do not treat a field that looks informative as a repair.** exp2's
   `counts + alternations` is *more* informative than `counts` and fails closed
   update, a property `counts` alone passed.
3. **Do not chase injectivity.** exp2's `counts + accum` has 94 classes rather
   than 115 and is sufficient; the injective `pi3` costs 58.8 bytes and buys
   nothing more. exp3's behaviour vector is likewise sufficient without being
   injective.
4. **Do not infer sufficiency from interface quality.** exp4 shows an object
   that passes the interface and descent gates and still fails task sufficiency.
5. **Do not upgrade a bounded result.** Every number above carries its domain.
   The reserved family strengthens exp2's recommendation without converting it
   into a theorem.
