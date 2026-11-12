# F_7, PSL(2,7), and the Paper IV counts

**Status:** research note v0.1, 2026-11-12. Not a paper claim, not a trial, not a
proof record. It records what the repository already says about \(\mathbb F_7\),
and the finite group-action correspondences that can be built on top of Paper IV's
calibration.

**One-line result.** The 56 regular bivaluations of Paper IV are, as a
\(PSL_2(\mathbb F_7)\)-set, the 56 elements of order 3; the 8 projective points are
the 8 Sylow 7-subgroups; the 21 Fano flags are the 21 involutions. The 42 ordered
Fano pairs and the 42 elements of order 4 have the same size but different
stabilizers (\(V_4\) against \(C_4\)), so that one stays a numerical coincidence.

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
six frame lifts above each pair. Paper IV also computes a cross-ratio holonomy in
\(\mathbb F_7^\times\) (`04b-transport-density.tex`, the witness loop with
\(\Lambda(\square)=4\neq1\)). Paper III uses \(\mathbb F_7\) only as a residue field
of a specialization (`05-history-divisor-naturality.tex`, the point
\((7,\sqrt2-3)\)), and Paper V's appendix mentions a conjugacy choice over
\(\mathbb F_7\). No part of the repository discusses \(PSL_2(\mathbb F_7)\) as a
group.

## 2. The group

\(PSL_2(\mathbb F_7)\) has order \(168\), is the index-two subgroup of
\(\mathrm{PGL}_2(\mathbb F_7)\) (the determinant-square half), and is isomorphic to
\(GL(3,2)\), the automorphism group of the Fano plane. Its conjugacy classes are

\[
1,\quad 21,\quad 56,\quad 42,\quad 48
\]

for the identity, the involutions, the order-3 elements, the order-4 elements, and
the order-7 elements; the 48 order-7 elements split into two classes of 24 (the two
primitive directions). The Sylow counts are \(n_2=21\), \(n_3=28\), \(n_7=8\).

## 3. Correspondences

The script `verify_psl27.py` builds \(PSL_2(\mathbb F_7)\) as the permutations of
\(\mathbb P^1(\mathbb F_7)\) induced by \(SL_2(\mathbb F_7)\), computes the classes
and Sylow counts above, and checks the stabilizer conjugacies used below. Its
evidence is `evidence-psl27-v1.json`.

| AEG / combinatorial object | \(PSL_2(\mathbb F_7)\) object | status |
|---|---|---|
| the 8 projective points | the 8 Sylow 7-subgroups | both transitive; point stabilizer has order 21 and is conjugate to the normalizer of a Sylow 7; the two \(PSL\)-sets are isomorphic |
| the 56 regular bivaluations (ordered pairs of points) | the 56 elements of order 3 (conjugation) | \(PSL\) is 2-transitive on 8 points; the ordered-pair stabilizer is a \(C_3\) conjugate to a Sylow 3; the two \(PSL\)-sets are isomorphic |
| the 21 Fano flags | the 21 involutions (or the 21 Sylow 2-subgroups) | flag stabilizer is the Borel of order 8, a Sylow 2; an involution's centralizer is a Sylow 2; all Sylow 2-subgroups are conjugate, so the \(PSL\)-sets are isomorphic (classical \(GL(3,2)\) action) |
| the 42 ordered Fano pairs | the 42 order-4 elements | same size only: the ordered-pair stabilizer is \(V_4\), while an order-4 element has centralizer \(C_4\); **not** isomorphic as \(PSL\)-sets |
| the 24 heptagons of the Klein quartic | the 24 cosets of a Sylow 7-subgroup | classical; the two classes of order-7 elements of size 24 are the two orientations |
| the 42 six-leaf \(\iota\)-trees (\(K_6\)) | 42 order-4 elements / ordered Fano pairs | numerical only; no natural action is constructed |

Two remarks on the table. First, the 56-row is the substantive one for AEG: it
upgrades Paper IV's bivaluation count from a number to a transitive
\(PSL_2(\mathbb F_7)\)-set, and identifies it with a conjugacy class of the group.
Second, the 42-row is a warning: equal cardinality does not imply a group-set
isomorphism, and here the stabilizers decide against it. The same caution applies
to the 42 \(K_6\) trees: they coincide in number, but nothing here gives them a
\(PSL_2(\mathbb F_7)\)-action.

## 4. The Klein quartic and the \((2,3,7)\) triangle

\(PSL_2(\mathbb F_7)\) is the Hurwitz group of genus \(3\):
\(168=84(g-1)\), and the Klein quartic \(X=\mathbb H^2/\ker\) for a quotient
\((2,3,7)\)-triangle group \(\to PSL_2(\mathbb F_7)\) carries the \(\{3,7\}\) tiling
with \(24\) heptagons, \(56\) triangles and \(84\) edges.

The hyperbolic numbers line up with the group-set table:

* the \((2,3,7)\) triangle has area \(\pi-( \pi/2+\pi/3+\pi/7)=\pi/42\);
* the orientation-preserving \((2,3,7)\) orbifold has area \(\pi/21\);
* the Klein quartic has area \(4\pi(g-1)=8\pi=168\cdot(\pi/21)\);
* the 56 triangles match the 56 order-3 elements; the 24 heptagons match the 24
  cosets of a Sylow 7; the 168 automorphisms are the group.

This is the hyperbolic partner of the \((2,4,\infty)\) triangle of the \(q=4\)
Hecke group used in the frames note: both are triangle groups, but the
\((2,3,7)\) one is the Hurwitz case and produces a closed genus-3 surface rather
than an annulus or a cone.

## 5. What is proved, what is classical, what is open

* **Computed here** (`COMPUTATIONALLY VERIFIED EXAMPLE`): the class sizes, the
  Sylow counts, 2-transitivity on the 8 points, the conjugacy of the ordered-pair
  stabilizer with a Sylow 3, the conjugacy of the point stabilizer with the Sylow-7
  normalizer, the \(V_4\) type of the Fano ordered-pair stabilizer, and the 24
  cosets of a Sylow 7.
* **Classical:** \(PSL_2(\mathbb F_7)\cong GL(3,2)\); the Fano flags are the Borel
  cosets; the Klein quartic and its \(\{3,7\}\) tiling; the Hurwitz bound.
* **Open:** a natural \(PSL_2(\mathbb F_7)\)-action on the 42 six-leaf
  \(\iota\)-trees; a lift of the \(PSL\)-set isomorphisms to the AEG structures
  themselves (bivaluations, frame lifts, cross-ratio holonomy); whether the
  56 bivaluations' six frame lifts admit a \(PSL\)-compatible splitting.

No claim here is entered in `governance/05` or `05c`; it is research scaffold.
