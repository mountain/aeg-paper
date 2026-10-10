# Experiment 5 — braids as non-arithmetic processes

Work-plan section 6, 实验五. Contract `contracts/exp5-braid-nonarithmetic.v1.json`,
sha256 `3cb4feaa8ed326ce80b73ca1945f122a645d6031dd1df5d00db162c081da58f6`.

Evidence: `evidence/exp5-braid-nonarithmetic.json`,
`evidence/exp5-braid-words.raw.json` (5461 rows),
`evidence/exp5-braid-nonarithmetic-independent.json`.

## 1. Question

Do the native compositions of braid crossings constitute a computational
process, and under exactly which task and equivalence does a notion of
"computational power" hold? The work plan requires at least four layers to be
kept apart, and requires the conventions to be declared and *verified* rather
than assumed.

## 2. Declared conventions, verified before any counting

* Letters are read **left to right in time**.
* Automorphisms compose by `(f ∘ g)(x) = f(g(x))`, and
  `Φ(ε) = id`, `Φ(w · σ) = Φ(w) ∘ φ_σ`; hence
  `Φ(w) = φ_{w₁} ∘ … ∘ φ_{wₙ}`.
* `σ_i` sends `x_i ↦ x_i x_{i+1} x_i⁻¹` and `x_{i+1} ↦ x_i`.
* `σ_i⁻¹` sends `x_i ↦ x_{i+1}` and `x_{i+1} ↦ x_{i+1}⁻¹ x_i x_{i+1}`.

Verified as obligations inside the run, not assumed:

* `φ_σ ∘ φ_{σ⁻¹} = id` and `φ_{σ⁻¹} ∘ φ_σ = id` for `σ = σ₁, σ₂`;
* `Φ(σ₁σ₂σ₁) = Φ(σ₂σ₁σ₂)`;
* every declared generator image is freely reduced.

The order convention is not cosmetic. It is where an independent route caught a
real defect (section 7).

## 3. The four layers on the declared domain

All crossing words over `{s₁, s₂, S₁, S₂}` of length at most 6, including the
empty word: `1 + 4 + 16 + 64 + 256 + 1024 + 4096 = 5461`.

| layer | object | classes | merges from the layer above |
|---|---|---|---|
| L4 | literal crossing word | **5461** | — |
| L3 | freely reduced word | **1457** | 4004 by free cancellation |
| L2 | braid group element (Artin automorphism) | **577** | 880 by Artin relations |
| L1 | endpoint permutation in `S₃` | **6** | 571 by forgetting the action |
| — | writhe and generator counts | 210 | (a different, incomparable summary) |

So of 5461 literal histories, free cancellation removes 73%, the braid quotient
removes a further 60% of what remains, and the endpoint permutation keeps only
6 classes. Each step is a genuine information loss, and the experiment records
which.

**Faithfulness statement.** Artin's representation `B_n → Aut(F_n)` is
faithful, so L2 determines the braid group element exactly. That theorem is
**used**, not reproved; the finite computation is consistent with it and is
reported as such. Faithfulness holds at the braid-element layer only: L2 does
not determine the literal history, and L1 determines strictly less than L2.

## 4. The three mandatory witnesses

### W1 — `ε` versus `σ₁²`

| | |
|---|---|
| endpoint permutation | both the identity `[0,1,2]` |
| Artin images | `[x, y, z]` versus `[xyxy⁻¹x⁻¹, xyx⁻¹, z]` |
| same braid element | **no** |
| separated at L2 | **yes** |

The coarsest layer cannot see torsion that the group layer sees.

### W2 — `σ₁σ₂σ₁` versus `σ₂σ₁σ₂`

| | |
|---|---|
| literal words | different |
| generator counts `(s₁−S₁, s₂−S₂, s₁, s₂, S₁, S₂)` | `(2,1,2,1,0,0)` vs `(1,2,1,2,0,0)` |
| Artin images | identical: `[xyzy⁻¹x⁻¹, xyx⁻¹, x]` |
| endpoint permutation | both `[1,2,0]` |

The braid quotient merges two distinct literal histories with different
generator counts. Per the work plan this is **not** a group-semantic
counterexample when Artin rewriting is allowed; it shows exactly what the
quotient forgets. A task that observes construction cost or literal
construction history is not served by the group quotient.

### W3 — the frozen probe family

Pre-registered probes:
`x₁`, `x₂`, `x₃`, `x₁x₂`, `x₁x₂x₃`, `x₁x₂x₁⁻¹`, the commutator
`x₁x₂x₃x₁⁻¹x₂⁻¹x₃⁻¹`, and `(x₁x₂)³`.

Observing the image of **one** free-group word is in general not the action:

| probe | distinct signatures (of 577 classes) | collision pairs | largest collision |
|---|---|---|---|
| `x₁` | 213 | 364 | 13 |
| `x₂` | 315 | 262 | 11 |
| `x₃` | 213 | 364 | 13 |
| `x₁x₂` | 213 | 364 | 13 |
| `x₁x₂x₃` | **1** | **576** | **577** |
| `x₁x₂x₁⁻¹` | 315 | 262 | 11 |
| `(x₁x₂)³` | 213 | 364 | 13 |
| commutator | **577** | **0** | 1 |

`x₁x₂x₃` is the sharpest negative: the image of the product of all three
generators is **constant** across all 577 classes, so that probe observes
nothing at all. The commutator, by contrast, separates all 577 classes on this
domain; the exhaustively-determined minimal separating subfamily has size 1.

**Scope.** The commutator's separating power is a statement about the declared
domain (length ≤ 6, 577 classes) only. It is not a claim that one free-group
word determines an automorphism in general, and it is not a claim that any
particular probe is canonical.

## 5. Independent verification

Two independent routes sharing no semantic helper with the primary (only
deterministic JSON serialisation is common):

1. **Free-group substitution against composite image tuples** — the work plan's
   own named independence pattern. The primary materialises each automorphism
   as an image triple and substitutes into it; the checker applies one
   generator action at a time directly to the probe word, in the reverse letter
   order the declared convention forces, and never forms a composite.
   Agreement: 5461 words × 8 probes = 43 688 evaluations, **0 disagreements**.
2. **Cayley-graph breadth-first enumeration** of the automorphism group, in
   place of word enumeration plus de-duplication. It independently reproduces
   L2 = **577**. L3 = 1457 and L1 = 6 were likewise re-derived independently and
   agree.
3. Both defining relations were re-verified by **direct substitution on a
   10-element generating set of free words**, rather than by composing triples.

A defect this second route found *in itself* is retained as a negative control:
composing the automorphism in the wrong order silently computes the reversed
composite, and the two routes then disagree on the first word of length two
(`s₁s₂` on probe `x₁`: `xyx⁻¹` versus `xyzy⁻¹x⁻¹`). That is a concrete
demonstration that the independence requirement does real work rather than
decorative work.

Determinism: primary and independent both emit byte-identical output across
repeated runs and across `python3` / `python3 -O`.

## 6. Cost, per layer, over the 5461-word domain

| layer | total storage bytes | structural size | computation steps |
|---|---|---|---|
| L4 literal word | 369 549 | 67 357 | 5461 |
| L3 reduced word | 251 181 | 43 789 | 5461 |
| L2 Artin automorphism | 320 614 | 32 766 | 5461 |
| L1 endpoint permutation | 98 298 | 32 766 | 5461 |

The Artin automorphism triple costs **less** per word than the literal word
(320 614 vs 369 549 bytes) while determining the braid group element exactly.
That is a genuine compression at the braid-element layer — and it is exactly
the layer at which the literal construction history is lost (W2). The cost
table and the information-loss table are two views of the same trade.

## 7. Negative controls

| id | expected diagnostic | observed |
|---|---|---|
| `braid-relation-fails` | `EXP5-BRAID-RELATION` | `EXP5-BRAID-RELATION` |
| `inverse-relation-fails` | `EXP5-INVERSE-RELATION` | `EXP5-INVERSE-RELATION` |
| `sign-flip` | `EXP5-WITNESS-SIGN` | `EXP5-WITNESS-SIGN` |
| `single-crossing-mutation` | `EXP5-WITNESS-SIGN` | `EXP5-WITNESS-SIGN` |
| `free-reduction-wrong` | `EXP5-REDUCTION-NOT-ADJACENT` | `EXP5-REDUCTION-NOT-ADJACENT` |
| `route-disagreement` | `EXP5-ROUTE-DISAGREEMENT` | `EXP5-ROUTE-DISAGREEMENT` |
| `layer-conflation` | `EXP5-LAYER-CONFLATION` | `EXP5-LAYER-CONFLATION` |
| `enumeration-count` | `EXP5-ENUMERATION-MISMATCH` | `EXP5-ENUMERATION-MISMATCH` |
| `reversed-composition-route` (independent) | `EXP5-ROUTE-DISAGREEMENT` | `EXP5-ROUTE-DISAGREEMENT` |
| `single-generator-image-mutation` (independent) | `EXP5-ROUTE-DISAGREEMENT` | `EXP5-ROUTE-DISAGREEMENT` |

## 8. Objectification candidates, and where they stand

The work plan asks for objectification candidates under the three gates of
section 4.4. Two are visible here, and neither is promoted:

* **The braid element as an object.** Task sufficiency: sufficient for
  braid-level tasks, **insufficient** for construction-history tasks (W2).
  Stable composable interface: concatenation and inverse exist and the Artin
  action is a homomorphism. Descent consistency: exact, by construction, at the
  automorphism layer.
* **The Artin automorphism as an object.** Same interface and descent status;
  it is literally the same object as the braid element by Artin faithfulness,
  so it is **not** a higher rank — it is a different presentation of the same
  layer. Counting it as an elevation would be exactly the naming fallacy the
  work plan forbids.

No new rank is claimed. Experiment 4 performs the explicit gate-by-gate test.

## 9. What is explicitly NOT claimed

* No linear representation: no Burau matrices, no Alexander or Jones
  invariants, no spectral observation. The work plan requires these under a
  **separate** contract and forbids letting a matrix replace the braid process.
* No topological quantum computation. The plan requires an anyon model, an
  encoding space, a measurement model, an approximation accuracy and an error
  model before any universality claim; none is supplied.
* No bridge to knots: braid closure, Markov equivalence and braid-element
  equality are never identified with knot equality.
* No claim for lengths beyond 6, and no claim that the Artin automorphism is a
  decision procedure for infinite braid words (for a finite word it is a finite
  object, but nothing beyond that is asserted here).
* No arithmetic encoding at any layer. The Artin action is a nonlinear symbolic
  transformation of free-group words, which is precisely the contrast the plan
  asks for against a linearized observation.

## 10. Open items carried forward

* Whether a *small* probe family, or a canonical one, determines the action on
  domains beyond length 6 is open. The commutator's success here is a
  finite-domain finding.
* The cost of the probe observation was not yet separated from the cost of
  materialising the automorphism; only the four layer costs above are measured.

## 11. Declared reference used

[Representing braids by automorphisms](https://arxiv.org/abs/math/0203167) is
the cited entry for the Artin representation; the theorem is used with its
stated hypothesis and is not reproved here.
