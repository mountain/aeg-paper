# F_7, PGL(2,7), PSL(2,7), and the Paper IV counts

**Status:** research scaffold v0.2, 2026-11-12. Not a paper claim, not a trial, not
a proof record. It records what the repository already says about
\(\mathbb F_7\), and the finite group-action correspondences that can be built on
top of Paper IV's calibration.

**One-line result.** As \(PSL_2(\mathbb F_7)\)-sets, the 56 regular bivaluations of
Paper IV are isomorphic to the 56 elements of order 3, the 8 projective points to
the 8 Sylow 7-subgroups, and the 21 Fano flags to the 21 involutions (the last
through the canonical Sylow-2 center map). The 42 ordered Fano pairs and the 42
elements of order 4 have the same size but are **not** isomorphic \(PSL\)-sets
(\(V_4\) against \(C_4\)).

---

## 1. What the repository already has on \(\mathbb F_7\)

Paper IV, `paper-4/sections/03-projective-quotients.tex`, Example
`ex:f7-counts`, and Appendix C:

\[
|\mathbb P^1(\mathbb F_7)|=8,\qquad
|\mathrm{Biv}^{\mathrm{reg}}_{\mathbb F_7}|=8\cdot 7=56,\qquad
|\mathrm{PGL}_2(\mathbb F_7)|=8\cdot7\cdot6=336.
\]

The 336 ordered projective frames condense to 56 ordered image--kernel pairs, with
six frame lifts above each pair. The cross-ratio holonomy example is
`ex:f7-cross-ratio-holonomy` in
`paper-4/sections/04-condensation-and-continuation.tex` (\(\Lambda(\square)=4\neq1\)
in \(\mathbb F_7^\times\)); the edge-by-edge transport version is
`ex:f7-edge-transports` in `paper-4/sections/04b-transport-density.tex`. Paper III
uses \(\mathbb F_7\) only as a residue field of a specialization
(`05-history-divisor-naturality.tex`, the point \((7,\sqrt2-3)\)), and Paper V's
appendix mentions a conjugacy choice over \(\mathbb F_7\).

Two existing pieces of work are closer than the papers: note 49,
`notes/analysis-and-calculus/49-conic-histories-and-finite-calculi.tex`,
the paragraph preceding Proposition `prop:commutant` records
\(|\mathrm{PGL}_2(\mathbb F_7)|=336\), and the proof of that proposition uses the
two-transitivity of \(\mathrm{PGL}_2(\mathbb F_7)\) on ordered pairs of distinct
lines;
`notes/analysis-and-calculus/finite-field-calculi/conic-dynamics/verify.py`
enumerates all 336 projective matrices over \(\mathbb F_7\) and checks covariance
against every one of them. **Paper IV's native group is \(\mathrm{PGL}_2(\mathbb
F_7)\); everything below is a restriction to the index-two subgroup
\(\mathrm{PSL}_2(\mathbb F_7)\).** Where the PGL statement is stronger, it is
recorded as well.

## 2. The two groups

\(\mathrm{PGL}_2(\mathbb F_7)\) has order 336 and conjugacy classes
\[
1,\ 21,\ 28,\ 56,\ 42,\ 56,\ 48,\ 42,\ 42
\]
(order 1, two involution classes, order 3, order 4, order 6, a single order-7
class, and two order-8 classes).

\(\mathrm{PSL}_2(\mathbb F_7)\) has order 168, is the index-two subgroup of
determinant-square matrices, and is isomorphic to \(GL(3,2)\), the automorphism
group of the Fano plane. Its classes are
\[
1,\quad 21,\quad 56,\quad 42,\quad 24,\quad 24,
\]
i.e. the identity, the involutions, the order-3 elements, the order-4 elements,
and the two inverse classes of order-7 elements. The Sylow counts are
\(n_2=21\), \(n_3=28\), \(n_7=8\).

## 3. Correspondences

The script `verify_psl27.py` builds both groups as permutations of
\(\mathbb P^1(\mathbb F_7)\), computes the classes, Sylow counts, stabilizers and
centralizers below, and checks the conjugacies on which the isomorphisms rest.
Its evidence is `evidence-psl27-v1.json`.

| AEG / combinatorial object | group object | status |
|---|---|---|
| the 8 projective points | the 8 Sylow 7-subgroups of \(PSL\) | both transitive; point stabilizer order 21 is conjugate to the Sylow-7 normalizer; isomorphic \(PSL\)-sets |
| the 56 regular bivaluations (ordered pairs of points) | the 56 order-3 elements (conjugation in \(PGL\) and in \(PSL\)) | \(PGL\) is 2-transitive on 8 points and its ordered-pair stabilizer has order 6, conjugate to the centralizer of an order-3 element; the same holds for \(PSL\) with order 3. Isomorphic sets in both groups |
| the 21 Fano flags | the 21 involutions / the 21 Sylow 2-subgroups | flag stabilizer is a Sylow 2 (order 8, element orders \(1,2^5,4^2\)); the Sylow 2-subgroups are \(D_8\), and \(S\mapsto z(S)\) (the unique nonidentity central involution) is a canonical bijection onto the 21 involutions, inverse to \(t\mapsto C_G(t)\); computed here |
| the 42 ordered Fano pairs | the 42 order-4 elements | same size only: the ordered-pair stabilizer is \(V_4\), while an order-4 element has centralizer \(C_4\); **not** isomorphic \(PSL\)-sets |
| the 24 heptagons of the Klein quartic | the 24 cosets of a Sylow 7-subgroup | classical; the two inverse order-7 classes are the two orientations |

The 42 row is a warning: equal cardinality does not imply a group-set
isomorphism, and here the stabilizers decide against it. The flags and the
involutions, by contrast, are canonically identified through the Sylow 2 centers,
so the two rows are genuinely different: the 21-row is an isomorphism of
\(PSL\)-sets with a canonical map, the 42-row is only a numerical coincidence.

## 4. The Klein quartic and the \((2,3,7)\) triangle

The Klein quartic carries two dual tilings, which must not be conflated:

* the \(\{3,7\}\) tiling has \(56\) triangular faces, \(84\) edges and \(24\)
  vertices;
* its dual \(\{7,3\}\) tiling has \(24\) heptagonal faces, \(84\) edges and \(56\)
  vertices.

The 56 \(\{3,7\}\) triangles form \(PSL_2(\mathbb F_7)/C_3\), matching the 56
order-3 elements; the 24 \(\{7,3\}\) heptagons form \(PSL_2(\mathbb F_7)/C_7\),
matching the 24 cosets of a Sylow 7-subgroup.

The surface has area \(4\pi(g-1)=8\pi\). Each \(\{3,7\}\) triangle therefore has
area \(\pi/7\). The \((2,3,7)\) *fundamental* triangle has area
\[
\pi-\left(\frac{\pi}{2}+\frac{\pi}{3}+\frac{\pi}{7}\right)=\frac{\pi}{42},
\]
and the closed surface contains \(8\pi/(\pi/42)=336\) such fundamental triangles.
The \((2,3,7)\)-triangle statement is not the same as the 56-triangle statement:
the 56 faces are the \(\{3,7\}\) tiles, while the 336 are the fundamental
\((2,3,7)\) triangles.

Precisely, the uniformization is
\[
X=\mathbb H^2/\ker\bigl(\Delta^+(2,3,7)\to PSL_2(\mathbb F_7)\bigr),
\]
where \(\Delta^+(2,3,7)\) is the *orientation-preserving* triangle group and the
kernel is the genus-3 surface group; the finite quotient acting on \(X\) is
\(PSL_2(\mathbb F_7)\).

This is the hyperbolic partner of the \((2,4,\infty)\) triangle of the \(q=4\)
Hecke group used in the frames note: both are triangle groups, but the
\((2,3,7)\) one is the Hurwitz case and gives a closed genus-3 surface, not an
annulus or a cone.

## 5. What is proved, what is classical, what is open

* **Computed here** (`COMPUTATIONALLY VERIFIED EXAMPLE`): the class multisets of
  both groups, the Sylow counts, 2-transitivity on the 8 points, the conjugacy of
  the ordered-pair stabilizer with a Sylow 3 (PSL) and with the order-3
  centralizer (PGL), the conjugacy of the point stabilizer with the Sylow-7
  normalizer, the \(V_4\) type of the Fano ordered-pair stabilizer, the \(C_4\)
  type of the order-4 centralizer, the flag stabilizer of order 8, and the 24
  cosets of a Sylow 7.
* **Classical:** \(PSL_2(\mathbb F_7)\cong GL(3,2)\); \(PGL_2(\mathbb F_7)\) is
  2-transitive on the conic (note 49, the paragraph and proof of
  `prop:commutant`); the Fano flag action and
  the Borel stabilizer; the Klein quartic and its dual \(\{3,7\}/\{7,3\}\) tilings;
  the Hurwitz bound.
* **Open:** a lift of the \(PSL\)-set isomorphisms to the AEG structures
  themselves (bivaluations, frame lifts, cross-ratio holonomy); and the precise
  meaning of a "PSL-compatible splitting" of the six frame lifts. On the last
  point: \(H\cap PSL_2(\mathbb F_7)\) has order 3, so the six lifts already split
  into two \(PSL\)-orbits of size 3; a \(PSL\)-equivariant section
  \(\mathrm{Biv}\to\mathrm{Frames}\) does not exist. If "splitting" means the
  two-orbit partition, it is automatic; if it means an equivariant section, it is
  impossible.

No claim here is entered in `governance/05` or `05c`; it is research scaffold.

## 6. Reproduce

```bash
python3 research/f7-psl27/verify_psl27.py research/f7-psl27/evidence-psl27-v1.json
python3 -O research/f7-psl27/verify_psl27.py /tmp/psl27-o.json
python3 research/f7-psl27/verify_psl27.py /tmp/psl27-n.json
cmp /tmp/psl27-o.json /tmp/psl27-n.json
python3 research/f7-psl27/verify_psl27.py research/f7-psl27/evidence-psl27-v1.json --verify-evidence
```

The script exits non-zero when any check fails, so the normal and `-O` runs must
agree byte for byte with the committed evidence. This calibration is
same-author and was checked with the codex-review scaffold; it has not had an
independent human review, and it should not be cited as one.
