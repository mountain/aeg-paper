# Paper I Core Theorem Dependency Graph with Cross-Paper Extension Nodes

**File:** `governance/03-theorem-dependency-graph.md`
**Status:** Authoritative
**Version:** 1.1
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`

**Applies to:** the theorem core of **Arithmetic Expression Geometry I:
Foundations**, together with the explicitly separated Paper II--III extension nodes
in Part XX.

---

## 1. Purpose

This document defines the logical dependency graph of the definitions, lemmas,
propositions, and theorems required for Paper I and records downstream extension
nodes without changing the Paper I proof order.

Its purposes are to:

* prevent results from being used before their hypotheses and definitions are established;
* distinguish strict proof dependencies from narrative or motivational dependencies;
* expose missing lemmas and convention choices;
* prevent circular dependencies;
* identify the critical path required for Paper I;
* identify optional results that may be removed without breaking the foundational argument;
* provide Codex and human editors with a machine-readable implementation order.

This document does not assign the final proof status of every result. Current proof status must be recorded in:

```text
governance/05-mathematical-status.md
```

---

# Part I. Dependency conventions

## 2. Edge types

The graph uses four edge types.

### 2.1 Strict proof dependency

Notation:

```text
A ==> B
```

Meaning:

* result (B) uses the statement, definition, or proof of (A);
* (B) must not be proved or formally stated before (A) is available;
* changing (A) requires rechecking (B).

---

### 2.2 Definitional dependency

Notation:

```text
A --> B
```

Meaning:

* object (B) is defined using object (A);
* the definition of (A) must be stable before (B) is finalized.

A definitional dependency is normally also a strict ordering constraint.

---

### 2.3 Narrative dependency

Notation:

```text
A -.-> B
```

Meaning:

* (A) explains the conceptual placement or motivation of (B);
* the proof of (B) may not logically require (A);
* the paper should normally present (A) first for coherence.

---

### 2.4 Optional or conditional dependency

Notation:

```text
A ~~~> B
```

Meaning:

* (B) is optional, conditional, or dependent on additional verification;
* removing (B) does not break the critical path of Paper I.

---

## 3. Node classes

Each graph node has one of the following classes:

* `CONV`: convention;
* `DEF`: definition;
* `LEM`: lemma;
* `PROP`: proposition;
* `THM`: theorem;
* `COR`: corollary;
* `EX`: example;
* `REM`: structural remark;
* `OPEN`: open problem or deferred obligation.

Only `DEF`, `LEM`, `PROP`, `THM`, and `COR` may appear in the strict theorem dependency path.

Examples and remarks must not serve as substitutes for proofs.

---

## 4. Critical-path notation

A node marked:

```text
[CRITICAL]
```

is required for the foundational argument of Paper I.

A node marked:

```text
[SUPPORTING]
```

strengthens or clarifies the paper but is not required for the central theorem chain.

A node marked:

```text
[OPTIONAL]
```

may be omitted if it is incomplete, too long, or outside the length budget.

---

# Part II. Global graph

## 5. Human-readable dependency graph

```mermaid
flowchart TD
    C0["C0 Composition and action conventions"]
    C1["C1 Algebraic domains and admissibility"]
    C2["C2 Differential-geometric hypotheses"]

    S1["S1 Arithmetic expression trees"]
    S2["S2 Internal-node dependency poset"]
    T1["T1 Sequential-tree classification"]
    S3["S3 Marked spinal histories"]
    S4["S4 Mirror, reversal, and path inverse"]
    S5["S5 Levels of equality"]

    P1["P1 Projective semantics of one-hole contexts"]
    P2["P2 Projective evaluation map"]
    T2["T2 Bilateral generation of PGL₂(K)"]
    P3["P3 Affine/Borel sector"]
    P4["P4 Positive real affine sector"]
    P5["P5 Riccati completion remark"]

    A1["A1 Affine composition law"]
    T3["T3 Target-frame cocycle formula"]
    T4["T4 Source-normalized cocycle formula"]
    A2["A2 Left/right Maurer–Cartan formulas"]
    A3["A3 Relative affine defect"]
    A4["A4 Elementary arithmetic torsion"]

    F1["F1 Affine Lie algebra generators"]
    T5["T5 Continuous affine flow"]
    F2["F2 Pfaffian propagation law"]
    F3["F3 Metric-compatible eikonal equation"]
    F4["F4 Rectifying coordinate"]
    F5["F5 Infinitesimal torsion density"]

    E1["E1 Definition of regular AES"]
    E2["E2 Invariant affine metric"]
    T6["T6 Basic hyperbolic AES"]
    E3["E3 Curvature calculation"]
    E4["E4 Arithmetic grid actions"]
    E5["E5 Baumslag–Solitar relation"]
    E6["E6 Laplace eigenfunction"]

    Z1["Z1 Zero set definition"]
    T7["T7 Regular zero-locus theorem"]
    Z2["Z2 Zero-set rigidity corollaries"]
    Z3["Z3 Definition of singular AES"]
    Z4["Z4 Classification of isolated-zero model"]
    Z5["Z5 Smooth parameter family"]
    T8["T8 Regular total-zero-set theorem"]
    Z6["Z6 Properness and tube warning"]
    Z7["Z7 Minimal multi-zero example"]

    G1["G1 ACS charge map and paths"]
    T9["T9 ACS evaluation formula"]
    G2["G2 Scale-compatible histories"]
    G3["G3 Charge-compatible histories"]
    T10["T10 Relative torsion independence"]
    T11["T11 Boundary-integral formula"]
    T12["T12 Weighted torsion–Stokes theorem"]

    K1["K1 Arithmetic contact form"]
    T13["T13 Contact nondegeneracy"]
    K2["K2 Horizontal lifts"]
    T14["T14 Legendrian realization of flow"]
    T15["T15 Horizontal curvature bracket"]
    K3["K3 Exact finite commutator formulas"]
    K4["K4 Horizontal covariant differential"]
    T16["T16 Horizontal curvature formula"]
    T17["T17 Local-global torsion synthesis"]

    C0 --> S3
    C0 --> P2
    C0 --> A1
    C0 --> G1

    C1 --> S1
    C1 --> P1
    C2 --> F3
    C2 --> E1
    C2 --> Z3

    S1 --> S2
    S2 ==> T1
    T1 --> S3
    S3 --> S4
    S3 --> S5

    S3 --> P1
    P1 --> P2
    P2 ==> T2
    T2 ==> P3
    P3 ==> P4
    T2 -.-> P5

    P3 --> A1
    A1 ==> T3
    T3 ==> T4
    T3 ==> A3
    T4 ==> A2
    A3 ==> A4

    P3 --> F1
    F1 ==> T5
    T5 ==> F2
    E1 --> F3
    T5 ==> F3
    F3 ==> F4
    T5 ==> F5

    F3 --> E1
    P4 -.-> E2
    E1 --> T6
    E2 ==> T6
    T6 ==> E3
    T6 ==> E4
    E4 ==> E5
    T6 ==> E6

    E1 --> Z1
    F3 ==> T7
    Z1 --> T7
    T7 ==> Z2
    E1 --> Z3
    T7 -.-> Z3
    Z3 --> Z4
    T6 --> Z4
    Z3 --> Z5
    Z5 ==> T8
    T8 ==> Z6
    Z3 ~~~> Z7
    T7 ~~~> Z7

    T3 --> G1
    G1 ==> T9
    T9 --> G2
    G2 ==> T10
    G1 --> G3
    G3 ==> T11
    T10 ==> T11
    T11 ==> T12

    F2 --> K1
    K1 ==> T13
    K1 --> K2
    K2 ==> T14
    T5 ==> T14
    K2 ==> T15
    T15 ==> K3
    K2 --> K4
    T15 ==> T16
    A4 -.-> T17
    T12 ==> T17
    T15 ==> T17
    K3 ==> T17
```

---

## 6. Critical path

The minimum theorem chain required for Paper I is:

```text
C0 Composition convention
  ↓
S1 Arithmetic expression tree
  ↓
S2 Dependency poset
  ↓
T1 Sequential-tree classification
  ↓
S3 Marked spinal history
  ↓
P1 Projective semantics
  ↓
P2 Projective evaluation
  ↓
T2 Bilateral PGL₂ generation
  ↓
P3 Affine/Borel sector
  ↓
A1 Affine composition
  ↓
T3–T4 Affine cocycles
  ↓
F1 Affine Lie algebra
  ↓
T5 Continuous affine flow
  ├─────────────┬─────────────────────┐
  ↓             ↓                     ↓
E1 Regular AES  G1 ACS               K1 Contact form
  ↓             ↓                     ↓
T6 Hyperbolic   T9 ACS evaluation     T13 Contact nondegeneracy
model           ↓                     ↓
  ↓             T10 Relative torsion  T15 Curvature bracket
T7 Regular      ↓                     ↓
zero theorem    T12 Stokes theorem    T16 Horizontal curvature
                 \                    /
                  \                  /
                   └───── T17 ──────┘
                   Local-global synthesis
```

The following nodes are **not** part of the minimum critical path:

* the isolated-zero example;
* the minimal multi-zero example;
* the Baumslag–Solitar proposition;
* the Laplace eigenfunction result;
* the rectifying coordinate;
* detailed Maurer–Cartan formulas;
* the full parameter-family result, if length is constrained.

They may remain because they strengthen the paper, but Paper I must not depend on them for its main thesis.

---

# Part III. Convention nodes

## 7. C0 — Chronological composition and action conventions

**Class:** `CONV`
**Priority:** `[CRITICAL]`
**Target location:** Introduction or Appendix A, referenced before Chapter 2

### Required content

Fix the convention that a history:

[
\gamma=(g_1,\ldots,g_n)
]

applies (g_1) first and (g_n) last:

[
\nu_x(\gamma)
=============

g_n\circ\cdots\circ g_1(x).
]

Fix the corresponding matrix product convention.

Fix notation for concatenation:

[
\gamma\delta.
]

The paper must state whether this means:

* apply (\gamma) and then (\delta), or
* apply (\delta) and then (\gamma).

Every cocycle and relative-defect formula depends on this choice.

### Downstream dependencies

```text
C0 --> S3
C0 --> P2
C0 --> A1
C0 --> G1
C0 --> K3
```

### Failure condition

If C0 remains ambiguous, none of the following may be considered verified:

* affine cocycle formulas;
* matrix decompositions;
* Baumslag–Solitar relation;
* ACS path orientation;
* finite contact commutator.

---

## 8. C1 — Algebraic domain and admissibility conventions

**Class:** `CONV`
**Priority:** `[CRITICAL]`

### Required content

Distinguish:

* a general field (K);
* ordinary arithmetic evaluation;
* non-degenerate projective evaluation;
* division-domain exclusions;
* constant and non-invertible contexts;
* (\mathbb P^1(K)) as projective continuation.

### Downstream dependencies

```text
C1 --> S1
C1 --> P1
C1 --> T2
```

---

## 9. C2 — Differential-geometric hypotheses

**Class:** `CONV`
**Priority:** `[CRITICAL]`

### Required content

Specify when:

* (\mu,\lambda) are real constants;
* (\mu\neq0);
* (\lambda\neq0);
* (\mu,\lambda>0);
* the metric is smooth and non-degenerate;
* the assignment is smooth;
* the manifold has boundary;
* completeness is or is not assumed.

### Downstream dependencies

```text
C2 --> F3
C2 --> E1
C2 --> T6
C2 --> T7
C2 --> Z3
C2 --> T13
```

---

# Part IV. Sequential syntax branch

## 10. S1 — Arithmetic expression trees

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define binary arithmetic expression trees with:

* atomic leaves;
* internal operation labels;
* admissible ordinary evaluation.

### Depends on

```text
C1
```

### Exports

* tree (T);
* internal-node set (I(T));
* recursive evaluation relation.

---

## 11. S2 — Dependency poset

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define the partial order on internal nodes:

[
u\preceq v
]

when the output of (u) is required to evaluate (v).

### Depends on

```text
S1
```

### Exports

* internal dependency poset;
* legal evaluation orders as linear extensions.

---

## 12. T1 — Sequential-tree classification

**Class:** `THM`
**Priority:** `[CRITICAL]`
**Target label:** `thm:sequential-tree-classification`

### Statement

For a finite binary expression tree (T), the following are equivalent:

1. its internal dependency poset has a unique linear extension;
2. the internal dependency poset is a chain;
3. every internal vertex has at most one internal child;
4. the internal vertices form a single spine.

### Strict dependencies

```text
S1
S2
```

### Proof obligations

* prove that a finite poset with a unique linear extension is a chain;
* prove that two internal children of one vertex are incomparable;
* prove that the one-internal-child property yields a unique spine;
* handle the leaf-only tree separately.

### Exports

* intrinsic definition of sequential tree;
* replacement for the ambiguous historical “threadlike” definition.

---

## 13. S3 — Marked spinal histories

**Class:** `DEF`
**Priority:** `[CRITICAL]`
**Target label:** `def:marked-spinal-history`

### Definition

A marked spinal history is:

[
\gamma
======

\bigl(
x_0;
(\omega_i,c_i,\varepsilon_i)_{i=1}^{n}
\bigr),
\qquad
\varepsilon_i\in{1,2},
]

with:

[
C_{\omega,c}^{(1)}[z]=\omega(z,c),
\qquad
C_{\omega,c}^{(2)}[z]=\omega(c,z).
]

### Strict dependencies

```text
C0
T1
```

### Proof or construction obligation

Prove that a sequential tree with a marked seed determines a unique marked spinal history.

If claiming a bijection, prove the inverse construction.

### Exports

* free and bounded histories;
* chirality word;
* chronological context word;
* history composition.

---

## 14. S4 — Mirror, reversal, and path inverse

**Class:** `DEF`
**Priority:** `[CRITICAL]`

### Dependencies

```text
S3
C0
```

### Required distinctions

* mirror swaps slot labels;
* temporal reversal reverses the context order;
* path inverse reverses order and replaces each context by its inverse.

### Required example

For one explicit (\gamma), show:

[
m\gamma\neq r\gamma.
]

No theorem may use “reverse” without specifying which operation is intended.

---

## 15. S5 — Levels of equality

**Class:** `DEF` / `REM`
**Priority:** `[SUPPORTING]`

### Dependencies

```text
S3
P2
G1
```

### Required levels

* literal tree equality;
* marked-history equality;
* induced-operator equality;
* total-charge equality;
* endpoint equality;
* quotient equality.

This node must not introduce the full condensation theory.

---

# Part V. Projective semantics branch

## 16. P1 — Projective semantics of one-hole contexts

**Class:** `DEF` / `PROP`
**Priority:** `[CRITICAL]`

### Statement

Every non-degenerate one-hole arithmetic context extends to a fractional linear transformation of:

[
\mathbb P^1(K).
]

### Strict dependencies

```text
C1
S3
```

### Required table

Include projective representatives for:

[
z+c,\quad
z-c,\quad
c-z,\quad
cz,\quad
z/c,\quad
c/z.
]

### Proof obligations

For each context:

* give a matrix representative;
* state invertibility assumptions;
* state ordinary-domain exclusions;
* identify degenerate cases excluded from (PGL_2(K)).

---

## 17. P2 — Projective evaluation map

**Class:** `DEF` / `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `def:projective-evaluation`

Define:

[
\rho:
\operatorname{Hist}^{\pm,\times}_K
\longrightarrow
PGL_2(K).
]

### Strict dependencies

```text
C0
P1
S3
```

### Proof obligations

Prove compatibility with chronological composition.

Do not claim injectivity.

Do not quotient histories by equal projective evaluation at the definition stage.

---

## 18. T2 — Bilateral arithmetic generates (PGL_2(K))

**Class:** `THM`
**Priority:** `[CRITICAL]`
**Target label:** `thm:bilateral-pgl2-generation`

### Statement

The non-degenerate projective evaluations of bilateral arithmetic spinal histories generate:

[
PGL_2(K).
]

### Strict dependencies

```text
P1
P2
C1
```

### Proof obligations

Show that the history language contains:

[
T_s(z)=z+s,
\qquad
D_q(z)=qz,
\qquad
J(z)=-1/z.
]

Handle separately:

#### Case (C=0)

Show that:

[
\frac{Az+B}{D}
]

is affine.

#### Case (C\neq0)

Verify explicitly:

[
\frac{Az+B}{Cz+D}
=================

T_{A/C}
\circ
D_{(AD-BC)/C^2}
\circ
J
\circ
T_{D/C}.
]

Check the formula under the adopted chronological convention.

### Field warning

The proof must be reviewed for:

* characteristic (2);
* sign conventions;
* nonzero denominators;
* scalar equivalence in (PGL_2(K)).

---

## 19. P3 — Affine/Borel sector

**Class:** `COR`
**Priority:** `[CRITICAL]`
**Target label:** `cor:affine-borel-sector`

### Statement

The projective transformations fixing (\infty) are:

[
B_\infty
========

\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

The constant-chirality AEG language used for the continuous theory lands in this sector, subject to the exact language restrictions stated in the paper.

### Strict dependencies

```text
T2
P1
```

### Proof obligations

* identify which elementary contexts preserve (\infty);
* distinguish the whole algebraic Borel from the positive real component;
* do not state that every slot-(1) history is non-degenerate without conditions.

---

## 20. P4 — Positive real affine sector

**Class:** `PROP` / `REM`
**Priority:** `[CRITICAL]`

### Statement

With real exponential scaling:

[
z\mapsto e^\lambda z,
]

the continuous theory lies in:

[
\operatorname{Aff}^{+}(1,\mathbb R).
]

### Dependencies

```text
P3
C2
```

### Exports

* the real Lie group used by the flow and hyperbolic model.

---

## 21. P5 — Riccati completion

**Class:** `REM`
**Priority:** `[SUPPORTING]`

### Statement

The general infinitesimal projective flow has the form:

[
\dot z
======

\beta+\alpha z+\kappa z^2,
]

while Paper I studies the affine slice:

[
\kappa=0.
]

### Dependencies

```text
T2
P3
F1
```

### Exclusion

No full projective differential geometry is proved here.

---

# Part VI. Affine cocycle branch

## 22. A1 — Affine composition law

**Class:** `PROP`
**Priority:** `[CRITICAL]`

For:

[
f_i(x)=s_i x+t_i,
]

define:

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n.
]

### Strict dependencies

```text
C0
P3
```

### Exports

* accumulated scale;
* accumulated translation;
* recursive composition law.

---

## 23. T3 — Target-frame cocycle formula

**Class:** `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `prop:target-affine-cocycle`

### Statement

[
\Phi_n=\prod_{i=1}^{n}s_i,
]

[
\xi_n
=====

\sum_{i=1}^{n}
t_i\prod_{j=i+1}^{n}s_j.
]

### Strict dependencies

```text
A1
C0
```

### Proof obligation

Prove by induction under chronological composition.

### Interpretation

Each translation is weighted by all future scalings.

---

## 24. T4 — Source-normalized cocycle formula

**Class:** `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `prop:source-normalized-cocycle`

### Definition

[
\widehat\xi_n
=============

\Phi_n^{-1}\xi_n.
]

### Statement

[
\widehat\xi_n
=============

\sum_{i=1}^{n}
\frac{t_i}{\prod_{j=1}^{i}s_j}.
]

### Strict dependencies

```text
T3
```

### Interpretation

Each translation is normalized by accumulated past scale.

---

## 25. A2 — Left and right affine differentials

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

For:

[
g=
\begin{pmatrix}
e^\lambda&\xi\
0&1
\end{pmatrix},
]

prove:

[
(g^{-1}dg)_{\mathrm{tr}}
========================

e^{-\lambda}d\xi,
]

[
(dg,g^{-1})_{\mathrm{tr}}
=========================

d\xi-\xi,d\lambda.
]

### Dependencies

```text
T3
T4
C0
```

### Warning

These are frame conventions, not definitions of operand-slot chirality.

---

## 26. A3 — Relative affine defect

**Class:** `DEF` / `PROP`
**Priority:** `[CRITICAL]`

For:

[
\rho(\gamma)(x)
===============

\Phi_\gamma x+\xi_\gamma,
]

[
\rho(\delta)(x)
===============

\Phi_\delta x+\xi_\delta,
]

define their relative affine comparison.

### Strict dependencies

```text
T3
P3
```

### Key proposition

If:

[
\Phi_\gamma=\Phi_\delta,
]

then:

[
\nu_x(\gamma)-\nu_x(\delta)
===========================

\xi_\gamma-\xi_\delta
]

is independent of (x).

### Required distinction

* same scale is sufficient for endpoint-difference independence;
* same full ACS endpoint is required for a closed ACS filling.

---

## 27. A4 — Elementary arithmetic torsion

**Class:** `EX` / `PROP`
**Priority:** `[CRITICAL]`

Recover:

[
(x+\mu)e^\lambda
----------------

# (xe^\lambda+\mu)

\mu(e^\lambda-1).
]

### Dependencies

```text
A3
T3
```

### Export

This is the elementary finite defect compared later with:

* ACS weighted area;
* contact commutator;
* infinitesimal curvature.

---

# Part VII. Continuous-flow branch

## 28. F1 — Affine Lie algebra generators

**Class:** `DEF` / `LEM`
**Priority:** `[CRITICAL]`

Define:

[
E=\partial_a,
\qquad
H=a\partial_a.
]

Record:

[
[H,E]=-E
]

under the chosen sign convention.

### Dependencies

```text
P4
C2
```

---

## 29. T5 — Continuous affine flow

**Class:** `THM`
**Priority:** `[CRITICAL]`
**Target label:** `thm:continuous-affine-flow`

### Statement

For a unit direction making angle (\theta) with the additive generator:

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

### Strict dependencies

```text
F1
C2
```

### Preferred proof

Use the affine Lie algebra generator:

[
\Omega(\theta)
==============

\mu\cos\theta,E
+
\lambda\sin\theta,H.
]

### Secondary proof

A first-order expansion of add–multiply updates may be included as verification.

### Exclusion

Do not derive the full Riccati flow here.

---

## 30. F2 — Pfaffian propagation law

**Class:** `PROP`
**Priority:** `[CRITICAL]`

Write:

[
da
==

\mu,du+\lambda a,dv.
]

### Strict dependencies

```text
T5
```

### Warning

This is the horizontal propagation relation. It is not the differential of a globally defined scalar function on the unrestricted ((u,v,a))-space.

---

## 31. E1 — Definition of regular AES

**Class:** `DEF`
**Priority:** `[CRITICAL]`
**Target label:** `def:regular-aes`

A regular AES should specify:

[
(\mathcal M,g,a;\mu,\lambda)
]

with the regularity and domain assumptions required for:

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

### Dependencies

```text
C2
T5
```

### Definition obligation

Clarify whether the eikonal equation is:

* the definition of a regular AES;
* a consequence of a framed flow structure;
* one component of a broader definition.

One version must be selected consistently.

---

## 32. F3 — Metric-compatible eikonal equation

**Class:** `PROP`
**Priority:** `[CRITICAL]`

### Statement

In a metric for which the additive and multiplicative directions form the specified orthonormal or normalized frame:

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

### Strict dependencies

```text
T5
E1
C2
```

### Warning

The equation is not metric-free.

---

## 33. F4 — Rectifying coordinate

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

For suitable nonzero parameters, define:

[
r(a)
====

\operatorname{arcsinh}
\left(
\frac{\lambda a}{\mu}
\right).
]

Show:

[
|\nabla r|
==========

|\lambda|.
]

### Dependencies

```text
F3
```

### Required cases

Either:

* assume (\mu>0,\lambda>0), or
* state separate sign conventions.

---

## 34. F5 — Infinitesimal torsion density

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

Show:

[
d\tau
=====

\mu\lambda,du,dv
+
O(|(du,dv)|^3).
]

### Dependencies

```text
T5
A4
```

### Warning

This is an asymptotic finite-step comparison, not an exact two-form identity by itself.

---

# Part VIII. Hyperbolic-model branch

## 35. E2 — Invariant affine metric

**Class:** `PROP`
**Priority:** `[CRITICAL]`

Construct the normalized invariant metric on:

[
\operatorname{Aff}^{+}(1,\mathbb R).
]

In suitable coordinates:

[
g_{\mu,\lambda}
===============

e^{-2\lambda v}\frac{du^2}{\mu^2}
+
dv^2.
]

### Dependencies

```text
P4
C2
```

### Proof obligations

* identify the group coordinates;
* state left- or right-invariance;
* verify the metric transformation law;
* avoid uniqueness claims.

---

## 36. T6 — Basic hyperbolic AES

**Class:** `THM`
**Priority:** `[CRITICAL]`
**Target label:** `thm:basic-hyperbolic-aes`

### Statement

On the upper half-plane:

[
\mathcal H={(x,y):y>0},
]

with:

[
g_{\mu,\lambda}
===============

\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
\qquad
a(x,y)=-\frac{x}{y},
]

one has:

[
|\nabla a|*{g*{\mu,\lambda}}^2
==============================

\mu^2+\lambda^2a^2.
]

### Strict dependencies

```text
E1
E2
F3
```

### Proof obligations

* compute the inverse metric;
* compute (a_x,a_y);
* verify the equation exactly;
* state parameter assumptions.

### Export

Define:

[
\mathfrak E_0(\mu,\lambda).
]

---

## 37. E3 — Curvature calculation

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

### Statement

Compute the Gaussian curvature of the normalized metric.

Expected result under the stated normalization:

[
K=-\lambda^2.
]

### Dependencies

```text
T6
```

### Verification obligation

Check the coordinate rescaling carefully.

---

## 38. E4 — Arithmetic grid actions

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

Define transformations implementing:

[
a\mapsto a+s,
\qquad
a\mapsto ka.
]

### Dependencies

```text
T6
C0
```

### Proof obligations

* verify the assignment transformation;
* state whether each map is an isometry;
* fix action order.

---

## 39. E5 — Baumslag–Solitar relation

**Class:** `PROP`
**Priority:** `[OPTIONAL]`

### Statement

Verify the chosen relation, for example:

[
Y_k^{-1}X_s^{,k}Y_k=X_s,
]

under the adopted transformation convention.

### Dependencies

```text
E4
C0
```

### Warning

This proposition must be omitted if the action-order convention is not fully checked.

No complexity conclusion follows from it in Paper I.

---

## 40. E6 — Laplace eigenfunction

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

### Statement

Compute:

[
\Delta_g a
==========

c_\lambda a
]

with the exact eigenvalue determined by the metric and Laplacian sign convention.

### Dependencies

```text
T6
C2
```

### Proof obligations

* define (\Delta_g);
* compute using the actual anisotropically normalized metric;
* do not reuse the normalized (\mu=\lambda=1) result without rescaling.

---

# Part IX. Zero-geometry branch

## 41. Z1 — Zero-set definition

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define:

[
Z(a)=a^{-1}(0).
]

### Dependencies

```text
E1
```

---

## 42. T7 — Regular zero-locus theorem

**Class:** `THM`
**Priority:** `[CRITICAL]`
**Target label:** `thm:regular-zero-locus`

### Statement

If:

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

and:

[
\mu\neq0,
]

then on (Z(a)):

[
|\nabla a|=|\mu|>0.
]

Therefore (0) is a regular value and:

[
Z(a)
]

is a smooth codimension-one submanifold.

### Strict dependencies

```text
F3
Z1
C2
```

### Proof obligations

* invoke the regular-value theorem;
* state the manifold and boundary assumptions;
* distinguish interior zeros from possible boundary behavior.

---

## 43. Z2 — Zero-set rigidity corollaries

**Class:** `COR`
**Priority:** `[CRITICAL]`

For a two-dimensional regular AES, conclude that regular zero sets are unions of disjoint smooth one-manifolds.

Subject to exact hypotheses, record:

* no isolated regular zero;
* no regular crossing;
* no regular branch point;
* no regular interior endpoint.

### Strict dependencies

```text
T7
```

### Warning

Global statements about components being circles or proper lines require additional topology or properness assumptions.

---

## 44. Z3 — Singular AES

**Class:** `DEF`
**Priority:** `[CRITICAL]`
**Target label:** `def:singular-aes`

Define:

[
(\mathcal M,S,g,a;\mu,\lambda),
]

where the regular equations hold on:

[
\mathcal M\setminus S.
]

### Dependencies

```text
E1
C2
```

### Required distinctions

Allow singularities in:

* assignment;
* metric;
* parameters;
* chart;
* domain;
* projective continuation.

Define:

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

---

## 45. Z4 — Isolated-zero model

**Class:** `EX` / `PROP`
**Priority:** `[SUPPORTING]`

Reclassify the current isolated-center model.

### Dependencies

```text
Z3
T6
T7
```

### Required proof obligations

Determine:

* whether the center belongs to the manifold;
* whether the assignment extends continuously;
* whether it extends smoothly;
* whether the metric is regular;
* where the flow equation holds;
* why the isolated zero does not contradict T7.

The model must not be called a regular AES if it violates the hypotheses of T7.

---

## 46. Z5 — Smooth parameter families

**Class:** `DEF`
**Priority:** `[SUPPORTING]`

Define:

[
a_t:\mathcal M\to\mathbb R,
]

[
A(p,t)=a_t(p),
]

[
\mathcal Z=A^{-1}(0).
]

### Dependencies

```text
Z3
C2
```

---

## 47. T8 — Regular total-zero-set theorem

**Class:** `PROP` / `THM`
**Priority:** `[SUPPORTING]`
**Target label:** `prop:regular-total-zero-set`

### Statement

If:

[
d_pa_t\neq0
]

for every ((p,t)\in\mathcal Z), then (0) is a regular value of (A), and:

[
\mathcal Z
]

is a smooth codimension-one submanifold of (\mathcal M\times I).

If (\dim\mathcal M=2), then (\mathcal Z) is a surface.

### Strict dependencies

```text
Z5
```

### Optional strengthening

The projection:

[
\pi:\mathcal Z\to I
]

is a submersion under the same spatial regularity condition.

If included, prove it explicitly.

### Exclusion

Do not conclude global local triviality without properness.

---

## 48. Z6 — Properness and tube warning

**Class:** `REM` / `OPEN`
**Priority:** `[CRITICAL]`

State that Ehresmann-type local triviality requires appropriate assumptions such as:

* properness;
* compact fibers;
* suitable boundary control.

This node prevents T8 from being overstated.

---

## 49. Z7 — Minimal multi-zero example

**Class:** `EX`
**Priority:** `[OPTIONAL]`

### Entry condition

This node may enter Paper I only after verifying:

1. domain;
2. metric;
3. assignment;
4. singular set;
5. flow equation;
6. exact zero topology.

### Dependencies

```text
Z3
T7
```

### Failure rule

If any verification is incomplete, move the example to Paper III or the open-problem list.

No later Paper I theorem may depend on Z7.

---

# Part X. ACS branch

## 50. G1 — ACS charge map and paths

**Class:** `DEF`
**Priority:** `[CRITICAL]`
**Target label:** `def:acs`

For an affine history, define additive and logarithmic multiplicative increments:

[
(\Delta A_i,\Delta M_i).
]

Define the cumulative path:

[
C_\gamma.
]

### Dependencies

```text
C0
T3
```

### Required conventions

Fix:

* chronological direction;
* orientation;
* signed charges;
* endpoint notation.

---

## 51. T9 — ACS evaluation formula

**Class:** `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `prop:acs-evaluation`

### Preferred statement

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
]

### Strict dependencies

```text
T3
G1
```

### Proof obligation

Derive directly from the target-frame affine cocycle formula.

Do not introduce the weighting kernel as an independent geometric choice.

---

## 52. G2 — Scale-compatible histories

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define (\gamma,\delta) to be scale-compatible when:

[
M_\gamma=M_\delta,
]

equivalently:

[
\Phi_\gamma=\Phi_\delta
]

in the positive real affine sector.

### Dependencies

```text
T9
A3
```

---

## 53. G3 — Charge-compatible histories

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define (\gamma,\delta) to be charge-compatible when:

[
A_\gamma=A_\delta,
\qquad
M_\gamma=M_\delta.
]

Then (C_\gamma) and (C_\delta) have the same ACS endpoints.

### Dependencies

```text
G1
```

### Required distinction

Charge compatibility is stronger than scale compatibility.

---

## 54. T10 — Relative torsion independence

**Class:** `PROP`
**Priority:** `[CRITICAL]`

For scale-compatible histories define:

[
\tau(\gamma,\delta)
===================

\nu_x(\gamma)-\nu_x(\delta).
]

Prove that it is independent of (x).

### Strict dependencies

```text
T9
G2
A3
```

---

## 55. T11 — Boundary-integral formula

**Class:** `PROP`
**Priority:** `[CRITICAL]`

For charge-compatible histories, express:

[
\tau(\gamma,\delta)
]

as a closed weighted contour integral.

One consistent form is:

[
\tau(\gamma,\delta)
===================

e^{M_*}
\oint_{\partial\Sigma_{\gamma,\delta}}
e^{-M},dA,
]

with orientation fixed explicitly.

### Strict dependencies

```text
T10
G3
G1
```

### Proof obligation

Check sign and path orientation against at least two explicit examples.

---

## 56. T12 — Weighted torsion–Stokes theorem

**Class:** `THM`
**Priority:** `[CRITICAL]`
**Target label:** `thm:torsion-stokes`

Let:

[
\eta_*
======

e^{M_*}e^{-M},dA
]

for a fixed common terminal multiplicative charge (M_*), or use an equivalent normalized convention.

Prove:

[
\tau(\gamma,\delta)
===================

# \oint_{\partial\Sigma_{\gamma,\delta}}\eta_*

\iint_{\Sigma_{\gamma,\delta}}d\eta_*.
]

### Strict dependencies

```text
T11
```

### Proof obligations

* state existence or choice of the oriented (2)-chain;
* show independence from filling when applicable;
* state the role of the simply connected ACS plane;
* handle signed or self-intersecting paths using chains, not informal enclosed regions.

---

# Part XI. Contact branch

## 57. K1 — Arithmetic contact form

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define:

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

### Dependencies

```text
F2
C2
```

---

## 58. T13 — Contact nondegeneracy

**Class:** `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `prop:contact-form`

Prove:

[
\alpha\wedge d\alpha
====================

\mu\lambda,du\wedge da\wedge dv
]

up to the fixed orientation convention.

Conclude that (\alpha) is a contact form when:

[
\mu\lambda\neq0.
]

### Strict dependencies

```text
K1
C2
```

---

## 59. K2 — Horizontal lifts

**Class:** `DEF` / `PROP`
**Priority:** `[CRITICAL]`

Define:

[
D_u
===

\partial_u+\mu\partial_a,
]

[
D_v
===

\partial_v+\lambda a\partial_a.
]

Prove:

[
\alpha(D_u)=\alpha(D_v)=0.
]

### Dependencies

```text
K1
```

---

## 60. T14 — Legendrian realization of affine flow

**Class:** `PROP`
**Priority:** `[CRITICAL]`

For:

[
D_\theta
========

\cos\theta,D_u+\sin\theta,D_v,
]

show that a tangent curve satisfies:

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

### Strict dependencies

```text
K2
T5
```

### Purpose

Establish that the contact model reproduces, rather than independently postulates, the affine flow.

---

## 61. T15 — Horizontal curvature bracket

**Class:** `THM` / `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `thm:contact-curvature`

Prove:

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

### Strict dependencies

```text
K2
C2
```

### Interpretation

The bracket is vertical and measures failure of horizontal integrability.

---

## 62. K3 — Exact finite commutator formulas

**Class:** `PROP`
**Priority:** `[SUPPORTING]`

Compute separately:

### Open two-path defect

[
\mu h(e^{\lambda k}-1).
]

### Closed-loop vertical holonomy

Compute the exact formula under the adopted flow composition convention.

### Dependencies

```text
K2
T15
C0
```

### Required warning

The two finite quantities are not identical, although they share the same leading infinitesimal density.

---

## 63. K4 — Horizontal covariant differential

**Class:** `DEF`
**Priority:** `[CRITICAL]`

Define on smooth scalar fields:

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
]

### Dependencies

```text
K1
K2
```

### Scope restriction

Paper I defines (\delta_H) primarily on scalar fields.

A full graded differential calculus on forms is not required.

---

## 64. T16 — Horizontal curvature formula

**Class:** `PROP`
**Priority:** `[CRITICAL]`
**Target label:** `prop:horizontal-differential-curvature`

Define the antisymmetrized second horizontal derivative by:

[
\delta_H^2F
:=
(D_uD_vF-D_vD_uF),du\wedge dv.
]

Prove:

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

In particular:

[
\delta_H^2a
===========

\mu\lambda,du\wedge dv.
]

### Strict dependencies

```text
K4
T15
```

### Required warning

This notation does not assert that (\delta_H) has already been extended to a full differential complex.

---

## 65. T17 — Local-global torsion synthesis

**Class:** `THM` / `SYNTHESIS`
**Priority:** `[CRITICAL]`

This result should state the precise relationship among:

1. finite affine endpoint defect;
2. ACS weighted area;
3. exact finite contact commutator or holonomy;
4. infinitesimal contact curvature.

### Strict dependencies

```text
A4
T12
T15
K3
T16
```

### Required form

The theorem must not claim that all four quantities are literally equal at finite scale.

It should separate:

#### Exact affine/ACS identity

[
\text{relative affine defect}
=============================

\text{ACS weighted area}.
]

#### Infinitesimal contact identity

[
\text{leading local defect}
===========================

# \mu\lambda,du\wedge dv

\text{horizontal curvature density}.
]

#### Finite contact relation

State the exact exponential correction.

### Purpose

This is the conceptual culmination of Paper I.

---

# Part XII. Forbidden dependency edges

## 66. Explicitly prohibited edges

The following proof dependencies are not allowed.

### 66.1 Analysis cannot support foundations

```text
Arithmetic holomorphicity =/=> contact curvature
Arithmetic Cauchy–Riemann equations =/=> regular AES
Twisted harmonicity =/=> affine flow
```

These analytic structures belong to Paper II and must not be used to prove Paper I foundations.

---

### 66.2 Singular examples cannot define the regular theory

```text
isolated-zero model =/=> definition of regular AES
multi-zero example =/=> general zero-locus theorem
tube picture =/=> singular-AES definition
```

Definitions must precede and control examples.

---

### 66.3 Hyperbolicity cannot be inferred from noncommutativity alone

```text
affine torsion =/=> hyperbolic metric
noncommuting generators =/=> negative curvature
Baumslag–Solitar relation =/=> computational hardness
```

The hyperbolic model requires an explicit metric construction and verification.

---

### 66.4 Projective semantics cannot erase ordinary domains

```text
PGL₂ action =/=> ordinary division by zero is defined
projective continuation =/=> all intermediate arithmetic steps are admissible
```

---

### 66.5 Contact structure cannot force a unique complex structure

```text
contact form =/=> canonical almost-complex structure
contact curvature =/=> arithmetic holomorphicity
```

Paper II must add the analytic data explicitly.

---

### 66.6 Regular total zero set cannot imply global tube triviality

```text
smooth total zero set =/=> proper projection
submersion =/=> global product
regular family =/=> knot invariant
```

---

# Part XIII. Narrative dependencies

## 67. Narrative but non-strict edges

The following ordering is preferred but not required by proof.

### Projective placement before affine development

```text
T2 Bilateral PGL₂ generation -.-> A1 Affine cocycles
T2 Bilateral PGL₂ generation -.-> T5 Affine flow
```

The affine cocycle and flow can be developed independently, but the projective theorem explains their correct scope.

---

### Affine group before hyperbolic model

```text
P4 Positive affine sector -.-> E2 Invariant metric
```

The model can be verified directly, but deriving it from the affine group improves conceptual coherence.

---

### Regular-zero theorem before singular definitions

```text
T7 Regular zero-locus theorem -.-> Z3 Singular AES
```

The singular definition can be stated independently, but the theorem explains why singularity is necessary for isolated or branching zeros.

---

### ACS before contact synthesis

```text
T12 Torsion–Stokes -.-> T17 Local-global synthesis
```

The contact bracket does not depend on ACS, but the final interpretation does.

---

# Part XIV. Optional nodes and deletion policy

## 68. Optional nodes

The following nodes may be removed from the main text without breaking the critical path:

| Node | Result                              | Recommended fallback       |
| ---- | ----------------------------------- | -------------------------- |
| A2   | Maurer–Cartan formulas              | Appendix B                 |
| F4   | Rectifying coordinate               | Appendix C or Paper II     |
| F5   | Taylor-derived torsion density      | Contact chapter comparison |
| E3   | Curvature normalization             | Appendix C                 |
| E5   | Baumslag–Solitar relation           | Remark or appendix         |
| E6   | Laplace eigenfunction               | Paper II if too long       |
| Z4   | Isolated-zero model                 | Example or appendix        |
| Z7   | Multi-zero example                  | Paper III                  |
| K3   | Long finite commutator calculations | Appendix D                 |

Optional nodes must not be cited as prerequisites by critical nodes.

---

## 69. Conditional inclusion test

An optional node enters the main text only if:

1. its statement is mathematically stable;
2. its proof is complete;
3. its notation is consistent;
4. it materially advances the central narrative;
5. it does not cause Paper I to exceed the scope or length budget.

---

# Part XV. Machine-readable adjacency list

## 70. Strict and definitional dependencies

The following list is intended for Codex and audit scripts.

```yaml
nodes:
  C0:
    type: convention
    title: chronological composition and action conventions
    critical: true
    depends_on: []

  C1:
    type: convention
    title: algebraic domains and admissibility
    critical: true
    depends_on: []

  C2:
    type: convention
    title: differential-geometric hypotheses
    critical: true
    depends_on: []

  S1:
    type: definition
    title: arithmetic expression trees
    critical: true
    depends_on: [C1]

  S2:
    type: definition
    title: internal-node dependency poset
    critical: true
    depends_on: [S1]

  T1:
    type: theorem
    title: sequential-tree classification
    critical: true
    depends_on: [S1, S2]

  S3:
    type: definition
    title: marked spinal histories
    critical: true
    depends_on: [C0, T1]

  S4:
    type: definition
    title: mirror reversal and path inverse
    critical: true
    depends_on: [C0, S3]

  S5:
    type: definition
    title: levels of equality
    critical: false
    depends_on: [S3, P2, G1]

  P1:
    type: definition
    title: projective semantics of one-hole contexts
    critical: true
    depends_on: [C1, S3]

  P2:
    type: definition
    title: projective evaluation map
    critical: true
    depends_on: [C0, P1, S3]

  T2:
    type: theorem
    title: bilateral arithmetic generates PGL2
    critical: true
    depends_on: [C1, P1, P2]

  P3:
    type: corollary
    title: affine Borel sector
    critical: true
    depends_on: [P1, T2]

  P4:
    type: proposition
    title: positive real affine sector
    critical: true
    depends_on: [C2, P3]

  P5:
    type: remark
    title: Riccati completion
    critical: false
    depends_on: [T2, P3, F1]

  A1:
    type: proposition
    title: affine composition law
    critical: true
    depends_on: [C0, P3]

  T3:
    type: proposition
    title: target-frame affine cocycle
    critical: true
    depends_on: [A1, C0]

  T4:
    type: proposition
    title: source-normalized affine cocycle
    critical: true
    depends_on: [T3]

  A2:
    type: proposition
    title: left and right affine differentials
    critical: false
    depends_on: [C0, T3, T4]

  A3:
    type: proposition
    title: relative affine defect
    critical: true
    depends_on: [P3, T3]

  A4:
    type: proposition
    title: elementary arithmetic torsion
    critical: true
    depends_on: [A3, T3]

  F1:
    type: definition
    title: affine Lie algebra generators
    critical: true
    depends_on: [C2, P4]

  T5:
    type: theorem
    title: continuous affine flow
    critical: true
    depends_on: [C2, F1]

  F2:
    type: proposition
    title: Pfaffian propagation law
    critical: true
    depends_on: [T5]

  E1:
    type: definition
    title: regular arithmetic expression space
    critical: true
    depends_on: [C2, T5]

  F3:
    type: proposition
    title: metric-compatible eikonal equation
    critical: true
    depends_on: [C2, E1, T5]

  F4:
    type: proposition
    title: rectifying coordinate
    critical: false
    depends_on: [F3]

  F5:
    type: proposition
    title: infinitesimal torsion density
    critical: false
    depends_on: [A4, T5]

  E2:
    type: proposition
    title: invariant affine metric
    critical: true
    depends_on: [C2, P4]

  T6:
    type: theorem
    title: basic hyperbolic AES
    critical: true
    depends_on: [E1, E2, F3]

  E3:
    type: proposition
    title: Gaussian curvature
    critical: false
    depends_on: [T6]

  E4:
    type: proposition
    title: arithmetic grid actions
    critical: false
    depends_on: [C0, T6]

  E5:
    type: proposition
    title: Baumslag-Solitar relation
    critical: false
    depends_on: [C0, E4]

  E6:
    type: proposition
    title: Laplace eigenfunction
    critical: false
    depends_on: [C2, T6]

  Z1:
    type: definition
    title: zero set
    critical: true
    depends_on: [E1]

  T7:
    type: theorem
    title: regular zero-locus theorem
    critical: true
    depends_on: [C2, F3, Z1]

  Z2:
    type: corollary
    title: zero-set rigidity
    critical: true
    depends_on: [T7]

  Z3:
    type: definition
    title: singular arithmetic expression space
    critical: true
    depends_on: [C2, E1]

  Z4:
    type: example
    title: isolated-zero model
    critical: false
    depends_on: [T6, T7, Z3]

  Z5:
    type: definition
    title: smooth parameter family and total zero set
    critical: false
    depends_on: [C2, Z3]

  T8:
    type: proposition
    title: regular total-zero-set theorem
    critical: false
    depends_on: [Z5]

  Z6:
    type: warning
    title: properness and tube boundary
    critical: true
    depends_on: [T8]

  Z7:
    type: example
    title: minimal multi-zero example
    critical: false
    depends_on: [T7, Z3]

  G1:
    type: definition
    title: ACS charge map and path
    critical: true
    depends_on: [C0, T3]

  T9:
    type: proposition
    title: ACS evaluation formula
    critical: true
    depends_on: [G1, T3]

  G2:
    type: definition
    title: scale-compatible histories
    critical: true
    depends_on: [A3, T9]

  G3:
    type: definition
    title: charge-compatible histories
    critical: true
    depends_on: [G1]

  T10:
    type: proposition
    title: relative torsion independence
    critical: true
    depends_on: [A3, G2, T9]

  T11:
    type: proposition
    title: boundary-integral formula
    critical: true
    depends_on: [G1, G3, T10]

  T12:
    type: theorem
    title: weighted torsion-Stokes theorem
    critical: true
    depends_on: [T11]

  K1:
    type: definition
    title: arithmetic contact form
    critical: true
    depends_on: [C2, F2]

  T13:
    type: proposition
    title: contact nondegeneracy
    critical: true
    depends_on: [C2, K1]

  K2:
    type: definition
    title: horizontal lifts
    critical: true
    depends_on: [K1]

  T14:
    type: proposition
    title: Legendrian realization of flow
    critical: true
    depends_on: [K2, T5]

  T15:
    type: theorem
    title: horizontal curvature bracket
    critical: true
    depends_on: [C2, K2]

  K3:
    type: proposition
    title: exact finite commutator formulas
    critical: false
    depends_on: [C0, K2, T15]

  K4:
    type: definition
    title: horizontal covariant differential
    critical: true
    depends_on: [K1, K2]

  T16:
    type: proposition
    title: horizontal differential curvature
    critical: true
    depends_on: [K4, T15]

  T17:
    type: theorem
    title: local-global torsion synthesis
    critical: true
    depends_on: [A4, K3, T12, T15, T16]
```

---

# Part XVI. Topological implementation order

## 71. Required implementation sequence

A valid topological implementation order is:

```text
1.  C0, C1, C2
2.  S1
3.  S2
4.  T1
5.  S3
6.  S4
7.  P1
8.  P2
9.  T2
10. P3
11. P4
12. A1
13. T3
14. T4
15. A3
16. A4
17. F1
18. T5
19. F2
20. E1
21. F3
22. E2
23. T6
24. Z1
25. T7
26. Z2
27. Z3
28. G1
29. T9
30. G2
31. G3
32. T10
33. T11
34. T12
35. K1
36. T13
37. K2
38. T14
39. T15
40. K4
41. T16
42. K3
43. T17
```

Supporting and optional nodes may be inserted after their prerequisites:

```text
S5, P5, A2, F4, F5, E3, E4, E5, E6, Z4, Z5, T8, Z6, Z7.
```

---

# Part XVII. Audit obligations

## 72. Dependency audit questions

For every theorem or proposition, the audit must answer:

1. Are all symbols defined before the statement?
2. Are all hypotheses inherited explicitly?
3. Is the result local or global?
4. Does it require ordinary or projective admissibility?
5. Does it require (\mu\neq0), (\lambda\neq0), or positivity?
6. Does it require a metric?
7. Does it require completeness or properness?
8. Does it depend on a convention not yet fixed?
9. Is the proof independent of later-paper material?
10. Is the result used by any earlier node, creating a cycle?

---

## 73. Missing-proof handling

If a required node is not fully proved:

* do not remove the node silently;
* mark its status in `05-mathematical-status.md`;
* list the missing proof obligation;
* prevent downstream nodes from being marked complete;
* use conditional wording in the draft if necessary.

A polished but incomplete proof does not satisfy a dependency.

---

## 74. Change-propagation rule

When a node changes, recheck all descendants.

Examples:

### If C0 changes

Recheck:

* P2;
* T2;
* T3;
* E4–E5;
* G1 and T9–T12;
* K3.

### If the regular AES definition changes

Recheck:

* F3;
* T6;
* T7;
* Z3;
* Paper II imports;
* Paper III imports.

### If the torsion sign convention changes

Recheck:

* A4;
* T10–T12;
* K3;
* T17;
* every ACS figure and example.

### If (\mathfrak E_0) normalization changes

Recheck:

* E3;
* E4;
* E6;
* zero-set examples;
* Paper II operator formulas.

---

# Part XVIII. Exports to later papers

## 75. Paper II export boundary

Paper II may import only completed versions of:

```text
E1  Regular AES
F3  Eikonal equation
T6  Basic hyperbolic model
T7  Regular zero-locus theorem
K1  Contact form
K2  Horizontal lifts
T15 Horizontal curvature bracket
K4  Horizontal covariant differential
T16 Horizontal curvature formula
```

Paper II must add, rather than assume:

* horizontal metric choices beyond Paper I;
* compatible complex structure;
* analytic operator domains;
* adjoints;
* boundary theory;
* arithmetic holomorphicity.

---

## 76. Paper III export boundary

Paper III may import:

```text
E1  Regular AES
T7  Regular zero-locus theorem
Z3  Singular AES
Z5  Parameter-family notation
T8  Regular total-zero-set theorem, if retained
K1–T16 Contact and horizontal structures
```

Paper III must prove:

* discriminant theory;
* proper tube theorems;
* topology change;
* monodromy;
* braid or knot invariance.

---

## 77. Paper IV export boundary

Paper IV may import:

```text
S3  Marked spinal histories
S4  Mirror/reversal/inverse
P2  Projective evaluation
T2  PGL₂ generation
P3  Affine/Borel sector
T3–T4 Affine cocycles
A3  Relative affine defect
G1  ACS
T12 Torsion–Stokes theorem
```

Paper IV must develop:

* history groupoid;
* bivaluation;
* quotient tower;
* projective condensation;
* complexity metrics and cost models.

---

# Part XIX. Completion criterion

## 78. Graph completion test

The theorem dependency graph is satisfied only when:

* every `[CRITICAL]` node has a stable definition or proved statement;
* every strict dependency points backward in the final paper;
* no critical theorem depends on an optional example;
* no Paper II–IV result is used to prove a Paper I result;
* all convention-sensitive formulas have been checked under C0;
* all zero-set statements are checked under C2;
* all ACS signs are checked under one orientation convention;
* T17 distinguishes exact finite identities from infinitesimal correspondences.

---

## 79. Final dependency summary

Paper I has one foundational trunk:

[
\boxed{
\text{sequential tree}
\to
\text{marked history}
\to
PGL_2
\supset
\operatorname{Aff}(1)
\to
\text{cocycle}
\to
\text{flow}.
}
]

From this trunk emerge three largely independent geometric branches:

[
\boxed{
\begin{array}{lll}
\textbf{Model branch:}
&
\text{flow}
\to
\text{regular AES}
\to
\mathfrak E_0
\to
\text{regular zeros};
[2mm]
\textbf{Global branch:}
&
\text{affine cocycle}
\to
\text{ACS}
\to
\text{relative torsion}
\to
\text{weighted area};
[2mm]
\textbf{Local branch:}
&
\text{flow}
\to
\text{contact connection}
\to
\text{horizontal curvature}.
\end{array}
}
]

The paper culminates by joining the global and local branches:

[
\boxed{
\text{history-order defect}
\longleftrightarrow
\text{ACS weighted area}
\longleftrightarrow
\text{contact curvature},
}
]

with exact finite identities and infinitesimal correspondences stated separately.

---

## 81. Arithmetic--automorphic extension nodes

The following nodes extend the closed Paper I graph without changing its internal
proof order.

```text
P1-H1  Paper I projective arithmetic contexts T_s and J
P1-H2  q=4 Hecke subgroup identification
P1-Z9  complete boundaryless regular-AES splitting

P2-A1  planar harmonic AES target
P2-A2  cylindrical AES target
P2-A3  holomorphic local-diffeomorphism pullback

P3-S1  critical-point essentiality
P3-S2  2m-prong / 2 pi m cone theorem
P3-S3  normalized (2,4,infinity) Hauptmodul input
P3-S4  exact Hecke zero-dessin AES

P3-K1  sign-cover signature and coarse cylindrical completion
P3-K2  hyperbolic unit-tangent sign cover as S3 minus T(2,4)
P3-K3  primitive Hecke classes and periodic-orbit knots
P3-K4  zero-dessin coding spine and template boundary

P3-R1  relative prime-divisor normalization
P3-R2  arithmetic/geometric irreducibility separation
P3-R3  history-to-divisor naturality [RESTRICTED MODEL PROVED; GENERAL OPEN]
P3-R4  quadratic supplied-register divisor, collapse kernel, and Frobenius
P3-R5  quartic arithmetic/geometric splitting and Frobenius test

P3-H1  polynomial carrier and intrinsic root thread
P3-H2  quadratic threaded-carrier topology and torus-link thread
P3-H3  discriminant--framing--braid--Euler identity
P3-H4  q=4 marked peripheral toric binomial
P3-H5  q=4 logarithmic-tangent weighted cone and cusp link
P3-H6  supplied four-strand braid-center and LHS-transgression calibration
P3-H7  unrestricted history-to-coefficient-path naturality [OPEN]

P3-L1  supplied sextic event-polynomial calculation
P3-L2  regular sextic LL cover: 1296 normalized sheets / 216 rotation orbits
P3-L3  caustic-cubed / Maxwell-squared bifurcation divisor
P3-L4  displayed spanning-star surjection onto B6
P3-L5  compatible carrier, six-root thread, and genus-two mapping torus
P3-L6  genus-two mapping-class and symplectic monodromy specialization
P3-L7  mixed-braid exact sequence and LL pullback
P3-L8  displayed arithmetic fiber: S6 Galois and geometric End = Z
P3-L9  explicit geometric LL--Igusa twin; spectral descent, forgetting variance,
       and balanced moving-slice divisor charge [PROVED]
P3-L10 full 216-orbit census; arithmetic/period/marked/Hodge-energy refinements [OPEN]
```

The new dependency edges are:

```text
P1-H1 -> P1-H2
T7 regular zero theorem -> P1-Z9
complete metric + boundaryless carrier -> P1-Z9
P1-H2 -> P3-S3

P2-A1 -> P2-A3
P2-A2 -> P2-A3
P2-A3 -> P3-S1 -> P3-S2
P2-A3 -> P3-S4
P3-S3 -> P3-S4

P3-S4 -> P3-K1
P3-K1 + classical lens-space input -> P3-K2
P1-H2 -> P3-K3
P3-S4 + classical geodesic coding -> P3-K4

P3-R1 -> P3-R2
P1-H2 + supplied quadratic register -> P3-R4
P3-R1 + supplied quartic registers -> P3-R5
P3-R4 -. restricted naturality evidence .-> P3-R3
P3-R5 -. finite arithmetic test .-> P3-R3

P2-A3 -> P3-H1 -> P3-H2
P3-H1 -> P3-H3
P3-K2 -> P3-H4 -> P3-H5
P3-K1 -> P3-H5
P1-H2 + braid-center input -> P3-H6
P3-H4 -. marked toric evidence .-> P3-H7
P3-H5 -. logarithmic-cone evidence .-> P3-H7
P3-H6 -. extension-class evidence .-> P3-H7

supplied P0 + direct discriminant calculation -> P3-L1
classical LL theorem + normalized sextic space -> P3-L2
classical LL local bifurcation models -> P3-L3
P3-L1 + classical local half-twist input -> P3-L4
P3-H1 + P3-L1 + collision-free loop -> P3-L5
P3-L4 + classical Birman--Hilden/symplectic input -> P3-L6
P3-L2 + mixed configuration-space extension -> P3-L7
P3-L4 -> P3-L7
supplied arithmetic fiber + classical Galois/Zarhin criteria -> P3-L8
P3-L2 + exact sparse resultant + Clebsch invariant -> P3-L9
P3-L2 + finite-etale quotient + sheet observable -> P3-L9
P3-L9 + moving t-slices -> P3-L9 divisor charge
P3-L9 -. existence input for deeper census .-> P3-L10
P3-L7 -. typed path target evidence .-> P3-H7
```

The dotted edges do not authorize a theorem.  In particular, `P3-R3` is not a
dependency for `P3-S4`: the exact Hecke model is constructed from the operator
subgroup and its standard Hauptmodul without a general history functor.

## 82. Status and non-implication gates

* `P1-H2` is proved by an elementary matrix calculation and a cited standard Hecke
  group identification.
* `P1-Z9` is proved by rectifying the assignment, completeness of bounded vector
  fields on a complete Riemannian manifold, and the global flow map.  It gives only
  a diffeomorphic product, not an isometric splitting.
* `P2-A1`--`P2-A3` are direct analytic calculations on the regular locus.
* `P3-S1`--`P3-S2` are local calculations in the singular-AES category.
* `P3-S3` is an external standard uniformization input and must be cited.
* `P3-S4` is an AEG construction proved conditional on the normalized input.
* `P3-R1`--`P3-R2` are standard relative-divisor facts with hypotheses stated.
* `P3-K1` is proved from the explicit sign character and the Hauptmodul--Cayley
  coordinate.  Its coarse flat cylinder is not the hyperbolic unit tangent bundle.
* `P3-K2` combines an explicit index-two cover and slope calculation with the cited
  classical lens-space compactification.  The upstairs local cone angle is not a
  torus-link invariant.
* `P3-K3`--`P3-K4` specialize cited geodesic-flow coding theorems and prove the
  object-type identifications needed here.  They produce no new knot invariant.
* `P3-R4`--`P3-R5` are proved for explicitly supplied typed registers.  They test
  divisor equivariance, collapse, irreducibility, monodromy, and Frobenius without
  deriving those registers from unrestricted histories.
* `P3-R3` is therefore partially resolved in the restricted models, while the
  general history-to-divisor functor remains open and cannot support a general
  naturality or faithfulness claim.
* `P3-L1`, `P3-L4`, `P3-L5`, and `P3-L7` are proved for the supplied sextic and
  the printed loop/configuration hypotheses.  They do not define a construction
  on unrestricted histories.
* `P3-L2`, `P3-L3`, `P3-L6`, and `P3-L8` are classical results or criteria
  specialized and audited in the sextic laboratory.  The (1296) normalized LL
  sheets and their (216) source-rotation orbits are not counts of nonisomorphic
  curves.
* `P3-L9` is proved by the displayed exact second sheet: equality of the LL
  event polynomial follows from an exact resultant and scaling identity, while
  a distinct absolute Igusa--Clebsch ratio at (t=1) proves that the two curves
  are not isomorphic over (\mathbb C).  On the degree-(216) quotient cover,
  finite-flat norm descent gives the spectral polynomial and permutation
  averaging gives the canonical constant/zero-sum exact sequence and
  monodromy-invariant variance.  The twin supplies its exact positive lower
  bound.  Along the two explicit slice pencils, the same invariant ratio has
  divisor (5[\beta]-5[0]) at regular fibers.
* `P3-L10` remains open.  The theorem does not enumerate all (216) rotation
  orbits, compare Frobenius polynomials or reduced Siegel periods, or fix and
  quotient marked local symplectic monodromy/Hurwitz data.  It also does not
  construct a Hodge- or Siegel-metric energy.
* The P3-L9 variance is invariant under the permutation monodromy of a closed
  loop but need not be constant along an arbitrary open path of event
  polynomials.  The moving-slice divisor is a balanced logarithmic charge, not a
  finite Dirichlet energy.
* The solid edge into `P3-L7` is a pullback of the mixed braid extension.  It is
  not, and must not be redrawn as, a homomorphism (B_5\to B_6) after the LL sheet
  is forgotten.
* The dotted edge from `P3-L7` to `P3-H7` records a typed target for a future
  history functor, not existence or naturality of that functor.

The following implications are forbidden:

```text
Hecke subgroup generation =/=> histories are tiles
rich zero dessin          =/=> history-derived arithmetic divisor
local four-prong cone      =/=> the global T(2,4) link
bare zero dessin           =/=> the three-dimensional flow template
primitive Hecke element    =/=> prime knot
terminal endpoint divisor  =/=> marked-history faithfulness
arithmetic divisor        =/=> proper zero tube
singular zero tube        =/=> Markov invariant
1296 normalized LL sheets =/=> 1296 nonisomorphic genus-two curves
216 source-rotation orbits =/=> 216 nonisomorphic genus-two curves
critical-value braid      =/=> unmarked B5-to-B6 homomorphism
common Sp4(F2) = S6 target =/=> Frobenius/topological-loop identification
full B6 monodromy         =/=> new knot invariant.
```
