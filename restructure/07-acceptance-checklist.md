# Paper I Acceptance Checklist

**File:** `restructure/07-acceptance-checklist.md`
**Status:** Authoritative
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

**Applies to:**
**Arithmetic Expression Geometry I: Foundations**

---

## 1. Purpose

This document defines the acceptance gates for the restructuring and completion of Paper I.

It is intended for:

* author review;
* collaborator review;
* Codex task validation;
* preprint preparation;
* mathematical audit;
* repository migration control.

A checked item means that the requirement has been verified against the actual source, proof, build output, or migration record.

An item must not be checked merely because the intended result appears in a planning document.

---

## 2. Acceptance levels

Paper I progresses through five acceptance levels.

### Level A — Repository baseline

The current repository is understood, builds reproducibly, and has a complete source inventory.

### Level B — Structural migration

The target chapter structure exists and all legacy material has a declared disposition.

### Level C — Mathematical closure

All critical definitions and theorem nodes are stable and proved under explicit hypotheses.

### Level D — Editorial closure

The exposition, notation, citations, figures, and paper boundaries are consistent.

### Level E — Release candidate

The complete manuscript builds cleanly, survives independent review, and makes no claim stronger than its proofs.

Paper I must pass each level in order.

---

# Part I. Level A — Repository baseline

## 3. Source inventory

* [ ] Every root-level source file has been inventoried.
* [ ] Every file under `sections/` has been inventoried.
* [ ] Every file under `notes/` has been classified by topic.
* [ ] Every file under `gpt/` has been classified as archival or active.
* [ ] Every file under `../archive/plans/` has been classified.
* [ ] Every figure and image asset has been inventoried.
* [ ] Every interactive or generated artifact has been inventoried.
* [ ] Every current build entry point has been identified.
* [ ] Every bibliography file has been identified.
* [ ] Every style and macro file has been identified.
* [ ] No opaque source file remains without a recorded role.

### Required evidence

The inventory must appear in:

```text
restructure/audit-report.md
```

or a linked source-inventory file.

---

## 4. Baseline build

* [ ] The unmodified baseline branch has been built.
* [ ] The exact build command has been recorded.
* [ ] The expected PDF has been produced.
* [ ] The baseline PDF filename has been recorded.
* [ ] The baseline page count has been recorded.
* [ ] All baseline build errors have been recorded.
* [ ] All undefined-reference warnings have been recorded.
* [ ] All missing-citation warnings have been recorded.
* [ ] All missing-figure warnings have been recorded.
* [ ] All duplicate-label warnings have been recorded.
* [ ] The Docker build path has been tested or its failure documented.
* [ ] The local build and Docker build use compatible source paths.

### Baseline commands

Primary:

```bash
./build.sh
```

Docker:

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

---

## 5. Baseline mathematical audit

* [ ] The current definition of threadlike expression has been located.
* [ ] The left-child/right-child inconsistency has been documented.
* [ ] All current uses of mirror, reversal, and inverse have been located.
* [ ] All current model names (\mathfrak E_0,\mathfrak E_1,E_k,E_{\log}) have been inventoried.
* [ ] All current definitions of torsion have been inventoried.
* [ ] All current ACS orientation conventions have been inventoried.
* [ ] All current left/right matrix-action conventions have been inventoried.
* [ ] All current uses of (\delta) have been inventoried.
* [ ] All current claims involving arithmetic holomorphicity have been inventoried.
* [ ] All current claims involving isolated or multiple zeros have been inventoried.
* [ ] All current claims involving tubes, braids, knots, or complexity have been inventoried.
* [ ] All known typographical problems, including (u/\nu), have been recorded.

---

## 6. Baseline acceptance gate

Level A is passed only when:

* [ ] the source inventory is complete;
* [ ] the baseline build result is reproducible;
* [ ] known mathematical conflicts are documented;
* [ ] no source modification has been used to conceal a baseline failure.

---

# Part II. Level B — Structural migration

## 7. Target chapter skeleton

The following Paper I chapters must exist as active source units:

* [ ] Introduction
* [ ] Sequential Arithmetic Histories
* [ ] Projective Semantics and the Affine Sector
* [ ] Affine Cocycles and Relative Defects
* [ ] Continuous Arithmetic Flow
* [ ] The Basic Hyperbolic Expression Space
* [ ] Zero Loci and Singular Expression Spaces
* [ ] Global Torsion and the ACS
* [ ] Contact Connection and Horizontal Curvature
* [ ] Conclusions and Research Interfaces

The active entry point must include them in this dependency order.

---

## 8. Appendix skeleton

The following appendix roles must exist or be explicitly waived:

* [ ] Composition and action conventions
* [ ] Affine-cocycle calculations
* [ ] Hyperbolic-model calculations
* [ ] ACS and contact calculations
* [ ] Equality and neutrality examples

A waived appendix must have its required material located elsewhere.

---

## 9. Legacy-section disposition

For every current section file:

* [ ] a canonical target has been assigned;
* [ ] a migration state has been assigned;
* [ ] a claim-treatment state has been assigned;
* [ ] retained material has one canonical active copy;
* [ ] moved material exists in its destination;
* [ ] archived material has an archival status header;
* [ ] rejected material has a recorded reason;
* [ ] no legacy section is accidentally included in the active Paper I build.

### Required files

The mapping must agree with:

```text
restructure/04-current-to-target-map.md
```

and every completed move must appear in:

```text
restructure/migration-log.md
```

---

## 10. Later-paper destinations

### Paper II

* [x] Arithmetic Cauchy–Riemann material has a canonical Paper II destination.
* [x] Twisted harmonicity has a canonical Paper II destination.
* [x] Affine–Appell calculations have a canonical Paper II destination.
* [x] Horizontal analytic operator material has a canonical Paper II destination.
* [x] Paper I retains only the foundational horizontal differential.

### Paper III

* [ ] Multi-zero constructions have a canonical Paper III destination.
* [ ] (E_k) material has a canonical Paper III destination.
* [ ] (E_{\log}) material has a canonical Paper III destination.
* [ ] Tube material has a canonical Paper III destination.
* [ ] Braid and knot material has a canonical Paper III notes destination.
* [ ] Paper I retains only the regular total-zero-set lemma and disciplined outlook.

### Paper IV

* [ ] Bivaluation material has a canonical Paper IV destination.
* [ ] Rank-one projector material has a canonical Paper IV destination.
* [ ] Quotient-tower material has a canonical Paper IV destination.
* [ ] Condensation material has a canonical Paper IV destination.
* [ ] Resource geometry and complexity material has a canonical Paper IV destination.
* [ ] Paper I retains only projective placement and affine foundations.

---

## 11. Provenance preservation

* [ ] No substantive note has been deleted without archival disposition.
* [ ] Every moved theorem retains its proof provenance.
* [ ] Every moved example retains its original source reference.
* [ ] Every migrated figure retains editable source or generation instructions.
* [ ] Every superseded definition remains recoverable from version history or archive.
* [ ] Temporary duplicate sources identify the canonical version.
* [ ] No unresolved TODO has been deleted without resolution or relocation.

---

## 12. Structural-build gate

After skeleton migration:

* [ ] Paper I builds.
* [ ] All active chapters appear in the table of contents.
* [ ] No later-paper chapter is accidentally included.
* [ ] All temporary placeholders are labeled.
* [ ] No placeholder is mistaken for a theorem or completed proof.
* [ ] Page and section ordering matches the target outline.

---

## 13. Structural acceptance gate

Level B is passed only when:

* [ ] every current source has a destination or hold status;
* [ ] the target Paper I skeleton builds;
* [ ] later-paper material is isolated without loss;
* [ ] no large-scale deletion remains unaudited.

---

# Part III. Level C — Mathematical closure

# A. Conventions

## 14. Chronological composition convention

* [ ] A single chronological convention is stated.
* [ ] History concatenation notation is defined.
* [ ] Function composition order is defined.
* [ ] Matrix multiplication order is defined.
* [ ] Every worked example agrees with the convention.
* [ ] The (PGL_2) decomposition has been checked under the convention.
* [ ] Affine cocycle formulas have been checked under the convention.
* [ ] Baumslag–Solitar formulas have been checked under the convention.
* [ ] ACS path orientation has been checked under the convention.
* [ ] Contact finite-commutator formulas have been checked under the convention.

---

## 15. Domain conventions

* [ ] Ordinary arithmetic evaluation is defined.
* [ ] Projective evaluation is defined separately.
* [ ] Division-by-zero exclusions are explicit.
* [ ] Projective poles are identified.
* [ ] Degenerate constant maps are excluded from (PGL_2) where necessary.
* [ ] Multiplication by zero is handled explicitly.
* [ ] Every theorem states whether it concerns ordinary or projective semantics.
* [ ] No projective formula is used to claim ordinary admissibility.

---

## 16. Differential-geometric standing assumptions

* [ ] The role of (\mu) is stated.
* [ ] The role of (\lambda) is stated.
* [ ] Each theorem states whether (\mu\neq0) is required.
* [ ] Each theorem states whether (\lambda\neq0) is required.
* [ ] Positivity assumptions are distinct from non-vanishing assumptions.
* [ ] Smoothness assumptions on (a) are explicit.
* [ ] Smoothness and non-degeneracy assumptions on (g) are explicit.
* [ ] Manifold boundary assumptions are explicit.
* [ ] Completeness is not assumed silently.
* [ ] Properness is not assumed silently.

---

# B. Sequential syntax

## 17. Arithmetic trees and dependency posets

* [ ] Arithmetic expression trees are defined.
* [ ] Internal vertices are defined.
* [ ] Legal evaluation orders are defined.
* [ ] The dependency partial order is defined.
* [ ] Legal evaluation orders are identified with linear extensions.
* [ ] Branching and sequential examples are included.

---

## 18. Sequential-tree classification

* [ ] The theorem statement matches T1.
* [ ] The finite-poset lemma is proved or cited precisely.
* [ ] Unique linear extension implies chain is proved.
* [ ] Chain implies unique linear extension is proved.
* [ ] Two internal children are shown to be incomparable.
* [ ] The one-internal-child condition is shown to produce a spine.
* [ ] The leaf-only case is handled.
* [ ] No ambiguous left/right-child condition remains as the canonical definition.

---

## 19. Marked spinal histories

* [ ] The marked accumulator is defined.
* [ ] Slot-(1) and slot-(2) contexts are defined.
* [ ] Chirality words are defined.
* [ ] Free histories are defined.
* [ ] Bounded histories are defined.
* [ ] History composition is defined.
* [ ] Admissibility is defined.
* [ ] The tree-to-history construction is proved.
* [ ] The inverse history-to-tree construction is proved if bijectivity is claimed.
* [ ] The term `threadlike expression` is removed, deprecated, or explicitly mapped to the new definition.

---

## 20. Mirror, reversal, and inverse

* [ ] Mirror is defined.
* [ ] Temporal reversal is defined.
* [ ] Path inverse is defined under invertibility.
* [ ] A worked example distinguishes mirror from reversal.
* [ ] No use of “reverse” remains ambiguous.
* [ ] Torsion is not described as a mirror invariant without proof.

---

# C. Projective and affine semantics

## 21. Elementary projective contexts

For each map below:

* [ ] (z\mapsto z+c)
* [ ] (z\mapsto z-c)
* [ ] (z\mapsto c-z)
* [ ] (z\mapsto cz)
* [ ] (z\mapsto z/c)
* [ ] (z\mapsto c/z)

verify:

* [ ] a correct projective matrix;
* [ ] non-degeneracy conditions;
* [ ] ordinary-domain conditions;
* [ ] projective behavior at (0) and (\infty);
* [ ] consistency with the matrix-action convention.

---

## 22. Projective evaluation map

* [ ] The history language in the domain is defined.
* [ ] The target is (PGL_2(K)).
* [ ] Composition compatibility is proved.
* [ ] Projective scalar equivalence is handled.
* [ ] Injectivity is not claimed.
* [ ] History equality is not identified with operator equality.

---

## 23. Bilateral generation theorem

* [ ] Translation generators are realized by arithmetic contexts.
* [ ] Nonzero scaling generators are realized.
* [ ] Inversion is realized.
* [ ] The (C=0) Möbius case is proved.
* [ ] The (C\neq0) decomposition is proved.
* [ ] All denominators are checked.
* [ ] Characteristic-(2) wording has been reviewed.
* [ ] The theorem states non-degeneracy assumptions.
* [ ] The result is generation of (PGL_2(K)), not of all projective endomorphisms.

---

## 24. Affine/Borel sector

* [ ] The stabilizer of (\infty) is identified.
* [ ] Its affine action is written explicitly.
* [ ] The relevant restricted history language is identified.
* [ ] The whole algebraic Borel is distinguished from the positive real component.
* [ ] Reflections and negative scales are handled explicitly.
* [ ] Current continuous AEG is described as an affine/Borel sector, not the full projective theory.

---

## 25. Riccati placement

* [ ] The projective vector-field basis is stated correctly.
* [ ] The Riccati equation is stated as projective placement.
* [ ] The affine slice (\kappa=0) is identified.
* [ ] No full projective geometry is claimed.
* [ ] The result is not used as a dependency for unproved Paper IV constructions.

---

# D. Affine cocycles

## 26. Target-frame cocycle

* [ ] The affine composition recursion is stated.
* [ ] (\Phi_n) is derived.
* [ ] (\xi_n) is derived.
* [ ] The induction proof uses the final convention.
* [ ] Empty-history and one-step cases are checked.
* [ ] The future-scaling interpretation matches the formula.

---

## 27. Source-normalized cocycle

* [ ] (\widehat\xi_n=\Phi_n^{-1}\xi_n) is defined.
* [ ] All scales are nonzero.
* [ ] The closed formula is proved.
* [ ] Past-normalization language matches the formula.
* [ ] (\xi) and (\widehat\xi) are never interchanged.

---

## 28. Maurer–Cartan formulas

* [ ] (g^{-1}dg) is computed.
* [ ] (dg,g^{-1}) is computed.
* [ ] Translation components are identified.
* [ ] Accumulated logarithmic scale is not confused with fixed intensity (\lambda).
* [ ] Source/body and target/spatial interpretations are stated.
* [ ] These formulas are not identified with operand-slot chirality.

---

## 29. Relative affine defect

* [ ] Two affine histories are written with explicit scales and translations.
* [ ] The equal-scale condition is stated.
* [ ] Endpoint-difference independence from (x) is proved.
* [ ] The group-valued relative transformation is distinguished from scalar endpoint defect.
* [ ] Elementary arithmetic torsion is recovered as a special case.
* [ ] The sign convention is fixed.

---

# E. Continuous flow

## 30. Affine Lie algebra

* [ ] Translation and dilation generators are defined.
* [ ] Their bracket is computed.
* [ ] The sign convention is fixed.
* [ ] The relevant real Lie group is identified.

---

## 31. Affine flow theorem

* [ ] One primary derivation is selected.
* [ ] The direction vector is defined.
* [ ] The angle convention is stated.
* [ ] The equation
  [
  \frac{da}{ds}
  =============

  \mu\cos\theta+\lambda a\sin\theta
  ]
  is proved.
* [ ] Pure additive motion is recovered.
* [ ] Pure multiplicative motion is recovered.
* [ ] Directional solutions are correct.
* [ ] Exceptional cases (\mu=0) or (\lambda=0) are treated or excluded.

---

## 32. Pfaffian form

* [ ] The coordinate relation
  [
  da=\mu,du+\lambda a,dv
  ]
  is derived.
* [ ] It is identified as a horizontal propagation constraint.
* [ ] It is not presented as globally integrable on unrestricted ((u,v,a))-space.
* [ ] Its connection with the later contact form is stated.

---

## 33. Eikonal form

* [ ] A compatible metric frame is specified.
* [ ] The metric dependence is explicit.
* [ ] The equation
  [
  |\nabla a|_g^2
  ==============

  \mu^2+\lambda^2a^2
  ]
  is proved.
* [ ] It is clear whether this equation is definitional or derived.
* [ ] The norm always carries an explicit metric where ambiguity exists.

---

## 34. Rectifying coordinate

If retained:

* [ ] its domain is stated;
* [ ] sign assumptions are stated;
* [ ] its gradient norm is proved;
* [ ] it is not used when (\mu=0);
* [ ] it is moved to an appendix if not needed downstream.

---

## 35. Infinitesimal torsion

* [ ] The finite two-step expressions are written.
* [ ] The Taylor expansion order is correct.
* [ ] The remainder order is correct.
* [ ] The formula is labeled asymptotic.
* [ ] It is distinguished from the exact contact-curvature formula.

---

# F. Regular AES and hyperbolic model

## 36. Regular AES definition gate

Before the model chapter is accepted:

* [ ] Primitive data are specified.
* [ ] Derived data are identified.
* [ ] The role of the metric is fixed.
* [ ] The role of the framed additive/multiplicative directions is fixed.
* [ ] The domain of the defining equation is fixed.
* [ ] Smoothness requirements are fixed.
* [ ] Constant versus variable (\mu,\lambda) is fixed.
* [ ] The definition does not depend circularly on (\mathfrak E_0).
* [ ] The definition is broad enough for later papers but narrow enough to have consequences.

---

## 37. Invariant affine metric

* [ ] Affine group coordinates are defined.
* [ ] Left or right invariance is declared.
* [ ] Generator lengths are normalized.
* [ ] The metric formula is derived.
* [ ] No uniqueness theorem is claimed.
* [ ] Coordinate rescalings are documented.

---

## 38. Basic hyperbolic model

* [ ] The upper-half-plane domain is defined.
* [ ] The metric is positive definite under stated assumptions.
* [ ] The assignment (a=-x/y) is defined.
* [ ] The inverse metric is computed.
* [ ] (a_x) and (a_y) are computed.
* [ ] The eikonal identity is verified.
* [ ] The model is named consistently.
* [ ] Completeness is stated or proved.
* [ ] The relation with the affine group is explained.

---

## 39. Curvature normalization

If retained:

* [ ] the Gaussian curvature is computed;
* [ ] metric rescaling is handled correctly;
* [ ] the final value is consistent throughout the paper;
* [ ] curvature is not used to infer complexity.

---

## 40. Arithmetic grid

* [ ] Addition action is defined.
* [ ] Multiplication action is defined.
* [ ] Their effects on the assignment are verified.
* [ ] It is stated whether they are isometries.
* [ ] Grid figures agree with formulas.
* [ ] The path orientation agrees with the chronological convention.

---

## 41. Baumslag–Solitar relation

If retained:

* [ ] the group relation is written under the final action convention;
* [ ] (k) and (s) assumptions are explicit;
* [ ] the calculation is verified;
* [ ] the relation is not used to infer hyperbolicity or hardness;
* [ ] the exact subgroup represented is identified.

---

## 42. Laplace eigenfunction

If retained:

* [ ] the Laplace–Beltrami sign convention is stated;
* [ ] the anisotropic metric is used;
* [ ] the eigenvalue is recomputed;
* [ ] (\mu)-dependence or independence is explained;
* [ ] the result is not presented as a full function theory.

---

# G. Zero geometry

## 43. Regular zero-locus theorem

* [ ] (Z(a)=a^{-1}(0)) is defined.
* [ ] (\mu\neq0) is explicit.
* [ ] The gradient norm on (Z(a)) is computed.
* [ ] (0) is shown to be a regular value.
* [ ] The regular-value theorem is invoked correctly.
* [ ] The codimension is correct.
* [ ] Boundary points are treated separately.
* [ ] No global finiteness conclusion is inferred.

---

## 44. Zero-set rigidity corollaries

* [ ] No isolated regular interior zero is stated correctly.
* [ ] No regular crossing is stated correctly.
* [ ] No regular branching is stated correctly.
* [ ] No regular interior endpoint is stated correctly.
* [ ] All corollaries remain local unless global hypotheses are added.
* [ ] Figures distinguish local theorem from global topology.

---

## 45. Singular AES definition

* [ ] A singular locus (S) is declared.
* [ ] The regular locus is (\mathcal M\setminus S).
* [ ] Regular AES equations hold on the regular locus.
* [ ] Allowed assignment singularities are described.
* [ ] Allowed metric singularities are described.
* [ ] Parameter degeneracies are described.
* [ ] Domain and projective-chart singularities are distinguished.
* [ ] The definition is not vacuous.
* [ ] (Z_{\mathrm{reg}}(a)) is defined.
* [ ] (Z_{\mathrm{sing}}(a)) is defined.

---

## 46. Isolated-zero model

If retained:

* [ ] its domain is explicit;
* [ ] inclusion or exclusion of the center is explicit;
* [ ] Cartesian regularity is checked;
* [ ] metric regularity is checked;
* [ ] the flow-equation domain is checked;
* [ ] the center is correctly classified;
* [ ] the model does not contradict the regular-zero theorem;
* [ ] model numbering is consistent.

---

## 47. Parameter-family zero surface

If retained:

* [ ] the family (a_t) is smooth in all variables;
* [ ] the total function (A(p,t)) is defined;
* [ ] the total zero set (\mathcal Z) is defined;
* [ ] spatial regularity (d_pa_t\neq0) is stated;
* [ ] regularity of (A) is proved;
* [ ] codimension is correct;
* [ ] the projection to parameter space is shown to be a submersion if claimed;
* [ ] no global tube triviality is inferred.

---

## 48. Properness warning

* [ ] Properness is stated as an additional hypothesis.
* [ ] Compactness of fibers is not assumed silently.
* [ ] Ehresmann-type conclusions are cited precisely.
* [ ] Boundary and non-proper escape mechanisms are acknowledged.
* [ ] The full tube theorem is deferred to Paper III.

---

## 49. Minimal multi-zero example

If retained:

* [ ] domain verified;
* [ ] metric verified;
* [ ] assignment verified;
* [ ] singular set verified;
* [ ] flow equation verified;
* [ ] number of zero components proved;
* [ ] zero topology proved;
* [ ] parameter restrictions stated;
* [ ] no uniqueness claim made without proof.

If any item is unchecked:

* [ ] the example has been moved to Paper III or labeled open.

---

# H. ACS and global torsion

## 50. ACS definition

* [ ] Additive increments are defined.
* [ ] Multiplicative logarithmic increments are defined.
* [ ] Signed increments are handled.
* [ ] Cumulative coordinates are defined.
* [ ] ACS paths follow chronological order.
* [ ] ACS is described as a charge shadow, not the full expression space.
* [ ] Symbol (M) is not confused with the manifold.

---

## 51. Direct ACS evaluation formula

* [ ] The formula is derived from the affine cocycle.
* [ ] The weighting kernel is correct.
* [ ] The path orientation is correct.
* [ ] A one-step addition example is checked.
* [ ] An add–multiply example is checked.
* [ ] The formula agrees with direct operator evaluation.
* [ ] The relation to the previous reverse-path formula is explained.

---

## 52. Compatibility conditions

* [ ] Scale compatibility is defined.
* [ ] Charge compatibility is defined.
* [ ] Their difference is explained.
* [ ] Endpoint-difference independence uses only the hypotheses required.
* [ ] Closed ACS fillings use equal endpoints.
* [ ] No stronger compatibility is assumed than needed.

---

## 53. Relative torsion

* [ ] (\tau(\gamma,\delta)) is defined.
* [ ] Dependence or independence from initial value is proved.
* [ ] Temporal reversal is treated as a special case.
* [ ] Mirror comparison is not conflated with torsion.
* [ ] Scalar endpoint defect is distinguished from group-valued relative defect.

---

## 54. Boundary-integral formula

* [ ] The weighted (1)-form is fixed.
* [ ] The orientation is fixed.
* [ ] The boundary chain is fixed.
* [ ] The sign is checked on a rectangle.
* [ ] The sign is checked on a nontrivial four-step example.
* [ ] Self-intersecting paths are treated as chains.
* [ ] No simple-region assumption is made unnecessarily.

---

## 55. Weighted torsion–Stokes theorem

* [ ] The theorem statement matches the selected normalization.
* [ ] The (2)-chain is defined.
* [ ] Stokes’ theorem is applied correctly.
* [ ] Filling independence is justified in the ACS plane.
* [ ] Signed charges are handled or explicitly excluded.
* [ ] The previous path-versus-reversal theorem is recovered.
* [ ] All figures and captions use the same sign convention.

---

# I. Contact and horizontal curvature

## 56. Contact form

* [ ] The contact form is defined.
* [ ] (d\alpha) is computed.
* [ ] (\alpha\wedge d\alpha) is computed.
* [ ] The orientation sign is consistent.
* [ ] (\mu\lambda\neq0) is stated.
* [ ] The result is described as an arithmetic coordinatization of a standard contact model.

---

## 57. Horizontal lifts

* [ ] (D_u) is defined.
* [ ] (D_v) is defined.
* [ ] Both lie in (\ker\alpha).
* [ ] They form a frame under the stated hypotheses.
* [ ] Their arithmetic interpretations are stated.

---

## 58. Legendrian realization of flow

* [ ] (D_\theta) is defined.
* [ ] Tangent components are computed.
* [ ] The affine flow equation is recovered.
* [ ] The contact model is shown to reproduce rather than redefine the flow.
* [ ] Any arclength assumption is explicit.

---

## 59. Horizontal curvature bracket

* [ ] ([D_u,D_v]) is computed.
* [ ] The result is vertical.
* [ ] The coefficient is correct.
* [ ] The sign matches (d\alpha(D_u,D_v)).
* [ ] Non-integrability is stated correctly.
* [ ] The bracket is not confused with Riemannian torsion.

---

## 60. Finite commutator formulas

If retained:

* [ ] the open two-path defect is computed;
* [ ] the closed-loop holonomy is computed;
* [ ] the composition order is explicit;
* [ ] the two finite quantities are distinguished;
* [ ] their common leading term is identified;
* [ ] the signs agree with the ACS convention.

---

## 61. Horizontal covariant differential

* [ ] (\delta_HF) is defined on scalar fields.
* [ ] Its equivalent formula using (\alpha) is proved.
* [ ] Its equivalent formula using (D_u,D_v) is proved.
* [ ] It is not described as a full differential on forms unless extended.
* [ ] The notation does not conflict with Paper II operators.

---

## 62. Horizontal curvature formula

* [ ] (\delta_H^2F) is explicitly defined as an antisymmetrized second derivative.
* [ ] The bracket identity is used.
* [ ] The formula is proved.
* [ ] The special case (F=a) is checked.
* [ ] Non-nilpotence is stated.
* [ ] The result is not confused with de Rham (d^2=0).

---

## 63. Local-global synthesis

* [ ] Exact affine defect is distinguished from infinitesimal density.
* [ ] Exact ACS weighted-area equality is stated.
* [ ] Exact finite contact correction is stated separately.
* [ ] Contact curvature is identified as the leading local density.
* [ ] No theorem claims all quantities are literally equal at finite scale.
* [ ] The synthesis statement has no circular dependency.
* [ ] The synthesis is understandable without Paper II–IV.

---

# J. Mathematical-status closure

## 64. Status register consistency

For every theorem-like result in Paper I:

* [ ] it has an entry in `05-mathematical-status.md`;
* [ ] its source statement matches the status entry;
* [ ] its proof location is recorded;
* [ ] all hypotheses match;
* [ ] all downstream nodes have been rechecked after changes;
* [ ] no `STRUCTURAL PROPOSAL` appears as a theorem;
* [ ] no `OPEN PROBLEM` appears in the abstract as a result;
* [ ] no `UNSUPPORTED AND EXCLUDED` claim remains as established prose.

---

## 65. Mathematical acceptance gate

Level C is passed only when:

* [ ] all critical nodes in `03-theorem-dependency-graph.md` are complete;
* [ ] every critical theorem has a proof;
* [ ] every standard consequence required by Paper I has been integrated;
* [ ] no critical result depends on an optional example;
* [ ] no Paper II–IV result is used circularly;
* [ ] all convention audits are complete;
* [ ] all known rejected formulations are removed.

---

# Part IV. Level D — Editorial closure

## 66. Title and metadata

* [ ] The final title matches Paper I’s actual scope.
* [ ] The subtitle does not imply a complete projective theory.
* [ ] Author name is correct.
* [ ] Affiliation is correct.
* [ ] Email is correct.
* [ ] Date policy is correct.
* [ ] Keywords match the final content.
* [ ] DOI or version information is accurate.
* [ ] Header and preprint metadata are updated.

---

## 67. Abstract

* [ ] The abstract is between approximately 180 and 280 words.
* [ ] It introduces marked sequential histories.
* [ ] It states projective (PGL_2) placement.
* [ ] It identifies the affine/Borel sector.
* [ ] It states the flow result.
* [ ] It states the hyperbolic model.
* [ ] It states the torsion/contact-curvature result.
* [ ] It mentions zero-set regularity if proved.
* [ ] It does not claim a complete function theory.
* [ ] It does not claim a tube or knot theory.
* [ ] It does not claim complexity results.
* [ ] Every abstract claim maps to a theorem or proposition in the body.

---

## 68. Introduction

* [ ] The process-to-result hierarchy is explicit.
* [ ] Sequential histories are motivated.
* [ ] The bilateral completion is introduced early.
* [ ] The affine limitation is explicit.
* [ ] Main contributions correspond to actual theorem labels.
* [ ] Scope exclusions are stated.
* [ ] Papers II–IV are introduced as interfaces, not completed results.
* [ ] Historical placement is restrained.
* [ ] No novelty claim exceeds the literature audit.
* [ ] The chapter guide matches the final structure.

---

## 69. Section openings and transitions

For every main chapter:

* [ ] the opening identifies imported objects;
* [ ] the opening identifies the new problem;
* [ ] the opening previews the main result;
* [ ] the closing states what has been established;
* [ ] the closing identifies the next dependency;
* [ ] transitions do not introduce unproved conclusions;
* [ ] repetitive summaries are removed.

---

## 70. Terminology

* [ ] `marked spinal history` is canonical.
* [ ] `threadlike expression` is deprecated or historically qualified.
* [ ] `left-expanded/right-expanded` is absent or slot-qualified.
* [ ] mirror, reversal, and inverse are consistently distinguished.
* [ ] regular and singular AES are consistently distinguished.
* [ ] total zero set and tube are consistently distinguished.
* [ ] affine and projective are consistently distinguished.
* [ ] ordinary and projective evaluation are consistently distinguished.
* [ ] horizontal covariant differential is used consistently.
* [ ] Riemannian torsion is not confused with arithmetic torsion.
* [ ] `natural`, `canonical`, `unique`, and `forced` are justified at every use.

---

## 71. Notation

* [ ] (K) is used consistently for a general field.
* [ ] (\rho(\gamma)) denotes operator evaluation.
* [ ] (\nu_x(\gamma)) denotes endpoint evaluation.
* [ ] (\Phi,\xi,\widehat\xi) are stable.
* [ ] (a) denotes the assignment.
* [ ] (A,M) denote ACS charges.
* [ ] (\mathcal M) is used when (M) would conflict.
* [ ] (\mu,\lambda) are not overloaded.
* [ ] (u) and (\nu) are visually and semantically distinguished.
* [ ] (\mathfrak E_0,\mathfrak E_1) are stable.
* [ ] (\alpha,D_u,D_v,\delta_H) are stable.
* [ ] No symbol changes meaning across adjacent chapters without declaration.

---

## 72. Theorem environments

* [ ] Theorem environments share a coherent counter.
* [ ] Examples print as `Example`, not `Theorem`.
* [ ] Definitions use the definition style.
* [ ] Conjectures are precise.
* [ ] Open problems use a dedicated environment.
* [ ] Warnings are visibly distinct from theorems.
* [ ] No proposal appears in a theorem environment.
* [ ] Theorem titles are semantic and restrained.

---

## 73. Labels and references

* [ ] Every theorem has a semantic label.
* [ ] Every important equation has a semantic label.
* [ ] Editing-history labels have been removed.
* [ ] No label is duplicated.
* [ ] Every cross-reference resolves.
* [ ] No reference points to a moved or deleted section.
* [ ] Prospective references are clearly prospective.
* [ ] Appendix references are accurate.

---

## 74. Equations

* [ ] Only referenced or structurally important equations are numbered.
* [ ] Exact and asymptotic formulas are distinguished.
* [ ] Norms carry the relevant metric.
* [ ] Wedge-product orientation is consistent.
* [ ] Operator domains are not implied by formal notation.
* [ ] Equation punctuation is consistent with prose.
* [ ] Manual equation tags have been removed unless required.
* [ ] Long derivations are moved to appendices where appropriate.

---

## 75. Proofs

* [ ] Every proof proves the exact stated result.
* [ ] Every hypothesis is used or removed.
* [ ] No proof relies on a later theorem.
* [ ] No proof relies on an example.
* [ ] Local conclusions are not inflated globally.
* [ ] Standard theorem invocations identify hypotheses.
* [ ] Convention-sensitive steps reference the convention.
* [ ] “Clearly” and “obviously” do not hide essential steps.
* [ ] Long proofs are structured into meaningful parts.

---

## 76. Examples

* [ ] Every example has one declared purpose.
* [ ] Examples are labeled as examples.
* [ ] No example is used as a general proof.
* [ ] Same-value/different-history examples are included.
* [ ] Mirror/reversal distinction is illustrated.
* [ ] Projective/ordinary-domain distinction is illustrated.
* [ ] Regular/singular-zero distinction is illustrated.
* [ ] ACS signs are illustrated.
* [ ] Finite/infinite or finite/infinitesimal distinctions are illustrated accurately.

---

## 77. Figures

* [ ] Every figure has a mathematical purpose.
* [ ] Every figure has an editable or reproducible source.
* [ ] Captions are mathematically self-contained.
* [ ] Axis and orientation conventions match the text.
* [ ] Colors and line styles are explained.
* [ ] Historical notation has been updated.
* [ ] Figures do not serve as proof.
* [ ] Later-paper promotional figures have been removed from Paper I.
* [ ] Figure references occur in the prose.
* [ ] No figure file is missing.

---

## 78. Tables

* [ ] Context-to-matrix tables include domain conditions.
* [ ] Status tables distinguish mathematical and editorial status.
* [ ] Tables use precise headings.
* [ ] No table duplicates long prose without benefit.
* [ ] Table references resolve.

---

## 79. Citations and bibliography

* [ ] Every citation supports the statement it follows.
* [ ] Standard group-theoretic facts have suitable references.
* [ ] Hyperbolic geometry references are appropriate.
* [ ] Contact geometry references are appropriate.
* [ ] Regular-value and proper-submersion results are cited where used.
* [ ] Historical claims are restrained.
* [ ] Novelty claims are qualified.
* [ ] No unused citation remains in active Paper I without reason.
* [ ] No bibliography entry required by Papers II–IV has been deleted prematurely.
* [ ] Bibliography compiles without errors.

---

## 80. Conclusion

* [ ] The conclusion summarizes proved results only.
* [ ] It includes projective placement.
* [ ] It includes the affine geometric foundation.
* [ ] It includes torsion and contact curvature.
* [ ] It includes the regular/singular-zero boundary.
* [ ] It does not claim completed function theory.
* [ ] It does not claim completed tube or knot theory.
* [ ] It does not claim complexity consequences.
* [ ] Interfaces to Papers II–IV are explicit.
* [ ] Open problems are labeled as open.

---

## 81. Editorial acceptance gate

Level D is passed only when:

* [ ] all prose conforms to `06-editorial-rules.md`;
* [ ] terminology and notation audits are complete;
* [ ] abstract, introduction, and conclusion match the theorem set;
* [ ] all figures, citations, labels, and references are stable;
* [ ] no known scope drift remains.

---

# Part V. Level E — Release candidate

## 82. Clean build

* [ ] The release branch builds from a clean checkout.
* [ ] The local build succeeds.
* [ ] The Docker build succeeds or an exact documented substitute exists.
* [ ] The expected Paper I PDF is produced.
* [ ] The PDF opens successfully.
* [ ] No undefined references remain.
* [ ] No missing citations remain.
* [ ] No duplicate labels remain.
* [ ] No missing figures remain.
* [ ] No fatal overfull boxes remain in mathematical statements.
* [ ] Important underfull or layout warnings have been reviewed.
* [ ] Table of contents is correct.
* [ ] Bibliography is present and formatted.
* [ ] Appendices are included correctly.

---

## 83. Reproducibility

* [ ] Build instructions in `README.md` are current.
* [ ] Required TeX tools are documented.
* [ ] Docker instructions are current.
* [ ] Figure-generation scripts are documented.
* [ ] External data or computation inputs are versioned.
* [ ] No build depends on untracked local files.
* [ ] Generated PDF paths are deterministic.
* [ ] The repository contains no required proprietary font dependency.

---

## 84. Repository hygiene

* [ ] Temporary build files are ignored.
* [ ] No accidental PDFs or auxiliary files are committed outside policy.
* [ ] No duplicate active source tree remains.
* [ ] Archived transcripts are marked non-authoritative.
* [ ] Migration logs are complete.
* [ ] Status changes are recorded.
* [ ] Open questions are updated.
* [ ] Branch name and release tag policy are clear.
* [ ] The final source commit is identifiable.

---

## 85. Independent mathematical review

At least one reviewer other than the primary restructuring agent must verify:

* [ ] sequential-tree theorem;
* [ ] (PGL_2) generation;
* [ ] affine cocycle formulas;
* [ ] flow derivation;
* [ ] hyperbolic-model normalization;
* [ ] regular-zero theorem;
* [ ] ACS sign convention;
* [ ] contact finite and infinitesimal formulas;
* [ ] local-global synthesis.

Reviewer identity and date must be recorded.

---

## 86. Independent scope review

A reviewer must verify:

* [ ] Paper II analytic material has not leaked back into Paper I.
* [ ] Paper III multi-zero/tube material has not been presented as complete.
* [ ] Paper IV condensation/complexity material has not been presented as proved.
* [ ] Projective placement remains concise.
* [ ] Paper I can be read independently.
* [ ] Paper I does not require unpublished later-paper results.

---

## 87. Abstract-to-body traceability

For every substantive abstract sentence:

* [ ] the supporting theorem or proposition is identified;
* [ ] all qualifications are preserved;
* [ ] no sentence depends on an optional result omitted from the final draft;
* [ ] no sentence depends on an open problem.

A traceability table may be maintained in the audit report.

---

## 88. Conclusion-to-body traceability

For every substantive conclusion sentence:

* [ ] the supporting result is identified;
* [ ] interpretation is labeled as interpretation;
* [ ] future work is labeled as future work;
* [ ] no conjecture is presented as established.

---

## 89. Version and release metadata

* [ ] The manuscript version is stated.
* [ ] The release date is stated.
* [ ] The Git commit is recorded.
* [ ] The relation to earlier DOI versions is stated.
* [ ] Superseded versions are not confused with the restructured manuscript.
* [ ] Preprint metadata matches the PDF.
* [ ] Repository README matches the release state.

---

## 90. Release-candidate acceptance gate

Level E is passed only when:

* [ ] Levels A–D are complete;
* [ ] the clean build passes;
* [ ] independent mathematical review passes;
* [ ] independent scope review passes;
* [ ] abstract and conclusion are traceable;
* [ ] no unresolved critical issue remains in `08-open-questions.md`;
* [ ] every unchecked item is explicitly waived with a written reason.

---

# Part VI. Chapter-level sign-off sheets

## 91. Chapter 1 — Introduction

* [ ] Central problem stated
* [ ] Process-to-result hierarchy stated
* [ ] Sequential restriction justified
* [ ] Bilateral completion stated
* [ ] Affine sector stated
* [ ] Contributions match theorem labels
* [ ] Scope exclusions stated
* [ ] Historical placement restrained
* [ ] Section guide correct
* [ ] No unproved later-paper result presented as established

**Reviewer:**
**Date:**
**Notes:**

---

## 92. Chapter 2 — Sequential Arithmetic Histories

* [ ] Tree definition stable
* [ ] Dependency poset stable
* [ ] T1 proved
* [ ] Marked accumulator defined
* [ ] Context slots defined
* [ ] History correspondence proved
* [ ] Mirror/reversal/inverse separated
* [ ] Equality levels separated
* [ ] Examples verified
* [ ] Deprecated terminology removed

**Reviewer:**
**Date:**
**Notes:**

---

## 93. Chapter 3 — Projective Semantics and the Affine Sector

* [ ] Context matrix table audited
* [ ] Domain conditions explicit
* [ ] Projective evaluation functorial
* [ ] T2 proved
* [ ] Affine/Borel corollary proved
* [ ] Positive real restriction stated
* [ ] Bruhat remark accurate
* [ ] Riccati placement restrained
* [ ] Paper IV material excluded

**Reviewer:**
**Date:**
**Notes:**

---

## 94. Chapter 4 — Affine Cocycles and Relative Defects

* [ ] Composition convention fixed
* [ ] Target cocycle proved
* [ ] Source-normalized cocycle proved
* [ ] Maurer–Cartan formulas audited
* [ ] Relative defect defined
* [ ] Equal-scale independence proved
* [ ] Elementary torsion checked
* [ ] Perturbation formulas integrated
* [ ] No free-group conflation remains

**Reviewer:**
**Date:**
**Notes:**

---

## 95. Chapter 5 — Continuous Arithmetic Flow

* [ ] Lie-algebra derivation complete
* [ ] Flow equation proved
* [ ] Axis solutions correct
* [ ] Pfaffian form interpreted correctly
* [ ] Eikonal metric dependence explicit
* [ ] Rectifying coordinate checked or moved
* [ ] Infinitesimal torsion labeled asymptotic
* [ ] Riccati relation stated accurately

**Reviewer:**
**Date:**
**Notes:**

---

## 96. Chapter 6 — Basic Hyperbolic Expression Space

* [ ] Regular AES definition fixed
* [ ] Invariant metric derived
* [ ] Upper-half-plane coordinates correct
* [ ] Basic model theorem proved
* [ ] Curvature checked
* [ ] Grid actions checked
* [ ] Baumslag–Solitar relation checked or removed
* [ ] Laplace eigenfunction checked or moved
* [ ] Model naming stable
* [ ] No uniqueness overclaim remains

**Reviewer:**
**Date:**
**Notes:**

---

## 97. Chapter 7 — Zero Loci and Singular Expression Spaces

* [ ] Regular-zero theorem proved
* [ ] Local rigidity corollaries correct
* [ ] Boundary caveats included
* [ ] Singular AES defined
* [ ] Regular/singular zero notation fixed
* [ ] Isolated-zero model audited
* [ ] Parameter-family lemma proved or removed
* [ ] Properness warning included
* [ ] Multi-zero example verified or moved

**Reviewer:**
**Date:**
**Notes:**

---

## 98. Chapter 8 — Global Torsion and the ACS

* [ ] ACS direct-path convention fixed
* [ ] Evaluation formula derived
* [ ] Scale compatibility defined
* [ ] Charge compatibility defined
* [ ] Relative torsion proved independent of (x)
* [ ] Boundary formula proved
* [ ] Stokes formula proved
* [ ] Signs checked with examples
* [ ] Reversal reduced to a special case
* [ ] Quotient speculation moved to Paper IV

**Reviewer:**
**Date:**
**Notes:**

---

## 99. Chapter 9 — Contact Connection and Horizontal Curvature

* [ ] Contact form defined
* [ ] Nondegeneracy proved
* [ ] Horizontal lifts defined
* [ ] Legendrian flow proved
* [ ] Curvature bracket proved
* [ ] Finite defects separated
* [ ] Horizontal differential defined
* [ ] Curvature formula proved
* [ ] Local-global synthesis precise
* [ ] Analytic material moved to Paper II

**Reviewer:**
**Date:**
**Notes:**

---

## 100. Chapter 10 — Conclusions and Research Interfaces

* [ ] Proved chain summarized accurately
* [ ] Paper II interface accurate
* [ ] Paper III interface accurate
* [ ] Paper IV interface accurate
* [ ] Open problems labeled
* [ ] No completed-function-theory claim
* [ ] No completed-tube claim
* [ ] No complexity claim
* [ ] No promotional overstatement

**Reviewer:**
**Date:**
**Notes:**

---

# Part VII. Codex task acceptance

## 101. Required fields for every Codex restructuring task

Before execution:

* [ ] Task scope stated
* [ ] Allowed files stated
* [ ] Forbidden files stated
* [ ] Theorem nodes in scope stated
* [ ] Claim-status changes allowed stated
* [ ] Required build command stated
* [ ] Expected output stated

After execution:

* [ ] Files changed listed
* [ ] Claims added listed
* [ ] Claims weakened listed
* [ ] Claims moved listed
* [ ] Assumptions changed listed
* [ ] Open issues listed
* [ ] Build result reported
* [ ] Warnings reported
* [ ] No out-of-scope file changed
* [ ] Diff reviewed by a human

---

## 102. Automatic rejection conditions for a Codex task

A task must be rejected or reverted if Codex:

* [ ] deletes substantive notes without archival disposition;
* [ ] strengthens a claim without authorization;
* [ ] invents a missing proof;
* [ ] changes model numbering globally without an audit;
* [ ] changes composition convention without propagation review;
* [ ] merges mirror and reversal;
* [ ] presents projective continuation as ordinary arithmetic;
* [ ] calls an isolated zero regular;
* [ ] promotes a smooth total zero set to a global tube without properness;
* [ ] leaves Paper II–IV theory in Paper I as established results;
* [ ] reports build success without producing the PDF;
* [ ] changes forbidden files.

Any checked item in this rejection section means the task has failed acceptance.

---

# Part VIII. Waivers

## 103. Waiver policy

An acceptance item may be waived only when:

1. the item is noncritical;
2. the reason is written;
3. downstream effects are identified;
4. the waiver is approved by the author;
5. the waiver does not contradict `00-authoritative-scope.md`.

A waiver must use:

```markdown
## Waiver W-XXXX

- Checklist item:
- Reason:
- Mathematical effect:
- Editorial effect:
- Downstream papers affected:
- Approved by:
- Date:
```

Critical mathematical gates may not be waived for release.

---

# Part IX. Final release declaration

## 104. Release declaration template

```markdown
# Paper I Release Declaration

- Manuscript title:
- Version:
- Date:
- Git commit:
- PDF filename:
- Page count:
- Build command:
- Build status:
- Mathematical reviewer:
- Scope reviewer:
- Editorial reviewer:
- Open critical issues: none / listed below
- Waivers: none / listed below

## Acceptance levels

- Level A — Repository baseline: PASS / FAIL
- Level B — Structural migration: PASS / FAIL
- Level C — Mathematical closure: PASS / FAIL
- Level D — Editorial closure: PASS / FAIL
- Level E — Release candidate: PASS / FAIL

## Author approval

I confirm that the manuscript’s definitions, claims, proofs, scope, and paper-series interfaces have been reviewed against the authoritative restructuring documents.

- Name:
- Date:
```

---

## 105. Governing acceptance principle

Paper I is accepted only when its claims, proofs, source structure, and paper boundaries agree.

The governing test is:

[
\boxed{
\text{defined before used}
\quad+\quad
\text{proved before claimed}
\quad+\quad
\text{migrated without loss}
\quad+\quad
\text{built reproducibly}.
}
]

A polished manuscript that fails a mathematical gate is not acceptable.

A mathematically correct manuscript with unresolved source migration is not release-ready.

A complete release requires both.
