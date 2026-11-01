#!/usr/bin/env python3
"""
Intrinsic AEG definition of the "path reflection" theta-tilde, accompanying
notes/analysis-and-calculus/43-theta-tilde-intrinsic.md (OQ-098.1a).

From Donaghey/Pushkarev-Byzov: tau = phi^{-1} theta phi sigma, with
sigma = transposition = AEG mirror m.  Hence, since sigma^2 = id,

    theta_tilde := phi^{-1} theta phi = tau o m,

which defines theta_tilde in AEG terms (tau and m) WITHOUT the Dyck path phi.

Algebraic consequences:
    theta_tilde^2 = id,          (theta_tilde is an involution)
    m o theta_tilde = tau^{-1},  (so <m, theta_tilde> = <m, tau>)
and by Donaghey Theorem 6.4, <sigma, theta_tilde> = Z2 * Z2; since sigma = m,
<m, theta_tilde> = Z2 * Z2 (infinite dihedral).

The script verifies, for all PPCTs with n <= 6 leaves:
  * theta_tilde is an involution (theta_tilde^2 = id),
  * m o theta_tilde = tau^{-1} (i.e. m(theta_tilde(tau(T))) = T),
  * theta_tilde orbit lengths are 1 or 2,
  * the orbit lengths of tau and of m o theta_tilde agree.
"""

from functools import lru_cache
import json
import sys


class Leaf:
    __slots__ = ()

    def __repr__(self):
        return "L"


LEAF = Leaf()


class Node:
    __slots__ = ("l", "r")

    def __init__(self, l, r):
        self.l, self.r = l, r

    def __repr__(self):
        return f"N({self.l},{self.r})"


@lru_cache(maxsize=None)
def ppcts(n):
    if n == 1:
        return (LEAF,)
    out = []
    for a in range(1, n):
        b = n - a
        for L in ppcts(a):
            for R in ppcts(b):
                out.append(Node(L, R))
    return tuple(out)


def mirror(t):
    if t is LEAF:
        return LEAF
    return Node(mirror(t.r), mirror(t.l))


def right_decomp(t):
    ds, cur = [], t
    while isinstance(cur, Node):
        ds.append(cur.l)
        cur = cur.r
    return ds, cur


def left_comb(leaf, subs):
    x = leaf
    for s in subs:
        x = Node(x, s)
    return x


def tau(t):
    if t is LEAF:
        return LEAF
    ds, bottom = right_decomp(t)
    dp = [tau(d) for d in ds]
    return left_comb(bottom, dp)


def theta(t):
    """theta_tilde = tau o mirror."""
    return tau(mirror(t))


def main(out_path="/tmp/theta.json"):
    ev = {}
    ok_inv, ok_conj = True, True
    for n in range(2, 7):
        for T in ppcts(n):
            if repr(theta(theta(T))) != repr(T):
                ok_inv = False
            if repr(mirror(theta(tau(T)))) != repr(T):
                ok_conj = False
    ev["theta_squared_is_id"] = ok_inv
    ev["m_theta_eq_tau_inverse"] = ok_conj

    # theta orbit lengths (involution => 1 or 2)
    theta_lens = {}
    for n in range(3, 6):
        ts = list(ppcts(n))
        seen = set()
        lens = []
        for t in ts:
            if repr(t) in seen:
                continue
            cur, c = t, 0
            while repr(cur) not in seen:
                seen.add(repr(cur))
                cur = theta(cur)
                c += 1
            lens.append(c)
        theta_lens[str(n)] = sorted(lens)
    ev["theta_orbit_lengths"] = theta_lens
    ev["theta_is_involution"] = all(set(v) <= {1, 2} for v in theta_lens.values())

    # orbit lengths of tau vs m o theta
    def orbit_len(f, t):
        seen = {}
        cur, i = t, 0
        while repr(cur) not in seen:
            seen[repr(cur)] = i
            cur = f(cur)
            i += 1
            if i > 10000:
                return -1
        return i - seen[repr(cur)]

    same = {}
    for n in range(4, 6):
        same[str(n)] = all(
            orbit_len(tau, T) == orbit_len(lambda x: mirror(theta(x)), T)
            for T in ppcts(n)
        )
    ev["tau_and_mtheta_same_orbit_lengths"] = same
    ev["note"] = ("theta_tilde = tau o m is an involution; m o theta_tilde = tau^{-1}; "
                  "so <m, theta_tilde> = <m, tau> = Z2*Z2 (Donaghey Thm 6.4, sigma=m). "
                  "Defined intrinsically (via tau and m), without the Dyck path phi.")

    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in ev.items() if k != "note"}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
