from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass(slots=True)
class PackingState:
    positions: np.ndarray
    base_radii: np.ndarray
    log_radii: np.ndarray
    box_length: float
    metadata: dict[str, Any] = field(default_factory=dict)

    def copy(self) -> "PackingState":
        return PackingState(
            positions=np.array(self.positions, copy=True),
            base_radii=np.array(self.base_radii, copy=True),
            log_radii=np.array(self.log_radii, copy=True),
            box_length=float(self.box_length),
            metadata=dict(self.metadata),
        )

    @property
    def n(self) -> int:
        return int(self.positions.shape[0])

    @property
    def radii(self) -> np.ndarray:
        return self.base_radii * np.exp(self.log_radii)

    @property
    def area(self) -> float:
        return float(self.box_length ** 2)

    @property
    def packing_fraction(self) -> float:
        r = self.radii
        return float(np.pi * np.sum(r * r) / self.area)

    def wrap(self) -> None:
        self.positions %= self.box_length

    def scaled_box_copy(self, factor: float, scale_positions: bool = True) -> "PackingState":
        new = self.copy()
        if scale_positions:
            new.positions *= factor
        new.box_length *= factor
        new.wrap()
        new.metadata["scaled_from"] = self.metadata.get("protocol_stage", "unknown")
        new.metadata["scale_factor"] = float(factor)
        return new

    def unit_rescale_copy(self, factor: float) -> "PackingState":
        new = self.copy()
        new.positions *= factor
        new.base_radii *= factor
        new.box_length *= factor
        new.wrap()
        new.metadata["unit_rescale_factor"] = float(factor)
        return new
