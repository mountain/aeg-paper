import Chapter04Poles
open AEGPaper0.Chapter04Poles

example {X : Type*} (infinity : X) (P Q : Equiv.Perm X) :
    pole infinity (compose P Q) = pole infinity Q := by
  exact postcompose_affine_keeps_current_pole infinity P Q
