import ProjectiveGeneration
import Mathlib.LinearAlgebra.AffineSpace.AffineEquiv

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   The actual infinity stabilizer in PGL is multiplicatively equivalent to
   Mathlib's one-dimensional affine-equivalence group. The coefficient of x
   is nonzero, and multiplication applies the right factor first. -/
namespace AEGPaper0.AffineStabilizer

noncomputable section
open ProjectiveLine ProjectiveGeneralLinear Chapter04ProjectiveBridge ProjectiveGeneration
variable {K : Type*} [Field K]

abbrev Aff (K : Type*) [Field K] := K ≃ᵃ[K] K
def slope (e : Aff K) : K := e.linear 1
def offset (e : Aff K) : K := e 0

theorem affine_formula (e : Aff K) (x : K) : e x = slope e*x+offset e := by
  have hlin : e.linear x=x*e.linear 1 := by simpa using e.linear.map_smul x (1:K)
  calc
    e x = e.linear x+e 0 := by simpa using e.map_vadd (0:K) x
    _ = slope e*x+offset e := by rw [hlin]; unfold slope offset; ring

theorem slope_nonzero (e : Aff K) : slope e ≠ 0 := by
  intro h
  have hh : e.linear 1=e.linear 0 := by rw [map_zero]; exact h
  exact one_ne_zero (e.linear.injective hh)

def normalizedAffine (a b : K) (ha : a ≠ 0) : Aff K where
  toEquiv :=
    { toFun := fun x => a*x+b
      invFun := fun y => (y-b)/a
      left_inv := by intro x; field_simp; ring
      right_inv := by intro y; field_simp; ring }
  linear :=
    { toFun := fun x => a*x
      invFun := fun y => y/a
      left_inv := by intro x; field_simp
      right_inv := by intro y; field_simp
      map_add' := by intro x y; ring
      map_smul' := by intro c x; change a*(c*x)=c*(a*x); ring }
  map_vadd' := by intro p v; change a*(v+p)+b=a*v+(a*p+b); ring

theorem normalizedAffine_apply (a b x : K) (ha : a ≠ 0) : normalizedAffine a b ha x = a*x+b := rfl

theorem normalizedAffine_inverse_apply (a b y : K) (ha : a ≠ 0) :
    (normalizedAffine a b ha).symm y=(y-b)/a := rfl

theorem affine_map_exists (a b : K) (ha : a ≠ 0) :
    ∃ e : Aff K, ∀ x : K, e x=a*x+b := ⟨normalizedAffine a b ha,fun _ => rfl⟩

theorem zero_slope_impossible (b : K) : ¬ ∃ e : Aff K, ∀ x : K, e x=0*x+b := by
  rintro ⟨e,he⟩
  have hh : e 0=e 1 := by rw [he 0,he 1]; simp
  exact zero_ne_one (e.injective hh)

theorem normalizedAffine_slope (a b : K) (ha : a ≠ 0) : slope (normalizedAffine a b ha)=a := by
  simp [slope, normalizedAffine]

theorem normalizedAffine_offset (a b : K) (ha : a ≠ 0) : offset (normalizedAffine a b ha)=b := by
  simp [offset, normalizedAffine]

theorem affine_parameters_unique (a b c d : K) (ha : a ≠ 0) (hc : c ≠ 0) :
    normalizedAffine a b ha = normalizedAffine c d hc ↔ a=c ∧ b=d := by
  constructor
  · intro he
    have hb := congrArg offset he
    have hA := congrArg slope he
    simpa only [normalizedAffine_slope, normalizedAffine_offset] using And.intro hA hb
  · rintro ⟨rfl,rfl⟩; rfl

def affineMatrix (e : Aff K) : Matrix2 K := ⟨slope e, offset e, 0, 1⟩

theorem affineMatrix_determinant (e : Aff K) : determinant (affineMatrix e)=slope e := by
  simp [determinant, affineMatrix]

def affineClass (e : Aff K) : PGL2 K := ofMatrix (affineMatrix e) (by rw [affineMatrix_determinant]; exact slope_nonzero e)

theorem affineClass_infinity (e : Aff K) : quotientAction (affineClass e) none=none := by
  rw [affineClass, ofMatrix_action, infinity_action]; simp [affineMatrix]

theorem affineClass_finite (e : Aff K) (x : K) : quotientAction (affineClass e) (some x)=some (e x) := by
  rw [affineClass, ofMatrix_action, finite_action, affine_formula e x]
  simp [affineMatrix]

theorem affineClass_injective : Function.Injective (affineClass (K := K)) := by
  intro e f he
  apply AffineEquiv.ext
  intro x
  have h := congrArg (fun q => quotientAction q (some x)) he
  dsimp only at h
  rw [affineClass_finite, affineClass_finite] at h
  exact Option.some.inj h

theorem affineClass_one : affineClass (1 : Aff K)=1 := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  cases x <;> simp only [affineClass_infinity, affineClass_finite, quotient_action_one, AffineEquiv.coe_one, id_eq]

theorem affineClass_mul (e f : Aff K) : affineClass (e*f)=affineClass e*affineClass f := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  cases x <;> simp only [quotient_action_mul, affineClass_infinity, affineClass_finite, AffineEquiv.coe_mul, Function.comp_apply]

def affineHom : Aff K →* PGL2 K where
  toFun := affineClass
  map_one' := affineClass_one
  map_mul' := affineClass_mul

def infinityStabilizer : Subgroup (PGL2 K) where
  carrier := {q | quotientAction q none=none}
  one_mem' := quotient_action_one none
  mul_mem' := by
    intro g h hg hh
    simp only [Set.mem_setOf_eq] at hg hh ⊢
    rw [quotient_action_mul, hh, hg]
  inv_mem' := by
    intro g hg
    change quotientAction g none=none at hg
    change quotientAction g⁻¹ none=none
    have he := congrArg (fun x => quotientAction g⁻¹ x) hg
    dsimp only at he
    rw [quotient_action_inverse] at he
    exact he.symm

def toStabilizer : Aff K →* (infinityStabilizer (K := K)) where
  toFun e := ⟨affineClass e, affineClass_infinity e⟩
  map_one' := Subtype.ext affineClass_one
  map_mul' e f := Subtype.ext (affineClass_mul e f)

theorem toStabilizer_injective : Function.Injective (toStabilizer (K := K)) := by
  intro e f he
  exact affineClass_injective (congrArg Subtype.val he)

theorem infinity_iff_lower_left_zero (m : Matrix2 K) (hm : determinant m ≠ 0) :
    ofMatrix m hm ∈ infinityStabilizer ↔ m.c=0 := by
  change quotientAction (ofMatrix m hm) none=none ↔ m.c=0
  rw [ofMatrix_action, fixes_infinity_iff]

theorem affine_matrix_class_normal_form (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c=0) :
    ofMatrix m hm=affineClass (normalizedAffine (m.a/m.d) (m.b/m.d)
      (div_ne_zero (affine_diagonal_nonzero m hm hc).1 (affine_diagonal_nonzero m hm hc).2)) := by
  have hd := (affine_diagonal_nonzero m hm hc).2
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  cases x with
  | none => rw [affineClass_infinity, ofMatrix_action]; exact (fixes_infinity_iff m).mpr hc
  | some x =>
    rw [affineClass_finite, normalizedAffine_apply, ofMatrix_action, finite_action]
    simp only [hc, zero_mul, zero_add, hd, if_false, Option.some.injEq]
    field_simp

theorem toStabilizer_surjective : Function.Surjective (toStabilizer (K := K)) := by
  intro q
  obtain ⟨m,hm,he⟩ := ofMatrix_surjective q.val
  have hc : m.c=0 := (infinity_iff_lower_left_zero m hm).mp (by rw [he]; exact q.property)
  refine ⟨normalizedAffine (m.a/m.d) (m.b/m.d)
    (div_ne_zero (affine_diagonal_nonzero m hm hc).1 (affine_diagonal_nonzero m hm hc).2), ?_⟩
  apply Subtype.ext
  exact (affine_matrix_class_normal_form m hm hc).symm.trans he

def affineStabilizerEquiv : Aff K ≃* (infinityStabilizer (K := K)) :=
  MulEquiv.ofBijective toStabilizer ⟨toStabilizer_injective,toStabilizer_surjective⟩

theorem affineStabilizerEquiv_finite (e : Aff K) (x : K) :
    quotientAction (affineStabilizerEquiv e).val (some x)=some (e x) := affineClass_finite e x

theorem normalized_class_unique (a b c d : K) (ha : a ≠ 0) (hc : c ≠ 0) :
    affineClass (normalizedAffine a b ha)=affineClass (normalizedAffine c d hc) ↔ a=c ∧ b=d := by
  rw [affineClass_injective.eq_iff, affine_parameters_unique]

theorem affine_parameter_composition (e f : Aff K) :
    slope (e*f)=slope e*slope f ∧ offset (e*f)=slope e*offset f+offset e := by
  have he : e*f=normalizedAffine (slope e*slope f) (slope e*offset f+offset e)
      (mul_ne_zero (slope_nonzero e) (slope_nonzero f)) := by
    apply AffineEquiv.ext
    intro x
    change e (f x)=_
    rw [affine_formula e, affine_formula f, normalizedAffine_apply]
    ring
  rw [he, normalizedAffine_slope, normalizedAffine_offset]
  exact ⟨rfl,rfl⟩

theorem inversion_not_in_affine_stabilizer : (inversionClass : PGL2 K) ∉ infinityStabilizer := by
  change quotientAction (inversionClass : PGL2 K) none ≠ none
  rw [inversionClass_infinity]
  exact Option.some_ne_none _

theorem affine_composition_order_matters :
    affineClass (normalizedAffine (1:ℚ) 1 (by norm_num)) * affineClass (normalizedAffine (2:ℚ) 0 (by norm_num)) ≠
      affineClass (normalizedAffine (2:ℚ) 0 (by norm_num)) * affineClass (normalizedAffine (1:ℚ) 1 (by norm_num)) := by
  intro he
  have h := congrArg (fun q : PGL2 ℚ => quotientAction q (some 0)) he
  dsimp only at h
  simp only [quotient_action_mul, affineClass_finite, normalizedAffine_apply] at h
  norm_num at h

end
end AEGPaper0.AffineStabilizer

#print axioms AEGPaper0.AffineStabilizer.affine_formula
#print axioms AEGPaper0.AffineStabilizer.slope_nonzero
#print axioms AEGPaper0.AffineStabilizer.normalizedAffine_apply
#print axioms AEGPaper0.AffineStabilizer.normalizedAffine_inverse_apply
#print axioms AEGPaper0.AffineStabilizer.affine_map_exists
#print axioms AEGPaper0.AffineStabilizer.zero_slope_impossible
#print axioms AEGPaper0.AffineStabilizer.normalizedAffine_slope
#print axioms AEGPaper0.AffineStabilizer.normalizedAffine_offset
#print axioms AEGPaper0.AffineStabilizer.affine_parameters_unique
#print axioms AEGPaper0.AffineStabilizer.affineMatrix_determinant
#print axioms AEGPaper0.AffineStabilizer.affineClass_infinity
#print axioms AEGPaper0.AffineStabilizer.affineClass_finite
#print axioms AEGPaper0.AffineStabilizer.affineClass_injective
#print axioms AEGPaper0.AffineStabilizer.affineClass_one
#print axioms AEGPaper0.AffineStabilizer.affineClass_mul
#print axioms AEGPaper0.AffineStabilizer.toStabilizer_injective
#print axioms AEGPaper0.AffineStabilizer.infinity_iff_lower_left_zero
#print axioms AEGPaper0.AffineStabilizer.affine_matrix_class_normal_form
#print axioms AEGPaper0.AffineStabilizer.toStabilizer_surjective
#print axioms AEGPaper0.AffineStabilizer.affineStabilizerEquiv_finite
#print axioms AEGPaper0.AffineStabilizer.normalized_class_unique
#print axioms AEGPaper0.AffineStabilizer.affine_parameter_composition
#print axioms AEGPaper0.AffineStabilizer.inversion_not_in_affine_stabilizer
#print axioms AEGPaper0.AffineStabilizer.affine_composition_order_matters
