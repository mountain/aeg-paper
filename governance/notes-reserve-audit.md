# Notes Reserve Audit

**File:** `governance/notes-reserve-audit.md`
**Status:** Audit record (inventory and status register for `notes/`; non-authoritative, does not revise scope)
**Version:** 1.0
**Date:** 2026-08-10
**Prepared by:** DeepSeekHarness (AI coding agent), working under the repository
author's direction; all mathematical grades follow the official status
vocabulary of `governance/05-mathematical-status.md` and no claim status is
changed by this audit.
**Depends on:**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/05-mathematical-status.md`
* `governance/08-open-questions.md`

**Applies to:** Every note under `notes/`, together with cross-references to
archival material in `archive/` where a conflict or a corrected statement
originates there.

---

## 1. Purpose and method

The five canonical manuscripts (Papers 0–IV) have incorporated a subset of the
material in `notes/`.  This audit inventories what was and was not incorporated,
grades the unincorporated reserve by proof completeness using the official
status vocabulary of `governance/05-mathematical-status.md`, records conflicts
and obsolescence without reconciling them silently, and recommends dispositions.
It deliberately **does not** modify any paper source, promote any claim, or
revise the authoritative scope.  Promotion of any item below requires a
separate task with the integration audits prescribed by
`governance/05-mathematical-status.md`, Section 4.

Grade labels used below:

* `WORKING-NOTE PROVED` — complete proofs exist inside the note itself;
  **INTEGRATION AUDIT REQUIRED** before the result may be marked `PROVED` in a
  paper (statement/proof match, conventions, field and regularity hypotheses).
* `COMPUTATIONALLY VERIFIED EXAMPLE` — checked for a finite dataset by a
  reproducible script; no general theorem.
* `STRUCTURAL PROPOSAL` — coherent framework, no completeness/uniqueness theorem.
* `OPEN PROGRAM` — research program with a declared pass/fail criterion.
* `EXPLORATORY` — idea-level material, not yet a precise mathematical claim.
* `CORRECTED` — contains a statement later shown to be wrong or imprecise; the
  correction is recorded here.

---

## 2. Disposition of every note

### 2.1 `notes/foundations-and-geometry/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-cayley-hyperbolic-model | Unincorporated | STRUCTURAL PROPOSAL + conjecture | Cayley model with fractal boundary; the claim "K=−2 almost everywhere" is conjectural and unverified. See OQ-078-A. |
| 02-parameterized-evaluation-frameworks | Partially incorporated | STRUCTURAL PROPOSAL | The dual-tube idea survives in the (A,M) charge picture; the algebraic total space `E_alg → B_eval` and the observation "ACS = identity-parameter fiber (r=0,t=1)" are not in any paper. Outlook candidate for Paper IV. |
| 03-single-zero-diffusion-model | Incorporated | (conflict) | Content equals Paper I §7 isolated-zero disc model, **but under inverted names E₀/E₁**; see C-1. |
| 04-affine-torus-holonomy | Unincorporated | WORKING-NOTE PROVED | 4×4 piecewise map on T², 16-face torsion table, discrete Stokes law with conjugation weights, four worked loops. Toy calibration candidate for Paper III (threading/quandle layer) or Paper IV (resource loops). |
| 05-process-groups-and-zariski-topology | Unincorporated | elementary part WORKING-NOTE PROVED; interpretation STRUCTURAL | Preimages of ideals in ℤ under the charge homomorphism give normal subgroups of F₂ with lattice correspondence to Zariski closed sets; elementary and correct. The "process space with Spec ℤ as sections" reading is structural. Optional Paper IV outlook. |

### 2.2 `notes/analysis-and-calculus/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-horizontal-analysis-program | Incorporated | program | Realized by Paper II: operator selection (factorization vs variational), frame drift `Δ_g = X_u²+X_v²−c_vX_u+c_uX_v`, Appell modules, boundaries. |
| 02-mixed-affine-integration | Unincorporated | WORKING-NOTE PROVED | Continuous mixed integral `∫u·exp(∫_x^b v)`, transport/splitting/window-derivative identities, adjoint pairing, continuous ACS triple identity. Complete proofs; **integration audit required** (which paper, which conventions). |
| 03-weighted-contact-calculus | Unincorporated | WORKING-NOTE PROVED | Graded covariant differential `∇^{(n)}f=δf−nf dM`, graded Leibniz law, gauge rectification `ã=e^{−M}a`, twisted product `⋆_M` with derivation `D_M`, twisted Rota–Baxter identity, dual weight-line adjoint geometry, E₀/ACS structure equations `dω_A=ω_M∧ω_A`. Complete proofs; **integration audit required**. |

### 2.3 `notes/computation-and-resources/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-binary-expression-complexity-program | Partially incorporated | STRUCTURAL PROPOSAL | Program themes realized in Paper IV case studies (Horner, OBDD, transforms, checkpointing). The length-four Catalan cost program itself remains open. |
| 02-path-loop-homology-toy-model | Partially incorporated | WORKING-NOTE PROVED (toy) | T/D world, rewrite 2-cells, Thue–Morse parity as an H¹ cochain with H₁(G)≅ℤ. Philosophy used in Paper IV §8 (rewrite fibers, telescope obstruction); the Thue–Morse calibration example itself is unincorporated. |
| 03-turing-machine-resource-geometry | Partially incorporated | STRUCTURAL PROPOSAL + definitions | Resource plane (A,M), ω=e^M dA, resource torsion; Paper IV chose the residual/state route instead. The TM-specific torsion and its falsifiability criterion (classify realizable reorderings) remain open; see OQ-078-E. |
| 04-resource-geometry-progress-memo | Partially incorporated | COMPUTATIONALLY VERIFIED EXAMPLE | Y-DAG pebble example with τ = 2e(e−1); "ghost waiting" closure for differing end times. Worked examples unincorporated; closure rule untested beyond the toy. |
| 05-computational-spacetime-geometry-program | Unincorporated | OPEN PROGRAM | PD₃ program with three milestones and explicit pass/fail criteria; Milestone 1 (torus stage T²×[a₋,a₊], `[κ]=μλ[du∧dv]≠0`, PD dual class) is well-posed. See OQ-078-F. |
| 06-computational-spacetime-duality | Unincorporated | STRUCTURAL PROPOSAL | "Route B" 2-groupoid: paths as 1-morphisms, interchange squares as 2-morphisms labelled by torsion, de Rham pairing as the time–space duality bridge. No coherence theorem yet. |

### 2.4 `notes/knots-and-loops/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-figure-eight-arithmetic-loop | Partially incorporated | WORKING-NOTE PROVED | 4₁ relator on the two grids, closure ⇔ Δ(t)=0; the affine word computation is Paper III App C. |
| 02-zero-taxonomy-and-arithmetic-loops | Partially incorporated | STRUCTURAL PROPOSAL | Six-layer zero taxonomy; Paper I App E retains the first four layers. The poset of zeros and separation problems remain open. |
| 03-figure-eight-aeg-summary | Unincorporated | EXPLORATORY / superseded | `E_{4_1}` on H³, "fire-burning", λ=φ² tuning, π₁↔paths / H₁↔ACS dictionary. Superseded by the q=4 Hecke route of Papers I–III; archive. |
| 04-figure-eight-hnn-arithmetization | Partially incorporated | derivation WORKING-NOTE PROVED | HNN arithmetization forces t to be an Alexander root (u↦+1, v↦+φ, t↦·φ⁻²); the note's own critique (scalar additions cannot represent F₂) is correct and prefigures Paper III's collapse theorems. |
| 05-figure-eight-modulo-arithmetization | Unincorporated | **CORRECTED** | The "dense singularity" claim is wrong: the quotient R²/(ℤ(1,0)+ℤ(0,φ)) is a compact Hausdorff torus; denseness belongs only to its 1-dimensional projection (Kronecker). See C-8. |
| 06-fox-calculus-and-alexander-modules | Partially incorporated | WORKING-NOTE PROVED | Affine cocycle `D(uv)=D(u)+φ(u)D(v)` as the Fox-Leibniz rule; commutator and BS(1,2) Alexander computations; the Alexander-layer placement is Paper III §8. |
| 07-figure-eight-arithmetic-interpretation | Partially incorporated | COMPUTATIONALLY VERIFIED EXAMPLE | SageMath/snappy dataset: relator closure recovers Δ(t)=0 for a list of knots up to 11 crossings. Presentation- and mapping-dependent; not a theorem. |
| 08-small-knot-group-embeddings | Unincorporated | WORKING-NOTE PROVED (computations) | Three-parameter group G with aᵐbⁿ normal forms; trefoil/cinquefoil embeddings with Δ as factor. Dataset candidate; embedding-level claims only. |
| 09-knot-torsion-and-cyclotomic-fields | Unincorporated | COMPUTATIONALLY VERIFIED EXAMPLE | Empirical factorization τ = σΔ(t)(t^K−1)/t^k, cyclotomic factors, random-shuffle controls. Dataset, not a theorem; see OQ-078-G. |
| 10-arithmetic-knot-geometry-zh | Partially incorporated | COMPUTATIONALLY VERIFIED EXAMPLE | Early Chinese statement of the same dataset. |
| 11, 12 (presentation questions, zh) | Unincorporated | EXPLORATORY | Presentation-selection questions feeding notes 01–09. |
| 13-knot-torsion-results | Unincorporated | COMPUTATIONALLY VERIFIED EXAMPLE | Complete tables for 4₁, 6₂, 6₃, 7₆. Dataset. |

### 2.5 `notes/projective-condensation/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-bilateral-projective-condensation | Incorporated | — | Direct source of Paper I §2–3 (sequential classification, PGL₂ generation) and Paper IV §1–4 (bivaluations, quotient tower, frame torsor, finite-field counts, telescope obstruction). Its §10 contact-comparison conjecture (AEG horizontal distribution vs the PSL₂(R) unit-tangent contact structure) remains a CONJECTURE; see OQ-078-H. |
| 02-projective-geometric-frameworks | Unincorporated | EXPLORATORY | May 2025 discussion of projective vs hyperbolic placement; superseded by the incorporated note 01. |
| 03-canonical-forms-and-condensation | Partially incorporated | STRUCTURAL PROPOSAL | Condensation-as-quotient became Paper IV's algebraic condensation; the BS(1,1) grid discussion feeds Paper 0. The "computational energy/mass inducing curvature" metaphor remains unincorporated and is archival. |

### 2.6 `notes/thermodynamics-and-renormalization/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-physical-evolution-landscapes | Unincorporated | EXPLORATORY | Conceptual memorandum (richness, similarity/popularity, condensation). |
| 02-aeg-flow-and-renormalization-en | Unincorporated | EXPLORATORY | Dual-timescale reading (addition=dynamical time, multiplication=evolutionary time/scale); interpretive. |
| 03, 04 (zh) | Unincorporated | EXPLORATORY | RG discussion and iteration examples; historical. |
| 05-aeg-thermodynamics | Unincorporated | core WORKING-NOTE PROVED | Explicit contactomorphism Φ:(u,v,a)↦(S,V;U,T,p)=(v,−u;a,λa,μ) pulling back the thermodynamic form; Maxwell relations in AEG variables; the compatibility remark (constant (λ,μ) is incompatible with a nontrivial fundamental equation U(S,V)); Massieu representation; solvable family. Strong candidate for a standalone correspondence note; **integration audit required**. |
| 06-algorithmic-thermodynamics | Unincorporated | PARTIALLY PROVED | Baez–Stay bridge via first-hitting paths for a linear cost W=A+αM; the prefix-free first-hitting argument is proved; the full Gibbs/partition correspondence is open. |
| 07-contact-algorithmic-thermodynamics | Unincorporated | WORKING-NOTE PROVED (fixed-N sector) | Contactomorphism onto the fixed-N slice of the Baez–Stay contact form. Candidate note. |
| 08-keraia-aeg-correspondence | Unincorporated | EXPLORATORY | Keraia machine dictionary (n₀,n₁ ↔ additive/multiplicative charges). |
| 09-keraia-aeg-mapping-correction | Unincorporated | CORRECTED (as critique) | Documents two real errors of the prototype visualizer: collapsing independent observables E,V to one static quantity, and confusing hardware costs with thermodynamic conjugate variables. Keep attached to any future use of 06–08. |

### 2.7 Archival cross-references (one-line each)

* `archive/revision-2/aristotle/` — Lean 4/Mathlib formalization (37 theorems, zero `sorry`) of the **legacy** paper statements. Machine check, but version-mismatched with the current papers; any citation needs a legacy→current statement map.
* `archive/ideal_glass/` — Python prototype + Chinese working note applying AEG contact/ACS to ideal glass protocols; declared approximations throughout; exploratory.
* `archive/peddle/` — interactive pebble-game resource lab (HTML); visual, not audited mathematically.

---

## 3. Conflict and obsolescence register

Recorded here, not reconciled.  Priority order for any future work remains
`AGENTS.md` → authoritative governance → current paper sources.

| ID | Conflict | Evidence | Current authoritative resolution |
| --- | --- | --- | --- |
| C-1 | E₀/E₁ naming inversion | `notes/foundations-and-geometry/03` names the isolated-zero disc E₀ and the zero-line upper half-plane E₁; legacy and current papers use the opposite assignment | Paper I §6–7 and the series notation table; `governance/01`, §17 (E₀ = basic hyperbolic model; E₁ fixed only after singular status) |
| C-2 | "threadlike" = every left child is a leaf | legacy `sec02-00`; used in knots notes | Paper I §2 intrinsic spine classification (Definition 2.x, sequential tree) |
| C-3 | ACS evaluation via the reversed path `ν_x(γ)=e^{M}x+∫_{C̄γ}e^M dA` | legacy `sec05` | Paper I §8 direct-path formula `ν_x(γ)=e^{M_γ}(x+∫_{C_γ}e^{−M}dA)` |
| C-4 | Laplace eigenvalue −2 claimed for μ=λ=1 | `archive/paper4p` abstract | Direct computation and Paper I §6/App C: `Δa=2a` (divergence-of-gradient convention) |
| C-5 | δ defined on coordinate functions and extended by Leibniz | legacy `sec07` | Paper I §9: δ_H restricted to scalar fields; no graded complex claimed |
| C-6 | torsion defined only against temporal reversal | legacy `sec05` | Paper I §8: relative torsion for arbitrary scale/charge-compatible pairs |
| C-7 | tube structure proposed inside Paper I | `archive/paper4p` | Paper III owns tubes; Paper I keeps only the regular total-zero-set lemma |
| C-8 | "dense singularity" from the lattice ℤ(1,0)+ℤ(0,φ) | `notes/knots-and-loops/05` | Wrong: the quotient is a compact Hausdorff torus; denseness is a property of the 1-D projection only. Note marked CORRECTED. |
| C-9 | contact CR / twisted harmonicity / Appell basis as Paper I content | legacy `sec06`, `sec08` | Paper II owns all of it; Paper I keeps only the contact form and horizontal bracket. |

---

## 4. Unincorporated reserve, by readiness tier

### Tier A — working-note proved, promotion candidates

Integration audit (statement/proof, conventions, domain data) required before
any paper entry; none is promoted by this audit.

1. `analysis-and-calculus/02` — mixed additive-multiplicative integration.
2. `analysis-and-calculus/03` — graded δ-calculus, twisted product, Rota–Baxter,
   dual weight-line geometry.
3. `thermodynamics-and-renormalization/05` — AEG↔thermodynamics contactomorphism
   and Maxwell transfer (plus the compatibility obstruction remark).
4. `thermodynamics-and-renormalization/07` — fixed-N algorithmic-thermodynamics
   contactomorphism.
5. `foundations-and-geometry/04` — affine torus holonomy toy model.
6. `foundations-and-geometry/05` (elementary part) — charge homomorphism vs
   ideals in ℤ and the normal-subgroup lattice.
7. `knots-and-loops/06` — Fox calculus ↔ affine cocycle (already partially in
   Paper III §8; the BS(1,2) calculation is extra).
8. `knots-and-loops/08` — small-knot embeddings in the three-parameter group.

### Tier B — computationally verified datasets

Preserve as data; any general claim needs presentation/mapping-dependence
analysis and a proof.

* `knots-and-loops/07`, `09`, `10`, `13` — relator→Alexander closure and
  torsion factorization tables (SageMath/snappy).
* `computation-and-resources/04` — Y-DAG pebble torsion and ghost-waiting
  closure (worked example).
* `archive/aristotle` — Lean verification of legacy statements (version-mismatch
  caveat, C-set above).

### Tier C — structural proposals and open programs

* `computation-and-resources/05`, `06` — PD₃ program and Route B 2-groupoid.
  Milestone 1 is well-posed with a pass/fail criterion and should be attempted
  or retired explicitly.
* `computation-and-resources/03` — Turing-machine resource torsion; blocking
  question is the classification of realizable memory-increment reorderings
  (the note's own falsifiability criterion).
* `foundations-and-geometry/01` — Cayley model; the K=−2 a.e. curvature claim
  is an open conjecture.
* `thermodynamics-and-renormalization/06`, `08` — algorithmic-thermodynamics
  bridge; carry `09`'s corrections.
* `projective-condensation/01` §10 — contact comparison conjecture for
  PSL₂(R)/unit tangent bundle vs the AEG horizontal distribution.

### Tier D — exploratory, superseded, or corrected

Retain in `notes/` as provenance; do not use as dependencies:

* `foundations-and-geometry/02` (E_alg bundle, ACS-as-fiber observation is the
  one salvageable idea), `thermodynamics-and-renormalization/01`–`04`,
  `knots-and-loops/03` (E_{4_1}, λ=φ²), `05` (corrected), `11`, `12`,
  `projective-condensation/02`.

---

## 5. Recommended dispositions

Each item requires a separate authorized task; this audit does not execute any
of them.

1. **Mixed-calculus technical note** (Tier A 1–2): consolidate into one
   self-contained note or a Paper II appendix expansion; audit the frame
   conventions against Paper II's scalar δ_H and the Paper I contact form.
2. **Thermodynamic correspondence note** (Tier A 3–4): standalone correspondence
   note or future series member; audit units/normalization and decide the
   destination before any paper placement.
3. **Torus toy calibration** (Tier A 5): optional appendix for Paper III
   (threading layer) or Paper IV (resource loops).
4. **Knot datasets** (Tier B): keep under `notes/` with the scripts; only the
   4₁ instance is currently used in Paper III.  A general
   "relator closure ⇒ Alexander polynomial" theorem is **not** authorized by
   the data and would need a proof of the presentation/mapping dependence.
5. **PD₃ Milestone 1** (Tier C): attempt `[κ]=μλ[du∧dv]≠0` on
   `T²_{u,v}×[a₋,a₊]` and the explicit PD dual class, or record why it is
   retired.  This is the cheapest concrete step of the whole reserve.
6. **TM resource torsion** (Tier C): solve or narrow the realizable-reordering
   classification before investing in further invariants.
7. **Cayley model** (Tier C): verify or falsify the K=−2 a.e. claim via the
   distributional curvature of the piecewise-linear conformal factor.
8. **Archive formalization** (Tier B): if cited anywhere, publish the
   legacy→current statement map first.

---

## 6. New open questions registered

The following were added to `governance/08-open-questions.md` by this audit:

* OQ-078 — Notes reserve: promotion candidates and their integration audits.
* OQ-079 — Notes reserve: conflict and correction ledger (C-1 … C-9).
* OQ-080 — Notes reserve: open programs with pass/fail criteria
  (PD₃ Milestone 1, TM realizable reorderings, Cayley K=−2, algorithmic-thermo
  bridge, contact-comparison conjecture).

All are Priority P3 (research; they do not block Papers 0–IV).

---

## 7. What this audit deliberately does not do

* It does **not** edit any paper source, appendix, or bibliography.
* It does **not** promote any note from its recorded grade.
* It does **not** assign any unincorporated material to a paper; dispositions
  above are recommendations only.
* It does **not** delete or rename any note, including the corrected one
  (`knots-and-loops/05`), which is retained with its correction recorded in C-8.
* It does **not** resolve the conflicts in Section 3; they remain recorded and
  are governed by the existing priority order until closed by an authorized task.
