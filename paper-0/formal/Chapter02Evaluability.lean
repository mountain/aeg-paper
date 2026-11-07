import Chapter02Domains
import Init.Data.Rat.Lemmas

/- Original CC0 continuation by Codex (OpenAI), 2026-11-07.
   Ordinary tree semantics, effective evaluation and projective continuation
   are separate. Computation uses structural recursion and a supplied zero
   decision; no decision procedure for arbitrary real constants is assumed. -/
namespace AEGPaper0.Chapter02Evaluability

open AEGPaper0.Chapter02
variable {A : Type u}

def Domain (s : FieldData A) (tree : Tree Op A) (input : A) : Prop :=
  ∃ output, TreeEval (Eval s) input tree output

def holes : Tree Op A → Nat
  | .hole => 1
  | .constant _ => 0
  | .binary _ l r => holes l + holes r

theorem tree_eval_functional (s : FieldData A) (tree : Tree Op A)
    (input x y : A) (hx : TreeEval (Eval s) input tree x)
    (hy : TreeEval (Eval s) input tree y) : x = y := by
  induction tree generalizing x y with
  | hole => exact hx.trans hy.symm
  | constant c => exact hx.trans hy.symm
  | binary op l r ihl ihr =>
    obtain ⟨a, b, ha, hb, h⟩ := hx
    obtain ⟨c, d, hc, hd, g⟩ := hy
    have ac := ihl a c ha hc
    have bd := ihr b d hb hd
    subst c; subst d
    exact eval_functional s op a b x y h g

/- The dependent argument restricts this value function to the domain.
   It specifies the semantic map even without an effective presentation. -/
noncomputable def value (s : FieldData A) (tree : Tree Op A) (input : A)
    (h : Domain s tree input) : A := Classical.choose h

theorem value_spec (s : FieldData A) (tree : Tree Op A) (input : A)
    (h : Domain s tree input) : TreeEval (Eval s) input tree (value s tree input h) :=
  Classical.choose_spec h

theorem value_unique (s : FieldData A) (tree : Tree Op A) (input output : A)
    (h : Domain s tree input) (g : TreeEval (Eval s) input tree output) :
    value s tree input h = output :=
  tree_eval_functional s tree input _ output (value_spec s tree input h) g

theorem left_comb_domain (s : FieldData A) (word : List (Op × A)) (input : A) :
    Domain s (leftTree word) input ↔ ∃ output, PartialFold (Eval s) word input output := by
  exact exists_congr (fun output => left_tree_correspondence (Eval s) word input output)

theorem right_comb_domain (s : FieldData A) (word : List (Op × A)) (input : A) :
    Domain s (rightTree word) input ↔
      ∃ output, PartialFold (Opposite (Eval s)) word input output := by
  exact exists_congr (fun output => right_tree_correspondence (Eval s) word input output)

theorem prefix_domain (s : FieldData A) (before after : List (Op × A)) (input : A) :
    Domain s (leftTree (before ++ after)) input ↔
      ∃ intermediate, PartialFold (Eval s) before input intermediate ∧
        Domain s (leftTree after) intermediate := by
  rw [left_comb_domain]
  constructor
  · rintro ⟨output, h⟩
    obtain ⟨mid, hbefore, hafter⟩ := (partial_fold_append (Eval s) before after input output).mp h
    exact ⟨mid, hbefore, (left_comb_domain s after mid).mpr ⟨output, hafter⟩⟩
  · rintro ⟨mid, hbefore, hafter⟩
    obtain ⟨output, h⟩ := (left_comb_domain s after mid).mp hafter
    exact ⟨output, (partial_fold_append (Eval s) before after input output).mpr ⟨mid, hbefore, h⟩⟩

theorem undefined_prefix_persists (s : FieldData A) (before after : List (Op × A))
    (input : A) (h : ¬ Domain s (leftTree before) input) :
    ¬ Domain s (leftTree (before ++ after)) input := by
  intro g
  obtain ⟨mid, hb, _⟩ := (prefix_domain s before after input).mp g
  exact h ((left_comb_domain s before input).mpr ⟨mid, hb⟩)

/- Inverse image is a relation on conditions, not an inverse function. -/
def pullCondition {S : Type v} (relation : S → A → A → A → Prop)
    (word : List (S × A)) (condition : A → Prop) (input : A) : Prop :=
  ∃ output, PartialFold relation word input output ∧ condition output

theorem condition_append {S : Type v} (relation : S → A → A → A → Prop)
    (before after : List (S × A)) (condition : A → Prop) (input : A) :
    pullCondition relation (before ++ after) condition input ↔
      pullCondition relation before (pullCondition relation after condition) input := by
  constructor
  · rintro ⟨output, h, hc⟩
    obtain ⟨mid, hb, ha⟩ := (partial_fold_append relation before after input output).mp h
    exact ⟨mid, hb, output, ha, hc⟩
  · rintro ⟨mid, hb, output, ha, hc⟩
    exact ⟨output, (partial_fold_append relation before after input output).mpr ⟨mid, hb, ha⟩, hc⟩

def Closed : Tree Op A → Prop
  | .hole => False
  | .constant _ => True
  | .binary _ l r => Closed l ∧ Closed r

theorem closed_input_independent (s : FieldData A) (tree : Tree Op A) (h : Closed tree)
    (input other output : A) :
    TreeEval (Eval s) input tree output ↔ TreeEval (Eval s) other tree output := by
  induction tree generalizing output with
  | hole => exact False.elim h
  | constant c => rfl
  | binary op l r ihl ihr =>
    simp only [Closed] at h
    simp only [TreeEval, ihl h.1, ihr h.2]

theorem closed_domain_independent (s : FieldData A) (tree : Tree Op A) (h : Closed tree)
    (input other : A) : Domain s tree input ↔ Domain s tree other :=
  exists_congr (fun output => closed_input_independent s tree h input other output)

def opCompute (s : FieldData A) [DecidableEq A] (op : Op) (x y : A) : Option A :=
  match op with
  | .add => some (s.add x y)
  | .sub => some (s.add x (s.neg y))
  | .mul => some (s.mul x y)
  | .div => if y = s.zero then none else some (s.mul x (s.inv y))

theorem op_compute_correct (s : FieldData A) [DecidableEq A] (op : Op) (x y r : A) :
    opCompute s op x y = some r ↔ Eval s op x y r := by
  cases op <;> simp only [opCompute, Eval]
  · simp only [Option.some.injEq, eq_comm]
  · simp only [Option.some.injEq, eq_comm]
  · simp only [Option.some.injEq, eq_comm]
  · split <;> simp_all [eq_comm]

def compute (s : FieldData A) [DecidableEq A] : Tree Op A → A → Option A
  | .hole, input => some input
  | .constant c, _ => some c
  | .binary op l r, input =>
    match compute s l input, compute s r input with
    | some x, some y => opCompute s op x y
    | _, _ => none

theorem compute_correct (s : FieldData A) [DecidableEq A] (tree : Tree Op A)
    (input output : A) : compute s tree input = some output ↔
      TreeEval (Eval s) input tree output := by
  induction tree generalizing output with
  | hole => simp only [compute, TreeEval, Option.some.injEq, eq_comm]
  | constant c => simp only [compute, TreeEval, Option.some.injEq, eq_comm]
  | binary op l r ihl ihr =>
    simp only [compute, TreeEval]
    cases hl : compute s l input <;> cases hr : compute s r input
    · constructor
      · intro h; cases h
      · rintro ⟨x, y, hx, _, _⟩
        have := (ihl x).mpr hx
        rw [hl] at this; cases this
    · constructor
      · intro h; cases h
      · rintro ⟨x, y, hx, _, _⟩
        have := (ihl x).mpr hx
        rw [hl] at this; cases this
    · constructor
      · intro h; cases h
      · rintro ⟨x, y, _, hy, _⟩
        have := (ihr y).mpr hy
        rw [hr] at this; cases this
    · rename_i x y
      rw [op_compute_correct]
      constructor
      · intro h; exact ⟨x, y, (ihl x).mp hl, (ihr y).mp hr, h⟩
      · rintro ⟨a, b, ha, hb, h⟩
        have ax : x = a := Option.some.inj (hl.symm.trans ((ihl a).mpr ha))
        have by' : y = b := Option.some.inj (hr.symm.trans ((ihr b).mpr hb))
        subst a; subst b; exact h

theorem compute_none_iff (s : FieldData A) [DecidableEq A] (tree : Tree Op A) (input : A) :
    compute s tree input = none ↔ ¬ Domain s tree input := by
  constructor
  · intro hn ⟨output, h⟩
    have := (compute_correct s tree input output).mpr h
    rw [hn] at this; cases this
  · intro h
    cases hc : compute s tree input with
    | none => rfl
    | some output => exact False.elim (h ⟨output, (compute_correct s tree input output).mp hc⟩)

def decideDomain (s : FieldData A) [DecidableEq A] (tree : Tree Op A) (input : A) :
    Decidable (Domain s tree input) :=
  match hc : compute s tree input with
  | none => isFalse ((compute_none_iff s tree input).mp hc)
  | some output => isTrue ⟨output, (compute_correct s tree input output).mp hc⟩

theorem computed_value (s : FieldData A) [DecidableEq A] (tree : Tree Op A)
    (input : A) (h : Domain s tree input) :
    compute s tree input = some (value s tree input h) :=
  (compute_correct s tree input _).mpr (value_spec s tree input h)

def identityTree : Tree Op A := .hole
def zeroDenominator (s : FieldData A) : Tree Op A := .binary .div .hole (.constant s.zero)
def reciprocalTree (s : FieldData A) (tree : Tree Op A) : Tree Op A :=
  .binary .div (.constant s.one) tree
def cancelledReciprocal (s : FieldData A) : Tree Op A := reciprocalTree s (reciprocalTree s .hole)

theorem identity_domain (s : FieldData A) (input : A) : Domain s identityTree input :=
  ⟨input, rfl⟩

theorem zero_denominator_empty (s : FieldData A) (input : A) :
    ¬ Domain s (zeroDenominator s) input := by
  rintro ⟨output, x, y, _, hy, h⟩
  change y = s.zero at hy
  subst y; exact h.1 rfl

theorem undefined_child_propagates (s : FieldData A) (op : Op) (l r : Tree Op A)
    (input : A) (h : ¬ Domain s l input ∨ ¬ Domain s r input) :
    ¬ Domain s (.binary op l r) input := by
  rintro ⟨output, x, y, hx, hy, _⟩
  cases h with
  | inl h => exact h ⟨x, hx⟩
  | inr h => exact h ⟨y, hy⟩

theorem cancelled_reciprocal_one_hole (s : FieldData A) : holes (cancelledReciprocal s) = 1 := rfl

theorem reciprocal_tree_eval (s : FieldData A) (tree : Tree Op A) (input output : A) :
    TreeEval (Eval s) input (reciprocalTree s tree) output ↔
      ∃ x, TreeEval (Eval s) input tree x ∧ x ≠ s.zero ∧ output = s.inv x := by
  simp only [reciprocalTree, TreeEval, Eval]
  constructor
  · rintro ⟨_, x, rfl, hx, hn, ho⟩
    exact ⟨x, hx, hn, ho.trans (one_mul s _)⟩
  · rintro ⟨x, hx, hn, ho⟩
    exact ⟨s.one, x, rfl, hx, hn, ho.trans (one_mul s _).symm⟩

theorem inverse_inverse (s : FieldData A) (x : A) (hx : x ≠ s.zero) :
    s.inv (s.inv x) = x := by
  apply mul_left_cancel s (s.inv x) (inverse_nonzero s x hx)
  exact (s.mul_inv (s.inv x) (inverse_nonzero s x hx)).trans
    ((s.mul_comm (s.inv x) x).trans (s.mul_inv x hx)).symm

theorem cancelled_reciprocal_eval (s : FieldData A) (input output : A) :
    TreeEval (Eval s) input (cancelledReciprocal s) output ↔
      input ≠ s.zero ∧ output = input := by
  simp only [cancelledReciprocal, reciprocal_tree_eval, TreeEval]
  constructor
  · rintro ⟨v, ⟨x, hx, hn, hv⟩, _, ho⟩
    subst x; subst v
    exact ⟨hn, ho.trans (inverse_inverse s input hn)⟩
  · rintro ⟨hn, ho⟩
    subst output
    exact ⟨s.inv input, ⟨input, rfl, hn, rfl⟩, inverse_nonzero s input hn,
      (inverse_inverse s input hn).symm⟩

theorem cancelled_reciprocal_domain (s : FieldData A) (input : A) :
    Domain s (cancelledReciprocal s) input ↔ input ≠ s.zero := by
  constructor
  · rintro ⟨output, h⟩; exact ((cancelled_reciprocal_eval s input output).mp h).1
  · intro h; exact ⟨input, (cancelled_reciprocal_eval s input input).mpr ⟨h, rfl⟩⟩

theorem cancelled_identity_partial_maps_differ (s : FieldData A) :
    ¬ (∀ input output, TreeEval (Eval s) input (cancelledReciprocal s) output ↔
      TreeEval (Eval s) input identityTree output) := by
  intro h
  have bad := ((cancelled_reciprocal_eval s s.zero s.zero).mp
    ((h s.zero s.zero).mpr rfl)).1
  exact bad rfl

theorem reciprocal_graph_functional (s : FieldData A) (c : A) (hc : c ≠ s.zero)
    (p q r : Point A) (h : ReciprocalGraph s c hc p q)
    (g : ReciprocalGraph s c hc p r) : q = r := by
  cases h with
  | zero =>
    cases g with
    | zero => rfl
    | regular x hx => exact False.elim (hx rfl)
  | infinity => cases g; rfl
  | regular x hx =>
    cases g with
    | zero => exact False.elim (hx rfl)
    | regular => rfl

theorem reciprocal_projective_involution (s : FieldData A) (p : Point A) :
    ∃ q, ReciprocalGraph s s.one s.zero_ne_one.symm p q ∧
      ReciprocalGraph s s.one s.zero_ne_one.symm q p := by
  classical
  cases p with
  | infinity => exact ⟨.finite s.zero, .infinity, .zero⟩
  | finite x =>
    by_cases hx : x = s.zero
    · subst x; exact ⟨.infinity, .zero, .infinity⟩
    · have hi := inverse_nonzero s x hx
      have h1 : ReciprocalGraph s s.one s.zero_ne_one.symm (.finite x) (.finite (s.inv x)) := by
        simpa only [one_mul] using (ReciprocalGraph.regular (s := s) (c := s.one)
          (hc := s.zero_ne_one.symm) x hx)
      have h2 : ReciprocalGraph s s.one s.zero_ne_one.symm (.finite (s.inv x)) (.finite x) := by
        simpa only [one_mul, inverse_inverse s x hx] using (ReciprocalGraph.regular (s := s)
          (c := s.one) (hc := s.zero_ne_one.symm) (s.inv x) hi)
      exact ⟨.finite (s.inv x), h1, h2⟩

theorem reciprocal_projective_identity (s : FieldData A) (p q r : Point A)
    (h : ReciprocalGraph s s.one s.zero_ne_one.symm p q)
    (g : ReciprocalGraph s s.one s.zero_ne_one.symm q r) : r = p := by
  obtain ⟨other, h1, h2⟩ := reciprocal_projective_involution s p
  have he := reciprocal_graph_functional s s.one s.zero_ne_one.symm p q other h h1
  subst other
  exact reciprocal_graph_functional s s.one s.zero_ne_one.symm q r p g h2

theorem subtraction_expansion (s : FieldData A) (c z k : A) :
    s.mul (s.add c (s.neg z)) k = s.add (s.mul (s.neg k) z) (s.mul k c) := by
  have hn : s.mul (s.neg z) k = s.mul (s.neg k) z :=
    (congrArg (fun t => s.mul t k) (neg_one_mul s z).symm).trans
      ((s.mul_assoc (s.neg s.one) z k).trans
        ((congrArg (s.mul (s.neg s.one)) (s.mul_comm z k)).trans
          ((s.mul_assoc (s.neg s.one) k z).symm.trans
            (congrArg (fun t => s.mul t z) (neg_one_mul s k)))))
  exact (AEGPaper0.right_distributivity s.toAlgebra c (s.neg z) k).trans
    ((congrArg (fun t => s.add t (s.mul (s.neg z) k)) (s.mul_comm c k)).trans
      ((congrArg (s.add (s.mul k c)) hn).trans (s.add_comm _ _)))

/- A concrete effective presentation. Rat stores arbitrary-size normalized
   integer fractions; its constructors require a nonzero denominator.
   This is not the fixed-width Adva rational profile. -/
def rationalField : FieldData Rat where
  add := (· + ·)
  mul := (· * ·)
  zero := 0
  one := 1
  add_assoc := Rat.add_assoc
  add_comm := Rat.add_comm
  add_zero := Rat.add_zero
  mul_assoc := Rat.mul_assoc
  mul_comm := Rat.mul_comm
  mul_one := Rat.mul_one
  mul_add := Rat.mul_add
  mul_zero := Rat.mul_zero
  neg := (- ·)
  inv := Rat.inv
  add_neg := Rat.add_neg_cancel
  inv_zero := Rat.inv_zero
  mul_inv := Rat.mul_inv_cancel
  zero_ne_one := by decide

def evaluateRational (tree : Tree Op Rat) (input : Rat) : Option Rat :=
  compute rationalField tree input

theorem rational_evaluation_correct (tree : Tree Op Rat) (input output : Rat) :
    evaluateRational tree input = some output ↔ TreeEval (Eval rationalField) input tree output :=
  compute_correct rationalField tree input output

theorem rational_failure_exact (tree : Tree Op Rat) (input : Rat) :
    evaluateRational tree input = none ↔ ¬ Domain rationalField tree input :=
  compute_none_iff rationalField tree input

theorem rational_evaluation_total (tree : Tree Op Rat) (input : Rat) :
    (∃ output, evaluateRational tree input = some output ∧
      TreeEval (Eval rationalField) input tree output) ∨
      (evaluateRational tree input = none ∧ ¬ Domain rationalField tree input) := by
  cases h : evaluateRational tree input with
  | none => exact Or.inr ⟨rfl, (rational_failure_exact tree input).mp h⟩
  | some output => exact Or.inl ⟨output, rfl, (rational_evaluation_correct tree input output).mp h⟩

def rationalDomainDecision (tree : Tree Op Rat) (input : Rat) :
    Decidable (Domain rationalField tree input) := decideDomain rationalField tree input

/- Boundary regressions are kernel reductions, alongside the universal proofs.
   All constants here are valid Rat values. Raw fraction denominators must be
   validated before constructing such constants. -/
theorem rational_cancelled_nonzero :
    evaluateRational (cancelledReciprocal rationalField) (mkRat 3 2) = some (mkRat 3 2) := by
  decide +kernel

theorem rational_cancelled_zero :
    evaluateRational (cancelledReciprocal rationalField) 0 = none := by decide

theorem rational_branching_guard :
    evaluateRational (.binary .div (.binary .add (.constant (mkRat 3 2)) (.constant (mkRat 2 3)))
      (.binary .sub (.constant (mkRat 5 6)) (.constant (mkRat 5 6)))) 7 = none := by decide +kernel

theorem rational_undefined_before_zero :
    evaluateRational (.binary .mul (zeroDenominator rationalField) (.constant 0)) 1 = none := by
  decide

theorem rational_zero_numerator_guard :
    evaluateRational (.binary .div (.constant 0) .hole) 0 = none ∧
      evaluateRational (.binary .div (.constant 0) .hole) (mkRat (-3) 2) = some 0 := by decide +kernel

theorem rational_unbounded_integer :
    evaluateRational (.binary .mul .hole (.constant 2)) 9223372036854775807 =
      some 18446744073709551614 := by decide +kernel

#print axioms tree_eval_functional
#print axioms value_spec
#print axioms value_unique
#print axioms left_comb_domain
#print axioms right_comb_domain
#print axioms prefix_domain
#print axioms undefined_prefix_persists
#print axioms condition_append
#print axioms closed_input_independent
#print axioms closed_domain_independent
#print axioms op_compute_correct
#print axioms compute_correct
#print axioms compute_none_iff
#print axioms computed_value
#print axioms identity_domain
#print axioms zero_denominator_empty
#print axioms undefined_child_propagates
#print axioms cancelled_reciprocal_one_hole
#print axioms reciprocal_tree_eval
#print axioms inverse_inverse
#print axioms cancelled_reciprocal_eval
#print axioms cancelled_reciprocal_domain
#print axioms cancelled_identity_partial_maps_differ
#print axioms reciprocal_graph_functional
#print axioms reciprocal_projective_involution
#print axioms reciprocal_projective_identity
#print axioms subtraction_expansion
#print axioms rational_evaluation_correct
#print axioms rational_failure_exact
#print axioms rational_evaluation_total
#print axioms rational_cancelled_nonzero
#print axioms rational_cancelled_zero
#print axioms rational_branching_guard
#print axioms rational_undefined_before_zero
#print axioms rational_zero_numerator_guard
#print axioms rational_unbounded_integer
end AEGPaper0.Chapter02Evaluability
