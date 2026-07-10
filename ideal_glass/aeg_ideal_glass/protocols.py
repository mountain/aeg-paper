from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .config import ExperimentConfig
from .core import build_repair_graph, inject_defects, isotropic_box_rescale, relax_state
from .metrics import ACSAccumulator, compute_final_observables, stage_metrics
from .state import PackingState


@dataclass(slots=True)
class ProtocolRun:
    protocol: str
    final_state: PackingState
    stages: list[dict[str, Any]]
    final_observables: dict[str, Any]



def _log_stage(
    records: list[dict[str, Any]],
    protocol: str,
    stage_name: str,
    state: PackingState,
    cfg: ExperimentConfig,
    acs: ACSAccumulator,
    repair_edges: np.ndarray | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    rec = {
        "protocol": protocol,
        "stage_name": stage_name,
        **stage_metrics(state, cfg.protocol, repair_edges=repair_edges),
    }
    rec.update(acs.update(rec["a_G"], rec["v"]))
    if extra:
        rec.update(extra)
    records.append(rec)
    return rec



def run_protocol_p0(initial: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = initial.copy()
    state.log_radii[:] = 0.0
    state.metadata["protocol_stage"] = "P0_init"
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P0", "init", state, cfg, acs)
    stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=False, repair_edges=None, repair_kappa=0.0)
    _log_stage(records, "P0", "relaxed", state, cfg, acs, extra={
        "relax_converged": stats.converged,
        "relax_steps": stats.steps_taken,
        "relax_energy": stats.final_energy,
        "relax_pressure": stats.pressure,
        "relax_mean_overlap": stats.mean_overlap,
    })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P0", final_state=state, stages=records, final_observables=final_obs)



def run_protocol_p1(initial: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = initial.copy()
    state.metadata["protocol_stage"] = "P1_init"
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P1", "init", state, cfg, acs)
    stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=None, repair_kappa=0.0)
    _log_stage(records, "P1", "relaxed", state, cfg, acs, extra={
        "relax_converged": stats.converged,
        "relax_steps": stats.steps_taken,
        "relax_energy": stats.final_energy,
        "relax_pressure": stats.pressure,
        "relax_mean_overlap": stats.mean_overlap,
    })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P1", final_state=state, stages=records, final_observables=final_obs)



def run_protocol_p2(parent: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = parent.copy()
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P2", "start_from_P1", state, cfg, acs)
    for idx, kappa in enumerate(cfg.protocol.repair_kappa_schedule):
        repair_edges = build_repair_graph(
            state,
            k=cfg.protocol.repair_k,
            gap_tol=cfg.protocol.repair_gap_tol,
            max_degree=cfg.protocol.repair_max_degree,
        )
        _log_stage(records, "P2", f"repair_graph_{idx}", state, cfg, acs, repair_edges=repair_edges, extra={"repair_kappa": float(kappa)})
        stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=repair_edges, repair_kappa=float(kappa))
        _log_stage(records, "P2", f"repair_relax_{idx}", state, cfg, acs, repair_edges=repair_edges, extra={
            "repair_kappa": float(kappa),
            "relax_converged": stats.converged,
            "relax_steps": stats.steps_taken,
            "relax_energy": stats.final_energy,
            "relax_pressure": stats.pressure,
            "relax_mean_overlap": stats.mean_overlap,
        })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P2", final_state=state, stages=records, final_observables=final_obs)



def run_protocol_p3(parent: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = parent.copy()
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P3", "start_from_P1", state, cfg, acs)
    state = isotropic_box_rescale(state, cfg.protocol.scale_factor)
    _log_stage(records, "P3", "scale", state, cfg, acs, extra={"scale_factor": float(cfg.protocol.scale_factor)})
    repair_edges = build_repair_graph(state, cfg.protocol.repair_k, cfg.protocol.repair_gap_tol, cfg.protocol.repair_max_degree)
    stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=repair_edges, repair_kappa=float(cfg.protocol.repair_kappa_schedule[-1]))
    _log_stage(records, "P3", "repair_relax", state, cfg, acs, repair_edges=repair_edges, extra={
        "repair_kappa": float(cfg.protocol.repair_kappa_schedule[-1]),
        "relax_converged": stats.converged,
        "relax_steps": stats.steps_taken,
        "relax_energy": stats.final_energy,
        "relax_pressure": stats.pressure,
        "relax_mean_overlap": stats.mean_overlap,
    })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P3", final_state=state, stages=records, final_observables=final_obs)



def run_protocol_p4(parent: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = parent.copy()
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P4", "start_from_P1", state, cfg, acs)
    repair_edges = build_repair_graph(state, cfg.protocol.repair_k, cfg.protocol.repair_gap_tol, cfg.protocol.repair_max_degree)
    stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=repair_edges, repair_kappa=float(cfg.protocol.repair_kappa_schedule[-1]))
    _log_stage(records, "P4", "repair_relax", state, cfg, acs, repair_edges=repair_edges, extra={
        "repair_kappa": float(cfg.protocol.repair_kappa_schedule[-1]),
        "relax_converged": stats.converged,
        "relax_steps": stats.steps_taken,
        "relax_energy": stats.final_energy,
        "relax_pressure": stats.pressure,
        "relax_mean_overlap": stats.mean_overlap,
    })
    state = isotropic_box_rescale(state, cfg.protocol.scale_factor)
    _log_stage(records, "P4", "scale", state, cfg, acs, extra={"scale_factor": float(cfg.protocol.scale_factor)})
    post_stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=None, repair_kappa=0.0)
    _log_stage(records, "P4", "post_scale_relax", state, cfg, acs, extra={
        "relax_converged": post_stats.converged,
        "relax_steps": post_stats.steps_taken,
        "relax_energy": post_stats.final_energy,
        "relax_pressure": post_stats.pressure,
        "relax_mean_overlap": post_stats.mean_overlap,
    })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P4", final_state=state, stages=records, final_observables=final_obs)



def run_protocol_p5(parent: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = parent.copy()
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P5", "start_from_P1", state, cfg, acs)
    micro_factor = cfg.protocol.scale_factor ** (1.0 / max(cfg.protocol.micro_steps, 1))
    micro_kappa = float(cfg.protocol.repair_kappa_schedule[-1]) / max(cfg.protocol.micro_steps, 1)
    for t in range(cfg.protocol.micro_steps):
        state = isotropic_box_rescale(state, micro_factor)
        _log_stage(records, "P5", f"micro_scale_{t}", state, cfg, acs, extra={"scale_factor": float(micro_factor), "micro_step": int(t)})
        repair_edges = build_repair_graph(state, cfg.protocol.repair_k, cfg.protocol.repair_gap_tol, cfg.protocol.repair_max_degree)
        stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=repair_edges, repair_kappa=micro_kappa)
        _log_stage(records, "P5", f"micro_repair_{t}", state, cfg, acs, repair_edges=repair_edges, extra={
            "repair_kappa": float(micro_kappa),
            "micro_step": int(t),
            "relax_converged": stats.converged,
            "relax_steps": stats.steps_taken,
            "relax_energy": stats.final_energy,
            "relax_pressure": stats.pressure,
            "relax_mean_overlap": stats.mean_overlap,
        })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P5", final_state=state, stages=records, final_observables=final_obs)



def run_protocol_p6(parent: PackingState, cfg: ExperimentConfig, rng: np.random.Generator) -> ProtocolRun:
    state = parent.copy()
    records: list[dict[str, Any]] = []
    acs = ACSAccumulator()
    _log_stage(records, "P6", "start_from_P2", state, cfg, acs)
    state = inject_defects(state, cfg.protocol.reverse_jitter_pos, cfg.protocol.reverse_jitter_logr, rng)
    _log_stage(records, "P6", "defect_injection", state, cfg, acs, extra={
        "reverse_jitter_pos": float(cfg.protocol.reverse_jitter_pos),
        "reverse_jitter_logr": float(cfg.protocol.reverse_jitter_logr),
    })
    stats = relax_state(state, cfg.relax, cfg.protocol, allow_radii=True, repair_edges=None, repair_kappa=0.0)
    _log_stage(records, "P6", "relax_after_injection", state, cfg, acs, extra={
        "relax_converged": stats.converged,
        "relax_steps": stats.steps_taken,
        "relax_energy": stats.final_energy,
        "relax_pressure": stats.pressure,
        "relax_mean_overlap": stats.mean_overlap,
    })
    final_obs = compute_final_observables(state, cfg.protocol, cfg.relax, cfg.observables, rng)
    return ProtocolRun(protocol="P6", final_state=state, stages=records, final_observables=final_obs)
