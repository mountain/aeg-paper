import Chapter03Coordinates
open Lean.Grind AEGPaper0.Chapter03Coordinates

/- Deliberate negative control: the nonzero chart height is missing. -/
example {A : Type} [Field A] (s : A) (p : Vec A) :
    assignment (translate s p) = assignment p + s := by
  exact translation_assignment s p
