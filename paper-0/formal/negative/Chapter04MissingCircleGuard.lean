import Chapter04Ripples
open AEGPaper0.Chapter04Ripples

example (m : Coefficients) (t x y : ℝ) :
    determinant m * y = t * ((m.c * x + m.d)^2 + m.c^2 * y^2) ↔
      circleEquation m t x y := by
  exact completed_square m t x y
