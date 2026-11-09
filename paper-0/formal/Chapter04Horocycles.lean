import Chapter04Ripples
import Mathlib.Analysis.Complex.UpperHalfPlane.Metric

/- Original CC0 proofs by Codex (OpenAI), 2026-11-09.
   Horospheres are level sets of actual Poincare-distance Busemann limits.
   The reference rays and their isometries are constructed, not assumed. -/
noncomputable section
namespace AEGPaper0.Chapter04Horocycles
open Filter Real
open scoped UpperHalfPlane Topology MatrixGroups

def vertical (a s : ℝ) : ℍ := UpperHalfPlane.mk ⟨a, exp s⟩ (exp_pos s)

theorem vertical_isometry (a : ℝ) : Isometry (vertical a) :=
  UpperHalfPlane.isometry_vertical_line a

theorem horizontal_gap_bound (a b s : ℝ) :
    dist (vertical a s) (vertical b s) ≤ |a-b| / exp s := by
  have h := UpperHalfPlane.dist_le_dist_coe_div_sqrt (vertical a s) (vertical b s)
  have he : dist (vertical a s : ℂ) (vertical b s : ℂ)=|a-b| := by
    simpa only [Real.dist_eq] using (Complex.dist_of_im_eq
      (z := (vertical a s : ℂ)) (w := (vertical b s : ℂ)) rfl)
  rw [he] at h
  simpa only [vertical, UpperHalfPlane.mk_im, UpperHalfPlane.coe_mk,
    Real.sqrt_mul_self (le_of_lt (exp_pos s))] using h

theorem horizontal_gap_tends_zero (a b : ℝ) :
    Tendsto (fun s => dist (vertical a s) (vertical b s)) atTop (𝓝 0) := by
  apply squeeze_zero (fun _ => dist_nonneg) (horizontal_gap_bound a b)
  simpa using tendsto_const_nhds.div_atTop tendsto_exp_atTop

theorem vertical_distance_eventually (z : ℍ) :
    ∀ᶠ s in atTop, dist z (vertical z.re s)-s = -log z.im := by
  filter_upwards [eventually_ge_atTop (log z.im)] with s hs
  rw [UpperHalfPlane.dist_of_re_eq (by rfl), Real.dist_eq]
  simp only [vertical, UpperHalfPlane.mk_im, Real.log_exp]
  rw [abs_of_nonpos (sub_nonpos.mpr hs)]
  ring

def infinityBusemann (z : ℍ) : ℝ := -log z.im

theorem infinity_busemann_limit (z : ℍ) :
    Tendsto (fun s => dist z (vertical 0 s)-s) atTop (𝓝 (infinityBusemann z)) := by
  have hv : Tendsto (fun s => dist z (vertical z.re s)-s) atTop (𝓝 (infinityBusemann z)) :=
    tendsto_const_nhds.congr' ((vertical_distance_eventually z).mono (fun _ h => h.symm))
  apply hv.congr_dist
  apply squeeze_zero (fun _ => dist_nonneg) (fun s => ?_) (horizontal_gap_tends_zero z.re 0)
  simpa only [Real.dist_eq, sub_sub_sub_cancel_right, dist_comm z] using
    abs_dist_sub_le (vertical z.re s) (vertical 0 s) z

theorem infinity_busemann_reference_independent (a : ℝ) (z : ℍ) :
    Tendsto (fun s => dist z (vertical a s)-s) atTop (𝓝 (infinityBusemann z)) := by
  apply (infinity_busemann_limit z).congr_dist
  apply squeeze_zero (fun _ => dist_nonneg) (fun s => ?_) (horizontal_gap_tends_zero 0 a)
  simpa only [Real.dist_eq, sub_sub_sub_cancel_right, dist_comm z] using
    abs_dist_sub_le (vertical 0 s) (vertical a s) z

theorem infinity_busemann_lipschitz : LipschitzWith 1 infinityBusemann := by
  apply LipschitzWith.of_dist_le_mul
  intro z w
  simpa only [infinityBusemann, dist_neg_neg, NNReal.coe_one, one_mul] using
    UpperHalfPlane.dist_log_im_le z w

def flipMatrix : SL(2, ℝ) := ⟨!![0,-1;1,0], by norm_num [Matrix.det_fin_two]⟩
def flip (z : ℍ) : ℍ := flipMatrix • z

theorem flip_complex (z : ℍ) : (flip z : ℂ) = -1 / (z : ℂ) := by
  simp [flip, UpperHalfPlane.coe_specialLinearGroup_apply, flipMatrix]

theorem flip_isometry : Isometry flip := isometry_smul ℍ flipMatrix

theorem flip_involutive (z : ℍ) : flip (flip z)=z := by
  apply UpperHalfPlane.ext
  rw [flip_complex, flip_complex]
  field_simp

def gauge (q : ℝ) (z : ℍ) : ℍ := flip ((-q) +ᵥ z)
def ungauge (q : ℝ) (z : ℍ) : ℍ := q +ᵥ flip z

theorem gauge_isometry (q : ℝ) : Isometry (gauge q) :=
  flip_isometry.comp (UpperHalfPlane.isometry_real_vadd (-q))

theorem ungauge_gauge (q : ℝ) (z : ℍ) : ungauge q (gauge q z)=z := by
  simp [ungauge, gauge, flip_involutive, vadd_vadd]

theorem gauge_ungauge (q : ℝ) (z : ℍ) : gauge q (ungauge q z)=z := by
  simp [gauge, ungauge, vadd_vadd, flip_involutive]

def gaugeEquiv (q : ℝ) : ℍ ≃ᵢ ℍ where
  toFun := gauge q
  invFun := ungauge q
  left_inv := ungauge_gauge q
  right_inv := gauge_ungauge q
  isometry_toFun := gauge_isometry q

theorem gauge_imaginary (q : ℝ) (z : ℍ) :
    (gauge q z).im = z.im / ((z.re-q)^2+z.im^2) := by
  change (gauge q z : ℂ).im = _
  rw [gauge, flip_complex]
  simp [Complex.div_im, Complex.normSq_apply]
  ring

def finiteBusemann (q : ℝ) (z : ℍ) : ℝ := infinityBusemann (gauge q z)
def basedRay (q s : ℝ) : ℍ := (gaugeEquiv q).symm (vertical 0 s)

theorem based_ray_isometry (q : ℝ) : Isometry (basedRay q) :=
  (gaugeEquiv q).symm.isometry.comp (vertical_isometry 0)

theorem finite_busemann_limit (q : ℝ) (z : ℍ) :
    Tendsto (fun s => dist z (basedRay q s)-s) atTop (𝓝 (finiteBusemann q z)) := by
  have h := infinity_busemann_limit (gauge q z)
  convert h using 1
  funext s
  rw [← (gaugeEquiv q).isometry.dist_eq z (basedRay q s)]
  change dist (gauge q z) ((gaugeEquiv q) ((gaugeEquiv q).symm (vertical 0 s)))-s = _
  rw [IsometryEquiv.apply_symm_apply]

theorem based_ray_vertical (q s : ℝ) : basedRay q s=vertical q (-s) := by
  apply UpperHalfPlane.ext
  change (q +ᵥ flip (vertical 0 s) : ℂ) = _
  rw [UpperHalfPlane.coe_vadd, flip_complex]
  apply Complex.ext
  · simp [vertical, Complex.div_re, Complex.normSq_apply]
  · simp [vertical, Complex.div_im, Complex.normSq_apply, Real.exp_neg]
    field_simp

def infinityHorosphere (h : ℝ) : Set ℍ := {z | infinityBusemann z=h}
def finiteHorosphere (q h : ℝ) : Set ℍ := {z | finiteBusemann q z=h}

theorem finite_busemann_lipschitz (q : ℝ) : LipschitzWith 1 (finiteBusemann q) := by
  simpa only [one_mul] using infinity_busemann_lipschitz.comp (gauge_isometry q).lipschitz

theorem infinity_horosphere_closed (h : ℝ) : IsClosed (infinityHorosphere h) :=
  isClosed_eq infinity_busemann_lipschitz.continuous continuous_const

theorem finite_horosphere_closed (q h : ℝ) : IsClosed (finiteHorosphere q h) :=
  isClosed_eq (finite_busemann_lipschitz q).continuous continuous_const

theorem infinity_horosphere_nonempty (h : ℝ) : (infinityHorosphere h).Nonempty := by
  exact ⟨vertical 0 (-h), by simp [infinityHorosphere, infinityBusemann, vertical]⟩

theorem finite_horosphere_nonempty (q h : ℝ) : (finiteHorosphere q h).Nonempty := by
  refine ⟨(gaugeEquiv q).symm (vertical 0 (-h)),?_⟩
  change infinityBusemann ((gaugeEquiv q) ((gaugeEquiv q).symm (vertical 0 (-h))))=h
  rw [IsometryEquiv.apply_symm_apply]
  simp [infinityBusemann, vertical]

theorem infinity_horosphere_level (t : ℝ) (ht : 0 < t) (z : ℍ) :
    z ∈ infinityHorosphere (-log t) ↔ z.im=t := by
  simp only [infinityHorosphere, Set.mem_setOf_eq, infinityBusemann, neg_inj]
  exact ⟨fun h => Real.log_injOn_pos z.im_pos ht h, fun h => congrArg log h⟩

theorem finite_horosphere_level (q t : ℝ) (ht : 0 < t) (z : ℍ) :
    z ∈ finiteHorosphere q (-log t) ↔ (gauge q z).im=t := by
  exact infinity_horosphere_level t ht (gauge q z)

theorem finite_horosphere_circle (q t : ℝ) (ht : 0 < t) (z : ℍ) :
    z ∈ finiteHorosphere q (-log t) ↔
      (z.re-q)^2 + (z.im-1/(2*t))^2 = (1/(2*t))^2 := by
  rw [finite_horosphere_level q t ht z, gauge_imaginary]
  have hd : (z.re-q)^2+z.im^2 ≠ 0 := by nlinarith [sq_nonneg (z.re-q),sq_pos_of_pos z.im_pos]
  rw [div_eq_iff hd]
  have ht' := ne_of_gt ht
  constructor <;> intro h
  · field_simp; field_simp at h; nlinarith [h]
  · field_simp at h; nlinarith [h]

theorem affine_ripple_is_horosphere (m : Chapter04Ripples.Coefficients) (t : ℝ)
    (hd : 0 < Chapter04Ripples.determinant m) (ht : 0 < t) (hc : m.c=0) (z : ℍ) :
    (z : ℂ) ∈ Chapter04Ripples.ripple m t ↔
      z ∈ infinityHorosphere (-log (t*m.d^2/Chapter04Ripples.determinant m)) := by
  rw [Chapter04Ripples.affine_ripple_line m t z hd hc z.im_pos]
  exact (infinity_horosphere_level _ (by
    have hn := Chapter04Ripples.affine_diagonal_nonzero m (ne_of_gt hd) hc
    exact div_pos (mul_pos ht (sq_pos_of_ne_zero hn)) hd) z).symm

theorem nonaffine_ripple_is_horosphere (m : Chapter04Ripples.Coefficients) (t : ℝ)
    (hd : 0 < Chapter04Ripples.determinant m) (ht : 0 < t) (hc : m.c ≠ 0) (z : ℍ) :
    (z : ℂ) ∈ Chapter04Ripples.ripple m t ↔
      z ∈ finiteHorosphere (Chapter04Ripples.poleX m)
        (-log (t*m.c^2/Chapter04Ripples.determinant m)) := by
  rw [Chapter04Ripples.ripple_circle m t z hd ht hc z.im_pos,
    finite_horosphere_circle _ _ (div_pos (mul_pos ht (sq_pos_of_ne_zero hc)) hd) z]
  have hr : 1/(2*(t*m.c^2/Chapter04Ripples.determinant m))=Chapter04Ripples.radius m t := by
    unfold Chapter04Ripples.radius
    field_simp
  rw [hr]
  simp only [Chapter04Ripples.circleEquation, Chapter04Ripples.poleX, sub_neg_eq_add, neg_div,
    UpperHalfPlane.coe_re, UpperHalfPlane.coe_im]

#print axioms AEGPaper0.Chapter04Horocycles.vertical_isometry
#print axioms AEGPaper0.Chapter04Horocycles.horizontal_gap_bound
#print axioms AEGPaper0.Chapter04Horocycles.horizontal_gap_tends_zero
#print axioms AEGPaper0.Chapter04Horocycles.vertical_distance_eventually
#print axioms AEGPaper0.Chapter04Horocycles.infinity_busemann_limit
#print axioms AEGPaper0.Chapter04Horocycles.infinity_busemann_reference_independent
#print axioms AEGPaper0.Chapter04Horocycles.infinity_busemann_lipschitz
#print axioms AEGPaper0.Chapter04Horocycles.flip_complex
#print axioms AEGPaper0.Chapter04Horocycles.flip_isometry
#print axioms AEGPaper0.Chapter04Horocycles.flip_involutive
#print axioms AEGPaper0.Chapter04Horocycles.gauge_isometry
#print axioms AEGPaper0.Chapter04Horocycles.ungauge_gauge
#print axioms AEGPaper0.Chapter04Horocycles.gauge_ungauge
#print axioms AEGPaper0.Chapter04Horocycles.gauge_imaginary
#print axioms AEGPaper0.Chapter04Horocycles.based_ray_isometry
#print axioms AEGPaper0.Chapter04Horocycles.finite_busemann_limit
#print axioms AEGPaper0.Chapter04Horocycles.based_ray_vertical
#print axioms AEGPaper0.Chapter04Horocycles.finite_busemann_lipschitz
#print axioms AEGPaper0.Chapter04Horocycles.infinity_horosphere_closed
#print axioms AEGPaper0.Chapter04Horocycles.finite_horosphere_closed
#print axioms AEGPaper0.Chapter04Horocycles.infinity_horosphere_nonempty
#print axioms AEGPaper0.Chapter04Horocycles.finite_horosphere_nonempty
#print axioms AEGPaper0.Chapter04Horocycles.infinity_horosphere_level
#print axioms AEGPaper0.Chapter04Horocycles.finite_horosphere_level
#print axioms AEGPaper0.Chapter04Horocycles.finite_horosphere_circle
#print axioms AEGPaper0.Chapter04Horocycles.affine_ripple_is_horosphere
#print axioms AEGPaper0.Chapter04Horocycles.nonaffine_ripple_is_horosphere
end AEGPaper0.Chapter04Horocycles
