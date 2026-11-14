#!/usr/bin/env python3
"""OQ-104.1 image measurement: Encke-gap edge waves from PIA08257.

Downloads NASA's "Encke Waves" image (PIA08257, public domain), detects the gap
edges, and measures the edge-wave azimuthal wavelength and radial amplitude.

Processing metadata (from the PIA08257 caption):
  * original Cassini NAC image: 1 km/pixel;
  * stretched 4x in the horizontal (= radial) direction to exaggerate amplitude;
  * reduced to half size; cropped to the gap.

So the vertical (= azimuthal) pixel scale is 2 km/px, and the horizontal
(= radial) scale is self-calibrated from the 325-km gap width.

Requires numpy + Pillow.  Companion: 008-encke-density-wave.md.
"""

import io
import urllib.request

import numpy as np
from PIL import Image

URL = "https://images-assets.nasa.gov/image/PIA08257/PIA08257~orig.jpg"
GAP_KM = 325.0
R_EDGE = 133_700.0      # Encke gap radius, km
AZ_SCALE = 2.0          # km/px, azimuthal (vertical), from "reduced to half size"


def main():
    data = urllib.request.urlopen(URL).read()
    a = np.array(Image.open(io.BytesIO(data)).convert("L")).astype(float)

    # Detect the two gap edges per row (bright ring -> dark gap -> bright ring).
    left = np.full(a.shape[0], np.nan)
    right = np.full(a.shape[0], np.nan)
    for y in range(a.shape[0]):
        dk = np.where(a[y, :] < 60)[0]
        if len(dk):
            left[y] = dk[0]
            right[y] = dk[-1]

    ys = np.arange(a.shape[0])
    valid = ~np.isnan(left)
    gap_width_px = np.median(right[valid] - left[valid])
    rad_scale = GAP_KM / gap_width_px            # radial km/px (self-calibrated)

    results = {}
    for name, edge in (("left", left), ("right", right)):
        e = edge[valid]
        yv = ys[valid]
        coef = np.polyfit(yv, e, 3)               # remove slow trend
        rc = (e - np.polyval(coef, yv))
        rc = rc - rc.mean()
        best = (0.0, 0)
        for lam in range(10, 200):
            c = np.cos(2 * np.pi * yv / lam)
            s = np.sin(2 * np.pi * yv / lam)
            M = np.vstack([c, s, np.ones_like(yv)]).T
            cf, *_ = np.linalg.lstsq(M, rc, rcond=None)
            amp = np.hypot(cf[0], cf[1])
            if amp > best[0]:
                best = (amp, lam)
        results[name] = (best[1], best[0], rc.std())

    print(f"gap width = {gap_width_px:.1f} px  ->  radial scale = {rad_scale:.3f} km/px")
    print(f"azimuthal scale = {AZ_SCALE} km/px (caption)\n")
    print("edge | wavelength (px) | wavelength (km) | amplitude (px) | amplitude (km) | m = 2pi r / lambda")
    for name, (lam_px, amp_px, rms) in results.items():
        lam_km = lam_px * AZ_SCALE
        amp_km = amp_px * rad_scale
        m = 2 * np.pi * R_EDGE / lam_km
        print(f"{name:5s} | {lam_px:9.0f} | {lam_km:11.0f} | {amp_px:9.2f} | {amp_km:9.2f} | {m:8.0f}")
    print("\n(amplitudes are the strongest single-sinusoid fit; RMS ~ same order)")


if __name__ == "__main__":
    main()
