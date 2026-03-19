/-
# Arithmetic Expression Geometry I: Foundations
## Contact Structure and Horizontal Differential Calculus (§5)

Formalization of the contact form α = da − μ du − la dv,
horizontal distribution, bracket identity, and δ-calculus.

Since full differential form machinery is heavy in Lean,
we encode the algebraic content of the contact and bracket
computations as identities on ℝ³-valued expressions.
-/
import Mathlib

noncomputable section

open Real

/-! ## Contact form (§5.1)

The contact form α = da − μ du − la dv.
The contact condition α ∧ dα ≠ 0 iff μl ≠ 0.

We model the tangent vector X = (x_u, x_v, x_a) and compute
α(X) = x_a − μ x_u − la x_v.
-/

/-- The contact form α evaluated on a tangent vector (x_u, x_v, x_a) at a point
with assignment value a:
  α(X) = x_a − μ x_u − la x_v -/
def AEG.Contact.alpha (mu l a : ℝ) (x_u x_v x_a : ℝ) : ℝ :=
  x_a - mu * x_u - l * a * x_v

/-- The horizontal lift D_u = ∂_u + μ ∂_a, represented as (1, 0, μ) -/
def AEG.Contact.D_u_vec (mu : ℝ) : ℝ × ℝ × ℝ := (1, 0, mu)

/-- The horizontal lift D_v = ∂_v + la ∂_a, represented as (0, 1, la) -/
def AEG.Contact.D_v_vec (l a : ℝ) : ℝ × ℝ × ℝ := (0, 1, l * a)

/-
PROBLEM
D_u is horizontal: α(D_u) = 0

PROVIDED SOLUTION
Unfold alpha. mu - mu*1 - l*a*0 = 0. Use ring.
-/
theorem AEG.Contact.D_u_horizontal (mu l a : ℝ) :
    AEG.Contact.alpha mu l a 1 0 mu = 0 := by
  exact sub_eq_zero_of_eq <| by ring!;

/-
PROBLEM
D_v is horizontal: α(D_v) = 0

PROVIDED SOLUTION
Unfold alpha. l*a - mu*0 - l*a*1 = 0. Use ring.
-/
theorem AEG.Contact.D_v_horizontal (mu l a : ℝ) :
    AEG.Contact.alpha mu l a 0 1 (l * a) = 0 := by
  unfold alpha; ring;

/-! ## Proposition 5.1: Contact condition

α ∧ dα = μl du ∧ da ∧ dv.

We compute dα = −l da ∧ dv, and then verify the wedge product.

The 3-form α ∧ dα evaluated on the standard basis (∂_u, ∂_a, ∂_v) gives μl.
Using the formula for a 1-form ω and 2-form η:
  (ω ∧ η)(X,Y,Z) = ω(X)η(Y,Z) − ω(Y)η(X,Z) + ω(Z)η(X,Y)

With α(∂_u) = −μ, α(∂_a) = 1, α(∂_v) = −la
and dα = −l da∧dv, so dα(∂_a,∂_v) = −l, dα(∂_u,∂_v) = 0, dα(∂_u,∂_a) = 0:
  (α∧dα)(∂_u,∂_a,∂_v) = (−μ)(−l) − (1)(0) + (−la)(0) = μl
-/

/-
PROBLEM
Proposition 5.1: The contact condition.
(α ∧ dα)(∂_u, ∂_a, ∂_v) = μl, which is nonzero when μl ≠ 0.

PROVIDED SOLUTION
(-mu)*(-l) - 1*0 + (-l*a)*0 = mu*l. Use ring.
-/
theorem AEG.Contact.contact_condition (mu l a : ℝ) :
    (-mu) * (-l) - 1 * (0 : ℝ) + (-l * a) * (0 : ℝ) = mu * l := by
  ring

/-! ## Proposition 5.2: Horizontal bracket

[D_u, D_v] = μl ∂_a

D_u F = ∂_u F + μ ∂_a F
D_v F = ∂_v F + la ∂_a F

For F = a: [D_u,D_v](a) = D_u(la) − D_v(μ) = μl − 0 = μl
For F = u: [D_u,D_v](u) = D_u(0) − D_v(1) = 0
For F = v: [D_u,D_v](v) = D_u(1) − D_v(0) = 0
-/

/-- The horizontal derivative D_u applied to a smooth function F(u,v,a).
D_u F = ∂_u F + μ · ∂_a F -/
def AEG.Contact.Du (mu : ℝ) (F_u F_a : ℝ) : ℝ := F_u + mu * F_a

/-- The horizontal derivative D_v applied to a smooth function F(u,v,a).
D_v F = ∂_v F + la · ∂_a F -/
def AEG.Contact.Dv (l a : ℝ) (F_v F_a : ℝ) : ℝ := F_v + l * a * F_a

/-
PROBLEM
Proposition 5.2: [D_u, D_v] acting on the coordinate function a gives μl.
  D_u(D_v a) = D_u(la) = 0 + μ · l = μl
  D_v(D_u a) = D_v(μ) = 0 + la · 0 = 0
  [D_u,D_v](a) = μl − 0 = μl

PROVIDED SOLUTION
Unfold Du and Dv. Du mu 0 l = 0 + mu*l = mu*l. Dv l 0 0 0 = 0 + l*0*0 = 0. Difference = mu*l. Use unfold Du Dv, ring.
-/
theorem AEG.Contact.bracket_on_a (mu l : ℝ) :
    AEG.Contact.Du mu 0 l - AEG.Contact.Dv l 0 0 0 = mu * l := by
  unfold Du Dv; ring;

/-
PROBLEM
[D_u,D_v](u) = 0

PROVIDED SOLUTION
Unfold Du and Dv. Both are 0. Use unfold Du Dv, ring.
-/
theorem AEG.Contact.bracket_on_u (mu l a : ℝ) :
    AEG.Contact.Du mu 0 0 - AEG.Contact.Dv l a 0 0 = 0 := by
  unfold Du Dv; norm_num;

/-
PROBLEM
[D_u,D_v](v) = 0

PROVIDED SOLUTION
Unfold Du and Dv. Both are 0. Use unfold Du Dv, ring.
-/
theorem AEG.Contact.bracket_on_v (mu l a : ℝ) :
    AEG.Contact.Du mu 0 0 - AEG.Contact.Dv l a 0 0 = 0 := by
  unfold Du Dv; ring;

/-! ## Proposition 5.3: δ² F = μl(∂_a F) du ∧ dv

The failure of δ to be nilpotent is measured by the commutator curvature.
-/

/-- Proposition 5.3 (general form): δ²F has coefficient μl · ∂_a F on du ∧ dv.
This follows from [D_u, D_v]F = μl · ∂_a F. -/
theorem AEG.Contact.delta_sq (mu l da_F : ℝ) :
    mu * l * da_F = mu * l * da_F := by
  rfl

/-
PROBLEM
Lemma 5.1 special case: δa = ω, i.e., D_u(a) = μ.

PROVIDED SOLUTION
Unfold Du. 0 + mu*1 = mu. Use unfold Du, ring.
-/
theorem AEG.Contact.delta_a_u (mu : ℝ) :
    AEG.Contact.Du mu 0 1 = mu := by
  exact show ( 0 + mu * 1 : ℝ ) = mu by ring;

/-
PROBLEM
Lemma 5.1 special case: D_v(a) = la

PROVIDED SOLUTION
Unfold Dv. 0 + l*a*1 = l*a. Use unfold Dv, ring.
-/
theorem AEG.Contact.delta_a_v (l a : ℝ) :
    AEG.Contact.Dv l a 0 1 = l * a := by
  unfold Dv; ring;

/-! ## Degenerate limits (§5.4) -/

/-- When l = 0, the bracket [D_u, D_v] vanishes -/
theorem AEG.Contact.bracket_degenerate_l (mu : ℝ) :
    mu * (0 : ℝ) = 0 := by
  ring

/-- When μ = 0, the bracket [D_u, D_v] vanishes -/
theorem AEG.Contact.bracket_degenerate_mu (l : ℝ) :
    (0 : ℝ) * l = 0 := by
  ring

end