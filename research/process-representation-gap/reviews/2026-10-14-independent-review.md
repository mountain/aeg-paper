# Independent mathematical and engineering review of PR 18

Reviewed commit: `5e4a620ce3a3214159e38b6344a0ae2dd98aa343`.
Review date: 2026-10-14. Decision: **changes required; not ready to merge**.
No manuscript theorem, original contract or frozen evidence is replaced by this review.

## Independently confirmed results

The accompanying `independent_review_2026_10_14.py` uses its own free-word
substitution implementation, rather than either exp5 semantic implementation.
It checks every one of the 5461 committed raw rows (Artin images and permutations),
and independently obtains the four counts **5461 / 1457 / 577 / 6**.
It checks both inverse relations and the braid relation on all three free
generators. The product probe has one image; the selected six-letter probe has
577 distinct images. This separation statement remains restricted to crossing
words of length at most six. Artin faithfulness is a classical theorem used to
identify image triples with braid elements, not a theorem proved by enumeration.

The declared convention is internally consistent: append on the right means
`Phi(w a) = Phi(w) o phi(a)`. Evaluation on a free word therefore applies the
last crossing first. Left-to-right history order should not be confused with
left-to-right application of a left action to a probe. A right-action or
pullback interpretation must be stated at a future geometric interface.

The report's W2 permutation `[1,2,0]` is a transcription error. For
`s1 s2 s1 = s2 s1 s2` the declared zero-based convention gives `[2,1,0]`.
The raw evidence is correct. Also, the pure braid `s1^2` is not a torsion
element: the phrase “see torsion” should mean a declared process defect, or be
replaced by “detect a nontrivial pure braid”.

For exp6 witness 4, all **20** coordinate separation certificates are recomputed
from independently transcribed square geometry and obstacle timetable. Their
corners, inequalities and gap-free coverage of every edge over `[0,1]` agree.
The certified clearance bound **3/4** holds. A separate analytic calculation
gives, on `[1/4,3/8]`,

`d(t)^2 = (8t-1)^2 + (30-80t)^2`,

whose minimum at `301/808` is `400/101 = 40400/10201`.
Before that interval the obstacle height is 10; after it the horizontal
distance is at least 2, so this is also the global minimum. Thus 3/4 is a
conservative certificate bound, not the exact minimum clearance.
P2 is stationary until 1/2, and its bottom edge contains the obstacle centre
at **3/8**, independently proving collision. Both free-space paths remain
embedded by the separate argument that they are translations of one fixed
simple square. This particular witness survives the checker defect below.
P2 uses a nondecreasing time map with a waiting interval; it is not a strictly
increasing reparameterisation. No speed-constrained physical-rope claim follows.

## Merge blockers and smallest honest repair

### R1 — Both interval self-embedding routes accept a collapsed triangle

Take three nodes at time 0:
`(0,0,0), (1,0,0), (0,1,0)`,
and at time 1:
`(0,0,0), (-1,0,0), (0,-1,0)`.
Linear interpolation collapses all three nodes at time **1/2**. Both endpoints
are embedded triangles. Nevertheless `check_self_embedding()` and the independent
`self_embedded_verdict()` return **valid** with no interval certificates.
All three edge pairs are adjacent, so the interval obligation is vacuous.
Both routes also lack whole-interval adjacent-overlap and edge-nondegeneracy
obligations. Different algorithms sharing this omission are not independent
evidence of a sound embedding predicate.

Repair: add whole-interval nonzero-edge, node-distinctness and adjacent-edge
intersection obligations, using separately justified methods in the two routes.
Alternatively, explicitly restrict certification to verified rigid translations,
and return `not-certified` for all other motions until these obligations exist.
Add the collapsing triangle and an adjacent-overlap regression. Do not repair
this by checking one extra midpoint: degeneracy can occur at other interior times.
For a closed polygon reject fewer than three nodes as an embedding input.

### R2 — The purported Reidemeister calculus generates nonplanar records

`r2_insert(diagram((),()), 0, 0)` produces `(1,2,-1,-2)`.
Ignoring over/under signs, each crossing has an odd number of entries between
its occurrences. This violates the necessary Gauss parity condition for a
generic closed plane curve. More seriously, the **actual committed R2 fixture**
`r2_insert((1,-1,2,-2), 1, 3)` produces
`(1,3,4,-1,2,-3,-4,-2)`, with odd intervening counts for labels 3 and 4.
Thus this is not merely an out-of-fixture concern. The independent route repeats
the same insertion rule. Round-trip identity and writhe cancellation do not
prove that either intermediate record is a classical knot diagram or that a
planar bigon exists.

Repair: use an explicitly embedded planar tangle/diagram, carrying cyclic order,
face/location and over/under information, and verify the local disk and strands
on which R2 acts. Gauss parity is a useful rejection test, **not a sufficient
realisability test**. If that exceeds this round's scope, retain the current
results as an abstract signed-word calculus and withdraw its Reidemeister/knot
process claims, including gate C's topological interpretation. R1 sign/order
restrictions likewise describe a chosen syntactic convention, not all legal
oriented Reidemeister-I moves. Lack of R3 is incompleteness; unsound R2 is a
different problem and cannot be discharged by declaring incompleteness.

### R3 — A strict torus can carry nontrivial spatial knots

`environment_records().thickened_surface.not_strict_embedding` says that a
strict simple closed curve in `S^2 or T^2` cannot carry a classical nontrivial
knot. The `T^2` part is false. A primitive `(2,3)` curve on the standard embedded
torus is a trefoil. Intrinsic surface embedding has no self-crossings, while its
projection into a plane can have crossings. The torus embedding into R3 is
essential data for interpreting a spatial knot type.

Repair: retain the sphere statement with its tame embedded-sphere assumptions;
explicitly allow torus knots; specify the **standard unknotted embedding** and
meridian/longitude framing for the free-space witness. A longitude on a knotted
torus need not be an unknot. Surface isotopy preserves the homology class; an
allowed mapping-class homeomorphism changes the equivalence relation and need
not be isotopic to the identity or extend in a specified ambient environment.
Orientation/marking must decide whether `(p,q)` and `(-p,-q)` are identified.
Update generated evidence as a successor record rather than silently replacing
the historical claim.

### R4 — Verification refreshes the frozen baseline; raw replay is incomplete

`verify_all.py` calls `freeze_contracts.py` before experiment validation.
That tool overwrites the digest of an already frozen version. The review's
isolated temporary-copy mutation test changes `example.v1.json` and obtains exit
0 and a refreshed digest. Downstream evidence comparisons may detect further
differences, but this is not an immutable contract guard; in particular the
ledger itself is absent from `ci_check.py`'s exact-artifact list.

Also, `check_determinism.py` invokes the experiment scripts without `--raw`.
Exp5's raw word table is neither regenerated there nor consumed by its original
independent route. `ci_check.py` compares the unchanged raw working file to its
own HEAD blob: that is **not raw evidence replay**. The review's independent
5461-row comparison fills this gap for the reviewed exp5 table, not the general
pipeline. Missing recorded evidence is treated as optional by the determinism
harness, and filesystem glob enumeration in CI cannot establish completeness.

Repair: make verification read-only for contracts; refuse modification of an
existing version even in the freezing utility; only register a new version.
Compare the ledger against a pinned baseline, require an explicit inventory of
all expected scripts/contracts/evidence/raw files, regenerate main and raw
outputs into a temporary directory, and compare those outputs to committed
blobs. Test old-version mutation, ledger mutation, deleted evidence and a
single mutated exp5 raw row. Contract hashes in this head agree, but the Git
history introduces contracts, implementations and evidence together: it cannot
independently prove the claimed pre-implementation registration chronology.

## Arithmetic gates: status and corrections

| Gate | Review conclusion |
|---|---|
| A | Round trips support finitely described literal records. This is a tagged string serialisation, not an implemented arithmetic-expression geometric simulation. A structural induction can prove the codec for a precisely restricted canonical type grammar; seven fixtures alone are not that proof. |
| B | Code equality is finer than topological equivalence; the meridian/longitude witness supports failure of the stated iff only with the standard torus embedding specified. This refutes this chosen equality relation, not the possibility of a faithful arithmetic representation equipped with a semantic equivalence predicate. |
| C | Encoding/decoding and concatenating chosen histories work syntactically. Endpoint replay alone does not establish process equality; the local legality grid covers only two kink records. Unsound R2 and the interval embedding defect prevent promotion to a faithful knot-process interface. |
| D | Bounded searches terminate with incomplete outcomes. General tame-knot decidability is a classical external result, not implemented here and not a dynamic-obstacle planning theorem. Boundaries on literal coordinates/nodes do not by themselves prove failure to represent every knot type modulo isotopy; specify the target category. |

Writhe is not an ambient-knot invariant and should not be called a necessary
constraint on ambient knot type. Nonzero linking number obstructs a split link;
zero linking number does **not** certify splitting. A slope classifies essential
surface curves only with its surface, basis, orientation and equivalence fixed.
These limitations must travel with the exported claims.

The 63-candidate typed-hole result is a finite negative over a declared feature
grid. It justifies investigating an explicit input-context family; it does not
prove that every bounded residual, every local feature or arithmetic encoding
must fail. The other experiments remain research-model results rather than
native Adva learner or continuation semantics.

## Minimal future interfaces, after repair

Paper IV can first import a typed **representation contract**: native domain,
allowed contexts/continuations, equivalence relation, encode/decode, legality
predicate, scope and theorem/evidence provenance. Keep syntactic injectivity,
semantic reflection/preservation and decision completeness as separate claims.

Process geometry should distinguish intrinsic surface, ambient embedding,
thickening and obstacles; carry absolute-time schedules, the time map, relative
boundary/marking conditions and whole-interval certificate coverage. Preserve
literal process history or its source digest when costs or construction are
observable; a group element or knot type cannot substitute for that history.

Adva should initially consume a documentary research package only: repository,
full commit, path/blob/hash, versioned contract, checker/profile, bounded outcome
and certificate/provenance references. No native continuation or learner authority
is granted. A later executable profile needs its own legal append/composition
and identity rules plus the regressions above.

## Reproduction and merge condition

`python3 reviews/independent_review_2026_10_14.py` (relative to this research
directory) intentionally exits **1** on the reviewed implementation. Ordinary
and `-O` output agree. Exit 1 reports reproduced merge blockers, not a failure
of the confirmed braid or timing computations. This script is outside the
original experiment harness and does not overwrite frozen evidence.

Merge requires sound embedding and local-move contracts (or explicit narrowing
of claims), correction of the torus statement and arithmetic-gate language,
immutable contract/raw evidence checking, and a complete replay at the repaired
head. A green original workflow is insufficient to discharge these findings.

Sources used for classical facts:

* [Artin faithfulness](https://arxiv.org/abs/math/0203167).
* [Gauss parity and planar realisability](https://jeffe.cs.illinois.edu/teaching/comptop/2020/notes/07-Gauss-codes.html).
* [Torus knots as simple curves on an embedded torus](https://digitalcommons.usu.edu/gradreports/1130/).
