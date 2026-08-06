from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(slots=True)
class RelaxConfig:
    steps: int = 300
    dt_pos: float = 1.0e-2
    dt_logr: float = 1.0e-3
    momentum: float = 0.85
    neighbor_update: int = 5
    force_tol: float = 5.0e-4
    min_steps: int = 50
    max_step_norm: float = 5.0e-2


@dataclass(slots=True)
class ProtocolConfig:
    phi_init: float = 0.915
    polydispersity: float = 0.20
    mean_radius: float = 1.0
    contact_tol: float = 0.03
    neighbor_cut_factor: float = 1.45
    repair_k: int = 6
    repair_gap_tol: float = 0.50
    repair_max_degree: int = 6
    overlap_kappa: float = 1.0
    radius_penalty: float = 0.50
    repair_kappa_schedule: Sequence[float] = field(default_factory=lambda: (0.02, 0.05, 0.15, 0.40))
    scale_factor: float = 0.985
    micro_steps: int = 5
    reverse_jitter_pos: float = 0.02
    reverse_jitter_logr: float = 0.01
    logging_gap_tol: float = 0.30
    force_rebuild_repair_graph: bool = True


@dataclass(slots=True)
class ObservableConfig:
    phi_target_pressure: float = 1.0e-4
    jamming_bisect_steps: int = 10
    jamming_relax_steps: int = 120
    bulk_eps: Sequence[float] = field(default_factory=lambda: (5.0e-4, 1.0e-3, 2.0e-3))
    shear_gamma: float = 1.0e-3
    dos_max_n: int = 512
    chi_shell_nmax: int = 2
    c6_bins: int = 30
    g2_bins: int = 40
    structural_rmax_factor: float = 6.0
    thermal_selected_max_n: int = 512
    thermal_temperatures: Sequence[float] = field(default_factory=lambda: (1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3))
    thermal_mc_sweeps: int = 25
    thermal_move_scale: float = 0.05
    thermal_order_threshold: float = 0.35
    phi_m_scan: Sequence[float] = field(default_factory=lambda: (0.70, 0.74, 0.78, 0.82, 0.86, 0.90))


@dataclass(slots=True)
class ExperimentConfig:
    n_list: Sequence[int] = field(default_factory=lambda: (256, 512, 1024, 2048, 4096, 8192))
    seeds: Sequence[int] = field(default_factory=lambda: tuple(range(20)))
    protocols: Sequence[str] = field(default_factory=lambda: ("P0", "P1", "P2", "P3", "P4", "P5", "P6"))
    outdir: Path = Path("results")
    workers: int = 1
    save_stage_npz: bool = True
    save_summary_csv: bool = True
    relax: RelaxConfig = field(default_factory=RelaxConfig)
    protocol: ProtocolConfig = field(default_factory=ProtocolConfig)
    observables: ObservableConfig = field(default_factory=ObservableConfig)

    @classmethod
    def from_args(
        cls,
        n_list: Iterable[int],
        seeds: Iterable[int],
        protocols: Iterable[str],
        outdir: str | Path,
        workers: int = 1,
    ) -> "ExperimentConfig":
        return cls(
            n_list=tuple(int(x) for x in n_list),
            seeds=tuple(int(x) for x in seeds),
            protocols=tuple(str(x) for x in protocols),
            outdir=Path(outdir),
            workers=int(workers),
        )
