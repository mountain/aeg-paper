import ProjectiveFixedPoints

/- Original CC0 proofs by Codex (OpenAI), 2026-11-08.
   Ordinary affine updates include zero slope. Invertible affine-group and
   PGL powers require nonzero slope. Nat casts retain positive characteristic. -/
namespace AEGPaper0.AffineIteration

noncomputable section
open ProjectiveLine ProjectiveGeneralLinear Chapter04ProjectiveBridge
open ProjectiveGeneration AffineStabilizer ProjectiveFixedPoints
variable {K : Type*} [Field K]

def update (a b : K) (z : K) : K := a*z+b
def iterate (a b : K) (n : ℕ) (z : K) : K := (update a b)^[n] z

theorem iterate_zero (a b z : K) : iterate a b 0 z=z := rfl
theorem iterate_succ (a b z : K) (n : ℕ) :
    iterate a b (n+1) z=a*iterate a b n z+b := Function.iterate_succ_apply' _ _ _

theorem iterate_add (a b z : K) (n m : ℕ) :
    iterate a b (n+m) z=iterate a b n (iterate a b m z) := Function.iterate_add_apply _ _ _ _

theorem fixed_center_relation (a b : K) (ha : a ≠ 1) :
    (1-a)*(b/(1-a))=b := by
  have hn : 1-a ≠ 0 := sub_ne_zero.mpr ha.symm
  field_simp

theorem centered_update (a b z : K) (ha : a ≠ 1) :
    update a b z=b/(1-a)+a*(z-b/(1-a)) := by
  have h := fixed_center_relation a b ha
  dsimp [update]
  linear_combination -h

theorem centered_iterate (a b z : K) (ha : a ≠ 1) (n : ℕ) :
    iterate a b n z=b/(1-a)+a^n*(z-b/(1-a)) := by
  induction n with
  | zero => simp [iterate_zero]
  | succ n ih =>
    rw [iterate_succ,ih,pow_succ]
    have h := fixed_center_relation a b ha
    linear_combination -h

theorem finite_geometric_iterate (a b z : K) (n : ℕ) :
    iterate a b n z=a^n*z+b*∑ k ∈ Finset.range n, a^k := by
  induction n generalizing z with
  | zero => simp [iterate_zero]
  | succ n ih =>
    rw [show iterate a b (n+1) z=iterate a b n (update a b z) from Function.iterate_succ_apply _ _ _]
    rw [ih,Finset.sum_range_succ,pow_succ]
    dsimp [update]; ring

theorem translation_iterate (b z : K) (n : ℕ) : iterate 1 b n z=z+(n:K)*b := by
  induction n with
  | zero => simp [iterate_zero]
  | succ n ih => rw [iterate_succ,ih,Nat.cast_add,Nat.cast_one]; ring

theorem zero_slope_iterate (b z : K) (n : ℕ) : iterate 0 b (n+1) z=b := by
  rw [iterate_succ]; ring

theorem fixed_center_unique (a b z : K) (ha : a ≠ 1) :
    update a b z=z ↔ z=b/(1-a) := by
  have hn : 1-a ≠ 0 := sub_ne_zero.mpr ha.symm
  rw [eq_div_iff hn]
  dsimp [update]
  constructor <;> intro h <;> linear_combination -h

theorem translation_fixed_iff_offset_zero (b z : K) : update 1 b z=z ↔ b=0 := by
  simp [update]

theorem affine_iterate_agrees_with_power (e : Aff K) (n : ℕ) (z : K) :
    (e^n) z=iterate (AffineStabilizer.slope e) (offset e) n z := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [pow_succ']
    change e ((e^n) z)=_
    rw [ih,affine_formula,iterate_succ]

theorem normalized_power_centered (a b : K) (ha : a ≠ 0) (h1 : a ≠ 1) (n : ℕ) (z : K) :
    ((normalizedAffine a b ha)^n) z=b/(1-a)+a^n*(z-b/(1-a)) := by
  rw [affine_iterate_agrees_with_power,normalizedAffine_slope,normalizedAffine_offset,centered_iterate a b z h1]

theorem normalized_power_translation (b : K) (n : ℕ) (z : K) :
    ((normalizedAffine (1:K) b one_ne_zero)^n) z=z+(n:K)*b := by
  rw [affine_iterate_agrees_with_power,normalizedAffine_slope,normalizedAffine_offset,translation_iterate]

theorem affineClass_power (e : Aff K) (n : ℕ) : affineClass (e^n)=(affineClass e)^n :=
  (affineHom (K := K)).map_pow e n

theorem projective_power_finite (e : Aff K) (n : ℕ) (z : K) :
    ProjectiveGeneralLinear.quotientAction ((affineClass e)^n) (some z)=
      some (iterate (AffineStabilizer.slope e) (offset e) n z) := by
  rw [← affineClass_power,affineClass_finite,affine_iterate_agrees_with_power]

theorem projective_power_infinity (e : Aff K) (n : ℕ) :
    ProjectiveGeneralLinear.quotientAction ((affineClass e)^n) none=none := by
  rw [← affineClass_power,affineClass_infinity]

theorem translation_period_when_cast_zero (b z : K) (n : ℕ) (hn : (n:K)=0) : iterate 1 b n z=z := by
  rw [translation_iterate,hn]; ring

theorem translation_group_period (b : K) (n : ℕ) (hn : (n:K)=0) :
    (normalizedAffine (1:K) b one_ne_zero)^n=1 := by
  apply AffineEquiv.ext
  intro z
  rw [normalized_power_translation,hn]
  simp

theorem affine_fixed_set_slope_ne_one (a b : K) (ha : a ≠ 0) (h1 : a ≠ 1) :
    fixedSet (affineClass (normalizedAffine a b ha))={none,some (b/(1-a))} := by
  ext p
  cases p with
  | none => simp [fixedSet,affineClass_infinity]
  | some z =>
    simp only [fixedSet,Set.mem_setOf_eq,affineClass_finite,normalizedAffine_apply,
      Option.some.injEq,Set.mem_insert_iff,Set.mem_singleton_iff,reduceCtorEq,false_or]
    exact fixed_center_unique a b z h1

theorem affine_fixed_set_translation (b : K) (hb : b ≠ 0) :
    fixedSet (affineClass (normalizedAffine (1:K) b one_ne_zero))={none} := by
  ext p
  cases p with
  | none => simp [fixedSet,affineClass_infinity]
  | some z =>
    simp only [fixedSet,Set.mem_setOf_eq,affineClass_finite,normalizedAffine_apply,
      Option.some.injEq,Set.mem_singleton_iff,reduceCtorEq,iff_false]
    intro h
    exact hb ((translation_fixed_iff_offset_zero b z).mp h)

theorem affine_fixed_set_identity :
    fixedSet (affineClass (normalizedAffine (1:K) 0 one_ne_zero))=Set.univ := by
  have he : normalizedAffine (1:K) 0 one_ne_zero=(1:Aff K) := by
    apply AffineEquiv.ext; intro z; simp [normalizedAffine_apply]
  rw [he,affineClass_one,fixedSet_one]

end
end AEGPaper0.AffineIteration

#print axioms AEGPaper0.AffineIteration.iterate_zero
#print axioms AEGPaper0.AffineIteration.iterate_succ
#print axioms AEGPaper0.AffineIteration.iterate_add
#print axioms AEGPaper0.AffineIteration.fixed_center_relation
#print axioms AEGPaper0.AffineIteration.centered_update
#print axioms AEGPaper0.AffineIteration.centered_iterate
#print axioms AEGPaper0.AffineIteration.finite_geometric_iterate
#print axioms AEGPaper0.AffineIteration.translation_iterate
#print axioms AEGPaper0.AffineIteration.zero_slope_iterate
#print axioms AEGPaper0.AffineIteration.fixed_center_unique
#print axioms AEGPaper0.AffineIteration.translation_fixed_iff_offset_zero
#print axioms AEGPaper0.AffineIteration.affine_iterate_agrees_with_power
#print axioms AEGPaper0.AffineIteration.normalized_power_centered
#print axioms AEGPaper0.AffineIteration.normalized_power_translation
#print axioms AEGPaper0.AffineIteration.affineClass_power
#print axioms AEGPaper0.AffineIteration.projective_power_finite
#print axioms AEGPaper0.AffineIteration.projective_power_infinity
#print axioms AEGPaper0.AffineIteration.translation_period_when_cast_zero
#print axioms AEGPaper0.AffineIteration.translation_group_period
#print axioms AEGPaper0.AffineIteration.affine_fixed_set_slope_ne_one
#print axioms AEGPaper0.AffineIteration.affine_fixed_set_translation
#print axioms AEGPaper0.AffineIteration.affine_fixed_set_identity
