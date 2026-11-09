import Chapter04IdealBoundary
import Chapter04Tangency

/- Original CC0 proofs by Codex (OpenAI), 2026-11-09.
   The closure of a finite-based intrinsic horosphere meets the actual
   compactified boundary at exactly its base. Differential tangency is
   interpreted in the ambient continuation chart, not a boundary metric. -/
noncomputable section
namespace AEGPaper0.Chapter04HorocycleBoundary
open Filter Set Real
open scoped UpperHalfPlane Topology
open Chapter04Horocycles Chapter04IdealBoundary Chapter04Tangency

def circleSet (q r : ℝ) : Set ℂ := {z | circleResidual q r (z.re,z.im)=0}
def horosphereImage (q t : ℝ) : Set Ambient :=
  (fun z : ℍ => OnePoint.some (z : ℂ)) '' finiteHorosphere q (-log t)

theorem circle_set_sphere (q r : ℝ) (hr : 0 ≤ r) :
    circleSet q r=Metric.sphere (⟨q,r⟩ : ℂ) r := by
  ext z
  change circleResidual q r (z.re,z.im)=0 ↔ dist z (⟨q,r⟩ : ℂ)=r
  rw [← sq_eq_sq₀ dist_nonneg hr]
  have he : dist z (⟨q,r⟩ : ℂ)^2=circleResidual q r (z.re,z.im)+r^2 := by
    simp [Complex.dist_eq, Complex.sq_norm, Complex.normSq_apply, circleResidual]
    ring
  rw [he]
  constructor <;> intro h <;> linarith

theorem circle_image_closed (q r : ℝ) (hr : 0 ≤ r) :
    IsClosed ((OnePoint.some : ℂ → Ambient) '' circleSet q r) := by
  rw [circle_set_sphere q r hr]
  exact ((isCompact_sphere (⟨q,r⟩ : ℂ) r).image OnePoint.continuous_coe).isClosed

theorem circle_boundary_unique (q r : ℝ) (p : Ambient)
    (hp : p ∈ frontier upperImage) (hc : p ∈ (OnePoint.some : ℂ → Ambient) '' circleSet q r) :
    p=embed (OnePoint.some q) := by
  rcases hc with ⟨z,hz,rfl⟩
  rw [frontier_upper_image] at hp
  rcases hp with ⟨b,hb⟩
  have hi : z.im=0 := by
    cases b with
    | none => exact False.elim (OnePoint.infty_ne_coe z hb)
    | some b =>
      have he : (b : ℂ)=z := Option.some.inj hb
      simpa only [Complex.ofReal_im] using (congrArg Complex.im he).symm
  have hx : z.re=q := by
    change (z.re-q)^2+(z.im-r)^2-r^2=0 at hz
    rw [hi] at hz
    nlinarith [sq_nonneg (z.re-q)]
  change OnePoint.some z=OnePoint.some (q : ℂ)
  exact congrArg OnePoint.some (Complex.ext hx hi)

theorem horosphere_image_subset_circle (q t : ℝ) (ht : 0 < t) :
    horosphereImage q t ⊆ (OnePoint.some : ℂ → Ambient) '' circleSet q (1/(2*t)) := by
  rintro _ ⟨z,hz,rfl⟩
  refine ⟨(z : ℂ),?_,rfl⟩
  have h := (finite_horosphere_circle q t ht z).mp hz
  change (z.re-q)^2+(z.im-1/(2*t))^2-(1/(2*t))^2=0
  linarith

theorem horosphere_closure_boundary_subset (q t : ℝ) (ht : 0 < t) :
    closure (horosphereImage q t) ∩ frontier upperImage ⊆ {embed (OnePoint.some q)} := by
  rintro p ⟨hp,hb⟩
  have hc := closure_minimal (horosphere_image_subset_circle q t ht)
    (circle_image_closed q (1/(2*t)) (by positivity)) hp
  exact circle_boundary_unique q (1/(2*t)) p hb hc

def circleApproach (q r s : ℝ) : ℂ :=
  ⟨(circleParam q r (Real.pi*exp (-s))).1,(circleParam q r (Real.pi*exp (-s))).2⟩

theorem circle_approach_tendsto (q r : ℝ) :
    Tendsto (circleApproach q r) atTop (𝓝 (q : ℂ)) := by
  have ht : Tendsto (fun s => Real.pi*exp (-s)) atTop (𝓝 (0:ℝ)) := by
    simpa using Real.tendsto_exp_neg_atTop_nhds_zero.const_mul Real.pi
  have hp := (circle_param_contact_derivative q r).continuousAt.tendsto.comp ht
  have hm : Continuous (fun p : Plane => (p.1 : ℂ)+(p.2 : ℂ)*Complex.I) := by fun_prop
  have h := hm.tendsto (circleParam q r 0) |>.comp hp
  convert h using 1
  · funext s
    exact (Complex.re_add_im (circleApproach q r s)).symm
  · simp [circle_param_contact]

theorem circle_approach_positive (q r s : ℝ) (hr : 0 < r) (hs : 0 ≤ s) :
    0 < (circleApproach q r s).im := by
  have he : exp (-s) ≤ 1 := Real.exp_le_one_iff.mpr (neg_nonpos.mpr hs)
  have ht : 0 < Real.pi*exp (-s) := mul_pos Real.pi_pos (exp_pos _)
  have hle : Real.pi*exp (-s) ≤ Real.pi := by nlinarith [Real.pi_pos]
  have hc := Real.cos_lt_cos_of_nonneg_of_le_pi (x := 0) (by norm_num) hle ht
  simp only [Real.cos_zero] at hc
  exact mul_pos hr (sub_pos.mpr hc)

theorem horosphere_contact_mem_closure (q t : ℝ) (ht : 0 < t) :
    embed (OnePoint.some q) ∈ closure (horosphereImage q t) := by
  have hr : 0 < 1/(2*t) := by positivity
  have hlim := OnePoint.continuous_coe.tendsto (q : ℂ) |>.comp (circle_approach_tendsto q (1/(2*t)))
  apply mem_closure_of_tendsto hlim
  filter_upwards [eventually_ge_atTop (0:ℝ)] with s hs
  let z : ℍ := UpperHalfPlane.mk (circleApproach q (1/(2*t)) s)
    (circle_approach_positive q (1/(2*t)) s hr hs)
  refine ⟨z,?_,rfl⟩
  apply (finite_horosphere_circle q t ht z).mpr
  have he := circle_param_lies_on_circle q (1/(2*t)) (Real.pi*exp (-s))
  change (z.re-q)^2+(z.im-1/(2*t))^2-(1/(2*t))^2=0 at he
  linarith

theorem finite_horosphere_ideal_contact (q t : ℝ) (ht : 0 < t) :
    closure (horosphereImage q t) ∩ frontier upperImage={embed (OnePoint.some q)} := by
  apply Set.Subset.antisymm (horosphere_closure_boundary_subset q t ht)
  rintro p rfl
  refine ⟨horosphere_contact_mem_closure q t ht,?_⟩
  rw [frontier_upper_image]
  exact ⟨OnePoint.some q,rfl⟩

def infinityHorosphereImage (t : ℝ) : Set Ambient :=
  (fun z : ℍ => OnePoint.some (z : ℂ)) '' infinityHorosphere (-log t)
def horizontalClosed (t : ℝ) : Set Ambient :=
  (OnePoint.some : ℂ → Ambient) '' {z : ℂ | z.im=t} ∪ {OnePoint.infty}

theorem horizontal_closed_finite (t : ℝ) (z : ℂ) :
    OnePoint.some z ∈ horizontalClosed t ↔ z.im=t := by
  change ((∃ w : ℂ, w.im=t ∧ Option.some w=Option.some z) ∨ Option.some z=none) ↔ _
  simp only [Option.some.injEq, exists_eq_right, Option.some_ne_none, or_false]

theorem horizontal_closed (t : ℝ) : IsClosed (horizontalClosed t) := by
  apply (OnePoint.isClosed_iff_of_mem (by right; rfl : OnePoint.infty ∈ horizontalClosed t)).mpr
  have he : (OnePoint.some : ℂ → Ambient) ⁻¹' horizontalClosed t={z : ℂ | z.im=t} := by
    ext z; exact horizontal_closed_finite t z
  rw [he]
  exact isClosed_eq Complex.continuous_im continuous_const

theorem infinity_horosphere_closure_boundary_subset (t : ℝ) (ht : 0 < t) :
    closure (infinityHorosphereImage t) ∩ frontier upperImage ⊆ {OnePoint.infty} := by
  have hsub : infinityHorosphereImage t ⊆ horizontalClosed t := by
    rintro _ ⟨z,hz,rfl⟩
    exact Or.inl ⟨(z : ℂ),(infinity_horosphere_level t ht z).mp hz,rfl⟩
  rintro p ⟨hp,hb⟩
  have hc := closure_minimal hsub (horizontal_closed t) hp
  rw [frontier_upper_image] at hb
  rcases hb with ⟨b,rfl⟩
  cases b with
  | none => rfl
  | some q =>
    have he : (0:ℝ)=t := (horizontal_closed_finite t (q : ℂ)).mp hc
    exact False.elim ((ne_of_gt ht) he.symm)

theorem infinity_horosphere_contact_mem_closure (t : ℝ) (ht : 0 < t) :
    OnePoint.infty ∈ closure (infinityHorosphereImage t) := by
  have hn : Tendsto (fun s : ℝ => ‖(⟨s,t⟩ : ℂ)‖) atTop atTop := by
    apply tendsto_atTop_mono (fun s => Complex.re_le_norm (⟨s,t⟩ : ℂ)) tendsto_id
  have hc : Tendsto (fun s : ℝ => (⟨s,t⟩ : ℂ)) atTop (coclosedCompact ℂ) := by
    rw [coclosedCompact_eq_cocompact]
    exact (tendsto_norm_atTop_iff_cobounded.mp hn).mono_right Metric.cobounded_le_cocompact
  apply mem_closure_of_tendsto (OnePoint.tendsto_coe_infty.comp hc)
  exact Eventually.of_forall (fun s => ⟨UpperHalfPlane.mk (⟨s,t⟩ : ℂ) ht,
    (infinity_horosphere_level t ht _).mpr rfl,rfl⟩)

theorem infinity_horosphere_ideal_contact (t : ℝ) (ht : 0 < t) :
    closure (infinityHorosphereImage t) ∩ frontier upperImage={OnePoint.infty} := by
  apply Set.Subset.antisymm (infinity_horosphere_closure_boundary_subset t ht)
  rintro p rfl
  refine ⟨infinity_horosphere_contact_mem_closure t ht,?_⟩
  rw [frontier_upper_image]
  exact ⟨OnePoint.infty,rfl⟩

theorem inversion_transports_infinity_level (t : ℝ) (z : ℍ) :
    flip z ∈ finiteHorosphere 0 (-log t) ↔ z ∈ infinityHorosphere (-log t) := by
  change infinityBusemann (Chapter04Horocycles.gauge 0 (Chapter04Horocycles.flip z)) = -log t ↔
    infinityBusemann z = -log t
  simp only [Chapter04Horocycles.gauge, neg_zero, zero_vadd, flip_involutive]

theorem inversion_circle_tangent_kernel (t : ℝ) (ht : 0 < t) (v : Plane) :
    fderiv ℝ (circleResidual 0 (1/(2*t))) (0,0) v=0 ↔ v.2=0 :=
  boundary_tangent_kernel 0 (1/(2*t)) (by positivity) v

#print axioms AEGPaper0.Chapter04HorocycleBoundary.circle_set_sphere
#print axioms AEGPaper0.Chapter04HorocycleBoundary.circle_image_closed
#print axioms AEGPaper0.Chapter04HorocycleBoundary.circle_boundary_unique
#print axioms AEGPaper0.Chapter04HorocycleBoundary.horosphere_image_subset_circle
#print axioms AEGPaper0.Chapter04HorocycleBoundary.horosphere_closure_boundary_subset
#print axioms AEGPaper0.Chapter04HorocycleBoundary.circle_approach_tendsto
#print axioms AEGPaper0.Chapter04HorocycleBoundary.circle_approach_positive
#print axioms AEGPaper0.Chapter04HorocycleBoundary.horosphere_contact_mem_closure
#print axioms AEGPaper0.Chapter04HorocycleBoundary.finite_horosphere_ideal_contact
#print axioms AEGPaper0.Chapter04HorocycleBoundary.horizontal_closed_finite
#print axioms AEGPaper0.Chapter04HorocycleBoundary.horizontal_closed
#print axioms AEGPaper0.Chapter04HorocycleBoundary.infinity_horosphere_closure_boundary_subset
#print axioms AEGPaper0.Chapter04HorocycleBoundary.infinity_horosphere_contact_mem_closure
#print axioms AEGPaper0.Chapter04HorocycleBoundary.infinity_horosphere_ideal_contact
#print axioms AEGPaper0.Chapter04HorocycleBoundary.inversion_transports_infinity_level
#print axioms AEGPaper0.Chapter04HorocycleBoundary.inversion_circle_tangent_kernel
end AEGPaper0.Chapter04HorocycleBoundary
