import ProjectiveArithmetic

namespace AEGPaper0.ProjectiveArithmetic
open Chapter02 ProjectiveGeneralLinear
variable {K : Type*} [Field K]
example (slot : Slot) (word : List (Op × K)) (h : regularWord word) (x y : K)
    (_endpoint : quotientAction (wordClass slot word h) (some x)=some y) :
    ∃ z, PartialFold (relation slot) word x z := by
  exact (ordinary_domain_iff_safe slot word h x).mpr
end AEGPaper0.ProjectiveArithmetic
