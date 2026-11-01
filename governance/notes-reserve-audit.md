# Notes Reserve Audit

**File:** `governance/notes-reserve-audit.md`
**Status:** Audit record (inventory and status register for `notes/`; non-authoritative, does not revise scope)
**Version:** 1.1
**Date:** 2026-08-10; amended 2026-09-29, 2026-10-31
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

**Amendment (2026-09-29).** Four notes were added to
`notes/foundations-and-geometry/` after version 1.0, so that section 2 no longer
covered every note under `notes/`. Rows for `07`, `08`, `09` and `10` were added
to section 2.1, corresponding entries to section 4, and one new conflict,
C-10, to section 3. A file-by-file comparison carried out at the same time
showed that the gap was wider than that: nine notes present before this amendment
had never been covered either, and `foundations-and-geometry/06` was one of them.
`06` is now graded in section 2.1, and the remaining nine are recorded, ungraded
and explicitly so, in the new section 2.7. The amendment extends coverage; it
does not revise any grade assigned in version 1.0, promote any note, or change
any paper claim. The notes added are themselves exploratory records, and the one
substantive consequence — that a registered Paper 0 claim is refuted as printed —
is recorded in C-10 and carried into the registers it names, not decided here.

**Amendment (2026-10-31).** One note was added to
`notes/analysis-and-calculus/` after the 2026-09-29 amendment:
`09-order-topology-scott-lawson`. It was first recorded ungraded in section 2.7's
coverage-gap list (counts nine→ten) and then, on the same date, read and graded:
section 2.2 gains a row and section 4 Tier C a bullet, and section 2.7 reverts to
nine. The grade is `STRUCTURAL PROPOSAL` + `REFORMULATION` — the classical
domain-theory content is marked `CLASSICAL` in the note, the AEG instantiations
(prefix-order information order, additive = way-below, multiplicative =
Scott-automorphism, backward adjoint = reciprocal, separate Scott-continuity) are
correct reformulations, and the integrative "missing-involution = backward
adjoint = order-topology-analysis foundation" reading is a structural proposal,
not a theorem. Three companion open questions (OQ-091–OQ-093) are added to
`governance/08-open-questions.md`; OQ-092 and OQ-093 are resolved, OQ-091 is
partially resolved with the branching-history case still open.

**Amendment (2026-10-31, second).** Eleven further notes were added to
`notes/analysis-and-calculus/` on the same date, continuing the thread opened by
`09` and applying it to the Paper I main body and the Paper 0 contact structure:
`10`–`20`. Section 2.2 gains one consolidated row for the thread (the eleven
notes are graded together, since they form one continuous argument), section 4
Tier C gains a thread bullet, and the residuals are registered as OQ-094
(094a–094d, resolved in `11`–`16`) and OQ-095 (macro Stokes and the full DAG Lie
realization, open). The thread's grade is `STRUCTURAL PROPOSAL` + `REFORMULATION`
(+ `CLASSICAL`), with two provable sub-results noted explicitly: the monotonicity
obstruction of `14` Theorem 1 (`WORKING-NOTE PROVED`) and the computational
verifications (`D_{-1}=T_1¬T_{-1}¬T_1¬`, the BCH density, the ends enumeration).
No paper source is edited and no claim is promoted by this amendment; the
consolidated disposition is recorded in
`governance/scott-lawson-paper-1-integration-2026-10-31.md`.

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
| 06-hole-obstructions-ledger | Retained provenance copy | COMPUTATIONALLY VERIFIED EXAMPLE + `EXPLORATORY` reading | Added to the reserve 2026-09-22, after version 1.0, so it was missing from the earlier inventory; added here 2026-09-29. A verbatim copy of the exploration register `temp/孔的不可避免性_v0.1.md` with a status header prepended, retained so that the citations in `paper-0/sections/11-holed-aes.tex` point at a tracked file (cited there as `Yuan2026AEGHoleRegister`). Six classes of computed obstruction with their scripts; the "hole carries exchange" sentence is the chapter's motivation and is **not** proved by any of the six witnesses — Paper 0 §11.6 records exactly that as a non-claim. Not to be used as a dependency. |
| 07-joint-quotient-acs-charge-aes-operator | Unincorporated | WORKING-NOTE PROVED | Added 2026-09-29. The joint quotient `G = ℝ_A × Aff⁺(1,ℝ)` of the ACS charge endpoint and the AES affine operator; its centre and derived subgroup are characteristic; the two readouts are the two projections, with kernels `[G,G]` and `Z(G)`; the pair recovers the group element by the fibre product `G ≅ 𝔼² ×_ℝ ℍ²`; the contact form `α = dB − dA − B dM` has non-integrable horizontal distribution (`[X,Y] = ∂_B`), so the order defect is the non-integrability. **Integration audit required**; `G` is not a Paper 0 object and Paper 0 owns ACS, AES and the contact structure. |
| 08-isometric-realisations-thurston-geometries | Unincorporated | WORKING-NOTE PROVED (classification cited as standard) | Added 2026-09-29. Lossless realisation `ρ: G → Isom(X)` with diffeomorphic orbit map exists exactly for `ℍ²×ℝ` and `SL~₂(ℝ)`; the other six models are excluded by an adjoint-spectrum argument (𝔼³, 𝕊³, 𝕊²×ℝ, Nil), by the centre (ℍ³) and by the dimension of the derived subalgebra (Sol). The identification that Paper 0 §9's contact model, after a Reeb unit extension and the inversion `I(A,M,B)=(−A,−M,−Be^{−M})`, **is** the `SL~₂(ℝ)` geometry (`I*α = ω = dA − e^{−M}dB`, `I*g_contact = F*g_SL`) is the reusable part. **Integration audit required**; the eight-geometry classification itself is cited, not re-derived. |
| 09-automorphisms-dilation-and-obstructions | Unincorporated | WORKING-NOTE PROVED | Added 2026-09-29. All Lie automorphisms are `F_{α,γ,δ,κ}(A,S,B) = (αA + γ log S, S, δB + κ(S−1))`, `αδ ≠ 0`; the inner ones are exactly `α=1, γ=0, δ>0`; `Φ_λ(A,S,B)=(λA,S,λB)` implements the plane similarity, `D_λ T_g D_λ^{−1} = T_{Φ_λ(g)}`, and is outer for `λ≠1`; the outer hierarchy `Φ_2^n(Γ)` has trivial intersection whereas the inner one leaves `ℤ×{0}`; `γ≠0` is obstructed twice — `log` is not semialgebraic, and the point-stabiliser argument forbids a plane conjugation. **Integration audit required**. |
| 10-punctures-are-critical-counterexample-record | Unincorporated | EVIDENCE RECORD (exact refutation; not a promotion candidate) | Added 2026-09-29. Retains a verified counterexample to `thm:p0-punctures-are-critical` so that the accompanying review has a tracked referent, in the same spirit as `06-hole-obstructions-ledger.md`. The model is a punctured AES with a smoothly extending assignment and `S = {0} ≠ ∅ = Crit(ã)`; the gap is that the proof constructs a new metric and calls it an extension of the given `g`. Disposition is bound to C-10; this record changes no claim status by itself. |

### 2.2 `notes/analysis-and-calculus/`

| File | Disposition | Grade | Current status / destination |
| --- | --- | --- | --- |
| 01-horizontal-analysis-program | Incorporated | program | Realized by Paper II: operator selection (factorization vs variational), frame drift `Δ_g = X_u²+X_v²−c_vX_u+c_uX_v`, Appell modules, boundaries. |
| 02-mixed-affine-integration | Unincorporated | WORKING-NOTE PROVED | Continuous mixed integral `∫u·exp(∫_x^b v)`, transport/splitting/window-derivative identities, adjoint pairing, continuous ACS triple identity. Complete proofs; **integration audit required** (which paper, which conventions). |
| 03-weighted-contact-calculus | Unincorporated | WORKING-NOTE PROVED | Graded covariant differential `∇^{(n)}f=δf−nf dM`, graded Leibniz law, gauge rectification `ã=e^{−M}a`, twisted product `⋆_M` with derivation `D_M`, twisted Rota–Baxter identity, dual weight-line adjoint geometry, E₀/ACS structure equations `dω_A=ω_M∧ω_A`. Complete proofs; **integration audit required**. |
| 09-order-topology-scott-lawson | Unincorporated | STRUCTURAL PROPOSAL + REFORMULATION | Reference vocabulary (Scott/Lawson/way-below/ideal completion, cited `CLASSICAL`) plus a faithful instantiation to AEG marked spinal histories: information order = chronological prefix order, ideal completion = finite∪infinite histories (OQ-091, partial — branching case open); additive = way-below, multiplicative = Scott-automorphism, dual = reciprocal involution (OQ-092, resolves and corrects the §6 wording); backward adjoint `p=¬(K)` mod constant, join = Lawson = Euclidean (OQ-093); mixed integral separately Scott-continuous (functional pairing). The integrative "missing-involution = backward adjoint = order-topology-analysis foundation" reading is a structural proposal, not a theorem. |
| 10–20 (Scott–Lawson thread) | Unincorporated | STRUCTURAL PROPOSAL + REFORMULATION (+ CLASSICAL); two proved sub-results | One continuous argument (2026-10-31) reading `09` back into the Paper I main body and the Paper 0 contact structure. `10` generator correspondence `T_s=C_{+,s}^{(1)}`, `D_k=C_{×,k}^{(1)}`, `¬=C_{/,1}^{(2)}`; `11`–`13` OQ-094a (Scott ⟷ `Aff^+`, Lawson ⟷ `PGL₂`, "adjoin ¬" commutes, **not** a Galois equivalence); `14` OQ-094b (`ρ` monotone only for the trivial preorder — **`WORKING-NOTE PROVED` Theorem 1** — and the only candidate extension is the infinite matrix product = continued fraction, out of Paper I scope); `15` OQ-094c (branching-history dcpo: information order = down-set embedding, `Idl(FinDAG)` = finite∪infinite DAGs, Birkhoff `O(P)`, prefix = chain specialization — `CLASSICAL` ideal completion instantiated); `16` OQ-094d (Hecke history space = Cantor, `G₄≅C₂*C₄` ends = Cantor, `H(√2)` first-kind limit set = circle; corrects `10` §4); `17`–`18` contact curvature = minimal-DAG order defect (generators = exact flows, order defect = Lie bracket `[D_u,D_v]=μλ∂a`, BCH); `19` holographic Stokes + bulk-boundary (bulk flat, defect = boundary holonomy — `STRUCTURAL PROPOSAL`); `20` defect is a group-valued 1-cocycle (telescoping additivity, local defect = conjugated commutator, hexagon = Jacobi identity — **`WORKING-NOTE PROVED`**, though largely classical/trivial). Computational checks: `D_{-1}=T_1¬T_{-1}¬T_1¬`, the BCH density `μλ`, the ends enumeration. The integrative "Contact = the DAG language of volume computation" and the bulk-boundary ("holographic") readings are structural proposals, not theorems. Residuals: OQ-095 (higher-order brackets, full DAG Lie realization, macro Stokes, spectral docking). Disposition in `governance/scott-lawson-paper-1-integration-2026-10-31.md`. |
| 25-pants-interface-disks-and-substitution | Unincorporated; new thread | STRUCTURAL PROPOSAL + PROVED WITH STATED HYPOTHESES (working note; integration audit required) | Specifies decorated ball-and-tube thickening, surface pants and internal interface disks; gives finite topological proofs, the polynomial substitution/character example, and the constant-boundary regular-AES disk obstruction. Canonical AEG realization, general decorated composition and the native Seal bridge remain open (OQ-096). V1 now has executed same-author finite evidence: 56 cubes, 336 tetrahedra, local links, surface/body filling distinction, substitution and ten negative controls; general V2–V4 obligations remain open. Does not promote or rewrite notes 15–24 or manuscript claims. Direction: Mingli Yuan; construction, proofs and drafting: Codex (OpenAI), 2026-10-31. |
| 21–24 (series theory + cross-project correspondence) | Unincorporated | STRUCTURAL PROPOSAL + REFORMULATION (+ CLASSICAL); one computationally verified example | Continuation of the `10`–`20` thread (2026-10-31). `21` series theory = Magnus expansion into the free Lie algebra, with the arity-`k` ↔ (`k−1`)-cell correspondence (low orders 1–3 **`COMPUTATIONALLY VERIFIED EXAMPLE`** via the `E₁₂,E₂₃,E₃₄` nilpotent model, coefficient `hkl/3`; general arity-`k` is `OPEN`/`STRUCTURAL PROPOSAL` — OQ-095.1/095.2) and the bulk-boundary triple reduction; `22` cross-project Wu/Yang/Zhang ↔ AEG semi-direct/distributivity/defect correspondence (skeleton with `[Adva]`/`[AEG]`/`[对应]` marking); `23` difference substitution = abelianized Magnus via PBW (`CLASSICAL` BCH/PBW + `structural proposal`); `24` nondegeneracy condition = defect `μλ` and weak nondegeneracy = level-by-level penetration (`structural proposal`, with the honest note that `lc=0` is non-invertible vs `μλ=0` is integrable). Residuals: OQ-095 (macro Stokes, full DAG Lie realization, spectral docking). No paper claim promoted. |
| 26-donaghey-general-to-binary-tree | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL (structural correspondence; integration audit required) | Reads Donaghey 1980, Pushkarev–Byzov 2014 and OEIS A014486; aligns the general-tree ↔ binary-tree bijections with AEG's tree layer. Tight `[对应]`: Donaghey's σ (left/right transposition) ↔ AEG mirror `m`; θ (Dyck reflection) ↔ temporal reversal `r`; φ (PPCT↔Dyck) ↔ up-down code; right/left bijection ↔ `conv:p0-left-right-convention` (right/left comb); four Catalan families ↔ binary (sequential) vs general (branching) trees. Records the non-commutative difference: AEG word-level `⟨m,r⟩ ≅ Z₂×Z₂` (Klein), whereas Donaghey tree-level `⟨σ,θ⟩ ≅ Z₂*Z₂` (infinite dihedral) with `τ` of infinite order (Pushkarev–Byzov Thm 6.4, Cor 6.3). Also records carousel effect, fringing theorem, `O(n^{log₂3})` orbit growth, PPCT distributive-lattice claim. Residuals registered as OQ-098 (non-commutative extension, PPCT lattice vs `O(P)`, carousel/orbit correspondence, functoriality). No paper claim promoted. |
| 27-mirror-reversal-tree-layer | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL (structural correspondence; integration audit required) | Advances OQ-098.1. Establishes that AEG's mirror `m` and reversal `r` commute (`def:mirror-temporal-reversal`), so `⟨m,r⟩ ≅ Z₂×Z₂` (Klein); the word ↔ comb bijection (`prop:marked-tree-history-correspondence`) preserves commutation, so the marked-history (single-spine comb) layer is Klein — the non-commutative `Z₂*Z₂` is **not** obtained by transporting AEG's existing operations to trees. Donaghey's `σ` equals `m`, but `θ̃=φ⁻¹θφ` (Dyck-path reflection) is not AEG's `r` (word reversal); `τ`'s infinite order and arbitrarily long orbits are constructed on branching trees (complete tree + fringing, Pushkarev–Byzov Cor 6.3), so the non-commutative extension belongs to the branching layer (`O(P)`, linear extensions). Includes an `n=2` comb computation confirming `mr=rm`, and the companion finite verification `research/donaghey-orbits/` (implements `τ` per Pushkarev–Byzov Def. 2.1; reproduces Donaghey's `M_n(x)` for `n=1..10`; shows caterpillars are not `τ`-invariant and all orbits of length `>6` are branching) — `COMPUTATIONALLY VERIFIED EXAMPLE`, `n≤10`, not a general proof. Shifted residuals: `θ̃` naturality, branching-layer lift of `τ`, exact order of `τ` on combs. No paper claim promoted. |
| 28-ppct-lattice-attribution | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL (lattice attribution; integration audit required) | Advances OQ-098.2. Separates the two candidate lattices on PPCTs: (A) the Tamari / rotation lattice is a lattice but **not distributive** (witness for `T_4`, `n=5`, `research/ppct-lattice/`); (B) the Birkhoff down-set lattice of the infinite binary (cubic) tree is distributive with join-irreducibles = the vertices and `R(N)=Catalan(N)` down-sets of size `N`. The Pushkarev–Byzov phrase "distributive lattice whose irreducibles are ordered as the vertices of the infinite cubic tree" matches (B), while "standard lattice ordering of all trees" is (A); the two are mutually exclusive, so the source phrase conflates them. AEG's `O(P)` is the same Birkhoff construction over a finite dependency poset, hence the distributive reading aligns with AEG but the two are not isomorphic in general. Residuals: sublattice embedding of `O(P)` into a down-set lattice over `T_∞`, and the precise source meaning of "standard lattice ordering". No paper claim promoted. |
| 29-branching-layer-descent | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (n<=8; integration audit required) | Advances OQ-098.1(b), resolving it negatively. AEG's dependency poset (`def:internal-dependency-poset`) is the internal skeleton (descendant order), which forgets the planar left/right data. Donaghey's `τ` does **not** respect dependency-poset isomorphism: two trees with isomorphic dependency posets can map to trees whose dependency posets differ (explicit `n=4` witness: a 3-chain class member maps to a 3-chain, another to a "V"; every skeleton class has a non-unique `τ`-image for `n≥5`, verified `n≤8`). Hence `τ` does not descend to `P` or `O(P)`, and the hyperbolic/long-orbit behaviour is strictly a planar-tree phenomenon, not a poset-layer one. Residuals: general-`n` proof of non-descent; whether the branching layer has its own (non-τ) hyperbolic structure; exact planar data needed for a well-defined descent. No paper claim promoted. |
| 30-donaghey-aeg-tree-layer-overview | Unincorporated; synthesis | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (integration audit required) | Synthesis of notes 26–29 (OQ-098 line). One-line: the Donaghey/De Bruijn–Morselt general-tree ↔ binary-tree transform matches AEG's tree layer precisely (σ↔mirror `m`, θ↔temporal reversal `r`, φ↔up-down code, R/L↔left/right comb), but its non-commutative `Z₂*Z₂` / hyperbolic long-orbit structure belongs to the planar-tree layer, not to the comb layer (098.1: AEG's `m,r` give `Z₂×Z₂`/Klein; caterpillars not τ-invariant, long orbits all branching, verified `n≤10`) and does not descend to the dependency poset / `O(P)` (098.1(b), verified `n≤8`). The 'PPCT distributive lattice' is the Birkhoff down-set lattice of the infinite cubic tree, not the Tamari/rotation lattice (098.2). Residuals: 098.1(a) `θ̃` naturality, 098.2 sublattice embedding / source meaning, 098.1(b) general-`n` and branching-layer own dynamics, 098.3 carousel↔Hecke, 098.4 functoriality. No paper claim promoted. |
| 31-carousel-and-iota | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (conjecture; integration audit required) | Investigates the user's guess carousel <-> iota. Three distinct iotas separated: (A) AEG cut contraction in the six-state carrier (`c_i=ε_i+ι_i`, `Ω=TSR`, `Ω²=-1`, chirality sign law even-preserves/odd-flips); (B) Adva **iota frame** = complex structure `J²=-I` on doubled cut coordinates; (C) Adva **iota combinator** (SKI basis; adva `0168` rules out braid/swap under it). Key finding: AEG's six-state carrier and Adva's `0010` chirality carrier `W=(T⊕SR)⊕(S⊕RT)⊕(R⊕TS)` are the same 6-dim space with `J²=-I` (so AEG iota = Adva iota frame). Carousel: class-level core is a 4-cycle (`LL→RL→RN→LN`), count shadow is an involution (order 2, verified `n≤7`, `research/donaghey-orbits/verify_carousel.py`). Conjecture: carousel 4-cycle = discrete shadow of the iota complex unit, with index `k` a separate shift; the order-2 vs order-4 mismatch is open. Residuals: class->carrier map, action alignment, order mismatch, fringing/exp relation. No paper claim promoted. |
| 32-carousel-iota-alignment | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (refutes strong form; integration audit required) | Attempts note 31 §4's two items (class->carrier map; carousel = J?). Verifies `Ω²=-I`, `Ω⁴=I`, J preserves each plane `W_T,W_S,W_R`, and on each plane's four signed states J is a single 4-cycle (`research/iota-carousel/`). Strong form "carousel = J on the six states" is **refuted**: J sends positive states to signed states (`SR↦-T`), preserves planes, and the carousel has 5 classes. The carousel's class-level 4-cycle `LL→RL→RN→LN→LL` can be aligned (non-canonically; 3 planes × 2 orientations = 6 candidates) to J's 4-cycle on one plane's signed states; but the `SR→LL` entry and the index shift have no J counterpart. So carousel = (J-type rotation) + (shift); the shift's iota carrier is open (candidate: Laplacian `H` or `Λ¹↔Λ²` grading). No paper claim promoted. |
| 33-shift-research | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (negative result; integration audit required) | Advances the shift question of note 32. The iota frame is a **screw**: `[J,H]=0`, `J²=-I`, `A=-JH`, `A²=-H²`, `exp(tA)=cos(tH)-J sin(tH)` (rotation angle ∝ H eigenvalue) — verified. But `H` **cannot** carry the carousel index `k`: the cut graph is the down-set Hasse diagram of the dependency poset (forgets left/right), while `k = #left leaves` is planar; at `n=4` four trees share the same cut-graph spectrum yet have `k=3,2,1` (`research/iota-carousel/verify_shift.py`). Same planarity obstruction as note 29. So the shift needs a planar, unbounded carrier (candidates not established). No paper claim promoted. |
| 34-planar-carrier | Unincorporated; new thread | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE (construction; integration audit required) | Constructs the explicit **screw module** `V = V_class ⊗ V_index` with `V_class=⟨LL,RL,RN,LN⟩` (planar: left/right × leaf/nonleaf) and `V_index=⟨e_k:k≥1⟩` (unbounded). Operators `J:(c,k)↦(c+1,k)` (iota complex unit, Z/4), `S:(c,k)↦(c,k+1)` (shift/height), carousel `C:(c,k)↦(c+1 mod 4, k+[c=LN])`. Verified (all True, `research/iota-carousel/verify_planar.py`): `C⁴=S` (carousel is a **screw** / projective Z/4 = 4th root of the shift), `J⁴=id`, `[J,S]=0`, count shadow `M²=id` (screw invisible to counts). So a planar carrier exists; the iota supplies `J` (rotation half), `S` (height) is independent. Residuals: derive `S` from AEG/Adva; absorb `SR`/wrap; word/history Z/4; corner-level Thm 4.3. No paper claim promoted. |
| 35-derive-shift | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (partial derivation; integration audit required) | Derives the shift `S` of note 34 from an AEG-native structure. The carousel index `k` is a **traversal position** (Pushkarev–Byzov Thm 4.2); AEG's **chronological index** of the marked history (`def:marked-spinal-history`, `eq:chronological-history-concatenation`) is the natural unbounded position + successor, so `S` = the chronological successor (append one context). Layered precision: **left comb** exact (DFS left traversal = spine order = chronological); **right comb** differs by a left/right flip (DFS visits off-spine left leaf first); **branching** layer parts ways (DFS ≠ linear extension), same gap as note 29. Verified `research/iota-carousel/verify_traversal.py`. Residuals: branching-layer `S`; direct vs semi-direct `V_class⊗V_index`; general `n`; cut-basis/clock index vs word index. No paper claim promoted. |
| 36-branching-layer-shift | Unincorporated; new thread | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE (derivation; integration audit required) | Derives the branching-layer `S`. Corrects note 35: its 'left traversal' was the **preorder**; the chronological/evaluation order is the **postorder**. Verified: the **left-first postorder** of internal nodes is a **linear extension** of the dependency poset for every PPCT (`n≤5`), and equals the chronological order `[2,1,0]` for **both** left and right combs; the preorder is not a linear extension. So `S` = the postorder successor = 'advance along the canonical (left-first) spinal history' (`thm:birkhoff-downset-spinal`), planar (left-first), unbounded, AEG-native. Residuals: corner-order vs evaluation-order alignment (Thm 4.2), left/right-first choice, general `n`, relation to note 29's descent obstruction. No paper claim promoted. |
| 37-corner-order-alignment | Unincorporated; new thread | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE (alignment; integration audit required) | Derives the corner-order ↔ evaluation-order alignment. OCR of Pushkarev–Byzov confirms: "corner" = **vertex** (SR/LL/RL/LN/RN classify vertices), and the **left standard traversal is the PREORDER**. So the carousel `k` is a preorder position; the evaluation order is the postorder. Alignment (paper Remark + computation, `research/iota-carousel/verify_corner_order.py`): **leaves** — preorder = postorder (left-to-right frontier); **nonleaf chains** — inverted; **across incomparable chains** — a choice (balanced tree fails global reversal). Hence `S` for the carousel `k` = **preorder (corner) successor**; note 36's `S` = postorder is the evaluation order, equal on leaves and inverted on nonleaves. Residuals: canonical cross-chain choice; general `n`; `S`-to-screw; distinguish note 29's multi-valued descent from the corner-order-not-linear-extension gap. No paper claim promoted. |
| 38-canonical-cross-chain-choice | Unincorporated; new thread | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE (canonicalization; integration audit required) | Canonicalizes note 37's cross-chain choice: define the canonical linear extension as the one **minimizing inversions (Kendall tau) with the corner order (preorder)**. Verified for all PPCTs with `n=4,5` (`research/iota-carousel/verify_canonical_choice.py`): the minimizer is **unique** and equals the **left-first postorder**. So `S` (note 36) is not an arbitrary left-first pick but the unique evaluation order closest to the corner order; the 'choice' is resolved. Structural reason: preorder and postorder differ only in the root position, the left-first order preserved. Residuals: general-`n` proof; other intrinsic criteria (leaf-order preservation) giving the same minimizer; σ-equivariance; formal separation from note 29. No paper claim promoted. |

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

### 2.7 Coverage gap (recorded 2026-09-29)

This audit's "Applies to" line claims every note under `notes/`. A file-by-file
comparison of section 2 against the working tree on 2026-09-29 found **nine notes
that version 1.0 never covered** and that the 2026-09-29 amendment does not
grade, because grading them requires reading them and no such reading has been
done here:

* `notes/analysis-and-calculus/` — `04-hyperoperation`,
  `05-hyperoperation-calculus`, `06-process-concept-representation`,
  `07-reflection-on-coordinates`, `08-reflection-on-measurement-systems`;
* `notes/knots-and-loops/` — `11-figure-eight-presentation-problem-zh`,
  `12-knot-presentation-questions-zh`;
* `notes/thermodynamics-and-renormalization/` —
  `03-aeg-flow-and-renormalization-zh`,
  `04-renormalization-iteration-examples-zh`.

Two of the eight subject directories are fully covered; four are not. Nothing is
asserted here about the content of these files. Until a separate authorized task
reads and grades them, this audit covers **all but nine** of the notes under
`notes/`, and the "Applies to" line above should be read with that qualification.
The same check should be re-run whenever notes are added.

### 2.8 Archival cross-references (one-line each)

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
| C-10 | `thm:p0-punctures-are-critical` is false as printed | `notes/foundations-and-geometry/10` and the root review `AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md`; counterexample verified symbolically | **UNRESOLVED — recorded, not reconciled.** The printed statement assumes only that `a` extends smoothly; the proof's first step builds `g~ = |dã|²_{g₀} g₀ / (μ²+λ²ã²)`, which satisfies the eikonal identity but is *not* an extension of the given `g`, whereas condition (ii) of `def:p0-punctured-aes` requires extending `g` itself. `cor:p0-puncture-count` inherits the gap. The reverse inclusion `Crit(ã) ⊆ S` and `thm:p0-four-circle-model` are unaffected. Amended in `governance/05b-paper-0-status-register.md` and `governance/08-open-questions.md` (OQ-082); the paper source is **not** edited by this audit. |

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
9. `foundations-and-geometry/07` — joint quotient of the ACS charge and the AES
   affine operator (added 2026-09-29).
10. `foundations-and-geometry/08` — isometric realisations in the Thurston
    geometries, including the identification of Paper 0 §9's contact model with
    the `SL~₂(ℝ)` geometry (added 2026-09-29).
11. `foundations-and-geometry/09` — automorphisms of the joint group, dilation,
    and the two obstructions to `γ≠0` (added 2026-09-29).

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

* `analysis-and-calculus/25` — new pants/interface-disk/substitution thread
  (2026-10-31), OQ-096. Short conditional proofs are supplied inside a specified
  finite model, including the constant-boundary regular-AES capping obstruction.
  Its semantic/geometric identification and native Seal bridge remain open;
  it is not a manuscript promotion candidate as a whole.

* `analysis-and-calculus/09` — Scott/Lawson reference vocabulary plus a faithful
  AEG instantiation (prefix-order information order, additive = way-below,
  backward adjoint = reciprocal, Lawson = Euclidean). The integrative
  "order-topology analysis" reading is a structural proposal; the
  branching-history dcpo remains open (OQ-091).
* `analysis-and-calculus/10`–`20` — the Scott–Lawson thread (added 2026-10-31):
  reads `09` into the Paper I main body and the Paper 0 contact structure. The
  provable core (OQ-094a–d resolved; contact curvature `μλ` = minimal-DAG order
  defect; defect is a 1-cocycle) assembles `CLASSICAL` domain/Lie theory and
  `proved in paper-0/paper-1` facts; the integrative "Contact = the DAG language
  of volume computation" and the bulk-boundary ("holographic") readings are
  structural proposals. Residuals: OQ-095 (higher-order brackets, full DAG Lie
  realization, macro Stokes, spectral docking). Not a promotion candidate as a
  whole; any paper entry requires the integration audits of
  `05-mathematical-status.md` §4.
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

### Tier E — evidence records (added 2026-09-29)

Retained so that a review has a tracked referent; not promotion candidates and
not dependencies:

* `foundations-and-geometry/10` — counterexample record for
  `thm:p0-punctures-are-critical`. Its disposition is bound to C-10. Together
  with the root review it is the evidence behind the amendments to
  `governance/05b-paper-0-status-register.md` and `governance/08-open-questions.md`;
  it is not itself a status record.

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
9. **Joint-quotient notes** (Tier A 9–11, added 2026-09-29): decide the
   destination of `07`–`09` before any paper placement. `07` and `09` are new
   organising objects around `G` and must not be attributed to Paper 0; `08`
   contains one item that looks directly reusable — the identification of
   Paper 0 §9's contact model with the `SL~₂(ℝ)` geometry after the Reeb unit
   extension and the inversion — and that single proposition can be audited on
   its own, independently of the rest.
10. **C-10 counterexample** (Tier E, added 2026-09-29): decide whether to
    restate `thm:p0-punctures-are-critical` under the conformal-extension
    hypothesis, to widen `def:p0-punctured-aes` so that the counterexample class
    is excluded, or to narrow the claim. The paper source is not edited by this
    audit; C-10 stays open until an authorized task closes it.
11. **Close the coverage gap** (§2.7, added 2026-09-29): read and grade the nine
    notes this audit has never covered, so that its "Applies to" line becomes
    true. This is bookkeeping, not mathematics, and is the cheapest item here.

---

## 6. New open questions registered

The following were added to `governance/08-open-questions.md` by this audit:

* OQ-078 — Notes reserve: promotion candidates and their integration audits.
* OQ-079 — Notes reserve: conflict and correction ledger (C-1 … C-10).
* OQ-080 — Notes reserve: open programs with pass/fail criteria
  (PD₃ Milestone 1, TM realizable reorderings, Cayley K=−2, algorithmic-thermo
  bridge, contact-comparison conjecture).

All are Priority P3 (research; they do not block Papers 0–IV).

The 2026-09-29 amendment registers **no new open question**. C-10 belongs to an
existing Paper 0 item and is carried into `governance/08-open-questions.md` by
amending OQ-082 rather than by opening a parallel question; OQ-079's ledger
range is updated to C-1 … C-10 accordingly.

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
* It is a **dated snapshot**. Version 1.0 covered the notes present on
  2026-08-10; the 2026-09-29 amendment extends it to the four notes added since.
  Any note added later must be appended the same way, or this file stops
  covering what its "Applies to" line claims.

