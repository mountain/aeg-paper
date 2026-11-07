import ProjectiveBruhat

namespace AEGPaper0.ProjectiveBruhat
open ProjectiveLine ProjectiveGeneration
variable {K : Type*} [Field K]
example (m : Matrix2 K) (hm : determinant m ≠ 0) : ofMatrix m hm ∈ bigCell := by
  exact nonaffine_in_bigCell m hm
end AEGPaper0.ProjectiveBruhat
