# From local frames to global blocks

**Status:** research note v0.1, 2026-11-01. Not a paper claim, not a trial, not a
proof record. It is scaffold for Paper VI
(`governance/00e-paper-VI-process-geometry-scope.md`) and for the octagon note in
`mountain/math-notes`.

**Question.** A local frame theory — the iota frame of Paper V and of the process
corpus — describes one chart, one cut, one slot. A global object is assembled from
many such pieces. How do the pieces hand over to one another, and what exactly does
a block construction generate? The occasion is the octagon construction of
`~/AEG/math-notes/octagons.tex`, with the guess that it (i) handles all hyperbolic
cases and (ii) is a universal combinatorial basis of the same kind as the iota
combinator.

**Verdict in one paragraph.** The octagon construction is an exact local-to-global
mechanism — a fundamental polygon with side pairings, i.e. an
$(\mathrm{PSL}_2(\mathbb R),\mathbb H^2)$-structure — but as stated it generates a
thin family: covers of a fixed genus-2 base with deck group $Z_{g-1}$. A dimension
count and a symmetry count rule out "all hyperbolic surfaces". The universal
version of the same mechanism replaces one octagon block by a pants block and the
cyclic deck gluing by arbitrary gluing along boundary geodesics; that is the
Fenchel--Nielsen description of the whole moduli space. On the second guess: at the
topological level polygon blocks and edge flips do generate, in a precise finitary
sense; at the hyperbolic-metric level the gluing coefficients are continuous, so the
assembly is not a finite combinator basis in the sense of SKI/iota.

---

## 1. What the octagon construction does

Let $S_2$ be a closed orientable genus-2 surface with fundamental group
$\Gamma_2=\langle A_1,B_1,A_2,B_2\mid [A_1,B_1][A_2,B_2]=1\rangle$, and let
$\phi:\Gamma_2\to Z_N$ be a surjective homomorphism. The cover
$S_g=\mathbb H^2/\ker\phi$ has degree $N$ and genus
$g=N+1$ by Euler characteristic: $\chi(S_g)=N\chi(S_2)=-2N$, so
$2-2g=-2N$.

Geometrically, take $N$ copies of an octagonal fundamental domain $P_2$ of $S_2$
and glue edge $e_i^j$ to $(e_k^{j+\phi(X)})^{-1}$ whenever $e_i$ is paired with
$e_k^{-1}$ by $X\in\Gamma_2$. With $P_2$ the regular hyperbolic octagon of angle
$\pi/4$ (the Bolza domain), the resulting $P_g^\star=\bigcup_j P_2^j$ satisfies the
Poincaré polygon conditions, so $S_g$ carries the pullback hyperbolic metric.

Three features of what has been constructed matter below.

1. **The base is fixed.** The construction takes $S_2$ and its octagon as given and
   produces its covers. It does not vary the conformal structure of the base inside
   the construction.
2. **The deck group acts.** $Z_N$ acts on $S_g$ by isometries of the pullback
   metric; this is a covering symmetry, not an accident of the example.
3. **The gluing datum is a cocycle.** The side pairings of the cover are the
   elements $\phi(X)\in Z_N$; consistency around a vertex is the statement that the
   relation word of $\Gamma_2$ maps to the identity of $Z_N$.

Status: `CLASSICAL` (covering theory, Euler characteristic, Poincaré polygon
theorem), with the note's construction as the instance.

## 2. Why the construction cannot be "all hyperbolic cases"

Write $\mathcal M_g$ for the moduli space of closed hyperbolic surfaces of genus
$g$; $\dim \mathcal M_g=6g-6$ for $g\ge 2$.

**Dimension.** The construction has two inputs: the base surface in
$\mathcal M_2$ (six real parameters) and a surjective
$\phi:\Gamma_2\to Z_{g-1}$ (finitely many choices). Its image in
$\mathcal M_g$ therefore has dimension at most $6$. For $g\ge 3$,
$6<6g-6$, so the image is a proper subset; the gap is $6g-12$ real dimensions.

**Symmetry.** Every surface produced carries the deck group $Z_{g-1}$ as a group
of isometries of the constructed metric. A generic point of $\mathcal M_g$ has
trivial isometry group, and a surface with a non-trivial isometry group is a proper
closed subset. This is an independent obstruction.

**Cover structure.** A degree-$(g-1)$ cover of a genus-2 surface is a cover of a
*fixed* base; not every $S_g$ admits such a cover at all, and among those that do
the metric is the pullback, not an arbitrary one.

The count is not a defect of the note: the note proves exactly what it states. What
fails is the strengthening of its scope.

Status: `PROVED` (dimension and symmetry counts, standard moduli theory).

## 3. The local-to-global bridge: developing map and holonomy

The correct general form of "local frame $\to$ global block" for hyperbolic
surfaces is the theory of $(\mathrm{PSL}_2(\mathbb R),\mathbb H^2)$-structures.

* A **local frame** is a chart $\varphi_i:U_i\to\mathbb H^2$ with the transition
  $\varphi_j\circ\varphi_i^{-1}$ in $\mathrm{PSL}_2(\mathbb R)$.
* A **developing map** $\mathrm{dev}:\widetilde S\to\mathbb H^2$ integrates the
  local frames; it is equivariant for a **holonomy**
  $\rho:\pi_1(S)\to\mathrm{PSL}_2(\mathbb R)$:
  $\mathrm{dev}(\gamma\cdot x)=\rho(\gamma)\,\mathrm{dev}(x)$.
* A **block** is a fundamental polygon or a subdomain with boundary; its side
  pairings are elements of $\mathrm{PSL}_2(\mathbb R)$, and the polygon relation
  is the cocycle identity for $\rho$.

The octagon construction is the special case in which the holonomy factors through
a finite deck group, $\rho=\iota\circ\phi$ with $\phi:\Gamma_2\to Z_N$; the gluing
rules of the note are precisely the side pairings induced by $\rho$. "Chunking" —
assembling a global object from blocks — is therefore not a different operation
from the local frame theory: it is the same developing data read on a presentation
of $\pi_1$. The consistency condition is always the cocycle identity on relation
words.

Status: `CLASSICAL` (Thurston's $(G,X)$-structures; Poincaré polygon theorem).

## 4. The universal version: pants blocks and Fenchel--Nielsen

Replace the single octagon block by a **pants block**: a pair of pants, i.e. a
sphere with three boundary geodesics. Every closed hyperbolic surface of genus
$g\ge 2$ admits a pants decomposition into $2g-2$ pairs of pants. Gluing two
boundary geodesics requires two real parameters, a length $\ell$ and a twist
$\tau\in\mathbb R/\ell\mathbb Z$; for a fixed pants decomposition and a marking,
the coordinates
\[
(\ell_1,\tau_1,\dots,\ell_{3g-3},\tau_{3g-3})\in
\mathbb R_{>0}^{3g-3}\times\mathbb R^{3g-3}
\]
give a real-analytic homeomorphism of Teichmüller space with
$\mathbb R^{6g-6}$ (Fenchel--Nielsen); moduli are the quotient by the mapping
class group, and the marked moduli space has dimension $6g-6$.

In this language the octagon construction is the special case

> one block type (octagon) + gluing only along the deck action + base fixed.

The universal local-to-global statement is instead

> pants blocks + arbitrary gluing along boundary geodesics + Fenchel--Nielsen
> parameters = all hyperbolic structures.

This is the precise sense in which "all hyperbolic cases" can be reached: by
changing the block and allowing arbitrary transitions, not by adding more copies of
one block.

Status: `CLASSICAL` (pants decomposition, Fenchel--Nielsen theorem).

## 5. Is it a universal combinatorial basis like iota?

The comparison must separate two levels.

**Topological level — a finitary generation exists.** Every closed orientable
surface has a polygon presentation. Any two triangulations of a surface are
connected by edge flips, and the flip graph is connected (Hatcher--Thurston);
equivalently, pants decompositions are connected by the moves of the
Hatcher--Thurston complex (Penner). In this sense block assembly has a finite
generator set and a normal-form-like calculus on *topological* data. That is a
genuine universality statement, and it is the closest analogue of "a universal
basis".

**Metric level — the coefficients are continuous.** For hyperbolic structures the
gluing data are lengths and twists, and no finite combinatorial alphabet encodes
them; the moduli space is a real manifold of positive dimension. A finite
combinator basis in the sense of SKI/iota would require a finite set of symbols and
a terminating reduction relation whose normal forms exhaust the objects. Pants
assembly has neither: it has continuous labels and a groupoid action, not a rewrite
system.

The honest summary is therefore:

| Claim | Status |
|---|---|
| The octagon construction handles all hyperbolic surfaces | **False as stated** (dimension and symmetry; it handles covers of a fixed genus-2 base) |
| The octagon construction is the local-to-global mechanism of a fundamental polygon with holonomy | **True / `CLASSICAL`** |
| Replacing octagons by pants blocks and allowing arbitrary gluing reaches all hyperbolic structures | **True / `CLASSICAL`** |
| Block assembly has a finitary topological generator set (edge flips) | **True / `CLASSICAL`** |
| Block assembly is a finite combinator basis in the SKI/iota sense | **False for the metric level; open at the topological level** |
| iota's arity-one local frames plus a gluing cocycle reproduce the hyperbolic block assembly | **`CONJECTURE`** (Paper VI programme; see §6) |

## 6. Relation to Paper VI and the iota carrier

Paper VI reads the iota carrier at one slot: arity one, a local frame at the place
where a program is filled. The present note says what a global block would have to
be:

* a **block** is an open program with holes (the process reading), or a polygon /
  pants domain with boundary (the geometric reading);
* a **frame at a slot** is the iota carrier at that hole;
* a **gluing datum** is an element of the structure group attached to the boundary,
  and consistency around a block complex is the cocycle identity;
* the **global object** is the associated bundle over the block complex, i.e. the
  surface together with its hyperbolic structure in the geometric case, and the
  composed process in the process case.

In this dictionary the octagon note supplies an explicit finite-group instance:
blocks are octagons, the structure group is $Z_N$, and the transition data are the
deck elements $\phi(X)$. The iota carrier supplies the local complex structure at a
slot (Paper V, §4), and the global assembly would be a discrete
$(G,X)$-structure whose structure group is generated by the local frames and the
gluing transitions.

What is missing, and therefore what the conjecture asserts, is that the process
side has a cocycle calculus with the same consistency condition, and that the
resulting discrete $(G,X)$-structures are rich enough to recover the classical
polygon presentations. This is exactly the kind of statement Paper VI currently
records as a programme rather than a theorem.

## 7. Falsifiers and next checks

1. **Universality falsifier (already available).** A dimension count: for $g\ge3$
   the image of the octagon construction has dimension at most $6$ inside
   $6g-6$. Any claim of "all hyperbolic cases" must fail this count.
2. **Symmetry falsifier.** A surface with trivial isometry group cannot be a
   non-trivial cover with deck symmetry.
3. **Block-calculus test.** For Paper VI: define composition of open programs with
   iota frames at holes and check whether the composition is associative up to a
   cocycle; if it is, the process side has the same shape as the geometric side.
4. **Coefficient test.** Decide whether the process-side gluing data are finite
   (combinatorial) or continuous (metric-like). The answer determines which of the
   two universality statements — topological or metric — the process side can
   support.

## 8. References and provenance

* `mountain/math-notes`, `octagons.tex` (the construction under discussion;
  authored by Mingli Yuan with Gemini, ChatGPT and DeepSeek).
* Paper V, §4 (`paper-5/sections/04-six-state-carrier.tex`) for the six-state
  carrier and the iota frame.
* Paper VI (`paper-6/`) for the process reading of slots and blocks.
* Classical: Poincaré polygon theorem; Thurston's $(G,X)$-structures; pants
  decomposition and Fenchel--Nielsen coordinates; Hatcher--Thurston and Penner on
  flips and the mapping class groupoid; Bolza surface.

No claim of this note is entered in `governance/05-mathematical-status.md`; it is
research scaffold, and any promotion would go through the Paper VI scope
(`00e`) and register (`05c`).
