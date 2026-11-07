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
| §2 evaluability continuation | General finite-tree domain/value, closed-input independence, exact rational evaluation, cancelled reciprocal and projective round trip, prefix domains/condition pullbacks, and subtraction expansion in Lean | External Richardson theorem, real exponential/ACS example, topology and cardinality background retain their separate dependencies |
| §2 distributive operator identity | Unchanged symbolic Adva/Lean identity; new general-field proof of the corrected marked/scalar clauses | The previous counterexample and its old source snapshot remain historical evidence |
| §3 coordinate foundation and real analysis | 61 coordinate statements plus 66 Mathlib statements: actual differential/Jacobian, smooth real coordinate-AES model, Laplace eigenfunction, positive smooth root, rectification, signed-frame bracket and affine ODE solution/uniqueness | Gaussian curvature/completeness, length/trace theory, punctured E1, full arbitrary-manifold/boundary-chart and intrinsic bundle-operator equivalences |
| §4 ripple, pole and Apollonius components | 57 ripple/pole statements plus 39 complex-norm statements: guarded modulus-to-distance equivalence, actual Euclidean circles and bisectors, and degenerate parameter cases | Full PGL action identification, intrinsic horocycles/tangency and chart independence; source wording limitations remain explicit |
| §§5–6 reciprocal and projective synthesis | Inventoried | Formal domains, nonzero hypotheses and projective action identification |
| §7 chronological affine cocycle | Auxiliary pointwise polynomial identity checked by Adva and Lean; shared finite-history scalar expansion in `AppendixC.lean` | Definition/uniqueness of affine coordinates, inverse and normalized-coordinate laws |
| §§8–12 ACS, contact, nonlinearity, punctures, compactification | Inventoried | Algebraic/differential/topological dependencies and explicit side conditions |
| Appendix C alternating expressions | 24 Lean theorems: independent suffix-sum expansion, arbitrary finite/prefix perturbation, actual tree/word correspondence and guarded ratio; one native symbolic induction-step certificate | ACS/exponentials/RG, identity-padding syntax transformations, and a native Adva induction kernel are outside this continuation |
| §13 interfaces and appendices A, B, D, E | Inventoried | Formal statement and dependency correspondence |
| Appendix F cuts and expression foundations | Background and structural proposal, source inventoried | Cited external constructions and open design obligations; no new formal certificate coverage |

`inventory.json` follows active `\input` directives from the canonical manuscript
and recorded 20 files and 91 theorem-like environments at the first checkpoint.
The current live inventory has 22 source files and 102 theorem-like environments,
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
python paper-0/formal/chapter03_run.py \
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

At that checkpoint, CI invoked the Appendix C successor, including the old
regression. The Chapter 2 evaluability successor below now extends that run.
Calling `run.py` directly uses the older Chapter 2 profile and does not check
either the induction module or the evaluability module.

## Chapter 2 evaluability successor (2026-11-07)

`Chapter02Evaluability.lean` supplies 36 additional audited statements. Its
separate `evaluability-map.json` binds both the unchanged expansion source and
the added evaluability subsection. The domain is existence of an ordinary
`TreeEval`; evaluation is functional, and the dependent semantic value map is
defined only at inputs in that domain. Closed trees are independent of the
unused input. Both comb domains agree with their chronological partial folds;
arbitrary undefined prefixes and undefined child subtrees stay undefined.
Condition pullback through concatenation equals nested pullback in reverse
composition order, without an inverse-function assumption.

For `1/(1/z)`, Lean proves that the actual tree has one hole, has domain exactly
`z != 0`, and returns `z` there. Its partial graph differs from the identity
graph. The existing projective reciprocal graph is functional and two
reciprocals compose to identity, including the zero/infinity round trip. This
does not construct the full `PGL_2` quotient or admit ordinary division by zero.
The previously missing slot-(2) subtraction expansion is also checked over
the existing explicit field-law parameters.

The new `compute` function uses structural recursion on finite trees and a
supplied `DecidableEq`, with exact soundness and completeness against ordinary
evaluation. `none` means precisely that no ordinary evaluation exists.
`rationalField` instantiates every existing field law using the pinned Lean
standard `Rat` library; `evaluateRational` therefore gives a terminating exact
procedure on arbitrary finite rational trees. This includes closed trees and
branching trees, beyond the bounded native comb profile. Valid `Rat` constants
already have nonzero representation denominators; raw fraction validation is
a separate input obligation, covered in the old native cases. Kernel-checked
boundary examples include an intermediate zero denominator, an undefined
subtree multiplied by zero, zero numerators, cancelled reciprocals and an
integer result beyond signed 64-bit range. No real-language decision procedure
or running-time/space guarantee follows. The semantic value function uses
classical choice; the executable `compute` does not call it. Exact disclosed
axiom sets are recorded for every theorem, including standard Rat dependencies.

`negative/CancelledReciprocalTotal.lean` must be rejected for the specific
missing-nonzero-hypothesis type mismatch after the positive module compiles.
Three new native comb cases check double reciprocals at positive, negative and
zero rational inputs, with the unchanged rational program, independent
`Fraction` oracle, native replay and generic instruction receiver.

`contract-evaluability.json` declares the combined successor before execution.
Only native call capacity increases, from 64 to 72, to receive the expected 66
executions; all fuel, instruction, per-child, command and shared wall-time
bounds remain unchanged. The preceding 95 Lean statements and all old native
controls are included. The completed receipt is
`evidence/evaluability-execution.json`, with a separately retained source and
trace archive; historical proof/program/goal/contract/archive bytes are not
rewritten. The reproduction command is now:

```sh
python paper-0/formal/evaluability_run.py \
  --machine-root /absolute/path/to/pinned/adva-machine \
  --binary /absolute/path/to/pinned/adva-machine/target/debug/adva \
  --lean /absolute/path/to/lean \
  --output /absolute/path/to/new-evidence-directory
```

At that checkpoint, the live inventory also received the seven Chapter 3
additions found by the November 1 drift diagnosis, as `not-yet-formalized`.
Updating navigation did not review or prove them. Archived inventories and
generators remain bound to their original snapshots. That workflow invoked
the evaluability successor and restored push triggering; repository
required-check rules were unchanged. The Chapter 3 successor below now adds
separate component coverage, including one conjugation identity in that group.

The completed combined run is `Passed`: 66 native executions, 139 child
commands, 50,205 independently received instruction transitions, and 131 Lean
statements including the 36 new audits. Both missing-hypothesis controls reject
for their expected diagnostics. The run took 200.89 seconds within the existing
300-second shared deadline. Twenty-one engineering regressions passed before
execution; all 22 pass after adding the completed archive check. Paper 0 and
Paper I builds produce 103- and 61-page PDFs with no undefined references,
missing citations, duplicate labels or missing assets. Existing layout and
bookmark warnings remain; no TeX source or tracked PDF is changed.

## Chapter 3 coordinate foundation (2026-11-07)

`Chapter03Coordinates.lean` advances the current third chapter with 61 audited
statements, separately mapped in `chapter03-map.json`. Its field laws are
Lean's standard `Lean.Grind.Field` parameters, with standard linear-order and
ordered-ring laws added where positivity matters. A checked `fieldData`
conversion and exact rational-field bridge connect this interface to the
unchanged Chapter 2 semantics. `grind` produces kernel-checked proof terms;
each theorem's exact global axioms are disclosed. No target AES conclusion is
installed as an axiom or a structure field.

The canonical-frame construction, orientation, directional coefficients,
uniqueness and converse eikonal equation are checked in an orthonormal
coordinate plane under an explicit nonzero `q` with the required square.
Ordered-field reasoning proves that the radicand is positive for nonzero
additive intensity and that any supplied root is nonzero. Existence and
smoothness of the positive real square root and gradient-adapted frame still
need an analytic interpretation.

For the basic model, the displayed coordinate metric is symmetric, bilinear,
positive definite and invariant under the displayed affine left translation
and tangent map. The signed frame is orthonormal and positively oriented for
positive intensities/height. Its coordinate assignment action and the scaling
to the standard metric are proved. The displayed rational formula for the
assignment covector is linear; its metric-dual candidate gradient exists
explicitly, is unique, is nonzero, and satisfies the coordinate eikonal
identity. These are genuine metric/covector algebra, rather than a declaration
that the norm has its desired value. Identifying the candidate covector and
tangent map with analytic differentials remains open. Neither a smooth
Riemannian manifold nor its Gaussian curvature/completeness follows from these
algebraic proofs.

Guarded translation, scaling, inverse and reflection formulas are checked.
The ordered-field positive-height carrier is preserved by positive scaling.
Zero scaling leaves the chart. Arbitrary finite nonzero-affine paths and all
prefixes carry the expected arithmetic values; they are connected to actual
ordinary expression-tree evaluation through the unchanged Appendix C bridge.
That bridge encodes each affine section as multiplication followed by addition,
including identity events when a coefficient is one or zero. It certifies the
interpreted values of that explicit tree; it does not identify its marked
history or literal syntax with an original four-operation word.
Unique affine coefficients and chronological prefix recursions are proved.
Natural translation iterates and both conjugation orders are checked, with an
explicit nonzero natural scalar in a general field. The four-step example has
exact point coordinates and all five intermediate assignment values checked
by kernel reduction. Only the algebraic conjugation component of the new
two-layer proposition is covered, not its full conjugacy classification.

Two negative modules must reject after positive compilation: omitting the
nonzero chart height and omitting frame orientation. A concrete rational
orientation counterexample is also checked. Three new bounded native runs
check the four-step scalar path and the two conjugation orders; they do not
check native geometry. The native machine, programs and previous cases are
unchanged, and the current `chapter03_run.py` retains the preceding 131 Lean
statements and complete native regression. `contract-chapter03.json` declares
69 native runs and 148 child commands under the unchanged 72/160/300-second
caps and all preceding per-child/fuel/instruction limits.

Current navigation has 20 component-mapped environments, one fragment-certified
environment and 81 not yet formalized, still 22 source files and 102
theorem-like environments overall. Eight Chapter 3 environments now have
explicit component maps; none is silently marked wholly formalized. Full
regular-AES smooth structure, analytic derivatives, curvature/completeness,
the Laplace eigenfunction, continuous ODE/rectification, hyperbolic length and
trace trichotomy, and the punctured model remain outside this continuation.
Historical Lean sources are not imported: their old sign/frame conventions
and identity-only model corollaries do not certify the current manuscript.
The original execution archives retain their own inventories, generator and
test snapshots. Successor navigation updates are separately pinned.

The canonical reproduction command at the top now invokes `chapter03_run.py`;
the earlier `evaluability_run.py` command still checks only its predecessor
scope. CI invokes the Chapter 3 successor on the existing push/PR/manual
triggers; required-check settings are unchanged.

The completed successor is `Passed`: 69 native runs, 148 child commands,
51,137 independently received instruction transitions and all 192 Lean audits
(131 preceding, 61 new). Both new missing-height/orientation controls reject
for their expected diagnostics, alongside the two earlier negative modules.
The run took 177.71 seconds under the unchanged 300-second shared deadline.
All 26 regressions pass, including the new source/trace/archive binding test;
25 passed before execution. The separately retained receipt is
`evidence/chapter03-execution.json`. Paper 0 and Paper I builds pass at 103/61
pages with no reference/citation/asset or duplicate-label failures. Existing
layout/bookmark warnings remain; no TeX source or tracked PDF is changed.

Authoring commands (`author.py`, `fixtures.py`, `appendix_fixtures.py`,
`inventory.py`) update artifacts
for review. Verification never calls them to rewrite expected results or locks.
An intentional change requires reviewing the new statements, proof rules,
manuscript mapping and negative controls before publishing successor pins.

## Chapter 3 real-analysis successor (2026-11-07)

The five `Chapter03Analysis`, `Chapter03Flow`, `Chapter03Calculus`,
`Chapter03Rectification` and `Chapter03Dynamics` modules add 66 audited
statements using Mathlib `v4.24.0` at
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, with the existing Lean 4.24.0.
`analysis-map.json` binds every theorem and its exact global axiom set to the
unchanged current third chapter. `mathlib.lock.json` separately binds the
dependency manifest/revisions, 7,600 library source files and 3,175 observed
compiled-library objects. These are explicit trusted library/compiler builds
with integrity fingerprints, not an authenticated build-provenance theorem.
The original coordinate proofs and native machine/programs remain unchanged.

The earlier candidate assignment covector and affine tangent map are now
proved equal to actual real Fréchet derivatives. The smooth tensor is a
continuous bilinear form with verified positivity, and its unique gradient
pairs with the genuine differential. The basic model is constructed as a
`CoordinateRegularAES` on the open upper half-plane. Its carrier also has a
Mathlib smooth two-dimensional manifold structure. This is an explicit global
coordinate interpretation of the model, not a general equivalence of all
manifolds, boundary charts or Riemannian bundle/distance instances.

First and second partial derivatives are actual `deriv` operations. The
constructed metric determinant gives the positive density `sqrt(det g)` when
the intensities are positive. The declared divergence-of-gradient coordinate
Laplace--Beltrami operator reduces to the displayed diagonal second-derivative
formula and satisfies `Delta a = 2 lambda^2 a`. Its sign is checked by a
deliberately wrong-sign control. A separate intrinsic bundle Laplacian is not
identified by definition or assumed to have this eigenfunction.

The real positive eikonal square root now exists and is smooth. Actual
`arsinh` derivatives give the rectified metric gradient and magnitude
`|lambda|`; the `lambda=0` unit rectifier `a/mu` is proved separately for a
supplied smooth coordinate AES. The signed model fields have actual Fréchet
derivatives, bracket and assignment action `mu*lambda`. The curve chain rule
gives the angular propagation equation and unit speed. The constant-angle
scalar ODE has a global explicit solution, both zero/nonzero coefficient
branches, its initial value, semigroup law and uniqueness via an integrating
factor. A coordinate curve with the required tangent and nonzero height
follows that solution. General varying-angle existence, general-interval
uniqueness and arbitrary-manifold flow infrastructure are not claimed.

The Gaussian curvature and metric completeness of the model, hyperbolic
translation length/projective trace classification, and punctured E1 remain
open formal obligations. In particular, the ambient/subspace Euclidean metric
is not substituted for the Riemannian length metric in a completeness claim.
Navigation has 23 component-mapped environments, one fragment certificate and
78 not yet formalized, still 102 theorem-like environments in 22 source files.
These navigation labels do not assert whole-environment completion.

The new analytic receiving profile is separate from the unchanged native
profile. It rebuilds and exactly audits the 192 preceding source statements
as imports, then audits all 66 new theorems and four deliberate negative
modules: missing height, wrong Laplace sign, missing ODE initial value and
missing nonzero additive intensity. Both profiles must pass. The analytic
profile has its own 300-second deadline, 60-second child CPU/120-second child
wall limits and 8 GiB Lean virtual-address limit, declared before invocation
after measuring the library import costs. The native profile keeps its
original deadline and 1/4 GiB child split. Neither run refills the other's
budget or receives replacement proof/library bytes after a failure.

After the usual pinned machine preparation, reproduce both profiles with:

```sh
python paper-0/formal/prepare_analysis.py \
  --mathlib-root /absolute/path/to/new-or-pinned/mathlib \
  --lean-bin /absolute/path/to/lean/bin
python paper-0/formal/chapter03_run.py \
  --machine-root /absolute/path/to/pinned/adva-machine \
  --binary /absolute/path/to/pinned/adva-machine/target/debug/adva \
  --lean /absolute/path/to/lean/bin/lean \
  --output /absolute/path/to/new-native-evidence-directory
python paper-0/formal/analysis_run.py \
  --mathlib-root /absolute/path/to/pinned/mathlib \
  --lean /absolute/path/to/lean/bin/lean \
  --output /absolute/path/to/new-analysis-evidence-directory
```

Library fetching/cache preparation is separate engineering work. Verification
checks every declared source/cache fingerprint before receiving the proofs;
it never rewrites goals, expected audits, dependencies or locks. CI has
separate native and `real-analysis` jobs. Historical archives retain their
own inventories and test/generator snapshots, with separately pinned
successor navigation. The previous pushed coordinate checkpoint's remote
formal CI passed before this successor was implemented.

The first analytic invocation is retained as `Failed` in
`evidence/analysis-attempt-1.json` and its full source/native/analytic archive.
It stopped before proof compilation: the Lake environment query was assigned
the 1 GiB native limit even though Lake is a Lean process, and reported
`INTERNAL PANIC: out of memory`. Its 14.27 seconds and the independently
completed native run's 196.51 seconds remain recorded. They are not relabelled
as a successful combined analytic run. `contract-analysis-v1.1.json` declares
a fresh bounded successor after assigning Lake the already declared 8 GiB
Lean limit. Proof, library, goal and numerical budget bytes are unchanged;
the regression checks that exact receiving correction. Both profiles are
rerun against a separately captured successor source snapshot.

The completed first successor is `Passed` in `evidence/analysis-execution-02.json`:
the native profile has 69 runs, 148 child commands and 51,137 independently
received instruction transitions; the analytic profile has 16 child commands,
192 rebuilt import audits and all 66 new audits. There are 258 distinct
audited statements overall, including supporting lemmas. All four analytic
negative controls reject for their expected diagnostics. The native and
analytic profiles took 255.02 and 186.44 seconds respectively, each within its
own unchanged 300-second deadline. All 31 regressions pass after the archive
binding check; 30 passed before the successor. All 69 native reports are
byte-identical across attempts. The failed invocation and its additional
costs remain separately recorded. Both manuscript builds pass at 103/61 pages
without undefined references, missing citations/assets or duplicate labels;
existing layout/bookmark warnings remain and tracked PDFs are preserved.

The first remote analytic job at commit `4387911` failed during external
library preparation, before invoking the analytic receiver: the fresh Git
checkout lacked `origin`, which the official Mathlib cache tool requires.
`evidence/analysis-ci-preparation-01.json` and its complete job log retain
that failure. The independent remote symbolic/native job passed. Preparation
now registers the pinned repository as `origin` before fetching the exact
detached commit. The preceding local success and its original archive remain
in `evidence/analysis-execution-02.json`. A new source snapshot binds the
preparation correction and receipt-navigation changes; no proof, library pin,
goal, verification contract or numerical bound is changed.

The current `evidence/analysis-execution.json` and `analysis-run-03.tar.gz`
retain the clean preparation log, full new source snapshot and both fresh
bounded invocations. The native profile passes in 232.16 seconds with the
same 69 reports; the analytic profile passes in 143.57 seconds with all 192
import audits, 66 new audits and four expected negative-control rejections.
All 31 regressions pass against this archive. Both manuscript builds again
produce 103/61 pages, with the same existing layout warnings and preserved
tracked PDFs. The external library's 7,600 source and 3,175 compiled-module
fingerprints all match in a fresh checkout without changing the library lock.

## Chapter 4: ripple coordinates and pole laws

At the user's request, the remaining Chapter 3 geometric work is deferred in
`chapter03-obligations.json`: curvature, completeness for the Riemannian length
distance, length/trace, punctured E1, intrinsic interfaces and general flows.
Each entry records its source labels, missing formal prerequisites and a
condition for resuming. This changes work order; it does not turn an
unformalized manuscript proof into a new mathematical open problem.

`Chapter04Ripples.lean` supplies 36 statements in the manuscript's complex
continuation chart. The map is actual complex division, with its imaginary
part derived explicitly. Positive determinant and height give a nonzero
denominator and positive image height. Pullbacks of positive output levels
give the affine horizontal-line case and the non-affine completed-square
circle equation. Radius positivity, the unique real-axis contact, height
bounds and nesting of the **enclosed disks** are proved. Distinct positive
level sets are disjoint, not subsets of one another. The exact inversion
example, contravariant preimages and the persistence of a whole pencil under
posttranslation are included.

`Chapter04Poles.lean` supplies 21 statements. Pole covariance and the stepwise,
all-prefix and first-exit rigidity laws are proved for actual bijections of a
pointed carrier, under the convention `compose P Q = P after Q`. Additional
real matrix lemmas verify the nonzero pole column, its vanishing denominator
and nonvanishing numerator. The PGL/projective-line representation and the
matrix-to-bijection/affine-stabilizer identifications remain explicit separate
obligations; this is not a formal certificate of those full manuscript
environments. No matrix coefficients or expected pole laws are added as axioms.

There is a source wording limitation in `rem:p0-pole-forward`: a first exit
from the affine sector does not make every later step non-affine. The actual
maps `J` followed by `T_s` have the same finite pole zero and the same ripple
pencil. The correct per-step criterion is the one in the preceding lemma.
`chapter04-map.json` and the authoritative status register retain this finding;
the prospective transport discussion is not certified by the component map.
Manuscript source text is preserved for a separate wording amendment.

The new source-bound map attaches components to seven environments. Live
navigation has 30 component-mapped environments, one fragment-certified and
71 not yet formalized, across the unchanged 22 manuscript files and 102
theorem-like environments. These counts do not certify whole environments.
The compiler/standard library and fingerprinted Mathlib remain trusted builds;
the existing library lock is unchanged. All 57 exact theorem audits disclose
only their actual subsets of `propext`, `Classical.choice` and `Quot.sound`.

`contract-chapter04.json` declares a separate 300-second profile with the same
numerical bounds as the existing analytic profile. It has two positive modules,
57 audits, eight child commands and four specific rejecting controls: missing
positive determinant, missing circle guards, missing affine-step hypothesis
and reversed composition order. Both preceding profiles remain required under
their unchanged contracts, with historical archives retained. After the usual
pinned library preparation, invoke the new profile with:

```sh
python paper-0/formal/chapter04_run.py \
  --mathlib-root /absolute/path/to/pinned/mathlib \
  --lean /absolute/path/to/lean/bin/lean \
  --output /absolute/path/to/new-chapter04-evidence-directory
```

CI invokes Chapter 4 after the separate Chapter 3 analytic profile and uploads
its evidence separately. It does not reuse or refill either profile's deadline.

The completed `evidence/chapter04-execution.json` and
`chapter04-run-01.tar.gz` retain the 70 pinned formal source files plus the
lock, 22 manuscript files, all three profile reports, native traces/replay
receipts, exact Lean audits, negative diagnostics, workflow and both build
logs. The native, analytic and Chapter 4 profiles pass in 174.33, 136.43 and
58.91 seconds respectively, each within its own unchanged 300-second limit.
All 69 native reports are byte-identical to the preceding success. There are
315 distinct audited statements overall; the analytic import rechecks are not
counted twice. All 35 regressions pass against the completed archive, following
34 successful pre-receipt checks and the then-pending archive-binding test.
Both builds pass at 103/61 pages without unresolved references/citations,
duplicate labels or missing assets. Existing overfull boxes remain (2/8,
maximum 11.13/105.15 pt), along with existing bookmark/underfull warnings;
tracked PDFs and TeX sources are unchanged.

## Apollonius modulus, metric circles and bisectors

`Chapter04Apollonius.lean` supplies 39 new audited statements corresponding to
`eq:p0-apollonius-pencil` and the surrounding zero-pole classification prose.
It imports the unchanged ripple coefficients and actual complex map. The
existing Mathlib lock already contains the complex-norm objects used here;
no source, cached-library fingerprint or dependency revision is changed.

For nonzero `A,C`, the numerator and denominator factor at the real zero
`q=-B/A` and pole `p=-D/C`. Excluding the pole proves the actual norm-level
equivalence with weight `k=r*|C/A|`. Nonzero determinant gives distinct foci,
which exclude the pole from the weighted locus and identify the entire guarded
complex level set. Positivity of the manuscript's determinant implies the
nonzero hypothesis. A positive-height input automatically avoids the real
pole; a full complex-plane statement must retain the denominator guard.

Nonnegative `k` permits the reversible squared-distance equation. For `k!=1`,
completing the square gives the real center `(q-k^2*p)/(1-k^2)` and radius
`|k|*|q-p|/|1-k^2|`. The locus is proved equal to an actual `Metric.sphere` of
the standard complex Euclidean distance. Positive `k` and distinct foci give
a positive radius and an upper-half-plane witness. For `k=1`, the actual
equidistance locus is exactly the vertical line `re z=(q+p)/2`. Final theorems
specialize these results to the guarded Möbius level sets.

Zero and negative levels remain separate. The zero level is the single real
zero in the full complex domain and empty after restriction to the upper
half-plane; negative levels are empty. The source's proper-circle wording
therefore requires positive `r`. Explicit positive proofs also show why the
pole, sign and distinct-focus guards matter: total complex division assigns
zero at the pole, negative unit weight is not the bisector, and equal foci at
unit weight give the whole plane. These are recorded in `apollonius-map.json`
and the status register; manuscript source text is preserved.

The map is attached to a numbered equation and prose, not a theorem-like
environment. `inventory.json` now has a separate `equation_components` entry
with all 39 statements. The 102 environment counts stay at 30 component-mapped,
one fragment-certified and 71 not yet formalized; none is promoted by this
equation map. The development has 354 distinct audited statements overall.
All new exact axiom sets disclose only their actual subsets of `propext`,
`Classical.choice` and `Quot.sound`. Compiler/standard-library and fingerprinted
Mathlib builds retain their declared trust boundary.

`contract-apollonius.json` fixes a separate profile with the unchanged numerical
bounds of the preceding Chapter 4 profile. It has eight child commands: version
and library-path checks, a source rebuild with 36 exact ripple import audits,
39 new audits and four rejecting controls for the pole, nonnegative weight,
nonunit weight and distinct foci. The 36 import audits are not new statements.
All three predecessor profiles remain independently required under their
unchanged contracts. Run the additional profile after pinned preparation with:

```sh
python paper-0/formal/apollonius_run.py \
  --mathlib-root /absolute/path/to/pinned/mathlib \
  --lean /absolute/path/to/lean/bin/lean \
  --output /absolute/path/to/new-apollonius-evidence-directory
```

CI runs this as its own bounded step after the original real-analysis and
ripple profiles, with a separate artifact. Historical receipts keep their own
source locks and navigation snapshots; current navigation and its receipt test
have separately pinned successors.

The completed `evidence/apollonius-execution.json` and
`apollonius-run-01.tar.gz` retain 79 pinned formal sources plus the lock,
22 manuscript sources, the workflow, all four reports, native traces/replay
receipts, exact Lean audits, negative diagnostics and both build logs. All
four profiles pass in 174.35/131.33/52.99/73.61 seconds respectively, each within
its own unchanged 300-second deadline. The 69 native reports remain
byte-identical to the preceding success. All 39 regressions pass against the
completed archive; the preparatory log retains its 38 passes and then-pending
receipt test without relabelling that check. Both builds pass at 103/61 pages
with no unresolved references/citations, duplicate labels or missing assets.
Existing overfull boxes (2/8, maximum 11.13/105.15 pt) and bookmark/underfull
warnings remain; manuscript text and tracked PDFs are unchanged.

## Continuation order

The §2 continuations and §3 coordinate/real-analysis bridge are received above.
The deferred geometric steps and their prerequisites are now in
`chapter03-obligations.json`. Advance easier remaining Chapter 4 work first:
the projective-line/PGL bridge and elementary coefficient action laws, keeping
the intrinsic horocycle and chart-independence obligations separate. The
general-manifold/bundle identifications retain their explicit hypotheses.
Reuse old Lean material
only after a legacy-to-current statement map. Each theorem still needs its
formal prerequisites and evidence; topology, smooth geometry, convergence and
proof-library translation are not supplied by this algebraic foundation.

Original implementation and documentation by Codex (OpenAI), contributed under
CC0. Source ownership or an account proxy is not independent human review or
endorsement. Correctness claims are limited to the retained executed checks.
