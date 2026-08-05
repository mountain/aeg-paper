# AGENTS.md

## Repository purpose

This repository contains the source, notes, figures, bibliography, and build tooling for the Arithmetic Expression Geometry (AEG) paper series.

The current restructuring effort separates the material into four papers:

1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
3. **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
4. **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

The repository contains research notes written at different stages of development. Some notes contain exploratory, superseded, conjectural, or incorrect formulations. Do not treat every file as equally authoritative.

---

## Instruction hierarchy

When instructions conflict, use the following priority order:

1. The explicit task prompt.
2. This `AGENTS.md`.
3. Authoritative files under `restructure/`.
4. The current main paper source.
5. Research notes under `notes/`, `gpt/`, `plans/`, or other archival directories.

Files under `restructure/` should explicitly identify whether they are authoritative specifications, status records, audits, or archival discussions.

Chat transcripts and historical notes are evidence of the development process, not final specifications.

Do not reconcile conflicting sources silently. Record the conflict and follow the highest-priority source.

---

## General working principles

### Preserve mathematical meaning

This is a research mathematics repository, not a general prose-editing project.

When modifying the paper:

* preserve the distinction between definitions, lemmas, propositions, theorems, examples, remarks, conjectures, proposals, and open problems;
* do not convert an intuition, analogy, computational observation, or structural proposal into a theorem;
* do not strengthen assumptions or conclusions without an explicit proof;
* do not remove hypotheses merely to simplify exposition;
* do not infer uniqueness, existence, regularity, compactness, properness, or invariance unless it has been established;
* do not conceal mathematical gaps with polished prose;
* state unresolved points explicitly.

If a proof is incomplete, mark the result as incomplete, proposed, conjectural, or conditional according to the authoritative mathematical-status file.

### Process before result

AEG distinguishes several levels that must not be collapsed:

[
\text{expression tree}
\longrightarrow
\text{marked history}
\longrightarrow
\text{operator}
\longrightarrow
\text{endpoint value}.
]

When editing definitions or arguments, preserve the distinction between:

* literal syntactic equality;
* equality of marked histories;
* equality of induced operators;
* equality of total charges;
* equality of endpoint values;
* equality after quotient, normalization, or condensation.

Do not identify two histories merely because they evaluate to the same value.

### Preserve provenance

Do not delete research material merely because it is no longer part of Paper I.

When material is moved out of the main paper:

* move it to the appropriate paper draft, note, appendix, or archive;
* preserve useful labels, citations, formulas, examples, and proof fragments;
* record the source and destination in the restructuring log;
* avoid destructive rewrites that make the development history unrecoverable.

---

## Authoritative restructuring documents

Before performing any restructuring task, read the relevant files under `restructure/`.

The expected authoritative files include:

* `restructure/00-authoritative-scope.md`
* `restructure/01-paper-series-architecture.md`
* `restructure/02-paper-I-outline.md`
* `restructure/03-theorem-dependency-graph.md`
* `restructure/04-current-to-target-map.md`
* `restructure/05-mathematical-status.md`
* `restructure/06-editorial-rules.md`
* `restructure/07-acceptance-checklist.md`
* `restructure/08-open-questions.md`

If one or more of these files do not yet exist, do not invent their contents. Work only within the scope explicitly provided by the task.

The files under `restructure/discussions/` summarize research routes but are subordinate to the authoritative scope and mathematical-status files.

The files under `restructure/archive/` are archival and must not be treated as current decisions.

---

## Paper I scope discipline

Paper I establishes the foundational affine geometry of AEG within its projective context.

Its intended logical spine is:

[
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
]

Paper I may contain:

* sequential-tree classification;
* marked spinal histories;
* operand-slot chirality;
* mirror, temporal reversal, and path inverse;
* projective evaluation of non-degenerate bilateral histories;
* generation of (PGL_2(K));
* identification of the affine/Borel sector;
* affine cocycle formulas;
* continuous affine flow;
* the basic hyperbolic model;
* regular zero-locus results;
* a foundational definition of singular arithmetic expression spaces;
* a minimal multi-zero example, if fully verified;
* a basic parameter-family zero-surface lemma;
* ACS and generalized torsion;
* contact connection and horizontal covariant differential.

Paper I must not develop as a main theory:

* full bivaluation or rank-one projector theory;
* the complete (G/H) and (G/B_\pm) quotient tower;
* concept–predicate semantics;
* a full arithmetic holomorphic function theory;
* Poisson kernels, Green functions, or boundary-value theory;
* general (E_k) or (E_{\log}) classifications;
* singular tube bifurcation theory;
* braids, knots, Markov moves, or new knot invariants;
* general computational-complexity conclusions.

These belong to later papers unless an authoritative scope file says otherwise.

---

## Important mathematical distinctions

### Sequential trees

Do not use informal left-expanded/right-expanded terminology when it is ambiguous.

Prefer intrinsic definitions based on:

* the dependency poset of internal vertices;
* uniqueness of the evaluation order;
* the existence of a single internal spine;
* a marked accumulator;
* explicit operand-slot labels.

Use:

[
C_{\omega,c}^{(1)}[z]=\omega(z,c),
\qquad
C_{\omega,c}^{(2)}[z]=\omega(c,z).
]

Do not confuse the planar orientation of a tree with the temporal order of evaluation.

### Mirror and reversal

Keep the following distinct:

* **mirror**: swaps operand-slot positions;
* **temporal reversal**: reverses the context word;
* **path inverse**: reverses the word and replaces each invertible context by its inverse.

Arithmetic torsion defined from order comparison does not automatically detect tree mirror.

### Projective and ordinary arithmetic semantics

Projective continuation changes the semantic category.

For example, a Möbius map may send (0) to (\infty), while ordinary arithmetic declares division by zero undefined.

Always distinguish:

* ordinary admissible arithmetic evaluation;
* projective continuation;
* chart transitions;
* poles and domain exclusions.

Do not state that projective completion removes ordinary arithmetic singularities without qualification.

### Affine and projective flow

The existing continuous AEG flow is the affine/Borel slice of the projective Riccati flow.

Keep distinct:

[
\dot z=\beta+\alpha z
]

and

[
\dot z=\beta+\alpha z+\kappa z^2.
]

Do not use conclusions proved only in the affine sector as though they automatically hold in the full projective theory.

### Left and right group conventions

Whenever using matrix evolution or Maurer–Cartan forms, state the convention explicitly.

Distinguish:

[
g^{-1}dg
\qquad\text{from}\qquad
dg,g^{-1}.
]

Also distinguish:

* source/body-frame coordinates;
* target/spatial-frame coordinates;
* left multiplication;
* right multiplication;
* operand-slot chirality.

These are related structures but are not identical by definition.

### Torsion

Prefer a two-history formulation when possible.

If histories (\gamma) and (\delta) have compatible total charge or linear part, define and analyze their relative defect explicitly.

Do not privilege reversal unless the theorem or example specifically requires it.

Keep distinct:

* endpoint difference;
* affine translation coordinate;
* group-valued relative defect;
* open two-step torsion;
* closed-loop holonomy;
* infinitesimal curvature density;
* ACS weighted area.

### Contact structure and analysis

The contact form and horizontal distribution do not by themselves uniquely determine a complex structure.

Keep distinct:

* contact form;
* horizontal distribution;
* horizontal metric;
* orientation;
* compatible almost-complex structure;
* arithmetic Cauchy–Riemann operator.

Do not claim that arithmetic holomorphicity is uniquely forced by the contact form unless a uniqueness theorem is supplied.

### Horizontal differential

The operator currently denoted by (\delta) is curvature-sensitive and generally not nilpotent.

Prefer terminology such as:

* horizontal covariant differential;
* horizontal differential;
* connection-induced differential.

Do not describe it as an ordinary differential complex when

[
\delta^2\neq0.
]

### Zero loci and singularities

For a smooth non-degenerate arithmetic expression space satisfying

[
|\nabla a|^2=\mu^2+\lambda^2a^2
]

with (\mu\neq0), the zero set is regular because

[
|\nabla a|=|\mu|
\quad\text{on }a^{-1}(0).
]

Consequently, in the smooth non-degenerate setting, do not introduce:

* isolated zero points;
* zero-line crossings;
* branching zero lines;
* zero-line birth or death;

without identifying the necessary singularity, degeneracy, boundary effect, failure of properness, or change of category.

Use explicit notation for:

[
Z_{\mathrm{reg}}(a)
\qquad\text{and}\qquad
Z_{\mathrm{sing}}(a).
]

### Tube structures

A regular parameter family may produce a smooth total zero set, but stronger conclusions require additional hypotheses.

Do not claim:

* global product structure;
* topology preservation;
* compactness;
* properness;
* isotopy invariance;
* braid or knot invariance;

without stating and proving the required assumptions.

---

## Mathematical status labels

Every substantial result introduced or moved during restructuring must have one of the following statuses:

* `proved`;
* `proved with stated hypotheses`;
* `standard consequence requiring an in-paper proof`;
* `computationally verified example`;
* `partially proved`;
* `structural proposal`;
* `conjecture`;
* `open problem`;
* `unsupported and excluded`.

Use the authoritative mathematical-status file to determine the status.

If the status is unclear, do not guess. Add the issue to the open-questions or audit file.

---

## Editing rules

### Make small, reviewable changes

Prefer a sequence of narrow commits over a single global rewrite.

Each task should modify only the files required by its scope.

Do not combine in one commit:

* foundational definition changes;
* chapter reordering;
* notation normalization;
* proof repair;
* bibliography cleanup;
* figure redesign;
* migration to another paper;

unless the task explicitly requires that combination.

### Maintain dependency order

A definition or theorem must appear before it is used, unless the reference is explicitly prospective.

Use the theorem dependency graph when restructuring.

After moving a result, check:

* all references;
* labels;
* theorem numbering;
* notation dependencies;
* bibliography entries;
* introductory summaries;
* abstract claims;
* conclusion claims.

### Avoid duplicated theories

When a result is moved to another paper:

* leave only the minimal statement or forward reference needed by Paper I;
* do not maintain divergent full versions in two locations;
* identify one canonical source file.

### Preserve notation consistency

Before introducing new notation, search the repository for existing uses.

Pay particular attention to:

* (\mathfrak E_0) versus (\mathfrak E_1);
* (u) versus visually similar symbols such as (\nu);
* (A,M) as ACS coordinates;
* (a) as assignment value;
* (\lambda,\mu) as generator intensities;
* source-normalized versus target-normalized affine coordinates;
* (E_k), (E_{\log}), and other model labels;
* left/right, slot (1)/slot (2), source/target, mirror/reversal.

Do not rename established notation globally without an explicit migration plan.

### Proof discipline

When editing a proof:

* preserve all hypotheses;
* check every use of regularity, positivity, invertibility, compactness, and field assumptions;
* distinguish real, complex, characteristic-zero, and arbitrary-field arguments;
* distinguish local from global conclusions;
* distinguish finite from infinitesimal identities;
* distinguish exact formulas from asymptotic expansions.

Do not replace a proof with phrases such as “clearly,” “naturally,” or “it follows” unless the omitted step is genuinely routine and still recoverable.

---

## LaTeX rules

### Source organization

Use existing section files where appropriate.

If a chapter is substantially restructured, prefer clear new section files rather than accumulating unrelated material in one file.

Keep appendices for:

* long computations;
* extended examples;
* coordinate checks;
* tables of cases;
* secondary derivations.

Keep the main text focused on definitions, central examples, propositions, theorems, and conceptual transitions.

### Labels and references

Use semantic labels, for example:

```latex
\label{thm:sequential-tree-classification}
\label{def:marked-spinal-history}
\label{prop:affine-cocycle}
\label{thm:regular-zero-locus}
```

Avoid autogenerated or narrative labels containing words such as `final`, `revised`, or `enhanced`.

Do not reuse a label.

After structural changes, search for broken references and duplicate labels.

### Theorem environments

Use the correct theorem heading.

In particular, examples must use an `example` environment whose printed title is `Example`, not `Theorem`.

Do not introduce unnumbered theorem-like claims unless there is a clear editorial reason.

### Equations

Use exact equations for mathematical content.

Do not use displayed equations merely as decoration.

State whether identities are:

* exact;
* local;
* asymptotic;
* infinitesimal;
* valid only on the horizontal distribution;
* valid only away from singularities.

### Bibliography

Do not add citations merely to make a section appear broader.

Use primary or standard mathematical references when making historical or technical comparisons.

Do not cite a source for a theorem unless the cited source actually contains the relevant result.

Do not remove bibliography entries that remain used elsewhere.

---

## Build and validation

The normal local build command is:

```bash
./build.sh
```

A Docker build path is also available:

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

For every task that modifies LaTeX source:

1. run the available build process;
2. report whether the PDF was produced;
3. inspect build errors and important warnings;
4. check for undefined references;
5. check for missing citations;
6. check for duplicate labels;
7. check for missing figures or assets.

Do not report success merely because a command exits without an obvious error. Confirm that the expected PDF artifact exists.

If the environment cannot build the paper, report the exact limitation and still perform static checks.

---

## Required task report

At the end of a restructuring task, provide a concise report containing:

1. files changed;
2. mathematical claims added, removed, weakened, or relocated;
3. assumptions introduced or made explicit;
4. unresolved mathematical issues;
5. material moved to another paper or archive;
6. build result;
7. remaining warnings;
8. recommended next task.

Do not describe a mathematical gap as resolved unless the repository contains the proof.

---

## Prohibited behavior

Do not:

* rewrite the entire paper in one uncontrolled pass;
* silently discard research notes;
* silently merge inconsistent definitions;
* invent missing proofs;
* turn analogies into mathematical equivalences;
* turn experimental evidence into general theorems;
* infer computational lower bounds from geometric growth alone;
* infer hyperbolicity from noncommutativity alone;
* infer knot invariance from a visually suggestive tube construction;
* infer uniqueness from a symmetric example;
* claim that a parameter family is topologically trivial without properness or equivalent hypotheses;
* treat projective continuation as ordinary arithmetic evaluation;
* treat the current affine theory as the complete projective theory;
* treat archival discussion as authoritative specification.

---

## Safe default when uncertain

When a mathematical or editorial decision cannot be resolved from authoritative files:

1. preserve the existing source;
2. add a precise note to the task report or open-questions file;
3. propose the minimum viable change;
4. do not guess the author's intended theorem.

The goal of restructuring is not merely to improve presentation. It is to produce a paper series whose definitions, proofs, dependencies, and research boundaries are explicit, stable, and auditable.
