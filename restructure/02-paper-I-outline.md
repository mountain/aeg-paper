# Paper I Detailed Outline

**File:** `restructure/02-paper-I-outline.md`
**Status:** Authoritative
**Version:** 1.1
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `restructure/00-authoritative-scope.md`
* `restructure/01-paper-series-architecture.md`

**Applies to:**
**Arithmetic Expression Geometry I: Foundations**

---

## 1. Purpose of this document

This document fixes the target structure of Paper I at the level of:

* sections and subsections;
* definitions and theorem slots;
* logical dependencies;
* required examples;
* source-material migration;
* exclusions;
* validation criteria.

It is the authoritative chapter-level specification for the current
`paper-1/aeg-paper-1.tex`.

It does not determine the final wording of the paper. It determines what the paper must establish, in what dependency order, and what material must be moved elsewhere.

---

# Part I. Paper identity

## 2. Provisional title

### Main title

**Arithmetic Expression Geometry I: Foundations**

### Recommended subtitle

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

Alternative subtitle:

**From Arithmetic Histories to Affine Geometry**

The title must not imply that Paper I develops the full projective, analytic, singular, or computational theory.

---

## 3. Intended audience

The paper should be readable by mathematicians with background in some combination of:

* algebra;
* differential geometry;
* geometric group theory;
* dynamical systems;
* formal languages or rewriting;
* contact geometry.

The paper must not assume prior knowledge of AEG.

All AEG-specific terms must be defined from first principles.

---

## 4. Central thesis

Paper I establishes the following chain:

[
\boxed{
\text{sequential expression syntax}
\longrightarrow
\text{marked arithmetic histories}
\longrightarrow
\text{projective operator semantics}
\supset
\text{affine/Borel sector}
}
]

[
\boxed{
\text{affine sector}
\longrightarrow
\text{cocycles and flow}
\longrightarrow
\text{hyperbolic realization}
\longrightarrow
\text{torsion and contact curvature}.
}
]

The paper should defend the following central statement:

> Arithmetic expressions with a sequential dependency structure can be treated as marked histories rather than merely as trees with endpoint values. Their non-degenerate bilateral one-hole contexts act projectively on (\mathbb P^1(K)) and generate (PGL_2(K)). The previously developed continuous AEG theory is the affine/Borel sector of this projective semantics. Within that sector, arithmetic histories carry natural cocycles, an infinitesimal flow, a hyperbolic realization, global torsion formulas, regular zero-set structure, and a contact connection whose curvature records local noncommutativity.

---

## 5. Main mathematical contributions

The final paper should present the following as its principal contributions.

1. **Sequential-tree classification.**

   A binary expression tree has a unique legal internal evaluation order if and only if its internal nodes form a single spine.

2. **Marked spinal-history formalism.**

   Sequential trees are converted into histories of one-hole contexts with explicit operand-slot data.

3. **Projective completion theorem.**

   Non-degenerate bilateral arithmetic contexts generate (PGL_2(K)).

4. **Affine-sector identification.**

   The existing AEG add–multiply theory is identified with the affine/Borel subgroup stabilizing a point at infinity.

5. **Affine cocycle formulas.**

   Target-frame and source-normalized translation coordinates are derived and distinguished.

6. **Continuous affine flow.**

   The arithmetic flow equation is derived from the affine Lie algebra.

7. **Basic hyperbolic realization.**

   The model (\mathfrak E_0) is derived and verified as a regular arithmetic expression space.

8. **Regular zero-locus theorem.**

   Under the non-degenerate flow equation, zero sets are smooth codimension-one submanifolds.

9. **Singular-AES foundation.**

   Singular assignment functions and singular zero sets are given a precise initial definition.

10. **Generalized affine torsion theorem.**

    The ACS comparison is extended from path-versus-reversal to compatible pairs of histories.

11. **Contact-curvature theorem.**

    The local horizontal distribution has curvature proportional to (\mu\lambda), reproducing infinitesimal arithmetic torsion.

---

## 6. Claims intentionally not made

Paper I must not claim that:

* all arithmetic expression trees are sequential;
* all arithmetic histories are affine;
* projective continuation is equivalent to ordinary arithmetic evaluation;
* the affine flow is the full projective flow;
* every AES is hyperbolic;
* the basic hyperbolic model is unique;
* noncommutativity implies hyperbolicity;
* hyperbolicity implies computational hardness;
* the contact form uniquely determines a complex structure;
* arithmetic holomorphicity is already a complete function theory;
* every multi-zero construction produces a tube or knot;
* regular parameter families are globally topologically trivial without properness.

---

# Part II. Global narrative

## 7. Recommended section sequence

The target Paper I should have the following main structure:

```text
1. Introduction
2. Sequential Arithmetic Histories
3. Projective Semantics and the Affine Sector
4. Affine Cocycles and Relative Defects
5. Continuous Arithmetic Flow
6. The Basic Hyperbolic Expression Space
7. Zero Loci and Singular Expression Spaces
8. Global Torsion and the Accumulative Commutative Space
9. Contact Connection and Horizontal Curvature
10. Conclusions and Research Interfaces
```

Recommended appendices:

```text
Appendix A. Conventions for chronological composition and matrix actions
Appendix B. Supplementary affine-cocycle calculations
Appendix C. Hyperbolic-model calculations
Appendix D. Supplementary ACS and contact computations
Appendix E. Examples separating equality and neutrality levels
```

---

## 8. High-level dependency order

The internal theorem dependency is:

```text
Sequential-tree classification
        ↓
Marked spinal histories
        ↓
Projective evaluation of contexts
        ↓
PGL2 generation
        ↓
Affine/Borel restriction
        ↓
Affine cocycle formulas
        ↓
Continuous affine flow
       ↙ ↓ ↘
Hyperbolic model   ACS torsion   Contact connection
       ↓                              ↓
Regular zero theorem            Curvature theorem
```

No chapter may use a concept before its defining chapter unless the use is explicitly prospective.

---

# Part III. Detailed chapter outline

# 1. Introduction

## 1.1 Purpose

Introduce the problem:

> Ordinary evaluation sends an expression to a value and discards the path by which the value was produced. AEG studies the retained evaluation history and asks what algebraic and geometric structures are carried by that history.

The introduction must explain why the paper begins with sequential trees rather than arbitrary expression trees.

---

## 1.2 The process-to-result hierarchy

Introduce the hierarchy:

[
\text{tree}
\longrightarrow
\text{marked history}
\longrightarrow
\text{operator}
\longrightarrow
\text{endpoint value}.
]

Explain that each arrow forgets information.

Do not yet introduce the full condensation theory of Paper IV.

---

## 1.3 Why bilateral completion matters

State briefly:

* existing AEG used a constant-chirality affine language;
* allowing the accumulator to occupy either operand slot yields projective transformations;
* the affine theory is not invalidated but correctly located as a Borel sector.

The introduction should state the projective-completion result without developing its proof.

---

## 1.4 What Paper I establishes

Give a concise theorem-level summary:

* sequential syntax;
* projective placement;
* affine cocycles;
* continuous flow;
* hyperbolic realization;
* regular zeros;
* global torsion;
* contact curvature.

---

## 1.5 What Paper I does not establish

Name the later-paper interfaces:

* horizontal and hyperbolic function theory: Paper II;
* multi-zero singularities and tubes: Paper III;
* projective condensation and complexity: Paper IV.

These statements must be framed as scope boundaries, not as claims that the future theories are already complete.

---

## 1.6 Historical and mathematical placement

Retain a restrained discussion of:

* formal generation and rewriting;
* affine and projective group actions;
* Hamilton–Jacobi-type first-order equations;
* hyperbolic geometry;
* Pfaffian and contact structures;
* Stokes-type identities.

Do not claim that AEG is a direct application of any one of these traditions.

---

## 1.7 Structure of the paper

Give a one-paragraph chapter guide matching the final structure.

---

## Required output of Chapter 1

The reader should understand:

1. what information AEG retains;
2. why sequential histories are the first tractable class;
3. why the affine theory sits inside a projective completion;
4. what the paper proves;
5. where the later research programs begin.

---

## Existing source material

Primary sources:

* `sections/sec01.tex`
* abstract and introduction in `paper-1/aeg-paper-1.tex`
* selected introductory material from `notes/bilateral_projective_condensation.tex`

---

## Required changes

* Rewrite the current list of contributions.
* Remove the claim that contact geometry directly forces a complete function theory.
* Replace the existing linear narrative ending in arithmetic holomorphicity with the new foundational narrative ending in contact curvature and zero-set boundaries.
* State the affine/projective relationship at the beginning.

---

# 2. Sequential Arithmetic Histories

## 2.1 Arithmetic expression trees

Define arithmetic expressions over a field or specified coefficient set.

Recommended initial algebraic setting:

[
K
]

a field, with ordinary arithmetic domains explicitly restricted when division is used.

Define:

* leaves;
* internal vertices;
* operation labels;
* evaluation dependency;
* legal evaluation order.

The paper may initially describe ordinary rational expressions for intuition, but theorem statements should use the appropriate general field assumptions.

---

## 2.2 Dependency poset

For an expression tree (T), define:

[
I(T)
]

as the set of internal vertices, ordered by dependency.

A vertex (u) precedes (v) if the output of (u) is required before evaluating (v).

---

## 2.3 Sequential-tree classification

### Theorem slot

**Theorem: Sequential-tree classification**

For a finite binary expression tree (T), the following are equivalent:

1. (I(T)) has a unique linear extension;
2. (I(T)) is a chain;
3. every internal vertex has at most one internal child;
4. the internal vertices form a single spine.

The proof must be included in the main text.

---

## 2.4 Marked accumulator

Explain why an unmarked innermost binary node does not uniquely determine which leaf is the evolving state.

Define a marked initial accumulator.

This marking converts a sequential tree into a history of one-hole contexts.

---

## 2.5 One-hole arithmetic contexts

Define:

[
C_{\omega,c}^{(1)}[z]
=====================

\omega(z,c),
]

[
C_{\omega,c}^{(2)}[z]
=====================

\omega(c,z).
]

Define a marked spinal history:

[
\gamma
======

\bigl(
x_0;
(\omega_i,c_i,\varepsilon_i)_{i=1}^{n}
\bigr).
]

Define the chirality word:

[
\varepsilon(\gamma)
===================

\varepsilon_1\cdots\varepsilon_n.
]

---

## 2.6 Free and bounded histories

Define:

* free history;
* bounded history;
* initial state;
* chronological composition;
* admissibility.

Fix the convention:

[
\nu_x(\gamma)
=============

g_n\circ\cdots\circ g_1(x).
]

---

## 2.7 Mirror, reversal, and inverse

Define separately:

* mirror (m\gamma);
* temporal reversal (r\gamma);
* path inverse (\gamma^{-1}), when defined.

Include a small example showing:

[
m\gamma\neq r\gamma.
]

State explicitly that existing affine torsion is an order-comparison effect and not automatically a mirror invariant.

---

## 2.8 Levels of equality

Retain and sharpen the current hierarchy:

1. literal equality;
2. marked-history equality;
3. operator equality;
4. charge equality;
5. endpoint equality;
6. quotient or relational equality.

Do not develop full relation or loop theory.

---

## 2.9 Examples

Required examples:

1. a non-sequential branching expression;
2. a pure slot-(1) history;
3. a pure slot-(2) history;
4. a mixed chirality history;
5. mirror versus temporal reversal;
6. two distinct histories with the same endpoint value.

---

## Required output of Chapter 2

The chapter must produce one stable foundational object:

[
\boxed{\text{marked spinal history}.}
]

All later chapters must use this object rather than the ambiguous previous definition of “threadlike expression.”

---

## Existing source material

Primary sources:

* `sections/sec02-00.tex`
* `sections/sec02-01.tex`
* `notes/bilateral_projective_condensation.tex`

---

## Material to remove or replace

* Replace the existing left-child/right-child definition.
* Avoid ambiguous “left-expanded” and “right-expanded” terminology unless accompanied by slot notation.
* Move extensive loop and neutrality discussion to an appendix or future work.

---

# 3. Projective Semantics and the Affine Sector

## 3.1 Ordinary and projective semantics

Define:

[
\mathbb P^1(K)=K\cup{\infty}.
]

Explain that non-degenerate one-hole contexts act by fractional linear transformations.

Distinguish:

* ordinary arithmetic admissibility;
* projective continuation;
* poles;
* chart transitions;
* constant or degenerate maps.

---

## 3.2 Matrix representatives of elementary contexts

Provide a table for:

* (z\mapsto z+c);
* (z\mapsto z-c);
* (z\mapsto c-z);
* (z\mapsto cz);
* (z\mapsto z/c);
* (z\mapsto c/z).

State invertibility assumptions.

---

## 3.3 Projective evaluation map

Define:

[
\rho:
\operatorname{Hist}^{\pm,\times}_K
\longrightarrow
PGL_2(K).
]

State the chronological matrix-composition convention.

---

## 3.4 Bilateral generation theorem

### Theorem slot

**Theorem: Bilateral arithmetic generates (PGL_2(K))**

Show that translations, nonzero scalings, and Weyl inversion generate all fractional linear transformations.

Use an explicit decomposition such as:

[
\frac{Az+B}{Cz+D}
=================

T_{A/C}
\circ
D_{(AD-BC)/C^2}
\circ
J
\circ
T_{D/C}
]

when (C\neq0).

Handle (C=0) separately.

---

## 3.5 Affine/Borel sector

### Corollary slot

Show that restricting to the affine-compatible contexts gives:

[
B_\infty
========

\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

State precisely which restricted history language maps to this subgroup.

---

## 3.6 The (q=4) Hecke arithmetic sublanguage

Over (K=\mathbb Q(\sqrt2)), isolate the projective contexts

[
T(z)=z+\sqrt2,
\qquad
J(z)=-1/z.
]

Prove the matrix relation (J^2=(JT)^4=1) in the projective group and cite the
standard identification of their image with the (q=4) Hecke triangle group.
Record the factorization

[
\text{marked history}
\longrightarrow G_4
\longrightarrow G_4/H_{\mathcal C}
]

for a chosen cell stabilizer.  Neither arrow is generally injective.  Ordinary
arithmetic admissibility at a real seed remains separate from the projective
Fuchsian action.

---

## 3.7 Positive real sector

Explain that the current continuous parameterization:

[
z\mapsto e^\lambda z
]

with (\lambda\in\mathbb R) covers positive real scaling.

Thus the differential-geometric theory developed later corresponds to:

[
\operatorname{Aff}^{+}(1,\mathbb R),
]

not automatically to all of (\operatorname{Aff}(1,\mathbb R)).

---

## 3.8 Bruhat placement

A concise remark may state:

[
PGL_2(K)=B\sqcup BJB.
]

Interpret bilateral completion as the rank-one Bruhat completion of the affine sector.

Do not develop representation theory beyond what is needed for placement.

---

## 3.9 Riccati outlook

State without full development that the Lie algebra of projective vector fields includes:

[
\partial_z,\qquad
z\partial_z,\qquad
z^2\partial_z.
]

Thus the general projective flow has the form:

[
\dot z
======

\beta+\alpha z+\kappa z^2.
]

The affine theory developed in Paper I is the slice:

[
\kappa=0.
]

---

## Required output of Chapter 3

The reader should understand:

[
\boxed{
\text{current AEG}
==================

\text{a natural affine/Borel sector of bilateral projective arithmetic}.
}
]

---

## Existing source material

Primary source:

* `notes/bilateral_projective_condensation.tex`

Supporting source:

* affine-group material from `sections/sec02-01.tex`
* matrix-Lie material from `sections/sec03.tex`

---

## Material excluded from this chapter

Move to Paper IV:

* bivaluation;
* rank-one projector theorem;
* (G/H);
* (G/B_\pm);
* process-result bundle;
* concept–predicate semantics;
* finite-field quotient counts;
* projective condensation.

---

# 4. Affine Cocycles and Relative Defects

## 4.1 Affine history evaluation

For affine contexts:

[
f_i(x)=s_i x+t_i,
\qquad s_i\in K^\times,
]

define:

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n.
]

---

## 4.2 Target-frame cocycle

### Proposition slot

Prove:

[
\Phi_n
======

\prod_{i=1}^n s_i,
]

[
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j.
]

Interpret each additive event as weighted by all future scales.

---

## 4.3 Source-normalized cocycle

Define:

[
\widehat\xi_n
=============

\Phi_n^{-1}\xi_n.
]

Prove:

[
\widehat\xi_n
=============

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

Interpret each additive event as normalized by accumulated past scale.

---

## 4.4 Left and right Maurer–Cartan readings

For:

[
g=
\begin{pmatrix}
e^\lambda & \xi\
0&1
\end{pmatrix},
]

derive:

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

Explain source/body and target/spatial readings.

Do not identify these with operand-slot chirality.

---

## 4.5 Relative affine defect

For two affine histories:

[
\rho(\gamma)(x)=\Phi_\gamma x+\xi_\gamma,
]

[
\rho(\delta)(x)=\Phi_\delta x+\xi_\delta,
]

define a relative comparison.

When:

[
\Phi_\gamma=\Phi_\delta,
]

the endpoint difference is independent of (x):

[
\nu_x(\gamma)-\nu_x(\delta)
===========================

\xi_\gamma-\xi_\delta.
]

Also record the normalized relative affine transformation:

[
\rho(\delta)^{-1}\rho(\gamma).
]

---

## 4.6 Elementary torsion as a cocycle defect

Recover:

[
(x+\mu)e^\lambda
----------------

# (xe^\lambda+\mu)

\mu(e^\lambda-1).
]

Interpret this as the elementary affine translation defect.

---

## 4.7 Perturbation propagation

Retain the useful perturbation formula for alternating histories:

[
\frac{\alpha(\widetilde x)-\alpha(x)}
{\widetilde x-x}
================

\Phi_\alpha.
]

This should be presented as a direct consequence of affine evaluation rather than as an independent theory.

---

## Required output of Chapter 4

The chapter must establish that the weighting kernels later appearing in ACS are not inserted geometrically by hand. They are forced by the affine cocycle.

---

## Existing source material

Primary sources:

* `sections/sec02-01.tex`
* `sections/sec03.tex`
* `notes/bilateral_projective_condensation.tex`

---

## Material to move

Move extensive free-group, loop, and condensation interpretation to Paper IV.

---

# 5. Continuous Arithmetic Flow

## 5.1 From discrete histories to infinitesimal generators

Introduce local coordinates:

[
(u,v),
]

representing additive and multiplicative directions.

Fix real parameters:

[
\mu,\lambda.
]

Explain the limiting transition from:

[
a\mapsto a+\mu,du,
]

[
a\mapsto e^{\lambda,dv}a.
]

---

## 5.2 Affine Lie algebra derivation

Use:

[
E=\partial_a,
\qquad
H=a\partial_a.
]

For a direction:

[
\Omega(\theta)
==============

\mu\cos\theta,E
+
\lambda\sin\theta,H,
]

derive:

[
\frac{da}{ds}
=============

\mu\cos\theta
+
\lambda a\sin\theta.
]

The Lie-theoretic derivation should be primary.

The two-order Taylor expansion may remain as intuition or a supplementary check.

---

## 5.3 Pfaffian form

Write:

[
da
==

\mu,du
+
\lambda a,dv.
]

State clearly that this relation describes admissible horizontal propagation and is not globally integrable over the entire three-dimensional state space.

---

## 5.4 Directional solutions

For fixed (\theta), solve:

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

Include the special additive and multiplicative directions.

---

## 5.5 Gradient and eikonal form

After introducing a compatible orthonormal frame, derive:

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2.
]

Clarify that this equation depends on the metric choice.

---

## 5.6 Rectifying coordinate

Define:

[
r(a)
====

\operatorname{arcsinh}
\left(
\frac{\lambda a}{\mu}
\right)
]

under appropriate assumptions.

Show that along gradient trajectories:

[
|\nabla r|
==========

|\lambda|.
]

Handle signs and cases (\mu=0) or (\lambda=0) separately or exclude them explicitly.

---

## 5.7 Local torsion density

Compare infinitesimal add–multiply orderings and obtain:

[
d\tau
=====

\mu\lambda,du,dv
+
\text{higher-order terms}.
]

State that this is an infinitesimal formula, not the exact finite formula.

---

## 5.8 Affine versus Riccati flow

Close the chapter with the placement:

[
\dot z
======

\beta+\alpha z
]

inside:

[
\dot z
======

\beta+\alpha z+\kappa z^2.
]

---

## Required output of Chapter 5

The chapter must provide one clear, convention-controlled derivation of the flow equation.

It must not present several incompatible derivations without identifying their relation.

---

## Existing source material

Primary source:

* `sections/sec03.tex`

Supporting source:

* `notes/bilateral_projective_condensation.tex`

---

## Material to reduce

* Compress extended contour-angle algebra if it interrupts the main logic.
* Move repetitive coordinate calculations to an appendix.
* Retain only formulas used later.

---

# 6. The Basic Hyperbolic Expression Space

## 6.1 From the affine group to a homogeneous surface

Identify:

[
\operatorname{Aff}^{+}(1,\mathbb R)
]

with a two-dimensional solvable Lie group.

Choose a normalized invariant metric in which additive and multiplicative generator directions have specified lengths.

Derive a coordinate form such as:

[
g_{\mu,\lambda}
===============

e^{-2\lambda v}
\frac{du^2}{\mu^2}
+
dv^2.
]

---

## 6.2 Upper-half-plane form

Transform to coordinates ((x,y)) and obtain:

[
g_{\mu,\lambda}
===============

\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right).
]

Define:

[
a(x,y)
======

-\frac{x}{y}.
]

---

## 6.3 Verification theorem

### Theorem slot

**Theorem: Basic hyperbolic AES**

Prove:

[
|\nabla a|*{g*{\mu,\lambda}}^2
==============================

\mu^2+\lambda^2a^2.
]

Define:

[
\mathfrak E_0(\mu,\lambda)
==========================

(\mathcal H,g_{\mu,\lambda},a).
]

State all assumptions.

---

## 6.4 Curvature and normalization

Compute the Gaussian curvature.

Explain which parameter controls:

* curvature scale;
* additive unit;
* coordinate normalization.

Avoid overclaiming uniqueness.

---

## 6.5 Horocyclic geometry

Describe:

* horocycles;
* orthogonal geodesics;
* level sets of multiplicative coordinate;
* assignment contours.

Explain how addition and multiplication act geometrically.

---

## 6.6 Arithmetic grid

Define finite transformations implementing:

[
a\mapsto a+s,
]

[
a\mapsto ka.
]

Verify them directly.

---

## 6.7 Baumslag–Solitar relation

Retain the exact relation when correctly formulated:

[
Y_k^{-1}X_s^{,k}Y_k=X_s,
]

or the conventionally equivalent form.

Check composition order carefully.

State that the relation is realized by the grid action.

Do not infer computational complexity from it.

---

## 6.8 Laplace eigenfunction

Compute the appropriate Laplace–Beltrami operator and prove the eigenvalue relation for (a).

State sign convention for (\Delta).

---

## 6.9 Local area interpretation

Retain the staircase examples only as illustrations of the local torsion-area principle.

The global theorem belongs to Chapter 8.

---

## Required output of Chapter 6

The basic hyperbolic model must appear as a structured realization of the affine theory, not as an isolated ansatz.

---

## Existing source material

Primary source:

* `sections/sec04.tex`

Supporting sources:

* `sections/sec02-00.tex`
* `sections/sec03.tex`
* `notes/note_06.tex`

---

## Material to move

Move to Paper III:

* general parameter-family tube speculation;
* general (E_k) discussion;
* multi-zero classifications.

---

# 7. Zero Loci and Singular Expression Spaces

## 7.1 Regular zero sets

For a regular AES satisfying:

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2,
]

show that on:

[
Z(a)=a^{-1}(0),
]

one has:

[
|\nabla a|
==========

|\mu|.
]

---

## 7.2 Regular-zero theorem

### Theorem slot

**Theorem: Regular zero locus**

If (\mu\neq0), then (0) is a regular value of (a).

Therefore:

[
Z(a)
]

is a smooth codimension-one submanifold.

For a two-dimensional AES, it is a disjoint union of smooth curves.

---

## 7.3 Consequences

Record explicit corollaries:

* no isolated regular zero;
* no regular crossing;
* no regular branching;
* no regular interior endpoint;
* no regular birth or death inside a fixed smooth non-degenerate model.

Each statement must be formulated under the correct hypotheses.

---

## 7.4 Complete regular splitting

For a connected, complete, boundaryless regular AES, define

[
r(a)=\int_0^a\frac{ds}{\sqrt{\mu^2+\lambda^2s^2}}.
]

Prove that (|\nabla r|=1), that its gradient field has a complete flow, and that

[
Z(a)\times\mathbb R\longrightarrow M,
\qquad
(q,t)\longmapsto\Phi_t(q)
]

is a diffeomorphism.  State explicitly that this need not be a Riemannian product.
Conclude that (a) is surjective and (Z(a)) is nonempty and connected.  Explain
why a boundary or incomplete metric invalidates the global-flow proof.

---

## 7.5 Singular arithmetic expression spaces

Define a singular AES:

[
(\mathcal M,S,g,a;\mu,\lambda),
]

where the regular equations hold on:

[
\mathcal M\setminus S.
]

Allow singular behavior in:

* (a);
* (g);
* (\mu,\lambda);
* chart structure;
* domain;
* projective continuation.

---

## 7.6 Regular and singular zero sets

Define:

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

Clarify that a point may lie in the zero set but fail to be a regular zero because the function, metric, parameter, or domain is singular.

---

## 7.7 The isolated-zero model

Reassess the current model denoted (\mathfrak E_1).

Required treatment:

1. state its domain;
2. state whether the center is included;
3. state whether (a) is smooth there;
4. state whether the metric is regular there;
5. state where the flow equation holds;
6. classify the center as a singular zero.

Do not present it as a regular AES with an isolated zero.

---

## 7.8 Minimal multi-zero example

Include only if fully verified.

Required checklist:

* explicit domain;
* explicit metric;
* explicit assignment;
* complete singular set;
* flow verification;
* exact zero topology.

If no example passes this checklist, omit it from the main body and state the construction problem in the outlook.

---

## 7.9 Parameter families

Let:

[
a_t:\mathcal M\to\mathbb R,
]

and define:

[
A(p,t)=a_t(p).
]

Define:

[
\mathcal Z=A^{-1}(0).
]

---

## 7.10 Regular total-zero-set lemma

### Proposition slot

If:

[
d_pa_t\neq0
]

at every zero, then:

[
\mathcal Z
]

is a smooth codimension-one submanifold of (\mathcal M\times I).

If (\dim\mathcal M=2), then (\mathcal Z) is a surface.

Do not yet call it a globally trivial tube.

---

## 7.11 Properness warning

State that topology preservation or local triviality of:

[
\pi:\mathcal Z\to I
]

requires additional assumptions such as properness.

The full theorem belongs to Paper III.

---

## Required output of Chapter 7

The chapter must establish the boundary between:

[
\text{regular zero geometry}
]

and:

[
\text{singular multi-zero/tube geometry}.
]

This boundary is one of the central foundational results of Paper I.

---

## Existing source material

Primary source:

* singular and zero-set portions of `sections/sec04.tex`

Supporting sources:

* multi-zero and tube notes, used only for classification and migration;
* recent research summaries under `restructure/discussions/`.

---

## Material to move

Move to Paper III:

* full multi-zero constructions;
* (E_k);
* (E_{\log});
* zero-line bifurcation;
* tube threading;
* braids;
* knots;
* Markov normalization.

---

# 8. Global Torsion and the Accumulative Commutative Space

## 8.1 Purpose of the ACS

Explain that the ACS records total additive and multiplicative charges while forgetting the full noncommutative history.

Define:

[
(A,M).
]

State that it is a commutative shadow, not the full expression space.

---

## 8.2 ACS path

For an affine history (\gamma), define the broken path:

[
C_\gamma.
]

Fix orientation and chronological convention.

---

## 8.3 Evaluation as a weighted path integral

Derive an evaluation formula directly from the affine cocycle.

Choose one canonical orientation convention.

A preferred form is:

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+
\int_{C_\gamma}e^{-M},dA
\right).
]

If the reverse-path formulation is retained, prove its equivalence and explain the change of orientation.

---

## 8.4 Compatible histories

Define two histories (\gamma,\delta) as charge-compatible when they have the same total additive and multiplicative charge, or at minimum the same total multiplicative scale when only endpoint independence is required.

State the exact compatibility condition used by each theorem.

---

## 8.5 Relative torsion

Define:

[
\tau(\gamma,\delta)
===================

\nu_x(\gamma)-\nu_x(\delta).
]

Prove independence from (x) under the stated compatibility condition.

Temporal reversal becomes a special case:

[
\tau(\gamma,r\gamma).
]

---

## 8.6 Boundary-integral theorem

### Proposition slot

Express:

[
\tau(\gamma,\delta)
]

as a weighted contour integral around:

[
C_\gamma-C_\delta.
]

Fix signs explicitly.

---

## 8.7 Weighted-area theorem

### Theorem slot

For an oriented filling:

[
\partial\Sigma_{\gamma,\delta}
==============================

C_\gamma-C_\delta,
]

prove:

[
\tau(\gamma,\delta)
===================

# \oint_{\partial\Sigma_{\gamma,\delta}}\eta

\iint_{\Sigma_{\gamma,\delta}}d\eta.
]

State the one-form (\eta) and orientation convention.

---

## 8.8 Examples

Required examples:

1. one add–multiply square;
2. a four-step staircase;
3. two non-reversed histories with equal total charge;
4. a signed-charge example, if the orientation formalism supports it cleanly.

---

## 8.9 Algebraic interpretation

State briefly that the ACS is related to abelianized charge data.

Do not claim that the entire evaluated affine group is the free group (F_2).

Distinguish:

* free symbolic history;
* evaluated affine operator;
* abelianized charge path.

---

## Required output of Chapter 8

The chapter must establish a precise local-global relation:

[
\boxed{
\text{affine cocycle difference}
================================

# \text{weighted boundary integral}

\text{weighted area}.
}
]

---

## Existing source material

Primary source:

* `sections/sec05.tex`

Supporting source:

* affine cocycle material from Chapter 4 sources.

---

## Required changes

* Generalize beyond path-versus-reversal.
* Simplify the evaluation formula using the cocycle.
* Fix one consistent sign and orientation convention.
* Remove speculative quotient theory reserved for Paper IV.

---

# 9. Contact Connection and Horizontal Curvature

## 9.1 State space

Define:

[
\mathcal C
==========

\mathbb R^3_{(u,v,a)}
]

or the appropriate local bundle over the ((u,v))-plane.

---

## 9.2 Contact form

Define:

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

Prove:

[
\alpha\wedge d\alpha\neq0
]

when:

[
\mu\lambda\neq0.
]

---

## 9.3 Horizontal distribution

Define:

[
\mathcal H=\ker\alpha.
]

Introduce:

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

Show:

[
\alpha(D_u)=\alpha(D_v)=0.
]

---

## 9.4 Legendrian arithmetic flow

Show that a curve tangent to:

[
\cos\theta D_u+\sin\theta D_v
]

satisfies the arithmetic flow equation.

This establishes that the contact structure packages the affine propagation law.

---

## 9.5 Curvature bracket

### Theorem slot

Prove:

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

Interpret the bracket as vertical failure of the horizontal distribution to close.

---

## 9.6 Exact finite commutator

Compute the finite add–multiply comparison:

[
\mu h(e^{\lambda k}-1).
]

Compute the closed-loop vertical drift separately.

State explicitly that:

* open two-path defect;
* closed-loop holonomy;
* infinitesimal bracket

are related but not identical at finite scale.

---

## 9.7 Horizontal covariant differential

Define:

[
\delta_HF
=========

dF-(\partial_aF)\alpha.
]

Equivalently:

[
\delta_HF
=========

(D_uF),du+(D_vF),dv.
]

---

## 9.8 Curvature of the horizontal differential

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

State clearly that (\delta_H) is not a nilpotent differential.

---

## 9.9 Local-global comparison

Conclude with the structural correspondence:

[
\boxed{
\begin{aligned}
\text{finite affine history defect}
&\longleftrightarrow
\text{ACS weighted area},\
\text{infinitesimal history defect}
&\longleftrightarrow
\text{contact curvature}.
\end{aligned}}
]

Clarify that the finite and infinitesimal formulas differ by exponential weighting and higher-order effects.

---

## 9.10 What is not yet analytic

State that the contact distribution does not by itself supply:

* a unique horizontal metric;
* a unique complex structure;
* a canonical (\bar\partial)-operator;
* a complete harmonic theory.

These are developed in Paper II.

---

## Required output of Chapter 9

The chapter must complete the main foundational arc:

[
\text{history order defect}
\longrightarrow
\text{curvature}.
]

---

## Existing source material

Primary sources:

* `sections/sec06.tex`
* foundational portions of `sections/sec07.tex`

---

## Material to move

Move to Paper II:

* extensive chain-rule tables;
* affine–Appell basis;
* antidifferentiation procedures;
* arithmetic Cauchy–Riemann equations;
* arithmetic holomorphicity;
* twisted harmonicity.

---

# 10. Conclusions and Research Interfaces

## 10.1 What has been established

Summarize the actual proved chain:

[
\text{sequential histories}
\to
PGL_2
\supset
\operatorname{Aff}(1)
\to
\text{flow}
\to
\mathfrak E_0
\to
\text{torsion/contact curvature}.
]

Include regular zero-set structure as a separate foundational consequence.

---

## 10.2 Interface to Paper II

State that Paper II adds:

* horizontal metric and compatible complex structure;
* second-order operators;
* boundary-value theory;
* arithmetic holomorphicity.

Do not state future analytic results as already proved.

---

## 10.3 Interface to Paper III

State that Paper III studies failure of the regular-zero hypotheses:

* singular zeros;
* multi-zero models;
* parameter discriminants;
* regular and singular tubes;
* monodromy and conditional knot structures.

---

## 10.4 Interface to Paper IV

State that Paper IV develops:

* full projective process-result hierarchy;
* bivaluation;
* quotient towers;
* condensation;
* representation and computational complexity.

---

## 10.5 Open foundational problems

Paper I may end with a restrained list:

1. classification of regular affine AES models;
2. projective replacement for ACS;
3. comparison between affine contact curvature and projective holonomy;
4. construction of fully verified multi-zero models;
5. precise relation between geometric and computational complexity.

These must be labeled as open.

---

## Required output of Chapter 10

The conclusion must not repeat the old claim that Paper I already establishes a function theory.

It should end with the stable foundation and clearly marked interfaces.

---

# Part IV. Appendices

# Appendix A. Composition and action conventions

Include:

* chronological composition;
* matrix multiplication order;
* left versus right actions;
* ordinary versus projective domains;
* notation conversion table.

This appendix should eliminate convention ambiguity from the main text.

---

# Appendix B. Affine cocycle calculations

Include:

* induction proofs;
* alternating-history expansions;
* perturbation propagation;
* conversion between (\xi) and (\widehat\xi);
* selected explicit examples.

---

# Appendix C. Hyperbolic-model calculations

Include:

* coordinate transformations;
* inverse metric;
* gradient calculation;
* curvature calculation;
* Laplacian calculation;
* grid transformations;
* Baumslag–Solitar relation check.

---

# Appendix D. ACS and contact calculations

Include:

* signed path examples;
* finite commutator computations;
* Stokes sign checks;
* contact-form Darboux normalization;
* Reeb field, if retained;
* detailed (\delta_H^2) calculation.

---

# Appendix E. Equality and neutrality examples

Retain a small set of examples distinguishing:

* same value, different operator;
* same operator, different history;
* same charge, different torsion;
* zero endpoint defect, nontrivial history;
* local torsion versus closed-loop holonomy.

Do not develop full loop theory.

---

# Part V. Target source-file organization

## 11. Recommended LaTeX structure

A possible target organization is:

```text
paper-1/
├── aeg-paper-1.tex
├── sections/
│   ├── 01-introduction.tex
│   ├── 02-sequential-histories.tex
│   ├── 03-projective-affine.tex
│   ├── 04-affine-cocycles.tex
│   ├── 05-affine-flow.tex
│   ├── 06-hyperbolic-model.tex
│   ├── 07-zero-geometry.tex
│   ├── 08-acs-torsion.tex
│   ├── 09-contact-curvature.tex
│   └── 10-conclusion.tex
├── appendices/
│   ├── app-A-conventions.tex
│   ├── app-B-cocycles.tex
│   ├── app-C-hyperbolic.tex
│   ├── app-D-acs-contact.tex
│   └── app-E-equality.tex
└── images/
```

The repository now uses this logical division under `paper-1/`, with the appendices
stored in the sibling `paper-1/appendices/` directory.

The restructuring task must not rename every file before the mathematical audit is complete.

---

# Part VI. Current-to-target migration summary

## 12. Existing source mapping

| Current source                                | Target destination                                            |
| --------------------------------------------- | ------------------------------------------------------------- |
| `sections/sec01.tex`                          | Chapter 1, heavily rewritten                                  |
| `sections/sec02-00.tex`                       | Chapter 2, expression-tree material retained                  |
| `sections/sec02-01.tex`                       | Split between Chapters 2 and 4                                |
| `sections/sec03.tex`                          | Chapter 5; affine-group material also Chapter 4               |
| `sections/sec04.tex`                          | Chapters 6 and 7                                              |
| `sections/sec05.tex`                          | Chapter 8, generalized                                        |
| `sections/sec06.tex`                          | Chapter 9                                                     |
| `sections/sec07.tex`                          | Foundational part to Chapter 9; analytic material to Paper II |
| `sections/sec08.tex`                          | Move to Paper II                                              |
| `sections/sec09.tex`                          | Replace with Chapter 10                                       |
| `notes/bilateral_projective_condensation.tex` | Chapter 2 and 3 foundations; remainder to Paper IV            |
| multi-zero and tube notes                     | Chapter 7 definitions only; remainder to Paper III            |
| resource/complexity notes                     | Paper IV                                                      |
| old loop notes                                | Appendix E or later relation-theory work                      |

The detailed line-level migration belongs in:

```text
restructure/04-current-to-target-map.md
```

---

# Part VII. Suggested length budget

## 13. Main-text budget

Recommended main-text target:

| Chapter                            | Approximate pages |
| ---------------------------------- | ----------------: |
| 1. Introduction                    |               4–6 |
| 2. Sequential histories            |              8–10 |
| 3. Projective and affine semantics |               7–9 |
| 4. Affine cocycles                 |               6–8 |
| 5. Continuous flow                 |               7–9 |
| 6. Hyperbolic model                |              9–12 |
| 7. Zero geometry                   |              7–10 |
| 8. ACS torsion                     |              8–10 |
| 9. Contact curvature               |              8–10 |
| 10. Conclusion                     |               3–4 |

Recommended main text:

[
65\text{–}85\ \text{pages}
]

including figures but excluding appendices.

If the draft exceeds this range significantly, move calculations or secondary examples to appendices.

---

# Part VIII. Figure plan

## 14. Required conceptual figures

Paper I should contain a limited set of figures with clear mathematical functions.

### Figure 1: Process-to-result tower

[
\text{tree}
\to
\text{history}
\to
\text{operator}
\to
\text{value}.
]

### Figure 2: Sequential versus branching tree

Show the dependency-chain criterion.

### Figure 3: Slot-(1), slot-(2), and mixed histories

Show chirality without relying on left/right prose.

### Figure 4: Affine sector inside projective transformations

A schematic showing:

[
B_\infty\subset PGL_2.
]

### Figure 5: Hyperbolic arithmetic grid

Retain and improve the existing add–multiply grid.

### Figure 6: Regular zero line versus singular isolated zero

Show why the latter lies outside the regular theorem.

### Figure 7: Two compatible ACS histories and weighted filling

Use the generalized two-history formulation.

### Figure 8: Contact commutator square

Distinguish open two-path defect and closed-loop holonomy.

No figure should be used as evidence for an unproved theorem.

---

# Part IX. Theorem inventory

## 15. Required theorem and proposition slots

The target paper should contain stable labels for at least:

```text
thm:sequential-tree-classification
def:marked-spinal-history
def:projective-evaluation
thm:bilateral-pgl2-generation
cor:affine-borel-sector
prop:affine-cocycle-formulas
prop:left-right-affine-differentials
thm:continuous-affine-flow
def:regular-aes
thm:basic-hyperbolic-aes
prop:laplace-eigenfunction
thm:regular-zero-locus
def:singular-aes
prop:regular-total-zero-set
def:acs
def:relative-torsion
thm:torsion-stokes
prop:contact-form
thm:contact-curvature
prop:horizontal-differential-curvature
```

Labels may be refined, but narrative labels such as `final_revised_enhanced` must be removed.

---

# Part X. Validation checklist

## 16. Mathematical validation

Before Paper I is considered structurally complete, verify:

* [ ] The sequential-tree definition agrees with all examples.
* [ ] Mirror and reversal are never conflated.
* [ ] Projective matrix composition matches chronological evaluation.
* [ ] Division domains are stated.
* [ ] (PGL_2) generation proof handles all cases.
* [ ] The affine sector is stated with the correct field and orientation qualifications.
* [ ] (\xi) and (\widehat\xi) are not interchanged.
* [ ] The flow derivation uses one explicit left/right convention.
* [ ] The eikonal equation is stated only after a metric is specified.
* [ ] The hyperbolic-model gradient calculation is correct.
* [ ] Laplacian sign conventions are fixed.
* [ ] The Baumslag–Solitar relation uses the correct action order.
* [ ] The regular-zero theorem includes (\mu\neq0).
* [ ] The isolated-zero model is classified as singular.
* [ ] The total-zero-set result is not overstated as a global tube theorem.
* [ ] Relative torsion hypotheses are explicit.
* [ ] ACS orientation and sign conventions are consistent.
* [ ] Open defect and closed holonomy are distinguished.
* [ ] (\delta_H) is not described as nilpotent.
* [ ] No analytic complex structure is claimed to be contact-canonical.

---

## 17. Editorial validation

* [ ] Abstract matches the final theorem set.
* [ ] Introduction contains no future-paper result as an established theorem.
* [ ] All symbols are introduced before use.
* [ ] (\mathfrak E_0) and (\mathfrak E_1) are used consistently.
* [ ] `u` and `\nu` are not confused.
* [ ] Examples use the `Example` theorem environment.
* [ ] Duplicate labels are removed.
* [ ] Undefined references are resolved.
* [ ] Citations are relevant and accurate.
* [ ] Material moved to Papers II–IV is recorded.
* [ ] The PDF builds successfully.

---

# Part XI. Restructuring phases

## 18. Recommended implementation order

### Phase 0: Audit

Do not modify the body.

Produce:

```text
restructure/audit-report.md
```

---

### Phase 1: Skeleton

Create the target chapter structure while preserving current content in temporary locations.

Ensure the PDF builds.

---

### Phase 2: Sequential and projective foundations

Implement Chapters 2 and 3.

Do not modify later geometric chapters beyond necessary references.

---

### Phase 3: Affine cocycles and flow

Implement Chapters 4 and 5.

Normalize composition conventions.

---

### Phase 4: Hyperbolic and zero geometry

Implement Chapters 6 and 7.

Resolve (\mathfrak E_0/\mathfrak E_1) status.

---

### Phase 5: ACS and contact geometry

Implement Chapters 8 and 9.

Generalize torsion and normalize curvature terminology.

---

### Phase 6: Migration

Move:

* function theory to Paper II;
* multi-zero/tube theory to Paper III;
* projective condensation and complexity to Paper IV.

---

### Phase 7: Global rewrite

Rewrite:

* abstract;
* introduction;
* conclusion;
* section transitions;
* bibliography references;
* figure captions.

---

### Phase 8: Mathematical audit

Check every theorem against:

```text
restructure/05-mathematical-status.md
```

Do not resolve open mathematical issues by editorial rewriting.

---

## 19. Final structural criterion

Paper I succeeds only if a reader can follow the complete chain:

[
\boxed{
\begin{aligned}
\text{Why is a sequential expression a history?}\
\Downarrow\
\text{What operator does that history induce?}\
\Downarrow\
\text{Why is the current theory affine inside a projective completion?}\
\Downarrow\
\text{How do affine histories produce flow and geometry?}\
\Downarrow\
\text{How does order defect become torsion and curvature?}\
\Downarrow\
\text{Where do regular geometry and singular extensions separate?}
\end{aligned}}
]

Any section that does not advance this chain should be shortened, moved to an appendix, or assigned to a later paper.
