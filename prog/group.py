from prog.monoidal import Monoidal


def amb(x, y, z, a, m, b):
    return (x - a) * (y / m) + b


class Numerator(Monoidal):
    @classmethod
    def identity_value(cls):
        return 0

    @classmethod
    def combine_values(cls, left, right):
        return left + right


class Denominator(Monoidal):
    @classmethod
    def identity_value(cls):
        return 1

    @classmethod
    def combine_values(cls, left, right):
        return left * right


class Fraction(Monoidal):
    @classmethod
    def identity_value(cls):
        return 1

    @classmethod
    def combine_values(cls, left, right):
        return left * right


class Helper(Fraction):
    pass


assert amb(1, 2, 7, 5, 3) == (1 - 7) * (2 / 5) + 3
assert Numerator.identity().combine(Numerator(2)).value == 2
assert Denominator.identity().combine(Denominator(3)).value == 3
assert Fraction.identity().combine(Fraction(4)).value == 4
