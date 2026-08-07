# Paper IV Decision Record

**Paper:** *Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity*  
**Subtitle:** *From Histories and Quotients to Representation and Cost*  
**Decision date:** 2026-08-07  
**Repository baseline:** `264b7edeade754b706b575929fbbe3c8df72b5c3`  
**Status:** integrated manuscript decisions

This record fixes the conventions and claim boundary of the Paper IV
mathematical-review manuscript. It is subordinate to the repository's existing
restructuring authority and should be read with `paper-IV-source-audit.md` and
`paper-IV-closure-report.md`.

## D4-01 — Paper IV has four layers, not one complexity quantity

The manuscript keeps projective quotient fibers, contextual residuals,
operational live configurations, and rewrite fibers distinct. Comparisons among
layers are stated only after the relevant action, observation, encoding, or
machine model has been supplied.

## D4-02 — Histories, operators, quotients, and endpoints remain distinct

The canonical tower is

```text
Hist_K -> PGL_2(K) -> G/H -> G/B_± -> observation.
```

The first fiber is a word-relation fiber. The `G -> G/H` fiber is an
`H`-torsor of projective frames. They are not both called the same kind of
history residue.

## D4-03 — A regular bivaluation is an ordered image--kernel pair

A regular bivaluation is an ordered pair of distinct points of `P^1(K)`,
equivalently a rank-one idempotent on `K^2`. Interchanging the two points
replaces the projector by its complement. The transverse divisor is part of the
definition.

## D4-04 — Algebraic and dynamical condensation are separated

Passage to `G/H` or a rank-one idempotent is algebraic condensation. Convergence
of normalized matrix products requires topology or valuation, lifts, and a
normalization. Finite-field idempotents are not described as attracting limits.

## D4-05 — Chronological futures act on the left

Under the Paper I chronology convention, appending a future context gives left
multiplication of the accumulated operator. This is not operand-slot chirality.

## D4-06 — Single right descent and reversible right action have different tests

A single right update by `k` descends to `G/H` exactly when
`k^{-1} H k` is contained in `H`. A reversible right action requires equality,
so its group lies in the normalizer. The manuscript does not collapse the
inclusion statement into the normalizer statement for infinite groups.

## D4-07 — Projective residue becomes semantic only through futures

The cardinality of `H` is not by itself computational information. It coincides
with a continuation residual only for an experiment whose future action and
observation make the quotient sufficient.

## D4-08 — Partial arithmetic is totalized by an absorbing outcome

Illegal ordinary arithmetic, type errors, or forbidden continuations map to a
distinguished absorbing state `bottom`. This prevents vacuous equivalence based
only on common legal futures.

## D4-09 — An online state representation must be equivariant

An exact machine state must update from the current encoded state under every
legal continuation and reproduce the current observation. A representation is
not called an online state when a hidden procedure uses the entire past to
recompute transitions.

## D4-10 — The residual quotient is the minimal exact deterministic state

The contextual residual is the canonical reachable exact machine. Every other
exact deterministic online realization maps surjectively and equivariantly onto
it.

## D4-11 — The bit bound has an explicit encoding convention

The lower bound `ceil(log_2 |R_C|)` applies to a fixed-width state register or
to a prefix-free code of bounded maximum length. Arbitrary unframed
variable-length strings are not counted as self-delimiting states.

## D4-12 — Summed residual bounds are capacity--time

The sum over cuts is called a fixed-register capacity--time bound. It is an
actual memory--time lower bound only when the operational model charges the
complete register as live at every snapshot.

## D4-13 — Live configurations, not completed sets, define workspace

A monotone set of nodes ever computed cannot determine space when values may be
erased or recomputed. A frontier formula is retained only for the restricted
no-recomputation, retain-until-last-use policy.

## D4-14 — Resource geometry is vector-valued and model-relative

Static description, work, elapsed steps, causal depth, peak workspace,
memory--time, and communication are separate coordinates. They are not added
without compatible units and a declared objective.

## D4-15 — Complexity is attached to uniform families

The Pareto resource set is defined at fixed input size inside a uniform family
of realizations. Hard-coded finite maps and unlimited preprocessing do not
support asymptotic claims.

## D4-16 — Word growth and fiber growth are not runtime

The fiber--image and entropy inequalities are promoted as exact counting
results. No implication from noncommutativity, hyperbolicity, or exponential
group growth to computational hardness is claimed.

## D4-17 — Exact rewrite labels fail the holonomy test

Endpoint potential differences and pure-gauge group labels telescope around
closed loops. Nontrivial projective rewrite holonomy requires a genuinely
non-exact transport, gauge law, and coherence structure.

## D4-18 — Horner injectivity is characteristic-zero

The multinomial fixed-histogram count is stated over the integers or a
characteristic-zero field containing the relevant digits. Finite-characteristic
collisions are not suppressed.

## D4-19 — OBDD width is representation- and order-specific

The equality separation is a theorem for deterministic OBDDs with a fixed
variable order. It is not advertised as a lower bound for all equality
algorithms. The example is used specifically to show exponential order effects
with commuting restrictions.

## D4-20 — Butterfly quotients do not replace linear network semantics

The local identity `B_omega = B_1 D_omega` is a right-torus-coset statement.
Exact inverse transforms retain central scalars, and a full FFT/NTT is a
multi-wire `GL` network rather than a one-wire `PGL_2` history.

## D4-21 — Static twiddles and dynamic wire states are separate

Twiddle factors belong to the program description or a generation procedure.
Wire values vary with input and belong to live state. Storage of one is not
called entropy of the other.

## D4-22 — Matrix intermediate size is not peak memory

The matrix-chain calibration records scalar work and the principal intermediate
matrix. Peak memory additionally depends on allocation, retention, overwrite,
blocking, and temporary-buffer conventions.

## D4-23 — Checkpointing is a live-trace example, not a universal AEG theorem

The two endpoint schedules are proved in a unit-cost chain model. General
reversible-computation and checkpointing results are cited as external
calibrations; their optimal tradeoffs are not transferred automatically to every
AEG condensation.

## D4-24 — The remaining programme stays open

Non-flat projective transport, multi-wire AEG, costed AEG-native representation
changes, approximate residuals, history-natural cost functors, and robust
simulation across machine models are open problems, not completed consequences
of the present paper.
