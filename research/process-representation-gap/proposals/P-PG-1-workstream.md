# P-PG-1 — draft workstream (process-geometry)

**Status: PROPOSAL. Not applied. Requires repository governance review.**

Target: `workstreams/process_representation_gap/`
Precedent: `workstreams/native_method_firewall/` (README + one module + one
external test); `workstreams/am_weight_compiler/` for the frozen-contract,
commit/reveal and `RESEARCH_DISPOSITION.json` schema.

The repository documents the workstream convention by example rather than in
prose (`grep -rn "workstreams/" docs/ README.md AGENTS.md` returns nothing), so
this draft follows the smallest complete example and uses the richer schema only
where an economy claim is made.

## Proposed layout

```text
workstreams/process_representation_gap/
    README.md                     issue number, scope, outcome, boundary, gate, disposition
    FROZEN_CONTRACT.json          the declared model and budgets, frozen before the module
    RESEARCH_DISPOSITION.json     EXPAND | NARROW | ELIMINATE | STOP + claim ceiling
    gap_continuation.py           the declared typed feedback machine and its analysis
    tests/test_gap_continuation.py
```

and one thin wrapper under the repository's own root suite, as the existing
workstreams do, so a root `pytest` run reaches it.

## Proposed `README.md` content

```markdown
# Process-representation gap

Research-local executable calibration for the question: when does a declared
presentation of a process stop being sufficient for a declared task, and what is
the cheapest presentation that is not?

This workstream carries the non-arithmetic process, continuation-equivalence and
objectification findings.  It changes nothing in `src/` and adds no public API.

## Declared model

A free mechanism monoid `{c, v, l}`, a declared partial legality
(`c` always; `v` iff `#c > #v`; `l` iff `#v >= 1`), the exact accumulator
`A(u.c)=2A(u)+1`, `A(u.v)=A(u)/2`, `A(u.l)=A(u)+1`, and a Moore observation.
This is a declared small typed model, not native execution of anything.

## Outcomes

- The three-scalar readout has 17 classes over 115 reachable words; largest
  fibre 26; neither task-sufficient nor closed-update.
- Shortest distinguishing continuation for `ccv` / `cvc` has length 1.
- Exactly one of seven declared one-field extensions of the incidence summary is
  both sufficient and closed-update: the exact accumulator, at 26.0 mean bytes
  per history against 40.3 for the literal word.
- That choice survives a reserved held-out family of 751 words of length 7 and 8
  that was not used to select it.
- An object can pass the interface and exact-descent gates and still fail task
  sufficiency; the braid object passes all three gates and is a quotient.

## Important boundary

Exact finite results on declared domains and budgets.  No general theorem, no
unbounded recursion, no spectrum, and no new rank.  The braid object is a
quotient (5461 -> 577), not an elevation.

## Reuse of the existing experimental entry point

`process_geometry.experimental.minimize_finite_task_process` was used
unmodified as an exact oracle: it decided the same two properties by stable
partition refinement with no continuation-depth cutoff, and agreed with an
independently written checker on every representation and both shortest
witnesses.  No change to it is requested; this row records that it is reusable
as it stands.

## Executable gate

    python -m pytest
    python gap_continuation.py --check FROZEN_CONTRACT.json

## Governance disposition

- Mathematical Core: unchanged.
- Research Programme: U5 objectification pressure only; no universality result.
- Engineering Architecture: research-local calibration, no new stage.
- Theory Map: unchanged; no stable node.
- Public API: no pressure.
```

## Proposed `FROZEN_CONTRACT.json` (shape)

```json
{
  "schema": "process-geometry/process-representation-gap-contract/v0",
  "frozen_on": "<date>",
  "declared_model": {
    "alphabet": ["c", "v", "l"],
    "legality": "c always; v iff #c > #v; l iff #v >= 1",
    "accumulator": ["A()=0", "A(u.c)=2A(u)+1", "A(u.v)=A(u)/2", "A(u.l)=A(u)+1"]
  },
  "budget": { "max_word_length": 6, "max_continuation_depth": 3 },
  "reserved_verification_family": { "length_range": [7, 8], "used_for_selection": false },
  "expected": {
    "domain_size": 115,
    "pi0_classes": 17,
    "shortest_distinguishing_depth": 1,
    "grid_qualified": ["counts+accum"],
    "reserved_sufficient": true,
    "reserved_closed_update": true
  },
  "claim_ceiling": "exact finite calibration; no general theorem, no new rank"
}
```

The `expected` block is the regression condition: the workstream must reproduce
these numbers, and `tools/build_gap_classification.py` in the aeg-paper branch
re-checks the same values against the originating evidence.

## Interface pressure observed — and deliberately *not* requested

`minimize_finite_task_process` was reused **unmodified**. The promotion signal
is *"reusable as-is, and here is what it was used for"*, not *"change it"*. No
widening of the `Experimental` surface is proposed, and no
`Objectification` / `ProcessRank` / `RankLowering` abstraction is proposed —
this repository and the work plan both deliberately omit them.

## Relation to the repository's own open obligations

`docs/MATHEMATICAL_CORE.md` lists as open: *"a theorem deciding when a
nontrivial continuation-value fibre is only a horizontal task-state lift and
when it objectifies into a higher-rank compositional process"*. The gate-by-gate
result is evidence **toward** that question and does not settle it: it exhibits
one object that is a quotient rather than a lift, and one that objects but fails
task sufficiency.

## Regression condition

Reproduce the `expected` block from the pinned sources. A mismatch against
`evidence/exp2-loop-continuation.json` in the aeg-paper branch is a failure.
