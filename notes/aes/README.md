# AES notes: the elliptic AES programme

**Status:** design and research notes, created 2026-11-07. These are not paper
claims, not governance records, and not a change to any mathematical-status
register. They record a working discussion whose goal is a genuine elliptic AES
(positive curvature, compactification, analysis).

## Why a separate `aes/` folder

The notes under `analysis-and-calculus/` and `foundations-and-geometry/` develop
the existing AES theory, whose geometric core is the basic hyperbolic model of
Paper 0. This folder isolates the **elliptic AES programme**: the choice of the
Cayley–Klein real-form family as skeleton, the audit of the same-named
trichotomies, and the arithmetic/expression-side questions that this choice
opens.

## Contents

- [01 – Trichotomy audit and the Cayley–Klein skeleton](01-trichotomy-audit-and-cayley-klein-skeleton.md)
- [02 – The arithmetic side of the elliptic AES](02-arithmetic-side-of-the-elliptic-aes.md)

## One-paragraph summary

Five different trichotomies in the repository share the names elliptic /
parabolic / hyperbolic. Within the paper series, only the projective trace
trichotomy of Paper 0 is a complete classification-level geometric theory, but
it classifies isometries of the split real form $\mathrm{PSL}_2(\mathbb R)$; it
does not produce a positive-curvature AES. The constant-curvature trichotomy of
Paper 0, §12.6, has a developed hyperbolic entry, a parabolic degeneration, and
an elliptic entry explicitly marked "not developed". The skeleton proposed here
is the Cayley–Klein family

$$
g_c=\frac{4\,|dz|^2}{(1+c|z|^2)^2},
\qquad
a_c=\frac{2\mu\operatorname{Im}z}{1+c|z|^2},
\qquad
K_{g_c}=c,
$$

with $c<0$ the basic hyperbolic model, $c=0$ the flat model, and $c>0$ a
spherical model. For $c>0$ the assignment is bounded, the two poles form a
critical (turning) locus, the arithmetic motions are partial, and the expression
side acquires a new "range domain".

## Relation to the papers

- Paper 0, §3.6, Proposition 3.13 (`prop:p0-projective-trichotomy`): trace
  classification and length of a projective motion.
- Paper 0, §12.6: the three constant-curvature models; the elliptic entry is
  explicitly "not developed".
- Paper 3, §4: $\Gamma_4=\langle J,T\rangle$, the order-2 and order-4 elliptic
  points, cone angles, and the cusp; the only worked elliptic configuration in
  the paper series.
- Paper 5, §3–§4: the quadratic scalar and signature trichotomies. §8 still
  says that Paper 0 does not develop the trace trichotomy; that statement is
  stale relative to Paper 0.
- Note 49: the finite-field conic trichotomy; it explicitly disclaims a curvature
  reading.
- `governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`:
  the $c$-family formulas and the real-form proposals. Discussion-level, not a
  paper claim.

## Open questions

1. Define a **compact/critical AES** that admits the $c>0$ model without forcing
   it into the regular/singular dichotomy of Papers 0 and I.
2. Re-derive the arithmetic frame and the contact bracket for $c>0$; the
   canonical frame $X_u a=\mu$, $X_v a=\lambda a$ has no real solution when
   $\lambda^2=-c<0$.
3. Define the **range domain** and compare it with the ordinary and projective
   domains of Papers I and the finite-field notes.
4. Develop the spherical analysis: $a_c$ is an $\ell=1$ spherical harmonic, the
   zero set is the equator, and the critical locus is the two poles.
5. Decide whether the elliptic AES is a real form of the complexified AES or a
   separate category with its own axioms.

## Provenance

Written 2026-11-07 from a three-part working discussion. Paths and line numbers
refer to the repository state at commit `f1fe625` (2026-11-07). No paper source
was modified.
