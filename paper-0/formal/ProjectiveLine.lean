import Mathlib.Tactic

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   A concrete projective line over an arbitrary field: none is infinity and
   some x is [x:1]. Matrix actions and inverses are derived from nonzero
   homogeneous vectors, not supplied as target axioms. Ordinary arithmetic
   division remains separate from this total projective continuation. -/
namespace AEGPaper0.ProjectiveLine

noncomputable section
variable {K : Type*} [Field K]
attribute [local instance] Classical.propDecidable

abbrev Point (K : Type*) := Option K
abbrev Vec (K : Type*) := K × K

def homogeneous : Point K → Vec K
  | none => (1, 0)
  | some x => (x, 1)
def project (v : Vec K) : Point K := if v.2 = 0 then none else some (v.1 / v.2)
def scaleVec (s : K) (v : Vec K) : Vec K := (s * v.1, s * v.2)

structure Matrix2 (K : Type*) where
  a : K
  b : K
  c : K
  d : K

def determinant (m : Matrix2 K) : K := m.a * m.d - m.b * m.c
def mapVec (m : Matrix2 K) (v : Vec K) : Vec K :=
  (m.a * v.1 + m.b * v.2, m.c * v.1 + m.d * v.2)
def identity : Matrix2 K := ⟨1, 0, 0, 1⟩
def multiply (m n : Matrix2 K) : Matrix2 K :=
  ⟨m.a*n.a+m.b*n.c, m.a*n.b+m.b*n.d, m.c*n.a+m.d*n.c, m.c*n.b+m.d*n.d⟩
def adjugate (m : Matrix2 K) : Matrix2 K := ⟨m.d, -m.b, -m.c, m.a⟩
def scaleMatrix (s : K) (m : Matrix2 K) : Matrix2 K := ⟨s*m.a, s*m.b, s*m.c, s*m.d⟩
def act (m : Matrix2 K) (x : Point K) : Point K := project (mapVec m (homogeneous x))

theorem homogeneous_nonzero (x : Point K) : homogeneous x ≠ (0, 0) := by
  cases x <;> simp [homogeneous]

theorem project_homogeneous (x : Point K) : project (homogeneous x) = x := by
  cases x <;> simp [project, homogeneous]

theorem project_scale (s : K) (v : Vec K) (hs : s ≠ 0) : project (scaleVec s v) = project v := by
  by_cases hv : v.2 = 0
  · simp [project, scaleVec, hv]
  · simp [project, scaleVec, hs, hv]
    field_simp

theorem representative_scale (v : Vec K) (hv : v ≠ (0, 0)) :
    ∃ s : K, s ≠ 0 ∧ v = scaleVec s (homogeneous (project v)) := by
  by_cases hy : v.2 = 0
  · have hx : v.1 ≠ 0 := by intro hx; exact hv (Prod.ext hx hy)
    refine ⟨v.1, hx, ?_⟩
    apply Prod.ext <;> simp [scaleVec, homogeneous, project, hy]
  · refine ⟨v.2, hy, ?_⟩
    apply Prod.ext
    · simp [scaleVec, homogeneous, project, hy]
      field_simp
    · simp [scaleVec, homogeneous, project, hy]

theorem mapVec_scale (m : Matrix2 K) (s : K) (v : Vec K) :
    mapVec m (scaleVec s v) = scaleVec s (mapVec m v) := by
  apply Prod.ext <;> dsimp [mapVec, scaleVec] <;> ring

theorem determinant_multiply (m n : Matrix2 K) :
    determinant (multiply m n) = determinant m * determinant n := by
  dsimp [determinant, multiply]; ring

theorem determinant_adjugate (m : Matrix2 K) : determinant (adjugate m) = determinant m := by
  dsimp [determinant, adjugate]; ring

theorem mapVec_multiply (m n : Matrix2 K) (v : Vec K) :
    mapVec (multiply m n) v = mapVec m (mapVec n v) := by
  apply Prod.ext <;> dsimp [mapVec, multiply] <;> ring

theorem adjugate_left (m : Matrix2 K) (v : Vec K) :
    mapVec (adjugate m) (mapVec m v) = scaleVec (determinant m) v := by
  apply Prod.ext <;> dsimp [mapVec, adjugate, scaleVec, determinant] <;> ring

theorem adjugate_right (m : Matrix2 K) (v : Vec K) :
    mapVec m (mapVec (adjugate m) v) = scaleVec (determinant m) v := by
  apply Prod.ext <;> dsimp [mapVec, adjugate, scaleVec, determinant] <;> ring

theorem mapVec_nonzero (m : Matrix2 K) (v : Vec K)
    (hd : determinant m ≠ 0) (hv : v ≠ (0, 0)) : mapVec m v ≠ (0, 0) := by
  intro h
  have he := congrArg (mapVec (adjugate m)) h
  rw [adjugate_left] at he
  have hx : determinant m * v.1 = 0 := by simpa [mapVec, scaleVec] using congrArg Prod.fst he
  have hy : determinant m * v.2 = 0 := by simpa [mapVec, scaleVec] using congrArg Prod.snd he
  exact hv (Prod.ext ((mul_eq_zero.mp hx).resolve_left hd) ((mul_eq_zero.mp hy).resolve_left hd))

theorem project_map_normalize (m : Matrix2 K) (v : Vec K) (hv : v ≠ (0, 0)) :
    project (mapVec m (homogeneous (project v))) = project (mapVec m v) := by
  obtain ⟨s, hs, he⟩ := representative_scale v hv
  conv_rhs => rw [he, mapVec_scale, project_scale s _ hs]

theorem action_identity (x : Point K) : act identity x = x := by
  simpa [act, mapVec, identity] using project_homogeneous x

theorem action_multiply (m n : Matrix2 K) (x : Point K) (hn : determinant n ≠ 0) :
    act (multiply m n) x = act m (act n x) := by
  unfold act
  rw [mapVec_multiply]
  exact (project_map_normalize m _ (mapVec_nonzero n _ hn (homogeneous_nonzero x))).symm

theorem action_adjugate_left (m : Matrix2 K) (x : Point K) (hd : determinant m ≠ 0) :
    act (adjugate m) (act m x) = x := by
  unfold act
  rw [project_map_normalize _ _ (mapVec_nonzero m _ hd (homogeneous_nonzero x)),
    adjugate_left, project_scale _ _ hd, project_homogeneous]

theorem action_adjugate_right (m : Matrix2 K) (x : Point K) (hd : determinant m ≠ 0) :
    act m (act (adjugate m) x) = x := by
  unfold act
  rw [project_map_normalize _ _ (mapVec_nonzero (adjugate m) _ (by rwa [determinant_adjugate])
    (homogeneous_nonzero x)), adjugate_right, project_scale _ _ hd, project_homogeneous]

def actionEquiv (m : Matrix2 K) (hd : determinant m ≠ 0) : Equiv.Perm (Point K) where
  toFun := act m
  invFun := act (adjugate m)
  left_inv := fun x => action_adjugate_left m x hd
  right_inv := fun x => action_adjugate_right m x hd

theorem actionEquiv_apply (m : Matrix2 K) (hd : determinant m ≠ 0) (x : Point K) :
    actionEquiv m hd x = act m x := rfl

theorem actionEquiv_inverse (m : Matrix2 K) (hd : determinant m ≠ 0) (x : Point K) :
    (actionEquiv m hd).symm x = act (adjugate m) x := rfl

theorem finite_action (m : Matrix2 K) (x : K) :
    act m (some x) = if m.c*x+m.d=0 then none else some ((m.a*x+m.b)/(m.c*x+m.d)) := by
  simp [act, project, mapVec, homogeneous]

theorem infinity_action (m : Matrix2 K) :
    act m none = if m.c=0 then none else some (m.a/m.c) := by
  simp [act, project, mapVec, homogeneous]

theorem fixes_infinity_iff (m : Matrix2 K) : act m none = none ↔ m.c = 0 := by
  rw [infinity_action]; split_ifs <;> simp_all

theorem pole_formula (m : Matrix2 K) (hd : determinant m ≠ 0) :
    (actionEquiv m hd).symm none = if m.c=0 then none else some (-m.d/m.c) := by
  rw [actionEquiv_inverse, infinity_action]
  simp [adjugate, div_neg, neg_div]

theorem finite_pole_unique (m : Matrix2 K) (hd : determinant m ≠ 0) (hc : m.c ≠ 0) (x : K) :
    act m (some x) = none ↔ x = -m.d/m.c := by
  have h := (actionEquiv m hd).apply_eq_iff_eq_symm_apply (x := some x) (y := none)
  simpa only [actionEquiv_apply, pole_formula, hc, if_false, Option.some.injEq] using h

theorem action_scale (s : K) (m : Matrix2 K) (x : Point K) (hs : s ≠ 0) :
    act (scaleMatrix s m) x = act m x := by
  have he : mapVec (scaleMatrix s m) (homogeneous x) = scaleVec s (mapVec m (homogeneous x)) := by
    apply Prod.ext <;> dsimp [mapVec, scaleMatrix, scaleVec] <;> ring
  unfold act
  rw [he, project_scale _ _ hs]

theorem project_eq_iff_cross (u v : Vec K) (hu : u ≠ (0, 0)) (hv : v ≠ (0, 0)) :
    project u = project v ↔ u.1*v.2 = v.1*u.2 := by
  by_cases hy : u.2 = 0
  · have hx : u.1 ≠ 0 := by intro h; exact hu (Prod.ext h hy)
    by_cases hz : v.2 = 0
    · simp [project, hy, hz]
    · simp [project, hy, hz, hx]
  · by_cases hz : v.2 = 0
    · have hx : v.1 ≠ 0 := by intro h; exact hv (Prod.ext h hz)
      simp [project, hy, hz, hx]
    · simp only [project, hy, hz, if_false, Option.some.injEq]
      exact div_eq_div_iff hy hz

theorem projection_eq_iff_scalar (u v : Vec K) (hu : u ≠ (0, 0)) (hv : v ≠ (0, 0)) :
    project u = project v ↔ ∃ s : K, s ≠ 0 ∧ u = scaleVec s v := by
  constructor
  · intro h
    obtain ⟨s, hs, he⟩ := representative_scale u hu
    obtain ⟨t, ht, hf⟩ := representative_scale v hv
    refine ⟨s/t, div_ne_zero hs ht, ?_⟩
    rw [he, hf, h]
    apply Prod.ext <;> dsimp [scaleVec] <;> field_simp
  · rintro ⟨s, hs, he⟩
    rw [he, project_scale _ _ hs]

theorem finite_fixed_point_iff (m : Matrix2 K) (hd : determinant m ≠ 0) (x : K) :
    act m (some x) = some x ↔ m.c*x^2+(m.d-m.a)*x-m.b=0 := by
  rw [finite_action]
  by_cases hz : m.c*x+m.d=0
  · simp only [hz, if_true, reduceCtorEq, false_iff]
    intro hp
    have hn : m.a*x+m.b=0 := by linear_combination x*hz-hp
    exact hd (by unfold determinant; linear_combination m.a*hz-m.c*hn)
  · simp only [hz, if_false, Option.some.injEq]
    rw [div_eq_iff hz]
    constructor <;> intro h <;> linear_combination -h

def lineSetoid : Setoid {v : Vec K // v ≠ (0, 0)} where
  r u v := u.val.1 * v.val.2 = v.val.1 * u.val.2
  iseqv := ⟨fun _ => rfl, fun h => h.symm, fun {u v w} huv hvw =>
    (project_eq_iff_cross u.val w.val u.property w.property).mp
      (((project_eq_iff_cross u.val v.val u.property v.property).mpr huv).trans
        ((project_eq_iff_cross v.val w.val v.property w.property).mpr hvw))⟩

def chartEquiv : Quotient (lineSetoid (K := K)) ≃ Point K where
  toFun := Quotient.lift (fun v => project v.val) (fun u v h =>
    (project_eq_iff_cross u.val v.val u.property v.property).mpr h)
  invFun := fun x => Quotient.mk _ ⟨homogeneous x, homogeneous_nonzero x⟩
  left_inv := by
    intro q
    refine Quotient.inductionOn q ?_
    intro v
    apply Quotient.sound
    exact (project_eq_iff_cross _ _ (homogeneous_nonzero (project v.val)) v.property).mp
      (project_homogeneous (project v.val))
  right_inv := project_homogeneous

theorem chart_representative (v : Vec K) (hv : v ≠ (0, 0)) :
    chartEquiv (Quotient.mk (lineSetoid (K := K)) ⟨v, hv⟩) = project v := rfl

theorem quotient_eq_iff_nonzero_scalar (u v : Vec K) (hu : u ≠ (0, 0)) (hv : v ≠ (0, 0)) :
    Quotient.mk (lineSetoid (K := K)) ⟨u, hu⟩ = Quotient.mk (lineSetoid (K := K)) ⟨v, hv⟩ ↔
      ∃ s : K, s ≠ 0 ∧ u = scaleVec s v := by
  rw [← chartEquiv.injective.eq_iff, chart_representative, chart_representative]
  exact projection_eq_iff_scalar u v hu hv

def quotientAction (m : Matrix2 K) (hd : determinant m ≠ 0) :
    Equiv.Perm (Quotient (lineSetoid (K := K))) :=
  (chartEquiv.trans (actionEquiv m hd)).trans chartEquiv.symm

theorem quotient_action_representative (m : Matrix2 K) (hd : determinant m ≠ 0)
    (v : Vec K) (hv : v ≠ (0, 0)) :
    quotientAction m hd (Quotient.mk _ ⟨v, hv⟩) =
      Quotient.mk _ ⟨mapVec m v, mapVec_nonzero m v hd hv⟩ := by
  apply chartEquiv.injective
  change chartEquiv (chartEquiv.symm (act m (project v))) = project (mapVec m v)
  rw [Equiv.apply_symm_apply]
  exact project_map_normalize m v hv

theorem zero_scalar_changes_action :
    act (scaleMatrix 0 (identity : Matrix2 K)) (some 0) ≠ act identity (some 0) := by
  simp [act, project, homogeneous, mapVec, scaleMatrix, identity]

end
end AEGPaper0.ProjectiveLine

#print axioms AEGPaper0.ProjectiveLine.homogeneous_nonzero
#print axioms AEGPaper0.ProjectiveLine.project_homogeneous
#print axioms AEGPaper0.ProjectiveLine.project_scale
#print axioms AEGPaper0.ProjectiveLine.representative_scale
#print axioms AEGPaper0.ProjectiveLine.mapVec_scale
#print axioms AEGPaper0.ProjectiveLine.determinant_multiply
#print axioms AEGPaper0.ProjectiveLine.determinant_adjugate
#print axioms AEGPaper0.ProjectiveLine.mapVec_multiply
#print axioms AEGPaper0.ProjectiveLine.adjugate_left
#print axioms AEGPaper0.ProjectiveLine.adjugate_right
#print axioms AEGPaper0.ProjectiveLine.mapVec_nonzero
#print axioms AEGPaper0.ProjectiveLine.project_map_normalize
#print axioms AEGPaper0.ProjectiveLine.action_identity
#print axioms AEGPaper0.ProjectiveLine.action_multiply
#print axioms AEGPaper0.ProjectiveLine.action_adjugate_left
#print axioms AEGPaper0.ProjectiveLine.action_adjugate_right
#print axioms AEGPaper0.ProjectiveLine.actionEquiv_apply
#print axioms AEGPaper0.ProjectiveLine.actionEquiv_inverse
#print axioms AEGPaper0.ProjectiveLine.finite_action
#print axioms AEGPaper0.ProjectiveLine.infinity_action
#print axioms AEGPaper0.ProjectiveLine.fixes_infinity_iff
#print axioms AEGPaper0.ProjectiveLine.pole_formula
#print axioms AEGPaper0.ProjectiveLine.finite_pole_unique
#print axioms AEGPaper0.ProjectiveLine.action_scale
#print axioms AEGPaper0.ProjectiveLine.project_eq_iff_cross
#print axioms AEGPaper0.ProjectiveLine.projection_eq_iff_scalar
#print axioms AEGPaper0.ProjectiveLine.finite_fixed_point_iff
#print axioms AEGPaper0.ProjectiveLine.chart_representative
#print axioms AEGPaper0.ProjectiveLine.quotient_eq_iff_nonzero_scalar
#print axioms AEGPaper0.ProjectiveLine.quotient_action_representative
#print axioms AEGPaper0.ProjectiveLine.zero_scalar_changes_action
