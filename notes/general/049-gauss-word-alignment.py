#!/usr/bin/env python3
"""
049 — Gauss-word alignment: the fire-front twist on the flat torus vs the
thrice-punctured sphere.

Unifying observation (verified below).  In both models a crossing of C_t that is
labelled by a deck element g lies on the *perpendicular bisector* of the segment
[ p, g^{-1} p ] (p = basepoint).  As t -> +inf the crossing escapes along that
bisector, so its asymptotic *direction* is the direction of the bisector:

  * flat torus  T^2 = R^2 / Z^2 :  g = translation by v in Z^2.
      bisector = line { x . v = -|v|^2/2 }, direction = arg(v^perp)
      (depends only on the *direction* of v, not |v|).
  * thrice-punctured sphere H^2 / Γ(2):  g = γ in Γ(2).
      bisector = geodesic { d(p, z) = d(γ^{-1} p, z) }, direction = its two
      boundary endpoints (ξ1, ξ2), which depend on the full γ and on p.

Hence the Gauss word of the fire front is, in the limit t -> +inf, the circular
order on the direction circle S^1 of these perpendicular directions — the SAME
combinatorial object in both models.  The flat torus is the degenerate (abelian)
case: every v contributes an *antipodal* pair {arg v^perp, arg v^perp + π},
whereas the hyperbolic non-abelian case contributes a general pair {ξ1, ξ2}.

STATUS: the bisector/direction statements are PROVED (flat: 3-line argument;
hyperbolic: the crossing lies on the geodesic bisector by equidistance, so its
ray-endpoint tends to a bisector endpoint).  The convergence below and the
direction circles are COMPUTATIONALLY VERIFIED EXAMPLE.  The claim that the flat
tangent circle S^1 and the hyperbolic limit circle are the two avatars of "the
direction circle" is a STRUCTURAL PROPOSAL (they are different S^1's: the flat
deck group acts trivially on its boundary, the hyperbolic one by Möbius).
"""

from math import acosh, sqrt, pi, atan2, cos, sin, cosh, sinh, isfinite
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
P = 1j

# ---------------------------------------------------------------- flat torus
def flat_directions(t):
    """Crossing directions for lattice vectors |v| < 2t.
    Returns list of (v, theta_v_perp) with theta in [0, 2pi)."""
    R = 2.0 * t
    out = []
    M = int(R) + 1
    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            if m * m + n * n >= R * R:
                continue
            if not (m > 0 or (m == 0 and n > 0)):
                continue
            th = atan2(m, -n) % (2 * pi)   # arg(v^perp), perp = (-n, m)
            out.append(((m, n), th))
    return out


def flat_crossing_dirs(t, v):
    """The two crossing directions (angles) for lattice vector v at time t."""
    m, n = v
    L = sqrt(m * m + n * n)
    d = sqrt(t * t - L * L / 4.0)
    perp = (-n / L, m / L)
    dirs = []
    for sgn in (+1.0, -1.0):
        mid = (sgn * d * perp[0], sgn * d * perp[1])
        x = (mid[0] - m / 2.0, mid[1] - n / 2.0)
        dirs.append(atan2(x[1], x[0]) % (2 * pi))
    return dirs


# ---------------------------------------------------------------- hyperbolic
GENS = {"A": (1, 2, 0, 1), "a": (1, -2, 0, 1), "B": (1, 0, 2, 1), "b": (1, 0, -2, 1)}
INV = {"A": "a", "a": "A", "B": "b", "b": "B"}


def matmul(X, Y):
    a, b, c, d = X; e, f, g, h = Y
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def minv(M):
    a, b, c, d = M; return (d, -b, -c, a)


def mob(M, z):
    a, b, c, d = M; return (a * z + b) / (c * z + d)


def hypdist(z, w):
    return acosh(1.0 + abs(z - w) ** 2 / (2.0 * z.imag * w.imag))


def disp(M, p=P):
    return hypdist(p, mob(M, p))


def word_mat(word):
    M = (1, 0, 0, 1)
    for ch in word:
        M = matmul(M, GENS[ch])
    return M


def enumerate_words(max_depth):
    cur = [(g, GENS[g], g) for g in GENS]
    for _d in range(1, max_depth + 1):
        for (w, M, last) in cur:
            yield w, M
        nxt = []
        for (w, M, last) in cur:
            for g in GENS:
                if g != INV[last]:
                    nxt.append((w + g, matmul(M, GENS[g]), g))
        cur = nxt


def bisector_endpoints(M):
    """Boundary endpoints of the geodesic bisector of [p, γ^{-1}p]."""
    q = mob(minv(M), P)
    px, py, qx, qy = P.real, P.imag, q.real, q.imag
    A = 1.0 / py - 1.0 / qy
    B = -2.0 * (px / py - qx / qy)
    C = (px * px + py * py) / py - (qx * qx + qy * qy) / qy
    if abs(A) < 1e-12:
        return (-C / B, float("inf"))
    disc = B * B - 4.0 * A * C
    r = sqrt(max(0.0, disc))
    return ((-B + r) / (2.0 * A), (-B - r) / (2.0 * A))


def ray_endpoint(p, z):
    """Boundary endpoint of the geodesic ray from p through z (upper half plane)."""
    if abs(z.real - p.real) < 1e-12:
        return float("inf") if z.imag > p.imag else p.real
    # circle through p, z orthogonal to R: center c on real axis
    c = (abs(p) ** 2 - abs(z) ** 2) / (2.0 * (p.real - z.real))
    R = abs(p - c)
    fp = atan2(p.imag, p.real - c)
    fz = atan2(z.imag, z.real - c)
    return c - R if fz > fp else c + R


def circle_at(z0, t):
    return complex(z0.real, z0.imag * cosh(t)), z0.imag * sinh(t)


def circle_intersect(c1, r1, c2, r2):
    d = abs(c2 - c1)
    if d < 1e-12 or d > r1 + r2 or d < abs(r1 - r2):
        return []
    a_ = (r1 * r1 - r2 * r2 + d * d) / (2.0 * d)
    h = sqrt(max(0.0, r1 * r1 - a_ * a_))
    mid = c1 + a_ * (c2 - c1) / d
    e = (c2 - c1) / d
    off = 1j * h * e
    return [mid + off, mid - off]


def hyp_crossing_dirs(t, M):
    """The two crossing directions (ray endpoints) for γ = matrix M at time t."""
    c1, r1 = circle_at(P, t)
    q0 = mob(minv(M), P)
    c2, r2 = circle_at(q0, t)
    dirs = []
    for z in circle_intersect(c1, r1, c2, r2):
        if z.imag > 1e-9:
            dirs.append(ray_endpoint(P, z))
    return dirs


# ---------------------------------------------------------------- circle map
def cayley_angle(xi):
    """Map a hyperbolic boundary point xi ∈ R ∪ {∞} to an angle on S^1 via
    the Cayley transform C(z) = (z - i)/(z + i), C(∞) = 1."""
    if not isfinite(xi):
        return 0.0
    w = (xi - 1j) / (xi + 1j)
    return atan2(w.imag, w.real) % (2 * pi)


# ---------------------------------------------------------------- main
def main():
    print("=== 1. flat torus: crossing direction -> arg(v^perp) (convergence) ===")
    for v in ((1, 0), (1, 1), (2, 1)):
        th_perp = atan2(v[0], -v[1]) % (2 * pi)
        print(f"  v={v}  arg(v^perp)={th_perp:.4f}", end="   ")
        for t in (1.2, 3.0, 8.0):
            dirs = flat_crossing_dirs(t, v)
            err = min(abs(d - th_perp) % (2 * pi) for d in dirs)
            print(f"t={t}: min|dir-arg_vperp|={err:.3f}", end="  ")
        print()

    print("\n=== 2. hyperbolic: crossing direction -> bisector endpoint ===")
    for w in ("A", "B", "AB", "AbA"):
        M = word_mat(w)
        xi1, xi2 = bisector_endpoints(M)
        print(f"  γ={w}  bisector endpoints=({xi1:.4f}, {xi2:.4f})", end="   ")
        for t in (1.0, 2.0, 4.0):
            dirs = hyp_crossing_dirs(t, M)
            if dirs:
                err = min(min(abs(d - xi1), abs(d - xi2)) for d in dirs)
                print(f"t={t}: min|dir-endpt|={err:.3f}", end="  ")
            else:
                print(f"t={t}: (no crossing yet)", end="  ")
        print()

    # direction-circle figures
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), subplot_kw={})
    # left: flat torus
    ax = axes[0]
    ax.set_aspect("equal")
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.6", lw=0.8)
    for (v, thp) in flat_directions(2.0):
        for sgn in (+1, -1):
            a = (thp + (0 if sgn > 0 else pi)) % (2 * pi)
            ax.plot([cos(a)], [sin(a)], "o", color="#1f77b4", ms=4)
            ax.plot([0, cos(a)], [0, sin(a)], color="0.85", lw=0.5)
    ax.set_title("flat torus: $\\arg v^\\perp$ (antipodal pairs)", fontsize=9)
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25); ax.axis("off")

    # right: hyperbolic limit circle
    ax = axes[1]
    ax.set_aspect("equal")
    ax.plot(np.cos(th), np.sin(th), color="0.6", lw=0.8)
    words = enumerate_words(6)
    seen = set()
    for (w, M) in words:
        dd = disp(M)
        if dd >= 2 * 1.6:
            continue
        key = min(M, minv(M))
        if key in seen:
            continue
        seen.add(key)
        xi1, xi2 = bisector_endpoints(M)
        for xi in (xi1, xi2):
            a = cayley_angle(xi)
            ax.plot([cos(a)], [sin(a)], "o", color="#d62728", ms=4)
    ax.set_title("hyperbolic: bisector endpoints on $\\partial\\mathbb{H}^2$ "
                 "(via Cayley)", fontsize=9)
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25); ax.axis("off")

    fig.suptitle("Gauss-word alignment: perpendicular directions on the direction circle $S^1$")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fname = OUT / "049-gauss-word-alignment.png"
    fig.savefig(fname, dpi=120)
    print("\nwrote", fname.name)


if __name__ == "__main__":
    main()
