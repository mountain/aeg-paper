import Chapter03Rectification
open AEGPaper0.Chapter03Rectification
example (mu lambda a : ℝ) : coefficient mu lambda a^2 * (mu^2 + lambda^2 * a^2) = lambda^2 := by
  exact coefficient_eikonal mu lambda a
