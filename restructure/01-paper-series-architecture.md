# AEG Paper Series Architecture

**File:** `restructure/01-paper-series-architecture.md`
**Status:** Authoritative
**Version:** 1.1
**Date:** 2026-08-06
**Depends on:** `restructure/00-authoritative-scope.md`
**Applies to:** Papers I–IV of the Arithmetic Expression Geometry series

---

## 1. Purpose

This document defines the architectural relationship among the first four papers in the Arithmetic Expression Geometry series.

It specifies:

* the dependency graph among the papers;
* the mathematical objects owned by each paper;
* the interfaces through which later papers depend on earlier ones;
* the shared notation and conventions;
* the rules for importing, extending, or replacing earlier definitions;
* the migration of existing repository material;
* the conditions under which results may be cited across papers.

This document does not replace the detailed scope of each paper. The authoritative scope remains:

```text
restructure/00-authoritative-scope.md
```

The purpose here is to ensure that the four papers form one coherent research program rather than four partially overlapping expositions.

---

## 2. Series-level thesis

The first four papers study successive layers of a single process-to-result architecture:

[
\boxed{
\text{syntax}
\longrightarrow
\text{history}
\longrightarrow
\text{operator}
\longrightarrow
\text{geometry}
\longrightarrow
\text{quotient or observable}.
}
]

The four papers divide this architecture as follows:

[
\begin{array}{ll}
\textbf{Paper I:} &
\text{foundational objects and the affine geometric sector};[2mm]
\textbf{Paper II:} &
\text{analysis on the regular affine/hyperbolic geometry};[2mm]
\textbf{Paper III:} &
\text{singular zero geometry and parameterized topology};[2mm]
\textbf{Paper IV:} &
\text{projective quotients, condensation, and complexity}.
\end{array}
]

The papers must preserve the distinction between the following levels:

[
\text{expression tree}
\longrightarrow
\text{marked spinal history}
\longrightarrow
\text{projective or affine operator}
\longrightarrow
\text{assignment state}
\longrightarrow
\text{endpoint value}.
]

A later paper may quotient, enrich, or analyze an earlier object, but it must not silently identify two distinct levels.

---

## 3. Global dependency graph

The primary paper dependency graph is:

[
\boxed{
\begin{tikzcd}[column sep=large,row sep=large]
& \text{Paper II: Hyperbolic Analysis}
\
\text{Paper I: Foundations}
\arrow[ur]
\arrow[r]
\arrow[dr]
&
\text{Paper IV: Projective Condensation and Complexity}
\
& \text{Paper III: Singular Zeros and Tubes}
\end{tikzcd}
}
]

In plain form:

```text
Paper I ──→ Paper II
Paper I ──→ Paper III
Paper I ──→ Paper IV
```

A secondary dependency may later be used:

```text
Paper II ──→ selected analytic tools in Paper III
```

This secondary dependency is optional. Paper III must not rely on an unproved or unpublished analytic theorem from Paper II unless the theorem is reproduced or stated conditionally.

There is no required dependency:

```text
Paper III ──→ Paper IV
```

or

```text
Paper IV ──→ Paper II.
```

Cross-references may be added, but the main theorem architecture must remain acyclic.

---

## 4. Architectural layers

The series is organized into four layers.

### Layer A: Historical syntax

Objects:

* arithmetic expression trees;
* dependency posets;
* sequential trees;
* marked spinal histories;
* chirality words;
* one-hole contexts;
* history composition;
* temporal reversal;
* mirror;
* path inverse.

Owner:

```text
Paper I
```

All later papers inherit these definitions.

---

### Layer B: Operator semantics

Objects:

* affine transformations;
* Möbius transformations;
* projective evaluation;
* affine cocycles;
* relative operator defects;
* the affine/Borel sector;
* projective completion.

Primary owner:

```text
Paper I: foundational semantics
Paper IV: full quotient and condensation theory
```

Paper I defines the operator semantics needed to locate the affine theory. Paper IV develops the full projective and quotient consequences.

---

### Layer C: Geometric realization

Objects:

* arithmetic flow;
* assignment functions;
* regular AES;
* the basic hyperbolic model;
* ACS;
* torsion;
* contact connection;
* horizontal differential;
* zero loci.

Primary owner:

```text
Paper I
```

Extensions:

```text
Paper II: analytic geometry
Paper III: singular and parametric geometry
Paper IV: metric and quotient complexity
```

---

### Layer D: Derived structures

Objects:

* horizontal harmonic analysis;
* arithmetic holomorphicity;
* singular strata;
* tube geometry;
* monodromy;
* projective condensation;
* complexity measures.

Owners:

```text
Paper II: analysis
Paper III: singular topology
Paper IV: quotient and complexity
```

These objects must be defined using interfaces exported by Paper I.

---

# Part I. Paper ownership

## 5. Paper I ownership

Paper I owns the canonical definitions of:

* sequential arithmetic tree;
* marked spinal history;
* chirality word;
* one-hole arithmetic context;
* ordinary arithmetic evaluation;
* projective evaluation;
* affine sector;
* affine cocycles;
* arithmetic flow;
* regular arithmetic expression space;
* basic hyperbolic model;
* regular zero locus;
* foundational singular AES;
* ACS;
* relative affine torsion;
* arithmetic contact connection;
* horizontal covariant differential.

Later papers must cite or import these definitions rather than reintroducing competing versions.

Paper I also owns the notation and hypotheses associated with these definitions unless an extension is explicitly declared.

---

## 6. Paper II ownership

Paper II owns the canonical definitions of:

* compatible horizontal metric;
* horizontal orientation;
* compatible almost-complex structure;
* horizontal volume form;
* analytic domains and function spaces;
* horizontal Laplacian;
* formally adjoint operators;
* AEG Dirichlet and Neumann problems;
* arithmetic harmonicity;
* twisted harmonicity;
* arithmetic Cauchy–Riemann operators;
* arithmetic holomorphicity;
* analytic kernels and continuation results.

Paper II must not redefine the contact distribution or affine flow.

It may add analytic data to the Paper I structure:

[
(M,g,a,\alpha,\mathcal H)
\quad\leadsto\quad
(M,g,a,\alpha,\mathcal H,g_H,J,d\mathrm{vol}_H).
]

This enrichment must be stated explicitly.

---

## 7. Paper III ownership

Paper III owns the canonical definitions of:

* stratified singular AES;
* singular zero germ;
* multi-zero model;
* zero-set discriminant;
* parameter-space regular stratum;
* regular zero tube;
* singular fiber;
* zero-component monodromy;
* braid transport;
* threading;
* any rigorously defined knot-related invariant.

Paper III extends the foundational singular-AES definition of Paper I.

It must not redefine regular AES or regular zero loci.

The extension should have the form:

[
(M,S,g,a;\mu,\lambda)
\quad\leadsto\quad
(M,\mathcal S,g,a;\mu,\lambda),
]

where (\mathcal S) is a specified stratification or singularity structure.

---

## 8. Paper IV ownership

Paper IV owns the canonical definitions of:

* history category or groupoid;
* evaluation functor;
* operator kernel pair;
* projective relative defect;
* bivaluation;
* point–predicate transport;
* rank-one idempotent representation;
* quotient tower;
* condensation map;
* quotient fiber complexity;
* canonical representative complexity;
* representation complexity;
* geometric complexity;
* computational cost model;
* time and space complexity comparisons.

Paper IV must reuse the projective evaluation introduced in Paper I.

It may enlarge the operator-level object from:

[
\operatorname{Aff}(1,K)
]

to:

[
PGL_2(K)
]

and may study quotient structures such as:

[
G/H,\qquad G/B_\pm.
]

---

# Part II. Exported interfaces

## 9. Paper I export interface

Paper I exports the following data to all later papers.

### 9.1 Syntax interface

A marked spinal history is represented schematically by:

[
\gamma
======

\bigl(
x_0;
(\omega_i,c_i,\varepsilon_i)_{i=1}^{n}
\bigr),
]

with:

[
\varepsilon_i\in{1,2}.
]

The syntax interface includes:

* history length;
* chirality word;
* context composition;
* bounded and free histories;
* admissibility conditions;
* temporal reversal;
* path inverse.

---

### 9.2 Operator interface

Projective evaluation:

[
\rho:
\operatorname{Hist}^{\pm,\times}_K
\longrightarrow
PGL_2(K).
]

Affine restriction:

[
\rho_{\mathrm{aff}}:
\operatorname{Hist}^{\mathrm{aff}}_K
\longrightarrow
\operatorname{Aff}(1,K).
]

The operator interface must specify:

* field assumptions;
* invertibility assumptions;
* domain restrictions;
* ordinary versus projective semantics;
* chronological composition convention.

---

### 9.3 Cocycle interface

For:

[
\rho_{\mathrm{aff}}(\gamma)(x)
==============================

\Phi_\gamma x+\xi_\gamma,
]

Paper I exports:

[
\Phi_{\gamma\delta}
===================

\Phi_\delta\Phi_\gamma,
]

with the exact composition convention stated in the paper, and the corresponding translation cocycle law.

It also exports the source-normalized coordinate:

[
\widehat\xi_\gamma
==================

\Phi_\gamma^{-1}\xi_\gamma.
]

Later papers must not interchange (\xi) and (\widehat\xi) without explicit conversion.

---

### 9.4 Flow interface

Paper I exports the affine flow equation:

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

In coordinate form:

[
da=\mu,du+\lambda a,dv.
]

When a compatible metric has been specified:

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

Later papers must state which of these formulations they assume.

---

### 9.5 Regular AES interface

A regular AES must include at least:

[
\mathfrak E
===========

(M,g,a;\mu,\lambda),
]

together with a stated domain on which the defining equation holds.

Paper I must specify whether:

* (\mu,\lambda) are constants;
* (\mu,\lambda) may vary;
* (M) is connected;
* (M) has boundary;
* (g) is complete;
* (a) is globally defined.

Later papers must not silently add these properties.

---

### 9.6 Zero-set interface

Paper I exports:

[
Z(a)=a^{-1}(0),
]

and, in the singular setting:

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

The regular-zero theorem applies only under the stated hypotheses, including:

[
\mu\neq0.
]

Paper III must identify precisely where those hypotheses fail.

---

### 9.7 ACS interface

Paper I exports:

* additive charge (A);
* multiplicative logarithmic charge (M);
* the ACS path (C_\gamma);
* the total charge map;
* the weighted one-form;
* relative torsion for compatible histories.

The exact sign and orientation conventions must be fixed once and reused.

---

### 9.8 Contact interface

Paper I exports:

[
\alpha
======

da-(\mu,du+\lambda a,dv),
]

[
\mathcal H=\ker\alpha,
]

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a,
]

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

It also exports:

[
\delta_HF
=========

(D_uF),du+(D_vF),dv.
]

Paper II may equip (\mathcal H) with additional analytic structure. Paper III may pull (\mathcal H) to tube or singular strata. Paper IV may interpret the bracket or holonomy as process residue.

---

## 10. Paper II import contract

Paper II may assume the following Paper I results:

* existence of the regular affine AES framework;
* the basic hyperbolic model;
* the contact distribution;
* the horizontal fields;
* the curvature bracket;
* the regular-zero theorem;
* the affine flow.

Paper II must not assume:

* a canonical horizontal complex structure;
* essential self-adjointness of any operator;
* existence of Green or Poisson kernels;
* boundary regularity;
* spectral completeness;
* a global function theory.

These must be established in Paper II.

---

## 11. Paper III import contract

Paper III may assume:

* regular and singular AES terminology;
* the regular-zero theorem;
* the basic parameter-family zero-surface lemma;
* the affine flow;
* the contact connection;
* the basic hyperbolic model.

Paper III must not assume:

* global properness of the zero family;
* topology preservation across singular parameters;
* a finite number of zero components;
* existence of a global tube;
* braid or knot invariance;
* normal forms for all singularities.

These must be proved or imposed as hypotheses.

---

## 12. Paper IV import contract

Paper IV may assume:

* marked spinal histories;
* projective evaluation;
* (PGL_2) generation;
* the affine/Borel restriction;
* affine cocycles;
* relative affine defects;
* the distinction between histories, operators, and endpoint values.

Paper IV must not assume:

* that every history quotient has a canonical representative;
* that shortest representatives are computable;
* that quotient distance equals computational cost;
* that exponential group growth implies computational hardness;
* that geometric curvature yields complexity lower bounds.

These are research questions for Paper IV.

---

# Part III. Shared notation

## 13. Base fields and number systems

Use:

[
K
]

for a general field.

Use:

[
\mathbb R
]

for real differential geometry.

Use:

[
\mathbb C
]

for complexified or analytic theories.

Use:

[
\mathbb F_q
]

for finite-field models.

A theorem over a general field must not use analytic exponentials or real differential calculus without qualification.

The notation:

[
e^\lambda
]

is reserved for characteristic-zero real or complex settings, unless introduced formally.

---

## 14. Expressions and histories

Recommended notation:

[
T
]

for an expression tree.

[
I(T)
]

for the dependency poset of internal nodes.

[
\gamma,\delta
]

for histories.

[
\varepsilon(\gamma)
]

for a chirality word.

[
r\gamma
]

for temporal reversal, if adopted.

[
m\gamma
]

for mirror, if adopted.

[
\gamma^{-1}
]

for path inverse only when every context is invertible.

The notation must not overload reversal and inverse.

---

## 15. Operators

Use:

[
\rho(\gamma)
]

for projective evaluation.

Use:

[
\nu_x(\gamma)
]

for evaluation of a history at initial value (x), when ordinary evaluation is admissible.

Use:

[
\operatorname{Aff}(1,K)
]

for the affine group.

Use:

[
PGL_2(K)
]

for the projective linear group.

Use:

[
B_\infty
]

for the stabilizer of (\infty), unless another Borel notation is globally adopted.

Use:

[
J(z)=-\frac1z
]

for the Weyl inversion, if that convention is retained.

---

## 16. Affine coordinates

For an affine map:

[
x\mapsto\Phi x+\xi,
]

use:

[
\Phi
]

for accumulated scale.

Use:

[
\xi
]

for target-frame or future-scaled translation.

Use:

[
\widehat\xi=\Phi^{-1}\xi
]

for source-normalized translation.

Do not use (a) simultaneously for the affine translation coordinate and the AES assignment field in the same argument.

---

## 17. AES notation

Use:

[
a
]

for the assignment function or assignment coordinate.

Use:

[
M
]

for the underlying manifold only when no conflict with the ACS multiplicative coordinate occurs.

Where confusion is likely, use:

[
\mathcal M
]

for the manifold and reserve:

[
M
]

for multiplicative charge.

Use:

[
g
]

for a Riemannian metric.

Use:

[
\mathfrak E
]

for a general arithmetic expression space.

Use:

[
\mathfrak E_0
]

for the basic regular hyperbolic model.

Use:

[
\mathfrak E_1
]

only after its singular status and definition have been fixed.

Do not renumber (\mathfrak E_k) casually.

---

## 18. Flow parameters

Use:

[
\mu
]

for additive intensity.

Use:

[
\lambda
]

for logarithmic multiplicative intensity.

State whether:

[
\mu,\lambda
]

are:

* constants;
* functions;
* parameters;
* nonzero;
* positive.

Do not infer positivity from non-vanishing.

---

## 19. ACS notation

Use:

[
(A,M)
]

for ACS coordinates:

* (A): accumulated additive charge;
* (M): accumulated logarithmic multiplicative charge.

Use:

[
C_\gamma
]

for the ACS path of (\gamma).

Use:

[
\Sigma_{\gamma,\delta}
]

for an oriented filling between two compatible histories.

Use one canonical notation for the weighted one-form, preferably:

[
\eta.
]

The sign convention for:

[
d\eta
]

must remain consistent across Papers I, III, and IV.

---

## 20. Contact notation

Use:

[
\alpha
]

for the contact form.

Use:

[
\mathcal H=\ker\alpha
]

for the horizontal distribution.

Use:

[
D_u,D_v
]

for the preferred horizontal lifts.

Use:

[
\delta_H
]

for the horizontal covariant differential, unless a later editorial decision retains (\delta).

If (\delta) is retained, its non-nilpotence must be stated wherever relevant.

Use:

[
\Delta_H
]

for the horizontal second-order operator only after Paper II fixes its exact analytic definition.

Paper I may use a formal expression, but must not assign analytic properties prematurely.

---

## 21. Zero-set notation

Use:

[
Z(a)=a^{-1}(0).
]

Use:

[
Z_{\mathrm{reg}}(a)
]

for regular zero points.

Use:

[
Z_{\mathrm{sing}}(a)
]

for singular zero points.

For a family (a_t), use:

[
\mathcal Z
==========

{(p,t):a_t(p)=0}
]

for the total zero set.

Use:

[
\mathcal D
]

for the discriminant in parameter space.

Do not use “tube” for every total zero set. Reserve it for a total zero set satisfying the regularity and local-triviality conditions adopted in Paper III.

---

## 22. Projective condensation notation

Paper IV should use:

[
G=PGL_2(K)
]

unless a broader group is required.

Use:

[
H
]

for a stabilizer of an ordered pair or reference structure.

Use:

[
B_\pm
]

for point stabilizers when two distinguished projective points are present.

Use:

[
G/H
]

for the bivaluation or ordered-pair quotient only after the stabilizer has been defined.

Use:

[
\Pi
]

for rank-one idempotent projectors.

Use:

[
\mathcal K(\gamma,\delta)
]

for group-valued relative defect, if retained.

---

## 23. Complexity notation

Paper IV should distinguish:

[
C_{\mathrm{syn}}
]

syntactic complexity,

[
C_{\mathrm{word}}
]

word complexity,

[
C_{\mathrm{op}}
]

operator representation complexity,

[
C_{\mathrm{geo}}
]

geometric complexity,

[
C_{\mathrm{time}}
]

time complexity,

[
C_{\mathrm{space}}
]

space complexity.

No equality among these quantities should be assumed by notation.

If a complexity is model-dependent, include the model in a subscript or argument.

---

# Part IV. Shared conventions

## 24. Composition convention

The series must adopt one chronological composition convention.

Recommended convention:

If history (\gamma) applies (g_1) first and (g_n) last, then:

[
\nu_x(\gamma)
=============

g_n\circ\cdots\circ g_1(x).
]

Matrix products must follow the same convention.

Every paper using group multiplication must include a short convention statement.

Do not rely solely on diagram orientation.

---

## 25. Left and right actions

The series must distinguish:

* left group multiplication;
* right group multiplication;
* left Maurer–Cartan form;
* right Maurer–Cartan form;
* source-frame coordinates;
* target-frame coordinates.

No paper may identify operand-slot chirality with left/right group multiplication without an explicit theorem.

---

## 26. Ordinary and projective domains

Each projective arithmetic context must carry domain information.

At minimum, distinguish:

1. ordinary arithmetic domain;
2. projective domain;
3. exceptional point or pole;
4. chart transition.

A projective identity does not imply that every intermediate ordinary arithmetic expression is defined.

---

## 27. Local and global statements

Each result must state whether it is:

* local;
* global;
* chart-dependent;
* defined only on the regular locus;
* valid only under completeness;
* valid only under properness;
* valid only for compact fibers.

A local contact model must not be promoted to a global classification.

A local zero-surface result must not be promoted to a global tube theorem.

---

## 28. Exact and infinitesimal defects

The series must distinguish:

* exact finite affine endpoint defect;
* translation coordinate of relative affine holonomy;
* commutator loop drift;
* infinitesimal bracket;
* curvature two-form;
* ACS weighted area.

These quantities may agree to first order without being equal at finite scale.

The distinction must be retained across Papers I, III, and IV.

---

# Part V. Cross-paper theorem reuse

## 29. Citation of earlier results

A later paper may cite an earlier theorem if:

* the theorem is published or available in a stable preprint;
* the statement and hypotheses match;
* notation changes are explicitly translated;
* no stronger conclusion is inferred.

If an earlier result changes during restructuring, dependent drafts must be updated.

---

## 30. Conditional imports

If Paper II, III, or IV is drafted before Paper I is finalized, imported results must be marked as:

```text
Assuming Theorem X of Paper I.
```

or:

```text
Conditional on the current formulation of the regular AES theorem.
```

Draft dependencies must be tracked in the mathematical-status file.

---

## 31. No circular proof dependencies

The following pattern is prohibited:

```text
Paper I cites a theorem proved only in Paper II,
while Paper II assumes Paper I's result to prove that theorem.
```

If a result is genuinely foundational, it must move to Paper I or be reproved there in the required restricted form.

---

## 32. Shared lemmas

A technical lemma used substantially by multiple papers should be handled in one of three ways:

1. placed in Paper I if foundational;
2. proved in an independent technical note;
3. restated with citation in each paper when short and standard.

Do not maintain divergent versions of the same lemma.

---

# Part VI. Material migration architecture

## 33. Canonical destinations

Existing repository material should be assigned one canonical destination.

### Paper I destination classes

* expression syntax;
* marked histories;
* affine/projective placement;
* affine flow;
* (\mathfrak E_0);
* regular zeros;
* ACS;
* torsion;
* contact geometry.

### Paper II destination classes

* (\delta)-calculus beyond foundational curvature;
* arithmetic holomorphicity;
* twisted harmonicity;
* explicit analytic bases;
* boundary-value ideas;
* analytic kernels.

### Paper III destination classes

* singular AES expansions;
* (E_k);
* (E_{\log});
* multi-zero constructions;
* tube structures;
* threading;
* braid and knot directions.

### Paper IV destination classes

* bivaluation;
* projectors;
* quotient towers;
* process residue;
* condensation;
* resource geometry;
* time–space duality;
* complexity cases.

---

## 34. Migration states

Every relocated block should have one of the following states:

* `moved unchanged`;
* `moved and edited`;
* `split across papers`;
* `retained as summary only`;
* `archived as superseded`;
* `discarded as incorrect`.

The state should be recorded in:

```text
restructure/04-current-to-target-map.md
```

No substantial material should disappear without a recorded state.

---

## 35. Forward references

Paper I may include disciplined forward references such as:

* “The compatible horizontal complex structures are developed in Paper II.”
* “The singular parameter locus and tube topology are developed in Paper III.”
* “The full projective quotient tower is developed in Paper IV.”

Forward references must not summarize unproved future results as established facts.

---

## 36. Avoiding duplicate exposition

When material is moved:

* Paper I should retain only the minimum definition or theorem needed for foundations;
* the later paper should own the detailed development;
* identical full proofs should not be copied into multiple papers;
* a shared proof may be cited if the papers are independently readable.

---

# Part VII. Paper-specific architecture

## 37. Paper I internal architecture

The recommended Paper I progression is:

```text
1. Introduction and architecture
2. Sequential trees and marked spinal histories
3. Projective semantics and the affine sector
4. Affine cocycles
5. Continuous affine flow
6. The basic hyperbolic model
7. Regular and singular zero geometry
8. Global torsion and the ACS
9. Contact connection and horizontal differential
10. Outlook and interfaces to Papers II–IV
```

The exact chapter numbering may change, but the dependency order should remain.

The contact geometry must not appear before the flow and affine cocycle foundations.

The zero-locus theorem must appear after the regular AES and eikonal equation are defined.

---

## 38. Paper II internal architecture

Recommended progression:

```text
1. Analytic data added to the Paper I geometry
2. Horizontal metrics, measures, and adjoints
3. First- and second-order operators
4. Analysis on the basic hyperbolic model
5. Harmonic and boundary-value theory
6. Explicit solution families
7. Arithmetic Cauchy–Riemann theory
8. Relation to classical and hyperbolic complex analysis
```

Arithmetic holomorphicity should follow, not precede, the real operator theory.

---

## 39. Paper III internal architecture

Recommended progression:

```text
1. Singular AES and stratified regular loci
2. Local zero-set singularities
3. Verified multi-zero constructions
4. Parameter spaces and discriminants
5. Regular zero tubes
6. Singular fibers and topology change
7. Monodromy and braid transport
8. Conditional threading and knot invariants
```

Knot material must remain downstream of discriminant and monodromy theory.

---

## 40. Paper IV internal architecture

Recommended progression:

```text
1. History categories and evaluation
2. Full bilateral projective semantics
3. Bivaluations and projectors
4. Quotient towers and process residue
5. Condensation and canonical forms
6. Representation growth
7. Geometric and computational cost models
8. Time–space–representation relations
9. Case studies
```

Complexity claims must come after the quotient and cost models are fixed.

---

# Part VIII. Architectural invariants

## 41. Definitions must be monotone across papers

A later paper may enrich an earlier definition but must not contradict it.

Allowed:

[
\text{regular AES}
\longrightarrow
\text{regular AES with analytic data}.
]

Allowed:

[
\text{singular AES}
\longrightarrow
\text{stratified singular AES}.
]

Not allowed:

* changing the meaning of marked history;
* reversing composition order without warning;
* changing the role of (\mu) and (\lambda);
* renumbering (\mathfrak E_0) and (\mathfrak E_1) independently;
* redefining torsion with an incompatible sign convention.

---

## 42. Hypotheses must be monotone

Later papers may add hypotheses.

For example:

[
\text{smooth AES}
\quad\leadsto\quad
\text{complete smooth AES with bounded geometry}.
]

Later papers must not cite a theorem after dropping a required hypothesis.

---

## 43. Conjectures must retain identity

A conjecture appearing across papers should retain:

* a stable name;
* a stable identifier;
* a statement history;
* a current status.

If revised, the old and new forms must be distinguished.

---

## 44. Examples must not control definitions

No paper should define a general object solely to fit:

* (\mathfrak E_0);
* one (E_k) model;
* one tube picture;
* one finite-field count;
* one complexity example.

Definitions must state their intended generality independently of examples.

---

# Part IX. Architecture validation

## 45. Required checks before major restructuring

Before moving or rewriting a chapter, verify:

1. which paper owns the material;
2. which definitions it imports;
3. which results depend on it;
4. whether the notation is shared;
5. whether the current claim status is known;
6. whether moving it creates a circular dependency;
7. whether an abstract or conclusion must be updated;
8. whether the destination paper already contains a competing version.

---

## 46. Required output of an architecture audit

An architecture audit should list:

* duplicated definitions;
* conflicting notation;
* circular dependencies;
* results used before definition;
* results assigned to the wrong paper;
* claims imported with weaker hypotheses;
* materials lacking a canonical destination;
* unresolved ownership questions.

The audit must not silently repair these issues.

---

## 47. Series-level completion test

The first four papers form a coherent series only if:

1. Paper I can be read independently as the foundation;
2. Paper II imports Paper I without redefining the geometry;
3. Paper III imports Paper I without redefining regular zeros;
4. Paper IV imports Paper I without redefining projective evaluation;
5. no major theorem has circular dependencies;
6. every shared symbol has one canonical meaning;
7. every substantial repository note has a canonical destination or archival status;
8. conjectures and open programs are clearly separated from proved results.

---

# Part X. Interface summary

## 48. Paper interfaces at a glance

### Paper I → Paper II

Exports:

[
(M,g,a;\mu,\lambda),
\quad
\alpha,
\quad
\mathcal H,
\quad
D_u,D_v,
\quad
[D_u,D_v].
]

Paper II adds:

[
g_H,
\quad
J,
\quad
d\mathrm{vol},
\quad
\Delta_H,
\quad
\partial_{\mathrm{AEG}},
\quad
\bar\partial_{\mathrm{AEG}}.
]

---

### Paper I → Paper III

Exports:

[
Z_{\mathrm{reg}}(a),
\quad
Z_{\mathrm{sing}}(a),
\quad
\text{regular-zero theorem},
\quad
\mathcal Z=A^{-1}(0).
]

Paper III adds:

[
\mathcal D,
\quad
\text{singular strata},
\quad
\text{tube topology},
\quad
\text{monodromy}.
]

---

### Paper I → Paper IV

Exports:

[
\operatorname{Hist},
\quad
\rho,
\quad
PGL_2,
\quad
B_\infty,
\quad
\Phi,\xi,\widehat\xi,
\quad
\tau.
]

Paper IV adds:

[
G/H,
\quad
G/B_\pm,
\quad
\Pi,
\quad
\text{condensation},
\quad
C_{\mathrm{rep}},
\quad
C_{\mathrm{time}},
\quad
C_{\mathrm{space}}.
]

---

## 49. Final architectural principle

The series must develop outward from one stable center:

[
\boxed{
\text{history-sensitive arithmetic}
\longrightarrow
\text{operator semantics}
\longrightarrow
\text{geometric realization}.
}
]

Paper II asks what can be analyzed on that geometry.

Paper III asks how that geometry becomes singular and topologically nontrivial.

Paper IV asks what information is lost when histories are quotiented and how that loss relates to representation and computation.

The architecture is successful only if each later paper extends Paper I without forcing Paper I’s foundational objects to be redefined.

---

## 50. Activated Paper I--II--III analytic interface

The optional Paper II to Paper III dependency is now activated for one bounded
interface only:

```text
Paper I:
  projective histories and the q=4 Hecke subgroup
          |
          v
Paper II:
  planar/cylindrical regular AES targets
  + holomorphic local-diffeomorphism pullback
          |
          v
Paper III:
  critical-set singularities
  + Hecke-Hauptmodul zero dessin
  + sign-cover and geodesic-knot interfaces
  + restricted relative arithmetic zero divisors.
```

The dependency remains acyclic.  Paper II proves no singular conclusion, and Paper
I uses no analytic or automorphic theorem from Papers II or III.

### Export contract from Paper I

Paper I exports the explicit projective operators (T_{\sqrt2}) and (J), their
matrix relation, and the identification of the generated subgroup with (G_4).
It does not export a history-to-zero-set functor.

### Export contract from Paper II

Paper II exports:

1. the planar harmonic AES target;
2. the cylindrical AES target;
3. functorial pullback by a holomorphic local diffeomorphism;
4. the associated regular-locus Laplacian and curvature identities.

The export explicitly excludes critical points and singular metric completion.

### Paper III additions

Paper III may combine those exports with standard triangle-group uniformization.
It must prove all AEG-specific zero-set and cone calculations in the active source.
It must distinguish a standard external Hauptmodul input from the newly derived
AEG pullback construction.

The q=4 sign cover has two distinct downstream realizations that must not be
identified.  Its completed coarse AEG quotient is a flat cylinder.  The unit
tangent bundle of the hyperbolic Hecke orbifold is instead the three-dimensional
carrier for periodic-orbit knots; on the same index-two cover its cusp
compactification produces the complement of the two-component torus link
T(2,4).  The equality of the covering character is structural, but the classical
geodesic-flow coding and lens-space compactification remain cited external inputs.

At the operator quotient, primitive hyperbolic q=4 histories map onto oriented
primitive periodic-orbit knots.  Cyclic history shifts become conjugacy, path
inversion gives the time-reversed orbit, and neutral relators exhibit explicit
collapse.  Any enhancement that remembers marked histories inside these fibers is
still open.

### Arithmetic divisor layer

The relative-divisor hierarchy is:

[
\text{history presentation}
\to \text{operator}
\to \text{section over a field of definition}
\to \text{relative prime divisor}
\to \text{geometric sheets}.
]

Arithmetic irreducibility over (K(B)), geometric irreducibility over
(\overline K(B)), topological monodromy, and Galois action must not be identified.
For supplied typed quadratic and quartic registers, Paper III now proves explicit
finite-flat models that are finite etale on the stated discriminant complements,
together with equivariance, collapse kernels, discriminants, geometric splitting,
and Frobenius cycle tests.  These are minimal naturality models, not a construction
of the registers from arbitrary histories.  The general arrow from history syntax
to a canonical arithmetic section therefore remains open.

---

## 51. M-0008 bounded sextic laboratory interface

The sextic Lyashko--Looijenga addition extends Paper III horizontally across four
typed layers without changing the import contracts of Papers I or II:

```text
supplied monic-centered sextic
  |-- critical-value polynomial and LL sheet
  |-- real carrier and six-root thread
  |-- genus-two branched-cover monodromy
  `-- one arithmetic genus-two fiber.
```

The direct Paper III contribution is bounded: it computes the event polynomial
for (x^6-x), proves the displayed spanning-star (B_6) monodromy, constructs the
carrier/thread/mapping-torus readings, and installs the mixed-braid pullback.
LL degree and bifurcation theory, Birman--Hilden and symplectic monodromy, and the
Galois/endomorphism criteria remain cited classical inputs.

There are two successive forgetting operations and they must not be collapsed:

[
\text{normalized sextic sheet}
\longrightarrow
\text{critical-value configuration}
\longrightarrow
\text{double LL discriminant}.
]

The first regular fiber has (1296) coordinate-normalized sheets and (216) free
source-rotation orbits, not (1296) or (216) nonisomorphic genus-two curves.  The
second arrow forgets still more event data.  A future moduli comparison must pass
the finite LL--Igusa twin test before either count acquires a curve-theoretic
interpretation.

Critical-value braiding and root braiding occupy different levels.  Their
architectural interface is the mixed configuration-space extension and its LL
pullback (or the equivalent Hurwitz groupoid), never an unmarked homomorphism
(B_5\to B_6).  This preserves the information-loss direction:

[
\text{LL sheet plus moving test parameter}
\longrightarrow
\text{mixed braid path}
\longrightarrow
\text{six-root braid}.
]

The genus-two mapping-class, integral symplectic, mod-two permutation, and
arithmetic Galois layers may be compared only through their declared maps.  The
abstract isomorphism (\operatorname{Sp}_4(\mathbb F_2)\cong S_6) is a common
finite target, not a canonical matching between individual Frobenius elements and
topological loops.

This laboratory supplies strong evidence that one polynomial can coordinate real,
complex, topological, and arithmetic readings.  It does not supply a functor from
general histories to LL sheets, a proper zero tube, an LL--Igusa twin pair, Markov
descent, or a new knot invariant.  Those arrows remain dotted/open and cannot be
used as dependencies of the proved P3-L1--P3-L8 nodes.
