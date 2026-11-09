"""Additional source-built geometry modules, preserving the old Mathlib lock (CC0)."""

import json
from pathlib import Path

from analysis_dependencies import sha

HERE = Path(__file__).resolve().parent


def check(mathlib_root, library_root, tick=lambda: None):
    lock = json.loads((HERE / "geometry-library.lock.json").read_text())
    if sha(HERE / "mathlib.lock.json") != lock["mathlib_lock_sha256"]:
        raise ValueError("geometry base-library lock drift")
    old = json.loads((HERE / "mathlib.lock.json").read_text())
    prefix = ".lake/build/lib/lean/"
    for n, name in enumerate(old["compiled_library"]):
        if n % 128 == 0:
            tick()
        if name.startswith(prefix + "Mathlib/"):
            link = library_root / name[len(prefix):]
            if not link.is_symlink() or link.resolve() != (mathlib_root / name).resolve():
                raise ValueError("geometry overlay does not expose the pinned base module: " + name)
    for module in lock["modules"]:
        tick()
        if sha(mathlib_root / module["source"]) != module["source_sha256"]:
            raise ValueError("geometry library source drift: " + module["source"])
        if sha(library_root / module["olean"]) != module["olean_sha256"]:
            raise ValueError("geometry compiled-library drift: " + module["module"])
    return {"geometry_library_lock_sha256": sha(HERE / "geometry-library.lock.json"),
            "additional_geometry_modules": len(lock["modules"])}
