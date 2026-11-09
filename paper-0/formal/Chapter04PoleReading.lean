import ProjectiveBruhat

/- Original CC0 proofs by Codex (OpenAI), 2026-11-09.
   The rightmost translation in T D J T reads the quotient pole.
   A pole fiber is not a point stabilizer or equality of operators. -/
noncomputable section
namespace AEGPaper0.Chapter04PoleReading

open ProjectiveLine ProjectiveGeneralLinear ProjectiveGeneration
open Chapter04ProjectiveBridge
open ProjectiveBruhat AffineStabilizer
variable {K : Type*} [Field K]

def bruhatWord (a : K) (u : Kˣ) (t : K) : PGL2 K :=
  translationClass a * (dilationClass u * (inversionClass * translationClass t))

theorem rightmost_translation_reads_pole (a : K) (u : Kˣ) (t : K) :
    quotientPole (bruhatWord a u t)=some (-t) := by
  apply ((quotientPole_unique_preimage _ (some (-t))).mp ?_).symm
  simp only [bruhatWord, quotient_action_mul, translationClass_finite,
    neg_add_cancel, inversionClass_zero, dilationClass_infinity, translationClass_infinity]

theorem bruhat_word_in_bigCell (a : K) (u : Kˣ) (t : K) : bruhatWord a u t ∈ bigCell := by
  rw [bigCell_iff_finite_pole]
  exact ⟨-t, rightmost_translation_reads_pole a u t⟩

theorem bruhat_word_poles_equal_iff (a b : K) (u v : Kˣ) (t s : K) :
    quotientPole (bruhatWord a u t)=quotientPole (bruhatWord b v s) ↔ t=s := by
  simp only [rightmost_translation_reads_pole, Option.some.injEq, neg_inj]

theorem pole_invariant_under_affine_output (b g : PGL2 K) (hb : b ∈ infinityStabilizer) :
    quotientPole (b*g)=quotientPole g := by
  rw [quotientPole_product, (quotientPole_infinity_iff b).mpr hb]
  rfl

theorem rightmost_translation_unique (g : PGL2 K) (a b t s : K) (u v : Kˣ)
    (h : g=bruhatWord a u t) (k : g=bruhatWord b v s) : t=s := by
  exact (bruhat_word_poles_equal_iff a b u v t s).mp (congrArg quotientPole (h.symm.trans k))

theorem matrix_bruhat_word (m : Matrix2 K) (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    ofMatrix m hm=bruhatWord (m.a/m.c)
      (Units.mk0 (determinant m/m.c^2) (nonaffine_scale_nonzero m hm hc)) (m.d/m.c) :=
  quotient_nonaffine_factorization m hm hc

theorem matrix_pole_from_rightmost_translation (m : Matrix2 K)
    (hm : determinant m ≠ 0) (hc : m.c ≠ 0) :
    quotientPole (ofMatrix m hm)=some (-(m.d/m.c)) := by
  rw [matrix_bruhat_word m hm hc, rightmost_translation_reads_pole]

theorem affine_cell_pole_reading (g : PGL2 K) :
    g ∈ infinityStabilizer ↔ quotientPole g=none := (quotientPole_infinity_iff g).symm

theorem projective_cell_pole_reading (g : PGL2 K) :
    g ∈ bigCell ↔ ∃ t : K, quotientPole g=some (-t) := by
  rw [bigCell_iff_finite_pole]
  constructor <;> rintro ⟨q,h⟩
  · exact ⟨-q,by simpa only [neg_neg] using h⟩
  · exact ⟨-q,h⟩

theorem same_pole_distinct_output (g : PGL2 K) (s z : K) (hs : s ≠ 0)
    (hz : quotientAction g none=some z) :
    quotientPole (translationClass s*g)=quotientPole g ∧
      quotientAction (translationClass s*g) none ≠ quotientAction g none := by
  refine ⟨pole_invariant_under_affine_output _ g (translation_in_stabilizer s),?_⟩
  rw [quotient_action_mul,hz,translationClass_finite]
  intro he
  have he' := Option.some.inj he
  exact hs (add_left_cancel (he'.trans (add_zero z).symm))

#print axioms AEGPaper0.Chapter04PoleReading.rightmost_translation_reads_pole
#print axioms AEGPaper0.Chapter04PoleReading.bruhat_word_in_bigCell
#print axioms AEGPaper0.Chapter04PoleReading.bruhat_word_poles_equal_iff
#print axioms AEGPaper0.Chapter04PoleReading.pole_invariant_under_affine_output
#print axioms AEGPaper0.Chapter04PoleReading.rightmost_translation_unique
#print axioms AEGPaper0.Chapter04PoleReading.matrix_bruhat_word
#print axioms AEGPaper0.Chapter04PoleReading.matrix_pole_from_rightmost_translation
#print axioms AEGPaper0.Chapter04PoleReading.affine_cell_pole_reading
#print axioms AEGPaper0.Chapter04PoleReading.projective_cell_pole_reading
#print axioms AEGPaper0.Chapter04PoleReading.same_pole_distinct_output
end AEGPaper0.Chapter04PoleReading
