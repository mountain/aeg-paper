import Chapter04Tangency
namespace AEGPaper0.Chapter04Tangency
example (q r : ℝ) (v : Plane) :
    fderiv ℝ (circleResidual q r) (q,0) v=0 ↔ v.2=0 := by
  exact boundary_tangent_kernel q r
end AEGPaper0.Chapter04Tangency
