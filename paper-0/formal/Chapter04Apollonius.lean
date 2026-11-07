import Chapter04Ripples
import Mathlib.Analysis.Complex.Norm

/- Original CC0 continuation by Codex (OpenAI), 2026-11-07.
   Actual complex norms in the declared continuation chart. The pole is
   excluded before clearing a denominator. Proper circles require positive
   level/weight and distinct foci; zero and negative parameters are separate.
   No intrinsic hyperbolic or PGL identification is asserted. -/
namespace AEGPaper0.Chapter04Apollonius

noncomputable section
open Chapter04Ripples

def zeroX (m : Coefficients) : ℝ := -m.b / m.a
def weight (m : Coefficients) (r : ℝ) : ℝ := r * |m.c / m.a|
def weightedLocus (q p k : ℝ) : Set ℂ := {z | ‖z - (q : ℂ)‖ = k * ‖z - (p : ℂ)‖}
def levelSet (m : Coefficients) (r : ℝ) : Set ℂ :=
  {z | denominator m z ≠ 0 ∧ ‖mobius m z‖ = r}
def center (q p k : ℝ) : ℝ := (q - k^2 * p) / (1 - k^2)
def radiusSq (q p k : ℝ) : ℝ := k^2 * (q - p)^2 / (1 - k^2)^2
def circleRadius (q p k : ℝ) : ℝ := Real.sqrt (radiusSq q p k)

theorem norm_shift_square (z : ℂ) (q : ℝ) :
    ‖z - (q : ℂ)‖^2 = (z.re - q)^2 + z.im^2 := by
  rw [Complex.sq_norm, Complex.normSq_apply]
  simp
  ring

theorem numerator_factor (m : Coefficients) (z : ℂ) (ha : m.a ≠ 0) :
    (m.a : ℂ) * z + m.b = m.a * (z - (zeroX m : ℂ)) := by
  have h : (m.a : ℂ) ≠ 0 := by exact_mod_cast ha
  unfold zeroX
  push_cast
  field_simp
  ring

theorem denominator_factor (m : Coefficients) (z : ℂ) (hc : m.c ≠ 0) :
    denominator m z = m.c * (z - (poleX m : ℂ)) := by
  have h : (m.c : ℂ) ≠ 0 := by exact_mod_cast hc
  unfold denominator poleX
  push_cast
  field_simp
  ring

theorem zero_pole_distinct (m : Coefficients) (ha : m.a ≠ 0) (hc : m.c ≠ 0)
    (hd : determinant m ≠ 0) : zeroX m ≠ poleX m := by
  intro h
  unfold zeroX poleX at h
  field_simp at h
  exact hd (by unfold determinant; linarith [h])

theorem denominator_nonzero_iff (m : Coefficients) (z : ℂ) (hc : m.c ≠ 0) :
    denominator m z ≠ 0 ↔ z ≠ (poleX m : ℂ) := by
  rw [denominator_factor m z hc]
  have h : (m.c : ℂ) ≠ 0 := by exact_mod_cast hc
  simp [h, sub_ne_zero]

theorem norm_mobius_factor (m : Coefficients) (z : ℂ) (ha : m.a ≠ 0) (hc : m.c ≠ 0) :
    ‖mobius m z‖ = |m.a| * ‖z - (zeroX m : ℂ)‖ / (|m.c| * ‖z - (poleX m : ℂ)‖) := by
  unfold mobius
  rw [numerator_factor m z ha, denominator_factor m z hc]
  simp only [norm_div, norm_mul, Complex.norm_real, Real.norm_eq_abs]

theorem norm_level_apollonius (m : Coefficients) (r : ℝ) (z : ℂ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hz : z ≠ (poleX m : ℂ)) :
    ‖mobius m z‖ = r ↔ z ∈ weightedLocus (zeroX m) (poleX m) (weight m r) := by
  have ha' : |m.a| ≠ 0 := abs_ne_zero.mpr ha
  have hc' : |m.c| ≠ 0 := abs_ne_zero.mpr hc
  have hz' : ‖z - (poleX m : ℂ)‖ ≠ 0 := norm_ne_zero_iff.mpr (sub_ne_zero.mpr hz)
  rw [norm_mobius_factor m z ha hc]
  change _ ↔ _ = _
  unfold weight
  rw [abs_div]
  field_simp

theorem positive_weight (m : Coefficients) (r : ℝ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hr : 0 < r) : 0 < weight m r := by
  exact mul_pos hr (abs_pos.mpr (div_ne_zero hc ha))

theorem nonnegative_weight (m : Coefficients) (r : ℝ) (hr : 0 ≤ r) : 0 ≤ weight m r := by
  exact mul_nonneg hr (abs_nonneg _)

theorem pole_not_in_weighted_locus (q p k : ℝ) (hqp : q ≠ p) :
    (p : ℂ) ∉ weightedLocus q p k := by
  simp only [weightedLocus, Set.mem_setOf_eq, sub_self, norm_zero, mul_zero, norm_eq_zero,
    sub_eq_zero, Complex.ofReal_inj]
  exact Ne.symm hqp

theorem levelSet_is_weighted_locus (m : Coefficients) (r : ℝ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hd : determinant m ≠ 0) :
    levelSet m r = weightedLocus (zeroX m) (poleX m) (weight m r) := by
  ext z
  constructor
  · intro h
    exact (norm_level_apollonius m r z ha hc ((denominator_nonzero_iff m z hc).mp h.1)).mp h.2
  · intro h
    have hz : z ≠ (poleX m : ℂ) := by
      intro he; subst z
      exact pole_not_in_weighted_locus _ _ _ (zero_pole_distinct m ha hc hd) h
    exact ⟨(denominator_nonzero_iff m z hc).mpr hz, (norm_level_apollonius m r z ha hc hz).mpr h⟩

theorem weighted_squared_equation (q p k : ℝ) (z : ℂ) (hk : 0 ≤ k) :
    z ∈ weightedLocus q p k ↔
      (z.re - q)^2 + z.im^2 = k^2 * ((z.re - p)^2 + z.im^2) := by
  change ‖z - (q : ℂ)‖ = k * ‖z - (p : ℂ)‖ ↔ _
  rw [← sq_eq_sq₀ (norm_nonneg _) (mul_nonneg hk (norm_nonneg _)), mul_pow,
    norm_shift_square, norm_shift_square]

theorem nonunit_square_denominator (k : ℝ) (hk : 0 ≤ k) (hunit : k ≠ 1) : 1 - k^2 ≠ 0 := by
  intro h
  have hs : k^2 = (1 : ℝ)^2 := by linarith [h]
  exact hunit ((sq_eq_sq₀ hk (by norm_num)).mp hs)

theorem completed_square (q p k x y : ℝ) (hden : 1 - k^2 ≠ 0) :
    (x - q)^2 + y^2 = k^2 * ((x - p)^2 + y^2) ↔
      (x - center q p k)^2 + y^2 = radiusSq q p k := by
  have he : (x - center q p k)^2 + y^2 - radiusSq q p k =
      ((x - q)^2 + y^2 - k^2 * ((x - p)^2 + y^2)) / (1 - k^2) := by
    unfold center radiusSq
    field_simp
    ring
  conv_rhs => rw [← sub_eq_zero, he, div_eq_zero_iff]
  simp only [hden, or_false]
  constructor <;> intro h <;> linarith [h]

theorem weighted_circle_equation (q p k : ℝ) (z : ℂ) (hk : 0 ≤ k) (hunit : k ≠ 1) :
    z ∈ weightedLocus q p k ↔ (z.re - center q p k)^2 + z.im^2 = radiusSq q p k := by
  rw [weighted_squared_equation q p k z hk]
  exact completed_square q p k z.re z.im (nonunit_square_denominator k hk hunit)

theorem radiusSq_nonnegative (q p k : ℝ) : 0 ≤ radiusSq q p k := by
  unfold radiusSq; positivity

theorem radiusSq_positive (q p k : ℝ) (hqp : q ≠ p) (hk : 0 < k) (hunit : k ≠ 1) :
    0 < radiusSq q p k := by
  unfold radiusSq
  exact div_pos (mul_pos (sq_pos_of_pos hk) (sq_pos_of_ne_zero (sub_ne_zero.mpr hqp)))
    (sq_pos_of_ne_zero (nonunit_square_denominator k (le_of_lt hk) hunit))

theorem circleRadius_square (q p k : ℝ) : (circleRadius q p k)^2 = radiusSq q p k := by
  exact Real.sq_sqrt (radiusSq_nonnegative q p k)

theorem circleRadius_positive (q p k : ℝ) (hqp : q ≠ p) (hk : 0 < k) (hunit : k ≠ 1) :
    0 < circleRadius q p k := by
  exact Real.sqrt_pos.mpr (radiusSq_positive q p k hqp hk hunit)

theorem weighted_locus_is_metric_circle (q p k : ℝ) (hk : 0 ≤ k) (hunit : k ≠ 1) :
    weightedLocus q p k = Metric.sphere (center q p k : ℂ) (circleRadius q p k) := by
  ext z
  rw [weighted_circle_equation q p k z hk hunit]
  change _ ↔ dist z (center q p k : ℂ) = circleRadius q p k
  rw [dist_eq_norm]
  have hr : 0 ≤ circleRadius q p k := Real.sqrt_nonneg _
  rw [← sq_eq_sq₀ (norm_nonneg _) hr, norm_shift_square, circleRadius_square]

theorem unit_weight_equidistance (q p : ℝ) (z : ℂ) :
    z ∈ weightedLocus q p 1 ↔ dist z (q : ℂ) = dist z (p : ℂ) := by
  simp only [weightedLocus, Set.mem_setOf_eq, one_mul, dist_eq_norm]

theorem unit_weight_bisector (q p : ℝ) (z : ℂ) (hqp : q ≠ p) :
    z ∈ weightedLocus q p 1 ↔ z.re = (q + p) / 2 := by
  rw [weighted_squared_equation q p 1 z (by norm_num)]
  constructor
  · intro h
    have he : (q - p) * (2 * z.re - (q + p)) = 0 := by nlinarith [h]
    have hz := (mul_eq_zero.mp he).resolve_left (sub_ne_zero.mpr hqp)
    linarith [hz]
  · intro h; rw [h]; ring

theorem unit_locus_is_bisector_line (q p : ℝ) (hqp : q ≠ p) :
    weightedLocus q p 1 = {z : ℂ | z.re = (q + p) / 2} := by
  ext z; exact unit_weight_bisector q p z hqp

theorem zero_weight_singleton (q p : ℝ) : weightedLocus q p 0 = {(q : ℂ)} := by
  ext z
  simp [weightedLocus, sub_eq_zero]

theorem negative_weight_empty (q p k : ℝ) (hqp : q ≠ p) (hk : k < 0) :
    weightedLocus q p k = ∅ := by
  apply Set.eq_empty_iff_forall_notMem.mpr
  intro z hz
  have hzp : z ≠ (p : ℂ) := by
    intro he; subst z; exact pole_not_in_weighted_locus q p k hqp hz
  have hp : 0 < ‖z - (p : ℂ)‖ := norm_pos_iff.mpr (sub_ne_zero.mpr hzp)
  have he : ‖z - (q : ℂ)‖ = k * ‖z - (p : ℂ)‖ := hz
  nlinarith [norm_nonneg (z - (q : ℂ)), mul_neg_of_neg_of_pos hk hp]

theorem equal_foci_unit_locus (q : ℝ) : weightedLocus q q 1 = Set.univ := by
  ext z; simp [weightedLocus]

theorem negative_level_empty (m : Coefficients) (r : ℝ) (hr : r < 0) : levelSet m r = ∅ := by
  apply Set.eq_empty_iff_forall_notMem.mpr
  intro z hz
  have h : 0 ≤ ‖mobius m z‖ := norm_nonneg _
  rw [hz.2] at h
  exact (not_le_of_gt hr) h

theorem zero_level_singleton (m : Coefficients) (ha : m.a ≠ 0) (hc : m.c ≠ 0)
    (hd : determinant m ≠ 0) : levelSet m 0 = {(zeroX m : ℂ)} := by
  rw [levelSet_is_weighted_locus m 0 ha hc hd]
  simp only [weight, zero_mul]
  exact zero_weight_singleton _ _

theorem upper_zero_level_empty (m : Coefficients) (ha : m.a ≠ 0) (hc : m.c ≠ 0)
    (hd : determinant m ≠ 0) : upper ∩ levelSet m 0 = ∅ := by
  rw [zero_level_singleton m ha hc hd]
  apply Set.eq_empty_iff_forall_notMem.mpr
  intro z hz
  have he : z = (zeroX m : ℂ) := Set.mem_singleton_iff.mp hz.2
  have hy := hz.1
  rw [he] at hy
  simp [upper] at hy

theorem mobius_level_is_metric_circle (m : Coefficients) (r : ℝ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hd : determinant m ≠ 0)
    (hr : 0 ≤ r) (hunit : weight m r ≠ 1) :
    levelSet m r = Metric.sphere (center (zeroX m) (poleX m) (weight m r) : ℂ)
      (circleRadius (zeroX m) (poleX m) (weight m r)) := by
  rw [levelSet_is_weighted_locus m r ha hc hd]
  exact weighted_locus_is_metric_circle _ _ _ (nonnegative_weight m r hr) hunit

theorem mobius_circle_radius_positive (m : Coefficients) (r : ℝ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hd : determinant m ≠ 0)
    (hr : 0 < r) (hunit : weight m r ≠ 1) :
    0 < circleRadius (zeroX m) (poleX m) (weight m r) := by
  exact circleRadius_positive _ _ _ (zero_pole_distinct m ha hc hd) (positive_weight m r ha hc hr) hunit

theorem mobius_unit_level_is_bisector (m : Coefficients) (r : ℝ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hd : determinant m ≠ 0) (hunit : weight m r = 1) :
    levelSet m r = {z : ℂ | z.re = (zeroX m + poleX m) / 2} := by
  rw [levelSet_is_weighted_locus m r ha hc hd, hunit]
  exact unit_locus_is_bisector_line _ _ (zero_pole_distinct m ha hc hd)

theorem circleRadius_formula (q p k : ℝ) :
    circleRadius q p k = |k| * |q - p| / |1 - k^2| := by
  unfold circleRadius radiusSq
  rw [Real.sqrt_div (mul_nonneg (sq_nonneg _) (sq_nonneg _)),
    Real.sqrt_mul (sq_nonneg _), Real.sqrt_sq_eq_abs, Real.sqrt_sq_eq_abs, Real.sqrt_sq_eq_abs]

theorem circle_upper_witness (q p k : ℝ) (hqp : q ≠ p) (hk : 0 < k) (hunit : k ≠ 1) :
    ∃ z : ℂ, z ∈ upper ∧ z ∈ weightedLocus q p k := by
  refine ⟨⟨center q p k, circleRadius q p k⟩, ?_, ?_⟩
  · exact circleRadius_positive q p k hqp hk hunit
  · rw [weighted_circle_equation q p k _ (le_of_lt hk) hunit]
    change (center q p k - center q p k)^2 + (circleRadius q p k)^2 = radiusSq q p k
    rw [sub_self, zero_pow (by decide : 2 ≠ 0), zero_add, circleRadius_square]

theorem unit_upper_witness (q p : ℝ) (hqp : q ≠ p) :
    ∃ z : ℂ, z ∈ upper ∧ z ∈ weightedLocus q p 1 := by
  refine ⟨⟨(q + p) / 2, 1⟩, by norm_num [upper], ?_⟩
  exact (unit_weight_bisector q p _ hqp).mpr rfl

theorem totalized_pole_value (m : Coefficients) (hc : m.c ≠ 0) :
    mobius m (poleX m : ℂ) = 0 := by
  unfold mobius
  rw [denominator_factor m _ hc]
  simp

theorem unguarded_zero_level_at_pole_fails (m : Coefficients)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hd : determinant m ≠ 0) :
    ‖mobius m (poleX m : ℂ)‖ = 0 ∧
      (poleX m : ℂ) ∉ weightedLocus (zeroX m) (poleX m) (weight m 0) := by
  exact ⟨by rw [totalized_pole_value m hc, norm_zero],
    pole_not_in_weighted_locus _ _ _ (zero_pole_distinct m ha hc hd)⟩

theorem negative_unit_weight_is_not_bisector (q p : ℝ) (hqp : q ≠ p) :
    weightedLocus q p (-1) = ∅ ∧ weightedLocus q p 1 ≠ ∅ := by
  refine ⟨negative_weight_empty q p (-1) hqp (by norm_num), ?_⟩
  obtain ⟨z, _, hz⟩ := unit_upper_witness q p hqp
  exact Set.nonempty_iff_ne_empty.mp ⟨z, hz⟩

theorem positive_level_upper_nonempty (m : Coefficients) (r : ℝ)
    (ha : m.a ≠ 0) (hc : m.c ≠ 0) (hd : determinant m ≠ 0) (hr : 0 < r) :
    (upper ∩ levelSet m r).Nonempty := by
  rw [levelSet_is_weighted_locus m r ha hc hd]
  have hqp := zero_pole_distinct m ha hc hd
  by_cases hunit : weight m r = 1
  · rw [hunit]
    obtain ⟨z, hy, hz⟩ := unit_upper_witness _ _ hqp
    exact ⟨z, hy, hz⟩
  · obtain ⟨z, hy, hz⟩ := circle_upper_witness _ _ _ hqp (positive_weight m r ha hc hr) hunit
    exact ⟨z, hy, hz⟩

end
end AEGPaper0.Chapter04Apollonius

#print axioms AEGPaper0.Chapter04Apollonius.norm_shift_square
#print axioms AEGPaper0.Chapter04Apollonius.numerator_factor
#print axioms AEGPaper0.Chapter04Apollonius.denominator_factor
#print axioms AEGPaper0.Chapter04Apollonius.zero_pole_distinct
#print axioms AEGPaper0.Chapter04Apollonius.denominator_nonzero_iff
#print axioms AEGPaper0.Chapter04Apollonius.norm_mobius_factor
#print axioms AEGPaper0.Chapter04Apollonius.norm_level_apollonius
#print axioms AEGPaper0.Chapter04Apollonius.positive_weight
#print axioms AEGPaper0.Chapter04Apollonius.nonnegative_weight
#print axioms AEGPaper0.Chapter04Apollonius.pole_not_in_weighted_locus
#print axioms AEGPaper0.Chapter04Apollonius.levelSet_is_weighted_locus
#print axioms AEGPaper0.Chapter04Apollonius.weighted_squared_equation
#print axioms AEGPaper0.Chapter04Apollonius.nonunit_square_denominator
#print axioms AEGPaper0.Chapter04Apollonius.completed_square
#print axioms AEGPaper0.Chapter04Apollonius.weighted_circle_equation
#print axioms AEGPaper0.Chapter04Apollonius.radiusSq_nonnegative
#print axioms AEGPaper0.Chapter04Apollonius.radiusSq_positive
#print axioms AEGPaper0.Chapter04Apollonius.circleRadius_square
#print axioms AEGPaper0.Chapter04Apollonius.circleRadius_positive
#print axioms AEGPaper0.Chapter04Apollonius.weighted_locus_is_metric_circle
#print axioms AEGPaper0.Chapter04Apollonius.unit_weight_equidistance
#print axioms AEGPaper0.Chapter04Apollonius.unit_weight_bisector
#print axioms AEGPaper0.Chapter04Apollonius.unit_locus_is_bisector_line
#print axioms AEGPaper0.Chapter04Apollonius.zero_weight_singleton
#print axioms AEGPaper0.Chapter04Apollonius.negative_weight_empty
#print axioms AEGPaper0.Chapter04Apollonius.equal_foci_unit_locus
#print axioms AEGPaper0.Chapter04Apollonius.negative_level_empty
#print axioms AEGPaper0.Chapter04Apollonius.zero_level_singleton
#print axioms AEGPaper0.Chapter04Apollonius.upper_zero_level_empty
#print axioms AEGPaper0.Chapter04Apollonius.mobius_level_is_metric_circle
#print axioms AEGPaper0.Chapter04Apollonius.mobius_circle_radius_positive
#print axioms AEGPaper0.Chapter04Apollonius.mobius_unit_level_is_bisector
#print axioms AEGPaper0.Chapter04Apollonius.circleRadius_formula
#print axioms AEGPaper0.Chapter04Apollonius.circle_upper_witness
#print axioms AEGPaper0.Chapter04Apollonius.unit_upper_witness
#print axioms AEGPaper0.Chapter04Apollonius.totalized_pole_value
#print axioms AEGPaper0.Chapter04Apollonius.unguarded_zero_level_at_pole_fails
#print axioms AEGPaper0.Chapter04Apollonius.negative_unit_weight_is_not_bisector
#print axioms AEGPaper0.Chapter04Apollonius.positive_level_upper_nonempty
