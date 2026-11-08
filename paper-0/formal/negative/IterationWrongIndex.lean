import AffineIteration
namespace AEGPaper0.AffineIteration
variable {K : Type*} [Field K]
example (a b z : K) (h1 : a ≠ 1) (n : ℕ) :
    iterate a b n z=b/(1-a)+a^(n+1)*(z-b/(1-a)) := by
  exact centered_iterate a b z h1 n
end AEGPaper0.AffineIteration
