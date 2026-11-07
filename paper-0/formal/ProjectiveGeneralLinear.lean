import ProjectiveFaithfulness
import Mathlib.LinearAlgebra.Matrix.GeneralLinearGroup.Defs
import Mathlib.GroupTheory.QuotientGroup.Basic

/- Original CC0 continuation by Codex (OpenAI), 2026-11-07.
   Standard Mathlib GL(2,K), its explicit nonzero scalar subgroup and quotient.
   Kernel identification is proved using the concrete projective action;
   faithful descent is not a target axiom. No history quotient is defined. -/
namespace AEGPaper0.ProjectiveGeneralLinear

noncomputable section
open ProjectiveLine ProjectiveFaithfulness
variable {K : Type*} [Field K]

def toMatrix (m : Matrix2 K) : Matrix (Fin 2) (Fin 2) K := !![m.a, m.b; m.c, m.d]
def coefficients (M : Matrix (Fin 2) (Fin 2) K) : Matrix2 K := ⟨M 0 0, M 0 1, M 1 0, M 1 1⟩

omit [Field K] in
theorem coefficients_toMatrix (m : Matrix2 K) : coefficients (toMatrix m) = m := by
  apply matrix_ext <;> rfl

omit [Field K] in
theorem toMatrix_coefficients (M : Matrix (Fin 2) (Fin 2) K) : toMatrix (coefficients M) = M := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl

theorem coefficients_determinant (M : Matrix (Fin 2) (Fin 2) K) :
    determinant (coefficients M) = M.det := by
  rw [Matrix.det_fin_two]; rfl

theorem toMatrix_determinant (m : Matrix2 K) : (toMatrix m).det = determinant m := by
  rw [← coefficients_determinant, coefficients_toMatrix]

theorem coefficients_product (M N : Matrix (Fin 2) (Fin 2) K) :
    coefficients (M*N) = multiply (coefficients M) (coefficients N) := by
  apply matrix_ext <;> simp [coefficients, multiply, Matrix.mul_apply, Fin.sum_univ_two]

theorem coefficients_one : coefficients (1 : Matrix (Fin 2) (Fin 2) K) = identity := by
  apply matrix_ext <;> simp [coefficients, identity]

abbrev GL2 (K : Type*) [Field K] := Matrix.GeneralLinearGroup (Fin 2) K

theorem gl_nondegenerate (g : GL2 K) : determinant (coefficients g.val) ≠ 0 := by
  rw [coefficients_determinant]
  exact Matrix.GeneralLinearGroup.det_ne_zero g

def toGL (m : Matrix2 K) (hd : determinant m ≠ 0) : GL2 K :=
  Matrix.GeneralLinearGroup.mkOfDetNeZero (toMatrix m) (by rwa [toMatrix_determinant])

theorem toGL_coefficients (m : Matrix2 K) (hd : determinant m ≠ 0) :
    coefficients (toGL m hd).val = m := by
  change coefficients (toMatrix m) = m
  exact coefficients_toMatrix m

theorem coefficients_injective : Function.Injective (fun g : GL2 K => coefficients g.val) := by
  intro g h he
  apply Units.ext
  simpa only [toMatrix_coefficients] using congrArg toMatrix he

def coefficientEquiv : GL2 K ≃ {m : Matrix2 K // determinant m ≠ 0} where
  toFun g := ⟨coefficients g.val, gl_nondegenerate g⟩
  invFun m := toGL m.val m.property
  left_inv g := coefficients_injective (toGL_coefficients (coefficients g.val) (gl_nondegenerate g))
  right_inv m := Subtype.ext (toGL_coefficients m.val m.property)

def actionHom : GL2 K →* Equiv.Perm (Point K) where
  toFun g := actionEquiv (coefficients g.val) (gl_nondegenerate g)
  map_one' := by
    apply Equiv.ext
    intro x
    change act (coefficients (1 : Matrix (Fin 2) (Fin 2) K)) x = x
    rw [coefficients_one, action_identity]
  map_mul' g h := by
    apply Equiv.ext
    intro x
    change act (coefficients (g.val*h.val)) x = act (coefficients g.val) (act (coefficients h.val) x)
    rw [coefficients_product, action_multiply _ _ x (gl_nondegenerate h)]

theorem actionHom_apply (g : GL2 K) (x : Point K) : actionHom g x = act (coefficients g.val) x := rfl

theorem actionHom_kernel_scalar (g : GL2 K) :
    g ∈ (actionHom (K := K)).ker ↔ ∃ s : K, s ≠ 0 ∧ coefficients g.val = scaleMatrix s identity := by
  rw [MonoidHom.mem_ker, ← identity_action_iff_scalar _ (gl_nondegenerate g)]
  exact Equiv.ext_iff

theorem actionHom_equal_iff_scalar (g h : GL2 K) :
    actionHom g = actionHom h ↔ ∃ s : K, s ≠ 0 ∧ coefficients g.val = scaleMatrix s (coefficients h.val) := by
  exact equivalence_equality_iff_scalar _ _ (gl_nondegenerate g) (gl_nondegenerate h)

def scalarSubgroup : Subgroup (GL2 K) where
  carrier := {g | ∃ s : K, s ≠ 0 ∧ coefficients g.val = scaleMatrix s identity}
  one_mem' := (actionHom_kernel_scalar 1).mp (actionHom.ker.one_mem)
  mul_mem' := fun hg hh => (actionHom_kernel_scalar _).mp
    (actionHom.ker.mul_mem ((actionHom_kernel_scalar _).mpr hg) ((actionHom_kernel_scalar _).mpr hh))
  inv_mem' := fun hg => (actionHom_kernel_scalar _).mp (actionHom.ker.inv_mem ((actionHom_kernel_scalar _).mpr hg))

theorem scalarSubgroup_eq_kernel : scalarSubgroup (K := K) = actionHom.ker := by
  ext g; exact (actionHom_kernel_scalar g).symm

instance scalarSubgroup_normal : (scalarSubgroup (K := K)).Normal := by
  rw [scalarSubgroup_eq_kernel]; infer_instance

def PGL2 (K : Type*) [Field K] := GL2 K ⧸ (scalarSubgroup (K := K))
instance : Group (PGL2 K) := inferInstanceAs (Group (GL2 K ⧸ scalarSubgroup))

def quotientAction : PGL2 K →* Equiv.Perm (Point K) :=
  QuotientGroup.lift scalarSubgroup actionHom (by rw [scalarSubgroup_eq_kernel])

theorem quotientAction_representative (g : GL2 K) :
    quotientAction (QuotientGroup.mk g : PGL2 K) = actionHom g := rfl

theorem quotient_equality_iff_action (g h : GL2 K) :
    (QuotientGroup.mk g : PGL2 K) = QuotientGroup.mk h ↔ actionHom g = actionHom h := by
  rw [QuotientGroup.eq_iff_div_mem, scalarSubgroup_eq_kernel, MonoidHom.mem_ker, map_div, div_eq_one]

theorem quotient_equality_iff_nonzero_scalar (g h : GL2 K) :
    (QuotientGroup.mk g : PGL2 K) = QuotientGroup.mk h ↔
      ∃ s : K, s ≠ 0 ∧ coefficients g.val = scaleMatrix s (coefficients h.val) := by
  rw [quotient_equality_iff_action, actionHom_equal_iff_scalar]

theorem quotient_action_injective : Function.Injective (quotientAction (K := K)) := by
  intro x y
  refine Quotient.inductionOn₂ x y ?_
  intro g h he
  exact (quotient_equality_iff_action g h).mpr he

def quotientRangeEquiv : PGL2 K ≃* (actionHom (K := K)).range :=
  (QuotientGroup.quotientMulEquivOfEq scalarSubgroup_eq_kernel).trans
    (QuotientGroup.quotientKerEquivRange actionHom)

theorem quotient_action_mul (g h : PGL2 K) (x : Point K) :
    quotientAction (g*h) x = quotientAction g (quotientAction h x) := by
  rw [map_mul]; rfl

theorem quotient_action_one (x : Point K) : quotientAction (1 : PGL2 K) x = x := by
  rw [map_one]; rfl

theorem quotient_action_inverse (g : PGL2 K) (x : Point K) :
    quotientAction g⁻¹ (quotientAction g x) = x := by
  rw [map_inv]
  exact Equiv.symm_apply_apply _ _

theorem scalarMatrix_standard (s : K) :
    toMatrix (scaleMatrix s (identity : Matrix2 K)) = s • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [toMatrix, scaleMatrix, identity]

theorem scalarSubgroup_matrix_membership (g : GL2 K) :
    g ∈ scalarSubgroup ↔ ∃ s : K, s ≠ 0 ∧ g.val = s • (1 : Matrix (Fin 2) (Fin 2) K) := by
  constructor
  · rintro ⟨s, hs, he⟩
    refine ⟨s, hs, ?_⟩
    have hh := congrArg toMatrix he
    simpa only [toMatrix_coefficients, scalarMatrix_standard] using hh
  · rintro ⟨s, hs, he⟩
    refine ⟨s, hs, ?_⟩
    rw [he, ← scalarMatrix_standard, coefficients_toMatrix]

theorem three_points_determine_quotient (g h : GL2 K)
    (hinf : actionHom g none = actionHom h none)
    (hzero : actionHom g (some 0) = actionHom h (some 0))
    (hone : actionHom g (some 1) = actionHom h (some 1)) :
    (QuotientGroup.mk g : PGL2 K) = QuotientGroup.mk h := by
  apply (quotient_equality_iff_nonzero_scalar g h).mpr
  exact three_images_determine_scalar_class _ _ (gl_nondegenerate g) (gl_nondegenerate h) hinf hzero hone

end
end AEGPaper0.ProjectiveGeneralLinear

#print axioms AEGPaper0.ProjectiveGeneralLinear.coefficients_toMatrix
#print axioms AEGPaper0.ProjectiveGeneralLinear.toMatrix_coefficients
#print axioms AEGPaper0.ProjectiveGeneralLinear.coefficients_determinant
#print axioms AEGPaper0.ProjectiveGeneralLinear.toMatrix_determinant
#print axioms AEGPaper0.ProjectiveGeneralLinear.coefficients_product
#print axioms AEGPaper0.ProjectiveGeneralLinear.coefficients_one
#print axioms AEGPaper0.ProjectiveGeneralLinear.gl_nondegenerate
#print axioms AEGPaper0.ProjectiveGeneralLinear.toGL_coefficients
#print axioms AEGPaper0.ProjectiveGeneralLinear.coefficients_injective
#print axioms AEGPaper0.ProjectiveGeneralLinear.actionHom_apply
#print axioms AEGPaper0.ProjectiveGeneralLinear.actionHom_kernel_scalar
#print axioms AEGPaper0.ProjectiveGeneralLinear.actionHom_equal_iff_scalar
#print axioms AEGPaper0.ProjectiveGeneralLinear.scalarSubgroup_eq_kernel
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotientAction_representative
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotient_equality_iff_action
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotient_equality_iff_nonzero_scalar
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotient_action_injective
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotient_action_mul
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotient_action_one
#print axioms AEGPaper0.ProjectiveGeneralLinear.quotient_action_inverse
#print axioms AEGPaper0.ProjectiveGeneralLinear.scalarMatrix_standard
#print axioms AEGPaper0.ProjectiveGeneralLinear.scalarSubgroup_matrix_membership
#print axioms AEGPaper0.ProjectiveGeneralLinear.three_points_determine_quotient
