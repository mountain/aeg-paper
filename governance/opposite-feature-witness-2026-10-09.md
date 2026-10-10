# Minimal opposite-process feature snapshot experiment

Date: 2026-10-09. Author direction: Mingli Yuan; implementation and analysis
prepared with Codex. Baseline: aeg-paper `dd7b93e5eda57343e1ff05ed954883db310eda1d`.
Status: independent finite experiment and mathematical boundary record.
No existing frozen evidence or manuscript theorem is changed.

## Sources and authority

Pinned source repository: `mountain/adva`, commit
`cce73004c2b4fbfb87d9ba1ccc66820423273cf6`.
Source paths: `docs/research/0114-three-sided-trace-arithmetic-calibration.md`
and `programs/bootstrap-0/first-trace-arithmetic.adva`.
The latter's fetched UTF-8 bytes are copied into
`paper-4/scripts/fixtures/opposite-features/adva-0114.json`.
SHA-256: `637c2d05663fcee780156d93f4f9e19f829418213a4948c91113141b64d3a579`.
Git blob: `de247cd071f714e14a91b0e54a9bab77b0de43e9`.
The source's BLAKE3 document/witness/trace references are retained as opaque
coordinates; this checker does not recalculate those upstream digest protocols
or rerun the Rust producer. SHA-256 checks transport bytes, not external truth.
No current Adva main claim is inferred from this pinned record.

The governing Paper IV conditions are PIV-S1/S2/S3/S5/S6 and
`paper-4/sections/05b-ported-aes-programs.tex`. This is a snapshot adapter
attached to that finite interface, not an implementation of Adva mechanisms
or a construction of faithful AES gate motions.

## Interface: observable, formal, spectral

| Kind | Candidate | Meaning and limit |
|---|---|---|
| Direct recorded observation | Ordered events with frame IDs, mechanisms, labelled inputs/outputs and routed handoffs | Recomputed against frozen projection records; events are records, not independently witnessed execution |
| Direct projection | T=(frames,handoffs,transferred ports), S=(labelled start,end), C=(compute,verify,learn,length,alternations) | Policy fixes coordinate order and literal carrier labels; carrier IDs are not numerical assignment values |
| Source package | Repository, full commit, path, byte hash, source digests, side, trace reference | Preserved beside values; no global identity or external authentication claim |
| Formal candidate | Commutative monomial compute^c verify^v and ratio exponent (-1,+1) | Not a spectrum; right/left=verify/compute symbolically, not identically 1 |
| Spectral candidate | None instantiated | Needs a specified endomorphism, closed input/output object, operator domain, marking and residual; no such operator is supplied |

Snapshot policy `snapshot-v1` retains literal events, carrier labels, full
source package and left-minus-right residuals. The trust policy is pinned
repository evidence, with no external truth authentication. The source truth
fiber and semantic filler remain open. Discarding the source package would
change the observation policy and is not licensed by numerical equality.

## Exact finite calculation

Host extraction independently checks event-word agreement, unique frames,
boundary carriers, ordered handoff coverage, route and carrier continuity.
It derives T, S, C and checks them against the persisted projections and
residuals. It does not execute `compute`, `verify` or `learn`.

For each side, four distinct Q-valued producer programs expose
(c,v,f,h)=(compute count,verify count,frame count,handoff count).
These are typed *scalar adapters* from a source package, not casts of the
whole event record. Their immutable source fields identify the pinned side
and adapter field; the output envelope retains the complete packet.
The scalar producers are constant snapshot programs. Their extraction is a
separate host computation, not an arithmetic realization of the event trace.

The finite body has explicit copy gates for f and h and reads:

    y1 = c + v
    y2 = f - h
    y3 = (3*h)/f

The coefficient 3 is a separately declared route-arity constant. The extractor
checks the three routed ports per handoff. Left inputs are (2,1,3,2), right
inputs (1,2,3,2). Both outputs are exactly (3,1,2).
The four holes and three scalar outputs may use the already declared four-end
carrier/anchoring interface of Paper IV; input arity is independent of end
count. No new collar or motion claim is required or checked here.

All producer outputs are bound once, types match Q, copy is explicit, all
sources and producer occurrences survive the graft receipt, and the assembled
event graph is acyclic. The body's exact domain is f != 0; its producers are
total. Substituted and separately evaluated outputs agree, as do two different
legal schedules. Every gate is executed strictly. The output observation is
explicitly either the scalar triple or the triple **with** its source/event
packet. These are distinct observations. Three scalar outputs are not Adva's
native history/result/evidence roles.

## Negative controls and feature sufficiency

1. The two frozen paths yield equal triples but different ordered mechanism
   words, events, frame occurrences and trace references. The packet-aware
   observation distinguishes them by actual words, independently of hashes.
2. Synthetic words `compute verify compute verify` and
   `verify compute verify compute` share incidence, length and alternations
   (2,2,4,3), but differ in order. These are newly constructed controls,
   not extra frozen process executions.
3. A CarrierID-typed producer cannot feed a Q arithmetic gate.
4. f=0 causes strict division failure; it is not projectively continued.
5. Changing an event mechanism without changing the source word/projection is
   rejected. The fixture byte hash separately rejects altered transport bytes.

For the two-record snapshot domain and identity continuation only, the scalar
triple is sufficient for the scalar observation. It is insufficient for the
history-aware observation: its fiber contains both histories, whose observed
words differ. This directly exhibits the kernel obstruction in PIV-S5.
The rich packet is injective on these two records and hence sufficient for
this snapshot observation. No continuation action or update implementation is
supplied; PIV-S6 and three-side feedback remain untested. Keeping all history
makes snapshot separation easy, not a compressed cross-side reconstruction.

## Cross-side conclusions

**Finite projection obstruction (proved with stated hypotheses).** Let D
contain these two recorded paths and let T,S,C have exactly the coordinate
policy above. No function chi_C on (T,S)(D) satisfies
C(d)=chi_C(T(d),S(d)) for every d in D.

Proof: both records have T=(3,2,6) and
S=(0,1,2,15,16,17), while C is respectively (2,1,0,3,2) and
(1,2,0,3,2). A function at the same input cannot return two different
outputs. The residual (+1,-1,0,0,0) is exact. This excludes this *projection*
definition of chi_C, not every enriched time/space feature or future theory.
Adding literal history to T or S changes the problem and does not prove the
original equation.

For T=chi_T(S,C) and S=chi_S(C,T), the input pairs differ between the two
records. A two-row lookup is possible but provides no independently derived
cross-side witness, unseen-instance generalization or reconstruction law.
Neither relation is promoted. Required next conditions: define admissible
process domain and feature codomains, proposed extraction laws, a frozen
unseen-instance test, and source/observation preservation. For chi_C, enrich
(T,S) with independently justified information or restrict the domain so the
collision disappears. Any restriction must exclude or explicitly quotient
one of these records, with an observation-descent argument.

The formal ratio verify/compute is not identically one; specialising both
weights to equal nonzero numbers can hide it. A holonomy/target-algebra
witness is still required for descent through M6. No spectrum, common truth
coordinate, fixed point, or AES/Adva equivalence follows.

## Reproduction and review decision

    python3 paper-4/scripts/verify-opposite-features.py > /tmp/opposite.json
    cmp /tmp/opposite.json paper-4/scripts/fixtures/opposite-features/evidence.json
    python3 -O paper-4/scripts/verify-opposite-features.py > /tmp/opposite-O.json
    cmp /tmp/opposite.json /tmp/opposite-O.json
    python3 paper-4/scripts/verify-ported-aes.py > /tmp/ported.json
    cmp /tmp/ported.json paper-4/scripts/fixtures/ported-aes/integration-evidence.json
    python3 paper-4/scripts/verify-paper4.py

All commands passed locally; the existing Paper IV suite passed all seven
verification groups. CI adds normal/optimized replay and exact evidence
comparison. No LaTeX source changes: no PDF build is required by the
source-edit rule, and no new PDF is claimed produced locally. Existing full
paper build remains in CI. No theorem, label, notation or material is moved;
no old claim is strengthened. Frozen upstream and integration evidence remain
unchanged. No warning was emitted by the finite checks.

A narrow successor PR is warranted by a replayable external-source adapter
and a precise finite impossibility certificate. The status register records
both without closing PIV-F2. The next useful task is an independently defined
cross-side feature law on a broader declared process domain, with histories
retained as negative controls; manuscript promotion can follow that review.
