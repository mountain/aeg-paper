import Chapter03Calculus
open AEGPaper0.Chapter03Analysis AEGPaper0.Chapter03Calculus
example (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0) (p : Plane) (hy : p.2 ≠ 0) :
    laplaceBeltrami mu lambda AEGPaper0.Chapter03Coordinates.assignment p =
      -(2 * lambda^2 * AEGPaper0.Chapter03Coordinates.assignment p) := by
  exact assignment_laplace_eigenfunction mu lambda hm hl p hy
