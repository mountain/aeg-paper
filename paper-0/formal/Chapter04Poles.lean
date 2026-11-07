import Mathlib.Tactic

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   The pole laws use bijections of a pointed carrier. Nondegenerate projective
   actions satisfy this interface, but their PGL representation is a separate
   obligation. The coefficient lemmas below are exact real matrix algebra.
   Composition is explicitly P after Q, matching chronological prefixes. -/
namespace AEGPaper0.Chapter04Poles

variable {X : Type*}

def compose (P Q : Equiv.Perm X) : Equiv.Perm X := Q.trans P
def pole (infinity : X) (P : Equiv.Perm X) : X := P.symm infinity
def fixesInfinity (infinity : X) (P : Equiv.Perm X) : Prop := P infinity = infinity

theorem composition_apply (P Q : Equiv.Perm X) (x : X) :
    compose P Q x = P (Q x) := rfl

theorem pole_covariance (infinity : X) (P Q : Equiv.Perm X) :
    pole infinity (compose P Q) = Q.symm (pole infinity P) := rfl

theorem pole_is_unique_preimage (infinity x : X) (P : Equiv.Perm X) :
    P x = infinity ↔ x = pole infinity P := P.apply_eq_iff_eq_symm_apply

theorem pole_eq_infinity_iff (infinity : X) (P : Equiv.Perm X) :
    pole infinity P = infinity ↔ fixesInfinity infinity P := by
  unfold pole fixesInfinity
  rw [Equiv.symm_apply_eq]
  exact eq_comm

theorem pole_constancy_criterion (infinity : X) (P Q : Equiv.Perm X) :
    pole infinity (compose P Q) = pole infinity Q ↔ fixesInfinity infinity P := by
  rw [pole_covariance]
  change Q.symm (pole infinity P) = Q.symm infinity ↔ _
  rw [Q.symm.injective.eq_iff, pole_eq_infinity_iff]

theorem pole_moves_iff (infinity : X) (P Q : Equiv.Perm X) :
    pole infinity (compose P Q) ≠ pole infinity Q ↔ ¬ fixesInfinity infinity P := by
  exact not_congr (pole_constancy_criterion infinity P Q)

def prefixMap (F : ℕ → Equiv.Perm X) : ℕ → Equiv.Perm X
  | 0 => Equiv.refl X
  | n + 1 => compose (F n) (prefixMap F n)

theorem prefix_initial_pole (infinity : X) (F : ℕ → Equiv.Perm X) :
    pole infinity (prefixMap F 0) = infinity := rfl

theorem prefix_successor_apply (F : ℕ → Equiv.Perm X) (n : ℕ) (x : X) :
    prefixMap F (n + 1) x = F n (prefixMap F n x) := rfl

theorem prefix_pole_covariance (infinity : X) (F : ℕ → Equiv.Perm X) (n : ℕ) :
    pole infinity (prefixMap F (n + 1)) = (prefixMap F n).symm (pole infinity (F n)) := rfl

theorem prefix_step_pole_iff (infinity : X) (F : ℕ → Equiv.Perm X) (n : ℕ) :
    pole infinity (prefixMap F (n + 1)) = pole infinity (prefixMap F n) ↔
      fixesInfinity infinity (F n) := pole_constancy_criterion infinity (F n) (prefixMap F n)

theorem history_step_rigidity (infinity : X) (F : ℕ → Equiv.Perm X) (n : ℕ) :
    (∀ k < n, pole infinity (prefixMap F (k + 1)) = pole infinity (prefixMap F k)) ↔
      (∀ k < n, fixesInfinity infinity (F k)) := by
  simp_rw [prefix_step_pole_iff]

theorem affine_prefix_fixes_infinity (infinity : X) (F : ℕ → Equiv.Perm X) (n : ℕ)
    (h : ∀ k < n, fixesInfinity infinity (F k)) : fixesInfinity infinity (prefixMap F n) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    change F n (prefixMap F n infinity) = infinity
    rw [ih (fun k hk => h k (Nat.lt_trans hk (Nat.lt_succ_self n)))]
    exact h n (Nat.lt_succ_self n)

theorem history_prefix_rigidity (infinity : X) (F : ℕ → Equiv.Perm X) (n : ℕ) :
    (∀ k ≤ n, pole infinity (prefixMap F k) = infinity) ↔
      (∀ k < n, fixesInfinity infinity (F k)) := by
  constructor
  · intro h k hk
    apply (prefix_step_pole_iff infinity F k).mp
    rw [h (k + 1) (by omega), h k (by omega)]
  · intro h k hk
    apply (pole_eq_infinity_iff infinity _).mpr
    exact affine_prefix_fixes_infinity infinity F k (fun j hj => h j (lt_of_lt_of_le hj hk))

theorem first_nonaffine_step_moves_pole (infinity : X) (F : ℕ → Equiv.Perm X) (n : ℕ)
    (hprev : ∀ k < n, fixesInfinity infinity (F k)) (hstep : ¬ fixesInfinity infinity (F n)) :
    pole infinity (prefixMap F (n + 1)) ≠ infinity := by
  have hp := (pole_eq_infinity_iff infinity _).mpr (affine_prefix_fixes_infinity infinity F n hprev)
  have hm := (pole_moves_iff infinity (F n) (prefixMap F n)).mpr hstep
  simpa only [hp] using hm

theorem postcompose_affine_keeps_current_pole (infinity : X) (P Q : Equiv.Perm X)
    (h : fixesInfinity infinity P) : pole infinity (compose P Q) = pole infinity Q :=
  (pole_constancy_criterion infinity P Q).mpr h

theorem terminal_pole_does_not_detect_every_step (infinity x : X) (hx : x ≠ infinity) :
    ∃ F : ℕ → Equiv.Perm X,
      ¬ fixesInfinity infinity (F 0) ∧ pole infinity (prefixMap F 2) = infinity := by
  classical
  let P := Equiv.swap infinity x
  refine ⟨fun _ => P, ?_, ?_⟩
  · simpa [fixesInfinity, P] using hx
  · simp [prefixMap, compose, pole, P]

/- A finite boundary point is a nonzero homogeneous column (u,v), with
   infinity characterized by v=0. No quotient equality is assumed here. -/
theorem pole_column_nonzero (A B C D : ℝ) (hd : A * D - B * C ≠ 0) :
    (-D, C) ≠ (0, 0) := by
  intro h
  have hD : D = 0 := neg_eq_zero.mp (congrArg Prod.fst h)
  have hC : C = 0 := congrArg Prod.snd h
  exact hd (by simp [hD, hC])

theorem pole_column_annihilates_denominator (C D : ℝ) :
    C * (-D) + D * C = 0 := by ring

theorem finite_pole_denominator_zero (C D : ℝ) (hc : C ≠ 0) :
    C * (-D / C) + D = 0 := by field_simp; ring

theorem finite_pole_numerator_nonzero (A B C D : ℝ)
    (hd : A * D - B * C ≠ 0) (hc : C ≠ 0) : A * (-D / C) + B ≠ 0 := by
  intro h
  apply hd
  have hh := (div_eq_zero_iff).mp (show (-A * D + B * C) / C = 0 by
    calc
      _ = A * (-D / C) + B := by field_simp
      _ = 0 := h)
  have hh' := hh.resolve_right hc
  linarith [hh']

theorem affine_infinity_criterion (A B C D : ℝ) (hd : A * D - B * C ≠ 0) :
    C = 0 ↔ (C = 0 ∧ A ≠ 0) := by
  constructor
  · intro hc
    refine ⟨hc, ?_⟩
    intro ha; apply hd; simp [hc, ha]
  · exact And.left

end AEGPaper0.Chapter04Poles

#print axioms AEGPaper0.Chapter04Poles.composition_apply
#print axioms AEGPaper0.Chapter04Poles.pole_covariance
#print axioms AEGPaper0.Chapter04Poles.pole_is_unique_preimage
#print axioms AEGPaper0.Chapter04Poles.pole_eq_infinity_iff
#print axioms AEGPaper0.Chapter04Poles.pole_constancy_criterion
#print axioms AEGPaper0.Chapter04Poles.pole_moves_iff
#print axioms AEGPaper0.Chapter04Poles.prefix_initial_pole
#print axioms AEGPaper0.Chapter04Poles.prefix_successor_apply
#print axioms AEGPaper0.Chapter04Poles.prefix_pole_covariance
#print axioms AEGPaper0.Chapter04Poles.prefix_step_pole_iff
#print axioms AEGPaper0.Chapter04Poles.history_step_rigidity
#print axioms AEGPaper0.Chapter04Poles.affine_prefix_fixes_infinity
#print axioms AEGPaper0.Chapter04Poles.history_prefix_rigidity
#print axioms AEGPaper0.Chapter04Poles.first_nonaffine_step_moves_pole
#print axioms AEGPaper0.Chapter04Poles.postcompose_affine_keeps_current_pole
#print axioms AEGPaper0.Chapter04Poles.terminal_pole_does_not_detect_every_step
#print axioms AEGPaper0.Chapter04Poles.pole_column_nonzero
#print axioms AEGPaper0.Chapter04Poles.pole_column_annihilates_denominator
#print axioms AEGPaper0.Chapter04Poles.finite_pole_denominator_zero
#print axioms AEGPaper0.Chapter04Poles.finite_pole_numerator_nonzero
#print axioms AEGPaper0.Chapter04Poles.affine_infinity_criterion
