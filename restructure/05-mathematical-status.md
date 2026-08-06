# Mathematical Status Register

**File:** `restructure/05-mathematical-status.md`
**Status:** Authoritative
**Version:** 1.1
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `restructure/00-authoritative-scope.md`
* `restructure/01-paper-series-architecture.md`
* `restructure/02-paper-I-outline.md`
* `restructure/03-theorem-dependency-graph.md`
* `restructure/04-current-to-target-map.md`

**Applies to:** Mathematical claims in Papers I–IV and their supporting notes.

---

## 1. Purpose

This document records the current mathematical status of the principal definitions, claims, propositions, theorems, constructions, and research programs in the AEG repository.

Its purposes are to:

* prevent conjectures and proposals from being promoted into theorems during editorial restructuring;
* distinguish an existing proof from a result that is merely plausible or standard;
* record hypotheses that must remain attached to a result;
* identify proof obligations before dependent results may be marked complete;
* determine which claims may appear in abstracts, introductions, and conclusions;
* provide Codex and human collaborators with a common status vocabulary.

This file records mathematical status, not merely editorial destination.

A claim may belong to Paper I while remaining unproved. Conversely, a proved claim may be moved to Paper IV because it is outside Paper I’s scope.

---

# Part I. Status vocabulary

## 2. Authoritative status labels

Every substantial mathematical claim must use one of the following labels.

### `PROVED`

A complete proof is present in the repository or has been independently checked, and the theorem is correct as stated.

A result with this label may still require editorial migration or notation normalization.

---

### `PROVED WITH STATED HYPOTHESES`

A complete proof is available, but the result is valid only under hypotheses that must remain explicit.

Typical hypotheses include:

* (K) is a field;
* a context is non-degenerate;
* a multiplier is nonzero;
* (\mu\lambda\neq0);
* a metric and assignment are smooth;
* a statement is local rather than global.

---

### `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`

The result follows directly from a standard theorem or a short calculation, but the required proof or citation is not yet present in the target paper.

This status does not authorize omission of hypotheses.

---

### `COMPUTATIONALLY VERIFIED EXAMPLE`

The claim has been checked for a finite set of parameters, a symbolic computation, or a plotted example, but no general proof is available.

It may appear as an example, not as evidence for a general theorem.

---

### `PARTIALLY PROVED`

A proof exists for a restricted case or several components are proved, but the full target statement is not established.

The exact proved subcase must be recorded.

---

### `STRUCTURAL PROPOSAL`

The claim defines a potentially useful framework, interpretation, or object, but no theorem of existence, uniqueness, invariance, or completeness has yet been proved.

Definitions may have this status while they are being stabilized.

---

### `CONJECTURE`

A mathematically precise statement is proposed as true but remains unproved.

A conjecture must include explicit hypotheses and a stable formulation before it appears under this label.

---

### `OPEN PROBLEM`

A research question has been identified, but no precise conjectural answer is currently asserted.

---

### `UNSUPPORTED AND EXCLUDED`

The claim does not follow from current results and must not appear as an established conclusion.

It may be retained in an archive as historical motivation if clearly labeled.

---

## 3. Auxiliary editorial labels

The following labels may accompany, but do not replace, the mathematical status.

* `INTEGRATION AUDIT REQUIRED`
* `SIGN CONVENTION AUDIT REQUIRED`
* `DOMAIN AUDIT REQUIRED`
* `NORMALIZATION AUDIT REQUIRED`
* `PROPERNESS REQUIRED`
* `FUNCTIONAL-ANALYTIC FRAMEWORK REQUIRED`
* `MOVED TO PAPER II`
* `MOVED TO PAPER III`
* `MOVED TO PAPER IV`
* `OPTIONAL IN PAPER I`
* `DO NOT USE AS A DEPENDENCY`

---

## 4. Interpretation rule

A result described as “proved in a working note” is not automatically ready for publication.

Before the target paper marks it `PROVED`, the following must be checked:

1. the theorem statement matches the proof;
2. all field and regularity hypotheses are explicit;
3. composition and sign conventions match the target paper;
4. no superseded notation remains;
5. the proof is independent of claims moved to later papers;
6. examples do not replace missing general arguments.

---

# Part II. Executive status summary

## 5. Stable algebraic core

The following claims have proofs or direct calculations in the current repository and are expected to survive the restructuring:

* sequential-tree classification;
* projective matrices for bilateral arithmetic contexts;
* generation of (PGL_2(K)) by translations, scalings, and inversion;
* identification of the affine/Borel subgroup;
* affine composition and cocycle formulas;
* elementary affine torsion;
* affine Lie-algebra flow;
* explicit verification of the basic upper-half-plane model;
* contact nondegeneracy;
* horizontal bracket curvature;
* horizontal scalar curvature formula.

These results still require convention and integration audits.

---

## 6. Standard but not yet fully integrated results

The following are mathematically straightforward but need formal insertion into Paper I:

* regular zero-locus theorem;
* regular total-zero-set theorem;
* direct ACS formula from the affine cocycle;
* generalized two-history torsion formula;
* weighted Stokes theorem for compatible histories;
* curvature and Laplace calculations for the fully normalized metric;
* invariant affine metric derivation.

---

## 7. Incomplete or conditional programs

The following are not yet complete theories:

* a fully verified general multi-zero construction;
* classification of (E_k);
* a general (E_{\log}) theory;
* singularity normal forms compatible with the AEG flow;
* global tube triviality;
* braid and knot invariants;
* Markov-normalized threading invariants;
* a complete hyperbolic real function theory;
* a rigorous equivalence among representation, time, and space complexity.

---

## 8. Claims explicitly excluded from current conclusions

The following are not established:

[
\text{noncommutativity}
\Rightarrow
\text{negative curvature};
]

[
\text{negative curvature}
\Rightarrow
\text{algorithmic hardness};
]

[
\text{multiple zero lines}
\Rightarrow
\text{knot invariant};
]

[
\text{contact structure}
\Rightarrow
\text{unique complex structure};
]

[
\text{projective continuation}
\Rightarrow
\text{ordinary arithmetic regularity}.
]

These claims must not appear as theorems, corollaries, or abstract-level conclusions.

---

# Part III. Paper I convention and definition status

## 9. Convention nodes

| ID | Object                                                 | Current status                                                | Target action                                           |
| -- | ------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------- |
| C0 | Chronological composition and matrix-action convention | STRUCTURAL PROPOSAL; inconsistent usage possible across files | Fix one convention before migrating proofs              |
| C1 | Ordinary versus projective admissibility               | PARTIALLY DEFINED                                             | Write one explicit domain convention                    |
| C2 | Differential-geometric hypotheses                      | PARTIALLY DEFINED                                             | State constant/positive/nonzero assumptions per theorem |

These are not mathematical theorems, but no downstream result is publication-ready until they are fixed.

---

## 10. Definition nodes

| ID | Object                            | Current status                                      | Target status                           |
| -- | --------------------------------- | --------------------------------------------------- | --------------------------------------- |
| S1 | Arithmetic expression tree        | PROVED/standard definition                          | Preserve and normalize                  |
| S2 | Internal dependency poset         | Definition present implicitly                       | Make explicit                           |
| S3 | Marked spinal history             | PROVED as a coherent definition in bilateral note   | Adopt as canonical                      |
| S4 | Mirror, reversal, path inverse    | PROVED as distinct operations                       | Adopt and illustrate                    |
| S5 | Levels of equality                | STRUCTURAL PROPOSAL with useful examples            | Retain minimal hierarchy                |
| P1 | Projective semantics of contexts  | PROVED WITH STATED HYPOTHESES                       | Integrate into Paper I                  |
| P2 | Projective evaluation map         | STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF    | Prove composition compatibility         |
| E1 | Regular AES                       | STRUCTURAL PROPOSAL; exact definition not yet fixed | Resolve before Chapter 6                |
| Z1 | Zero set                          | Standard definition                                 | Preserve                                |
| Z3 | Singular AES                      | STRUCTURAL PROPOSAL                                 | Adopt a minimal foundational definition |
| Z5 | Parameterized assignment family   | Standard definition                                 | Preserve                                |
| G1 | ACS and charge path               | PROVED as a usable definition                       | Generalize orientation conventions      |
| G2 | Scale-compatible histories        | New target definition                               | Add                                     |
| G3 | Charge-compatible histories       | New target definition                               | Add                                     |
| K1 | Arithmetic contact form           | PROVED as a definition                              | Preserve                                |
| K2 | Horizontal lifts                  | PROVED                                              | Preserve                                |
| K4 | Horizontal covariant differential | PROVED on scalar fields                             | Restrict claim to defined scope         |

---

# Part IV. Sequential syntax status

## 11. T1 — Sequential-tree classification

### Target statement

For a finite binary expression tree (T), the following are equivalent:

1. the internal dependency poset has a unique linear extension;
2. the dependency poset is a chain;
3. every internal vertex has at most one internal child;
4. the internal vertices form a single spine.

### Current status

```text id="co2rs6"
PROVED
INTEGRATION AUDIT REQUIRED
```

### Existing support

A complete proof appears in:

```text id="bxj5pu"
notes/bilateral_projective_condensation.tex
```

### Remaining obligations

* state the finite-poset lemma clearly;
* handle a tree with no internal vertices;
* distinguish unique internal evaluation order from choice of initial marked leaf;
* prove the marked-history correspondence separately if claimed as a bijection.

### Dependency authorization

T1 may support S3 after integration.

---

## 12. Marked-tree-to-history correspondence

### Candidate statement

A sequential tree together with a marked accumulator determines a unique marked spinal context word.

### Current status

```text id="adjnrk"
PROVED IN ESSENCE
STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF
```

### Remaining obligations

* define the innermost marked leaf convention;
* prove reconstruction from a context word;
* decide whether the result is a bijection or only a canonical encoding.

---

## 13. Mirror versus temporal reversal

### Current status

```text id="cg4iw6"
PROVED BY DEFINITION AND EXAMPLE
```

### Established content

Mirror swaps operand slots without reversing temporal order.

Temporal reversal reverses the context word.

These operations are distinct and commute at the marked-word level under the current definition.

### Remaining obligation

Check whether the commutation statement remains true after domain restrictions and path inversion are included.

---

## 14. Associativity as a (2)-cell

### Current status

```text id="ma29sc"
STRUCTURAL PROPOSAL
OPTIONAL IN PAPER I
```

### Permitted use

May appear as a short outlook remark.

### Prohibited use

It must not be used to claim that the full associahedral or higher-categorical theory has been constructed.

---

# Part V. Projective semantics status

## 15. Elementary projective matrices

### Current status

```text id="4fmzph"
PROVED WITH STATED HYPOTHESES
DOMAIN AUDIT REQUIRED
```

### Established contexts

[
z\mapsto z+c,
\qquad
z\mapsto z-c,
\qquad
z\mapsto c-z,
]

[
z\mapsto cz,
\qquad
z\mapsto z/c,
\qquad
z\mapsto c/z.
]

### Remaining obligations

* state (c\neq0) when invertibility requires it;
* classify multiplication by zero and constant maps as monoid elements, not (PGL_2) elements;
* distinguish projective value at (\infty) from ordinary arithmetic admissibility.

---

## 16. T2 — Bilateral arithmetic generates (PGL_2(K))

### Current status

```text id="hu6q8e"
PROVED WITH STATED HYPOTHESES
INTEGRATION AUDIT REQUIRED
```

### Existing proof

The current working note proves generation using:

[
T_s(z)=z+s,
\qquad
D_q(z)=qz,
\qquad
J(z)=-1/z.
]

For (C\neq0):

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

### Remaining obligations

* verify chronological composition notation;
* state (AD-BC\neq0);
* verify characteristic-(2) wording and sign conventions;
* handle (C=0) explicitly;
* distinguish generation by the language from surjectivity of any restricted positive-real parameterization.

### Dependency authorization

May support P3 after the composition audit.

---

## 17. P3 — Affine/Borel-sector identification

### Current status

```text id="ewch0b"
PROVED
```

### Established statement

[
\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

The first-slot non-degenerate arithmetic sector is affine, subject to the exact context restrictions.

### Remaining obligations

* state whether reflections (z\mapsto c-z) are included;
* distinguish the algebraic Borel from its identity component;
* avoid identifying all constant-chirality syntactic histories with all affine maps unless generator coverage is proved.

---

## 18. P4 — Positive real affine sector

### Current status

```text id="ijcl9j"
PROVED
```

### Statement

The real parameterization:

[
z\mapsto e^\lambda z
]

uses positive multipliers, so the continuous theory lies in:

[
\operatorname{Aff}^{+}(1,\mathbb R).
]

### Remaining obligation

Use this qualification consistently in Paper I.

---

## 19. Bruhat interpretation

### Current status

```text id="v43vcq"
PROVED AS A STANDARD GROUP-THEORETIC FACT
OPTIONAL IN PAPER I
```

### Permitted statement

[
PGL_2(K)=B\sqcup BJB
]

at the rank-one Bruhat-cell level.

### Remaining obligation

Do not use the remark as a substitute for the explicit generation proof.

---

## 20. P5 — Riccati completion

### Current status

```text id="m8b216"
PROVED AS AN INFINITESIMAL LIE-ALGEBRA STATEMENT
PARTIALLY DEVELOPED AS GEOMETRY
```

### Established statement

The projective vector fields:

[
E=\partial_z,
\qquad
H=z\partial_z,
\qquad
F=z^2\partial_z
]

span the local projective Lie algebra, producing:

[
\dot z=\beta+\alpha z+\kappa z^2.
]

The current affine flow is the slice:

[
\kappa=0.
]

### Not established

* a full projective AES;
* a projective metric replacing the affine hyperbolic model;
* a projective contact connection;
* a projective replacement for the ACS area formula.

These remain open or belong to Paper IV.

---

# Part VI. Affine cocycle status

## 21. A1/T3 — Affine composition and target-frame cocycle

### Current status

```text id="77hkeo"
PROVED
```

### Established formulas

For:

[
f_i(x)=s_ix+t_i,
]

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n,
]

with:

[
\Phi_n=\prod_{i=1}^{n}s_i,
]

[
\xi_n
=====

\sum_{i=1}^{n}
t_i\prod_{j=i+1}^{n}s_j.
]

### Remaining obligation

Rewrite under the final chronological convention.

---

## 22. T4 — Source-normalized cocycle

### Current status

```text id="q65oy5"
PROVED
```

### Established formula

[
\widehat\xi_n
=============

# \frac{\xi_n}{\Phi_n}

\sum_{i=1}^{n}
\frac{t_i}{\prod_{j=1}^{i}s_j}.
]

### Remaining obligation

State whether the field is arbitrary or real, and require (s_i\neq0).

---

## 23. A2 — Left and right Maurer–Cartan translation forms

### Current status

```text id="2xgiat"
PROVED
SIGN CONVENTION AUDIT REQUIRED
```

### Established formulas

For:

[
g=
\begin{pmatrix}
e^\lambda&\xi\
0&1
\end{pmatrix},
]

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

### Remaining obligations

* identify source/body and target/spatial interpretation;
* ensure (\lambda) here means accumulated logarithmic scale, not the fixed flow intensity;
* consider renaming the accumulated coordinate to avoid overloading.

---

## 24. A3 — Relative affine defect

### Current status

```text id="rw4dxl"
PROVED
```

### Established statement

If:

[
\rho(\gamma)(x)=\Phi_\gamma x+\xi_\gamma,
]

[
\rho(\delta)(x)=\Phi_\delta x+\xi_\delta,
]

and:

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

### Remaining obligation

Distinguish endpoint difference from the normalized group-valued relative transformation:

[
\rho(\delta)^{-1}\rho(\gamma).
]

---

## 25. A4 — Elementary arithmetic torsion

### Current status

```text id="8qwzri"
PROVED
```

### Exact formula

[
(x+\mu)e^\lambda
----------------

# (xe^\lambda+\mu)

\mu(e^\lambda-1).
]

### Remaining obligations

* fix orientation and sign;
* distinguish this open two-path difference from a closed commutator-loop holonomy;
* distinguish it from a mirror comparison.

---

## 26. Bilateral recursion examples

### Current status

```text id="jh4m7z"
PARTIALLY PROVED
MOVED TO PAPER IV OR ACTIVE NOTES
```

### Established negative result

For one fixed element (p) and central common seed, the recursions:

[
S_{n+1}=1+pS_n,
\qquad
\widetilde S_{n+1}=1+\widetilde S_np
]

may collapse to the same polynomial or resolvent.

### Structural lesson

Noncommutativity alone is insufficient; retained step-dependent or noncentral data are required.

### Not established

A general bilateral resolvent theory.

---

# Part VII. Continuous-flow status

## 27. F1 — Affine Lie algebra

### Current status

```text id="pe3vw8"
PROVED
```

### Established structure

Translation and dilation generators form:

[
\mathfrak{aff}(1).
]

The precise bracket sign depends on basis order.

---

## 28. T5 — Continuous affine flow

### Current status

```text id="ma4j9t"
PROVED WITH STATED CONVENTIONS
INTEGRATION AUDIT REQUIRED
```

### Established equation

[
\frac{da}{ds}
=============

\mu\cos\theta
+
\lambda a\sin\theta.
]

### Existing derivations

* first-order expansion of add/multiply updates;
* affine matrix Lie-algebra evolution.

### Remaining obligations

* select one primary derivation;
* fix left/right evolution convention;
* distinguish constant flow intensities from accumulated affine coordinates;
* specify whether ((u,v)) is orthonormal or merely normalized.

---

## 29. F2 — Pfaffian propagation law

### Current status

```text id="k7nf3e"
PROVED AS THE LOCAL HORIZONTAL FORM OF T5
```

### Formula

[
da
==

\mu,du+\lambda a,dv.
]

### Required warning

On the three-dimensional state space, this is a horizontal constraint:

[
\alpha=0,
]

not a globally integrable equality of independent coordinate differentials.

---

## 30. F3 — Eikonal equation

### Current status

```text id="l49zwh"
PROVED WITH A COMPATIBLE METRIC FRAME
```

### Formula

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

### Remaining obligations

* make the metric assumption explicit;
* do not call the equation metric-free;
* decide whether it is the definition of regular AES or a consequence of a framed AES.

---

## 31. F4 — Rectifying coordinate

### Current status

```text id="hxtbyg"
PROVED WITH STATED HYPOTHESES
OPTIONAL IN PAPER I
```

### Formula

For suitable nonzero parameters:

[
r(a)
====

\operatorname{arcsinh}
\left(
\frac{\lambda a}{\mu}
\right),
]

[
|\nabla r|=|\lambda|.
]

### Remaining obligations

* handle signs;
* exclude or treat (\mu=0);
* state domains.

---

## 32. F5 — Infinitesimal torsion density

### Current status

```text id="9hw6l6"
PROVED AS AN ASYMPTOTIC EXPANSION
```

### Formula

[
\Delta\tau
==========

\mu\lambda,du,dv
+
O(|(du,dv)|^3).
]

### Required warning

The expression:

[
\mu\lambda,du\wedge dv
]

becomes an exact curvature two-form only in the contact/horizontal formulation, not merely from the finite-step Taylor expansion.

---

# Part VIII. Regular AES and hyperbolic-model status

## 33. E1 — Regular AES definition

### Current status

```text id="4o7q84"
STRUCTURAL PROPOSAL
DECISION REQUIRED
```

### Current ambiguity

It is not yet fully fixed whether a regular AES consists of:

1. a Riemannian surface and assignment satisfying the eikonal equation; or
2. a framed surface with additive/multiplicative directions satisfying the directional flow; or
3. both, with a compatibility condition.

### Required decision

Paper I must select one canonical definition and state which structures are:

* primitive;
* derived;
* local;
* global.

### Dependency restriction

T6 and T7 must not be finalized until E1 is fixed.

---

## 34. E2 — Invariant affine metric

### Current status

```text id="hc7nds"
STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF
NORMALIZATION AUDIT REQUIRED
```

### Target formula

[
g_{\mu,\lambda}
===============

e^{-2\lambda v}\frac{du^2}{\mu^2}
+
dv^2.
]

### Remaining obligations

* define the affine group coordinates;
* specify left or right invariance;
* derive the metric from the normalized generator frame;
* avoid uniqueness claims.

---

## 35. T6 — Basic hyperbolic AES

### Current status

```text id="9nopac"
PROVED WITH STATED HYPOTHESES
NORMALIZATION AUDIT REQUIRED
```

### Established model

[
g_{\mu,\lambda}
===============

\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
]

[
a(x,y)=-\frac{x}{y}.
]

Direct calculation gives:

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2.
]

### Remaining obligations

* derive or connect the model to E2;
* fix positivity assumptions for the metric;
* confirm the canonical model name (\mathfrak E_0);
* state whether the domain is connected and complete.

---

## 36. E3 — Curvature of the basic metric

### Current status

```text id="8c6lw0"
STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF
```

### Expected result

Under the displayed normalization:

[
K=-\lambda^2.
]

### Verification

Using:

[
X=x/\mu,
\qquad
Y=y/\lambda,
]

the metric becomes a constant multiple of the standard upper-half-plane metric.

### Remaining obligation

Write the coordinate change and curvature scaling explicitly.

---

## 37. E4 — Arithmetic grid actions

### Current status

```text id="8as51s"
PROVED AS ASSIGNMENT TRANSFORMATIONS
```

### Established actions

In horocyclic coordinates, transformations can be chosen so that:

[
a\circ X_s=a+s,
]

[
a\circ Y_k=ka.
]

### Not established automatically

That every such transformation is an isometry.

### Required action

State precisely whether the maps preserve:

* assignment only;
* the metric;
* the framed flow;
* the full AES structure.

---

## 38. E5 — Baumslag–Solitar relation

### Current status

```text id="v6ywjv"
PROVED UNDER THE CURRENT ACTION FORMULAS
SIGN AND COMPOSITION AUDIT REQUIRED
OPTIONAL IN PAPER I
```

### Current formula

[
Y_k^{-1}X_s^{,k}Y_k=X_s.
]

### Remaining obligations

* confirm chronological action order;
* specify integer (k>0);
* distinguish a representation of the relation from a statement about the full geometry.

### Prohibited inference

No complexity result follows directly from this relation.

---

## 39. E6 — Laplace eigenfunction

### Current status

```text id="60ho3n"
PROVED BY DIRECT CALCULATION
NORMALIZATION AUDIT REQUIRED
```

### Expected general formula

With the positive-sign Laplace–Beltrami convention:

[
\Delta_g a
==========

2\lambda^2a.
]

For (\lambda=1):

[
\Delta_g a=2a.
]

### Remaining obligations

* state Laplacian sign convention;
* verify no (\mu)-dependence remains;
* update every normalized statement.

---

## 40. Uniqueness of (\mathfrak E_0)

### Current status

```text id="5zskg4"
OPEN PROBLEM
```

### Not established

* conformal uniqueness;
* uniqueness among homogeneous AES models;
* uniqueness from the flow equation alone.

### Permitted wording

“The basic model” or “a canonical homogeneous model after chosen normalization.”

### Prohibited wording

“The unique arithmetic expression space satisfying the flow equation.”

---

# Part IX. Zero-locus and singularity status

## 41. T7 — Regular zero-locus theorem

### Current status

```text id="k22qgu"
STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF
```

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

Therefore (0) is a regular value.

### Consequence

For a two-dimensional boundaryless regular AES:

[
Z(a)
]

is a disjoint union of smooth one-dimensional submanifolds.

### Remaining obligations

* invoke the regular-value theorem;
* treat manifolds with boundary separately;
* avoid unjustified global classification of connected components.

---

## 42. Z2 — Zero-set rigidity corollaries

### Current status

```text id="ywx9nn"
STANDARD CONSEQUENCES REQUIRING PRECISE HYPOTHESES
```

### Locally established consequences

In the regular interior:

* no isolated zero;
* no zero-line crossing;
* no branch point;
* no zero-line endpoint.

### Not established globally without more assumptions

* every component is a circle;
* every component is proper;
* the number of components is finite;
* topology is preserved in non-proper families.

---

## 43. Z3 — Singular AES definition

### Current status

```text id="oz4bcq"
STRUCTURAL PROPOSAL
```

### Target role

Provide a category broad enough to include:

* non-smooth assignment;
* degenerate metric;
* degenerate flow parameters;
* deleted points;
* chart singularities;
* projective poles.

### Remaining obligation

Avoid making the definition so broad that every failed model becomes a singular AES without usable structure.

The definition should require a well-defined regular locus on which the Paper I equations hold.

---

## 44. Z4 — Isolated-zero model (\mathfrak E_1)

### Current status

```text id="60y33f"
PARTIALLY PROVED
RECLASSIFICATION REQUIRED
```

### Current formula

In a radial hyperbolic disk coordinate:

[
a(r)
====

\frac{\mu}{\lambda}
\frac{2r}{1-r^2}.
]

### Current mathematical assessment

At (r=0), the function behaves linearly in the Euclidean radius:

[
a(r)\sim \frac{2\mu}{\lambda}r.
]

As a function of Cartesian coordinates, (r=\sqrt{x^2+y^2}) is not differentiable at the origin.

Thus the isolated zero is compatible with the regular-zero theorem only if the origin is treated as:

* a singular assignment point; or
* a deleted point with a singular extension.

### Remaining obligations

* write the model in Cartesian coordinates;
* verify regularity of the metric at the center;
* state exactly where the flow equation holds;
* determine whether the model is included or punctured.

### Target status after proof

```text id="ql1rso"
PROVED SINGULAR EXAMPLE
```

---

## 45. T8 — Regular total-zero-set theorem

### Current status

```text id="znx2ps"
STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF
```

### Statement

For:

[
A(p,t)=a_t(p),
]

if:

[
d_pa_t\neq0
]

at every zero, then:

[
\mathcal Z=A^{-1}(0)
]

is a smooth codimension-one submanifold of (\mathcal M\times I).

### Additional standard consequence

The projection:

[
\pi:\mathcal Z\to I
]

is a submersion under the same spatial regularity condition.

### Not established without more assumptions

* properness;
* local triviality as a fiber bundle;
* global product structure;
* constant topology in a non-proper family.

---

## 46. Regular tube theorem with properness

### Current status

```text id="j8vfzo"
STANDARD CONSEQUENCE REQUIRING HYPOTHESES AND CITATION
MOVED TO PAPER III
```

### Conditional statement

If:

[
\pi:\mathcal Z\to I
]

is a proper submersion, then an Ehresmann-type theorem gives local triviality.

### Remaining obligations

* state boundary assumptions;
* verify properness in each explicit family;
* distinguish local triviality from ambient isotopy.

---

## 47. Z7 — Minimal multi-zero example

### Current status

```text id="7iwdkq"
OPEN PROBLEM FOR PAPER I
MOVED TO PAPER III UNLESS VERIFIED
```

### Entry test

No example may be marked proved until all are verified:

* domain;
* metric;
* assignment;
* singular set;
* flow equation;
* exact zero topology.

### Current assessment

The repository contains promising multi-zero constructions, but no single example has yet been certified under the full target checklist.

---

## 48. General (E_k) construction

### Current status

```text id="wao0uy"
PARTIALLY PROVED / OPEN PROGRAM
MOVED TO PAPER III
```

### Not yet established

* a universal construction for all (k);
* existence under one fixed AES definition;
* uniqueness;
* exact singularity classification;
* compatibility with a common metric normalization.

---

## 49. (E_{\log}) construction

### Current status

```text id="btxszb"
STRUCTURAL PROPOSAL WITH PARTIAL EXPLICIT CONSTRUCTION
MOVED TO PAPER III
```

### Remaining obligations

* define domain and branches;
* verify the flow equation;
* classify zero components;
* determine singular parameters;
* prove tube behavior.

---

## 50. Zero-line bifurcation classification

### Current status

```text id="10t1dx"
OPEN PROBLEM
MOVED TO PAPER III
```

### Required future components

* local normal forms;
* discriminant definition;
* compatibility with the AEG flow;
* boundary and non-proper events;
* birth/death, fold, cusp, and reconnection classification.

---

# Part X. ACS and torsion status

## 51. G1 — ACS definition

### Current status

```text id="67v7ld"
PROVED AS A COHERENT CONSTRUCTION
```

### Established meaning

ACS records:

[
(A,M)
]

as accumulated additive and logarithmic multiplicative charge.

It is a commutative shadow of affine histories.

### Required warning

ACS is not the full expression space and not the evaluated affine group.

---

## 52. T9 — Direct ACS evaluation formula

### Current status

```text id="9elupv"
STANDARD CONSEQUENCE OF THE PROVED AFFINE COCYCLE
REQUIRING AN IN-PAPER PROOF
```

### Target formula

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
]

### Existing support

The current paper proves an equivalent future-weighted formula using the reversed path.

### Remaining obligations

* prove equivalence;
* fix direct-path orientation;
* test against explicit examples.

---

## 53. T10 — Relative torsion independence

### Current status

```text id="gpbtsu"
PROVED AS AN AFFINE-COCYCLE CONSEQUENCE
```

### Statement

If:

[
M_\gamma=M_\delta,
]

then:

[
\nu_x(\gamma)-\nu_x(\delta)
]

is independent of (x).

### Remaining obligation

State the weaker scale-compatibility condition separately from full charge compatibility.

---

## 54. T11 — Boundary-integral formula

### Current status

```text id="l7zbeu"
PARTIALLY PROVED
SIGN CONVENTION AUDIT REQUIRED
```

### Existing proof

The current paper proves the special case comparing a path and its temporal reverse.

### Target extension

For any charge-compatible pair:

[
\gamma,\delta,
]

express relative torsion as a closed weighted contour integral.

### Remaining obligations

* fix orientation;
* use chains for self-intersections;
* verify signs in at least two examples.

---

## 55. T12 — Weighted torsion–Stokes theorem

### Current status

```text id="i7hcuo"
PROVED IN A SPECIAL CASE
STANDARD CONSEQUENCE FOR THE GENERALIZED FORM
SIGN CONVENTION AUDIT REQUIRED
```

### Established special case

Path-versus-reversal torsion equals a boundary integral and a weighted area integral.

### Target generalization

Any charge-compatible pair of histories.

### Remaining obligations

* select the canonical weighted (1)-form;
* define the oriented (2)-chain;
* prove filling independence in the ACS plane;
* separate scale compatibility from endpoint compatibility.

---

## 56. ACS as abelianization shadow

### Current status

```text id="85h5gf"
PROVED AT THE FORMAL-CHARGE LEVEL
STRUCTURAL INTERPRETATION
```

### Established content

The charge map forgets order and records additive and multiplicative totals.

### Required warning

The symbolic history language, evaluated affine group, and free group (F_2) are not automatically identical.

A free-group formulation requires an explicitly chosen formal generator language.

---

# Part XI. Contact and horizontal-curvature status

## 57. T13 — Contact nondegeneracy

### Current status

```text id="zxj4ko"
PROVED
```

### Formula

[
\alpha
======

da-(\mu,du+\lambda a,dv),
]

[
\alpha\wedge d\alpha
====================

\mu\lambda,du\wedge da\wedge dv
]

up to orientation.

### Hypothesis

[
\mu\lambda\neq0.
]

---

## 58. K2/T14 — Horizontal lifts and Legendrian flow

### Current status

```text id="g1ql3n"
PROVED
```

### Established fields

[
D_u=\partial_u+\mu\partial_a,
]

[
D_v=\partial_v+\lambda a\partial_a.
]

A curve tangent to:

[
\cos\theta D_u+\sin\theta D_v
]

satisfies the affine flow equation.

---

## 59. T15 — Horizontal curvature bracket

### Current status

```text id="j4i2yh"
PROVED
```

### Formula

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

### Established interpretation

The horizontal distribution is non-integrable, and the bracket defect is vertical.

---

## 60. K3 — Exact finite commutator formulas

### Current status

```text id="m3cl5d"
PROVED UNDER THE CURRENT FLOW ORDER
SIGN AND COMPOSITION AUDIT REQUIRED
```

### Established open-path defect

[
\mu h(e^{\lambda k}-1).
]

### Established closed-loop drift

An exact exponential formula is present in the current contact section.

### Remaining obligations

* recalculate after C0 is fixed;
* align sign with ACS orientation;
* avoid identifying open and closed finite defects.

---

## 61. K4/T16 — Horizontal covariant differential

### Current status

```text id="bkf0yr"
PROVED ON SCALAR FIELDS
```

### Formula

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
]

Define:

[
\delta_H^2F
:=
(D_uD_vF-D_vD_uF),du\wedge dv.
]

Then:

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

### Required limitation

This is not yet a full graded differential calculus on forms.

Do not claim that an operator literally squares in the de Rham sense unless its extension has been defined.

---

## 62. T17 — Local-global torsion synthesis

### Current status

```text id="ckjht9"
PARTIALLY PROVED
FORMULATION REQUIRED
```

### Established components

* finite affine relative defect;
* ACS weighted-area identity in a special case;
* exact contact commutator formulas;
* infinitesimal horizontal curvature.

### Not yet established as one theorem

A single precise statement separating:

1. exact affine/ACS equality;
2. exact finite contact correction;
3. infinitesimal curvature equality.

### Target recommendation

Present T17 as a synthesis theorem or proposition only after all three levels are stated without conflation.

### Dependency restriction

T17 must not claim literal equality among all finite quantities.

---

## 63. Reeb field and Darboux form

### Current status

```text id="q42t76"
PROVED BY DIRECT CALCULATION
OPTIONAL IN PAPER I
```

### Use

Suitable for an appendix or brief remark.

### Scope warning

The arithmetic significance lies in the chosen coordinates and horizontal frame, not in a new contact-isomorphism class.

---

# Part XII. Paper II analytic status

## Paper II integration update — 2026-08-06

The canonical manuscript `paper-2/aeg-paper-2.tex` now resolves the analytic
inventory below.  This table supersedes the pre-manuscript status descriptions in
Items 64--73, which are retained afterward as provenance for the original open
questions.

| Item | Integrated status | Canonical resolution |
|---|---|---|
| 64. Compatible horizontal complex structure | **PROVED / DATA DECLARED** | On a regular AES surface, the metric and orientation already determine (J).  On the contact space, Paper II explicitly chooses the metric making (D_u,D_v) orthonormal, the compatible rotation, positive contact volume, and test domain.  No contactomorphism-canonicity is claimed. |
| 65. Arithmetic Cauchy--Riemann equations | **PROVED IN TWO DISTINCT SETTINGS** | Surface operators (X_u,X_v) and contact lifts (D_u,D_v) use different notation, measures, and harmonic consequences. |
| 66. Horizontal conformality identities | **PROVED LOCALLY** | The surface CR system gives the equal-length, orthogonality, and nonnegative-Jacobian identities.  No global mapping theorem is inferred. |
| 67. Arithmetic holomorphic coordinate | **PROVED WITH A BRANCH DOMAIN** | On the contact space, (z=u+iv) and (zeta=u+(i/lambda)operatorname{Log}_mu(mu+ilambda a)) are verified CR first integrals on a named half-plane branch. |
| 68. Composition | **PROVED WITH DOMAIN HYPOTHESIS** | Holomorphic postcomposition follows by the chain rule when the image lies in the classical holomorphic domain. |
| 69. Assignment-only fields | **PROVED / CLASSIFIED** | Surface arithmetic-holomorphic fields of the form (H(a)) are constant.  On the basic hyperbolic AES, all harmonic (h(a)) are (C_0+C_1arctan(lambda a/mu)). |
| 70. Factorization and twisted harmonicity | **PROVED WITH MEASURE AND DOMAIN LEVELS** | The manuscript separates raw, exact-drift, formal-adjoint, and closed-operator identities.  Surface holomorphicity implies (Delta_gF=0); contact CR gives separately named vertical/Reeb-twisted equations. |
| 71. Affine--Appell family | **PROVED AS A FILTERED MODULE** | The constant span is not asserted invariant.  The corrected (C^infty(u,v))-module is operator-stable; no Hilbert, Schauder, density, or completeness claim is made. |
| 72. Hyperbolic real function theory | **PROVED ON THE BASIC MODEL** | Paper II proves the normalized Poisson kernel, the compactified-(C_0) Dirichlet theorem, exact Fourier/energy identity, variational Dirichlet-to-Neumann operator, and explicit assignment-dependent families.  General Green, spectral-resolution, and continuation theories remain open. |
| 73. Relation to classical complex analysis | **RESOLVED ON SURFACES; DISTINCT ON CONTACT SPACE** | The surface arithmetic operator differs from the ordinary Riemann-surface operator by a nowhere-zero (U(1)) gauge, so their kernels agree.  The three-dimensional contact-CR branch is not identified with that surface theory. |

### Pre-manuscript inventory retained for provenance

## 64. Compatible horizontal complex structure

### Current status

```text id="bxnysn"
STRUCTURAL PROPOSAL
MOVED TO PAPER II
```

### Required data

Paper II must specify:

* horizontal metric;
* orientation;
* compatible almost-complex structure (J);
* measure;
* operator domains.

### Not established

Uniqueness or contact-canonicity of (J).

---

## 65. Arithmetic Cauchy–Riemann equations

### Current status

```text id="dkk72l"
PROVED AS A FORMAL DEFINITION AFTER CHOOSING A FRAME
FUNCTIONAL-ANALYTIC FRAMEWORK REQUIRED
MOVED TO PAPER II
```

### Current system

[
D_uf=D_vg,
\qquad
D_vf=-D_ug.
]

Equivalent formal operator:

[
\bar\partial_{\mathrm{AEG}}
===========================

\frac12(D_u+iD_v).
]

### Remaining obligations

* justify the selected complex structure;
* define function spaces;
* specify local or global domains.

---

## 66. Horizontal conformality identities

### Current status

```text id="xj42bq"
PROVED FORMALLY
MOVED TO PAPER II
```

These identities follow algebraically from the chosen Cauchy–Riemann system.

They do not establish a global conformal mapping theory.

---

## 67. Arithmetic holomorphic coordinate (\zeta)

### Current status

```text id="ag8jpb"
PARTIALLY PROVED
TYPOGRAPHICAL CORRECTION AND DOMAIN AUDIT REQUIRED
MOVED TO PAPER II
```

### Current formula

The source appears to intend:

[
\zeta(u,v,a)
============

u+\frac{i}{\lambda}\log(\mu+i\lambda a),
]

not a formula beginning with (\nu).

### Remaining obligations

* fix the coordinate typo;
* select a branch of logarithm;
* state the domain;
* verify the Cauchy–Riemann equation under the chosen frame.

---

## 68. Composition of arithmetic holomorphic fields

### Current status

```text id="mmrm1w"
PROVED FORMALLY UNDER THE CHAIN RULE
MOVED TO PAPER II
```

### Limitation

The result is local and depends on the image lying in the domain of a classical holomorphic function.

---

## 69. Rigidity for (a)-only fields

### Current status

```text id="9lc47q"
PROVED UNDER \(\mu>0\)
MOVED TO PAPER II
```

### Statement

An arithmetic holomorphic field depending only on (a) is constant, under the current real-axis and non-vanishing coefficient assumptions.

---

## 70. Factorization and twisted harmonicity

### Current status

```text id="v5pk9e"
PROVED AS A FORMAL OPERATOR IDENTITY
FUNCTIONAL-ANALYTIC INTERPRETATION OPEN
MOVED TO PAPER II
```

### Formula

[
4\partial_{\mathrm{AEG}}\bar\partial_{\mathrm{AEG}}
===================================================

\Delta_H+i\mu\lambda\partial_a
]

under the current sign convention.

### Remaining obligations

* audit signs;
* define (\Delta_H) analytically;
* specify domains;
* determine adjoints and self-adjoint realizations;
* distinguish formal PDE solutions from Hilbert-space theory.

---

## 71. Affine–Appell basis

### Current status

```text id="acgeal"
PARTIALLY PROVED AS AN ALGEBRAICALLY STABLE FAMILY
MOVED TO PAPER II
```

### Established

Certain finite spans are stable under the horizontal operators.

### Not yet established

* completeness;
* basis properties in a function space;
* convergence;
* spectral significance;
* boundary approximation.

The word “basis” must be used cautiously unless linear independence and spanning context are specified.

---

## 72. Hyperbolic real function theory

### Current status

```text id="v0ukd3"
OPEN RESEARCH PROGRAM
MOVED TO PAPER II
```

### Not yet proved as a coherent package

* maximum principle;
* Harnack inequality;
* Green function;
* Poisson kernel;
* Dirichlet or Neumann well-posedness;
* spectral resolution;
* continuation theorem.

Paper II requires at least one nontrivial theorem from this list or an equivalent analytic result.

---

## 73. Relation to classical complex analysis

### Current status

```text id="wsrt16"
OPEN STRUCTURAL QUESTION
```

### Current valid statement

Classical holomorphic functions independent of (a) provide a consistency subfamily under the chosen horizontal complex structure.

### Not established

* equivalence with classical complex analysis;
* categorical deformation;
* universal extension;
* replacement of Euclidean complex analysis.

---

# Part XIII. Paper III singular and tube status

## 74. Stratified singular AES

### Current status

```text id="mmxxh9"
STRUCTURAL PROPOSAL
MOVED TO PAPER III
```

### Remaining obligations

* define strata;
* specify regularity across strata;
* define equivalence of singular models;
* determine admissible metric and assignment singularities.

---

## 75. Discriminant set

### Current status

```text id="2nkpyk"
STANDARD DEFINITION / OPEN DEVELOPMENT
MOVED TO PAPER III
```

### Candidate definition

[
\mathcal D
==========

\left{
t:
\exists p,\
a_t(p)=0,\
d_pa_t=0
\right}.
]

### Remaining obligations

* account for metric singularities;
* account for boundary and non-proper events;
* determine whether parameter derivatives should enter;
* prove stability on the complement.

---

## 76. Regular tube theorem

### Current status

```text id="jban37"
STANDARD CONSEQUENCE WITH PROPERNESS
MOVED TO PAPER III
```

### Conditional result

A proper submersion:

[
\pi:\mathcal Z\to B
]

is locally trivial under the appropriate smooth hypotheses.

### Not established for current AEG families

Properness and compactness must be checked model by model.

---

## 77. Tube topology change requires singularity

### Current status

```text id="r039wk"
PARTIALLY PROVED AS A CONDITIONAL PRINCIPLE
```

### Valid conditional statement

Within a proper smooth submersion family, fiber topology is locally constant.

### Required qualification

Topology can also change through:

* failure of properness;
* boundary escape;
* domain change;
* metric degeneration;
* projective chart transition.

Thus “topology change implies (da=0)” is too strong without excluding these mechanisms.

---

## 78. Monodromy and braid representation

### Current status

```text id="de4njy"
STRUCTURAL PROPOSAL
MOVED TO PAPER III
```

### Required future theorem

For an appropriate parameter-space complement:

[
\pi_1(\mathcal P\setminus\mathcal D)
\longrightarrow
S_n
\quad\text{or}\quad
B_n.
]

### Not yet established

* finite number of zero branches;
* global labeling;
* braid-group lift;
* invariance under parameter homotopy.

---

## 79. Threading construction

### Current status

```text id="c1o743"
STRUCTURAL PROPOSAL WITH EXAMPLES
MOVED TO PAPER III
```

### Remaining obligations

Distinguish:

* zero tube;
* an embedded line inside the tube;
* an externally added thread;
* monodromy-generated braid;
* braid closure.

No invariant status is currently authorized.

---

## 80. Knot invariant

### Current status

```text id="d1o3ur"
OPEN PROBLEM
```

### Not established

* isotopy invariance;
* Markov invariance;
* normalization;
* independence from choices;
* distinction beyond Alexander/Burau data.

### Publication rule

May appear only as a conjectural program until at least one invariance theorem is proved.

---

## 81. New invariant beyond Alexander/Burau

### Current status

```text id="1yc3xn"
OPEN PROBLEM
```

This remains the decisive success criterion of the knot direction.

No claim of novelty is authorized yet.

---

# Part XIV. Paper IV projective-condensation status

## 82. History groupoid

### Current status

```text id="oi9310"
STRUCTURAL PROPOSAL WITH A COHERENT BASIC DEFINITION
MOVED TO PAPER IV
```

### Remaining obligations

* fix objects and arrows;
* define partial-domain composition;
* distinguish ordinary and projective action groupoids;
* define the evaluation functor precisely.

---

## 83. Group-valued relative projective defect

### Current status

```text id="7la5ye"
PROVED AS A DEFINITION
MOVED TO PAPER IV
```

### Definition

[
\mathcal K(\gamma,\delta)
=========================

\rho(\delta)^{-1}\rho(\gamma).
]

### Remaining questions

* gauge or reference dependence;
* endpoint stabilizer class;
* conjugacy invariants;
* geometric holonomy interpretation.

---

## 84. Regular bivaluation as ordered distinct points

### Current status

```text id="wy54s2"
PROVED AS A DEFINITION
MOVED TO PAPER IV
```

[
\operatorname{Biv}^{\mathrm{reg}}_K
===================================

\mathbb P^1(K)\times\mathbb P^1(K)\setminus\Delta.
]

---

## 85. Bivaluations as rank-one idempotents

### Current status

```text id="1k0gy4"
PROVED
MOVED TO PAPER IV
```

### Established bijection

Ordered pairs of distinct projective lines correspond to rank-one idempotent projectors on (K^2).

### Remaining obligation

Normalize point/covector coordinate conventions consistently.

---

## 86. Covariant and contravariant transport

### Current status

```text id="y6mcnp"
PROVED
MOVED TO PAPER IV
```

### Established transformation

[
v\mapsto Gv,
\qquad
\varphi\mapsto\varphi G^{-1},
]

[
\Pi\mapsto G\Pi G^{-1}.
]

### Required warning

This duality is not identical to operand-slot chirality.

---

## 87. Quotient tower

### Current status

```text id="4upbft"
PROVED AS A HOMOGENEOUS-SPACE IDENTIFICATION
MOVED TO PAPER IV
```

### Established statements

For suitable stabilizers:

[
G/H
\cong
\operatorname{Biv}^{\mathrm{reg}}_K,
]

[
G/B_\pm
\cong
\mathbb P^1(K).
]

### Remaining obligation

Specify reference pair and stabilizers precisely.

---

## 88. Principal (H)-bundle and process residue

### Current status

```text id="0rcdn0"
PARTIALLY PROVED / STRUCTURAL PROPOSAL
MOVED TO PAPER IV
```

### Established standard structure

[
G\to G/H
]

is a homogeneous principal-bundle construction under appropriate group assumptions.

### Not yet established

A canonical arithmetic interpretation of the fiber as process residue.

Any (H)-valued coordinate requires a chosen reference lift.

---

## 89. Concept–predicate interpretation

### Current status

```text id="6a0g6n"
STRUCTURAL PROPOSAL
MOVED TO PAPER IV
```

### Prohibited claim

The rank-one projector theorem alone does not prove that projective points and copoints are semantic concepts and predicates.

That interpretation requires an independent semantic model.

---

## 90. Projective condensation

### Current status

```text id="7afh4n"
STRUCTURAL PROPOSAL WITH A PROVED QUOTIENT SKELETON
MOVED TO PAPER IV
```

### Established skeleton

[
\text{marked history}
\to
G
\to
G/H
\to
G/B.
]

Each map forgets information.

### Not yet established

* a universal numerical measure of lost information;
* a canonical reconstruction;
* complexity consequences;
* a unique condensation functor for all expression systems.

---

## 91. Finite-field counting model

### Current status

```text id="iz4pqh"
PARTIALLY AUDITED
INTEGRATION AUDIT REQUIRED
MOVED TO PAPER IV
```

### Required action

Before publication:

* recompute group and quotient cardinalities;
* state exclusions for coincident pairs;
* check characteristic-(2) cases;
* verify stabilizer sizes.

No count should be imported solely from the working-note abstract.

---

## 92. Telescoping obstruction

### Current status

```text id="vz8jd8"
PROVED IN THE WORKING NOTE, SOURCE AUDIT REQUIRED
MOVED TO PAPER IV
```

### Meaning

An endpoint-defined exact transport may telescope and erase process information.

### Remaining obligation

Extract the exact proposition and proof from the note and state its hypotheses.

---

# Part XV. Paper IV complexity status

## 93. Complexity taxonomy

### Current status

```text id="v9p9ad"
STRUCTURAL PROPOSAL
```

Candidate quantities include:

[
C_{\mathrm{syn}},
\quad
C_{\mathrm{word}},
\quad
C_{\mathrm{op}},
\quad
C_{\mathrm{geo}},
\quad
C_{\mathrm{time}},
\quad
C_{\mathrm{space}}.
]

### Remaining obligation

Each quantity needs:

* a domain;
* an encoding;
* a generating set or metric;
* an invariance class;
* a cost model.

---

## 94. Complexity as path length

### Current status

```text id="ofqo7z"
CONDITIONAL STRUCTURAL PROPOSAL
```

### Valid conditional form

Given a state graph, generating set, admissible transitions, and cost per edge, shortest-path length may represent a computational cost.

### Unsupported general form

“All computational complexity is geometric path length.”

---

## 95. Representation complexity precedes time and space complexity

### Current status

```text id="n3vk85"
STRUCTURAL HYPOTHESIS
```

### Research content

Time and space complexity may be projections of a richer representation geometry.

### Not established

A general theorem identifying them.

---

## 96. Noncommutativity causes exponential representation growth

### Current status

```text id="hxkxs5"
UNSUPPORTED AND EXCLUDED AS A GENERAL THEOREM
```

### Reason

Noncommutative groups can have polynomial growth, and commutative encodings can still produce large search spaces.

### Permitted replacement

Study growth for explicitly defined groups, semigroups, languages, or rewriting systems.

---

## 97. Hyperbolicity is forced by expression complexity

### Current status

```text id="oj0xbm"
UNSUPPORTED AND EXCLUDED AS A GENERAL THEOREM
```

### Permitted status

Research motivation or model-specific conjecture.

A proof would require:

* a defined expression-state metric;
* a quasi-isometry or curvature theorem;
* explicit hypotheses on the operation system.

---

## 98. Hyperbolicity implies computational hardness

### Current status

```text id="r43pvk"
UNSUPPORTED AND EXCLUDED
```

No such unconditional implication is authorized.

---

## 99. Time-space complexity equals representation complexity

### Current status

```text id="fq69b1"
OPEN PROBLEM / RESEARCH HYPOTHESIS
```

### Required future work

* define representation volume;
* connect it to memory states;
* specify recomputation tradeoffs;
* prove model-specific inequalities.

---

## 100. Pebble-game and resource-geometry program

### Current status

```text id="ayr4ne"
STRUCTURAL PROPOSAL WITH STANDARD EXTERNAL MODELS
MOVED TO PAPER IV
```

### Permitted use

Use pebble games as an explicit computational model.

### Required proof

Any claimed AEG correspondence must be defined and proved; analogy is insufficient.

---

## 101. Computational mass and induced curvature

### Current status

```text id="wb8b0c"
UNSUPPORTED ANALOGY
ARCHIVAL OR MOTIVATIONAL USE ONLY
```

It must not appear as a theorem unless a metric field equation or equivalent formal mechanism is defined.

---

## 102. Algorithmic thermodynamics analogy

### Current status

```text id="pcukwe"
STRUCTURAL MOTIVATION
```

May motivate a model but does not currently produce a proved AEG theorem.

---

# Part XVI. Explicit rejection register

## 103. Rejected formulations

The following formulations must be removed or rewritten wherever they appear.

### R1

> Every arithmetic expression has a unique evaluation history.

```text id="ta2oy5"
UNSUPPORTED AND FALSE IN GENERAL
```

Only sequential trees have a unique legal internal evaluation order.

---

### R2

> Threadlike means every left child is a leaf.

```text id="qxnkdu"
REJECTED AS CURRENT CANONICAL DEFINITION
```

The wording conflicts with examples or depends on tree orientation.

Replace with the intrinsic sequential-tree and marked-spine definition.

---

### R3

> Existing AEG is the full geometry of arithmetic expressions.

```text id="yd0mqt"
REJECTED
```

Existing continuous AEG is an affine/Borel sector of the bilateral projective semantics.

---

### R4

> Projective continuation resolves division by zero in ordinary arithmetic.

```text id="l9lbna"
REJECTED
```

It changes the semantic category and must retain domain labels.

---

### R5

> The contact form uniquely forces arithmetic holomorphicity.

```text id="hez1ca"
REJECTED
```

A horizontal metric, orientation, and compatible complex structure are additional choices.

---

### R6

> (\delta) is an ordinary nilpotent differential.

```text id="kn3pqc"
REJECTED
```

On scalar fields:

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

---

### R7

> A smooth non-degenerate AES can have an isolated regular zero.

```text id="1u2q51"
REJECTED
```

This contradicts the regular-zero theorem when (\mu\neq0).

---

### R8

> Every smooth total zero set is a globally trivial tube.

```text id="mdrm8q"
REJECTED
```

Properness or equivalent hypotheses are required.

---

### R9

> A tube with a thread defines a knot invariant.

```text id="6ak4h0"
REJECTED AS AN ESTABLISHED CLAIM
```

Invariance and normalization remain open.

---

### R10

> Noncommutativity implies hyperbolic geometry and exponential complexity.

```text id="x3mqr1"
REJECTED
```

Each implication requires independent hypotheses and proof.

---

# Part XVII. Paper I completion gates

## 104. Gate A — Foundational syntax

Paper I may mark the syntax branch complete only when:

* [ ] C0 and C1 are fixed;
* [ ] T1 is integrated and checked;
* [ ] the marked-history correspondence is proved;
* [ ] mirror and reversal are separated;
* [ ] the old threadlike definition is removed or explicitly superseded.

---

## 105. Gate B — Projective and affine semantics

Complete only when:

* [ ] elementary matrices are domain-audited;
* [ ] T2 is checked under the final composition convention;
* [ ] P3 and P4 are stated precisely;
* [ ] ordinary and projective semantics are separated;
* [ ] no bivaluation semantics remains in Paper I’s main theory.

---

## 106. Gate C — Affine cocycle and flow

Complete only when:

* [ ] T3 and T4 use the final convention;
* [ ] relative affine defect is distinguished from endpoint equality;
* [ ] T5 has one primary derivation;
* [ ] flow parameters and accumulated coordinates are not overloaded;
* [ ] eikonal dependence on the metric is explicit.

---

## 107. Gate D — Hyperbolic model

Complete only when:

* [ ] E1 is fixed;
* [ ] E2 is derived;
* [ ] T6 is proved under final normalization;
* [ ] curvature and Laplacian formulas are checked;
* [ ] model numbering is stable;
* [ ] no uniqueness claim remains without proof.

---

## 108. Gate E — Zero geometry

Complete only when:

* [ ] T7 is proved;
* [ ] boundary qualifications are explicit;
* [ ] Z3 is defined;
* [ ] the isolated-zero model is reclassified;
* [ ] T8 is not overstated as global tube triviality;
* [ ] unverified multi-zero examples are excluded or moved.

---

## 109. Gate F — ACS

Complete only when:

* [ ] T9 is derived directly from the affine cocycle;
* [ ] scale and charge compatibility are distinguished;
* [ ] T10–T12 have one sign convention;
* [ ] reversal is only a special case;
* [ ] chain language is used where paths self-intersect.

---

## 110. Gate G — Contact curvature

Complete only when:

* [ ] T13–T16 are checked;
* [ ] open and closed finite defects are separated;
* [ ] (\delta_H) is restricted to its defined scope;
* [ ] T17 is formulated without false finite equalities;
* [x] analytic complex-structure claims have moved to Paper II.

---

# Part XVIII. Status-update protocol

## 111. Required fields for changing a status

Any task changing a claim’s status must record:

```markdown id="5rm6s2"
## Status change S-XXXX

- Claim ID:
- Previous status:
- New status:
- Exact statement:
- Hypotheses:
- Proof location:
- Verification performed:
- Downstream nodes affected:
- Papers affected:
- Reviewer:
- Date:
```

---

## 112. Promotion rules

A claim may be promoted:

### From `STRUCTURAL PROPOSAL` to `CONJECTURE`

Only after it has a precise statement and hypotheses.

### From `CONJECTURE` to `PARTIALLY PROVED`

Only after a nontrivial general subcase is proved.

### From `PARTIALLY PROVED` to `PROVED`

Only after the full statement is proved.

### From `STANDARD CONSEQUENCE` to `PROVED`

Only after the target paper contains a proof or an adequate precise citation.

### From `COMPUTATIONALLY VERIFIED EXAMPLE` to `PROVED`

Only after a general proof is supplied; more examples are not sufficient.

---

## 113. Downgrade rules

A status must be downgraded if:

* a missing hypothesis is discovered;
* a proof uses a later result circularly;
* a sign or composition convention invalidates the statement;
* a model is singular where regularity was assumed;
* a numerical example was mistaken for a theorem;
* a projective argument was used for ordinary arithmetic without domain control.

Downgrading is a correction, not a failure of the restructuring process.

---

# Part XIX. Final status summary

## 114. Paper I core after integration

As of 2026-08-06, the canonical Paper I source contains statements and proofs for:

* the sequential-tree classification and the marked planar tree--bounded-history
  bijection;
* ordinary and projective evaluation, arbitrary-field \(PGL_2(K)\) generation, and
  the affine/Borel image;
* target- and source-frame affine cocycles, Maurer--Cartan forms, relative defect,
  and continuous affine flow;
* the intrinsic regular-AES definition and canonical arithmetic-frame equivalence;
* the normalized invariant affine metric, complete hyperbolic model, curvature,
  Laplacian, regular-zero theorem, singular-AES framework, isolated singular zero,
  and total-zero-set submersion;
* direct ACS evaluation and generalized two-history weighted Stokes for
  charge-compatible positive add--scale histories;
* contact nondegeneracy, horizontal lifts, exact open and source-normalized closed
  defects, scalar horizontal curvature, and their layered finite/infinitesimal
  synthesis.

The analytic, multi-zero/tube, projective-condensation, and complexity programmes
retain the later-paper statuses recorded below.  They are not dependencies of this
integrated Paper I core.

---

## 115. Later-paper status at present

### Paper II

The canonical mathematical-review manuscript now contains a proved function theory
on the basic hyperbolic AES: measure-sensitive surface and contact operators,
factorizations with declared domains, a Poisson--Dirichlet theorem, an exact
Dirichlet-to-Neumann energy identity on Schwartz data, and explicit
assignment-dependent families.  General Green kernels, spectral completeness,
contact boundary representations, and singular continuation remain open.

### Paper III

Contains significant constructions and geometric intuition, but the general multi-zero, discriminant, tube, and knot theories remain incomplete.

### Paper IV

Contains a comparatively strong algebraic projective core, including projectors and homogeneous quotients, but condensation semantics and computational-complexity consequences remain structural proposals.

---

## 116. Governing principle

No claim may be strengthened merely because it fits the intended architecture.

The restructuring must preserve the following distinction:

[
\boxed{
\text{what has been imagined}
\neq
\text{what has been constructed}
\neq
\text{what has been verified}
\neq
\text{what has been proved}.
}
]

A successful Paper I will be narrower than the full AEG vision, but mathematically stable enough for Papers II–IV to build upon without redefining its objects or retracting its claims.

---

# Part XX. Paper I integration status changes (2026-08-06)

These entries supersede the integration-audit qualifiers in the earlier node records
for the canonical source `paper-1/aeg-paper-1.tex`, `paper-1/sections/`, and
`paper-1/appendices/`.  They do not
promote any later-paper programme.

## Status change S-0001

- **Claim ID:** T1; marked-tree-to-history correspondence; mirror/reversal/inverse
  distinctions.
- **Previous status:** T1 `PROVED / INTEGRATION AUDIT REQUIRED`; correspondence
  `PROVED IN ESSENCE / STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`; symmetry
  distinctions `PROVED BY DEFINITION AND EXAMPLE`.
- **New status:** `PROVED WITH STATED HYPOTHESES`.
- **Exact statement:** finite binary trees have a unique internal evaluation order
  exactly when their internal dependency poset is a chain, equivalently when their
  internal vertices form one spine; fully labelled marked planar sequential trees are
  in bijection with bounded marked spinal histories.  Planar mirror, temporal
  reversal, and path inverse are distinct operations.
- **Hypotheses:** finite planar binary tree; all labels and the innermost accumulator
  retained for the bijection; invertibility on a declared domain for path inverse.
- **Proof location:** Section 2 and Appendix A.
- **Verification performed:** independent algebra review; global hierarchy review;
  explicit counterexamples for equality levels.
- **Downstream nodes affected:** S1--S5, P1--P2.
- **Papers affected:** Paper I; exported syntax interface to Paper IV.
- **Reviewer:** independent algebra, mathematical, and scope reviews.
- **Date:** 2026-08-06.

---

## Arithmetic--automorphic integration update — 2026-08-06

| ID | Claim | Status | Required boundary |
|---|---|---|---|
| P1-H1 | (T_{\sqrt2}) and (J=-1/z) are projective evaluations of explicit bilateral arithmetic contexts | **PROVED WITH ORDINARY/PROJECTIVE DOMAIN DISTINCTION** | The history word may cross (0) or (\infty) projectively without being an ordinary admissible evaluation. |
| P1-H2 | Their projective image is the (q=4) Hecke triangle group | **PROVED / STANDARD GROUP IDENTIFICATION** | Equality is at the operator quotient; histories are not identified with group elements or tiles before quotienting. |
| P1-Z9 | A connected complete boundaryless regular AES splits as (Z(a)\times\mathbb R) | **PROVED WITH STATED HYPOTHESES** | The product is diffeomorphic, not necessarily isometric; a boundary or incomplete metric invalidates the global-flow argument. |
| P2-A1 | The planar rotated-imaginary-part target is a harmonic regular AES with the printed curvature law | **PROVED BY DIRECT CALCULATION** | (\mu\ne0); the metric and phase are explicitly declared. |
| P2-A2 | The logarithmic cylindrical target is a regular AES | **PROVED BY DIRECT CALCULATION** | Use the linear limiting definition when (\lambda=0). |
| P2-A3 | Holomorphic local diffeomorphisms pull back either target to a regular AES | **PROVED** | The derivative must be nonzero; no statement is made at a branch point. |
| P3-S1 | A holomorphic critical point in the pullback is locally essential | **PROVED WITH STATED HYPOTHESES** | The target assignment must obey the positive-(\mu^2) eikonal identity and its zero line must meet the critical value for the prong conclusion. |
| P3-S2 | Local degree (m) gives a (2m)-prong zero germ and cone angle (2\pi m) | **PROVED BY LOCAL NORMAL FORM AND METRIC CALCULATION** | This is a singular metric completion, not a smooth regular AES point. |
| P3-S3 | A normalized Hauptmodul has orbifold signature ((2,4,\infty)), finite ramification indices (2) and (4), and a simple pole at the cusp | **STANDARD EXTERNAL INPUT REQUIRING CITATION** | The chosen finite branch values and cusp normalization must be printed. |
| P3-S4 | The square-root/Cayley/cylindrical construction has zero set (\beta^{-1}([0,1])) and four-valent (4\pi)-cone vertices upstairs | **PROVED CONDITIONAL ON P3-S3** | The sign character is explicit.  The completed full-orbifold length quotient is complete with an infinite-distance cusp and coarse angle (\pi) at each elliptic image; properness and tube conclusions are not automatic. |
| P3-R1 | Prime relative divisors normalize to finite covers away from discriminant and bad fibers | **STANDARD CONSEQUENCE WITH FINITENESS HYPOTHESES** | Arithmetic and geometric irreducibility must be separated. |
| P3-R2 | Galois, inertia, reduction, and Frobenius may decorate the geometric sheets of an integral family | **STANDARD ARITHMETIC FRAMEWORK** | It applies only after a ring/field of definition and integral model are declared. |
| P3-R3 | Every suitable AEG history has a functorial arithmetic relative zero divisor | **STRUCTURAL PROPOSAL / OPEN PROBLEM** | No existence, uniqueness, completeness, or Markov descent claim is authorized. |

### Abstract-level authorization

Papers I and II may advertise only their proved exports.  Paper III may advertise
the branched-pullback theorem and the exact (q=4) automorphic example after their
proofs and citations are present.  It may describe the history-to-divisor map only
as the principal open naturality problem.

### Number-theoretic limitation

The (q=4) model is defined over the Hecke arithmetic associated with
(\mathbb Q(\sqrt2)), but it does not demonstrate nonunique factorization in
(\mathbb Z[\sqrt2]).  A factorization-theoretic version of inequivalent zero
histories requires a separate integral model, preferably with nontrivial ideal
class or factorization data.

## Status change S-0002

- **Claim ID:** elementary projective matrices; T2; P3--P4; A1/T3; T4; A2--A4;
  T5; F2--F3.
- **Previous status:** proved nodes carried domain, sign, normalization, or integration
  audits; T5 was `PROVED WITH STATED CONVENTIONS / INTEGRATION AUDIT REQUIRED`.
- **New status:** `PROVED WITH STATED HYPOTHESES`.
- **Exact statement:** non-degenerate bilateral contexts act on \(\mathbb P^1(K)\)
  and generate \(PGL_2(K)\); the elementary contexts fixing infinity map onto the
  affine Borel subgroup; chronological affine histories satisfy both cocycle formulas
  and the declared Maurer--Cartan identities; their Lie algebra gives the continuous
  affine flow and metric-dependent eikonal law.
- **Hypotheses:** \(K\) a field; matrices non-degenerate; affine multipliers nonzero;
  continuous theory over \(\operatorname{Aff}^+(1,\mathbb R)\); ordinary and
  projective domains kept separate.
- **Proof location:** Sections 3--5 and Appendices A--B.
- **Verification performed:** arbitrary-characteristic decomposition checked;
  chronological matrix order, source/target frames, and elementary defect signs
  independently recomputed.
- **Downstream nodes affected:** P1--P5, T2--T5, F1--F5.
- **Papers affected:** Paper I; algebraic export to Paper IV.
- **Reviewer:** independent algebra, torsion/contact, and mathematical reviews.
- **Date:** 2026-08-06.

## Status change S-0003

- **Claim ID:** E1--E6; T6--T8; Z2--Z5.
- **Previous status:** E1 and Z3 `STRUCTURAL PROPOSAL`; E2, E3, T7, Z2, and T8
  required in-paper proofs; T6 and E6 required normalization audits; Z4 was
  `PARTIALLY PROVED / RECLASSIFICATION REQUIRED`.
- **New status:** `PROVED WITH STATED HYPOTHESES`.
- **Exact statement:** the intrinsic regular-AES eikonal definition is equivalent to
  its canonical oriented frame; the normalized affine group yields a complete
  hyperbolic model with \(K=-\lambda^2\) and
  \(\Delta a=2\lambda^2a\); zero is a regular value; the disc-center example is a
  singular AES with a smooth metric and non-\(C^1\) assignment; a spatially regular
  parameter family has a smooth total zero set with submersive projection.
- **Hypotheses:** oriented smooth surface and Riemannian metric; \(\mu\ne0\);
  \(\mu,\lambda>0\) for the displayed hyperbolic normalization; zero theorem on a
  boundaryless surface or in the interior; singular set closed nowhere dense and
  locally essential; no global tube claim without properness.
- **Proof location:** Sections 5--7 and Appendix C.
- **Verification performed:** frame signs, group invariance, metric scaling,
  curvature, Laplacian, isolated-disc regularity, and tangent-space submersion proof
  independently recomputed.
- **Downstream nodes affected:** E1--E6, T6--T8, Z2--Z6.
- **Papers affected:** Paper I; definition exports to Papers II--III.
- **Reviewer:** independent geometry, algebra, mathematical, and scope reviews.
- **Date:** 2026-08-06.

## Status change S-0004

- **Claim ID:** G1; T9--T12.
- **Previous status:** G1 coherent; T9 required an in-paper proof; T11 was partially
  proved with a sign audit; T12 was proved only for a special case.
- **New status:** `PROVED WITH STATED HYPOTHESES`.
- **Exact statement:** every positive add--scale history has the direct ACS evaluation
  formula; scale-compatible pairs have a seed-independent target-frame translation
  defect; charge-compatible pairs satisfy the weighted boundary and Stokes formulas
  for arbitrary signed singular chains.
- **Hypotheses:** histories are chronological words in
  \(\mathsf A_p(x)=x+p\) and \(\mathsf M_q(x)=e^qx\); Stokes pairs have equal
  additive and logarithmic terminal charges; orientation is \(dA\wedge dM\).
- **Proof location:** Section 8 and Appendix D.
- **Verification performed:** direct one-step and two-step evaluation, rectangle sign,
  chain orientation, filling independence, and add--scale quantifier scope reviewed
  independently.
- **Downstream nodes affected:** G1--G3, T9--T12, T17.
- **Papers affected:** Paper I.
- **Reviewer:** independent geometry, torsion/contact, mathematical, and scope
  reviews.
- **Date:** 2026-08-06.

## Status change S-0005

- **Claim ID:** T13; K2/T14; T15; K3; K4/T16; T17.
- **Previous status:** T13--T15 proved; K3 retained sign/composition audits; K4/T16
  was proved on scalars; T17 was `PARTIALLY PROVED / FORMULATION REQUIRED`.
- **New status:** `PROVED WITH STATED HYPOTHESES`.
- **Exact statement:** for \(\mu\lambda\ne0\), the propagation form is contact;
  its horizontal lifts realize the affine flow and have bracket
  \(\mu\lambda\partial_a\); the scalar horizontal curvature formula holds; the
  exact target-frame open defect, source-normalized closed drift, and common
  infinitesimal density satisfy the three separately stated synthesis identities.
- **Hypotheses:** real constants; contact assertion only for
  \(\mu\lambda\ne0\); \(\delta_H^2\) only denotes the declared antisymmetrized
  scalar operator, not a graded nilpotent differential.
- **Proof location:** Section 9 and Appendix D.
- **Verification performed:** wedge orientation, bracket sign, open and closed flow
  compositions, frame conversion, and two-variable limit independently recomputed.
- **Downstream nodes affected:** K1--K4, T13--T17.
- **Papers affected:** Paper I; scalar horizontal interface to Paper II.
- **Reviewer:** independent geometry, torsion/contact, mathematical, and scope
  reviews.
- **Date:** 2026-08-06.

## Status change S-0006

- **Claim ID:** Paper II Items 64--73; P2-T1--P2-T9 in the Paper II source audit.
- **Previous status:** compatible contact analytic data were structural proposals;
  CR and factorization statements were formal or partially proved; the
  affine--Appell family lacked a correct ambient structure; hyperbolic real function
  theory and its relation to classical complex analysis remained open.
- **New status:** `PROVED WITH STATED HYPOTHESES` on the declared regular-surface,
  normalized-contact, and basic-hyperbolic settings; general boundary, Green,
  spectral-completeness, contact-representation, and singular-continuation claims
  remain `OPEN`.
- **Exact statement:** Riemannian area determines the structure-coefficient drift and
  the surface Laplace--Beltrami adjoints; the surface arithmetic CR operator is a
  unitary gauge of the Riemann-surface operator and its kernel is harmonic; positive
  contact volume determines a distinct variational sub-Laplacian and Reeb-twisted CR
  factorization; the corrected affine--Appell object is a finite filtered module; on
  the complete basic hyperbolic AES, the transported Poisson kernel solves the
  compactified `C_0` Dirichlet problem uniquely, its Schwartz-data variational
  conormal is `|D_x|`, its energy is the homogeneous `H^{1/2}` quadratic form, and
  explicit assignment-dependent holomorphic, harmonic, and contact-CR families are
  constructed.
- **Hypotheses:** real constants with `mu != 0` on a regular AES; `mu lambda != 0`
  for contact nondegeneracy; the declared normalized horizontal metric, rotation,
  positive contact measure, and test/Friedrichs domains; `mu,lambda>0` for the global
  hyperbolic model; `C_0`, Schwartz, Sobolev, or branch-domain hypotheses as stated
  theorem by theorem.
- **Proof location:** Paper II Sections 2--7 and Appendices A--C.
- **Verification performed:** every frame, adjoint, drift, factorization, gauge,
  Poisson, Fourier, conormal, energy, logarithmic, and finite upward-sweep formula was
  independently recomputed; labels and citations were checked; LaTeX/BibTeX built a
  clean PDF; all pages were rendered and visually inspected; independent
  cross-branch mathematical and scope reviews were completed.
- **Downstream nodes affected:** the Paper II analytic interface and possible future
  analytic tools for Paper III; no Paper III or Paper IV theorem is imported.
- **Papers affected:** Paper II; Paper I remains unchanged apart from the documented
  export interface.
- **Reviewer:** independent surface/operator, contact/boundary, whole-manuscript
  mathematics, and scope/provenance reviews.
- **Date:** 2026-08-06.

## Status change S-0007

- **Claim ID:** Paper III tube, multi-zero, discriminant, braid, logarithmic, and
  affine-filter results.
- **Previous status:** no certifiable general multi-zero, `E_k`, or `E_log` model;
  proper tubes, discriminants, finite-root braids, threading, Markov descent, and
  knot invariants were conditional or open.  The discussion-level resonant twisted
  affine class was open.
- **New status:** the results listed below are `PROVED WITH STATED HYPOTHESES`;
  natural threading, AEG Markov descent, and separation beyond Alexander/Burau
  remain `OPEN`.
- **Exact proved statements:**
  1. every smooth surface submersion is a regular AES for an explicit conformal
     metric, and every smooth function with closed nowhere-dense critical set gives
     a singular AES off that set;
  2. descriptive parallel models realize every finite zero-component count, and
     the exponential-cover model realizes countably many sheets as two downstairs
     zero components with deck action;
  3. vertical zero-section transversality gives a smooth incidence and submersive
     projection, while properness gives a smooth bundle;
  4. with a smooth global vertical orientation, a compact boundaryless real zero
     tube over `S^1` is a disjoint union of tori; the compact helical family computes its interval permutation, annular
     components, logarithmic shifts, and boundary homology;
  5. conformal Morse families realize definite birth/death and indefinite
     reconnection, while a transverse simple complex polynomial discriminant has
     local root model `w^2=tau`;
  6. square-free arithmetic-holomorphic polynomial families have proper finite root
     coverings and realize every braid on the basic hyperbolic AES;
  7. logarithmic root endpoint shifts obey the printed lift-gauge law and have
     invariant cycle sums;
  8. stateless additive braid scalars collapse to writhe and to zero under compatible
     two-sided Markov stabilization; fixed-multiplier affine torsion is an ordinary
     coboundary;
  9. finite-field resonant affine torsion is a nonzero twisted quandle cohomology
     class, but its classical planar state sum is an Alexander-extension obstruction
     state sum and equals the coloring count.
- **Hypotheses:** exactly those printed theorem by theorem in Paper III; in
  particular `mu != 0`, vertical transversality, properness and neat boundary where
  invoked, square-free monic complex polynomials for braid monodromy, and finite
  field with `t != 1` for the resonant theorem.
- **Proof location:** Paper III Sections 2--8 and Appendices A--C.
- **Provenance correction:** the multi-zero, logarithmic, and helical formulas are
  new audited constructions in Paper III, not migrations of a missing historical
  `E_k` or `E_log` theorem.  Historical ambient-tube notes remain motivation only.
- **Claims deliberately not promoted:** canonical singular classification;
  completeness of conformal models; intrinsic thread selection; a general
  real-assignment-to-braid functor; a new knot invariant; any separation beyond
  Alexander/Burau; an associator interpretation of the variable-multiplier anomaly.
- **Papers affected:** Paper III; Paper I and Paper II are imported without changing
  their theorems.
- **Date:** 2026-08-06.
