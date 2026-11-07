import ProjectiveBruhat

namespace AEGPaper0.ProjectiveBruhat
open AffineStabilizer
variable {K : Type*} [Field K]
example (q : K) (e : Aff K) :
    (finiteAffineEquiv q e).val=poleGauge q*affineClass e*(poleGauge q)⁻¹ := by
  exact finiteAffineEquiv_class q e
end AEGPaper0.ProjectiveBruhat
