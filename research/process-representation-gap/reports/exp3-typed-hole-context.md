# exp3 — Typed hole filling and context

Work-plan reference: `AEG-process-representation-work-plan.md`, section 6, 实验三
(and section 4.2 task-relative sufficiency, 4.3 closed update, section 5 frozen
template, section 9 gap classification).

Governing interface: `paper-4/sections/05b-ported-aes-programs.tex` — strict
finite arithmetic networks, ordered typed boundaries, explicit copy and strict
discard, immutable source/occurrence identity, certified simultaneous
substitution with a graft receipt, the substitution–evaluation theorem, and the
feature-descent / online-update propositions.

## 1. Question

> Can two open processes that give the same output under one filling be
> replaced by each other in another legal context?

Answered here on a declared, frozen, finite domain: **no**. Value equality at
the frozen initial filling is never sufficient for contextual
substitutability, and the separation is computed exhaustively inside the
declared budget. The result is a `computationally-verified-example` plus a
`bounded-domain-compatible` sufficiency verdict for one candidate; it is not a
general theorem.

## 2. Frozen contract

* `research/process-representation-gap/contracts/exp3-typed-hole-context.v1.json`
* sha256 `bd7f958740b1c5d686da5012d59ec1995ad3c1f5af98bead0e3ee9637aa0eb8f`
* frozen (`contracts/FROZEN.sha256`) **before** the implementation was written;
  both checkers re-read the contract, re-hash it, and raise
  `EXP-CONTRACT-DRIFT` on mismatch. A negative control mutates a copy and
  requires that code.

**Interface fixed first (contract section (a))**

| Element | Declaration |
|---|---|
| Types | `Q` (exact rational), `CarrierID` (opaque label from `{L, M}`) |
| Holes | `h1..h4 : Q`, ordered; exactly one consumer per hole, via explicit copy |
| Output | `y : Q` |
| Primitives | `const_Q(c)`, `const_carrier(L)`, `add`, `sub`, `mul`, `div`, `copy`, `discard`, `transport`, `route(L)` |
| Strict evaluation | a gate never observes an undefined operand; `discard` requires its producer to be defined, so `discard(1/0)` is outside the domain |
| Copy/discard contract | one producer and one consumer per wire, external output counting as a consumer; unused hole ⇒ explicit `discard`; unused producer output ⇒ explicit `discard`; a declared body output may never be discarded |
| Provenance | `route(L)` requires the incoming carrier label to equal its declared expectation `L`; `transport` carries the label unchanged |
| Error contract | observation mode is total and returns `DEFINED` / `UNDEFINED` / `REJECTED`; strict execution mode raises the coded diagnostic of the first failing gate |
| Rewrites allowed | administrative renaming (never refreshing sources), contraction of a bound body-input segment, replacement only inside a proved contextual-equivalence class, template reuse through fresh named instances |

## 3. Declared domain and budget

* Body budget: all expression trees over holes `h1..h4`, literals `{-1, 0, 1, 2}`
  and operators `{add, sub, mul, div}` with **at most two binary gates**:
  `8 + 256 + 16384 = 16648` bodies (exact, total, no sampling; the count is
  re-derived by both routes and a negative control mutates it).
* Filling family `F` (size 7): `beta0 = (q1,q2,q3,q4) = (2,7,3,5)` (the frozen
  Paper IV producer quadruple) plus the one-hole perturbations `beta1..beta5`
  by `q5 = 2+2 = 4`, plus `beta_undef` which replaces hole 4 by
  `u0 = 1/0`. Producers: `q1 = 1+1`, `q2 = 3+4`, `q3 = 6/2`, `q4 = 9-4`.
* Carrier layer: 4 declared carrier bodies over the interface
  `(k1 : CarrierID) -> (k2 : CarrierID)` and 2 declared carrier fillings
  (`gamma_L`, `gamma_M`).
* Candidate grid: the existing summary plus any non-empty subset of six
  declared fields `{dom_profile, literals, op_count, operators, support,
  use_counts}` ⇒ all `2^6 - 1 = 63` subsets.

## 4. Headline results (exact)

| Quantity | Value |
|---|---|
| Declared bodies | 16648 (8 / 256 / 16384) |
| Substitution–evaluation compatibility checks | **116536 = 16648 × 7**, all agreeing |
| Initial-summary `pi0` classes on the domain | **341** |
| `pi0` fibres that `F` separates (insufficiency witnesses) | **232** |
| `F`-equivalence classes on the domain | **1847** |
| `F`-equivalence classes over `beta0..beta5` alone | **1847** (see below) |
| Grid candidates that are sufficient | **0 of 63** |
| Grid candidates insufficient (each with a minimal witness) | **63 of 63** |
| Bodies that are `UNDEFINED` under `beta_undef` | **16648 of 16648** |
| Paper IV snapshot output | `(9, 15, 5/2)` exactly, both via the certified graft and via the body alone |

Two consequences worth stating separately:

1. **`beta_undef` contributes no discriminating information.** All 16648 bodies
   are `UNDEFINED` under it; the class count over all 7 fillings (1847) equals
   the class count over `beta0..beta5` alone. This is a direct consequence of
   Paper IV's strict discard rule: a body cannot escape an undefined filling
   producer even for a hole it only discards.
2. **No pre-declared bounded residual built from the six declared fields fixes
   `pi0`.** Even their union (all six fields, 5323 classes) still has 281
   insufficient fibres.

## 5. Witnesses (b) — concrete values

Measurement conventions: a body is closed by a filling through certified
simultaneous substitution with an explicit copy chain for repeated holes and an
explicit `discard` for unused holes. `O_scalar` is the ordered tuple of exact
output values, or `UNDEFINED`, or `REJECTED`.

### W1 — minimal witness: same value at `beta0`, different at the legal filling `beta3`

| | body A | body B |
|---|---|---|
| gates | `const_Q(2)` + explicit discards of `h1..h4` | `h1` passed through with explicit discards of `h2..h4` |
| canonical encoding | `const(2)` | `h1` |
| binary gates | 0 | 0 |
| at `beta0 = (q1,q2,q3,q4) = (2,7,3,5)` | `DEFINED (2)` | `DEFINED (2)` |
| at `beta3 = (q5,q2,q3,q4) = (4,7,3,5)` | `DEFINED (2)` | `DEFINED (4)` |

The full behaviour vectors differ only in the `beta3` coordinate
(`h1` also gives `2` under `beta0`, `beta1`, `beta2`, `beta4`, `beta5` and
`UNDEFINED` under `beta_undef`). Rank `(0, "const(2)", "h1")` under the declared
ranking rule; this is the minimal pair and it is exactly Paper IV's remark that
*a literal constant two and the producer `1+1` have the same scalar output but
different sources and operation histories*.

### W2 — witness whose six declared residues are all identical

| | body A | body B |
|---|---|---|
| encoding | `div(const(2),h1)` | `div(h1,const(2))` |
| at `beta0` | `DEFINED (1)` | `DEFINED (1)` |
| at `beta3` | `DEFINED (1/2)` | `DEFINED (2)` |
| support | `[1]` | `[1]` |
| use_counts | `(1,0,0,0)` | `(1,0,0,0)` |
| literals | `[2]` | `[2]` |
| operators | `["div"]` | `["div"]` |
| op_count | `1` | `1` |
| dom_profile | `D,D,D,D,D,D,U` | `D,D,D,D,D,D,U` |

Only the operand order of one division differs. This pair is the witness for the
joint `dom_profile+literals+op_count+operators+support+use_counts` candidate.

### W3 — minimal witness for the `support` and `use_counts` candidates

`add(const(-1),h1)` vs `div(const(2),h1)`: both use hole 1 exactly once
(`support = [1]`, `use_counts = (1,0,0,0)`), both give `1` at `beta0`
(`-1 + 2 = 1` and `2/2 = 1`), and separate at `beta3` (`-1 + 4 = 3` vs `2/4 = 1/2`).

### W4 — minimal witness for the `literals` candidate

`h4` vs `add(h1,h3)`: both use no literal constants at all, both give `5` at
`beta0` (`h4 = 5`; `h1 + h3 = 2 + 3 = 5`), and separate at `beta1`
(`h4 = 4` vs `h1 + h3 = 5`).

### W5 — carrier value witness (provenance, not arithmetic)

| body | under `gamma_L` (carrier `L`) | under `gamma_M` (carrier `M`) |
|---|---|---|
| `cb_pass` (`transport(k1)`) | `DEFINED (carrier:L)` | `DEFINED (carrier:M)` |
| `cb_fresh_L` (`discard(k1); const_carrier(L)`) | `DEFINED (carrier:L)` | `DEFINED (carrier:L)` |

Same observation under the initial filling; different under the legal
re-filling. The two bodies are *not* identified by numerical equality: one
transports the incoming carrier, the other replaces the producing process with
a fresh constant carrier source.

### W6 — carrier legality witness

| body | under `gamma_L` | under `gamma_M` |
|---|---|---|
| `cb_pass` | `DEFINED (carrier:L)` | `DEFINED (carrier:M)` |
| `cb_route_L` (`route(L)(k1)`) | `DEFINED (carrier:L)` | `REJECTED / EXP3-PROVENANCE-MISWIRE` |

Same observation under `gamma_L`; under the equally legal filling `gamma_M` one
body returns a carrier and the other is refused by the declared handoff route
contract.

### W7 — positive control (a genuine equivalence, not a gap)

`const(-1)` vs `add(const(-1),const(0))`: literally distinct bodies (0 vs 1
binary gates, different gate inventories) with **identical** behaviour on all
seven declared fillings (`DEFINED (-1)` six times and `UNDEFINED` under
`beta_undef`). This is the control the plan demands so that an arbitrary
syntactic difference is never mistaken for a semantic difference. An
augmentation that separated this pair would be over-refined for the declared
task.

## 6. (c) Independent reproduction of the Paper IV scalar snapshot

Reproduced exactly, and labelled as an **EXISTING BOUNDED EXAMPLE**, not as new
work, not as native Adva execution and not as a faithful AES motion:

* producers `q1 = 1+1 = 2`, `q2 = 3+4 = 7`, `q3 = 6/2 = 3`, `q4 = 9-4 = 5`;
* body `y1 = x1+x2`, `y2 = x3*x4`, `y3 = (x1+x3)/(x2-x4)` with an explicit copy
  gate for each twice-used input;
* certified composite output `(9, 15, 5/2)`; the body evaluated alone on
  `(2,7,3,5)` gives the same triple (Paper IV Theorem 5.5 instantiated);
* 21 primitive gates, **8 distinct constant sources**, **4 explicit copy gates**,
  output constant-source ancestry sizes `(4, 4, 8)`;
* strict domain: defined exactly when `x2 − x4 ≠ 0`; the control
  `(2,5,3,5)` raises `EXP3-STRICT-DIVISION-BY-ZERO`.

## 7. (d) Declared error and rejection battery

Every entry is a **negative control**: the mutation is applied, the specific
declared code is required, and `gapkit.reject` compares the code exactly (no
"some exception" acceptance). All 18 controls pass; the last column is the
observed code, produced by the run.

| # | id | expected code | observed |
|---|---|---|---|
| 1 | `contract-drift` | `EXP-CONTRACT-DRIFT` | `EXP-CONTRACT-DRIFT` |
| 2 | `graft-boundary-type-mismatch` | `EXP3-TYPE-MISMATCH` | `EXP3-TYPE-MISMATCH` |
| 3 | `strict-division-by-zero-paper4-denominator` | `EXP3-STRICT-DIVISION-BY-ZERO` | `EXP3-STRICT-DIVISION-BY-ZERO` |
| 4 | `strict-division-by-zero-frames-zero` | `EXP3-STRICT-DIVISION-BY-ZERO` | `EXP3-STRICT-DIVISION-BY-ZERO` |
| 5 | `provenance-miswire` | `EXP3-PROVENANCE-MISWIRE` | `EXP3-PROVENANCE-MISWIRE` |
| 6 | `event-order-not-topological` | `EXP3-EVENT-ORDER-MISMATCH` | `EXP3-EVENT-ORDER-MISMATCH` |
| 7 | `event-order-producer-after-body` | `EXP3-EVENT-ORDER-MISMATCH` | `EXP3-EVENT-ORDER-MISMATCH` |
| 8 | `implicit-sharing` | `EXP3-IMPLICIT-SHARING` | `EXP3-IMPLICIT-SHARING` |
| 9 | `illegal-discard` | `EXP3-ILLEGAL-DISCARD` | `EXP3-ILLEGAL-DISCARD` |
| 10 | `cross-wired-cycle` | `EXP3-GLOBAL-CYCLE` | `EXP3-GLOBAL-CYCLE` |
| 11 | `unused-producer-output` | `EXP3-UNUSED-PRODUCER-OUTPUT` | `EXP3-UNUSED-PRODUCER-OUTPUT` |
| 12 | `duplicate-binding` | `EXP3-DUPLICATE-BINDING` | `EXP3-DUPLICATE-BINDING` |
| 13 | `boundary-order-mismatch` | `EXP3-BOUNDARY-ORDER-MISMATCH` | `EXP3-BOUNDARY-ORDER-MISMATCH` |
| 14 | `raw-value-input` | `EXP3-RAW-VALUE-INPUT` | `EXP3-RAW-VALUE-INPUT` |
| 15 | `value-equality-substitutability-claim` | `EXP3-VALUE-EQUALITY-INSUFFICIENT` | `EXP3-VALUE-EQUALITY-INSUFFICIENT` |
| 16 | `initial-summary-sufficiency-claim` | `EXP3-SUFFICIENCY-CLAIM-REFUTED` | `EXP3-SUFFICIENCY-CLAIM-REFUTED` |
| 17 | `enumerated-count-mismatch` | `EXP3-ENUMERATION-MISMATCH` | `EXP3-ENUMERATION-MISMATCH` |
| 18 | `primary-independent-disagreement` | `EXP3-ROUTE-DISAGREEMENT` | `EXP3-ROUTE-DISAGREEMENT` |

Notes on the two order-sensitive entries and the two discard entries:

* **Event/order mismatch** has two declared sub-cases with one code: (6) an
  event order that is not topological for the assembled graph, and (7) an order
  that *is* topological but schedules a body-region event before a
  producer-region event. Sub-case (7) is declared as a **history** obligation:
  Paper IV's Theorem 5.5 proof chooses producer gates before body gates, and
  purity means the numerical result is unchanged by another topological order
  while the ordered trace changes. Rejecting it therefore separates historical
  from numerical equality, which is exactly this experiment's theme.
* **Illegal discard** is the case where a discard consumes a wire that the
  declared output boundary requires, so the graft silently drops a promised
  body output. The declared check order puts this before the generic
  one-consumer check, so it is not confused with `EXP3-IMPLICIT-SHARING`
  (a second consumer of a copy output).
* **`cross-wired-cycle`** first asserts that each piece alone is acyclic and
  evaluates to `DEFINED (3)`, then requires the assembled global graph to raise
  `EXP3-GLOBAL-CYCLE` — local acyclicity does not imply global acyclicity.

## 8. (e) Rejected contexts, with the reason for each

| id | rejected context | reason | code |
|---|---|---|---|
| `carrier-producer-into-rational-hole` | fill a `Q` hole with `pc_L` | the graft boundary preserves types and positions; an opaque label is not a rational | `EXP3-TYPE-MISMATCH` |
| `rational-producer-into-carrier-hole` | fill `k1 : CarrierID` with a `Q` producer | the graft boundary preserves types and positions | `EXP3-TYPE-MISMATCH` |
| `partial-closure-claimed-closed` | claim a closed composite with one hole unbound | unselected holes stay on the open frontier; the external order is producer inputs in argument order then the unfilled body inputs | `EXP3-UNUSED-PRODUCER-OUTPUT` |
| `one-instance-used-twice-without-fresh-renaming` | identify two uses of one producer occurrence | template reuse first creates separate named instances with fresh occurrences; the declared renaming does exactly that, any other identification does not | `EXP3-DUPLICATE-OCCURRENCE` |
| `unused-producer-output` | leave a supplied producer output unconsumed | every supplied output is used once; an unused output needs an explicit discard | `EXP3-UNUSED-PRODUCER-OUTPUT` |
| `duplicate-binding` | bind one hole twice, or one output occurrence twice | the binding is injective on both sides | `EXP3-DUPLICATE-BINDING` |
| `reordered-boundary-without-permutation` | reorder the boundary with no declared typed permutation | sequential partial filling can induce a different order than simultaneous filling; comparison then needs a declared permutation | `EXP3-BOUNDARY-ORDER-MISMATCH` |
| `discard-a-declared-output` | consume a declared body output with a discard | a graft is accepted only when its boundary inventory is complete | `EXP3-ILLEGAL-DISCARD` |
| `cross-wired-cycle` | cross-wire two locally acyclic pieces | local acyclicity does not imply global acyclicity | `EXP3-GLOBAL-CYCLE` |
| `bare-numerical-input` | supply a number as a bare value | a numerical input enters only through an explicit constant producer with a source record, never by erasing the producing process | `EXP3-RAW-VALUE-INPUT` |
| `wrong-carrier-handoff` | hand a carrier `M` to an interface expecting `L` | the declared handoff route contract requires carrier identity at the seam | `EXP3-PROVENANCE-MISWIRE` |
| `producer-after-body-event-order` | schedule a producer event after a body event | the graft receipt declares the call order producer-then-body; a history obligation, since the number is schedule independent | `EXP3-EVENT-ORDER-MISMATCH` |
| `identify-bodies-by-one-filling` | replace one body by another because they agree at `beta0` | value equality at one filling is not contextual equality; the search exhibits legal fillings separating such pairs | `EXP3-VALUE-EQUALITY-INSUFFICIENT` |

**Numerical equality versus contextual equality.** *Numerical equality* is
agreement of `O_scalar` at the single frozen initial filling `beta0`.
*Contextual equality* is agreement of `O_scalar` for **every** filling in the
declared family `F`, with `UNDEFINED` and `REJECTED` counted as observations.
`pi0` — the existing summary — is exactly numerical equality at `beta0`; it is
**not sufficient**, and the failure is witnessed 232 times inside the declared
budget, the least of them W1 above. Conversely W7 shows two literally different
bodies that *are* contextually equal, so literal difference alone is not a gap.
No conclusion anywhere in this report upgrades numerical equality to
substitutability.

## 9. (f) Three comparison tiers

| Tier | Candidate | Datatype | Verdict on the declared domain |
|---|---|---|---|
| 1 existing summary | `pi0` = `O_scalar(body ∘ beta0)` | one observation vector | **insufficient**: 341 classes, 232 separating fibres |
| 2 bounded, pre-declared enhancement | `pi_grid` = `pi0` + any non-empty subset of the six declared fields (63 candidates) | vector + declared residues | **63 of 63 insufficient**; best single field `dom_profile` still leaves 242 separating fibres; the union of all six leaves 281 |
| 2 bounded, maximal | `pi_F` = behaviour vector over `F` | 7 observation vectors | **sufficient and closed-update by construction** (`u_beta` is the projection onto the `beta` coordinate) |
| 3 full history / exact semantics | `hist` = the literal network with sources, occurrences and graft receipt, observed through `O_exact` | unbounded occurrences | sufficient, and **strictly finer** than the task: it separates W7, which the task cannot and should not |

Costs, reported per channel and never collapsed (domain of 16648 bodies):

| Candidate | storage bytes (total / mean / max) | structural size | computation steps | observations | verification cost |
|---|---|---|---|---|---|
| `pi0` | 1256881 / `1256881/16648` / 80 | 113392 | 16648 | 16648 | 116536 |
| `pi_grid`, `support` | 1861501 / `1861501/16648` / 132 | 173792 | 16648 | 16648 | 116536 |
| `pi_grid`, all six fields | 6640754 / `3320377/8324` / 407 | 772304 | 116536 | 116536 | 116536 |
| `pi_F` | 6640754 / `3320377/8324` / 407 | 772304 | 116536 | 116536 | 116536 |
| `hist` | 41339614 / `20669807/8324` / 3186 | 3016860 | 105536 | 16648 | 116536 |
| exhaustive search itself | — | — | 2158172 | 116536 | — |

Selection under the plan's section 9 rule (smallest `(structural_size,
storage_bytes)` among sufficient candidates): **`pi_F`**, `structural_size`
772304, `storage_bytes` 6640754, because no candidate in the declared grid is
sufficient. `pi_F` is the cheapest sufficient candidate *found*, and it is not
claimed to be a minimal repair. `hist` costs 6.2× `pi_F` in storage bytes
(41339614 vs 6640754) and buys only the over-refinement that separates W7.

## 10. Independent route and agreement

`research/process-representation-gap/experiments/exp3_typed_hole_context_independent.py`

* **Route.** Direct substitution-and-evaluation. Producer values are substituted
  into the body's expression term and the term is evaluated with
  `fractions.Fraction`; the same is done for the carrier layer with carrier
  labels. **No wire, gate, network, schedule, graft receipt or constant-source
  ancestry is ever constructed.** The declared composite-domain rule (Paper IV
  Equation (5.2)) is written out directly: the composite is defined iff every
  closure producer is defined **and** the body term is defined on the
  substituted values.
* **Why it is independent.** The primary route's semantics live in graph
  construction: explicit copy gates, strict discard gates, the
  one-producer/one-consumer inventory, boundary completeness, the graft receipt,
  acyclicity and constant-source ancestry. None of that code exists in the
  independent route, which shares with the primary only `tools/gapkit.py`
  (deterministic JSON, hashing, diagnostics, cost accumulation — no experiment
  semantics). The two files also never import each other.
* **Result.** 344 comparisons, **0 disagreements**. It independently reproduces
  16648 bodies, the 341/232 initial-summary figures, the 1847 filling-equivalence
  classes, all 63 candidate class counts, insufficient-fibre counts and
  sufficiency verdicts, the minimal witness rank `(0, "const(2)", "h1")`, every
  reported grid witness's separating filling, the positive control, the Paper IV
  triple `(9, 15, 5/2)`, the `UNDEFINED` verdict for `x2 − x4 = 0`, and the whole
  carrier layer including the `REJECTED / EXP3-PROVENANCE-MISWIRE` outcome.
  Any difference would raise `EXP3-ROUTE-DISAGREEMENT`; a mutated-table control
  demonstrates that the comparison is sensitive.
* **Its own negative controls** (all pass): `independent-contract-drift`
  (`EXP-CONTRACT-DRIFT`), `independent-graft-type-mismatch`
  (`EXP3-TYPE-MISMATCH`), `independent-strict-division-by-zero`
  (`EXP3-STRICT-DIVISION-BY-ZERO`), `independent-route-disagreement`
  (`EXP3-ROUTE-DISAGREEMENT`).

**Robustness.** Both checkers use no `assert` at all (every obligation is
`gapkit.require`; the word `assert` occurs only inside one docstring sentence in
the primary file and nowhere in the independent file), and `python3 -O` output
is byte-identical to the normal output for both (`cmp` reported no difference
for the primary and for the independent route). Both are deterministic: two
independent runs of each produce identical bytes.

## 11. Scope boundary and what is NOT claimed

* Finite, acyclic, **strict** arithmetic networks only. No recursion, no
  feedback, no fixpoint and no unbounded interpretation semantics is claimed or
  implemented.
* Sufficiency is decided on the declared budget of 16648 bodies (at most two
  binary gates) and the declared filling family of size 7 only. No body with
  three or more binary gates was searched; no filling outside `F` was used; no
  carrier outside `{L, M}` was used. A finite enumeration is **never** upgraded
  into a general theorem.
* **Numerical equality is never treated as substitutability.** The whole point
  of the experiment is the opposite, and the "value-equal ⇒ substitutable"
  claim is registered as a refuted negative control.
* No claim that value equality is *never* sufficient, in general or for any
  richer interface; no claim that `F` is complete, or that behaviour on `F`
  determines behaviour on any other filling.
* The Paper IV four-input three-output scalar snapshot is an **existing bounded
  example** reproduced for compatibility, not new work, **not** native Adva
  execution, and **not** a faithful AES motion (Paper IV Warning
  `warn:ported-motion-bridge` is not discharged).
* The carrier/`route` expectation contract is a declared structural proposal
  abstracted from the handoff route discipline in the pinned PR-16 record; it is
  not an implementation of Adva compute and no pinned byte hash is recomputed
  here.
* No spectral, operator, matrix or complexity claim. No endomorphism closure,
  operator domain, marking or residual is declared, so no spectral feature is
  used (Paper IV section 5.6).
* No geometric claim: nothing here asserts that a gate is an AES motion or that
  a binary gate has a path through a carrier.

## 12. Open items and blockers

* **Closed update under re-filling outside `F`.** `pi_F` is closed-update only
  because the declared action family *is* `F`. Whether any bounded residual is
  closed under composition of fillings (or under wrapping in a declared outer
  context) is open and needs its own contract version.
* **Adaptive context selection** is out of scope for v1 (declared in the
  contract); all fillings are chosen from a frozen family.
* **Bodies with three or more binary gates** are unsearched. A declared
  extension witness list was described in the contract but not instantiated,
  precisely so that no bounded-domain result is extended by it; extending the
  budget is a new resource declaration, not a result.
* **`beta_undef` carries no information** on this domain because every body is
  `UNDEFINED` under it. A domain in which strict discard is observable would
  need a producer that is undefined for only some bodies, which the declared
  strict interface does not permit; this is reported as a finding rather than
  worked around.
* **The cheapest sufficient candidate is not a minimal repair.** No lower bound
  on the information a sufficient bounded residual must carry is proved; only
  the negative result for the 63 declared candidates is established.
* No blocker prevented the experiment from completing inside the declared
  budget; nothing here required access outside
  `research/process-representation-gap/`.

## 13. File inventory and reproduction

Created (all under `research/process-representation-gap/`):

| File | sha256 |
|---|---|
| `contracts/exp3-typed-hole-context.v1.json` | `bd7f958740b1c5d686da5012d59ec1995ad3c1f5af98bead0e3ee9637aa0eb8f` |
| `evidence/exp3-typed-hole-context.json` | `82362f569ddcfefe90b54a4a75a99b12fba88e0950ffc5614ec0876625fb2931` |
| `evidence/exp3-typed-hole-context-independent.json` | `cffd9905d0996880cd25257ab41f1d6ec6ccf7dd6e0d66478f642f9e1bd96532` |
| `experiments/exp3_typed_hole_context.py` | primary route |
| `experiments/exp3_typed_hole_context_independent.py` | independent route |
| `contracts/FROZEN.sha256` | regenerated by `tools/freeze_contracts.py` (merge-preserving; other experiments' entries retained) |

```bash
cd /Users/mingli/AEG/.worktrees/aeg-paper-research-gap
R=research/process-representation-gap

# contract digest is already in the ledger
python3 $R/tools/freeze_contracts.py

# primary: stdout must equal the checked-in evidence byte for byte
python3 $R/experiments/exp3_typed_hole_context.py > /tmp/exp3.json
cmp /tmp/exp3.json $R/evidence/exp3-typed-hole-context.json

# normal and optimized execution must agree
python3 -O $R/experiments/exp3_typed_hole_context.py > /tmp/exp3-O.json
cmp /tmp/exp3.json /tmp/exp3-O.json

# independent route (raises EXP3-ROUTE-DISAGREEMENT on any disagreement)
python3 $R/experiments/exp3_typed_hole_context_independent.py > /tmp/exp3i.json
cmp /tmp/exp3i.json $R/evidence/exp3-typed-hole-context-independent.json
```

Runtime: about 55 s for the primary and about 30 s for the independent route on
the recorded environment (CPython 3.14.6, not optimized).
