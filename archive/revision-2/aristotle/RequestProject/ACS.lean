/-
# Arithmetic Expression Geometry I: Foundations
## Accumulative Commutative Space and Arithmetic Torsion (§4)

Formalization of the ACS evaluation formula, torsion independence from
the initial value, and the discrete evaluation identity.
-/
import Mathlib

noncomputable section

open Real BigOperators Finset

/-! ## Arithmetic paths and evaluation (§4.1–4.2)

An arithmetic path is a finite sequence of steps, each either
additive (⊕_μ) or multiplicative (⊗_l).
-/

inductive AEG.Step where
  | add (mu : ℝ)
  | mul (l : ℝ)

def AEG.Step.apply : AEG.Step → ℝ → ℝ
  | .add mu, x => x + mu
  | .mul l, x => exp l * x

def AEG.eval (path : List AEG.Step) (x : ℝ) : ℝ :=
  path.foldl (fun acc s => s.apply acc) x

def AEG.totalMulCharge : List AEG.Step → ℝ
  | [] => 0
  | (.mul l) :: rest => l + AEG.totalMulCharge rest
  | (.add _) :: rest => AEG.totalMulCharge rest

def AEG.globalTorsion (path : List AEG.Step) (x : ℝ) : ℝ :=
  AEG.eval path x - AEG.eval path.reverse x

/-! ## Evaluation formula (Proposition 4.1) -/

def AEG.futureMulCharge (path : List AEG.Step) (j : ℕ) : ℝ :=
  AEG.totalMulCharge (path.drop (j + 1))

def AEG.weightedAdditiveSum : List AEG.Step → ℝ
  | [] => 0
  | (.add mu) :: rest => mu * exp (AEG.totalMulCharge rest) + AEG.weightedAdditiveSum rest
  | (.mul _) :: rest => AEG.weightedAdditiveSum rest

/-! ## Two-step and three-step examples -/

theorem AEG.eval_add_mul (mu l x : ℝ) :
    AEG.eval [.add mu, .mul l] x = exp l * (x + mu) := by rfl

theorem AEG.eval_mul_add (mu l x : ℝ) :
    AEG.eval [.mul l, .add mu] x = exp l * x + mu := by rfl

theorem AEG.torsion_two_step (mu l x : ℝ) :
    AEG.globalTorsion [.add mu, .mul l] x = mu * (exp l - 1) := by
  unfold globalTorsion; unfold eval; norm_num [Step.apply]; ring

theorem AEG.torsion_two_step_independent (mu l x₁ x₂ : ℝ) :
    AEG.globalTorsion [.add mu, .mul l] x₁ =
    AEG.globalTorsion [.add mu, .mul l] x₂ := by
  simp [torsion_two_step]

theorem AEG.eval_three_step (mu1 l mu2 x : ℝ) :
    AEG.eval [.add mu1, .mul l, .add mu2] x = exp l * (x + mu1) + mu2 := by rfl

theorem AEG.eval_three_step_rev (mu1 l mu2 x : ℝ) :
    AEG.eval [.add mu2, .mul l, .add mu1] x = exp l * (x + mu2) + mu1 := by rfl

/-! ## Discrete weighted sum theorem (Proposition 4.1, algebraic form) -/

theorem AEG.eval_weightedAdditiveSum (path : List AEG.Step) (x : ℝ) :
    AEG.eval path x =
      exp (AEG.totalMulCharge path) * x + AEG.weightedAdditiveSum path := by
  induction' path with s path ih generalizing x
  · simp [eval, totalMulCharge, weightedAdditiveSum]
  · cases s <;>
      simp_all +decide [AEG.eval, AEG.totalMulCharge, AEG.weightedAdditiveSum] <;> ring!
    · rw [AEG.Step.apply]; ring!
    · unfold AEG.Step.apply; rw [Real.exp_add]; ring

theorem AEG.eval_weightedAdditiveSum_three_step (mu1 l mu2 x : ℝ) :
    AEG.eval [.add mu1, .mul l, .add mu2] x =
      exp (AEG.totalMulCharge [.add mu1, .mul l, .add mu2]) * x
        + AEG.weightedAdditiveSum [.add mu1, .mul l, .add mu2] :=
  AEG.eval_weightedAdditiveSum _ _

theorem AEG.torsion_three_step (mu1 l mu2 x : ℝ) :
    AEG.globalTorsion [.add mu1, .mul l, .add mu2] x = (mu1 - mu2) * (exp l - 1) := by
  unfold globalTorsion; unfold eval; norm_num [Step.apply]; ring

/-! ## Geometry scaffold (§4, geometric layer)

Interpret the ACS path in the (A, M)-plane and define the discrete
line integral of the 1-form η = e^M dA along the axis-aligned path.
-/

def AEG.stateAfter (init : ℝ × ℝ) : List AEG.Step → ℝ × ℝ
  | [] => init
  | (.add mu) :: rest => AEG.stateAfter (init.1 + mu, init.2) rest
  | (.mul l) :: rest => AEG.stateAfter (init.1, init.2 + l) rest

def AEG.vertices (init : ℝ × ℝ) : List AEG.Step → List (ℝ × ℝ)
  | [] => [init]
  | (.add mu) :: rest => init :: AEG.vertices (init.1 + mu, init.2) rest
  | (.mul l) :: rest => init :: AEG.vertices (init.1, init.2 + l) rest

/-- Discrete line integral of η = e^M dA along an axis-aligned ACS path,
with M₀ as the current multiplicative height. -/
def AEG.acsEtaIntegralAux : ℝ → List AEG.Step → ℝ
  | _, [] => 0
  | M, (.add mu) :: rest => exp M * mu + AEG.acsEtaIntegralAux M rest
  | M, (.mul l) :: rest => AEG.acsEtaIntegralAux (M + l) rest

def AEG.acsEtaIntegral (path : List AEG.Step) : ℝ :=
  AEG.acsEtaIntegralAux 0 path

theorem AEG.acsEtaIntegralAux_shift (M₀ M : ℝ) (path : List AEG.Step) :
    AEG.acsEtaIntegralAux (M₀ + M) path =
      exp M₀ * AEG.acsEtaIntegralAux M path := by
  have h_ind : ∀ (M₀ M : ℝ) (path : List AEG.Step),
      AEG.acsEtaIntegralAux (M₀ + M) path =
        Real.exp M₀ * AEG.acsEtaIntegralAux M path := by
    intros M₀ M path
    induction' path with step path ih generalizing M₀ M
    · simp [AEG.acsEtaIntegralAux]
    · cases step <;> simp [AEG.acsEtaIntegralAux]
      · rw [ih, Real.exp_add]; ring
      · convert ih M₀ (M + ‹_›) using 1; ring
  exact h_ind M₀ M path

/-
PROVIDED SOLUTION
Induction on path. Nil: both sides are 0 by definition. Cons s rest ih: case split on s. For .add mu: (s :: rest).reverse = rest.reverse ++ [.add mu]. Unfold weightedAdditiveSum to get mu * exp(totalMulCharge rest) + weightedAdditiveSum rest. By IH, weightedAdditiveSum rest = acsEtaIntegral rest.reverse. Need helper: acsEtaIntegralAux M (xs ++ [.add mu]) = acsEtaIntegralAux M xs + exp(M + totalMulCharge xs) * mu (by induction on xs). Also need: totalMulCharge xs.reverse = totalMulCharge xs (by induction on xs, using helpers for totalMulCharge of append). For .mul l: (s :: rest).reverse = rest.reverse ++ [.mul l]. weightedAdditiveSum (.mul l :: rest) = weightedAdditiveSum rest. Need helper: acsEtaIntegralAux M (xs ++ [.mul l]) = acsEtaIntegralAux M xs (by induction on xs). Then apply IH.
-/
theorem AEG.acsEtaIntegral_reverse_eq_weightedAdditiveSum (path : List AEG.Step) :
    AEG.acsEtaIntegral path.reverse = AEG.weightedAdditiveSum path := by
  -- By induction on the path, we can show that the acsEtaIntegral of the reversed path is equal to the weightedAdditiveSum of the original path.
  induction' path with s path ih;
  · rfl;
  · cases s <;> simp_all +decide [ acsEtaIntegral, weightedAdditiveSum ];
    · -- By definition of `acsEtaIntegralAux`, we can split the integral into the sum of the integrals over the reversed path and the added step.
      have h_split : ∀ (path : List Step) (mu : ℝ) (M : ℝ), AEG.acsEtaIntegralAux M (path ++ [Step.add mu]) = AEG.acsEtaIntegralAux M path + Real.exp (M + AEG.totalMulCharge path) * mu := by
        intros path mu M; induction' path with s path ih generalizing M <;> simp_all +decide [ acsEtaIntegralAux ] ; ring;
        · exact Or.inl rfl;
        · cases s <;> simp +decide [ acsEtaIntegralAux, ih ] ; ring!;
          exact Or.inl ( by rw [ show totalMulCharge ( Step.mul _ :: path ) = _ + totalMulCharge path from rfl ] ; ring );
      rw [ h_split, ih, mul_comm ];
      -- By definition of `totalMulCharge`, we know that `totalMulCharge path.reverse = totalMulCharge path`.
      have h_totalMulCharge_rev : ∀ (path : List Step), AEG.totalMulCharge path.reverse = AEG.totalMulCharge path := by
        intro path; induction' path using List.reverseRecOn with s path ih; aesop;
        cases path <;> simp_all +decide [ totalMulCharge ];
        · -- By definition of `totalMulCharge`, adding an additive step does not change the total multiplicative charge.
          have h_totalMulCharge_add : ∀ (path : List Step) (mu : ℝ), totalMulCharge (path ++ [Step.add mu]) = totalMulCharge path := by
            intros path mu; induction' path with s path ih <;> simp_all +decide [ totalMulCharge ] ;
            cases s <;> simp_all +decide [ totalMulCharge ];
          rw [ h_totalMulCharge_add ];
        · -- By definition of `totalMulCharge`, we know that `totalMulCharge (s ++ [Step.mul l]) = totalMulCharge s + l`.
          have h_totalMulCharge_append : ∀ (s : List Step) (l : ℝ), AEG.totalMulCharge (s ++ [Step.mul l]) = AEG.totalMulCharge s + l := by
            intros s l; induction' s with s ih generalizing l <;> simp_all +decide [ totalMulCharge ] ; ring;
            cases s <;> simp_all +decide [ totalMulCharge ] ; ring;
          rw [ h_totalMulCharge_append, add_comm ]
      rw [h_totalMulCharge_rev]
      ring!;
    · -- By definition of `acsEtaIntegralAux`, we can split the integral into the integral of `path.reverse` and the integral of `[Step.mul l]`.
      have h_split : acsEtaIntegralAux 0 (path.reverse ++ [Step.mul ‹_›]) = acsEtaIntegralAux 0 path.reverse := by
        -- By definition of `acsEtaIntegralAux`, we can split the integral into the integral of `path.reverse` and the integral of `[Step.mul l]` using the recursive definition.
        have h_split : ∀ (M : ℝ) (xs : List AEG.Step) (l : ℝ), acsEtaIntegralAux M (xs ++ [Step.mul l]) = acsEtaIntegralAux M xs := by
          intros M xs l; induction' xs with s xs ih generalizing M; aesop;
          cases s <;> simp_all +decide [ acsEtaIntegralAux ];
        exact h_split _ _ _;
      linarith

/-- The evaluation formula in geometric form:
  ν_x(γ) = e^{M_γ} · x + ∫_{C_{γ̄}} e^M dA -/
theorem AEG.eval_eq_expMulCharge_mul_add_integral (path : List AEG.Step) (x : ℝ) :
    AEG.eval path x =
      exp (AEG.totalMulCharge path) * x + AEG.acsEtaIntegral path.reverse := by
  rw [AEG.acsEtaIntegral_reverse_eq_weightedAdditiveSum]
  exact AEG.eval_weightedAdditiveSum path x

/-! ## Connecting to analytic integrals (optional, incremental) -/

theorem AEG.horizontal_segment_integral (M₀ mu : ℝ) :
    ∫ t in (0 : ℝ)..mu, exp M₀ = exp M₀ * mu := by
  norm_num [mul_comm]

end