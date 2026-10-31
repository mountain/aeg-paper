# Scott–Lawson 拓扑落回 Paper I 主体：整合登记

**File:** `governance/scott-lawson-paper-1-integration-2026-10-31.md`
**Status:** Integration record (research-thread summary and registration; does not
revise scope or promote any claim)
**Date:** 2026-10-31
**Prepared by:** DeepSeek Harness (AI coding agent) under the repository author's
direction; all mathematical statuses use the vocabulary of
`governance/05-mathematical-status.md` and `governance/notes-reserve-audit.md`,
and no claim status is changed here.
**Depends on:**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/05-mathematical-status.md`
* `governance/08-open-questions.md`
* `governance/notes-reserve-audit.md`

**Applies to:** `notes/analysis-and-calculus/09`–`20`, and their contact with
`paper-1/sections/02-sequential-histories.tex`,
`paper-1/sections/03-projective-affine.tex`, and
`paper-0/sections/09-contact-of-tearing.tex`.

---

## 1. Purpose and provenance

This record registers a single continuous research thread carried out in
2026-10-31: read the recent Scott/Lawson vocabulary note
`notes/analysis-and-calculus/09-order-topology-scott-lawson.md` back into the
**main body of Paper I** (the history layer and the projective semantics), and
from there into the **contact structure of Paper 0 §9**. The thread produced
twelve new notes (`10`–`20`) and closed the four sub-items of OQ-094, and it
ends in a single precise statement:

> **The contact curvature `μλ` is the order defect of the minimal branching
> DAG `{add, multiply}`, integrated (as a 1-cocycle) over the region between two
> threads; the bulk (finite DAG) is flat, and the defect is a boundary holonomy
> living on the ideal boundary (the surface).**

No Paper I or Paper 0 theorem is changed, added, or promoted by this thread.
The thread is a **structural reading** that connects existing proved facts
(Paper 0's `thm:contact-curvature`, `thm:torsion-stokes`,
`thm:legendre-dual-tearing`; Paper I's `thm:bilateral-pgl2-generation`,
`cor:affine-borel-sector`) to the domain-theoretic structure of Paper I's
histories.

---

## 2. The spine (notes 09–20)

| Note | Content | Status (grade) |
|---|---|---|
| `09` | Scott/Lawson vocabulary; prefix-order information order; additive = way-below, multiplicative = Scott-automorphism, dual = reciprocal; ideal completion = finite∪infinite histories | STRUCTURAL PROPOSAL + REFORMULATION (OQ-091 partial, OQ-092/093 resolved) |
| `10` | The generator correspondence: `T_s = C_{+,s}^{(1)}`, `D_k = C_{×,k}^{(1)}`, `¬ = C_{/,1}^{(2)}`; mapping to Paper I §2–§3 | STRUCTURAL PROPOSAL + REFORMULATION |
| `11` | OQ-094a proof skeleton: Scott ⟷ `Aff^+`, Lawson ⟷ `PGL₂`; correction of `10` §2 (`Aff^+`, `B_∞^+`, `B_∞`, `PGL₂` levels; `D_{-1} = T_1¬T_{-1}¬T_1¬`) | 094a RESOLVED |
| `12` | Galois connection: homeo level `{D_k}` ↦ `Stab([0,∞])`, endo level `Aff^+` ↦ `PGL₂` | 094a RESOLVED |
| `13` | Functorial language: commutative diagram + naturality `Φ(σ∨¬_*σ)=⟨Φ(σ),¬⟩`; not a full Galois equivalence | 094a RESOLVED |
| `14` | 094b: `ρ` monotone only for the trivial preorder; no Scott-continuous extension; only candidate = infinite matrix product = continued fraction (out of scope) | 094b RESOLVED |
| `15` | 094c: branching-history dcpo; information order = down-set (ideal) embedding; `Idl(FinDAG)` = finite∪infinite DAGs; Birkhoff `O(P)`; prefix = chain specialization | 094c RESOLVED (core) |
| `16` | 094d: Hecke history space = Cantor; `G₄ ≅ C₂*C₄` virtually free (ends = Cantor); `H(√2)` first-kind (limit set = circle); correction of `10` §4 | 094d RESOLVED |
| `17` | Contact curvature = order defect of `{A,M}`; Birkhoff `Stone(O({A,M}))={A,M}`; refinement: DAG flat, curvature from non-commutative realization | REFORMULATION + STRUCTURAL PROPOSAL |
| `18` | Limit/smoothing functor: generators = exact flows; word = composition; order defect = flow commutator = Lie bracket `[D_u,D_v]=μλ∂a` (BCH) | proved (ingredients) |
| `19` | Integration + bulk-boundary: holographic Stokes; bulk flat, curvature = boundary holonomy; discrete Stokes on `O(P)` (open) | STRUCTURAL PROPOSAL + open |
| `20` | Defect is a group-valued 1-cocycle: telescoping additivity; local defect = conjugated commutator; BCH expansion; hexagon = Jacobi identity | proved (ingredients) |

The chain is: **09 (vocabulary) → 10 (generator correspondence) → 11–16 (OQ-094 a–d) → 17–18 (contact = DAG defect) → 19 (bulk-boundary) → 20 (1-cocycle)**.

---

## 3. Provable core (what this thread establishes)

The following are **proved from existing sources** (Paper 0, Paper I) plus
`CLASSICAL` domain theory / Lie theory; none is a new Paper theorem, all are
readings or assemblies of proved facts:

1. **Generator correspondence** (`10` §1): `T_s`, `D_k`, `¬` are literally
   Paper I's elementary contexts `C_{+,s}^{(1)}`, `C_{×,k}^{(1)}`, `C_{/,1}^{(2)}`.
2. **Scott ⟷ Aff⁺, Lawson ⟷ PGL₂** (`11`–`13`): on `L=[0,∞]`, the affine
   Scott-continuous monoid is `Aff^+ = C(σ)∩B_∞ = {ka+s : k>0, s≥0}`; the
   group `⟨Aff^+,¬⟩ = PGL₂`; "adjoin ¬" commutes (`Φ(σ∨¬_*σ)=⟨Φ(σ),¬⟩`). It is a
   natural isomorphism of generating data, **not** a full Galois equivalence
   (three proved reasons: `A(σ)=A(λ)`, `H(λ)=Stab([0,∞])⊊PGL₂`, `¬T_s¬∈E(σ)∖Aff^+`).
3. **ρ has no Scott-continuous extension** (`14`): `ρ` is monotone only for the
   trivial preorder; the only candidate limit extension is the infinite matrix
   product = continued fraction (out of Paper I scope).
4. **Branching-history dcpo** (`15`): information order = down-set embedding;
   `Idl(FinDAG)` = finite∪infinite computation DAGs; compact = finite; prefix
   order is the chain specialization; `O(P)` is a finite distributive lattice
   with linear extensions = maximal chains = spinal histories (Birkhoff).
5. **Hecke history space** (`16`): `Γ_4^≤ω` is a Cantor space; `G₄ ≅ C₂*C₄`
   (ends = Cantor), while `H(√2)` is first-kind (limit set = `P^1(ℝ)`, not
   Cantor).
6. **Contact curvature = minimal DAG order defect** (`17`–`18`): the generators
   are exact flows of `D_u, D_v`; the order defect of `{A,M}` has infinitesimal
   density `μλ = [D_u,D_v](a)` (BCH; the non-trivial step is Paper 0's
   `prop:torsion-curvature-synthesis`).
7. **Defect is a 1-cocycle** (`20`): telescoping additivity (exact); local
   defect = suffix-conjugated commutator; hexagon closure = Jacobi identity.

---

## 4. Structural proposals (the integrative readings)

These are the "readings" that give the thread its shape; they are coherent but
**not theorems**, and must be cited only as `structural proposal`:

1. **"Contact = the DAG language of volume computation"** (`17` §4): the
   contact structure is the infinitesimal form of the minimal branching DAG
   `{A,M}`; the full DAG language (note `15`) is its macroscopic generalization.
2. **Bulk-boundary correspondence** (`19`): bulk = finite DAG (flat, compact);
   surface = ideal boundary (infinite histories = the "limit"); the defect is a
   boundary holonomy living on the surface. This is the "holographic" reading.
3. **Alexandrov vs Scott = flatten vs preserve the surface** (`19` §4, from the
   discussion preceding it): Alexandrov reifies the ideal boundary as isolated
   points; Scott keeps it as a genuine limit. The bulk-boundary correspondence
   holds only in the Scott reading.

---

## 5. Open problems (residuals; register OQ-095)

The thread leaves the following **open** (none blocks the provable core of §3):

1. **Higher-order brackets** (`18` §8, `20` §8): do the BCH higher-order terms
   `[X,[X,Y]]`, `[Y,[X,Y]]`, … correspond to nested defects of multiple
   antichain edges? Requires generalizing the single-diamond defect to the
   higher-dimensional cells of `O(P)`.
2. **Full DAG Lie realization** (`18` §8): the functor `F` is defined on the
   two generators `{A,M}`; generalizing to arbitrary generator sets needs a
   free Lie algebra / free flow-group realization (the DAG dcpo → a free Lie
   algebra).
3. **Macro Stokes** (`19` §3): the "discrete Stokes on `O(P)`" — defect between
   two threads = `∫∫ μλ` over the region, for arbitrary `P` — is established at
   the 1-cocycle level (`20`) but the assembly into a full statement for
   arbitrary `P` (additivity + exactness + spectral docking with `15` §6) is
   not yet written.
4. **Spectral docking** (`19` §3, `20` §8): `O(P)`'s Scott/Lawson topology as
   the spectral space of the discrete Stokes complex.

---

## 6. Scope mapping (which paper owns what)

| Content | Owner | Status |
|---|---|---|
| Marked spinal histories, prefix order, `PGL₂` generation, affine/Borel, Bruhat, Hecke `q=4` | Paper I | proved (already) |
| Contact form, horizontal fields, curvature `[D_u,D_v]=μλ∂a`, torsion-Stokes, Legendre duality | Paper 0 | proved (already) |
| Scott/Lawson reading of Paper I §2–§3 (`11`–`16`) | note reserve (not a paper) | resolved as notes |
| Contact = DAG defect, bulk-boundary, 1-cocycle (`17`–`20`) | note reserve (not a paper) | structural proposal + open |
| General convergence of infinite expressions (continued fractions) | Paper II/III | excluded from Paper I (094b) |
| Higher-order brackets, macro Stokes, spectral docking | note reserve → future | open (OQ-095) |

---

## 7. Claim discipline (what must not be said)

* "Scott ⟷ affine sector" must be read as `Scott ⟷ Aff^+` (the positive affine
  **semigroup** `{ka+s : k>0, s≥0}`), not `B_∞` (the full affine group, which
  already contains the reflection `D_{-1} = T_1¬T_{-1}¬T_1¬`).
* "Lawson ⟷ PGL₂" is a **natural isomorphism of generating data**, not a Galois
  equivalence over `Top(L)` (`13` §4).
* "Contact = the DAG language" is the **infinitesimal** form at the minimal
  antichain `{A,M}`, not a claim that the contact structure classifies
  arbitrary branching DAGs.
* The bulk-boundary ("holographic") reading is a `structural proposal`; the
  defect being a boundary holonomy is **proved** (Stokes + `dα` exact), but the
  "surface = ideal boundary = where curvature lives" is a reading.
* The Alexandrov/Scott "flatten vs preserve" contrast is a reading, not a
  theorem of Paper I.

---

## 8. Disposition (recommended next steps)

1. **Register OQ-095** in `governance/08-open-questions.md` (the four residuals
   of §5). [This record names them; the register entry follows.]
2. **Grade notes 10–20** in `governance/notes-reserve-audit.md` §2.2 (currently
   only `09` is graded there; `10`–`20` are new and ungraded).
3. **Decide the promotion question**: whether the provable core of §3 (items
   6–7, contact curvature = DAG defect via the functor) merits a short
   "order-topological reading" subsection in Paper I §3 or Paper 0 §9, at the
   recorded statuses. No promotion is performed here.
4. **Attack OQ-095.1** (higher-order brackets) next: this is the gate to the
   macro Stokes (OQ-095.3) and the full DAG Lie realization (OQ-095.2).

---

**Prepared:** 2026-10-31. This record changes no paper source and no claim
status; it registers the thread, its proved core, its proposals, and its
residuals, and it names the follow-up registration steps.
