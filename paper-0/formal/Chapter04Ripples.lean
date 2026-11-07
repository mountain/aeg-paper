import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   Real coefficients in the manuscript's complex continuation chart.
   Ordinary partial arithmetic is not replaced by total complex division.
   Circle/disk equations below are Euclidean coordinate equations; no new
   intrinsic hyperbolic geometry or chart independence is inferred. -/
namespace AEGPaper0.Chapter04Ripples

noncomputable section

structure Coefficients where
  a : ℝ
  b : ℝ
  c : ℝ
  d : ℝ

def determinant (m : Coefficients) : ℝ := m.a * m.d - m.b * m.c
def denominator (m : Coefficients) (z : ℂ) : ℂ := m.c * z + m.d
def denominatorSq (m : Coefficients) (z : ℂ) : ℝ :=
  (m.c * z.re + m.d)^2 + m.c^2 * z.im^2
def mobius (m : Coefficients) (z : ℂ) : ℂ :=
  (m.a * z + m.b) / denominator m z
def upper : Set ℂ := {z | 0 < z.im}
def horocycle (t : ℝ) : Set ℂ := {z | z ∈ upper ∧ z.im = t}
def ripple (m : Coefficients) (t : ℝ) : Set ℂ :=
  upper ∩ mobius m ⁻¹' horocycle t
def radius (m : Coefficients) (t : ℝ) : ℝ := determinant m / (2 * t * m.c^2)
def poleX (m : Coefficients) : ℝ := -m.d / m.c
def circleEquation (m : Coefficients) (t x y : ℝ) : Prop :=
  (x + m.d / m.c)^2 + (y - radius m t)^2 = (radius m t)^2
def tangentDisk (p r : ℝ) : Set (ℝ × ℝ) :=
  {v | (v.1 - p)^2 + (v.2 - r)^2 ≤ r^2}

theorem denominator_normSq (m : Coefficients) (z : ℂ) :
    Complex.normSq (denominator m z) = denominatorSq m z := by
  simp [denominator, denominatorSq, Complex.normSq_apply]
  ring

theorem denominator_ne_zero (m : Coefficients) (z : ℂ)
    (hd : determinant m ≠ 0) (hy : z ∈ upper) : denominator m z ≠ 0 := by
  intro h
  have hi := congrArg Complex.im h
  have hr := congrArg Complex.re h
  simp [denominator] at hi hr
  have hc : m.c = 0 := hi.resolve_right (ne_of_gt hy)
  have hz : m.d = 0 := by simpa [hc] using hr
  exact hd (by simp [determinant, hc, hz])

theorem denominatorSq_positive (m : Coefficients) (z : ℂ)
    (hd : determinant m ≠ 0) (hy : z ∈ upper) : 0 < denominatorSq m z := by
  rw [← denominator_normSq]
  exact Complex.normSq_pos.mpr (denominator_ne_zero m z hd hy)

theorem mobius_imaginary (m : Coefficients) (z : ℂ) :
    (mobius m z).im = determinant m * z.im / denominatorSq m z := by
  simp only [mobius, Complex.div_im]
  rw [denominator_normSq]
  simp [denominator, determinant]
  ring

theorem mobius_preserves_upper (m : Coefficients) (z : ℂ)
    (hd : 0 < determinant m) (hy : z ∈ upper) : mobius m z ∈ upper := by
  change 0 < (mobius m z).im
  rw [mobius_imaginary]
  exact div_pos (mul_pos hd hy) (denominatorSq_positive m z (ne_of_gt hd) hy)

theorem ripple_membership (m : Coefficients) (t : ℝ) (z : ℂ) :
    z ∈ ripple m t ↔ z ∈ upper ∧ mobius m z ∈ horocycle t := Iff.rfl

theorem ripple_level (m : Coefficients) (t : ℝ) (z : ℂ)
    (hd : 0 < determinant m) (hy : z ∈ upper) :
    z ∈ ripple m t ↔ (mobius m z).im = t := by
  simp only [ripple_membership, horocycle, Set.mem_setOf_eq]
  exact and_iff_right hy |>.trans (and_iff_right (mobius_preserves_upper m z hd hy))

theorem ripple_equation (m : Coefficients) (t : ℝ) (z : ℂ)
    (hd : 0 < determinant m) (hy : z ∈ upper) :
    z ∈ ripple m t ↔ determinant m * z.im = t * denominatorSq m z := by
  rw [ripple_level m t z hd hy, mobius_imaginary]
  exact div_eq_iff (ne_of_gt (denominatorSq_positive m z (ne_of_gt hd) hy))

theorem affine_diagonal_nonzero (m : Coefficients)
    (hd : determinant m ≠ 0) (hc : m.c = 0) : m.d ≠ 0 := by
  intro h
  exact hd (by simp [determinant, hc, h])

theorem affine_ripple_line (m : Coefficients) (t : ℝ) (z : ℂ)
    (hd : 0 < determinant m) (hc : m.c = 0) (hy : z ∈ upper) :
    z ∈ ripple m t ↔ z.im = t * m.d^2 / determinant m := by
  rw [ripple_equation m t z hd hy]
  simp only [denominatorSq, hc, zero_mul, zero_add, zero_pow (by decide : 2 ≠ 0),
    add_zero]
  constructor
  · intro h; apply (eq_div_iff (ne_of_gt hd)).mpr; nlinarith [h]
  · intro h; have hh := (eq_div_iff (ne_of_gt hd)).mp h; nlinarith [hh]

theorem radius_positive (m : Coefficients) (t : ℝ)
    (hd : 0 < determinant m) (ht : 0 < t) (hc : m.c ≠ 0) : 0 < radius m t := by
  exact div_pos hd (mul_pos (mul_pos (by norm_num) ht) (sq_pos_of_ne_zero hc))

theorem completed_square (m : Coefficients) (t x y : ℝ)
    (ht : t ≠ 0) (hc : m.c ≠ 0) :
    determinant m * y = t * ((m.c * x + m.d)^2 + m.c^2 * y^2) ↔
      circleEquation m t x y := by
  have he : (x + m.d / m.c)^2 + (y - radius m t)^2 - (radius m t)^2 =
      (t * ((m.c * x + m.d)^2 + m.c^2 * y^2) - determinant m * y) / (t * m.c^2) := by
    unfold radius
    field_simp
    ring
  change _ ↔ _ = _
  have htc : t * m.c^2 ≠ 0 := mul_ne_zero ht (pow_ne_zero 2 hc)
  conv_rhs => rw [← sub_eq_zero, he, div_eq_zero_iff]
  simp only [htc, or_false]
  constructor <;> intro h <;> linarith [h]

theorem ripple_circle (m : Coefficients) (t : ℝ) (z : ℂ)
    (hd : 0 < determinant m) (ht : 0 < t) (hc : m.c ≠ 0) (hy : z ∈ upper) :
    z ∈ ripple m t ↔ circleEquation m t z.re z.im := by
  rw [ripple_equation m t z hd hy]
  exact completed_square m t z.re z.im (ne_of_gt ht) hc

theorem circle_boundary_contact (m : Coefficients) (t x : ℝ) :
    circleEquation m t x 0 ↔ x = poleX m := by
  unfold circleEquation poleX
  constructor
  · intro h
    have hh : x + m.d / m.c = 0 := by nlinarith [sq_nonneg (x + m.d / m.c)]
    simpa [neg_div] using (eq_neg_iff_add_eq_zero.mpr hh)
  · intro h; rw [h]; ring

theorem circle_height_bounds (m : Coefficients) (t x y : ℝ)
    (hr : 0 < radius m t) (h : circleEquation m t x y) : 0 ≤ y ∧ y ≤ 2 * radius m t := by
  have he : (x + m.d / m.c)^2 + y^2 = 2 * radius m t * y := by
    unfold circleEquation at h; nlinarith [h]
  constructor
  · nlinarith [sq_nonneg (x + m.d / m.c), sq_nonneg y]
  · nlinarith [sq_nonneg (x + m.d / m.c)]

theorem radius_antitone (m : Coefficients) (s t : ℝ)
    (hd : 0 < determinant m) (hc : m.c ≠ 0) (hs : 0 < s) (hst : s ≤ t) :
    radius m t ≤ radius m s := by
  unfold radius
  apply div_le_div_of_nonneg_left (le_of_lt hd)
  · positivity
  · exact mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hst (by norm_num)) (sq_nonneg _)

theorem tangentDisk_equation (p r : ℝ) (v : ℝ × ℝ) :
    v ∈ tangentDisk p r ↔ (v.1 - p)^2 + v.2^2 ≤ 2 * r * v.2 := by
  unfold tangentDisk; simp only [Set.mem_setOf_eq]; constructor <;> intro h <;> nlinarith [h]

theorem tangentDisk_height_nonnegative (p r : ℝ) (v : ℝ × ℝ)
    (hr : 0 < r) (hv : v ∈ tangentDisk p r) : 0 ≤ v.2 := by
  rw [tangentDisk_equation] at hv
  nlinarith [sq_nonneg (v.1 - p), sq_nonneg v.2]

theorem tangentDisk_nested (p r s : ℝ) (hr : 0 < r) (hrs : r ≤ s) :
    tangentDisk p r ⊆ tangentDisk p s := by
  intro v hv
  have hy := tangentDisk_height_nonnegative p r v hr hv
  rw [tangentDisk_equation] at hv ⊢
  nlinarith [mul_nonneg (sub_nonneg.mpr hrs) hy]

theorem ripple_disks_nested (m : Coefficients) (s t : ℝ)
    (hd : 0 < determinant m) (hc : m.c ≠ 0) (hs : 0 < s) (hst : s ≤ t) :
    tangentDisk (poleX m) (radius m t) ⊆ tangentDisk (poleX m) (radius m s) := by
  exact tangentDisk_nested _ _ _ (radius_positive m t hd (lt_of_lt_of_le hs hst) hc)
    (radius_antitone m s t hd hc hs hst)

theorem distinct_ripples_disjoint (m : Coefficients) (s t : ℝ) (hst : s ≠ t) :
    Disjoint (ripple m s) (ripple m t) := by
  apply Set.disjoint_left.mpr
  intro z hs ht
  exact hst (hs.2.2.symm.trans ht.2.2)

theorem ripple_parameter_positive (m : Coefficients) (t : ℝ) (z : ℂ)
    (h : z ∈ ripple m t) : 0 < t := by
  have hi := h.2.1
  change 0 < (mobius m z).im at hi
  rwa [h.2.2] at hi

theorem ripple_empty_nonpositive (m : Coefficients) (t : ℝ) (ht : t ≤ 0) :
    ripple m t = ∅ := by
  apply Set.eq_empty_iff_forall_notMem.mpr
  intro z hz
  exact (not_lt_of_ge ht) (ripple_parameter_positive m t z hz)

theorem ripple_unique_positive_level (m : Coefficients) (z : ℂ)
    (hd : 0 < determinant m) (hy : z ∈ upper) :
    ∃! t : ℝ, 0 < t ∧ z ∈ ripple m t := by
  refine ⟨(mobius m z).im, ⟨mobius_preserves_upper m z hd hy,
    ⟨hy, mobius_preserves_upper m z hd hy, rfl⟩⟩, ?_⟩
  intro t ht
  exact ht.2.2.2.symm

def translateOutput (s : ℝ) (m : Coefficients) : Coefficients :=
  ⟨m.a + s * m.c, m.b + s * m.d, m.c, m.d⟩

theorem output_translation_determinant (s : ℝ) (m : Coefficients) :
    determinant (translateOutput s m) = determinant m := by
  simp only [determinant, translateOutput]; ring

theorem output_translation_map (s : ℝ) (m : Coefficients) (z : ℂ)
    (h : denominator m z ≠ 0) : mobius (translateOutput s m) z = mobius m z + s := by
  unfold mobius translateOutput denominator at *
  push_cast
  field_simp
  ring

theorem output_translation_pole (s : ℝ) (m : Coefficients) :
    poleX (translateOutput s m) = poleX m := rfl

theorem output_translation_ripple (s t : ℝ) (m : Coefficients)
    (hd : 0 < determinant m) : ripple (translateOutput s m) t = ripple m t := by
  ext z
  by_cases hy : z ∈ upper
  · rw [ripple_level _ t z (by rwa [output_translation_determinant]) hy,
      ripple_level m t z hd hy, output_translation_map s m z
        (denominator_ne_zero m z (ne_of_gt hd) hy)]
    simp
  · simp only [ripple_membership, hy, false_and]

def inversion : Coefficients := ⟨0, -1, 1, 0⟩

theorem inversion_determinant : determinant inversion = 1 := by norm_num [determinant, inversion]

theorem inversion_map (z : ℂ) : mobius inversion z = -(1 / z) := by
  simp [mobius, inversion, denominator, neg_div]

theorem inversion_radius (t : ℝ) : radius inversion t = 1 / (2 * t) := by
  rw [radius, inversion_determinant]
  norm_num [inversion]

theorem inversion_pole : poleX inversion = 0 := by simp [poleX, inversion]

theorem inversion_followed_by_translation_has_same_finite_pole (s : ℝ) :
    poleX (translateOutput s inversion) = 0 ∧ (translateOutput s inversion).c ≠ 0 := by
  rw [output_translation_pole, inversion_pole]
  norm_num [translateOutput, inversion]

theorem inversion_ripple (t : ℝ) (z : ℂ) (ht : 0 < t) (hy : z ∈ upper) :
    z ∈ ripple inversion t ↔ z.re^2 + (z.im - 1 / (2 * t))^2 = (1 / (2 * t))^2 := by
  rw [ripple_circle inversion t z (by rw [inversion_determinant]; norm_num) ht
    (by norm_num [inversion]) hy]
  simp only [circleEquation, inversion_radius]
  simp [inversion]

theorem pullback_point_duality {X Y : Type*} (f : X → Y) (S : Set Y) (x : X) :
    x ∈ f ⁻¹' S ↔ f x ∈ S := Iff.rfl

theorem chronological_pullback {X : Type*} (P Q : X → X) (S : Set X) :
    (P ∘ Q) ⁻¹' S = Q ⁻¹' (P ⁻¹' S) := rfl

end
end AEGPaper0.Chapter04Ripples

#print axioms AEGPaper0.Chapter04Ripples.denominator_normSq
#print axioms AEGPaper0.Chapter04Ripples.denominator_ne_zero
#print axioms AEGPaper0.Chapter04Ripples.denominatorSq_positive
#print axioms AEGPaper0.Chapter04Ripples.mobius_imaginary
#print axioms AEGPaper0.Chapter04Ripples.mobius_preserves_upper
#print axioms AEGPaper0.Chapter04Ripples.ripple_membership
#print axioms AEGPaper0.Chapter04Ripples.ripple_level
#print axioms AEGPaper0.Chapter04Ripples.ripple_equation
#print axioms AEGPaper0.Chapter04Ripples.affine_diagonal_nonzero
#print axioms AEGPaper0.Chapter04Ripples.affine_ripple_line
#print axioms AEGPaper0.Chapter04Ripples.radius_positive
#print axioms AEGPaper0.Chapter04Ripples.completed_square
#print axioms AEGPaper0.Chapter04Ripples.ripple_circle
#print axioms AEGPaper0.Chapter04Ripples.circle_boundary_contact
#print axioms AEGPaper0.Chapter04Ripples.circle_height_bounds
#print axioms AEGPaper0.Chapter04Ripples.radius_antitone
#print axioms AEGPaper0.Chapter04Ripples.tangentDisk_equation
#print axioms AEGPaper0.Chapter04Ripples.tangentDisk_height_nonnegative
#print axioms AEGPaper0.Chapter04Ripples.tangentDisk_nested
#print axioms AEGPaper0.Chapter04Ripples.ripple_disks_nested
#print axioms AEGPaper0.Chapter04Ripples.distinct_ripples_disjoint
#print axioms AEGPaper0.Chapter04Ripples.ripple_parameter_positive
#print axioms AEGPaper0.Chapter04Ripples.ripple_empty_nonpositive
#print axioms AEGPaper0.Chapter04Ripples.ripple_unique_positive_level
#print axioms AEGPaper0.Chapter04Ripples.output_translation_determinant
#print axioms AEGPaper0.Chapter04Ripples.output_translation_map
#print axioms AEGPaper0.Chapter04Ripples.output_translation_pole
#print axioms AEGPaper0.Chapter04Ripples.output_translation_ripple
#print axioms AEGPaper0.Chapter04Ripples.inversion_determinant
#print axioms AEGPaper0.Chapter04Ripples.inversion_map
#print axioms AEGPaper0.Chapter04Ripples.inversion_radius
#print axioms AEGPaper0.Chapter04Ripples.inversion_pole
#print axioms AEGPaper0.Chapter04Ripples.inversion_followed_by_translation_has_same_finite_pole
#print axioms AEGPaper0.Chapter04Ripples.inversion_ripple
#print axioms AEGPaper0.Chapter04Ripples.pullback_point_duality
#print axioms AEGPaper0.Chapter04Ripples.chronological_pullback
