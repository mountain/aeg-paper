# 01 – Trichotomy audit and the Cayley–Klein skeleton

**Status:** design note and audit, 2026-11-07. Structural proposal; no paper
claim and no change to a mathematical-status register. Standard facts about
$\mathrm{PSL}_2(\mathbb R)$, $\mathrm{PSU}(2)$, and $\mathrm{PSL}_2(\mathbb C)$
are used as standard and are not re-proved. The $c$-family formulas are imported
from a governance discussion and have not been integrated as AEG results.

**Status labels used below:** `audit conclusion` (repository survey, not a paper
claim); `IMPORTED DISCUSSION RESULT` (the $c$-family formulas); `STRUCTURAL
PROPOSAL` (the choice of skeleton and the compact/critical category); `OPEN
PROBLEM`.

## 1. The question

The goal is a genuine elliptic AES: positive curvature, a compact model, and an
analysis. Several constructions in the repository use the words elliptic,
parabolic, and hyperbolic for different objects. The question of this note is
which of them has a complete geometric theory that can serve as a skeleton, and
what happens to the other two cases of that skeleton when the target is the
elliptic AES.

The short answer is:

- Within the paper series, only the **projective trace trichotomy** of Paper 0
  (§3.6, Proposition 3.13, `prop:p0-projective-trichotomy`) is a complete
  classification-level geometric theory. It classifies isometries of
  $\mathbb H^2$ in the split real form $\mathrm{PSL}_2(\mathbb R)$.
- That trichotomy is **not** a positive-curvature AES theory. Its elliptic case
  is a rotation about a point of $\mathbb H^2$, i.e. a cone point in a negatively
  curved surface, not a spherical ambient geometry.
- The right skeleton for the elliptic AES is the **Cayley–Klein real-form
  family** $g_c$, $a_c$ with curvature $c$. The family is already written down in
  a governance discussion, but it is discussion-level mathematics, not a paper
  result.

## 2. Five same-named trichotomies

| scheme | location | criterion | geometric content | status | complete geometric theory? |
|---|---|---|---|---|---|
| **trace trichotomy** | Paper 0, §3.6, Prop. 3.13 | $\tau^2-4$ | classification of $\mathrm{PSL}_2(\mathbb R)$ motions: fixed points, invariant geodesics, translation length, rotation angle | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`; proof supplied | **yes, at classification level** |
| quadratic scalar trichotomy | Paper 5, §3 | $\kappa=-1,0,1$; sign of the norm | algebra of $\mathbb R[j]/(j^2-\kappa)$; geometry only through the inversion criterion and the central sign | algebra proved; the selection of $\kappa=-1$ is a Proposal | no (algebraic only) |
| signature trichotomy | Paper 5, §4 | $-\varepsilon_T\varepsilon_S\varepsilon_R$ | sign algebra of the six-state carrier | proved | no (sign algebra) |
| finite-field conic trichotomy | Note 49, §4 | square class of the discriminant (explicit $\mathbb F_7$ example) | finite projective motions; Fourier/Jordan calculi | proved with stated hypotheses; computationally verified | no (finite operator theory) |
| constant-curvature trichotomy | Paper 0, §12.6 | type of the absolute conic: real, degenerate, imaginary | hyperbolic model developed; parabolic degeneration; elliptic compactification | table is bookkeeping; only the hyperbolic entry is developed | no (hyperbolic entry only) |

There is also a flat/hyperbolic/spherical proposal in
`governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`. It is a
discussion, not a paper claim, and its first blocking problem is the
negative-curvature comparison.

The five schemes are not interchangeable. In particular:

- the trace trichotomy classifies **motions**;
- the quadratic and signature trichotomies classify **scalars or signs**;
- the finite-field trichotomy classifies **projective operators over a finite
  field**;
- the constant-curvature trichotomy classifies **ambient geometries**.

The word "elliptic" therefore has at least four distinct meanings in the current
repository: a conic/quadratic type, a Möbius motion type, a constant-curvature
sign, and an elliptic curve. The finite-field resource README already warns that
these must not be conflated.

## 3. What the audit shows

"Complete" is used here in a narrow sense: an exhaustive case split, with
geometric invariants and a worked realization, stated inside the paper series.

- The **trace trichotomy** satisfies the exhaustive split and the invariants. It
  has a worked realization of the elliptic case only in Paper 3's
  $\Gamma_4$-orbifold, and even there the elliptic points are cone points in a
  hyperbolic surface, not a spherical geometry.
- The **quadratic scalar trichotomy** is complete as algebra. Its geometric
  content is a selection criterion (the negative-inverse involution) and a
  central sign, not a configuration theory. Paper 5 itself says that the three
  names are field-dependent and that the three members are not separated by the
  algebraic requirements alone.
- The **signature trichotomy** is a sign computation.
- The **finite-field conic trichotomy** is a finite operator classification. It
  explicitly does not assert a curvature sign for a two-dimensional AES, and a
  precise elliptic AES definition is listed there as an open problem.
- The **constant-curvature trichotomy** is the closest in subject matter, but it
  is a bookkeeping table. The elliptic entry is the compactification
  $\mathbb P^1(\mathbb C)$ with one point per end, and the paper says it is "not
  developed". The middle entry is a degeneration $\lambda\to0$ of the basic
  model, not the Euclidean plane; the flat entry is a separate real form.

So no existing trichotomy is a complete positive-curvature AES theory. The trace
trichotomy is the only complete classification, and it is complete for the wrong
real form.

## 4. Trace versus curvature: two axes

| | trace trichotomy | AES constant curvature |
|---|---|---|
| object classified | $M\in\mathrm{PSL}_2(\mathbb R)$ | the metric $g$ |
| criterion | $\tau^2-4$ | $K=-\lambda^2$ |
| hyperbolic | two boundary fixed points, invariant geodesic, length $\ell>0$, dilation | $K<0$, basic model $\mathfrak E_0(\mu,\lambda)$ |
| parabolic | one boundary fixed point, length $0$, translation | $\lambda\to0$ degeneration (not flat) |
| elliptic | one interior fixed point, rotation, length $0$ | $K>0$, compactification $\mathbb P^1(\mathbb C)$ (not developed) |

The rows have the same names but not the same objects. A fixed hyperbolic AES
($K<0$) contains both trace-hyperbolic and trace-parabolic motions. In the basic
model, an affine motion $\varphi(z)=\Phi z+\xi$ with $\Phi>0$ has lift trace
$\Phi^{1/2}+\Phi^{-1/2}\ge 2$: it is hyperbolic for $\Phi\ne1$ and parabolic for
$\Phi=1$. There is no elliptic element in the affine/Borel sector. The elliptic
element $J(z)=-1/z$ sends $\infty$ to $0$, so it is outside the stabilizer of
$\infty$ and is not a symmetry of the regular basic model.

The precise relation between the two trichotomies is **holonomy**, not identity.
For a $(G,X)$-structure, the conjugacy type of the holonomy of a loop describes
the local model of the quotient:

- hyperbolic holonomy: collar around a closed geodesic;
- parabolic holonomy: cusp;
- elliptic holonomy: cone point.

Paper 3's $\Gamma_4=\langle J,T\rangle$ is the exact instance: the ambient
geometry is hyperbolic, but the orbifold has order-2 and order-4 elliptic points
and a parabolic cusp. The assignment $a_4$ is $\Gamma_4$-invariant, so $J$ is a
symmetry of that singular AES. This is the sense in which the trace
hyperbolic/parabolic cases are "internal" to a hyperbolic AES: they classify its
defects and ends, not its ambient curvature. The general quotient dictionary
(collar/cusp/cone) is stated in `research/frames-to-blocks/README.md`, which is
explicitly not a paper claim.

## 5. Why the trace trichotomy does not transfer to positive curvature

For $c>0$ the Cayley–Klein model has structure group

$$
G_c\simeq \mathrm{PSU}(2),
$$

which is compact. Every orientation-preserving isometry of the round sphere is a
rotation, hence elliptic in the $\mathrm{PSL}_2(\mathbb C)$ classification. There
are no hyperbolic or parabolic isometries. The trace trichotomy collapses to a
single elliptic type.

Two further differences matter:

- On $\mathbb S^2$ a nontrivial rotation has **two antipodal fixed points** (an
  axis), not one interior fixed point. The hyperbolic-plane elliptic picture does
  not transfer verbatim.
- The complexified group $\mathrm{PSL}_2(\mathbb C)$ has the four standard types
  (elliptic, parabolic, hyperbolic, loxodromic). The real form selects which
  types occur: $\mathrm{PSL}_2(\mathbb R)$ sees elliptic/parabolic/hyperbolic and
  no loxodromic; $\mathrm{PSU}(2)$ sees only elliptic. The trace trichotomy is a
  feature of the **split real form**, not a universal skeleton.

This is the precise sense in which the trace-elliptic case and the elliptic AES
are different: the first is a cone point in $\mathbb H^2$ ($K<0$); the second is
a spherical ambient geometry ($K>0$).

A naive analytic continuation does not repair this. Substituting
$\lambda\mapsto i\kappa$ in the affine flow gives
$z\mapsto e^{i\kappa s}z+b$, a Euclidean rotation–translation, not the sphere.
The governance discussion records this as a rejected formulation: the compact
real form requires additional data (a Hermitian form or an involution), not just
an imaginary parameter.

## 6. The Cayley–Klein family

The candidate family in the governance discussion is

$$
G_c\simeq
\begin{cases}
\mathrm{PSU}(2), & c>0,\\
\mathrm{SE}(2), & c=0,\\
\mathrm{PSU}(1,1)\simeq\mathrm{PSL}_2(\mathbb R), & c<0,
\end{cases}
\qquad
X_c\simeq G_c/L_c,
\qquad
L_c\simeq \mathrm{SO}(2),
$$

with metric and assignment

$$
g_c=\frac{4\,|dz|^2}{(1+c|z|^2)^2},
\qquad
a_c=\frac{2\mu\operatorname{Im}z}{1+c|z|^2}.
$$

A direct coordinate calculation gives

$$
K_{g_c}=c,
\qquad
\lvert\nabla a_c\rvert_{g_c}^2=\mu^2-ca_c^2,
\qquad
\Delta_{g_c}a_c=-2c\,a_c.
$$

The three branches are:

- $c<0$: write $c=-\lambda^2$. The metric and assignment recover the basic
  upper-half-plane model at the metric/assignment level. The process layer is not
  automatic; the discussion says the identities have not been written into a
  repository proof and do not recover the arithmetic directions by themselves.
- $c=0$: the flat model, with structure group $\mathrm{SE}(2)$.
- $c>0$: a spherical chart with a bounded assignment and a periodic frame
  behaviour.

This is a **real-form family**, not a path inside the real regular AES family.
For $c>0$ one has $\lambda^2=-c<0$, so there is no real $\lambda$ satisfying the
regular AES equation $|\nabla a|^2=\mu^2+\lambda^2a^2$. The discussion states
that the calculations have not been integrated as AEG results and that the
canonical regular-AES definition remains open. Proposal S-1 targets Paper IV;
S-3 targets Paper IV for the geometry and Paper II for the analysis.

## 7. The spherical model

For $c>0$ put $R=1/\sqrt c$ and use the Cartesian coordinate $Y$ on the sphere of
radius $R$. Then

$$
a_c=\mu Y,
\qquad
\lvert a_c\rvert\le \frac{\mu}{\sqrt c},
\qquad
\lvert\nabla a_c\rvert^2=\mu^2(1-cY^2)=\mu^2-ca_c^2.
$$

- The zero set is the equator $Y=0$.
- The critical locus is the two poles $Y=\pm R$, where $a_c=\pm\mu/\sqrt c$ and
  $|\nabla a_c|=0$.
- $a_c$ is an $\ell=1$ spherical harmonic; $\Delta a_c=-2c\,a_c$.
- The gradient part of the flow has turning points at the poles; the azimuthal
  part is periodic.

At the poles the eikonal equation **degenerates**: both sides vanish. It does not
fail. This is not a singular AES in the sense of Paper I, because the complement
is not a regular AES (its equation has $\lambda^2<0$), and it is not a regular
AES because the right-hand side is not bounded below by $\mu^2$. It is a new
candidate category: a **compact/critical AES** with a smooth metric and a smooth
assignment, but a degenerate arithmetic frame at the extrema.

## 8. Decision and open problems

**Decision.** Use the Cayley–Klein family as the geometric skeleton of the
elliptic AES programme. Keep the trace trichotomy as a negative control: it
states exactly which structures fail to transfer to positive curvature (no
boundary, no cusp, no length spectrum, rotation axis instead of a single fixed
point).

**Open problems.**

1. Define a compact/critical AES that admits the $c>0$ model and states its
   regularity, critical locus, and range.
2. Re-derive the arithmetic frame and the contact bracket for $c>0$. The real
   frame is $(E_a,JE_a)$ with $E_a a=q$ and $JE_a a=0$; there is no real $X_v$
   with $X_v a=\lambda a$.
3. Determine whether the elliptic AES is a real form of a complexified AES or a
   separate category with its own axioms.
4. Develop the spherical analysis: spherical harmonics, the equator as zero set,
   the poles as turning points.
5. Compare the $c>0$ model with Paper 3's singular AES and Paper 1's
   ordinary/projective domains.

## 9. Consistency notes

- Paper 5, §8 (`paper-5/sections/08-through-crossings.tex:68–70`) still says
  that Paper 0 does not develop the trace trichotomy. This is stale: Paper 0,
  §3.6, Proposition 3.13 was added on 2026-10-24.
- OQ-047 (`governance/08-open-questions.md:1857`) repeats the same stale
  statement.
- `paper-0/formal/inventory.json` does not contain
  `prop:p0-projective-trichotomy`; `research/formal-inventory-drift/README.md`
  records the drift.
- Paper 0, §12.6 uses "parabolic" for the $\lambda\to0$ degeneration and
  explicitly says this is not the flat model. The flat entry is a separate real
  form. The $c=0$ branch of the Cayley–Klein family is the flat model. These are
  three different "parabolic" objects: a motion type, a degeneration, and a flat
  geometry.

## 10. Sources

- Paper 0: `paper-0/sections/03-aes-and-motion.tex`, §3.6;
  `paper-0/sections/12-compactification.tex`, §12.6.
- Paper 3: `paper-3/sections/04-arithmetic-zero-networks.tex`, §4.
- Paper 5: `paper-5/sections/03-scalar-trichotomy.tex`,
  `paper-5/sections/04-six-state-carrier.tex`,
  `paper-5/sections/08-through-crossings.tex`.
- Note 49: `notes/analysis-and-calculus/49-conic-histories-and-finite-calculi.tex`.
- Discussion: `governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`,
  §4.6–§4.7, §6.1, §7.
- Quotient dictionary: `research/frames-to-blocks/README.md`, §9.
- Status: `governance/05b-paper-0-status-register.md:72`.
