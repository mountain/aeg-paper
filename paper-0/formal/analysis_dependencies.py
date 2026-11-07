"""Pinned Mathlib checkout and compiled-library integrity checks (CC0)."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def head(root):
    # Preparation deliberately uses detached, pinned checkouts. A symbolic
    # branch cannot silently replace a published dependency revision.
    value = (root / ".git/HEAD").read_text().strip()
    if len(value) != 40 or any(c not in "0123456789abcdef" for c in value):
        raise ValueError("dependency checkout must have a pinned detached HEAD: " + str(root))
    return value


def check(root, tick=lambda: None):
    lock = json.loads((HERE / "mathlib.lock.json").read_text())
    if head(root) != lock["commit"]:
        raise ValueError("Mathlib checkout revision mismatch")
    for package in lock["packages"].values():
        if head(root / package["path"]) != package["revision"]:
            raise ValueError("Mathlib package revision mismatch: " + package["path"])
    for category in ("sources", "compiled_library"):
        for n, (name, digest) in enumerate(lock[category].items()):
            if n % 128 == 0:
                tick()
            if sha(root / name) != digest:
                raise ValueError("Mathlib " + category + " drift: " + name)
    return {"mathlib_commit": lock["commit"], "mathlib_lock_sha256": sha(HERE / "mathlib.lock.json"),
            "mathlib_source_files": len(lock["sources"]),
            "mathlib_compiled_modules": len(lock["compiled_library"])}
