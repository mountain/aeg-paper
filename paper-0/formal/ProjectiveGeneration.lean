import ProjectiveGeneralLinear
import Chapter04ProjectiveBridge

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   The existing elementary matrix/action formulas descend to genuine PGL
   quotient equalities and subgroup generation. Every dilation is a unit.
   This is an operator group, not a quotient of arithmetic histories. -/
namespace AEGPaper0.ProjectiveGeneration

noncomputable section
open ProjectiveLine ProjectiveGeneralLinear Chapter04ProjectiveBridge
variable {K : Type*} [Field K]

def ofMatrix (m : Matrix2 K) (hm : determinant m ≠ 0) : PGL2 K := QuotientGroup.mk (toGL m hm)

theorem ofMatrix_action (m : Matrix2 K) (hm : determinant m ≠ 0) (x : Point K) :
    quotientAction (ofMatrix m hm) x = act m x := by
  simp only [ofMatrix, quotientAction_representative, actionHom_apply, toGL_coefficients]

theorem ofMatrix_surjective : ∀ q : PGL2 K, ∃ m : Matrix2 K, ∃ hm : determinant m ≠ 0, ofMatrix m hm = q := by
  intro q
  obtain ⟨g, rfl⟩ := QuotientGroup.mk_surjective q
  refine ⟨coefficients g.val, gl_nondegenerate g, ?_⟩
  apply congrArg QuotientGroup.mk
  exact coefficients_injective (toGL_coefficients _ _)

theorem ofMatrix_equal_iff_scalar (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0) :
    ofMatrix m hm = ofMatrix n hn ↔ ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s n := by
  simpa only [toGL_coefficients] using
    (quotient_equality_iff_nonzero_scalar (toGL m hm) (toGL n hn))

theorem ofMatrix_product (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hmn : determinant (multiply m n) ≠ 0) : ofMatrix (multiply m n) hmn = ofMatrix m hm * ofMatrix n hn := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  rw [quotient_action_mul, ofMatrix_action, ofMatrix_action, ofMatrix_action]
  exact action_multiply m n x hn

def translationClass (s : K) : PGL2 K := ofMatrix (translation s) (by rw [translation_determinant]; exact one_ne_zero)
def dilationClass (u : Kˣ) : PGL2 K := ofMatrix (dilation (u : K)) (by rw [dilation_determinant]; exact u.ne_zero)
def inversionClass : PGL2 K := ofMatrix inversion (by rw [inversion_determinant]; exact one_ne_zero)

theorem translationClass_finite (s x : K) : quotientAction (translationClass s) (some x) = some (x+s) := by
  rw [translationClass, ofMatrix_action, translation_finite]

theorem translationClass_infinity (s : K) : quotientAction (translationClass s) none = none := by
  rw [translationClass, ofMatrix_action, infinity_action]
  simp [translation]

theorem dilationClass_finite (u : Kˣ) (x : K) : quotientAction (dilationClass u) (some x) = some ((u : K)*x) := by
  rw [dilationClass, ofMatrix_action, dilation_finite]

theorem dilationClass_infinity (u : Kˣ) : quotientAction (dilationClass u) none = none := by
  rw [dilationClass, ofMatrix_action, infinity_action]
  simp [dilation]

theorem inversionClass_infinity : quotientAction (inversionClass : PGL2 K) none = some 0 := by
  rw [inversionClass, ofMatrix_action, inversion_infinity]

theorem inversionClass_zero : quotientAction (inversionClass : PGL2 K) (some 0) = none := by
  rw [inversionClass, ofMatrix_action, inversion_zero]

theorem inversionClass_finite (x : K) (hx : x ≠ 0) :
    quotientAction (inversionClass : PGL2 K) (some x) = some (-1/x) := by
  rw [inversionClass, ofMatrix_action, inversion_finite x hx]

theorem quotient_affine_factorization (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c = 0) :
    ofMatrix m hm = translationClass (m.b/m.d) *
      dilationClass (Units.mk0 (m.a/m.d) (div_ne_zero (affine_diagonal_nonzero m hm hc).1
        (affine_diagonal_nonzero m hm hc).2)) := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  simp only [quotient_action_mul, translationClass, dilationClass, ofMatrix_action, Units.val_mk0]
  exact affine_action_factorization m hm hc x

theorem quotient_nonaffine_factorization (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    ofMatrix m hm = translationClass (m.a/m.c) *
      (dilationClass (Units.mk0 (determinant m/m.c^2) (nonaffine_scale_nonzero m hm hc)) *
        ((inversionClass : PGL2 K) * translationClass (m.d/m.c))) := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  simp only [quotient_action_mul, translationClass, dilationClass, inversionClass, ofMatrix_action, Units.val_mk0]
  exact nonaffine_action_factorization m hm hc x

def elementaryGenerators : Set (PGL2 K) :=
  Set.range translationClass ∪ Set.range dilationClass ∪ {inversionClass}

theorem subgroup_containing_elementary_is_top (H : Subgroup (PGL2 K))
    (hT : ∀ s, translationClass s ∈ H) (hD : ∀ u, dilationClass u ∈ H) (hJ : inversionClass ∈ H) : H = ⊤ := by
  apply (Subgroup.eq_top_iff' H).mpr
  intro q
  obtain ⟨m, hm, rfl⟩ := ofMatrix_surjective q
  by_cases hc : m.c = 0
  · rw [quotient_affine_factorization m hm hc]
    exact H.mul_mem (hT _) (hD _)
  · rw [quotient_nonaffine_factorization m hm hc]
    exact H.mul_mem (hT _) (H.mul_mem (hD _) (H.mul_mem hJ (hT _)))

theorem elementary_generators_generate : Subgroup.closure (elementaryGenerators (K := K)) = ⊤ := by
  apply subgroup_containing_elementary_is_top
  · intro s; apply Subgroup.subset_closure; exact Or.inl (Or.inl ⟨s,rfl⟩)
  · intro u; apply Subgroup.subset_closure; exact Or.inl (Or.inr ⟨u,rfl⟩)
  · apply Subgroup.subset_closure; exact Or.inr rfl

end
end AEGPaper0.ProjectiveGeneration

#print axioms AEGPaper0.ProjectiveGeneration.ofMatrix_action
#print axioms AEGPaper0.ProjectiveGeneration.ofMatrix_surjective
#print axioms AEGPaper0.ProjectiveGeneration.ofMatrix_equal_iff_scalar
#print axioms AEGPaper0.ProjectiveGeneration.ofMatrix_product
#print axioms AEGPaper0.ProjectiveGeneration.translationClass_finite
#print axioms AEGPaper0.ProjectiveGeneration.translationClass_infinity
#print axioms AEGPaper0.ProjectiveGeneration.dilationClass_finite
#print axioms AEGPaper0.ProjectiveGeneration.dilationClass_infinity
#print axioms AEGPaper0.ProjectiveGeneration.inversionClass_infinity
#print axioms AEGPaper0.ProjectiveGeneration.inversionClass_zero
#print axioms AEGPaper0.ProjectiveGeneration.inversionClass_finite
#print axioms AEGPaper0.ProjectiveGeneration.quotient_affine_factorization
#print axioms AEGPaper0.ProjectiveGeneration.quotient_nonaffine_factorization
#print axioms AEGPaper0.ProjectiveGeneration.subgroup_containing_elementary_is_top
#print axioms AEGPaper0.ProjectiveGeneration.elementary_generators_generate
