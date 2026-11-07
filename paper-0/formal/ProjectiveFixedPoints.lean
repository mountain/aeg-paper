import ProjectiveBruhat

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   Eigenlines are actual invariant one-dimensional spans of nonzero vectors.
   Eigenvalues belong to matrix representatives; projective fixed points do
   not imply attraction or existence of a rational eigenline. -/
namespace AEGPaper0.ProjectiveFixedPoints

noncomputable section
open ProjectiveLine ProjectiveGeneralLinear Chapter04ProjectiveBridge
open ProjectiveGeneration ProjectiveBruhat
variable {K : Type*} [Field K]

def linearMap (m : Matrix2 K) : Vec K →ₗ[K] Vec K where
  toFun := mapVec m
  map_add' := by intro v w; apply Prod.ext <;> dsimp [mapVec] <;> ring
  map_smul' := by intro s v; apply Prod.ext <;> dsimp [mapVec] <;> ring

theorem linearMap_apply (m : Matrix2 K) (v : Vec K) : linearMap m v=mapVec m v := rfl

theorem scaleVec_eq_smul (s : K) (v : Vec K) : scaleVec s v=s • v := rfl

def invariantSpan (m : Matrix2 K) (v : Vec K) : Prop :=
  ∀ w ∈ Submodule.span K {v}, linearMap m w ∈ Submodule.span K {v}

theorem invariantSpan_iff_eigenvector (m : Matrix2 K) (v : Vec K) :
    invariantSpan m v ↔ ∃ s : K, mapVec m v=scaleVec s v := by
  constructor
  · intro h
    obtain ⟨s,hs⟩ := Submodule.mem_span_singleton.mp (h v (Submodule.mem_span_singleton_self v))
    exact ⟨s,hs.symm⟩
  · rintro ⟨s,hs⟩ w hw
    obtain ⟨t,rfl⟩ := Submodule.mem_span_singleton.mp hw
    rw [map_smul]
    exact Submodule.smul_mem _ t (Submodule.mem_span_singleton.mpr ⟨s,hs.symm⟩)

theorem eigenvalue_nonzero (m : Matrix2 K) (hm : determinant m ≠ 0) (v : Vec K)
    (hv : v ≠ (0,0)) (s : K) (he : mapVec m v=scaleVec s v) : s ≠ 0 := by
  intro hs
  subst s
  exact mapVec_nonzero m v hm hv (by simpa [scaleVec] using he)

theorem eigenvalue_unique (m : Matrix2 K) (v : Vec K) (hv : v ≠ (0,0))
    (s t : K) (hs : mapVec m v=scaleVec s v) (ht : mapVec m v=scaleVec t v) : s=t := by
  have he := hs.symm.trans ht
  have hx : s*v.1=t*v.1 := congrArg Prod.fst he
  have hy : s*v.2=t*v.2 := congrArg Prod.snd he
  by_cases h : v.1=0
  · have hn : v.2 ≠ 0 := by intro hh; exact hv (Prod.ext h hh)
    exact mul_right_cancel₀ hn hy
  · exact mul_right_cancel₀ h hx

theorem matrix_fixed_iff_eigenvector (m : Matrix2 K) (hm : determinant m ≠ 0)
    (v : Vec K) (hv : v ≠ (0,0)) :
    act m (project v)=project v ↔ ∃ s : K, s ≠ 0 ∧ mapVec m v=scaleVec s v := by
  change project (mapVec m (homogeneous (project v)))=project v ↔ _
  rw [project_map_normalize m v hv]
  exact projection_eq_iff_scalar _ v (mapVec_nonzero m v hm hv) hv

theorem matrix_fixed_iff_invariantSpan (m : Matrix2 K) (hm : determinant m ≠ 0)
    (v : Vec K) (hv : v ≠ (0,0)) : act m (project v)=project v ↔ invariantSpan m v := by
  rw [matrix_fixed_iff_eigenvector m hm v hv,invariantSpan_iff_eigenvector]
  constructor
  · rintro ⟨s,_,hs⟩; exact ⟨s,hs⟩
  · rintro ⟨s,hs⟩; exact ⟨s,eigenvalue_nonzero m hm v hv s hs,hs⟩

theorem point_fixed_iff_homogeneous_eigenvector (m : Matrix2 K) (hm : determinant m ≠ 0) (p : Point K) :
    act m p=p ↔ ∃ s : K, s ≠ 0 ∧ mapVec m (homogeneous p)=scaleVec s (homogeneous p) := by
  simpa only [project_homogeneous] using matrix_fixed_iff_eigenvector m hm _ (homogeneous_nonzero p)

theorem quotient_fixed_iff_eigenline (m : Matrix2 K) (hm : determinant m ≠ 0)
    (v : Vec K) (hv : v ≠ (0,0)) :
    ProjectiveGeneralLinear.quotientAction (ofMatrix m hm) (project v)=project v ↔ invariantSpan m v := by
  rw [ofMatrix_action]
  exact matrix_fixed_iff_invariantSpan m hm v hv

theorem homogeneous_quotient_fixed_iff (m : Matrix2 K) (hm : determinant m ≠ 0)
    (v : Vec K) (hv : v ≠ (0,0)) :
    ProjectiveLine.quotientAction m hm (Quotient.mk _ ⟨v,hv⟩)=Quotient.mk _ ⟨v,hv⟩ ↔
      ∃ s : K, s ≠ 0 ∧ mapVec m v=scaleVec s v := by
  rw [ProjectiveLine.quotient_action_representative]
  exact quotient_eq_iff_nonzero_scalar _ v (mapVec_nonzero m v hm hv) hv

theorem finite_fixed_eigenvector (m : Matrix2 K) (x : K)
    (hx : m.c*x^2+(m.d-m.a)*x-m.b=0) :
    mapVec m (x,1)=scaleVec (m.c*x+m.d) (x,1) := by
  apply Prod.ext
  · dsimp [mapVec,scaleVec]; linear_combination -hx
  · simp [mapVec,scaleVec]

theorem finite_fixed_eigenvalue_nonzero (m : Matrix2 K) (hm : determinant m ≠ 0) (x : K)
    (hx : m.c*x^2+(m.d-m.a)*x-m.b=0) : m.c*x+m.d ≠ 0 :=
  eigenvalue_nonzero m hm (x,1) (by simp) _ (finite_fixed_eigenvector m x hx)

theorem quotient_finite_fixed_iff (m : Matrix2 K) (hm : determinant m ≠ 0) (x : K) :
    ProjectiveGeneralLinear.quotientAction (ofMatrix m hm) (some x)=some x ↔
      m.c*x^2+(m.d-m.a)*x-m.b=0 := by
  rw [ofMatrix_action]
  exact finite_fixed_point_iff m hm x

theorem quotient_infinity_fixed_iff (m : Matrix2 K) (hm : determinant m ≠ 0) :
    ProjectiveGeneralLinear.quotientAction (ofMatrix m hm) none=none ↔ m.c=0 := by
  rw [ofMatrix_action,fixes_infinity_iff]

theorem mapVec_scaleMatrix (s : K) (m : Matrix2 K) (v : Vec K) :
    mapVec (scaleMatrix s m) v=scaleVec s (mapVec m v) := by
  apply Prod.ext <;> dsimp [mapVec,scaleMatrix,scaleVec] <;> ring

theorem vector_rescaling_preserves_eigenvector (s t : K) (m : Matrix2 K) (v : Vec K)
    (hs : s ≠ 0) : mapVec m (scaleVec s v)=scaleVec t (scaleVec s v) ↔ mapVec m v=scaleVec t v := by
  rw [mapVec_scale]
  constructor <;> intro h
  · apply Prod.ext
    · have he := congrArg Prod.fst h
      dsimp [scaleVec] at he ⊢
      apply mul_left_cancel₀ hs
      linear_combination he
    · have he := congrArg Prod.snd h
      dsimp [scaleVec] at he ⊢
      apply mul_left_cancel₀ hs
      linear_combination he
  · rw [h]
    apply Prod.ext <;> dsimp [scaleVec] <;> ring

theorem matrix_rescaling_rescales_eigenvalue (s t : K) (m : Matrix2 K) (v : Vec K)
    (h : mapVec m v=scaleVec t v) :
    mapVec (scaleMatrix s m) v=scaleVec (s*t) v := by
  rw [mapVec_scaleMatrix,h]
  apply Prod.ext <;> dsimp [scaleVec] <;> ring

theorem matrix_rescaling_preserves_eigenline (s : K) (hs : s ≠ 0) (m : Matrix2 K)
    (hm : determinant m ≠ 0) (v : Vec K) (hv : v ≠ (0,0)) :
    invariantSpan (scaleMatrix s m) v ↔ invariantSpan m v := by
  have hsm : determinant (scaleMatrix s m) ≠ 0 := by
    rw [ProjectiveFaithfulness.determinant_scale]
    exact mul_ne_zero (pow_ne_zero 2 hs) hm
  rw [← matrix_fixed_iff_invariantSpan _ hsm v hv,← matrix_fixed_iff_invariantSpan m hm v hv,action_scale s m _ hs]

def fixedSet (g : PGL2 K) : Set (Point K) := {p | ProjectiveGeneralLinear.quotientAction g p=p}

def fixedPointConjugacy (g h : PGL2 K) : {p // p ∈ fixedSet h} ≃ {p // p ∈ fixedSet (g*h*g⁻¹)} where
  toFun p := ⟨ProjectiveGeneralLinear.quotientAction g p.val,
    (conjugation_stabilizer_iff g h p.val).mpr p.property⟩
  invFun p := ⟨ProjectiveGeneralLinear.quotientAction g⁻¹ p.val,by
    apply (conjugation_stabilizer_iff g h _).mp
    rw [action_inverse_cancel]
    exact p.property⟩
  left_inv p := Subtype.ext (quotient_action_inverse g p.val)
  right_inv p := Subtype.ext (action_inverse_cancel g p.val)

theorem fixedPointConjugacy_apply (g h : PGL2 K) (p : {p // p ∈ fixedSet h}) :
    (fixedPointConjugacy g h p).val=ProjectiveGeneralLinear.quotientAction g p.val := rfl

theorem fixedSet_conjugate (g h : PGL2 K) :
    fixedSet (g*h*g⁻¹)=ProjectiveGeneralLinear.quotientAction g '' fixedSet h := by
  ext p
  constructor
  · intro hp
    let q := (fixedPointConjugacy g h).symm ⟨p,hp⟩
    exact ⟨q.val,q.property,congrArg Subtype.val ((fixedPointConjugacy g h).apply_symm_apply ⟨p,hp⟩)⟩
  · rintro ⟨q,hq,rfl⟩
    exact (fixedPointConjugacy g h ⟨q,hq⟩).property

theorem exists_fixed_conjugate_iff (g h : PGL2 K) :
    (∃ p, p ∈ fixedSet (g*h*g⁻¹)) ↔ ∃ p, p ∈ fixedSet h := by
  rw [fixedSet_conjugate]
  constructor
  · rintro ⟨_,q,hq,_⟩; exact ⟨q,hq⟩
  · rintro ⟨q,hq⟩; exact ⟨_,q,hq,rfl⟩

theorem conjugation_transports_eigenline (n m : Matrix2 K) (hn : determinant n ≠ 0)
    (hm : determinant m ≠ 0) (v : Vec K) (hv : v ≠ (0,0)) (he : invariantSpan m v) :
    project (mapVec n v) ∈ fixedSet (ofMatrix n hn*ofMatrix m hm*(ofMatrix n hn)⁻¹) := by
  have hp := (quotient_fixed_iff_eigenline m hm v hv).mpr he
  have hh := (fixedPointConjugacy (ofMatrix n hn) (ofMatrix m hm) ⟨project v,hp⟩).property
  simpa only [fixedPointConjugacy_apply,ofMatrix_action,act,project_map_normalize n v hv] using hh

theorem invariantSpan_depends_only_on_line (m : Matrix2 K) (hm : determinant m ≠ 0)
    (v w : Vec K) (hv : v ≠ (0,0)) (hw : w ≠ (0,0)) (h : project v=project w) :
    invariantSpan m v ↔ invariantSpan m w := by
  rw [← matrix_fixed_iff_invariantSpan m hm v hv,← matrix_fixed_iff_invariantSpan m hm w hw,h]

theorem homogeneous_quotient_fixed_iff_invariantSpan (m : Matrix2 K) (hm : determinant m ≠ 0)
    (v : Vec K) (hv : v ≠ (0,0)) :
    ProjectiveLine.quotientAction m hm (Quotient.mk _ ⟨v,hv⟩)=Quotient.mk _ ⟨v,hv⟩ ↔ invariantSpan m v := by
  rw [homogeneous_quotient_fixed_iff m hm v hv,← matrix_fixed_iff_eigenvector m hm v hv,
    matrix_fixed_iff_invariantSpan m hm v hv]

abbrev Lines (K : Type*) [Field K] := Quotient (lineSetoid (K := K))

def lineAction : PGL2 K →* Equiv.Perm (Lines K) where
  toFun g := (chartEquiv.trans (ProjectiveGeneralLinear.quotientAction g)).trans chartEquiv.symm
  map_one' := by
    apply Equiv.ext
    intro l
    change chartEquiv.symm (ProjectiveGeneralLinear.quotientAction 1 (chartEquiv l))=l
    rw [quotient_action_one,Equiv.symm_apply_apply]
  map_mul' g h := by
    apply Equiv.ext
    intro l
    change chartEquiv.symm (ProjectiveGeneralLinear.quotientAction (g*h) (chartEquiv l))=
      chartEquiv.symm (ProjectiveGeneralLinear.quotientAction g
        (chartEquiv (chartEquiv.symm (ProjectiveGeneralLinear.quotientAction h (chartEquiv l)))))
    rw [quotient_action_mul,Equiv.apply_symm_apply]

theorem lineAction_representative (m : Matrix2 K) (hm : determinant m ≠ 0) :
    lineAction (ofMatrix m hm)=ProjectiveLine.quotientAction m hm := by
  apply Equiv.ext
  intro l
  change chartEquiv.symm (ProjectiveGeneralLinear.quotientAction (ofMatrix m hm) (chartEquiv l))=
    chartEquiv.symm (act m (chartEquiv l))
  rw [ofMatrix_action]

theorem lineAction_chart (g : PGL2 K) (l : Lines K) :
    chartEquiv (lineAction g l)=ProjectiveGeneralLinear.quotientAction g (chartEquiv l) :=
  chartEquiv.apply_symm_apply _

theorem lineAction_vector (m : Matrix2 K) (hm : determinant m ≠ 0) (v : Vec K) (hv : v ≠ (0,0)) :
    lineAction (ofMatrix m hm) (Quotient.mk _ ⟨v,hv⟩)=Quotient.mk _ ⟨mapVec m v,mapVec_nonzero m v hm hv⟩ := by
  rw [lineAction_representative,ProjectiveLine.quotient_action_representative]

def eigenlineFixedEquiv (g : PGL2 K) :
    {l : Lines K // lineAction g l=l} ≃ {p : Point K // p ∈ fixedSet g} where
  toFun l := ⟨chartEquiv l.val,by
    have h := congrArg (chartEquiv (K := K)) l.property
    rw [lineAction_chart] at h
    exact h⟩
  invFun p := ⟨chartEquiv.symm p.val,by
    apply chartEquiv.injective
    rw [lineAction_chart,Equiv.apply_symm_apply]
    exact p.property⟩
  left_inv l := Subtype.ext (chartEquiv.symm_apply_apply l.val)
  right_inv p := Subtype.ext (chartEquiv.apply_symm_apply p.val)

theorem eigenlineFixedEquiv_apply (g : PGL2 K) (l : {l : Lines K // lineAction g l=l}) :
    (eigenlineFixedEquiv g l).val=chartEquiv l.val := rfl

theorem fixedSet_one : fixedSet (1 : PGL2 K)=Set.univ := by
  ext p
  simp [fixedSet]

theorem translation_fixed_iff (s : K) (hs : s ≠ 0) (p : Point K) :
    p ∈ fixedSet (translationClass s) ↔ p=none := by
  cases p with
  | none => simp [fixedSet,translationClass_infinity]
  | some x =>
    simp only [fixedSet,Set.mem_setOf_eq,translationClass_finite,Option.some.injEq,reduceCtorEq,iff_false]
    intro h
    apply hs
    linear_combination h

theorem dilation_fixed_iff (u : Kˣ) (hu : (u:K) ≠ 1) (p : Point K) :
    p ∈ fixedSet (dilationClass u) ↔ p=none ∨ p=some 0 := by
  cases p with
  | none => simp [fixedSet,dilationClass_infinity]
  | some x =>
    simp only [fixedSet,Set.mem_setOf_eq,dilationClass_finite,Option.some.injEq,reduceCtorEq,false_or]
    constructor
    · intro h
      have hf : ((u:K)-1)*x=0 := by linear_combination h
      exact (mul_eq_zero.mp hf).resolve_left (sub_ne_zero.mpr hu)
    · intro h; rw [h]; simp

theorem inversion_no_rational_fixed_point (p : Point ℚ) : p ∉ fixedSet (inversionClass : PGL2 ℚ) := by
  cases p with
  | none => simp [fixedSet,inversionClass_infinity]
  | some x =>
    intro h
    have hx : act (inversion : Matrix2 ℚ) (some x)=some x := h
    have hp := (finite_fixed_point_iff inversion (by norm_num [determinant,inversion]) x).mp hx
    dsimp [inversion] at hp
    nlinarith [sq_nonneg x]

theorem representative_eigenvalues_are_not_intrinsic :
    ofMatrix (scaleMatrix (2:ℚ) identity) (by norm_num [determinant,scaleMatrix,identity])=
      ofMatrix identity (by norm_num [determinant,identity]) ∧
    mapVec (scaleMatrix (2:ℚ) identity) (1,0)=scaleVec 2 (1,0) ∧
    mapVec (identity : Matrix2 ℚ) (1,0)=scaleVec 1 (1,0) ∧ (2:ℚ) ≠ 1 := by
  constructor
  · apply (ofMatrix_equal_iff_scalar _ _ _ _).mpr
    exact ⟨2,by norm_num,rfl⟩
  · norm_num [mapVec,scaleMatrix,identity,scaleVec]

end
end AEGPaper0.ProjectiveFixedPoints

#print axioms AEGPaper0.ProjectiveFixedPoints.linearMap_apply
#print axioms AEGPaper0.ProjectiveFixedPoints.scaleVec_eq_smul
#print axioms AEGPaper0.ProjectiveFixedPoints.invariantSpan_iff_eigenvector
#print axioms AEGPaper0.ProjectiveFixedPoints.eigenvalue_nonzero
#print axioms AEGPaper0.ProjectiveFixedPoints.eigenvalue_unique
#print axioms AEGPaper0.ProjectiveFixedPoints.matrix_fixed_iff_eigenvector
#print axioms AEGPaper0.ProjectiveFixedPoints.matrix_fixed_iff_invariantSpan
#print axioms AEGPaper0.ProjectiveFixedPoints.point_fixed_iff_homogeneous_eigenvector
#print axioms AEGPaper0.ProjectiveFixedPoints.quotient_fixed_iff_eigenline
#print axioms AEGPaper0.ProjectiveFixedPoints.homogeneous_quotient_fixed_iff
#print axioms AEGPaper0.ProjectiveFixedPoints.finite_fixed_eigenvector
#print axioms AEGPaper0.ProjectiveFixedPoints.finite_fixed_eigenvalue_nonzero
#print axioms AEGPaper0.ProjectiveFixedPoints.quotient_finite_fixed_iff
#print axioms AEGPaper0.ProjectiveFixedPoints.quotient_infinity_fixed_iff
#print axioms AEGPaper0.ProjectiveFixedPoints.mapVec_scaleMatrix
#print axioms AEGPaper0.ProjectiveFixedPoints.vector_rescaling_preserves_eigenvector
#print axioms AEGPaper0.ProjectiveFixedPoints.matrix_rescaling_rescales_eigenvalue
#print axioms AEGPaper0.ProjectiveFixedPoints.matrix_rescaling_preserves_eigenline
#print axioms AEGPaper0.ProjectiveFixedPoints.fixedPointConjugacy_apply
#print axioms AEGPaper0.ProjectiveFixedPoints.fixedSet_conjugate
#print axioms AEGPaper0.ProjectiveFixedPoints.exists_fixed_conjugate_iff
#print axioms AEGPaper0.ProjectiveFixedPoints.conjugation_transports_eigenline
#print axioms AEGPaper0.ProjectiveFixedPoints.invariantSpan_depends_only_on_line
#print axioms AEGPaper0.ProjectiveFixedPoints.homogeneous_quotient_fixed_iff_invariantSpan
#print axioms AEGPaper0.ProjectiveFixedPoints.lineAction_representative
#print axioms AEGPaper0.ProjectiveFixedPoints.lineAction_chart
#print axioms AEGPaper0.ProjectiveFixedPoints.lineAction_vector
#print axioms AEGPaper0.ProjectiveFixedPoints.eigenlineFixedEquiv_apply
#print axioms AEGPaper0.ProjectiveFixedPoints.fixedSet_one
#print axioms AEGPaper0.ProjectiveFixedPoints.translation_fixed_iff
#print axioms AEGPaper0.ProjectiveFixedPoints.dilation_fixed_iff
#print axioms AEGPaper0.ProjectiveFixedPoints.inversion_no_rational_fixed_point
#print axioms AEGPaper0.ProjectiveFixedPoints.representative_eigenvalues_are_not_intrinsic
