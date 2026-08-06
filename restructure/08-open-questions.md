# Open Questions and Decision Register

**File:** `restructure/08-open-questions.md`
**Status:** Authoritative issue register
**Version:** 1.0
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `restructure/00-authoritative-scope.md`
* `restructure/01-paper-series-architecture.md`
* `restructure/02-paper-I-outline.md`
* `restructure/03-theorem-dependency-graph.md`
* `restructure/04-current-to-target-map.md`
* `restructure/05-mathematical-status.md`
* `restructure/06-editorial-rules.md`
* `restructure/07-acceptance-checklist.md`

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
**State:** OPEN

### Question

Under what hypotheses can one conclude that zero components are:

* properly embedded lines;
* circles;
* finite in number?

### Current evidence

The regular-value theorem only gives a one-dimensional submanifold locally.

### Default rule while open

Make no global classification.

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
**State:** OPEN

### Question

Should `gpt/` remain in place with archival status or move under `restructure/archive/`?

### Default rule

Preserve paths until references and provenance have been audited.

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
**State:** OPEN

### Question

Should `build.sh` support paper selection, or should each paper have its own build script?

### Default rule

Keep Paper I build stable first.

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
* [ ] OQ-021 — multi-zero example inclusion
* [ ] OQ-022 — local-global synthesis formulation
* [ ] OQ-023 — (\mathcal H) notation collision
* [ ] OQ-024 — (\lambda/M) notation
* [ ] OQ-025 — (\delta/\delta_H) notation
* [ ] OQ-059 — repository migration timing
* [ ] OQ-064 — DOI/version distinction

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
OQ-031–OQ-058
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
