# 00 — Interface promotion proposals (work plan §10)

Work-plan section 10:

> Process Geometry 优先承载非算术过程、继续等价与对象化实验；Adva 承载与原生程序核心实际接口有关的实现；aeg-paper 承载经治理审查的数学状态和跨仓库见证。不要一次跨三个仓库改动稳定接口。先完成研究证据，确有必要再提出接口晋升。

And the limit this section carries:

> 本计划本身不授予发布或合并新研究的额外权限。

**Nothing below has been applied.** All three sibling repositories are
untouched. `tools/build_interface_promotion.py` emits the proposals with
`"applied": false` and refuses to emit one that claims otherwise; it also
re-reads and re-tests every verdict each proposal cites, so a proposal cannot
drift away from the finding that motivates it. The generated artefact is
`evidence/interface-promotion.json`.

Three promotion paths, one destination each, deliberately **not** attempted in
one cross-repository change.

## P-AEG-1 — aeg-paper: register the findings, promote nothing

| | |
|---|---|
| target | `governance/process-representation-gap-2026-10-10.md` |
| status rows | `governance/05-mathematical-status.md` |
| kind | additive governance status record |
| precedent | `governance/opposite-feature-witness-2026-10-09.md`, added by PR 16 |

PR 16 registered a finite snapshot witness as a governance record without
touching any theorem. This programme has the same shape and should be registered
the same way: a new governance document citing the frozen contracts, the
evidence hashes and the gap taxonomy, with status rows for the findings that are
genuinely new relative to the existing register.

**What it adds.** A hash-pinned, reproducible record of where six declared
representations stop being sufficient, with the cost of each candidate and the
exact witness — the thing an auditor of `PIV-F2` would otherwise have to
reconstruct.

**Cost.** One governance document. No runtime cost, no API, no change to the
paper build.

**What it does *not* do.** It does not close `PIV-F2`. `chi_T` and `chi_S` still
have only two-record sample consistency, and no experiment result is promoted to
a theorem.

**Regression condition.** Any cited evidence file changing its SHA-256, or any
cited verdict changing value. Both are re-checked on every run.

**Review gate.** Repository governance under `AGENTS.md`; no automatic merge.

## P-PG-1 — process-geometry: a workstream, not an API

| | |
|---|---|
| target | `workstreams/process_representation_gap/` |
| kind | research-local workstream; no `src/` change, no public API |
| precedent | `workstreams/native_method_firewall/` (README + one module + one external test); `workstreams/am_weight_compiler/` for the frozen-contract and disposition schema |

Section 10 assigns the non-arithmetic process, continuation-equivalence and
objectification experiments to Process Geometry. Its repository documents the
workstream convention by example rather than in prose, and the smallest complete
example is a README, one module and one external test — so the promotion here
can be small.

**What it adds.** The declared typed feedback machine, its exact continuation
quotient, the one-field enhancement grid, the reserved verification family, and
the gate-by-gate elevation criterion.

**Interface pressure actually observed — and it is *not* a change request.**
`process_geometry.experimental.minimize_finite_task_process` was reused
**unmodified** as an exact oracle by experiment 2's independent route, deciding
the same two properties by a different algorithm (stable partition refinement,
no continuation-depth cutoff) and agreeing with the primary on all five
representations and both shortest witnesses. The promotion signal is therefore
*"this experimental entry point is reusable as-is, and here is what it was used
for"* — not *"change it"*. That is recorded as evidence supporting the existing
API, not as pressure to widen it.

**Cost.** Research-local only; workstream-internal tests are not collected by
the repository's root suite, so nothing in the existing CI changes.

**What it still fails.** The exp5 Artin object is a quotient, not an elevation,
so no new rank is claimed anywhere. No general theorem is asserted; the
enhancement grid is bounded to its declared domain.

**Regression condition.** The workstream must reproduce the recorded numbers
from the pinned commit; a mismatch against
`evidence/exp2-loop-continuation.json` is a failure.

**Review gate.** Repository governance; the workstream must declare a claim
ceiling, as its richer examples do.

## P-ADVA-1 — adva: a new declared profile, never a silent PSC0 extension

| | |
|---|---|
| target | `docs/research/<NNNN>-declared-continuation-profile.md` |
| companion | `experiments/<name>/contract.json` |
| kind | new declared research profile |
| precedent | `docs/research/0129-bounded-breakthrough-trusted-boundaries.md`, which fixes the six-part bounded-run contract template |

`experiments/adva_continuation_interface.py` establishes from the Git object
store, by 23 re-checked facts, that the pinned source supplies **no** native
legal-continuation interface for a relation path or a relation cell:
`RelationCellV0` exposes only `{new, check, transport}`, `transport()` refuses an
open filling, `check_braid` fixes exactly three steps, ADR 0022 rejects
frame-id reuse for iteration, and PSC0 excludes recursion, cyclic substitution
and stable feedback.

**What it adds.** The five semantics a downstream experiment must invent, stated
explicitly: a legality predicate on these records; an append/step/gluing
operation on `FrameRelationPathV0` or `RelationCellV0`; a boundary-agreement
rule for an appended step; an identity policy that does not reuse a
`FrameIdV0`; and a filler/transport decision. Experiment 2's model already
declares all five and can serve as the calibration.

**Cost.** One research note plus one bounded-run contract. No Rust type, no
`SourceId` or `OccurrenceId` allocation, no change to PSC0, and no change to any
frozen artefact or historical evidence.

**What it still fails.** It does not implement continuation — the profile is a
specification. It does not execute `compute`/`verify`/`learn` mechanisms, which
matches the existing declared boundary rather than extending it.

**Regression condition.** If a pinned Adva operation later appends a step to a
`FrameRelationPathV0`, or composes two `RelationCellV0`, the gap claim is
falsified and the probe exits nonzero. The claim is therefore falsifiable by the
repository it describes.

**Review gate.** Repository governance; the profile must declare its own scope
and claim ceiling, and must not present itself as PSC0.

## What was deliberately *not* proposed

* **No change to any stable interface.** The only `src/` entry point involved
  (`minimize_finite_task_process`) is reused exactly as it stands.
* **No new Rust type, no new public API, no new package abstraction.**
  `Objectification`, `ProcessRank` and `RankLowering` remain deliberately absent
  from Process Geometry, and the work plan forbids building a generic rank API.
* **No manuscript change.** No LaTeX file, label, notation, theorem or status
  row is touched by this branch.
* **No promotion of any research result to a theorem.** Every finding keeps its
  declared status and its declared domain.

## Ordering

The three proposals are independent and can be reviewed in any order, but the
intended order is: **P-AEG-1 first** (it registers the cross-repository
evidence), then **P-PG-1** and **P-ADVA-1** in whichever order their own
governance prefers. Applying any one of them does not require the others, and
this branch requires none of them.
