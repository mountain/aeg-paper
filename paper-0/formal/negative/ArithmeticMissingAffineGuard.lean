import ProjectiveArithmetic

namespace AEGPaper0.ProjectiveArithmetic
open Chapter02 ProjectiveGeneralLinear
variable {K : Type*} [Field K]
example (q : PGL2 K) : ∃ word, ∃ h : regularWord word, wordClass .first word h=q := by
  exact (first_word_image_is_stabilizer q).mpr
end AEGPaper0.ProjectiveArithmetic
