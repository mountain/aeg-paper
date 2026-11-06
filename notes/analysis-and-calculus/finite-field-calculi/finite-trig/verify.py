#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finite trigonometry over F_7: verification script.

The conic C: x^2 + y^2 = 1 over F_7 is the norm-one group of
F_49 = F_7[i]/(i^2+1).  alpha = 2+2i has order 8; write
    alpha^k = cos k + i sin k,   k in Z/8.
The script prints the table and checks the claims used in the note:
basic identities, the conic, the norm fibres, the polarity counts, arcs,
the translation experiment, the ripple conics, the similarity groups
O(Q), F_7^ x O(Q), GO(Q) and their orbits, the line-direction angle
relation, Thales, and the finite-field Fourier layer.

Exit code is 0 only if every check passes.
"""
import sys
from collections import Counter

P = 7


def add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def sub(a, b):
    return ((a[0] - b[0]) % P, (a[1] - b[1]) % P)


def mul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % P,
            (a[0] * b[1] + a[1] * b[0]) % P)


def inv(a):
    n = (a[0] * a[0] + a[1] * a[1]) % P
    ni = pow(n, -1, P)
    return ((a[0] * ni) % P, (-a[1] * ni) % P)


def div(a, b):
    return mul(a, inv(b))


def conj(a):
    return (a[0], (-a[1]) % P)


def power(a, k):
    out = (1, 0)
    for _ in range(k):
        out = mul(out, a)
    return out


def dot(a, b):
    return (a[0] * b[0] + a[1] * b[1]) % P


alpha = (2, 2)
T = [power(alpha, k) for k in range(8)]
cos = [z[0] for z in T]
sin = [z[1] for z in T]


def centered(x):
    return x if x <= 3 else x - 7


def leg(a):
    a %= P
    if a == 0:
        return 0
    return 1 if pow(a, (P - 1) // 2, P) == 1 else -1


print("k | alpha^k | cos | sin | centered cos | centered sin")
for k in range(8):
    print(f"{k} | {T[k][0]}+{T[k][1]}i | {cos[k]} | {sin[k]} | "
          f"{centered(cos[k]):>2} | {centered(sin[k]):>2}")

print("\nchecks")
ok = True
failures = []


def check(name, cond):
    global ok
    print(("  OK  " if cond else "  FAIL") + "  " + name)
    if not cond:
        failures.append(name)
        ok = False


check("alpha^4 = -1", T[4] == (6, 0))
check("alpha^8 = 1 (computed)", power(alpha, 8) == (1, 0))
check("all points on the conic", all((x * x + y * y) % P == 1 for x, y in T))
check("period 8 (computed)", all(power(alpha, k + 8) == power(alpha, k)
                                 for k in range(8)))
conic = {(x, y) for x in range(P) for y in range(P) if (x * x + y * y) % P == 1}
check("the eight points are exactly the conic (independent enumeration)",
      set(T) == conic and len(conic) == 8)
check("cos^2 + sin^2 = 1",
      all((cos[k] ** 2 + sin[k] ** 2) % P == 1 for k in range(8)))
check("cos even", all(cos[(8 - k) % 8] == cos[k] for k in range(8)))
check("sin odd", all(sin[(8 - k) % 8] == (-sin[k]) % P for k in range(8)))

add_ok = True
for k in range(8):
    for l in range(8):
        c = (cos[k] * cos[l] - sin[k] * sin[l]) % P
        s = (sin[k] * cos[l] + cos[k] * sin[l]) % P
        add_ok = add_ok and (c, s) == T[(k + l) % 8]
check("addition formulas (64 cases)", add_ok)

dbl_ok = True
for k in range(8):
    c = (cos[k] ** 2 - sin[k] ** 2) % P
    s = (2 * sin[k] * cos[k]) % P
    dbl_ok = dbl_ok and (c, s) == T[(2 * k) % 8]
check("doubling formulas (8 cases)", dbl_ok)

print("\nstereographic t = sin k / (1 + cos k)")
stereo_ok = True
for k in range(8):
    if k == 4:
        print(f"  k={k}: t = infinity  (point ({cos[k]},{sin[k]}) = (-1,0))")
        continue
    t = (sin[k] * pow((1 + cos[k]) % P, -1, P)) % P
    c = ((1 - t * t) * pow((1 + t * t) % P, -1, P)) % P
    s = ((2 * t) * pow((1 + t * t) % P, -1, P)) % P
    print(f"  k={k}: t={t}  -> (cos,sin)=({c},{s})")
    stereo_ok = stereo_ok and (c, s) == T[k]
check("stereographic inverse (7 finite k)", stereo_ok)

print("\nfirst differences (centred)")
diff_ok = True
for name, f in (("cos", cos), ("sin", sin)):
    d = [(f[(k + 1) % 8] - f[k]) % P for k in range(8)]
    dc = [centered(x) for x in d]
    print(f"  Delta {name} = {dc}   sum = {sum(d) % P}")
    diff_ok = diff_ok and sum(d) % P == 0
    diff_ok = diff_ok and all((f[(k + 1) % 8] - f[k]) % P == d[k] for k in range(8))
check("Delta f has sum zero and matches the table", diff_ok)

fib = Counter((x * x + y * y) % P for x in range(P) for y in range(P))
print("\nnorm fibre sizes:", dict(sorted(fib.items())))
check("norm fibres: 1 point at a=0 and 8 points for a=1..6",
      fib[0] == 1 and all(fib[a] == 8 for a in range(1, P)))


def canon(v):
    v = tuple(x % P for x in v)
    for x in v:
        if x:
            inv_x = pow(x, -1, P)
            return tuple((y * inv_x) % P for y in v)
    return None


conic_pts = {canon((X, Y, Z)) for X in range(P) for Y in range(P) for Z in range(P)
             if (X, Y, Z) != (0, 0, 0) and (X * X + Y * Y - Z * Z) % P == 0}
plane_pts = {canon((X, Y, Z)) for X in range(P) for Y in range(P) for Z in range(P)
             if (X, Y, Z) != (0, 0, 0)}
polar = Counter(sum(1 for Q in conic_pts
                    if (x * Q[0] + y * Q[1] - z * Q[2]) % P == 0)
                for x, y, z in plane_pts)
check("polar intersections: 8 on C, 21 internal, 28 external",
      polar == {2: 28, 0: 21, 1: 8})


def arc_components(S):
    N = 8
    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for a in range(N):
        for s in S:
            union(a, (a + s) % N)
    return len({find(a) for a in range(N)})


check("arc components: {1}->1, {2}->2, {4}->4, {3}->1",
      [arc_components(s) for s in [{1}, {2}, {4}, {3}]] == [1, 2, 4, 1])

translated = [((x) % P, (y + 1) % P) for x, y in T]
check("translated points satisfy x^2+(y-1)^2=1",
      all((x * x + (y - 1) * (y - 1)) % P == 1 for x, y in translated))
check("original and translated conics are disjoint",
      not (set(T) & set(translated)))
check("old centre (0,0) lies on the translated conic",
      ((0 - 0) ** 2 + (0 - 1) ** 2) % P == 1)
check("new centre (0,1) lies on the original conic",
      (0 * 0 + 1 * 1) % P == 1)


def ripple(t):
    return {(x, y) for x in range(P) for y in range(P)
            if (t * (x * x + y * y) - y) % P == 0}


check("ripple conics: 8 points through 0",
      all(len(ripple(t)) == 8 and (0, 0) in ripple(t) for t in range(1, P)))
ripple_union = set().union(*(ripple(t) for t in range(1, P))) - {(0, 0)}
check("ripple conics partition the points with y != 0",
      ripple_union == {(x, y) for x in range(P) for y in range(P) if y != 0})
check("ripple common tangent y=0 meets C_t only at 0",
      all({(x, 0) for x in range(P) if (t * x * x) % P == 0} == {(0, 0)}
          for t in range(1, P)))

# D_2(C_t) = C_{t/2} and D_lambda(S_r) = S_{lambda^2 r}
scale_ok = True
for lam in range(1, P):
    for t in range(1, P):
        image = {((lam * x) % P, (lam * y) % P) for x, y in ripple(t)}
        scale_ok = scale_ok and image == ripple((t * pow(lam, -1, P)) % P)
    for r in range(1, P):
        image = {((lam * x) % P, (lam * y) % P) for x, y in
                 [(x, y) for x in range(P) for y in range(P)
                  if (x * x + y * y) % P == r]}
        target = {(x, y) for x in range(P) for y in range(P)
                  if (x * x + y * y) % P == (lam * lam * r) % P}
        scale_ok = scale_ok and image == target
check("scaling: D_lambda(C_t)=C_{t/lambda}, D_lambda(S_r)=S_{lambda^2 r}",
      scale_ok)

# Inversion: J(H_t) = C_t minus the pole 0.  J(z) = -1/z.
def J(z):
    return mul((P - 1, 0), inv(z))


inv_ok = True
for t in range(1, P):
    H = [(x, t) for x in range(P)]
    image = {J(z) for z in H}
    inv_ok = inv_ok and image == ripple(t) - {(0, 0)} and (0, 0) not in image
check("inversion: J(H_t) = C_t minus the pole 0 (all t)", inv_ok)


# Similarity groups of Q: O(Q), F_7^ x O(Q), GO(Q).
def mat_vec(A, v):
    return ((A[0][0] * v[0] + A[0][1] * v[1]) % P,
            (A[1][0] * v[0] + A[1][1] * v[1]) % P)


def qform(A, v):
    w = mat_vec(A, v)
    return (w[0] * w[0] + w[1] * w[1]) % P


def mu_of(A):
    a, b = A[0]
    c, d = A[1]
    mu = (a * a + c * c) % P
    if (b * b + d * d) % P != mu:
        return None
    if (a * b + c * d) % P != 0:
        return None
    return mu


mats = []
for a in range(P):
    for b in range(P):
        for c in range(P):
            for d in range(P):
                if (a * d - b * c) % P == 0:
                    continue
                A = ((a, b), (c, d))
                mu = mu_of(A)
                if mu is not None:
                    mats.append((A, mu))
OQ = [A for A, mu in mats if mu == 1]
GO = [A for A, mu in mats]
scalarOQ = {((lam * A[0][0]) % P, (lam * A[0][1]) % P,
             (lam * A[1][0]) % P, (lam * A[1][1]) % P)
            for lam in range(1, P) for A in OQ}
check("group orders: |O(Q)|=16, |GO(Q)|=96, |F_7^ x O(Q)|=48",
      len(OQ) == 16 and len(GO) == 96 and len(scalarOQ) == 48)


def orbit_count(multipliers):
    seen = set()
    count = 0
    for r in range(1, P):
        if r in seen:
            continue
        count += 1
        stack = [r]
        seen.add(r)
        while stack:
            x = stack.pop()
            for m in multipliers:
                y = (x * m) % P
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return count


check("radius orbits: O(Q) six, F_7^ x O(Q) two, GO(Q) one",
      orbit_count({1}) == 6
      and orbit_count({1, 2, 4}) == 2
      and orbit_count(set(range(1, P))) == 1)

A = ((1, 4), (3, 1))
check("counterexample A: A^T A = 3I", mu_of(A) == 3)
check("counterexample A: Q(Av) = 3 Q(v)",
      all(qform(A, v) == (3 * (v[0] * v[0] + v[1] * v[1])) % P
          for v in [(x, y) for x in range(P) for y in range(P)]))
S1 = {(x, y) for x in range(P) for y in range(P) if (x * x + y * y) % P == 1}
S3 = {(x, y) for x in range(P) for y in range(P) if (x * x + y * y) % P == 3}
check("counterexample A: A(S_1) = S_3",
      {mat_vec(A, v) for v in S1} == S3)


# Line-direction angle: D = F_49^*/F_7^*, rho(z) = z / conj(z).
def rho(z):
    return div(z, conj(z))


D_image = {rho(z) for z in [(x, y) for x in range(P) for y in range(P)
                            if (x, y) != (0, 0)]}
check("rho image has order 8", len(D_image) == 8)
check("rho kernel is F_7^* (6 elements)",
      len([z for z in [(x, y) for x in range(P) for y in range(P)
                       if (x, y) != (0, 0)] if rho(z) == (1, 0)]) == 6)

# A direction missing the unit circle has nonsquare norm, not zero norm.
directions = {canon((x, y)) for x in range(P) for y in range(P)
              if (x, y) != (0, 0)}
direction_hits = {v: sum(canon(z) == v for z in T) for v in directions}
check("no nonzero isotropic direction over F_7",
      all((x * x + y * y) % P != 0 for x, y in directions))
check("four directions meet C twice; four have nonsquare norm and miss C",
      sorted(direction_hits.values()) == [0] * 4 + [2] * 4
      and all((direction_hits[v] == 2) == (leg(v[0]**2 + v[1]**2) == 1)
              for v in directions))

triples = 0
line_ok = True
for A in T:
    for B in T:
        if B == A:
            continue
        for Pp in T:
            if Pp == A or Pp == B:
                continue
            triples += 1
            lhs = rho(div(sub(B, Pp), sub(A, Pp)))
            rhs = div(B, A)
            line_ok = line_ok and lhs == rhs
check("line-direction inscribed relation (336 triples)",
      line_ok and triples == 336)

thal = 0
thal_ok = True
for A in T:
    B = ((-A[0]) % P, (-A[1]) % P)
    for Pp in T:
        if Pp == A or Pp == B:
            continue
        thal += 1
        thal_ok = thal_ok and dot(sub(A, Pp), sub(B, Pp)) == 0
check("finite Thales with P != A,B", thal_ok and thal == 8 * 6)

check("bisection: 2h=1 unsolvable; 2h=2 has two solutions",
      all((2 * h) % 8 != 1 for h in range(8))
      and [h for h in range(8) if (2 * h) % 8 == 2] == [1, 5])
check("n-section: 2h=k is solvable exactly for even k; 3h=k always",
      all((any((2 * h) % 8 == k for h in range(8))) == (k % 2 == 0)
          for k in range(8))
      and all(any((3 * h) % 8 == k for h in range(8)) for k in range(8)))

# Finite-field Fourier layer: chi_j(k) = alpha^{jk} in F_49.
def chi(j, k):
    return power(alpha, (j * k) % 8)


orth = True
for j in range(8):
    for l in range(8):
        total = (0, 0)
        for k in range(8):
            total = add(total, mul(chi(j, k), chi((-l) % 8, k)))
        expected = (1, 0) if j == l else (0, 0)  # 8 = 1 in F_49
        orth = orth and total == expected
check("finite-field character orthogonality (8 = 1)", orth)

eig = True
for j in range(8):
    for k in range(8):
        lhs = sub(chi(j, k + 1), chi(j, k))
        rhs = mul(sub(power(alpha, j), (1, 0)), chi(j, k))
        eig = eig and lhs == rhs
check("Delta chi_j = (alpha^j - 1) chi_j (64 cases)", eig)

trig = True
for k in range(8):
    trig = trig and add(chi(1, k), chi(-1, k)) == ((2 * cos[k]) % P, 0)
    trig = trig and sub(chi(1, k), chi(-1, k)) == (0, (2 * sin[k]) % P)
check("cos/sin via chi_1 and chi_-1 (8 cases)", trig)

# Fourier inversion on the cos function.
def sum_chi(f, j):
    total = (0, 0)
    for k in range(8):
        total = add(total, mul((f[k], 0), chi((-j) % 8, k)))
    return total


def ifft(hat):
    out = []
    for k in range(8):
        total = (0, 0)
        for j in range(8):
            total = add(total, mul(hat[j], chi(j, k)))
        out.append(total)
    return out


def invert_check():
    f = [(cos[k], 0) for k in range(8)]
    hat = [sum_chi([z[0] for z in f], j) for j in range(8)]
    return ifft(hat) == f


check("finite-field Fourier inversion (cos)", invert_check())

if not ok:
    print("\nFAILED: " + ", ".join(failures))
    sys.exit(1)
print("\nALL CHECKS PASSED")
sys.exit(0)
