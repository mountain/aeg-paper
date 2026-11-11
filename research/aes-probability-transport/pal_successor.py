"""Research successor interface for the frozen PAL branch-centre model.

This is an explicit completion of the index-based gate, not an existing trained
rollout API. Rational coefficients retain one shared positive observation scale.
All probability values are mathematical softmax values with rational bounds.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Optional

import verify_boundary_gluing as boundary
import verify_memory_and_gates as gates

ZERO = (F(0),) * 8
IDENTITY = (F(1), F(0), ZERO)
INTERFACE_ID = "pal-fixed-scale-branch-centres-v1"


class NeedsRefinement(ValueError):
    """The current rational enclosure does not determine a gate sign."""


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def mul(x, y):
    p = [a*b for a in x for b in y]
    return min(p), max(p)


def scalar(c, x):
    return mul((c, c), x)


def reciprocal(x):
    if x[0] <= 0:
        raise ValueError("observation scale must have a positive lower bound")
    if x[0] == x[1]:
        return 1/x[0], 1/x[0]
    return gates.down(1/x[1]), gates.up(1/x[0])


def square(x):
    lo, hi = x
    return (F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi), max(lo*lo, hi*hi))


def interval_sum(xs):
    answer = (F(0), F(0))
    for x in xs:
        answer = add(answer, x)
    return answer


def exp_bounds(alpha):
    if alpha >= 0:
        return reciprocal(gates.exp_negative_bounds(alpha))
    return gates.exp_negative_bounds(-alpha)


def linear_apply(real, imag, x):
    out = []
    for a, b in zip(x[::2], x[1::2]):
        out.extend((real*a-imag*b, imag*a+real*b))
    return tuple(out)


def compose(after, before):
    ar, ai, ab = after
    br, bi, bb = before
    moved = linear_apply(ar, ai, bb)
    return ar*br-ai*bi, ai*br+ar*bi, tuple(x+y for x, y in zip(moved, ab))


def inverse(op):
    r, i, b = op
    norm = r*r+i*i
    if norm == 0:
        raise ValueError("singular relation cannot be inverted")
    r, i = r/norm, -i/norm
    return r, i, tuple(-x for x in linear_apply(r, i, b))


@dataclass(frozen=True)
class Seed:
    coordinates: tuple
    scale: tuple
    scale_name: str
    direction: Optional[tuple] = None

    def __post_init__(self):
        if len(self.coordinates) != 8 or self.scale[0] <= 0 or self.scale[1] < self.scale[0]:
            raise ValueError("invalid typed seed")
        if self.direction is not None and len(self.direction) != 8:
            raise ValueError("germ direction must have dimension eight")


@dataclass(frozen=True)
class State:
    seed: Seed
    affine: tuple = IDENTITY
    word: tuple = ()
    gate_rows: tuple = ()

    def coordinate_bounds(self):
        # x_t = M_t x_0 + B_t/c. The same c occurs at every step.
        r, i, b = self.affine
        u = linear_apply(r, i, self.seed.coordinates)
        inv_c = reciprocal(self.seed.scale)
        return tuple(add((x, x), scalar(y, inv_c)) for x, y in zip(u, b))

    def value_bounds(self):
        # a_t = c M_t x_0 + B_t; the formula, not just its box, is retained.
        r, i, b = self.affine
        u = linear_apply(r, i, self.seed.coordinates)
        return tuple(add(scalar(x, self.seed.scale), (y, y)) for x, y in zip(u, b))

    def direction(self):
        if self.seed.direction is None:
            return ZERO
        return linear_apply(self.affine[0], self.affine[1], self.seed.direction)

    def transported_face(self, normal, constant):
        """Exact value-space pullback h o F_word^{-1}."""
        r, i, b = inverse(self.affine)
        # Transpose of the inverse linear map applied to a covector.
        target_normal = linear_apply(r, -i, normal)
        target_constant = constant+sum(x*y for x, y in zip(normal, b))
        return target_normal, target_constant


def sign_of_germ(coefficients):
    """Sign for epsilon -> 0+, or zero for an identically-zero polynomial.

    A coefficient interval containing zero is not assumed to be zero.
    """
    for lo, hi in coefficients:
        if lo > 0:
            return 1
        if hi < 0:
            return -1
        if lo != 0 or hi != 0:
            raise NeedsRefinement("gate sign is unresolved by the scale enclosure")
    return 0


def gate_row(state, radius=F(4)):
    if radius <= 0:
        raise ValueError("gate radius must be positive")
    x, v = state.coordinate_bounds(), state.direction()
    def linear_sign(c, slope):
        return sign_of_germ((c, (slope, slope)))
    sx = linear_sign(x[0], v[0])
    sy = linear_sign(x[1], v[1])
    plus = linear_sign(add(x[0], x[1]), v[0]+v[1])
    minus = linear_sign(add(x[0], neg(x[1])), v[0]-v[1])
    # Half-open angle sectors matching atan2 in (-pi,pi], with the negative
    # real axis assigned to sector 7 and the zero pair assigned to sector 4.
    if sx == 0 and sy == 0:
        sector = 4
    elif sy < 0:
        if sx < 0:
            sector = 0 if minus < 0 else 1
        else:
            sector = 2 if plus < 0 else 3
    elif sy == 0:
        sector = 4 if sx > 0 else 7
    elif sx > 0:
        sector = 4 if minus > 0 else 5
    else:
        sector = 6 if plus > 0 else 7
    radial0 = interval_sum(square(t) for t in x)
    radial1 = interval_sum(scalar(2*s, t) for s, t in zip(v, x))
    radial2 = sum(t*t for t in v)
    depth = 0
    for d in (1, 2, 3):
        threshold = (d*radius/4)**2
        radial_sign = sign_of_germ((add(radial0, (-threshold, -threshold)),
                                    radial1, (radial2, radial2)))
        depth += int(radial_sign >= 0)
    return 4*sector+depth


class Successor:
    def __init__(self, relations, probabilities, radius=F(4)):
        if len(relations) != 32 or len(probabilities) != 32 or radius <= 0:
            raise ValueError("invalid frozen successor configuration")
        self.relations = tuple(relations)
        self.probabilities = tuple(tuple(row) for row in probabilities)
        self.radius = radius

    @classmethod
    def from_files(cls, relations_path, logits_path, radius=F(4)):
        relations = boundary.read_relations(relations_path)
        probabilities = [gates.softmax_bounds(row) for row in gates.read_pinned_logits(logits_path)]
        return cls(relations, probabilities, radius)

    def row(self, state):
        return gate_row(state, self.radius)

    def advance(self, state, channel, expected_row=None):
        if not 0 <= channel < 32:
            raise ValueError("channel outside frozen atlas")
        row = self.row(state)
        if expected_row is not None and expected_row != row:
            raise ValueError("stale gate cache does not match the successor state")
        return self._advance_at_row(state, channel, row)

    def _advance_at_row(self, state, channel, row):
        return State(state.seed, compose(self.relations[channel], state.affine),
                     state.word+(channel,), state.gate_rows+(row,))

    def children(self, state):
        row = self.row(state)
        return [(self._advance_at_row(state, j, row), self.probabilities[row][j])
                for j in range(32)]

    def rewind(self, state):
        """Controlled inverse of the last marked channel, not a stochastic inverse."""
        if not state.word:
            raise ValueError("empty history has no marked last step")
        j = state.word[-1]
        return State(state.seed, compose(inverse(self.relations[j]), state.affine),
                     state.word[:-1], state.gate_rows[:-1])

    def probability_bounds(self, state, first_row=None, frozen_row=None):
        ans = (F(1), F(1))
        for t, (row, channel) in enumerate(zip(state.gate_rows, state.word)):
            if frozen_row is not None:
                row = frozen_row
            elif t == 0 and first_row is not None:
                row = first_row
            ans = mul(ans, self.probabilities[row][channel])
        return ans
