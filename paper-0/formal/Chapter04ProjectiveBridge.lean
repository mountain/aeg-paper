import ProjectiveLine
import Chapter04Poles

/- Original CC0 continuation by Codex (OpenAI), 2026-11-07.
   Concrete nondegenerate matrices now supply the actual bijections required
   by the preceding pole laws. Products act in chronological right-to-left
   order. This is a field-generic homogeneous quotient/chart model, not an
   asserted identification with every external PGL API. -/
namespace AEGPaper0.Chapter04ProjectiveBridge

noncomputable section
open ProjectiveLine
variable {K : Type*} [Field K]

def matrixPole (m : Matrix2 K) (hd : determinant m ≠ 0) : Point K :=
  Chapter04Poles.pole none (actionEquiv m hd)

theorem equiv_product (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hmn : determinant (multiply m n) ≠ 0) :
    actionEquiv (multiply m n) hmn = Chapter04Poles.compose (actionEquiv m hm) (actionEquiv n hn) := by
  apply Equiv.ext
  intro x
  exact action_multiply m n x hn

theorem concrete_pole_covariance (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hmn : determinant (multiply m n) ≠ 0) :
    matrixPole (multiply m n) hmn = (actionEquiv n hn).symm (matrixPole m hm) := by
  unfold matrixPole
  rw [equiv_product m n hm hn hmn]
  exact Chapter04Poles.pole_covariance none _ _

theorem concrete_stabilizer_criterion (m : Matrix2 K) (hm : determinant m ≠ 0) :
    Chapter04Poles.fixesInfinity none (actionEquiv m hm) ↔ m.c = 0 := fixes_infinity_iff m

theorem concrete_pole_at_infinity_iff (m : Matrix2 K) (hm : determinant m ≠ 0) :
    matrixPole m hm = none ↔ m.c = 0 := by
  rw [matrixPole, Chapter04Poles.pole_eq_infinity_iff]
  exact concrete_stabilizer_criterion m hm

theorem concrete_finite_pole (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    matrixPole m hm = some (-m.d/m.c) := by
  unfold matrixPole Chapter04Poles.pole
  rw [pole_formula]
  simp only [hc, if_false]

theorem concrete_step_constancy (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hmn : determinant (multiply m n) ≠ 0) :
    matrixPole (multiply m n) hmn = matrixPole n hn ↔ m.c = 0 := by
  unfold matrixPole
  rw [equiv_product m n hm hn hmn, Chapter04Poles.pole_constancy_criterion]
  exact concrete_stabilizer_criterion m hm

theorem affine_postcompose_keeps_pole (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hmn : determinant (multiply m n) ≠ 0) (hc : m.c = 0) :
    matrixPole (multiply m n) hmn = matrixPole n hn :=
  (concrete_step_constancy m n hm hn hmn).mpr hc

abbrev Nondegenerate (K : Type*) [Field K] := {m : Matrix2 K // determinant m ≠ 0}
def prefixMatrix (F : ℕ → Nondegenerate K) : ℕ → Matrix2 K
  | 0 => identity
  | n+1 => multiply (F n).val (prefixMatrix F n)

theorem prefix_nondegenerate (F : ℕ → Nondegenerate K) (n : ℕ) : determinant (prefixMatrix F n) ≠ 0 := by
  induction n with
  | zero => simp [prefixMatrix, identity, determinant]
  | succ n ih =>
    rw [prefixMatrix, determinant_multiply]
    exact mul_ne_zero (F n).property ih

theorem prefix_equiv (F : ℕ → Nondegenerate K) (n : ℕ) :
    actionEquiv (prefixMatrix F n) (prefix_nondegenerate F n) =
      Chapter04Poles.prefixMap (fun k => actionEquiv (F k).val (F k).property) n := by
  induction n with
  | zero => apply Equiv.ext; intro x; exact action_identity x
  | succ n ih =>
    change actionEquiv (multiply (F n).val (prefixMatrix F n)) _ =
      Chapter04Poles.compose (actionEquiv (F n).val (F n).property)
        (Chapter04Poles.prefixMap (fun k => actionEquiv (F k).val (F k).property) n)
    rw [equiv_product _ _ (F n).property (prefix_nondegenerate F n), ih]

theorem concrete_history_step_rigidity (F : ℕ → Nondegenerate K) (n : ℕ) :
    (∀ k < n, matrixPole (prefixMatrix F (k+1)) (prefix_nondegenerate F (k+1)) =
      matrixPole (prefixMatrix F k) (prefix_nondegenerate F k)) ↔
      (∀ k < n, (F k).val.c = 0) := by
  simp only [matrixPole, prefix_equiv, Chapter04Poles.prefix_step_pole_iff, concrete_stabilizer_criterion]

theorem concrete_history_prefix_rigidity (F : ℕ → Nondegenerate K) (n : ℕ) :
    (∀ k ≤ n, matrixPole (prefixMatrix F k) (prefix_nondegenerate F k) = none) ↔
      (∀ k < n, (F k).val.c = 0) := by
  simp only [matrixPole, prefix_equiv, Chapter04Poles.history_prefix_rigidity, concrete_stabilizer_criterion]

theorem first_exit_has_finite_pole (F : ℕ → Nondegenerate K) (n : ℕ)
    (hprev : ∀ k < n, (F k).val.c = 0) (hstep : (F n).val.c ≠ 0) :
    (prefixMatrix F (n+1)).c ≠ 0 ∧
    matrixPole (prefixMatrix F (n+1)) (prefix_nondegenerate F (n+1)) =
      some (-(prefixMatrix F (n+1)).d/(prefixMatrix F (n+1)).c) := by
  have hmove := Chapter04Poles.first_nonaffine_step_moves_pole none
    (fun k => actionEquiv (F k).val (F k).property) n
    (fun k hk => (concrete_stabilizer_criterion _ _).mpr (hprev k hk))
    (fun h => hstep ((concrete_stabilizer_criterion _ _).mp h))
  have hp : matrixPole (prefixMatrix F (n+1)) (prefix_nondegenerate F (n+1)) ≠ none := by
    simpa only [matrixPole, prefix_equiv] using hmove
  have hc := mt (concrete_pole_at_infinity_iff _ _).mpr hp
  exact ⟨hc, concrete_finite_pole _ _ hc⟩

def translation (s : K) : Matrix2 K := ⟨1, s, 0, 1⟩
def dilation (s : K) : Matrix2 K := ⟨s, 0, 0, 1⟩
def inversion : Matrix2 K := ⟨0, -1, 1, 0⟩

theorem translation_determinant (s : K) : determinant (translation s) = 1 := by simp [determinant, translation]
theorem dilation_determinant (s : K) : determinant (dilation s) = s := by simp [determinant, dilation]
theorem inversion_determinant : determinant (inversion : Matrix2 K) = 1 := by simp [determinant, inversion]

theorem translation_finite (s x : K) : act (translation s) (some x) = some (x+s) := by
  rw [finite_action]; simp [translation]
theorem dilation_finite (s x : K) : act (dilation s) (some x) = some (s*x) := by
  rw [finite_action]; simp [dilation]
theorem inversion_infinity : act (inversion : Matrix2 K) none = some 0 := by
  rw [infinity_action]; simp [inversion]
theorem inversion_zero : act (inversion : Matrix2 K) (some 0) = none := by
  rw [finite_action]; simp [inversion]
theorem inversion_finite (x : K) (hx : x ≠ 0) : act inversion (some x) = some (-1/x) := by
  rw [finite_action]; simp [inversion, hx]

theorem affine_diagonal_nonzero (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c = 0) :
    m.a ≠ 0 ∧ m.d ≠ 0 := by
  have h : m.a*m.d ≠ 0 := by simpa [determinant, hc] using hm
  exact mul_ne_zero_iff.mp h

theorem affine_matrix_factorization (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c = 0) :
    multiply (translation (m.b/m.d)) (dilation (m.a/m.d)) = scaleMatrix (1/m.d) m := by
  have hd := (affine_diagonal_nonzero m hm hc).2
  cases m
  simp only [multiply, translation, dilation, scaleMatrix]
  simp_all [div_eq_mul_inv, mul_comm]

theorem nonaffine_scale_nonzero (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    determinant m / m.c^2 ≠ 0 := div_ne_zero hm (pow_ne_zero 2 hc)

theorem nonaffine_matrix_factorization (m : Matrix2 K) (hc : m.c ≠ 0) :
    multiply (translation (m.a/m.c))
      (multiply (dilation (determinant m/m.c^2)) (multiply inversion (translation (m.d/m.c)))) =
      scaleMatrix (1/m.c) m := by
  cases m
  simp only [multiply, translation, dilation, inversion, scaleMatrix, determinant]
  congr 1 <;> field_simp <;> ring

theorem affine_action_factorization (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c = 0) (x : Point K) :
    act m x = act (translation (m.b/m.d)) (act (dilation (m.a/m.d)) x) := by
  have hD : determinant (dilation (m.a/m.d)) ≠ 0 := by
    rw [dilation_determinant]
    exact div_ne_zero (affine_diagonal_nonzero m hm hc).1 (affine_diagonal_nonzero m hm hc).2
  rw [← action_multiply _ _ x hD]
  rw [affine_matrix_factorization m hm hc, action_scale _ _ _ (one_div_ne_zero (affine_diagonal_nonzero m hm hc).2)]

theorem nonaffine_action_factorization (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) (x : Point K) :
    act m x = act (translation (m.a/m.c))
      (act (dilation (determinant m/m.c^2)) (act inversion (act (translation (m.d/m.c)) x))) := by
  have hT : determinant (translation (m.d/m.c)) ≠ 0 := by rw [translation_determinant]; exact one_ne_zero
  have hJT : determinant (multiply inversion (translation (m.d/m.c))) ≠ 0 := by
    rw [determinant_multiply, inversion_determinant, one_mul]; exact hT
  have hDJT : determinant (multiply (dilation (determinant m/m.c^2))
      (multiply inversion (translation (m.d/m.c)))) ≠ 0 := by
    rw [determinant_multiply, dilation_determinant]
    exact mul_ne_zero (nonaffine_scale_nonzero m hm hc) hJT
  rw [← action_multiply _ _ _ hT, ← action_multiply _ _ _ hJT, ← action_multiply _ _ _ hDJT,
    nonaffine_matrix_factorization m hc, action_scale _ _ _ (one_div_ne_zero hc)]

theorem singular_composition_counterexample :
    act (multiply (inversion : Matrix2 K) ⟨0,0,0,0⟩) none ≠
      act inversion (act ⟨0,0,0,0⟩ none) := by
  classical
  simp [act, project, homogeneous, mapVec, multiply, inversion]

end
end AEGPaper0.Chapter04ProjectiveBridge

#print axioms AEGPaper0.Chapter04ProjectiveBridge.equiv_product
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_pole_covariance
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_stabilizer_criterion
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_pole_at_infinity_iff
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_finite_pole
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_step_constancy
#print axioms AEGPaper0.Chapter04ProjectiveBridge.affine_postcompose_keeps_pole
#print axioms AEGPaper0.Chapter04ProjectiveBridge.prefix_nondegenerate
#print axioms AEGPaper0.Chapter04ProjectiveBridge.prefix_equiv
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_history_step_rigidity
#print axioms AEGPaper0.Chapter04ProjectiveBridge.concrete_history_prefix_rigidity
#print axioms AEGPaper0.Chapter04ProjectiveBridge.first_exit_has_finite_pole
#print axioms AEGPaper0.Chapter04ProjectiveBridge.translation_determinant
#print axioms AEGPaper0.Chapter04ProjectiveBridge.dilation_determinant
#print axioms AEGPaper0.Chapter04ProjectiveBridge.inversion_determinant
#print axioms AEGPaper0.Chapter04ProjectiveBridge.translation_finite
#print axioms AEGPaper0.Chapter04ProjectiveBridge.dilation_finite
#print axioms AEGPaper0.Chapter04ProjectiveBridge.inversion_infinity
#print axioms AEGPaper0.Chapter04ProjectiveBridge.inversion_zero
#print axioms AEGPaper0.Chapter04ProjectiveBridge.inversion_finite
#print axioms AEGPaper0.Chapter04ProjectiveBridge.affine_diagonal_nonzero
#print axioms AEGPaper0.Chapter04ProjectiveBridge.affine_matrix_factorization
#print axioms AEGPaper0.Chapter04ProjectiveBridge.nonaffine_scale_nonzero
#print axioms AEGPaper0.Chapter04ProjectiveBridge.nonaffine_matrix_factorization
#print axioms AEGPaper0.Chapter04ProjectiveBridge.affine_action_factorization
#print axioms AEGPaper0.Chapter04ProjectiveBridge.nonaffine_action_factorization
#print axioms AEGPaper0.Chapter04ProjectiveBridge.singular_composition_counterexample
