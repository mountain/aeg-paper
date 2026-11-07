import Chapter03Flow
open AEGPaper0.Chapter03Flow
example (b c initial : ℝ) (f : ℝ → ℝ) (hf : ∀ t, HasDerivAt f (c + b * f t) t) :
    f = solution b c initial := by
  exact solution_unique b c initial f (hf := hf)
