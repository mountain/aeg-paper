# OQ-100.7 — first native sequential fixture

**Status:** COMPUTATIONALLY VERIFIED EXAMPLE; OQ-100.7 remains OPEN.
**Date:** 2026-11-01. **Author:** Codex (OpenAI), through Mingli Yuan's
authorized GitHub account proxy. Account use is not his authorship, technical
review or correctness guarantee. Producer and checkers have the same model
author; independent execution and a separate combinatorial implementation are
not independent human review.

## Result

The fixed free expression is `((-1) * (x * (-1))) * (-1)`. Reading from the
hole outward gives contexts with slots `(1,2,1)`, each multiplying by `-1`.
The initial mark is absent. The tree vertices in corner order are
`[v0,v1,v2]`, with direct dependencies `v2 < v1 < v0`.

The named Adva one-hole functions `mul-m1-s1` and `mul-m1-s2` both contain one
native `neg` operation. They declare, respectively, `z*(-1)` and `(-1)*z`.
The checked call history and graft frames retain the signature distinction;
the operation graph alone loses it. This is a **fixed two-context research
adapter**, not a native Paper I signature API or a lowering for all arithmetic
contexts. It adds no stable primitive, certificate type or IR schema.

| Quantity | Expression tree | Named unary-context program | Explicit constants + binary `mul` |
|---|---|---|---|
| Internal vertices / native events | 3 | 3 | 6 |
| Strict dependency pairs | 3 | 3 | 9 |
| Linear extensions / native schedules | 1 | 1 | 15 |
| Canonical order | `[v2,v1,v0]` | `[0,1,2]` | `[0,1,2,3,4,5]` |
| Corner order | `[v0,v1,v2]` | `[2,1,0]` | `[5,3,0,2,1,4]` |
| Minimum inversions | 3 | 3 | 9 |

The checked association is `v2 -> 0`, `v1 -> 1`, `v0 -> 2`, recovered from
wire dependencies and graft body regions. No equality is inferred from
values, matching node numbers in different diagrams, or compiler emission
order. The tree's hook-length count is `3! / (3*2*1) = 1`.

All 6 permutations of the unary program and all 720 of the expanded program
are tested by `advance_causal_cut`; 5 and 705 are rejected, respectively.
There are 1,389 actual advance attempts per producer/receiver invocation,
under an enforced cap of 4,500. Frozen evidence retains both compilation
artifacts, exact grafts, every legal schedule, strict orders, the canonical
step/cut certificates, the mapping and rejection reasons. It is 69,909 bytes.

The expanded program is a useful **rejected candidate for literal schedule
preservation**, not a counterexample to Conjecture 5.3 or Theorem 5.2. Its
arithmetic events are `[2,3,5]`. All 15 native schedules project to that one
word after constant events are forgotten. A 15-to-1 projection is not a
schedule bijection. We retain that fibre instead of counting its image as the
native schedule count. No quotient schedule or atomic-call semantics is
installed to repair the mismatch.

## Reproduce and receive

Use sibling checkouts named `aeg-paper` and `adva`; check out the latter at
`87a1a6933bca3fdb5c176cbf612729e278d172f7`, without submodules. Then, from
`aeg-paper`:

```bash
python3 research/program-side-fixtures/replay.py
```

Rust 1.94.0 with rustfmt/clippy and Python 3.10+ are required. The runner
verifies Adva's exact clean source checkout before building the path
dependencies. `Cargo.lock` fixes transitive versions; source references and
byte/blob hashes are in `sources.json`. Existing manuscript imports at
`adva@1b9bd090...` remain historical imports; this fixture explicitly tests
the later revision above and does not silently update them.

The runner performs two Rust tests, formatting and Clippy, debug/release
byte-identical production, fresh-process native reception, normal/optimized
Python cross-checking, six saved-candidate mutation refusals, and byte replay
of the existing 193-tree calibration. It never overwrites evidence. Direct
inspection commands after the build:

```bash
research/program-side-fixtures/target/debug/aeg-oq1007-native produce > /tmp/oq1007.json
research/program-side-fixtures/target/debug/aeg-oq1007-native receive /tmp/oq1007.json
python3 research/program-side-fixtures/verify.py /tmp/oq1007.json
```

Rust owns compilation, identity, diagram import, graft validation and legal
causal advances. The Python oracle only reads checked exports and independently
enumerates permutations, computes closure, the hook-length product and
inversion minimizers. Its success alone does not authorize a semantic object.
The native receiver compares the complete saved artifact against fresh
compilation of the fixed source, then compares the recomputed report. Generic
diagram validity cannot authenticate a receipt's source. Stored `certified`
flags are never accepted as evidence without recomputation.

## Refusal layers

Nine controls run inside each native report:

| Control | Actual refusal layer |
|---|---|
| Change middle slot 2 to slot 1, retaining the same `neg` graph | Research signature binding against checked graft names |
| Execute event 1 before event 0 | Native causal-step checker |
| Repeat an event | Native causal-step checker |
| End after two of three events | Research complete-schedule check |
| Use an unknown event | Native causal-step checker |
| Substitute an occurrence in a wire | Native diagram importer |
| Substitute a source in the occurrence table | Native diagram importer |
| Supply a valid foreign program with the same NodeIds | Research exact-source binding after successful native validation |
| Change an ordered graft-hole wire | Native graft revalidation |

The wrong-slot program is a valid different Adva program. Adva is not claimed
to know our Paper I slot vocabulary. The receiver separately refuses six
edited saved files: invented count, missing schedule, reversed canonical
word, wrong slot receipt, occurrence replacement and source replacement.
The first four also fail the Python oracle in normal and optimized modes.

## Can this extend to the 193-tree census?

Not as a completed general assignment. A read-only classification of the
existing catalogue gives:

| Internal vertices | Trees | Single-spine shapes | Branching shapes |
|---|---:|---:|---:|
| 3 | 5 | 4 | 1 |
| 4 | 14 | 8 | 6 |
| 5 | 42 | 16 | 26 |
| 6 | 132 | 32 | 100 |
| Total | 193 | 60 | 133 |

These are unmarked shapes, not 193 program fixtures. The adapter has not been
run on the other 59 sequential shapes. A marked accumulator leaf and declared
signature must first be supplied even there. The 133 branching shapes require
an assignment with ordered holes and explicit subtree substitution; the unary
profile rejects a branching input. A six-event permutation cap must also be
revised before any larger native event set is enumerated.

**Schedule count still needs:** (1) an exact arithmetic-vertex/native-event
bijection, or a separately defined schedule notion with its own proof;
(2) preservation *and reflection* of dependency, including any additional
scope/source constraints; (3) corner/slot data recovered from the program;
(4) completeness of the legal-schedule enumeration; (5) compatibility with
subtree substitution; and (6) explicit treatment of constants, copy/discard
and sharing. The tree hook-length formula applies only to the specified tree
poset, not arbitrary DAGs. The current source has ordered input wires and
graft/cut operations, but no Paper I general context signature, no atomic
schedule event for a whole multi-event call, and no registered planar
tree-to-program assignment. `scale`, despite its name, is binary at this pin
and also emits a constant node when given a literal. An isolated `.ir.json`
diagram does not carry the complete graft companion by itself.

**Carrier check still needs:** a declared realization of the three oriented
planes `(T,SR)`, `(S,RT)`, `(R,TS)` on actual program data; a chosen alignment
and orientation; exact `J` actions; the cyclic-permutation and transposition
actions; and a certificate that the program map intertwines the sign law
on every plane, including transposition reversal. Slot names, `Real` wire
types, and the one-hole chain do not supply these structures. The bounded
three-source observer requires three sources and is not silently applied to
this one-source program. Carrier check is NOT RUN.

## Provenance, failures and manuscript effect

Source baseline: `mountain/aeg-paper@663b812d314a857ff3f041684b64e614bfc90d21`,
after PRs #22, #23 and #24; exact paths/hashes in `sources.json`. Native code
is linked as an external dependency, not copied or reinterpreted. The new
fixtures, adapter, oracle and report are original project contributions.

During preparation, a proposed `scale` shortcut was withdrawn on source
inspection because it is binary, before any positive result was claimed.
The first Cargo fetch also failed because Adva's inherited submodule URL was
not accepted by Cargo's git loader. The final reproducible route uses clean,
pinned sibling checkouts and no submodule; neither dependency source nor its
submodule configuration was changed. An initial fetch before `src/main.rs`
existed failed with "no targets specified"; it produced no finite evidence.

Only the fixture status sentences of Paper VI and OQ-100.7/PVI-12 are updated.
Theorem 5.2 stays proved on its abstract sequential domain; the new example
is finite evidence; Conjecture 5.3 stays unproved. No earlier paper is changed,
no material is migrated, and no general theorem or physical claim is added.
The next task is to specify event granularity and a smallest branching
assignment with retained planar slots before any full census.

## Validation record

- `replay.py`: PASS, including Rust's two tests, formatting/Clippy, native
  debug/release byte equality, fresh import/reception, normal/optimized oracle,
  nine internal and six saved-candidate refusal cases, and unchanged 193-tree
  calibration.
- `./build.sh 6`: PASS; refreshed `paper-6/aeg-paper-6.pdf`, 16 pages,
  447,182 bytes. No undefined references/citations, duplicate labels or
  overfull boxes. Five underfull bibliography boxes remain. Pages 14--15
  containing the changed status text were rendered and visually inspected.
- Static label/reference closure and `git diff --check`: PASS. Theorem 5.2
  and Conjecture 5.3 statements are byte-identical to the source baseline.
- Remote workflow results are attached to the PR's exact head and are separate
  from this local validation record.
