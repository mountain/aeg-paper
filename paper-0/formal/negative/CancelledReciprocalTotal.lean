import Chapter02Evaluability

/- Deliberate negative control: the nonzero input hypothesis is missing. -/
open AEGPaper0.Chapter02 AEGPaper0.Chapter02Evaluability
example {A : Type} (s : FieldData A) (input : A) :
    Domain s (cancelledReciprocal s) input := by
  exact (cancelled_reciprocal_domain s input).mpr
