import Chapter04Apollonius
open AEGPaper0.Chapter04Apollonius

example (q p : ℝ) (z : ℂ) : z ∈ weightedLocus q p 1 ↔ z.re = (q + p) / 2 := by
  exact unit_weight_bisector q p z
