# K_n database: iota trees, their normal forms and their fibres

**Status:** computational evidence, 2026-11-12. Not a paper claim and not entered
in `governance/05` or `05c`; it is the finite database behind the discussion of
the \(K_n\) expansion.

## 1. What is in the database

For \(n=1,\dots,13\) the script `verify_normal_forms.py` enumerates the
\(C_{n-1}\) plane binary trees with \(n\) leaves, reads each as a closed
\(\lambda\)-term with one \(\iota=\lambda x.xSK\) per leaf, and records:

| field | meaning |
|---|---|
| `term` | the \(\beta\)-normal form in de Bruijn serialization |
| `pretty` | the same form in named notation (\(S,K,I,\iota\) recognised) |
| `arity` | number of leading lambdas of the normal form |
| `size` | number of nodes of the normal form |
| `birth` | smallest leaf count at which the form appears |
| `fiber` | number of \(n\)-leaf trees with this normal form |
| `witness` | one tree expression (parenthesized, `i` for \(\iota\)) with this form |

The enumeration is exact: it uses the congruence
\(\mathrm{nf}(AB)=\mathrm{nf}(\mathrm{nf}(A)\,\mathrm{nf}(B))\), so the forms at
level \(n\) are generated from the forms at smaller levels; the fibre counts are
carried along the same recursion and the totals reproduce \(C_{n-1}\). The
script asserts the sequence \(s_n=1,1,2,2,5,7,13,17,23,28,41,59,90\), the
Catalan totals, and the presence of exactly two forms at \(n=13\) whose
application to \(\iota\) exceeds the 20,000-node cap.

## 2. The table

\(s_n\) is the number of distinct \(\beta\)-normal forms; \(E_n\) is the Shannon
entropy (bits) of the fibre distribution, i.e. \(2^{E_n}\) is the effective
number of observation classes seen by a random tree.

| \(n\) | \(C_{n-1}\) | \(s_n\) | max fibre | \(E_n\) | arity distribution |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 0.000 | \(1{:}1\) |
| 2 | 1 | 1 | 1 | 0.000 | \(1{:}1\) |
| 3 | 2 | 2 | 1 | 1.000 | \(1{:}1,\ 2{:}1\) |
| 4 | 5 | 2 | 4 | 0.722 | \(1{:}1,\ 2{:}1\) |
| 5 | 14 | 5 | 6 | 1.870 | \(1{:}2,\ 2{:}2,\ 3{:}1\) |
| 6 | 42 | 7 | 27 | 1.669 | \(1{:}2,\ 2{:}4,\ 3{:}1\) |
| 7 | 132 | 13 | 46 | 2.486 | \(1{:}4,\ 2{:}7,\ 3{:}2\) |
| 8 | 429 | 17 | 231 | 2.231 | \(1{:}7,\ 2{:}7,\ 3{:}3\) |
| 9 | 1430 | 23 | 422 | 2.759 | \(1{:}11,\ 2{:}7,\ 3{:}4,\ 4{:}1\) |
| 10 | 4862 | 28 | 2292 | 2.530 | \(1{:}12,\ 2{:}8,\ 3{:}7,\ 4{:}1\) |
| 11 | 16796 | 41 | 4376 | 2.881 | \(1{:}14,\ 2{:}14,\ 3{:}10,\ 4{:}3\) |
| 12 | 58786 | 59 | 25147 | 2.704 | \(1{:}21,\ 2{:}22,\ 3{:}12,\ 4{:}4\) |
| 13 | 208012 | 90 | 60470 | 2.940 | \(1{:}38,\ 2{:}33,\ 3{:}13,\ 4{:}5,\ 5{:}1\) |

Two readings matter for the process-geometry discussion:

* the fibre distribution is very uneven: at \(n=13\) one form takes 60,470 of the
  208,012 trees, and \(2^{2.94}\approx 7.7\) effective classes cover the random
  tree, although 90 forms exist;
* the number of forms grows slowly compared with \(C_{n-1}\) (roughly
  \(1.4^n\) against \(4^n\)), so the observation quotient is a strong
  compression of the construction side.

## 3. The two explosive forms at \(n=13\)

At \(n=14\) the application \(\iota\cdot b\) of a 13-leaf form \(b\) to the leaf is
the only operation that can produce the two terms whose normal forms exceed
20,000 nodes (and also 80,000: the head reduction alone does not finish in
minutes). The two forms are:

\[
b_1=\lambda a.\,aSK\,(a(aSK)),\qquad
b_2=\lambda a.\,aSK\,(aSK)(aSK).
\]

| | \(b_1\) | \(b_2\) |
|---|---|---|
| size | 36 | 51 |
| arity | 1 | 1 |
| birth | 13 | 13 |
| fibre at \(n=13\) | 1 | 1 |
| witness | `(((i(i(i(ii))))((i(i(i(ii))))(ii)))i)` | `(((i(i(i(ii))))(((i(i(i(ii))))i)i))i)` |

Both are born at 13, have a unique tree, and are obtained by the same
two-step pattern:

\[
b_1 = p_1\cdot\iota,\quad p_1=S\cdot(\lambda a.\lambda b.\,b(ab)),
\]
\[
b_2 = p_2\cdot\iota,\quad p_2=S\cdot(\lambda a.\,aSK\,(aSK)).
\]

Here \(S\) has birth 5; the right factors \(\lambda a.\lambda b.b(ab)\) and
\(\lambda a.aSK(aSK)\) have birth 7 and are among the most frequent forms
(fibres 2,249 and 2,213 at \(n=13\)); the parents \(p_1,p_2\) have birth 12.
So \(b_1,b_2\) are second-generation self-application forms: an abundant
birth-7 form, composed with \(S\), then applied to \(\iota\).

This is not a size effect: the \(n=13\) family \(p\cdot\iota\) has 28 members,
including a size-52 sibling
\(\lambda a.\,aSK(\iota)(aSK)\) which is born at 13 with fibre 1 but whose
\(n=14\) application stays below the cap. Explosiveness is shape-specific, not
monotone in size or fibreness.

At \(n=14\) the exact count is bounded by \(128\le s_{14}\le 130\): all but the
two explosive pairs normalise below the 20,000-node cap and contribute 128
distinct forms; the remaining two contribute at most two more.

## 4. Reproduce

```bash
python3 research/iota-normal-forms/verify_normal_forms.py /tmp/nf.json
cmp /tmp/nf.json research/iota-normal-forms/evidence-normal-forms-v1.json
python3 -O research/iota-normal-forms/verify_normal_forms.py /tmp/nf-o.json
cmp /tmp/nf-o.json research/iota-normal-forms/evidence-normal-forms-v1.json
python3 research/iota-normal-forms/verify_normal_forms.py research/iota-normal-forms/evidence-normal-forms-v1.json --verify-evidence
```

The first command writes to `/tmp`; the committed evidence is never overwritten.
The calibration is same-author and has not had an independent human review.
