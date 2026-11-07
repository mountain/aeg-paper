import Chapter03Coordinates
open Lean.Grind AEGPaper0.Chapter03Coordinates

/- Deliberate negative control: ordinary orthonormality lacks orientation. -/
example {A : Type} [Field A] (mu lambda a q : A) (hq : q ≠ 0) (f : Frame A)
    (hf : dot f.u f.u = 1 ∧ dot f.v f.v = 1 ∧ dot f.u f.v = 0)
    (hu : q * f.u.1 = mu) (hv : q * f.v.1 = lambda * a) :
    f = canonicalFrame mu lambda a q := by
  exact canonical_frame_unique mu lambda a q hq f hf hu hv
