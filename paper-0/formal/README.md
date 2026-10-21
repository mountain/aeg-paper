# Paper 0 formal derivations

This is the beginning of a chapter-by-chapter formalization of the **current**
Paper 0. It is separate from the mathematical-status register and the archived
Lean formalization of older manuscripts. Existing definitions, manuscript
proofs, conjectures and excluded claims keep their own status. A checked
fragment does not mark an entire proposition or chapter complete.

## Verification arrangement

The original theory is equality in a commutative semiring. Its basis is explicitly
listed in `Chapter02.lean`: addition/multiplication associativity and
commutativity, additive zero, multiplicative one and zero, and distributivity.
These are parameters of a structure, not axioms asserting the target AEG
statements. Fields interpret this smaller signature. The native equality
kernel has no inverse, subtraction, order, analysis or geometry rules; the
separate Lean field-law continuation is described below.

`checker.adva` is a new, original Adva-written equational kernel. It uses the
existing `mountain/adva-machine` data-machine-v1 at the exact revision in
`machine.lock.json`. It preserves the old Metamath toy checker and installs no
machine instruction or stable semantic operation. This kernel supports
reflexivity, symmetry, transitivity, addition/multiplication congruence, and
instances of the declared basis. There is no arbitrary-proposition rule.
Terms are explicit variable/zero/one/add/multiply trees. Adva constructs both
sides of each rule instance, checks every term, compares transitivity joins
node by node, and compares the final equation with the independently supplied
goal. Bounds are 64 proof instructions, 63 nodes per term and 32 stack entries.

`author.py` only produces bytecode; `fixtures.py` produces explicit proof
certificates. Neither runs inside Adva. `statements.json` fixes the goals
separately from `certificates.json`. Successful named checks must match those
goals and the pinned manuscript/statement/checker sources. A valid proof of a
different equation cannot satisfy a named target.

`run.py` receives the complete native trace through both fresh Rust replay and
the separately implemented, pinned generic Python v1 instruction interpreter.
An independent sparse-polynomial oracle compares symbolic coefficients; it
does not replace Adva proof checking. Lean checks separate general statements
over the explicit algebraic laws. Five algebraic theorems use no global axioms;
the inductive comb-order theorem reports `propext`. These checks do not prove a
general soundness theorem for the Adva checker or mechanically certify the
translation from manuscript prose. The machine, its declared build, the
statement correspondence and the reviewed equality kernel remain trusted.

## Current coverage

| Manuscript component | Formal work supplied | Remaining obligation |
| --- | --- | --- |
| §1 Introduction | Source inventory | Interpretive prose has no automatic proof status |
| §2 comb grammars | Planar trees, left/right chronological append, tree/partial-fold correspondence, mirror involution, and independent child-interleaving schedules in Lean | Native universal grammar-proof certificates and a theorem about the implementation remain open |
| §2 four-operation sections | All eight ordinary values/domains and nonzero affine inverse laws in Lean; separate bounded rational Adva evaluator | These universal field theorems are Lean-checked; finite Adva executions do not promote a new field-proof kernel |
| §2 distributive operator identity | Unchanged symbolic Adva/Lean identity; new general-field proof of the corrected marked/scalar clauses | The previous counterexample and its old source snapshot remain historical evidence |
| §§3–6 AES, ripple, reciprocal and projective theory | Inventoried, including the nested pole-covariance subsection | Formal domains, nonzero hypotheses, projective and geometric theories |
| §7 chronological affine cocycle | Auxiliary pointwise polynomial identity checked by Adva and Lean; shared finite-history scalar expansion in `AppendixC.lean` | Definition/uniqueness of affine coordinates, inverse and normalized-coordinate laws |
| §§8–12 ACS, contact, nonlinearity, punctures, compactification | Inventoried | Algebraic/differential/topological dependencies and explicit side conditions |
| Appendix C alternating expressions | 24 Lean theorems: independent suffix-sum expansion, arbitrary finite/prefix perturbation, actual tree/word correspondence and guarded ratio; one native symbolic induction-step certificate | ACS/exponentials/RG, identity-padding syntax transformations, and a native Adva induction kernel are outside this continuation |
| §13 interfaces and appendices A, B, D, E | Inventoried | Formal statement and dependency correspondence |
| Appendix F cuts and expression foundations | Background and structural proposal, source inventoried | Cited external constructions and open design obligations; no new formal certificate coverage |

`inventory.json` follows active `\input` directives from the canonical manuscript
and recorded 20 files and 91 theorem-like environments at the first checkpoint.
The current live inventory has 22 source files and 95 theorem-like environments,
with a separate source-bound map for Appendix C.
The Appendix F addition refreshes navigation and its live source-lock digest.
The Appendix C archive still binds its original inventory and manuscript
snapshot; its regression checks that snapshot independently of live navigation.
This is navigation and drift detection, not a complete TeX parser or proof of
coverage of prose and unnumbered equations. `not-yet-formalized` means exactly
that; it does not downgrade or certify a manuscript's mathematical status.
Every attached certificate records its **component** coverage explicitly.

The first [execution record](evidence/execution.json) is `Passed`: five named
derivations, twenty positive/negative controls, 29 native runs, 60 child
commands and 31,637 independent instruction transitions, including suspension,
resume and fuel exhaustion. The bounded invocation took 125.47 seconds. Its
archive retains every native trace and replay receipt plus the exact first-party
verification sources. Seven engineering tests passed before that run; a
subsequent eighth test checks archive/source/report bindings without launching
another experiment. The dedicated CI workflow is supplied but has not been
executed remotely in this session.

At the initial checkpoint, the scanner followed a commented `\input` example as a self-include;
comment stripping repaired that preflight error before execution. The native
checker and proof rules were unaffected. The initial Paper 0 and I build attempts stopped at
`bibtex executable not found`. The continuation supplies actual successful
builds after installing the declared TeX dependencies; see below.

## Marked-data finding and correction

At the initial source checkpoint, `prop:p0-distributive-operator-identity`'s operator identity
`k*(z+p)=k*z+k*p` is valid, including zero. The additional assertion that the
chronological constant pairs `(p,k)` and `(k,k*p)` coincide only at `p=k=1`
fails at `p=k=0`. The section starts with a field and does not restrict `k`
to be nonzero in this proposition. `zero_pair_counterexample` checks the exact
zero computation; ordinary field zero gives the same witness.

There is a second interpretation issue: complete marked words retain operation
labels, so `add(1); multiply(1)` and `multiply(1); add(1)` remain different
marked histories even when their constant pairs agree. Neither operator
equality nor equality of the two constant pairs proves history equality.
The amended manuscript now defines full marked steps by operation/slot/constant
and reserves `(p,k)` for the separate chronological scalar projection. The new
`constant_pair_coincidence` theorem over explicit field laws includes exactly
`(0,0)` and `(1,1)`; `marked_words_distinct` applies to all parameters. OQ-090
is resolved. The old equation-kernel certificate still covers only operator
equality; the additional general-field claims are checked separately in Lean. No conclusion about charge descent, geometry or
Adva source/occurrence identity follows from this equality check.


## Chapter 2 continuation: guarded division and definitions

`contract-v2.json` declares the successor before execution; the explicitly
revised `contract-v2.1.json` retains the failure and receiving repair below.
`definition-map.json`
binds the amended Chapter 2 source to **63** audited theorems in
`Chapter02Domains.lean`, separately from the unchanged eight initial Lean
statements. `FieldData` extends the explicit semiring structure by additive
inverses, inversion, nonzero inverse cancellation and `0 != 1`. These are
standard field-law parameters, not assumed AEG conclusions. The axiom audit
permits only Lean's disclosed `propext`, `Classical.choice` and `Quot.sound`;
any `sorryAx` or other global axiom fails reception.

The syntax/semantics bridge now has actual planar trees and chronological
folds, an opposite **partial relation**, and a tree evaluation relation. A
separate schedule relation interleaves independent child schedules before the
parent executes. Its comb characterization proves that every legal schedule
has exactly the chronological input labels; occurrence indices can be kept
in those labels. This replaces reliance solely on the initial inductive
`LegalCombOrder` presentation. Commutativity relates values and domains, not
literal planar syntax.

`domain-checker.adva` is a separate 216-instruction bounded rational evaluator
using unchanged data-machine-v1 instructions. `domain_author.py` authors it;
`domain-cases.json` fixes 28 exact cases and `domain_fixtures.py` provides an
independent unbounded `Fraction` oracle. Native rational pairs are not silently
normalized. Both operand slots, negative rational representations, intermediate
zeros, zero numerators and invalid rational data are tested. Arithmetic
integer overflow and the 16-step profile bound are reported as resource/profile
refusals even when the underlying rational expression is well defined.

The division guard examines the **actual right operand** at every step:
`z/c` requires `c != 0`; `c/z` requires `z != 0` even when `c=0` or a later
multiplication by zero would simplify the final expression. Lean proves that
an undefined prefix cannot acquire an evaluation by appending a suffix.
Affine group membership requires a nonzero multiplier. Ordinary `0/z` remains
a partial zero map, whereas only `c != 0` supplies the invertible homogeneous
reciprocal map `[X:Y] -> [cY:X]`. Infinity behavior and nonzero representatives
are proved; a full formal `PGL_2` quotient construction is not included.

The original `contract.json`, equality bytecode, certificate family,
`Chapter02.lean`, and `evidence/run-01.tar.gz` are unchanged. Historical evidence
is checked against its archived verifier/mapping snapshot; it is never rebound
to amended manuscript bytes. Current inventory and source locks are successor
records. That archived Chapter 2 run uses `run.py` and the v2.1 contract;
the current reproduction command below invokes the Appendix C successor.
The real-exponential/ACS argument in the charge example remains explicitly
dependent on the manuscript and Chapter 8; it is not promoted by this pilot.

### Retained receiving failure and resource repair

The first v2 attempt checked all 61 native executions and their two replay
routes, then failed at Lean import/elaboration with `INTERNAL PANIC: out of
memory` under the original 1 GiB virtual-address-space limit. Its complete
[failure record](evidence/chapter02-attempt-1.json), source snapshot, native
outputs and diagnostics remain archived. That whole invocation is **Failed**;
the native results are not relabelled as a completed combined verification.

A bounded engineering measurement of the same proof file with one Lean thread
observed about 2.12 GiB virtual address space and 408 MiB resident memory. One
thread alone still did not fit a 1 GiB address-space limit. A separate 4 GiB
Lean limit passed the engineering check. The v2.1 contract permits one fresh
complete invocation with `-j1` and that **Lean-only** limit. Native children
stay at 1 GiB; proof sources, programs, inputs, fuel, wall time and every other
counting bound are unchanged. The failed attempt's costs are additional.

The [completed successor record](evidence/chapter02-execution.json) is
`Passed`: five unchanged symbolic certificates, twenty original controls,
28 rational cases and continuation/fuel controls, for **61 native runs**,
**125 child commands** and **35,735 independently received instruction
transitions**. All 63 new Lean theorems and the eight original statements
passed their separate audits. The successful invocation took 135.31 seconds;
the failed invocation's additional 129.19 seconds remain separately recorded.
All 61 native reports and replay receipts are byte-identical across the two
attempts, confirming the repair changed the receiving resource envelope only.
Thirteen engineering tests passed before the invocation; a fourteenth checks
the completed archive and the per-child native/Lean resource split afterward.

The v2.1 build validation produced Paper 0's 93-page PDF and Paper I's 32-page
PDF, with no undefined references, missing citations or duplicate labels.
Existing layout warnings remain outside the edited chapter: one 11.13 pt
overfull paragraph in Paper 0 §10, two overfull boxes in Paper I, and hyperref
math-in-bookmark warnings. The amended proposition page was visually checked.

### Editorial continuation: evaluability and effective presentations

The later §2 subsection `02a-evaluation-and-effectivity.tex` restores historical
terminology and distinguishes ordinary partial semantics, effective rational
evaluation and Richardson's decision obstruction. The
[discussion record](../../governance/discussions/evaluable-expressions-and-effective-presentations.md)
retains its provenance and the author's connection to Adva's finite viewpoint.

The new definition and example are `not-yet-formalized` in the current
inventory. The original Chapter 2 source, definition map, proof programs,
Lean modules and executed evidence are unchanged. Only the live manuscript
inventory and its source-lock entry advanced; the archived inventory continues
to describe the source snapshot that was actually checked. The archive test
verifies those historical bytes. The later Appendix C successor also versions
the inventory generator, while keeping all old proof and execution sources
equal to their executed snapshots. No new native or Lean coverage is
claimed for the added prose, example or cited external theorem.

At the editorial restoration, Appendix C's new definition and proposition were
`not-yet-formalized`. The successor below supplies their reviewed component
mapping. The worked ACS connection and historical RG reading retain their
separate in-manuscript/interpretive status.

## Appendix C induction successor

`AppendixC.lean` imports the unchanged Chapter 2 modules. Its chronological
list evaluator is related to an actual two-event-per-pair word and its planar
tree through the existing ordinary `Eval`/`PartialFold` semantics. The snoc
theorem identifies the manuscript recurrence. An independent list of suffix
contributions, with an indexed lookup theorem, represents the displayed finite
sum of each additive constant times its remaining product.

Finite list induction proves the expansion and additive perturbation for
arbitrary lengths. Explicit field laws then give exact differences at every
prefix, the nonzero initial-difference condition, the guarded difference
quotient, and undefinedness of the equal-input quotient. The polynomial
identities require only commutative-semiring laws, so their proofs even allow
zero multipliers; `NonzeroMultipliers` and `scale_nonzero` separately recover
the manuscript's invertible-multiplier hypothesis. No smallness or analytic
limit is used.

The [source map](appendix-map.json) declares all 24 theorem names and their
exact global-axiom sets. The primary expansion, perturbation and quotient
proofs use no global axioms. Two supporting list/tree correspondences report
`propext` and `Quot.sound`; the event-count lemma and two finite-product
helpers report `propext`.
The receiver rejects any changed axiom set, diagnostic or missing audit name.

`appendix-statement.json` and `appendix-certificate.json` supply a separately
fixed symbolic semiring induction step:

```text
q * (x + delta) + mu = (q * x + mu) + q * delta
```

The unchanged `checker.adva` checks that certificate. A changed goal that
confuses scale-then-add with add-then-scale must reject. The independent
polynomial oracle, fresh native replay and generic instruction receiver check
both executions. This is a symbolic induction-step check, not an Adva rule
for universal induction; Lean checks the arbitrary finite iteration.

`negative/MissingRatioGuard.lean` deliberately omits `y != x`. Reception
requires Lean to reject it with exactly the expected missing-hypothesis type
mismatch, after the positive module has compiled; an unrelated import or
compiler failure is not accepted as a passing negative control.

`contract-appendix-c.json` declared the first combined invocation after
engineering checks, with the preceding 300-second shared deadline, 64 native
call cap, 160 child-command cap, unchanged native memory limits and the
existing 4 GiB Lean limit. `appendix_run.py` reuses the original supervisor,
also emitting the unchanged domain module's import artifact, and adds the
new checks. The first invocation stopped at an exact axiom-inventory mismatch:
`propext` had been omitted for `scale_append` and `scale_snoc`. Its complete
[failure record](evidence/appendix-c-attempt-1.json) remains `Failed`.
`contract-appendix-c-v1.1.json` declares a fresh invocation after correcting
only those two expected axiom entries, with identical proof/program/goal/case
bytes and resource bounds. The successor is recorded separately in
[appendix-c-execution.json](evidence/appendix-c-execution.json). Older archives
remain checked against their own source snapshots; current navigation and
the two source maps receive successor byte pins. The §2 evaluability example,
ACS integration, real-exponential interpretation and RG discussion remain
outside this new proof coverage.

The completed successor is `Passed`: **63 native runs**, **131 child
commands**, **49,581 independently received instruction transitions**, and all
24 new Lean statements in addition to the preceding 71. The missing-ratio-guard
control rejects as intended. The run took 182.03 seconds; the retained failed
invocation cost an additional 184.11 seconds. All 63 native reports and replay
receipts, and the positive Appendix C Lean audit, are byte-identical between
attempts. Seventeen tests passed before the successor; eighteen pass after
adding the completed archive/source/trace binding test. Both manuscript builds
pass (Paper 0: 97 pages; Paper I: 32), with no new reference or layout issues.
These theorem counts include supporting lemmas and are not counts of covered
manuscript environments.

## Reproduce

Use Python 3.11+ on Linux, `blake3==1.0.9`, Lean 4.24.0, and a separate checkout
of `mountain/adva-machine` at `51ee98981ebbc62f8614ed20920c11dc76ea298d`.
Build the machine there with `cargo build --locked -p adva-witness --bin adva`.
From the AEG repository root:

```sh
python -m unittest discover -s paper-0/formal -p 'test_*.py'
python paper-0/formal/appendix_run.py \
  --machine-root /absolute/path/to/pinned/adva-machine \
  --binary /absolute/path/to/pinned/adva-machine/target/debug/adva \
  --lean /absolute/path/to/lean \
  --output /absolute/path/to/new-evidence-directory
```

The output directory must be new. Proof traces, input and goal bytes, Rust
replay receipts, oracle costs, Lean output and a final outcome are retained.
The 300-second invocation budget covers checking and controls; source fetching
and compilation are engineering preparation. `Suspended`, `FuelExhausted` and
out-of-profile refusals do not mean a theorem is false. Missing evidence or a
source/profile mismatch fails the run; no automatic fallback or fuel refill is
provided. The supplied executable is a declared trusted build: its recorded
digest is integrity evidence, not an authenticated compiler-provenance proof.

The CI workflow now invokes this Appendix C successor, including the old
regression. Calling `run.py` directly uses the older Chapter 2 profile and
does not check the new induction module.

Authoring commands (`author.py`, `fixtures.py`, `appendix_fixtures.py`,
`inventory.py`) update artifacts
for review. Verification never calls them to rewrite expected results or locks.
An intentional change requires reviewing the new statements, proof rules,
manuscript mapping and negative controls before publishing successor pins.

## Continuation order

The requested §2 syntax/domain correspondence and marked-data repair are
implemented in the versioned continuation below. The next chapter can
introduce the regular-AES definitions and hypotheses for §3, maintaining
explicit imports for later geometry. Reuse the old Lean material only after a
legacy-to-current statement map. Add each theorem's formal prerequisites and
evidence as it is received; do not assume general topology, differential
geometry, convergence or proof-library translation from this algebraic pilot.

Original implementation and documentation by Codex (OpenAI), contributed under
CC0. Source ownership or an account proxy is not independent human review or
endorsement. Correctness claims are limited to the retained executed checks.
