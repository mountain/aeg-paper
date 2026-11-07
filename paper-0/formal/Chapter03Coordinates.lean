import Chapter02Evaluability
import AppendixC
import Init.Grind

/- Original CC0 continuation by Codex (OpenAI), 2026-11-07.
   Coordinate algebra for the CURRENT Chapter 3. The coefficient field and
   order laws are standard explicit typeclass parameters, not AES axioms.
   No smooth-manifold, derivative, completeness or curvature conclusion is
   assumed or asserted. The displayed assignment differential below is a
   candidate coordinate covector, whose metric-dual bridge is proved here.
   Identifying it with the analytic differential remains a separate task. -/
namespace AEGPaper0.Chapter03Coordinates

open Lean.Grind Std
open AEGPaper0.Chapter02
attribute [local instance] Semiring.natCast
variable {A : Type u} [Field A]

/- Exact interface to the preceding ordinary partial semantics. -/
def fieldData : FieldData A where
  add := (· + ·)
  mul := (· * ·)
  zero := 0
  one := 1
  add_assoc := Semiring.add_assoc
  add_comm := Semiring.add_comm
  add_zero := Semiring.add_zero
  mul_assoc := Semiring.mul_assoc
  mul_comm := CommSemiring.mul_comm
  mul_one := Semiring.mul_one
  mul_add := Semiring.left_distrib
  mul_zero := Semiring.mul_zero
  neg := (- ·)
  inv := Inv.inv
  add_neg := by intro a; grind
  inv_zero := Field.inv_zero
  mul_inv := by intro a h; exact Field.mul_inv_cancel h
  zero_ne_one := Field.zero_ne_one

theorem rational_field_bridge : fieldData (A := Rat) =
    AEGPaper0.Chapter02Evaluability.rationalField := by rfl

abbrev Vec (A : Type u) := A × A
def dot (v w : Vec A) : A := v.1 * w.1 + v.2 * w.2
def det (v w : Vec A) : A := v.1 * w.2 - v.2 * w.1
def rotate (v : Vec A) : Vec A := (-v.2, v.1)

structure Frame (A : Type u) where
  u : Vec A
  v : Vec A

def OrthonormalOriented (f : Frame A) : Prop :=
  dot f.u f.u = 1 ∧ dot f.v f.v = 1 ∧ dot f.u f.v = 0 ∧ det f.u f.v = 1

def canonicalFrame (mu lambda a q : A) : Frame A :=
  ⟨(mu / q, -(lambda * a) / q), (lambda * a / q, mu / q)⟩

theorem frame_rotation (f : Frame A) (h : OrthonormalOriented f) : f.v = rotate f.u := by
  obtain ⟨hu, _, huv, hd⟩ := h
  simp only [dot, det] at hu huv hd
  apply Prod.ext <;> simp only [rotate] <;> grind

theorem canonical_frame_orthonormal (mu lambda a q : A) (hq : q ≠ 0)
    (he : q^2 = mu^2 + lambda^2 * a^2) : OrthonormalOriented (canonicalFrame mu lambda a q) := by
  simp only [OrthonormalOriented, canonicalFrame, dot, det]
  grind

theorem canonical_frame_directional (mu lambda a q : A) (hq : q ≠ 0) :
    q * (canonicalFrame mu lambda a q).u.1 = mu ∧
      q * (canonicalFrame mu lambda a q).v.1 = lambda * a := by
  simp only [canonicalFrame]
  grind

theorem canonical_frame_unique (mu lambda a q : A) (hq : q ≠ 0) (f : Frame A)
    (hf : OrthonormalOriented f) (hu : q * f.u.1 = mu) (hv : q * f.v.1 = lambda * a) :
    f = canonicalFrame mu lambda a q := by
  have hr := frame_rotation f hf
  cases f with
  | mk u v =>
    congr 1 <;> apply Prod.ext <;>
      simp only [rotate] at * <;> grind

theorem frame_eikonal_converse (mu lambda a q : A) (f : Frame A)
    (hf : OrthonormalOriented f) (hu : q * f.u.1 = mu) (hv : q * f.v.1 = lambda * a) :
    q^2 = mu^2 + lambda^2 * a^2 := by
  have hr := frame_rotation f hf
  obtain ⟨hunit, _, _, _⟩ := hf
  simp only [dot, rotate] at *
  grind

/- Nonzero y is the algebraic chart guard. Positivity is handled separately. -/
def assignment (p : Vec A) : A := -p.1 / p.2
def metric (mu lambda : A) (p v w : Vec A) : A :=
  v.1 * w.1 / (mu^2 * p.2^2) + v.2 * w.2 / (lambda^2 * p.2^2)
def assignmentCovector (p v : Vec A) : A := -v.1 / p.2 + p.1 * v.2 / p.2^2
def gradientCandidate (mu lambda : A) (p : Vec A) : Vec A :=
  (-mu^2 * p.2, lambda^2 * p.1)
def modelFrame (mu lambda : A) (p : Vec A) : Frame A :=
  ⟨(-mu * p.2, 0), (0, -lambda * p.2)⟩
def leftTranslate (g p : Vec A) : Vec A := (g.1 + g.2 * p.1, g.2 * p.2)
def leftTangent (g v : Vec A) : Vec A := (g.2 * v.1, g.2 * v.2)
def addVec (v w : Vec A) : Vec A := (v.1 + w.1, v.2 + w.2)
def scaleVec (c : A) (v : Vec A) : Vec A := (c * v.1, c * v.2)

theorem metric_add_left (mu lambda : A) (p u v w : Vec A) :
    metric mu lambda p (addVec u v) w = metric mu lambda p u w + metric mu lambda p v w := by
  simp only [metric, addVec]; grind

theorem metric_scale_left (mu lambda c : A) (p v w : Vec A) :
    metric mu lambda p (scaleVec c v) w = c * metric mu lambda p v w := by
  simp only [metric, scaleVec]; grind

theorem covector_linear (p v w : Vec A) (c : A) :
    assignmentCovector p (addVec v w) = assignmentCovector p v + assignmentCovector p w ∧
      assignmentCovector p (scaleVec c v) = c * assignmentCovector p v := by
  simp only [assignmentCovector, addVec, scaleVec]; grind

theorem metric_symmetric (mu lambda : A) (p v w : Vec A) :
    metric mu lambda p v w = metric mu lambda p w v := by
  simp only [metric]; grind

theorem model_frame_orthonormal (mu lambda : A) (p : Vec A)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    metric mu lambda p (modelFrame mu lambda p).u (modelFrame mu lambda p).u = 1 ∧
    metric mu lambda p (modelFrame mu lambda p).v (modelFrame mu lambda p).v = 1 ∧
    metric mu lambda p (modelFrame mu lambda p).u (modelFrame mu lambda p).v = 0 := by
  simp only [metric, modelFrame]; grind

theorem model_frame_determinant (mu lambda : A) (p : Vec A) :
    det (modelFrame mu lambda p).u (modelFrame mu lambda p).v = mu * lambda * p.2^2 := by
  simp only [det, modelFrame]; grind

theorem model_frame_assignment (mu lambda : A) (p : Vec A) (hy : p.2 ≠ 0) :
    assignmentCovector p (modelFrame mu lambda p).u = mu ∧
      assignmentCovector p (modelFrame mu lambda p).v = lambda * assignment p := by
  simp only [assignmentCovector, modelFrame, assignment]; grind

theorem gradient_metric_dual (mu lambda : A) (p v : Vec A)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    metric mu lambda p (gradientCandidate mu lambda p) v = assignmentCovector p v := by
  simp only [metric, gradientCandidate, assignmentCovector]; grind

theorem gradient_metric_unique (mu lambda : A) (p w : Vec A)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0)
    (h : ∀ v, metric mu lambda p w v = assignmentCovector p v) :
    w = gradientCandidate mu lambda p := by
  have hx := h (1, 0)
  have hv := h (0, 1)
  apply Prod.ext <;> simp only [metric, assignmentCovector, gradientCandidate] at * <;> grind

theorem model_eikonal_coordinate (mu lambda : A) (p : Vec A)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    metric mu lambda p (gradientCandidate mu lambda p) (gradientCandidate mu lambda p) =
      mu^2 + lambda^2 * (assignment p)^2 := by
  simp only [metric, gradientCandidate, assignment]; grind

theorem model_gradient_nonzero (mu lambda : A) (p : Vec A)
    (hm : mu ≠ 0) (hy : p.2 ≠ 0) : gradientCandidate mu lambda p ≠ (0, 0) := by
  intro h
  have hx := congrArg Prod.fst h
  simp only [gradientCandidate] at hx
  grind

theorem invariant_metric_coordinates (mu lambda : A) (g p v w : Vec A)
    (hg : g.2 ≠ 0) (hy : p.2 ≠ 0) :
    metric mu lambda (leftTranslate g p) (leftTangent g v) (leftTangent g w) =
      metric mu lambda p v w := by
  simp only [metric, leftTranslate, leftTangent]; grind

theorem left_invariant_frame (mu lambda : A) (g p : Vec A) :
    leftTangent g (modelFrame mu lambda p).u = (modelFrame mu lambda (leftTranslate g p)).u ∧
      leftTangent g (modelFrame mu lambda p).v = (modelFrame mu lambda (leftTranslate g p)).v := by
  constructor <;> apply Prod.ext <;> simp only [leftTangent, modelFrame, leftTranslate] <;> grind

theorem scaled_standard_metric (mu lambda : A) (p v w : Vec A)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    metric mu lambda p v w =
      (((lambda / mu * v.1) * (lambda / mu * w.1) + v.2 * w.2) / p.2^2) / lambda^2 := by
  simp only [metric]; grind

theorem assignment_contour (p : Vec A) (hy : p.2 ≠ 0) (c : A) :
    assignment p = c ↔ p.1 = -c * p.2 := by
  simp only [assignment]; grind

def translate (s : A) (p : Vec A) : Vec A := (p.1 - s * p.2, p.2)
def scale (k : A) (p : Vec A) : Vec A := (p.1, p.2 / k)
def reflect (p : Vec A) : Vec A := (-p.1, p.2)

theorem translation_assignment (s : A) (p : Vec A) (hy : p.2 ≠ 0) :
    assignment (translate s p) = assignment p + s := by
  simp only [assignment, translate]; grind

theorem scaling_assignment (k : A) (hk : k ≠ 0) (p : Vec A) (hy : p.2 ≠ 0) :
    assignment (scale k p) = k * assignment p := by
  simp only [assignment, scale]; grind

theorem reflection_assignment (p : Vec A) : assignment (reflect p) = -assignment p := by
  simp only [assignment, reflect]; grind

theorem translation_composition (s t : A) (p : Vec A) :
    translate s (translate t p) = translate (s + t) p := by
  apply Prod.ext <;> simp only [translate] <;> grind

theorem translation_inverse (s : A) (p : Vec A) : translate (-s) (translate s p) = p := by
  apply Prod.ext <;> simp only [translate] <;> grind

theorem scaling_composition (k l : A) (p : Vec A) : scale k (scale l p) = scale (k * l) p := by
  apply Prod.ext <;> simp only [scale] <;> grind

theorem scaling_inverse (k : A) (hk : k ≠ 0) (p : Vec A) : scale k⁻¹ (scale k p) = p := by
  apply Prod.ext <;> simp only [scale] <;> grind

theorem zero_scaling_leaves_chart (p : Vec A) : (scale 0 p).2 = 0 := by
  simp only [scale]; grind

theorem scaling_translation_conjugation (k s : A) (hk : k ≠ 0) (p : Vec A) :
    scale k⁻¹ (translate s (scale k p)) = translate (s / k) p := by
  apply Prod.ext <;> simp only [scale, translate] <;> grind

def translationIterate (s : A) : Nat → Vec A → Vec A
  | 0, p => p
  | n + 1, p => translate s (translationIterate s n p)

theorem translation_iterate (s : A) (n : Nat) (p : Vec A) :
    translationIterate s n p = translate ((n : A) * s) p := by
  induction n with
  | zero => apply Prod.ext <;> simp only [translationIterate, translate] <;> grind
  | succ n ih =>
    rw [translationIterate, ih, translation_composition]
    apply congrArg (fun t => translate t p)
    grind

theorem baumslag_solitar_coordinates (s : A) (m : Nat) (hm : (m : A) ≠ 0) (p : Vec A) :
    scale (m : A)⁻¹ (translationIterate s m (scale (m : A) p)) = translate s p := by
  rw [translation_iterate, scaling_translation_conjugation _ _ hm]
  congr 1
  grind

/- A lift of a nonzero affine value operator to the punctured coordinate
   chart. It has the required assignment action; it need not be an isometry. -/
structure Affine (A : Type u) where
  multiplier : A
  translation : A

def evalAffine (f : Affine A) (z : A) : A := f.multiplier * z + f.translation
def liftAffine (f : Affine A) (p : Vec A) : Vec A := translate f.translation (scale f.multiplier p)
def compose (outer inner : Affine A) : Affine A :=
  ⟨outer.multiplier * inner.multiplier, outer.multiplier * inner.translation + outer.translation⟩
def identityAffine : Affine A := ⟨1, 0⟩

theorem affine_lift_assignment (f : Affine A) (hf : f.multiplier ≠ 0) (p : Vec A)
    (hy : p.2 ≠ 0) : assignment (liftAffine f p) = evalAffine f (assignment p) := by
  have hscale : (scale f.multiplier p).2 ≠ 0 := by simp only [scale]; grind
  rw [liftAffine, translation_assignment _ _ hscale, scaling_assignment _ hf _ hy]
  rfl

theorem affine_lift_chart (f : Affine A) (hf : f.multiplier ≠ 0) (p : Vec A)
    (hy : p.2 ≠ 0) : (liftAffine f p).2 ≠ 0 := by
  simp only [liftAffine, translate, scale]; grind

theorem affine_composition_value (outer inner : Affine A) (z : A) :
    evalAffine (compose outer inner) z = evalAffine outer (evalAffine inner z) := by
  simp only [evalAffine, compose]; grind

theorem affine_composition_lift (outer inner : Affine A)
    (ho : outer.multiplier ≠ 0) (hi : inner.multiplier ≠ 0) (p : Vec A) :
    liftAffine (compose outer inner) p = liftAffine outer (liftAffine inner p) := by
  apply Prod.ext <;> simp only [liftAffine, compose, translate, scale] <;> grind

def pathPoint : List (Affine A) → Vec A → Vec A
  | [], p => p
  | f :: rest, p => pathPoint rest (liftAffine f p)
def pathValue : List (Affine A) → A → A
  | [], z => z
  | f :: rest, z => pathValue rest (evalAffine f z)
def ValidWord (word : List (Affine A)) : Prop := ∀ f ∈ word, f.multiplier ≠ 0

theorem finite_path_assignment (word : List (Affine A)) (hw : ValidWord word)
    (p : Vec A) (hy : p.2 ≠ 0) :
    assignment (pathPoint word p) = pathValue word (assignment p) := by
  induction word generalizing p with
  | nil => rfl
  | cons f rest ih =>
    have hf := hw f (by simp)
    have hr : ValidWord rest := by intro g hg; exact hw g (by simp [hg])
    rw [pathPoint, pathValue, ih hr _ (affine_lift_chart f hf p hy), affine_lift_assignment f hf p hy]

theorem prefix_path_assignment (word : List (Affine A)) (hw : ValidWord word)
    (n : Nat) (p : Vec A) (hy : p.2 ≠ 0) :
    assignment (pathPoint (word.take n) p) = pathValue (word.take n) (assignment p) := by
  apply finite_path_assignment _ _ p hy
  intro f hf; exact hw f (List.mem_of_mem_take hf)

theorem affine_value_unique (f g : Affine A) (h : ∀ z, evalAffine f z = evalAffine g z) : f = g := by
  have h0 := h 0
  have h1 := h 1
  cases f; cases g
  congr 1 <;> simp only [evalAffine] at * <;> grind

theorem affine_value_bridge (f : Affine A) (z : A) :
    evalAffine f z = AffineValue fieldData f.multiplier f.translation z := rfl

theorem affine_list_bridge (word : List (Affine A)) (z : A) :
    pathValue word z = AEGPaper0.AppendixC.evaluate fieldData.toAlgebra
      (word.map (fun f => (f.multiplier, f.translation))) z := by
  induction word generalizing z with
  | nil => rfl
  | cons f rest ih => exact ih (evalAffine f z)

theorem point_path_tree_bridge (word : List (Affine A)) (hw : ValidWord word)
    (p : Vec A) (hy : p.2 ≠ 0) :
    TreeEval (Eval fieldData) (assignment p)
      (leftTree (AEGPaper0.AppendixC.events (word.map (fun f => (f.multiplier, f.translation)))))
      (assignment (pathPoint word p)) := by
  apply (AEGPaper0.AppendixC.tree_correspondence fieldData _ _ _).mpr
  exact (finite_path_assignment word hw p hy).trans (affine_list_bridge word (assignment p))

theorem compose_associative (f g h : Affine A) : compose f (compose g h) = compose (compose f g) h := by
  apply affine_value_unique
  intro z
  simp only [affine_composition_value]

theorem compose_identity (f : Affine A) : compose identityAffine f = f ∧ compose f identityAffine = f := by
  constructor <;> apply affine_value_unique <;> intro z <;>
    simp only [evalAffine, identityAffine, compose] <;> grind

def prefixOperator : List (Affine A) → Affine A
  | [] => identityAffine
  | f :: rest => compose (prefixOperator rest) f

theorem prefix_operator_value (word : List (Affine A)) (z : A) :
    evalAffine (prefixOperator word) z = pathValue word z := by
  induction word generalizing z with
  | nil => simp only [prefixOperator, pathValue, identityAffine, evalAffine]; grind
  | cons f rest ih => rw [prefixOperator, affine_composition_value, pathValue, ih]

theorem prefix_operator_snoc (word : List (Affine A)) (f : Affine A) :
    prefixOperator (word ++ [f]) = compose f (prefixOperator word) := by
  induction word with
  | nil =>
    simp only [List.nil_append, prefixOperator]
    exact (compose_identity f).1.trans (compose_identity f).2.symm
  | cons g rest ih =>
    simp only [List.cons_append, prefixOperator, ih]
    exact (compose_associative f (prefixOperator rest) g).symm

theorem prefix_multiplier_nonzero (word : List (Affine A)) (hw : ValidWord word) :
    (prefixOperator word).multiplier ≠ 0 := by
  induction word with
  | nil => simp only [prefixOperator, identityAffine]; exact Field.zero_ne_one.symm
  | cons f rest ih =>
    have hf := hw f (by simp)
    have hr := ih (fun g hg => hw g (by simp [hg]))
    simp only [prefixOperator, compose]
    grind

theorem dilation_translation_conjugation (k s : A) (hk : k ≠ 0) (p : Vec A) :
    scale k (translate s (scale k⁻¹ p)) = translate (k * s) p := by
  apply Prod.ext <;> simp only [scale, translate] <;> grind

theorem finite_order_defect (k s z : A) : k * (z + s) - (k * z + s) = s * (k - 1) := by
  grind

/- Positivity is an extra STANDARD ordered-field structure. It is not
   inferred from nonzero coordinates or from a field-law certificate. -/
section Ordered
variable [LE A] [LT A] [IsLinearOrder A] [LawfulOrderLT A] [OrderedRing A]

theorem inverse_positive (k : A) (hk : 0 < k) : 0 < k⁻¹ := by
  have hn : k ≠ 0 := by grind
  have hp : 0 < k * k⁻¹ := by rw [Field.mul_inv_cancel hn]; exact OrderedRing.zero_lt_one
  cases OrderedRing.mul_pos_iff.mp hp with
  | inl h => exact h.2
  | inr h => grind

theorem quotient_positive (y k : A) (hy : 0 < y) (hk : 0 < k) : 0 < y / k := by
  rw [Field.div_eq_mul_inv]
  exact OrderedRing.mul_pos hy (inverse_positive k hk)

structure UpperPoint (A : Type u) [Field A] [LT A] where
  coordinates : Vec A
  height_positive : 0 < coordinates.2

def upperTranslate (s : A) (p : UpperPoint A) : UpperPoint A :=
  ⟨translate s p.coordinates, p.height_positive⟩
def upperScale (k : A) (hk : 0 < k) (p : UpperPoint A) : UpperPoint A :=
  ⟨scale k p.coordinates, quotient_positive p.coordinates.2 k p.height_positive hk⟩

theorem upper_translation_assignment (s : A) (p : UpperPoint A) :
    assignment (upperTranslate s p).coordinates = assignment p.coordinates + s := by
  apply translation_assignment
  have h := p.height_positive; grind

theorem upper_scaling_assignment (k : A) (hk : 0 < k) (p : UpperPoint A) :
    assignment (upperScale k hk p).coordinates = k * assignment p.coordinates := by
  apply scaling_assignment
  · grind
  · have h := p.height_positive; grind

theorem model_frame_positive_orientation (mu lambda : A) (hm : 0 < mu) (hl : 0 < lambda)
    (p : UpperPoint A) : det (modelFrame mu lambda p.coordinates).u
      (modelFrame mu lambda p.coordinates).v > 0 := by
  rw [model_frame_determinant]
  have hy : p.coordinates.2 ≠ 0 := by have h := p.height_positive; grind
  exact OrderedRing.mul_pos (OrderedRing.mul_pos hm hl) (OrderedRing.sq_pos hy)

theorem eikonal_rhs_positive (mu lambda a : A) (hm : mu ≠ 0) : 0 < mu^2 + lambda^2 * a^2 := by
  have hp := OrderedRing.sq_pos hm
  have hl := OrderedRing.sq_nonneg (a := lambda)
  have ha := OrderedRing.sq_nonneg (a := a)
  have hprod := OrderedRing.mul_nonneg hl ha
  grind

theorem root_nonzero (mu lambda a q : A) (hm : mu ≠ 0)
    (hq : q^2 = mu^2 + lambda^2 * a^2) : q ≠ 0 := by
  have hp := eikonal_rhs_positive mu lambda a hm
  grind

theorem metric_positive_definite (mu lambda : A) (p v : Vec A)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) (hv : v ≠ (0, 0)) :
    0 < metric mu lambda p v v := by
  have he : metric mu lambda p v v = (v.1 / (mu * p.2))^2 + (v.2 / (lambda * p.2))^2 := by
    simp only [metric]; grind
  rw [he]
  have hn1 := OrderedRing.sq_nonneg (a := v.1 / (mu * p.2))
  have hn2 := OrderedRing.sq_nonneg (a := v.2 / (lambda * p.2))
  by_cases hx : v.1 = 0
  · have hvy : v.2 ≠ 0 := by intro h; exact hv (Prod.ext hx h)
    have hn : v.2 / (lambda * p.2) ≠ 0 := by grind
    have hp := OrderedRing.sq_pos hn
    grind
  · have hn : v.1 / (mu * p.2) ≠ 0 := by grind
    have hp := OrderedRing.sq_pos hn
    grind

end Ordered

def fourStepWord : List (Affine Rat) := [⟨4, 0⟩, ⟨1, -1⟩, ⟨2, 0⟩, ⟨1, -3⟩]

theorem rational_four_step_point : pathPoint fourStepWord (-8, 8) = (-3, 1) := by decide +kernel

theorem rational_four_step_prefixes :
    (List.range 5).map (fun n => assignment (pathPoint (fourStepWord.take n) (-8, 8))) =
      ([1, 4, 3, 6, 3] : List Rat) := by decide +kernel

theorem rational_model_eikonal :
    assignment ((-8, 8) : Vec Rat) = 1 ∧
      metric 2 3 (-8, 8) (gradientCandidate 2 3 (-8, 8)) (gradientCandidate 2 3 (-8, 8)) = (13 : Rat) := by
  decide +kernel

theorem rational_orientation_counterexample :
    dot ((1, 0) : Vec Rat) (1, 0) = 1 ∧ dot ((0, -1) : Vec Rat) (0, -1) = 1 ∧
      dot ((1, 0) : Vec Rat) (0, -1) = 0 ∧ det ((1, 0) : Vec Rat) (0, -1) = -1 ∧
      det (canonicalFrame (1 : Rat) 0 0 1).u (canonicalFrame (1 : Rat) 0 0 1).v = 1 := by
  decide +kernel

#print axioms rational_field_bridge
#print axioms frame_rotation
#print axioms canonical_frame_orthonormal
#print axioms canonical_frame_directional
#print axioms canonical_frame_unique
#print axioms frame_eikonal_converse
#print axioms metric_add_left
#print axioms metric_scale_left
#print axioms covector_linear
#print axioms metric_symmetric
#print axioms model_frame_orthonormal
#print axioms model_frame_determinant
#print axioms model_frame_assignment
#print axioms gradient_metric_dual
#print axioms gradient_metric_unique
#print axioms model_eikonal_coordinate
#print axioms model_gradient_nonzero
#print axioms invariant_metric_coordinates
#print axioms left_invariant_frame
#print axioms scaled_standard_metric
#print axioms assignment_contour
#print axioms translation_assignment
#print axioms scaling_assignment
#print axioms reflection_assignment
#print axioms translation_composition
#print axioms translation_inverse
#print axioms scaling_composition
#print axioms scaling_inverse
#print axioms zero_scaling_leaves_chart
#print axioms scaling_translation_conjugation
#print axioms translation_iterate
#print axioms baumslag_solitar_coordinates
#print axioms affine_lift_assignment
#print axioms affine_lift_chart
#print axioms affine_composition_value
#print axioms affine_composition_lift
#print axioms finite_path_assignment
#print axioms prefix_path_assignment
#print axioms affine_value_unique
#print axioms affine_value_bridge
#print axioms affine_list_bridge
#print axioms point_path_tree_bridge
#print axioms compose_associative
#print axioms compose_identity
#print axioms prefix_operator_value
#print axioms prefix_operator_snoc
#print axioms prefix_multiplier_nonzero
#print axioms dilation_translation_conjugation
#print axioms finite_order_defect
#print axioms inverse_positive
#print axioms quotient_positive
#print axioms upper_translation_assignment
#print axioms upper_scaling_assignment
#print axioms model_frame_positive_orientation
#print axioms eikonal_rhs_positive
#print axioms root_nonzero
#print axioms metric_positive_definite
#print axioms rational_four_step_point
#print axioms rational_four_step_prefixes
#print axioms rational_model_eikonal
#print axioms rational_orientation_counterexample
end AEGPaper0.Chapter03Coordinates
