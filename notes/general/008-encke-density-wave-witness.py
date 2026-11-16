#!/usr/bin/env python3
"""OQ-104.1 witness: tight-winding density-wave dispersion near the Encke edge.

Solves the self-gravitating, pressure-supported density-wave dispersion relation
in the tight-winding (WKB) limit,

    (omega - m Omega)^2 = kappa^2 - 2 pi G Sigma |k| + c^2 k^2 ,   kappa = Omega,

for the m-th outer Lindblad resonance of Pan (pattern speed omega = m Omega_P).
It is a closed-form quadratic in k, so no multivariate solver is needed here.

Key result: the radial wavelength is lambda ~ c^2/(G Sigma) at the resonance and
DECREASES away from it (the "wrapped-up" spiral).  This "wavelength varies
smoothly" signature is exactly what the Encke gap edges show (Tiscareno et al.,
DPS 2005, abstract 64.02).  Plain-Python math only, no third-party deps.

Companion: 008-encke-density-wave.md.
"""

import math

G = 6.674e-11           # m^3 kg^-1 s^-2
GM = 3.7931187e16       # Saturn GM, m^3/s^2
A_P = 1.33584e8         # Pan semi-major axis, m
OMEGA_P = math.sqrt(GM / A_P ** 3)

SIGMA = 500.0           # A-ring surface density near Encke, kg/m^2
C = 0.005               # velocity dispersion, m/s  (~0.5 cm/s)


def omega(r):
    return math.sqrt(GM / r ** 3)          # Keplerian; kappa = omega


def wavelength(m, r):
    """Radial wavelength of the m-th density wave at radius r (None if evanescent)."""
    sig = m * (OMEGA_P - omega(r))         # Doppler-shifted frequency
    D = sig * sig - omega(r) ** 2          # detuning (0 at resonance)
    a = C * C
    b = 2.0 * math.pi * G * SIGMA
    disc = b * b + 4.0 * a * D
    if disc < 0:
        return None
    k = (b + math.sqrt(disc)) / (2.0 * a)  # trailing wave, k > 0
    return 2.0 * math.pi / k


lam0 = C * C / (G * SIGMA)                  # wavelength at resonance
print(f"Wavelength at resonance  lambda_0 = c^2/(G Sigma) = {lam0:.0f} m = {lam0/1e3:.3f} km")
print(f"  (Sigma = {SIGMA} kg/m^2, c = {C} m/s)\n")

for m in (551, 100, 20):
    r_res = A_P * ((m + 1) / m) ** (2.0 / 3.0)
    lam_theta = 2.0 * math.pi * r_res / m   # azimuthal wavelength
    print(f"m = {m}: r_res = a_P + {(r_res - A_P)/1e3:.1f} km, "
          f"azimuthal lambda_theta = {lam_theta/1e3:.0f} km")
    for dr_km in (0.0, 0.5, 2.0, 10.0):
        lam = wavelength(m, r_res + dr_km * 1e3)
        s = f"{lam/1e3:6.3f} km" if lam else "evanescent"
        print(f"    dr = +{dr_km:5.1f} km  ->  radial lambda = {s}")
    print()

print("Interpretation: the radial wavelength is ~ c^2/(G Sigma) ~ sub-km and")
print("DECREASES away from resonance (wrapped-up spiral) — matching the observed")
print("'wavelength varies smoothly' signature. The azimuthal wavelength 2 pi r/m")
print("is a separate (constant for fixed m) quantity.")
