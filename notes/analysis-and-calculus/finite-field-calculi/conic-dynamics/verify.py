#!/usr/bin/env python3
"""Exact, dependency-free checks for conic-dynamics.tex (arithmetic mod 7).

The general-field statements are proved in the note. These finite checks use
independent matrix enumeration, point evaluation, and linear algebra. Function
spaces are checked on spanning bases, rather than on selected waveforms.
"""
from itertools import product
from math import comb

P = 7
X = tuple(range(P)) + (None,)  # None represents infinity.
IDENTITY = (1, 0, 0, 1)
ZERO, ONE = (0, 0), (1, 0)
checks = 0


def check(name, condition):
    global checks
    if not condition:
        raise AssertionError(name)
    checks += 1
    print(f"OK  {name}")


def canon(values):
    values = tuple(v % P for v in values)
    first = next((v for v in values if v), None)
    if first is None:
        raise ValueError("zero projective representative")
    scale = pow(first, -1, P)
    return tuple(v * scale % P for v in values)


def det(a):
    return (a[0] * a[3] - a[1] * a[2]) % P


def mm(a, b):
    return canon((a[0]*b[0] + a[1]*b[2], a[0]*b[1] + a[1]*b[3],
                  a[2]*b[0] + a[3]*b[2], a[2]*b[1] + a[3]*b[3]))


def mi(a):
    return canon((a[3], -a[1], -a[2], a[0]))


def mpow(a, n):
    out = IDENTITY
    for _ in range(n):
        out = mm(a, out)
    return out


def act(a, x):
    u, v = (1, 0) if x is None else (x, 1)
    y, z = (a[0]*u + a[1]*v) % P, (a[2]*u + a[3]*v) % P
    return None if z == 0 else y * pow(z, -1, P) % P


def orbit(a, start):
    result, x = [], start
    while x not in result:
        result.append(x)
        x = act(a, x)
    if x != start:
        raise AssertionError("invertible map must close its orbit at start")
    return tuple(result)


def fa(a, b):
    return ((a[0]+b[0]) % P, (a[1]+b[1]) % P)


def fs(a, b):
    return ((a[0]-b[0]) % P, (a[1]-b[1]) % P)


def fm(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % P,
            (a[0]*b[1]+a[1]*b[0]) % P)


def fpow(a, n):
    out = ONE
    for _ in range(n):
        out = fm(a, out)
    return out


def finv(a):
    s = pow((a[0]*a[0]+a[1]*a[1]) % P, -1, P)
    return (a[0]*s % P, -a[1]*s % P)


def fsum(values):
    out = ZERO
    for v in values:
        out = fa(out, v)
    return out


def rho(z):
    return fm(z, finv((z[0], -z[1] % P)))


def stereo(t):
    if t is None:
        return (6, 0)
    s = pow((1+t*t) % P, -1, P)
    return ((1-t*t)*s % P, 2*t*s % P)


def shift(f):
    return f[1:] + f[:1]


def diff(f):
    return [(a-b) % P for a, b in zip(shift(f), f)]


def rank(a):
    a = [[v % P for v in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        scale = pow(a[r][j], -1, P)
        a[r] = [v*scale % P for v in a[r]]
        for k in range(len(a)):
            if k != r:
                scale = a[k][j]
                a[k] = [(v-scale*w) % P for v, w in zip(a[k], a[r])]
        r += 1
    return r


def delta_matrix(n):
    return [[(int(j == (i+1) % n)-int(i == j)) % P
             for j in range(n)] for i in range(n)]


def matrix_product(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % P
             for col in zip(*b)] for row in a]


def basis(n):
    return [[int(i == j) for i in range(n)] for j in range(n)]


def primitive(g):
    if sum(g) % P:
        raise ValueError("nonzero cyclic sum")
    f = [0]
    for v in g[:-1]:
        f.append((f[-1]+v) % P)
    return f


def fourier(f, zeta):
    n = len(f)
    return [fsum(fm(v, fpow(zeta, (-j*k) % n))
                 for k, v in enumerate(f)) for j in range(n)]


def inverse_fourier(hat, zeta):
    n = len(hat)
    scale = (pow(n % P, -1, P), 0)
    return [fm(scale, fsum(fm(v, fpow(zeta, (j*k) % n))
                          for j, v in enumerate(hat))) for k in range(n)]


def main():
    group = sorted({canon(a) for a in product(range(P), repeat=4) if det(a)})
    check("independent enumeration gives |PGL2(F7)| = 336", len(group) == 336)
    permutations = {tuple(act(a, x) for x in X) for a in group}
    check("all 336 projective matrices act faithfully", len(permutations) == 336)

    r = (1, 3, 4, 1)
    s = (3, 0, 0, 1)
    u = (1, 1, 0, 1)
    torus = {mpow(r, k) for k in range(8)}
    a2, reciprocal, m2 = (1, 2, 0, 1), (0, 1, 1, 0), (2, 0, 0, 1)
    word = IDENTITY
    for step in (a2, reciprocal, m2, a2):
        word = mm(step, word)
    check("four arithmetic contexts evaluate to R3", word == r)
    check("R3 is an eight-cycle in the stated order",
          orbit(r, 0) == (0, 3, 1, 5, None, 2, 6, 4))
    check("split and unipotent orbit decompositions",
          orbit(s, 1) == (1, 3, 2, 6, 4, 5)
          and all(act(s, x) == x for x in (0, None))
          and orbit(u, 0) == tuple(range(7)) and act(u, None) is None)

    def ordinary_word(t):
        t = (t+2) % P
        if t == 0:
            return None
        return (2*pow(t, -1, P)+2) % P

    for n in range(9):
        domain = []
        for x in range(P):
            t = x
            for _ in range(n):
                t = ordinary_word(t)
                if t is None:
                    break
            if t is not None:
                domain.append(x)
                if t != act(mpow(r, n), x):
                    raise AssertionError("ordinary/projective agreement on domain")
        cycle = orbit(r, 0)
        predicted = [cycle[j] for j in range(8) if cycle[j] is not None
                     and all((j+k) % 8 != 3 for k in range(n))]
        check(f"ordinary domain of W^{n}: size {max(7-n, 0)}",
              set(domain) == set(predicted) and len(domain) == max(7-n, 0))
    check("W^8 is projectively the identity", mpow(word, 8) == IDENTITY)

    nonzero = [z for z in product(range(P), repeat=2) if z != ZERO]
    norm_one = {z for z in nonzero if (z[0]*z[0]+z[1]*z[1]) % P == 1}
    beta_group = {canon((a, b, -b, a)) for a, b in nonzero}
    check("quotient torus, norm-one image, and kernel orders",
          beta_group == torus and {rho(z) for z in nonzero} == norm_one
          and len(norm_one) == 8 and sum(rho(z) == ONE for z in nonzero) == 6)
    intertwines = all(stereo(act((a, b, -b, a), t)) == fm(rho((a, b)), stereo(t))
                      for a, b in nonzero for t in X)
    check("all 48 quotient representatives intertwine on all 8 points", intertwines)
    alpha = (2, 2)
    direct = canon((2, -2, 2, 2))
    check("factor of two: direct norm-one matrix has projective order 4",
          rho((1, 3)) == alpha and fpow(alpha, 4) == (6, 0)
          and mpow(direct, 4) == IDENTITY and mpow(direct, 2) != IDENTITY)

    # Check the general four-context factorization and homogeneous parameter law
    # on all parameters for the finite test field, including infinity.
    def param(t):
        return (0, 1, -1 % P, 0) if t is None else canon((1, t, -t, 1))

    factors_ok = True
    for t in range(1, P):
        inv_t = pow(t, -1, P)
        a = (1, -inv_t % P, 0, 1)
        m = (-(1+t*t)*inv_t*inv_t % P, 0, 0, 1)
        factors_ok &= mm(a, mm(m, mm(reciprocal, a))) == param(t)
    check("four-context factorization for all nonzero finite parameters", factors_ok)
    law_ok = True
    for t, v in product(X, repeat=2):
        t1, t0 = (1, 0) if t is None else (t, 1)
        v1, v0 = (1, 0) if v is None else (v, 1)
        w1, w0 = (t1*v0+t0*v1) % P, (t0*v0-t1*v1) % P
        w = None if w0 == 0 else w1*pow(w0, -1, P) % P
        law_ok &= mm(param(t), param(v)) == param(w)
    check("homogeneous parameter group law (64 pairs)", law_ok)

    # Independent direction enumeration; none are isotropic over F7.
    directions = {canon(v) for v in nonzero}
    squares = {v*v % P for v in range(1, P)}
    hits = {d: sum(canon(z) == d for z in norm_one) for d in directions}
    check("8 directions: 4 meet C twice, 4 have nonsquare norm, none isotropic",
          len(directions) == 8 and sorted(hits.values()) == [0]*4+[2]*4
          and all((a*a+b*b) % P != 0 for a, b in directions)
          and all((hits[(a, b)] == 2) == ((a*a+b*b) % P in squares)
                  for a, b in directions))

    for n in (6, 7, 8):
        d = delta_matrix(n)
        power = basis(n)  # identity matrix
        ranks = []
        for k in range(1, 8):
            power = matrix_product(power, d)
            ranks.append(rank(power))
        expected = [7-k for k in range(1, 8)] if n == 7 else [n-1]*7
        check(f"cycle {n}: ranks of Delta^1,...,Delta^7 = {ranks}", ranks == expected)
        solvable = True
        for e in basis(n)[:-1]:
            g = e[:]
            g[-1] = P-1  # e_j - e_last spans the zero-sum space.
            f = primitive(g)
            solvable &= diff(f) == g and sum(diff(e)) % P == 0
            if n != 7:
                c = -sum(f)*pow(n % P, -1, P) % P
                f = [(v+c) % P for v in f]
                solvable &= sum(f) % P == 0 and diff(f) == g
        check(f"cycle {n}: primitives on a basis of the whole zero-sum space", solvable)
        products_ok = True
        for f, g in product(basis(n), repeat=2):
            fg = [a*b % P for a, b in zip(f, g)]
            rhs = [(a*b+c*d) % P for a, b, c, d in zip(diff(f), g, shift(f), diff(g))]
            backward_g = g[-1:] + g[:-1]
            lhs_sum = sum(a*b for a, b in zip(diff(f), g)) % P
            rhs_sum = sum(a*(b-c) for a, b, c in zip(f, backward_g, g)) % P
            products_ok &= diff(fg) == rhs and lhs_sum == rhs_sum
        check(f"cycle {n}: twisted product and summation by parts on all basis pairs",
              products_ok)

    b = [[comb(k, j) % P for k in range(P)] for j in range(P)]
    check("binomial point functions form a Jordan basis",
          rank(b) == 7 and diff(b[0]) == [0]*7
          and all(diff(b[j]) == b[j-1] for j in range(1, 7)))
    check("seven-cycle normalization: constant RHS and impossible zero-sum primitive",
          diff(b[1]) == [1]*7 and sum(b[1]) % P == 0
          and diff(b[6]) == b[5] and sum(b[5]) % P == 0 and sum(b[6]) % P == 1
          and all(sum([(v+c) % P for v in b[6]]) % P == 1 for c in range(P)))

    for n, zeta in ((6, (3, 0)), (8, alpha)):
        transforms_ok, eigen_ok, primitives_ok, descent_ok = True, True, True, True
        for e in basis(n):
            f = [(v, 0) for v in e]
            hat = fourier(f, zeta)
            transforms_ok &= inverse_fourier(hat, zeta) == f
            if n == 8:
                descent_ok &= all(fpow(hat[j], 7) == hat[-j % n] for j in range(n))
        for j in range(n):
            chi = [fpow(zeta, j*k % n) for k in range(n)]
            dchi = [fs(a, b0) for a, b0 in zip(chi[1:]+chi[:1], chi)]
            eigen_ok &= dchi == [fm(fs(fpow(zeta, j), ONE), v) for v in chi]
        for e in basis(n)[:-1]:
            g = [(v, 0) for v in e]
            g[-1] = (6, 0)
            hat = fourier(g, zeta)
            fhat = [ZERO] + [fm(hat[j], finv(fs(fpow(zeta, j), ONE)))
                             for j in range(1, n)]
            f = inverse_fourier(fhat, zeta)
            primitives_ok &= fsum(f) == ZERO and all(v[1] == 0 for v in f)
            primitives_ok &= [fs(a, b0) for a, b0 in zip(f[1:]+f[:1], f)] == g
        check(f"cycle {n}: Fourier inversion on all point indicators", transforms_ok)
        check(f"cycle {n}: every character eigenvalue and zero-sum Fourier primitive",
              eigen_ok and primitives_ok)
        if n == 8:
            check("eight-cycle Frobenius pairing and F7 descent", descent_ok)

    centralizer, normalizer = [], []
    covariance = True
    for h in group:
        hi = mi(h)
        conjugate = mm(h, mm(r, hi))
        if conjugate == r:
            centralizer.append(h)
        if conjugate in torus:
            normalizer.append(h)
        for g in (r, s, u):
            hg = mm(h, mm(g, hi))
            for q in X:  # point indicator f = 1_q
                for x in X:
                    lhs = (int(act(h, act(g, act(hi, x))) == q)-int(x == q)) % P
                    rhs = (int(act(hg, x) == q)-int(x == q)) % P
                    covariance &= lhs == rhs
    reflection = (6, 0, 0, 1)
    check("covariance: 336 conjugators, 3 motions, all point basis vectors", covariance)
    check("centralizer order 8 and normalizer order 16",
          set(centralizer) == torus and len(normalizer) == 16
          and all(mm(h, mm(r, mi(h))) in (r, mi(r)) for h in normalizer))
    check("reflection inverts R; generator change R -> R^3 changes neighbors",
          mm(reflection, mm(r, mi(reflection))) == mi(r)
          and {act(r, 0), act(mi(r), 0)} != {act(mpow(r, 3), 0), act(mpow(r, 5), 0)})
    pair_orbit = {(act(h, 0), act(h, 1)) for h in group}
    check("full projective action is two-transitive (56 ordered distinct pairs)",
          pair_orbit == {(x, y) for x in X for y in X if x != y})
    print(f"\nALL {checks} CHECK GROUPS PASSED")


if __name__ == "__main__":
    main()
