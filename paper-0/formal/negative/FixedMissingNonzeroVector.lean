import ProjectiveFixedPoints

namespace AEGPaper0.ProjectiveFixedPoints
open ProjectiveLine
variable {K : Type*} [Field K]
example (m : Matrix2 K) (hm : determinant m ≠ 0) (v : Vec K) :
    act m (project v)=project v ↔ invariantSpan m v := by
  exact matrix_fixed_iff_invariantSpan m hm v
end AEGPaper0.ProjectiveFixedPoints
