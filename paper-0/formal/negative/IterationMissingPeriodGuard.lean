import AffineIteration
namespace AEGPaper0.AffineIteration
variable {K : Type*} [Field K]
example (b z : K) (n : ℕ) : iterate 1 b n z=z := by
  exact translation_period_when_cast_zero b z n
end AEGPaper0.AffineIteration
