import Chapter04Apollonius
open AEGPaper0.Chapter04Ripples AEGPaper0.Chapter04Apollonius

example (m : Coefficients) (r : ℝ) (z : ℂ) (ha : m.a ≠ 0) (hc : m.c ≠ 0) :
    ‖mobius m z‖ = r ↔ z ∈ weightedLocus (zeroX m) (poleX m) (weight m r) := by
  exact norm_level_apollonius m r z ha hc
