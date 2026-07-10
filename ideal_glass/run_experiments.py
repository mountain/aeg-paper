#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from aeg_ideal_glass.config import ExperimentConfig
from aeg_ideal_glass.runner import run_experiment


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="AEG ideal-glass prototype experiment runner")
    p.add_argument("--n-list", type=int, nargs="+", default=[256, 512, 1024, 2048, 4096, 8192])
    p.add_argument("--seeds", type=int, nargs="*", default=None, help="Explicit seed list. Overrides --num-seeds.")
    p.add_argument("--num-seeds", type=int, default=20)
    p.add_argument("--seed-start", type=int, default=0)
    p.add_argument("--protocols", nargs="+", default=["P0", "P1", "P2", "P3", "P4", "P5", "P6"])
    p.add_argument("--outdir", type=str, default="results")
    p.add_argument("--workers", type=int, default=1)
    p.add_argument("--steps", type=int, default=None, help="Override relaxation steps.")
    p.add_argument("--neighbor-update", type=int, default=None)
    p.add_argument("--phi-init", type=float, default=None)
    p.add_argument("--scale-factor", type=float, default=None)
    p.add_argument("--repair-kappa-schedule", type=float, nargs="*", default=None)
    p.add_argument("--dos-max-n", type=int, default=None)
    p.add_argument("--thermal-selected-max-n", type=int, default=None)
    p.add_argument("--skip-thermal", action="store_true")
    p.add_argument("--skip-dos", action="store_true")
    p.add_argument("--fast", action="store_true", help="Convenience preset for pilot runs.")
    p.add_argument("--smoke-test", action="store_true", help="Very small pilot run.")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.seeds is None or len(args.seeds) == 0:
        seeds = list(range(args.seed_start, args.seed_start + args.num_seeds))
    else:
        seeds = list(args.seeds)
    if args.smoke_test:
        n_list = [64]
        seeds = [0]
        protocols = ["P0", "P1", "P2", "P3", "P4"]
        outdir = Path(args.outdir)
    else:
        n_list = args.n_list
        protocols = args.protocols
        outdir = Path(args.outdir)

    cfg = ExperimentConfig.from_args(n_list=n_list, seeds=seeds, protocols=protocols, outdir=outdir, workers=args.workers)

    if args.fast:
        cfg.relax.steps = 120
        cfg.observables.jamming_bisect_steps = 6
        cfg.observables.jamming_relax_steps = 60
        cfg.observables.thermal_mc_sweeps = 8
        cfg.observables.thermal_selected_max_n = min(cfg.observables.thermal_selected_max_n, 256)
        cfg.observables.dos_max_n = min(cfg.observables.dos_max_n, 256)
    if args.smoke_test:
        cfg.relax.steps = 60
        cfg.observables.jamming_bisect_steps = 4
        cfg.observables.jamming_relax_steps = 40
        cfg.observables.thermal_mc_sweeps = 4
        cfg.observables.thermal_selected_max_n = 64
        cfg.observables.dos_max_n = 64
        cfg.protocol.repair_kappa_schedule = (0.02, 0.08)
        cfg.protocol.micro_steps = 3
    if args.steps is not None:
        cfg.relax.steps = int(args.steps)
    if args.neighbor_update is not None:
        cfg.relax.neighbor_update = int(args.neighbor_update)
    if args.phi_init is not None:
        cfg.protocol.phi_init = float(args.phi_init)
    if args.scale_factor is not None:
        cfg.protocol.scale_factor = float(args.scale_factor)
    if args.repair_kappa_schedule:
        cfg.protocol.repair_kappa_schedule = tuple(float(x) for x in args.repair_kappa_schedule)
    if args.dos_max_n is not None:
        cfg.observables.dos_max_n = int(args.dos_max_n)
    if args.thermal_selected_max_n is not None:
        cfg.observables.thermal_selected_max_n = int(args.thermal_selected_max_n)
    if args.skip_thermal:
        cfg.observables.thermal_selected_max_n = 0
        cfg.observables.thermal_temperatures = tuple()
        cfg.observables.phi_m_scan = tuple()
    if args.skip_dos:
        cfg.observables.dos_max_n = 0

    df = run_experiment(cfg)
    print(df.head())
    print(f"\nSaved summary to: {cfg.outdir / 'summary.csv'}")


if __name__ == "__main__":
    main()
