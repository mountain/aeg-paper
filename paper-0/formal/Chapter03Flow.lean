import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/- Original CC0 contribution by Codex (OpenAI), 2026-11-07.
   Real constant-coefficient affine ODE: explicit solution, existence and
   uniqueness. This is separate from an intrinsic manifold chain rule. -/
noncomputable section
namespace AEGPaper0.Chapter03Flow

def solution (b c initial t : ℝ) : ℝ :=
  if b = 0 then initial + c * t
  else Real.exp (b * t) * initial + c * (Real.exp (b * t) - 1) / b

theorem solution_initial (b c initial : ℝ) : solution b c initial 0 = initial := by
  by_cases hb : b = 0 <;> simp [solution, hb]

theorem solution_zero_coefficient (c initial t : ℝ) : solution 0 c initial t = initial + c * t := by
  simp [solution]

theorem solution_nonzero_coefficient (b c initial t : ℝ) (hb : b ≠ 0) :
    solution b c initial t = Real.exp (b * t) * initial + c * (Real.exp (b * t) - 1) / b := by
  simp [solution, hb]

theorem solution_hasDerivAt (b c initial t : ℝ) :
    HasDerivAt (solution b c initial) (c + b * solution b c initial t) t := by
  by_cases hb : b = 0
  · subst b
    have he : solution 0 c initial = fun u => initial + c * u := by
      funext u; exact solution_zero_coefficient c initial u
    rw [he]
    simpa only [zero_mul, add_zero, mul_one] using ((hasDerivAt_id t).const_mul c).const_add initial
  · have he : HasDerivAt (fun t : ℝ => Real.exp (b * t)) (Real.exp (b * t) * b) t :=
      by simpa only [Function.comp_def, mul_one] using
        (Real.hasDerivAt_exp (b * t)).comp t ((hasDerivAt_id t).const_mul b)
    have h := (he.mul_const initial).add (((he.sub_const 1).const_mul c).div_const b)
    convert h using 1
    · funext t; simp [solution, hb]
    · simp only [solution, if_neg hb]
      field_simp
      ring

theorem solution_derivative (b c initial t : ℝ) :
    deriv (solution b c initial) t = c + b * solution b c initial t :=
  (solution_hasDerivAt b c initial t).deriv

theorem solution_composition (b c initial s t : ℝ) :
    solution b c initial (s + t) = solution b c (solution b c initial s) t := by
  by_cases hb : b = 0
  · simp [solution, hb]; ring
  · simp only [solution, if_neg hb, mul_add, Real.exp_add]
    field_simp
    ring

theorem solution_unique (b c initial : ℝ) (f : ℝ → ℝ) (h0 : f 0 = initial)
    (hf : ∀ t, HasDerivAt f (c + b * f t) t) : f = solution b c initial := by
  let weighted : ℝ → ℝ := fun t => Real.exp (-b * t) * (f t - solution b c initial t)
  have hw : ∀ t, HasDerivAt weighted 0 t := by
    intro t
    have he := (Real.hasDerivAt_exp (-b * t)).comp t ((hasDerivAt_id t).const_mul (-b))
    have hd := (hf t).sub (solution_hasDerivAt b c initial t)
    convert he.mul hd using 1
    simp only [Function.comp_def, Pi.sub_apply]
    ring
  funext t
  have hc := is_const_of_deriv_eq_zero (fun t => (hw t).differentiableAt)
    (fun t => (hw t).deriv) t 0
  have heq : Real.exp (-b * t) * (f t - solution b c initial t) = 0 := by
    simpa [weighted, h0, solution_initial] using hc
  exact sub_eq_zero.mp ((mul_eq_zero.mp heq).resolve_left (Real.exp_ne_zero _))

theorem angular_solution (mu lambda theta initial t : ℝ) :
    HasDerivAt (solution (lambda * Real.sin theta) (mu * Real.cos theta) initial)
      (mu * Real.cos theta + lambda *
        solution (lambda * Real.sin theta) (mu * Real.cos theta) initial t * Real.sin theta) t := by
  convert solution_hasDerivAt (lambda * Real.sin theta) (mu * Real.cos theta) initial t using 1
  ring

theorem additive_axis (mu initial t : ℝ) : solution 0 mu initial t = initial + mu * t := by
  exact solution_zero_coefficient mu initial t

theorem multiplicative_axis (lambda initial t : ℝ) :
    solution lambda 0 initial t = Real.exp (lambda * t) * initial := by
  by_cases hl : lambda = 0 <;> simp [solution, hl]

#print axioms solution_initial
#print axioms solution_zero_coefficient
#print axioms solution_nonzero_coefficient
#print axioms solution_hasDerivAt
#print axioms solution_derivative
#print axioms solution_composition
#print axioms solution_unique
#print axioms angular_solution
#print axioms additive_axis
#print axioms multiplicative_axis
end AEGPaper0.Chapter03Flow
