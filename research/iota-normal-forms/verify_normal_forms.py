#!/usr/bin/env python3
"""The K_n database: iota trees, their beta-normal forms, and their fibres.

n leaves of the single combinator iota = lambda x. x S K; the C_{n-1} plane
binary trees are the programs (construction side K), the beta-normal form of the
associated closed lambda term is the observation (frontier side F), and the
fibre of a normal form is the set of programs with that observation.  The script
enumerates the normal forms for n = 1..13 by the congruence
nf(A B) = nf(nf(A) nf(B)), with exact fibre counts, a witness tree for each
form, its arity and size, its birth level, and the two n = 13 forms whose
application to iota (the n = 14 explosive terms) exceeds the size cap.

Every table entry is asserted; the script exits non-zero when a check fails.
`--verify-evidence` compares the regenerated JSON byte for byte with the
committed evidence.

Run: python3 verify_normal_forms.py [out.json] [--verify-evidence]
"""
import json
import sys
from collections import Counter

MAX_N = 13
CAP = 20000


def V(n):
    return ('v', n)


def L(b):
    return ('l', b)


def A(a, b):
    return ('a', a, b)


def shift(t, d, c=0):
    if t[0] == 'v':
        return V(t[1] + d) if t[1] >= c else t
    if t[0] == 'l':
        return L(shift(t[1], d, c + 1))
    return A(shift(t[1], d, c), shift(t[2], d, c))


def subst(t, j, s):
    if t[0] == 'v':
        return s if t[1] == j else t
    if t[0] == 'l':
        return L(subst(t[1], j + 1, shift(s, 1)))
    return A(subst(t[1], j, s), subst(t[2], j, s))


def beta(m, arg):
    return shift(subst(m, 0, shift(arg, 1)), -1)


def step(t):
    if t[0] == 'a':
        a, b = t[1], t[2]
        if a[0] == 'l':
            return beta(a[1], b)
        na = step(a)
        if na is not None:
            return A(na, b)
        nb = step(b)
        if nb is not None:
            return A(a, nb)
        return None
    if t[0] == 'l':
        n = step(t[1])
        return L(n) if n is not None else None
    return None


CACHE = {}


def norm(t):
    if t in CACHE:
        return CACHE[t]
    orig = t
    while True:
        n = step(t)
        if n is None:
            break
        t = n
    CACHE[orig] = t
    return t


def size(t):
    if t[0] == 'v':
        return 1
    if t[0] == 'l':
        return 1 + size(t[1])
    return 1 + size(t[1]) + size(t[2])


def arity(t):
    n = 0
    while t[0] == 'l':
        n += 1
        t = t[1]
    return n


I = L(V(0))
K = L(L(V(1)))
S = L(L(L(A(A(V(2), V(0)), A(V(1), V(0))))))
IOTA = L(A(A(V(0), S), K))
NAMES = 'abcdefghijklmnopqrstuvwxyz'


def pretty(t, d=0):
    if t == S:
        return 'S'
    if t == K:
        return 'K'
    if t == I:
        return 'I'
    if t == IOTA:
        return 'iota'
    if t[0] == 'v':
        idx = d - 1 - t[1]
        return NAMES[idx] if 0 <= idx < d else 'v%d' % t[1]
    if t[0] == 'l':
        nm = NAMES[d] if d < len(NAMES) else 'x%d' % d
        return 'lambda %s.%s' % (nm, pretty(t[1], d + 1))
    a, b = t[1], t[2]
    sa, sb = pretty(a, d), pretty(b, d)
    if a[0] == 'l':
        sa = '(' + sa + ')'
    if b[0] in ('l', 'a'):
        sb = '(' + sb + ')'
    return sa + sb


def serialize(t):
    if t[0] == 'v':
        return ['v', t[1]]
    if t[0] == 'l':
        return ['l', serialize(t[1])]
    return ['a', serialize(t[1]), serialize(t[2])]


def entropy(counts, total):
    import math
    h = 0.0
    for c in counts:
        p = c / total
        if p > 0:
            h -= p * math.log2(p)
    return round(h, 6)


def check(name, condition, detail=None):
    if not condition:
        raise SystemExit('check failed: ' + name +
                         ('' if detail is None else ' (%r)' % (detail,)))


def norm_capped(t, cap):
    """Normalize; return (term, hit) where hit marks exceeding the size cap."""
    while True:
        if size(t) > cap:
            return t, True
        n = step(t)
        if n is None:
            return t, False
        t = n


def main(argv):
    out_path = '/tmp/iota-normal-forms.json'
    verify = False
    for arg in argv:
        if arg == '--verify-evidence':
            verify = True
        else:
            out_path = arg

    def term_key(t):
        return json.dumps(serialize(t))

    forms = {1: {IOTA}}
    counts = {1: {IOTA: 1}}
    witness = {1: {IOTA: 'i'}}
    for n in range(2, MAX_N + 1):
        fs, cnt, wit = set(), Counter(), {}
        for i in range(1, n):
            for a in sorted(forms[i], key=term_key):
                for b in sorted(forms[n - i], key=term_key):
                    nf = norm(A(a, b))
                    fs.add(nf)
                    cnt[nf] += counts[i][a] * counts[n - i][b]
                    wit.setdefault(nf, '(' + witness[i][a] + witness[n - i][b] + ')')
        forms[n], counts[n], witness[n] = fs, dict(cnt), wit

    birth = {}
    for n in range(1, MAX_N + 1):
        for f in forms[n]:
            birth.setdefault(f, n)

    expected_s = [1, 1, 2, 2, 5, 7, 13, 17, 23, 28, 41, 59, 90]
    check('s_n sequence', [len(forms[n]) for n in range(1, MAX_N + 1)] == expected_s)

    import math

    def cat(n):
        return math.comb(2 * n, n) // (n + 1)

    for n in range(1, MAX_N + 1):
        check('tree count at %d' % n, sum(counts[n].values()) == cat(n - 1))

    # explosive n=14 pairs: b in S_13 with iota·b exceeding CAP
    explosive = []
    for b in sorted(forms[13], key=term_key):
        _, hit = norm_capped(A(IOTA, b), CAP)
        if hit:
            explosive.append(b)
    check('two explosive forms at n=13', len(explosive) == 2, len(explosive))

    levels = []
    for n in range(1, MAX_N + 1):
        rows = []
        for f in sorted(forms[n], key=lambda t: (size(t), pretty(t))):
            rows.append({
                'term': serialize(f),
                'pretty': pretty(f),
                'arity': arity(f),
                'size': size(f),
                'birth': birth[f],
                'fiber': counts[n][f],
                'witness': witness[n][f],
            })
        ar = Counter(r['arity'] for r in rows)
        levels.append({
            'n': n,
            'trees': sum(counts[n].values()),
            'catalan': cat(n - 1),
            'forms': len(rows),
            'max_fiber': max(r['fiber'] for r in rows),
            'entropy_bits': entropy([r['fiber'] for r in rows], sum(counts[n].values())),
            'arity_distribution': {str(k): ar[k] for k in sorted(ar)},
            'rows': rows,
        })

    # lineage of the two explosive forms
    lineage = []
    for b in explosive:
        parents = []
        for i in range(1, 13):
            for x in forms[i]:
                for y in forms[13 - i]:
                    if norm(A(x, y)) == b:
                        parents.append({'split': [i, 13 - i],
                                        'left': pretty(x), 'right': pretty(y),
                                        'left_birth': birth[x], 'right_birth': birth[y]})
        grandparents = []
        for p in parents:
            x = next(f for f in forms[12] if pretty(f) == p['left'])
            for i in range(1, 12):
                for u in forms[i]:
                    for v in forms[12 - i]:
                        if norm(A(u, v)) == x:
                            grandparents.append({'split': [i, 12 - i],
                                                 'left': pretty(u), 'right': pretty(v),
                                                 'left_birth': birth[u],
                                                 'right_birth': birth[v]})
        lineage.append({
            'form': pretty(b), 'size': size(b), 'arity': arity(b),
            'birth': birth[b], 'fiber_at_13': counts[13][b],
            'parents_at_13': parents,
            'parent_decompositions_at_12': grandparents,
        })

    ev = {
        'definitions': {
            'leaf': 'iota = lambda x. x S K',
            'tree': 'plane binary tree with n leaves, C_{n-1} of them',
            'form': 'beta-normal form of the closed lambda term (leaf = iota)',
            'fiber': 'number of n-leaf trees whose normal form is the given form',
            'birth': 'minimal leaf count at which the form appears',
            'arity': 'number of leading lambdas of the normal form',
            'explosive': 'form b at n=13 whose application iota·b exceeds CAP=%d nodes' % CAP,
        },
        'summary': {
            's_n': expected_s,
            'catalan': [cat(n - 1) for n in range(1, MAX_N + 1)],
            'max_fiber': [max(counts[n].values()) for n in range(1, MAX_N + 1)],
        },
        'levels': levels,
        'explosive_lineage': lineage,
    }
    text = json.dumps(ev, indent=2, sort_keys=True) + '\n'
    if verify:
        with open(out_path, 'rb') as f:
            committed = f.read()
        check('evidence matches byte for byte', text.encode('utf-8') == committed)
        print('evidence verified:', out_path)
        return
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(json.dumps({'levels': [len(levels[n]['rows']) for n in range(MAX_N)],
                      'explosive': [pretty(b) for b in explosive]}, indent=2))
    print('wrote', out_path)


if __name__ == '__main__':
    main(sys.argv[1:])
