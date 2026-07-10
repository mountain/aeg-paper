from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

import numpy as np
from scipy.spatial import cKDTree

from .config import ObservableConfig, ProtocolConfig, RelaxConfig
from .core import (
    build_contact_pairs,
    build_neighbor_pairs,
    build_repair_graph,
    compute_forces,
    isotropic_box_rescale,
    relax_state,
)
from .state import PackingState


@dataclass(slots=True)
class ACSAccumulator:
    A: float = 0.0
    M: float = 0.0
    tau_disc: float = 0.0
    last_a_g: float | None = None
    last_v: float | None = None

    def update(self, a_g: float, v: float) -> dict[str, float]:
        if self.last_a_g is None or self.last_v is None:
            self.last_a_g = float(a_g)
            self.last_v = float(v)
            return {
                "delta_M": 0.0,
                "r_t": 0.0,
                "A_t": self.A,
                "M_t": self.M,
                "tau_disc": self.tau_disc,
            }
        delta_M = 2.0 * (float(v) - self.last_v)
        r_t = float(a_g) - np.exp(delta_M) * self.last_a_g
        self.A += r_t
        self.M += delta_M
        self.tau_disc += np.exp(self.M - delta_M) * r_t
        self.last_a_g = float(a_g)
        self.last_v = float(v)
        return {
            "delta_M": float(delta_M),
            "r_t": float(r_t),
            "A_t": float(self.A),
            "M_t": float(self.M),
            "tau_disc": float(self.tau_disc),
        }


def _pair_geometry(state: PackingState, pairs: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if pairs.size == 0:
        return (
            np.empty((0, 2), dtype=float),
            np.empty((0,), dtype=float),
            np.empty((0,), dtype=float),
            np.empty((0,), dtype=float),
        )
    pos = state.positions
    radii = state.radii
    i = pairs[:, 0]
    j = pairs[:, 1]
    dx = pos[j] - pos[i]
    dx -= state.box_length * np.round(dx / state.box_length)
    d2 = np.sum(dx * dx, axis=1)
    d = np.sqrt(d2 + 1.0e-24)
    sr = radii[i] + radii[j]
    g = d2 - sr * sr
    return dx, d, sr, g


def stage_metrics(
    state: PackingState,
    protocol_cfg: ProtocolConfig,
    repair_edges: np.ndarray | None = None,
) -> dict[str, Any]:
    if repair_edges is None:
        repair_edges = build_repair_graph(
            state,
            k=protocol_cfg.repair_k,
            gap_tol=protocol_cfg.logging_gap_tol,
            max_degree=protocol_cfg.repair_max_degree,
        )
    neighbor_pairs = build_neighbor_pairs(state, protocol_cfg.neighbor_cut_factor)
    contact_pairs = build_contact_pairs(state, neighbor_pairs, protocol_cfg.contact_tol)
    _, _, _, g_contact = _pair_geometry(state, contact_pairs)
    _, _, _, g_repair = _pair_geometry(state, repair_edges)
    m = int(contact_pairs.shape[0])
    z = 2.0 * m / state.n if state.n > 0 else 0.0
    a_c = 3.0 - m / state.n if state.n > 0 else np.nan
    a_g = float(np.sqrt(np.mean(g_repair * g_repair))) if g_repair.size > 0 else 0.0
    out = {
        "phi": float(state.packing_fraction),
        "box_length": float(state.box_length),
        "v": float(np.log(state.box_length)),
        "m_contact": m,
        "z_contact": float(z),
        "a_C": float(a_c),
        "repair_edges": int(repair_edges.shape[0]),
        "a_G": float(a_g),
        "a_G_abs_mean": float(np.mean(np.abs(g_repair))) if g_repair.size > 0 else 0.0,
        "a_G_max_abs": float(np.max(np.abs(g_repair))) if g_repair.size > 0 else 0.0,
        "contact_gap_abs_mean": float(np.mean(np.abs(g_contact))) if g_contact.size > 0 else 0.0,
    }
    return out


def estimate_phi_j(
    state: PackingState,
    protocol_cfg: ProtocolConfig,
    relax_cfg: RelaxConfig,
    obs_cfg: ObservableConfig,
) -> dict[str, float]:
    target = float(obs_cfg.phi_target_pressure)

    def pressure_at_factor(factor: float) -> tuple[float, float]:
        trial = isotropic_box_rescale(state, factor)
        local_relax = RelaxConfig(
            steps=obs_cfg.jamming_relax_steps,
            dt_pos=relax_cfg.dt_pos,
            dt_logr=0.0,
            momentum=relax_cfg.momentum,
            neighbor_update=relax_cfg.neighbor_update,
            force_tol=relax_cfg.force_tol * 2.0,
            min_steps=max(20, relax_cfg.min_steps // 2),
            max_step_norm=relax_cfg.max_step_norm,
        )
        stats = relax_state(
            trial,
            local_relax,
            protocol_cfg,
            allow_radii=False,
            repair_edges=None,
            repair_kappa=0.0,
        )
        return float(stats.pressure), float(trial.packing_fraction)

    factor = 1.0
    p0, phi0 = pressure_at_factor(factor)
    if abs(p0 - target) < target:
        return {"phi_J": phi0, "pressure_J": p0, "jamming_factor": factor}

    if p0 > target:
        low_f, low_p = factor, p0
        high_f, high_p = factor, p0
        for _ in range(12):
            high_f *= 1.01
            high_p, high_phi = pressure_at_factor(high_f)
            if high_p <= target:
                break
        else:
            return {"phi_J": phi0, "pressure_J": p0, "jamming_factor": factor}
        low_phi = state.packing_fraction / (low_f * low_f)
    else:
        high_f, high_p = factor, p0
        low_f, low_p = factor, p0
        for _ in range(12):
            low_f *= 0.99
            low_p, low_phi = pressure_at_factor(low_f)
            if low_p >= target:
                break
        else:
            return {"phi_J": phi0, "pressure_J": p0, "jamming_factor": factor}
        high_phi = state.packing_fraction / (high_f * high_f)

    best_phi = phi0
    best_p = p0
    best_f = factor
    for _ in range(obs_cfg.jamming_bisect_steps):
        mid_f = 0.5 * (low_f + high_f)
        mid_p, mid_phi = pressure_at_factor(mid_f)
        best_phi, best_p, best_f = mid_phi, mid_p, mid_f
        if mid_p > target:
            low_f, low_p = mid_f, mid_p
        else:
            high_f, high_p = mid_f, mid_p
    return {"phi_J": float(best_phi), "pressure_J": float(best_p), "jamming_factor": float(best_f)}



def estimate_moduli(
    state: PackingState,
    protocol_cfg: ProtocolConfig,
    relax_cfg: RelaxConfig,
    obs_cfg: ObservableConfig,
) -> dict[str, float]:
    eps_list = list(obs_cfg.bulk_eps)
    pressures: list[float] = []
    phis: list[float] = []
    energies: list[float] = []
    compressed_states: list[PackingState] = []
    for eps in eps_list:
        factor = 1.0 - eps
        trial = isotropic_box_rescale(state, factor)
        local_relax = RelaxConfig(
            steps=max(80, relax_cfg.steps // 2),
            dt_pos=relax_cfg.dt_pos,
            dt_logr=0.0,
            momentum=relax_cfg.momentum,
            neighbor_update=relax_cfg.neighbor_update,
            force_tol=relax_cfg.force_tol * 2.0,
            min_steps=max(20, relax_cfg.min_steps // 2),
            max_step_norm=relax_cfg.max_step_norm,
        )
        stats = relax_state(trial, local_relax, protocol_cfg, allow_radii=False, repair_edges=None, repair_kappa=0.0)
        pressures.append(stats.pressure)
        phis.append(trial.packing_fraction)
        energies.append(stats.final_energy)
        compressed_states.append(trial)
    eta = np.array([1.0 - (1.0 - eps) ** 2 for eps in eps_list], dtype=float)
    p = np.array(pressures, dtype=float)
    if len(eta) >= 2 and np.any(np.diff(eta) != 0):
        K = float(np.polyfit(eta, p, deg=1)[0])
    else:
        K = float("nan")

    gamma = float(obs_cfg.shear_gamma)
    # Use the most compressed state as a finite-pressure reference.
    ref = compressed_states[-1].copy()
    base_pairs = build_neighbor_pairs(ref, protocol_cfg.neighbor_cut_factor)
    base_force = compute_forces(ref, protocol_cfg, base_pairs, allow_radii=False, repair_edges=None, repair_kappa=0.0)
    e0 = base_force.energy
    area = ref.area
    g_vals = []
    for sign in (-1.0, 1.0):
        trial = ref.copy()
        trial.positions[:, 0] = (trial.positions[:, 0] + sign * gamma * trial.positions[:, 1]) % trial.box_length
        local_relax = RelaxConfig(
            steps=max(60, relax_cfg.steps // 3),
            dt_pos=relax_cfg.dt_pos,
            dt_logr=0.0,
            momentum=relax_cfg.momentum,
            neighbor_update=relax_cfg.neighbor_update,
            force_tol=relax_cfg.force_tol * 3.0,
            min_steps=max(20, relax_cfg.min_steps // 2),
            max_step_norm=relax_cfg.max_step_norm,
        )
        stats = relax_state(trial, local_relax, protocol_cfg, allow_radii=False, repair_edges=None, repair_kappa=0.0)
        dE = max(0.0, stats.final_energy - e0)
        G = 2.0 * dE / (area * gamma * gamma + 1.0e-24)
        g_vals.append(G)
    G0 = float(np.mean(g_vals)) if g_vals else float("nan")
    return {
        "K0": float(K),
        "G0": float(G0),
        "pressure_ref": float(pressures[-1]) if pressures else float("nan"),
        "phi_ref": float(phis[-1]) if phis else float("nan"),
    }


def _neighbor_graph_for_order(state: PackingState, protocol_cfg: ProtocolConfig) -> np.ndarray:
    return build_repair_graph(
        state,
        k=protocol_cfg.repair_k,
        gap_tol=protocol_cfg.logging_gap_tol,
        max_degree=protocol_cfg.repair_max_degree,
    )


def compute_psi6(state: PackingState, protocol_cfg: ProtocolConfig) -> np.ndarray:
    edges = _neighbor_graph_for_order(state, protocol_cfg)
    n = state.n
    if edges.size == 0:
        return np.zeros(n, dtype=np.complex128)
    accum = np.zeros(n, dtype=np.complex128)
    count = np.zeros(n, dtype=np.int64)
    pos = state.positions
    i = edges[:, 0]
    j = edges[:, 1]
    dx = pos[j] - pos[i]
    dx -= state.box_length * np.round(dx / state.box_length)
    theta = np.arctan2(dx[:, 1], dx[:, 0])
    phase_ij = np.exp(1j * 6.0 * theta)
    phase_ji = np.exp(1j * 6.0 * (theta + np.pi))
    np.add.at(accum, i, phase_ij)
    np.add.at(accum, j, phase_ji)
    np.add.at(count, i, 1)
    np.add.at(count, j, 1)
    psi6 = np.zeros(n, dtype=np.complex128)
    mask = count > 0
    psi6[mask] = accum[mask] / count[mask]
    return psi6


def compute_c6_metrics(state: PackingState, protocol_cfg: ProtocolConfig, obs_cfg: ObservableConfig) -> dict[str, Any]:
    psi6 = compute_psi6(state, protocol_cfg)
    mean_r = float(np.mean(state.radii))
    rmax = min(0.45 * state.box_length, obs_cfg.structural_rmax_factor * mean_r)
    tree = cKDTree(state.positions, boxsize=state.box_length)
    pairs = tree.query_pairs(r=rmax, output_type="ndarray")
    if pairs.size == 0:
        return {"psi6_abs_mean": float(np.mean(np.abs(psi6))), "xi6": float("nan"), "c6_r": [], "c6": []}
    pos = state.positions
    i = pairs[:, 0]
    j = pairs[:, 1]
    dx = pos[j] - pos[i]
    dx -= state.box_length * np.round(dx / state.box_length)
    d = np.sqrt(np.sum(dx * dx, axis=1) + 1.0e-24)
    corr = np.real(psi6[i] * np.conj(psi6[j]))
    bins = np.linspace(0.0, rmax, obs_cfg.c6_bins + 1)
    idx = np.digitize(d, bins) - 1
    c6 = np.zeros(obs_cfg.c6_bins, dtype=float)
    counts = np.zeros(obs_cfg.c6_bins, dtype=float)
    for b, val in zip(idx, corr):
        if 0 <= b < obs_cfg.c6_bins:
            c6[b] += val
            counts[b] += 1.0
    mask = counts > 0
    c6[mask] /= counts[mask]
    centers = 0.5 * (bins[:-1] + bins[1:])
    fit_mask = mask & (c6 > 1.0e-4)
    if np.sum(fit_mask) >= 4:
        slope, intercept = np.polyfit(centers[fit_mask], np.log(c6[fit_mask]), deg=1)
        xi6 = float(-1.0 / slope) if slope < 0 else float("inf")
    else:
        xi6 = float("nan")
    return {
        "psi6_abs_mean": float(np.mean(np.abs(psi6))),
        "xi6": float(xi6),
        "c6_r": centers.tolist(),
        "c6": c6.tolist(),
    }


def compute_g2_tau_tr(state: PackingState, obs_cfg: ObservableConfig) -> dict[str, Any]:
    mean_r = float(np.mean(state.radii))
    rmax = min(0.45 * state.box_length, obs_cfg.structural_rmax_factor * mean_r)
    tree = cKDTree(state.positions, boxsize=state.box_length)
    pairs = tree.query_pairs(r=rmax, output_type="ndarray")
    bins = np.linspace(0.0, rmax, obs_cfg.g2_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    counts = np.zeros(obs_cfg.g2_bins, dtype=float)
    if pairs.size > 0:
        pos = state.positions
        i = pairs[:, 0]
        j = pairs[:, 1]
        dx = pos[j] - pos[i]
        dx -= state.box_length * np.round(dx / state.box_length)
        d = np.sqrt(np.sum(dx * dx, axis=1) + 1.0e-24)
        idx = np.digitize(d, bins) - 1
        for b in idx:
            if 0 <= b < obs_cfg.g2_bins:
                counts[b] += 1.0
    rho = state.n / state.area
    shell_areas = 2.0 * np.pi * centers * np.diff(bins)
    expected_pairs = 0.5 * state.n * rho * shell_areas
    g2 = np.zeros_like(centers)
    mask = expected_pairs > 0
    g2[mask] = counts[mask] / expected_pairs[mask]
    tau_tr = float(np.trapezoid(np.abs(g2 - 1.0), centers) / (rmax + 1.0e-12))
    return {"tau_tr": tau_tr, "g2_r": centers.tolist(), "g2": g2.tolist()}


def compute_chi_tilde_small_k(state: PackingState, obs_cfg: ObservableConfig) -> dict[str, float]:
    weights = np.pi * state.radii ** 2
    weights = weights - np.mean(weights)
    L = state.box_length
    vals = []
    for nx in range(-obs_cfg.chi_shell_nmax, obs_cfg.chi_shell_nmax + 1):
        for ny in range(-obs_cfg.chi_shell_nmax, obs_cfg.chi_shell_nmax + 1):
            if nx == 0 and ny == 0:
                continue
            if max(abs(nx), abs(ny)) > obs_cfg.chi_shell_nmax:
                continue
            k = 2.0 * np.pi / L * np.array([nx, ny], dtype=float)
            phase = np.exp(-1j * (state.positions @ k))
            amp = np.sum(weights * phase)
            vals.append((np.abs(amp) ** 2) / (np.sum(weights * weights) + 1.0e-24))
    return {"chi_tilde_small_k": float(np.mean(vals)) if vals else float("nan")}


def compute_dos_proxy(state: PackingState, protocol_cfg: ProtocolConfig, obs_cfg: ObservableConfig) -> dict[str, Any]:
    if state.n > obs_cfg.dos_max_n:
        return {"omega": [], "dos_hist": [], "dos_omega_min": float("nan"), "dos_omega_mean": float("nan")}
    neighbor_pairs = build_neighbor_pairs(state, protocol_cfg.neighbor_cut_factor)
    contact_pairs = build_contact_pairs(state, neighbor_pairs, protocol_cfg.contact_tol)
    if contact_pairs.size == 0:
        return {"omega": [], "dos_hist": [], "dos_omega_min": float("nan"), "dos_omega_mean": float("nan")}
    ndof = 2 * state.n
    H = np.zeros((ndof, ndof), dtype=float)
    dx, d, _, _ = _pair_geometry(state, contact_pairs)
    nvec = dx / np.maximum(d[:, None], 1.0e-12)
    for (i, j), n in zip(contact_pairs, nvec):
        k_mat = np.outer(n, n)
        ii = slice(2 * i, 2 * i + 2)
        jj = slice(2 * j, 2 * j + 2)
        H[ii, ii] += k_mat
        H[jj, jj] += k_mat
        H[ii, jj] -= k_mat
        H[jj, ii] -= k_mat
    evals = np.linalg.eigvalsh(H)
    evals = evals[evals > 1.0e-9]
    omega = np.sqrt(np.maximum(evals, 0.0))
    if omega.size == 0:
        return {"omega": [], "dos_hist": [], "dos_omega_min": float("nan"), "dos_omega_mean": float("nan")}
    hist, edges = np.histogram(omega, bins=min(30, max(8, omega.size // 4)), density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return {
        "omega": omega.tolist(),
        "dos_hist": hist.tolist(),
        "dos_centers": centers.tolist(),
        "dos_omega_min": float(np.min(omega)),
        "dos_omega_mean": float(np.mean(omega)),
    }


def _mc_energy(state: PackingState, protocol_cfg: ProtocolConfig) -> float:
    pairs = build_neighbor_pairs(state, protocol_cfg.neighbor_cut_factor)
    fr = compute_forces(state, protocol_cfg, pairs, allow_radii=False, repair_edges=None, repair_kappa=0.0)
    return float(fr.energy)


def estimate_thermal_proxies(
    state: PackingState,
    protocol_cfg: ProtocolConfig,
    obs_cfg: ObservableConfig,
    rng: np.random.Generator,
) -> dict[str, float]:
    if state.n > obs_cfg.thermal_selected_max_n:
        return {"T_m_proxy": float("nan"), "phi_m_proxy": float("nan")}
    mean_r = float(np.mean(state.radii))
    initial = state.copy()
    psi0 = compute_c6_metrics(initial, protocol_cfg, obs_cfg)["psi6_abs_mean"]
    tm = float("nan")
    for T in obs_cfg.thermal_temperatures:
        trial = initial.copy()
        accepted = 0
        attempted = 0
        for _ in range(obs_cfg.thermal_mc_sweeps * trial.n):
            idx = int(rng.integers(0, trial.n))
            old_pos = trial.positions[idx].copy()
            old_E = _mc_energy(trial, protocol_cfg)
            disp = rng.normal(scale=obs_cfg.thermal_move_scale * mean_r, size=2)
            trial.positions[idx] = (trial.positions[idx] + disp) % trial.box_length
            new_E = _mc_energy(trial, protocol_cfg)
            dE = new_E - old_E
            attempted += 1
            if dE <= 0.0 or rng.random() < np.exp(-dE / max(T, 1.0e-12)):
                accepted += 1
            else:
                trial.positions[idx] = old_pos
        psi = compute_c6_metrics(trial, protocol_cfg, obs_cfg)["psi6_abs_mean"]
        accept_rate = accepted / max(attempted, 1)
        if psi < max(obs_cfg.thermal_order_threshold * max(psi0, 1e-12), 0.05) or accept_rate > 0.65:
            tm = float(T)
            break
    phi_m = float("nan")
    for phi in obs_cfg.phi_m_scan:
        factor = np.sqrt(state.packing_fraction / phi)
        trial = isotropic_box_rescale(state, factor)
        local_relax = RelaxConfig(steps=80, dt_pos=1e-2, dt_logr=0.0, momentum=0.8, neighbor_update=4, force_tol=1e-3, min_steps=20, max_step_norm=5e-2)
        relax_state(trial, local_relax, protocol_cfg, allow_radii=False, repair_edges=None, repair_kappa=0.0)
        metrics = stage_metrics(trial, protocol_cfg)
        if metrics["z_contact"] < 4.5 or metrics["a_C"] > 0.7:
            phi_m = float(phi)
            break
    return {"T_m_proxy": tm, "phi_m_proxy": phi_m}


def compute_final_observables(
    state: PackingState,
    protocol_cfg: ProtocolConfig,
    relax_cfg: RelaxConfig,
    obs_cfg: ObservableConfig,
    rng: np.random.Generator,
) -> dict[str, Any]:
    out: dict[str, Any] = {}
    out.update(estimate_phi_j(state, protocol_cfg, relax_cfg, obs_cfg))
    out.update(estimate_moduli(state, protocol_cfg, relax_cfg, obs_cfg))
    out.update(compute_c6_metrics(state, protocol_cfg, obs_cfg))
    out.update(compute_g2_tau_tr(state, obs_cfg))
    out.update(compute_chi_tilde_small_k(state, obs_cfg))
    out.update(compute_dos_proxy(state, protocol_cfg, obs_cfg))
    out.update(estimate_thermal_proxies(state, protocol_cfg, obs_cfg, rng))
    return out
