import AffineStabilizer

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   Point stabilizers, fixed-pole fibers and Bruhat double cosets are distinct.
   Everything is in the actual PGL quotient over an arbitrary field. -/
namespace AEGPaper0.ProjectiveBruhat

noncomputable section
open ProjectiveLine ProjectiveGeneralLinear Chapter04ProjectiveBridge
open ProjectiveGeneration AffineStabilizer
variable {K : Type*} [Field K]

theorem action_inverse_cancel (g : PGL2 K) (x : Point K) :
    quotientAction g (quotientAction g⁻¹ x)=x := by
  simpa only [inv_inv] using quotient_action_inverse g⁻¹ x

def pointStabilizer (p : Point K) : Subgroup (PGL2 K) where
  carrier := {g | quotientAction g p=p}
  one_mem' := quotient_action_one p
  mul_mem' := by
    intro g h hg hh
    change quotientAction (g*h) p=p
    rw [quotient_action_mul,hh,hg]
  inv_mem' := by
    intro g hg
    change quotientAction g p=p at hg
    change quotientAction g⁻¹ p=p
    have he := congrArg (fun x => quotientAction g⁻¹ x) hg
    dsimp only at he
    rw [quotient_action_inverse] at he
    exact he.symm

theorem pointStabilizer_none : pointStabilizer (none : Point K)=infinityStabilizer := rfl

theorem conjugation_stabilizer_iff (g h : PGL2 K) (p : Point K) :
    g*h*g⁻¹ ∈ pointStabilizer (quotientAction g p) ↔ h ∈ pointStabilizer p := by
  change quotientAction (g*h*g⁻¹) (quotientAction g p)=quotientAction g p ↔ quotientAction h p=p
  rw [quotient_action_mul,quotient_action_mul,quotient_action_inverse]
  exact (quotientAction g).injective.eq_iff

def stabilizerConjugacy (g : PGL2 K) (p : Point K) :
    pointStabilizer p ≃* pointStabilizer (quotientAction g p) where
  toFun h := ⟨g*h.val*g⁻¹,(conjugation_stabilizer_iff g h.val p).mpr h.property⟩
  invFun h := ⟨g⁻¹*h.val*g,by
    apply (conjugation_stabilizer_iff g _ p).mp
    have he : g*(g⁻¹*h.val*g)*g⁻¹=h.val := by group
    rw [he]; exact h.property⟩
  left_inv h := Subtype.ext (by dsimp; group)
  right_inv h := Subtype.ext (by dsimp; group)
  map_mul' h k := Subtype.ext (by dsimp; group)

theorem stabilizerConjugacy_apply (g : PGL2 K) (p : Point K) (h : pointStabilizer p) :
    (stabilizerConjugacy g p h).val=g*h.val*g⁻¹ := rfl

def poleGauge (q : K) : PGL2 K := inversionClass * translationClass (-q)

theorem poleGauge_at_pole (q : K) : quotientAction (poleGauge q) (some q)=none := by
  rw [poleGauge,quotient_action_mul,translationClass_finite]
  simp only [add_neg_cancel,inversionClass_zero]

theorem poleGauge_at_infinity (q : K) : quotientAction (poleGauge q) none=some 0 := by
  rw [poleGauge,quotient_action_mul,translationClass_infinity,inversionClass_infinity]

theorem poleGauge_finite (q z : K) (hz : z ≠ q) :
    quotientAction (poleGauge q) (some z)=some (-1/(z-q)) := by
  rw [poleGauge,quotient_action_mul,translationClass_finite]
  simpa only [sub_eq_add_neg] using inversionClass_finite (z-q) (sub_ne_zero.mpr hz)

theorem poleGauge_inverse_infinity (q : K) : quotientAction (poleGauge q)⁻¹ none=some q := by
  have h := quotient_action_inverse (poleGauge q) (some q)
  rw [poleGauge_at_pole] at h
  exact h

theorem poleGauge_inverse_zero (q : K) : quotientAction (poleGauge q)⁻¹ (some 0)=none := by
  have h := quotient_action_inverse (poleGauge q) none
  rw [poleGauge_at_infinity] at h
  exact h

theorem finite_stabilizer_iff (q : K) (g : PGL2 K) :
    g ∈ pointStabilizer (some q) ↔ poleGauge q*g*(poleGauge q)⁻¹ ∈ infinityStabilizer := by
  have h := conjugation_stabilizer_iff (poleGauge q) g (some q)
  rw [poleGauge_at_pole,pointStabilizer_none] at h
  exact h.symm

def finiteStabilizerEquiv (q : K) : pointStabilizer (some q) ≃* (infinityStabilizer (K := K)) where
  toFun g := ⟨poleGauge q*g.val*(poleGauge q)⁻¹,(finite_stabilizer_iff q g.val).mp g.property⟩
  invFun b := ⟨(poleGauge q)⁻¹*b.val*poleGauge q,by
    apply (finite_stabilizer_iff q _).mpr
    have he : poleGauge q*((poleGauge q)⁻¹*b.val*poleGauge q)*(poleGauge q)⁻¹=b.val := by group
    rw [he]; exact b.property⟩
  left_inv g := Subtype.ext (by dsimp; group)
  right_inv b := Subtype.ext (by dsimp; group)
  map_mul' g h := Subtype.ext (by dsimp; group)

def finiteAffineEquiv (q : K) : Aff K ≃* pointStabilizer (some q) :=
  affineStabilizerEquiv.trans (finiteStabilizerEquiv q).symm

theorem finiteAffineEquiv_class (q : K) (e : Aff K) :
    (finiteAffineEquiv q e).val=(poleGauge q)⁻¹*affineClass e*poleGauge q := rfl

theorem finiteAffineEquiv_fixes_point (q : K) (e : Aff K) :
    quotientAction (finiteAffineEquiv q e).val (some q)=some q := (finiteAffineEquiv q e).property

def quotientPole (g : PGL2 K) : Point K := quotientAction g⁻¹ none

theorem quotientPole_unique_preimage (g : PGL2 K) (p : Point K) :
    quotientAction g p=none ↔ p=quotientPole g := by
  constructor
  · intro h
    have he := congrArg (fun x => quotientAction g⁻¹ x) h
    dsimp only at he
    rw [quotient_action_inverse] at he
    exact he
  · intro h
    rw [h,quotientPole,action_inverse_cancel]

theorem quotientPole_infinity_iff (g : PGL2 K) :
    quotientPole g=none ↔ g ∈ infinityStabilizer := by
  change quotientPole g=none ↔ quotientAction g none=none
  exact ((quotientPole_unique_preimage g none).trans eq_comm).symm

theorem quotientPole_product (g h : PGL2 K) :
    quotientPole (g*h)=quotientAction h⁻¹ (quotientPole g) := by
  simp only [quotientPole,mul_inv_rev,quotient_action_mul]

theorem quotientPole_ofMatrix (m : Matrix2 K) (hm : determinant m ≠ 0) :
    quotientPole (ofMatrix m hm)=matrixPole m hm := by
  apply Eq.symm
  apply (quotientPole_unique_preimage (ofMatrix m hm) (matrixPole m hm)).mp
  rw [ofMatrix_action]
  exact (actionEquiv m hm).apply_symm_apply none

theorem quotientPole_finite_formula (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    quotientPole (ofMatrix m hm)=some (-m.d/m.c) := by
  rw [quotientPole_ofMatrix,concrete_finite_pole m hm hc]

theorem poleGauge_pole (q : K) : quotientPole (poleGauge q)=some q := poleGauge_inverse_infinity q

theorem finite_pole_fiber (q : K) (g : PGL2 K) :
    quotientPole g=some q ↔ ∃ b : PGL2 K, b ∈ infinityStabilizer ∧ g=b*poleGauge q := by
  constructor
  · intro hp
    refine ⟨g*(poleGauge q)⁻¹,?_,by group⟩
    change quotientAction (g*(poleGauge q)⁻¹) none=none
    rw [quotient_action_mul,poleGauge_inverse_infinity]
    exact (quotientPole_unique_preimage g (some q)).mpr hp.symm
  · rintro ⟨b,hb,rfl⟩
    apply ((quotientPole_unique_preimage (b*poleGauge q) (some q)).mp ?_).symm
    rw [quotient_action_mul,poleGauge_at_pole]
    exact hb

theorem finite_stabilizer_excludes_own_pole (q : K) (g : PGL2 K)
    (hg : g ∈ pointStabilizer (some q)) : quotientPole g ≠ some q := by
  intro hp
  have he := (quotientPole_unique_preimage g (some q)).mpr hp.symm
  change quotientAction g (some q)=some q at hg
  rw [hg] at he
  exact Option.some_ne_none _ he

theorem poleGauge_not_point_stabilizer (q : K) : poleGauge q ∉ pointStabilizer (some q) := by
  intro h
  change quotientAction (poleGauge q) (some q)=some q at h
  rw [poleGauge_at_pole] at h
  exact Option.noConfusion h

theorem translation_in_stabilizer (s : K) : translationClass s ∈ infinityStabilizer :=
  translationClass_infinity s

theorem dilation_in_stabilizer (u : Kˣ) : dilationClass u ∈ infinityStabilizer :=
  dilationClass_infinity u

def bigCell : Set (PGL2 K) :=
  {g | ∃ b : PGL2 K, b ∈ infinityStabilizer ∧
    ∃ c : PGL2 K, c ∈ infinityStabilizer ∧ g=b*inversionClass*c}

theorem bigCell_excludes_stabilizer (g : PGL2 K) (hg : g ∈ bigCell) : g ∉ infinityStabilizer := by
  obtain ⟨b,hb,c,hc,rfl⟩ := hg
  intro h
  change quotientAction (b*inversionClass*c) none=none at h
  rw [quotient_action_mul,quotient_action_mul,hc,inversionClass_infinity] at h
  have he : quotientAction b (some 0)=quotientAction b none := h.trans hb.symm
  exact Option.some_ne_none _ ((quotientAction b).injective he)

theorem nonaffine_in_bigCell (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    ofMatrix m hm ∈ bigCell := by
  refine ⟨translationClass (m.a/m.c)*dilationClass (Units.mk0 (determinant m/m.c^2)
    (nonaffine_scale_nonzero m hm hc)),Subgroup.mul_mem _ (translation_in_stabilizer _) (dilation_in_stabilizer _),
    translationClass (m.d/m.c),translation_in_stabilizer _,?_⟩
  rw [quotient_nonaffine_factorization m hm hc]
  simp only [mul_assoc]

theorem bigCell_iff_not_stabilizer (g : PGL2 K) : g ∈ bigCell ↔ g ∉ infinityStabilizer := by
  constructor
  · exact bigCell_excludes_stabilizer g
  · intro h
    obtain ⟨m,hm,rfl⟩ := ofMatrix_surjective g
    have hc : m.c ≠ 0 := by
      intro hc
      exact h ((infinity_iff_lower_left_zero m hm).mpr hc)
    exact nonaffine_in_bigCell m hm hc

theorem bigCell_matrix_iff (m : Matrix2 K) (hm : determinant m ≠ 0) :
    ofMatrix m hm ∈ bigCell ↔ m.c ≠ 0 := by
  rw [bigCell_iff_not_stabilizer,infinity_iff_lower_left_zero]

theorem bruhat_cover : (↑(infinityStabilizer (K := K)) : Set (PGL2 K)) ∪ bigCell=Set.univ := by
  ext g
  simp only [Set.mem_union,SetLike.mem_coe,bigCell_iff_not_stabilizer,Set.mem_univ,iff_true]
  exact Classical.em _

theorem bruhat_disjoint : Disjoint (↑(infinityStabilizer (K := K)) : Set (PGL2 K)) bigCell := by
  apply Set.disjoint_left.mpr
  intro g hb hg
  exact bigCell_excludes_stabilizer g hg hb

theorem bruhat_factorization (g : PGL2 K) : g ∈ infinityStabilizer ∨
    ∃ b : PGL2 K, b ∈ infinityStabilizer ∧
      ∃ c : PGL2 K, c ∈ infinityStabilizer ∧ g=b*inversionClass*c := by
  by_cases hg : g ∈ infinityStabilizer
  · exact Or.inl hg
  · exact Or.inr ((bigCell_iff_not_stabilizer g).mpr hg)

theorem bigCell_iff_finite_pole (g : PGL2 K) :
    g ∈ bigCell ↔ ∃ q : K, quotientPole g=some q := by
  rw [bigCell_iff_not_stabilizer,← quotientPole_infinity_iff]
  cases hp : quotientPole g <;> simp

theorem inversion_in_bigCell : (inversionClass : PGL2 K) ∈ bigCell := by
  exact (bigCell_iff_not_stabilizer _).mpr inversion_not_in_affine_stabilizer

theorem identity_not_in_bigCell : (1 : PGL2 K) ∉ bigCell := by
  rw [bigCell_iff_not_stabilizer,not_not]
  exact Subgroup.one_mem _

theorem bigCell_iff_affine_gauge (g : PGL2 K) :
    g ∈ bigCell ↔ ∃ q : K, ∃ b : PGL2 K, b ∈ infinityStabilizer ∧ g=b*poleGauge q := by
  constructor
  · intro hg
    obtain ⟨q,hq⟩ := (bigCell_iff_finite_pole g).mp hg
    obtain ⟨b,hb,he⟩ := (finite_pole_fiber q g).mp hq
    exact ⟨q,b,hb,he⟩
  · rintro ⟨q,b,hb,he⟩
    exact (bigCell_iff_finite_pole g).mpr ⟨q,(finite_pole_fiber q g).mpr ⟨b,hb,he⟩⟩

theorem finite_pole_fiber_not_subgroup (q : K) :
    ¬ ∃ H : Subgroup (PGL2 K), ∀ g, g ∈ H ↔ quotientPole g=some q := by
  rintro ⟨H,hH⟩
  have hp := (hH 1).mp H.one_mem
  have hi : quotientPole (1 : PGL2 K)=none := (quotientPole_infinity_iff 1).mpr (Subgroup.one_mem _)
  rw [hi] at hp
  exact Option.noConfusion hp

end
end AEGPaper0.ProjectiveBruhat

#print axioms AEGPaper0.ProjectiveBruhat.action_inverse_cancel
#print axioms AEGPaper0.ProjectiveBruhat.pointStabilizer_none
#print axioms AEGPaper0.ProjectiveBruhat.conjugation_stabilizer_iff
#print axioms AEGPaper0.ProjectiveBruhat.stabilizerConjugacy_apply
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_at_pole
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_at_infinity
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_finite
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_inverse_infinity
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_inverse_zero
#print axioms AEGPaper0.ProjectiveBruhat.finite_stabilizer_iff
#print axioms AEGPaper0.ProjectiveBruhat.finiteAffineEquiv_class
#print axioms AEGPaper0.ProjectiveBruhat.finiteAffineEquiv_fixes_point
#print axioms AEGPaper0.ProjectiveBruhat.quotientPole_unique_preimage
#print axioms AEGPaper0.ProjectiveBruhat.quotientPole_infinity_iff
#print axioms AEGPaper0.ProjectiveBruhat.quotientPole_product
#print axioms AEGPaper0.ProjectiveBruhat.quotientPole_ofMatrix
#print axioms AEGPaper0.ProjectiveBruhat.quotientPole_finite_formula
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_pole
#print axioms AEGPaper0.ProjectiveBruhat.finite_pole_fiber
#print axioms AEGPaper0.ProjectiveBruhat.finite_stabilizer_excludes_own_pole
#print axioms AEGPaper0.ProjectiveBruhat.poleGauge_not_point_stabilizer
#print axioms AEGPaper0.ProjectiveBruhat.translation_in_stabilizer
#print axioms AEGPaper0.ProjectiveBruhat.dilation_in_stabilizer
#print axioms AEGPaper0.ProjectiveBruhat.bigCell_excludes_stabilizer
#print axioms AEGPaper0.ProjectiveBruhat.nonaffine_in_bigCell
#print axioms AEGPaper0.ProjectiveBruhat.bigCell_iff_not_stabilizer
#print axioms AEGPaper0.ProjectiveBruhat.bigCell_matrix_iff
#print axioms AEGPaper0.ProjectiveBruhat.bruhat_cover
#print axioms AEGPaper0.ProjectiveBruhat.bruhat_disjoint
#print axioms AEGPaper0.ProjectiveBruhat.bruhat_factorization
#print axioms AEGPaper0.ProjectiveBruhat.bigCell_iff_finite_pole
#print axioms AEGPaper0.ProjectiveBruhat.inversion_in_bigCell
#print axioms AEGPaper0.ProjectiveBruhat.identity_not_in_bigCell
#print axioms AEGPaper0.ProjectiveBruhat.bigCell_iff_affine_gauge
#print axioms AEGPaper0.ProjectiveBruhat.finite_pole_fiber_not_subgroup
