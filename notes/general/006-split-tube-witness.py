#!/usr/bin/env python3
"""OQ-103.4 witness: the VdP C11 split-tube as an HTWR main/auxiliary decomposition.

Checks two things on the Van der Pol augmented 8D system
(z = (x, y, phi11, phi12, phi21, phi22, A_hor, I)):

1. Block-triangularity (definitional): the phase/action RHS components
   (x', y', A_hor', I') depend only on (x, y), NOT on the variational phi.
   This is the "one-way coupling" that makes the HTWR "main wire + fanout"
   reading exact: the main wire (phase + action) does not read the fanout
   wires (phi).

2. The split-tube wrapping reduction: the phase/action tube radius is
   r_phase = 0.5 h max|F_phase|, while the unsplit single radius is
   r_unsplit = 0.5 h max(|F_phase|, |F_phi|). Since r_phase <= r_unsplit,
   the split never widens the phase tube and is strict exactly when the
   variational RHS dominates the phase RHS.

Companion: 006-split-tube-htwr.md.  Status labels follow
governance/05-mathematical-status.md.
"""

EPS = 1.0
Y0 = 2.1727126964  # VdP C11 reference initial y0 (docs/17)

PHASE = (0, 1, 6, 7)      # x, y, A_hor, I        -> main wire
PHI = (2, 3, 4, 5)        # phi11..phi22           -> fanout-auxiliary wire


def rhs(z):
    x, y, p11, p12, p21, p22, A, I = z
    j21 = -1.0 - 2.0 * EPS * x * y
    j22 = EPS * (1.0 - x * x)
    return [
        y,                                          # x'
        -x + EPS * (1.0 - x * x) * y,               # y'
        p21,                                        # phi11'
        p22,                                        # phi12'
        j21 * p11 + j22 * p21,                      # phi21'
        j21 * p12 + j22 * p22,                      # phi22'
        -x + EPS * (1.0 - x * x) * y - y * y,       # A_hor'
        y * y,                                      # I'
    ]


def rk4(z0, t_end, steps):
    z = list(z0)
    dt = t_end / steps
    for _ in range(steps):
        k1 = rhs(z)
        k2 = rhs([z[i] + 0.5 * dt * k1[i] for i in range(8)])
        k3 = rhs([z[i] + 0.5 * dt * k2[i] for i in range(8)])
        k4 = rhs([z[i] + dt * k3[i] for i in range(8)])
        z = [z[i] + dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6.0 for i in range(8)]
    return z


# --- 1. Block-triangularity: phase/action RHS must not depend on phi. ------
z0 = [0.0, Y0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
f_actual = rhs(z0)
z0_zero_phi = z0[:]
z0_zero_phi[2:6] = [0.0, 0.0, 0.0, 0.0]
f_zero_phi = rhs(z0_zero_phi)
triangular = all(abs(f_actual[i] - f_zero_phi[i]) < 1e-15 for i in PHASE)
print("Block-triangularity: phase/action RHS unchanged when phi := 0 ?", triangular)
for i in PHASE:
    assert abs(f_actual[i] - f_zero_phi[i]) < 1e-15, f"component {i} reads phi"
print("  (phase/action components", PHASE, "read only x,y; components", PHI, "read x,y AND phi)")
print()

# --- 2. Split-tube radius vs unsplit radius along the orbit. ---------------
print("t      | max|F_phase|  max|F_phi|  r_phase/r_unsplit")
for t in (0.0, 1.0, 2.0, 3.0, 3.62, 4.0):
    z = rk4(z0, t, 10000)
    f = rhs(z)
    fp = max(abs(f[i]) for i in PHASE)
    fq = max(abs(f[i]) for i in PHI)
    # split phase radius / unsplit radius  =  fp / max(fp, fq)
    ratio = fp / max(fp, fq)
    print(f"{t:6.2f} | {fp:11.4f}  {fq:9.4f}  {ratio:8.4f}")

print()
print("Interpretation: r_phase <= r_unsplit always (ratio <= 1). The reduction is")
print("strict exactly where max|F_phi| > max|F_phase| (ratio < 1). On the C11")
print("periodic orbit the variational RHS is NOT consistently dominant, so the")
print("split's wrapping gain is modest (ratio ~ 0.7-1.0); its decisive value was")
print("during shooting, where phi grows large before convergence (docs/17 sec 11).")
