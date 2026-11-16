#!/usr/bin/env python3
"""OQ-104.3 (pressure re-check): pressure-supported edge mode at the Encke edge.

Adds the pressure term to the dispersion, sigma^2 = kappa^2 - 2 pi G Sigma |k| + c^2 k^2
(Toomre Q = c kappa / (pi G Sigma)), and checks whether it creates a confined
Papaloizou-Lin edge mode for the measured m ~ 2800.

Result (honest negative): the edge-mode existence condition is geometric, not
dispersive -- the turning point (Lindblad resonance) must lie in the ring
(r_t > r_edge), which requires omega < 0.99818 (m+1) Omega_P, i.e. m < 548 for
omega ~ m Omega_P. For m = 2800 the edge is far off-resonance (sigma ~ 5.1 kappa)
and the pressure-supported short wave has radial wavelength ~ c/sigma ~ 50 m,
not the observed ~0.65 km radial amplitude. The pressure does not rescue the
edge-mode reading.
"""

import numpy as np

GM = 3.7931187e16
A_P = 1.33584e8
OMEGA_P = np.sqrt(GM / A_P ** 3)
G = 6.674e-11
SIGMA = 500.0
C = 0.005               # velocity dispersion, m/s (~0.5 cm/s)
R_EDGE = A_P + 162.5e3


def Omega(r):
    return np.sqrt(GM / r ** 3)


def short_wavelength(m):
    Om_e = Omega(R_EDGE)
    sig = m * (OMEGA_P - Om_e)                 # > 0 for r > a_P
    k = (2 * np.pi * G * SIGMA
         + np.sqrt((2 * np.pi * G * SIGMA) ** 2 + 4 * C ** 2 * sig ** 2)) / (2 * C ** 2)
    return 2 * np.pi / k, sig / Om_e


kappa = OMEGA_P
Q = C * kappa / (np.pi * G * SIGMA)
lam_crit = C ** 2 / (G * SIGMA)
print(f"Toomre Q = {Q:.2f}")
print(f"critical wavelength lambda_crit = c^2/(G Sigma) = {lam_crit/1e3:.3f} km\n")

print("m    | sigma/kappa at edge | lambda_short (radial) | lambda_theta (azimuthal)")
for m in (551, 1000, 2800, 10000):
    lam_s, sigk = short_wavelength(m)
    lam_theta = 2 * np.pi * R_EDGE / m
    print(f"{m:5d} | {sigk:8.2f} | {lam_s:8.1f} m = {lam_s/1e3:.3f} km | {lam_theta/1e3:7.1f} km")

print("\nEdge-mode existence condition (geometric): r_t > r_edge  <=>  omega < 0.99818 (m+1) Omega_P")
print("  => for omega ~ m Omega_P, need m < 548. For m = 2800, no confined edge mode.")
print("Conclusion: pressure (Q ~ 6) does NOT turn the m~2800 edge wave into an edge mode;")
print("the short wave there is ~50 m (radial), not the observed ~0.65 km amplitude.")
