import ProjectiveArithmetic

namespace AEGPaper0.ProjectiveArithmetic
open Chapter02
variable {K : Type*} [Field K]
example (slot : Slot) (before after : List (Op × K)) (h : regularWord (before++after)) :
    wordClass slot (before++after) h = wordClass slot before ((regularWord_append before after).mp h).1 *
      wordClass slot after ((regularWord_append before after).mp h).2 := by
  exact wordClass_append slot before after h
end AEGPaper0.ProjectiveArithmetic
