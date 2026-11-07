import Chapter04ProjectiveBridge
import Chapter04Ripples

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   The existing actual complex Mobius map is the finite chart of the concrete
   homogeneous projective action. Nonzero denominators guard that chart;
   sending a denominator root to infinity does not legalize ordinary division. -/
namespace AEGPaper0.Chapter04ComplexProjective

noncomputable section
open ProjectiveLine Chapter04ProjectiveBridge

def realMatrix (m : Chapter04Ripples.Coefficients) : Matrix2 ℝ := ⟨m.a, m.b, m.c, m.d⟩
def complexMatrix (m : Chapter04Ripples.Coefficients) : Matrix2 ℂ := ⟨m.a, m.b, m.c, m.d⟩

theorem real_determinant (m : Chapter04Ripples.Coefficients) :
    determinant (realMatrix m) = Chapter04Ripples.determinant m := rfl

theorem complex_determinant (m : Chapter04Ripples.Coefficients) :
    determinant (complexMatrix m) = (Chapter04Ripples.determinant m : ℂ) := by
  simp [determinant, complexMatrix, Chapter04Ripples.determinant]

theorem real_nondegenerate (m : Chapter04Ripples.Coefficients) (hd : Chapter04Ripples.determinant m ≠ 0) :
    determinant (realMatrix m) ≠ 0 := hd

theorem complex_nondegenerate (m : Chapter04Ripples.Coefficients) (hd : Chapter04Ripples.determinant m ≠ 0) :
    determinant (complexMatrix m) ≠ 0 := by
  rw [complex_determinant]
  exact_mod_cast hd

theorem complex_finite_chart (m : Chapter04Ripples.Coefficients) (z : ℂ)
    (hz : Chapter04Ripples.denominator m z ≠ 0) :
    act (complexMatrix m) (some z) = some (Chapter04Ripples.mobius m z) := by
  rw [finite_action]
  change (if (m.c : ℂ)*z+m.d=0 then none else some (((m.a : ℂ)*z+m.b)/((m.c : ℂ)*z+m.d))) = _
  change (m.c : ℂ)*z+m.d≠0 at hz
  rw [if_neg hz]
  rfl

theorem complex_pole_input_goes_to_infinity (m : Chapter04Ripples.Coefficients)
    (hd : Chapter04Ripples.determinant m ≠ 0) (hc : m.c ≠ 0) :
    act (complexMatrix m) (some (Chapter04Ripples.poleX m : ℂ)) = none := by
  apply (finite_pole_unique _ (complex_nondegenerate m hd)
    (by change (m.c : ℂ) ≠ 0; exact_mod_cast hc) _).mpr
  simp [complexMatrix, Chapter04Ripples.poleX]

theorem real_pole_formula (m : Chapter04Ripples.Coefficients)
    (hd : Chapter04Ripples.determinant m ≠ 0) (hc : m.c ≠ 0) :
    matrixPole (realMatrix m) (real_nondegenerate m hd) = some (Chapter04Ripples.poleX m) :=
  concrete_finite_pole _ _ hc

theorem complex_pole_formula (m : Chapter04Ripples.Coefficients)
    (hd : Chapter04Ripples.determinant m ≠ 0) (hc : m.c ≠ 0) :
    matrixPole (complexMatrix m) (complex_nondegenerate m hd) = some (Chapter04Ripples.poleX m : ℂ) := by
  rw [concrete_finite_pole _ _ (by change (m.c : ℂ) ≠ 0; exact_mod_cast hc)]
  simp [complexMatrix, Chapter04Ripples.poleX]

theorem complex_stabilizer (m : Chapter04Ripples.Coefficients) (hd : Chapter04Ripples.determinant m ≠ 0) :
    Chapter04Poles.fixesInfinity none (actionEquiv (complexMatrix m) (complex_nondegenerate m hd)) ↔ m.c = 0 := by
  rw [concrete_stabilizer_criterion]
  simp [complexMatrix]

theorem upper_chart_action (m : Chapter04Ripples.Coefficients) (z : ℂ)
    (hd : 0 < Chapter04Ripples.determinant m) (hy : z ∈ Chapter04Ripples.upper) :
    ∃ w : ℂ, act (complexMatrix m) (some z) = some w ∧ w ∈ Chapter04Ripples.upper := by
  exact ⟨Chapter04Ripples.mobius m z,
    complex_finite_chart m z (Chapter04Ripples.denominator_ne_zero m z (ne_of_gt hd) hy),
    Chapter04Ripples.mobius_preserves_upper m z hd hy⟩

theorem real_complex_chart_compatibility (m : Chapter04Ripples.Coefficients) (x : Point ℝ) :
    act (complexMatrix m) (x.map Complex.ofReal) = (act (realMatrix m) x).map Complex.ofReal := by
  cases x with
  | none =>
    simp only [Option.map_none]
    rw [infinity_action, infinity_action]
    by_cases hc : m.c = 0 <;> simp [realMatrix, complexMatrix, hc]
  | some x =>
    rw [Option.map_some, finite_action, finite_action]
    by_cases h : m.c*x+m.d=0
    · have hh : (m.c : ℂ)*x+m.d=0 := by exact_mod_cast h
      simp [realMatrix, complexMatrix, h, hh]
    · have hh : (m.c : ℂ)*x+m.d≠0 := by exact_mod_cast h
      simp [realMatrix, complexMatrix, h, hh]

theorem complex_ripple_chart_membership (m : Chapter04Ripples.Coefficients) (z w : ℂ) (t : ℝ)
    (hd : 0 < Chapter04Ripples.determinant m) (hy : z ∈ Chapter04Ripples.upper)
    (hact : act (complexMatrix m) (some z) = some w) :
    z ∈ Chapter04Ripples.ripple m t ↔ w ∈ Chapter04Ripples.horocycle t := by
  have he := complex_finite_chart m z (Chapter04Ripples.denominator_ne_zero m z (ne_of_gt hd) hy)
  have hw : w = Chapter04Ripples.mobius m z := Option.some.inj (hact.symm.trans he)
  rw [hw, Chapter04Ripples.ripple_membership]
  exact and_iff_right hy

end
end AEGPaper0.Chapter04ComplexProjective

#print axioms AEGPaper0.Chapter04ComplexProjective.real_determinant
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_determinant
#print axioms AEGPaper0.Chapter04ComplexProjective.real_nondegenerate
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_nondegenerate
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_finite_chart
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_pole_input_goes_to_infinity
#print axioms AEGPaper0.Chapter04ComplexProjective.real_pole_formula
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_pole_formula
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_stabilizer
#print axioms AEGPaper0.Chapter04ComplexProjective.upper_chart_action
#print axioms AEGPaper0.Chapter04ComplexProjective.real_complex_chart_compatibility
#print axioms AEGPaper0.Chapter04ComplexProjective.complex_ripple_chart_membership
