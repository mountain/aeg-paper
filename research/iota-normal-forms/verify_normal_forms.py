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

The aggregate sequence, the Catalan totals, the n=14 bound, the cap-hit identity,
the p·iota family and the semantic oracle are asserted; the individual rows are
emitted for the database and are not compared against an independent fixture.
The script exits non-zero when a check fails, and a fuel bound prevents a cyclic
reduction from hanging CI.
`--verify-evidence` compares the regenerated JSON byte for byte with the
committed evidence.

Run: python3 verify_normal_forms.py [out.json] [--verify-evidence]
"""
import json
import sys
from collections import Counter

MAX_N = 13
CAP = 20000
MAX_STEPS = 2000000


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
    steps = 0
    while True:
        n = step(t)
        if n is None:
            break
        t = n
        steps += 1
        if steps > MAX_STEPS:
            raise SystemExit('normalization fuel exhausted')
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


def reduce_capped(t, cap):
    """Reduce; return (state, exceeded_cap, terminated, terminal_above_cap).

    exceeded_cap marks that a non-terminal intermediate state exceeded the cap.
    A terminal normal form larger than the cap is reported as terminated with
    terminal_above_cap=True, not as a cap hit.
    """
    steps = 0
    while True:
        n = step(t)
        if n is None:
            return t, False, True, size(t) > cap
        if size(t) > cap:
            return t, True, False, False
        t = n
        steps += 1
        if steps > MAX_STEPS:
            raise SystemExit('reduction fuel exhausted')


def semantics_tests():
    """Known reductions and one capture-avoidance test for the normalizer."""
    checks = [
        ('I x -> x', norm(A(I, V(0))) == V(0)),
        ('K x y -> x', norm(A(A(K, V(0)), V(1))) == V(0)),
        ('S K K -> I', norm(A(A(S, K), K)) == L(V(0))),
        ('iota iota -> I', norm(A(IOTA, IOTA)) == L(V(0))),
        ('iota I -> F', norm(A(IOTA, I)) == L(L(V(0)))),
        ('iota K -> S', norm(A(IOTA, K)) == L(L(L(A(A(V(2), V(0)), A(V(1), V(0))))))),
        ('capture: K y -> lambda y. y with y free', norm(A(K, V(0))) == L(V(1))),
    ]
    for name, ok in checks:
        check('semantics: ' + name, ok)
    return len(checks)


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

    # independent brute-force enumeration of the trees for small n
    def all_trees(n):
        if n == 1:
            return [()]
        out = []
        for i in range(1, n):
            for l in all_trees(i):
                for r in all_trees(n - i):
                    out.append((l, r))
        return out

    def tree_term(t):
        if t == ():
            return IOTA
        return A(tree_term(t[0]), tree_term(t[1]))

    brute_checked = []
    for n in range(1, 8):
        c = Counter(norm(tree_term(t)) for t in all_trees(n))
        check('brute-force level %d matches the recursion' % n,
              dict(c) == counts[n], (n, len(c), len(counts[n])))
        brute_checked.append(n)

    # explosive n=14 pairs: b in S_13 with iota·b exceeding CAP
    explosive = []
    explosive_meta = {}
    for b in sorted(forms[13], key=term_key):
        state, hit, terminated, above_cap = reduce_capped(A(IOTA, b), CAP)
        if hit:
            explosive.append(b)
            explosive_meta[b] = {'cap': CAP, 'reduction_exceeded_cap': True,
                                 'terminated': False, 'state_size_at_cap': size(state)}
    check('two explosive forms at n=13', len(explosive) == 2, len(explosive))

    # the advertised n=14 two-sided bound: all root splits
    s14_forms = set()
    s14_hits = []
    s14_above = 0
    for i in range(1, 14):
        for a in sorted(forms[i], key=term_key):
            for b in sorted(forms[14 - i], key=term_key):
                state, hit, terminated, above_cap = reduce_capped(A(a, b), CAP)
                if hit:
                    s14_hits.append((i, a, b))
                else:
                    check('n=14 non-hit reduction terminates', terminated)
                    if above_cap:
                        s14_above += 1
                    s14_forms.add(state)
    check('n=14 non-hit forms = 128', len(s14_forms) == 128, len(s14_forms))
    check('n=14 non-hit terminal-above-cap = 0', s14_above == 0, s14_above)
    check('n=14 cap-hitting pairs = 2', len(s14_hits) == 2, len(s14_hits))
    check('n=14 hits are iota applied to the two explosive forms',
          all(i == 1 and a == IOTA for i, a, b in s14_hits)
          and {json.dumps(serialize(b)) for _, _, b in s14_hits} ==
              {json.dumps(serialize(b)) for b in explosive})
    s14 = {'nonhit_forms': len(s14_forms), 'cap_hits': len(s14_hits),
           'lower': len(s14_forms), 'upper': len(s14_forms) + len(s14_hits),
           'cap': CAP, 'nonhit_terminated': True,
           'nonhit_terminal_above_cap': s14_above,
           'cap_hit_splits': [{'split': [i, 14 - i], 'left': serialize(a),
                              'right': serialize(b), 'right_pretty': pretty(b)}
                              for i, a, b in s14_hits]}

    # the p·iota family and its size-52 sibling
    family = [f for f in sorted(forms[13], key=term_key)
              if any(norm(A(x, IOTA)) == f for x in forms[12])]
    check('p·iota image at n=13 has 28 distinct output forms',
          len(family) == 28, len(family))
    family_set = set(family)
    multiplicity = Counter()
    for x in forms[12]:
        out = norm(A(x, IOTA))
        if out in family_set:
            multiplicity[out] += 1
    check('every p maps into the image', sum(multiplicity.values()) == len(forms[12]),
          (sum(multiplicity.values()), len(forms[12])))
    sibling = next((f for f in family if size(f) == 52), None)
    check('p·iota image has a size-52 member', sibling is not None)
    _, sibling_hit, sibling_term, sibling_above = reduce_capped(A(IOTA, sibling), CAP)
    check('size-52 sibling stays below the cap',
          sibling_term and not sibling_hit and not sibling_above)
    family_info = {'distinct_output_forms': len(family),
                   'input_forms': len(forms[12]),
                   'multiplicity_min': min(multiplicity.values()),
                   'multiplicity_max': max(multiplicity.values()),
                   'sibling': {'pretty': pretty(sibling), 'size': size(sibling),
                               'cap_hit': sibling_hit,
                               'terminal_above_cap': sibling_above}}

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

    # lineage of the two explosive forms (sorted iteration, serialized lookup)
    lineage = []
    for b in explosive:
        parents = []
        for i in range(1, 13):
            for x in sorted(forms[i], key=term_key):
                for y in sorted(forms[13 - i], key=term_key):
                    if norm(A(x, y)) == b:
                        parents.append({'split': [i, 13 - i],
                                        'left': serialize(x), 'right': serialize(y),
                                        'left_pretty': pretty(x), 'right_pretty': pretty(y),
                                        'left_birth': birth[x], 'right_birth': birth[y]})
        grandparents = []
        for p in parents:
            i0 = p['split'][0]
            x = next(f for f in forms[i0] if serialize(f) == p['left'])
            for j in range(1, i0):
                for u in sorted(forms[j], key=term_key):
                    for v in sorted(forms[i0 - j], key=term_key):
                        if norm(A(u, v)) == x:
                            grandparents.append({'split': [j, i0 - j],
                                                 'left': serialize(u), 'right': serialize(v),
                                                 'left_pretty': pretty(u),
                                                 'right_pretty': pretty(v),
                                                 'left_birth': birth[u],
                                                 'right_birth': birth[v]})
        lineage.append({
            'form': pretty(b), 'size': size(b), 'arity': arity(b),
            'birth': birth[b], 'fiber_at_13': counts[13][b],
            'reduction_at_14': explosive_meta[b],
            'parents_at_13': parents,
            'parent_decompositions': grandparents,
        })

    ev = {
        'definitions': {
            'leaf': 'iota = lambda x. x S K',
            'tree': 'plane binary tree with n leaves, C_{n-1} of them',
            'form': 'beta-normal form of the closed lambda term (leaf = iota)',
            'fiber': 'number of n-leaf trees whose normal form is the given form',
            'birth': 'minimal leaf count at which the form appears',
            'arity': 'number of leading lambdas of the normal form',
            'explosive': 'form b at n=13 whose reduction of iota·b exceeds CAP=%d nodes; this does not assert a normal-form size' % CAP,
        },
        'summary': {
            's_n': expected_s,
            'catalan': [cat(n - 1) for n in range(1, MAX_N + 1)],
            'max_fiber': [max(counts[n].values()) for n in range(1, MAX_N + 1)],
        },
        'levels': levels,
        's14': s14,
        'p_iota_family': family_info,
        'brute_force_levels': brute_checked,
        'semantics_tests': {'passed': semantics_tests(),
                            'cases': ['I x -> x', 'K x y -> x', 'S K K -> I',
                                      'iota iota -> I', 'iota I -> F',
                                      'iota K -> S',
                                      'capture: K y -> lambda y. y with y free']},
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
