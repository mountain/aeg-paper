# Conic motions, histories, and three finite calculi

This second note connects the existing finite trigonometry to Paper I's
projective arithmetic semantics. It proves an explicit elliptic history and
compares the differences on nonsplit, split, and unipotent orbits over F7.

The note contains proofs, not just finite experiments. Its principal results
are **proved with stated hypotheses** within the note; incorporation into the
AEG papers remains a proposal. The migration is recorded in AEG governance; no manuscript claim is changed.

| File | Content |
| --- | --- |
| [`49-conic-histories-and-finite-calculi.tex`](../../49-conic-histories-and-finite-calculi.tex) | Proofs, conventions, Paper I interface, open questions |
| [`49-conic-histories-and-finite-calculi.pdf`](../../49-conic-histories-and-finite-calculi.pdf) | Compiled article |
| `verify.py` | Exact checks using only the Python standard library |
| `build.sh` | Verification, three LaTeX passes, reference and layout checks |

Run `./build.sh`, or run `python3 verify.py` for the finite checks alone.
The build needs `pdflatex` and `rg`.

The four-step chronological word `(+2, reciprocal, ×2, +2)` acts as

\[
R(t)=\frac{t+3}{1-3t}=2+\frac{2}{t+2}
\]

and visits `0, 3, 1, 5, infinity, 2, 6, 4` in order. Its eighth power is the
projective identity, but its repeated ordinary domain is already empty after
seven copies. This preserves the distinction between a history, its operator,
its ordinary domain, and its endpoint.

The moving cycles have lengths 8 (nonsplit), 6 (split), and 7 (unipotent).
Over characteristic 7, the first two have Fourier eigenbases over F49 and F7
respectively; the third has a single nilpotent Jordan block, with the binomial
functions as an explicit basis. All three have the same zero-sum solvability
condition, but only the first two have unique zero-sum antiderivatives. The
seven-cycle admits no shift-equivariant linear choice of antiderivative.

The script checks matrix enumeration, all ordinary initial inputs, every
quotient-torus representative, full function-space bases, and covariance
against all 336 elements of PGL2(F7). The article also proves the real
projective flow `dt/dh = 1+t²` and the compactness obstruction to using the
existing regular-AES equation on a compact boundaryless manifold. Finite
verification does not replace those proofs.

This resource directory accompanies note 49 in the canonical AEG notes.
See [migration provenance](../README.md) for the source revision and scope.

The next research tasks are the general odd-q orbit comparison (translations
have order p, not q), retention of marked histories and domains within each
operator class, and a precise elliptic-AES definition. Gauss sums and local-field
trees are deferred until one of these tasks requires them.
