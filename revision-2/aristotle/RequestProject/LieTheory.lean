/-
# Arithmetic Expression Geometry I: Foundations
## Lie-theoretic formulation via Aff(1) (§2.4)

Formalization of the Aff(1) Lie algebra bracket [H,N] = N
and the flow equation as the translation component of a
left-invariant evolution on the affine group.
-/
import Mathlib

noncomputable section

open Matrix Real

/-! ## The Lie algebra 𝔞𝔣𝔣(1) (§2.4)

The Lie algebra of Aff(1) has basis H = [[1,0],[0,0]] and N = [[0,1],[0,0]]
with bracket [H,N] = N.
-/

/-- The Lie algebra element H = [[1,0],[0,0]] -/
def AEG.Aff1.H : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, 0]

/-- The Lie algebra element N = [[0,1],[0,0]] -/
def AEG.Aff1.N : Matrix (Fin 2) (Fin 2) ℝ := !![0, 1; 0, 0]

/-
PROBLEM
The Lie bracket [H,N] = HN − NH = N.
This is the fundamental bracket relation of 𝔞𝔣𝔣(1).

PROVIDED SOLUTION
Compute HN and NH as 2x2 matrices using the !! notation. HN = !![0,1;0,0] = N. NH = !![0,0;0,0] = 0. So HN - NH = N. Use ext, fin_cases, simp.
-/
theorem AEG.Aff1.bracket_H_N :
    AEG.Aff1.H * AEG.Aff1.N - AEG.Aff1.N * AEG.Aff1.H = AEG.Aff1.N := by
  -- By definition of matrix multiplication, we can compute H * N and N * H.
  ext i j; fin_cases i <;> fin_cases j <;> norm_num [ Matrix.mul_apply, AEG.Aff1.H, AEG.Aff1.N ]

/-
PROBLEM
H² = H (idempotent)

PROVIDED SOLUTION
H = !![1,0;0,0]. H*H has (i,j) entry = sum_k H(i,k)*H(k,j). Use ext i j, fin_cases i, fin_cases j, then norm_num with H and Matrix.mul_apply and Fin.sum_univ_two.
-/
theorem AEG.Aff1.H_sq :
    AEG.Aff1.H * AEG.Aff1.H = AEG.Aff1.H := by
  ext i j ; fin_cases i <;> fin_cases j <;> norm_num [ Matrix.mul_apply, Fin.sum_univ_succ ];
  · unfold H; norm_num;
  · unfold H; norm_num;
  · simp [AEG.Aff1.H];
  · unfold H; norm_num;

/-
PROBLEM
N² = 0 (nilpotent)

PROVIDED SOLUTION
ext, fin_cases, simp [AEG.Aff1.N, Matrix.mul_apply, Fin.sum_univ_two]
-/
theorem AEG.Aff1.N_sq :
    AEG.Aff1.N * AEG.Aff1.N = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp +decide [ N, Fin.sum_univ_two ] ;

/-
PROBLEM
HN = N

PROVIDED SOLUTION
ext, fin_cases, simp [AEG.Aff1.H, AEG.Aff1.N, Matrix.mul_apply, Fin.sum_univ_two]
-/
theorem AEG.Aff1.H_mul_N :
    AEG.Aff1.H * AEG.Aff1.N = AEG.Aff1.N := by
  ext i j ; fin_cases i <;> fin_cases j <;> norm_num [ H, N ]

/-
PROBLEM
NH = 0

PROVIDED SOLUTION
ext, fin_cases, simp [AEG.Aff1.N, AEG.Aff1.H, Matrix.mul_apply, Fin.sum_univ_two]
-/
theorem AEG.Aff1.N_mul_H :
    AEG.Aff1.N * AEG.Aff1.H = 0 := by
  ext i j ; fin_cases i <;> fin_cases j <;> norm_num [ AEG.Aff1.N, AEG.Aff1.H, Matrix.mul_apply ]

/-! ## The direction-dependent Lie algebra element Ω(θ) (§2.4, eq. 2.8)

Ω(θ) = l sin θ · H + μ cos θ · N
-/

/-- The direction-dependent Lie algebra element Ω(θ) = l sin θ · H + μ cos θ · N -/
def AEG.Aff1.Omega (mu l theta : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  (l * sin theta) • AEG.Aff1.H + (mu * cos theta) • AEG.Aff1.N

/-
PROBLEM
Ω(θ) has the explicit matrix form [[l sin θ, μ cos θ], [0, 0]]

PROVIDED SOLUTION
Unfold Omega, H, N. Use ext, fin_cases, simp, ring.
-/
theorem AEG.Aff1.Omega_eq (mu l theta : ℝ) :
    AEG.Aff1.Omega mu l theta = !![l * sin theta, mu * cos theta; 0, 0] := by
  unfold Omega H N;
  ext i j ; fin_cases i <;> fin_cases j <;> norm_num

/-! ## Affine group multiplication law

The group law of Aff(1): (Φ₁,a₁)(Φ₂,a₂) = (Φ₁Φ₂, a₁ + Φ₁a₂).
We verify this as matrix multiplication.
-/

/-- An element of Aff(1) as a 2×2 matrix [[Φ,a],[0,1]] -/
def AEG.Aff1.elem (phi a : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![phi, a; 0, 1]

/-
PROBLEM
The affine group multiplication law:
[[Φ₁,a₁],[0,1]] · [[Φ₂,a₂],[0,1]] = [[Φ₁Φ₂, a₁+Φ₁a₂],[0,1]]

PROVIDED SOLUTION
Unfold elem. Use ext, fin_cases, simp [Matrix.mul_apply, Fin.sum_univ_two], ring.
-/
theorem AEG.Aff1.mul_law (phi1 a1 phi2 a2 : ℝ) :
    AEG.Aff1.elem phi1 a1 * AEG.Aff1.elem phi2 a2 =
    AEG.Aff1.elem (phi1 * phi2) (a1 + phi1 * a2) := by
  unfold elem; norm_num [ Fin.sum_univ_two, Matrix.mul_apply ] ; ring;

end