# From local frames to global blocks

**Status:** research note v0.1, 2026-11-01. Not a paper claim, not a trial, not a
proof record. It is scaffold for the Paper VI draft and for the octagon note in
`mountain/math-notes`.

**Branch dependency.** This note is stacked on the Paper VI draft
(`agent/paper-6-process-geometry`, PR #22). The paths `paper-6/`,
`governance/00e-paper-VI-process-geometry-scope.md` and
`governance/05c-paper-VI-status-register.md` exist on that branch, not on `main`;
until PR #22 lands, they refer to that branch. The note itself makes no claim
inside Paper VI's scope.

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

Provenance: standard covering theory, Euler characteristic and the Poincaré polygon
theorem, with the note's construction as the instance; no new theorem is claimed.

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
*fixed* base; when such a cover exists, the metric is the pullback, not an arbitrary
one. Topological coverability is a separate question from the metric obstruction
above, and the dimension and symmetry counts already decide the metric question.

The count is not a defect of the note: the note proves exactly what it states. What
fails is the strengthening of its scope.

Provenance: elementary counts on standard moduli theory (Teichmüller dimension and
isometry groups); not a new theorem.

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

Two different data must not be conflated here. The hyperbolic structure on the
cover has a Fuchsian holonomy
$\rho_g:\pi_1(S_g)\to\mathrm{PSL}_2(\mathbb R)$, namely the restriction of the base
holonomy $\rho_2$ to $\ker\phi$; it does **not** factor through $Z_N$. The finite
group $Z_N$ is the cover's *deck monodromy*: it records which sheet is glued to
which, not the structure group of the geometric structure. The octagon note uses
both: the base octagon's side pairings are elements of
$\mathrm{PSL}_2(\mathbb R)$, while the rule that glues sheet $j$ to sheet
$j+\phi(X)$ uses the deck element $\phi(X)$.

"Chunking" — assembling a global object from blocks — is therefore the pair
(geometric side pairings, deck monodromy) read on a presentation of $\pi_1$; the
consistency condition on the geometric side is the cocycle identity for $\rho$, and
on the covering side it is the identity for $\phi$ on relation words. Keeping the
two groups apart is part of the content of the bridge.

Provenance: Thurston's $(G,X)$-structures and the Poincaré polygon theorem.

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

Provenance: pants decomposition and the Fenchel--Nielsen theorem (Wolpert for the
Weil--Petersson form; the coordinates are classical).

## 5. Is it a universal combinatorial basis like iota?

The comparison must separate two levels.

**Topological level — a connectivity statement.** Every closed orientable surface
has a polygon presentation. Any two triangulations of a fixed surface are connected
by edge flips, and the flip graph is connected (Hatcher--Thurston); equivalently,
pants decompositions are connected by the moves of the Hatcher--Thurston complex
(Penner). This is a connectivity theorem about presentations of a fixed surface. It
does not by itself produce a finite generating set for *block assembly*, nor a
normal-form calculus, nor the terminating reduction relation that the SKI/iota
comparison would need. The honest reading is: the topological layer has a
connectivity property in the right direction, not a demonstrated combinator basis.

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
| Replacing octagons by pants blocks and allowing arbitrary gluing reaches all closed orientable hyperbolic surfaces of genus $g\ge2$ | **Standard (Fenchel--Nielsen)** |
| Block assembly has a finitary topological generator set (edge flips) | **Not established**: flips give connectivity of triangulations, not a block basis |
| Block assembly is a finite combinator basis in the SKI/iota sense | **Not established** at either level; the metric level has continuous parameters |
| The iota carrier at a slot plus a gluing cocycle reproduces the hyperbolic block assembly | **Proposal / conjecture** (Paper VI programme, §6); no precise functor or cocycle calculus is constructed here |
| Every one-point basis is arity one, so the syntactic layer applies to all of them | **Standard** (Barendregt; Fokker; Goldberg) |
| The geometric frame transfers to an arbitrary one-point basis | **Open**: it requires a representation into the carrier, which the known constructions do not supply |

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


## 7. One-point bases: arity one is generic

The iota term is not the only single-term basis, and its arity-one shape is shared
by all of them. Two constructions make the point.

* **Barendregt's example.** A set $B$ is a basis for a set $W$ when every
  $M\in W$ is $\beta\eta$-equal to some term in the closure of $B$ under
  application. The term
  \[
  X\equiv\lambda x.xSK
  \]
  is a one-point basis for the $\lambda K$-combinators:
  $X(X(XX))\to_\beta K$ and $X(X(X(XX)))\to_\beta S$.
  This $X$ *is* the iota combinator of the process corpus; it consumes one
  argument and hands the argument to $S$ and $K$.  Note~40 distinguishes three
  different objects called iota: the six-state carrier (AEG $\iota$), the Adva
  iota frame ($J$), and this iota *combinator*; the present section is about the
  third, the syntactic basis.
* **Fokker (1992).** A single closed $\lambda$-expression generating all
  $\lambda$-expressions is constructed, with simplicity as the criterion; the
  abstract states the result is simpler than known single-combinator bases.
* **Goldberg (BRICS RS-01-35, 2001).** For every recursively enumerable set $S$
  of terms (possibly with constants and free variables) there is a single term
  $X$ with
  $X(\underbrace{X\cdots X}_{k+1})\to_\beta S_k$; the construction packages the
  enumeration into one term. The basis term is again a unary $\lambda$-term, and
  generation proceeds by self-application.

The consequence for the present note is a sharpening, not a weakening, of the
arity-one principle:

1. **Arity one is generic.** Every $\lambda$-term is unary at the head, and every
   one-point basis is arity one. What distinguishes bases is what they generate
   (combinators, all $\lambda$-terms, terms with constants), how they reduce, and
   whether they come with a carrier representation. "Arity one" alone therefore
   does not single out iota.
2. **The syntactic layer is basis-independent.** Slot occurrences, construction
   order, schedules and the canonical evaluation order are properties of the
   application tree. They apply unchanged to terms written in any one-point
   basis, because the tree is the same kind of object whatever the leaves are
   called.
3. **The geometric layer is basis-relative.** The six-state carrier, $\Omega$ and
   the chirality sign law are extra data. To obtain a frame from a basis $B$ one
   needs a representation $\rho_B$ of its term algebra into the carrier that
   respects application, $\rho_B(xy)=\rho_B(x)\rho_B(y)$, and sends the basis
   term to an element satisfying the frame identities. For $B=\iota$ such a
   reading is available (Paper V's carrier together with the note-40
   correspondence). For the Fokker and Goldberg terms the construction is a
   *syntactic packaging*; no representation into the carrier is supplied, and its
   existence is open.
4. **Basis-independence is up to translation.** Generation by self-application
   means the encoded term is not the source program; the induced order is the
   order of the encoding. Different one-point bases give different encodings,
   hence different trees, and no canonical cross-basis order is claimed.

This yields a checkable question for Paper VI:

> For which one-point bases $B$ does a representation
> $\rho_B:\mathrm{Term}(B)\to W$ exist that respects application and carries the
> frame identities of Paper V? The syntactic layer holds for all; the geometric
> layer holds exactly for those $B$.

The question is open, and it is the precise form of the guess that "any arity-one
basis fits the theory".

## 8. Falsifiers and next checks

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

## 9. References and provenance

* `mountain/math-notes`, `octagons.tex` (the construction under discussion;
  authored by Mingli Yuan with Gemini, ChatGPT and DeepSeek).
* Paper V, §4 (`paper-5/sections/04-six-state-carrier.tex`) for the six-state
  carrier only; the identification of that carrier with the Adva iota frame is the
  correspondence recorded in the carousel--iota overview note (note~40), not a
  claim of Paper V.
* Paper VI (`paper-6/`) for the process reading of slots and blocks.
* Classical: Poincaré polygon theorem; Thurston's $(G,X)$-structures; pants
  decomposition and Fenchel--Nielsen coordinates; Hatcher--Thurston and Penner on
  flips and the mapping class groupoid; Bolza surface.
* One-point bases: Barendregt, *The Lambda Calculus* (Definition 8.1.1 and the
  example $X\equiv\lambda x.xSK$); J. Fokker, "The systematic construction of a
  one-combinator basis for lambda-terms", *Formal Aspects of Computing* 4 (1992),
  doi:10.1007/BF03180572; M. Goldberg, "A general schema for constructing
  one-point bases in the lambda calculus", BRICS RS-01-35 (2001).

No claim of this note is entered in `governance/05-mathematical-status.md`; it is
research scaffold, and any promotion would go through the Paper VI scope
(`00e`) and register (`05c`).
