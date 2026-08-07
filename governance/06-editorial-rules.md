# Editorial Rules for the AEG Paper Series

**File:** `governance/06-editorial-rules.md`
**Status:** Authoritative
**Version:** 1.0
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`
* `governance/04-current-to-target-map.md`
* `governance/05-mathematical-status.md`

**Applies to:** Papers I–IV, their appendices, and active technical notes intended for eventual publication.

---

## 1. Purpose

This document defines the editorial and expository standards of the Arithmetic Expression Geometry paper series.

Its purposes are to:

* keep terminology and notation stable across papers;
* ensure that mathematical status is visible in the prose;
* prevent exploratory language from being mistaken for proved mathematics;
* enforce consistent theorem, definition, equation, figure, and citation practices;
* make the papers independently readable while preserving a coherent series architecture;
* support precise review by human collaborators and Codex.

These rules govern presentation. They do not override mathematical scope or status.

When an editorial preference conflicts with mathematical accuracy, mathematical accuracy takes priority.

---

# Part I. General prose principles

## 2. Language of publication

The main papers are written in English.

Research notes may remain in Chinese or bilingual form, but any material migrated into a paper must be rewritten into publication-quality mathematical English.

The English should be:

* direct;
* formal;
* economical;
* explicit about hypotheses;
* restrained in claims;
* free of promotional language.

Avoid literal translation from Chinese when it produces unnatural English syntax.

---

## 3. Default paragraph structure

A mathematical paragraph should normally perform one principal function:

1. define an object;
2. state a claim;
3. prove a claim;
4. interpret a result;
5. connect two sections;
6. delimit scope.

Do not combine definition, proof, speculation, and historical commentary in one paragraph.

Long paragraphs should be split when they contain multiple logical steps.

---

## 4. Claim-first exposition

When introducing a substantial result, use the order:

1. motivation;
2. precise statement;
3. proof;
4. interpretation;
5. limitations or downstream use.

Do not spend several pages motivating a theorem before the reader knows its statement.

Do not interpret a theorem more strongly than its formal conclusion.

---

## 5. Show the logical chain

Each section should make clear:

* what objects are already available;
* what new object or result is introduced;
* what hypothesis is added;
* what downstream result depends on it.

Use explicit transition sentences such as:

> The preceding cocycle formula supplies the weighting kernel used in the ACS construction.

or:

> The regular-zero theorem shows that isolated zeros require a failure of the regular hypotheses; this motivates the singular-AES definition.

Avoid vague transitions such as:

> This naturally leads to many interesting directions.

---

## 6. Avoid rhetorical inflation

Do not use promotional phrases such as:

* “revolutionary”;
* “groundbreaking”;
* “deeply profound”;
* “completely new geometry”;
* “unavoidable”;
* “obviously fundamental”;
* “the ultimate theory”;
* “a universal principle”;

unless the statement is mathematically defined and proved.

Preferred alternatives:

* “provides”;
* “suggests”;
* “gives a model of”;
* “defines”;
* “establishes under the stated hypotheses”;
* “raises the question whether”;
* “serves as a first example.”

---

## 7. Distinguish mathematics from interpretation

Use explicit markers.

### For proved mathematical content

> Proposition 4.2 shows that …

### For an interpretation

> This may be interpreted as …

### For a structural proposal

> We propose to regard …

### For a conjecture

> We conjecture that …

### For an open problem

> It remains open whether …

Do not move from one register to another without signaling the change.

---

## 8. Avoid anthropomorphic causal language

Prefer:

> The multiplicative steps rescale earlier additive contributions.

Avoid:

> Each additive step remembers the future.

Metaphorical language may appear sparingly after the precise formula has been established.

---

# Part II. Status-sensitive writing

## 9. Proved results

A result with status `PROVED` or `PROVED WITH STATED HYPOTHESES` may be written declaratively.

Example:

> The horizontal fields satisfy
> [
> [D_u,D_v]=\mu\lambda\partial_a.
> ]

The statement must include every required hypothesis either in the theorem or in a clearly active standing assumption.

---

## 10. Standard consequences

A result with status `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` must not be described as already established until the proof or exact citation appears.

Before integration, use:

> Under the regularity assumptions, the regular-value theorem is expected to imply that (Z(a)) is a smooth submanifold.

After proof integration, declarative wording is permitted.

---

## 11. Partially proved claims

State the proved scope before the intended generalization.

Preferred form:

> We prove the statement for the basic model (\mathfrak E_0). Its extension to general regular AES remains open.

Avoid:

> The theorem holds generally, as illustrated by (\mathfrak E_0).

---

## 12. Structural proposals

A structural proposal must be introduced with language such as:

* “We define provisionally …”
* “We propose the following framework …”
* “The following construction is intended as …”
* “This section formulates, but does not yet prove, …”

A proposal must not be enclosed in a `theorem`, `proposition`, or `corollary` environment.

Use a `definition`, `construction`, `program`, or `remark` environment as appropriate.

---

## 13. Conjectures

A conjecture must be mathematically precise.

It must state:

* ambient category;
* all hypotheses;
* exact conclusion;
* known special cases;
* known obstructions, if any.

Do not label a broad aspiration as a conjecture.

Use an `openproblem` environment instead when no definite answer is proposed.

---

## 14. Open problems

Open problems should be short and falsifiable where possible.

Preferred form:

> **Open Problem.** Classify the regular affine AES models that are homogeneous under a transitive two-dimensional Lie-group action.

Avoid lists of vague aspirations such as:

> Develop the whole theory and understand all its applications.

---

## 15. Unsupported claims

Claims marked `UNSUPPORTED AND EXCLUDED` must not appear in active paper prose except in one of the following forms:

* a historical note explaining why the formulation was abandoned;
* an explicit warning;
* a question whose answer is not presumed.

Example:

> Noncommutativity alone does not imply negative curvature; any such relation must be established for a specified metric model.

---

# Part III. Terminology

## 16. Canonical foundational terminology

Use the following terms consistently.

### `arithmetic expression tree`

A binary syntax tree whose internal nodes are arithmetic operations.

### `sequential tree`

A finite binary expression tree whose internal-node dependency poset is a chain.

### `marked spinal history`

A sequential tree together with a marked accumulator, represented as a chronological word of one-hole contexts.

### `chirality word`

The operand-slot sequence:

[
\varepsilon_1\cdots\varepsilon_n,
\qquad
\varepsilon_i\in{1,2}.
]

### `ordinary arithmetic evaluation`

Evaluation subject to ordinary domain restrictions, including division by zero.

### `projective evaluation`

Evaluation as a fractional linear transformation on (\mathbb P^1(K)).

### `affine sector`

The subgroup fixing the chosen point at infinity.

### `assignment function`

The scalar field (a) on an arithmetic expression space.

### `regular AES`

An arithmetic expression space satisfying the selected smooth regular definition.

### `singular AES`

A space with a declared singular locus and a regular AES structure on its complement.

### `ACS`

The Accumulative Commutative Space recording additive and logarithmic multiplicative charge.

### `relative torsion`

A defect comparing two compatible histories.

### `horizontal covariant differential`

The operator denoted (\delta_H), unless a later scope decision changes the notation.

---

## 17. Deprecated terminology

Avoid the following unless discussing historical usage.

### `threadlike expression`

This term is deprecated as the primary definition because it has been associated with ambiguous child orientation.

It may be used parenthetically after the canonical definition:

> marked spinal histories, called threadlike expressions in earlier drafts.

### `left-expanded` and `right-expanded`

Avoid unless the exact tree orientation is diagrammed and operand slots are specified.

Use:

* slot-(1) history;
* slot-(2) history;
* pure-chirality history;
* mixed-chirality history.

### `arithmetic holomorphicity is forced by contact geometry`

Do not use.

Preferred:

> After choosing compatible horizontal metric and complex data, one may define an arithmetic Cauchy–Riemann operator.

### `tube`

Do not use for every parameterized zero set.

Use the hierarchy:

1. total zero set;
2. regular zero surface;
3. locally trivial zero family;
4. zero tube;
5. threaded tube.

---

## 18. Mirror, reversal, and inverse

Use the terms exactly as follows.

* **mirror:** operand-slot exchange;
* **temporal reversal:** reversal of the context word;
* **path inverse:** reversal together with inversion of each invertible context.

Do not use “reverse” without a qualifier when ambiguity is possible.

---

## 19. Regular and singular zeros

Use:

[
Z(a)=a^{-1}(0),
]

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

Do not call an isolated zero “regular” when the regular-zero theorem applies with (\mu\neq0).

Use:

* singular zero;
* deleted zero;
* boundary zero;
* degenerate zero;

only after specifying the relevant mechanism.

---

# Part IV. Notation

## 20. General notation policy

Every symbol must have one canonical role within a paper.

Do not assign two conceptually distinct meanings to the same symbol in one chapter.

When inherited notation is potentially ambiguous, rename the secondary quantity rather than relying on context.

---

## 21. Fields and spaces

Use:

[
K
]

for a general field.

Use:

[
\mathbb R,\quad \mathbb C,\quad \mathbb F_q
]

for standard specializations.

Use:

[
\mathbb P^1(K)
]

for the projective line.

Use:

[
\operatorname{Aff}(1,K),
\qquad
PGL_2(K)
]

with consistent roman operator typography.

Do not alternate between `\PGL`, `\operatorname{PGL}`, and plain italic (PGL) within one paper.

---

## 22. Histories and evaluation

Use:

[
\gamma,\delta
]

for histories.

Use:

[
\rho(\gamma)
]

for projective or operator evaluation.

Use:

[
\nu_x(\gamma)
]

for ordinary endpoint evaluation at initial value (x).

Use:

[
C_\gamma
]

for the ACS path.

Use:

[
\Sigma_{\gamma,\delta}
]

for a filling between compatible ACS paths.

---

## 23. Affine data

For:

[
x\mapsto \Phi x+\xi,
]

use:

* (\Phi): accumulated scale;
* (\xi): target-frame translation;
* (\widehat\xi=\Phi^{-1}\xi): source-normalized translation.

Do not use (a) for affine translation when (a) is already the assignment function.

---

## 24. Flow data

Use:

* (u): additive coordinate;
* (v): multiplicative coordinate;
* (a): assignment;
* (\mu): additive intensity;
* (\lambda): logarithmic multiplicative intensity;
* (\theta): direction angle;
* (s): curve parameter or arclength.

Avoid using (\lambda) simultaneously for:

* a fixed flow intensity;
* accumulated logarithmic scale;
* eigenvalue.

If accumulated scale is needed in the same chapter, use another symbol such as:

[
M
\quad\text{or}\quad
\Lambda.
]

---

## 25. Manifold notation

Prefer:

[
\mathcal M
]

for a manifold when the letter (M) is also used for multiplicative charge.

Use:

[
g
]

for a Riemannian metric.

Use:

[
\mathcal H
]

for a horizontal distribution only when it is not confused with the upper half-plane.

For the upper half-plane, prefer:

[
\mathbb H
\quad\text{or}\quad
\mathbb H^2.
]

If both are present in the same chapter, reserve:

[
\mathcal D=\ker\alpha
]

for the contact distribution.

---

## 26. ACS notation

Use:

[
(A,M)
]

for additive and multiplicative charges.

Use one canonical weighted form.

For example:

[
\eta=e^{-M},dA
]

or its terminally normalized variant.

Once selected, do not switch between (e^M dA) and (e^{-M}dA) without an explicit coordinate or orientation conversion.

---

## 27. Contact notation

Use:

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

Use:

[
D_u,\quad D_v
]

for horizontal lifts.

Use:

[
\delta_H
]

for the horizontal covariant differential.

Use:

[
\Delta_H
]

only after its exact definition has been fixed.

---

## 28. Model notation

Use:

[
\mathfrak E_0
]

for the basic regular hyperbolic model after the model-name audit is complete.

Use:

[
\mathfrak E_1
]

only after its singular definition is fixed.

Do not assign (E_k) labels based solely on the number of visible zero lines unless that indexing convention has been formally adopted.

---

# Part V. Definitions

## 29. Definition style

A definition should:

* identify the ambient category;
* state all data;
* state all required conditions;
* avoid embedding unproved consequences;
* avoid motivation inside the formal sentence.

Preferred:

> **Definition 3.1.** A marked spinal history over (K) consists of an initial value (x_0) and a finite sequence ((\omega_i,c_i,\varepsilon_i)), where …

Then follow with interpretation in a separate paragraph.

---

## 30. Avoid circular definitions

Do not define:

* AES using “arithmetic flow” before arithmetic flow is defined;
* singular AES using “singular” without declaring the regular locus;
* tube using topological invariance before the relevant theorem;
* condensation using complexity loss before complexity is defined.

---

## 31. Definitions versus examples

A motivating example may precede a definition, but it must not substitute for it.

After the definition, return to the example and verify it satisfies every condition.

---

## 32. Provisional definitions

A provisional definition must be labeled as such in notes.

In published papers, only stable definitions should appear without qualification.

When a definition remains under development, use:

> For the purposes of this paper, we use the following restricted definition.

---

# Part VI. Theorem environments

## 33. Standard environments

Use a consistent environment set:

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{construction}[theorem]{Construction}
\newtheorem{example}[theorem]{Example}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{openproblem}[theorem]{Open Problem}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{warning}[theorem]{Warning}
```

The exact numbering scheme may vary, but all theorem-like environments should share a coherent counter.

---

## 34. Environment selection

Use:

* `theorem` for central results with significant consequences;
* `proposition` for substantial but local or computational results;
* `lemma` for supporting results;
* `corollary` for immediate consequences;
* `definition` for stable objects;
* `construction` for a defined procedure or model;
* `example` for explicit instances;
* `conjecture` for precise unproved claims;
* `openproblem` for questions;
* `remark` for interpretation;
* `warning` for scope or domain hazards.

Do not place a proposal inside a theorem environment.

---

## 35. Theorem titles

Use concise, semantic theorem titles.

Preferred:

* Sequential-tree classification
* Bilateral generation theorem
* Regular zero-locus theorem
* Weighted torsion–Stokes theorem

Avoid titles such as:

* Main theorem
* Revised theorem
* Improved final theorem
* Fundamental groundbreaking identity

---

## 36. Theorem labels

Use semantic labels:

```latex
\label{thm:sequential-tree-classification}
\label{prop:target-affine-cocycle}
\label{def:singular-aes}
```

Avoid:

```latex
\label{eq:final_revised_enhanced_acs_AM_lc}
```

Labels must describe mathematical content, not editing history.

---

## 37. Standing assumptions

Standing assumptions may be declared at the beginning of a section.

Example:

> Throughout this section, (K) is a field and all affine multipliers are nonzero.

Do not rely on assumptions declared several chapters earlier when they are essential to a theorem.

Repeat critical hypotheses in the theorem statement.

---

# Part VII. Proof style

## 38. Proof completeness

Every proof should expose the key mathematical step.

Do not replace essential reasoning with:

* “it is easy to see”;
* “obviously”;
* “clearly”;
* “by standard arguments”;

unless a precise citation or immediately recoverable calculation is available.

---

## 39. Proof decomposition

For longer proofs, use short internal paragraphs:

* `Existence.`
* `Uniqueness.`
* `Injectivity.`
* `Surjectivity.`
* `Regularity.`
* `Compatibility with composition.`

Do not use excessive itemization when continuous prose is clearer.

---

## 40. Calculation proofs

In calculations:

1. state the formula being computed;
2. show the nontrivial intermediate step;
3. identify where each hypothesis is used;
4. state the resulting conclusion.

Example:

[
|\nabla a|_g^2
==============

# g^{xx}a_x^2+g^{yy}a_y^2

\mu^2+\lambda^2a^2.
]

Do not omit the inverse metric when the normalization is nonstandard.

---

## 41. Convention-sensitive proofs

Any proof involving:

* group composition;
* path order;
* matrix multiplication;
* orientation;
* Stokes’ theorem;
* commutators;

must explicitly reference the adopted convention.

At least one explicit example should be used to verify signs.

---

## 42. Local versus global conclusions

At the end of a proof, state the actual scope.

Preferred:

> Thus (Z(a)) is a smooth one-dimensional submanifold near every interior zero.

Do not conclude:

> Hence the zero set is globally a finite collection of circles.

unless compactness and global topology have been established.

---

## 43. Standard theorem invocation

When invoking a standard theorem, state:

* the theorem;
* the map or object to which it is applied;
* the verified hypotheses;
* the conclusion.

Example:

> Since (d_pa_t\neq0) on (\mathcal Z), the value (0) is regular for (A(p,t)=a_t(p)). The regular-value theorem therefore implies that (\mathcal Z) is a codimension-one submanifold.

---

# Part VIII. Equations

## 44. Display-equation policy

Display an equation when it is:

* referenced later;
* structurally important;
* too long for inline prose;
* central to a derivation.

Do not display trivial equations merely to create visual emphasis.

---

## 45. Equation numbering

Number equations only when they are referenced later.

Use semantic labels:

```latex
\label{eq:affine-flow}
\label{eq:target-cocycle}
\label{eq:contact-form}
```

Do not manually tag equations with provisional numbers such as `\tag{7}` unless required by an external format.

Let LaTeX manage numbering.

---

## 46. Exact versus asymptotic formulas

Mark asymptotic formulas explicitly:

[
\Delta\tau
==========

\mu\lambda,du,dv
+
O(|(du,dv)|^3).
]

Do not rewrite an asymptotic expansion as an exact differential-form identity.

Use:

* `=`;
* `\sim`;
* `O(\cdot)`;
* `o(\cdot)`;

according to their precise meanings.

---

## 47. Differential-form orientation

For wedge products and Stokes formulas:

* fix orientation;
* state boundary orientation;
* avoid switching (dM\wedge dA) and (dA\wedge dM) silently;
* verify sign with an elementary rectangle.

---

## 48. Norm notation

Use:

[
|\nabla a|_g
]

when the metric matters.

Avoid:

[
|\nabla a|
]

unless the metric is unambiguous in the immediate context.

---

## 49. Operator notation

State whether operators act:

* on scalar fields;
* on differential forms;
* locally;
* on compactly supported smooth functions;
* on a Hilbert-space domain.

Formal differential identities must not be presented as operator-theoretic results without domains.

---

# Part IX. Examples

## 50. Function of examples

Every example should have one declared purpose:

* demonstrate a definition;
* separate two notions;
* verify a sign;
* show necessity of a hypothesis;
* illustrate a theorem;
* exhibit an open phenomenon.

The opening sentence should state that purpose.

---

## 51. Examples are not proofs

Do not infer a general claim from:

* one plotted zero set;
* a finite computation;
* one symbolic model;
* one knot diagram;
* one finite-field count.

Use phrases such as:

> This example shows that the phenomenon can occur.

not:

> This proves that the phenomenon is general.

---

## 52. Worked examples

A worked example should include:

1. input history or model;
2. operator evaluation;
3. geometric representation;
4. final invariant or conclusion;
5. relation to the theorem being illustrated.

---

## 53. Counterexamples and warnings

Use explicit counterexamples to prevent common misreadings.

Important examples include:

* same endpoint but different operator;
* same operator but different history;
* mirror not equal to reversal;
* projectively defined value but ordinarily undefined intermediate step;
* isolated zero caused by singularity;
* smooth total zero set without proper global tube behavior.

---

# Part X. Figures

## 54. Mathematical role of figures

A figure must serve one of:

* define or clarify a construction;
* show a geometric model;
* illustrate a theorem;
* compare distinct notions;
* visualize a parameter family.

Do not include figures only for visual impact.

---

## 55. Figure captions

A caption must be mathematically self-contained.

It should state:

* what objects are shown;
* what color or line style means;
* which conclusion is illustrative rather than proved;
* any parameter values used.

Avoid captions such as:

> A beautiful arithmetic universe.

Preferred:

> The two ACS paths have equal total charge and bound an oriented (2)-chain. The weighted area represents their relative affine torsion.

---

## 56. Figure references

Introduce every figure in the prose before or immediately after it appears.

Do not write:

> The result is obvious from Figure 6.

Use:

> Figure 6 illustrates the geometry; the proof is given in Proposition 7.3.

---

## 57. Figure provenance

Every figure should have:

* source file;
* generation script where applicable;
* parameter record;
* target paper;
* license or authorship information if externally sourced.

Hand-edited figures should retain an editable source format.

---

## 58. Coordinate consistency

A figure must use the same:

* axis orientation;
* sign convention;
* color legend;
* model numbering;
* notation;

as the text.

If a historical figure uses superseded notation, redraw it rather than relying on caption corrections.

---

# Part XI. Tables

## 59. Appropriate use of tables

Use tables for:

* context-to-matrix correspondences;
* status registers;
* notation comparisons;
* assumptions and conclusions;
* migration summaries.

Do not use tables for long proofs or dense conceptual exposition.

---

## 60. Table captions and headings

Column headings must describe mathematical roles precisely.

Preferred:

| Context | Ordinary map | Projective matrix | Domain condition |

Avoid:

| Type | Formula | Notes |

when the meanings are ambiguous.

---

# Part XII. Citations

## 61. Citation purpose

Cite sources for:

* standard theorems;
* historical attribution;
* established terminology;
* comparison with known structures;
* external computational models.

Do not cite a general textbook as evidence that a new AEG theorem is correct.

---

## 62. Primary and standard sources

Prefer:

* original papers for named results;
* standard monographs for background;
* authoritative surveys for historical placement.

For highly standard facts, one suitable reference is enough.

---

## 63. Historical claims

Avoid broad historical claims such as:

> No previous theory has considered arithmetic geometrically.

Unless a literature review justifies the statement.

Preferred:

> The present construction differs from the cited approaches in treating ordered arithmetic evaluation histories as the primary objects.

---

## 64. Novelty claims

Use restrained language.

Preferred:

> We are not aware of a prior formulation of this particular history-to-contact construction.

Stronger novelty claims require a dedicated literature audit.

---

## 65. Citation placement

Place citations immediately after the supported statement.

Avoid collecting several unrelated citations at the end of a long paragraph.

---

# Part XIII. Abstract

## 66. Abstract content

The abstract should contain:

1. the problem;
2. the primary object;
3. the central algebraic placement;
4. the main geometric constructions;
5. the principal theorem-level conclusions;
6. the paper’s scope boundary.

It should not contain:

* detailed literature discussion;
* undefined notation beyond what can be understood locally;
* future-paper promises;
* conjectural applications;
* complexity or knot claims not proved in the paper.

---

## 67. Abstract status discipline

Only include results with status:

* `PROVED`;
* `PROVED WITH STATED HYPOTHESES`;
* `STANDARD CONSEQUENCE` after its proof is integrated.

Do not mention a minimal multi-zero example unless it has passed the verification checklist.

---

## 68. Abstract length

Target approximately 180–280 words.

The abstract should not attempt to summarize every chapter.

---

# Part XIV. Introduction

## 69. Introduction architecture

Recommended order:

1. problem and viewpoint;
2. process-to-result hierarchy;
3. sequential-history restriction;
4. bilateral projective placement;
5. affine geometric program;
6. main results;
7. scope exclusions;
8. section guide.

---

## 70. Main-results list

The introduction may contain a short numbered list of principal results.

Each item must correspond to an actual theorem or proposition in the body.

Do not list:

* broad research ambitions;
* later-paper programs;
* speculative applications.

---

## 71. Historical placement

Keep historical placement concise and mathematically relevant.

Avoid turning the introduction into a survey of:

* formal language theory;
* all of hyperbolic geometry;
* all of contact geometry;
* philosophy of computation.

---

# Part XV. Section openings and closings

## 72. Section opening

Each main section should begin with two short paragraphs:

1. what problem the section addresses;
2. what it establishes and what it assumes.

Example:

> The previous section identifies the affine operator sector. We now derive the two natural translation cocycles carried by an affine history. These formulas will later determine the weight appearing in the ACS integral.

---

## 73. Section closing

Each main section should end with:

* the result now available;
* the next dependency.

Example:

> We have therefore obtained the affine flow independently of any chosen surface model. The next section constructs a homogeneous metric realization of this flow.

Avoid repetitive summaries of every subsection.

---

## 74. Cross-paper transitions

At the end of Paper I, use precise interfaces.

Preferred:

> Paper II adds compatible horizontal metric and complex data and studies the resulting analytic operators.

Avoid:

> In the next paper we will solve the complete analytic theory.

---

# Part XVI. Appendices

## 75. Appendix role

Appendices may contain:

* convention details;
* long coordinate calculations;
* secondary examples;
* sign checks;
* proofs too technical for the main line.

Appendices must not contain foundational definitions used earlier without prior statement.

---

## 76. Appendix references

The main text should state exactly why an appendix is relevant.

Example:

> The full coordinate verification of the Laplace eigenvalue is given in Appendix C.

---

## 77. No hidden second paper

Material should move to Paper II–IV rather than remain in an oversized Paper I appendix when it develops an independent theory.

---

# Part XVII. Paper-specific editorial rules

## 78. Paper I

Paper I should emphasize:

* definitions;
* exact algebraic structure;
* convention control;
* finite versus infinitesimal distinctions;
* foundational scope.

Avoid extended analytic, knot-theoretic, or complexity discussion.

---

## 79. Paper II

Paper II must distinguish:

* formal operator identities;
* PDE results;
* functional analysis;
* global boundary theory.

The term `basis` requires a declared ambient vector space or function space.

The term `harmonic` requires a specified operator.

---

## 80. Paper III

Paper III must distinguish:

* regular zero set;
* singular germ;
* total zero set;
* tube;
* braid;
* knot.

Every visual topology claim requires a mathematical invariant or classification argument.

---

## 81. Paper IV

Paper IV must specify a cost model before using the word `complexity`.

Distinguish:

* word growth;
* representation size;
* search complexity;
* running time;
* memory;
* lower bounds.

The term `condensation` must be accompanied by an explicit map or quotient.

---

# Part XVIII. Formatting and LaTeX

## 82. Package discipline

Remove duplicate package imports.

Add packages only when required.

Avoid package combinations that redefine theorem, caption, or hyperlink behavior unpredictably.

---

## 83. Macros

Create macros for frequently used operators and spaces.

Examples:

```latex
\newcommand{\Aff}{\operatorname{Aff}}
\newcommand{\PGL}{\operatorname{PGL}}
\newcommand{\Hist}{\operatorname{Hist}}
\newcommand{\AES}{\mathrm{AES}}
```

Do not create macros for one-time expressions.

Macro names must be semantic and stable.

---

## 84. Typography

Use:

* `\operatorname{}` for named operators;
* `\mathbb{}` for standard number systems;
* `\mathfrak{}` for named expression spaces;
* `\mathcal{}` for geometric structures and families;
* upright differential (d) consistently, if a macro is adopted.

Do not mix stylistic conventions within a paper.

---

## 85. Quotations

Use quotation environments only for:

* a central guiding question;
* a short cited statement.

Do not use quotation formatting as visual decoration.

---

## 86. Lists

Use lists when items are genuinely parallel.

Avoid long nested itemizations in proofs and conceptual discussions.

When a list encodes logical alternatives, number the items so they can be referenced.

---

## 87. Footnotes

Use footnotes sparingly.

Do not place essential mathematical hypotheses in footnotes.

---

# Part XIX. Terminology audit list

## 88. Mandatory search terms before finalization

Search the full Paper I source for:

```text id="0qpg4h"
threadlike
left-expanded
right-expanded
reverse
canonical
unique
natural
forced
obvious
clearly
torsion
curvature
holomorphic
tube
knot
complexity
hyperbolic
projective
singular
```

Each occurrence must be checked for:

* current canonical meaning;
* unjustified strength;
* ambiguity;
* scope drift.

---

## 89. Model-name audit

Search for:

```text id="ap59kk"
\mathfrak{E}_0
\mathfrak{E}_1
E_0
E_1
zeroth kind
first kind
```

Create one authoritative correspondence table before global edits.

---

## 90. Symbol audit

Search for:

```text id="8uxt3v"
u
\nu
M
\mathcal M
\lambda
\Lambda
a
A
\delta
\delta_H
```

Check for visual and semantic collisions.

---

# Part XX. Editorial review protocol

## 91. First-pass review

Review for:

* structure;
* theorem order;
* scope;
* duplicated exposition;
* unsupported claims.

Do not spend the first pass polishing sentences around mathematically unstable content.

---

## 92. Second-pass review

Review for:

* notation;
* hypotheses;
* signs;
* composition order;
* local/global distinctions;
* status labels.

---

## 93. Third-pass review

Review for:

* prose;
* paragraph rhythm;
* transitions;
* captions;
* citations;
* typographical consistency.

---

## 94. Final abstract-conclusion audit

Compare every abstract and conclusion sentence against the body.

For each claim, identify:

* theorem number;
* proposition number;
* definition;
* explicitly labeled interpretation.

Delete or weaken any sentence that lacks support.

---

# Part XXI. Codex-specific editorial constraints

## 95. No silent strengthening

Codex must not replace:

> may suggest

with:

> proves

or:

> appears to

with:

> is

unless the status file authorizes the change.

---

## 96. No global terminology replacement without audit

Codex must not perform blind replacement of:

* `threadlike`;
* `left`;
* `right`;
* `E_0`;
* `E_1`;
* `torsion`;
* `delta`.

Each replacement requires semantic context.

---

## 97. Preserve mathematical comments

When moving a proof or theorem, preserve comments explaining:

* missing hypotheses;
* alternative conventions;
* unresolved signs;
* intended later-paper destination.

Do not delete TODO markers without resolving or relocating them.

---

## 98. Required report after editorial tasks

Each editorial task report must state:

1. terminology changed;
2. theorem environments changed;
3. labels changed;
4. notation changed;
5. claims weakened or strengthened;
6. material moved;
7. unresolved ambiguities;
8. build result.

---

# Part XXII. Acceptance rules

## 99. Editorial acceptance conditions for a chapter

A chapter is editorially acceptable only when:

* every object is defined before use;
* every theorem has explicit hypotheses;
* every proof supports the exact conclusion;
* mathematical status matches `05-mathematical-status.md`;
* terminology matches this file;
* notation matches the series architecture;
* figures and captions use current conventions;
* later-paper material is reduced to a forward reference;
* all references and citations resolve;
* no known rejected formulation remains.

---

## 100. Series-level editorial principle

The AEG series should sound ambitious because its objects and results are precise, not because its prose is expansive.

The governing editorial rule is:

[
\boxed{
\text{state less, define more, prove exactly, and mark the frontier}.
}
]

A successful exposition makes four boundaries visible:

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
