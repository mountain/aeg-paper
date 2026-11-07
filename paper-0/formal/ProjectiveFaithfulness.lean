import ProjectiveLine

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   Faithfulness modulo nonzero matrix scalars over every field. Equality of
   all projective point actions determines a scalar class, not a literal
   matrix or an arithmetic history. -/
namespace AEGPaper0.ProjectiveFaithfulness

noncomputable section
open ProjectiveLine
variable {K : Type*} [Field K]

omit [Field K] in
@[ext] theorem matrix_ext {m n : Matrix2 K} (ha : m.a=n.a) (hb : m.b=n.b)
    (hc : m.c=n.c) (hd : m.d=n.d) : m=n := by
  cases m; cases n; cases ha; cases hb; cases hc; cases hd; rfl

theorem multiply_assoc (m n p : Matrix2 K) : multiply (multiply m n) p = multiply m (multiply n p) := by
  apply matrix_ext <;> dsimp [multiply] <;> ring

theorem multiply_one_left (m : Matrix2 K) : multiply identity m = m := by
  apply matrix_ext <;> simp [multiply, identity]

theorem multiply_one_right (m : Matrix2 K) : multiply m identity = m := by
  apply matrix_ext <;> simp [multiply, identity]

theorem scale_one (m : Matrix2 K) : scaleMatrix 1 m = m := by
  apply matrix_ext <;> simp [scaleMatrix]

theorem scale_scale (s t : K) (m : Matrix2 K) : scaleMatrix s (scaleMatrix t m) = scaleMatrix (s*t) m := by
  apply matrix_ext <;> dsimp [scaleMatrix] <;> ring

theorem scale_multiply_left (s : K) (m n : Matrix2 K) :
    multiply (scaleMatrix s m) n = scaleMatrix s (multiply m n) := by
  apply matrix_ext <;> dsimp [scaleMatrix, multiply] <;> ring

theorem scale_multiply_right (s : K) (m n : Matrix2 K) :
    multiply m (scaleMatrix s n) = scaleMatrix s (multiply m n) := by
  apply matrix_ext <;> dsimp [scaleMatrix, multiply] <;> ring

theorem determinant_scale (s : K) (m : Matrix2 K) :
    determinant (scaleMatrix s m) = s^2 * determinant m := by
  dsimp [determinant, scaleMatrix]; ring

theorem matrix_adjugate_left (m : Matrix2 K) :
    multiply (adjugate m) m = scaleMatrix (determinant m) identity := by
  apply matrix_ext <;> dsimp [multiply, adjugate, scaleMatrix, determinant, identity] <;> ring

theorem matrix_adjugate_right (m : Matrix2 K) :
    multiply m (adjugate m) = scaleMatrix (determinant m) identity := by
  apply matrix_ext <;> dsimp [multiply, adjugate, scaleMatrix, determinant, identity] <;> ring

theorem three_fixed_points_force_scalar (m : Matrix2 K) (hd : determinant m ≠ 0)
    (hinf : act m none = none) (hzero : act m (some 0) = some 0)
    (hone : act m (some 1) = some 1) :
    ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s identity := by
  have hc := (fixes_infinity_iff m).mp hinf
  have hAD : m.a*m.d ≠ 0 := by simpa [determinant, hc] using hd
  have hD : m.d ≠ 0 := (mul_ne_zero_iff.mp hAD).2
  rw [finite_action] at hzero hone
  simp only [hc, zero_add, mul_zero, hD, if_false, Option.some.injEq] at hzero
  have hb : m.b = 0 := ((div_eq_zero_iff).mp hzero).resolve_right hD
  simp only [hc, zero_add, mul_one, hb, add_zero, hD, if_false, Option.some.injEq] at hone
  have ha : m.a=m.d := (div_eq_one_iff_eq hD).mp hone
  refine ⟨m.d, hD, ?_⟩
  apply matrix_ext <;> simp [scaleMatrix, identity, ha, hb, hc]

theorem identity_action_iff_scalar (m : Matrix2 K) (hd : determinant m ≠ 0) :
    (∀ x : Point K, act m x = x) ↔ ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s identity := by
  constructor
  · intro h; exact three_fixed_points_force_scalar m hd (h none) (h (some 0)) (h (some 1))
  · rintro ⟨s, hs, he⟩ x
    rw [he, action_scale _ _ _ hs, action_identity]

theorem equal_actions_iff_nonzero_scalar (m n : Matrix2 K)
    (hm : determinant m ≠ 0) (hn : determinant n ≠ 0) :
    (∀ x : Point K, act m x = act n x) ↔ ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s n := by
  constructor
  · intro h
    let r := multiply (adjugate n) m
    have hr : determinant r ≠ 0 := by
      dsimp [r]; rw [determinant_multiply, determinant_adjugate]; exact mul_ne_zero hn hm
    have he : ∀ x : Point K, act r x = x := by
      intro x
      dsimp [r]
      rw [action_multiply _ _ x hm, h x, action_adjugate_left n x hn]
    obtain ⟨s, hs, hsI⟩ := (identity_action_iff_scalar r hr).mp he
    have heq : scaleMatrix (determinant n) m = scaleMatrix s n := by
      calc
        _ = multiply (multiply n (adjugate n)) m := by rw [matrix_adjugate_right, scale_multiply_left, multiply_one_left]
        _ = multiply n r := multiply_assoc n (adjugate n) m
        _ = scaleMatrix s n := by rw [hsI, scale_multiply_right, multiply_one_right]
    refine ⟨s / determinant n, div_ne_zero hs hn, ?_⟩
    have hh := congrArg (scaleMatrix (determinant n)⁻¹) heq
    simpa [scale_scale, scale_one, hn, div_eq_mul_inv, mul_comm] using hh
  · rintro ⟨s, hs, he⟩ x
    rw [he, action_scale _ _ _ hs]

theorem three_images_determine_scalar_class (m n : Matrix2 K)
    (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hinf : act m none = act n none) (hzero : act m (some 0) = act n (some 0))
    (hone : act m (some 1) = act n (some 1)) :
    ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s n := by
  let r := multiply (adjugate n) m
  have hr : determinant r ≠ 0 := by
    dsimp [r]; rw [determinant_multiply, determinant_adjugate]; exact mul_ne_zero hn hm
  have hinf' : act r none = none := by
    dsimp [r]; rw [action_multiply _ _ _ hm, hinf, action_adjugate_left n _ hn]
  have hzero' : act r (some 0) = some 0 := by
    dsimp [r]; rw [action_multiply _ _ _ hm, hzero, action_adjugate_left n _ hn]
  have hone' : act r (some 1) = some 1 := by
    dsimp [r]; rw [action_multiply _ _ _ hm, hone, action_adjugate_left n _ hn]
  obtain ⟨s, hs, hscalar⟩ := three_fixed_points_force_scalar r hr hinf' hzero' hone'
  apply (equal_actions_iff_nonzero_scalar m n hm hn).mp
  intro x
  have he : act r x=x := (identity_action_iff_scalar r hr).mpr ⟨s,hs,hscalar⟩ x
  dsimp [r] at he
  rw [action_multiply _ _ _ hm] at he
  have hh := congrArg (act n) he
  rw [action_adjugate_right n _ hn] at hh
  exact hh

theorem equivalence_equality_iff_scalar (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0) :
    actionEquiv m hm = actionEquiv n hn ↔ ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s n := by
  rw [← equal_actions_iff_nonzero_scalar m n hm hn]
  exact Equiv.ext_iff

theorem literal_matrix_equality_is_stronger :
    (∀ x : Point ℚ, act (scaleMatrix 2 identity) x = act identity x) ∧
      (scaleMatrix 2 (identity : Matrix2 ℚ)) ≠ identity := by
  refine ⟨fun x => action_scale 2 identity x (by norm_num), ?_⟩
  intro h
  have hh := congrArg Matrix2.a h
  norm_num [scaleMatrix, identity] at hh

theorem one_point_agreement_is_insufficient :
    act (⟨1,1,0,1⟩ : Matrix2 K) none = act identity none ∧
      act (⟨1,1,0,1⟩ : Matrix2 K) (some 0) ≠ act identity (some 0) := by
  classical
  simp [act, project, homogeneous, mapVec, identity]

end
end AEGPaper0.ProjectiveFaithfulness

#print axioms AEGPaper0.ProjectiveFaithfulness.matrix_ext
#print axioms AEGPaper0.ProjectiveFaithfulness.multiply_assoc
#print axioms AEGPaper0.ProjectiveFaithfulness.multiply_one_left
#print axioms AEGPaper0.ProjectiveFaithfulness.multiply_one_right
#print axioms AEGPaper0.ProjectiveFaithfulness.scale_one
#print axioms AEGPaper0.ProjectiveFaithfulness.scale_scale
#print axioms AEGPaper0.ProjectiveFaithfulness.scale_multiply_left
#print axioms AEGPaper0.ProjectiveFaithfulness.scale_multiply_right
#print axioms AEGPaper0.ProjectiveFaithfulness.determinant_scale
#print axioms AEGPaper0.ProjectiveFaithfulness.matrix_adjugate_left
#print axioms AEGPaper0.ProjectiveFaithfulness.matrix_adjugate_right
#print axioms AEGPaper0.ProjectiveFaithfulness.three_fixed_points_force_scalar
#print axioms AEGPaper0.ProjectiveFaithfulness.identity_action_iff_scalar
#print axioms AEGPaper0.ProjectiveFaithfulness.equal_actions_iff_nonzero_scalar
#print axioms AEGPaper0.ProjectiveFaithfulness.three_images_determine_scalar_class
#print axioms AEGPaper0.ProjectiveFaithfulness.equivalence_equality_iff_scalar
#print axioms AEGPaper0.ProjectiveFaithfulness.literal_matrix_equality_is_stronger
#print axioms AEGPaper0.ProjectiveFaithfulness.one_point_agreement_is_insufficient
