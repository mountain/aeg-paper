import ProjectiveLine
open AEGPaper0.ProjectiveLine

example {K : Type*} [Field K] (s : K) (m : Matrix2 K) (x : Point K) :
    act (scaleMatrix s m) x = act m x := by
  exact action_scale s m x
