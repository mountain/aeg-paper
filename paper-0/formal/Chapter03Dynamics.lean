import Chapter03Analysis
import Chapter03Flow

/- Original CC0 contribution by Codex (OpenAI), 2026-11-07.
   Actual derivatives of the signed model frame, its Lie bracket and the
   assignment chain rule along real coordinate curves. -/
noncomputable section
namespace AEGPaper0.Chapter03Dynamics

open AEGPaper0.Chapter03Analysis

def frameUDerivative (mu : ℝ) : Plane →L[ℝ] Plane :=
  ((-mu) • ContinuousLinearMap.snd ℝ ℝ ℝ).prod 0
def frameVDerivative (lambda : ℝ) : Plane →L[ℝ] Plane :=
  (0 : Plane →L[ℝ] ℝ).prod ((-lambda) • ContinuousLinearMap.snd ℝ ℝ ℝ)

theorem frame_u_hasFDerivAt (mu lambda : ℝ) (p : Plane) :
    HasFDerivAt (fun q => (Chapter03Coordinates.modelFrame mu lambda q).u) (frameUDerivative mu) p := by
  exact ((hasFDerivAt_snd (𝕜 := ℝ) (p := p)).const_mul (-mu)).prodMk
    (hasFDerivAt_const (𝕜 := ℝ) (c := (0 : ℝ)) p)

theorem frame_v_hasFDerivAt (mu lambda : ℝ) (p : Plane) :
    HasFDerivAt (fun q => (Chapter03Coordinates.modelFrame mu lambda q).v) (frameVDerivative lambda) p := by
  exact (hasFDerivAt_const (𝕜 := ℝ) (c := (0 : ℝ)) p).prodMk
    ((hasFDerivAt_snd (𝕜 := ℝ) (p := p)).const_mul (-lambda))

def frameBracket (mu lambda : ℝ) (p : Plane) : Plane :=
  fderiv ℝ (fun q => (Chapter03Coordinates.modelFrame mu lambda q).v) p
    (Chapter03Coordinates.modelFrame mu lambda p).u -
  fderiv ℝ (fun q => (Chapter03Coordinates.modelFrame mu lambda q).u) p
    (Chapter03Coordinates.modelFrame mu lambda p).v

theorem frame_bracket (mu lambda : ℝ) (p : Plane) :
    frameBracket mu lambda p = lambda • (Chapter03Coordinates.modelFrame mu lambda p).u := by
  unfold frameBracket
  rw [(frame_v_hasFDerivAt mu lambda p).fderiv, (frame_u_hasFDerivAt mu lambda p).fderiv]
  apply Prod.ext <;> simp [frameUDerivative, frameVDerivative, Chapter03Coordinates.modelFrame]
  ring

theorem frame_bracket_on_assignment (mu lambda : ℝ) (p : Plane) (hy : p.2 ≠ 0) :
    fderiv ℝ Chapter03Coordinates.assignment p (frameBracket mu lambda p) = mu * lambda := by
  rw [frame_bracket, map_smul, (model_frame_actual_derivatives mu lambda p hy).1]
  simp only [smul_eq_mul]
  ring

theorem assignment_curve_hasDerivAt (mu lambda theta t : ℝ) (curve : ℝ → Plane) (tangent : Plane)
    (hc : HasDerivAt curve tangent t) (hy : (curve t).2 ≠ 0)
    (ht : tangent = Real.cos theta • (Chapter03Coordinates.modelFrame mu lambda (curve t)).u +
      Real.sin theta • (Chapter03Coordinates.modelFrame mu lambda (curve t)).v) :
    HasDerivAt (fun s => Chapter03Coordinates.assignment (curve s))
      (mu * Real.cos theta + lambda * Chapter03Coordinates.assignment (curve t) * Real.sin theta) t := by
  have h := (assignment_hasFDerivAt (curve t) hy).comp_hasDerivAt t hc
  have fields := model_frame_actual_derivatives mu lambda (curve t) hy
  have he : assignmentDerivative (curve t) tangent =
      mu * Real.cos theta + lambda * Chapter03Coordinates.assignment (curve t) * Real.sin theta := by
    rw [ht, map_add, map_smul, map_smul, ← (assignment_hasFDerivAt (curve t) hy).fderiv,
      fields.1, fields.2]
    simp only [smul_eq_mul]
    ring
  exact he ▸ h

theorem directional_unit_speed (mu lambda theta : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0)
    (p : Plane) (hy : p.2 ≠ 0) :
    let v := Real.cos theta • (Chapter03Coordinates.modelFrame mu lambda p).u +
      Real.sin theta • (Chapter03Coordinates.modelFrame mu lambda p).v
    Chapter03Coordinates.metric mu lambda p v v = 1 := by
  dsimp only
  rw [← metric_tensor_apply]
  simp only [map_add, map_smul, ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply, smul_eq_mul,
    metric_tensor_apply]
  have fields := Chapter03Coordinates.model_frame_orthonormal mu lambda p hm hl hy
  have cross : Chapter03Coordinates.metric mu lambda p (Chapter03Coordinates.modelFrame mu lambda p).v
      (Chapter03Coordinates.modelFrame mu lambda p).u = 0 := by
    rw [Chapter03Coordinates.metric_symmetric]; exact fields.2.2
  rw [fields.1, fields.2.1, fields.2.2, cross]
  nlinarith [Real.sin_sq_add_cos_sq theta]

theorem coordinate_curve_solution (mu lambda theta : ℝ) (curve : ℝ → Plane)
    (hc : ∀ t, HasDerivAt curve
      (Real.cos theta • (Chapter03Coordinates.modelFrame mu lambda (curve t)).u +
        Real.sin theta • (Chapter03Coordinates.modelFrame mu lambda (curve t)).v) t)
    (hy : ∀ t, (curve t).2 ≠ 0) (t : ℝ) :
    Chapter03Coordinates.assignment (curve t) =
      Chapter03Flow.solution (lambda * Real.sin theta) (mu * Real.cos theta)
        (Chapter03Coordinates.assignment (curve 0)) t := by
  have hf : ∀ t, HasDerivAt (fun s => Chapter03Coordinates.assignment (curve s))
      (mu * Real.cos theta + (lambda * Real.sin theta) * Chapter03Coordinates.assignment (curve t)) t := by
    intro t
    convert assignment_curve_hasDerivAt mu lambda theta t curve _ (hc t) (hy t) rfl using 1
    ring
  exact congrArg (fun f => f t) (Chapter03Flow.solution_unique _ _ _
    (fun s => Chapter03Coordinates.assignment (curve s)) rfl hf)

#print axioms frame_u_hasFDerivAt
#print axioms frame_v_hasFDerivAt
#print axioms frame_bracket
#print axioms frame_bracket_on_assignment
#print axioms assignment_curve_hasDerivAt
#print axioms directional_unit_speed
#print axioms coordinate_curve_solution
end AEGPaper0.Chapter03Dynamics
