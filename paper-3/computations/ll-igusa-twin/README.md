# Exact LL--Igusa twin verification

This directory verifies the explicit twin in
`sections/05-sextic-ll-laboratory.tex` without a computer-algebra dependency.
The script works over the exact quadratic field `Q(sqrt(5))`, evaluates the
Sylvester determinant at six rational values of the slice parameter, and uses
the fact that the normalized discriminant is a monic quintic in that parameter.

Run from the repository root:

```sh
PYTHONHASHSEED=0 python3 \
  paper-3/computations/ll-igusa-twin/verify-explicit-twin.py
```

The calculation proves

```text
6^-6 Disc_x(S_eps-t) = t^5 - 256/(3^18 5^5)
```

for the displayed sparse sextic.  The scaling relation in the manuscript then
places the explicit polynomial `P_1` in the same LL fiber as `x^6-x`.  At the
common slice `t=1`, both binary sextics have discriminant `49781`, while their
absolute quadratic-Clebsch ratios `A^5/Disc` differ.

The same exact coefficient calculation is repeated with the slice parameter
left symbolic.  It verifies

```text
A_0(t) = -2t
A_1(t) = -2(t-beta),  beta=(4/135)alpha^3
div(J_1/J_0) = 5[beta]-5[0]
```

and checks that both divisor points are away from the common discriminant.
Together with the theorem's two distinct sheet values, this also certifies the
strict positivity of the full degree-216 fiberwise forgetting variance, without
enumerating its other 214 orbit values.

This is an existential twin certificate.  It does not enumerate all 1296 LL
sheets or classify the 216 source-rotation orbits in genus-two moduli space.
