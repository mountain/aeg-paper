import Chapter04PoleReading
namespace AEGPaper0.Chapter04PoleReading
open ProjectiveBruhat
variable {K : Type*} [Field K]
example (a : K) (u : Kˣ) (t : K) : quotientPole (bruhatWord a u t)=some t := by
  exact rightmost_translation_reads_pole a u t
end AEGPaper0.Chapter04PoleReading
