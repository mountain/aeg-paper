import Chapter04Normalization
namespace AEGPaper0.Chapter04Normalization
example (mu lambda : ℝ) (p v w : Chapter03Analysis.Plane)
    (hm : mu ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Coordinates.metric mu lambda p v w =
      standardMetric (normalize mu lambda p)
        (fderiv ℝ (normalize mu lambda) p v) (fderiv ℝ (normalize mu lambda) p w) / lambda^2 := by
  exact metric_pullback mu lambda p v w hm
end AEGPaper0.Chapter04Normalization
