import AffineIteration
namespace AEGPaper0.AffineIteration
variable {K : Type*} [Field K]
example (a b z : K) (n : ℕ) : iterate a b n z=b/(1-a)+a^n*(z-b/(1-a)) := by
  exact centered_iterate a b z
end AEGPaper0.AffineIteration
