import Chapter03Coordinates
import Mathlib.Analysis.Calculus.ContDiff.Operations
import Mathlib.Analysis.Calculus.FDeriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.SpecialFunctions.Arsinh
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FunProp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/- Original CC0 continuation by Codex (OpenAI), 2026-11-07.
   Genuine real analytic derivatives for the current Chapter 3. Mathlib and
   its dependency manifest are pinned separately. No derivative is supplied
   as an assumed AES axiom. The coordinate proofs remain unchanged imports. -/
noncomputable section
namespace AEGPaper0.Chapter03Analysis

open scoped ContDiff
open ContinuousLinearMap

abbrev Plane := ℝ × ℝ
def upper : Set Plane := {p | 0 < p.2}

theorem upper_isOpen : IsOpen upper := isOpen_lt continuous_const continuous_snd

theorem upper_height_ne_zero (p : Plane) (hp : p ∈ upper) : p.2 ≠ 0 := ne_of_gt hp

def assignmentDerivative (p : Plane) : Plane →L[ℝ] ℝ :=
  (-p.2⁻¹) • fst ℝ ℝ ℝ + (p.1 / p.2^2) • snd ℝ ℝ ℝ

theorem assignment_derivative_apply (p v : Plane) :
    assignmentDerivative p v = Chapter03Coordinates.assignmentCovector p v := by
  simp [assignmentDerivative, Chapter03Coordinates.assignmentCovector, div_eq_mul_inv]
  ring

theorem assignment_hasFDerivAt (p : Plane) (hy : p.2 ≠ 0) :
    HasFDerivAt Chapter03Coordinates.assignment (assignmentDerivative p) p := by
  have h := (hasFDerivAt_fst (𝕜 := ℝ) (p := p)).neg.mul
    ((hasDerivAt_inv hy).comp_hasFDerivAt p hasFDerivAt_snd)
  convert h using 1
  apply ContinuousLinearMap.ext
  intro v
  simp [assignmentDerivative, div_eq_mul_inv]
  ring

theorem assignment_fderiv_apply (p v : Plane) (hy : p.2 ≠ 0) :
    fderiv ℝ Chapter03Coordinates.assignment p v = Chapter03Coordinates.assignmentCovector p v := by
  rw [(assignment_hasFDerivAt p hy).fderiv]
  exact assignment_derivative_apply p v

theorem assignment_smooth : ContDiffOn ℝ ∞ Chapter03Coordinates.assignment upper := by
  exact contDiff_fst.neg.contDiffOn.div contDiff_snd.contDiffOn upper_height_ne_zero

def leftDerivative (g : Plane) : Plane →L[ℝ] Plane := g.2 • ContinuousLinearMap.id ℝ Plane

theorem left_derivative_apply (g v : Plane) : leftDerivative g v = Chapter03Coordinates.leftTangent g v := rfl

theorem left_translate_hasFDerivAt (g p : Plane) :
    HasFDerivAt (Chapter03Coordinates.leftTranslate g) (leftDerivative g) p := by
  have hx := (hasFDerivAt_const (𝕜 := ℝ) (c := g.1) p).add
    ((hasFDerivAt_fst (𝕜 := ℝ) (p := p)).const_mul g.2)
  have hy := hasFDerivAt_snd (𝕜 := ℝ) (p := p) |>.const_mul g.2
  convert hx.prodMk hy using 1
  apply ContinuousLinearMap.ext
  intro v
  apply Prod.ext <;> simp [leftDerivative]

theorem left_translate_smooth (g : Plane) : ContDiff ℝ ∞ (Chapter03Coordinates.leftTranslate g) := by
  unfold Chapter03Coordinates.leftTranslate
  fun_prop

theorem left_translate_preserves_upper (g p : Plane) (hg : 0 < g.2) (hp : p ∈ upper) :
    Chapter03Coordinates.leftTranslate g p ∈ upper := mul_pos hg hp

theorem invariant_metric_fderiv (mu lambda : ℝ) (g p v w : Plane)
    (hg : g.2 ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Coordinates.metric mu lambda (Chapter03Coordinates.leftTranslate g p)
      (fderiv ℝ (Chapter03Coordinates.leftTranslate g) p v) (fderiv ℝ (Chapter03Coordinates.leftTranslate g) p w) =
        Chapter03Coordinates.metric mu lambda p v w := by
  rw [(left_translate_hasFDerivAt g p).fderiv]
  exact Chapter03Coordinates.invariant_metric_coordinates mu lambda g p v w hg hy

def tensorXX : Plane →L[ℝ] Plane →L[ℝ] ℝ :=
  (mul ℝ ℝ).bilinearComp (fst ℝ ℝ ℝ) (fst ℝ ℝ ℝ)
def tensorYY : Plane →L[ℝ] Plane →L[ℝ] ℝ :=
  (mul ℝ ℝ).bilinearComp (snd ℝ ℝ ℝ) (snd ℝ ℝ ℝ)
def metricTensor (mu lambda : ℝ) (p : Plane) : Plane →L[ℝ] Plane →L[ℝ] ℝ :=
  (1 / (mu^2 * p.2^2)) • tensorXX + (1 / (lambda^2 * p.2^2)) • tensorYY

theorem metric_tensor_apply (mu lambda : ℝ) (p v w : Plane) :
    metricTensor mu lambda p v w = Chapter03Coordinates.metric mu lambda p v w := by
  simp [metricTensor, tensorXX, tensorYY, Chapter03Coordinates.metric, div_eq_mul_inv]
  ring

theorem metric_tensor_smooth (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) :
    ContDiffOn ℝ ∞ (metricTensor mu lambda) upper := by
  have hmden : ∀ p ∈ upper, mu^2 * p.2^2 ≠ 0 := fun p hp =>
    mul_ne_zero (pow_ne_zero 2 hm) (pow_ne_zero 2 (upper_height_ne_zero p hp))
  have hlden : ∀ p ∈ upper, lambda^2 * p.2^2 ≠ 0 := fun p hp =>
    mul_ne_zero (pow_ne_zero 2 hl) (pow_ne_zero 2 (upper_height_ne_zero p hp))
  exact ((contDiffOn_const.div (contDiffOn_const.mul (contDiff_snd.pow 2).contDiffOn) hmden).smul
    contDiffOn_const).add
    ((contDiffOn_const.div (contDiffOn_const.mul (contDiff_snd.pow 2).contDiffOn) hlden).smul
      contDiffOn_const)

theorem gradient_actual_dual (mu lambda : ℝ) (p v : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Coordinates.metric mu lambda p (Chapter03Coordinates.gradientCandidate mu lambda p) v = fderiv ℝ Chapter03Coordinates.assignment p v := by
  rw [assignment_fderiv_apply p v hy]
  exact Chapter03Coordinates.gradient_metric_dual mu lambda p v hm hl hy

theorem gradient_actual_unique (mu lambda : ℝ) (p w : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0)
    (h : ∀ v, Chapter03Coordinates.metric mu lambda p w v = fderiv ℝ Chapter03Coordinates.assignment p v) :
    w = Chapter03Coordinates.gradientCandidate mu lambda p := by
  apply Chapter03Coordinates.gradient_metric_unique mu lambda p w hm hl hy
  intro v
  rw [h v, assignment_fderiv_apply p v hy]

theorem gradient_smooth (mu lambda : ℝ) : ContDiff ℝ ∞ (Chapter03Coordinates.gradientCandidate mu lambda) := by
  unfold Chapter03Coordinates.gradientCandidate
  fun_prop

theorem model_frame_u_smooth (mu lambda : ℝ) : ContDiff ℝ ∞ (fun p : Plane => (Chapter03Coordinates.modelFrame mu lambda p).u) := by
  unfold Chapter03Coordinates.modelFrame
  fun_prop

theorem model_frame_v_smooth (mu lambda : ℝ) : ContDiff ℝ ∞ (fun p : Plane => (Chapter03Coordinates.modelFrame mu lambda p).v) := by
  unfold Chapter03Coordinates.modelFrame
  fun_prop

theorem model_frame_actual_derivatives (mu lambda : ℝ) (p : Plane) (hy : p.2 ≠ 0) :
    fderiv ℝ Chapter03Coordinates.assignment p (Chapter03Coordinates.modelFrame mu lambda p).u = mu ∧
      fderiv ℝ Chapter03Coordinates.assignment p (Chapter03Coordinates.modelFrame mu lambda p).v = lambda * Chapter03Coordinates.assignment p := by
  simp only [assignment_fderiv_apply p _ hy]
  exact Chapter03Coordinates.model_frame_assignment mu lambda p hy

/- A regular AES in ONE open oriented real coordinate chart. The fields
   express the geometric definition; the model constructor proves them all.
   This is not a classification of arbitrary manifolds or boundary charts. -/
structure CoordinateRegularAES where
  domain : Set Plane
  domain_open : IsOpen domain
  mu : ℝ
  lambda : ℝ
  mu_nonzero : mu ≠ 0
  a : Plane → ℝ
  g : Plane → Plane →L[ℝ] Plane →L[ℝ] ℝ
  grad : Plane → Plane
  a_smooth : ContDiffOn ℝ ∞ a domain
  g_smooth : ContDiffOn ℝ ∞ g domain
  grad_smooth : ContDiffOn ℝ ∞ grad domain
  g_symmetric : ∀ p ∈ domain, ∀ v w, g p v w = g p w v
  g_positive : ∀ p ∈ domain, ∀ v, v ≠ 0 → 0 < g p v v
  gradient_dual : ∀ p ∈ domain, ∀ v, g p (grad p) v = fderiv ℝ a p v
  eikonal : ∀ p ∈ domain, g p (grad p) (grad p) = mu^2 + lambda^2 * a p^2

def basicAES (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) : CoordinateRegularAES where
  domain := upper
  domain_open := upper_isOpen
  mu := mu
  lambda := lambda
  mu_nonzero := hm
  a := Chapter03Coordinates.assignment
  g := metricTensor mu lambda
  grad := Chapter03Coordinates.gradientCandidate mu lambda
  a_smooth := assignment_smooth
  g_smooth := metric_tensor_smooth mu lambda hm hl
  grad_smooth := (gradient_smooth mu lambda).contDiffOn
  g_symmetric := by intro p hp v w; simp only [metric_tensor_apply]; exact Chapter03Coordinates.metric_symmetric mu lambda p v w
  g_positive := by
    intro p hp v hv
    rw [metric_tensor_apply]
    exact Chapter03Coordinates.metric_positive_definite mu lambda p v hm hl (upper_height_ne_zero p hp) hv
  gradient_dual := by
    intro p hp v; rw [metric_tensor_apply]
    exact gradient_actual_dual mu lambda p v hm hl (upper_height_ne_zero p hp)
  eikonal := by
    intro p hp; rw [metric_tensor_apply]
    exact Chapter03Coordinates.model_eikonal_coordinate mu lambda p hm hl (upper_height_ne_zero p hp)

theorem basic_AES_eikonal (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) (p : Plane)
    (hp : p ∈ upper) :
    (basicAES mu lambda hm hl).g p ((basicAES mu lambda hm hl).grad p)
      ((basicAES mu lambda hm hl).grad p) = mu^2 + lambda^2 * Chapter03Coordinates.assignment p^2 :=
  (basicAES mu lambda hm hl).eikonal p hp

#print axioms upper_isOpen
#print axioms upper_height_ne_zero
#print axioms assignment_derivative_apply
#print axioms assignment_hasFDerivAt
#print axioms assignment_fderiv_apply
#print axioms assignment_smooth
#print axioms left_derivative_apply
#print axioms left_translate_hasFDerivAt
#print axioms left_translate_smooth
#print axioms left_translate_preserves_upper
#print axioms invariant_metric_fderiv
#print axioms metric_tensor_apply
#print axioms metric_tensor_smooth
#print axioms gradient_actual_dual
#print axioms gradient_actual_unique
#print axioms gradient_smooth
#print axioms model_frame_u_smooth
#print axioms model_frame_v_smooth
#print axioms model_frame_actual_derivatives
#print axioms basic_AES_eikonal
end AEGPaper0.Chapter03Analysis
