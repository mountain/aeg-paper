import Chapter04Poles
open AEGPaper0.Chapter04Poles

example {X : Type*} (infinity : X) (P Q : Equiv.Perm X) :
    pole infinity (compose P Q) = P.symm (pole infinity Q) := by
  exact pole_covariance infinity P Q
