import Chapter04ProjectiveBridge
open AEGPaper0.ProjectiveLine AEGPaper0.Chapter04ProjectiveBridge

example {K : Type*} [Field K] (m n : Matrix2 K) (hm : determinant m ≠ 0) (hn : determinant n ≠ 0)
    (hmn : determinant (multiply m n) ≠ 0) : matrixPole (multiply m n) hmn = matrixPole n hn := by
  exact affine_postcompose_keeps_pole m n hm hn hmn
