import Chapter04Normalization
namespace AEGPaper0.Chapter04Normalization
example (mu lambda : ℝ) (p v w : Chapter03Analysis.Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    Chapter03Analysis.metricTensor mu lambda p v w =
      standardMetric (normalize mu lambda p)
        (fderiv ℝ (normalize mu lambda) p v) (fderiv ℝ (normalize mu lambda) p w) := by
  exact tensor_pullback mu lambda p v w hm hl hy
end AEGPaper0.Chapter04Normalization
