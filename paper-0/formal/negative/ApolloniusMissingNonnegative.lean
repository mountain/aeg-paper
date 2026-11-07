import Chapter04Apollonius
open AEGPaper0.Chapter04Apollonius

example (q p k : ℝ) (z : ℂ) : z ∈ weightedLocus q p k ↔
    (z.re - q)^2 + z.im^2 = k^2 * ((z.re - p)^2 + z.im^2) := by
  exact weighted_squared_equation q p k z
