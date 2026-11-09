import Chapter04Ripples
import Mathlib.Analysis.Calculus.FDeriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv

/- Original CC0 proofs by Codex (OpenAI), 2026-11-09.
   Euclidean differential tangency at the ideal boundary in the continuation
   chart. The hyperbolic metric itself is not extended to boundary points. -/
noncomputable section
namespace AEGPaper0.Chapter04Tangency
open ContinuousLinearMap
open Real

abbrev Plane := ℝ × ℝ

def circleResidual (q r : ℝ) (p : Plane) : ℝ := (p.1-q)^2+(p.2-r)^2-r^2
def circleDerivative (q r : ℝ) (p : Plane) : Plane →L[ℝ] ℝ :=
  (2*(p.1-q)) • fst ℝ ℝ ℝ + (2*(p.2-r)) • snd ℝ ℝ ℝ

theorem circle_hasFDerivAt (q r : ℝ) (p : Plane) :
    HasFDerivAt (circleResidual q r) (circleDerivative q r p) p := by
  have h := (((hasFDerivAt_fst (𝕜 := ℝ) (p := p)).sub_const q).pow 2).add
    (((hasFDerivAt_snd (𝕜 := ℝ) (p := p)).sub_const r).pow 2)
  convert h.sub_const (r^2) using 1
  apply ContinuousLinearMap.ext
  intro v
  simp [circleDerivative]

theorem boundary_derivative_apply (q r : ℝ) (v : Plane) :
    fderiv ℝ (circleResidual q r) (q,0) v = -2*r*v.2 := by
  rw [(circle_hasFDerivAt q r (q,0)).fderiv]
  simp [circleDerivative]

theorem boundary_derivative_nonzero (q r : ℝ) (hr : r ≠ 0) :
    fderiv ℝ (circleResidual q r) (q,0) ≠ 0 := by
  intro h
  have he := congrArg (fun f : Plane →L[ℝ] ℝ => f (0,1)) h
  change fderiv ℝ (circleResidual q r) (q,0) (0,1)=0 at he
  rw [boundary_derivative_apply] at he
  simp only [mul_one] at he
  exact hr (by linarith)

theorem boundary_tangent_kernel (q r : ℝ) (hr : r ≠ 0) (v : Plane) :
    fderiv ℝ (circleResidual q r) (q,0) v=0 ↔ v.2=0 := by
  rw [boundary_derivative_apply]
  exact mul_eq_zero.trans (or_iff_right (mul_ne_zero (by norm_num) hr))

theorem boundary_tangent_horizontal_span (q r : ℝ) (hr : r ≠ 0) (v : Plane) :
    fderiv ℝ (circleResidual q r) (q,0) v=0 ↔ ∃ a : ℝ, v=(a,0) := by
  rw [boundary_tangent_kernel q r hr v]
  constructor
  · intro h; exact ⟨v.1,Prod.ext rfl h⟩
  · rintro ⟨a,rfl⟩; rfl

def circleParam (q r s : ℝ) : Plane := (q+r*sin s, r*(1-cos s))

theorem circle_param_lies_on_circle (q r s : ℝ) : circleResidual q r (circleParam q r s)=0 := by
  have h := congrArg (fun a : ℝ => r^2*a) (Real.sin_sq_add_cos_sq s)
  dsimp at h
  dsimp [circleResidual, circleParam]
  nlinarith [h]

theorem circle_param_hasDerivAt (q r s : ℝ) :
    HasDerivAt (circleParam q r) (r*cos s,r*sin s) s := by
  have hx := (hasDerivAt_const s q).add ((Real.hasDerivAt_sin s).const_mul r)
  have hy := ((hasDerivAt_const s (1:ℝ)).sub (Real.hasDerivAt_cos s)).const_mul r
  simpa using hx.prodMk hy

theorem circle_param_contact (q r : ℝ) : circleParam q r 0=(q,0) := by
  simp [circleParam]

theorem circle_param_contact_derivative (q r : ℝ) :
    HasDerivAt (circleParam q r) (r,0) 0 := by
  simpa using circle_param_hasDerivAt q r 0

theorem circle_param_regular_contact (r : ℝ) (hr : r ≠ 0) : (r,0) ≠ ((0,0) : Plane) := by
  intro h
  exact hr (congrArg Prod.fst h)

theorem circle_param_above_boundary (q r s : ℝ) (hr : 0 ≤ r) : 0 ≤ (circleParam q r s).2 :=
  mul_nonneg hr (sub_nonneg.mpr (Real.cos_le_one s))

theorem ripple_circle_residual (m : Chapter04Ripples.Coefficients) (t : ℝ) (p : Plane) :
    Chapter04Ripples.circleEquation m t p.1 p.2 ↔
      circleResidual (Chapter04Ripples.poleX m) (Chapter04Ripples.radius m t) p=0 := by
  simp only [Chapter04Ripples.circleEquation, circleResidual, Chapter04Ripples.poleX,
    neg_div, sub_neg_eq_add]
  exact sub_eq_zero.symm

theorem ripple_boundary_differential (m : Chapter04Ripples.Coefficients) (t : ℝ)
    (hd : 0 < Chapter04Ripples.determinant m) (ht : 0 < t) (hc : m.c ≠ 0) :
    fderiv ℝ (circleResidual (Chapter04Ripples.poleX m) (Chapter04Ripples.radius m t))
      (Chapter04Ripples.poleX m,0) ≠ 0 ∧
    ∀ v : Plane, fderiv ℝ (circleResidual (Chapter04Ripples.poleX m) (Chapter04Ripples.radius m t))
      (Chapter04Ripples.poleX m,0) v=0 ↔ v.2=0 := by
  have hr := ne_of_gt (Chapter04Ripples.radius_positive m t hd ht hc)
  exact ⟨boundary_derivative_nonzero _ _ hr, boundary_tangent_kernel _ _ hr⟩

theorem actual_curve_tangent (q r : ℝ) (hr : r ≠ 0) (gamma : ℝ → Plane) (v : Plane)
    (hg : HasDerivAt gamma v 0) (hc : gamma 0=(q,0))
    (hl : ∀ s, circleResidual q r (gamma s)=0) : v.2=0 := by
  have h := (circle_hasFDerivAt q r (gamma 0)).comp_hasDerivAt 0 hg
  have he : (fun s => circleResidual q r (gamma s))=(fun _ : ℝ => (0:ℝ)) := funext hl
  change HasDerivAt (fun s => circleResidual q r (gamma s)) _ 0 at h
  rw [he] at h
  have hd := h.unique (hasDerivAt_const (0:ℝ) (0:ℝ))
  have hd' : fderiv ℝ (circleResidual q r) (q,0) v=0 := by
    rw [(circle_hasFDerivAt q r (q,0)).fderiv]
    simpa only [hc] using hd
  exact (boundary_tangent_kernel q r hr v).mp hd'

#print axioms AEGPaper0.Chapter04Tangency.circle_hasFDerivAt
#print axioms AEGPaper0.Chapter04Tangency.boundary_derivative_apply
#print axioms AEGPaper0.Chapter04Tangency.boundary_derivative_nonzero
#print axioms AEGPaper0.Chapter04Tangency.boundary_tangent_kernel
#print axioms AEGPaper0.Chapter04Tangency.boundary_tangent_horizontal_span
#print axioms AEGPaper0.Chapter04Tangency.circle_param_lies_on_circle
#print axioms AEGPaper0.Chapter04Tangency.circle_param_hasDerivAt
#print axioms AEGPaper0.Chapter04Tangency.circle_param_contact
#print axioms AEGPaper0.Chapter04Tangency.circle_param_contact_derivative
#print axioms AEGPaper0.Chapter04Tangency.circle_param_regular_contact
#print axioms AEGPaper0.Chapter04Tangency.circle_param_above_boundary
#print axioms AEGPaper0.Chapter04Tangency.ripple_circle_residual
#print axioms AEGPaper0.Chapter04Tangency.ripple_boundary_differential
#print axioms AEGPaper0.Chapter04Tangency.actual_curve_tangent
end AEGPaper0.Chapter04Tangency
