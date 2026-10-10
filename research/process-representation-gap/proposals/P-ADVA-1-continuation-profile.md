# P-ADVA-1 — draft declared-continuation profile (adva)

**Status: PROPOSAL. Not applied. Requires repository governance review.**

Target: `docs/research/<NNNN>-declared-continuation-profile.md`, with a
companion bounded-run contract under `experiments/<name>/contract.json`.
Precedent: `docs/research/0129-bounded-breakthrough-trusted-boundaries.md`,
which fixes the six-part bounded-run contract template that
`docs/DEVELOPMENT.md` makes normative for bounded research runs.

## Why a new profile, and not an extension

`research/process-representation-gap/experiments/adva_continuation_interface.py`
re-derives 23 facts from the Git object store and concludes that the pinned
source supplies **no** native legal-continuation interface for a
`FrameRelationPathV0` or a `RelationCellV0`:

| fact | source |
|---|---|
| the cell exposes only `new`, `check`, `transport` | `crates/adva-witness/src/relation.rs` |
| `transport()` refuses a cell whose filling is still open | `RelationFormationErrorV0::OpenBoundaryCannotTransport` |
| `check_braid` destructures exactly three steps and requires the braid pattern | `fn check_braid` |
| the PR-16 filling is `{"state": "open", ...}` | `programs/bootstrap-0/first-trace-arithmetic.adva` |
| frame-id reuse for iteration is rejected | ADR 0022 |
| PSC0 excludes recursion, cyclic substitution and stable feedback | `docs/PROGRAM_PROCESS_CORE.md`, `docs/SEMANTIC_SCOPE.md` |

So a continuation notion cannot be a quiet addition to the existing objects. It
needs its own declared profile, exactly as the bounded data-machine profile was
walled off.

## Five semantics the profile must declare

These are the five things the probe shows a downstream experiment must invent.
The profile's whole job is to make them explicit rather than implicit:

1. a **legality predicate** on these records;
2. an **append / step / gluing operation** on `FrameRelationPathV0` or
   `RelationCellV0`;
3. a **boundary-agreement rule** for an appended step;
4. an **identity policy** that does not reuse a `FrameIdV0`;
5. a **filler / transport decision**, since `transport()` refuses the open
   boundary.

## Draft, following the research-0129 six-part template

```markdown
# Research NNNN: a declared continuation profile for recorded relation paths

Date: <date>.  Status: proposed native-compatible research profile.  This is not
an implemented native operation, not a Rust transformation certificate, and not
a change to PSC0.

## 1. Question and level

Can a finite, declared continuation operation be specified for the recorded
relation paths of `programs/bootstrap-0/first-trace-arithmetic.adva` without
extending PSC0 and without claiming mechanism execution?

Level: external finite specification plus an exact calibration.  The calibration
is external arithmetic; no native identity is created.

## 2. Imported knowledge

- `RelationCellV0` and `RelationProfileV0::braid_m6()` fix the cell to exactly
  the two three-step words `[a,b,a]` and `[b,a,b]`.
- `RelationFillingV0::Open` is the pinned state of the PR-16 cell.
- ADR 0022 records that V0 has no event re-enabling or feedback semantics.
- `docs/SEMANTIC_SCOPE.md` excludes recursion, cyclic modules and stable
  feedback, and walls off the bounded data-machine profile.

No imported result licenses a continuation operation on the existing objects.

## 3. Interface

The profile declares a new carrier: a *declared continuation* is a finite
sequence of (legality predicate, appended step, boundary rule, fresh occurrence
identity, filler decision).  What is translated in is the recorded path; what is
**not** translated is mechanism execution, provenance authentication, or the
open semantic filler.  The equality used is equality of the declared
continuation word, not equality of any native object.

## 4. Protected obligations

- the two PR-16 mechanism words stay distinct literals;
- `FrameIdV0` is never reused;
- the open filling stays open unless a filler is supplied;
- no `SourceId` or `OccurrenceId` is allocated;
- the existing frozen audit and evidence are not rewritten.

## 5. Acceptance and verification

Candidate family: finite continuation words up to a declared depth over the
declared legality.  Checker: an exact external checker over the declared model.
Negative controls: an illegal action accepted; a reused frame id; a step appended
past the fixed three-step braid word; a carried-over filling; a boundary mismatch.
Success condition: the declared word semantics is deterministic and its legality
is decidable at the abstract level.  Unresolved outcome: the open filler.

A calibration model already exists and declares all five semantics: experiment 2
of the AEG process-representation gap programme, with its frozen contract,
its independent checker and its evidence.

## 6. Resources and exit

Bounds: continuation depth, word length, and a finite checker budget declared
before the run.  Exit: a checked witness, a checked counterexample, a completed
declared finite search, a resource limit, an invalidated assumption, a checker
failure, or an explicit stop.  No automatic refetch or enlargement.

## Nonclaims

This profile does not implement continuation, does not execute
`compute`/`verify`/`learn` mechanisms, does not close the M6 semantic filler,
does not authenticate recorded output, and does not extend PSC0.
```

## Regression condition

The gap claim is falsifiable by the repository it describes: if a pinned Adva
operation later appends a step to a `FrameRelationPathV0`, or composes two
`RelationCellV0`, then
`experiments/adva_continuation_interface.py` exits nonzero on
`ADVA-CELL-OPS` or `ADVA-PATH-MISSING` and this proposal must be withdrawn.

## What is explicitly not requested

No Rust type, no CLI verb, no `SourceId`/`OccurrenceId` allocation, no change to
`adva.ir`, no change to any frozen artefact, and no promotion of the profile out
of research status. The profile is a specification, and the plan that produced
it grants no authority to publish or merge new research.
