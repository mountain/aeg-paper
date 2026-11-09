import Chapter04IdealBoundary
namespace AEGPaper0.Chapter04IdealBoundary
open Filter Chapter04Horocycles
open scoped UpperHalfPlane Topology
example : Tendsto (fun s => OnePoint.some (vertical 0 s : ℂ)) atTop
    (𝓝 (embed (OnePoint.some 0))) := by
  exact infinity_ray_tendsto
end AEGPaper0.Chapter04IdealBoundary
