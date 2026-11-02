# OQ-100.7 finite native acceptance contract v1

Status: research-only; first-party implementation under this repository's CC0.
Author: Codex (OpenAI), through Mingli Yuan's authorized account proxy;
account use is not his authorship, review or guarantee.

## Question and scope fixed before execution

Does the fixed three-context free history with chronological slot word (1,2,1),
all operations multiplication by -1, admit a native one-hole, three-event chain
whose exact schedules, dependency order and inversions match its expression tree?
Can a saved candidate be independently replayed, and can incorrect slots, illegal
schedules and substituted identities be rejected? What changes when constants
are emitted as events instead of the fixed unary `neg` realization?

Theorem 5.2 is an abstract sequential theorem, not a claim that every native
lowering preserves it. This adapter covers only the two explicitly named
contexts z*(-1) and (-1)*z. Both realize as `neg`, but their call names, graft
frames and source program remain distinct. No general tree assignment is
assumed or implemented; no primitive or native schema is modified.

Allowed: this research directory, its CI workflow, OQ-100/PVI status and
provenance entries, and narrow Paper VI status text. Forbidden: changes to
Papers 0--V, old evidence, Adva source/locks or mathematical theorem statements.
Theorem nodes 5.2/5.3 retain PROVED (sequential abstract)/CONJECTURE respectively.

## Authority and identities

Adva is an external software dependency at the full revision in sources.json; the replay runner checks its clean checkout;
Cargo.lock pins transitive dependencies. It is not vendored or relicensed.
Rust parsing/linking/compilation allocates semantic IDs. Stored diagrams enter
through `import_diagram_json`; grafts are rechecked with
`analyze_program_slice_with_graft`. The receiver also compares the full artifact
with fresh compilation of the fixed source: generic diagram validity alone
cannot authenticate a candidate's provenance. Python reads emitted JSON only
as an independent combinatorial oracle; it creates no semantic identity.
The tree-to-node association is derived from the checked graft body regions and
wire dependency, never from equal scalar values or assumed NodeId numbering.
Slots are declared data read from fixed callee names, not inferred from values.

## Budget and checks

Two fixed positive constructions: 3 and 6 native events, one input hole each.
Enumerate all 3! + 6! = 726 event permutations; at most 4,500 native advance attempts
per produce/receive pass, including canonical certificates and negative controls;
an atomic counter enforces this cap. Enumerate the tree's 3! orders independently. Keep
all accepted words and canonical step certificates. Fixed mutation controls
only; no adaptive search or scope expansion. Process timeout 300 seconds per
replay (compilation separate); max fixture input 1 MiB. Reject missing/extra
nodes, steps, incorrect source identities and mismatching reports. Failures
stop the command; noncompletion is Unknown, not evidence of nonexistence.

Rust derives edges/closure from checked wires and tests permutations using
native `advance_causal_cut`. A separate Python oracle enumerates extensions,
computes the tree hook-length count and minimizes inversions. Normal/optimized
Python and debug/release Rust outputs must agree. A fresh receiver reimports
saved artifacts and recomputes the finite report. No certificate boolean is
accepted merely because it was stored.

Build if manuscript source changes: `./build.sh 6`; inspect errors, references,
citations, duplicate labels and expected PDF. Existing 193-tree calibration
must replay unchanged. CI repeats native replay, reception and oracle tests.

## Residual gates

OQ-100.7 remains OPEN. Do not run the full 193-tree native census until a
branching assignment and event-granularity contract exist. Schedule count
requires an event bijection/order isomorphism or an explicitly justified
alternative notion of schedule (not silent deletion of constants). Carrier
check requires a three-plane carrier, signed action, chosen plane alignment,
transposition action and a certified map from actual program data. Neither
native Real wires nor a slot string supply those structures by themselves.
