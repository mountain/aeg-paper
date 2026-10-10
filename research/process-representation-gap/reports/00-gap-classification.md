# 00 — Gap classification and cost comparison

Work-plan sections 9 and 10. **This report is generated from evidence, not
written over it.** Every row cites a JSON pointer into a raw evidence document,
and `tools/build_gap_classification.py` re-checks each cited verdict at run
time: an unexpected or missing verdict fails the build instead of being dropped
from the table. The generated artefact is `evidence/gap-classification.json`.

## 1. Coverage

| experiment | contract | sha256 (first 12) | findings |
|---|---|---|---|
| exp1 order and mixing | `exp1-order-and-mixing.v1.json` | `d1ab186a2fef` | 5 |
| exp2 loop continuation | `exp2-loop-continuation.v1.1.json` | `e0b9d493d79a` | 6 |
| exp3 typed hole and context | `exp3-typed-hole-context.v1.json` | `bd7f958740b1` | 3 |
| exp4 objectification and elevation | `exp4-objectification-elevation.v1.json` | `a092fcd470d5` | 2 |
| exp5 braid as non-arithmetic process | `exp5-braid-nonarithmetic.v1.json` | `3cb4feaa8ed3` | 1 |
| exp6 knot deformation and environment | `exp6-knot-deformation-environment.v1.json` | `1b8a6d0ddbce` | 6 |
| adva pinned-source probe | — | — | 1 |

24 findings. The classifier refuses to emit a table in which any frozen
contract contributes no finding (`GAP-EXPERIMENT-UNCOVERED`), so an experiment
cannot be silently omitted.

## 2. The taxonomy, and what each category cost in evidence

Categories are the work plan's own section 9 rows, kept as data in the tool.

### 2.1 `observation-insufficient` — same summary, different future task (9 findings)

The most common gap, and it appears in four independent models.

| experiment | summary | what breaks |
|---|---|---|
| exp1 | `pi0 = (count_P, count_R, u)` | 95 classes over 127 words, 46 colliding pairs; witnesses `PRR` vs `RPR` |
| exp1 | counts alone | `PR` vs `RP`, counts `(1,1)`, states `(1,1/2)` vs `(1/2,1)` |
| exp1 | endpoint alone | `ε` vs `R`, `u=1`, states `(1,1)` vs `(1,1/2)` |
| exp1 | downstream spectral summary | 5 classes vs 31 task classes |
| exp2 | `pi0` = the PR-16 three-scalar readout | 17 classes over 115 words, largest fibre **26** |
| exp2 | `pi1` = mechanism counts | 29 classes; `cccvlv` vs `cccvvl` under `l` → `9/4` vs `11/4` |
| exp2 | `pi2` = counts + phase tag | 45 classes; `cccvlc` vs `ccvclc` under `l` → `10` vs `11` |
| exp4 | `pi_out` = the endpoint value at one state | `ε` and `D_2` both `0` at `x₀ = 0`; objects `(0,1)` vs `(0,2)` |
| exp4 | the exp2 accumulator object | `cvc` vs `ccvcv`, same object and same accumulator `2`, readouts `(3,1,2)` vs `(5,1,12/5)` |

The exp4 row is the sharpest: **an object can be stable, composable, exactly
lowerable — and still fail task sufficiency.** Passing the interface and descent
gates does not buy observation sufficiency.

### 2.2 `update-not-closed` — same summary and same action, different summary (3 findings)

| experiment | summary | failure |
|---|---|---|
| exp1 | `pi0` | same digest + same action → different digest |
| exp2 | `pi0` | `cccvl` vs `ccvlv`, readout `(4,1,12/5)`; `v` legal at the first, illegal at the second; digests after the same action `(5,1,5/2)` vs `INVALID` |
| exp2 | `counts + alternations` | equal counts and equal alternations do not determine the last mechanism, so the successor's alternation count is not a function of the digest |

The third row is worth keeping: an enhancement can be *more* informative than
the summary it extends and still not be a right congruence. It failed a property
the cheaper `counts` summary passed.

### 2.3 `legality-signature` — the two histories are not jointly legal (4 findings)

| experiment | witness |
|---|---|
| exp2 | `ccc` vs `ccv`: both readout `(3,1,2)`, legal sets `{c,v}` vs `{c,v,l}` |
| exp3 | 13 rejected contexts, each with its own code (`EXP3-TYPE-MISMATCH`, `EXP3-GLOBAL-CYCLE`, `EXP3-ILLEGAL-DISCARD`, …) |
| exp6 | obstacle changes legality: a free-space path rejected once a ball is added |
| exp6 | time changes legality: one parameterisation certified with margin `3/4`, the other colliding at `t = 3/8` |

Work-plan section 4.2 says a pair that is not jointly legal is separated only if
the legality signature is added to the equivalence definition. Every finding
above is reported under **both** relations, and the two are never conflated.

### 2.4 `value-equality-insufficient` — equal value, different behaviour in a legal context (3 findings)

| experiment | witness |
|---|---|
| exp3 | `const(2)` vs `h1`: both `DEFINED (2)` at `beta0 = (2,7,3,5)`; at the legal filling `beta3 = (4,7,3,5)` → `2` vs `4`. Stronger: `div(const(2),h1)` vs `div(h1,const(2))` agree on **all six** declared residues and differ only in operand order |
| exp6 | gate B refuted for topological semantics by an explicit witness pair |
| exp6 | environment changes equivalence: meridian and longitude differ on the strict torus and are equivalent as unknots in free R³; a basis swap (det `−1`) changes the contract |

### 2.5 `quotient-forgets-history` (2 findings)

| experiment | witness |
|---|---|
| exp5 | 5461 literal words → 1457 freely reduced → **577** braid elements → 6 endpoint permutations |
| exp6 | same knot type, different deformation history: identity path vs one Reidemeister move plus its inverse |

exp5's W2 is the canonical instance: `σ₁σ₂σ₁` and `σ₂σ₁σ₂` share the Artin
automorphism `(xyzy⁻¹x⁻¹, xyx⁻¹, x)` and the permutation `(2,1,0)`, with
generator counts `(2,1)` vs `(1,2)`. Per the work plan this is **not** a
group-semantic counterexample; it is exactly what the quotient is entitled to
forget, and it is why a construction-history task needs the second layer.

### 2.6 `bounded-compatible` — no counterexample inside the declared budget (2 findings)

| experiment | result |
|---|---|
| exp3 | **0 of 63** declared grid candidates are sufficient; the best single field (`dom_profile`) still leaves 242 classes, and the union of all six still leaves 281 |
| exp6 | gate D: no state completeness, no process completeness, no rewrite completeness (R3 not instantiated), termination yes with a declared `not-certified` |

exp3's row is the honest negative of the programme: in the typed-context
setting, **no cheap bounded residual in the declared grid repairs the gap**. The
sufficient candidate has to be the behaviour vector over the whole filling
family.

### 2.7 `source-interface-absent` (1 finding)

The pinned Adva source supplies **no** native legal-continuation interface for
the two PR-16 records. Verified from the Git object store by 23 checks in
`experiments/adva_continuation_interface.py`:

* `RelationCellV0` exposes exactly `{new, check, transport}` — no append, step,
  glue or continuation operation;
* `transport()` refuses a cell whose filling is still open, and the PR-16
  filling is `{"state": "open", …}`;
* `check_braid` destructures exactly three steps and requires the braid pattern,
  so a fourth step cannot be recorded;
* ADR 0022 rejects frame-id reuse for iteration because V0 has no event
  re-enabling or feedback semantics;
* PSC0 excludes recursion, cyclic substitution and stable feedback.

Downstream would have to invent a legality predicate, an append operation, a
boundary-agreement rule, an identity policy and a filler decision. Experiment 2
therefore builds its own declared model, exactly as the plan prescribes.

## 3. Cost comparison — and why it is not a single number

Work-plan section 5 requires cost per channel and forbids collapsing the
channels or defaulting a finite observer to a scalar. It also requires the
domain to be stated with every cost. **The six domains are different sizes, so
raw byte totals are not comparable across experiments.** What *is* comparable is
the pattern inside each experiment.

| experiment | domain | insufficient summary (mean bytes/history) | cheapest sufficient candidate (mean bytes/history) | full history (mean bytes/history) |
|---|---|---|---|---|
| exp1 | 127 words, 49 states | `pi0` 21.84 | `pi2_resp` 63.69 | 124.3 |
| exp2 | 115 words, 40 continuations | `pi0` 26.2 | **`counts+accum` 26.0** | 40.3 |
| exp3 | 16 648 bodies, 7 fillings | `pi0` 75.5 | `pi_F` 398.8 | 2 483 |
| exp5 | 5 461 crossing words | endpoint permutation 18.0 | Artin triple 58.7 | 67.7 |

The pattern, stated carefully:

* **The cheapest sufficient candidate is always more expensive than the
  insufficient summary it replaces** — by roughly 3× (exp1), 1× (exp2), 5×
  (exp3) and 3× (exp5). There is no free lunch anywhere in this programme.
* **In two of four measured cases the sufficient candidate is cheaper than full
  history**: exp2 (`counts+accum` 26.0 vs 40.3) and exp5 (Artin triple 58.7 vs
  67.7). exp5's is the cleaner one, because the Artin triple is a genuine
  quotient that *provably* determines the braid element and costs **less** than
  the literal word while the endpoint permutation costs far less and determines
  far less.
* **In exp3 full history is 6.2× the sufficient candidate**, so history is the
  clear loser; but exp3 is also the experiment where the cheapest bounded
  candidate is a total failure (0 of 63).
* exp2's `counts+accum` at 94 classes is *not* injective and is still
  sufficient. A repair that chased injectivity would have been over-refined and
  more expensive — `pi3` (counts + phase + 2-suffix + accumulator) is injective
  at 58.8 bytes and buys nothing the 26-byte candidate does not already buy.

**Therefore: retaining full history is not a recommended repair anywhere it was
measured, and it is also never the cheapest thing that works.** The work plan's
warning that "历史保留不是自动推荐的最小修补" is borne out; so is the converse
warning that a bounded enhancement is not automatically sufficient (exp3's 0 of
63).

## 4. What the six experiments agree on

1. **Observation sufficiency and closed update are independent properties.**
   exp2 exhibits a summary that is closed-update and insufficient (`pi1`,
   `pi2`), and one that fails both (`pi0`). exp1 exhibits a summary that fails
   sufficiency and closure at once. Neither failure implies the other, and the
   programme never reports one as the other.
2. **Value equality never implies substitutability.** exp3's `div(const(2),h1)`
   vs `div(h1,const(2))` agree on every declared residue and differ in a legal
   context; exp6's meridian/longitude differ only by environment; exp4's `ε`
   vs `D_2` agree at the single evaluation site.
3. **A stable, composable, exactly-lowerable object can still be observation-
   insufficient.** exp4's exp2 accumulator object passes gates (ii) and (iii)
   and fails gate (i); the exp5 Artin object passes all three gates and is still
   a quotient rather than a new rank. Both directions of the plan's question are
   answered the same way: single equality is not enough to make an object, and a
   stable object is not enough to make a higher-order computation.
4. **Legality is part of the process, not a side condition.** Four independent
   witnesses across exp2, exp3 and exp6 show two histories with the same
   observation and different legal continuations.
5. **Every non-arithmetic model measured here is a quotient, not an
   elevation.** exp5's braid objects (5461 → 577) and exp6's diagram classes are
   surjective images of literal histories.

## 5. What is *not* concluded

* No general theorem. Every count above is inside a declared domain and budget,
  and every per-experiment report states the domain with the number.
* No claim that the taxonomy is complete. It has eight categories because the
  work plan names categories; the programme did not prove that no ninth exists.
* No claim that any representation is minimal in an absolute sense. Where a
  grid was scanned, minimality is relative to that declared grid.
* No promotion of any claim into a manuscript. Work-plan section 10 requires
  governance review before that, and nothing here has been promoted.
