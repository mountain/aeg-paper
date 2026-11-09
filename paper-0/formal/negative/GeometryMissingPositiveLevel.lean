import Chapter04Horocycles
namespace AEGPaper0.Chapter04Horocycles
open scoped UpperHalfPlane
example (m : Chapter04Ripples.Coefficients) (t : ℝ)
    (hd : 0 < Chapter04Ripples.determinant m) (hc : m.c ≠ 0) (z : ℍ) :
    (z : ℂ) ∈ Chapter04Ripples.ripple m t ↔
      z ∈ finiteHorosphere (Chapter04Ripples.poleX m)
        (-Real.log (t*m.c^2/Chapter04Ripples.determinant m)) := by
  exact nonaffine_ripple_is_horosphere m t hd
end AEGPaper0.Chapter04Horocycles
