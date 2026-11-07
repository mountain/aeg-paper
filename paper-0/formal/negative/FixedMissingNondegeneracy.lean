import ProjectiveFixedPoints

namespace AEGPaper0.ProjectiveFixedPoints
open ProjectiveLine
variable {K : Type*} [Field K]
example (m : Matrix2 K) (v : Vec K) (hv : v ≠ (0,0)) :
    act m (project v)=project v ↔ invariantSpan m v := by
  exact matrix_fixed_iff_invariantSpan m
end AEGPaper0.ProjectiveFixedPoints
