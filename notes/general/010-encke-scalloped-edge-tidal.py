#!/usr/bin/env python3
"""Encke scalloped edge: static tidal distortion by Pan (forced epicycle).

The observed Encke gap edge wave is the forced epicyclic distortion of the edge
streamline by Pan's tidal gravity, in the LINEAR (d >> R_H) regime.  In the
co-rotating frame the radial force balance is

    kappa^2 * dr  =  - GM_P * d / (d^2 + y^2)^{3/2}          (radial, epicyclic)

so the forced eccentricity is  e_f = (M_P/M_S) (a_P/d)^2  and the radial
amplitude is  A = a_P e_f = GM_P/(kappa^2 d^2).  The azimuthal profile is a
localized bump of width ~ d.

Result: A ~ 0.79 km (observed ~0.65 km) and azimuthal FWHM ~ 249 km
(observed "wavelength" ~300 km).  Matches the image measurement.
"""

import numpy as np

GM_S = 3.7931187e16     # Saturn GM, m^3/s^2
A_P = 1.33584e8         # Pan semi-major axis, m
OMEGA_P = np.sqrt(GM_S / A_P ** 3)
KAPPA = OMEGA_P
GM_P = 3.30e5           # Pan GM = G * 4.95e15, m^3/s^2
D = 162.5e3             # edge distance from Pan, m


def dr(y):
    return -GM_P * D / (KAPPA ** 2 * (D ** 2 + y ** 2) ** 1.5)


dr_max = abs(dr(0.0))
e_f = dr_max / A_P
print(f"forced eccentricity  e_f = (M_P/M_S)(a_P/d)^2 = {e_f:.3e}")
print(f"radial amplitude      A = a_P e_f = GM_P/(kappa^2 d^2) = {dr_max/1e3:.3f} km")
print(f"  (observed radial amplitude ~ 0.65 km)\n")

y_half = D * np.sqrt(2 ** (2.0 / 3.0) - 1.0)
fwhm = 2 * y_half
print(f"azimuthal profile  dr(y) = dr_max (1 + (y/d)^2)^(-3/2)")
print(f"  FWHM = {fwhm/1e3:.1f} km   (observed 'wavelength' ~ 300 km)\n")

R_H = A_P * (GM_P / (3 * GM_S)) ** (1.0 / 3.0)
print(f"Hill radius R_H = {R_H/1e3:.1f} km;  d/R_H = {D/R_H:.1f}  -> linear tidal regime (d >> R_H)")
print("\nConclusion: the scalloped edge is the forced-epicycle (static tidal)")
print("distortion of the edge by Pan; amplitude and azimuthal scale match the image.")
