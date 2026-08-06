from __future__ import annotations

from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Iterable

import json
import math
import numpy as np
from numpy.random import Generator, PCG64


def make_rng(seed: int | None = None) -> Generator:
    return Generator(PCG64(seed))


def lognormal_from_cv(mean: float, cv: float, size: int, rng: Generator) -> np.ndarray:
    sigma2 = math.log(1.0 + cv * cv)
    sigma = math.sqrt(sigma2)
    mu = math.log(mean) - 0.5 * sigma2
    return rng.lognormal(mean=mu, sigma=sigma, size=size)


def sample_base_radii(n: int, mean_radius: float, polydispersity: float, rng: Generator) -> np.ndarray:
    radii = lognormal_from_cv(mean_radius, polydispersity, n, rng)
    # Renormalize by mean radius to stabilize units across seeds.
    radii *= mean_radius / np.mean(radii)
    return radii


def compute_box_length_from_phi(radii: np.ndarray, phi: float) -> float:
    total_area = float(np.pi * np.sum(radii * radii))
    return math.sqrt(total_area / phi)


def initialize_positions_grid_jitter(n: int, box_length: float, rng: Generator, jitter: float = 0.42) -> np.ndarray:
    side = int(math.ceil(math.sqrt(n)))
    xs = (np.arange(side) + 0.5) / side
    ys = (np.arange(side) + 0.5) / side
    gx, gy = np.meshgrid(xs, ys, indexing="xy")
    points = np.stack([gx.ravel(), gy.ravel()], axis=1)[:n]
    cell = box_length / side
    noise = (rng.random((n, 2)) - 0.5) * (2.0 * jitter * cell)
    pos = points * box_length + noise
    pos %= box_length
    return pos


def minimum_image(dx: np.ndarray, box_length: float) -> np.ndarray:
    return dx - box_length * np.round(dx / box_length)


def periodic_displacements(positions: np.ndarray, pairs: np.ndarray, box_length: float) -> np.ndarray:
    dx = positions[pairs[:, 1]] - positions[pairs[:, 0]]
    return minimum_image(dx, box_length)


def safe_norm(vec: np.ndarray, axis: int = 1, eps: float = 1.0e-12) -> np.ndarray:
    return np.sqrt(np.sum(vec * vec, axis=axis) + eps)


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def dataclass_to_jsonable(obj: Any) -> Any:
    if is_dataclass(obj):
        return {k: dataclass_to_jsonable(v) for k, v in asdict(obj).items()}
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (list, tuple)):
        return [dataclass_to_jsonable(v) for v in obj]
    if isinstance(obj, dict):
        return {str(k): dataclass_to_jsonable(v) for k, v in obj.items()}
    return obj


def dump_json(path: str | Path, payload: Any) -> None:
    p = Path(path)
    p.write_text(json.dumps(dataclass_to_jsonable(payload), indent=2, ensure_ascii=False), encoding="utf-8")


def chunked(iterable: Iterable[Any], size: int) -> list[list[Any]]:
    chunk: list[Any] = []
    out: list[list[Any]] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) >= size:
            out.append(chunk)
            chunk = []
    if chunk:
        out.append(chunk)
    return out
