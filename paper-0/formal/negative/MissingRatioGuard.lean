import AppendixC

/- Deliberate negative control: the supplied theorem requires y != x. -/
open AEGPaper0 AEGPaper0.Chapter02 AEGPaper0.AppendixC
example {A : Type} (s : FieldData A) (word : Word A) (x y : A) :
    quotient s (difference s (evaluate s.toAlgebra word y) (evaluate s.toAlgebra word x))
      (difference s y x) = scale s.toAlgebra word := by
  exact perturbation_ratio s word x y
