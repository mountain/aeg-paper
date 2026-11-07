import ProjectiveBruhat

namespace AEGPaper0.ProjectiveBruhat
open ProjectiveGeneralLinear
variable {K : Type*} [Field K]
example (q z : K) : quotientAction (poleGauge q) (some z)=some (-1/(z-q)) := by
  exact poleGauge_finite q z
end AEGPaper0.ProjectiveBruhat
