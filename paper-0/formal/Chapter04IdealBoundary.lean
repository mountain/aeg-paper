import Chapter04Horocycles
import Chapter04ProjectiveBridge
import Mathlib.Topology.Compactification.OnePoint.Basic

/- Original CC0 proofs by Codex (OpenAI), 2026-11-09.
   The ideal boundary model is the topological frontier of the upper plane
   inside OnePoint Complex, identified with OnePoint Real. This is not a
   classification of all geodesic rays modulo bounded-distance equivalence. -/
noncomputable section
namespace AEGPaper0.Chapter04IdealBoundary
open Filter Set Real
open scoped UpperHalfPlane Topology
open Chapter04Horocycles

abbrev Boundary := OnePoint ℝ
abbrev Ambient := OnePoint ℂ
def embed : Boundary → Ambient := OnePoint.map Complex.ofReal
def upperImage : Set Ambient := OnePoint.some '' {z : ℂ | 0 < z.im}
def closedUpper : Set Ambient := OnePoint.some '' {z : ℂ | 0 ≤ z.im} ∪ {OnePoint.infty}

def poleBoundaryEquiv : ProjectiveLine.Point ℝ ≃ Boundary := Equiv.refl _

def boundaryPole (m : ProjectiveLine.Matrix2 ℝ) (hm : ProjectiveLine.determinant m ≠ 0) : Boundary :=
  poleBoundaryEquiv (Chapter04ProjectiveBridge.matrixPole m hm)

theorem boundary_pole_finite (m : ProjectiveLine.Matrix2 ℝ)
    (hm : ProjectiveLine.determinant m ≠ 0) (hc : m.c ≠ 0) :
    boundaryPole m hm=OnePoint.some (-m.d/m.c) :=
  Chapter04ProjectiveBridge.concrete_finite_pole m hm hc

theorem boundary_pole_infinity (m : ProjectiveLine.Matrix2 ℝ)
    (hm : ProjectiveLine.determinant m ≠ 0) : boundaryPole m hm=OnePoint.infty ↔ m.c=0 :=
  Chapter04ProjectiveBridge.concrete_pole_at_infinity_iff m hm

theorem embed_continuous : Continuous embed := by
  apply OnePoint.continuous_map Complex.continuous_ofReal
  simpa only [coclosedCompact_eq_cocompact] using
    Complex.isometry_ofReal.isClosedEmbedding.tendsto_cocompact

theorem embed_injective : Function.Injective embed := by
  intro p q h
  cases p with
  | none => cases q with
    | none => rfl
    | some y => cases h
  | some x => cases q with
    | none => cases h
    | some y =>
      have he : (x : ℂ)=(y : ℂ) := Option.some.inj h
      exact congrArg OnePoint.some (Complex.ofReal_inj.mp he)

theorem boundary_compact : IsCompact (Set.range embed) := isCompact_range embed_continuous

theorem boundary_closed : IsClosed (Set.range embed) := boundary_compact.isClosed

theorem embed_finite (q : ℝ) : embed (OnePoint.some q)=OnePoint.some (q : ℂ) := rfl

theorem embed_infinity : embed OnePoint.infty=OnePoint.infty := rfl

theorem upper_image_open : IsOpen upperImage :=
  OnePoint.isOpen_image_coe.mpr (isOpen_lt continuous_const Complex.continuous_im)

theorem upper_image_finite (z : ℂ) : OnePoint.some z ∈ upperImage ↔ 0 < z.im := by
  change (∃ w : ℂ, 0 < w.im ∧ Option.some w=Option.some z) ↔ _
  simp only [Option.some.injEq, exists_eq_right]

theorem closed_upper_finite (z : ℂ) : OnePoint.some z ∈ closedUpper ↔ 0 ≤ z.im := by
  change ((∃ w : ℂ, 0 ≤ w.im ∧ Option.some w=Option.some z) ∨ Option.some z=none) ↔ _
  simp only [Option.some.injEq, exists_eq_right, Option.some_ne_none, or_false]

theorem closed_upper_closed : IsClosed closedUpper := by
  apply (OnePoint.isClosed_iff_of_mem (by right; rfl : OnePoint.infty ∈ closedUpper)).mpr
  have he : (OnePoint.some : ℂ → Ambient) ⁻¹' closedUpper={z : ℂ | 0 ≤ z.im} := by
    ext z; exact closed_upper_finite z
  rw [he]
  exact isClosed_le continuous_const Complex.continuous_im

theorem finite_ray_tendsto (q : ℝ) :
    Tendsto (fun s => OnePoint.some (basedRay q s : ℂ)) atTop (𝓝 (embed (OnePoint.some q))) := by
  have h : Tendsto (fun s => (q : ℂ)+(Real.exp (-s) : ℂ)*Complex.I) atTop (𝓝 (q : ℂ)) := by
    simpa using tendsto_const_nhds.add (Real.tendsto_exp_neg_atTop_nhds_zero.ofReal.mul_const Complex.I)
  have h' := OnePoint.continuous_coe.tendsto (q : ℂ) |>.comp h
  have he : (fun s => (basedRay q s : ℂ))=(fun s => (q : ℂ)+(Real.exp (-s) : ℂ)*Complex.I) := by
    funext s
    rw [based_ray_vertical]
    exact (Complex.re_add_im (⟨q,Real.exp (-s)⟩ : ℂ)).symm
  rw [show embed (OnePoint.some q)=OnePoint.some (q : ℂ) from rfl]
  change Tendsto ((OnePoint.some : ℂ → Ambient) ∘ fun s => (basedRay q s : ℂ)) atTop _
  rw [he]
  exact h'

theorem infinity_ray_tendsto :
    Tendsto (fun s => OnePoint.some (vertical 0 s : ℂ)) atTop (𝓝 (embed OnePoint.infty)) := by
  have hn : Tendsto (fun s => ‖(vertical 0 s : ℂ)‖) atTop atTop := by
    convert Real.tendsto_exp_atTop using 1
    funext s
    simp [vertical, Complex.norm_def, Complex.normSq_apply, Real.sqrt_mul_self (le_of_lt (exp_pos s))]
  have hc : Tendsto (fun s => (vertical 0 s : ℂ)) atTop (coclosedCompact ℂ) := by
    rw [coclosedCompact_eq_cocompact]
    exact (tendsto_norm_atTop_iff_cobounded.mp hn).mono_right Metric.cobounded_le_cocompact
  exact OnePoint.tendsto_coe_infty.comp hc

theorem boundary_in_closure : Set.range embed ⊆ closure upperImage := by
  rintro _ ⟨p,rfl⟩
  cases p with
  | none =>
    apply mem_closure_of_tendsto infinity_ray_tendsto
    exact Eventually.of_forall (fun s => ⟨(vertical 0 s : ℂ), (vertical 0 s).im_pos, rfl⟩)
  | some q =>
    apply mem_closure_of_tendsto (finite_ray_tendsto q)
    exact Eventually.of_forall (fun s => ⟨(basedRay q s : ℂ), (basedRay q s).im_pos, rfl⟩)

theorem closed_upper_decomposition : closedUpper=upperImage ∪ Set.range embed := by
  ext p
  cases p with
  | none =>
    constructor
    · intro _; right; exact ⟨OnePoint.infty,rfl⟩
    · intro _; right; rfl
  | some z =>
    change OnePoint.some z ∈ closedUpper ↔ OnePoint.some z ∈ upperImage ∪ Set.range embed
    rw [closed_upper_finite]
    change 0 ≤ z.im ↔ OnePoint.some z ∈ upperImage ∨ OnePoint.some z ∈ Set.range embed
    rw [upper_image_finite]
    constructor
    · intro hz
      by_cases hp : 0 < z.im
      · exact Or.inl hp
      · have he : z.im=0 := le_antisymm (le_of_not_gt hp) hz
        right
        exact ⟨OnePoint.some z.re, by rw [embed_finite]; congr 1; exact Complex.ext rfl (by simpa using he.symm)⟩
    · rintro (hw | ⟨q,hq⟩)
      · exact hw.le
      · cases q with
        | none => exact False.elim (OnePoint.infty_ne_coe z hq)
        | some x =>
          have he : (x : ℂ)=z := Option.some.inj hq
          have hi := congrArg Complex.im he
          simpa only [Complex.ofReal_im] using le_of_eq hi

theorem closure_upper_image : closure upperImage=closedUpper := by
  apply Set.Subset.antisymm
  · apply closure_minimal _ closed_upper_closed
    rintro _ ⟨z,hz,rfl⟩
    exact Or.inl ⟨z,(show 0 < z.im from hz).le,rfl⟩
  · rw [closed_upper_decomposition]
    exact Set.union_subset subset_closure boundary_in_closure

theorem upper_boundary_disjoint : Disjoint upperImage (Set.range embed) := by
  apply Set.disjoint_left.mpr
  rintro _ ⟨z,hz,rfl⟩ ⟨q,hq⟩
  cases q with
  | none => exact OnePoint.infty_ne_coe z hq
  | some q =>
    have hi := congrArg Complex.im (OnePoint.coe_injective hq)
    simp only [Complex.ofReal_im] at hi
    exact (ne_of_gt hz) hi.symm

theorem frontier_upper_image : frontier upperImage=Set.range embed := by
  rw [frontier, upper_image_open.interior_eq, closure_upper_image, closed_upper_decomposition]
  apply Set.union_diff_cancel_left
  rintro x ⟨hx,he⟩
  exact (Set.disjoint_left.mp upper_boundary_disjoint hx he).elim

#print axioms AEGPaper0.Chapter04IdealBoundary.boundary_pole_finite
#print axioms AEGPaper0.Chapter04IdealBoundary.boundary_pole_infinity
#print axioms AEGPaper0.Chapter04IdealBoundary.embed_continuous
#print axioms AEGPaper0.Chapter04IdealBoundary.embed_injective
#print axioms AEGPaper0.Chapter04IdealBoundary.boundary_compact
#print axioms AEGPaper0.Chapter04IdealBoundary.boundary_closed
#print axioms AEGPaper0.Chapter04IdealBoundary.embed_finite
#print axioms AEGPaper0.Chapter04IdealBoundary.embed_infinity
#print axioms AEGPaper0.Chapter04IdealBoundary.upper_image_open
#print axioms AEGPaper0.Chapter04IdealBoundary.upper_image_finite
#print axioms AEGPaper0.Chapter04IdealBoundary.closed_upper_finite
#print axioms AEGPaper0.Chapter04IdealBoundary.closed_upper_closed
#print axioms AEGPaper0.Chapter04IdealBoundary.finite_ray_tendsto
#print axioms AEGPaper0.Chapter04IdealBoundary.infinity_ray_tendsto
#print axioms AEGPaper0.Chapter04IdealBoundary.boundary_in_closure
#print axioms AEGPaper0.Chapter04IdealBoundary.closed_upper_decomposition
#print axioms AEGPaper0.Chapter04IdealBoundary.closure_upper_image
#print axioms AEGPaper0.Chapter04IdealBoundary.upper_boundary_disjoint
#print axioms AEGPaper0.Chapter04IdealBoundary.frontier_upper_image
end AEGPaper0.Chapter04IdealBoundary
