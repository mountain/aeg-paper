import AffineStabilizer
open AEGPaper0.ProjectiveLine AEGPaper0.ProjectiveGeneration AEGPaper0.AffineStabilizer

example {K : Type*} [Field K] (m : Matrix2 K) (hm : determinant m ≠ 0) :
    ofMatrix m hm ∈ infinityStabilizer := by
  exact (infinity_iff_lower_left_zero m hm).mpr
