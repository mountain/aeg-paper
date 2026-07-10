from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import math
import numpy as np
from numba import njit
from scipy.spatial import cKDTree

from .config import ProtocolConfig, RelaxConfig
from .state import PackingState


@dataclass(slots=True)
class ForceResult:
    energy: float
    forces: np.ndarray
    logr_dirs: np.ndarray
    overlap_pairs: np.ndarray
    pressure: float


@dataclass(slots=True)
class RelaxStats:
    converged: bool
    steps_taken: int
    final_energy: float
    max_force: float
    mean_overlap: float
    pressure: float


@njit(cache=True)
def _accumulate_overlap_numba(
    n: int,
    positions: np.ndarray,
    radii: np.ndarray,
    pairs: np.ndarray,
    box_length: float,
    kappa: float,
) -> tuple[float, np.ndarray, np.ndarray, float, float, int]:
    forces = np.zeros((n, 2), dtype=np.float64)
    logr_dirs = np.zeros(n, dtype=np.float64)
    energy = 0.0
    virial = 0.0
    mean_overlap = 0.0
    overlap_count = 0
    for p in range(pairs.shape[0]):
        i = int(pairs[p, 0])
        j = int(pairs[p, 1])
        dx = positions[j, 0] - positions[i, 0]
        dy = positions[j, 1] - positions[i, 1]
        dx -= box_length * np.round(dx / box_length)
        dy -= box_length * np.round(dy / box_length)
        d2 = dx * dx + dy * dy + 1.0e-24
        d = math.sqrt(d2)
        sr = radii[i] + radii[j]
        delta = sr - d
        if delta > 0.0:
            energy += 0.5 * kappa * delta * delta
            fmag = kappa * delta / d
            fx = fmag * dx
            fy = fmag * dy
            forces[i, 0] -= fx
            forces[i, 1] -= fy
            forces[j, 0] += fx
            forces[j, 1] += fy
            logr_dirs[i] -= kappa * delta * radii[i]
            logr_dirs[j] -= kappa * delta * radii[j]
            virial += fmag * d
            mean_overlap += delta
            overlap_count += 1
    if overlap_count > 0:
        mean_overlap /= overlap_count
    return energy, forces, logr_dirs, virial, mean_overlap, overlap_count


@njit(cache=True)
def _accumulate_gap_springs_numba(
    n: int,
    positions: np.ndarray,
    radii: np.ndarray,
    pairs: np.ndarray,
    box_length: np.float64,
    kappa: np.float64,
) -> tuple[float, np.ndarray, np.ndarray]:
    forces = np.zeros((n, 2), dtype=np.float64)
    logr_dirs = np.zeros(n, dtype=np.float64)
    energy = 0.0
    for p in range(pairs.shape[0]):
        i = int(pairs[p, 0])
        j = int(pairs[p, 1])
        dx = positions[j, 0] - positions[i, 0]
        dy = positions[j, 1] - positions[i, 1]
        dx -= box_length * np.round(dx / box_length)
        dy -= box_length * np.round(dy / box_length)
        d2 = dx * dx + dy * dy + 1.0e-24
        d = math.sqrt(d2)
        sr = radii[i] + radii[j]
        gap = d - sr
        energy += 0.5 * kappa * gap * gap
        fmag = kappa * gap / d
        fx = fmag * dx
        fy = fmag * dy
        forces[i, 0] += fx
        forces[i, 1] += fy
        forces[j, 0] -= fx
        forces[j, 1] -= fy
        logr_dirs[i] += kappa * gap * radii[i]
        logr_dirs[j] += kappa * gap * radii[j]
    return energy, forces, logr_dirs


@njit(cache=True)
def _max_row_norm(arr: np.ndarray) -> float:
    maxv = 0.0
    for i in range(arr.shape[0]):
        v = math.sqrt(arr[i, 0] * arr[i, 0] + arr[i, 1] * arr[i, 1])
        if v > maxv:
            maxv = v
    return maxv


@njit(cache=True)
def _clip_rows(arr: np.ndarray, max_norm: float) -> np.ndarray:
    out = np.empty_like(arr)
    for i in range(arr.shape[0]):
        v0 = arr[i, 0]
        v1 = arr[i, 1]
        norm = math.sqrt(v0 * v0 + v1 * v1)
        if norm > max_norm and norm > 0.0:
            scale = max_norm / norm
            out[i, 0] = v0 * scale
            out[i, 1] = v1 * scale
        else:
            out[i, 0] = v0
            out[i, 1] = v1
    return out


@njit(cache=True)
def _clip_vec(arr: np.ndarray, max_abs: float) -> np.ndarray:
    out = np.empty_like(arr)
    for i in range(arr.shape[0]):
        v = arr[i]
        if v > max_abs:
            out[i] = max_abs
        elif v < -max_abs:
            out[i] = -max_abs
        else:
            out[i] = v
    return out


@njit(cache=True)
def _wrap_positions_numba(positions: np.ndarray, box_length: float) -> None:
    for i in range(positions.shape[0]):
        for j in range(2):
            positions[i, j] = positions[i, j] % box_length


@njit(cache=True)
def _zero_mean(arr: np.ndarray) -> None:
    m = 0.0
    for i in range(arr.shape[0]):
        m += arr[i]
    m /= arr.shape[0]
    for i in range(arr.shape[0]):
        arr[i] -= m


@njit(cache=True)
def _copy_pairs(arr: np.ndarray) -> np.ndarray:
    out = np.empty_like(arr)
    for i in range(arr.shape[0]):
        out[i, 0] = arr[i, 0]
        out[i, 1] = arr[i, 1]
    return out


def build_neighbor_pairs(state: PackingState, cutoff_factor: float) -> np.ndarray:
    radii = state.radii
    cutoff = float(cutoff_factor * (2.0 * np.max(radii)))
    tree = cKDTree(state.positions, boxsize=state.box_length)
    pairs = tree.query_pairs(r=cutoff, output_type="ndarray")
    if pairs.size == 0:
        return np.empty((0, 2), dtype=np.int64)
    return np.asarray(pairs, dtype=np.int64)


def build_contact_pairs(state: PackingState, pairs: np.ndarray, contact_tol: float) -> np.ndarray:
    if pairs.size == 0:
        return np.empty((0, 2), dtype=np.int64)
    pos = state.positions
    r = state.radii
    i = pairs[:, 0]
    j = pairs[:, 1]
    dx = pos[j] - pos[i]
    dx -= state.box_length * np.round(dx / state.box_length)
    d = np.sqrt(np.sum(dx * dx, axis=1) + 1.0e-24)
    sr = r[i] + r[j]
    gap_norm = (d - sr) / np.maximum(sr, 1.0e-12)
    keep = gap_norm <= contact_tol
    return np.asarray(pairs[keep], dtype=np.int64)


def build_repair_graph(
    state: PackingState,
    k: int,
    gap_tol: float,
    max_degree: int = 6,
    max_edges: int | None = None,
) -> np.ndarray:
    n = state.n
    tree = cKDTree(state.positions, boxsize=state.box_length)
    dists, idxs = tree.query(state.positions, k=min(k + 1, n), workers=1)
    if idxs.ndim == 1:
        idxs = idxs[:, None]
        dists = dists[:, None]
    radii = state.radii
    per_i: list[list[tuple[int, float]]] = [[] for _ in range(n)]
    for i in range(n):
        for rank in range(1, idxs.shape[1]):
            j = int(idxs[i, rank])
            if j < 0 or j >= n or j == i:
                continue
            d = float(dists[i, rank])
            sr = float(radii[i] + radii[j])
            gn = (d - sr) / max(sr, 1.0e-12)
            if rank <= 3 or gn <= gap_tol:
                per_i[i].append((j, gn))
        per_i[i].sort(key=lambda x: x[1])
        if len(per_i[i]) > max_degree:
            per_i[i] = per_i[i][:max_degree]
    edge_map: dict[tuple[int, int], float] = {}
    for i, cand in enumerate(per_i):
        for j, gn in cand:
            a, b = (i, j) if i < j else (j, i)
            prev = edge_map.get((a, b))
            if prev is None or gn < prev:
                edge_map[(a, b)] = gn
    items = sorted(edge_map.items(), key=lambda kv: kv[1])
    if max_edges is None:
        max_edges = 3 * n
    items = items[:max_edges]
    if not items:
        return np.empty((0, 2), dtype=np.int64)
    pairs = np.array([edge for edge, _ in items], dtype=np.int64)
    return pairs


def compute_forces(
    state: PackingState,
    protocol_cfg: ProtocolConfig,
    overlap_pairs: np.ndarray,
    repair_edges: np.ndarray | None = None,
    allow_radii: bool = False,
    repair_kappa: float = 0.0,
) -> ForceResult:
    radii = state.radii.astype(np.float64)
    energy_o, forces_o, logr_o, virial, mean_overlap, overlap_count = _accumulate_overlap_numba(
        state.n,
        state.positions.astype(np.float64),
        radii,
        overlap_pairs.astype(np.int64),
        float(state.box_length),
        float(protocol_cfg.overlap_kappa),
    )
    energy = float(energy_o)
    forces = forces_o
    logr_dirs = logr_o
    if allow_radii:
        logr_dirs -= float(protocol_cfg.radius_penalty) * state.log_radii
        energy += 0.5 * float(protocol_cfg.radius_penalty) * float(np.sum(state.log_radii ** 2))
    else:
        logr_dirs[:] = 0.0
    if repair_edges is not None and repair_edges.size > 0 and repair_kappa > 0.0:
        energy_r, forces_r, logr_r = _accumulate_gap_springs_numba(
            state.n,
            state.positions.astype(np.float64),
            radii,
            repair_edges.astype(np.int64),
            float(state.box_length),
            float(repair_kappa),
        )
        energy += float(energy_r)
        forces += forces_r
        if allow_radii:
            logr_dirs += logr_r
    if allow_radii:
        _zero_mean(logr_dirs)
    pressure = virial / (2.0 * state.area) if state.area > 0 else 0.0
    return ForceResult(
        energy=energy,
        forces=forces,
        logr_dirs=logr_dirs,
        overlap_pairs=overlap_pairs,
        pressure=pressure,
    )


def relax_state(
    state: PackingState,
    relax_cfg: RelaxConfig,
    protocol_cfg: ProtocolConfig,
    allow_radii: bool,
    repair_edges: np.ndarray | None = None,
    repair_kappa: float = 0.0,
) -> RelaxStats:
    pos_vel = np.zeros_like(state.positions)
    logr_vel = np.zeros_like(state.log_radii)
    overlap_pairs = build_neighbor_pairs(state, protocol_cfg.neighbor_cut_factor)
    final_energy = 0.0
    max_force = np.inf
    mean_overlap = 0.0
    pressure = 0.0
    converged = False
    for step in range(relax_cfg.steps):
        if step == 0 or (step % relax_cfg.neighbor_update) == 0:
            overlap_pairs = build_neighbor_pairs(state, protocol_cfg.neighbor_cut_factor)
        fr = compute_forces(
            state,
            protocol_cfg=protocol_cfg,
            overlap_pairs=overlap_pairs,
            repair_edges=repair_edges,
            allow_radii=allow_radii,
            repair_kappa=repair_kappa,
        )
        max_force = max(_max_row_norm(fr.forces), float(np.max(np.abs(fr.logr_dirs))) if allow_radii else 0.0)
        final_energy = fr.energy
        pressure = fr.pressure
        if overlap_pairs.size > 0:
            # Recompute the mean overlap cheaply using the current pair list.
            pos = state.positions
            r = state.radii
            i = overlap_pairs[:, 0]
            j = overlap_pairs[:, 1]
            dx = pos[j] - pos[i]
            dx -= state.box_length * np.round(dx / state.box_length)
            d = np.sqrt(np.sum(dx * dx, axis=1) + 1.0e-24)
            delta = np.maximum(r[i] + r[j] - d, 0.0)
            active = delta > 0.0
            mean_overlap = float(delta[active].mean()) if np.any(active) else 0.0
        else:
            mean_overlap = 0.0
        if step >= relax_cfg.min_steps and max_force < relax_cfg.force_tol:
            converged = True
            break
        pos_vel = relax_cfg.momentum * pos_vel + relax_cfg.dt_pos * fr.forces
        pos_vel = _clip_rows(pos_vel, relax_cfg.max_step_norm)
        state.positions += pos_vel
        _wrap_positions_numba(state.positions, float(state.box_length))
        if allow_radii:
            logr_vel = relax_cfg.momentum * logr_vel + relax_cfg.dt_logr * fr.logr_dirs
            logr_vel = _clip_vec(logr_vel, relax_cfg.max_step_norm)
            state.log_radii += logr_vel
            _zero_mean(state.log_radii)
    return RelaxStats(
        converged=converged,
        steps_taken=step + 1,
        final_energy=float(final_energy),
        max_force=float(max_force),
        mean_overlap=float(mean_overlap),
        pressure=float(pressure),
    )


def isotropic_box_rescale(state: PackingState, factor: float) -> PackingState:
    return state.scaled_box_copy(float(factor), scale_positions=True)


def inject_defects(
    state: PackingState,
    pos_sigma: float,
    logr_sigma: float,
    rng: np.random.Generator,
) -> PackingState:
    out = state.copy()
    mean_r = float(np.mean(out.radii))
    out.positions += rng.normal(scale=pos_sigma * mean_r, size=out.positions.shape)
    out.wrap()
    out.log_radii += rng.normal(scale=logr_sigma, size=out.log_radii.shape)
    _zero_mean(out.log_radii)
    return out
