# Finite process spectrum and cyclic-prefix calibration

Date: 2026-10-10. Research direction: Mingli Yuan. Authored and checked by
Codex (OpenAI); account use does not constitute human review.
Status: bounded research record, proofs and independently authored examples.
Baseline: `mountain/aeg-paper@735695cbc7ce512a1cd5e188577613eda4b3083c`
(merged PR #16). Its evidence, projection definitions and impossibility result
remain unchanged. No manuscript theorem or release artifact is replaced.

## Authority and scope

Canonical upstream reference:
`mountain/adva@1b9bd090b2c4710916b6a0ccca0ad88fb7d323bd:docs/research/0005-causal-cut-alexandrov-topology.md`.
Git blob `de71e5890f064cf3ccac121d1fbad634fe560b64`.
This source motivates the lower-open convention and decorated frontier. The
present graphs are synthetic, independently calculated examples; they are not
Rust-checked Adva diagrams. No upstream executable or digest protocol is rerun.
The existing PIV-S5/S6 observation/update criteria govern interpretation.

Allowed changes: this note, its standalone verifier and evidence, status and
Paper IV entry points, and one CI replay step. Forbidden: all frozen PR #16
and ported-program evidence, native Adva semantics, Paper 0/I/II/III sources,
and existing manuscript claims. No material is relocated.

## Specified operators and exact counterexample

Let E={a,b,c}, with immutable event marks. C has cover edges a->b, b->c;
F has b->a, b->c. The event order is reflexive transitive reachability.
The operator here is the **unweighted undirected cover-graph** Laplacian,
not the Laplacian of the transitive closure or a directed weighted operator.
Rows and columns use a,b,c. Both give

    L = [[1,-1,0],[-1,2,-1],[0,-1,1]].

Its characteristic polynomial is det(tI-L)=t(t-1)(t-3); all eigenvalues
are exactly 0,1,3. The verifier derives the polynomial from integer principal
minors and determinant, without floating eigensolvers. These graphs have the
same full undirected operator, so retaining its eigenvectors also cannot
recover the discarded orientation.

| Object | C | F |
|---|---|---|
| Strict order | a<b, b<c, a<c | b<a, b<c |
| Lower opens | empty, {a}, {a,b}, E | empty, {b}, {a,b}, {b,c}, E |
| Open count | 4 | 5 |
| Ideal size polynomial | 1+t+t^2+t^3 | 1+t+2t^2+t^3 |
| Directed cover adjacency characteristic polynomial | t^3 | t^3 |

**PS-1 — proved with stated hypotheses.** Neither the specified undirected
Laplacian spectrum nor the directed adjacency eigenvalue multiset determines
the marked causal poset on this two-element model domain.
Proof: equal spectra above have different orders (also different numbers of
opens, hence nonisomorphic posets). The directed adjacency matrices are
strictly triangular after topological sorting, hence nilpotent. This last
argument applies to every finite DAG's adjacency matrix, but says nothing
about other directed operators or spectral data carrying marks and products.

## What recovers what

**PS-2 — proved with stated hypotheses.** For a finite poset P, its full
lower-open family on a marked event carrier determines its marked order by

    x <= y iff every open containing y contains x.

Proof: lower closure proves the forward direction. If x is not below y,
the principal ideal down(y) separates them. This orientation convention is
explicit; no opposite specialization-order convention is imported silently.

The abstract lattice J(P), retaining meet/join/order but forgetting event
marks, determines P up to isomorphism: its nonempty join-irreducibles are
exactly the principal ideals. A principal ideal cannot be a union of two
proper ideals because one must contain its generator. A nonprincipal ideal
has at least two maximal elements and is a union of proper ideals generated
by them. Inclusion down(x) subset down(y) is equivalent to x<=y. This proves
the reconstruction without assuming a classification theorem.
The checker independently identifies irreducibles using all pairwise joins
and verifies both reconstructions on all 19 labelled three-element posets.

| Candidate data | Sufficient information | Loss/boundary |
|---|---|---|
| Undirected L spectrum, even full L | Specified undirected observation | Orientation erased before eigenvalue extraction |
| Directed adjacency eigenvalues | Nilpotence in this DAG class | All eigenvalues zero; no causal reconstruction |
| Count or ideal size polynomial | Separates C and F | Chain and marked reversed chain collide |
| Full opens with membership and event marks | Exact marked poset | No wire multiplicity, source ancestry, operation or role labels |
| Abstract distributive lattice with operations | Poset up to isomorphism | Literal event marks lost |
| Labelled incidence/zeta matrix | Exact marked order | Linear encoding is faithful; its eigenvalues alone are all 1 |
| Full typed, endpoint-marked wire frontiers over opens | Stated port and source records | Needs extra records; not an earned presheaf/gluing law |
| Nonlinear Laplacian eigenvalues | No construction tested | Must specify operator, domain, normalization and reconstruction target |

The zeta statement follows from zeta(x,y)=1 iff x<=y: after topological
sorting it is upper triangular with diagonal 1. Thus a linear carrier can
retain order while its eigenvalue-only observation loses it. The ideal size
polynomial is a combinatorial lattice summary, not a nonlinear spectrum.
Its coefficient counts also agree on any marked poset and its relabelling;
the reversed marked chain is the explicit negative control. No necessity of
nonlinearity or general impossibility theorem for modern spectral theory is
claimed. An Alexandrov-based spectral object remains a structural proposal:
its multiplication/incidence, marking and decorated boundary must be specified
before a fidelity claim is meaningful.

## Sources, occurrences and boundary data

For each U the script lists wires whose producer is an external input or an
event in U and whose consumer is outside U or an external output. Each wire
retains producer, consumer, occurrence ID, immutable source ID, Q type, slot
and role. External input/output wires are included. This is the Research 0005
frontier convention on synthetic packets, not checked native authorization.

For example the C frontier at {a} is a->b; the F frontier at {b} contains
b->a and b->c. Independent sharing controls hold F and both occurrences fixed:
the two packets have either sources (s0,s0) or (s0,s1), with equal Q values
at s0 and s1. Source IDs are declared ancestry metadata, not event-order data.
The unadorned topology and all its lattice invariants coincide; decorated
frontiers separate shared from independent origins. The script checks that
only the source fields change. These controls are distinct from the earlier
default graph boundary packets, whose sources name synthetic producer sites.

For a finite loop-free wire system between comparable distinct events,
complete frontiers recover every wire: an event-event wire x->y crosses
down(x); input wires cross the empty cut and output wires the full cut.
Endpoint/occurrence/source/type/slot/role fields must all be retained. This
does not recover event operation bodies, internal hidden state, or wire-free
annotations. It is not a proof of a faithful reconstruction of arbitrary
program semantics, nor a transport/coherence theorem.

## Minimal cyclic anytime model

**Definition (synthetic test machine).** One control location has a self-loop
tick on state x in N, initially 0. Each tick sets x:=x+1 and emits a packet:
history=[0,...,k], result=k+1, evidence={checked_steps:k+1} after tick k.
The evidence is a generated record, not an independent proof certificate.
Each tick has two fresh occurrence labels and declared equal-valued zero
source slots, with shared ancestry s0/s0 or independent s0/s1. These are
metadata controls; they do not alter the increment transition.
This is minimal in control locations; its data state is infinite. It is not
a finite-state recurrent machine and is not an implementation of Adva.

Unfolding n ticks creates distinct events e0,...,e(n-1), a chain with n+1
lower opens. Edges run from one occurrence to the next; an event does not
execute repeatedly. The control transition tick executes repeatedly. At
horizons 0,1,2,3,6 the checker verifies prefix-compatible packets and order.
It rejects treating the self-loop control graph as a DAG event graph.

**PS-3 — proved with stated hypotheses.** No fixed finite prefix determines
whether this observed execution continues indefinitely within the class of
machines that may stop after that prefix.
Proof: for every n, compare the loop with a machine carrying a counter that
halts after n ticks. Their first n packets and unfolded event DAGs agree;
their enabled future tick differs. No function of this prefix can distinguish
their continuation behavior. The script checks the indicated horizons; the
quantified proof is the construction for arbitrary n. This is about recovering
unknown systems from prefixes, not about executing a known transition rule.

| Distinction | Retained by decorated finite unfolding | Extra information for continuation |
|---|---|---|
| Event order | Order between observed occurrences | Future enabling and causal dependencies |
| Repetition | Different occurrence IDs with common tick label | Transition rule, recurrence and stopping policy |
| Source identity | s0/s0 versus s0/s1 | Immutable ancestry propagation policy |
| History | Complete emitted prefix | Observation and update laws |
| Three output roles | Explicit history/result/evidence keys | Native role types, validators and feedback routing |

At the same control location, one tick and three ticks have different histories
and results. Quotienting occurrences to the tick label therefore fails the
output-factorization condition PIV-S5 for this observation. Swapping the
history and evidence keys preserves values as an unordered collection but
changes the role-aware packet; source substitution preserves all result
values but changes ancestry. Both are executed negative controls.

A fixed DAG faithfully describes this finite prefix under its declared
observations. It omits the continuation rule, terminal-versus-truncated status,
and repeatability unless they are separately attached. The compatible union
of all unfoldings is the infinite chain N; it recovers this run, not all
counterfactual transitions or alternative inputs. Known update rules plus
frontier state can compactly generate the next prefix, but history-observing
output is not reduced to a finite control label. General cyclic systems may
need guards, external inputs, branching and fairness assumptions. None is
silently inferred here. Native Adva three-side feedback and AES realization
remain PIV-F2 open obligations.

## Reproduction, acceptance and next experiment

    python3 paper-4/scripts/verify-process-spectrum.py > /tmp/process-spectrum.json
    cmp /tmp/process-spectrum.json paper-4/scripts/fixtures/process-spectrum/evidence.json
    python3 -O paper-4/scripts/verify-process-spectrum.py > /tmp/process-spectrum-O.json
    cmp /tmp/process-spectrum.json /tmp/process-spectrum-O.json

Checks use explicit exceptions and exact integers; optimized execution retains
the checks. Evidence includes every open, marked causal pair and decorated
frontier of the three models, the 19-poset census, source controls and all
tested unfoldings. CI replays and byte-compares evidence in both modes.
Existing finite verifiers are rerun separately; unchanged frozen evidence is
byte-compared. No LaTeX is edited or PDF produced locally; the existing CI
still builds Papers 0, I and IV. Human diff review and manuscript promotion
remain pending; no release declaration is made.

Next: take one native cyclic three-side trace with explicit restart/continuation
contract and source/role validators; test whether a proposed finite decorated
feature has a right-congruence kernel and output factorization. Separately
specify a directed Alexandrov/incidence operator with its full observation
policy, then search collisions beyond the three-event carrier. Developing a
nonlinear eigenproblem before choosing that observation policy would not
resolve the information-loss question.

## Independent review and executable guard repair (2026-10-10)

Review baseline: PR #17 head `ff262a77accf0a7ee894d9ffbfeec571bc6e33fb`.
The original prefix-only stopping assertion did not execute the next attempted
transition, and its future-enabling flags were literals. This was a software
coverage gap, not a counterexample to PS-3's independent quantified proof.

The producer now includes a separately implemented guarded counter machine.
Its finite control has the explicit tick guard `limit is None or x < limit`;
a refused tick leaves state and emitted history unchanged. At each horizon
0,1,2,3,6 both machines attempt n+1 ticks: their first n emitted packets agree,
but the loop emits e_n while the stopping machine records a disabled attempt
at x=n. Future-enabling flags are derived from the executed contract. At n=0
the stopping machine is terminal initially. Observation budget is separate
from the stopping limit. The data counter remains unbounded for the loop;
“finite machine” here means a finite transition specification and finite test,
not a finite-state implementation of this unbounded history semantics.

`receive-process-spectrum.py` imports no producer code. Its reference inputs
are the declared test horizon, stopping limit, ancestry-sharing and role
policies, rather than a receipt's self-claimed contract. Closed-form expected
histories and explicit attempt records verify 30 receipts. Equal-valued source
substitution and role exchange are also accepted under their own declared
contracts, and rejected under the original contract. Complete means the known
guard disables tick; truncated means observation ends while tick remains
enabled. Complete does not certify unspecified external/native transitions.

The receiver enumerates relations by 27 independent pair orientations and
filters transitivity, rather than taking closure of 64 graphs. It finds all
19 posets, reconstructs membership order, and identifies join-irreducibles by
unique lower covers rather than pairwise joins. Exact determinants at the
three distinct roots 0,1,3 establish the monic cubic characteristic; covers,
marked orders, opens and rank counts are independently checked.

It rejects 62 mutated receipts: missing stopping guard (at all five horizons,
explicitly shown to survive the old prefix-only check), forged enabling/status/
state/attempt records, source substitution, exchanged roles, lost history,
duplicate occurrences, foreign predecessor, altered result/evidence, deleted
event, and truncated observation claimed complete. The mutation list and
normal/optimized receiver output are frozen separately in
`paper-4/scripts/fixtures/process-spectrum/receiver-evidence.json`.

These checks are independent algorithms by the same AI author, not independent
human review or native authorization. Source IDs retain declared synthetic
ancestry; they do not authenticate external source bytes. PS-3's indistinguish-
ability is only for the packet/event-prefix observation: when the observer is
also given the transition contract or truthful terminal status, the two
machines are distinguishable. This repair adds no general Adva anytime theorem,
no infinite execution certificate and no manuscript claim.

Local acceptance: both scripts agree byte-for-byte in normal/optimized modes;
139 compactification checks and all seven Paper IV groups pass; ported-AES and
PR #16 opposite-feature fresh evidence match their unchanged frozen bytes.
No LaTeX changed; PDF builds and warning checks are delegated to remote CI.
PR remains Draft/Open; this AI audit is not human approval. Merge requires
Mingli Yuan's separate explicit approval for the reviewed final head.
