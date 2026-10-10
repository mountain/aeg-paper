# Frozen experiment contracts

Work-plan reference: `AEG-process-representation-work-plan.md` section 5,
"所有实验共享的冻结模板".

Every experiment in this directory is implemented only after its contract is
written and committed.  A contract is a JSON document under
`research/process-representation-gap/contracts/` named
`<experiment>.v<version>.json`.

## Freezing mechanism

A contract is *frozen*, not merely written:

* Each experiment's evidence record carries `contract.path` and
  `contract.sha256`, computed over the contract file bytes.
* Every verifier re-reads the contract, re-hashes it, and raises
  `EXP-CONTRACT-DRIFT` if the hash differs.
* Changing a frozen contract therefore invalidates the evidence that cites it.
  A changed requirement is published as a **new contract version** with a
  recorded reason and the old results retained; the old contract file is never
  overwritten in place.

Negative control `contract-drift` in each experiment's control suite mutates a
copy of the contract and requires `EXP-CONTRACT-DRIFT`.

## Required fields

| Field | Work-plan requirement it discharges |
|---|---|
| `native` | native syntax, types, state, history, process equivalence, and which rewrites are allowed |
| `domain` | input domain, generators, action/continuation set, length and resource budget |
| `task` | initial observation `pi`, task `Q`, observation points, whether later observations may be chosen adaptively, error semantics |
| `representations` | the three tiers: existing summary; bounded, pre-declared enhancement; full history or exact semantics as upper-bound control |
| `outcomes` | separate slots for success, expected negative result, implementation error, budget exhaustion, unknown |
| `independent_check` | the independent computation route and why it is not the primary route |
| `negative_controls` | each with the *specific* diagnostic it must raise |
| `evidence` | evidence format and determinism rule |
| `reproduction` | exact commands |

## Rules the schema cannot enforce but the reviewer must

1. `native.allowed_rewrites` and `native.forbidden_rewrites` are part of the
   experiment, not commentary.  A result may only use rewrites declared there.
2. `representations` must contain at least one entry per tier.  A tier may be
   declared `not-instantiated` with a reason; it may not be silently omitted.
3. `outcomes` must be pairwise distinguishable.  "Any exception" is never an
   accepted negative result; each negative control names its diagnostic code.
4. `independent_check.rationale` must explain why the route does not share a
   semantic helper with the primary implementation.  Two checkers calling the
   same helper are one checker.
5. Costs are reported per channel (storage bytes or structural size,
   computation steps, observation count, verification cost).  They are never
   collapsed into one number, and a finite observer is never defaulted to a
   scalar or a finite-state machine.

## Index

| Experiment | Contract | Plan section |
|---|---|---|
| exp1 | `exp1-order-and-mixing.v1.json` | 6, 实验一 |
| exp2 | `exp2-loop-continuation.v1.json` | 6, 实验二 (首要) |
| exp3 | `exp3-typed-hole-context.v1.json` | 6, 实验三 |
| exp4 | `exp4-objectification-elevation.v1.json` | 6, 实验四 |
| exp5 | `exp5-braid-nonarithmetic.v1.json` | 6, 实验五 |
| exp6 | `exp6-knot-deformation-environment.v1.json` | 6, 实验六 |
