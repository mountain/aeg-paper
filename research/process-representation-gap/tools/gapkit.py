#!/usr/bin/env python3
"""Shared, minimal harness for the process-representation-gap experiments.

Design rules forced by the work plan (AEG-process-representation-work-plan.md):

* Exact arithmetic only.  Integers, ``fractions.Fraction`` and strings.  No
  floating point ever carries a witness.
* No ``assert``.  Python removes assertions under ``-O``; a checker that
  silently stops checking is not a checker.  Every obligation is an explicit
  ``require`` raising a diagnostic with a stable machine-readable code.
* Deterministic serialisation.  Evidence is emitted through ``canonical`` so
  that byte-for-byte comparison across runs, and across ``-O``, is meaningful.
* Cost is reported, never implied.  ``Cost`` accumulates storage, structural
  size, computation steps, observation count and verification cost separately.

This module carries *no* experiment semantics.  It must not: two checkers that
share a semantic helper are one checker, not two.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from fractions import Fraction
from pathlib import Path

SCHEMA = "aeg.process-representation-gap.v1"


class Diagnostic(Exception):
    """A declared failure with a stable code.

    The code is the contract: negative controls must expect a *specific*
    diagnostic, not "any exception".
    """

    def __init__(self, code: str, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {detail}" if detail else code)

    def as_record(self) -> dict:
        return {"code": self.code, "detail": self.detail}


def require(condition, code: str, detail: str = "") -> None:
    """Raise ``Diagnostic(code, detail)`` unless ``condition`` holds."""
    if not condition:
        raise Diagnostic(code, detail)


def reject(callable_, code: str, detail: str = ""):
    """Run ``callable_`` and require it to fail with exactly ``code``."""
    try:
        callable_()
    except Diagnostic as exc:
        require(
            exc.code == code,
            "GAPKIT-WRONG-DIAGNOSTIC",
            f"expected {code!r}, observed {exc.code!r}",
        )
        return exc.as_record()
    raise Diagnostic("GAPKIT-NO-DIAGNOSTIC", f"expected {code!r}, nothing raised")


# --------------------------------------------------------------------------
# exact scalars
# --------------------------------------------------------------------------

def Q(text: str) -> Fraction:
    """Parse an exact rational from canonical string form."""
    return Fraction(text)


def qtext(value) -> str:
    """Canonical string form of an exact rational or integer."""
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def qtuple(values) -> list:
    return [qtext(v) for v in values]


# --------------------------------------------------------------------------
# deterministic evidence
# --------------------------------------------------------------------------

def canonical(obj) -> str:
    """Deterministic JSON text: sorted keys, fixed indent, trailing newline."""
    return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def emit(obj, path=None) -> str:
    text = canonical(obj)
    if path is not None:
        Path(path).write_text(text, encoding="utf-8")
    return text


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path) -> str:
    return sha256_bytes(Path(path).read_bytes())


# --------------------------------------------------------------------------
# cost accounting
# --------------------------------------------------------------------------

class Cost:
    """Explicit, separated cost channels.

    The plan forbids collapsing these into one number and forbids interpreting
    a finite observer as a scalar or finite-state machine by default.
    """

    def __init__(self) -> None:
        self.storage_bytes = 0        # serialised representation size
        self.structural_size = 0      # nodes/fields retained by the summary
        self.computation_steps = 0    # exact steps performed by the checker
        self.observations = 0         # times the task observation was read
        self.verification_cost = 0    # steps spent re-checking

    def as_record(self) -> dict:
        return {
            "storage_bytes": self.storage_bytes,
            "structural_size": self.structural_size,
            "computation_steps": self.computation_steps,
            "observations": self.observations,
            "verification_cost": self.verification_cost,
        }

    def step(self, n: int = 1) -> "Cost":
        self.computation_steps += n
        return self

    def observe(self, n: int = 1) -> "Cost":
        self.observations += n
        return self

    def verify(self, n: int = 1) -> "Cost":
        self.verification_cost += n
        return self

    def store(self, payload) -> "Cost":
        """Charge the canonical size of a summary payload."""
        text = canonical(payload)
        self.storage_bytes += len(text.encode("utf-8"))
        self.structural_size += _fields(payload)
        return self


def _fields(payload) -> int:
    """Count retained scalar fields in a nested summary payload."""
    if isinstance(payload, dict):
        return sum(_fields(v) for v in payload.values()) + len(payload)
    if isinstance(payload, (list, tuple)):
        return sum(_fields(v) for v in payload) + len(payload)
    return 1


# --------------------------------------------------------------------------
# enumeration helpers (ordering is part of determinism)
# --------------------------------------------------------------------------

def words(alphabet, max_length: int):
    """All words over ``alphabet`` of length 0..max_length, in a fixed order."""
    alphabet = tuple(alphabet)
    current = [()]
    yield ()
    for _ in range(max_length):
        nxt = []
        for prefix in current:
            for symbol in alphabet:
                word = prefix + (symbol,)
                nxt.append(word)
                yield word
        current = nxt


def julia_list(values) -> str:
    """Render a Julia-style list of string literals for frozen evidence."""
    return "[" + ", ".join(json.dumps(v, ensure_ascii=False) for v in values) + "]"


def environ() -> dict:
    """Stable environment provenance.

    ``sys.flags.optimize`` is deliberately EXCLUDED.  The work plan requires an
    experiment's output to be identical under CPython and under ``python3 -O``;
    recording the run mode inside the evidence would make that comparison fail
    for a reason that has nothing to do with the mathematics.  The run mode is
    reported separately by ``tools/check_determinism.py``.
    """
    return {
        "python_version": sys.version.split()[0],
        "implementation": sys.implementation.name,
    }


def run_mode() -> dict:
    """The mode marker, kept outside the evidence body on purpose."""
    return {"optimized": bool(sys.flags.optimize)}


# --------------------------------------------------------------------------
# pinned sibling checkouts
# --------------------------------------------------------------------------

SIBLING_DEFAULTS = {
    "AEG_ADVA_REPO": "/Users/mingli/Adva/adva",
    "AEG_PROCESS_GEOMETRY_REPO": "/Users/mingli/AEG/process-geometry",
    "AEG_PAPER_REPO": "/Users/mingli/AEG/aeg-paper",
}


def sibling_repo(env_var: str, default: str | None = None) -> Path:
    """Resolve a pinned sibling checkout, overridable by environment variable.

    Reproducing this programme requires three checkouts.  Hard-coding one
    machine's paths would make the evidence unreproducible elsewhere, so each
    path is read from an environment variable and falls back to the declared
    default.  The resolved path is recorded in the evidence, and a missing
    checkout is a LOUD failure: the programme never silently skips a
    cross-repository check, because a skipped check is not a check.
    """
    raw = os.environ.get(env_var) or default or SIBLING_DEFAULTS[env_var]
    return Path(raw).expanduser().resolve()


def sibling_file(env_var: str, relative: str) -> Path:
    return sibling_repo(env_var) / relative
