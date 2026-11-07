import Chapter02Domains
import AffineStabilizer

/- Original CC0 proofs by Codex (OpenAI), 2026-11-07.
   Pure first-slot and second-slot words reuse the Chapter 2 syntax and partial
   semantics. Chronological concatenation reverses group multiplication.
   Projective continuation never licenses an ordinary division by zero. -/
namespace AEGPaper0.ProjectiveArithmetic

noncomputable section
open Chapter02 ProjectiveLine ProjectiveGeneralLinear Chapter04ProjectiveBridge
open ProjectiveGeneration AffineStabilizer
variable {K : Type*} [Field K]

def fieldData : FieldData K where
  add := (· + ·)
  mul := (· * ·)
  zero := 0
  one := 1
  add_assoc := add_assoc
  add_comm := add_comm
  add_zero := add_zero
  mul_assoc := mul_assoc
  mul_comm := mul_comm
  mul_one := mul_one
  mul_add := mul_add
  mul_zero := mul_zero
  neg := (- ·)
  inv := Inv.inv
  add_neg := add_neg_cancel
  inv_zero := inv_zero
  mul_inv := fun _ h => mul_inv_cancel₀ h
  zero_ne_one := zero_ne_one

def regular : Op → K → Prop
  | .add, _ | .sub, _ => True
  | .mul, c | .div, c => c ≠ 0

def sectionMatrix : Slot → Op → K → Matrix2 K
  | _, .add, c => ⟨1,c,0,1⟩
  | .first, .sub, c => ⟨1,-c,0,1⟩
  | .second, .sub, c => ⟨-1,c,0,1⟩
  | _, .mul, c => ⟨c,0,0,1⟩
  | .first, .div, c => ⟨1,0,0,c⟩
  | .second, .div, c => ⟨0,c,1,0⟩

theorem section_nondegenerate_iff (slot : Slot) (op : Op) (c : K) :
    determinant (sectionMatrix slot op c) ≠ 0 ↔ regular op c := by
  cases slot <;> cases op <;> simp [sectionMatrix, determinant, regular]

def sectionClass (slot : Slot) (op : Op) (c : K) (h : regular op c) : PGL2 K :=
  ofMatrix (sectionMatrix slot op c) ((section_nondegenerate_iff slot op c).mpr h)

theorem section_finite_iff (slot : Slot) (op : Op) (c x y : K) (h : regular op c) :
    act (sectionMatrix slot op c) (some x) = some y ↔ Section fieldData slot op c x y := by
  cases slot <;> cases op <;>
    simp only [sectionMatrix, finite_action, Section, Eval, fieldData, regular] at h ⊢
  all_goals simp_all [div_eq_mul_inv, mul_comm, add_comm, eq_comm]

theorem sectionClass_finite_iff (slot : Slot) (op : Op) (c x y : K) (h : regular op c) :
    quotientAction (sectionClass slot op c h) (some x) = some y ↔ Section fieldData slot op c x y := by
  rw [sectionClass, ofMatrix_action]
  exact section_finite_iff slot op c x y h

def regularWord (word : List (Op × K)) : Prop := ∀ sc ∈ word, regular sc.1 sc.2

theorem regularWord_cons (sc : Op × K) (word : List (Op × K)) :
    regularWord (sc::word) ↔ regular sc.1 sc.2 ∧ regularWord word := by
  simp [regularWord]

def wordMatrix (slot : Slot) : List (Op × K) → Matrix2 K
  | [] => identity
  | (op,c)::rest => multiply (wordMatrix slot rest) (sectionMatrix slot op c)

theorem word_nondegenerate (slot : Slot) (word : List (Op × K)) (h : regularWord word) :
    determinant (wordMatrix slot word) ≠ 0 := by
  induction word with
  | nil => simp [wordMatrix, identity, determinant]
  | cons sc rest ih =>
    rw [wordMatrix, determinant_multiply]
    exact mul_ne_zero (ih ((regularWord_cons sc rest).mp h).2)
      ((section_nondegenerate_iff slot sc.1 sc.2).mpr ((regularWord_cons sc rest).mp h).1)

def wordClass (slot : Slot) (word : List (Op × K)) (h : regularWord word) : PGL2 K :=
  ofMatrix (wordMatrix slot word) (word_nondegenerate slot word h)

theorem wordClass_nil (slot : Slot) (h : regularWord ([] : List (Op × K))) : wordClass slot [] h = 1 := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  rw [wordClass, ofMatrix_action, quotient_action_one]
  exact action_identity x

theorem wordClass_cons (slot : Slot) (sc : Op × K) (rest : List (Op × K)) (h : regularWord (sc::rest)) :
    wordClass slot (sc::rest) h = wordClass slot rest ((regularWord_cons sc rest).mp h).2 *
      sectionClass slot sc.1 sc.2 ((regularWord_cons sc rest).mp h).1 := by
  exact ofMatrix_product _ _ _ _ _

theorem regularWord_append (before after : List (Op × K)) :
    regularWord (before++after) ↔ regularWord before ∧ regularWord after := by
  simp [regularWord, List.mem_append, or_imp, forall_and]

theorem wordMatrix_append (slot : Slot) (before after : List (Op × K)) :
    wordMatrix slot (before++after) = multiply (wordMatrix slot after) (wordMatrix slot before) := by
  induction before with
  | nil => simp [wordMatrix, ProjectiveFaithfulness.multiply_one_right]
  | cons sc rest ih =>
    simp only [List.cons_append, wordMatrix, ih, ProjectiveFaithfulness.multiply_assoc]

theorem wordClass_append (slot : Slot) (before after : List (Op × K)) (h : regularWord (before++after)) :
    wordClass slot (before++after) h = wordClass slot after ((regularWord_append before after).mp h).2 *
      wordClass slot before ((regularWord_append before after).mp h).1 := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  simp only [wordClass, quotient_action_mul, ofMatrix_action]
  rw [wordMatrix_append]
  exact action_multiply _ _ x (word_nondegenerate slot before ((regularWord_append before after).mp h).1)

def run (slot : Slot) : List (Op × K) → ProjectiveLine.Point K → List (ProjectiveLine.Point K)
  | [], x => [x]
  | (op,c)::rest, x => x :: run slot rest (act (sectionMatrix slot op c) x)

def safe (slot : Slot) : List (Op × K) → ProjectiveLine.Point K → Prop
  | [], x => x ≠ none
  | (op,c)::rest, x => x ≠ none ∧ safe slot rest (act (sectionMatrix slot op c) x)

theorem safe_iff_run_finite (slot : Slot) (word : List (Op × K)) (x : ProjectiveLine.Point K) :
    safe slot word x ↔ ∀ p ∈ run slot word x, p ≠ none := by
  induction word generalizing x with
  | nil => simp [safe, run]
  | cons sc rest ih => simp [safe, run, ih]

theorem safe_initial_finite (slot : Slot) (word : List (Op × K)) (x : ProjectiveLine.Point K)
    (h : safe slot word x) : x ≠ none := by
  cases word with
  | nil => exact h
  | cons => exact h.1

def relation (slot : Slot) (op : Op) (x c y : K) : Prop := Section fieldData slot op c x y

theorem ordinary_iff_safe (slot : Slot) (word : List (Op × K)) (h : regularWord word) (x y : K) :
    PartialFold (relation slot) word x y ↔
      safe slot word (some x) ∧ quotientAction (wordClass slot word h) (some x) = some y := by
  induction word generalizing x with
  | nil => simp [PartialFold, safe, wordClass_nil, eq_comm]
  | cons sc rest ih =>
    have hr := (regularWord_cons sc rest).mp h
    rw [wordClass_cons, quotient_action_mul]
    simp only [PartialFold, safe, ne_eq, reduceCtorEq, not_false_eq_true, true_and]
    constructor
    · rintro ⟨z,hz,ht⟩
      have hs := (section_finite_iff slot sc.1 sc.2 x z hr.1).mpr hz
      have hq := (sectionClass_finite_iff slot sc.1 sc.2 x z hr.1).mpr hz
      rw [hs, hq]
      exact (ih hr.2 z).mp ht
    · rintro ⟨hs,hq⟩
      have hn := safe_initial_finite slot rest _ hs
      cases he : act (sectionMatrix slot sc.1 sc.2) (some x) with
      | none => exact False.elim (hn he)
      | some z =>
        have hz := (section_finite_iff slot sc.1 sc.2 x z hr.1).mp he
        have heq := (sectionClass_finite_iff slot sc.1 sc.2 x z hr.1).mpr hz
        rw [he] at hs
        rw [heq] at hq
        exact ⟨z,hz,(ih hr.2 z).mpr ⟨hs,hq⟩⟩

theorem left_tree_projective_match (word : List (Op × K)) (h : regularWord word) (x y : K) :
    TreeEval (Eval fieldData) x (leftTree word) y ↔
      safe .first word (some x) ∧ quotientAction (wordClass .first word h) (some x)=some y := by
  rw [left_tree_correspondence]
  exact ordinary_iff_safe .first word h x y

theorem right_tree_projective_match (word : List (Op × K)) (h : regularWord word) (x y : K) :
    TreeEval (Eval fieldData) x (rightTree word) y ↔
      safe .second word (some x) ∧ quotientAction (wordClass .second word h) (some x)=some y := by
  rw [right_tree_correspondence]
  exact ordinary_iff_safe .second word h x y

theorem ordinary_domain_iff_safe (slot : Slot) (word : List (Op × K)) (h : regularWord word) (x : K) :
    (∃ y, PartialFold (relation slot) word x y) ↔ safe slot word (some x) := by
  constructor
  · rintro ⟨y,hy⟩; exact ((ordinary_iff_safe slot word h x y).mp hy).1
  · intro hs
    have hn : quotientAction (wordClass slot word h) (some x) ≠ none := by
      induction word generalizing x with
      | nil => rw [wordClass_nil, quotient_action_one]; exact Option.some_ne_none _
      | cons sc rest ih =>
        have hr := (regularWord_cons sc rest).mp h
        have hi := safe_initial_finite slot rest _ hs.2
        cases he : act (sectionMatrix slot sc.1 sc.2) (some x) with
        | none => exact False.elim (hi he)
        | some z =>
          rw [wordClass_cons, quotient_action_mul,
            (sectionClass_finite_iff slot sc.1 sc.2 x z hr.1).mpr
              ((section_finite_iff slot sc.1 sc.2 x z hr.1).mp he)]
          exact ih hr.2 z (by simpa [safe, he] using hs)
    cases he : quotientAction (wordClass slot word h) (some x) with
    | none => exact False.elim (hn he)
    | some y => exact ⟨y,(ordinary_iff_safe slot word h x y).mpr ⟨hs,he⟩⟩

theorem first_section_fixes_infinity (op : Op) (c : K) (h : regular op c) :
    quotientAction (sectionClass .first op c h) none=none := by
  rw [sectionClass, ofMatrix_action, fixes_infinity_iff]
  cases op <;> rfl

theorem first_section_has_finite_value (op : Op) (c x : K) (h : regular op c) :
    ∃ y, act (sectionMatrix .first op c) (some x)=some y := by
  cases op <;> simp_all [sectionMatrix, finite_action, regular]

theorem first_word_safe (word : List (Op × K)) (h : regularWord word) (x : K) :
    safe .first word (some x) := by
  induction word generalizing x with
  | nil => exact Option.some_ne_none _
  | cons sc rest ih =>
    have hr := (regularWord_cons sc rest).mp h
    obtain ⟨z,he⟩ := first_section_has_finite_value sc.1 sc.2 x hr.1
    exact ⟨Option.some_ne_none _,by rw [he]; exact ih hr.2 z⟩

theorem first_word_ordinary_total (word : List (Op × K)) (h : regularWord word) (x : K) :
    ∃ y, PartialFold (relation .first) word x y :=
  (ordinary_domain_iff_safe .first word h x).mpr (first_word_safe word h x)

theorem first_word_in_stabilizer (word : List (Op × K)) (h : regularWord word) :
    wordClass .first word h ∈ infinityStabilizer := by
  induction word with
  | nil => rw [wordClass_nil]; exact Subgroup.one_mem _
  | cons sc rest ih =>
    rw [wordClass_cons]
    exact Subgroup.mul_mem _ (ih _) (first_section_fixes_infinity sc.1 sc.2 _)

theorem sectionClass_add (slot : Slot) (c : K) (h : regular .add c) :
    sectionClass slot .add c h=translationClass c := by cases slot <;> rfl

theorem sectionClass_mul (slot : Slot) (c : K) (h : regular .mul c) :
    sectionClass slot .mul c h=dilationClass (Units.mk0 c h) := by cases slot <;> rfl

theorem second_division_is_inversion (h : regular .div (-1:K)) :
    sectionClass .second .div (-1:K) h=inversionClass := rfl

theorem affine_word_realizes (slot : Slot) (a b : K) (ha : a ≠ 0) :
    ∃ h : regularWord [(.mul,a),(.add,b)],
      wordClass slot [(.mul,a),(.add,b)] h=affineClass (normalizedAffine a b ha) := by
  refine ⟨by simp [regularWord, regular, ha], ?_⟩
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  cases x with
  | none =>
    rw [wordClass_cons, wordClass_cons, wordClass_nil, _root_.one_mul, quotient_action_mul,
      sectionClass_mul, dilationClass_infinity, sectionClass_add, translationClass_infinity, affineClass_infinity]
  | some x =>
    rw [wordClass_cons, wordClass_cons, wordClass_nil, _root_.one_mul, quotient_action_mul,
      sectionClass_mul, dilationClass_finite, sectionClass_add, translationClass_finite, affineClass_finite]
    rfl

theorem first_word_image_is_stabilizer (q : PGL2 K) :
    (∃ word, ∃ h : regularWord word, wordClass .first word h=q) ↔ q ∈ infinityStabilizer := by
  constructor
  · rintro ⟨word,h,rfl⟩; exact first_word_in_stabilizer word h
  · intro hq
    obtain ⟨e,he⟩ := toStabilizer_surjective ⟨q,hq⟩
    have heq : affineClass e=q := congrArg Subtype.val he
    obtain ⟨h,hh⟩ := affine_word_realizes .first (AffineStabilizer.slope e) (offset e) (slope_nonzero e)
    refine ⟨_,h,hh.trans ?_⟩
    rw [← heq]
    apply congrArg affineClass
    apply AffineEquiv.ext
    intro x
    exact (affine_formula e x).symm

theorem second_word_surjective (q : PGL2 K) :
    ∃ word : List (Op × K), ∃ h : regularWord word,
      word.length ≤ 4 ∧ wordClass .second word h=q := by
  obtain ⟨m,hm,rfl⟩ := ofMatrix_surjective q
  by_cases hc : m.c=0
  · have ha := div_ne_zero (affine_diagonal_nonzero m hm hc).1 (affine_diagonal_nonzero m hm hc).2
    obtain ⟨h,he⟩ := affine_word_realizes .second (m.a/m.d) (m.b/m.d) ha
    exact ⟨_,h,by simp,he.trans (affine_matrix_class_normal_form m hm hc).symm⟩
  · have hn := nonaffine_scale_nonzero m hm hc
    refine ⟨[(.add,m.d/m.c),(.div,-1),(.mul,determinant m/m.c^2),(.add,m.a/m.c)],
      by simp [regularWord, regular, hn], by simp, ?_⟩
    rw [quotient_nonaffine_factorization m hm hc]
    simp only [wordClass_cons, wordClass_nil, sectionClass_add, sectionClass_mul,
      second_division_is_inversion, _root_.one_mul, _root_.mul_assoc]

theorem second_word_image_is_top :
    {q : PGL2 K | ∃ word, ∃ h : regularWord word, wordClass .second word h=q}=Set.univ := by
  apply Set.eq_univ_of_forall
  intro q
  obtain ⟨word,h,_,he⟩ := second_word_surjective q
  exact ⟨word,h,he⟩

def reciprocalWord : List (Op × K) := [(.div,1),(.div,1)]

theorem reciprocal_word_regular : regularWord (reciprocalWord (K := K)) := by
  simp [regularWord, reciprocalWord, regular]

theorem reciprocal_word_class_identity :
    wordClass .second reciprocalWord reciprocal_word_regular=(1 : PGL2 K) := by
  apply quotient_action_injective
  apply Equiv.ext
  intro x
  rw [wordClass, ofMatrix_action, quotient_action_one]
  have he : wordMatrix .second (reciprocalWord (K := K))=identity := by
    simp [wordMatrix, reciprocalWord, sectionMatrix, multiply, identity]
  rw [he]
  exact action_identity x

theorem reciprocal_word_zero_unsafe : ¬ safe .second (reciprocalWord (K := K)) (some 0) := by
  simp [safe, reciprocalWord, sectionMatrix, finite_action]

theorem reciprocal_word_no_ordinary_zero (y : K) :
    ¬ PartialFold (relation .second) reciprocalWord 0 y := by
  intro h
  exact reciprocal_word_zero_unsafe ((ordinary_iff_safe .second _ reciprocal_word_regular 0 y).mp h).1

theorem group_equality_does_not_determine_domain :
    wordClass .second (reciprocalWord (K := K)) reciprocal_word_regular=wordClass .second [] (by simp [regularWord]) ∧
    safe .second ([] : List (Op × K)) (some (0:K)) ∧ ¬ safe .second reciprocalWord (some (0:K)) := by
  rw [reciprocal_word_class_identity, wordClass_nil]
  exact ⟨rfl,Option.some_ne_none _,reciprocal_word_zero_unsafe⟩

theorem reciprocal_word_syntax_distinct : (reciprocalWord (K := K)) ≠ [] := by
  simp [reciprocalWord]

theorem zero_multiplication_ordinary (slot : Slot) (x : K) :
    Section fieldData slot .mul 0 x 0 ∧ ¬ regular .mul (0:K) := by
  cases slot <;> simp [Section, Eval, fieldData, regular]

end
end AEGPaper0.ProjectiveArithmetic

#print axioms AEGPaper0.ProjectiveArithmetic.section_nondegenerate_iff
#print axioms AEGPaper0.ProjectiveArithmetic.section_finite_iff
#print axioms AEGPaper0.ProjectiveArithmetic.sectionClass_finite_iff
#print axioms AEGPaper0.ProjectiveArithmetic.regularWord_cons
#print axioms AEGPaper0.ProjectiveArithmetic.word_nondegenerate
#print axioms AEGPaper0.ProjectiveArithmetic.wordClass_nil
#print axioms AEGPaper0.ProjectiveArithmetic.wordClass_cons
#print axioms AEGPaper0.ProjectiveArithmetic.regularWord_append
#print axioms AEGPaper0.ProjectiveArithmetic.wordMatrix_append
#print axioms AEGPaper0.ProjectiveArithmetic.wordClass_append
#print axioms AEGPaper0.ProjectiveArithmetic.safe_iff_run_finite
#print axioms AEGPaper0.ProjectiveArithmetic.safe_initial_finite
#print axioms AEGPaper0.ProjectiveArithmetic.ordinary_iff_safe
#print axioms AEGPaper0.ProjectiveArithmetic.left_tree_projective_match
#print axioms AEGPaper0.ProjectiveArithmetic.right_tree_projective_match
#print axioms AEGPaper0.ProjectiveArithmetic.ordinary_domain_iff_safe
#print axioms AEGPaper0.ProjectiveArithmetic.first_section_fixes_infinity
#print axioms AEGPaper0.ProjectiveArithmetic.first_section_has_finite_value
#print axioms AEGPaper0.ProjectiveArithmetic.first_word_safe
#print axioms AEGPaper0.ProjectiveArithmetic.first_word_ordinary_total
#print axioms AEGPaper0.ProjectiveArithmetic.first_word_in_stabilizer
#print axioms AEGPaper0.ProjectiveArithmetic.sectionClass_add
#print axioms AEGPaper0.ProjectiveArithmetic.sectionClass_mul
#print axioms AEGPaper0.ProjectiveArithmetic.second_division_is_inversion
#print axioms AEGPaper0.ProjectiveArithmetic.affine_word_realizes
#print axioms AEGPaper0.ProjectiveArithmetic.first_word_image_is_stabilizer
#print axioms AEGPaper0.ProjectiveArithmetic.second_word_surjective
#print axioms AEGPaper0.ProjectiveArithmetic.second_word_image_is_top
#print axioms AEGPaper0.ProjectiveArithmetic.reciprocal_word_regular
#print axioms AEGPaper0.ProjectiveArithmetic.reciprocal_word_class_identity
#print axioms AEGPaper0.ProjectiveArithmetic.reciprocal_word_zero_unsafe
#print axioms AEGPaper0.ProjectiveArithmetic.reciprocal_word_no_ordinary_zero
#print axioms AEGPaper0.ProjectiveArithmetic.group_equality_does_not_determine_domain
#print axioms AEGPaper0.ProjectiveArithmetic.reciprocal_word_syntax_distinct
#print axioms AEGPaper0.ProjectiveArithmetic.zero_multiplication_ordinary
