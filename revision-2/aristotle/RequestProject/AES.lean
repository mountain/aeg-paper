/-
# Arithmetic Expression Geometry I: Foundations
## Arithmetic Expression Spaces (§3)

Formalization of the AES definition and model space verifications.
-/
import Mathlib

noncomputable section

open Real

/-! ## AES eikonal relation (Definition 3.1)

An AES satisfies ‖∇a‖² = μ² + l²a².
We verify this for the model spaces 𝔈₀ and 𝔈₁.
-/

/-! ### Model space 𝔈₀ (Theorem 3.1)

On the upper half-plane with metric g = (1/y²)(dx²/μ² + dy²/l²)
and assignment a(x,y) = −x/y, the eikonal relation holds:
  μ²y²·(∂ₓa)² + l²y²·(∂ᵧa)² = μ² + l²a²

where ∂ₓa = −1/y, ∂ᵧa = x/y².
-/

/-- The assignment field on 𝔈₀: a(x,y) = −x/y -/
def AEG.E0.assignment (x y : ℝ) : ℝ := -x / y

/-- Partial derivative of a with respect to x: ∂ₓa = −1/y -/
def AEG.E0.da_dx (_x y : ℝ) : ℝ := -1 / y

/-- Partial derivative of a with respect to y: ∂ᵧa = x/y² -/
def AEG.E0.da_dy (x y : ℝ) : ℝ := x / y ^ 2

/-
PROBLEM
Theorem 3.1: 𝔈₀ is an AES.
The eikonal relation μ²y²(∂ₓa)² + l²y²(∂ᵧa)² = μ² + l²a²
holds for a(x,y) = −x/y on the upper half-plane.

PROVIDED SOLUTION
Unfold all definitions. LHS = mu^2 * y^2 * (1/y)^2 + l^2 * y^2 * (x/y^2)^2 = mu^2 + l^2*x^2/y^2 = mu^2 + l^2*(x/y)^2. Use field_simp and ring.
-/
theorem AEG.E0.eikonal (mu l x y : ℝ) (hy : y ≠ 0) :
    mu ^ 2 * y ^ 2 * (AEG.E0.da_dx x y) ^ 2 +
    l ^ 2 * y ^ 2 * (AEG.E0.da_dy x y) ^ 2 =
    mu ^ 2 + l ^ 2 * (AEG.E0.assignment x y) ^ 2 := by
  unfold AEG.E0.da_dx AEG.E0.da_dy AEG.E0.assignment; ring; norm_num [ hy ] ; ring;
  grind

/-! ### Rectified assignment (Definition 3.2, Lemma 3.1)

f = arcsinh(l·a/μ) satisfies ‖∇f‖ = l.
We verify the chain-rule relation:
  (l/√(μ²+l²a²))² · (μ²+l²a²) = l²
-/

/-
PROBLEM
Lemma 3.1 (rectified gradient norm): The chain rule gives
  ∇f = (l/√(μ²+l²a²))·∇a, so ‖∇f‖² = l².

PROVIDED SOLUTION
(l/√(S))^2 * S = l^2/S * S = l^2 where S = mu^2 + l^2*a^2 > 0. Use div_pow, sq_sqrt, div_mul_cancel₀.
-/
theorem AEG.rectified_gradient_factor (mu l a : ℝ) (_hmu : mu ≠ 0)
    (hpos : 0 < mu ^ 2 + l ^ 2 * a ^ 2) :
    (l / Real.sqrt (mu ^ 2 + l ^ 2 * a ^ 2)) ^ 2 *
    (mu ^ 2 + l ^ 2 * a ^ 2) = l ^ 2 := by
  rw [ div_pow, Real.sq_sqrt hpos.le, div_mul_cancel₀ _ hpos.ne' ]

/-! ### Model space 𝔈₁ (Lemma 3.2)

On the Poincaré disc with curvature −l² and assignment
a(r) = (μ/l)·(2r/(1−r²)), the eikonal relation holds.

The verification: (l²/4)(1−r²)²·a_r² = μ²(1+r²)²/(1−r²)²
where a_r = (2μ/l)·(1+r²)/(1−r²)².
-/

/-- The assignment field on 𝔈₁: a(r) = (μ/l)·(2r/(1−r²)) -/
def AEG.E1.assignment (mu l r : ℝ) : ℝ := (mu / l) * (2 * r / (1 - r ^ 2))

/-- The radial derivative: a_r = (2μ/l)·(1+r²)/(1−r²)² -/
def AEG.E1.da_dr (mu l r : ℝ) : ℝ := (2 * mu / l) * ((1 + r ^ 2) / (1 - r ^ 2) ^ 2)

/-
PROBLEM
Lemma 3.2: 𝔈₁ satisfies the AES eikonal relation on the punctured disc.
  (l²/4)(1−r²)² · a_r² = μ² + l² · a(r)²

PROVIDED SOLUTION
Unfold da_dr and assignment. Both sides simplify to mu^2*(1+r^2)^2/(1-r^2)^2. Use field_simp and ring.
-/
theorem AEG.E1.eikonal (mu l r : ℝ) (hl : l ≠ 0) (hr : 1 - r ^ 2 ≠ 0) :
    (l ^ 2 / 4) * (1 - r ^ 2) ^ 2 * (AEG.E1.da_dr mu l r) ^ 2 =
    mu ^ 2 + l ^ 2 * (AEG.E1.assignment mu l r) ^ 2 := by
  -- Expand both sides of the equation using the definitions of `da_dr` and `assignment`.
  simp [da_dr, assignment]
  field_simp
  ring

/-! ### Hyperbolic sine growth law (eq. 3.5)

When propagation starts from a = 0 along a gradient line:
a(s) = (μ/l)·sinh(l·s)
-/

/-- The hyperbolic sine growth law: a(s) = (μ/l)·sinh(l·s) -/
def AEG.hyperbolic_growth (mu l s : ℝ) : ℝ := (mu / l) * sinh (l * s)

/-
PROBLEM
The growth law satisfies the eikonal along the gradient:
  (μ·cosh(l·s))² = μ² + l²·((μ/l)·sinh(l·s))²

PROVIDED SOLUTION
(mu*cosh(l*s))^2 = mu^2*cosh^2(l*s). RHS = mu^2 + l^2*(mu/l)^2*sinh^2(l*s) = mu^2 + mu^2*sinh^2(l*s) = mu^2*(1+sinh^2(l*s)) = mu^2*cosh^2(l*s). Use cosh_sq'.
-/
theorem AEG.hyperbolic_growth_eikonal (mu l s : ℝ) (hl : l ≠ 0) :
    (mu * cosh (l * s)) ^ 2 =
    mu ^ 2 + l ^ 2 * (AEG.hyperbolic_growth mu l s) ^ 2 := by
  unfold hyperbolic_growth; ring_nf; (
  simpa [ hl, Real.cosh_sq' ] using by ring;);

end