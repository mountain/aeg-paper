import ProjectiveFixedPoints

namespace AEGPaper0.ProjectiveFixedPoints
open ProjectiveGeneralLinear
variable {K : Type*} [Field K]
example (g h : PGL2 K) (p : {p // p ∈ fixedSet h}) :
    (fixedPointConjugacy g h p).val=quotientAction g⁻¹ p.val := by
  exact fixedPointConjugacy_apply g h p
end AEGPaper0.ProjectiveFixedPoints
