import Init

/- Original CC0 formalization by Codex (OpenAI), 2026-10-20.
   The laws below are explicit parameters. No arbitrary-proposition axiom,
   sorry, native_decide, or assumed AEG theorem is used. -/
namespace AEGPaper0

structure Algebra (A : Type u) where
  add : A → A → A
  mul : A → A → A
  zero : A
  one : A
  add_assoc : ∀ a b c, add (add a b) c = add a (add b c)
  add_comm : ∀ a b, add a b = add b a
  add_zero : ∀ a, add a zero = a
  mul_assoc : ∀ a b c, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b, mul a b = mul b a
  mul_one : ∀ a, mul a one = a
  mul_add : ∀ a b c, mul a (add b c) = add (mul a b) (mul a c)
  mul_zero : ∀ a, mul a zero = zero

variable {A : Type u} (s : Algebra A)

theorem addition_opposition (a b : A) : s.add a b = s.add b a := s.add_comm a b

theorem multiplication_opposition (a b : A) : s.mul a b = s.mul b a := s.mul_comm a b

theorem distributive_operator (k z p : A) :
    s.mul k (s.add z p) = s.add (s.mul k z) (s.mul k p) := s.mul_add k z p

theorem right_distributivity (a b c : A) :
    s.mul (s.add a b) c = s.add (s.mul a c) (s.mul b c) :=
  (s.mul_comm (s.add a b) c).trans ((s.mul_add c a b).trans
    ((congrArg (fun t => s.add t (s.mul c b)) (s.mul_comm c a)).trans
     (congrArg (fun t => s.add (s.mul a c) t) (s.mul_comm c b))))

theorem affine_composition (a b d e z : A) :
    s.add (s.mul d (s.add (s.mul a z) b)) e =
      s.add (s.mul (s.mul d a) z) (s.add (s.mul d b) e) :=
  (congrArg (fun t => s.add t e) (s.mul_add d (s.mul a z) b)).trans
    ((congrArg (fun t => s.add (s.add t (s.mul d b)) e)
      (s.mul_assoc d a z).symm).trans
      (s.add_assoc (s.mul (s.mul d a) z) (s.mul d b) e))

/- Pure-comb grammars use chronological fold order. This gives a separate
   Lean proof of the grammar opposition; it is not an Adva-checked result. -/
def leftComb {S : Type v} (op : S → A → A → A) (word : List (S × A)) (z : A) : A :=
  word.foldl (fun x sc => op sc.1 x sc.2) z

def rightComb {S : Type v} (op : S → A → A → A) (word : List (S × A)) (z : A) : A :=
  word.foldl (fun x sc => op sc.1 sc.2 x) z

theorem comb_opposition {S : Type v} (op : S → A → A → A)
    (word : List (S × A)) (z : A) :
    rightComb op word z = leftComb (fun label a b => op label b a) word z := rfl

inductive LegalCombOrder : Nat → List Nat → Prop where
  | empty : LegalCombOrder 0 []
  | next {n xs} : LegalCombOrder n xs → LegalCombOrder (n + 1) (xs ++ [n + 1])

theorem comb_order_unique {n : Nat} {xs ys : List Nat}
    (h : LegalCombOrder n xs) (g : LegalCombOrder n ys) : xs = ys := by
  induction h generalizing ys with
  | empty => cases g; rfl
  | @next n xs h ih =>
    cases g with
    | next g => exact congrArg (fun zs => zs ++ [n + 1]) (ih g)

/- The printed constant-pair coincidence clause includes k=p=0. This exact
   counterexample does not refute the distributive operator identity. -/
theorem zero_pair_counterexample :
    ((0 : Nat), 0) = (0, (0 : Nat) * 0) ∧ (0 : Nat) ≠ 1 := by decide

#print axioms addition_opposition
#print axioms multiplication_opposition
#print axioms distributive_operator
#print axioms right_distributivity
#print axioms affine_composition
#print axioms comb_opposition
#print axioms comb_order_unique
#print axioms zero_pair_counterexample
end AEGPaper0
