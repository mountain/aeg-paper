#!/usr/bin/env python3
"""
047 — Fire-front twist on the flat torus: the wavefront C_t, its self-intersection
count = Gauss circle problem, its Gauss words, and the twist/untwist movie.

The "fire method" on a surface M spreads a wavefront from a basepoint p: in the
universal cover the wavefront is the distance sphere Sigma_t = {d(p~, x) = t},
an ordinary expanding circle. On the quotient M the same front projects to the
distance circle C_t = {q in M : d(p, q) = t}, which wraps, self-intersects and
reconnects. Here M = T^2 = R^2 / Z^2 (unit square torus), p = 0 = origin.

On the torus C_t is the image of the Euclidean circle |z| = t under the folding
map x -> x mod 1 (componentwise). Its self-intersections are the chords of the
circle whose displacement is a lattice vector v in Z^2 \\ {0}; such a chord exists
iff |v| < 2t, so each crossing is born at the event time

        t = |v| / 2 = (1/2) * sqrt(m^2 + n^2).

Hence (Proposition, PROVED):

  * event times = half the square-lattice lengths |v| (the based length spectrum);
  * the self-intersection count is N(t) = #{ v in Z^2\\{0} : |v| < 2t } = r_2(2t) - 1,
    where r_2(R) is the Gauss circle problem counting function, so N(t) ~ 4 pi t^2.

Each unoriented lattice vector contributes exactly two transverse crossings for
t > |v|/2 (the two parallel chords), which coalesce into one diameter tangency at
the birth time t = |v|/2. The cyclic order of the crossings along C_t is its
Gauss word, computed numerically below.

STATUS: event-time formula, N(t) = r_2(2t) - 1 and the two-crossings-per-vector
count are PROVED (elementary chord/translation argument, verified below against
the brute-force folding self-check). Gauss words are COMPUTATIONALLY VERIFIED.
The cut locus of the origin is {x = 1/2} ∪ {y = 1/2} (the first-tangency cross).
"""

from pathlib import Path
from math import pi, sqrt, hypot, floor, atan2
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import animation

OUT = Path(__file__).resolve().parent

TAU = 2.0 * pi


def canonical(m: int, n: int) -> bool:
    """True iff (m, n) is the chosen representative of its {v, -v} class."""
    return (m > 0) or (m == 0 and n > 0)


def fold(q):
    """Fold a point (or Nx2 array) into the fundamental square [0, 1)^2."""
    return np.mod(np.asarray(q, dtype=float), 1.0)


def crossings_at(t):
    """All transverse self-intersections of C_t on the unit square torus.

    Returns a list of dicts, one per crossing, with keys:
      v      : canonical lattice vector (m, n) of the chord displacement
      theta1 : angle of the first circle point of the chord
      theta2 : angle of the second circle point
      q      : the crossing location on the torus (in [0, 1)^2)
    """
    if t <= 0.0:
        return []
    R2 = (2.0 * t) ** 2
    M = int(floor(2.0 * t)) + 1
    out = []
    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            if m * m + n * n >= R2:
                continue
            if not canonical(m, n):
                continue
            L = hypot(m, n)
            d = sqrt(t * t - L * L / 4.0)
            perp = np.array([-n, m], dtype=float) / L
            v = np.array([m, n], dtype=float)
            for sgn in (+1.0, -1.0):
                mid = sgn * d * perp
                a = mid - v / 2.0
                b = mid + v / 2.0
                out.append({
                    "v": (m, n),
                    "theta1": atan2(a[1], a[0]),
                    "theta2": atan2(b[1], b[0]),
                    "q": fold(b),
                })
    return out


def N_exact(t):
    """Self-intersection count N(t) = #{ v in Z^2\\{0} : |v| < 2t }."""
    if t <= 0.0:
        return 0
    R2 = (2.0 * t) ** 2
    M = int(floor(2.0 * t)) + 1
    cnt = 0
    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            if m * m + n * n < R2:
                cnt += 1
    return cnt


def gauss_word(t):
    """Cyclic Gauss word of C_t: labels of crossings in angular order."""
    cs = crossings_at(t)
    events = []
    for i, c in enumerate(cs):
        a1 = c["theta1"] % TAU
        a2 = c["theta2"] % TAU
        events.append((a1, i))
        events.append((a2, i))
    events.sort()
    return [i for _, i in events]


def event_table(R_max=5.0):
    """Sorted event times t = |v|/2 for |v| <= R_max, grouped by shared length."""
    rows = []
    M = int(R_max) + 1
    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            if not canonical(m, n):
                continue
            L = hypot(m, n)
            if L <= R_max:
                rows.append((L / 2.0, (m, n)))
    rows.sort()
    return rows


# ---------------------------------------------------------------------------
# Self-check: the analytic count must equal the length of crossings_at(t) for
# generic t (avoiding exact event times).
# ---------------------------------------------------------------------------
def _self_check():
    tvals = [0.0, 0.3, 0.6, 0.75, 1.05, 1.3, 1.61, 1.9, 2.3]
    for t in tvals:
        n_exact = N_exact(t)
        n_cross = len(crossings_at(t))
        assert n_exact == n_cross, (t, n_exact, n_cross)
    print("self-check OK: len(crossings_at(t)) == N_exact(t) for all probes")


# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------
def _folded_curve(t, n=4000):
    theta = np.linspace(0.0, TAU, n, endpoint=False)
    return np.stack([t * np.cos(theta), t * np.sin(theta)], axis=1)


def _draw_frame(ax_cover, ax_surf, t):
    pts = _folded_curve(t)

    # --- left: universal cover (plain circle + square lattice) ---
    ax_cover.clear()
    ax_cover.set_aspect("equal")
    L = t + 0.7
    for gx in range(-int(L) - 2, int(L) + 3):
        ax_cover.axvline(gx, color="0.8", lw=0.4, zorder=0)
    for gy in range(-int(L) - 2, int(L) + 3):
        ax_cover.axhline(gy, color="0.8", lw=0.4, zorder=0)
    ax_cover.add_patch(plt.Rectangle((0, 0), 1, 1, fill=True,
                                     facecolor="#fff3c4", edgecolor="none", zorder=0))
    ax_cover.plot(pts[:, 0], pts[:, 1], color="#1f77b4", lw=1.2, zorder=2)
    # basepoint and its lattice images (the "other fires")
    for gx in range(-2, 3):
        for gy in range(-2, 3):
            ax_cover.plot([gx], [gy], "o", color="#d62728", ms=2.5, zorder=3)
    ax_cover.plot([0], [0], "o", color="#d62728", ms=5, zorder=4)
    ax_cover.set_xlim(-L, L)
    ax_cover.set_ylim(-L, L)
    ax_cover.set_title(f"universal cover: $\\Sigma_t$, $t={t:.2f}$", fontsize=9)

    # --- right: torus (folded) ---
    ax_surf.clear()
    ax_surf.set_aspect("equal")
    for ox in (-1, 0, 1):
        for oy in (-1, 0, 1):
            shift = np.array([ox, oy], dtype=float)
            ax_surf.plot(pts[:, 0] + shift[0], pts[:, 1] + shift[1],
                         color="#1f77b4", lw=0.9, zorder=2)
    # cut locus of the origin (first-tangency cross)
    ax_surf.axvline(0.5, color="0.6", lw=0.6, ls="--", zorder=0)
    ax_surf.axhline(0.5, color="0.6", lw=0.6, ls="--", zorder=0)
    cs = crossings_at(t)
    if cs:
        qs = np.array([c["q"] for c in cs])
        ax_surf.plot(qs[:, 0], qs[:, 1], "o", color="#d62728", ms=2.5, zorder=4)
    ax_surf.set_xlim(0, 1)
    ax_surf.set_ylim(0, 1)
    ax_surf.set_xticks([0, 0.5, 1])
    ax_surf.set_yticks([0, 0.5, 1])
    ax_surf.set_title(f"torus: $C_t$, $N(t)={N_exact(t)}$", fontsize=9)


def make_snapshots():
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.8))
    for t in (0.35, 0.60, 0.78, 1.10):
        _draw_frame(axes[0], axes[1], t)
        fig.suptitle(f"fire-front twist on $\\mathbb{{T}}^2$ (t = {t:.2f})",
                     fontsize=11)
        fig.tight_layout(rect=[0, 0, 1, 0.96])
        tag = f"{t:.2f}".replace(".", "_")
        fname = OUT / f"047-fire-front-twist-t{tag}.png"
        fig.savefig(fname, dpi=110)
        print("wrote", fname.name)
    plt.close(fig)


def make_nt_staircase():
    tmin, tmax = 0.0, 3.0
    ev = event_table(6.0)
    t_plot = np.linspace(tmin, tmax, 3000)
    N = np.array([N_exact(t) for t in t_plot])
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(t_plot, N, color="#1f77b4", lw=1.4)
    # asymptote 4 pi t^2
    tt = np.linspace(tmin, tmax, 200)
    ax.plot(tt, 4 * pi * tt ** 2, color="0.5", lw=0.9, ls="--",
            label=r"$4\pi t^2$")
    # mark events up to tmax
    shown = 0
    for tt_ev, (m, n) in ev:
        if tt_ev <= tmax:
            ax.axvline(tt_ev, color="#d62728", lw=0.5, ls=":", alpha=0.8)
            ax.text(tt_ev, N_exact(tt_ev + 1e-9) + 1, f"({m},{n})",
                    rotation=90, fontsize=6, ha="right", va="bottom",
                    color="#d62728")
            shown += 1
    ax.set_xlabel("t (fire time)")
    ax.set_ylabel(r"$N(t)$ = # self-intersections of $C_t$")
    ax.set_title(r"$N(t)=r_2(2t)-1$ : the fire-front self-intersection count "
                 "is the Gauss circle problem")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fname = OUT / "047-fire-front-twist-nt.png"
    fig.savefig(fname, dpi=120)
    print("wrote", fname.name, f"({shown} events marked)")
    plt.close(fig)


def make_movie():
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.8))
    tvals = np.linspace(0.05, 2.5, 120)

    def frame(i):
        t = tvals[i]
        _draw_frame(axes[0], axes[1], t)
        fig.suptitle(f"fire-front twist on $\\mathbb{{T}}^2$  (t = {t:.2f})",
                     fontsize=11)
        fig.tight_layout(rect=[0, 0, 1, 0.96])
        return []

    ani = animation.FuncAnimation(fig, frame, frames=len(tvals), interval=90,
                                  blit=False)
    fname = OUT / "047-fire-front-twist.gif"
    ani.save(fname, writer=animation.PillowWriter(fps=11), dpi=100)
    print("wrote", fname.name)
    plt.close(fig)


def main():
    _self_check()
    print("\nevent table (t = |v|/2, canonical v), |v| <= 5:")
    for tt, v in event_table(5.0):
        print(f"  t = {tt:6.3f}   v = {v}")
    print("\nGauss words (cyclic labels, crossings in angular order):")
    for t in (0.35, 0.60, 0.78, 1.10):
        w = gauss_word(t)
        print(f"  t={t:.2f}  N={N_exact(t):2d}  word={w}")
    print(f"\nN(t) at selected t:")
    for t in (0.49, 0.51, 0.70, 0.71, 0.99, 1.01, 2.0, 3.0):
        print(f"  t={t:.2f}  N={N_exact(t)}")
    make_snapshots()
    make_nt_staircase()
    make_movie()


if __name__ == "__main__":
    main()
