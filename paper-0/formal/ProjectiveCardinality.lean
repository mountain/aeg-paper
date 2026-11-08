import AffineIteration

/- Original CC0 proofs by Codex (OpenAI), 2026-11-08.
   A nonidentity PGL element has at most two fixed points over any field.
   All points may be fixed by identity; zero/one/two cases need not all occur
   in every field. Explicit occurrence witnesses below are over the rationals. -/
namespace AEGPaper0.ProjectiveCardinality

noncomputable section
open ProjectiveLine ProjectiveGeneralLinear ProjectiveGeneration
open AffineStabilizer ProjectiveBruhat ProjectiveFixedPoints AffineIteration
variable {K : Type*} [Field K]

theorem conjugate_identity_iff (s g : PGL2 K) : s*g*s⁻¹=1 ↔ g=1 := by
  constructor
  · intro h
    have he : g=s⁻¹*(s*g*s⁻¹)*s := by group
    rw [h] at he
    simpa using he
  · intro h; rw [h]; group

theorem affine_nonidentity_fixed_subset (g : PGL2 K) (hg : g ∈ infinityStabilizer) (h1 : g ≠ 1) :
    ∃ z : K, fixedSet g ⊆ {none,some z} := by
  obtain ⟨e,he⟩ := toStabilizer_surjective ⟨g,hg⟩
  have hc : affineClass e=g := congrArg Subtype.val he
  have hn : e=normalizedAffine (AffineStabilizer.slope e) (offset e) (slope_nonzero e) := by
    apply AffineEquiv.ext
    intro z
    exact affine_formula e z
  rw [hn] at hc
  rw [← hc]
  by_cases hs : AffineStabilizer.slope e=1
  · have heq : normalizedAffine (AffineStabilizer.slope e) (offset e) (slope_nonzero e)=
        normalizedAffine (1:K) (offset e) one_ne_zero := by
      apply AffineEquiv.ext; intro z; simp only [normalizedAffine_apply,hs]
    have hb : offset e ≠ 0 := by
      intro hb
      apply h1
      rw [← hc,heq,hb]
      have hi : normalizedAffine (1:K) 0 one_ne_zero=(1:Aff K) := by
        apply AffineEquiv.ext; intro z; simp [normalizedAffine_apply]
      rw [hi,affineClass_one]
    refine ⟨0,?_⟩
    rw [heq,affine_fixed_set_translation _ hb]
    exact Set.singleton_subset_iff.mpr (by simp)
  · exact ⟨_,(affine_fixed_set_slope_ne_one _ _ _ hs).subset⟩

theorem nonidentity_fixed_subset_pair (g : PGL2 K) (hg : g ≠ 1) :
    ∃ p q : Point K, fixedSet g ⊆ {p,q} := by
  by_cases hf : ∃ p, p ∈ fixedSet g
  · obtain ⟨p,hp⟩ := hf
    cases p with
    | none =>
      obtain ⟨z,hz⟩ := affine_nonidentity_fixed_subset g hp hg
      exact ⟨none,some z,hz⟩
    | some x =>
      let s := poleGauge x
      have hs : s*g*s⁻¹ ∈ infinityStabilizer := (finite_stabilizer_iff x g).mp hp
      have hne : s*g*s⁻¹ ≠ 1 := fun h => hg ((conjugate_identity_iff s g).mp h)
      obtain ⟨z,hz⟩ := affine_nonidentity_fixed_subset _ hs hne
      refine ⟨ProjectiveGeneralLinear.quotientAction s⁻¹ none,
        ProjectiveGeneralLinear.quotientAction s⁻¹ (some z),?_⟩
      intro p hp
      have ht := (fixedPointConjugacy s g ⟨p,hp⟩).property
      have hm := hz ht
      simp only [Set.mem_insert_iff,Set.mem_singleton_iff] at hm ⊢
      cases hm with
      | inl h =>
        apply Or.inl
        have he := congrArg (fun y => ProjectiveGeneralLinear.quotientAction s⁻¹ y) h
        dsimp only [fixedPointConjugacy_apply] at he
        rw [quotient_action_inverse] at he
        exact he
      | inr h =>
        apply Or.inr
        have he := congrArg (fun y => ProjectiveGeneralLinear.quotientAction s⁻¹ y) h
        dsimp only [fixedPointConjugacy_apply] at he
        rw [quotient_action_inverse] at he
        exact he
  · refine ⟨none,none,?_⟩
    intro p hp
    exact False.elim (hf ⟨p,hp⟩)

theorem nonidentity_fixed_finite (g : PGL2 K) (hg : g ≠ 1) : (fixedSet g).Finite := by
  obtain ⟨p,q,h⟩ := nonidentity_fixed_subset_pair g hg
  exact ((Set.finite_singleton q).insert p).subset h

theorem nonidentity_fixed_ncard_le_two (g : PGL2 K) (hg : g ≠ 1) : (fixedSet g).ncard ≤ 2 := by
  obtain ⟨p,q,h⟩ := nonidentity_fixed_subset_pair g hg
  calc
    (fixedSet g).ncard ≤ ({p,q}:Set (Point K)).ncard := Set.ncard_le_ncard h ((Set.finite_singleton q).insert p)
    _ ≤ 2 := by simpa using Set.ncard_insert_le p ({q}:Set (Point K))

theorem nonidentity_fixed_cardinality_cases (g : PGL2 K) (hg : g ≠ 1) :
    (fixedSet g).ncard=0 ∨ (fixedSet g).ncard=1 ∨ (fixedSet g).ncard=2 := by
  have h := nonidentity_fixed_ncard_le_two g hg
  omega

theorem nonidentity_fixed_set_cases (g : PGL2 K) (hg : g ≠ 1) :
    fixedSet g=∅ ∨ (∃ p, fixedSet g={p}) ∨ ∃ p q, p ≠ q ∧ fixedSet g={p,q} := by
  obtain ⟨p,q,h⟩ := nonidentity_fixed_subset_pair g hg
  by_cases hp : p ∈ fixedSet g <;> by_cases hq : q ∈ fixedSet g
  · by_cases he : p=q
    · apply Or.inr; apply Or.inl
      refine ⟨p,?_⟩
      ext x
      constructor
      · intro hx; have hh := h hx; simpa [he] using hh
      · intro hx; have hx' : x=p := hx; rw [hx']; exact hp
    · apply Or.inr; apply Or.inr
      refine ⟨p,q,he,?_⟩
      exact Set.Subset.antisymm h (by intro x hx; simp only [Set.mem_insert_iff,Set.mem_singleton_iff] at hx; rcases hx with rfl|rfl <;> assumption)
  · apply Or.inr; apply Or.inl
    refine ⟨p,?_⟩
    ext x
    constructor
    · intro hx
      have hh := h hx
      simp only [Set.mem_insert_iff,Set.mem_singleton_iff] at hh ⊢
      exact hh.resolve_right (fun he => hq (he ▸ hx))
    · intro hx; have hx' : x=p := hx; rw [hx']; exact hp
  · apply Or.inr; apply Or.inl
    refine ⟨q,?_⟩
    ext x
    constructor
    · intro hx
      have hh := h hx
      simp only [Set.mem_insert_iff,Set.mem_singleton_iff] at hh ⊢
      exact hh.resolve_left (fun he => hp (he ▸ hx))
    · intro hx; have hx' : x=q := hx; rw [hx']; exact hq
  · apply Or.inl
    apply Set.eq_empty_iff_forall_notMem.mpr
    intro x hx
    have hh := h hx
    simp only [Set.mem_insert_iff,Set.mem_singleton_iff] at hh
    rcases hh with he|he
    · exact hp (he ▸ hx)
    · exact hq (he ▸ hx)

theorem three_distinct_fixed_force_identity (g : PGL2 K) (p q r : Point K)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (hp : p ∈ fixedSet g) (hq : q ∈ fixedSet g) (hr : r ∈ fixedSet g) : g=1 := by
  by_contra hg
  obtain ⟨a,b,h⟩ := nonidentity_fixed_subset_pair g hg
  have hpa := h hp
  have hqa := h hq
  have hra := h hr
  simp only [Set.mem_insert_iff,Set.mem_singleton_iff] at hpa hqa hra
  rcases hpa with rfl|rfl <;> rcases hqa with hq'|hq' <;> rcases hra with hr'|hr'
  all_goals simp_all

theorem fixed_ncard_conjugate (s g : PGL2 K) : (fixedSet (s*g*s⁻¹)).ncard=(fixedSet g).ncard := by
  rw [fixedSet_conjugate]
  exact Set.ncard_image_of_injective _ (ProjectiveGeneralLinear.quotientAction s).injective

theorem rational_zero_fixed_example : (fixedSet (inversionClass : PGL2 ℚ))=∅ := by
  apply Set.eq_empty_iff_forall_notMem.mpr
  exact inversion_no_rational_fixed_point

theorem rational_one_fixed_example : (fixedSet (translationClass (1:ℚ))).ncard=1 := by
  have he : fixedSet (translationClass (1:ℚ))={none} := by
    ext p; exact translation_fixed_iff 1 (by norm_num) p
  rw [he]; simp

theorem rational_two_fixed_example :
    (fixedSet (dilationClass (Units.mk0 (2:ℚ) (by norm_num)))).ncard=2 := by
  have he : fixedSet (dilationClass (Units.mk0 (2:ℚ) (by norm_num)))={none,some 0} := by
    ext p; exact dilation_fixed_iff _ (by norm_num) p
  rw [he]
  exact Set.ncard_pair (by simp)

theorem nonidentity_fixed_cardinality (g : PGL2 K) (hg : g ≠ 1) :
    (fixedSet g).Finite ∧ (fixedSet g).ncard ≤ 2 :=
  ⟨nonidentity_fixed_finite g hg,nonidentity_fixed_ncard_le_two g hg⟩

theorem identity_has_three_distinct_fixed : ∃ p q r : Point K,
    p ≠ q ∧ p ≠ r ∧ q ≠ r ∧ p ∈ fixedSet 1 ∧ q ∈ fixedSet 1 ∧ r ∈ fixedSet 1 := by
  refine ⟨none,some 0,some 1,by simp,by simp,by simp,?_,?_,?_⟩
  all_goals simp [fixedSet]

theorem rational_all_cardinalities_realized (n : ℕ) (hn : n ≤ 2) :
    ∃ g : PGL2 ℚ, g ≠ 1 ∧ (fixedSet g).Finite ∧ (fixedSet g).ncard=n := by
  have hc : n=0 ∨ n=1 ∨ n=2 := by omega
  rcases hc with rfl|rfl|rfl
  · have hne : (inversionClass : PGL2 ℚ) ≠ 1 := by
      intro h
      have he := congrArg (fun g : PGL2 ℚ => ProjectiveGeneralLinear.quotientAction g none) h
      dsimp only at he
      rw [inversionClass_infinity,quotient_action_one] at he
      exact Option.some_ne_none _ he
    refine ⟨inversionClass,hne,nonidentity_fixed_finite _ hne,?_⟩
    rw [rational_zero_fixed_example]; simp
  · have hne : translationClass (1:ℚ) ≠ 1 := by
      intro h
      have he := congrArg (fun g : PGL2 ℚ => ProjectiveGeneralLinear.quotientAction g (some 0)) h
      dsimp only at he
      norm_num [translationClass_finite,quotient_action_one] at he
    exact ⟨_,hne,nonidentity_fixed_finite _ hne,rational_one_fixed_example⟩
  · let u : ℚˣ := Units.mk0 2 (by norm_num)
    have hne : dilationClass u ≠ 1 := by
      intro h
      have he := congrArg (fun g : PGL2 ℚ => ProjectiveGeneralLinear.quotientAction g (some 1)) h
      dsimp only at he
      norm_num [dilationClass_finite,quotient_action_one,u] at he
    exact ⟨_,hne,nonidentity_fixed_finite _ hne,rational_two_fixed_example⟩

end
end AEGPaper0.ProjectiveCardinality

#print axioms AEGPaper0.ProjectiveCardinality.conjugate_identity_iff
#print axioms AEGPaper0.ProjectiveCardinality.affine_nonidentity_fixed_subset
#print axioms AEGPaper0.ProjectiveCardinality.nonidentity_fixed_subset_pair
#print axioms AEGPaper0.ProjectiveCardinality.nonidentity_fixed_finite
#print axioms AEGPaper0.ProjectiveCardinality.nonidentity_fixed_ncard_le_two
#print axioms AEGPaper0.ProjectiveCardinality.nonidentity_fixed_cardinality_cases
#print axioms AEGPaper0.ProjectiveCardinality.nonidentity_fixed_set_cases
#print axioms AEGPaper0.ProjectiveCardinality.three_distinct_fixed_force_identity
#print axioms AEGPaper0.ProjectiveCardinality.fixed_ncard_conjugate
#print axioms AEGPaper0.ProjectiveCardinality.rational_zero_fixed_example
#print axioms AEGPaper0.ProjectiveCardinality.rational_one_fixed_example
#print axioms AEGPaper0.ProjectiveCardinality.rational_two_fixed_example
#print axioms AEGPaper0.ProjectiveCardinality.nonidentity_fixed_cardinality
#print axioms AEGPaper0.ProjectiveCardinality.identity_has_three_distinct_fixed
#print axioms AEGPaper0.ProjectiveCardinality.rational_all_cardinalities_realized
