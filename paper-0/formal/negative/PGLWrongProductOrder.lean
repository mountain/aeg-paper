import ProjectiveGeneralLinear
open AEGPaper0.ProjectiveLine AEGPaper0.ProjectiveGeneralLinear

example {K : Type*} [Field K] (g h : PGL2 K) (x : Point K) :
    quotientAction (g*h) x = quotientAction h (quotientAction g x) := by
  exact quotient_action_mul g h x
