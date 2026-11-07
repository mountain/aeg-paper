import AffineStabilizer
namespace AEGPaper0.AffineStabilizer

example {K : Type*} [Field K] (e f : Aff K) :
    slope (e*f)=slope e*slope f ∧ offset (e*f)=slope f*offset e+offset f := by
  exact affine_parameter_composition e f

end AEGPaper0.AffineStabilizer
