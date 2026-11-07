import Chapter03Analysis
import Mathlib.Analysis.SpecialFunctions.Sqrt

/- Original CC0 contribution by Codex (OpenAI), 2026-11-07.
   Positive smooth real square root and actual arsinh rectification. -/
noncomputable section
namespace AEGPaper0.Chapter03Rectification

open AEGPaper0.Chapter03Analysis
open scoped ContDiff

def q (mu lambda : ℝ) (p : Plane) : ℝ :=
  Real.sqrt (mu^2 + lambda^2 * Chapter03Coordinates.assignment p^2)

theorem q_positive (mu lambda : ℝ) (hm : mu ≠ 0) (p : Plane) : 0 < q mu lambda p := by
  apply Real.sqrt_pos.mpr
  exact Chapter03Coordinates.eikonal_rhs_positive mu lambda _ hm

theorem q_square (mu lambda : ℝ) (p : Plane) :
    q mu lambda p^2 = mu^2 + lambda^2 * Chapter03Coordinates.assignment p^2 := by
  exact Real.sq_sqrt (by positivity)

theorem q_smooth (mu lambda : ℝ) (hm : mu ≠ 0) : ContDiffOn ℝ ∞ (q mu lambda) upper := by
  apply (contDiffOn_const.add (contDiffOn_const.mul (assignment_smooth.pow 2))).sqrt
  intro p hp
  exact ne_of_gt (Chapter03Coordinates.eikonal_rhs_positive mu lambda _ hm)

theorem canonical_coefficient_frame_exists (mu lambda : ℝ) (hm : mu ≠ 0) (p : Plane) :
    Chapter03Coordinates.OrthonormalOriented
      (Chapter03Coordinates.canonicalFrame mu lambda (Chapter03Coordinates.assignment p) (q mu lambda p)) :=
  Chapter03Coordinates.canonical_frame_orthonormal mu lambda _ _
    (ne_of_gt (q_positive mu lambda hm p)) (q_square mu lambda p)

def rectifying (mu lambda : ℝ) (p : Plane) : ℝ :=
  Real.arsinh ((lambda / mu) * Chapter03Coordinates.assignment p)
def coefficient (mu lambda a : ℝ) : ℝ :=
  (Real.sqrt (1 + ((lambda / mu) * a)^2))⁻¹ * (lambda / mu)
def rectifiedGradient (mu lambda : ℝ) (p : Plane) : Plane :=
  coefficient mu lambda (Chapter03Coordinates.assignment p) • Chapter03Coordinates.gradientCandidate mu lambda p

theorem rectifying_smooth (mu lambda : ℝ) : ContDiffOn ℝ ∞ (rectifying mu lambda) upper := by
  exact (contDiffOn_const.mul assignment_smooth).arsinh

theorem rectifying_hasFDerivAt (mu lambda : ℝ) (p : Plane) (hy : p.2 ≠ 0) :
    HasFDerivAt (rectifying mu lambda)
      (coefficient mu lambda (Chapter03Coordinates.assignment p) • assignmentDerivative p) p := by
  convert ((assignment_hasFDerivAt p hy).const_mul (lambda / mu)).arsinh using 1
  simp only [coefficient, smul_smul]

theorem rectifying_fderiv_apply (mu lambda : ℝ) (p v : Plane) (hy : p.2 ≠ 0) :
    fderiv ℝ (rectifying mu lambda) p v =
      coefficient mu lambda (Chapter03Coordinates.assignment p) * fderiv ℝ Chapter03Coordinates.assignment p v := by
  rw [(rectifying_hasFDerivAt mu lambda p hy).fderiv, (assignment_hasFDerivAt p hy).fderiv]
  rfl

theorem coefficient_eikonal (mu lambda a : ℝ) (hm : mu ≠ 0) :
    coefficient mu lambda a^2 * (mu^2 + lambda^2 * a^2) = lambda^2 := by
  have hs : 0 < 1 + ((lambda / mu) * a)^2 := by positivity
  have hsq := Real.sq_sqrt (le_of_lt hs)
  have hn : Real.sqrt (1 + ((lambda / mu) * a)^2) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr hs)
  unfold coefficient
  generalize hr : Real.sqrt (1 + ((lambda / mu) * a)^2) = r
  rw [hr] at hsq hn
  have hnormalize : r^2 * mu^2 = mu^2 + lambda^2 * a^2 := by
    rw [hsq]
    field_simp
  rw [← hnormalize]
  field_simp [hm, hn]

theorem rectified_gradient_actual_dual (mu lambda : ℝ) (p v : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Coordinates.metric mu lambda p (rectifiedGradient mu lambda p) v =
      fderiv ℝ (rectifying mu lambda) p v := by
  rw [rectifying_fderiv_apply mu lambda p v hy]
  change Chapter03Coordinates.metric mu lambda p
    (Chapter03Coordinates.scaleVec (coefficient mu lambda (Chapter03Coordinates.assignment p))
      (Chapter03Coordinates.gradientCandidate mu lambda p)) v = _
  rw [Chapter03Coordinates.metric_scale_left, gradient_actual_dual mu lambda p v hm hl hy]

theorem rectified_gradient_norm_sq (mu lambda : ℝ) (p : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Coordinates.metric mu lambda p (rectifiedGradient mu lambda p) (rectifiedGradient mu lambda p) = lambda^2 := by
  rw [← metric_tensor_apply]
  simp only [rectifiedGradient, map_smul, ContinuousLinearMap.smul_apply, smul_eq_mul]
  rw [metric_tensor_apply, Chapter03Coordinates.model_eikonal_coordinate mu lambda p hm hl hy]
  have hc := coefficient_eikonal mu lambda (Chapter03Coordinates.assignment p) hm
  nlinarith [hc]

theorem rectified_gradient_magnitude (mu lambda : ℝ) (p : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    Real.sqrt (Chapter03Coordinates.metric mu lambda p (rectifiedGradient mu lambda p)
      (rectifiedGradient mu lambda p)) = |lambda| := by
  rw [rectified_gradient_norm_sq mu lambda p hm hl hy, Real.sqrt_sq_eq_abs]

def unitRectifying (S : CoordinateRegularAES) (p : Plane) : ℝ := S.a p / S.mu
def unitGradient (S : CoordinateRegularAES) (p : Plane) : Plane := S.mu⁻¹ • S.grad p

theorem unit_rectifying_hasFDerivAt (S : CoordinateRegularAES) (p : Plane) (hp : p ∈ S.domain) :
    HasFDerivAt (unitRectifying S) (S.mu⁻¹ • fderiv ℝ S.a p) p := by
  have hs := (S.a_smooth.contDiffAt (S.domain_open.mem_nhds hp)).differentiableAt (by simp)
  convert hs.hasFDerivAt.const_mul S.mu⁻¹ using 1
  funext x
  simp [unitRectifying, div_eq_mul_inv, mul_comm]

theorem unit_rectifying_actual_dual (S : CoordinateRegularAES) (p v : Plane) (hp : p ∈ S.domain) :
    S.g p (unitGradient S p) v = fderiv ℝ (unitRectifying S) p v := by
  rw [(unit_rectifying_hasFDerivAt S p hp).fderiv]
  simp only [unitGradient, map_smul, ContinuousLinearMap.smul_apply, S.gradient_dual p hp]

theorem unit_gradient_when_lambda_zero (S : CoordinateRegularAES) (hl : S.lambda = 0)
    (p : Plane) (hp : p ∈ S.domain) : S.g p (unitGradient S p) (unitGradient S p) = 1 := by
  have he : S.g p (S.grad p) (S.grad p) = S.mu^2 := by simpa [hl] using S.eikonal p hp
  simp only [unitGradient, map_smul, ContinuousLinearMap.smul_apply, smul_eq_mul]
  rw [he]
  field_simp [S.mu_nonzero]

#print axioms q_positive
#print axioms q_square
#print axioms q_smooth
#print axioms canonical_coefficient_frame_exists
#print axioms rectifying_smooth
#print axioms rectifying_hasFDerivAt
#print axioms rectifying_fderiv_apply
#print axioms coefficient_eikonal
#print axioms rectified_gradient_actual_dual
#print axioms rectified_gradient_norm_sq
#print axioms rectified_gradient_magnitude
#print axioms unit_rectifying_hasFDerivAt
#print axioms unit_rectifying_actual_dual
#print axioms unit_gradient_when_lambda_zero
end AEGPaper0.Chapter03Rectification
