import ProjectiveFaithfulness
open AEGPaper0.ProjectiveLine AEGPaper0.ProjectiveFaithfulness

example {K : Type*} [Field K] (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (he : ∀ x : Point K, act m x = act n x) : m = n := by
  exact (equal_actions_iff_nonzero_scalar m n hm hn).mp he
