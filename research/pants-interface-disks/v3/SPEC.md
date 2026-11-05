# OQ-096 V3 — pre-execution finite specification

Date: 2026-11-05. Baseline: a1b203e32fa7012a8749328f39a85dd524eb3842.
This file and contract.json are committed before implementation/execution.
Human direction: Mingli Yuan. Formalization: Codex (OpenAI).

## 1. Typed blocks and composition convention

B compose A means execute A then B. Use exact rational arithmetic:
Q(x,y)=x+y; P(z)=4z; R(w)=1/w, with dom R = Q \ {0}.
P retains its explicit second input t from common:t=4, as in V1/V2.
R retains ordered inputs [u,w], u from common:u=1: w is input slot 1.
Thus Q:Q^2->Q, P:Q->Q and R:Q\{0}->Q. The effective program is
v = 1 / (4(x+y)), defined exactly when x+y != 0.
The underlying three-gate graph is a chain; no new geometric thickening is claimed.

The two constructions are (R compose P) compose Q and R compose (P compose Q).
An intermediate R compose P is an OPEN fragment at z. It must retain a symbolic
nonzero guard on the denominator input of R; it must not demand a supplied z,
drop the guard, or execute R before P. Bracketing is construction order.

## 2. Finite decorated records

A fragment is (E,O,B,L,G,In,Out). E is the finite map of production events,
with operation, immutable gate-source, ordered ports and rational type.
O is its finite map of ports, each with a role, slot, direction, event and
occurrence ID. B is the finite set of directed output/input bindings; its two
endpoints remain distinct occurrences. L binds external inputs to immutable
source records where supplied. G lists denominator guards. In and Out are the
live unbound ports, ordered by the contract's block/slot order.

All event/port occurrences are allocated once, at leaf instantiation under
the caller's expected request scope. Domains of event and port maps are
disjoint across leaves; source keys may be shared only as the caller permits.
A source identity is not an occurrence, a numeric value or a gate occurrence.

Composition is a PARTIAL operation. Take disjoint event/port/source-binding
unions, retain old B and G, add the declared cross-operand wires, recompute
In/Out, and reject duplicate identities, type/slot mismatch, non-linear use,
missing required ports or directed cycles. No port quotient is performed.
Input substitution is structural; concrete evaluation happens on a complete
request. Intermediate open ports are legal, missing required final inputs are not.

A complete receipt retains that graph and the replayed ordered event trace.
Each trace item includes event identity, gate-source, operation, ordered
operand values and result. Source observation may erase scope/occurrence
SPELLINGS only after roles, incidences and expected request are checked.
Numeric observation is (z,w,v) on successful runs; failure preserves a separate
domain-rejected judgment and the replayable graph, never a value at infinity.

## 3. Proposed bounded propositions (proof obligations before experiment)

F1. For these three leaves with fixed pairwise-disjoint occurrence domains,
unchanged source records, the two declared typed wires, and complete retained
graphs/guards, the two bracketings give identical canonical graph records and
the same strict partial numerical function.

Proof: both contain exactly E_Q disjoint-union E_P disjoint-union E_R,
all nine ports, both bindings, all four external source bindings, and the one
R-denominator guard. Union is associative on these disjoint domains and the
inserted edge set is independent of join order. Boundary ports are a function
of this same union. The directed graph has the sole execution order Q,P,R.
Deterministic replay yields z=x+y,w=4z, then v=1/w exactly if w!=0. Since 4!=0,
both domains are x+y!=0. No schedule/general thickening theorem is used.

F2. Numerical equality does not imply source-bound admissibility.
Replace A:x by C:x at Q slot 0, retaining value 2, A:y=3 and all operators.
Both produce (5,20,1/20), but a caller expecting A forbids the source C:x.
One changed source binding suffices; the obstruction already exists at one
input slot. Minimality here counts changed bindings, not all possible languages.

F3. Lossy residual composition need not be associative. Define a deliberately
bad algorithm that preserves the full numerical graph but replaces the audit
ledger at each join by ONLY the new cross-operand seam. The left bracketing
retains {Q->P}, the right retains {P->R}; both have v=1/20. There is no
role-preserving equality of those ledgers. Three leaves/two seams is minimal
for this bracketing witness (one/two leaves have no alternative binary tree).
This is a counterexample to numerical associativity being sufficient, not
a counterexample to F1 or to any frozen V1/V2 implementation.

Information, rather than this literal serialization, is necessary: a lossless
compressed history with a verified decoder could satisfy the same contract.

## 4. Acceptance and rejection fixed in advance

Positive cases: five V2 assignments extended by R, including A-copy with
new occurrence IDs but reused sources; all 36 ordered inputs from
{-2,-1,0,1,2,1/2}. Check graph, slots, source identities, occurrence freshness,
trace, guard, boundary and numerical equality separately for both bracketings.
Both constructions must reject each zero-denominator input.

Enumerate the 14x14 registered source pairs in each of the five V2 contexts.
Rebuild internally consistent arithmetic histories; reject every pair except
the caller-bound one, even if all declared numeric values remain unchanged.
Independently inspect all 18 possible single extra output/input edges:
topological legality alone must not authorize reuse, aliasing or feedback.

Rejection conditions are in contract.json. Check actual saved receipts against
an out-of-band request, not an identity selected by packet labels. Validate
arithmetic and source records, not merely a digest. Include fully rewritten
foreign requests, scope collision, bool-as-slot, wrong R slot, missing production
history, missing prior seam, dropped guard, strict zero domain, and malformed
saved-evidence/JSON controls. Exact bytes of all existing V1/V2 files are pinned.

## 5. Claim boundaries and manuscript decision

F1–F3 can become finite propositions only with explicit definitions and proofs.
Enumeration is a separate computational example. Neither proves invariance
under arbitrary DAG decomposition, canonical alpha transport for dynamically
allocated names, copying/sharing/discard, feedback semantics, geometric
thickening functoriality, AES extension, spectrum correspondence or native
Adva Seal. No Adva API is invoked.

After execution, assess a narrow Paper I proposition with the assumptions of
F1 and the counterexample F3. Keep actual manuscript integration separate from
establishing eligibility: the user requested that assessment, not automatic
promotion of general OQ-096.1. No independent human review is asserted.
