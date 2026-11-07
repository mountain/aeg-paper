import ProjectiveFixedPoints

namespace AEGPaper0.ProjectiveFixedPoints
open ProjectiveLine
variable {K : Type*} [Field K]
example (s t : K) (m : Matrix2 K) (v : Vec K) (he : mapVec m v=scaleVec t v) :
    mapVec (scaleMatrix s m) v=scaleVec t v := by
  exact matrix_rescaling_rescales_eigenvalue s t m v he
end AEGPaper0.ProjectiveFixedPoints
