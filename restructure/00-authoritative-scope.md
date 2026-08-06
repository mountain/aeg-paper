# Authoritative Scope for the AEG Paper Restructuring

**File:** `restructure/00-authoritative-scope.md`
**Status:** Authoritative
**Version:** 1.1
**Date:** 2026-08-06
**Applies to:** The restructuring of the Arithmetic Expression Geometry paper repository

---

## 1. Purpose

This document fixes the authoritative research and editorial scope of the first four papers in the Arithmetic Expression Geometry (AEG) series.

Its purpose is to prevent scope drift, accidental strengthening of mathematical claims, duplication between papers, and the loss of material during restructuring.

The four papers are provisionally titled:

1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
3. **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
4. **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

The titles may be refined later, but the mathematical division of labor stated here is binding unless this document is explicitly revised.

---

## 2. Authority and conflict resolution

This file is the highest-level repository specification for the scope of the four-paper series.

When sources conflict, use the following order:

1. explicit instructions in the current task;
2. this document;
3. `AGENTS.md`;
4. other authoritative files under `restructure/`;
5. the current Paper I source;
6. research notes, working papers, meeting notes, and archived discussions.

Historical notes and chat transcripts may contain:

* superseded definitions;
* abandoned terminology;
* exploratory analogies;
* intermediate conjectures;
* incomplete proofs;
* claims that were later weakened or rejected.

They must not override the decisions in this document.

Conflicts must not be reconciled silently. Record unresolved conflicts in:

```text
restructure/08-open-questions.md
```

---

## 3. Normative language

The terms **must**, **must not**, **should**, **should not**, and **may** are used normatively.

* **Must** indicates a required part of the paper or restructuring process.
* **Must not** indicates an excluded claim or development.
* **Should** indicates the preferred treatment unless a mathematical reason requires otherwise.
* **May** indicates optional material that does not alter the scope.

---

## 4. Shared conceptual architecture

The first four papers study different layers of one process-to-result hierarchy:

[
\text{expression tree}
\longrightarrow
\text{marked history}
\longrightarrow
\text{operator}
\longrightarrow
\text{geometric or quotient state}
\longrightarrow
\text{endpoint value}.
]

The papers must preserve the distinction between:

* syntax and semantics;
* history and induced operator;
* operator and endpoint value;
* local and global defects;
* affine and projective theories;
* regular and singular geometries;
* analytic structure and topological structure;
* representation complexity and computational cost.

No paper may silently collapse these levels.

The provisional dependency architecture is:

[
\boxed{
\begin{aligned}
\text{Paper I}
&\longrightarrow
\text{Paper II},\
\text{Paper I}
&\longrightarrow
\text{Paper III},\
\text{Paper I}
&\longrightarrow
\text{Paper IV}.
\end{aligned}}
]

Paper II may later provide analytic tools used in Paper III, but Paper III must not depend on unproved analytic claims.

---

# Part I. Paper I

## 5. Paper I title and role

### Provisional title

**Arithmetic Expression Geometry I: Foundations**

Recommended subtitle:

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

### Role

Paper I establishes the foundational mathematical objects and the affine geometric sector of AEG, while locating that sector inside the larger bilateral projective theory.

Its purpose is not to present all known or proposed branches of AEG. Its purpose is to provide stable definitions, proved structural results, and the common language required by Papers II–IV.

The intended logical spine is:

[
\boxed{
\text{sequential syntax}
\longrightarrow
\text{projective semantics}
\supset
\text{affine sector}
\longrightarrow
\text{affine flow}
\longrightarrow
\text{expression geometry}
\longrightarrow
\text{torsion and contact curvature}.
}
]

---

## 6. Paper I central thesis

Paper I should establish the following thesis:

> Sequential arithmetic expressions admit a history-sensitive formalism based on marked spinal trees. Non-degenerate bilateral arithmetic histories possess a projective evaluation whose image generates (PGL_2(K)), while the previously developed continuous AEG theory is the affine or Borel sector stabilizing a point at infinity. This affine sector carries natural cocycles, an infinitesimal flow, a basic hyperbolic realization, global torsion formulas, a contact connection, and a regular zero-set theory.

This thesis must be stated with the appropriate field, positivity, regularity, and non-degeneracy assumptions.

Paper I must not describe the affine sector as the whole of projective AEG.

---

## 7. Required content of Paper I

Paper I must include the following components.

### 7.1 Sequential trees and marked spinal histories

Paper I must define sequential arithmetic histories intrinsically.

It must include:

* arithmetic expression trees;
* the dependency partial order on internal nodes;
* uniqueness of evaluation order;
* the classification of sequential trees by a single internal spine;
* a marked accumulator or seed;
* operand-slot labels;
* marked one-hole contexts
  [
  C_{\omega,c}^{(1)}[z]=\omega(z,c),
  \qquad
  C_{\omega,c}^{(2)}[z]=\omega(c,z);
  ]
* chirality words;
* bounded and free histories;
* composition of histories.

The existing informal definition of a threadlike expression must be replaced or repaired so that it is consistent with the tree orientation and examples.

The paper must distinguish:

* planar mirror;
* operand-slot exchange;
* temporal reversal;
* path inverse;
* syntactic equality;
* history equality;
* operator equality;
* endpoint equality.

Mirror must not be identified with reversal.

---

### 7.2 Projective semantics of bilateral arithmetic

Paper I must introduce the projective semantics of non-degenerate bilateral one-hole arithmetic contexts.

It must include:

* the action on (\mathbb P^1(K));
* projective matrix representatives;
* explicit domain qualifications for division;
* the distinction between ordinary arithmetic evaluation and projective continuation;
* the evaluation map
  [
  \rho:\operatorname{Hist}^{\pm,\times}_K
  \longrightarrow PGL_2(K);
  ]
* the theorem that translations, nonzero scalings, and inversion generate (PGL_2(K));
* the identification
  [
  B_\infty
  ========

  \operatorname{Stab}_{PGL_2(K)}(\infty)
  \cong \operatorname{Aff}(1,K);
  ]
* the qualification that the current real exponential parameterization covers the positive affine component rather than every real affine map.

This section must remain concise. It provides the global algebraic placement of the affine theory; it does not develop the full projective quotient or bivaluation theory.

---

### 7.3 Affine cocycles

Paper I must derive the affine composition formulas.

For affine maps

[
f_i(x)=s_i x+t_i,
\qquad
s_i\neq0,
]

the paper should establish:

[
\Phi_n=\prod_{i=1}^n s_i,
]

[
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j,
]

and

[
\widehat\xi_n
=============

# \frac{\xi_n}{\Phi_n}

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

The two translation coordinates must be interpreted as different natural cocycles:

* future-scaled or target-frame translation;
* past-normalized or source-frame translation.

The paper must state clearly which multiplication and matrix conventions are being used.

---

### 7.4 Continuous affine flow

Paper I must derive the continuous affine flow from the affine group or its Lie algebra.

The core equation is:

[
\frac{da}{ds}
=============

\mu\cos\theta
+
\lambda a\sin\theta.
]

Equivalent forms may include:

[
da=\mu,du+\lambda a,dv,
]

and, after specifying a compatible metric,

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2.
]

The derivation must distinguish:

* left and right multiplication;
* source and target frames;
* (g^{-1}dg) and (dg,g^{-1});
* operand-slot chirality and temporal insertion side.

Paper I must state that the affine flow is the (\kappa=0) slice of the projective Riccati flow

[
\dot z=\beta+\alpha z+\kappa z^2.
]

The full Riccati geometry is not developed in Paper I.

---

### 7.5 Arithmetic expression spaces

Paper I must provide a precise definition of a regular arithmetic expression space.

At minimum, a regular AES must specify:

* a smooth manifold or surface (M);
* a metric (g);
* an assignment function (a);
* generator parameters (\mu,\lambda);
* the domain on which the flow or eikonal equation holds.

The definition must distinguish data that are intrinsic from data that depend on coordinates or normalization.

---

### 7.6 The basic hyperbolic model

Paper I must construct the basic affine/hyperbolic model, provisionally denoted (\mathfrak E_0).

The model should include:

[
g_{\mu,\lambda}
===============

\frac{1}{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
\qquad
a(x,y)=-\frac{x}{y}.
]

The paper must prove that the assignment satisfies the required flow or eikonal equation.

It may include:

* the hyperbolic interpretation;
* horocyclic and geodesic coordinates;
* addition and multiplication actions;
* the relation with the affine group;
* the Baumslag–Solitar-type grid relation;
* the Laplace eigenfunction calculation;
* local torsion-area formulas.

The preferred derivation is from the affine group and a normalized invariant metric, rather than presenting the model as an isolated inspired example.

Paper I must not claim a global or conformal uniqueness theorem unless such a theorem is fully proved.

---

### 7.7 Regular zero loci

Paper I must establish the basic regularity theorem for zero sets.

If a smooth AES satisfies

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

with (\mu\neq0), then on (a^{-1}(0)),

[
|\nabla a|=|\mu|>0.
]

The paper must conclude that zero is a regular value and that the zero set is a smooth codimension-one submanifold.

For a two-dimensional AES, this implies that regular zero sets are unions of disjoint smooth curves.

The paper must record the consequences:

* no isolated regular zero point;
* no regular zero-line crossing;
* no regular branching or merging;
* no regular birth or death of zero components in the interior.

Any example violating these conclusions must be classified as singular, degenerate, boundary-induced, non-proper, or outside the hypotheses.

---

### 7.8 Singular arithmetic expression spaces

Paper I must introduce a foundational definition of a singular AES.

A singular AES may be represented by data such as

[
(M,S,g,a;\mu,\lambda),
]

where (S\subset M) is a closed singular set and the regular AES equations hold on (M\setminus S).

The definition must allow singularity in one or more of:

* the assignment function;
* the metric;
* the parameters;
* the coordinate chart;
* the projective continuation;
* the domain of ordinary arithmetic evaluation.

The paper must distinguish:

[
Z_{\mathrm{reg}}(a)
\qquad\text{and}\qquad
Z_{\mathrm{sing}}(a).
]

The isolated-zero model currently denoted (\mathfrak E_1) may remain in Paper I only if it is explicitly treated as a singular model and its regularity status is stated accurately.

---

### 7.9 Minimal multi-zero content

Paper I should contain one minimal multi-zero example only if it is completely verified.

A multi-zero example is acceptable only if the paper specifies and verifies:

1. the domain;
2. the metric;
3. the assignment function;
4. the regular and singular sets;
5. the flow equation on the regular domain;
6. the topology and number of zero components.

General (E_k), (E_{\log}), or multi-zero classification does not belong to Paper I.

If no example currently satisfies these verification requirements, Paper I must state the problem and defer the construction to Paper III.

---

### 7.10 Parametric zero-set lemma

Paper I may include the foundational parameter-family construction.

For a smooth family

[
a_t:M\to\mathbb R,
]

define

[
A:M\times I\to\mathbb R,
\qquad
A(p,t)=a_t(p),
]

and the total zero set

[
\mathcal Z=A^{-1}(0).
]

Under a non-degeneracy condition ensuring that (d_p a_t\neq0) on the zero set, Paper I may prove that (\mathcal Z) is a smooth codimension-one submanifold of (M\times I).

Paper I may call this a basic regular zero-surface or preliminary tube result.

Paper I must not infer global triviality, isotopy invariance, compactness, or topology preservation without properness or equivalent hypotheses.

The full tube theory belongs to Paper III.

---

### 7.11 Global torsion and the ACS

Paper I must retain the Accumulative Commutative Space as the commutative charge shadow of affine histories.

The preferred formulation compares two histories (\gamma) and (\delta) with compatible total charge or common linear part.

The relative torsion or endpoint defect should be defined as

[
\tau(\gamma,\delta)
===================

\nu_x(\gamma)-\nu_x(\delta),
]

with explicit conditions under which it is independent of (x).

The paper should derive:

* an affine cocycle evaluation formula;
* a boundary integral representation;
* a weighted area representation;
* the associated Stokes identity.

Comparison with temporal reversal may remain as an important special case but must not be the only general definition.

The ACS must not be described as the full expression space. It records abelianized charge data and is therefore a quotient or shadow of the history calculus.

---

### 7.12 Contact connection and horizontal differential

Paper I must construct the local contact or connection model:

[
\alpha
======

da-(\mu,du+\lambda a,dv),
]

with horizontal fields

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a.
]

It must establish:

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

The paper may define the horizontal covariant differential

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
]

It must state that this operator is curvature-sensitive and generally not nilpotent:

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

The central local-global comparison should connect:

[
\text{finite affine defect},
\qquad
\text{ACS weighted area},
\qquad
\text{contact curvature}.
]

Elementary differentiation tables and extensive calculational bases should be placed in appendices or Paper II unless they are needed for a central theorem.

---

## 8. Required theorem-level results in Paper I

Paper I should not be considered complete unless it contains rigorous versions of the following results or explicitly records why one remains pending:

1. sequential-tree classification;
2. projective evaluation of bilateral contexts;
3. generation of (PGL_2(K));
4. identification of the affine/Borel sector;
5. affine cocycle formulas;
6. derivation of the continuous affine flow;
7. construction and verification of the basic hyperbolic model;
8. generalized torsion or cocycle-Stokes identity;
9. contact curvature identity;
10. regular zero-locus theorem;
11. foundational singular-AES definition;
12. basic regular parameter-family zero-surface lemma, if retained.

The authoritative mathematical status of each result will be recorded separately in:

```text
restructure/05-mathematical-status.md
```

---

## 9. Material excluded from Paper I

Paper I must not develop the following as main theories.

### 9.1 Full projective condensation theory

Exclude:

* regular bivaluations as the main object;
* rank-one idempotent classification as a main theorem sequence;
* the full homogeneous-space tower
  [
  G/H,\qquad G/B_\pm;
  ]
* principal (H)-bundles;
* concept–predicate semantics;
* projective process residue;
* projective holonomy beyond a short outlook.

These belong to Paper IV.

### 9.2 Full analytic function theory

Exclude:

* a full arithmetic holomorphic theory;
* Poisson kernels;
* Green functions;
* maximum principles;
* Harnack inequalities;
* Dirichlet or Neumann theories;
* spectral decompositions;
* global continuation theorems.

These belong to Paper II.

### 9.3 Full singular and tube theory

Exclude:

* general (E_k) classifications;
* complete (E_{\log}) theory;
* discriminant stratification;
* local bifurcation classification;
* zero-line birth, death, cusp, and reconnection theory;
* global tube topology;
* threading;
* braid monodromy;
* knot invariants;
* Markov normalization.

These belong to Paper III.

### 9.4 Computational complexity claims

Exclude:

* claims that noncommutativity alone implies negative curvature;
* claims that negative curvature alone implies exponential algorithmic complexity;
* claims that AEG proves complexity lower bounds;
* general equivalence of representation, time, and space complexity;
* complexity conclusions from diagrams or analogy alone.

These belong to Paper IV and require explicit state spaces, metrics, quotient maps, and cost models.

---

# Part II. Paper II

## 10. Paper II title and role

### Provisional title

**Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**

Recommended subtitle:

**Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity**

### Role

Paper II develops the analytic theory of the regular affine/hyperbolic spaces established in Paper I.

It must answer:

> What genuine real and complex function theory is supported by the metric, connection, and horizontal operators of AEG?

Paper II must begin from explicitly chosen analytic data. It must not claim that a contact form alone uniquely determines the full analytic structure.

---

## 11. Required scope of Paper II

Paper II should include:

* compatible horizontal metrics;
* orientation and almost-complex structure;
* first- and second-order horizontal operators;
* natural measures and energy forms;
* formal adjoints and domains;
* comparison with the hyperbolic Laplacian;
* analysis on (\mathfrak E_0);
* explicit solution families;
* boundary-value problems;
* harmonic or twisted harmonic theory;
* arithmetic Cauchy–Riemann equations;
* factorization identities;
* the relation to classical complex analysis and hyperbolic harmonic analysis.

At least one nontrivial boundary, kernel, spectral, or continuation result must be proved.

At least one genuinely (a)-dependent solution family must be constructed.

---

## 12. Exclusions from Paper II

Paper II must not become:

* a general introduction to contact analysis unrelated to arithmetic meaning;
* the primary location for multi-zero topology;
* the primary location for tube or knot theory;
* a computational-complexity paper;
* a place for unproved claims that AEG replaces classical complex analysis.

Nodal-set results may appear when analytically relevant, but global singular-zero classification belongs to Paper III.

---

# Part III. Paper III

## 13. Paper III title and role

### Provisional title

**Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**

Recommended subtitle:

**Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport**

### Role

Paper III develops the geometry and topology of singular assignment functions, multiple zero components, parameter families, and total zero sets.

It must answer:

> How do zero sets change when regularity or non-degeneracy fails, and how do parameterized zero sets form tubes, monodromy, braids, or knot-like structures?

---

## 14. Required scope of Paper III

Paper III should include:

* a full singular-AES category or stratified framework;
* local singular zero-set models;
* regular versus singular zero components;
* verified multi-zero constructions;
* the (E_k) program, if made rigorous;
* the (E_{\log}) construction, if made rigorous;
* parameter spaces;
* discriminant sets such as
  [
  \mathcal D
  ==========

  {t:\exists p,\ a_t(p)=0,\ d_pa_t=0};
  ]
* stability away from the discriminant;
* regular tube theorems;
* properness and local triviality;
* singular fibers;
* monodromy of zero components;
* braid representations when justified;
* threading constructions.

Every explicit model must specify:

1. its domain;
2. its metric;
3. its assignment function;
4. its singular set;
5. the equation satisfied on the regular locus;
6. the topology of the zero set;
7. the parameter range;
8. the status of all claimed invariants.

---

## 15. Conditional scope for knot theory

Knot and braid material may enter Paper III only under strict conditions.

A knot-theoretic construction may be presented as a main result only if at least one of the following is proved:

* isotopy invariance;
* invariance under the required braid or Markov moves;
* a well-defined monodromy representation;
* a nontrivial invariant not determined by an already known lower-level representation;
* a precise comparison with Alexander, Burau, or another established invariant.

Otherwise, knot material must remain:

* an example;
* a structural proposal;
* a conjecture;
* an open problem.

Visual resemblance to a knot is not sufficient.

---

## 16. Exclusions from Paper III

Paper III must not claim:

* that every multi-zero family yields a knot;
* that a tube is globally trivial without properness;
* that topology changes without a singular or non-proper event;
* that a proposed invariant survives Markov normalization without proof;
* that a numerical example establishes a general classification.

Computational complexity belongs to Paper IV.

---

# Part IV. Paper IV

## 17. Paper IV title and role

### Provisional title

**Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

Recommended subtitle:

**From Histories and Quotients to Representation and Cost**

### Role

Paper IV develops the complete process-to-result quotient architecture and investigates how historical, operator, geometric, and semantic compression relate to representation and computational complexity.

It must answer:

> What information is lost when histories are condensed into operators, quotient states, canonical forms, or endpoint values, and under what precise conditions can this loss be related to computational resources?

---

## 18. Required scope of Paper IV

Paper IV should include:

* the full history category or groupoid;
* projective evaluation;
* group-valued relative defects;
* bivaluations;
* point–predicate duality;
* rank-one idempotents;
* the homogeneous-space tower
  [
  G\to G/H\to G/B_\pm;
  ]
* principal-bundle interpretations;
* projective condensation;
* quotient fibers;
* canonical forms;
* rewriting and normalization;
* syntactic, word, representation, geometric, time, and space complexity;
* growth of word balls;
* polynomial versus exponential growth;
* quasi-isometric comparisons where provable;
* resource or pebble-game models;
* time–space tradeoffs;
* explicit algorithmic case studies.

The paper must state a cost model before making a complexity claim.

Every complexity result must specify:

* the state space;
* the generating set;
* the equivalence or quotient;
* the metric;
* the encoding;
* the computational model;
* the resource being measured.

---

## 19. Exclusions from Paper IV

Paper IV must not assert without proof:

[
\text{noncommutativity}
\Rightarrow
\text{hyperbolicity},
]

[
\text{hyperbolicity}
\Rightarrow
\text{exponential time},
]

or

[
\text{expression growth}
\Rightarrow
\text{NP-hardness}.
]

These implications require additional hypotheses and generally do not hold as unconditional statements.

Paper IV must distinguish:

* group growth;
* representation-space growth;
* search-tree growth;
* algorithm running time;
* memory usage;
* lower-bound complexity.

Analogies to thermodynamics, spacetime, mass, or curvature may motivate definitions but may not replace them.

---

# Part V. Cross-paper allocation

## 20. Authoritative concept allocation

| Concept                        | Paper I                      | Paper II                    | Paper III                    | Paper IV                           |
| ------------------------------ | ---------------------------- | --------------------------- | ---------------------------- | ---------------------------------- |
| Expression trees               | foundational                 | inherited                   | inherited                    | inherited                          |
| Sequential-tree classification | main result                  | cited                       | cited                        | cited                              |
| Marked spinal histories        | main object                  | inherited                   | inherited                    | main history input                 |
| Bilateral (PGL_2) generation   | concise main theorem         | cited                       | cited                        | fully developed                    |
| Affine/Borel sector            | main setting                 | analytic setting            | local setting                | compared with projective sector    |
| Riccati completion             | brief placement              | possible analytic extension | possible singular dynamics   | full projective context            |
| Affine cocycles                | main result                  | analytic input              | transport input              | complexity/condensation input      |
| Affine flow                    | main result                  | main analytic background    | local family equation        | geometric cost model               |
| Basic hyperbolic model         | main example                 | primary analytic background | regular comparison model     | metric example                     |
| ACS                            | main global charge shadow    | optional analytic use       | possible invariant source    | quotient/condensation example      |
| Torsion                        | main local-global invariant  | operator coupling           | tube or singular invariant   | relative process defect            |
| Contact connection             | main result                  | operator foundation         | tube geometry input          | holonomy input                     |
| Horizontal complex structure   | excluded as main theory      | main analytic choice        | optional tool                | not primary                        |
| Arithmetic holomorphicity      | excluded from main body      | main theory                 | optional construction tool   | not primary                        |
| Regular zero-locus theorem     | main theorem                 | nodal input                 | foundational input           | not primary                        |
| Singular AES                   | foundational definition      | local analytic use          | main theory                  | possible singular quotient example |
| Multi-zero models              | at most one verified example | optional analytic examples  | main theory                  | not primary                        |
| Parameter zero surface         | basic lemma                  | optional                    | main tube theory             | not primary                        |
| Tube topology                  | excluded beyond basic lemma  | not primary                 | main theory                  | possible state-space example       |
| Braid and knot structures      | excluded                     | excluded                    | conditional main theory      | not primary                        |
| Bivaluation/projector theory   | excluded                     | optional outlook            | optional representation tool | main theory                        |
| Condensation                   | brief outlook only           | not primary                 | geometric examples possible  | main theory                        |
| Computational complexity       | excluded as conclusion       | excluded                    | excluded                     | main theory                        |

This table is authoritative unless this document is revised.

---

# Part VI. Migration rules

## 21. Rules for moving current material

The current repository contains material belonging to several future papers.

During restructuring:

* material must be moved, not silently deleted;
* one canonical destination must be chosen;
* Paper I may retain only the minimum statement needed for continuity;
* full duplicate theories must not remain in multiple papers;
* labels and citations must be updated;
* relocated material must be logged.

Expected migrations include:

* arithmetic holomorphicity and associated operator calculations to Paper II;
* multi-zero constructions, (E_k), (E_{\log}), singular families, and tube material to Paper III;
* bivaluations, projector theory, quotient towers, projective condensation, and complexity material to Paper IV.

The exact file-level mapping will be maintained in:

```text
restructure/04-current-to-target-map.md
```

---

## 22. Treatment of appendices

Paper I appendices may contain:

* coordinate computations;
* detailed affine cocycle derivations;
* extended ACS examples;
* contact-form calculations;
* proof details for the basic hyperbolic model;
* regular zero-set calculations;
* supplementary examples separating notions of equality or neutrality.

Appendices must not be used to hide a second paper inside Paper I.

If an appendix develops an independent theory, it must be moved to the appropriate later paper.

---

# Part VII. Mathematical claim discipline

## 23. Required claim statuses

Every substantial claim considered during restructuring must be assigned one of:

* `proved`;
* `proved with stated hypotheses`;
* `standard consequence requiring an in-paper proof`;
* `computationally verified example`;
* `partially proved`;
* `structural proposal`;
* `conjecture`;
* `open problem`;
* `unsupported and excluded`.

The current status of each result must be maintained in:

```text
restructure/05-mathematical-status.md
```

No restructuring task may silently promote a claim to a stronger status.

---

## 24. Explicitly prohibited inferences

The following inferences are not authorized without independent proofs:

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
\text{knot structure};
]

[
\text{tube picture}
\Rightarrow
\text{isotopy invariant};
]

[
\text{symmetry of a model}
\Rightarrow
\text{uniqueness};
]

[
\text{projective continuation}
\Rightarrow
\text{ordinary arithmetic regularity};
]

[
\text{contact distribution}
\Rightarrow
\text{unique complex structure};
]

[
\text{numerical experiment}
\Rightarrow
\text{general theorem}.
]

When one of these ideas is discussed, it must be labeled as a proposal, conjecture, or open program unless a proof is present.

---

# Part VIII. Completion criteria

## 25. Paper I completion criteria

Paper I is ready for mathematical review only when:

1. the foundational objects are defined consistently;
2. the sequential-tree theorem is proved;
3. projective bilateral semantics is stated with domain qualifications;
4. (PGL_2) generation is proved;
5. the affine/Borel sector is identified precisely;
6. cocycle formulas are proved;
7. the affine flow is derived with explicit conventions;
8. the basic hyperbolic model is verified;
9. the regular zero-locus theorem is proved;
10. singular AES is defined;
11. the ACS torsion theorem is presented in a general two-history form or its restriction is explicitly justified;
12. contact curvature is proved;
13. analytic, tube, projective-condensation, and complexity material has been migrated or reduced to disciplined outlook statements;
14. the PDF builds without unresolved references or missing citations;
15. the abstract and conclusion make no claim stronger than the body proves.

---

## 26. Papers II–IV planning criteria

Papers II–IV may initially exist as structured outlines or partial drafts.

They must not be treated as established papers merely because material has been migrated into them.

Each must contain:

* a declared scope;
* a theorem dependency list;
* a mathematical-status table;
* a separation between proved results and research program;
* explicit completion criteria.

---

# Part IX. Change control

## 27. Revising this scope

This document may be revised only by an explicit scope-change task.

A revision must state:

1. the previous rule;
2. the proposed new rule;
3. the mathematical reason;
4. the papers affected;
5. the required migration;
6. the effect on theorem dependencies;
7. the effect on current drafts.

Routine editing must not alter the four-paper architecture implicitly.

---

## 28. Default decision under uncertainty

When it is unclear whether material belongs in Paper I or a later paper, use the following test.

Material belongs in Paper I only if it is required to define or prove one of:

* the sequential history formalism;
* projective placement of the affine sector;
* affine cocycles;
* affine flow;
* the basic regular AES;
* the basic hyperbolic model;
* regular zero-set theory;
* foundational singular-AES terminology;
* global affine torsion;
* contact connection and curvature.

Material that develops analysis, singular classification, tube topology, projective quotients, condensation, or complexity belongs in Papers II–IV.

When uncertainty remains:

* preserve the material;
* move it to the most plausible later-paper draft;
* leave a short forward reference in Paper I;
* record the question in `restructure/08-open-questions.md`.

---

## 29. Final scope summary

The four-paper series is fixed as follows:

[
\boxed{
\begin{array}{ll}
\textbf{Paper I:} &
\text{objects, histories, affine/projective placement, flow,}\
&
\text{basic space, torsion, contact curvature, and zero-set boundary};[2mm]

\textbf{Paper II:} &
\text{horizontal and hyperbolic real analysis, boundary theory,}\
&
\text{and arithmetic holomorphicity};[2mm]

\textbf{Paper III:} &
\text{singular assignment functions, multi-zero geometry,}\
&
\text{discriminants, tubes, monodromy, and conditional knot theory};[2mm]

\textbf{Paper IV:} &
\text{full projective condensation, quotient structures,}\
&
\text{representation growth, and computational cost}.
\end{array}}
]

Paper I must remain foundational and restrained. Its success is measured not by how many AEG directions it mentions, but by whether Papers II–IV can depend on it without redefining its objects, repairing its conventions, or weakening its claims.

---

## 30. Arithmetic--automorphic zero-network amendment

The following cross-paper interface is authorized as of 2026-08-06:

[
\text{restricted arithmetic histories}
\longrightarrow G_4
\longrightarrow \text{regular holomorphic pullback}
\longrightarrow \text{singular automorphic zero network}.
]

Its ownership is fixed as follows.

### Paper I

Paper I may prove that the projective contexts

[
T_{\sqrt2}(z)=z+\sqrt2,
\qquad
J(z)=-1/z
]

generate the (q=4) Hecke triangle subgroup of
(\operatorname{PGL}_2(\mathbb Q(\sqrt2))).  This is an operator-level example
of the process-to-operator quotient.  Paper I must retain the distinctions among
literal histories, marked histories, projective operators, Hecke group elements,
stabilizer cosets, and ordinary admissible endpoints.  It must not develop
Hauptmoduls, dessins, or singular zero networks as Paper I theory.

Paper I also owns the complete regular splitting theorem: on a connected,
complete, boundaryless regular AES with (\mu\ne0), the rectified assignment has
unit gradient and its complete flow gives

[
M\cong Z(a)\times\mathbb R.
]

The conclusion is a smooth, not necessarily Riemannian, product.  It implies that
the zero layer is nonempty and connected under these hypotheses and supplies the
global no-go boundary motivating the singular automorphic model.

### Paper II

Paper II owns the regular analytic pullback interface.  It may prove the planar and
cylindrical target AES formulas and their preservation under holomorphic local
diffeomorphisms.  It must state that critical points, degenerate pullback metrics,
cone completions, and branching zero sets lie outside the regular locus and are
treated in Paper III.

### Paper III

Paper III owns:

* holomorphic branched-pullback singularities;
* the (2m)-prong and (2\pi m)-cone local theorem;
* the normalized ((2,4,\infty)) Hecke--Hauptmodul zero-network model;
* sign-equivariant assignments and their line-bundle or index-two descent;
* arithmetic relative zero divisors, their normalizations, discriminants, and
  geometric monodromy;
* the proposed history-to-relative-divisor functor.

The last item remains a structural proposal until a functor respecting declared
history equivalence, composition, field of definition, and parameter base is
constructed.  The automorphic model must not be advertised as such a functor for
all AEG histories.

### Claim boundary

This amendment does not authorize any claim that:

* all histories are in bijection with tiles or zero branches;
* an arbitrary complex zero network is number-theoretic;
* projective equality implies ordinary arithmetic admissibility;
* the (q=4) model supplies nonunique factorization in
  (\mathbb Z[\sqrt2]);
* a singular zero network automatically gives a proper tube, finite braid, or knot
  invariant.

The detailed proof and status ledger is maintained in
`restructure/discussions/arithmetic-automorphic-zero-networks.md` and the
mathematical-status register.

---

## 31. Sign-cover knots and finite-register naturality amendment

The following two downstream extensions are authorized as of 2026-08-06.

### The q=4 operator-to-knot interface

Paper III may pass from the (q=4) Hecke operator quotient to the hyperbolic unit
tangent bundle.  For a marked history whose projective operator is primitive
hyperbolic, it may define the associated oriented geodesic-flow periodic orbit.
The map is allowed to factor through projective conjugacy, and its resulting
collapse of raw and marked histories must be stated explicitly.

The same Paper III model may identify the sign-character cover, using the
declared cusp compactification and a printed peripheral-slope calculation, as

[
T^1(\ker\chi\backslash\mathbb H)\cong S^3\setminus T(2,4).
]

The zero dessin may be used as the one-dimensional coding spine for the cited
geodesic template.  It must not be called the three-dimensional template, a zero
tube, or a knot.  The classical geodesic coding, template isotopy, lens-space
compactification, and cusp-linking formula must be cited as external inputs.

### The supplied-register divisor interface

Paper III may construct finite relative endpoint divisors from explicitly supplied
typed algebraic registers, including (u^2=t) and the tower
(v^2=3), (u^2=t+v).  It may prove equivariance, arithmetic and geometric
irreducibility, discriminant, monodromy, inertia, and Frobenius statements for
these declared families.  It may also retain a time-tagged prefix trace and an
ordinary pole divisor as computation-graph decorations.

This amendment does not convert those supplied registers into outputs of the
Paper I four-context grammar.  A terminal endpoint divisor that factors through
projective evaluation is not history-faithful.  The general history-to-relative-
prime-divisor functor remains open until the register source, history equivalence,
composition, and descent of non-tautological trace data are constructed.

### Additional claim boundary

This amendment does not authorize a claim that:

* the local four-pronged metric germ has link (T(2,4));
* the flat coarse cylinder and the hyperbolic orbifold unit tangent bundle are the
  same geometric carrier;
* primitive Hecke elements correspond to prime knots;
* the history-to-periodic-orbit map is injective;
* the cited Hecke linking formula or template is a new AEG knot invariant;
* the quadratic or quartic register is canonically generated by every arithmetic
  history;
* a tagged trace is automatically invariant under expression equivalence, ambient
  isotopy, or Markov moves.

---

## 32. Polynomial relations across slices and horizontal kernel residue

Paper III may use a supplied polynomial family (P(z,t)) in two compatible
ways: the real equation (operatorname{Im}P=0) defines a zero carrier, and the
complex equation (P=0) defines a finite root thread contained in that carrier.
This interface is authorized only when total smoothness, boundary neatness,
fiberwise singular strata, root square-freeness, and properness are checked
separately.

For (P_m(z,t)=z^2-t^m), (tin S^1), (mge 1), and a disc of radius
(R>1), Paper III may prove:

* the carrier is a compact connected smooth neat incidence with four boundary
  components, (2m) Morse saddles, Euler characteristic (-2m), and genus
  (m-1);
* its slice metrics are singular AES metrics with a declared essential center and
  (4pi) cone completion;
* the root thread is the closed braid (sigma_1^m) with closure (T(2,m));
* arithmetic prime components, thread components, and link components are counted
  by (gcd(2,m));
* discriminant order, logarithmic period, braid exponent, negative half Euler
  characteristic, and the carrier-framing period agree with the printed sign
  conventions.

The carrier projection is not a proper zero tube because of its saddles.  The
braid exponent and carrier framing are presentation- or trivialization-level data,
not Markov invariants.

For (m=4), the lifted q=4 cusp slopes and deck action may be used to derive the
peripheral toric divisor (u^2=t^4), up to the ordered meridian marking, Laurent
units, orientation, and character gauge.  Extending that torus divisor radially
to the genus-three carrier is additional supplied data.  The ordinary pure-braid
extension is not identified with the q=4 unit-tangent central extension or with
Paper I's affine torsion.

With the normalized Hauptmodul, residual orbifold marking, deck involution, and
two cusp points retained, Paper III may strengthen the peripheral statement over
the complex numbers.  The compactified sign cover is the marked weighted pair
(mathbb P(2,1),V(U^2-V^4)); its logarithmic tangent is (mathcal O(-1)), its
graded section ring is generated in weights one and two, and the cusp section is
the degree-four binomial.  The weighted Hopf circle bundle gives the standard
cusp filling and the (T(2,4)) link.  This is a graded-isomorphism statement, not a
coordinate-free equality in a pre-existing affine plane.  Over
(mathbb Q(sqrt2)), the split minus form and the nonsplit plus form are constant
quadratic twists; neither arithmetic descent may be called canonical until its
marking is declared.  The log-cone coordinate is not automatically the external
slice parameter of the radial carrier.

Paper III may also record a four-strand central-extension calibration.  For the
supplied Garside half-twist and four-point rotation paths, the two q=4 elliptic
relators have the same full-twist residue, and the pullback of the (B_4) center
extension agrees with the unit-tangent central extension after the printed
orientation convention.  The resulting conjugation-invariant integer character
on the free-word operator kernel has, in the Lyndon--Hochschild--Serre five-term
sequence, pushout class equal to the unit-tangent Euler extension class.  This is
a genuine group-extension transgression, not a Serre transgression over the
circle base, and the character is not Paper I's affine torsion.  This does not
prove that those coefficient paths arise
from unrestricted marked histories, does not require an injectivity claim, and
does not identify the inverse full-twist closure (T(4,-4)) with the q=4 cusp link
(T(2,4)).

The correct information-loss statement is the exact sequence

[
1\longrightarrow P_2\longrightarrow B_2\longrightarrow S_2\longrightarrow1.
]

At (m=4), permutation monodromy is trivial while the pure-braid coordinate and
mutual linking number are two.  A future history-to-path functor must act on full
marked coefficient paths and pass the neutral-word test; attaching this residual
after terminal projective evaluation is not authorized as a naturality theorem.

---

## 33. Bounded sextic Lyashko--Looijenga laboratory

Migration M-0008 authorizes one bounded Paper III laboratory based on the supplied
monic centered sextic

[
P_0(x)=x^6-x.
]

Paper III may directly compute its critical-value polynomial, prove that the five
displayed local half-twists form a spanning star generating (B_6), and construct
the compatible real carrier, six-root thread, and genus-two branched-cover mapping
torus for collision-free loops.  It may also prove the mixed critical-value/test-
parameter exact-sequence model and specialize cited arithmetic criteria to the
fiber (y^2=x^6-x-1).

The following remain cited classical inputs rather than new AEG theorems:

* finiteness and etaleness of the regular Lyashko--Looijenga map and its degree;
* the caustic and Maxwell multiplicities;
* transposition-factorization counts and local Picard--Lefschetz monodromy;
* Birman--Hilden lifting and genus-two symplectic monodromy;
* the irreducibility, Galois-group, and hyperelliptic-endomorphism criteria used
  for the displayed arithmetic fiber.

The count (6^4=1296) refers to normalized monic-centered LL sheets.  The free
residual (\mu_6) source rotations give (216) orbits.  Neither number is authorized
as a count of pairwise nonisomorphic genus-two curves.

The two braid layers must remain typed.  Critical-value transport acts through the
LL cover, while motion of the test parameter supplies a vertical (F_5) and then a
six-root braid.  Their interface is the pullback of

[
1\longrightarrow F_5\longrightarrow B_{5,1}\longrightarrow B_5
\longrightarrow1
]

along the LL cover, or the equivalent Hurwitz groupoid.  Forgetting the LL sheet
does not authorize a homomorphism (B_5\to B_6).

The sextic carrier may have saddle walls and is not thereby a proper zero tube.
Carrier-wall crossings, root collisions, critical-value collisions, and singular
hyperelliptic fibers must not be identified.  Likewise, the common abstract target
(\operatorname{Sp}_4(\mathbb F_2)\cong S_6) does not canonically identify an
arithmetic Frobenius element with a topological loop.

The following remain open:

* the LL--Igusa twin test for distinct genus-two moduli points in one LL fiber;
* any functor from unrestricted AEG histories to a canonical sextic, LL sheet,
  mixed-braid path, or six-root braid;
* a proper-zero-tube theorem for this singular carrier;
* Markov descent or a new knot invariant extracted from the laboratory.

Thus P3-L1--P3-L8 are authorized only with their supplied/calculated versus
classical-input statuses displayed, while P3-L9 and the general history
naturality arrows remain open.
