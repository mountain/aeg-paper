# Arithmetic histories, automorphic zero networks, and singular tubes

**Status:** Active research synthesis; subordinate to the authoritative scope and
mathematical-status register

**Date:** 2026-08-06

**Affected papers:** I, II, and III

## 1. Purpose

This note records the new cross-paper research interface

```text
arithmetic history
    -> projective Hecke operator
    -> triangle-group automorphic function
    -> branched singular AES zero network
    -> relative zero divisor and monodromy.
```

The purpose is not to identify all of these levels.  It is to state precisely which
arrows are proved, which use standard external uniformization results, and which
remain proposals.

The central correction is that a rich unlabelled zero set is not yet arithmetic
data.  Arithmetic content requires a field or ring of definition, a declared
history-to-operator quotient, and a functorial construction of the zero object.

## 2. Why singularities are necessary

For a regular AES with `mu != 0`,

```text
|grad a|^2 = mu^2 + lambda^2 a^2
```

implies `da != 0` at every zero.  Hence a real zero set on a surface is locally one
smooth curve.  It cannot have a four-valent vertex.  On a connected complete
boundaryless regular AES, rectification by

```text
r(a) = integral_0^a (mu^2 + lambda^2 s^2)^(-1/2) ds
```

gives `|grad r| = 1`; the complete gradient flow yields a global product with one
connected zero level.  Thus a periodic order-four zero network necessarily uses
singular points, a boundary, incompleteness, or an auxiliary higher-rank field.

This explains why the historical signed-distance approach to an apeirogonal tiling
encountered a structural obstruction.  Wavefronts from different sides meet at cut
loci, and four-valent zero vertices cannot remain regular AES points.

## 3. Paper I: the exact arithmetic subgroup

Paper I's projective semantics contains the elementary operators

```text
T_s(z) = z + s,
J(z)   = -1/z.
```

Over `K = Q(sqrt(2))`, put `T = T_sqrt(2)` and `S = J`.  Their projective matrices
generate the Hecke triangle group

```text
G_4 = <S,T>,             S^2 = 1,
R = S T^{-1},            R^4 = 1.
```

Equivalently, after a generator convention, one may use `(ST)^4 = 1`.  This is an
exact operator-level bridge from a restricted bilateral arithmetic sublanguage to
the signature `(2,4,infinity)` group.

The following levels remain distinct:

1. literal arithmetic context words;
2. marked histories;
3. their projective operators under `rho`;
4. elements of `G_4` after the Hecke relations;
5. cosets of stabilizers representing chambers, edges, and vertices;
6. ordinary arithmetic endpoints, when all intermediate operations are admissible.

In particular, histories are not in bijection with tiles.  Nor does projective
continuation make an ordinary division-by-zero step admissible.

## 4. Paper II: regular holomorphic pullback

Two target models provide the analytic interface.

### 4.1 Planar target

For a phase `phi`, define on `C`

```text
A_phi(w) = Im(exp(-i phi) w),
h_phi    = |dw|^2 / (mu^2 + lambda^2 A_phi(w)^2).
```

Then

```text
|grad A_phi|^2_h = mu^2 + lambda^2 A_phi^2,
Delta_h A_phi    = 0,
K_h              = lambda^2 (mu^2 - lambda^2 A_phi^2)
                   / (mu^2 + lambda^2 A_phi^2).
```

If `F` is holomorphic and `F' != 0`, then `(F^*h_phi, A_phi o F)` is a regular AES.
This is a functorial local-isometry pullback, not arbitrary conformal realization.

### 4.2 Cylindrical target

On `C*`, put

```text
s(W) = log |W|,
g_cyl = |dW/W|^2,
a_cyl = (mu/lambda) sinh(lambda s)
```

with the limiting definition `a_cyl = mu s` for `lambda = 0`.  Then

```text
|grad a_cyl|^2 = mu^2 + lambda^2 a_cyl^2,
Delta a_cyl    = lambda^2 a_cyl.
```

Holomorphic local diffeomorphisms into `C*` again pull this AES back.  Paper II
owns these regular-locus analytic statements.  Critical points and singular metric
completion belong to Paper III.

## 5. Paper III: branched pullback theorem

Let `F` be holomorphic near `p`, with local degree `m >= 2`, and suppose the target
zero line passes through `F(p)`.  In suitable source and target coordinates,

```text
F(z) - F(p) = z^m,
a(z) = Im(z^m).
```

The zero germ has `2m` prongs.  The pullback metric has asymptotic form

```text
g ~ C m^2 |z|^(2m-2) |dz|^2,
```

and its metric completion adds a cone point of total angle `2 pi m`.  Since
`da(p) = 0` while the AES eikonal right-hand side is positive, the critical point
is locally essential in the Paper I singular-AES category.

The case `m = 2` gives a four-valent zero vertex and a `4 pi` cone.  This is the
correct local replacement for a regular order-four crossing.

## 6. The exact `q = 4` automorphic candidate

Let

```text
beta : H -> P^1
```

be a normalized Hauptmodul for the `(2,4,infinity)` Hecke triangle group, with
orbifold branch values `0,1,infinity` of indices `2,4,infinity`.  On the simply
connected upper half-plane the divisor of `beta/(1-beta)` is even, so choose a
meromorphic square root

```text
F^2 = beta/(1-beta).
```

Set

```text
W = (F-i)/(F+i),
s = log |W|,
a_T = (mu/lambda) sinh(lambda s),
g_T = |dW/W|^2,
```

again with the linear limiting definition at `lambda = 0`.  On the complement of
`Crit(W)`, this is the holomorphic pullback of the cylindrical AES and hence is
regular.  Moreover,

```text
a_T = 0
  <=> |W| = 1
  <=> F is real projective
  <=> beta belongs to [0,1].
```

Consequently

```text
Z(a_T) = beta^(-1)([0,1]).
```

This preimage is the triangle-group dessin.  Points over `0` have degree two and
are ordinary edge midpoints after the square-root step.  Points over `1` become
local degree-two points of `W`; they are four-valent zero vertices with `4 pi`
cone completion.  Suppressing the degree-two midpoints gives the
`{infinity,4}` apeirogonal skeleton.

Because `beta` is group invariant, a deck transformation can send `F` to `F` or
`-F`.  Accordingly it sends `W` to `W` or `W^(-1)`, and sends `a_T` to `a_T` or
`-a_T`.  The metric and zero graph descend to the full quotient.  The assignment
itself descends either to the kernel of the sign character or as a section of the
associated real line bundle.

The theorem does not assert smooth completeness across cone points.  Those points
are declared singular.  It does prove the model-specific metric audit: upstairs
order-four points complete to (4 pi) cones, the full coarse quotient has angle
(pi) at each elliptic image, and its completed length space has an infinite-distance
cusp.  Universal-cover and finite-index properness, and every proper-tube conclusion,
remain separate questions.

## 7. Arithmetic paths and relative zero divisors

A local moving root is not by itself an irreducible divisor.  The stable object is a
relative zero divisor over a parameter base.

Let `R` be an integral domain, `K = Frac(R)`, and let a history-labelled family
produce

```text
P_H(z,t) in R[B][z].
```

On an appropriate integral model `X -> B`, define

```text
D_H = (P_H)_0 = sum_i m_i C_i.
```

The `C_i` are prime relative divisors.  Their normalizations map finitely to the
base away from the discriminant and vertical bad fibers.

The levels of irreducibility must remain separate:

* irreducibility over `K(B)` is arithmetic generic irreducibility;
* irreducibility over `Kbar(B)` is geometric irreducibility;
* geometric irreducibility gives a connected complex cover and transitive
  geometric monodromy;
* the absolute Galois group permutes geometric components and sheets;
* discriminant primes, inertia, reduction modulo primes, and Frobenius cycle types
  supply arithmetic data not visible in an arbitrary complex zero graph.

This is the precise sense in which inequivalent arithmetic routes to zero can
become topological sheets.  A factorization of a chosen complex polynomial with no
declared field of definition contains no such number-theoretic information.

## 8. The missing naturality theorem

The general arrow

```text
marked arithmetic history H
    -> arithmetic section or polynomial P_H
    -> relative divisor D_H
```

is not yet constructed.  A valid history functor must at least:

1. state which history equivalence it respects;
2. distinguish operator equality from endpoint equality;
3. preserve the field or ring of definition;
4. specify its behavior under composition and operand-slot chirality;
5. make coordinate, phase, lift, and probe changes explicit;
6. intertwine parameter concatenation with cover or braid composition;
7. provide the hypotheses under which its divisor is finite and proper over the
   parameter base.

The `q = 4` construction supplies a special operator-level realization:

```text
restricted histories -> G_4 -> beta -> singular zero dessin.
```

It does not yet supply a functor on all marked AEG histories.

A finite supplied-register test is now proved.  Starting with `u^2=t`, every
projective operator forces an equivariant binary quadratic endpoint divisor.  The
terminal divisor factors through the operator, while a time-tagged prefix trace and
ordinary pole cocycle distinguish the neutral word `omega_4` from the empty
history.  The second tower `v^2=3`, `u^2=t+v` supplies an arithmetically prime
quartic with two constant-geometric components and explicit monodromy and
Frobenius.  This implements composition and information-loss tests in a restricted
typed-register category; it does not provide the missing canonical register source
or descent under a general history equivalence.

## 9. A number-theoretic boundary

The ring of integers `Z[sqrt(2)]` has unique factorization.  Thus the `q = 4` model
provides arithmetic symmetry, continued-fraction structure, and automorphic
uniformization, but it does not by itself model inequivalent factorizations of one
element into irreducibles.

If “irreducible routes to zero” is intended in the factorization-theoretic sense, a
second family should use a number ring or order with nontrivial ideal class group.
Its correct labels are ideal classes, prime divisors, sets of lengths, or related
factorization invariants, not merely different syntactic words.

## 10. Claim ledger

| Claim | Status | Owner |
|---|---|---|
| `T_sqrt(2)` and `J` generate the projective `q=4` Hecke subgroup | proved by matrix calculation plus standard group identification | Paper I |
| planar and cylindrical AES formulas | proved by direct calculation | Paper II |
| local-biholomorphic pullback preserves the AES equation | proved | Paper II |
| a local degree-`m` branch gives `2m` prongs and cone angle `2 pi m` | proved by local normal form and metric calculation | Paper III |
| normalized `(2,4,infinity)` Hauptmodul exists with stated ramification | standard triangle-group uniformization; cited | Paper III input |
| the displayed `beta,F,W` model has the dessin as its zero set | proved conditional on the normalized Hauptmodul input | Paper III |
| the sign cover has coarse completion `C*` and hyperbolic unit tangent complement `S^3 minus T(2,4)` | proved from stabilizers, cusp filling, and slopes | Paper III |
| primitive hyperbolic operator histories map onto Hecke periodic-orbit knots | proved at the operator-conjugacy quotient | Paper III |
| the zero dessin is the coding spine of the cited geodesic template | proved/cited with the graph/template distinction | Paper III |
| the quadratic and quartic supplied-register divisor tests | proved, including collapse kernels and Frobenius | Paper III |
| the full history-to-relative-divisor functor exists | partially tested; general structural proposal / open problem | Paper III frontier |
| the resulting tube gives a new knot invariant | unsupported; excluded | none |

## 11. Current proof programme

1. [x] Complete the Paper I matrix and admissibility audit for the Hecke sublanguage.
2. [x] Prove the Paper II planar and cylindrical pullback formulas without using any
   singular conclusion.
3. [x] Prove the Paper III local branch and exact `q=4` zero-graph theorems.
4. [x] Compute the quotient sign character and the full-orbifold cusp/completion
   metric.  Coverwise local finiteness and properness remain OQ-072.
5. [x] Identify the sign cover topologically and construct the operator-quotient
   periodic-orbit knot map, retaining the zero-spine/template distinction.
6. [x] Develop finite supplied-register families before attempting an infinite
   history divisor.
7. [x] Test composition, collapse, arithmetic/geometric splitting, and Frobenius
   on the `q=4` quadratic and quartic register models.  Canonical history origin
   remains OQ-073/OQ-074.
8. [ ] Only after those steps, form parameterized singular tubes and ask which
   arithmetic labels survive isotopy and Markov descent.

## 12. Sources and provenance

The bridge from Paper I contexts to `T_s` and `J` is internal to the AEG
foundations.  The Hecke group, its special polygons, and its continued fractions
use the classical and modern sources now added to the shared bibliography.  The
triangle-group Hauptmodul input uses the cited automorphic-forms source.

The pullback formulas, the square-root/Cayley realification, and the AEG claim
ledger are rederived in the present 2026-08-06 integration.  They are not claimed
as recovered `E_k` or `E_log` formulas from the historical repository.  The source
audit's negative finding therefore remains unchanged.
