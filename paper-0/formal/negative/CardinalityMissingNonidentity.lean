import ProjectiveCardinality
namespace AEGPaper0.ProjectiveCardinality
open ProjectiveGeneralLinear ProjectiveFixedPoints
variable {K : Type*} [Field K]
example (g : PGL2 K) : (fixedSet g).Finite ∧ (fixedSet g).ncard ≤ 2 := by
  exact nonidentity_fixed_cardinality g
end AEGPaper0.ProjectiveCardinality
