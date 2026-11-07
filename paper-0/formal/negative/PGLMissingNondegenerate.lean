import ProjectiveFaithfulness
open AEGPaper0.ProjectiveLine AEGPaper0.ProjectiveFaithfulness

example {K : Type*} [Field K] (m n : Matrix2 K) :
    (∀ x : Point K, act m x = act n x) ↔ ∃ s : K, s ≠ 0 ∧ m = scaleMatrix s n := by
  exact equal_actions_iff_nonzero_scalar m n
