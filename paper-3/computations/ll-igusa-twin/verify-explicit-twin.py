#!/usr/bin/env python3
"""Dependency-free exact verification of the explicit LL--Igusa twin."""

from fractions import Fraction as F


class K:
    """An exact element a+b*s of Q(sqrt(5)), with s^2=5."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, K) else K(value)

    def __add__(self, other):
        other = K.coerce(other)
        return K(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-K.coerce(other))

    def __rsub__(self, other):
        return K.coerce(other) - self

    def __mul__(self, other):
        other = K.coerce(other)
        return K(
            self.a * other.a + 5 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def inverse(self):
        denominator = self.a * self.a - 5 * self.b * self.b
        if denominator == 0:
            raise ZeroDivisionError
        return K(self.a / denominator, -self.b / denominator)

    def __truediv__(self, other):
        return self * K.coerce(other).inverse()

    def __rtruediv__(self, other):
        return K.coerce(other) / self

    def __eq__(self, other):
        other = K.coerce(other)
        return self.a == other.a and self.b == other.b

    def __bool__(self):
        return bool(self.a or self.b)


def determinant(matrix):
    """Gaussian determinant over the exact field K."""

    matrix = [[K.coerce(value) for value in row] for row in matrix]
    size = len(matrix)
    result = K(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if matrix[row][column]), None
        )
        if pivot is None:
            return K(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        pivot_value = matrix[column][column]
        result *= pivot_value
        inverse = pivot_value.inverse()
        for row in range(column + 1, size):
            if not matrix[row][column]:
                continue
            quotient = matrix[row][column] * inverse
            for entry in range(column, size):
                matrix[row][entry] -= quotient * matrix[column][entry]
    return result


def resultant(first, second):
    """Sylvester resultant for descending coefficient lists."""

    degree_first = len(first) - 1
    degree_second = len(second) - 1
    size = degree_first + degree_second
    matrix = [[K(0) for _ in range(size)] for _ in range(size)]
    for row in range(degree_second):
        for column, value in enumerate(first):
            matrix[row][row + column] = value
    for row in range(degree_first):
        for column, value in enumerate(second):
            matrix[degree_second + row][row + column] = value
    return determinant(matrix)


def discriminant_of_sparse_sextic(t_value, sign=1):
    """Disc_x(S_sign(x)-t_value) in Q(sqrt(5))."""

    # 8/(225 sqrt(5)) = 8 sqrt(5)/1125.
    linear = K(0, F(sign * 8, 1125))
    polynomial = [
        K(1),
        K(0),
        K(1),
        K(0),
        K(F(4, 15)),
        linear,
        K(F(8, 675) - F(t_value)),
    ]
    derivative = [K(6), K(0), K(4), K(0), K(F(8, 15)), linear]
    # For degree six, Disc(f)=(-1)^15 Res(f,f')=-Res(f,f').
    return -resultant(polynomial, derivative)


constant = F(256, (3**18) * (5**5))
for sign in (1, -1):
    for t_value in range(6):
        computed = discriminant_of_sparse_sextic(t_value, sign) / (6**6)
        expected = K(F(t_value) ** 5 - constant)
        assert computed == expected
    print(f"sign={sign}: six exact resultant evaluations passed")

# Both sides are monic quintics in t.  Six exact evaluations prove identity.
print("6^-6 Disc_x(S_sign-t) = t^5 -", constant)

# If alpha^15=R, scaling gives the target event polynomial Q_0.
R = -F((3**12) * (5**10), 2**14)
assert -constant * R == F(5**5, 6**6)
print("alpha^15 =", R)
print("scaled constant =", -constant * R)


def symbolic_add(first, second):
    """Add sparse elements of Q[alpha,delta,t]."""

    result = dict(first)
    for monomial, coefficient in second.items():
        result[monomial] = result.get(monomial, F(0)) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def symbolic_scale(coefficient, polynomial):
    return {
        monomial: F(coefficient) * value
        for monomial, value in polynomial.items()
        if F(coefficient) * value
    }


def symbolic_multiply(first, second):
    result = {}
    for monomial_first, coefficient_first in first.items():
        for monomial_second, coefficient_second in second.items():
            monomial = tuple(
                first_exponent + second_exponent
                for first_exponent, second_exponent in zip(
                    monomial_first, monomial_second
                )
            )
            term = coefficient_first * coefficient_second
            result = symbolic_add(result, {monomial: term})
    return result


def quadratic_clebsch(coefficients):
    """Compute sum (-1)^k c_k c_(6-k)/binom(6,k)."""

    result = {}
    binomials = (1, 6, 15, 20, 15, 6, 1)
    for index in range(7):
        product = symbolic_multiply(
            coefficients[index], coefficients[6 - index]
        )
        result = symbolic_add(
            result,
            symbolic_scale(F((-1) ** index, binomials[index]), product),
        )
    return result


zero = {}
one = {(0, 0, 0): F(1)}
alpha = {(1, 0, 0): F(1)}
delta = {(0, 1, 0): F(1)}
parameter_t = {(0, 0, 1): F(1)}

# Coefficients c_k of F(X,Z)=sum c_k X^(6-k) Z^k.
coefficients_p0 = [
    one,
    zero,
    zero,
    zero,
    zero,
    {(0, 0, 0): F(-1)},
    {(0, 0, 0): F(-1)},
]
coefficients_p1 = [
    one,
    zero,
    alpha,
    zero,
    {(2, 0, 0): F(4, 15)},
    delta,
    {(3, 0, 0): F(8, 675), (0, 0, 0): F(-1)},
]
expected_a0 = {(0, 0, 0): F(-2)}
expected_a1 = {(0, 0, 0): F(-2), (3, 0, 0): F(8, 135)}
assert quadratic_clebsch(coefficients_p0) == expected_a0
assert quadratic_clebsch(coefficients_p1) == expected_a1

# Repeat the calculation with the slice parameter left symbolic.
coefficients_p0_t = [
    one,
    zero,
    zero,
    zero,
    zero,
    {(0, 0, 0): F(-1)},
    symbolic_scale(-1, parameter_t),
]
coefficients_p1_t = [
    one,
    zero,
    alpha,
    zero,
    {(2, 0, 0): F(4, 15)},
    delta,
    symbolic_add(
        {(3, 0, 0): F(8, 675)},
        symbolic_scale(-1, parameter_t),
    ),
]
expected_a0_t = {(0, 0, 1): F(-2)}
expected_a1_t = {(0, 0, 1): F(-2), (3, 0, 0): F(8, 135)}
assert quadratic_clebsch(coefficients_p0_t) == expected_a0_t
assert quadratic_clebsch(coefficients_p1_t) == expected_a1_t

# The displayed relation for delta is compatible with the normalized linear
# coefficient d_0=8/(225 sqrt(5)): d_0^2 alpha^5=64 alpha^5/253125.
assert F(8**2, (225**2) * 5) == F(64, 253125)

# beta=(4/135)alpha^3 is a regular (non-discriminant) slice value.
beta_fifth = F(4, 135) ** 5 * R
assert beta_fifth == -F(5**5, (2**4) * (3**3))
assert beta_fifth != -F(5**5, 6**6)

# Both discriminants at t=1 are 6^6 Q_0(1)=49781, so A^5/Disc differs.
common_discriminant = 6**6 + 5**5
assert common_discriminant == 49781
print("A_0 = -2")
print("A_1 = -2+(8/135)alpha^3 < -2 for alpha < 0")
print("A_1(t)/A_0(t) = (t-(4/135)alpha^3)/t")
print("div(J_1/J_0) = 5[beta]-5[0]")
print("common discriminant at t=1 =", common_discriminant)
print("therefore A_1^5/Disc != A_0^5/Disc")
