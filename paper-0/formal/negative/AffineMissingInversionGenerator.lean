import ProjectiveGeneration
open AEGPaper0.ProjectiveGeneralLinear AEGPaper0.ProjectiveGeneration

example {K : Type*} [Field K] (H : Subgroup (PGL2 K))
    (hT : ∀ s, translationClass s ∈ H) (hD : ∀ u, dilationClass u ∈ H) : H=⊤ := by
  exact subgroup_containing_elementary_is_top H hT hD
