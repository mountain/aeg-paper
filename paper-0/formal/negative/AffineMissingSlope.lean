import AffineStabilizer
open AEGPaper0.AffineStabilizer

example {K : Type*} [Field K] (a b : K) : ∃ e : Aff K, ∀ x : K, e x=a*x+b := by
  exact affine_map_exists a b
