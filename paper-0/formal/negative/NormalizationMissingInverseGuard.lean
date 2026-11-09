import Chapter04Normalization
namespace AEGPaper0.Chapter04Normalization
example (mu lambda : ℝ) (p : Chapter03Analysis.Plane) :
    normalize lambda mu (normalize mu lambda p)=p := by
  exact normalize_inverse mu lambda
end AEGPaper0.Chapter04Normalization
