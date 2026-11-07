import Chapter03Analysis
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.LinearAlgebra.Dimension.Constructions

/- Original CC0 contribution by Codex (OpenAI), 2026-11-07.
   Real smooth surface carrier, actual first/second partial derivatives and
   the divergence-of-gradient coordinate Laplace--Beltrami operator. The
   volume factor is proved to be sqrt(det g), not an assumed target equation. -/
noncomputable section
namespace AEGPaper0.Chapter03Calculus

open AEGPaper0.Chapter03Analysis
open scoped ContDiff Topology Manifold

def upperSurface : TopologicalSpace.Opens Plane := ⟨upper, upper_isOpen⟩

theorem upper_surface_isManifold : IsManifold 𝓘(ℝ, Plane) ∞ upperSurface := inferInstance

theorem surface_dimension : Module.finrank ℝ Plane = 2 := by simp

def partialX (f : Plane → ℝ) (p : Plane) : ℝ := deriv (fun x => f (x, p.2)) p.1
def partialY (f : Plane → ℝ) (p : Plane) : ℝ := deriv (fun y => f (p.1, y)) p.2

theorem assignment_hasDerivAt_x (x y : ℝ) :
    HasDerivAt (fun u => Chapter03Coordinates.assignment (u, y)) (-1 / y) x := by
  exact (hasDerivAt_id x).neg.div_const y

theorem assignment_partialX (p : Plane) : partialX Chapter03Coordinates.assignment p = -1 / p.2 :=
  (assignment_hasDerivAt_x p.1 p.2).deriv

theorem assignment_hasDerivAt_y (x y : ℝ) (hy : y ≠ 0) :
    HasDerivAt (fun v => Chapter03Coordinates.assignment (x, v)) (x / y^2) y := by
  convert (hasDerivAt_const y (-x)).div (hasDerivAt_id y) hy using 1
  simp

theorem assignment_partialY (p : Plane) (hy : p.2 ≠ 0) :
    partialY Chapter03Coordinates.assignment p = p.1 / p.2^2 :=
  (assignment_hasDerivAt_y p.1 p.2 hy).deriv

theorem assignment_partialXX (p : Plane) :
    partialX (partialX Chapter03Coordinates.assignment) p = 0 := by
  change deriv (fun x => partialX Chapter03Coordinates.assignment (x, p.2)) p.1 = 0
  simp only [assignment_partialX]
  exact deriv_const p.1 _

theorem assignment_partialY_hasDerivAt (p : Plane) (hy : p.2 ≠ 0) :
    HasDerivAt (fun y => partialY Chapter03Coordinates.assignment (p.1, y))
      (-2 * p.1 / p.2^3) p.2 := by
  have h : HasDerivAt (fun y : ℝ => p.1 / y^2) (-2 * p.1 / p.2^3) p.2 := by
    convert (hasDerivAt_const p.2 p.1).div ((hasDerivAt_id p.2).pow 2) (pow_ne_zero 2 hy) using 1
    simp only [id_eq, Pi.pow_apply, zero_mul, zero_sub, mul_one]
    field_simp
    ring
  apply h.congr_of_eventuallyEq
  filter_upwards [eventually_ne_nhds hy] with y hne
  exact assignment_partialY (p.1, y) hne

theorem assignment_partialYY (p : Plane) (hy : p.2 ≠ 0) :
    partialY (partialY Chapter03Coordinates.assignment) p = -2 * p.1 / p.2^3 :=
  (assignment_partialY_hasDerivAt p hy).deriv

def metricDeterminant (mu lambda : ℝ) (p : Plane) : ℝ :=
  metricTensor mu lambda p (1, 0) (1, 0) * metricTensor mu lambda p (0, 1) (0, 1) -
    metricTensor mu lambda p (1, 0) (0, 1) * metricTensor mu lambda p (0, 1) (1, 0)
def volumeDensity (mu lambda : ℝ) (p : Plane) : ℝ := 1 / (mu * lambda * p.2^2)

theorem metric_determinant (mu lambda : ℝ) (p : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    metricDeterminant mu lambda p = 1 / (mu^2 * lambda^2 * p.2^4) := by
  simp [metricDeterminant, metric_tensor_apply, Chapter03Coordinates.metric]
  field_simp

theorem volume_density_is_sqrt_determinant (mu lambda : ℝ) (p : Plane)
    (hm : 0 < mu) (hl : 0 < lambda) (hy : p.2 ≠ 0) :
    volumeDensity mu lambda p = Real.sqrt (metricDeterminant mu lambda p) := by
  have hv : 0 ≤ volumeDensity mu lambda p := by
    unfold volumeDensity
    positivity
  have hs : (volumeDensity mu lambda p)^2 = metricDeterminant mu lambda p := by
    rw [metric_determinant mu lambda p (ne_of_gt hm) (ne_of_gt hl) hy]
    unfold volumeDensity
    field_simp
  rw [← hs, Real.sqrt_sq hv]

theorem density_inverse_xx (mu lambda : ℝ) (p : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    volumeDensity mu lambda p * (mu^2 * p.2^2) = mu / lambda := by
  unfold volumeDensity
  field_simp

theorem density_inverse_yy (mu lambda : ℝ) (p : Plane)
    (hm : mu ≠ 0) (hl : lambda ≠ 0) (hy : p.2 ≠ 0) :
    volumeDensity mu lambda p * (lambda^2 * p.2^2) = lambda / mu := by
  unfold volumeDensity
  field_simp

/- The sign is div(grad), exactly the manuscript's displayed coordinate
   convention. This is a definition of that operator, not an eigenvalue axiom. -/
def laplaceBeltrami (mu lambda : ℝ) (f : Plane → ℝ) (p : Plane) : ℝ :=
  (partialX (fun q => (volumeDensity mu lambda q * (mu^2 * q.2^2)) * partialX f q) p +
   partialY (fun q => (volumeDensity mu lambda q * (lambda^2 * q.2^2)) * partialY f q) p) /
    volumeDensity mu lambda p

theorem laplace_coordinate_reduction (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0)
    (f : Plane → ℝ) (p : Plane) (hy : p.2 ≠ 0)
    (hxx : DifferentiableAt ℝ (fun x => partialX f (x, p.2)) p.1)
    (hyy : DifferentiableAt ℝ (fun y => partialY f (p.1, y)) p.2) :
    laplaceBeltrami mu lambda f p =
      mu^2 * p.2^2 * partialX (partialX f) p + lambda^2 * p.2^2 * partialY (partialY f) p := by
  have hx : partialX (fun q => (volumeDensity mu lambda q * (mu^2 * q.2^2)) * partialX f q) p =
      (mu / lambda) * partialX (partialX f) p := by
    change deriv (fun x => (volumeDensity mu lambda (x, p.2) * (mu^2 * p.2^2)) * partialX f (x, p.2)) p.1 = _
    have he : (fun x => (volumeDensity mu lambda (x, p.2) * (mu^2 * p.2^2)) * partialX f (x, p.2)) =
        (fun x => (mu / lambda) * partialX f (x, p.2)) := by
      funext x
      rw [density_inverse_xx mu lambda (x, p.2) hm hl hy]
    rw [he]
    exact (hxx.hasDerivAt.const_mul (mu / lambda)).deriv
  have hlocal : (fun y => (volumeDensity mu lambda (p.1, y) * (lambda^2 * y^2)) * partialY f (p.1, y)) =ᶠ[𝓝 p.2]
      (fun y => (lambda / mu) * partialY f (p.1, y)) := by
    filter_upwards [eventually_ne_nhds hy] with y hne
    rw [density_inverse_yy mu lambda (p.1, y) hm hl hne]
  have hyy' : partialY (fun q => (volumeDensity mu lambda q * (lambda^2 * q.2^2)) * partialY f q) p =
      (lambda / mu) * partialY (partialY f) p := by
    change deriv _ p.2 = _
    rw [hlocal.deriv_eq]
    exact (hyy.hasDerivAt.const_mul (lambda / mu)).deriv
  rw [laplaceBeltrami, hx, hyy']
  unfold volumeDensity
  field_simp

theorem assignment_laplace_eigenfunction (mu lambda : ℝ) (hm : mu ≠ 0) (hl : lambda ≠ 0)
    (p : Plane) (hy : p.2 ≠ 0) :
    laplaceBeltrami mu lambda Chapter03Coordinates.assignment p =
      2 * lambda^2 * Chapter03Coordinates.assignment p := by
  have hxx : DifferentiableAt ℝ (fun x => partialX Chapter03Coordinates.assignment (x, p.2)) p.1 := by
    simp only [assignment_partialX]
    exact differentiableAt_const _
  rw [laplace_coordinate_reduction mu lambda hm hl _ p hy hxx
    (assignment_partialY_hasDerivAt p hy).differentiableAt,
    assignment_partialXX, assignment_partialYY p hy]
  unfold Chapter03Coordinates.assignment
  field_simp
  ring

#print axioms upper_surface_isManifold
#print axioms surface_dimension
#print axioms assignment_hasDerivAt_x
#print axioms assignment_partialX
#print axioms assignment_hasDerivAt_y
#print axioms assignment_partialY
#print axioms assignment_partialXX
#print axioms assignment_partialY_hasDerivAt
#print axioms assignment_partialYY
#print axioms metric_determinant
#print axioms volume_density_is_sqrt_determinant
#print axioms density_inverse_xx
#print axioms density_inverse_yy
#print axioms laplace_coordinate_reduction
#print axioms assignment_laplace_eigenfunction
end AEGPaper0.Chapter03Calculus
