import ProjectiveBruhat

namespace AEGPaper0.ProjectiveBruhat
open ProjectiveGeneralLinear AffineStabilizer
variable {K : Type*} [Field K]
example (q : K) (g : PGL2 K) : poleGauge q*g*(poleGauge q)⁻¹ ∈ infinityStabilizer := by
  exact (finite_stabilizer_iff q g).mp
end AEGPaper0.ProjectiveBruhat
