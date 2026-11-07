import ProjectiveLine
open AEGPaper0.ProjectiveLine

example {K : Type*} [Field K] (m : Matrix2 K) (x : Point K) : act (adjugate m) (act m x) = x := by
  exact action_adjugate_left m x
