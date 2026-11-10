# AES notes: geometry, continuity and metric realization

**Status:** design and research notes, created 2026-11-07. These are not paper
claims, not governance records, and not a change to any mathematical-status
register. Notes 01–02 record the elliptic AES programme (positive curvature,
compactification, analysis). Notes 03–04, added 2026-11-10, record rational
neighborhood data, continuity in an explicit basic model, and the separate open
question of geometric metric realization. Note 05 records neighborhood mass,
Haar transport, conditional probability, information and their area connections.
Note 06 studies typed probability transport, the obstruction to stochastic
inverses, and the relation memory required for an observation to preserve closure.
Note 07 adds compact-set Scott transport, quantitative memory-error bounds,
and a certified audit of a fixed model's gate boundaries.
Note 08 compares channel-marked and value-only boundary limits, certifies
which jumps survive observation, and states the resulting gluing conditions.
Note 09 transports oriented boundary ports, tests shared memory under arithmetic
composition, and separates terminal observations from joint observation traces.

## Why a separate `aes/` folder

The notes under `analysis-and-calculus/` and `foundations-and-geometry/` develop
the existing AES theory, whose geometric core is the basic hyperbolic model of
Paper 0. The folder began with the **elliptic AES programme**: the choice of the
Cayley–Klein real-form family as skeleton, the audit of the same-named
trichotomies, and the arithmetic/expression-side questions that this choice
opens. It also holds the requested AES structural-data notes: local neighborhood
bases and relation transport, alongside metric-realization questions.

## Contents

- [01 – Trichotomy audit and the Cayley–Klein skeleton](01-trichotomy-audit-and-cayley-klein-skeleton.md)
- [02 – The arithmetic side of the elliptic AES](02-arithmetic-side-of-the-elliptic-aes.md)
- [03 – Quadrilateral neighborhoods and Scott continuity](03-quadrilateral-neighborhoods-and-scott-continuity.md)
- [04 – Structural data, metric unification and the catenoid example](04-structural-data-metric-unification-and-catenoid.md)
- [05 – Measure, probability, information and area](05-measure-probability-information-and-area.md)
- [06 – Typed probability transport and relation memory](06-typed-probability-transport-and-relation-memory.md)
- [07 – Memory error, gate boundaries and Scott transport](07-memory-error-gate-boundaries-and-scott-transport.md)
- [08 – Channel observation and boundary gluing](08-channel-observation-and-boundary-gluing.md)
- [09 – Boundary ports, composition and future observation](09-boundary-ports-composition-and-future-observation.md)

## Elliptic AES programme summary (notes 01–02)

Five different trichotomies in the repository share the names elliptic /
parabolic / hyperbolic. Within the paper series, only the projective trace
trichotomy of Paper 0 is a complete classification-level geometric theory, but
it classifies isometries of the split real form $\mathrm{PSL}_2(\mathbb R)$; it
does not produce a positive-curvature AES. The constant-curvature trichotomy of
Paper 0, §12.6, has a developed hyperbolic entry, a parabolic degeneration, and
an elliptic entry explicitly marked "not developed". The skeleton proposed here
is the Cayley–Klein family

$$
g_c=\frac{4\,|dz|^2}{(1+c|z|^2)^2},
\qquad
a_c=\frac{2\mu\operatorname{Im}z}{1+c|z|^2},
\qquad
K_{g_c}=c,
$$

with $c<0$ the basic hyperbolic model, $c=0$ the flat model, and $c>0$ a
spherical model. For $c>0$ the assignment is bounded, the two poles form a
critical (turning) locus, the arithmetic motions are partial, and the expression
side acquires a new "range domain".

## Continuity and metric realization (notes 03–04)

Note 03 gives proofs in a specified positive-affine basic model: rational
quadrilateral bases, transported reference values, closure relations, a marked
continuous family, and Scott-continuous box observations. Exact shared-parameter
relations remain distinct from their interval envelopes. This is not a complete
theory of arbitrary expression histories, singular tube gluing or binary
structural composition.

Note 04 preserves the metric-unification question and its catenoid example from
the linked discussion Page. The rational root brackets are certified; displayed
areas are numerical approximations. A general AES metric realization and a
geometric interpretation of structural mass remain open.

## Neighborhood mass, probability and information (note 05)

Note 05 separates structural mass, conditional probability, logarithmic
information, positive area and the signed ACS order defect. It fixes the
left/right Haar convention, proves the basic transport laws and a conditional
selection of the cross-layer motion, and includes a rational partition example
with certified logarithm bounds. A fixed-leaf construction connects these data
to continuous valuations on Scott opens. General metric realization and
probabilistic semantics for arbitrary histories remain open.

## Probability transport and relation memory (note 06)

Note 06 gives a finite rational transport contract and a quantitative continuity
bound. It proves the stochastic-inverse restriction, recalls strong lumpability
with a proof, and gives a finite algorithm for the coarsest compatible observation
refinement. Exact examples distinguish shared relation memory from independent
resampling, geometric closure from branch-mass closure, and Bayes reversal from
an inverse. A standard-library verification script replays the witnesses.
The interpretation of popularity / similarity, model interfaces and general
Scott-continuous history semantics remain open.

## Memory error and continuous probability transport (note 07)

Note 07 checks the interfaces of historical Sector-Prob analysis and two
dirac-belt variants. It proves a Scott-continuous compact uncertainty-set lift
for continuous finite-branch kernels, bounds approximate observation errors,
and quantifies the tension between contraction and an approximate inverse.
An exact rational certificate bounds adjacent-cell gate jumps in one frozen
32-channel PAL export. Channel jumps are distinguished from output-law
discontinuity or predictive failure; full history semantics remain open.

## Observation and boundary gluing (note 08)

Note 08 gives the output-collision criterion for a gate jump to disappear after
forgetting channel identity. A frozen PAL export has no complete cancellation
for its 56 adjacent gate pairs; one rational interface window has certified
positive W1 separation, with a matching primal/dual witness at its center.
Single-valued gluing fails there under both observations. Keeping two boundary
ports, or a compact relation retaining the two laws, gives explicit alternative
semantics; the latter has a Scott-continuous uncertainty-set transport.

## Boundary transport and composition (note 09)

Note 09 supplies rational port transport compatible with the basic A/M relations,
a closed-word counterexample to independent branch reselection, and finite
linear tests for future terminal and joint-trace equivalence. A pinned PAL audit
finds 32 distinct transported faces from one source face. A finite-horizon
common-refinement construction retains coherent trajectories; neither this
construction nor Scott continuity alone establishes arbitrary-history gluing.

## Relation to the papers

- Paper 0, §3.6, Proposition 3.13 (`prop:p0-projective-trichotomy`): trace
  classification and length of a projective motion.
- Paper 0, §12.6: the three constant-curvature models; the elliptic entry is
  explicitly "not developed".
- Paper 3, §4: $\Gamma_4=\langle J,T\rangle$, the order-2 and order-4 elliptic
  points, cone angles, and the cusp; the only worked elliptic configuration in
  the paper series.
- Paper 5, §3–§4: the quadratic scalar and signature trichotomies. §8 still
  says that Paper 0 does not develop the trace trichotomy; that statement is
  stale relative to Paper 0.
- Note 49: the finite-field conic trichotomy; it explicitly disclaims a curvature
  reading.
- `governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`:
  the $c$-family formulas and the real-form proposals. Discussion-level, not a
  paper claim.

## Elliptic programme open questions

1. Define a **compact/critical AES** that admits the $c>0$ model without forcing
   it into the regular/singular dichotomy of Papers 0 and I.
2. Re-derive the arithmetic frame and the contact bracket for $c>0$; the
   canonical frame $X_u a=\mu$, $X_v a=\lambda a$ has no real solution when
   $\lambda^2=-c<0$.
3. Define the **range domain** and compare it with the ordinary and projective
   domains of Papers I and the finite-field notes.
4. Develop the spherical analysis: $a_c$ is an $\ell=1$ spherical harmonic, the
   zero set is the equator, and the critical locus is the two poles.
5. Decide whether the elliptic AES is a real form of the complexified AES or a
   separate category with its own axioms.

## Provenance

Written 2026-11-07 from a three-part working discussion. Paths and line numbers
refer to the repository state at commit `f1fe625` (2026-11-07). No paper source
was modified.

The 2026-11-10 additions were directed by Mingli Yuan and formalized/drafted
with ChatGPT / Codex (OpenAI). Their per-note provenance, proofs, sources and
claim boundaries are recorded in notes 03–04. The source Page is preserved;
no manuscript or mathematical-status register was changed.

Note 05 records the separate measurement/probability thread of the same
2026-11-10 discussion. Its additional assumptions, derivations and user-reported
model motivation are distinguished in its provenance section.

Note 06 develops the subsequent popularity / similarity discussion into finite
theorems and rational witnesses. It retains the distinction between historical
model reports, standard probability results, and proposed AES interpretations.

Note 07, added 2026-11-11, records the subsequent source audit and quantitative
continuity work, with pinned provenance and a replayable gate certificate.

Note 08, added 2026-11-11, records the requested comparison of marked and
value-only limits, exact cancellation criteria, and a pinned boundary certificate.

Note 09, added 2026-11-11, continues with composition-compatible port data,
shared-parameter closure and explicit tests for future observable differences.
