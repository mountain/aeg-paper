# 02 – The arithmetic side of the elliptic AES

**Status:** design note and structural proposal, 2026-11-07. No paper claim and
no change to a mathematical-status register. The candidate definition is not
verified against the AES axioms. The "range domain" and the "compact/critical
AES" category are proposals.

**Status labels used below:** `STRUCTURAL PROPOSAL` (the range domain, the
compact/critical category, the candidate definition); `DIRECT COMPUTATION` (the
spherical formulas, not yet integrated as AEG results); `OPEN PROBLEM`.

## 1. The question

If the Cayley–Klein family is the geometric skeleton, what happens to the
arithmetic side and to the expression side? The short answer is:

- the syntax, the value operations, and the projective endpoint are unchanged;
- the **geometric realization** changes: the assignment is bounded, the affine
  motions are partial, and the eikonal equation degenerates at a critical locus;
- the expression side acquires a new domain condition, the **range domain**,
  which is independent of the usual division-by-zero condition.

## 2. Three layers

| layer | content | depends on $c$? |
|---|---|---|
| syntax / history | comb grammar, marked histories, one-hole contexts, evaluation $\nu:\text{histories}\to\mathrm{PGL}_2(K)$ | no |
| value operations | $z\mapsto z+1$, $z\mapsto\lambda z$, $z\mapsto -1/z$; ordinary domains (division by zero); projective endpoint | no |
| geometric realization | $(M,g_c,a_c)$, arithmetic motions, point paths, range | **yes** |

The $c$-family changes only the third layer (and the assignment function that
belongs to it). This is the same separation that Paper 0 makes between motions
that transport the assignment and a metric that measures cost: the motions need
not preserve the metric.

## 3. What stays the same

- **Syntax.** The comb grammar, the marked spinal histories, the one-hole
  contexts, and the projective evaluation are metric-independent. The same
  expression trees and histories are interpreted in every real form.
- **Value operations.** The four operations act on the value by Möbius
  transformations: addition $z\mapsto z+1$, multiplication $z\mapsto\lambda z$,
  subtraction and division as their inverses, and the reciprocal $z\mapsto -1/z$.
  The sign reflection $z\mapsto -z$ is the elementary signed-assignment instance.
  These are elements of $\mathrm{PGL}_2(\mathbb C)$ and do not depend on $c$.
- **Ordinary domains.** Division by zero remains undefined in ordinary
  evaluation. The ordinary/projective distinction of Paper I and Note 49 is
  unchanged.
- **Projective endpoint.** A history still has a projective operator and a
  projective endpoint. The endpoint forgets the path, as before.

## 4. The $c>0$ realization

Write $c=1/R^2$ and let $Y$ be the Cartesian coordinate on the sphere of radius
$R$. The assignment is

$$
a_c=\mu Y,
\qquad
\lvert a_c\rvert\le \frac{\mu}{\sqrt c}.
$$

The affine arithmetic motions are latitude maps:

$$
\mathsf X_s:\ Y\mapsto Y+\frac{s}{\mu},
\qquad
\mathsf Y_k:\ Y\mapsto kY.
$$

They satisfy

$$
a\circ\mathsf X_s=a+s,
\qquad
a\circ\mathsf Y_k=ka,
$$

but only where the new value stays in the range. They are assignment-compatible
and **not** isometries of the round metric. This is allowed by the AES
definition: the motions record arithmetic propagation; the metric measures the
infinitesimal cost. The point path is constructed as in Paper 0: choose $p_0$
with $a(p_0)=z_0$, apply the latitude motions, and obtain $p_0,\dots,p_n$ with
$a(p_i)=z_i$.

The local data are

$$
\lvert\nabla a_c\rvert^2=\mu^2-ca_c^2,
\qquad
\Delta_{g}a_c=-2c\,a_c,
\qquad
q=\sqrt{\mu^2-ca_c^2}.
$$

The zero set is the equator $Y=0$. The critical locus is the two poles
$Y=\pm R$, where $a_c=\pm\mu/\sqrt c$ and $q=0$.

## 5. A critical/turning locus, not a singular AES

The existing regular AES requires

$$
\lvert\nabla a\rvert^2=\mu^2+\lambda^2a^2\ \ge\ \mu^2>0,
$$

so $a$ is a submersion and no critical point is possible. A singular AES in the
sense of Paper I requires the complement of the singular set to be a regular AES.

The spherical model satisfies neither condition:

- at the poles both sides of $|\nabla a|^2=\mu^2-ca^2$ vanish, so the equation
  **degenerates** rather than failing;
- on the complement the equation has $\lambda^2=-c<0$, so the complement is not a
  regular AES in the sense of Paper 0.

Therefore the elliptic AES is not a regular AES and not a singular AES in the
existing sense. It is a candidate for a third category: a **compact/critical
AES** with a smooth metric and a smooth assignment, but a degenerate arithmetic
frame at the extrema. The poles are **turning points**, not holes, zeros, or
punctures: the arithmetic value reaches its bound and the frame cannot be
continued through it. The Paper I "locally essential" argument does not apply,
because at the pole the right-hand side of the equation is zero, so the
contradiction $0\ge\mu^2$ is not available.

## 6. The range domain

For a history with value path $z_0,z_1,\dots,z_n$, define

$$
\operatorname{Range}(h)
=
\left\{z_0:\ z_i(z_0)\in\left(-\frac{\mu}{\sqrt c},\frac{\mu}{\sqrt c}\right)
\text{ for all }i\right\}.
$$

The **realization domain** is

$$
\operatorname{Real}(h)
=
\operatorname{Ord}(h)\cap\operatorname{Range}(h),
$$

where $\operatorname{Ord}(h)$ is the ordinary domain (no division by zero).

Consequences:

- A history can have a projective endpoint but no spherical point path. This is
  a new kind of non-realizability, distinct from division by zero.
- A history that reaches $\pm\mu/\sqrt c$ hits a turning point: the forward
  operations that increase $|a|$ leave the range, while the inverse operations
  may stay inside.
- The reciprocal $z\mapsto -1/z$ remains a projective value operation. Its
  geometric realization would require $Y\mapsto -1/(\mu^2Y)$, which is not a
  latitude motion and is only defined where the image stays in the range. The
  affine/projective split of Paper 0 becomes essential here.
- The endpoint value still forgets the path; the point path retains the
  intermediate latitudes and the turning points.

The three domains should not be arranged as a chain. Ordinary and range are two
independent constraints on a history; their intersection is the realization
domain. The projective level is the global value-level, where the operations are
Möbius transformations of $\mathbb P^1(\mathbb C)$.

## 7. The frame and contact reinterpretation

The canonical arithmetic frame of Paper 0 is the orthonormal frame
$(X_u,X_v)$ with

$$
X_u a=\mu,
\qquad
X_v a=\lambda a.
$$

For $c>0$ one has $\lambda=i\sqrt c$, so there is no real vector field $X_v$
satisfying $X_v a=\lambda a$. The real orthonormal frame is

$$
(E_a,JE_a),
\qquad
E_a a=q,
\qquad
JE_a a=0.
$$

The interpretation changes:

- the additive direction is still the gradient direction, and it changes $a$;
- the former "multiplicative direction" becomes the azimuthal direction, which
  preserves $a$;
- the multiplication motion $\mathsf Y_k$ is a latitude scaling along the
  gradient direction, not the frame's second vector.

The frame slot and the operation are no longer the same object. So the naive
identification "$X_u$ = addition, $X_v$ = multiplication" fails for $c>0$. The
arithmetic frame, the contact bracket, and the sign of the curvature form must
be re-derived. This is the main technical open problem of the programme.

## 8. A candidate definition

A candidate elliptic AES is the tuple

$$
\mathfrak E_{\mathrm{ell}}
=
\left(\mathbb S^2_R,\ g_{\mathrm{round}},\ a=\mu Y;\ \mu,\ c=1/R^2\right),
$$

with the following data:

- the critical locus is the two poles;
- the equation $|\nabla a|^2=\mu^2-ca^2$ holds on the complement of the poles;
- the zero set is the equator;
- the arithmetic motions are latitude translations and scalings, partially
  defined;
- the point paths are latitude sequences on the sphere;
- the expression side uses the range domain;
- the analysis is spherical: $a$ is an $\ell=1$ spherical harmonic,
  $\Delta a=-2ca$, the zero set is the equator, and the critical locus is the
  two poles.

This is a structural proposal. It still needs:

1. verification against a stated AES axiom system;
2. a definition of the compact/critical category;
3. a proof that the range domain is the correct expression-side domain;
4. a frame/contact calculation for $c>0$;
5. a spherical analysis comparable to Paper II's hyperbolic analysis.

## 9. Design choices

**A. Real-form family.** Extend the regular AES equation to allow
$\lambda^2\in\mathbb R$ of either sign, i.e. allow imaginary $\lambda$, with
$c>0$ the compact member. This keeps one equation and one family, but requires a
third "critical" case in the regular/singular classification.

**B. New category "compact AES".** Define a compact AES directly: compact
surface, bounded assignment, degenerate eikonal at a critical locus, partial
motions. This avoids forcing the spherical model into the regular/singular
dichotomy, at the cost of a new axiom system.

**C. Conformal option.** Let $\mathrm{PGL}_2(\mathbb C)$ act on $\mathbb S^2$ by
conformal automorphisms, and treat $a$ as a conformal field. This is the most
faithful to the projective value operations, but the round metric is preserved
only up to a conformal factor, and the eikonal/isometric structure is lost. The
governance discussion already rejects bare $\mathrm{PGL}_2(\mathbb C)$ as a
real-form selector: a Hermitian form or an involution is additional data.

A hybrid of **A** and **B** seems most natural: state the real-form family,
then define the $c>0$ member as a compact/critical AES with its own regularity
and range data.

## 10. Open questions

1. What is the correct arithmetic frame for $c>0$? Is there a real frame with a
   meaningful additive/multiplicative pairing, or does the frame split into a
   gradient direction and an azimuthal phase?
2. What is the contact bracket and the curvature form for $c>0$? The hyperbolic
   bracket $[X_u,X_v]a=\mu\lambda$ has no direct real analogue.
3. Is the range domain the right expression-side notion, or should the spherical
   AES use a different valuation convention (for example, a bounded
   characteristic in the spirit of Paper 5's triadic framework)?
4. Can the reciprocal be realized geometrically, or is it intrinsically
   projective in every real form?
5. What is the spherical analogue of Paper II's hyperbolic function theory?
6. Does the compact/critical AES fit Paper 3's singular-AES framework, or does it
   require a separate category?
7. Does the elliptic AES change the process layer (arithmetic directions,
   contact, finite holonomy), or only the base geometry?

## 11. Sources

- Paper 0: `paper-0/sections/03-aes-and-motion.tex`, §3.2–§3.7.
- Paper I: `paper-1/sections/07-holes-and-zero-geometry.tex`, singular AES
  definition.
- Paper 3: `paper-3/sections/01-singular-aes.tex`, stratified singular AES;
  `paper-3/sections/02-local-zero-models.tex`, critical-point argument.
- Paper 5: `paper-5/sections/03-scalar-trichotomy.tex`.
- Note 49: `notes/analysis-and-calculus/49-conic-histories-and-finite-calculi.tex`,
  ordinary/projective domains.
- Discussion: `governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`,
  §4.6–§4.7, §6.1, §7.
