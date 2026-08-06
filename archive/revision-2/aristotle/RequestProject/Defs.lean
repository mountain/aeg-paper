/-
# Arithmetic Expression Geometry I: Foundations
## Core Definitions

Formalization of the basic operators, torsion defect, and path evaluation
from "Arithmetic Expression Geometry I: Foundations" by Mingli Yuan.
-/
import Mathlib

noncomputable section

open Real

/-! ## Basic arithmetic operators (§2.1)

The four curried operators on ℝ used for threadlike expressions:
  ⊕_μ : x ↦ x + μ
  ⊖_μ : x ↦ x - μ
  ⊗_l : x ↦ x · e^l
  ⊘_l : x ↦ x · e^{-l}
-/

/-- Additive operator ⊕_μ : x ↦ x + μ (Definition 2.1) -/
def AEG.oplus (mu : ℝ) (x : ℝ) : ℝ := x + mu

/-- Subtractive operator ⊖_μ : x ↦ x - μ -/
def AEG.ominus (mu : ℝ) (x : ℝ) : ℝ := x - mu

/-- Multiplicative operator ⊗_l : x ↦ x · e^l -/
def AEG.otimes (l : ℝ) (x : ℝ) : ℝ := x * exp l

/-- Divisive operator ⊘_l : x ↦ x · e^{-l} -/
def AEG.oslash (l : ℝ) (x : ℝ) : ℝ := x * exp (-l)

/-! ## Discrete arithmetic torsion (§2.2, eq. 2.5)

The commutator defect τ(x) = x⊕μ⊗l − x⊗l⊕μ = μ(e^l − 1).
-/

/-
PROBLEM
The discrete arithmetic torsion: the commutator defect of additive and
multiplicative propagation. This is equation (2.5) in the paper.
τ(x) := (x ⊕ μ) ⊗ l − (x ⊗ l) ⊕ μ = μ(e^l − 1)

PROVIDED SOLUTION
Unfold oplus and otimes. Then: (x + mu) * exp l - (x * exp l + mu) = mu * exp l - mu = mu * (exp l - 1). Use ring.
-/
theorem AEG.torsion_defect (mu l x : ℝ) :
    AEG.otimes l (AEG.oplus mu x) - AEG.oplus mu (AEG.otimes l x) = mu * (exp l - 1) := by
  unfold otimes oplus; ring;

/-! ## Inverse operators -/

/-
PROBLEM
⊕_μ and ⊖_μ are inverses

PROVIDED SOLUTION
Unfold oplus and ominus, then ring or simp.
-/
theorem AEG.oplus_ominus_inv (mu x : ℝ) : AEG.ominus mu (AEG.oplus mu x) = x := by
  unfold oplus ominus; ring;

/-
PROBLEM
⊗_l and ⊘_l are inverses

PROVIDED SOLUTION
Unfold otimes and oslash. x * exp l * exp(-l) = x * 1 = x. Use mul_assoc and exp_neg and mul_comm.
-/
theorem AEG.otimes_oslash_inv (l x : ℝ) : AEG.oslash l (AEG.otimes l x) = x := by
  unfold oslash otimes; ring; norm_num [ Real.exp_neg, Real.exp_ne_zero ] ;

/-! ## Finite commutator square (§5.2, eq. 5.8)

The finite commutator of the horizontal flows Φ_u^h and Φ_v^k:
  a(p_uv) − a(p_vu) = μh(e^{lk} − 1)
-/

/-- Flow of D_u for time h: (u,v,a) ↦ (u+h, v, a + μh) -/
def AEG.flow_u (mu h : ℝ) (u v a : ℝ) : ℝ × ℝ × ℝ := (u + h, v, a + mu * h)

/-- Flow of D_v for time k: (u,v,a) ↦ (u, v+k, e^{lk}·a) -/
def AEG.flow_v (l k : ℝ) (u v a : ℝ) : ℝ × ℝ × ℝ := (u, v + k, exp (l * k) * a)

/-
PROBLEM
The finite commutator square identity (equation 5.8):
a(Φ_v^k ∘ Φ_u^h) − a(Φ_u^h ∘ Φ_v^k) = μh(e^{lk} − 1)

PROVIDED SOLUTION
Unfold flow_u and flow_v. p_uv.2.2 = exp(l*k)*(a + mu*h), p_vu.2.2 = exp(l*k)*a + mu*h. Difference = mu*h*(exp(l*k) - 1). Use ring.
-/
theorem AEG.finite_commutator_square (mu l h k u v a : ℝ) :
    let p_uv := AEG.flow_v l k (u + h) v (a + mu * h)
    let p_vu := AEG.flow_u mu h u (v + k) (exp (l * k) * a)
    p_uv.2.2 - p_vu.2.2 = mu * h * (exp (l * k) - 1) := by
  unfold flow_v flow_u; ring;

end