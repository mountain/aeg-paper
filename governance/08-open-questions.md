# Open Questions and Decision Register

**File:** `governance/08-open-questions.md`
**Status:** Authoritative issue register
**Version:** 1.1
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`
* `governance/04-current-to-target-map.md`
* `governance/05-mathematical-status.md`
* `governance/06-editorial-rules.md`
* `governance/07-acceptance-checklist.md`

**Applies to:** Open mathematical, structural, editorial, and migration questions affecting Papers I–IV.

---

## 1. Purpose

This document records unresolved questions that must not be settled silently during restructuring.

It distinguishes:

* decisions that block Paper I;
* proof obligations that block dependent theorems;
* notation and convention choices;
* model-classification questions;
* optional material whose inclusion depends on verification;
* research questions assigned to Papers II–IV.

An item remains open until it has:

1. a recorded decision or proof;
2. an identified source change;
3. a status update in `05-mathematical-status.md`;
4. propagation to all affected documents and theorem nodes.

---

# Part I. Issue protocol

## 2. Priority levels

### `P0 — Blocking`

Paper I cannot be mathematically closed until the issue is resolved.

### `P1 — High`

The issue does not block all writing, but blocks one chapter, theorem branch, abstract claim, or migration decision.

### `P2 — Medium`

The issue affects exposition, optional theorems, appendices, or later-paper interfaces.

### `P3 — Research`

The issue belongs primarily to Papers II–IV or later research and does not block Paper I if properly deferred.

---

## 3. Issue states

Use one of:

* `OPEN`
* `UNDER REVIEW`
* `DECISION PROPOSED`
* `PROOF IN PROGRESS`
* `RESOLVED`
* `DEFERRED TO PAPER II`
* `DEFERRED TO PAPER III`
* `DEFERRED TO PAPER IV`
* `REJECTED`
* `DUPLICATE`

---

## 4. Required issue fields

Each issue should contain:

* **ID**
* **Priority**
* **State**
* **Question**
* **Why it matters**
* **Current evidence**
* **Default rule while open**
* **Resolution condition**
* **Affected files**
* **Affected theorem nodes**
* **Owner**
* **Decision record**

---

## 5. Closing an issue

When an issue is resolved, append:

```markdown
### Resolution

- Decision:
- Mathematical justification:
- Source changes:
- Status changes:
- Downstream nodes rechecked:
- Reviewer:
- Date:
```

Do not delete resolved issues. They form the decision history of the restructuring.

---

# Part II. Paper I blocking questions

## OQ-001 — Canonical definition of a regular AES

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

What is the canonical primitive definition of a regular arithmetic expression space?

Candidate forms include:

#### Option A — Eikonal definition

[
\mathfrak E=(\mathcal M,g,a;\mu,\lambda),
\qquad
|\nabla a|_g^2=\mu^2+\lambda^2a^2.
]

#### Option B — Framed-flow definition

A surface equipped with distinguished additive and multiplicative directions such that:

[
da(X_u)=\mu,
\qquad
da(X_v)=\lambda a.
]

#### Option C — Compatible combined definition

A framed Riemannian surface satisfying both the directional flow and metric compatibility.

### Why it matters

This definition controls:

* the logical status of the eikonal equation;
* the generality of the regular-zero theorem;
* whether the metric is primitive or derived;
* the interface to Paper II;
* the interface to singular AES in Paper III.

### Current evidence

The current paper alternates between flow-first and eikonal-first formulations.

The contact model naturally supplies preferred horizontal directions, while the upper-half-plane model supplies a metric realization.

### Default rule while open

Do not finalize `def:regular-aes`.

Use conditional wording:

> In the metric formulation considered here …

### Resolution condition

Select one definition and prove equivalence with the other formulations under explicit compatibility hypotheses.

### Affected files

* `sections/sec03.tex`
* `sections/sec04.tex`
* target Chapters 5–7

### Affected nodes

* E1
* F3
* T6
* T7
* Z3

### Owner

Author

### Decision record

Pending.

---

## OQ-002 — Chronological composition convention

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

For histories (\gamma) and (\delta), what does:

[
\gamma\delta
]

mean chronologically?

Does it mean:

1. apply (\gamma), then (\delta); or
2. apply (\delta), then (\gamma)?

### Why it matters

This affects:

* matrix multiplication;
* cocycle signs and order;
* projective decomposition;
* ACS orientation;
* Baumslag–Solitar relations;
* finite contact commutators.

### Current evidence

Current sources use function-composition and word-order language that may not always agree.

### Default rule while open

Do not rewrite convention-sensitive proofs.

Use explicit expressions:

[
g_n\circ\cdots\circ g_1
]

rather than compressed products.

### Resolution condition

Choose one convention and verify:

* one two-step affine example;
* one Möbius decomposition;
* one ACS example;
* one contact commutator.

### Affected nodes

* C0
* P2
* T2
* T3
* E5
* T9–T12
* K3

### Owner

Author and mathematical reviewer

### Decision record

Pending.

---

## OQ-003 — Projective matrix action convention

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

Is the adopted action:

[
\begin{pmatrix}
A&B\
C&D
\end{pmatrix}
\cdot z
=======

\frac{Az+B}{Cz+D},
]

and do chronological histories correspond to left multiplication or right multiplication of matrices?

### Why it matters

The (PGL_2) generation formula must match the history order exactly.

### Default rule while open

Every projective calculation must be written both as a composed map and as a matrix product.

### Resolution condition

Fix the convention in Appendix A and validate every elementary context.

### Affected nodes

* C0
* P1
* P2
* T2
* P3

### Owner

Mathematical reviewer

---

## OQ-004 — Exact field hypotheses for the (PGL_2) generation theorem

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

Does the current theorem and decomposition hold uniformly over every field (K), including characteristic (2)?

### Why it matters

The current use of:

[
J(z)=-1/z
]

changes form in characteristic (2), where (-1=1).

The theorem may remain true, but the proof and generator wording require checking.

### Current evidence

Translations, nonzero scalings, and inversion should still generate the rank-one projective group, but the existing formula is written with real-style signs.

### Default rule while open

State the theorem for fields of characteristic not equal to (2), or explicitly mark the arbitrary-field version as pending.

### Resolution condition

Provide a proof valid in all characteristics or restrict the theorem.

### Affected nodes

* T2
* P3
* Paper IV finite-field models

### Owner

Algebra reviewer

---

## OQ-005 — Exact affine history sublanguage

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

Which syntactic restrictions characterize the history language whose projective image lies in:

[
B_\infty\cong\operatorname{Aff}(1,K)?
]

Is it exactly:

* pure slot-(1) histories;
* histories excluding second-slot division;
* all contexts preserving (\infty);
* another syntactically defined class?

### Why it matters

Paper I’s central placement claim is:

[
\text{existing AEG}=\text{an affine/Borel sector}.
]

This requires a precise syntactic-to-group correspondence.

### Default rule while open

State only the operator-level result:

> The transformations fixing (\infty) form the affine Borel subgroup.

Do not yet claim a complete syntactic characterization.

### Resolution condition

Classify every elementary one-hole context by whether it fixes (\infty), then characterize the generated sublanguage.

### Affected nodes

* P3
* P4
* Chapters 2–4

### Owner

Author

---

## OQ-006 — Positive affine component versus full real affine group

**Priority:** P1
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

Should Paper I develop only:

[
\operatorname{Aff}^{+}(1,\mathbb R),
]

or include orientation-reversing affine maps as a disconnected extension?

### Why it matters

The differential flow uses:

[
e^\lambda>0.
]

Negative multipliers do not lie in the identity component and require a discrete reflection.

### Default rule while open

Develop the continuous geometry on (\operatorname{Aff}^{+}(1,\mathbb R)).

Mention the full real affine group algebraically.

### Resolution condition

Decide whether reflections contribute any essential Paper I geometry.

### Affected nodes

* P4
* F1
* E2
* T6

### Owner

Author

---

## OQ-007 — Meaning of “torsion”

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

Should the primary term `arithmetic torsion` refer to:

1. elementary endpoint order defect;
2. relative affine translation defect;
3. ACS weighted area;
4. closed-loop vertical holonomy;
5. contact curvature;
6. a family of related invariants?

### Why it matters

The current paper uses the same word for finite and infinitesimal quantities that are related but not literally identical.

It may also be confused with Riemannian torsion.

### Default rule while open

Use qualified terms:

* elementary affine torsion;
* relative affine defect;
* global ACS torsion;
* commutator holonomy;
* horizontal curvature.

### Resolution condition

Choose a primary definition and state how the remaining quantities derive from or approximate it.

### Affected nodes

* A4
* T10–T12
* K3
* T15–T17
* abstract and title

### Owner

Author

---

## OQ-008 — Direct ACS orientation and weight convention

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

Should the canonical ACS evaluation use:

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right),
]

or retain the reverse-path form with:

[
e^M,dA?
]

### Why it matters

The choice controls:

* orientation;
* Stokes sign;
* example values;
* comparison with source- and target-frame cocycles.

### Current evidence

Both formulations encode the same future scaling after an appropriate reversal or normalization.

The direct-path formula appears conceptually cleaner.

### Default rule while open

Do not globally replace the existing ACS formulas.

### Resolution condition

Prove the equivalence and test both conventions against:

* one addition;
* addition followed by multiplication;
* multiplication followed by addition;
* the four-step example.

### Affected nodes

* T3
* G1
* T9–T12
* T17

### Owner

Author and sign-convention reviewer

---

## OQ-009 — Compatibility condition for generalized torsion

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

What is the canonical domain of:

[
\tau(\gamma,\delta)?
]

Possibilities:

1. histories with equal accumulated scale;
2. histories with equal full ACS endpoint;
3. histories with the same projective endpoint action;
4. arbitrary histories with a base-point-dependent defect.

### Why it matters

Different conclusions require different conditions:

* equal scale gives independence from (x);
* equal charge gives a closed ACS chain;
* equal operator gives zero relative operator defect.

### Default rule while open

Maintain two definitions:

* scale-compatible;
* charge-compatible.

Do not call them equivalent.

### Resolution condition

State separate propositions for each compatibility level.

### Affected nodes

* A3
* G2
* G3
* T10–T12

### Owner

Author

---

## OQ-010 — Definition of singular AES

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

How broad should the singular-AES definition be?

Should singularity permit:

* non-smooth (a);
* degenerate (g);
* deleted points;
* variable or vanishing (\mu,\lambda);
* projective poles;
* boundaries;
* chart transitions?

### Why it matters

A definition that is too narrow excludes intended examples.

A definition that is too broad has no mathematical consequences.

### Default rule while open

Require:

1. a declared closed singular set (S);
2. a regular AES on (\mathcal M\setminus S);
3. explicit local behavior near (S).

### Resolution condition

Test the definition against:

* (\mathfrak E_0);
* the isolated-zero model;
* one multi-zero construction;
* one projective-pole example.

### Affected nodes

* Z3
* Z4
* Paper III architecture

### Owner

Author

---

## OQ-011 — Classification of the current isolated-zero model

**Priority:** P0
**State:** CLOSED — resolved in Paper I on 2026-08-06

### Question

What exactly is the status of the center of the current disk model?

Is it:

* included with a non-smooth assignment;
* removed from the manifold;
* a metric singularity;
* a parameter-degenerate point;
* an invalid extension?

### Current evidence

The radial assignment behaves as:

[
a(r)\sim Cr,
]

and (r=\sqrt{x^2+y^2}) is not differentiable at the origin.

### Default rule while open

Do not call the model a regular AES.

### Resolution condition

Rewrite the model in local Cartesian coordinates and audit:

* smoothness of (a);
* smoothness of (g);
* validity of the flow equation;
* topology of the punctured domain.

### Affected nodes

* Z4
* (\mathfrak E_1) naming
* Paper III singular examples

### Owner

Geometry reviewer

---

## OQ-012 — Canonical numbering of (\mathfrak E_0,\mathfrak E_1,\ldots)

**Priority:** P0
**State:** CLOSED — descriptive names adopted on 2026-08-06

### Question

What invariant determines the index in:

[
\mathfrak E_0,\mathfrak E_1,\mathfrak E_k?
]

Historical usage has varied.

Possible meanings include:

* regular versus singular hierarchy;
* number of zero components;
* order of construction;
* singularity index.

### Why it matters

Blind renaming risks corrupting old proofs and figures.

### Default rule while open

Use descriptive names:

* basic regular hyperbolic model;
* isolated-zero singular model;
* multi-zero model.

Retain historical symbols only with qualification.

### Resolution condition

Create a model registry containing:

| Formula | Domain | Zero set | Singular set | Historical name | Final name |

### Affected files

Entire repository

### Owner

Author

---

# Part III. Paper I high-priority proof questions

## OQ-013 — Derivation of the invariant affine metric

**Priority:** P1
**State:** CLOSED — proved in Paper I on 2026-08-06

### Question

Can the metric:

[
g_{\mu,\lambda}
===============

e^{-2\lambda v}\frac{du^2}{\mu^2}+dv^2
]

be derived canonically from the affine group and the normalized generator frame?

### Why it matters

This turns the upper-half-plane model from an ansatz into a homogeneous realization.

### Current evidence

The affine group has a natural left-invariant metric after choosing generator lengths.

### Default rule while open

Present the metric as a motivated explicit model, not as uniquely forced.

### Resolution condition

Specify group coordinates, Maurer–Cartan forms, and metric invariance.

### Affected nodes

* E2
* T6
* E3

### Owner

Differential-geometry reviewer

---

## OQ-014 — Curvature normalization

**Priority:** P1
**State:** CLOSED — proved in Paper I on 2026-08-06

### Question

For the general metric normalization, is the Gaussian curvature exactly:

[
-\lambda^2,
]

or does an additional factor appear?

### Default rule while open

Do not state the generalized curvature in the abstract or main-results list.

### Resolution condition

Perform a direct curvature calculation or reduce to the standard hyperbolic metric by an explicit coordinate scaling.

### Affected nodes

* E3
* Paper II analysis

### Owner

Geometry reviewer

---

## OQ-015 — Laplace–Beltrami eigenvalue

**Priority:** P1
**State:** CLOSED — proved in Paper I on 2026-08-06

### Question

For the general normalized metric, is:

[
\Delta_g a=2\lambda^2a
]

under the chosen sign convention?

### Why it matters

The current text states the normalized case:

[
\Delta a=2a.
]

### Default rule while open

State only the explicitly verified normalized formula.

### Resolution condition

Compute the full Laplace–Beltrami operator and fix the sign convention.

### Affected nodes

* E6
* Paper II operator comparison

### Owner

Analysis reviewer

---

## OQ-016 — Are arithmetic grid actions isometries?

**Priority:** P1
**State:** CLOSED — classified in Paper I on 2026-08-06

### Question

Do the transformations implementing:

[
a\mapsto a+s,
\qquad
a\mapsto ka
]

preserve:

* the assignment only;
* the metric;
* the framed AES structure;
* some subset of these?

### Why it matters

The current exposition may suggest a stronger geometric symmetry than has been verified.

### Default rule while open

Call them assignment-compatible transformations, not isometries.

### Resolution condition

Compute pullbacks of the metric.

### Affected nodes

* E4
* E5
* hyperbolic grid figures

### Owner

Geometry reviewer

---

## OQ-017 — Correct Baumslag–Solitar relation

**Priority:** P1
**State:** CLOSED — checked in Paper I on 2026-08-06

### Question

Under the final action and composition convention, what exact relation do (X_s) and (Y_k) satisfy?

Possibilities differ by inverses and generator naming.

### Default rule while open

Move the relation to an appendix or omit it.

### Resolution condition

Compute both sides as explicit maps and compare.

### Affected nodes

* E5

### Owner

Algebra reviewer

---

## OQ-018 — Regular-zero theorem at the boundary

**Priority:** P1
**State:** CLOSED — boundaryless/interior theorem adopted on 2026-08-06

### Question

How should Paper I state the regular-zero theorem when (\mathcal M) has boundary?

### Why it matters

An interior regular zero is a codimension-one submanifold, but a zero set may meet or terminate at the boundary.

### Default rule while open

State the main theorem for interior zeros or boundaryless manifolds.

### Resolution condition

Add a separate boundary formulation or explicit exclusion.

### Affected nodes

* T7
* Z2
* Paper III topology-change mechanisms

### Owner

Differential-topology reviewer

---

## OQ-019 — Number and global topology of regular zero components

**Priority:** P2
**State:** PARTIALLY RESOLVED BY THE COMPLETE REGULAR SPLITTING THEOREM

### Question

Under what hypotheses can one conclude that zero components are:

* properly embedded lines;
* circles;
* finite in number?

### Current evidence

The regular-value theorem only gives a one-dimensional submanifold locally.  The
new global result proves that if the AES is connected, complete, and boundaryless,
then

[
M\cong Z(a)\times\mathbb R,
]

so the zero layer is nonempty and connected.  This does not classify its intrinsic
one-manifold topology in higher-dimensional carriers, nor does it apply to
incomplete models or manifolds with boundary.

### Default rule while open

Outside the complete boundaryless hypotheses, make no global classification.

### Resolution condition

Add compactness, completeness, properness, or model-specific hypotheses.

### Affected nodes

* Z2
* Paper III multi-zero theory

### Owner

Topology reviewer

---

## OQ-020 — Regular total-zero-set theorem and projection submersion

**Priority:** P1
**State:** CLOSED — proved in Paper I on 2026-08-06

### Question

Does:

[
d_pa_t\neq0
]

on the zero set automatically imply that:

[
\pi:\mathcal Z\to I
]

is a submersion?

### Expected answer

Yes: one can solve for a tangent vector with arbitrary parameter component by correcting in a spatial direction.

### Default rule while open

Claim only that (\mathcal Z) is a smooth submanifold.

### Resolution condition

Write the tangent-space proof explicitly.

### Affected nodes

* T8
* Paper III tube theorem

### Owner

Differential-topology reviewer

---

## OQ-021 — Inclusion of a multi-zero example in Paper I

**Priority:** P1
**State:** CLOSED — omitted from Paper I and deferred to Paper III

### Question

Is there currently a multi-zero model that passes all six requirements?

1. explicit domain;
2. explicit metric;
3. explicit assignment;
4. singular-set classification;
5. flow verification;
6. exact zero topology.

### Default rule while open

Do not include a multi-zero example in Paper I’s main theorem sequence.

### Resolution condition

Certify one model against the checklist.

### Affected nodes

* Z7
* Paper I figures
* Paper III migration

### Owner

Author

---

## OQ-022 — Formulation of the local-global synthesis theorem

**Priority:** P1
**State:** CLOSED — layered synthesis adopted on 2026-08-06

### Question

Can T17 be written as one theorem without falsely equating:

* affine endpoint defect;
* ACS weighted area;
* finite contact holonomy;
* infinitesimal curvature?

### Default rule while open

Present the relationships as a final synthesis subsection rather than a theorem.

### Resolution condition

Separate:

1. exact affine/ACS identity;
2. exact finite contact formula;
3. common infinitesimal limit.

### Affected nodes

* T17
* abstract
* conclusion

### Owner

Author and reviewer

---

# Part IV. Editorial and notation questions

## OQ-023 — Assignment-space notation versus horizontal-distribution notation

**Priority:** P1
**State:** CLOSED — notation fixed on 2026-08-06

### Question

Should:

[
\mathcal H
]

denote the upper half-plane or the horizontal distribution?

### Default rule while open

Use:

[
\mathbb H^2
]

for the upper half-plane and:

[
\mathcal D=\ker\alpha
]

for the horizontal distribution.

### Resolution condition

Adopt one convention series-wide.

### Affected files

Papers I–III

### Owner

Editor

---

## OQ-024 — (\lambda) as intensity versus accumulated log scale

**Priority:** P1
**State:** CLOSED — notation fixed on 2026-08-06

### Question

Should accumulated multiplicative charge use:

[
M
]

or (\Lambda), reserving (\lambda) for the fixed infinitesimal intensity?

### Why it matters

Current Maurer–Cartan and flow formulas risk overloading (\lambda).

### Default rule while open

Reserve:

* (\lambda): fixed intensity;
* (M): accumulated logarithmic charge.

### Resolution condition

Audit all current formulas and update notation.

### Owner

Editor

---

## OQ-025 — Use of (\delta) versus (\delta_H)

**Priority:** P1
**State:** CLOSED — notation fixed on 2026-08-06

### Question

Should Paper I rename the current (\delta)-operator to:

[
\delta_H
]

to emphasize its horizontal and non-nilpotent nature?

### Default rule while open

Use `horizontal covariant differential` in prose and (\delta_H) in new material.

### Resolution condition

Determine compatibility with earlier papers and future Paper II notation.

### Affected nodes

* K4
* T16
* Paper II operators

### Owner

Author and editor

---

## OQ-026 — Use of the term “contact connection”

**Priority:** P2
**State:** OPEN

### Question

Should the contact construction be called:

* arithmetic contact manifold;
* contact connection;
* Ehresmann connection with contact horizontal distribution;
* arithmetic contact model?

### Why it matters

The projection:

[
(u,v,a)\mapsto(u,v)
]

with horizontal distribution is an Ehresmann connection, while (\alpha) is also a contact form.

### Default rule while open

Use:

> arithmetic contact model with its associated horizontal connection.

### Resolution condition

Choose terminology that distinguishes the two structures.

### Owner

Geometry editor

---

## OQ-027 — Title and subtitle of Paper I

**Priority:** P2
**State:** OPEN

### Options

1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry I: Affine Foundations**
3. **Arithmetic Expression Geometry I: Sequential Histories and Affine Geometry**

### Why it matters

`Foundations` is broad, while most developed geometry is affine.

### Default rule while open

Use:

**Arithmetic Expression Geometry I: Foundations**

with subtitle:

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

### Resolution condition

Decide after the final theorem set is fixed.

### Owner

Author

---

## OQ-028 — Role of “foundations” versus “affine foundations”

**Priority:** P2
**State:** OPEN

### Question

Does inclusion of the (PGL_2) completion theorem justify the broader title `Foundations`, even though the developed differential geometry remains affine?

### Default rule while open

State explicitly in the abstract that Paper I develops the affine foundational sector within a projective context.

### Owner

Author

---

## OQ-029 — Historical terminology “arithmetic torsion”

**Priority:** P2
**State:** OPEN

### Question

Should the paper retain the established term despite possible confusion with torsion tensors?

### Default rule while open

Retain the term with an early warning:

> Arithmetic torsion is an order defect and is unrelated to the torsion tensor of an affine connection unless explicitly compared.

### Resolution condition

Assess whether an alternative such as `arithmetic commutation defect` is preferable.

### Owner

Author

---

## OQ-030 — Placement of equality and neutrality hierarchy

**Priority:** P2
**State:** OPEN

### Question

How much of the current neutrality taxonomy belongs in Paper I?

### Default rule while open

Retain only equality levels in Chapter 2 and a few examples in Appendix E.

Defer full neutrality theory.

### Resolution condition

Identify whether the later theory belongs to Paper IV or a separate relation-theory paper.

### Owner

Author

---

# Part V. Paper II interface questions

## Paper II resolution update — 2026-08-06

The first canonical Paper II manuscript closes OQ-031--OQ-036 at the
mathematical-review level.  The original questions remain below as provenance.

| Question | State | Resolution |
|---|---|---|
| OQ-031 | **CLOSED** | The two-dimensional regular AES already has (g) and orientation.  The contact branch separately declares the horizontal metric making (D_u,D_v) orthonormal. |
| OQ-032 | **CLOSED WITH SCOPE LIMIT** | Surface (J) is intrinsic.  Contact (J) is compatible with the declared normalized metric and horizontal orientation; no invariance under arbitrary contactomorphisms is claimed. |
| OQ-033 | **CLOSED FOR THE CHOSEN REALIZATIONS** | Surface analysis uses Riemannian area and the minimal Dirichlet form.  Contact analysis uses positive contact volume and a Friedrichs realization of (-D_u^2-D_v^2-lambda D_v).  The raw sum of squares is treated separately and no essential-self-adjointness claim is made. |
| OQ-034 | **CLOSED** | The corrected logarithmic contact field is verified on the branch half-plane containing (mu+ilambdamathbb R); its domain and CR equation are explicit. |
| OQ-035 | **CLOSED BY CORRECTION** | The canonical object is a finite filtered (C^infty(u,v))-module, not an unspecified basis. |
| OQ-036 | **CLOSED** | The decisive result is the (C_0) ideal-boundary Poisson--Dirichlet theorem on the basic hyperbolic AES, strengthened by the exact Dirichlet-to-Neumann and energy identity. |

## OQ-031 — Canonical horizontal metric for analysis

**Priority:** P3
**State:** DEFERRED TO PAPER II

### Question

Does the contact distribution admit a preferred horizontal metric inherited from Paper I, or must Paper II choose one independently?

### Current default

Paper II must state the additional metric data explicitly.

### Research significance

This controls whether arithmetic holomorphicity is canonical or model-dependent.

---

## OQ-032 — Canonical almost-complex structure

**Priority:** P3
**State:** DEFERRED TO PAPER II

### Question

Given an oriented two-dimensional horizontal metric, the compatible (J) is locally determined. Is that structure globally canonical in the intended AEG category?

### Current default

No canonicity claim in Paper I.

---

## OQ-033 — Correct analytic domain of (\Delta_H)

**Priority:** P3
**State:** DEFERRED TO PAPER II

### Question

On which function space and measure should:

[
\Delta_H=D_u^2+D_v^2
]

be studied?

### Required future decisions

* reference measure;
* formal adjoint;
* boundary conditions;
* self-adjoint realization;
* completeness assumptions.

---

## OQ-034 — Arithmetic holomorphic coordinate

**Priority:** P3
**State:** DEFERRED TO PAPER II

### Question

Is the intended formula:

[
\zeta(u,v,a)
============

u+\frac{i}{\lambda}\log(\mu+i\lambda a)?
]

### Required verification

* branch domain;
* typo correction;
* horizontal Cauchy–Riemann equation;
* global versus local definition.

---

## OQ-035 — Status of the affine–Appell “basis”

**Priority:** P3
**State:** DEFERRED TO PAPER II

### Question

In what ambient space is the family a basis?

### Default rule

Call it an operator-stable family or finite triangular system until completeness is established.

---

## OQ-036 — First decisive theorem of hyperbolic real function theory

**Priority:** P3
**State:** DEFERRED TO PAPER II

### Question

Which result will make Paper II a genuine function theory rather than a formal operator note?

Candidates:

* Poisson kernel;
* Dirichlet problem;
* maximum principle;
* Green function;
* spectral theorem;
* continuation result.

### Owner

Author

---

# Part VI. Paper III interface questions

## OQ-037 — Definition of the parameter discriminant

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Should the discriminant include only:

[
a_t(p)=0,
\qquad
d_pa_t=0,
]

or also:

* metric degeneracy;
* parameter degeneracy;
* boundary collision;
* failure of properness;
* projective poles?

### Current default

Use a stratified discriminant with separate components.

---

## OQ-038 — General (E_k) indexing principle

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Does (k) record:

* number of zero components;
* singularity order;
* construction level;
* winding number;
* another invariant?

### Default rule

Do not stabilize (E_k) notation until this is settled.

---

## OQ-039 — Existence of a universal multi-zero construction

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Is there a uniform construction producing a verified AES with (k) regular zero components?

### Required future proof

* formula;
* metric;
* flow equation;
* zero topology;
* singularity control.

---

## OQ-040 — Conformal uniqueness of (E_0,E_1,E_k)

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Under what data could such a uniqueness statement be meaningful?

Candidates:

* fixed zero divisor;
* fixed curvature;
* fixed asymptotics;
* fixed boundary behavior;
* fixed flow parameters.

### Current status

Open.

---

## OQ-041 — Local singularity normal forms

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Which singularity types are compatible with the AEG flow and metric structure?

Candidates include:

* fold;
* cusp;
* crossing;
* branch point;
* birth/death;
* reconnection.

### Current default

Do not import generic catastrophe-theory labels before deriving compatible normal forms.

---

## OQ-042 — Properness of explicit zero families

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

For each proposed family, is:

[
\pi:\mathcal Z\to B
]

proper?

### Why it matters

Without properness, fiber topology may change by escape to infinity.

---

## OQ-043 — From zero-component permutation to braid

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

When does monodromy lift from:

[
S_n
]

to:

[
B_n?
]

### Required future data

* embedded moving points or curves;
* collision-free parameter paths;
* ambient isotopy class;
* base-space topology.

---

## OQ-044 — Definition of threading

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Is a thread:

* a section of the tube;
* an independent embedded curve;
* a marked history;
* a zero branch;
* a decoration carried by monodromy?

### Default rule

Do not define a knot invariant until the object being threaded is fixed.

---

## OQ-045 — Markov invariance

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Can any tube/thread quantity survive braid stabilization and conjugation?

### Current status

Open and decisive.

---

## OQ-046 — New information beyond Alexander/Burau

**Priority:** P3
**State:** DEFERRED TO PAPER III

### Question

Can a normalized AEG tube invariant distinguish examples not determined by the Alexander polynomial or Burau representation?

### Current status

Open success criterion.

---

# Part VII. Paper IV interface questions

## OQ-047 — Exact category of histories

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Should the main object be:

* a free category of partial contexts;
* an action groupoid;
* a path groupoid;
* a rewriting (2)-category?

### Why it matters

This determines how relations and condensation are represented.

### Partial affine-sector note (2026-10-24)

Paper 0 §3.6 (`subsec:p0-operation-to-length`) now states what the affine sector
answers without settling this question.  The source is the comb grammar of
`def:p0-left-right-combs`; the assignment to motions is the evaluation
homomorphism `nu` of `prop:p0-history-homomorphisms`; the composite to lengths is
`ell = |log o L o nu|` of `prop:p0-length-multiplicative-charge`, which is a
function of the induced motion and therefore not injective on histories
(`prop:p0-length-losses`).  Because `|.|` is not a homomorphism
(`eq:p0-length-not-additive`), the length is *not* a functorial target: the
functorial object is the multiplicative charge `M = log o L o nu` in `(R,+)`, and
the additive charge is the part that does not descend
(`thm:p0-descent`(4)).  Two extensions are blocked elsewhere and not by this
question: `Aff^+(1,R) -> PGL_2(K)` needs the trace trichotomy, which Paper 0 does
not develop; combs -> arbitrary binary trees needs Paper I's
`thm:sequential-tree-classification`.  The state of OQ-047 itself is unchanged.

---

## OQ-048 — Ordinary versus projective history groupoids

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Should ordinary admissibility and projective continuation form:

* separate categories;
* a category with domain labels;
* a partial functor;
* a localization?

---

## OQ-049 — Canonical process residue after quotient

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Given:

[
G\to G/H,
]

is the fiber (H) itself the process residue, or only after a reference lift and gauge choice?

### Current evidence

An (H)-valued coordinate is not canonical without a section.

---

## OQ-050 — Semantic meaning of bivaluation

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

What mathematical semantics justifies interpreting an ordered point–copoint pair as concept–predicate structure?

### Default rule

Treat the projector theorem algebraically, without semantic overclaim.

---

## OQ-051 — Definition of condensation

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Is condensation:

* quotient by history equivalence;
* canonical normalization;
* passage from history to operator;
* passage from operator to homogeneous quotient;
* a general family of forgetful maps?

### Default rule

Define each condensation map explicitly rather than using one universal metaphor.

---

## OQ-052 — Measuring information lost by condensation

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Possible measures include:

* fiber cardinality;
* orbit dimension;
* entropy;
* shortest representative length;
* stabilizer size;
* coding length.

No canonical measure is currently established.

---

## OQ-053 — Canonical representative complexity

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

When does a quotient class admit:

* a canonical representative;
* a computable normal form;
* a shortest representative?

### Why it matters

Complexity claims depend on this distinction.

---

## OQ-054 — Geometric metric versus computational cost

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Under what hypotheses is a geometric path metric comparable to an actual computation cost?

### Required future structure

* state graph;
* encoding;
* transition cost;
* simulation theorem;
* quasi-isometric comparison.

---

## OQ-055 — Representation complexity as a unifying quantity

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Can time and space complexity be derived as different projections of representation geometry?

### Current status

Research hypothesis, not theorem.

---

## OQ-056 — Growth consequences of noncommutativity

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Which explicit AEG-related groups or semigroups have:

* polynomial growth;
* exponential growth;
* intermediate growth?

### Default rule

No general implication from noncommutativity.

---

## OQ-057 — Quasi-isometry between history space and AES

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Question

Does any natural history graph quasi-isometrically embed into or map onto the hyperbolic AES?

### Why it matters

Without such a theorem, geometric distance cannot be identified with expression complexity.

---

## OQ-058 — Complexity case study selection

**Priority:** P3
**State:** DEFERRED TO PAPER IV

### Candidate cases

* Horner form versus expanded polynomial;
* FFT or large-integer multiplication;
* rewriting normalization;
* proof search;
* pebble games.

### Selection criterion

Choose examples with explicit state space, metric, and cost theorem.

---

# Part VIII. Migration and repository questions

## OQ-059 — Final repository layout

**Priority:** P1
**State:** CLOSED — top-level `paper-1/` canonical entry adopted

### Question

Should Paper I immediately move from:

```text
aeg-paper.tex
sections/
```

to the then-proposed Roman-numbered form:

```text
paper-I/paper-I.tex
paper-I/sections/
```

or should restructuring first occur within the current paths?

### Default rule

Restructure mathematically before large path renaming.

### Resolution condition

Complete the audit and confirm the build strategy.

### Owner

Repository maintainer

### Final resolution

After the mathematical audit and build closure, the repository maintainer authorized
the Arabic-numbered top-level layout.  The canonical paths are now
`paper-1/aeg-paper-1.tex`, `paper-1/sections/`, and `paper-1/appendices/`.

---

## OQ-060 — Shared versus paper-specific bibliography

**Priority:** P2
**State:** OPEN

### Question

Should all four papers use one shared `.bib` file or separate bibliographies?

### Default rule

Retain one shared bibliography during migration.

Split only after paper boundaries stabilize.

---

## OQ-061 — Shared figures

**Priority:** P2
**State:** OPEN

### Question

Which figures are genuinely shared across papers, and which should have paper-specific versions?

### Default rule

Use shared source assets but paper-specific rendered copies or captions where meaning differs.

---

## OQ-062 — Fate of legacy `aeg-lemma.tex`

**Priority:** P2
**State:** OPEN

### Question

Does this file contain unique proofs or only obsolete duplicates?

### Default rule

Do not delete.

### Resolution condition

Compare every lemma against active sections and notes.

---

## OQ-063 — Status of generated discussion files

**Priority:** P2
**State:** CLOSED — no tracked `gpt/` directory exists in the fixed baseline or
current tree

### Question

Should a tracked `gpt/` directory remain in place with archival status or move under
`governance/archive/`?

### Resolution

The source inventory found no tracked `gpt/` directory to migrate. Historical
references to such a directory remain provenance only. Any future generated
discussion material must be classified when added rather than creating an implied
current path.

---

## OQ-064 — Published DOI versus restructured manuscript

**Priority:** P1
**State:** CLOSED FOR PAPER I — versions explicitly distinguished

### Question

How should the repository distinguish:

* the existing DOI version;
* the active restructuring draft;
* the eventual new preprint?

### Default rule

Do not imply that the DOI points to the restructured version unless updated.

### Owner

Author

---

## OQ-065 — Multi-paper build system

**Priority:** P2
**State:** CLOSED — root selector-based build implemented

### Question

Should `build.sh` support paper selection, or should each paper have its own build script?

### Resolution

The root `build.sh` accepts `1`, `2`, `3`, `4`, or `all` and retains one canonical
build interface for the series. Per-paper scripts are unnecessary unless a future
paper develops genuinely different tooling requirements.

---

# Part IX. Literature and novelty questions

## OQ-066 — Literature on expression-history geometry

**Priority:** P2
**State:** OPEN

### Question

What prior work most closely studies:

* expression evaluation histories as geometric paths;
* affine actions generated by arithmetic contexts;
* contact geometry of evaluation processes?

### Why it matters

Paper I’s novelty claims must be restrained and accurately placed.

### Default rule

Use:

> We are not aware of …

only after a dedicated literature audit.

---

## OQ-067 — Relation to affine control systems

**Priority:** P2
**State:** OPEN

### Question

Is the affine flow and contact lift already a standard control-system model under another name?

### Why it matters

The mathematical novelty may lie in arithmetic interpretation and synthesis rather than the local contact form itself.

---

## OQ-068 — Relation to Riccati control and projective dynamics

**Priority:** P2
**State:** OPEN

### Question

Which established Riccati/projective-flow literature should be cited to place bilateral completion accurately?

---

## OQ-069 — Relation to cocycles and semidirect products

**Priority:** P2
**State:** OPEN

### Question

Should the affine cocycle be framed explicitly as a standard (1)-cocycle for a semidirect product action?

### Potential benefit

This could simplify proofs and clarify ACS weighting.

### Potential risk

Excessive abstraction may obscure the arithmetic origin.

---

## OQ-070 — Relation to contactization and jet spaces

**Priority:** P2
**State:** OPEN

### Question

Is the arithmetic contact model best understood as:

* a contactization;
* a first jet-space model;
* an Ehresmann connection;
* a standard Darboux contact structure with arithmetic coordinates?

### Default rule

State the standard contact equivalence and emphasize the arithmetic frame.

---

# Part X. Release-blocking register

## 71. Current P0 blockers

Paper I cannot reach mathematical closure while any of the following remain unresolved.
The checked entries below were closed by the resolution ledger in Part XIV:

* [x] OQ-001 — regular AES definition
* [x] OQ-002 — chronological composition
* [x] OQ-003 — matrix action convention
* [x] OQ-004 — field scope of (PGL_2) theorem
* [x] OQ-005 — affine syntactic sector
* [x] OQ-007 — primary meaning of torsion
* [x] OQ-008 — ACS orientation and weight
* [x] OQ-009 — compatibility for generalized torsion
* [x] OQ-010 — singular AES definition
* [x] OQ-011 — isolated-zero model classification
* [x] OQ-012 — model numbering

No release task may waive these items.

---

## 72. Current P1 chapter blockers

The following blocked specific chapters or optional main results and were closed by
the corresponding Part XIV resolutions:

* [x] OQ-013 — invariant affine metric
* [x] OQ-014 — curvature normalization
* [x] OQ-015 — Laplace eigenvalue
* [x] OQ-016 — grid symmetry status
* [x] OQ-017 — Baumslag–Solitar convention
* [x] OQ-018 — boundary zero formulation
* [x] OQ-020 — projection-submersion proof
* [x] OQ-021 — multi-zero example inclusion
* [x] OQ-022 — local-global synthesis formulation
* [x] OQ-023 — (\mathcal H) notation collision
* [x] OQ-024 — (\lambda/M) notation
* [x] OQ-025 — (\delta/\delta_H) notation
* [x] OQ-059 — repository migration timing
* [x] OQ-064 — DOI/version distinction

Optional results may be removed rather than blocking release where authorized by scope.

---

# Part XI. Recommended resolution order

## 73. Decision sequence

Resolve issues in this order:

### Stage 1 — Conventions

```text
OQ-002
OQ-003
OQ-004
OQ-005
OQ-006
OQ-024
```

### Stage 2 — Foundational definitions

```text
OQ-001
OQ-007
OQ-009
OQ-010
OQ-012
OQ-025
OQ-026
```

### Stage 3 — Algebraic and ACS proofs

```text
OQ-008
OQ-017
OQ-022
```

### Stage 4 — Geometric model

```text
OQ-013
OQ-014
OQ-015
OQ-016
```

### Stage 5 — Zero geometry

```text
OQ-011
OQ-018
OQ-019
OQ-020
OQ-021
```

### Stage 6 — Editorial and repository decisions

```text
OQ-023
OQ-027
OQ-028
OQ-029
OQ-030
OQ-059–OQ-065
```

### Stage 7 — Later-paper research

```text
OQ-037–OQ-058
```

Paper II questions closed by the canonical mathematical-review manuscript and
retained above only as provenance:

```text
OQ-031–OQ-036 — CLOSED
```

---

# Part XII. Decision templates

## 74. Definition decision

```markdown
## Decision D-XXXX — [Definition name]

- Issue:
- Adopted definition:
- Rejected alternatives:
- Reason:
- Primitive data:
- Derived data:
- Required hypotheses:
- Examples tested:
- Affected theorem nodes:
- Source files updated:
- Reviewer:
- Date:
```

---

## 75. Convention decision

```markdown
## Decision C-XXXX — [Convention name]

- Issue:
- Adopted convention:
- Two-step verification:
- Matrix verification:
- ACS verification:
- Contact verification:
- Affected formulas:
- Files updated:
- Reviewer:
- Date:
```

---

## 76. Proof closure

```markdown
## Proof closure P-XXXX — [Result]

- Issue:
- Final theorem statement:
- Hypotheses:
- Proof location:
- Independent verification:
- Status before:
- Status after:
- Downstream nodes released:
- Date:
```

---

## 77. Deferral decision

```markdown
## Deferral F-XXXX — [Topic]

- Issue:
- Deferred to:
- Minimal statement retained in Paper I:
- Material moved:
- Mathematical status:
- Reason for deferral:
- Re-entry condition:
- Date:
```

---

# Part XIII. Final governing rule

## 78. Frontier discipline

Open questions are part of the mathematical result, not editorial debris.

The restructuring must keep three layers distinct:

[
\boxed{
\text{resolved foundation}
\quad\subset\quad
\text{conditional extension}
\quad\subset\quad
\text{open research frontier}.
}
]

Paper I may mention the frontier, but it must be built only from the resolved foundation.

When evidence is incomplete, the default action is:

1. preserve the source;
2. weaken the claim;
3. record the question;
4. defer the dependent theory;
5. do not guess.

---

# Part XIV. Paper I resolution ledger (2026-08-06)

The detailed decisions are recorded in `decisions-paper-I.md`; theorem-by-theorem
evidence is recorded in `paper-I-closure-report.md`.  The entries below close the
issues whose `State` fields were changed above without deleting their original
questions or default rules.

## Resolution — OQ-001

- **Decision:** A regular AES is the intrinsic tuple
  \((M,g,a;\mu,\lambda)\), with \(M\) oriented, \(g\) Riemannian,
  \(a\) smooth, \(\mu\ne0\), and
  \(|\nabla a|_g^2=\mu^2+\lambda^2a^2\).
- **Mathematical justification:** Section 5 proves equivalence with a unique
  positively oriented orthonormal arithmetic frame satisfying
  \(X_ua=\mu\), \(X_va=\lambda a\).
- **Source changes:** `05-affine-flow.tex`, `decisions-paper-I.md`.
- **Status changes:** E1 and F3 promoted to proved Paper I foundations.
- **Downstream nodes rechecked:** T5--T8, Paper II frame interface.
- **Reviewer:** independent geometry and final mathematical reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-002 and OQ-003

- **Decision:** Histories act left-to-right in time; \(\gamma\delta\) means
  first \(\gamma\), then \(\delta\); matrices act on column homogeneous
  coordinates and \(\rho(\gamma\delta)=\rho(\delta)\rho(\gamma)\).
- **Mathematical justification:** explicit two-step affine, Möbius, ACS rectangle,
  and contact rectangle checks agree.
- **Source changes:** Sections 2--4 and Appendices A--B.
- **Status changes:** C0--C2 and P2 closed.
- **Downstream nodes rechecked:** PGL generation, all cocycles, ACS and contact signs.
- **Reviewer:** independent algebra and torsion/contact reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-004

- **Decision:** The bilateral generation theorem is valid over every field,
  including characteristic two.
- **Mathematical justification:** Section 3 gives separate \(C=0\) and
  \(C\ne0\) decompositions; every divisor is explicitly nonzero and the same
  identity survives \(-1=1\).
- **Source changes:** `03-projective-affine.tex`, Appendix A.
- **Status changes:** T2 promoted to proved.
- **Downstream nodes rechecked:** Borel placement and Paper IV field interface.
- **Reviewer:** independent algebra and final mathematical reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-005 and OQ-006

- **Decision:** The elementary affine sublanguage is generated by the
  non-degenerate elementary contexts individually fixing \(\infty\); its image is
  \(B_\infty\), without claiming that it equals the full inverse image.  Continuous
  geometry uses \(\operatorname{Aff}^+(1,\mathbb R)\); negative multipliers remain
  an algebraic disconnected extension.
- **Mathematical justification:** the elementary matrix table and the normal form
  \(z\mapsto az+b\) prove the image statement.
- **Source changes:** Section 3.
- **Status changes:** P3 and P4 closed.
- **Downstream nodes rechecked:** Sections 4--9.
- **Reviewer:** independent algebra and scope reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-007, OQ-008, and OQ-009

- **Decision:** Primary arithmetic torsion is the target-frame translation defect
  of two scale-compatible positive add--scale histories.  Charge compatibility is
  the stronger condition used for closed ACS chains.  The ACS uses
  \(dA\wedge dM\), \(C_\gamma-C_\delta\), and
  \(\eta_*=e^{M_*-M}dA\).
- **Mathematical justification:** Section 8 proves direct evaluation and weighted
  Stokes; the positive rectangle gives \(p(e^q-1)\) with the declared sign.
- **Source changes:** `08-acs-torsion.tex`, Appendices D--E.
- **Status changes:** G1--G3 and T9--T12 promoted to proved in the stated language.
- **Downstream nodes rechecked:** finite contact comparison and conclusion.
- **Reviewer:** independent geometry, algebra, and torsion/contact reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-010 and OQ-011

- **Decision:** A singular AES has a closed nowhere-dense, locally essential singular
  set and is regular on its nonempty dense complement.  The disc center is an
  assignment singularity: the metric is smooth there, but the radial assignment is
  not \(C^1\) and admits no smooth local extension.
- **Mathematical justification:** Section 7 verifies the Cartesian smoothness,
  punctured eikonal equation, and exact regular/singular zero decomposition.
- **Source changes:** `07-zero-geometry.tex`, Appendix C.
- **Status changes:** Z3--Z5 closed for the isolated-zero model.
- **Downstream nodes rechecked:** Paper III singular interface.
- **Reviewer:** independent algebra and geometry reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-012

- **Decision:** Paper I uses “basic regular hyperbolic model” and “isolated-zero
  singular model”; historical \(\mathfrak E_k\) indices are not canonical.
- **Mathematical justification:** no invariant indexing rule exists, while the
  descriptive names encode the verified regularity class.
- **Source changes:** Sections 6--7, root README, decision model registry.
- **Status changes:** model-numbering conflict closed by removal, not renumbering.
- **Downstream nodes rechecked:** Papers II--III README files.
- **Reviewer:** independent scope review.
- **Date:** 2026-08-06.

## Resolution — OQ-013, OQ-014, and OQ-015

- **Decision:** Use the normalized left-invariant affine metric; its complete
  upper-half-plane realization has \(K=-\lambda^2\), and with
  \(\Delta=\operatorname{div}\nabla\), the assignment satisfies
  \(\Delta a=2\lambda^2a\).
- **Mathematical justification:** Section 6 and Appendix C derive the invariant
  coframe and reduce explicitly to a scaled standard hyperbolic metric; the
  Laplacian is computed in coordinates.
- **Source changes:** `06-hyperbolic-model.tex`, Appendix C.
- **Status changes:** E2, E3, E6, and T6 promoted to proved.
- **Downstream nodes rechecked:** Paper II operator interface.
- **Reviewer:** independent algebra and geometry reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-016 and OQ-017

- **Decision:** The displayed grid maps are assignment-compatible and generally not
  isometries.  Their map-level relation is
  \(\mathsf Y_n^{-1}\mathsf X_s^n\mathsf Y_n=\mathsf X_s\), \(n\ge2\).
- **Mathematical justification:** metric pullbacks and both sides of the relation are
  computed explicitly.
- **Source changes:** Section 6 and Appendix C.
- **Status changes:** E4--E5 closed with the isometry claim weakened.
- **Downstream nodes rechecked:** abstract and conclusion contain no complexity
  inference.
- **Reviewer:** independent algebra review.
- **Date:** 2026-08-06.

## Resolution — OQ-018 and OQ-020

- **Decision:** The zero theorem is stated for boundaryless surfaces and for interior
  zeros when a boundary is present.  Spatial regularity in a smooth family gives a
  smooth total zero set and a submersive projection, but no global tube without
  additional hypotheses.
- **Mathematical justification:** Section 7 applies the regular-value theorem and
  supplies the missing tangent-space correction for an arbitrary parameter vector.
- **Source changes:** `07-zero-geometry.tex`.
- **Status changes:** T7 and T8 promoted to proved in their stated scope.
- **Downstream nodes rechecked:** Paper III properness warning.
- **Reviewer:** independent algebra and geometry reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-021

- **Decision:** No multi-zero example is included in Paper I.
- **Mathematical justification:** no candidate had a complete domain/metric/
  assignment/singularity/flow/topology audit.
- **Source changes:** Section 7 states the deferral; Paper III records provenance.
- **Status changes:** Z7 deferred to Paper III, removing it from Paper I closure.
- **Downstream nodes rechecked:** abstract, introduction, conclusion.
- **Reviewer:** independent scope review.
- **Date:** 2026-08-06.

## Resolution — OQ-022

- **Decision:** Use a layered synthesis: exact open affine/ACS defect, exact
  target-normalized closed drift, and their common infinitesimal limit.
- **Mathematical justification:** Section 9 proves the two finite formulas and the
  normalized \((h,k)\to(0,0)\) limit separately.
- **Source changes:** `09-contact-curvature.tex`, Appendix D.
- **Status changes:** T17 closed as a synthesis proposition rather than an equality
  of all finite quantities.
- **Downstream nodes rechecked:** abstract and conclusion.
- **Reviewer:** independent geometry and final mathematical reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-023, OQ-024, and OQ-025

- **Decision:** \(\mathbb H^2\) denotes the upper half-plane,
  \(\mathcal D=\ker\alpha\) the horizontal distribution, \(\lambda\) a fixed
  intensity, \(M\) accumulated logarithmic scale, and \(\delta_H\) the scalar
  horizontal covariant differential.
- **Mathematical justification:** the notation is consistent across Sections 4--9;
  \(\delta_H^2\) is explicitly only an antisymmetrized scalar shorthand and is not
  a nilpotent graded complex.
- **Source changes:** Sections 4--9 and Appendices A--D.
- **Status changes:** notation conflicts closed for Paper I.
- **Downstream nodes rechecked:** Paper II README interface.
- **Reviewer:** independent scope and mathematical reviews.
- **Date:** 2026-08-06.

## Resolution — OQ-059 and OQ-064

- **Decision:** During mathematical restructuring, retain `aeg-paper.tex` as the root canonical Paper I entry; after closure, move it to `paper-1/aeg-paper-1.tex` during
  mathematical restructuring.  Identify the Zenodo DOI as an earlier archived
  version, not the current manuscript.
- **Mathematical justification:** this minimizes path churn and prevents release
  metadata from overstating what the existing DOI represents.
- **Source changes:** root README, manuscript date block, source inventory.
- **Status changes:** repository layout and DOI distinction closed for Paper I;
  future publication metadata still requires author approval.
- **Downstream nodes rechecked:** build script and later-paper README files.
- **Reviewer:** independent repository and scope reviews.
- **Date:** 2026-08-06.

## Paper III disposition — OQ-037 through OQ-046

The canonical Paper III manuscript changes the disposition of this cluster as
follows.  A disposition marked partial closes the printed construction problem but
retains the stronger naturality or classification problem.

### OQ-037 — partially resolved

Paper III defines a structural discriminant with separate critical-zero, boundary,
singular/metric, domain/category, and nonproper-escape loci.  It proves stability on
proper vertically transverse regions.  A canonical Whitney stratification of the
full union remains open.

### OQ-038 — resolved by descriptive naming

No canonical historical `E_k` indexing principle was found.  The manuscript removes
the symbol from theorem names and calls the verified objects parallel `k`-zero,
logarithmic-cover, product-tube, and helical models.  Whether a restricted natural
category later supports an index remains open.

### OQ-039 — resolved in the metric-flexible category

The conformal realization theorem turns every smooth submersion into a regular AES.
The explicit choice `a=e^x product_j(y-c_j)` realizes exactly `k` zero components,
and `a=e^x sin y` realizes a locally finite countable family.  A canonical or
complete universal model remains open and is separated from bare existence.

### OQ-040 — remains open; a flexibility obstruction is proved

Conformal realization disproves any unqualified uniqueness expectation when the
metric may vary.  Uniqueness under a fixed metric, completeness, curvature,
asymptotic, homogeneous, or history-natural constraints remains open.

### OQ-041 — partially resolved by examples

The definite and indefinite parameterized Morse functions give verified
AEG-compatible birth/death and reconnection examples.  A transverse simple complex
polynomial discriminant gives `w^2=tau`.  These are not claimed as a complete
classification of AEG metric germs.

### OQ-042 — partially resolved

The cylindrical product and compact helical families are proved proper.  The
escape-to-infinity family proves why no general properness inference is available.
Criteria for broader noncompact families remain open.

### OQ-043 — resolved for complex roots, open for real-zero functoriality

The rank-two zero-section theorem and square-free polynomial interface produce
`B_n`-valued monodromy, and every braid is realized on the basic hyperbolic AES by
arithmetic-holomorphic fields.  A real assignment has curve zeros and does not
automatically yield `B_n`; a natural assignment-to-root or probe functor remains
open.

### OQ-044 — definition fixed; intrinsic selection remains open

A finite zero thread over a one-manifold base is now a properly embedded
one-dimensional submanifold in a real zero tube whose parameter projection is a
finite-sheeted covering, with the relative-boundary condition when needed.  The
helical slices provide explicit chosen threads.  Functorial, probe-independent
selection from AEG data remains open.

### OQ-045 — remains open for a new AEG decoration

The manuscript prints the conjugation and two stabilization gates, proves the
stateless-scalar collapse, and imports the standard twisted-quandle state-sum
invariance under exact finite-field hypotheses.  No new history-derived AEG
decoration has passed Markov descent.

### OQ-046 — remains open

The fixed affine branch is an Alexander quandle.  Ordinary torsion is exact;
resonant twisted torsion is a nonzero cohomology class, but its planar state sum
collapses to the Alexander-quandle coloring count.  No closure-level separation
beyond Alexander/Burau is claimed.

---

## OQ-071 — Exact descent of the (q=4) automorphic assignment

**State:** CLOSED WITH AN OBJECT-TYPE DISTINCTION

Paper III computes the sign character on the arithmetic generators:

[
\chi(J)=-1,
\qquad
\chi(JT)=-1,
\qquad
\chi(T)=+1.
]

Consequently no scalar normalization on the full orbifold quotient can remove the
nontrivial character.  The mathematically natural alternatives are now fixed:

1. a scalar assignment on (\ker\chi\backslash\mathbb H); or
2. a section of the associated real sign line bundle on the full quotient.

The metric and zero graph descend to the full quotient.  Choosing between the two
equivalent presentations is an object-type convention, not an unresolved character
calculation.

## OQ-072 — Cusp, completion, and properness audit of the Hecke zero network

**State:** PARTIALLY RESOLVED; GENERAL PROPERNESS REMAINS OPEN

The active theorem proves that

[
g=|dW/W|^2
]

has finite distance to the order-four orbit and infinite distance along the cusp.
Upstairs completion adds (4\pi) cone points; the completed full-orbifold length
quotient is complete, and its coarse elliptic images have angle (\pi).

The sign-character cover is now completely identified in the model-specific sense.
It has signature ((0;2;\infty,\infty)); after coarse AEG completion, (W) identifies
it with the complete flat cylinder (\mathbb C^\times).  Retaining the hyperbolic
orbifold structure, its unit tangent bundle is

[
T^1\mathcal O_4^\chi\cong S^3\setminus T(2,4)
]

under the declared cusp compactification.  This closes the topology of that one
index-two cover.  It remains to prove or disprove local finiteness and properness on
the universal cover and other finite-index quotients, and to identify any parameter
family for which the zero incidence is a proper tube.  None of the completion or
link-complement statements is a proper-tube theorem.

## OQ-073 — History-to-relative-divisor functor

**State:** PARTIALLY RESOLVED FOR SUPPLIED REGISTERS; GENERAL FUNCTOR OPEN

Construct a functor from a declared category of marked arithmetic histories to
arithmetic sections or polynomials over a parameter base,

[
H\longmapsto P_H\longmapsto (P_H)_0,
]

such that expression equivalence, composition, field of definition, chirality,
and parameter concatenation are respected.  Determine which kernel of projective
evaluation, if any, remains visible in the divisor.

The (q=4) Hecke construction is currently a special operator-quotient example,
not a solution for all histories.  Paper III now gives a minimal finite test:
the supplied register (u^2=t) forces an equivariant quadratic endpoint divisor,
while its tagged prefix trace and pole cocycle retain strictly more information
than the terminal operator.  In particular, they distinguish (\omega_4) from the
empty history even though their terminal divisors agree.  The construction still
depends on a supplied typed register and its terminal divisor factors through
(\rho); it therefore does not close the general question.

## OQ-074 — Arithmetic versus geometric irreducibility of zero paths

**State:** FINITE ALGEBRAIC TEST RESOLVED; CANONICAL AEG ORIGIN OPEN

Find a finite integral AEG family for which:

* the generic polynomial or section is irreducible over (K(B));
* its geometric factorization over (\overline K(B)) is explicit;
* geometric monodromy, arithmetic Galois action, inertia, and Frobenius cycle types
  can all be computed;
* the resulting sheets admit an AEG interpretation not imposed after the fact.

The finite algebraic test is now explicit.  The quadratic register gives a
constant-geometrically integral Kummer cover with computable Frobenius, while

[
(u^2-t)^2-3
]

is irreducible over (\mathbb Q(\sqrt2)(t)), splits into two irreducible geometric
components after extending constants, and has discriminant
(256\cdot3^2(t^2-3)), local sheet monodromy, and explicit Frobenius cycle types.
What remains open is the last bullet above: these registers are supplied inputs,
not yet canonical outputs of unrestricted AEG histories.

## OQ-075 — Factorization-theoretic zero histories

**State:** OPEN

If inequivalent routes to zero are meant to encode inequivalent irreducible
factorizations, replace the unique-factorization (\mathbb Z[\sqrt2]) test case by
an integral domain or order with nontrivial class or factorization data.  Determine
whether ideal classes, sets of lengths, elasticity, or catenary structure can be
realized as labels or monodromy invariants of a relative AEG zero divisor.

This question is distinct from the Hecke tessellation problem: the latter supplies
arithmetic symmetry and automorphic uniformization, not nonunique factorization by
itself.

## OQ-076 — Marked-history enhancement of Hecke periodic-orbit knots

**State:** OPEN AFTER AN OPERATOR-LEVEL SURJECTION

For every (q=4) marked history whose projective operator is primitive hyperbolic,
Paper III now defines the periodic-orbit knot (K_{\rho(h)}).  The map is surjective,
is invariant under cyclic word shift at the operator-conjugacy level, and sends path
inverse to the time-reversed orbit.  It necessarily collapses every insertion of
the neutral word (\omega_4) and every other marked change preserving the operator
conjugacy class.

Construct a non-tautological decoration of the classical cutting code or periodic
orbit that retains some of the tagged trace, ordinary-domain, divisor, framing, or
local-system data, and prove its behavior under the declared history equivalence.
Only after ambient-isotopy or Markov descent may such a decoration be called a new
knot invariant.

## OQ-077 — Mixed slice--tube naturality and the neutral-word test

**State:** EXPLICIT HORIZONTAL MODEL PROVED; HISTORY-NATURAL LIFT OPEN

The supplied family (P_m(z,t)=z^2-t^m) proves that a single polynomial can
simultaneously control a real singular carrier, a finite root thread, a
discriminant period, a braid, and, for even (m), a linking number.  It also
exhibits the exact information loss

[
1\longrightarrow P_2\longrightarrow B_2\longrightarrow S_2\longrightarrow1.
]

This does not yet connect Paper I's slice torsion to tube monodromy.  Over a
circle base, `Serre transgression' is not the correct language; the proved datum
is monodromy and a pure-braid kernel residue.  Paper I's existing affine torsion
is real-valued, is defined on a restricted add--scale kernel pair, vanishes when
the full affine operator agrees, and does not extend automatically through the
q=4 inversion generator.

Construct an invertible marked-history group or groupoid with a coefficient-path
assignment whose permutation action factors through the q=4 sign character and
whose same-operator fibers map naturally to pure braids or framed braids.  The
first hard test is the neutral word

[
\omega_4=(JT)^4.
]

Its terminal projective divisor equals that of the empty history.  Determine
whether a canonical full-history coefficient path nevertheless gives
(sigma_1^4) in the two-sheet cusp-thread target, (z_4^{-1}) in the four-sheet
unit-tangent target, an order-weighted framed class, or zero.  The two targets
are distinct and need not agree.  Prove invariance under
the declared history relations and every coordinate/register gauge before using
the output as an AEG datum.

The ordinary two-braid extension cannot simultaneously identify both q=4
elliptic relators with one unit-tangent fiber winding.  A positive solution must
therefore use an orbifold-weighted normalization, a higher-strand framed
configuration, or prove that the unit-tangent and polynomial residuals are
genuinely different structures.  The supplied four-strand Garside/rotation
calibration now matches the unit-tangent central extension exactly, but it does
not derive those coefficient paths from the q=4 dessin or from unrestricted
marked histories.  Naturality of that path selection is the remaining test.

---

# Part X. Notes reserve (added by the notes reserve audit, 2026-08-10)

The following three entries were registered by
`governance/notes-reserve-audit.md`.  The full inventory, grading, conflict
ledger, and disposition recommendations live in that file.

## OQ-078 — Notes reserve: promotion candidates and their integration audits

**Priority:** P3
**State:** OPEN

Eight note clusters carry complete working-note proofs that are not yet in any
paper:

1. `notes/analysis-and-calculus/02` — mixed additive-multiplicative integration
   (transport, splitting, adjoint pairing, continuous ACS triple identity);
2. `notes/analysis-and-calculus/03` — graded covariant delta-calculus, twisted
   product, twisted Rota--Baxter identity, dual weight-line geometry;
3. `notes/thermodynamics-and-renormalization/05` — AEG/thermodynamics
   contactomorphism, Maxwell relations in AEG variables, the constant-(λ,μ)
   incompatibility remark, Massieu representation;
4. `notes/thermodynamics-and-renormalization/07` — fixed-N algorithmic
   thermodynamic contactomorphism;
5. `notes/foundations-and-geometry/04` — affine torus holonomy toy model;
6. `notes/foundations-and-geometry/05` (elementary part) — charge homomorphism,
   ideals of ℤ, and the normal-subgroup lattice in F₂;
7. `notes/knots-and-loops/06` — Fox calculus and affine cocycle dictionary
   (BS(1,2) part beyond Paper III §8);
8. `notes/knots-and-loops/08` — small-knot embeddings in the three-parameter
   arithmetic-expression group.

Each cluster needs a full integration audit (statement/proof match, chronology
and sign conventions, field and regularity hypotheses, frame conventions
against the current papers) before it may enter any paper or be marked `PROVED`
beyond the working-note level.

## OQ-079 — Notes reserve: conflict and correction ledger

**Priority:** P3
**State:** OPEN

The audit records nine conflicts or corrected statements between the historical
sources and the current papers: E₀/E₁ naming inversion (C-1), the
"threadlike = left-child-leaf" definition (C-2), the reversed-path ACS formula
(C-3), the −2 Laplace eigenvalue (C-4), the coordinate-extended δ (C-5),
reversal-only torsion (C-6), tubes in Paper I (C-7), the erroneous
"dense singularity" in `notes/knots-and-loops/05` (C-8), and the former
placement of CR/twisted-harmonicity/Appell material in Paper I (C-9).

These are recorded, not reconciled.  Closing any of them requires an authorized
task that updates the affected note header, the governance register, and any
dependent reference.

## OQ-080 — Notes reserve: open programs with pass/fail criteria

**Priority:** P3
**State:** OPEN

The audit identifies five open programs whose pass/fail criteria are already
stated in the notes:

1. **PD₃ Milestone 1** (`notes/computation-and-resources/05`): exhibit
   `[κ]=μλ[du∧dv]≠0` on the torus stage T²×(a₋,a₊) and compute its
   Poincaré--Lefschetz dual relative 1-class; retire the milestone explicitly
   if not attempted.
2. **Turing-machine resource torsion** (`notes/computation-and-resources/03`):
   classify the memory-increment reorderings that are realizable by
   semantics-preserving program transformations; without this the torsion is
   only a diagnostic.
3. **Cayley model curvature** (`notes/foundations-and-geometry/01`): verify or
   falsify K=−2 almost everywhere for the Manhattan-distance conformal factor.
4. **Algorithmic-thermodynamics bridge** (`notes/thermodynamics-and-renormalization/06`, `08`):
   complete the Gibbs/partition correspondence beyond the fixed-N
   contactomorphism, carrying the corrections recorded in note 09.
5. **Contact-comparison conjecture** (`notes/projective-condensation/01`, §10):
   relate the AEG horizontal distribution to the canonical contact structure of
   T¹H² via an explicit Gauss/Iwasawa chart, intertwining arithmetic generators,
   brackets, and base projection.

---

## OQ-081 — Is ripple geometry intrinsic to the arithmetic word?

**Priority:** P2
**State:** OPEN

**Question:** the dual reading developed in Paper 0 §§4--6 pulls back standard
horocycles through a projective arithmetic operator.  Every proved statement
there is stated with respect to the standard horocycle family `H_t` and hence
with respect to one chart.  Is there a formulation in which the pole, the
pulled-back family, and the fixed points are attached to the *word* rather than
to a chosen realisation?

**Why it matters:** the name *ripple geometry* is used in Paper 0 only as a
descriptive label (`STRUCTURAL PROPOSAL`).  A positive answer would convert it
into a theorem-level statement and would supply the projective AES that
`00a` §5 and Paper 0 §12.4 list as an open programme.

**Current evidence:** `thm:p0-ripple-pencil-formula` (line/circle dichotomy),
`thm:p0-four-matrix-readings` (one matrix, four readings), and
`prop:p0-path-ripple-duality` are proved; no chart-independent formulation
exists in the repository.

**Default rule while open:** cite the proved formulas, never the name, as the
mathematical content.

**Resolution condition:** either an intrinsic definition with a proof that the
horocycle-chart construction is a special case, or a counterexample showing that
two words with the same operator have inequivalent dual families.

**Affected files:** `paper-0/sections/04-ripple-geometry.tex`,
`paper-0/sections/06-projective-unification.tex`,
`paper-0/sections/12-interface.tex`.
**Affected theorem nodes:** `def:p0-ripple-pencil`,
`thm:p0-ripple-pencil-formula`, `prop:p0-path-ripple-duality`.
**Owner:** author.
**Decision record:** `governance/00b-paper-0-geometric-foundation-amendment.md` §4.

## OQ-082 — Canonical choice of punctures

**Priority:** P2
**State:** REOPENED (2026-09-29).  Was RESOLVED for smoothly extending
assignments (2026-09-22), with the non-extending case reopened as OQ-088.  The
resolution does not hold as written; see the amendment at the end of this entry.

**Question:** `def:p0-punctured-aes` declares a finite puncture set `S`.  Can `S`
be determined by the arithmetic data instead of being stipulated, and is the
choice unique when it exists?

**Resolution.**  `Decision:` when the assignment extends to a smooth function
`a~` on the ambient surface, the puncture set is not a choice: it is exactly the
critical set of `a~`.
`Mathematical justification:` `thm:p0-punctures-are-critical` proves both
inclusions.  If `p` is a puncture and `d a~(p) != 0`, then the template metric
`g~ = |d a~|^2_{g_0} g_0 / (mu^2 + lambda^2 a~^2)`, built with any smooth
background metric `g_0`, is a smooth non-degenerate metric on a neighbourhood of
`p` satisfying the eikonal identity, so the regular structure extends across `p`,
contradicting local essentiality.  Conversely, if `d a~(p) = 0` and `p` is not a
puncture, the eikonal identity read at `p` gives `0 = mu^2 + lambda^2 a(p)^2 >=
mu^2 > 0`, a contradiction.  Hence `S = {d a~ = 0}`.
`Source changes:` Paper 0 §11 gained `lem:p0-gradient-nonvanishing`,
`thm:p0-punctures-are-critical`, `rem:p0-puncture-hypothesis`, and
`cor:p0-puncture-count`.
`Status changes:` the new nodes are `PROVED`; `thm:p0-four-circle-model` now has a
forced, not stipulated, puncture set, because its assignment satisfies
`Crit(P) ∩ D_r = {0}`; and the `k`-puncture question became a question about
smooth functions with exactly `k` critical points.
`Downstream nodes rechecked:` `def:p0-punctured-aes`,
`prop:p0-puncture-tangent-cone`, `thm:p0-four-circle-model`,
`op:p0-four-circle`, and Paper I's `prop:isolated-zero-singular-model`, which
does *not* satisfy the hypothesis (its assignment is not `C^1` at the puncture)
and is therefore the subject of OQ-088.
`Reviewer:` author.
`Date:` 2026-09-22 (evening).

**Amendment (2026-09-29) — the justification above is invalid.**
`Decision:` unchanged in spirit, but it is **not** established for smoothly
extending assignments, and the question is reopened.
`Reason:` the template metric `g~ = |d a~|^2_{g_0} g_0 / (mu^2 + lambda^2 a~^2)`
satisfies the eikonal identity, but nothing makes it agree with the **given** `g`
on the punctured neighbourhood; condition (ii) of `def:p0-punctured-aes` requires
extending `g` itself.  That missing step is the entire content of the "so the
regular structure extends across `p`" clause above.
`Counterexample (verified):` on the unit disc minus the origin with `a = x`,
`mu = lambda = 1` and `g = dx^2/(1+x^2) + dy^2/(x^2+y^2)`, the pair `(M,g,a;1,1)`
is a regular AES with `|grad a|_g^2 = 1 + x^2 = mu^2 + lambda^2 a^2`; `a` extends
smoothly to the whole disc; `g` does not extend at all, since
`g_yy = 1/(x^2+y^2)` is unbounded at the origin, so condition (ii) holds; yet
`S = {0}` while `Crit(a~) = emptyset`.  The same model translates to any interior
point, so the puncture is forced nowhere in this species.
`What survives:` the reverse inclusion `Crit(a~) subseteq S` (its proof uses the
eikonal identity only at a point of `M`), and `thm:p0-four-circle-model` (there
`d a~(0) = 0`, so the defective branch is never entered).
`Sufficient repair:` if in addition `g` is conformal, near each puncture, to a
metric extending smoothly and non-degenerately, then the eikonal identity forces
`g` to *be* the template metric and the original argument goes through.  The
counterexample evades this because `g_yy/g_xx = (1+x^2)/(x^2+y^2)` has no finite
nonzero limit at the origin.  Whether this hypothesis is also necessary is open.
`Status changes:` `thm:p0-punctures-are-critical` and `cor:p0-puncture-count` are
now `UNSUPPORTED AND EXCLUDED` as printed in
`governance/05b-paper-0-status-register.md`; `rem:p0-puncture-hypothesis` is
`PARTIALLY PROVED`.  No paper source is edited.
`Evidence:` root review `AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md`;
retained record `notes/foundations-and-geometry/10`; ledger entry C-10 in
`governance/notes-reserve-audit.md`.
`Reviewer:` DeepSeek Harness Agent (external review), 2026-09-29.
`Date:` 2026-09-29.

**Retained body (superseded default rule).**

**Why it matters:** the exploration register behind Paper 0 §11 states, as its
first unfinished item, that the choice of the two extra punctures in the
cut-and-glue accounting is not known to be canonical.

**Current evidence:** the register's topological witness (χ = #cycles(σ) = b,
exhaustive over 40320 gluings) and the verified one-puncture model
`prop:isolated-zero-singular-model` of Paper I.

**Default rule while open:** a puncture is always declared, never derived.  (For
smoothly extending assignments this default is now replaced by the theorem.)

**Affected files:** `paper-0/sections/11-holed-aes.tex`,
`notes/foundations-and-geometry/06-hole-obstructions-ledger.md`.
**Affected theorem nodes:** `def:p0-punctured-aes`,
`prop:p0-puncture-tangent-cone`, `thm:p0-punctures-are-critical`.
**Owner:** author.
**Decision record:** migration M-0022.

---

## OQ-088 — Canonical punctures when the assignment does not extend

**Priority:** P2
**State:** OPEN

**Question:** `thm:p0-punctures-are-critical` was to canonicalize the puncture set
when the assignment extends smoothly to the ambient surface (amended 2026-09-29:
that theorem is refuted as printed; the question is therefore *not* confined to
the non-extending case — see the OQ-082 amendment).  The disc model
imported from Paper I does not extend: there the metric extends smoothly across the
centre while the assignment is continuous but not `C^1`.  What plays the role of
the critical set in that case, and is the puncture then unique?

**Why it matters:** the two verified punctured models are of different species.
In the four-circle model the *metric* is what cannot be extended
non-degenerately and the punctures are forced by the assignment; in the disc
model the *assignment* is what fails, and the puncture set is still a
stipulation.
*(**Amended 2026-09-29.**  The contrast as drawn is too generous to the first
species.  "Metric cannot be extended" does not by itself force the punctures: the
counterexample recorded in the OQ-082 amendment is of exactly that species and
its puncture is forced nowhere.  What separates the four-circle model from it is
not the species but the fact that there `d a~(0) = 0`.  The dividing line that
survives is conformality of `g` near the puncture to a metric that extends.)*

**Current evidence:** ~~`thm:p0-punctures-are-critical`~~ (amended 2026-09-29:
refuted as printed, do **not** rely on it; see the OQ-082 amendment) and
`rem:p0-puncture-hypothesis` (Paper 0 §11, now `PARTIALLY PROVED`); Paper I's
`prop:isolated-zero-singular-model`, where `a_D` behaves like `rho` near the
centre and the one-sided derivatives differ.

**Default rule while open:** for a model whose assignment does not extend, `S` is
declared, and the "hole" language of Paper 0 §11 stays descriptive.

**Resolution condition:** a replacement for the critical set (for instance a
jet-level, blow-up, or one-sided-derivative criterion) that determines `S` for
assignments with a prescribed failure of differentiability, with a uniqueness
proof or a counterexample.

**Affected files:** `paper-0/sections/11-holed-aes.tex`.
**Affected theorem nodes:** `def:p0-punctured-aes`,
`thm:p0-punctures-are-critical`.
**Owner:** author.
**Decision record:** migration M-0022.

## OQ-083 — Does tearing admit a positive, non-linear description?

**Priority:** P3
**State:** OPEN

**Question:** Paper 0 §10 proves that the arithmetic generators do not close
into a finite-dimensional Lie algebra and that no observable of the
commutativized charges detects tearing.  Are there algebraic structures in which the
tearing is not an obstruction but a computable object, and can they be defined
intrinsically for AES rather than imported as a vocabulary?

**Why it matters:** the two propositions are refusals; a positive description
would replace a methodological position by a theory.

**Current evidence:** `prop:p0-arithmetic-generators` and
`prop:p0-characters-cannot-see-tearing` (proved here); the structural proposals
of `Yuan2026ProcessGeometry` and the exact calibrations matching
`eq:p0-bs-relation` (research-local, with that repository's own maturity labels).

**Default rule while open:** the imported vocabulary is labelled
`STRUCTURAL PROPOSAL` and is never used as a hypothesis of a theorem.

**Resolution condition:** an intrinsic structure on AES whose objects are the
two-history defects, with at least one nontrivial computation that the
commutativization cannot reproduce.

**Affected files:** `paper-0/sections/10-beyond-linear.tex`,
`paper-0/sections/08-acs-tearing.tex`.
**Affected theorem nodes:** `def:p0-tearing`, `prop:p0-arithmetic-generators`,
`prop:p0-characters-cannot-see-tearing`.
**Owner:** author.
**Decision record:** `governance/00b-paper-0-geometric-foundation-amendment.md` §4.

## OQ-084 — Two precision defects of the hole-obstruction register

**Priority:** P3
**State:** OPEN

**Question:** the exploration register records six obstructions while its
summary sentence speaks of five classes, and it identifies the `Z_3` monodromy
of its frame witness with a `Z_4` twist of sheet labels that appears in a
different computation.  Neither point is resolved.

**Why it matters:** Paper 0 §11 reproduces the six witnesses and explicitly
declines both identifications; if the identification is in fact correct, a
future revision must say so with a proof, and if it is not, the register should
carry a correction.

**Current evidence:** the register's table has six rows while its header says
五类; the two computations involve different groups and no source in the
repository relates them.

**Default rule while open:** Paper 0 counts six and records the discrepancy
(`rem:p0-holed-register-bookkeeping`); the identification is listed among the
non-claims of `subsec:p0-holed-nonclaims`.

**Resolution condition:** a proof or disproof of the identification, and a
corrected count in the register.

**Affected files:** `paper-0/sections/11-holed-aes.tex`,
`notes/foundations-and-geometry/06-hole-obstructions-ledger.md`,
`temp/孔的不可避免性_v0.1.md` (working original, not edited by this task).
**Affected theorem nodes:** none; the items are registered as
`COMPUTATIONALLY VERIFIED EXAMPLE` only.
**Owner:** author.
**Decision record:** migration M-0019 in `governance/migration-log.md`.

---

## OQ-085 — Attach AES data to the four-circle configuration

**Priority:** P2
**State:** RESOLVED (2026-09-22)

**Question:** construct an oriented surface, a finite puncture set containing
the origin, and data `(g,a)` on the complement such that the resulting object is
a punctured AES, such that the four limiting circles of
`prop:p0-puncture-tangent-cone` arise naturally from that data, and such that the
origin is non-extendable.

**Why it matters:** the review of 2026-09-22 observed correctly that the
tangent-cone computation is a statement about a curve configuration and that no
AES structure had been attached to it.

**Resolution.**  `Decision:` the configuration is realized as the *zero locus* of
an explicit punctured AES, not as an auxiliary curve family.
`Mathematical justification:` take the punctured disc of radius `r < rho`, the
assignment `a = P` where `P` is the union polynomial of the four circles, and the
metric `g = |grad a|^2 (dx^2+dy^2)/(mu^2+lambda^2 a^2)`, which is exactly the
metric the eikonal identity forces.  The critical set of `P` is computed exactly
(`grad P = 0` only at the origin on that disc, by the case analysis in the
proof), so `g` is a smooth Riemannian metric and `(M,g,a)` is a regular AES; the
factorization of `P` shows that its zero locus is precisely the four circles;
and non-extendability at the origin follows because a regular AES has
`|\nabla a| >= |mu| > 0` (`lem:p0-gradient-nonvanishing`), while `P` is critical
at the origin and any smooth extension of `a` must agree with `P` there by
continuity.  The metric is incomplete with the puncture at finite distance.
`Source changes:` Paper 0 §11.2 gained `lem:p0-gradient-nonvanishing` and
`thm:p0-four-circle-model`; the paragraph stating that no AES data were attached
was replaced; §11.6 gained the generalization problem.
`Status changes:` `lem:p0-gradient-nonvanishing` and `thm:p0-four-circle-model`
are `PROVED`; this issue is resolved; `op:p0-four-circle` now names the
generalization question instead of the construction.
`Downstream nodes rechecked:` `prop:p0-puncture-tangent-cone` (now the tangent
cone of the zero locus of an explicit model), `def:p0-punctured-aes` (a second
verified instance), Paper I's complete-splitting theorem (its completeness
hypothesis fails in this model, which is what permits the branching).
`Reviewer:` author, on the agent's construction.
`Date:` 2026-09-22.

**Superseded text (kept for the record).**  The earlier body of this issue, whose
`Default rule while open` was "cite the tangent-cone computation as an algebraic
statement about the configuration only", is retained here because the repository
does not delete resolved issues:

**Current evidence:** the exact expansion
`(S_2^2-4rho^2y^2)(S_2^2-4rho^2x^2) = S_2^4-4rho^2S_2^3+16rho^4x^2y^2` and the
verified one-puncture disc model of Paper I; no bridge between them.

**Affected files:** `paper-0/sections/11-holed-aes.tex`.
**Affected theorem nodes:** `def:p0-punctured-aes`,
`prop:p0-puncture-tangent-cone`.
**Owner:** author.
**Decision record:** the response to the 2026-09-22 review, item R7; migration
M-0021.

---

## OQ-087 — Generalize the four-circle model

**Priority:** P3
**State:** OPEN

**Question:** `thm:p0-four-circle-model` produces one puncture and four zero
branches from a prescribed polynomial assignment.  Which curve configurations
arise as zero loci of punctured AES in this way, can a `k`-punctured model be
built without stipulating `S`, and does the construction survive if the
assignment must come from the arithmetic motions rather than being prescribed?

**Why it matters:** the construction shows that the configuration is realizable
as a zero locus; it does not show that it is realizable as an *expression*.  The
difference is exactly the AEG question.

**Default rule while open:** cite `thm:p0-four-circle-model` for the one-puncture
construction only, and never as a statement about motion-generated assignments.

**Resolution condition:** a criterion on curve configurations that are zero loci
of punctured AES, with either a construction for `k >= 2` or a proof that the
assignment cannot be motion-generated.

**Affected files:** `paper-0/sections/11-holed-aes.tex`.
**Affected theorem nodes:** `thm:p0-four-circle-model`.
**Owner:** author.
**Decision record:** migration M-0021 in `governance/migration-log.md`.

## OQ-086 — A history monoid with declared relations, and descent of the charge map

**Priority:** P2
**State:** RESOLVED (2026-09-22)

**Question:** which relations should the history monoid carry, and does the
charge map descend to the resulting quotient?

**Resolution.**  `Decision:` adopt the *free product* choice: histories form the
group `G = (R,+) * (R,+)` generated by the additive and multiplicative step
families, with relations imposed only within each family (same-family
composition and the identity).  No cross-family relation is imposed.
`Mathematical justification:` with this choice (i) the charge endpoint and the
evaluation are homomorphisms `c: G -> R^2` and `nu: G -> Aff^+(1,R)`, both onto
(`prop:p0-history-homomorphisms`); (ii) `c` is the abelianization, `ker c =
[G,G]`, so the ACS endpoint is `G_ab = R^2`
(`prop:p0-acs-is-abelianization`); (iii) the descent question has the asymmetric
answer of `thm:p0-descent`: the *multiplicative* charge factors through `nu`
(it equals `log` of the linear part, a homomorphism of the motion group), while
the *additive* charge does not.  The witness is the transport element
`h(p,q) = M_q A_p M_{-q} A_{-e^{-q}p}`, which evaluates to the identity motion
(the chronological calculation is in the proof) while carrying charges
`(p(1-e^{-q}), 0)` with `p(1-e^{-q}) != 0`; hence `c` does not vanish on `ker nu`
and cannot factor through `nu`.  This is the reviewer's request carried out: the
monoid of relations is now explicit, and descent is verified relation by relation
--- it holds for the multiplicative charge and provably fails for the additive
one.
`Source changes:` Paper 0 §8 gained `conv:p0-history-group`,
`prop:p0-history-homomorphisms`, `prop:p0-acs-is-abelianization`, and
`thm:p0-descent`, together with three stated consequences (the ACS is the
abelianization of the history language; the charge path is what the endpoint
forgets; the two failure directions are dual).
`Status changes:` the four new nodes are `PROVED` (the convention is a
`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`); this issue is resolved.
`Downstream nodes rechecked:` `def:acs`, `prop:acs-evaluation`,
`ex:p0-distributive-charge-transport` (now an instance of `h(p,q)`-type
transport), `def:p0-tearing` (its hypotheses are unchanged),
`prop:p0-characters-cannot-see-tearing`.
`Reviewer:` author.
`Date:` 2026-09-22.

**Retained body.**

**Current evidence:** `prop:p0-distributive-operator-identity` and
`ex:p0-distributive-charge-transport` (the two expansions share an operator and
have charges `(p,q)` and `(kp,q)`); the abelianization computation in Paper 0 §8
(`Aff^+(1,R)_ab ≅ R_{>0}`).

**Affected files:** `paper-0/sections/08-acs-tearing.tex`,
`paper-0/sections/02-expansion.tex`.
**Affected theorem nodes:** `def:acs`, `prop:acs-evaluation`,
`ex:p0-distributive-charge-transport`.
**Owner:** author.
**Decision record:** M-0020 and M-0021 in `governance/migration-log.md`.

---

## OQ-089 — Is a tearing across a puncture measured by an ACS area or by a holonomy?

**Priority:** P2
**State:** RESOLVED (2026-09-22)

**Question:** on a punctured space a comparison of two motions may have to be
performed around a puncture rather than through it.  Is the relative torsion then
measured by an ACS area, by a holonomy of a loop around the puncture, or by
neither; and in the first case, what are the admissible filling classes?

**Resolution.**  `Decision:` it is measured by the ACS area, in every model; no
canonical holonomy around a puncture exists in the AES data; and what puncturing
changes is only the admissibility of a comparison performed *on the surface*.
`Mathematical justification:` three propositions in Paper 0 §11.4.
(1) `tau(gamma,delta) = xi_gamma - xi_delta` is a function of the two words
(`prop:affine-cocycle-formulas`, `def:relative-torsion`), so it is unchanged by
puncturing, by changing the model, or by changing the realisation.
(2) The two orderings of a rectangle in any regular AES end at points whose
assignments differ by `mu*h*(e^{lambda k}-1) != 0`
(`prop:p0-surface-does-not-close`), so the corresponding surface paths bound no
region: the ACS comparison is the canonical one in every AES, and is not a device
for avoiding holes.
(3) There is no canonical holonomy: the level-set foliation `ker d_a` is
integrable and therefore flat; a curved connection requires added data, and the
one the paper adds (the contact model) has its own canonical curvature form
relative to the charge projection (`prop:p0-curvature-form`), whose holonomy over
a base loop is the rectangle drift of §9; and in models with canonical punctures
the assignment is single-valued on the ambient surface, so there is no monodromy
(`prop:p0-no-puncture-holonomy`).
(4) The admissible fillings are the oriented two-chains of the charge plane with
the given boundary; by `thm:torsion-stokes` the value is independent of the
filling chosen, and puncturing neither adds nor removes classes.
`Source changes:` Paper 0 §11.4 rewritten (it previously proved nothing and
registered the question); `prop:p0-puncture-local-picture` added, computing the
puncture's local geometry.
`Status changes:` the four new nodes are `PROVED`; OQ-089 is resolved; the second
open problem of §11.6 was narrowed to models whose assignment does not extend
(OQ-088).
`Downstream nodes rechecked:` `def:p0-tearing`, `thm:torsion-stokes`,
`prop:p0-tearing-puncture-independent`, `thm:p0-punctures-are-critical`,
`prop:p0-curvature-form`.
`Reviewer:` author.
`Date:` 2026-09-22 (fourth revision of the day).

## Finite-type and ported AES update — 2026-10-09

This update supersedes only the affected conclusions of OQ-082/OQ-088 and the
multi-puncture/multi-wire entries; older dated research and review records are
retained.

**Resolved with hypotheses:** the printed critical-set theorem is repaired
using an extending conformal background for the given metric; some
conformally compactifiable AES exists for every k≥1; full collar data
reconstruct the original finite-type AES; strict finite program substitution
preserves exact evaluation domains; contextual feature factorization and
right-congruent online feature updates are distinguished and proved.

**Still open:**

1. Describe AES with prescribed conformal moduli, prescribed puncture locations
   or zero configurations, or assignments generated intrinsically by motions.
2. Construct an AES-compatible plumbing/degeneration family. Standard FN and
   plumbing data reconstruct auxiliary conformal/hyperbolic geometry, not g,a.
3. Relate the concrete circle deformation and three-sheet branched model to
   faithful arithmetic data. Neither is a proof of the tangent-ring AES.
4. Construct actual opposite-edge characteristic objects in a declared Adva
   experiment; prove observation sufficiency and, where needed, right
   congruence or retain the separating process residue.
5. Realize generic multi-input arithmetic gates by AES motions on a suitable
   configuration/fibre carrier, retaining source, occurrence, partial domains,
   conjugation/transport and the declared history equivalence.
6. Define productive feedback or fixed-point semantics for cyclic triadic
   inputs. Finite DAG substitution deliberately supplies no such theorem.
7. Recover and archive the original k4 and ported-program ZIP source/checker
   bundles to reproduce their historical 39/55-check evidence. The current
   proof adaptation and new independent verifiers do not close this task.

The scalar tearing identity depends on the words, whereas the new k4 example
has a nonzero full-state level-set residue for a scalar-identity word. These
are different observables, so the new result does not contradict scalar
puncture-independence or assert canonical puncture holonomy.

## OQ-090 — What equality is intended in the distributive marked-data clause?

**Priority:** P1 — blocks completion of the full §2 proposition, not its
operator-identity component.

**State:** RESOLVED (2026-10-20 continuation).

**Affected node:** `prop:p0-distributive-operator-identity` in
`paper-0/sections/02-expansion.tex`.

**Recorded:** 2026-10-20, Codex (OpenAI).

**Question:** The proposition permits all `p,k` in a field and says the two
words coincide as marked data exactly at `p=k=1`. Its proof compares only
the chronological constant pairs `(p,k)` and `(k,k*p)`. Which data and equality
does the claim intend to preserve?

**Current evidence:** At `p=k=0`, the two constant pairs are both `(0,0)`,
although the proof concludes only `(1,1)`. The step assuming `k` nonzero has no
such hypothesis in the proposition. If operation-labelled histories are
compared instead, `add(1); multiply(1)` and `multiply(1); add(1)` still have
different operation labels at their first positions. Equality of constant
pairs does not supply equality of these marked words.

The operator equation `k*(z+p)=k*z+k*p` is unaffected. Its symbolic semiring
component is checked by the Adva program and separate Lean theorem in
`paper-0/formal/`; the zero-pair computation is a separate Lean statement.
This finding does not identify operators, histories, charges or endpoint
values with one another.

**Historical default while open:** Preserve the manuscript; register the whole
proposition as `PARTIALLY PROVED`, with the operator component retained.
Do not attach its coincidence clause to a successful formal receipt.

**Resolution condition:** Explicitly choose constant-pair equality or complete
marked-history equality, correct the parameter scope and conclusion, supply
the corresponding proof including zero/unit cases, then update the source,
status register, statement map and any downstream uses. A nonzero-scaling
restriction can repair the constant-pair computation but does not make the
operation-labelled words equal.

### Resolution — 2026-10-20

The amended manuscript defines a marked step by its operation label, operand
slot and constant. The two distributive words are always different at their
first operation labels. Its separate chronological scalar projection forgets
those labels and agrees exactly at `(p,k)=(0,0)` or `(1,1)`. The source proof
now handles `k=0` before using cancellation in the nonzero case. No zero
arithmetic input is deleted to make a group statement pass.

`marked_words_distinct`, `constant_pair_coincidence` and
`nonzero_constant_pair_coincidence` in
`paper-0/formal/Chapter02Domains.lean` formalize these distinct claims over
explicit field laws. The original symbolic operator certificate and initial
zero-counterexample evidence are preserved. The status register now marks
the **corrected** proposition `PROVED` and retains the earlier failed clause
as a dated finding. The charge-transport example uses `p=1, k=exp(q)` and
requires only the unchanged operator identity and its stated nonzero charge
conditions; its downstream interpretation is not enlarged by this repair.

The same source revision distinguishes affine self-maps from affine group
elements and ordinary partial division from non-degenerate projective
continuation. `c=0` leaves a partial zero map on `K\{0}`, not a Möbius map.
Source-to-formal correspondence remains an explicit reviewed mapping, not a
claim that TeX prose was mechanically translated. Implementation and review
by Codex (OpenAI); no independent human mathematical review is asserted.

## OQ-091 — Information order and directed completeness of AEG histories

**Priority:** P3
**State:** PARTIALLY RESOLVED (2026-10-31) — the marked-spinal-history case is
settled; the branching case and a concrete value-domain instantiation remain
open.

**Question:** Can the histories treated in
`notes/analysis-and-calculus/09-order-topology-scott-lawson.md` — expression
trees, rewrite graphs, computation DAGs — be given an information order
`h ⊑ h'` ("`h'` refines / extends `h`") under which they form a dcpo
(directed-complete partial order), so that evaluation `ev` becomes a
Scott-continuous (directed-sup preserving) map?

**Why it matters:** This is the precondition for importing the Scott-topology
machinery into AEG's "history → compression → representation → geometry" ladder.
Without it, "the value of a limit process is the limit of its finite-history
values" (`ev` continuous) has no domain on which continuity is even defined.

**Current evidence:** `09` §8 now settles the marked-spinal-history case: the
information order is the chronological prefix order `γ ⊑ γδ`; its ideal
completion is the dcpo of finite and infinite histories (finite histories =
compact elements); and the free-dcpo universal property makes `ev` extend
Scott-continuously iff `ev` is monotone. Ordinary arithmetic evaluation fails
that test (the value field is not a dcpo, and `ev` is partial and non-monotone).

**Default rule while open:** Treat "Scott continuity of evaluation" as a
structural proposal, not a theorem; state no limit-of-histories convergence
result.

**Resolution condition:** Exhibit an information order on a fixed class of
histories, prove directed completeness, identify the compact (finite) elements,
and prove `ev` preserves directed suprema (or record the obstruction).

**Affected files:** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`.
**Affected theorem nodes:** none (research note; no paper node depends on it).
**Owner:** author.
**Decision record:** `governance/notes-reserve-audit.md` §2.7 (coverage gap).

### Partial resolution — 2026-10-31

For the marked spinal histories of `def:marked-spinal-history`
(`paper-1/sections/02-sequential-histories.tex`):

1. **Information order** = chronological prefix order `γ ⊑ γ' ⟺ γ' = γδ`,
   read directly from `eq:chronological-history-concatenation`.
2. **Directed completeness**: the ideal completion of the prefix-ordered free
   monoid is `Idl(H) ≅ Γ^∞ = Γ^* ∪ Γ^ω`, the dcpo of finite and countably
   infinite histories; the finite histories are exactly the compact elements,
   and each infinite history is the directed join of its finite prefixes
   (classical ideal-completion theorem, instantiated).
3. **Evaluation**: by the free-dcpo universal property, `ev` extends to a
   Scott-continuous map on all histories iff `ev` is monotone. Ordinary
   arithmetic evaluation is not monotone (and is partial, with a non-dcpo value
   field), so it is **not** order-continuous; this is recorded as the
   obstruction, and it motivates the lower-semicontinuous/monotone sector and
   the projective continuation of `paper-1/sections/03-projective-affine.tex`.

Remaining open: the branching (non-spinal) case, the concrete monotone-sector +
value-dcpo instantiation, and the reconciliation with projective continuation.

## OQ-092 — Order-theoretic placement of the additive versus multiplicative sides

**Priority:** P3
**State:** RESOLVED (2026-10-31) — the correspondence is made precise on the
value lattice `[0,∞]`, with a correction to `09` §6 (the dual side is carried by
the reciprocal involution, not by multiplication itself). The operator-level
backward-adjoint tie-in is folded into OQ-093.

**Question:** The correspondence in `09` §6 ("Scott ⟷ additive / forward /
accumulation side; lower topology ⟷ multiplicative / backward / scaling side")
is currently an intuition. What map or realization sends the AEG add/scale
process structure to a value-lattice order so that the correspondence becomes a
theorem (or is refuted)?

**Why it matters:** This is the bridge that would justify reading AEG's one-sided
accumulation as lower semicontinuity (`[0,1]`-valued, Scott topology) and its
backward adjoint as the dual/lower side, rather than a loose analogy.

**Current evidence:** `09` §9 now constructs the map. On the continuous lattice
`L=[0,∞]`, the additive generator `T_s(a)=a+s` is a Scott-continuous embedding
and is exactly the way-below witness (`a ≪ b ⟺ ∃s>0: a+s ≤ b`); the
multiplicative generator `D_k(a)=ka` is a Scott-automorphism (order
automorphism). The dual/lower side is carried by the order-reversing reciprocal
`¬(a)=1/a`, a homeomorphism `(L,σ) → (L,ω)` conjugating `D_k` to `D_{1/k}`.
The §6 wording "lower topology ⟷ multiplication" was therefore imprecise and is
corrected.

**Default rule while open:** Keep the Scott/lower correspondence as a heuristic;
cite it only as such.

**Resolution condition:** A concrete map from add/scale processes to a continuous
frame (or a counterexample), plus a proof that Scott-continuity ↔
lower-semicontinuous accumulation and the dual topology ↔ the backward side hold
under that map.

**Affected files:** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`,
`notes/analysis-and-calculus/02-mixed-affine-integration.tex`.
**Affected theorem nodes:** none.
**Owner:** author.
**Decision record:** `governance/notes-reserve-audit.md` §2.7 (coverage gap).

### Resolution — 2026-10-31

On the continuous lattice `L=[0,∞]` with Scott topology `σ` and lower topology
`ω`:

1. **Additive side**: the additive generator `T_s(a)=a+s` (`s≥0`) is a
   Scott-continuous embedding (not onto for `s>0`) and is precisely the
   way-below witness: `a ≪ b ⟺ a < b ⟺ ∃s>0, a+s ≤ b` (with the compact bottom
   `0` as the sole exception). So addition = the approximation / way-below
   primitive of the Scott topology — the "accumulate from below" direction.
2. **Multiplicative side**: `D_k(a)=ka` (`k>0`) is an order-automorphism, hence
   a Scott-homeomorphism (the "scale symmetry" primitive); in log coordinates it
   is a translation.
3. **Dual side**: the reciprocal `¬(a)=1/a` (`0↔∞`) is an order-reversing
   bijection, hence a homeomorphism `(L,σ) → (L,ω)`, and `¬∘D_k∘¬ = D_{1/k}`,
   i.e. it interchanges the forward scale `e^M` and the backward multiplier
   `e^{-M}`. So the lower/backward side is carried by the involution, and
   `ω = ¬_*σ`; this is exactly Warner's omitted involution.

Consequently the §6 correspondence holds in the refined form: additive ⟷ Scott
(way-below / forward accumulation); multiplicative ⟷ Scott-automorphism (scale
symmetry); lower/backward ⟷ reciprocal involution. The earlier statement that
multiplication itself is the "lower-topology side" was corrected. The remaining
task — matching `¬` with the backward adjoint `p(b)=1` of
`02-mixed-affine-integration` at the operator-equation level — is folded into
OQ-093.

## OQ-093 — Scott ∨ lower = Lawson as the topological form of backward-adjoint completion

**Priority:** P3
**State:** RESOLVED (2026-10-31) — the backward-adjoint multiplier is the
reciprocal-involution image of the forward scale, and their join is exactly the
Lawson (Euclidean/Hausdorff) topology; see resolution below.

**Question:** Does adjoining the dual (lower) topology to Scott — i.e. passing to
the Lawson topology — realize AEG's two-sided (add × multiply, forward ×
backward) structure, with the recovery of the Hausdorff/Euclidean topology
corresponding to the backward-adjoint completion of
`02-mixed-affine-integration`?

**Why it matters:** This is the strongest potential payoff of the Warner import:
it would explain "补上 Warner 故意丢掉的对合" as "从 Scott 升到 Lawson", i.e.
the missing involution side = the backward adjoint multiplier = the lower
topology. It is currently a conjecture.

**Current evidence:** `09` §10 now proves the correspondence. From
`02-mixed-affine-integration.tex`, the forward scale is `K(t)=e^{M(t)}` and the
backward adjoint is `p(t)=exp(∫_t^b v)`, `p(b)=1`; a direct computation gives
`p(t)=e^{M(b)}·¬(K(t))` with `¬(a)=1/a`. By `09` §9.3, `¬` is an order-reversing
homeomorphism `(L,σ)→(L,ω)`. Hence the forward scale is the Scott (from-below)
side, the backward adjoint is the lower (from-above) side, and their join is
Lawson = Euclidean.

**Default rule while open:** Do not claim the add/multiply double-sided structure
is the Scott/Lawson double-sided structure.

**Resolution condition:** A proof (or counterexample) that the backward
adjoint/dual side of the AEG mixed calculus corresponds, under OQ-092's map, to
the lower topology, so that their join recovers the classical symmetric geometry.

**Affected files:** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`,
`notes/analysis-and-calculus/02-mixed-affine-integration.tex`.
**Affected theorem nodes:** none.
**Owner:** author.
**Decision record:** `governance/notes-reserve-audit.md` §2.7 (coverage gap).

### Resolution — 2026-10-31

From `02-mixed-affine-integration.tex` (`eq:acs-path`, `eq:adjoint-solution`),
with multiplicative charge `M(t)=∫_a^t v`:

1. forward scale `K(t)=e^{M(t)}` (direct / past weighting);
2. backward adjoint `p(t)=exp(∫_t^b v)`, `p(b)=1`, solving `-p'(t)=v(t)p(t)`;
3. direct computation: `p(t)=e^{M(b)-M(t)}=e^{M(b)}·¬(K(t))`, `¬(a)=1/a`.

By `09` §9.3, `¬` is an order-reversing homeomorphism `(L,σ)→(L,ω)` with
`ω=¬_*σ`. Therefore:

- forward scale `K` = Scott / lower (from-below) side: `K(t)>a ⟺ M(t)>log a`;
- backward adjoint `p=¬(K)` (mod the constant `K(b)`) = lower / dual (from-above)
  side: `p(t)>a ⟺ M(t)<M(b)-log a`;
- their join `σ ∨ ω = λ` = Lawson = the Euclidean topology on `[0,∞]` /
  `[−∞,+∞]` (classical).

So backward-adjoint completion = adjoining `¬(K)` = passing Scott → Lawson =
recovering the Hausdorff/Euclidean topology, exactly as OQ-093 conjectured. The
constant `K(b)=e^{M(b)}` is the reference scale fixed by the terminal condition
`p(b)=1`.

Residual (non-blocking remark): a functional-level statement that the mixed
integral `𝔐[u;v]=∫_a^b p·u` is itself Lawson-continuous on the two-sided data is
not yet formulated; the additive source `u` enters via the way-below primitive
of `09` §9.2 and the pairing `eq:adjoint-pairing`.

Addressed in `09` §11 (2026-10-31): `𝔐` is separately Scott-continuous in `u`
and in `v` (nonnegative densities), and `∫u·p` is the two-sided duality pairing
— the functional-level form of Scott ∨ lower = Lawson.

## OQ-094 — Scott/Lawson reading of the Paper I affine sector and PGL₂

**Priority:** P3
**State:** 094a RESOLVED (2026-10-31) — the provable core, the Galois-connection
step, and the functorial language are all closed
(`11-oq094a-proof-skeleton.md`, `12-galois-connection-oq094a.md`,
`13-functorial-language-oq094a.md`). The precise form of 094a is: `Scott ⟷
Aff^+ = C(σ)∩B_∞ = {ka+s : k>0, s≥0}`, `Lawson ⟷ PGL₂ = ⟨Aff^+, ¬⟩`, with
"adjoin ¬" commuting (`Φ(σ∨¬_*σ) = ⟨Φ(σ),¬⟩`), and it is a natural isomorphism
of "generating data + adjoin ¬", *not* a full Galois equivalence over `Top(L)`
(three proved reasons: `A(σ)=A(λ)`, `H(λ)=Stab([0,∞])⊊PGL₂`,
`¬T_s¬∈E(σ)∖Aff^+`).

094b RESOLVED (2026-10-31) — `14-rho-scott-continuity-boundary.md` proves the
clean negative: `ρ` is monotone only for the trivial preorder (so no
Scott-continuous extension to the history dcpo `Γ^≤ω`), and the only candidate
limit extension is the infinite matrix product = continued-fraction convergence,
which is the excluded "general convergence theory for infinite arithmetic
expressions" (Paper II/III). This gives Paper I's finite-word scope an
order-topological + analytic justification.

094c RESOLVED (2026-10-31, core) — `15-branching-history-dcpo.md` gives the
branching-history dcpo: information order = down-set (order-ideal) embedding
("sub-computation"), ideal completion = finite ∪ infinite computation DAGs
(each operation with finitely many predecessors), compact = finite; the spinal
prefix order is the chain specialization (Theorem 2); partial evaluations form
the finite distributive lattice `O(P)` and legal evaluation orders = linear
extensions = maximal chains = spinal histories (Theorem 3, Birkhoff). Residual
(non-blocking): carrying the operation/constant/chirality labels, and the
branching `ev` Scott-continuity sector.

094d RESOLVED (2026-10-31) — `16-hecke-history-boundary.md`: the Hecke history
space `Γ_4^≤ω` is a Cantor space (proved in `10`/`12`); `G_4 ≅ C₂*C₄` is
virtually free so its space of ends is a Cantor set, while `G_4 = H(√2)` is a
first-kind Fuchsian lattice whose limit set is the full circle `P^1(ℝ)` (not
Cantor). The history Cantor space codes the space of ends (the symbolic
boundary), realizing the history-level form of
`rem:hecke-history-operator-coset`. This corrects `10` §4's "Cantor boundary"
wording (Cantor = ends, not limit set). Full cellulation + limit-set
correspondence is deferred to Paper II/III.

All of OQ-094 (094a–094d) is now addressed.

**Question:** The `09` note closes its value-lattice chain, but that chain works
on `[0,∞]` and on the analysis layer (`02-mixed-affine-integration`). Can the
same Scott/Lawson framework be read back into the Paper I *main body* — the
history layer (`paper-1/sections/02-sequential-histories.tex`) and the
projective semantics (`paper-1/sections/03-projective-affine.tex`) — so that the
affine/projective dichotomy and the Bruhat decomposition acquire an
order-topological meaning?

**Why it matters:** The three generators of `09` §9.1 are literally the three
elementary contexts of Paper I (`T_s = C_{+,s}^{(1)}`, `D_k = C_{×,k}^{(1)}`,
`¬ = C_{/,1}^{(2)}`), so "Scott → Lawson" (adjoining the reciprocal involution)
is group-theoretically the same move as "affine sector `B_∞` → `PGL₂`"
(adjoining the projective step `J = -1/z`). If this is made precise it gives
Paper I §3's affine/Borel placement and rank-one Bruhat decomposition a
topological justification rather than a purely algebraic one.

**Current evidence:** `10` §1–§5 record the precise correspondences and the
honest negative result (the operator map `ρ` carries no dcpo order on `PGL₂`,
so "Scott continuity of ρ" is not well-posed until an order is fixed; the
infinite-history limit of `ρ` is the infinite matrix product = continued-fraction
convergence, i.e. the excluded convergence theory of Paper II/III). The
history-layer topology is classical: the prefix dcpo's Lawson topology on
`Γ^∞ = Γ^* ∪ Γ^ω` is the product topology (Cantor space for finite `Γ`, Baire
space for countable `Γ`).

**Default rule while open:** Keep the "Scott ⟷ affine sector, Lawson ⟷ PGL₂"
correspondence as a `structural proposal`; cite it only as such; do not state a
topological equivalence between `B_∞` and a Scott space or between `PGL₂` and a
Lawson space. Per `11` §2/§6, the precise reading is `Scott ⟷ Aff^+` (the
positive affine *semigroup* `{ka+s : k>0, s≥0}`, = `B_∞ ∩ Stab([0,∞])`) and
`Lawson ⟷ PGL₂ = ⟨Aff^+, ¬⟩`; the group `⟨T_s(s≥0), D_k(k>0), ¬⟩` *does* equal
`PGL₂` (since `D_{-1} = T_1¬T_{-1}¬T_1¬`), but the Scott *side* is the
semigroup `Aff^+`, whose group closure is the identity component `B_∞^+ =
{ka+s : k>0, s∈ℝ}`, not all of `B_∞`; the reflection `D_{-1}` requires `¬`.
Distinguish semigroup from group closure, and `B_∞^+` from `B_∞`, when writing
these.

**Resolution condition:** For 094a, an explicit functor/order matching the
`[0,∞]` Scott/Lawson structure to `B_∞`/`PGL₂` at the level of generators and
Bruhat cells, respecting the three domain caveats of `10` §3. For 094b, a clean
statement and proof of the "infinite matrix product = out-of-scope convergence"
boundary. For 094c, a directed-complete sub-DAG refinement order on branching
histories with identified compact elements. For 094d, a history-level
topological realization of the Hecke cell/coset interface
`rem:hecke-history-operator-coset`.

**Affected files:**
`notes/analysis-and-calculus/10-scott-lawson-on-paper-1-main-body.md`,
`notes/analysis-and-calculus/11-oq094a-proof-skeleton.md`,
`notes/analysis-and-calculus/12-galois-connection-oq094a.md`,
`notes/analysis-and-calculus/13-functorial-language-oq094a.md`,
`notes/analysis-and-calculus/14-rho-scott-continuity-boundary.md`,
`notes/analysis-and-calculus/15-branching-history-dcpo.md`,
`notes/analysis-and-calculus/16-hecke-history-boundary.md`,
`notes/analysis-and-calculus/09-order-topology-scott-lawson.md`.
**Affected theorem nodes:** none (research note; no Paper I theorem node depends
on it yet).
**Owner:** author.
**Decision record:** `11` §6 (2026-10-31, v0.3) refines `10` §2: the correct
levels are the semigroup `Aff^+ = {ka+s : k>0, s≥0}` (= `B_∞ ∩ Stab([0,∞])`),
its group closure `B_∞^+ = {ka+s : k>0, s∈ℝ}` (identity component), the full
affine group `B_∞ = B_∞^+ ⊔ D_{-1}B_∞^+`, and `PGL₂ = ⟨Aff^+, ¬⟩` via
`D_{-1} = T_1¬T_{-1}¬T_1¬`. The reflection `D_{-1}` is dual data (requires
`¬`), so `B_∞` is not purely order-one-sided. `12` §3 (2026-10-31) proves the
Galois-connection commutativity: at the homeomorphism level
`Homeo(L,σ)∩PGL₂ = {D_k}` and `Homeo(L,λ)∩PGL₂ = Stab([0,∞]) = ⟨D_k,¬⟩`
(reaching only a proper subgroup), while at the endomorphism level
`Aff^+ = C(L,σ)∩B_∞` and `⟨Aff^+,¬⟩ = PGL₂` (the full group); the latter is
what makes "Lawson ⟷ PGL₂" hold. `13` (2026-10-31) completes the functorial
language: the correspondence is the commutative square on the generating set
`S_0 = {T_s, D_k}` with "adjoin ¬" naturality `Φ(σ∨¬_*σ) = ⟨Φ(σ),¬⟩`, and it
is *not* a full Galois equivalence over `Top(L)` (the three functors
`A, E, H` respectively collapse `σ`/`λ`, overshoot, or undershoot — proved in
`13` §4). `14` (2026-10-31) resolves 094b: `ρ` is monotone only for the trivial
preorder (Thm 1), so it has no Scott-continuous extension to the history dcpo;
the only candidate limit extension is the infinite matrix product =
continued-fraction convergence (Thm 2), i.e. the excluded convergence theory.
`15` (2026-10-31) resolves 094c (core): branching histories form the dcpo
`Idl(FinDAG)` = finite ∪ infinite computation DAGs under down-set (order-ideal)
embedding, compact = finite; the spinal prefix order is the chain
specialization; partial evaluations = the finite distributive lattice `O(P)`
with linear extensions = maximal chains = spinal histories (Birkhoff). `16`
(2026-10-31) resolves 094d: the Hecke history space is a Cantor space coding
the space of ends of the virtually-free group `G₄ ≅ C₂*C₄` (not the limit set —
`H(√2)` is first kind with limit set `P^1(ℝ)`), correcting `10` §4.

## OQ-095 — Macro Stokes and the full DAG Lie realization (residuals of the Scott–Lawson thread)

**Priority:** P3
**State:** OPEN (2026-10-31) — registered from
`governance/scott-lawson-paper-1-integration-2026-10-31.md` §5; sub-items
095.1–095.4.

**Question:** The Scott/Lawson thread (`notes/analysis-and-calculus/09`–`20`)
established the provable core that the contact curvature `μλ` is the order
defect of the minimal branching DAG `{A,M}`, integrated as a group-valued
1-cocycle (`20`). The macroscopic generalization — the "discrete Stokes on
`O(P)`" for arbitrary branching DAGs, and the full DAG Lie realization — is not
yet established.

**Why it matters:** This is the step that upgrades "Contact = the infinitesimal
form of the minimal DAG" (`17`) to "the curvature `μλ` integrates over an
arbitrary `O(P)` to the order defect between any two threads" (`19` §3). It is
the integration theory that links the infinitesimal (contact) to the
macroscopic (DAG), and it is the gate to a faithful bulk-boundary
correspondence beyond the minimal antichain.

**Current evidence:** `20` proves the defect is a 1-cocycle on the
linear-extension graph (telescoping additivity, local defect = conjugated
commutator, hexagon = Jacobi identity). `19` §2 proves the holographic Stokes
for the minimal case. The four residuals below are open.

**Default rule while open:** Cite the macro Stokes and the full DAG Lie
realization only as `structural proposal` / `open problem`; do not state a
defect integral for arbitrary `P` as proved.

**Resolution condition:**
- 095.1 (higher-order brackets): identify the BCH higher-order terms
  `[X,[X,Y]]`, `[Y,[X,Y]]`, … with the defects of nested antichain edges in
  `O(P)`'s higher-dimensional cells.
- 095.2 (full DAG Lie realization): a functor from the branching-history dcpo
  (`15`) to a free Lie algebra / free flow group, generalizing `18`'s `F` from
  two generators to an arbitrary generator set.
- 095.3 (macro Stokes): assemble `19` §3 into a full statement — the defect
  between two threads of arbitrary `P` = `∫∫ μλ` over the region — using the
  1-cocycle (`20`) and the additivity/exactness/spectral docking.
- 095.4 (spectral docking): `O(P)`'s Scott/Lawson topology (`15` §6) as the
  spectral space of the discrete Stokes complex.

**Affected files:**
`notes/analysis-and-calculus/15-branching-history-dcpo.md`,
`notes/analysis-and-calculus/18-limit-smoothing-functor.md`,
`notes/analysis-and-calculus/19-integration-and-bulk-boundary.md`,
`notes/analysis-and-calculus/20-defect-1-cocycle-bch.md`.
**Affected theorem nodes:** none (research notes; no paper theorem depends on
them yet).
**Owner:** author.
**Decision record:** `governance/scott-lawson-paper-1-integration-2026-10-31.md`.

## OQ-096 — Pants, interface disks and certified capping

**Priority:** P2
**State:** OPEN (2026-10-31); 096.1 has a completed V1 finite example, with
general composition still open. Sub-items 096.2–096.4 remain open.
**Origin:** Mingli Yuan asks to clarify pants, DAG substitution, the shared
boundary's cap and its spectral value before assigning geometric meaning to
Adva sealing. Codex (OpenAI) formalized the initial proposal and finite
obstruction in note 25; no independent human mathematical review is asserted.

**Question:** Can a decorated finite program be presented by a compatible
ball-and-tube thickening whose surface pants glue along the boundary of an
internal interface disk, while interface states compose by exact substitution
and retained evidence supports a precisely scoped closure certificate?

**Current evidence:**
`notes/analysis-and-calculus/25-pants-interface-disks-and-substitution.md`
gives short proofs for a specified topological model, the polynomial interface
example, and the impossibility of a compact regular AES disk with constant
assignment on its entire boundary when mu is nonzero. Paper IV PIV-S1–S4
already supply finite program substitution and conditional collar descent.
The model's canonical AEG status and its relation to native Seal are open.

**Sub-items and resolution conditions:**

- **096.1 — Decorated finite thickening and composition.** Start with the
  two-node example `z=x+y; w=zt`: construct and check a finite cellulation,
  local manifold links, the disk/seam boundary identity, four external ports,
  and exact correspondence to substitution. Then extend to compatible
  composition, preserving slots, sources, occurrences and distinct receipts;
  reject global feedback. The single example does not close this sub-item.
- **096.2 — Interface state, spectrum and reopening.** Define the observation
  algebra/state carrier; distinguish equal numerical values from production
  identity; demonstrate recovery of retained residuals under a stronger
  observer. An ordinary operator spectrum, the order spectrum and the
  interface character space are not identified by terminology. No bridge from
  the algebraic spectrum `Spec Q[z]` (value layer) to the Stone spectrum of the
  down-set lattice `O(P)` (order layer) is established; whether the compact-open
  lattice of the former relates to the down-set lattice `O(P)` of the latter is
  open. The seam-circle holonomy is the analytic realization of the order defect
  (derived from `P` through curvature + Stokes), linked to the algebraic spectrum
  only by the constant-boundary capping obstruction, not by derivation
  (`rem:three-interface-layers`).
- **096.3 — AES extension or explicit singular capping.** Specify actual
  metric/assignment collars and prove their extension or the exact obstruction.
  Respect note 25's constant-boundary obstruction and Paper 0's essential
  puncture definition; a numerical port label is not constant geometric
  boundary data.
- **096.4 — Evidence-preserving native Seal bridge.** Define a map from one
  explicit geometric closure obligation to the current witness kernel and
  prove what its additive/multiplicative residual checks certify. Retain body,
  source history and nonzero obligations. A disk or a matching value alone
  cannot issue Seal.

**Default rule while open:** Use the specified thickening only as a research
presentation. Do not identify it with a regular AES, an ideal-completion
boundary, a TQFT or native Adva admission. Keep pure dataflow scheduling
separate from noncommuting actions on a shared accumulator. OQ-095 remains
open and is not a prerequisite for the finite topological example.

**Finite update (2026-10-31):** V1 is implemented at
`research/pants-interface-disks/`: 56 cubes, 336 tetrahedra, all 132 whole-body
vertex links checked, two three-boundary pants and one four-boundary side
surface. The explicit internal disk fills the seam circle, whereas the
side-surface mod-two boundary matrix has rank 110 and augmented rank 111:
the same circle does not bound a surface two-chain. Exact substitution gives
interface 5 and output 20. Ten negative controls reject; normal/optimized
output and fresh-process saved-candidate reception agree. This is one
same-author finite calibration, not a general thickening functor or native
Adva execution. It records Mingli Yuan's complementary surface-hole/body-disk
view as a precisely bounded result.

**Affected files:** note 25 and `research/pants-interface-disks/` (V1).
**Affected theorem nodes:** none; the new proofs remain in the working-note
reserve and require integration audit before manuscript promotion.
**Owner:** author.
**Next bounded target:** note 25 V2 (equal interface values with distinct
production residuals). General composition is V3; the AES/Seal bridge is V4.
Their results must not be inferred from V1 success.

---

## OQ-097 — The surface series (Magnus series projected to the Legendre quotients)

**Priority:** P2
**State:** OPEN (2026-10-31) — registered with the calculus-dictionary surface
column rewrite; the series pillar is developed for the bulk, not for the
surface.

**Question:** The Magnus series `Ω(γ)` of the series pillar (Paper I §6) is
expanded in the free Lie algebra of the bulk contact model. What is its
reduction to the two Legendre quotients — the charge plane `π` and the Reeb
quotient `Q` — and in what sense is that reduction a "surface series"?

**Why it matters:** The calculus dictionary's surface column is now the
Legendre pair `(π, Q)`, whose differential and integral calculus are symbolic
(`e^{M_*−M} dA∧dM` on `π`, `dvol` on `Q`). The series column has no
corresponding symbolic surface form: the only candidate reduction is the
continued fraction as a canonical `Q`-boundary form
(`prop:bulk-boundary-series-reduction`), which is a structural proposal, not a
theorem. A symbolic surface series would complete the four-column dictionary
(classical / bulk / surface / series) on the Taylor row.

**Current evidence:** `prop:bulk-boundary-series-reduction` records the degree
descent (two-form curvature → one-form potential, Stokes) and the cocycle
reduction (interior cancellations by the 1-cocycle closure), both proved, and
the continued-fraction canonical form, a structural proposal. The PBW
abelianization (`thm:pbw-abelianization-difference-substitution`) is a bulk
abelianization, not a projection to `π` or `Q`.

**Default rule while open:** Do not state a symbolic "surface series" as proved.
Cite the continued fraction only as a structural proposal; keep the series
column's surface cell marked open (OQ-097).

**Resolution condition:**
- 097.1: a well-defined reduction of `Ω(γ)` to the charge plane `π` (the
  `e^{−M}`-normalized / weighted series) with a convergence or asymptotic
  statement.
- 097.2: a well-defined reduction to the Reeb quotient `Q` (the hyperbolic /
  continued-fraction side) and its relation to 097.1 under Legendre duality.

**Affected files:** `paper-1/sections/07-calculus-dictionary.tex`,
`paper-1/sections/06-series-theory.tex`.
**Affected theorem nodes:** none (no Paper I theorem depends on a surface
series).
**Owner:** author.
**Decision record:** the surface series is the series-side counterpart of
OQ-095.3/OQ-095.4 (macro Stokes and spectral docking); registered alongside the
calculus-dictionary surface-column rewrite of 2026-10-31.

