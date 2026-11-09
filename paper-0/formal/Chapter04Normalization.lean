import Chapter03Analysis
import Chapter04Ripples

/- Original CC0 proofs by Codex (OpenAI), 2026-11-09.
   Actual chart derivatives and pullback of the standard metric tensor.
   The factor lambda^-2 is retained. No curvature, completeness, intrinsic
   horocycle or ideal-boundary theorem is inferred from these coordinates. -/
noncomputable section
namespace AEGPaper0.Chapter04Normalization

open Chapter03Analysis
open ContinuousLinearMap
open scoped ContDiff

def normalize (mu lambda : ℝ) (p : Plane) : Plane := (lambda / mu * p.1, p.2)
def chart (mu lambda : ℝ) (p : Plane) : ℂ := ⟨(normalize mu lambda p).1, p.2⟩
def chartDerivative (mu lambda : ℝ) : Plane →L[ℝ] Plane :=
  ((lambda / mu) • fst ℝ ℝ ℝ).prod (snd ℝ ℝ ℝ)
def standardMetric (p v w : Plane) : ℝ := (v.1*w.1 + v.2*w.2) / p.2^2

theorem normalize_height (mu lambda : ℝ) (p : Plane) : (normalize mu lambda p).2=p.2 := rfl

theorem normalize_preserves_upper (mu lambda : ℝ) (p : Plane) :
    normalize mu lambda p ∈ Chapter03Analysis.upper ↔ p ∈ Chapter03Analysis.upper := Iff.rfl

theorem normalize_inverse (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) (p : Plane) :
    normalize lambda mu (normalize mu lambda p)=p := by
  apply Prod.ext
  · simp only [normalize]; field_simp
  · rfl

def normalizationEquiv (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) : Plane ≃ Plane where
  toFun := normalize mu lambda
  invFun := normalize lambda mu
  left_inv := normalize_inverse mu lambda hm hl
  right_inv := normalize_inverse lambda mu hl hm

theorem normalize_bijective (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) :
    Function.Bijective (normalize mu lambda) := (normalizationEquiv mu lambda hm hl).bijective

theorem normalize_smooth (mu lambda : ℝ) : ContDiff ℝ ∞ (normalize mu lambda) := by
  unfold normalize
  fun_prop

theorem chart_derivative_apply (mu lambda : ℝ) (v : Plane) :
    chartDerivative mu lambda v=normalize mu lambda v := rfl

theorem normalize_hasFDerivAt (mu lambda : ℝ) (p : Plane) :
    HasFDerivAt (normalize mu lambda) (chartDerivative mu lambda) p := by
  exact ((hasFDerivAt_fst (𝕜 := ℝ) (p := p)).const_mul (lambda / mu)).prodMk
    (hasFDerivAt_snd (𝕜 := ℝ) (p := p))

theorem normalize_fderiv (mu lambda : ℝ) (p v : Plane) :
    fderiv ℝ (normalize mu lambda) p v=normalize mu lambda v := by
  rw [(normalize_hasFDerivAt mu lambda p).fderiv, chart_derivative_apply]

theorem standard_metric_is_unit_model (p v w : Plane) :
    standardMetric p v w=Chapter03Coordinates.metric 1 1 p v w := by
  simp [standardMetric, Chapter03Coordinates.metric, add_div]

theorem metric_pullback (mu lambda : ℝ) (p v w : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Coordinates.metric mu lambda p v w =
      standardMetric (normalize mu lambda p)
        (fderiv ℝ (normalize mu lambda) p v) (fderiv ℝ (normalize mu lambda) p w) / lambda^2 := by
  simp only [normalize_fderiv, standardMetric, normalize]
  exact Chapter03Coordinates.scaled_standard_metric mu lambda p v w hm hl hy

theorem tensor_pullback (mu lambda : ℝ) (p v w : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    metricTensor mu lambda p v w =
      standardMetric (normalize mu lambda p)
        (fderiv ℝ (normalize mu lambda) p v) (fderiv ℝ (normalize mu lambda) p w) / lambda^2 := by
  rw [metric_tensor_apply]
  exact metric_pullback mu lambda p v w hm hl hy

theorem normalized_metric_scale (mu lambda : ℝ) (p v w : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    standardMetric (normalize mu lambda p) (normalize mu lambda v) (normalize mu lambda w) =
      lambda^2 * metricTensor mu lambda p v w := by
  rw [tensor_pullback mu lambda p v w hm hl hy]
  simp only [normalize_fderiv]
  field_simp

theorem equal_intensities_identity (mu : ℝ) (hm : mu ≠ 0) (p : Plane) : normalize mu mu p=p := by
  simp [normalize, div_self hm]

theorem chart_real_imag (mu lambda : ℝ) (p : Plane) :
    (chart mu lambda p).re=lambda / mu * p.1 ∧ (chart mu lambda p).im=p.2 := ⟨rfl,rfl⟩

theorem chart_upper (mu lambda : ℝ) (p : Plane) :
    chart mu lambda p ∈ Chapter04Ripples.upper ↔ p ∈ Chapter03Analysis.upper := Iff.rfl

theorem chart_horizontal_leaf (mu lambda t : ℝ) (p : Plane) :
    chart mu lambda p ∈ Chapter04Ripples.horocycle t ↔ 0 < p.2 ∧ p.2=t := Iff.rfl

theorem ripple_in_original_coordinates (mu lambda : ℝ) (m : Chapter04Ripples.Coefficients)
    (t : ℝ) (p : Plane) (hd : 0 < Chapter04Ripples.determinant m) (ht : 0 < t)
    (hc : m.c ≠ 0) (hp : p ∈ Chapter03Analysis.upper) :
    chart mu lambda p ∈ Chapter04Ripples.ripple m t ↔
      (lambda / mu * p.1 + m.d/m.c)^2 + (p.2 - Chapter04Ripples.radius m t)^2 =
        (Chapter04Ripples.radius m t)^2 :=
  Chapter04Ripples.ripple_circle m t (chart mu lambda p) hd ht hc hp

theorem original_boundary_contact (mu lambda : ℝ) (m : Chapter04Ripples.Coefficients)
    (t x : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) :
    Chapter04Ripples.circleEquation m t (lambda / mu * x) 0 ↔
      x=mu / lambda * Chapter04Ripples.poleX m := by
  rw [Chapter04Ripples.circle_boundary_contact]
  constructor
  · intro h
    calc x = mu / lambda * (lambda / mu * x) := by field_simp
         _ = _ := by rw [h]
  · intro h; rw [h]; field_simp

#print axioms AEGPaper0.Chapter04Normalization.normalize_height
#print axioms AEGPaper0.Chapter04Normalization.normalize_preserves_upper
#print axioms AEGPaper0.Chapter04Normalization.normalize_inverse
#print axioms AEGPaper0.Chapter04Normalization.normalize_bijective
#print axioms AEGPaper0.Chapter04Normalization.normalize_smooth
#print axioms AEGPaper0.Chapter04Normalization.chart_derivative_apply
#print axioms AEGPaper0.Chapter04Normalization.normalize_hasFDerivAt
#print axioms AEGPaper0.Chapter04Normalization.normalize_fderiv
#print axioms AEGPaper0.Chapter04Normalization.standard_metric_is_unit_model
#print axioms AEGPaper0.Chapter04Normalization.metric_pullback
#print axioms AEGPaper0.Chapter04Normalization.tensor_pullback
#print axioms AEGPaper0.Chapter04Normalization.normalized_metric_scale
#print axioms AEGPaper0.Chapter04Normalization.equal_intensities_identity
#print axioms AEGPaper0.Chapter04Normalization.chart_real_imag
#print axioms AEGPaper0.Chapter04Normalization.chart_upper
#print axioms AEGPaper0.Chapter04Normalization.chart_horizontal_leaf
#print axioms AEGPaper0.Chapter04Normalization.ripple_in_original_coordinates
#print axioms AEGPaper0.Chapter04Normalization.original_boundary_contact
end AEGPaper0.Chapter04Normalization
