import Chapter04Horocycles
namespace AEGPaper0.Chapter04Horocycles
open Filter Real
open scoped UpperHalfPlane Topology
example (z : ℍ) : Tendsto (fun s => dist z (vertical 0 s)-s) atTop (𝓝 (log z.im)) := by
  exact infinity_busemann_limit z
end AEGPaper0.Chapter04Horocycles
