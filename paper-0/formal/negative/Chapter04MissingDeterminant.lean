import Chapter04Ripples
open AEGPaper0.Chapter04Ripples

example (m : Coefficients) (z : ℂ) (hy : z ∈ upper) : mobius m z ∈ upper := by
  exact mobius_preserves_upper m z
