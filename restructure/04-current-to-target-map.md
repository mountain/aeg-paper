# Current-to-Target Material Map

**File:** `restructure/04-current-to-target-map.md`
**Status:** Authoritative
**Version:** 1.0
**Date:** 2026-08-06
**Depends on:**

* `AGENTS.md`
* `restructure/00-authoritative-scope.md`
* `restructure/01-paper-series-architecture.md`
* `restructure/02-paper-I-outline.md`
* `restructure/03-theorem-dependency-graph.md`

**Applies to:** The migration and restructuring of all existing material in the `aeg-paper` repository.

---

## 1. Purpose

This document assigns existing repository material to its target location in the four-paper AEG series.

It specifies, for each current source:

* its canonical destination;
* whether it is retained, split, rewritten, migrated, or archived;
* which mathematical claims may be preserved;
* which claims require weakening, verification, or removal;
* which target theorem nodes it supports;
* which downstream papers own the detailed development.

This document prevents three failure modes:

1. valuable research material being silently deleted;
2. superseded formulations remaining in the main paper;
3. the same theory being developed inconsistently in multiple papers.

---

# Part I. Migration vocabulary

## 2. Migration states

Every substantial source block must receive exactly one primary migration state.

### `KEEP`

Retain in its current paper with only local editing.

Use when:

* the mathematical role remains unchanged;
* the result belongs to the target paper;
* no substantial change of hypotheses or meaning is required.

---

### `REWRITE`

Retain the mathematical topic but rewrite its definitions, theorem statements, proofs, or narrative.

Use when:

* the current formulation is ambiguous;
* the result belongs to the target paper;
* its role or assumptions must be changed materially.

---

### `SPLIT`

Divide the source across two or more target locations.

Use when a current section contains:

* foundational and later-paper material;
* theorem and speculative outlook;
* local calculations and an independent theory.

Every split must identify one canonical destination for each component.

---

### `MOVE`

Relocate the material to another paper without retaining a full duplicate in Paper I.

Paper I may retain:

* a short summary;
* a theorem statement needed as context;
* a forward reference.

---

### `APPENDIX`

Move technical details, long computations, or secondary examples to an appendix of the same paper.

---

### `ARCHIVE`

Preserve the source as research history but remove it from active paper drafts.

Use for:

* superseded formulations;
* abandoned terminology;
* exploratory conversations;
* incorrect or incomplete approaches still useful for provenance.

---

### `REMOVE`

Delete only when the content is demonstrably:

* duplicated elsewhere with no additional provenance value;
* mechanically generated noise;
* incorrect and not useful even as an archive;
* a build artifact that should not be versioned.

Substantive mathematical material must not be removed without an archival record.

---

### `HOLD`

Do not migrate until an audit resolves its status.

Use when:

* the target paper is unclear;
* the mathematical correctness is uncertain;
* the source is referenced but not yet located;
* two incompatible versions exist.

---

## 3. Claim-treatment states

Migration state and mathematical claim status are distinct.

Each migrated claim must also be assigned one of:

* `PRESERVE`;
* `REPROVE`;
* `WEAKEN`;
* `CONDITIONALIZE`;
* `RECLASSIFY`;
* `OPEN`;
* `REJECT`.

Examples:

```text
Migration: MOVE to Paper III
Claim treatment: OPEN
```

```text
Migration: REWRITE in Paper I
Claim treatment: REPROVE
```

The authoritative claim statuses are maintained in:

```text
restructure/05-mathematical-status.md
```

---

# Part II. Target repository structure

## 4. Recommended top-level structure

The restructuring should converge toward:

```text
aeg-paper/
├── AGENTS.md
├── README.md
├── build.sh
├── Dockerfile
├── aeg-paper.bib
│
├── paper-I/
│   ├── paper-I.tex
│   ├── sections/
│   ├── appendices/
│   └── images/
│
├── paper-II/
│   ├── README.md
│   ├── paper-II.tex
│   ├── sections/
│   └── notes/
│
├── paper-III/
│   ├── README.md
│   ├── paper-III.tex
│   ├── sections/
│   └── notes/
│
├── paper-IV/
│   ├── README.md
│   ├── paper-IV.tex
│   ├── sections/
│   └── notes/
│
├── shared/
│   ├── styles/
│   ├── bibliography/
│   └── images/
│
├── notes/
│   ├── active/
│   └── archive/
│
└── restructure/
    ├── 00-authoritative-scope.md
    ├── 01-paper-series-architecture.md
    ├── 02-paper-I-outline.md
    ├── 03-theorem-dependency-graph.md
    ├── 04-current-to-target-map.md
    ├── 05-mathematical-status.md
    ├── 06-editorial-rules.md
    ├── 07-acceptance-checklist.md
    ├── 08-open-questions.md
    ├── migration-log.md
    ├── discussions/
    └── archive/
```

This structure is a target, not an instruction to rename every file immediately.

The audit must precede large-scale path changes.

---

## 5. Transitional structure

During restructuring, the repository may retain:

```text
aeg-paper.tex
sections/
notes/
images/
```

as active legacy paths.

In that case:

* `aeg-paper.tex` remains the Paper I entry point;
* new target section names may be introduced under `sections/foundations/`;
* migrated material may first be copied into `paper-II/`, `paper-III/`, and `paper-IV/`;
* the old source must remain until the new destination builds and has been reviewed.

No source should be deleted merely because a target directory has been created.

---

# Part III. Root-level files

## 6. `README.md`

### Current role

The current README presents AEG primarily as a connection among:

* arithmetic expressions;
* hyperbolic geometry;
* the flow equation;
* arithmetic torsion;
* the basic expression space.

It may use an earlier (\mathfrak E_0/\mathfrak E_1) naming scheme and does not yet reflect bilateral completion or the four-paper architecture.

### Migration state

```text
REWRITE
```

### Target role

The root README should describe:

* the repository as the source of the AEG paper series;
* Paper I as the active foundational manuscript;
* Papers II–IV as structured research drafts;
* the build commands;
* the authoritative restructuring documents;
* the distinction between active papers and exploratory notes.

### Required changes

* remove or update any inconsistent model numbering;
* avoid describing the current affine theory as the complete AEG theory;
* add the four-paper series map;
* link to `restructure/00-authoritative-scope.md`;
* retain DOI information only if it is still associated with the correct published version;
* distinguish the published or archived version from the current restructuring branch.

### Claim treatment

```text
WEAKEN and UPDATE
```

The README must not claim that all arithmetic expressions have been embedded into the developed geometry.

---

## 7. `aeg-paper.tex`

### Current role

Main Paper I entry point, including:

* title and author;
* abstract;
* theorem environments;
* section order;
* appendices;
* bibliography.

### Migration state

```text
REWRITE, then optionally MOVE to paper-I/paper-I.tex
```

### Target role

It must implement the chapter order in:

```text
restructure/02-paper-I-outline.md
```

### Required structural changes

Replace the current section sequence with:

```text
1. Introduction
2. Sequential Arithmetic Histories
3. Projective Semantics and the Affine Sector
4. Affine Cocycles and Relative Defects
5. Continuous Arithmetic Flow
6. The Basic Hyperbolic Expression Space
7. Zero Loci and Singular Expression Spaces
8. Global Torsion and the ACS
9. Contact Connection and Horizontal Curvature
10. Conclusions and Research Interfaces
```

### Required metadata fixes

* verify the author affiliation;
* verify title and subtitle;
* update keywords;
* fix the `example` theorem heading;
* remove duplicated package imports;
* normalize theorem environments;
* update abstract after all theorem migrations;
* update table-of-contents depth if necessary.

### Claim treatment

```text
REWRITE and REAUDIT
```

The current abstract must not be retained without revision.

---

## 8. `aeg-lemma.tex`

### Current role

Legacy or supplementary theorem source.

### Migration state

```text
HOLD pending audit
```

### Required audit

Determine:

* whether it is currently included by the build;
* which lemmas remain unique;
* whether any result duplicates current section proofs;
* whether its notation predates the current (\mathfrak E_0/\mathfrak E_1) scheme.

### Possible destinations

* Paper I appendices;
* `notes/archive/`;
* shared technical note;
* removal if entirely duplicated and mechanically obsolete.

No theorem may remain depended upon implicitly through an unused legacy file.

---

## 9. `aeg-paper.bib`

### Migration state

```text
KEEP and CLEAN
```

### Target role

Initially remain a shared bibliography.

### Required work

* identify unused entries;
* identify citations used only by later papers;
* do not remove entries before migrated papers have their bibliography;
* add primary references for:

  * projective transformations;
  * affine groups;
  * regular-value theorem;
  * Ehresmann-type proper submersion theorem, if cited;
  * contact geometry;
  * hyperbolic geometry.

### Prohibition

Do not use bibliography cleanup as an opportunity to broaden the literature review without relevance.

---

## 10. `build.sh`

### Migration state

```text
KEEP, then EXTEND
```

### Required behavior

During transition it must continue to build Paper I.

Later it may support:

```bash
./build.sh paper-I
./build.sh paper-II
./build.sh paper-III
./build.sh paper-IV
```

### Validation

Do not change the script until the current baseline build result is recorded in:

```text
restructure/audit-report.md
```

---

## 11. `Dockerfile`

### Migration state

```text
KEEP and VERIFY
```

### Required audit

* confirm it builds the current PDF;
* confirm paths remain valid after restructuring;
* verify figure and bibliography dependencies;
* avoid adding unrelated packages.

---

# Part IV. Current Paper I sections

## 12. `sections/sec01.tex`

### Current content

* evaluation histories rather than endpoint values;
* guiding question;
* historical placement;
* threadlike expressions;
* arithmetic torsion;
* flow equation;
* AES;
* ACS;
* contact structure;
* (\delta)-calculus;
* arithmetic holomorphicity;
* list of contributions;
* paper organization.

### Migration state

```text
REWRITE
```

### Target destinations

| Current component                        | Target                        |
| ---------------------------------------- | ----------------------------- |
| Endpoint value versus evaluation history | Paper I, Chapter 1            |
| Historical placement                     | Paper I, Chapter 1, shortened |
| Threadlike-expression introduction       | Paper I, Chapter 2, replaced  |
| Torsion motivation                       | Paper I, Chapters 1 and 4     |
| Flow overview                            | Paper I, Chapter 5            |
| AES overview                             | Paper I, Chapters 6–7         |
| ACS overview                             | Paper I, Chapter 8            |
| Contact overview                         | Paper I, Chapter 9            |
| Arithmetic holomorphicity overview       | MOVE to Paper II              |
| Current contribution list                | Replace                       |
| Current structure paragraph              | Replace                       |

### Required changes

* introduce bilateral/projective placement;
* replace “threadlike expression” with marked spinal history;
* remove the claim that the paper establishes the beginnings of a function theory as a main contribution;
* add the regular/singular zero boundary;
* distinguish exact finite torsion and infinitesimal curvature;
* add explicit scope interfaces to Papers II–IV.

### Claim treatment

```text
PRESERVE core motivation
REWRITE architecture
MOVE analytic claims
```

---

## 13. `sections/sec02-00.tex`

### Current content

* arithmetic expression grammar;
* evaluation;
* evaluation orders;
* tree examples;
* threadlike-expression definition;
* currying;
* path notation;
* mesh grid;
* encoding histories as paths;
* canonical-path examples.

### Migration state

```text
SPLIT and REWRITE
```

### Target mapping

#### Paper I, Chapter 2

Retain and rewrite:

* expression trees;
* ordinary evaluation;
* legal evaluation orders;
* examples of branching versus sequential trees;
* path composition;
* bounded and free histories.

Replace:

* current threadlike definition;
* ambiguous left/right terminology;
* any statement that unique evaluation order follows from the current child condition without proof.

Add:

* dependency poset;
* sequential-tree classification;
* marked seed;
* slot-(1)/slot-(2) contexts;
* chirality word.

#### Paper I, Chapter 6

Move or retain selected geometric examples:

* arithmetic grid;
* expression path drawn in (\mathfrak E_0);
* canonical pair illustrations.

These examples should appear only after the hyperbolic model is constructed.

#### Appendix E

Move examples distinguishing:

* same endpoint;
* different history;
* different canonical rearrangements.

### Material requiring caution

The current path examples may mix:

* syntax;
* algebraic rewriting;
* geometric path;
* semantic equality.

Each example must be relabeled by equality level.

### Claim treatment

```text
REWRITE definitions
PRESERVE elementary examples after reclassification
```

---

## 14. `sections/sec02-01.tex`

### Current content

* alternating histories;
* accumulated multiplicative parameters;
* perturbation propagation;
* arithmetic torsion;
* affine group representation;
* levels of equality;
* early neutrality discussion.

### Migration state

```text
SPLIT
```

### Target mapping

#### Paper I, Chapter 4

Move and rewrite:

* alternating affine histories;
* accumulated scale;
* exact evaluation formula;
* perturbation propagation;
* affine matrix representation;
* elementary torsion.

Reorganize around:

[
f_i(x)=s_ix+t_i,
\qquad
\Phi_n,\xi_n,\widehat\xi_n.
]

The alternating formulas become a special case of the general affine cocycle.

#### Paper I, Chapter 2

Move:

* levels of equality;
* path/operator/value distinctions.

#### Appendix B

Move:

* extended index notation;
* detailed perturbation recursions;
* special alternating examples.

#### Appendix E or future relation theory

Move:

* neutrality taxonomy;
* closed-word discussion.

#### Paper IV

Move full discussion of:

* free-group shadow;
* relation quotient;
* condensation consequences.

### Required changes

* do not define torsion solely by path reversal;
* distinguish common scale from common total charge;
* state chronological composition convention;
* avoid conflating symbolic free histories with their evaluated affine group.

### Claim treatment

```text
PRESERVE affine formulas after rederivation
GENERALIZE torsion
MOVE relation theory
```

---

## 15. `sections/sec03.tex`

### Current content

* derivation of flow equation;
* affine matrix Lie algebra;
* discrete generating directions;
* contour-gradient form;
* rectifying coordinate;
* arithmetic coordinates;
* local area formula;
* coordinate-free eikonal form;
* metric rectification.

### Migration state

```text
SPLIT and REWRITE
```

### Target mapping

#### Paper I, Chapter 5

Retain:

* affine Lie algebra derivation;
* continuous flow equation;
* Pfaffian form;
* directional solutions;
* additive and multiplicative axes;
* eikonal form;
* local torsion asymptotics.

The Lie-theoretic derivation should become primary.

#### Paper I, Chapter 4

Move:

* affine matrix evolution;
* twisted translation law;
* relation to affine cocycle.

#### Appendix C

Move:

* long contour-angle derivations;
* detailed integration of the rectifying coordinate;
* coordinate transformations not used in later theorems.

#### Paper II

Move or duplicate only by citation:

* analytic use of the rectifying coordinate;
* second-order or operator interpretations.

### Required changes

* explicitly state left/right multiplication convention;
* distinguish exact formulas from expansions;
* do not call the eikonal equation coordinate-free before specifying the metric;
* distinguish (\mu,\lambda) assumptions;
* add Riccati completion remark.

### Claim treatment

```text
REPROVE under fixed conventions
```

---

## 16. `sections/sec04.tex`

### Current content

* normalized upper-half-plane model;
* general ((\mu,\lambda))-model;
* flow verification;
* Laplace eigenfunction;
* horocyclic coordinates;
* grid actions;
* Baumslag–Solitar relation;
* torsion and area;
* isolated-zero (\mathfrak E_1);
* early parameter-family/tube remark.

### Migration state

```text
SPLIT and REWRITE
```

### Target mapping

#### Paper I, Chapter 6

Retain and strengthen:

* upper-half-plane model;
* metric;
* assignment (a=-x/y);
* gradient verification;
* horocyclic geometry;
* grid actions;
* optional Baumslag–Solitar relation;
* optional Laplace eigenfunction;
* local torsion-area examples.

Add:

* derivation from the affine group and invariant metric;
* explicit curvature normalization;
* clear definition of (\mathfrak E_0).

#### Paper I, Chapter 7

Move and reclassify:

* isolated-center model;
* regular versus singular zero comparison.

The isolated center must be described as a singular zero or excluded point, according to the actual model.

#### Paper III

Move:

* general parameter-family tube speculation;
* higher (E_k) and zero-locus program;
* topology-change expectations.

### Required corrections

* verify (\mathfrak E_0/\mathfrak E_1) naming throughout;
* check the Baumslag–Solitar action order;
* compute the Laplacian for the actual normalized metric;
* avoid uniqueness claims;
* avoid calling an isolated zero regular.

### Claim treatment

```text
PRESERVE basic model
REPROVE normalization-dependent formulas
RECLASSIFY isolated zero
MOVE tube program
```

---

## 17. `sections/sec05.tex`

### Current content

* ACS definition;
* path and reverse path;
* evaluation formula using future multiplicative charge;
* global torsion;
* four-step example;
* triple identity;
* abelianization interpretation.

### Migration state

```text
REWRITE
```

### Target destination

Paper I, Chapter 8.

### Required restructuring

Replace the privileged comparison:

[
\gamma\quad\text{versus}\quad\bar\gamma
]

with a general comparison of compatible histories:

[
\gamma,\delta.
]

Distinguish:

* scale compatibility:
  [
  M_\gamma=M_\delta;
  ]
* charge compatibility:
  [
  (A_\gamma,M_\gamma)=(A_\delta,M_\delta).
  ]

Derive evaluation from the affine cocycle:

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
]

Then derive:

* relative endpoint independence;
* contour formula;
* weighted Stokes formula.

### Material retained as examples

* current four-step example;
* path-versus-reversal as a special case;
* monotone positive-charge region.

### Material moved to Paper IV

* full quotient interpretation;
* condensation;
* process-result information loss;
* groupoid-level meaning.

### Required corrections

* fix orientation and sign convention;
* use (2)-chains for signed or self-intersecting paths;
* do not call every pair of paths a simple enclosed region;
* avoid identifying the symbolic history group with the evaluated affine group.

### Claim treatment

```text
GENERALIZE and REPROVE
```

---

## 18. `sections/sec06.tex`

### Current content

* contact form;
* nondegeneracy;
* Darboux coordinates;
* Reeb field;
* horizontal lifts;
* Legendrian flow;
* curvature bracket;
* finite commutator;
* closed-loop holonomy;
* boundary integral;
* Lie algebra remark.

### Migration state

```text
KEEP core, REWRITE organization
```

### Target destination

Paper I, Chapter 9 and Appendix D.

### Main-text content

Retain:

* contact form;
* contact nondegeneracy;
* horizontal distribution;
* horizontal lifts;
* Legendrian realization of affine flow;
* curvature bracket;
* concise finite defect comparison.

### Appendix D content

Move:

* detailed Darboux coordinate conversion;
* Reeb-field computation, unless used later;
* long finite commutator calculation;
* detailed Stokes surface calculation;
* solvable Lie algebra decomposition.

### Required changes

* call the structure a contact connection or arithmetic contact model without implying a novel contact-isomorphism class;
* distinguish:

  * open two-path defect;
  * closed commutator holonomy;
  * infinitesimal curvature;
* ensure signs match Chapter 8;
* do not use contact geometry to claim a canonical complex structure.

### Claim treatment

```text
PRESERVE and CLARIFY
```

---

## 19. `sections/sec07.tex`

### Current content

* definition of (\delta);
* equivalent horizontal formulas;
* chain rules;
* elementary examples;
* curvature package;
* connection viewpoint;
* natural units;
* affine–Appell basis;
* antidifferentiation.

### Migration state

```text
SPLIT
```

### Target mapping

#### Paper I, Chapter 9

Retain only:

* horizontal covariant differential;
* formula:
  [
  \delta_HF=dF-(\partial_aF)\alpha;
  ]
* horizontal derivatives;
* curvature:
  [
  \delta_H^2F
  ===========

  \mu\lambda(\partial_aF),du\wedge dv;
  ]
* connection interpretation.

#### Appendix D

Move:

* selected coordinate checks;
* elementary chain-rule examples needed for verification.

#### Paper II

Move:

* extensive differentiation tables;
* affine–Appell basis;
* operator-stable function classes;
* antidifferentiation;
* analytic use of natural units.

### Required terminology change

Prefer:

```text
horizontal covariant differential
```

or:

```text
horizontal differential
```

over an unqualified “differential calculus.”

If the notation (\delta) is retained, explicitly state that it is generally not nilpotent.

### Claim treatment

```text
PRESERVE curvature core
MOVE analytic machinery
```

---

## 20. `sections/sec08.tex`

### Current content

* arithmetic Cauchy–Riemann equations;
* (\partial_{\mathrm{AEG}}) and (\bar\partial_{\mathrm{AEG}});
* horizontal conformality;
* arithmetic holomorphic coordinate;
* composition;
* rigidity;
* factorization;
* twisted harmonicity;
* affine–Appell basis.

### Migration state

```text
MOVE to Paper II
```

### Target destination

Suggested:

```text
paper-II/sections/
├── 01-analytic-data.tex
├── 02-horizontal-operators.tex
├── 05-arithmetic-holomorphicity.tex
└── 06-explicit-families.tex
```

### Paper I retention

Paper I may retain one closing remark:

> A compatible horizontal metric and almost-complex structure support Cauchy–Riemann-type operators, developed in Paper II.

No full theorem from current `sec08.tex` should remain in Paper I.

### Required corrections before reuse

* fix `u` versus `\nu` in the arithmetic coordinate;
* explicitly define the chosen horizontal metric and complex structure;
* verify factorization signs;
* define analytic domains and function spaces;
* distinguish formal operator identities from functional-analytic results.

### Claim treatment

```text
RECLASSIFY as Paper II prototype
REPROVE after analytic data are fixed
```

---

## 21. `sections/sec09.tex`

### Current content

* summary of current paper;
* path-to-relation outlook;
* neutrality classes;
* analytic future;
* singular backgrounds;
* higher structures;
* future research goals.

### Migration state

```text
REWRITE and SPLIT
```

### Target mapping

#### Paper I, Chapter 10

Retain only:

* summary of proved foundations;
* interface to Paper II;
* interface to Paper III;
* interface to Paper IV;
* concise open foundational problems.

#### Paper II

Move:

* analytic program;
* kernels;
* boundary values;
* explicit analytic families.

#### Paper III

Move:

* singular backgrounds;
* higher zero structures;
* tubes;
* topology and monodromy.

#### Paper IV or future relation paper

Move:

* full loop and neutrality theory;
* relation-theoretic condensation.

### Required changes

Replace the current chain ending in arithmetic holomorphicity with:

[
\text{history}
\to
\text{projective placement}
\to
\text{affine flow}
\to
\text{torsion/contact curvature}.
]

### Claim treatment

```text
REWRITE
```

---

## 22. `sections/sec10.tex`

### Current role

Supplementary model and ACS calculations.

### Migration state

```text
SPLIT and APPENDIX
```

### Target mapping

* hyperbolic-model calculations → Appendix C;
* ACS calculations → Appendix D or Chapter 8 examples;
* obsolete naming or duplicated calculations → archive after comparison.

### Audit requirements

* check all parameter normalizations;
* check signs against the new ACS convention;
* identify formulas used by later papers.

---

## 23. `sections/sec11.tex`

### Current role

Supplementary contact, (\delta), and holomorphic calculations.

### Migration state

```text
SPLIT
```

### Target mapping

* contact calculations → Paper I, Appendix D;
* horizontal differential curvature → Paper I, Appendix D;
* holomorphic calculations → Paper II;
* extended analytic examples → Paper II notes or appendices.

### Prohibition

Do not leave Paper II analytic results hidden in a Paper I appendix.

---

## 24. `sections/sec12.tex`

### Current role

Examples involving equality levels and neutralities.

### Migration state

```text
APPENDIX and SPLIT
```

### Target mapping

#### Paper I, Appendix E

Retain examples needed to distinguish:

* same endpoint versus same operator;
* same charge versus same history;
* zero endpoint defect versus trivial history.

#### Future relation theory or Paper IV

Move examples whose main purpose is:

* closed-word classification;
* canonical quotient;
* condensation;
* neutrality hierarchy beyond Paper I needs.

### Claim treatment

```text
PRESERVE examples after reclassification
```

---

# Part V. Bilateral and projective notes

## 25. `notes/bilateral_projective_condensation.tex`

### Current content

* marked spinal histories;
* sequential-tree theorem;
* mirror versus reversal;
* bilateral recursion;
* projective semantics;
* (PGL_2) generation;
* affine/Borel sector;
* Bruhat placement;
* history before quotient;
* relative projective defect;
* affine Maurer–Cartan formulas;
* Riccati flow;
* bivaluation;
* rank-one projectors;
* quotient tower;
* process-result bundle;
* finite-field models;
* connection and holonomy proposals.

### Migration state

```text
SPLIT
```

### Paper I destinations

#### Chapter 2

Move and normalize:

* marked spinal-history definition;
* sequential-tree classification;
* marked-seed explanation;
* mirror versus temporal reversal;
* associativity-as-(2)-cell remark only if concise.

#### Chapter 3

Move:

* projective context table;
* projective evaluation;
* (PGL_2) generation theorem;
* affine/Borel corollary;
* positive real qualification;
* short Bruhat remark;
* Riccati placement.

#### Chapter 4

Move:

* affine future/past cocycle formulas;
* left/right Maurer–Cartan formulas;
* affine relative defect.

### Paper IV destinations

Move:

* history groupoid;
* evaluation functor;
* group-valued projective defect;
* bivaluation;
* point–predicate duality;
* rank-one projector theorem;
* quotient tower;
* principal (H)-bundle;
* process-result residue;
* finite-field counting;
* projective condensation;
* holonomy proposals.

### Archive or open-problem destinations

* telescoping obstruction;
* incomplete contextual transport ansatz;
* semantic concept/predicate interpretation not yet formalized.

### Required precautions

* Paper I must not inherit speculative semantic claims;
* projective continuation must retain ordinary-domain warnings;
* PGL theorem must be checked in all claimed characteristics;
* operand-slot chirality must not be identified with dual transport;
* `PGL_2` notation and matrix action convention must be unified.

### Claim treatment

```text
PRESERVE proved algebraic core
MOVE full quotient theory to Paper IV
OPEN geometric bridges
```

---

# Part VI. Analysis notes

## 26. Current analysis and (\delta)-calculus notes

This category includes notes whose main content concerns:

* arithmetic holomorphicity;
* twisted harmonicity;
* horizontal operators;
* affine–Appell bases;
* hyperbolic real function theory;
* kernels and boundary problems.

### Migration state

```text
MOVE to Paper II
```

### Target organization

```text
paper-II/
├── README.md
├── paper-II.tex
├── sections/
│   ├── 01-analytic-data.tex
│   ├── 02-horizontal-operators.tex
│   ├── 03-hyperbolic-real-analysis.tex
│   ├── 04-boundary-problems.tex
│   ├── 05-arithmetic-holomorphicity.tex
│   └── 06-explicit-families.tex
└── notes/
```

### Paper I retention

Only foundational operator identities remain in Paper I.

### Audit rule

Every analytic note must be checked for whether it assumes:

* a horizontal metric;
* a measure;
* a complex structure;
* operator domains;
* completeness;
* boundary regularity.

Unstated assumptions must be added before theorem status is assigned.

---

# Part VII. Multi-zero, singularity, and tube notes

## 27. Multi-zero construction notes

This category includes notes on:

* (E_k);
* (E_{\log});
* multiple zero lines;
* conformal uniqueness;
* zero-line classifications;
* analytic constructions.

### Migration state

```text
MOVE to Paper III, with one possible minimal example retained in Paper I
```

### Paper I eligibility test

A multi-zero model may remain in Paper I only if all are complete:

```text
[ ] domain
[ ] metric
[ ] assignment function
[ ] singular set
[ ] flow verification
[ ] zero topology
```

Otherwise it is moved entirely to Paper III.

### Paper III target organization

```text
paper-III/sections/
├── 01-singular-aes.tex
├── 02-local-zero-models.tex
├── 03-multi-zero-constructions.tex
├── 04-parameter-discriminants.tex
├── 05-regular-tubes.tex
├── 06-singular-fibers.tex
├── 07-monodromy-and-braids.tex
└── 08-threading-and-knot-questions.tex
```

### Claim treatment

* existence formulas → `REPROVE`;
* uniqueness claims → `HOLD` unless proved;
* visual zero counts → `COMPUTATIONAL EXAMPLE` until analytic verification;
* general (E_k) classification → `OPEN` unless completed.

---

## 28. Tube notes

This category includes:

* parameterized zero sets;
* tube construction;
* threading;
* zero-line transport;
* topology change;
* knot-like pictures.

### Migration state

```text
MOVE to Paper III
```

### Paper I retention

Only the general construction:

[
\mathcal Z
==========

{(p,t):a_t(p)=0}
]

and a regular-value lemma may remain.

### Required reclassification

Distinguish:

1. total zero set;
2. smooth zero surface;
3. locally trivial tube;
4. embedded tube;
5. threaded tube;
6. braid closure;
7. knot invariant.

These are not synonymous.

### Claims requiring proof before main-theorem status

* properness;
* local triviality;
* isotopy invariance;
* braid representation;
* Markov invariance;
* new knot invariant;
* independence from Alexander/Burau data.

---

## 29. Knot-related notes

Known categories include notes on:

* knot constructions;
* tube threading;
* Alexander/Burau comparison;
* Markov normalization;
* potential new invariants.

### Migration state

```text
MOVE to Paper III notes; HOLD from main paper
```

### Entry condition for Paper III main text

At least one of:

* isotopy invariance;
* braid-monodromy theorem;
* Markov invariance;
* nontrivial comparison theorem;
* rigorously defined invariant.

Without this, retain as:

* example;
* proposal;
* conjecture;
* open problem.

---

# Part VIII. Complexity and resource-geometry notes

## 30. `notes/rg_en.tex`

### Current role

English resource-geometry material, potentially including:

* computational resources;
* geometric interpretations;
* time-space relations;
* pebble-game ideas.

### Migration state

```text
MOVE to Paper IV
```

### Target destination

Suggested:

```text
paper-IV/sections/
├── 06-representation-growth.tex
├── 07-cost-models.tex
└── 08-time-space-relations.tex
```

### Claim treatment

All statements connecting geometry to complexity must be reclassified according to explicit cost models.

No Paper I theorem may depend on this note.

---

## 31. `notes/rg_zh.tex`

### Migration state

```text
MOVE to Paper IV notes or archive as Chinese source
```

### Required treatment

* compare with `rg_en.tex`;
* identify unique content;
* retain provenance;
* avoid maintaining two divergent theorem versions.

The English paper source should have one canonical mathematical formulation.

---

## 32. Resource geometry and computational spacetime notes

This category includes notes on:

* Turing machines;
* pebble games;
* computational spacetime duality;
* torsion and rewriting surfaces;
* de Rham pairing;
* algorithmic thermodynamics;
* canonical forms as computational mass;
* time-space complexity relations.

### Migration state

```text
MOVE to Paper IV
```

### Paper IV classification

| Topic                         | Target chapter                  |
| ----------------------------- | ------------------------------- |
| History and rewriting graph   | History categories              |
| Canonical forms and quotients | Condensation                    |
| Word-ball growth              | Representation growth           |
| Pebble games                  | Time-space cost models          |
| Computational spacetime       | Research synthesis              |
| Algorithmic thermodynamics    | Motivation or conditional model |
| Computational mass/curvature  | Proposal unless formalized      |

### Prohibited migration to Paper I

Do not use these notes to justify:

* hyperbolicity of AES;
* uniqueness of the metric;
* complexity lower bounds;
* physical analogies as mathematical consequences.

---

## 33. `notes/note_06.tex`

### Current content

* projective compatibility of (a=-x/y);
* hyperbolic geometry and combinatorial complexity;
* compactification;
* projective boundary;
* projective/hyperbolic interplay.

### Migration state

```text
SPLIT
```

### Paper I use

Retain only as conceptual support for:

* projective placement;
* homogeneous degree-zero assignment;
* projective boundary motivation.

Any claim used in Paper I must be rederived independently.

### Paper IV use

Move:

* projective compactification;
* history-to-boundary interpretations;
* quotient and condensation connections.

### Claim treatment

Statements such as:

> combinatorial complexity makes hyperbolicity unavoidable

must be:

```text
REJECT as theorem
RETAIN as research motivation only
```

---

## 34. `notes/note_09.tex`

### Current content

* (F_2) as source of complexity;
* canonical forms;
* condensation;
* space emerging from time;
* computational energy and mass;
* group quotient examples;
* torsion of commutator;
* curvature analogies.

### Migration state

```text
MOVE to Paper IV and ARCHIVE original
```

### Paper IV destinations

* condensation chapter;
* canonical-form discussion;
* quotient-space examples;
* complexity-metric motivation.

### Claim treatment

| Claim                                       | Treatment                          |
| ------------------------------------------- | ---------------------------------- |
| Quotient by relations as condensation model | Structural proposal                |
| (F_2) as universal source of complexity     | Weaken/open                        |
| Complexity as path length                   | Conditional on metric and model    |
| Computational mass induces curvature        | Analogy/open                       |
| Group growth gives algorithmic lower bound  | Reject without proof               |
| Commutator torsion formula                  | Recompute under current convention |

### Paper I use

None, except possibly a short historical note on ACS as a charge shadow.

---

# Part IX. Loop and relation notes

## 35. `notes/loop_02.tex`

### Current role

Arithmetic loops, zero taxonomy, or neutrality classes.

### Migration state

```text
SPLIT and HOLD
```

### Paper I destination

Only minimal examples needed for Appendix E:

* same endpoint but nontrivial history;
* different neutrality levels.

### Later destination

A future relation-theory paper or Paper IV, depending on whether the focus is:

* algebraic loop relations;
* quotient and condensation;
* semantic neutrality.

### Prohibition

Paper I must not develop a full loop theory.

---

## 36. Other `notes/note_*.tex`

### Migration state

```text
HOLD pending semantic audit
```

### Required audit procedure

For every note:

1. identify its primary topic;
2. identify whether it contains a unique theorem;
3. assign Paper I, II, III, IV, future paper, or archive;
4. assign mathematical status;
5. record dependencies;
6. record whether any current main-text claim cites it implicitly.

### Default routing rules

| Content                   | Destination   |
| ------------------------- | ------------- |
| Sequential syntax         | Paper I       |
| Affine/projective algebra | Paper I or IV |
| Hyperbolic model          | Paper I       |
| Function theory           | Paper II      |
| Multi-zero/singularity    | Paper III     |
| Tube/knot                 | Paper III     |
| Condensation/complexity   | Paper IV      |
| Superseded brainstorming  | Archive       |

No `note_*.tex` file should be bulk-deleted.

---

# Part X. Figures and assets

## 37. `images/`

### Migration state

```text
AUDIT, then KEEP/MOVE/ARCHIVE per figure
```

### Required figure inventory

For each figure record:

* filename;
* source format;
* current caption;
* current section;
* target paper;
* whether the mathematics is still valid;
* whether it depends on superseded notation;
* whether it is reproducible.

### Paper I figure classes

Retain or redesign:

1. expression tree;
2. sequential versus branching tree;
3. marked slot-(1)/slot-(2) histories;
4. projective versus affine sector schematic;
5. hyperbolic arithmetic grid;
6. regular versus singular zero set;
7. two-history ACS filling;
8. contact commutator square.

### Paper II figures

Move:

* operator plots;
* analytic solution families;
* holomorphic-coordinate visualizations;
* boundary kernels.

### Paper III figures

Move:

* multi-zero plots;
* tube surfaces;
* threading;
* knot and braid diagrams.

### Paper IV figures

Move:

* quotient towers;
* condensation diagrams;
* resource graphs;
* complexity growth diagrams.

### Prohibition

A figure must not remain in Paper I if its only purpose is to advertise a later-paper theory.

---

# Part XI. Historical and generated material

## 38. `gpt/`

### Current role

Generated discussions, meeting minutes, prompts, and exploratory drafts.

### Migration state

```text
ARCHIVE
```

### Target

```text
restructure/archive/generated-discussions/
```

or retain in place with an archival header.

### Required header

Each retained file should be understood as:

```text
STATUS: archival discussion, not authoritative.
```

### Use policy

Material may be mined for:

* examples;
* bibliographic leads;
* forgotten proof ideas;
* provenance.

It must not override authoritative restructuring documents.

---

## 39. `plans/`

### Migration state

```text
ARCHIVE or SPLIT
```

### Required treatment

* active restructuring plans → `restructure/`;
* historical study plans → archive;
* unresolved research programs → corresponding Paper II–IV `README.md`.

---

## 40. Interactive HTML or laboratory files

Examples include resource-geometry labs or visualization prototypes.

### Migration state

```text
MOVE to experiments/ or Paper IV supplements
```

### Policy

Interactive demonstrations are not paper proofs.

They may support:

* examples;
* reproducibility;
* computational verification.

Their mathematical claims must be restated and proved separately.

---

# Part XII. New target files to create

## 41. Paper I new section files

Recommended creation:

```text
sections/foundations/
├── 01-introduction.tex
├── 02-sequential-histories.tex
├── 03-projective-affine.tex
├── 04-affine-cocycles.tex
├── 05-affine-flow.tex
├── 06-hyperbolic-model.tex
├── 07-zero-geometry.tex
├── 08-acs-torsion.tex
├── 09-contact-curvature.tex
└── 10-conclusion.tex
```

These files should initially coexist with legacy `sec*.tex` files.

The legacy files must not be deleted until:

* all retained content has been mapped;
* the new section builds;
* migration has been logged;
* human review is complete.

---

## 42. Paper I appendices

Create as needed:

```text
sections/foundations/appendices/
├── app-A-conventions.tex
├── app-B-affine-cocycles.tex
├── app-C-hyperbolic-calculations.tex
├── app-D-acs-contact.tex
└── app-E-equality-neutrality.tex
```

---

## 43. Later-paper entry files

Create lightweight entry points:

```text
paper-II/README.md
paper-III/README.md
paper-IV/README.md
```

Each README must include:

* provisional title;
* authoritative scope reference;
* imported Paper I nodes;
* migrated source inventory;
* claim-status warning;
* completion criteria.

Do not create polished abstracts for Papers II–IV before their theorem sets stabilize.

---

# Part XIII. File-by-file migration table

## 44. Summary table

| Current path                                  | Primary state  | Canonical target                           |
| --------------------------------------------- | -------------- | ------------------------------------------ |
| `README.md`                                   | REWRITE        | Root series README                         |
| `aeg-paper.tex`                               | REWRITE        | Paper I entry point                        |
| `aeg-lemma.tex`                               | HOLD           | Audit, appendix, or archive                |
| `aeg-paper.bib`                               | KEEP/CLEAN     | Shared bibliography                        |
| `build.sh`                                    | KEEP/EXTEND    | Multi-paper build                          |
| `Dockerfile`                                  | KEEP/VERIFY    | Reproducible build                         |
| `sections/sec01.tex`                          | REWRITE        | Paper I Chapter 1                          |
| `sections/sec02-00.tex`                       | SPLIT/REWRITE  | Paper I Chapters 2 and 6                   |
| `sections/sec02-01.tex`                       | SPLIT          | Paper I Chapters 2 and 4; Paper IV         |
| `sections/sec03.tex`                          | SPLIT/REWRITE  | Paper I Chapters 4 and 5                   |
| `sections/sec04.tex`                          | SPLIT/REWRITE  | Paper I Chapters 6 and 7; Paper III        |
| `sections/sec05.tex`                          | REWRITE        | Paper I Chapter 8                          |
| `sections/sec06.tex`                          | KEEP/REWRITE   | Paper I Chapter 9                          |
| `sections/sec07.tex`                          | SPLIT          | Paper I Chapter 9; Paper II                |
| `sections/sec08.tex`                          | MOVE           | Paper II                                   |
| `sections/sec09.tex`                          | REWRITE/SPLIT  | Paper I Chapter 10; Papers II–IV           |
| `sections/sec10.tex`                          | SPLIT/APPENDIX | Paper I Appendices C–D                     |
| `sections/sec11.tex`                          | SPLIT          | Paper I Appendix D; Paper II               |
| `sections/sec12.tex`                          | SPLIT/APPENDIX | Paper I Appendix E; future relation theory |
| `notes/bilateral_projective_condensation.tex` | SPLIT          | Paper I Chapters 2–4; Paper IV             |
| `notes/rg_en.tex`                             | MOVE           | Paper IV                                   |
| `notes/rg_zh.tex`                             | MOVE/ARCHIVE   | Paper IV notes                             |
| `notes/note_06.tex`                           | SPLIT          | Paper I motivation; Paper IV               |
| `notes/note_09.tex`                           | MOVE/ARCHIVE   | Paper IV                                   |
| `notes/loop_02.tex`                           | SPLIT/HOLD     | Paper I Appendix E; future relation theory |
| multi-zero notes                              | MOVE           | Paper III                                  |
| tube notes                                    | MOVE           | Paper III                                  |
| knot notes                                    | MOVE/HOLD      | Paper III notes                            |
| analysis notes                                | MOVE           | Paper II                                   |
| complexity/resource notes                     | MOVE           | Paper IV                                   |
| `gpt/`                                        | ARCHIVE        | Generated-discussion archive               |
| `plans/`                                      | ARCHIVE/SPLIT  | Restructure or paper READMEs               |
| `images/`                                     | AUDIT          | Papers I–IV by figure role                 |

---

# Part XIV. Migration logging

## 45. Required migration log

Create:

```text
restructure/migration-log.md
```

Every substantive move must add an entry:

```markdown
## Migration M-XXXX

- Date:
- Source:
- Source section or line range:
- Destination:
- Migration state:
- Claim treatment:
- Theorem nodes affected:
- Notation changes:
- Content retained in source:
- Content removed from source:
- Build result:
- Reviewer notes:
```

---

## 46. Content-preservation rule

Before removing text from an active source, verify that one of the following is true:

1. it exists in the canonical destination;
2. it is preserved in an archive;
3. it is recorded as demonstrably duplicated;
4. it is recorded as rejected and the reason is stated.

“No longer in Paper I” is not sufficient justification for deletion.

---

## 47. Duplicate-source rule

During transition, temporary duplication is permitted.

Every duplicate block must contain or be accompanied by a migration note identifying:

* canonical version;
* temporary version;
* planned deletion point.

After review, only one canonical active version may remain.

---

# Part XV. Codex execution boundaries

## 48. Audit task permissions

For the initial audit, Codex may:

* read all repository files;
* run the build;
* create `restructure/audit-report.md`;
* create a source inventory.

It must not:

* rewrite the paper;
* move files;
* rename models;
* repair proofs silently;
* delete material.

---

## 49. Skeleton task permissions

For the skeleton phase, Codex may:

* create target section files;
* update the Paper I entry point;
* add placeholder introductions;
* preserve legacy sections in temporary includes.

It must not:

* delete legacy files;
* alter theorem claims substantially;
* migrate Paper II–IV material destructively.

---

## 50. Chapter migration permissions

Each chapter migration task must specify:

```text
Allowed source files
Allowed target files
Forbidden files
Theorem nodes in scope
Claim statuses allowed to change
Required build checks
```

A task may not infer permission from this map to rewrite unrelated files.

---

# Part XVI. Known high-risk migrations

## 51. Threadlike-expression migration

### Risk

The existing child-orientation definition appears inconsistent with examples.

### Required action

* do not patch one word without auditing all examples;
* replace with dependency-poset and marked-spine definitions;
* preserve old terminology only as historical commentary if necessary.

### Affected nodes

```text
S1, S2, T1, S3, S4
```

---

## 52. (\mathfrak E_0/\mathfrak E_1) migration

### Risk

Model numbering has changed across repository versions.

### Required action

Create a model-name audit table before global replacement:

| Formula/domain | Historical name | Target name | Status |
| -------------- | --------------- | ----------- | ------ |

Do not use blind search-and-replace.

---

## 53. ACS orientation migration

### Risk

The current formula uses a reversed history to encode future weighting; the target formula uses a direct cocycle integral.

### Required action

* prove equivalence;
* select one canonical orientation;
* recompute all examples;
* update every sign and caption;
* retain reversal as a special case.

### Affected nodes

```text
T3, G1, T9, T10, T11, T12, T17
```

---

## 54. Contact versus holomorphic migration

### Risk

The current narrative makes analytic structure appear intrinsic to contact geometry.

### Required action

* retain contact and horizontal curvature in Paper I;
* move complex-structure-dependent results to Paper II;
* state the additional analytic choices;
* prevent Paper I abstract and conclusion from claiming a completed function theory.

---

## 55. Isolated-zero migration

### Risk

The isolated-zero model may contradict the regular-zero theorem if presented as smooth and non-degenerate.

### Required action

Audit:

* domain;
* smoothness;
* metric;
* parameter behavior;
* equation domain.

Then classify it as:

* singular point;
* deleted point;
* degenerate parameter point;
* boundary artifact;
* invalid model.

Do not choose the classification editorially; establish it mathematically.

---

## 56. Tube migration

### Risk

“Total zero set,” “smooth tube,” and “knot” are currently too easily conflated.

### Required action

Paper I retains only the regular-value construction.

Paper III must separately prove:

* submersion;
* properness;
* local triviality;
* embedding;
* monodromy;
* knot invariance.

---

## 57. Complexity migration

### Risk

Conceptual analogies may be phrased as mathematical consequences.

### Required action

Move such material to Paper IV and label each claim by status.

No statement of the form:

[
\text{noncommutativity}
\Rightarrow
\text{computational hardness}
]

may remain in Paper I.

---

# Part XVII. Completion criteria

## 58. Paper I migration completeness

The current-to-target migration for Paper I is complete only when:

* [ ] every current `sec*.tex` file has a recorded disposition;
* [ ] all Paper I target chapters exist;
* [ ] all retained mathematical content has one canonical location;
* [ ] Paper II analytic material has been moved or clearly isolated;
* [ ] Paper III singular/tube material has been moved or clearly isolated;
* [ ] Paper IV quotient/complexity material has been moved or clearly isolated;
* [ ] no legacy section is still included accidentally;
* [ ] no theorem is lost during migration;
* [ ] model numbering is consistent;
* [ ] ACS signs are consistent;
* [ ] the Paper I PDF builds;
* [ ] abstract and conclusion match the migrated theorem set.

---

## 59. Repository-wide migration completeness

The repository-wide map is complete only when every substantive file is assigned one of:

```text
Paper I
Paper II
Paper III
Paper IV
future paper
shared support
active note
archive
remove
hold
```

No file may remain unclassified merely because its filename is opaque.

---

## 60. Final migration principle

The migration must transform the repository from a chronological accumulation of discoveries into a dependency-controlled paper series.

The governing rule is:

[
\boxed{
\text{preserve research provenance}
\quad+\quad
\text{choose one canonical mathematical location}
\quad+\quad
\text{state every unresolved claim honestly}.
}
]

Paper I should retain only what is necessary to establish:

[
\text{marked histories}
\to
PGL_2
\supset
\operatorname{Aff}(1)
\to
\text{flow}
\to
\mathfrak E_0
\to
\text{torsion and contact curvature},
]

together with the foundational boundary between regular and singular zero geometry.

Everything else must be migrated without being lost.
