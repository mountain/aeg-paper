import Chapter02

/- Chapter 2 continuation. Original CC0 code by Codex (OpenAI).
   All algebraic laws are explicit parameters. Ordinary evaluation is partial;
   the inverse operation's value at zero never makes division by zero legal. -/
namespace AEGPaper0.Chapter02

inductive Op where
  | add | sub | mul | div
  deriving DecidableEq

inductive Slot where
  | first | second
  deriving DecidableEq

structure FieldData (A : Type u) extends AEGPaper0.Algebra A where
  neg : A → A
  inv : A → A
  add_neg : ∀ a, add a (neg a) = zero
  inv_zero : inv zero = zero
  mul_inv : ∀ a, a ≠ zero → mul a (inv a) = one
  zero_ne_one : zero ≠ one

variable {A : Type u}

def Eval (s : FieldData A) : Op → A → A → A → Prop
  | .add, x, y, r => r = s.add x y
  | .sub, x, y, r => r = s.add x (s.neg y)
  | .mul, x, y, r => r = s.mul x y
  | .div, x, y, r => y ≠ s.zero ∧ r = s.mul x (s.inv y)

def Section (s : FieldData A) (slot : Slot) (op : Op) (c x r : A) : Prop :=
  match slot with
  | .first => Eval s op x c r
  | .second => Eval s op c x r

theorem first_div_domain (s : FieldData A) (c x : A) :
    (∃ r, Section s .first .div c x r) ↔ c ≠ s.zero := by
  constructor
  · rintro ⟨r, h, _⟩; exact h
  · intro h; exact ⟨s.mul x (s.inv c), h, rfl⟩

theorem second_div_domain (s : FieldData A) (c x : A) :
    (∃ r, Section s .second .div c x r) ↔ x ≠ s.zero := by
  constructor
  · rintro ⟨r, h, _⟩; exact h
  · intro h; exact ⟨s.mul c (s.inv x), h, rfl⟩

theorem zero_numerator_keeps_domain (s : FieldData A) (x : A) :
    (∃ r, Section s .second .div s.zero x r) ↔ x ≠ s.zero :=
  second_div_domain s s.zero x

theorem eval_functional (s : FieldData A) (op : Op) (x y r t : A)
    (h : Eval s op x y r) (g : Eval s op x y t) : r = t := by
  cases op <;> simp only [Eval] at h g
  · exact h.trans g.symm
  · exact h.trans g.symm
  · exact h.trans g.symm
  · exact h.2.trans g.2.symm

def Opposite {S : Type v} (relation : S → A → A → A → Prop) : S → A → A → A → Prop :=
  fun op x y r => relation op y x r

def PartialFold {S : Type v} (relation : S → A → A → A → Prop) :
    List (S × A) → A → A → Prop
  | [], x, y => y = x
  | (op, c) :: rest, x, y => ∃ t, relation op x c t ∧ PartialFold relation rest t y

theorem partial_fold_nil {S : Type v} (relation : S → A → A → A → Prop) (x y : A) :
    PartialFold relation [] x y ↔ y = x := Iff.rfl

theorem partial_fold_snoc {S : Type v} (relation : S → A → A → A → Prop)
    (word : List (S × A)) (op : S) (c x y : A) :
    PartialFold relation (word ++ [(op, c)]) x y ↔
      ∃ t, PartialFold relation word x t ∧ relation op t c y := by
  induction word generalizing x with
  | nil =>
    simp only [List.nil_append, PartialFold]
    constructor
    · rintro ⟨t, ht, rfl⟩; exact ⟨x, rfl, ht⟩
    · rintro ⟨t, rfl, ht⟩; exact ⟨y, ht, rfl⟩
  | cons head tail ih =>
    rcases head with ⟨label, value⟩
    simp only [List.cons_append, PartialFold]
    constructor
    · rintro ⟨t, h, rest⟩
      obtain ⟨u, hu, last⟩ := (ih t).mp rest
      exact ⟨u, ⟨t, h, hu⟩, last⟩
    · rintro ⟨u, ⟨t, h, ht⟩, last⟩
      exact ⟨t, h, (ih t).mpr ⟨u, ht, last⟩⟩

theorem partial_fold_append {S : Type v} (relation : S → A → A → A → Prop)
    (before after : List (S × A)) (x y : A) :
    PartialFold relation (before ++ after) x y ↔
      ∃ t, PartialFold relation before x t ∧ PartialFold relation after t y := by
  induction before generalizing x with
  | nil => simp [PartialFold]
  | cons sc rest ih =>
    simp only [List.cons_append, PartialFold]
    constructor
    · rintro ⟨u, hu, h⟩
      obtain ⟨t, ht, hs⟩ := (ih u).mp h
      exact ⟨t, ⟨u, hu, ht⟩, hs⟩
    · rintro ⟨t, ⟨u, hu, ht⟩, hs⟩
      exact ⟨u, hu, (ih u).mpr ⟨t, ht, hs⟩⟩

theorem commutative_fold_agreement {S : Type v} (relation : S → A → A → A → Prop)
    (hc : ∀ op x y r, relation op x y r ↔ relation op y x r)
    (word : List (S × A)) (x y : A) :
    PartialFold (Opposite relation) word x y ↔ PartialFold relation word x y := by
  induction word generalizing x with
  | nil => rfl
  | cons sc rest ih =>
    constructor
    · rintro ⟨t, h, ht⟩
      exact ⟨t, (hc sc.1 sc.2 x t).mp h, (ih t).mp ht⟩
    · rintro ⟨t, h, ht⟩
      exact ⟨t, (hc sc.1 x sc.2 t).mp h, (ih t).mpr ht⟩

theorem zero_denominator_refused (s : FieldData A) (x r : A) :
    ¬ Eval s .div x s.zero r := fun h => h.1 rfl

theorem undefined_first_prefix_persists (s : FieldData A)
    (suffix : List (Op × A)) (x r : A) :
    ¬ PartialFold (Eval s) ((.div, s.zero) :: suffix) x r := by
  rintro ⟨t, h, _⟩; exact h.1 rfl

theorem undefined_second_prefix_persists (s : FieldData A)
    (suffix : List (Op × A)) (c r : A) :
    ¬ PartialFold (Opposite (Eval s)) ((.div, c) :: suffix) s.zero r := by
  rintro ⟨t, h, _⟩; exact h.1 rfl

/- Planar syntax is represented independently of its value relation. -/
inductive Tree (S : Type v) (A : Type u) where
  | hole
  | constant (value : A)
  | binary (op : S) (left right : Tree S A)

def growLeft {S : Type v} (t : Tree S A) (sc : S × A) : Tree S A :=
  .binary sc.1 t (.constant sc.2)

def growRight {S : Type v} (t : Tree S A) (sc : S × A) : Tree S A :=
  .binary sc.1 (.constant sc.2) t

def leftTree {S : Type v} (word : List (S × A)) : Tree S A :=
  word.foldl growLeft .hole

def rightTree {S : Type v} (word : List (S × A)) : Tree S A :=
  word.foldl growRight .hole

def TreeEval {S : Type v} (relation : S → A → A → A → Prop) (input : A) :
    Tree S A → A → Prop
  | .hole, r => r = input
  | .constant c, r => r = c
  | .binary op l r, output => ∃ x y, TreeEval relation input l x ∧
      TreeEval relation input r y ∧ relation op x y output

theorem grow_left_eval {S : Type v} (relation : S → A → A → A → Prop)
    (input : A) (tree : Tree S A) (op : S) (c y : A) :
    TreeEval relation input (growLeft tree (op, c)) y ↔
      ∃ x, TreeEval relation input tree x ∧ relation op x c y := by
  simp only [growLeft, TreeEval]
  constructor
  · rintro ⟨x, z, hx, rfl, h⟩; exact ⟨x, hx, h⟩
  · rintro ⟨x, hx, h⟩; exact ⟨x, c, hx, rfl, h⟩

theorem left_tree_correspondence {S : Type v} (relation : S → A → A → A → Prop)
    (word : List (S × A)) (input output : A) :
    TreeEval relation input (leftTree word) output ↔ PartialFold relation word input output := by
  suffices ∀ (word : List (S × A)) (tree : Tree S A),
      TreeEval relation input (word.foldl growLeft tree) output ↔
        ∃ x, TreeEval relation input tree x ∧ PartialFold relation word x output by
    simpa only [leftTree, TreeEval, exists_eq_left] using this word .hole
  intro word
  induction word with
  | nil => intro tree; simp [PartialFold]
  | cons sc rest ih =>
    intro tree
    rcases sc with ⟨op, c⟩
    simp only [List.foldl_cons, ih, grow_left_eval, PartialFold]
    constructor
    · rintro ⟨t, ⟨x, hx, h⟩, ht⟩; exact ⟨x, hx, t, h, ht⟩
    · rintro ⟨x, hx, t, h, ht⟩; exact ⟨t, ⟨x, hx, h⟩, ht⟩

theorem left_tree_snoc {S : Type v} (word : List (S × A)) (op : S) (c : A) :
    leftTree (word ++ [(op, c)]) = .binary op (leftTree word) (.constant c) := by
  simp [leftTree, List.foldl_append, growLeft]

theorem right_tree_snoc {S : Type v} (word : List (S × A)) (op : S) (c : A) :
    rightTree (word ++ [(op, c)]) = .binary op (.constant c) (rightTree word) := by
  simp [rightTree, List.foldl_append, growRight]

def mirror {S : Type v} : Tree S A → Tree S A
  | .hole => .hole
  | .constant c => .constant c
  | .binary op l r => .binary op (mirror r) (mirror l)

theorem mirror_involution {S : Type v} (tree : Tree S A) : mirror (mirror tree) = tree := by
  induction tree with
  | hole => rfl
  | constant c => rfl
  | binary op l r ihl ihr => simp only [mirror, ihl, ihr]

theorem mirror_fold {S : Type v} (word : List (S × A)) (tree : Tree S A) :
    mirror (word.foldl growLeft tree) = word.foldl growRight (mirror tree) := by
  induction word generalizing tree with
  | nil => rfl
  | cons sc rest ih => exact ih (growLeft tree sc)

theorem mirror_left_tree {S : Type v} (word : List (S × A)) :
    mirror (leftTree word) = rightTree word := mirror_fold word .hole

theorem mirror_eval {S : Type v} (relation : S → A → A → A → Prop)
    (input : A) (tree : Tree S A) (output : A) :
    TreeEval relation input (mirror tree) output ↔
      TreeEval (Opposite relation) input tree output := by
  induction tree generalizing output with
  | hole => rfl
  | constant c => rfl
  | binary op l r ihl ihr =>
    simp only [mirror, TreeEval, ihl, ihr, Opposite]
    constructor
    · rintro ⟨y, x, hy, hx, h⟩; exact ⟨x, y, hx, hy, h⟩
    · rintro ⟨x, y, hx, hy, h⟩; exact ⟨y, x, hy, hx, h⟩

theorem right_tree_correspondence {S : Type v} (relation : S → A → A → A → Prop)
    (word : List (S × A)) (input output : A) :
    TreeEval relation input (rightTree word) output ↔
      PartialFold (Opposite relation) word input output := by
  rw [← mirror_left_tree]
  exact (mirror_eval relation input (leftTree word) output).trans
    (left_tree_correspondence (Opposite relation) word input output)

theorem partial_fold_functional {S : Type v} (relation : S → A → A → A → Prop)
    (hf : ∀ op x y r t, relation op x y r → relation op x y t → r = t)
    (word : List (S × A)) (input x y : A)
    (hx : PartialFold relation word input x) (hy : PartialFold relation word input y) : x = y := by
  induction word generalizing input with
  | nil => exact hx.trans hy.symm
  | cons sc rest ih =>
    obtain ⟨u, hu, hrest⟩ := hx
    obtain ⟨v, hv, grest⟩ := hy
    have he := hf sc.1 input sc.2 u v hu hv
    subst v
    exact ih u hrest grest

/- A schedule is specified independently of the comb grammar: both child
   schedules may be interleaved, then the parent runs. Occurrence identifiers
   can be included in S, e.g. S = Op × Nat; repeated operators are not merged. -/
inductive Shuffle {S : Type v} : List S → List S → List S → Prop where
  | empty : Shuffle [] [] []
  | left {x xs ys zs} : Shuffle xs ys zs → Shuffle (x :: xs) ys (x :: zs)
  | right {x xs ys zs} : Shuffle xs ys zs → Shuffle xs (x :: ys) (x :: zs)

theorem shuffle_nil_right {S : Type v} {xs zs : List S} (h : Shuffle xs [] zs) : zs = xs := by
  induction xs generalizing zs with
  | nil => cases h; rfl
  | cons x xs ih => cases h with
    | left h => exact congrArg (List.cons x) (ih h)

theorem shuffle_nil_left {S : Type v} {ys zs : List S} (h : Shuffle [] ys zs) : zs = ys := by
  induction ys generalizing zs with
  | nil => cases h; rfl
  | cons y ys ih => cases h with
    | right h => exact congrArg (List.cons y) (ih h)

theorem shuffle_with_right_empty {S : Type v} (xs : List S) : Shuffle xs [] xs := by
  induction xs with
  | nil => exact .empty
  | cons x xs ih => exact .left ih

theorem shuffle_with_left_empty {S : Type v} (xs : List S) : Shuffle [] xs xs := by
  induction xs with
  | nil => exact .empty
  | cons x xs ih => exact .right ih

inductive Trace {S : Type v} : Tree S A → List S → Prop where
  | hole : Trace .hole []
  | constant (c : A) : Trace (.constant c) []
  | binary {op l r xs ys zs} : Trace l xs → Trace r ys → Shuffle xs ys zs →
      Trace (.binary op l r) (zs ++ [op])

theorem grow_left_trace {S : Type v} (tree : Tree S A) (op : S) (c : A) (out : List S) :
    Trace (growLeft tree (op, c)) out ↔ ∃ xs, Trace tree xs ∧ out = xs ++ [op] := by
  constructor
  · intro h
    cases h with
    | binary hl hr hs =>
      cases hr
      exact ⟨_, hl, congrArg (fun zs => zs ++ [op]) (shuffle_nil_right hs)⟩
  · rintro ⟨xs, hx, rfl⟩
    exact .binary hx (.constant c) (shuffle_with_right_empty xs)

theorem grow_right_trace {S : Type v} (tree : Tree S A) (op : S) (c : A) (out : List S) :
    Trace (growRight tree (op, c)) out ↔ ∃ xs, Trace tree xs ∧ out = xs ++ [op] := by
  constructor
  · intro h
    cases h with
    | binary hl hr hs =>
      cases hl
      exact ⟨_, hr, congrArg (fun zs => zs ++ [op]) (shuffle_nil_left hs)⟩
  · rintro ⟨xs, hx, rfl⟩
    exact .binary (.constant c) hx (shuffle_with_left_empty xs)

theorem trace_fold_from {S : Type v} (grow : Tree S A → S × A → Tree S A)
    (hg : ∀ tree op c out, Trace (grow tree (op, c)) out ↔
      ∃ xs, Trace tree xs ∧ out = xs ++ [op])
    (word : List (S × A)) (tree : Tree S A) (out : List S) :
    Trace (word.foldl grow tree) out ↔
      ∃ xs, Trace tree xs ∧ out = xs ++ word.map Prod.fst := by
  induction word generalizing tree out with
  | nil => simp
  | cons sc rest ih =>
    rcases sc with ⟨op, c⟩
    rw [List.foldl_cons, ih]
    simp only [hg, List.map_cons]
    constructor
    · rintro ⟨ys, ⟨xs, hx, rfl⟩, rfl⟩
      exact ⟨xs, hx, by simp [List.append_assoc]⟩
    · rintro ⟨xs, hx, rfl⟩
      exact ⟨xs ++ [op], ⟨xs, hx, rfl⟩, by simp [List.append_assoc]⟩

theorem comb_trace_characterization {S : Type v} (word : List (S × A))
    (side : Slot) (out : List S) :
    Trace (word.foldl (if side = .first then growLeft else growRight) .hole) out ↔
      out = word.map Prod.fst := by
  have hg : ∀ (tree : Tree S A) (op : S) (c : A) (out : List S),
      Trace ((if side = .first then growLeft else growRight) tree (op, c)) out ↔
        ∃ xs, Trace tree xs ∧ out = xs ++ [op] := by
    cases side
    · exact grow_left_trace
    · exact grow_right_trace
  rw [trace_fold_from _ hg]
  constructor
  · rintro ⟨xs, h, he⟩; cases h; exact he
  · intro he; exact ⟨[], .hole, he⟩

theorem comb_legal_order_unique {S : Type v} (word : List (S × A)) (side : Slot)
    (xs ys : List S)
    (hx : Trace (word.foldl (if side = .first then growLeft else growRight) .hole) xs)
    (hy : Trace (word.foldl (if side = .first then growLeft else growRight) .hole) ys) : xs = ys :=
  ((comb_trace_characterization word side xs).mp hx).trans
    ((comb_trace_characterization word side ys).mp hy).symm

theorem inverse_nonzero (s : FieldData A) (x : A) (h : x ≠ s.zero) : s.inv x ≠ s.zero := by
  intro hi
  have hz : s.one = s.zero := (s.mul_inv x h).symm.trans (hi ▸ s.mul_zero x)
  exact s.zero_ne_one hz.symm

theorem zero_add (s : FieldData A) (x : A) : s.add s.zero x = x :=
  (s.add_comm s.zero x).trans (s.add_zero x)

theorem one_mul (s : FieldData A) (x : A) : s.mul s.one x = x :=
  (s.mul_comm s.one x).trans (s.mul_one x)

theorem zero_mul (s : FieldData A) (x : A) : s.mul s.zero x = s.zero :=
  (s.mul_comm s.zero x).trans (s.mul_zero x)

theorem add_left_cancel (s : FieldData A) (a : A) {x y : A}
    (h : s.add a x = s.add a y) : x = y := by
  have hneg : s.add (s.neg a) a = s.zero := (s.add_comm (s.neg a) a).trans (s.add_neg a)
  have reduce : ∀ t, s.add (s.neg a) (s.add a t) = t := fun t =>
    (s.add_assoc (s.neg a) a t).symm.trans
      ((congrArg (fun q => s.add q t) hneg).trans (zero_add s t))
  exact (reduce x).symm.trans ((congrArg (s.add (s.neg a)) h).trans (reduce y))

theorem neg_one_mul (s : FieldData A) (x : A) : s.mul (s.neg s.one) x = s.neg x := by
  apply add_left_cancel s x
  have hz : s.add x (s.mul (s.neg s.one) x) = s.zero :=
    (congrArg (fun q => s.add q (s.mul (s.neg s.one) x)) (one_mul s x).symm).trans
      ((AEGPaper0.right_distributivity s.toAlgebra s.one (s.neg s.one) x).symm.trans
        ((congrArg (fun q => s.mul q x) (s.add_neg s.one)).trans (zero_mul s x)))
  exact hz.trans (s.add_neg x).symm

theorem neg_one_nonzero (s : FieldData A) : s.neg s.one ≠ s.zero := by
  intro h
  have hz : s.one = s.zero := by simpa only [h, s.add_zero] using s.add_neg s.one
  exact s.zero_ne_one hz.symm

def AffineValue (s : FieldData A) (a b x : A) : A := s.add (s.mul a x) b

def AffineInverseValue (s : FieldData A) (a b y : A) : A :=
  s.mul (s.inv a) (s.add y (s.neg b))

theorem affine_left_inverse (s : FieldData A) (a b : A) (ha : a ≠ s.zero) (x : A) :
    AffineInverseValue s a b (AffineValue s a b x) = x := by
  have cancel_add : s.add (s.add (s.mul a x) b) (s.neg b) = s.mul a x :=
    (s.add_assoc (s.mul a x) b (s.neg b)).trans
      ((congrArg (s.add (s.mul a x)) (s.add_neg b)).trans (s.add_zero (s.mul a x)))
  have cancel_mul : s.mul (s.inv a) a = s.one :=
    (s.mul_comm (s.inv a) a).trans (s.mul_inv a ha)
  exact (congrArg (s.mul (s.inv a)) cancel_add).trans
    ((s.mul_assoc (s.inv a) a x).symm.trans
      ((congrArg (fun t => s.mul t x) cancel_mul).trans (one_mul s x)))

theorem affine_right_inverse (s : FieldData A) (a b : A) (ha : a ≠ s.zero) (y : A) :
    AffineValue s a b (AffineInverseValue s a b y) = y := by
  have cancel_mul : s.mul a (s.mul (s.inv a) (s.add y (s.neg b))) = s.add y (s.neg b) :=
    (s.mul_assoc a (s.inv a) (s.add y (s.neg b))).symm.trans
      ((congrArg (fun t => s.mul t (s.add y (s.neg b))) (s.mul_inv a ha)).trans
        (one_mul s (s.add y (s.neg b))))
  exact (congrArg (fun t => s.add t b) cancel_mul).trans
    ((s.add_assoc y (s.neg b) b).trans
      ((congrArg (s.add y) ((s.add_comm (s.neg b) b).trans (s.add_neg b))).trans
        (s.add_zero y)))

theorem first_add_affine (s : FieldData A) (c x r : A) :
    Section s .first .add c x r ↔ r = AffineValue s s.one c x := by
  simp [Section, Eval, AffineValue, one_mul]

theorem first_sub_affine (s : FieldData A) (c x r : A) :
    Section s .first .sub c x r ↔ r = AffineValue s s.one (s.neg c) x := by
  simp [Section, Eval, AffineValue, one_mul]

theorem first_mul_affine (s : FieldData A) (c x r : A) :
    Section s .first .mul c x r ↔ r = AffineValue s c s.zero x := by
  simp only [Section, Eval, AffineValue, s.add_zero, s.mul_comm x c]

theorem first_div_affine (s : FieldData A) (c x r : A) :
    Section s .first .div c x r ↔ c ≠ s.zero ∧ r = AffineValue s (s.inv c) s.zero x := by
  simp only [Section, Eval, AffineValue, s.add_zero, s.mul_comm x (s.inv c)]

theorem second_add_affine (s : FieldData A) (c x r : A) :
    Section s .second .add c x r ↔ r = AffineValue s s.one c x := by
  simp only [Section, Eval, AffineValue, one_mul, s.add_comm c x]

theorem second_sub_affine (s : FieldData A) (c x r : A) :
    Section s .second .sub c x r ↔ r = AffineValue s (s.neg s.one) c x := by
  simp only [Section, Eval, AffineValue, neg_one_mul, s.add_comm c (s.neg x)]

theorem second_mul_affine (s : FieldData A) (c x r : A) :
    Section s .second .mul c x r ↔ r = AffineValue s c s.zero x := by
  simp only [Section, Eval, AffineValue, s.add_zero]

theorem second_div_value (s : FieldData A) (c x r : A) :
    Section s .second .div c x r ↔ x ≠ s.zero ∧ r = s.mul c (s.inv x) := Iff.rfl

theorem addition_sections_agree (s : FieldData A) (c x r : A) :
    Section s .first .add c x r ↔ Section s .second .add c x r :=
  (first_add_affine s c x r).trans (second_add_affine s c x r).symm

theorem multiplication_sections_agree (s : FieldData A) (c x r : A) :
    Section s .first .mul c x r ↔ Section s .second .mul c x r :=
  (first_mul_affine s c x r).trans (second_mul_affine s c x r).symm

theorem reciprocal_scale_identity (s : FieldData A) (c k x : A) :
    s.mul (s.mul c (s.inv x)) k = s.mul (s.mul k c) (s.inv x) :=
  (s.mul_comm (s.mul c (s.inv x)) k).trans (s.mul_assoc k c (s.inv x)).symm

theorem guarded_reciprocal_scale (s : FieldData A) (c k x r : A) :
    (∃ t, Section s .second .div c x t ∧ Eval s .mul t k r) ↔
      x ≠ s.zero ∧ r = s.mul (s.mul k c) (s.inv x) := by
  constructor
  · rintro ⟨t, ⟨hx, ht⟩, hr⟩
    subst t
    exact ⟨hx, hr.trans (reciprocal_scale_identity s c k x)⟩
  · rintro ⟨hx, hr⟩
    exact ⟨s.mul c (s.inv x), ⟨hx, rfl⟩, hr.trans (reciprocal_scale_identity s c k x).symm⟩

theorem mul_left_cancel (s : FieldData A) (k : A) (hk : k ≠ s.zero)
    {x y : A} (h : s.mul k x = s.mul k y) : x = y := by
  have hi : s.mul (s.inv k) k = s.one := (s.mul_comm (s.inv k) k).trans (s.mul_inv k hk)
  have hx : s.mul (s.inv k) (s.mul k x) = x :=
    (s.mul_assoc (s.inv k) k x).symm.trans
      ((congrArg (fun t => s.mul t x) hi).trans
        ((s.mul_comm s.one x).trans (s.mul_one x)))
  have hy : s.mul (s.inv k) (s.mul k y) = y :=
    (s.mul_assoc (s.inv k) k y).symm.trans
      ((congrArg (fun t => s.mul t y) hi).trans
        ((s.mul_comm s.one y).trans (s.mul_one y)))
  exact hx.symm.trans ((congrArg (s.mul (s.inv k)) h).trans hy)

theorem constant_pair_coincidence (s : FieldData A) (p k : A) :
    (p, k) = (k, s.mul k p) ↔
      (p = s.zero ∧ k = s.zero) ∨ (p = s.one ∧ k = s.one) := by
  classical
  constructor
  · intro h
    have hp : p = k := congrArg Prod.fst h
    have hm : k = s.mul k p := congrArg Prod.snd h
    by_cases hk : k = s.zero
    · exact Or.inl ⟨hp.trans hk, hk⟩
    · have h1 : s.mul k p = s.mul k s.one := hm.symm.trans (s.mul_one k).symm
      have pp : p = s.one := mul_left_cancel s k hk h1
      exact Or.inr ⟨pp, hp.symm.trans pp⟩
  · intro h
    rcases h with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
    · simp only [s.mul_zero]
    · simp only [s.mul_one]

theorem nonzero_constant_pair_coincidence (s : FieldData A) (p k : A) (hk : k ≠ s.zero) :
    (p, k) = (k, s.mul k p) ↔ p = s.one ∧ k = s.one := by
  constructor
  · intro h
    rcases (constant_pair_coincidence s p k).mp h with hzero | hone
    · exact False.elim (hk hzero.2)
    · exact hone
  · intro h; exact (constant_pair_coincidence s p k).mpr (Or.inr h)

def firstWord (p k : A) : List (Op × Slot × A) :=
  [(.add, .first, p), (.mul, .first, k)]

def secondWord (s : FieldData A) (p k : A) : List (Op × Slot × A) :=
  [(.mul, .first, k), (.add, .first, s.mul k p)]

theorem marked_words_distinct (s : FieldData A) (p k : A) :
    firstWord p k ≠ secondWord s p k := by
  intro h
  have bad := congrArg (fun w => w.head?.map Prod.fst) h
  simp only [firstWord, secondWord, List.head?_cons, Option.map_some] at bad
  cases bad

inductive Point (A : Type u) where
  | finite (x : A)
  | infinity

inductive ReciprocalGraph (s : FieldData A) (c : A) (hc : c ≠ s.zero) :
    Point A → Point A → Prop where
  | zero : ReciprocalGraph s c hc (.finite s.zero) .infinity
  | infinity : ReciprocalGraph s c hc .infinity (.finite s.zero)
  | regular (x : A) (hx : x ≠ s.zero) :
      ReciprocalGraph s c hc (.finite x) (.finite (s.mul c (s.inv x)))

theorem reciprocal_infinity (s : FieldData A) (c : A) (hc : c ≠ s.zero) :
    ReciprocalGraph s c hc .infinity (.finite s.zero) := .infinity

theorem ordinary_reciprocal_projective_match (s : FieldData A) (c : A) (hc : c ≠ s.zero)
    (x r : A) (h : Section s .second .div c x r) :
    ReciprocalGraph s c hc (.finite x) (.finite r) := by
  rcases h with ⟨hx, rfl⟩
  exact .regular x hx

theorem reciprocal_not_infinity_stabilizing (s : FieldData A) (c : A) (hc : c ≠ s.zero) :
    ¬ ReciprocalGraph s c hc .infinity .infinity := by
  intro h; cases h

def reciprocalRaw (s : FieldData A) (c : A) (p : A × A) : A × A :=
  (s.mul c p.2, p.1)

theorem reciprocal_raw_infinity (s : FieldData A) (c : A) :
    reciprocalRaw s c (s.one, s.zero) = (s.zero, s.one) := by
  simp only [reciprocalRaw, s.mul_zero]

theorem reciprocal_raw_zero (s : FieldData A) (c : A) :
    reciprocalRaw s c (s.zero, s.one) = (c, s.zero) := by
  simp only [reciprocalRaw, s.mul_one]

theorem reciprocal_raw_preserves_nonzero (s : FieldData A) (c : A) (hc : c ≠ s.zero)
    (p : A × A) (hp : p ≠ (s.zero, s.zero)) :
    reciprocalRaw s c p ≠ (s.zero, s.zero) := by
  intro h
  have hx : p.1 = s.zero := congrArg Prod.snd h
  have hm : s.mul c p.2 = s.zero := congrArg Prod.fst h
  have hy := mul_left_cancel s c hc (hm.trans (s.mul_zero c).symm)
  exact hp (Prod.ext hx hy)

theorem zero_reciprocal_raw_invalid (s : FieldData A) :
    reciprocalRaw s s.zero (s.zero, s.one) = (s.zero, s.zero) := by
  simp only [reciprocalRaw, s.mul_one]

theorem zero_scale_not_injective (s : FieldData A) :
    ¬ Function.Injective (fun x => s.mul s.zero x) := by
  intro h
  exact s.zero_ne_one (h ((s.mul_zero s.zero).trans
    ((s.mul_comm s.zero s.one).trans (s.mul_zero s.one)).symm))

#print axioms first_div_domain
#print axioms second_div_domain
#print axioms zero_numerator_keeps_domain
#print axioms eval_functional
#print axioms partial_fold_nil
#print axioms partial_fold_snoc
#print axioms partial_fold_append
#print axioms commutative_fold_agreement
#print axioms zero_denominator_refused
#print axioms undefined_first_prefix_persists
#print axioms undefined_second_prefix_persists
#print axioms grow_left_eval
#print axioms left_tree_correspondence
#print axioms left_tree_snoc
#print axioms right_tree_snoc
#print axioms mirror_involution
#print axioms mirror_fold
#print axioms mirror_left_tree
#print axioms mirror_eval
#print axioms right_tree_correspondence
#print axioms partial_fold_functional
#print axioms shuffle_nil_right
#print axioms shuffle_nil_left
#print axioms shuffle_with_right_empty
#print axioms shuffle_with_left_empty
#print axioms grow_left_trace
#print axioms grow_right_trace
#print axioms trace_fold_from
#print axioms comb_trace_characterization
#print axioms comb_legal_order_unique
#print axioms inverse_nonzero
#print axioms zero_add
#print axioms one_mul
#print axioms zero_mul
#print axioms add_left_cancel
#print axioms neg_one_mul
#print axioms neg_one_nonzero
#print axioms affine_left_inverse
#print axioms affine_right_inverse
#print axioms first_add_affine
#print axioms first_sub_affine
#print axioms first_mul_affine
#print axioms first_div_affine
#print axioms second_add_affine
#print axioms second_sub_affine
#print axioms second_mul_affine
#print axioms second_div_value
#print axioms addition_sections_agree
#print axioms multiplication_sections_agree
#print axioms reciprocal_scale_identity
#print axioms guarded_reciprocal_scale
#print axioms mul_left_cancel
#print axioms constant_pair_coincidence
#print axioms nonzero_constant_pair_coincidence
#print axioms marked_words_distinct
#print axioms reciprocal_infinity
#print axioms ordinary_reciprocal_projective_match
#print axioms reciprocal_not_infinity_stabilizing
#print axioms reciprocal_raw_infinity
#print axioms reciprocal_raw_zero
#print axioms reciprocal_raw_preserves_nonzero
#print axioms zero_reciprocal_raw_invalid
#print axioms zero_scale_not_injective
end AEGPaper0.Chapter02
