# exp6 — knot deformation processes and environment dependence

Work plan: `AEG-process-representation-work-plan.md`, section 6 (实验六) and
section 5 (shared frozen template).
Contract: `contracts/exp6-knot-deformation-environment.v1.json`, version 1,
frozen, sha256 `1b8a6d0ddbce2efd708a3875e7c6f32bd05947ffb1b434e74e4d5c5f5cfa82ac`
(ledger entry in `contracts/FROZEN.sha256`).

## 1 Question

How is a *legal deformation process* of a knot represented — not just its final
knot type — and in each declared environment which arithmetic representation is
faithful for the state, the process and the continuations? The five declared
environments are R³, the strict 2-sphere, the strict torus, a thickened surface
Σ × I, and an obstacle environment M \ O_t.

## 2 Frozen contract summary

* **Native object** finite piecewise-linear (PL) ropes with exact rational
  control-node coordinates: at most **16 control nodes**, at most **12 time
  segments**, at most **3 known obstacles**, action-search depth at most **8**.
  Tame embeddings only; no wild knots; no arbitrary real input.
* **Process** k_t : S¹ → M with every instant a legal embedding and
  k_t(S¹) ∩ O_t = ∅ over the whole declared time interval. Merely allowing
  continuous maps or an ordinary homotopy would wrongly let the rope pass
  through itself; that is not a deformation here. If a task uses ambient
  isotopy, the ambient extension and the relative boundary data are required.
* **Two computational routes**: topological (complete diagram with crossing
  over/under information plus instantiated local moves, each recording position,
  before/after state and provenance) and geometric (control nodes,
  piecewise-linear time trajectories, explicit obstacles, exact rational
  interval certificates).
* **Observations** three tiers: existing summary (endpoint state); bounded
  pre-declared enhancement (endpoint + action word + obstacle timetables +
  stored interval certificates); full history / exact semantics as the
  upper-bound control.
* **Outcomes** success, expected negative, implementation error, budget
  exhausted, unknown — pairwise distinct, never collapsed.
* **Negative controls** 13, each naming the specific diagnostic it must raise.

## 3 The five environment contracts

| Environment | Native object | Information that must be preserved | Instantiated here |
|---|---|---|---|
| 3-dimensional Euclidean space | S¹ embedded in R³ (finite rational PL) | the embedding plus the ambient-isotopy contract: ambient extension and relative boundary conditions; a physical task additionally carries metric/thickness | interval self-embedding certificates; constructive ambient translation certificates (`w4-P1`, `w4-P2`, `w3-free`, `w3-plan`, `w5-rope`) |
| Strict 2-sphere | S¹ embedded in S² (simple closed curve on the surface) | simplicity and isotopy class on the surface; no 3-space isotopy contract and no room for a thickening | a curve bounding an embedded disk is unknotted (planar case computed exactly: planarity + convexity + fan triangulation); the on-sphere step is the cited Jordan–Schoenflies statement |
| Strict torus | S¹ embedded in T², primitive slope (p,q) in a **fixed oriented basis** | the integer slope, or contractibility; basis, orientation and allowed mapping classes | slopes (1,0), (0,1), (1,1): all primitive (gcd 1), geometric intersection numbers all 1; in a fixed basis the meridian and longitude are distinct classes; the classification itself is a cited classical statement |
| Thickened surface Σ × I | diagram on Σ with labelled crossings carrying over/under data (curve in Σ × I) | the surface diagram, crossing over/under data, handles and environment markings; stabilisation is a separate question | a Gauss-word + crossing-sign calculus; writhe effects of the instantiated moves; the over/under-free encoding is shown to lose information |
| Obstacle environment M \ O_t | S¹ embedded in M \ O_t, obstacles = closed rational balls with piecewise-linear centre timetables, or closed polygonal loops | obstacle geometry, identity, timetable, rope position, allowed control, safety margin | witness 3 (static ball, ball radius 1/2, centre (1,1,0)); witness 4 (moving ball, radius 1/4); witness 5 (untraversable closed loop) |

Distinctions the report keeps explicit: a strict simple closed curve in S² is
always a space-unknot, so classical non-trivial knots live only in the *thickened*
model (crossing over/under data on a sphere/torus diagram models Σ × I, never a
strict embedding in the surface); virtual knots additionally allow stabilisation
and are not conflated with knots in a fixed T² × I; a zero-thickness topological
rope is modelled and a physical rope (radius, length, curvature, velocity limits)
is a different contract; isotopy along a **fixed** torus is not spatial isotopy
after leaving it.

## 4 Exact headline results

All numbers below are exact rationals produced by the two routes; no floating
point appears anywhere in a witness, comparison, predicate or cost. Both routes
are byte-identical under `python3` and `python3 -O` (`cmp`).

* **36 whole-time-interval certificates** are stored for the two certified
  motions: the witness-4 safe parameterisation gives 5 time boxes × 4 edges =
  **20**, and the searched replacement path gives 4 boxes × 4 edges = **16**,
  each with an exact rational lower bound on the distance to the obstacle; every
  certified case has **zero** uncertified boxes, and the per-box certificate
  table is in the `.raw.json`.
* Witness-4 safe parameterisation **w4-P1** is certified clear with an exact
  rational clearance lower bound of **1** (safety margin **1 − 1/4 = 3/4**),
  per-box lower bounds `10, 1, 2, 3, 10` on the five time boxes; the
  hand-checked true minimum squared distance on the critical window is
  **40400/10201**, reproduced by closed-form minimisation of
  (8t−1)² + (80·(3/8 − t))² at t = 301/808.
* The same rope path under the other time parameterisation **w4-P2** is
  **rejected** by the continuous check: collision at t = **3/8**, edge 0,
  parameter s = **1/2**, point **(1,0,0)**, distance² = **0**, radius² = **1/16**.
* Witness 3: the free-space path is legal, the same path with one obstacle is
  rejected (exact: t = **1/4**, edge 1, s = **1/2**, point **(1,1,0)**), and a
  replacement path **`y+2, x+2, x+2, y-2`** is found and certified clear (16
  certificates, margin **1/2**, 260 search nodes, 2 pruned prefixes).
* Witness 5: linking number of rope and untraversable loop is **0** at the start
  and **±1** at the end, the free path must collide (exact: t = **2/3**, edge 3
  of the rope against edge 3 of the loop, parameters (1/2, 1/2), point
  **(0,0,0)**), and both linking routes agree on the rotated control (spanning
  disk: **1** at (5/4, 0, 0); signed crossing count: **1** in the projection
  along (1,2,3), two crossings of sign +1).
* Keyframes are **never** a safety proof: the `keyframe-blind` fixture is
  embedded at t = 0 and t = 1 and **not embedded at t = 1/4** (edges 0 and 3
  cross at parameters (2/5, 4/5), point **(4/5, 0, 0)**).
* Topological route: R1+ changes the writhe by **+1**, R1− by **−1**, R2 by
  **0**; R1 and R2 round trips return the original diagram record exactly;
  reachability to depth 2 gives 7 then 67 diagrams inside the declared
  (incomplete) calculus.

## 5 The six mandatory witnesses

1. **Same knot type, different deformation history** (topological). Identity path
   (0 moves) versus R1 kink insertion followed by its inverse (2 moves,
   `word=1,-1;signs=1` → `word=2,-2,1,-1;signs=1,1` → `word=1,-1;signs=1`).
   The endpoint states are literally equal, the literal histories and costs
   differ (46 / 85 / 207 storage bytes for the three tiers). **It is not
   claimed** that the two paths differ under process homotopy.
2. **Environment changes equivalence.** In a fixed oriented basis the meridian
   (1,0) and longitude (0,1) are distinct primitive classes (slopes differ and
   neither is the negative of the other, geometric intersection number 1), so
   the strict-surface task does **not** identify them; in unobstructed R³ both
   are unknots, so the free-space task does. The basis-swap homeomorphism
   (det −1) sends (1,0) ↦ (0,1), which would identify them and change the
   equivalence contract — reported, never silently adopted.
3. **Obstacle changes legality.** Free-space path `w3-free` (offsets (−2,0,0) →
   (2,0,0)) is certified legal in free space; adding the static ball (centre
   (1,1,0), radius 1/2) makes the continuous check reject it at t = 1/4, point
   (1,1,0). Replacement found inside the declared submodel: `y+2, x+2, x+2, y-2`
   (margin 1/2). With the search budget cut to depth 2 the same search returns
   **budget_exhausted** after 36 nodes — a bounded-domain result only: a failure
   in this fixed-node-count, fixed-parameter-family, fixed-action-dictionary
   submodel does **not** prove that no legal deformation exists.
4. **Time changes legality.** Identical start configuration, identical end
   configuration, identical knot type (the unknot at every instant, since the
   rope is a translate of a planar square bounding a flat disk), same rope path,
   two time parameterisations, one frozen moving-obstacle timetable (radius 1/4;
   centres (1,0,10) → (1,0,0) → (1,0,10) at t = 0, 1/4, 3/8, 1/2, 5/8, 1):
   w4-P1 is certified clear over the whole interval with margin 3/4, w4-P2
   collides at t = 3/8. The 20 continuous segment certificates are stored, and
   the raw per-box certificate table is in the `.raw.json`.
5. **Optional joint topological witness.** The obstacle is an untraversable
   closed loop (the boundary of a flat rectangle). The rope is the unknot at
   both ends, so its knot type carries no linking information; the linking
   number is 0 → ±1, and it jumps exactly when the rope passes through the
   loop's spanning disk at the same parameter value where the continuous check
   reports the collision (t = 2/3). Linking number is used as a **necessary
   constraint** (invariant under disjoint isotopy, cited classical fact) and is
   **not** claimed to be a complete link invariant.
6. **Negative controls.** See the table in section 8 — all 13 raise exactly the
   declared diagnostic.

## 6 The four arithmetic gates

| Gate | Question | Verdict | Evidence |
|---|---|---|---|
| A encodable | can diagram, finite action word and rational parameters become an integer string with an implemented round trip? | **satisfied on the declared finite model** (computationally-verified-example) | exact encode/decode round trip on all 7 fixtures; 7 distinct encodings; the encoding is prefix-free and self-delimiting |
| B state-faithful | is encode-equivalence *iff* declared state-semantics equivalence? | **satisfied for literal-data semantics; refuted for topological semantics** | literal: injective + exact round trip. Refutation witness: the meridian (1,0) and longitude (0,1) have different encodings but are equivalent under the free-3-space task, so topological equivalence does not imply encode-equivalence. Syntactic injectivity of the integer string does **not** decide topological equivalence. Writhe, linking number and torus slope are stated only as necessary constraints inside their declared domains; no polynomial invariant is computed and no completeness claim is made |
| C process-faithful | do encoded actions/compositions/continuations correspond to the native process, with legality reflected and no task-distinguishable process merged? | **satisfied on the declared domain** (computationally-verified-example) | explicit E and D: D(E(h)) reproduces the endpoint diagram exactly; E(h₂·h₁) = E(h₁) ++ E(h₂) exactly (declared concatenative composition); the encoded R1-deletability predicate reflects native legality on the declared grid; the two witness-1 histories share one endpoint state and have different history encodings |
| D completeness | can all target states be represented, all target processes generated, all semantic equivalences proved by rewriting, does the decision algorithm terminate? | **no / no / no / yes-with-declared-incomplete-outcomes** | states: bounded to ≤ 16-node rational PL curves (no wild knots, no arbitrary real input); processes: the declared action dictionary up to the declared depth (outside it → budget_exhausted or unknown); rewrites: R1 and R2 only — **R3 is not instantiated**, so the calculus is incomplete by declaration; termination: yes for all declared finite exact checks, with `not-certified` as a declared outcome |

Gate D carries the required statement explicitly: classical tame knot equivalence
has a decision algorithm (cited), but that gives a finite-depth action search
**no** decision completeness, and contracts with motion constraints and dynamic
obstacles must be re-studied separately. The four gates are not mutually
implied, and the evidence records that as a separate item.

## 7 Independent route

`experiments/exp6_knot_deformation_environment_independent.py` shares **no**
semantic helper with the primary: not the fixture builder (the fixtures are
transcribed literals, so a transcription error surfaces as a disagreement), not
a distance routine, not a certificate routine, not a move implementation, not a
cost or encoding helper. Only `gapkit` serialisation, the frozen contract and
the primary's evidence file (read as data to be checked) are shared.

Different algorithms for the same predicates:

| Predicate | Primary route | Independent route |
|---|---|---|
| self-embedding over a whole time interval | multilinear box-hull separation, exact Fourier–Motzkin elimination, subdivision | closed-form exact minimisation (2×2 normal equations + boundary enumeration) plus an exact rational motion/Lipschitz bound, time subdivision |
| ball clearance over a whole time interval | per-coordinate hull / separating-normal certificates, evaluation sampling for collisions | clamped-critical-parameter closed form plus the exact motion bound |
| linking number | algebraic intersection with a spanning disk | signed crossing count of a generic projection (cross-checked on a rotated Hopf-like control) |
| local moves | tuple-based calculus | independently written list-based calculus + hand-computed table entered as literals |

Result: **0 disagreements**. Every primary verdict is reproduced (w4-P1 clear,
w4-P2 and w3-free and the loop path rejected with the same times, parameters and
points, keyframe-blind invalid at t = 1/4 with parameters (2/5, 4/5),
w3-plan/w5-rope/w4-P2 self-embedding valid), the linking values 0 and ±1 match,
the writhe deltas match, and **all 20 stored interval certificates were
re-derived from independently recomputed box vertices with no problem**. The
independent route raises `EXP6-ROUTE-DISAGREEMENT` on any mismatch; its own
negative controls (hand-table mutation, route disagreement, contract drift,
wrong-sign R1 deletion) all fire. Residual shared mathematics is stated, not
hidden: both routes evaluate the same rational quadratics; what differs is the
interval-level decision procedure and the linking-number formulation.

## 8 Negative controls

| id | expected code | observed code |
|---|---|---|
| contract-drift | `EXP-CONTRACT-DRIFT` | `EXP-CONTRACT-DRIFT` |
| crossing-information-dropped | `EXP6-CROSSING-INFO-DROPPED` | `EXP6-CROSSING-INFO-DROPPED` |
| torus-basis-swapped | `EXP6-TORUS-BASIS-SWAP` | `EXP6-TORUS-BASIS-SWAP` |
| obstacle-timestamps-omitted | `EXP6-OBSTACLE-TIMETABLE-MISSING` | `EXP6-OBSTACLE-TIMETABLE-MISSING` |
| keyframe-only | `EXP6-KEYFRAME-BLIND` | `EXP6-KEYFRAME-BLIND` |
| self-passage-allowed | `EXP6-SELF-PASSAGE-DETECTED` | `EXP6-SELF-PASSAGE-DETECTED` |
| route-disagreement | `EXP6-ROUTE-DISAGREEMENT` | `EXP6-ROUTE-DISAGREEMENT` |
| hand-table-mismatch | `EXP6-HAND-TABLE-MISMATCH` | `EXP6-HAND-TABLE-MISMATCH` |
| encode-decode-roundtrip | `EXP6-ENCODE-ROUNDTRIP` | `EXP6-ENCODE-ROUNDTRIP` |
| model-beyond-budget | `EXP6-BUDGET-EXCEEDED` | `EXP6-BUDGET-EXCEEDED` |
| search-budget-claim | `EXP6-BUDGET-EXHAUSTED` | `EXP6-BUDGET-EXHAUSTED` |
| ambient-extension-claim | `EXP6-AMBIENT-EXTENSION-MISSING` | `EXP6-AMBIENT-EXTENSION-MISSING` |
| strict-sphere-knot-claim | `EXP6-STRICT-SPHERE-KNOT` | `EXP6-STRICT-SPHERE-KNOT` |

Polarity is the one the work plan requires: every control body *asserts the
distorted claim* and therefore fails; a control that passed silently would be a
bug. The recorded `detail` strings name the concrete distortion (e.g. the
over/under-free encodings coincide while the full records differ; the basis swap
identifies the meridian and longitude; the timestamp-free obstacle record is
refused; keyframe-only says valid while the continuous check says invalid at
t = 1/4). Extra declared diagnostics that are not controls
(`EXP6-OBSTACLE-TIMETABLE-INCOMPLETE`, `EXP6-SEPARATION-INVALID`,
`EXP6-MOVE-ROUNDTRIP`, …) guard the same obligations internally.

## 9 Cost per channel (three tiers)

Units are declared in the evidence (`costs.measurement_note`): observations =
declared observation points read; computation steps = exact obligations to
produce the payload; verification cost = stored exact claims an independent
checker must re-derive; storage/structural = canonical serialised size and
retained field count.

| Family | Tier | kind | storage bytes | structural size | steps | observations | verification |
|---|---|---|---|---|---|---|---|
| witness 4 (time parameterisation) | 1 | endpoint | 205 | 29 | 4 | 1 | 0 |
| witness 4 | 2 | endpoint + actions + obstacle timetable + certificates | 369 | 49 | 10 | 6 | 20 |
| witness 4 | 3 | full record (both models + obstacle) | 1671 | 183 | 20 | 12 | 40 |
| witness 1 (histories) | 1 | endpoint | 46 | 2 | 2 | 1 | 0 |
| witness 1 | 2 | endpoint + moves | 85 | 7 | 4 | 2 | 2 |
| witness 1 | 3 | full provenance | 207 | 17 | 6 | 2 | 4 |

Tier 1 cannot decide witness 4 (equal endpoints, equal knot type, different
executability) or witness 1 (equal endpoint state). Tier 2 repairs exactly the
two environment/time dependencies at 369/205 of the tier-1 payload for witness 4
(storage bytes); it is bounded by the declared budget and is not claimed sufficient for every
declared question. Tier 3 is the upper-bound control only: retaining everything
is not thereby a recommended minimal repair (work-plan section 9).

## 10 What is explicitly NOT claimed

* No completeness of any representation for all tame knots, and **no general
  knot-motion planner**; only concrete candidate paths are verified first, then
  a bounded search inside one fixed submodel. A failure inside that submodel is
  reported as `budget_exhausted`/`unknown`, never as non-existence.
* Keyframes alone are never a continuous safety proof; the continuous claim here
  is always carried by stored interval certificates, and where no certificate
  and no witness exists inside the budget the answer is `not-certified`
  (demonstrated: the keyframe-blind fixture at subdivision depth 0 returns
  not-certified with the uncertified box `[0,1]`).
* No isotopy claim from a visually suggestive construction; knot invariance is
  inferred nowhere.
* No bridging of braid closure, Markov equivalence or R-move completeness to
  knot equivalence; the classical R-move theorem is cited, not verified or
  implemented, and R3 is **not instantiated**.
* No claim that linking number is a complete link invariant, and no polynomial
  invariant is computed.
* Strict S² and strict T² results are cited classical statements
  (proved-with-stated-hypotheses) except where the arithmetic or a planar disk
  is computed exactly; the strict-versus-thickened distinction is kept, and no
  virtual-knot stabilisation equivalence is claimed.
* The ambient extension is certified constructively only for the declared
  rigid-translation class; for non-rigid motions no constructive certificate is
  produced (the classical isotopy extension theorem is cited, not reproved), and
  the check refuses with `EXP6-AMBIENT-EXTENSION-MISSING`.
* Physical ropes with radius, length, curvature or velocity limits are out of
  model; so are smooth embeddings, wild knots and arbitrary real input.

## 11 Outcome ledger (labels)

`proved`: interval self-embedding and obstacle-clearance certificates; torus
slope arithmetic and writhe effects on the declared diagram records.
`proved-with-stated-hypotheses`: torus classification, free-3-space unknot
comparison, Jordan–Schoenflies for the strict sphere, linking invariance under
disjoint isotopy, R-move completeness (all cited, not reproved).
`computationally-verified-example`: collision witnesses, keyframe blindness,
flat-disk certificates, linking values, encoding round trip, process
faithfulness on the declared domain, the not-certified demonstration.
`refuted`: state faithfulness for topological semantics (witness pair).
`bounded-domain-compatible`: gate-D answers, all of them restricted to the
declared budget.
`budget-exhausted`: the depth-2 planner run.
`unknown`: the depth-0 subdivision run (`not-certified`).
`structural-proposal`: a general knot-motion planner (not implemented).
`open`: completeness of any tier; planning failure implying non-existence;
linking-number completeness.

## 12 Open items and bounded requirements

* **R3 is not instantiated.** A faithful R3 needs a planar-tangle pattern whose
  exact implementation exceeds this round's budget, and the braid-relation route
  to it is explicitly out of scope for exp6. Consequence: the instantiated
  rewrite system is incomplete by declaration, and no diagram-equivalence
  completeness is claimed.
* **A general knot-motion planner is not implemented.** Escaping the declared
  submodel (more action primitives, continuous control, adaptive search) is an
  open engineering question; the depth-2 run shows the budget marker working.
* **Fixed-endpoint process homotopy is not decided.** The two witness-1
  histories differ literally and in cost; whether they are homotopic as paths in
  the embedding configuration space with fixed endpoints is left open.
* **The strict-sphere and strict-torus statements are cited, not modelled.** Only
  the planar disk certificate and the integer slope arithmetic are computed.
* **Stabilisation/virtual-knot equivalences** and any bridge to braid closure
  remain untouched (out of scope by the plan).
* **A physical-rope contract** (radius, curvature, velocity, tension limits) is a
  different contract and would need its own fixture and certificates.

## 13 Files, reproduction and verification status

Files created (all inside `research/process-representation-gap/`):

* `contracts/exp6-knot-deformation-environment.v1.json` — frozen first, sha256
  `1b8a6d0ddbce2efd708a3875e7c6f32bd05947ffb1b434e74e4d5c5f5cfa82ac`, entry added
  to the ledger by `tools/freeze_contracts.py` (merge-preserving; the ledger was
  never hand-edited).
* `experiments/exp6_knot_deformation_environment.py` (primary, 2779 lines) and
  `experiments/exp6_knot_deformation_environment_independent.py` (independent,
  1075 lines).
* `evidence/exp6-knot-deformation-environment.json` (57916 bytes, sha256
  `13b12a806236934505619bdc09acac9f08dfe79a3f4b2c1ef981fdc05685e210`),
  `evidence/exp6-knot-deformation-environment.raw.json` (23933 bytes, sha256
  `71c123ffa146a338fbcde437a33b7ad7c4cd9dd2a7ecfa453a0d879d2a0e9521`, the 36
  per-box certificates plus the per-move provenance table), and
  `evidence/exp6-knot-deformation-environment-independent.json` (sha256
  `631b4bbd0c5966ff672f2aab77e02c4c23ebf898c5b57c46aca518724a0a79c1`).

Reproduction:

```
python3 research/process-representation-gap/tools/freeze_contracts.py
python3 research/process-representation-gap/experiments/exp6_knot_deformation_environment.py \
  --out research/process-representation-gap/evidence/exp6-knot-deformation-environment.json \
  --raw research/process-representation-gap/evidence/exp6-knot-deformation-environment.raw.json
python3 -O research/process-representation-gap/experiments/exp6_knot_deformation_environment.py > /tmp/exp6-O.json
cmp /tmp/exp6-O.json research/process-representation-gap/evidence/exp6-knot-deformation-environment.json
python3 research/process-representation-gap/experiments/exp6_knot_deformation_environment_independent.py
```

Verified: both scripts produce byte-identical output under `python3` and
`python3 -O` (`cmp` reports equality), no `assert` statement exists in either
file, no float occurs in the evidence (`0` occurrences), the contract digest
matches the ledger, and the independent route reports zero disagreements.

## 14 Blockers

None. No source outside `research/process-representation-gap/` was modified, and
no pinned source was needed for this experiment: the two blockers that would
matter here (a missing pinned commit or an unavailable oracle) do not arise,
because exp6 is self-contained in exact rational geometry plus cited classical
statements.
