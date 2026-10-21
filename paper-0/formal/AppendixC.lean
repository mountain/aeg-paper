import Chapter02Domains

/- Original CC0 formalization by Codex (OpenAI).
   Finite chronological induction with explicit algebraic-law parameters.
   Contributions are defined by suffix products, independently of evaluation. -/
namespace AEGPaper0.AppendixC

open AEGPaper0.Chapter02
variable {A : Type u}

abbrev Word (A : Type u) := List (A × A)

def evaluate (s : Algebra A) : Word A → A → A
  | [], x => x
  | (q, mu) :: rest, x => evaluate s rest (s.add (s.mul q x) mu)

def scale (s : Algebra A) : Word A → A
  | [] => s.one
  | (q, _) :: rest => s.mul q (scale s rest)

def sum (s : Algebra A) : List A → A
  | [] => s.zero
  | x :: rest => s.add x (sum s rest)

def contributions (s : Algebra A) : Word A → List A
  | [] => []
  | (_, mu) :: rest => s.mul mu (scale s rest) :: contributions s rest

def events : Word A → List (Op × A)
  | [] => []
  | (q, mu) :: rest => (.mul, q) :: (.add, mu) :: events rest

def NonzeroMultipliers (s : FieldData A) (word : Word A) : Prop :=
  ∀ pair ∈ word, pair.1 ≠ s.zero

theorem evaluate_nil (s : Algebra A) (x : A) : evaluate s [] x = x := rfl

theorem evaluate_append (s : Algebra A) (before after : Word A) (x : A) :
    evaluate s (before ++ after) x = evaluate s after (evaluate s before x) := by
  induction before generalizing x with
  | nil => rfl
  | cons pair rest ih => exact ih (s.add (s.mul pair.1 x) pair.2)

theorem evaluate_snoc (s : Algebra A) (word : Word A) (q mu x : A) :
    evaluate s (word ++ [(q, mu)]) x = s.add (s.mul q (evaluate s word x)) mu :=
  evaluate_append s word [(q, mu)] x

theorem scale_append (s : Algebra A) (before after : Word A) :
    scale s (before ++ after) = s.mul (scale s before) (scale s after) := by
  induction before with
  | nil => exact ((s.mul_comm s.one (scale s after)).trans (s.mul_one (scale s after))).symm
  | cons pair rest ih =>
    simp only [List.cons_append, scale, ih, s.mul_assoc]

theorem scale_snoc (s : Algebra A) (word : Word A) (q mu : A) :
    scale s (word ++ [(q, mu)]) = s.mul q (scale s word) := by
  rw [scale_append]
  simp only [scale, s.mul_one, s.mul_comm (scale s word) q]

theorem contribution_at (s : Algebra A) (word : Word A) (i : Nat) :
    (contributions s word)[i]? =
      word[i]?.map (fun pair => s.mul pair.2 (scale s (word.drop (i + 1)))) := by
  induction word generalizing i with
  | nil => simp [contributions]
  | cons pair rest ih =>
    cases i with
    | zero => rfl
    | succ i => simpa only [contributions, List.getElem?_cons_succ, List.drop_succ_cons] using ih i

theorem expanded_evaluation (s : Algebra A) (word : Word A) (x : A) :
    evaluate s word x = s.add (s.mul (scale s word) x) (sum s (contributions s word)) := by
  induction word generalizing x with
  | nil =>
    exact (((s.mul_comm s.one x).trans (s.mul_one x)).symm).trans
      (s.add_zero (s.mul s.one x)).symm
  | cons pair rest ih =>
    rcases pair with ⟨q, mu⟩
    simp only [evaluate, scale, contributions, sum]
    rw [ih]
    rw [s.mul_add, ← s.mul_assoc, s.mul_comm (scale s rest) q,
        s.mul_comm (scale s rest) mu, s.add_assoc]

theorem perturbation_step (s : Algebra A) (q mu x delta : A) :
    s.add (s.mul q (s.add x delta)) mu =
      s.add (s.add (s.mul q x) mu) (s.mul q delta) := by
  rw [s.mul_add, s.add_assoc, s.add_comm (s.mul q delta) mu, ← s.add_assoc]

theorem additive_perturbation (s : Algebra A) (word : Word A) (x delta : A) :
    evaluate s word (s.add x delta) =
      s.add (evaluate s word x) (s.mul (scale s word) delta) := by
  induction word generalizing x delta with
  | nil => exact (congrArg (s.add x) ((s.mul_comm s.one delta).trans (s.mul_one delta))).symm
  | cons pair rest ih =>
    rcases pair with ⟨q, mu⟩
    simp only [evaluate, scale]
    rw [perturbation_step, ih, ← s.mul_assoc, s.mul_comm (scale s rest) q]

theorem events_length (word : Word A) : (events word).length = word.length * 2 := by
  induction word with
  | nil => rfl
  | cons pair rest ih =>
    simp only [events, List.length_cons, ih, Nat.succ_mul]

theorem events_correspondence (s : FieldData A) (word : Word A) (x r : A) :
    PartialFold (Eval s) (events word) x r ↔ r = evaluate s.toAlgebra word x := by
  induction word generalizing x with
  | nil => rfl
  | cons pair rest ih =>
    rcases pair with ⟨q, mu⟩
    constructor
    · rintro ⟨u, hu, v, hv, h⟩
      change u = s.mul x q at hu
      change v = s.add u mu at hv
      subst u; subst v
      simpa only [evaluate, s.mul_comm x q] using (ih (s.add (s.mul x q) mu)).mp h
    · intro h
      refine ⟨s.mul x q, rfl, s.add (s.mul x q) mu, rfl, ?_⟩
      apply (ih (s.add (s.mul x q) mu)).mpr
      simpa only [evaluate, s.mul_comm x q] using h

theorem tree_correspondence (s : FieldData A) (word : Word A) (x r : A) :
    TreeEval (Eval s) x (leftTree (events word)) r ↔ r = evaluate s.toAlgebra word x :=
  (left_tree_correspondence (Eval s) (events word) x r).trans (events_correspondence s word x r)

def difference (s : FieldData A) (y x : A) : A := s.add y (s.neg x)

def quotient (s : FieldData A) (numerator denominator : A) : A :=
  s.mul numerator (s.inv denominator)

theorem add_left_comm (s : Algebra A) (a b c : A) :
    s.add a (s.add b c) = s.add b (s.add a c) :=
  (s.add_assoc a b c).symm.trans
    ((congrArg (fun t => s.add t c) (s.add_comm a b)).trans (s.add_assoc b a c))

theorem restore_difference (s : FieldData A) (x y : A) :
    s.add x (difference s y x) = y := by
  unfold difference
  rw [add_left_comm s.toAlgebra, s.add_neg, s.add_zero]

theorem difference_of_translation (s : FieldData A) (x delta : A) :
    difference s (s.add x delta) x = delta := by
  unfold difference
  rw [s.add_comm x delta, s.add_assoc, s.add_neg, s.add_zero]

theorem difference_self (s : FieldData A) (x : A) : difference s x x = s.zero := s.add_neg x

theorem exact_difference (s : FieldData A) (word : Word A) (x y : A) :
    difference s (evaluate s.toAlgebra word y) (evaluate s.toAlgebra word x) =
      s.mul (scale s.toAlgebra word) (difference s y x) := by
  have h := additive_perturbation s.toAlgebra word x (difference s y x)
  rw [restore_difference] at h
  rw [h, difference_of_translation]

theorem prefix_difference (s : FieldData A) (word : Word A) (i : Nat) (x y : A) :
    difference s (evaluate s.toAlgebra (word.take i) y) (evaluate s.toAlgebra (word.take i) x) =
      s.mul (scale s.toAlgebra (word.take i)) (difference s y x) :=
  exact_difference s (word.take i) x y

theorem difference_nonzero (s : FieldData A) (x y : A) (hne : y ≠ x) :
    difference s y x ≠ s.zero := by
  intro h
  have restore := restore_difference s x y
  rw [h, s.add_zero] at restore
  exact hne restore.symm

theorem perturbation_ratio (s : FieldData A) (word : Word A) (x y : A) (hne : y ≠ x) :
    quotient s (difference s (evaluate s.toAlgebra word y) (evaluate s.toAlgebra word x))
      (difference s y x) = scale s.toAlgebra word := by
  unfold quotient
  rw [exact_difference, s.mul_assoc, s.mul_inv _ (difference_nonzero s x y hne), s.mul_one]

theorem guarded_ratio (s : FieldData A) (word : Word A) (x y : A) (hne : y ≠ x) :
    Eval s .div (difference s (evaluate s.toAlgebra word y) (evaluate s.toAlgebra word x))
      (difference s y x) (scale s.toAlgebra word) :=
  ⟨difference_nonzero s x y hne, (perturbation_ratio s word x y hne).symm⟩

theorem prefix_ratio (s : FieldData A) (word : Word A) (i : Nat) (x y : A) (hne : y ≠ x) :
    Eval s .div
      (difference s (evaluate s.toAlgebra (word.take i) y) (evaluate s.toAlgebra (word.take i) x))
      (difference s y x) (scale s.toAlgebra (word.take i)) :=
  guarded_ratio s (word.take i) x y hne

theorem diagonal_ratio_undefined (s : FieldData A) (word : Word A) (x r : A) :
    ¬ Eval s .div (difference s (evaluate s.toAlgebra word x) (evaluate s.toAlgebra word x))
      (difference s x x) r := by
  simp only [difference_self]
  exact zero_denominator_refused s _ r

theorem scale_nonzero (s : FieldData A) (word : Word A) (h : NonzeroMultipliers s word) :
    scale s.toAlgebra word ≠ s.zero := by
  induction word with
  | nil => exact fun hz => s.zero_ne_one hz.symm
  | cons pair rest ih =>
    have hq := h pair (List.mem_cons_self ..)
    have ht : NonzeroMultipliers s rest := fun p hp => h p (List.mem_cons_of_mem pair hp)
    intro hz
    exact ih ht (mul_left_cancel s pair.1 hq (hz.trans (s.mul_zero pair.1).symm))

#print axioms evaluate_nil
#print axioms evaluate_append
#print axioms evaluate_snoc
#print axioms scale_append
#print axioms scale_snoc
#print axioms contribution_at
#print axioms expanded_evaluation
#print axioms perturbation_step
#print axioms additive_perturbation
#print axioms events_length
#print axioms events_correspondence
#print axioms tree_correspondence
#print axioms add_left_comm
#print axioms restore_difference
#print axioms difference_of_translation
#print axioms difference_self
#print axioms exact_difference
#print axioms prefix_difference
#print axioms difference_nonzero
#print axioms perturbation_ratio
#print axioms guarded_ratio
#print axioms prefix_ratio
#print axioms diagonal_ratio_undefined
#print axioms scale_nonzero
end AEGPaper0.AppendixC
