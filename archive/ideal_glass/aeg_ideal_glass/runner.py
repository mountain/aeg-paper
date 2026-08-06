from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from aeg_ideal_glass.config import ExperimentConfig
from aeg_ideal_glass.protocols import (
    ProtocolRun,
    run_protocol_p0,
    run_protocol_p1,
    run_protocol_p2,
    run_protocol_p3,
    run_protocol_p4,
    run_protocol_p5,
    run_protocol_p6,
)
from aeg_ideal_glass.state import PackingState
from aeg_ideal_glass.utils import (
    compute_box_length_from_phi,
    dump_json,
    ensure_dir,
    initialize_positions_grid_jitter,
    make_rng,
    sample_base_radii,
)


DEPENDENCIES: dict[str, tuple[str, ...]] = {
    "P0": (),
    "P1": (),
    "P2": ("P1",),
    "P3": ("P1",),
    "P4": ("P1",),
    "P5": ("P1",),
    "P6": ("P2",),
}


def _initial_state(n: int, seed: int, cfg: ExperimentConfig) -> PackingState:
    rng = make_rng(seed)
    base_radii = sample_base_radii(n, cfg.protocol.mean_radius, cfg.protocol.polydispersity, rng)
    box_length = compute_box_length_from_phi(base_radii, cfg.protocol.phi_init)
    positions = initialize_positions_grid_jitter(n, box_length, rng)
    state = PackingState(
        positions=positions,
        base_radii=base_radii,
        log_radii=np.zeros(n, dtype=float),
        box_length=box_length,
        metadata={"seed": int(seed), "N": int(n), "phi_init": float(cfg.protocol.phi_init)},
    )
    return state


def _scalarize(final_obs: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in final_obs.items():
        if isinstance(v, (int, float, str, bool)) or v is None:
            out[k] = v
    return out


def _save_protocol_artifacts(case_dir: Path, run: ProtocolRun) -> None:
    protocol_dir = ensure_dir(case_dir / run.protocol)
    dump_json(protocol_dir / "stages.json", run.stages)
    dump_json(protocol_dir / "observables.json", run.final_observables)
    np.savez_compressed(
        protocol_dir / "final_state.npz",
        positions=run.final_state.positions,
        radii=run.final_state.radii,
        base_radii=run.final_state.base_radii,
        log_radii=run.final_state.log_radii,
        box_length=np.array([run.final_state.box_length], dtype=float),
    )


def run_case(n: int, seed: int, cfg: ExperimentConfig) -> list[dict[str, Any]]:
    case_dir = ensure_dir(cfg.outdir / f"N{n}" / f"seed{seed:04d}")
    dump_json(case_dir / "config.json", cfg)
    initial = _initial_state(n, seed, cfg)
    rng = make_rng(seed + 10_000_000)
    requested = set(cfg.protocols)
    completed: dict[str, ProtocolRun] = {}

    def need(protocol: str) -> bool:
        if protocol in requested:
            return True
        return any(protocol in DEPENDENCIES.get(p, ()) for p in requested)

    if need("P0"):
        completed["P0"] = run_protocol_p0(initial, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P0"])
    if need("P1"):
        completed["P1"] = run_protocol_p1(initial, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P1"])
    if need("P2"):
        completed["P2"] = run_protocol_p2(completed["P1"].final_state, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P2"])
    if need("P3"):
        completed["P3"] = run_protocol_p3(completed["P1"].final_state, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P3"])
    if need("P4"):
        completed["P4"] = run_protocol_p4(completed["P1"].final_state, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P4"])
    if need("P5"):
        completed["P5"] = run_protocol_p5(completed["P1"].final_state, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P5"])
    if need("P6"):
        completed["P6"] = run_protocol_p6(completed["P2"].final_state, cfg, rng)
        _save_protocol_artifacts(case_dir, completed["P6"])

    rows: list[dict[str, Any]] = []
    for protocol in cfg.protocols:
        run = completed[protocol]
        last_stage = dict(run.stages[-1]) if run.stages else {}
        row = {
            "N": int(n),
            "seed": int(seed),
            "protocol": protocol,
            **last_stage,
            **_scalarize(run.final_observables),
        }
        rows.append(row)
    dump_json(case_dir / "summary_rows.json", rows)
    return rows



def _safe_run_case(args: tuple[int, int, ExperimentConfig]) -> tuple[tuple[int, int], list[dict[str, Any]] | None, str | None]:
    n, seed, cfg = args
    try:
        rows = run_case(n, seed, cfg)
        return (n, seed), rows, None
    except Exception as exc:  # pragma: no cover - defensive runtime path
        return (n, seed), None, f"{type(exc).__name__}: {exc}"



def run_experiment(cfg: ExperimentConfig) -> pd.DataFrame:
    ensure_dir(cfg.outdir)
    all_rows: list[dict[str, Any]] = []
    jobs = [(int(n), int(seed), cfg) for n in cfg.n_list for seed in cfg.seeds]
    if cfg.workers <= 1:
        for n, seed, _ in jobs:
            _, rows, err = _safe_run_case((n, seed, cfg))
            if err is not None:
                err_path = ensure_dir(cfg.outdir / f"N{n}" / f"seed{seed:04d}") / "error.txt"
                err_path.write_text(err, encoding="utf-8")
                continue
            assert rows is not None
            all_rows.extend(rows)
    else:
        with ProcessPoolExecutor(max_workers=cfg.workers) as ex:
            futs = {ex.submit(_safe_run_case, job): job for job in jobs}
            for fut in as_completed(futs):
                (n, seed), rows, err = fut.result()
                if err is not None:
                    err_path = ensure_dir(cfg.outdir / f"N{n}" / f"seed{seed:04d}") / "error.txt"
                    err_path.write_text(err, encoding="utf-8")
                    continue
                assert rows is not None
                all_rows.extend(rows)

    df = pd.DataFrame(all_rows)

    if df.empty:
        error_files = sorted(cfg.outdir.rglob("error.txt"))
        sample_msgs = []
        for p in error_files[:10]:
            try:
                msg = p.read_text(encoding="utf-8").strip()
            except Exception:
                msg = "<unable to read>"
            sample_msgs.append(f"{p}: {msg}")

        joined = "\n".join(sample_msgs) if sample_msgs else "<no error.txt found>"
        raise RuntimeError(
            "No successful runs were produced; summary.csv would be empty.\n"
            f"Found {len(error_files)} error files.\n"
            f"Sample errors:\n{joined}"
        )

    if cfg.save_summary_csv:
        df.to_csv(cfg.outdir / "summary.csv", index=False)
    if cfg.save_summary_csv:
        df.to_csv(cfg.outdir / "summary.csv", index=False)
    dump_json(cfg.outdir / "config_used.json", cfg)

    return df
