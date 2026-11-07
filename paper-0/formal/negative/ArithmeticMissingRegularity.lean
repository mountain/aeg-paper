import ProjectiveArithmetic

namespace AEGPaper0.ProjectiveArithmetic
open Chapter02 ProjectiveLine
variable {K : Type*} [Field K]
example (slot : Slot) (word : List (Op × K)) : determinant (wordMatrix slot word) ≠ 0 := by
  exact word_nondegenerate slot word
end AEGPaper0.ProjectiveArithmetic
