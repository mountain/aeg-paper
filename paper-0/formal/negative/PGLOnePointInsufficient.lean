import ProjectiveGeneralLinear
open AEGPaper0.ProjectiveGeneralLinear

example {K : Type*} [Field K] (g h : GL2 K) (hinf : actionHom g none = actionHom h none) :
    (QuotientGroup.mk g : PGL2 K) = QuotientGroup.mk h := by
  exact three_points_determine_quotient g h hinf
