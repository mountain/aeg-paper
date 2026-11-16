#!/usr/bin/env python3
"""OQ-104.3 witness: WKB edge-mode quantization for the Encke gap.

Tests the Papaloizou-Lin edge mode in the cold self-gravitating WKB limit
(sigma^2 = kappa^2 - 2 pi G Sigma |k|) with a reflecting edge at the gap outer
edge and the Airy turning-point quantization  int_{r_edge}^{r_L} |k| dr = (n+3/4) pi.

Result (honest negative): the turning point r_L (Lindblad resonance) lies OUTSIDE
the edge only for m < 551. For m >= 551 (including the measured m ~ 2800), r_L is
inside the cleared gap, so there is NO confined mode at the edge; the cold WKB
"edge mode" reduces to the density wave (high radial order n) for m < 551 and
vanishes for m >= 551.  A genuine edge mode therefore requires pressure (c > 0),
which is not in this cold model.
"""

import numpy as np

GM = 3.7931187e16      # Saturn GM, m^3/s^2
A_P = 1.33584e8        # Pan semi-major axis, m
OMEGA_P = np.sqrt(GM / A_P ** 3)
G = 6.674e-11
SIGMA = 500.0          # A-ring surface density, kg/m^2
R_EDGE = A_P + 162.5e3 # outer edge, m


def Omega(r):
    return np.sqrt(GM / r ** 3)


def k_mag(r, w, m):
    """|k| = (kappa^2 - sigma^2) / (2 pi G Sigma), cold disk; sigma = w - m Omega."""
    Om = Omega(r)
    return (Om ** 2 - (w - m * Om) ** 2) / (2 * np.pi * G * SIGMA)


def turning_point(w, m):
    """Outer Lindblad resonance (sigma = +kappa): Omega(r_L) = w/(m+1)."""
    return (GM / (w / (m + 1)) ** 2) ** (1.0 / 3.0)


def phase_integral(m):
    w = m * OMEGA_P
    rL = turning_point(w, m)
    if rL <= R_EDGE:
        return None, rL
    rs = np.linspace(R_EDGE, rL, 4000)
    ks = np.array([k_mag(r, w, m) for r in rs])
    return np.trapezoid(ks, rs) / np.pi, rL


print("m    | r_L - a_P (km) | confined?               | phase/pi | n_eff = phase-0.75")
for m in (100, 200, 300, 400, 500, 551, 600, 1000, 2800):
    phase, rL = phase_integral(m)
    dr = (rL - A_P) / 1e3
    if phase is None:
        print(f"{m:5d} | {dr:10.1f} | r_L < edge (NO mode)     |      -   |   -")
    else:
        print(f"{m:5d} | {dr:10.1f} | edge < r_L (density wave)| {phase:8.1f} | {phase - 0.75:7.1f}")

# evanescent decay length at the edge for the measured m ~ 2800
m = 2800
w = m * OMEGA_P
Om_e = Omega(R_EDGE)
k_ev = ((w - m * Om_e) ** 2 - Om_e ** 2) / (2 * np.pi * G * SIGMA)
print(f"\nm = {m} at the edge: sigma^2 - kappa^2 = {(w - m*Om_e)**2 - Om_e**2:.2e} s^-2")
print(f"  evanescent radial decay length = {1/k_ev:.2f} m = {1/k_ev/1e3:.3f} km")
print("\nConclusion: the cold WKB edge mode does not exist for m >= 551;")
print("the observed m ~ 2800 edge wave is not a cold WKB edge mode (needs pressure).")
