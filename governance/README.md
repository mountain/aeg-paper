# Arithmetic Expression Geometry

Arithmetic Expression Geometry (AEG) studies arithmetic expressions through their **ordered evaluation histories**, rather than treating an expression as exhausted by its final numerical value.

The central hierarchy is:

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

Each arrow forgets information. AEG investigates the algebraic, geometric, analytic, topological, and computational structures carried by the levels before final evaluation.

---

## Repository status

> **The controlled restructuring has produced four canonical mathematical-review
> manuscripts. All four remain editorial and publication drafts.**

The current source contains material developed at different stages of the research program. Some notes are proved mathematics; others are exploratory constructions, structural proposals, conjectures, superseded formulations, or open problems.

Do not treat every file as equally authoritative.

The governing specifications are:

* [`AGENTS.md`](../AGENTS.md)
* [`governance/00-authoritative-scope.md`](00-authoritative-scope.md)
* [`governance/01-paper-series-architecture.md`](01-paper-series-architecture.md)
* [`governance/02-paper-I-outline.md`](02-paper-I-outline.md)
* [`governance/03-theorem-dependency-graph.md`](03-theorem-dependency-graph.md)
* [`governance/04-current-to-target-map.md`](04-current-to-target-map.md)
* [`governance/05-mathematical-status.md`](05-mathematical-status.md)
* [`governance/06-editorial-rules.md`](06-editorial-rules.md)
* [`governance/07-acceptance-checklist.md`](07-acceptance-checklist.md)
* [`governance/08-open-questions.md`](08-open-questions.md)

When repository sources conflict, these documents determine the current scope, terminology, claim status, and migration policy.

The completed mathematical-review integrations are documented in:

* [`paper-I-closure-report.md`](paper-I-closure-report.md)
* [`paper-II-closure-report.md`](paper-II-closure-report.md)
* [`paper-III-closure-report.md`](paper-III-closure-report.md)
* [`paper-IV-closure-report.md`](paper-IV-closure-report.md)

Paper III's corrected historical provenance and theorem decisions are recorded in
[`paper-III-source-audit.md`](paper-III-source-audit.md) and
[`decisions-paper-III.md`](decisions-paper-III.md).
Paper IV's corresponding records are
[`paper-IV-source-audit.md`](paper-IV-source-audit.md),
[`decisions-paper-IV.md`](decisions-paper-IV.md), and
[`paper-IV-red-team-report.md`](paper-IV-red-team-report.md).

The post-closure arithmetic--automorphic integration across Papers I--III is
documented in
[`discussions/arithmetic-automorphic-zero-networks.md`](discussions/arithmetic-automorphic-zero-networks.md).
Its proved components are promoted only through the authoritative scope,
dependency, status, and per-paper decision records; the general history-to-divisor
functor remains an open problem.

The inventory and readiness grading of the research notes, together with the
conflict and correction ledger, are recorded in
[`notes-reserve-audit.md`](notes-reserve-audit.md).  Its new open items are
registered as OQ-078--OQ-080 in
[`08-open-questions.md`](08-open-questions.md).

---

# The AEG paper series

The first phase of the program is organized into four papers.

| Paper | Current manuscript title                                                                    | Primary question                                                                                                   |
| ----- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| I     | **Arithmetic Expression Geometry I: Foundations**                                           | How do sequential arithmetic histories acquire affine and geometric structure?                                     |
| II    | **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**                      | What analytic and function-theoretic structures exist on regular AEG spaces?                                       |
| III   | **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**                    | How do multiple zeros, singularities, parameter families, and tube topology arise?                                 |
| IV    | **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity** | What information is lost under quotient and condensation, and how is it related to representation and computation? |

The dependency architecture is:

```text
Paper I ──→ Paper II
Paper I ──→ Paper III
Paper I ──→ Paper IV
Paper II ──→ Paper III  [bounded holomorphic-pullback interface]
```

Paper II now provides the declared planar/cylindrical pullback interface used in
Paper III.  The dependency is one-way and bounded: Paper II proves no singular,
tube, or knot conclusion, so the foundational architecture remains acyclic.

---

# Paper I: Foundations

## Provisional title

**Arithmetic Expression Geometry I: Foundations**

Recommended subtitle:

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

## Central thesis

Paper I develops the following chain:

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

The intended foundational result is:

> Sequential arithmetic expressions admit a history-sensitive formalism based on marked spinal trees. Non-degenerate bilateral arithmetic histories act projectively on (\mathbb P^1(K)) and generate (PGL_2(K)), while the continuous AEG theory developed in this paper is the affine or Borel sector stabilizing a point at infinity. This affine sector carries natural cocycles, an infinitesimal flow, a basic hyperbolic realization, global torsion formulas, a regular zero-set theory, and a contact connection whose curvature records local order defects.

---

## Required foundational results

Paper I is intended to establish rigorous versions of:

1. the sequential-tree classification;
2. marked spinal histories and chirality words;
3. the distinction among mirror, temporal reversal, and path inverse;
4. projective evaluation of bilateral one-hole arithmetic contexts;
5. generation of (PGL_2(K));
6. identification of the affine/Borel sector;
7. target-frame and source-normalized affine cocycles;
8. the continuous affine flow equation;
9. the basic hyperbolic model (\mathfrak E_0);
10. the regular zero-locus theorem;
11. a foundational definition of singular AES;
12. generalized two-history torsion in the ACS;
13. the contact-curvature and horizontal-differential identities.

---

## Paper I chapter plan

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
Appendix A. Composition and action conventions
Appendix B. Affine-cocycle calculations
Appendix C. Hyperbolic-model calculations
Appendix D. ACS and contact calculations
Appendix E. Equality and neutrality examples
```

---

## Paper I scope boundary

Paper I provides the common foundation for the later papers. It does **not** develop as main theories:

* the full bivaluation and rank-one-projector theory;
* the complete (G/H) and (G/B_\pm) quotient tower;
* projective condensation semantics;
* a complete arithmetic holomorphic function theory;
* Poisson kernels, Green functions, or boundary-value analysis;
* a general (E_k) or (E_{\log}) classification;
* singular tube bifurcation theory;
* braid, knot, or Markov invariants;
* general computational-complexity consequences.

These belong to Papers II–IV.

---

# Core mathematical architecture

## Sequential histories

A binary expression tree is called sequential when its internal-node dependency poset has a unique legal evaluation order.

The target classification theorem is:

[
\text{unique linear extension}
\iff
\text{dependency poset is a chain}
\iff
\text{internal vertices form one spine}.
]

After marking the evolving accumulator, a sequential tree becomes a history of one-hole contexts:

[
C_{\omega,c}^{(1)}[z]=\omega(z,c),
\qquad
C_{\omega,c}^{(2)}[z]=\omega(c,z).
]

The operand-slot sequence forms the **chirality word**.

The restructuring replaces the earlier ambiguous use of “threadlike expression” with this intrinsic marked-spine formalism.

---

## Projective and affine semantics

Non-degenerate one-hole arithmetic contexts act by fractional linear transformations on:

[
\mathbb P^1(K).
]

Translations, nonzero scalings, and inversion generate:

[
PGL_2(K).
]

The transformations fixing the selected point at infinity form:

[
B_\infty
========

\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

The continuous real AEG theory uses positive scalings:

[
z\mapsto e^\lambda z,
]

and therefore lies in:

[
\operatorname{Aff}^{+}(1,\mathbb R).
]

The general infinitesimal projective flow is Riccati:

[
\dot z=\beta+\alpha z+\kappa z^2,
]

while Paper I develops the affine slice:

[
\kappa=0.
]

Projective continuation and ordinary arithmetic evaluation remain distinct: a projective map may pass through (\infty), while an ordinary arithmetic expression may be undefined because of division by zero.

---

## Affine cocycles

For affine steps:

[
f_i(x)=s_ix+t_i,
\qquad
s_i\neq0,
]

their chronological composition has the form:

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n,
]

where:

[
\Phi_n=\prod_{i=1}^n s_i,
]

[
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j.
]

The source-normalized translation is:

[
\widehat\xi_n
=============

# \frac{\xi_n}{\Phi_n}

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

These two cocycles encode future scaling and past normalization, respectively. They determine the weighting kernels later used in the ACS.

---

## Continuous affine flow

The infinitesimal add and multiply directions produce:

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

In local additive and multiplicative coordinates:

[
da=\mu,du+\lambda a,dv.
]

After specifying a compatible metric frame:

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

The metric is part of the geometric structure; the eikonal equation is not metric-free.

---

## Basic hyperbolic model

The primary regular model is the upper half-plane equipped with:

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

and assignment:

[
a(x,y)=-\frac{x}{y}.
]

Direct calculation gives:

[
|\nabla a|*{g*{\mu,\lambda}}^2
==============================

\mu^2+\lambda^2a^2.
]

The restructuring seeks to derive this model from the affine group and a normalized invariant metric, rather than presenting it only as an isolated ansatz.

No uniqueness theorem for this model is currently claimed.

---

## Regular and singular zeros

If a smooth regular AES satisfies:

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

with:

[
\mu\neq0,
]

then on:

[
Z(a)=a^{-1}(0),
]

one has:

[
|\nabla a|=|\mu|>0.
]

Thus (0) is a regular value, and the zero set is a smooth codimension-one submanifold.

On a two-dimensional regular AES, regular zeros form disjoint smooth curves. In particular, the regular interior cannot contain:

* an isolated zero;
* a zero-line crossing;
* a branch point;
* a birth or death event.

Such behavior requires singularity, degeneration, boundary effects, failure of properness, or a change of semantic category.

Paper I introduces the initial regular/singular distinction. Full multi-zero and tube theory belongs to Paper III.

---

## Global torsion and the ACS

The Accumulative Commutative Space records:

[
(A,M),
]

where (A) is accumulated additive charge and (M) is accumulated logarithmic multiplicative charge.

It is a commutative shadow of an affine history, not the complete expression space.

The preferred direct-path evaluation formula is:

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
]

For compatible histories (\gamma,\delta), relative torsion is intended to satisfy an exact sequence of identities:

[
\text{affine cocycle difference}
================================

# \text{weighted boundary integral}

\text{weighted area}.
]

Temporal reversal remains an important special case, but is no longer the only general comparison.

The final sign and orientation conventions remain part of the active mathematical audit.

---

## Contact connection and curvature

The arithmetic contact form is:

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

Its horizontal fields are:

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a.
]

They satisfy:

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

For scalar fields, the horizontal covariant differential is:

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
]

Its antisymmetrized second horizontal derivative is:

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

This is a curvature-sensitive horizontal operator, not an ordinary nilpotent de Rham differential.

Paper II adds the horizontal metric, compatible complex structure, analytic domains, and function theory.

---

# Current mathematical status

Papers I--IV now have canonical mathematical-review manuscripts and per-paper closure
records. This does not make every research programme complete or authorize a public
release. Open questions retained by the manuscripts and governance register remain
open, and exploratory notes retain no automatic theorem authority.

Claim-level status, including the hypotheses and boundaries of proved, conditional,
proposed, conjectural, and excluded statements, is controlled by the mathematical
status register and the per-paper closure and decision records rather than by the
manuscripts' editorial `draft` labels.

The complete status register is:

[`governance/05-mathematical-status.md`](05-mathematical-status.md)

The unresolved decision register is:

[`governance/08-open-questions.md`](08-open-questions.md)

---

# Claims not established

The repository must not be read as proving any of the following unconditional implications:

[
\text{noncommutativity}
\Rightarrow
\text{negative curvature},
]

[
\text{negative curvature}
\Rightarrow
\text{algorithmic hardness},
]

[
\text{multiple zero lines}
\Rightarrow
\text{knot invariant},
]

[
\text{contact structure}
\Rightarrow
\text{unique complex structure},
]

[
\text{projective continuation}
\Rightarrow
\text{ordinary arithmetic regularity}.
]

These are either false in general, require additional hypotheses, or remain open research programs.

---

# Repository organization

## Current active layout

The repository currently uses the following top-level organization:

```text
aeg-paper/
├── AGENTS.md
├── README.md
├── LICENSE
├── build.sh
├── Dockerfile
├── bibliography/
├── governance/
├── images/
│   └── sources/
├── notes/
├── paper-1/
├── paper-2/
├── paper-3/
├── paper-4/
└── archive/
```

The completed migration from the historical layout is documented in:

[`governance/04-current-to-target-map.md`](04-current-to-target-map.md)
and [`migration-log.md`](migration-log.md).

Substantive research material is moved or archived, not silently deleted.

---

# Building the canonical manuscripts

A working LaTeX installation should provide at least:

* `pdflatex`;
* `bibtex`;
* the packages imported by the manuscript.

Build all four canonical manuscripts with:

```bash
./build.sh
```

To build one manuscript, run `./build.sh 1`, `./build.sh 2`, `./build.sh 3`, or
`./build.sh 4`. The corresponding entry point and artifact are
`paper-k/aeg-paper-k.tex` and `paper-k/aeg-paper-k.pdf`.

## Docker build

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

A build is considered successful only when the expected PDF is actually produced.

Build warnings that must be reviewed include:

* undefined references;
* missing citations;
* duplicate labels;
* missing figures;
* normalization or numbering inconsistencies.

# Working with Codex

Codex should not be asked to rewrite the complete paper in one pass.

Before executing a restructuring task, read:

1. `AGENTS.md`;
2. the authoritative restructuring files;
3. the mathematical-status register;
4. the open-question register;
5. the task-specific file permissions.

The first Codex task should be an audit only.

Expected output:

```text
governance/audit-report.md
```

The audit must:

* inventory the current paper;
* compare current and target structures;
* identify definition and notation conflicts;
* classify claims by mathematical status;
* identify missing proofs;
* recommend a sequence of small commits;
* run the current build as a baseline;
* leave the paper body unchanged.

Each later task must state:

```text
1. Scope
2. Files allowed to change
3. Files forbidden to change
4. Theorem nodes in scope
5. Claim statuses allowed to change
6. Required validation
7. Expected output
```

A Codex task must be rejected if it:

* invents a missing proof;
* strengthens a claim without authorization;
* silently changes composition conventions;
* deletes research material without archival disposition;
* conflates mirror and reversal;
* treats projective continuation as ordinary evaluation;
* calls an isolated singular zero regular;
* promotes a smooth total zero set to a globally trivial tube without properness;
* reports build success without producing the PDF.

---

# Contribution and review rules

This is a research mathematics repository. Contributions must preserve:

* proof status;
* hypotheses;
* domain restrictions;
* notation ownership;
* paper boundaries;
* source provenance.

Before modifying active paper sources, read:

[`AGENTS.md`](../AGENTS.md)

The governing editorial principle is:

[
\boxed{
\text{state less, define more, prove exactly, and mark the frontier}.
}
]

The four distinctions that must remain visible are:

[
\text{history}\neq\text{value},
]

[
\text{affine}\neq\text{projective},
]

[
\text{regular}\neq\text{singular},
]

[
\text{proved}\neq\text{proposed}.
]

---

# Acceptance and release

Paper I progresses through five acceptance levels:

1. repository baseline;
2. structural migration;
3. mathematical closure;
4. editorial closure;
5. release candidate.

The complete checklist is:

[`governance/07-acceptance-checklist.md`](07-acceptance-checklist.md)

Paper I is release-ready only when:

* all critical theorem nodes are proved;
* all P0 open questions are resolved;
* the source migration is complete;
* later-paper material has been separated without loss;
* the PDF builds reproducibly;
* independent mathematical and scope reviews have passed;
* the abstract and conclusion are traceable to the body.

---

# Version and DOI note

The repository may contain an earlier DOI-linked version of the manuscript.

The DOI version, the active restructuring branch, and any future restructured preprint must be distinguished explicitly.

Do not assume that an existing DOI automatically refers to the current working manuscript.

The root README and manuscript metadata should be updated when a new stable preprint is released.

---

# Research frontier

The four-paper program is organized around one stable foundation:

[
\text{history-sensitive arithmetic}
\longrightarrow
\text{operator semantics}
\longrightarrow
\text{geometric realization}.
]

From this foundation:

* Paper II asks what can be analyzed;
* Paper III asks how regular geometry becomes singular and topologically nontrivial;
* Paper IV asks what information is lost under quotient and how that loss relates to computation.

The project deliberately distinguishes:

[
\text{what has been imagined}
\neq
\text{what has been constructed}
\neq
\text{what has been verified}
\neq
\text{what has been proved}.
]

That distinction is part of the mathematical architecture of the project, not merely an editorial convention.
