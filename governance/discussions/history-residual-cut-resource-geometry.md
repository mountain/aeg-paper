# History–Residual–Cut: From Projective Condensation to Resource Geometry

**File:** <code>governance/discussions/history-residual-cut-resource-geometry.md</code>  
**Status:** Working research note  
**Version:** 1.0  
**Date:** 2026-08-06  
**Discussion period:** 2026-07-28–2026-08-06  
**Primary topic:** A History–Residual–Cut framework for quotient information, representation, and computational resources in AEG  
**Primary paper interface:** PAPER_IV  
**Relevant theorem nodes:** Paper IV imports <code>S3</code>, <code>S4</code>, <code>P2</code>, <code>T2</code>, <code>P3</code>, <code>T3</code>, <code>T4</code>, <code>A3</code>, <code>G1</code>, <code>T12</code>; conditional model inputs <code>E2</code>, <code>T6</code>, <code>E3</code>; candidate comparison nodes <code>K1</code>, <code>T15</code>, <code>K3</code>, <code>T17</code>; all HRC and network nodes below are unregistered candidates  
**Authority:** Subordinate to <code>governance/00–08</code>; not itself authoritative

> This note condenses a research discussion into a reusable working document.
> It contains intermediate ideas, rejected formulations, and open questions.
> When it conflicts with the authoritative restructuring files, the latter
> prevail.

## 1. Executive summary

The discussion asks whether AEG can place representation complexity, running
time, memory, rewriting cost, and process information inside one reusable
framework.  It began from bilateral projective condensation, noncommutative
history growth, and fast multiplication by FFT or NTT.  The strongest initial
intuition was that concept complexity, representation complexity, and
time–space complexity might be different measurements of one underlying
geometric object.

The current conclusion is narrower:

\[
\boxed{
\begin{aligned}
\text{continuation residuals}&\text{ give semantic distinguishability},\\
\text{live configurations}&\text{ give operational resource use},\\
\text{rewrite fibers}&\text{ organize equivalent realizations}.
\end{aligned}
}
\]

These three layers are related, but they are not identical.  A past state
induces a residual only relative to a declared interface, class of legal
future continuations, and observable.  The number of residual classes gives a
finite information lower bound on any exact online state.  Actual memory and
time depend on a machine model that specifies how residuals are encoded,
materialized, erased, communicated, and recomputed.  Equivalent realizations
form a separate rewrite fiber, with its own distance and filling questions.

This is the corrected **History–Residual–Cut** framework.  Its decisive
revision is that a monotone down-set of completed DAG nodes is not an
execution state: it cannot record deletion or recomputation.  A resource
theory must use a trace of live configurations with explicit
compute/erase/recompute actions.

Several finite statements survive the revision.  Binary Horner histories of
fixed length and ACS charge have an exactly countable set of distinct operator
images.  A radix-2 butterfly admits an exact factorization in
\(\operatorname{GL}_2(K)\), and after projectivization all twiddle variants
occupy one left coset of a diagonal torus, equivalently one orbit of the
right \(H\)-action.  Matrix-chain costs and the
telescoping obstruction for endpoint-potential rewrite labels are elementary
and exact.  The OBDD equality example shows that commuting restrictions may
still exhibit an exponential cut-order gap.

None of these results proves a general complexity theorem.  Raw history
growth can be compressed by shared quotient structure; noncommutativity does
not force exponential growth; hyperbolicity does not imply hardness; and a
local \(2\times2\) butterfly identity does not by itself turn the
\(\operatorname{GL}_N\) FFT network into AEG.

Paper IV owns the framework and the case studies.  Paper I supplies marked
histories, projective evaluation, affine cocycles, ACS, and contact geometry,
but must contain no complexity conclusion.  Paper II owns the affine–Appell
analytic family.  The next blocking step is a finite definition package:
contextual residual equivalence, live-configuration execution, and one
fixed-model counting theorem, followed by the Horner and OBDD calibrations.

## 2. Starting intuition

The first motivating example was fast multiplication.  Fourier methods do not
perform dense convolution more quickly in the original coordinates.  They
move to a representation in which convolution becomes pointwise
multiplication and then return.  This suggested:

\[
\text{fast algorithm}
\approx
\text{low-cost representation change}
+
\text{sparse core operator}.
\]

The bilateral projective note supplied a second ingredient:

\[
\mathsf{Hist}
\longrightarrow
G
\longrightarrow
G/H
\longrightarrow
G/B.
\]

Each map forgets process information.  The fiber above a condensed result
therefore appeared to be a possible home for representation complexity, while
the principal \(H\)-torsor \(G\to G/H\) suggested a decomposition into a
quotient-level skeleton and a frame-valued residue.

A third ingredient came from AEG's affine flow.  Ordered additive and
multiplicative operations retain positional information, and the number of
ordered histories can grow exponentially.  Hyperbolic volume also grows
exponentially with radius.  It was therefore tempting to propose:

\[
\text{noncommutative history growth}
\longleftrightarrow
\text{hyperbolic volume growth}
\longleftrightarrow
\text{representation complexity}.
\]

The intended payoff was a unified account of:

- why preserving a process consumes space;
- why recovering a discarded process consumes time;
- why changing basis can shorten an algorithm;
- why quotienting histories creates both compression and reconstruction cost.

At that stage, the following implications had not been proved:

- distinct histories remain distinguishable to all relevant futures;
- large history fibers have no compact shared representation;
- noncommutativity forces exponential representation growth;
- logarithmic geometric volume equals machine memory;
- a path metric is comparable to runtime without a simulation theorem;
- the \(H\)-coordinate in \(G\to G/H\) is canonical;
- one-wire projective AEG already supplies a multi-wire network semantics;
- time and space are one scalar rather than tradeoff coordinates.

The discussion preserved the strategic intuition while rejecting these
unconditional implications.  It moved from “history volume” to contextual
future residuals, and then separated semantic lower bounds from operational
realizations.

## 3. Objects and notation

### 3.1 Three layers

| Layer | Object | Meaning | Current status | Paper owner |
| --- | --- | --- | --- | --- |
| semantic | \(\mathsf{Hist}\), \(\rho\), continuation class, observable | What past distinctions can still affect a legal future? | STRUCTURAL PROPOSAL beyond established spinal/projective inputs | Paper IV |
| operational | machine \(\mathcal M\), live configuration \(L_t\), action trace \(\sigma\) | What is actually stored and executed? | STRUCTURAL PROPOSAL with standard external models | Paper IV |
| rewrite | fiber \(\rho^{-1}(F)\), rewrite relation \(\mathcal R\), 2-cells | How are semantically equivalent realizations connected? | STRUCTURAL PROPOSAL | Paper IV or later relation theory |

The authoritative **projective process residue** and the new
**continuation residual** must remain distinct:

| Term | Provisional meaning | Warning |
| --- | --- | --- |
| projective process residue | information in an \(H\)-lift or related fiber after \(G\to G/H\) | An \(H\)-coordinate needs a reference lift or section. |
| continuation residual | equivalence class of pasts indistinguishable by a declared class of futures | It depends on interface, future class, domains, and observable. |

No theorem currently identifies one with the other.

### 3.2 Semantic objects

| Notation | Meaning | Status and notes |
| --- | --- | --- |
| \(\mathsf{Hist}\) | History category or groupoid | STRUCTURAL PROPOSAL beyond Paper I's marked spinal core; OQ-047 and OQ-048 remain open. |
| \(\rho:\mathsf{Hist}\to\mathsf{Sem}\) | Evaluation functor into a declared semantic category | Projective evaluation is established; one universal codomain is not. |
| \(\mathcal F_F=\{\Gamma:\rho(\Gamma)=F\}\) | Evaluation fiber of realizations of \(F\) | Definition once \(\rho\) is fixed; cardinality is not complexity by itself. |
| \(C\) | Typed causal interface or cut | STRUCTURAL PROPOSAL; not merely an ever-completed node set. |
| \(\mathsf{Cont}(C)\) | Declared legal future continuations from \(C\) | Must include ordinary/projective domain rules. |
| \(\operatorname{Obs}(p;\eta)\) | Observable behavior after past \(p\) and continuation \(\eta\) | May be a value, distribution, trace, or accept/reject result. |
| \(p\equiv_Cp'\) | Contextual residual equivalence | STRUCTURAL PROPOSAL; see §4.7. |
| \(\mathcal R_C=P_C/{\equiv_C}\) | Continuation-residual space | May be finite, infinite, topological, or measurable. |
| \(V_C=|\mathcal R_C|\) | Residual cardinality in a finite model | Does not equal data-structure size. |
| \(H_C=\lceil\log_2V_C\rceil\) | Exact online state-selection lower bound | STANDARD CONSEQUENCE under finite deterministic exact semantics. |

### 3.3 Operational objects

An operational execution is provisionally a legal action sequence

\[
\sigma:
L_0
\xrightarrow{a_1}
L_1
\xrightarrow{a_2}
\cdots
\xrightarrow{a_T}
L_T,
\]

where actions may include computation, erasure, recomputation, communication,
or checkpoint operations.

| Notation | Meaning | Status and notes |
| --- | --- | --- |
| \(L_t\) | Current live configuration | May contain wire values, tensors, checkpoints, clauses, or machine states. |
| \(S_\sigma(t)=\operatorname{size}_{\mathcal M}(L_t)\) | Materialized workspace at time \(t\) | Encoding- and machine-dependent. |
| \(S_{\max}=\max_tS_\sigma(t)\) | Peak materialized workspace | Not determined by an ever-completed down-set. |
| \(\operatorname{ST}=\sum_t S_\sigma(t)\) | Discrete memory-time integral | Depends on time discretization and what is charged. |
| \(W\) | Weighted work or total action cost | Gate, field-operation, bit-operation, or proof-step model must be stated. |
| \(T\) | Scheduled makespan or step count | Must not be conflated with intrinsic depth. |
| \(D_{\mathrm{caus}}\) | Causal or circuit depth | A property of a network relative to a parallel model. |
| \(Q\) | Communication or I/O | Requires a memory or processor topology. |
| \(L_{\mathrm{desc}}\) | Static description size | Includes program, circuit, constants, or tables according to convention. |

### 3.4 Four representation quantities

The discussion initially mixed four different quantities.  The corrected
distinction is:

| Quantity | Question |
| --- | --- |
| residual cardinality \(V_C\) | How many semantic future behaviors remain distinguishable? |
| online state width \(H_C\) | How many bits are needed to identify the current residual class? |
| materialized workspace \(S_\sigma(t)\) | How large is the object actually held during this run? |
| static representation size | How large is the OBDD, e-graph, circuit, program, or transition table representing a family of runs? |

For a boundary with \(w\) indices of dimension \(d\), \(w\log_2d\) bits encode
one index tuple.  They do not encode an arbitrary boundary tensor.  If the
tensor has

\[
D_C=\prod_{e\in\partial C}d_e
\]

entries over \(\mathbb F_q\), a dense materialization uses \(D_C\) field
elements and has \(q^{D_C}\) possible values.  Its full state-selection
information can therefore be \(D_C\log_2q\), not \(w\log_2d\).

### 3.5 Projective and network notation

| Notation | Meaning | Status and notes |
| --- | --- | --- |
| \(G=\operatorname{PGL}_2(K)\) | Projective group for one-hole bilateral arithmetic | PROVED WITH STATED HYPOTHESES as an AEG input. |
| \(H<G\) | Stabilizer of an ordered distinct point pair | Its coordinate depends on a chosen lift. |
| \(\mathsf B_\omega\) | Local radix-2 butterfly in \(\operatorname{GL}_2(K)\) | A two-wire linear gate, not a one-hole Möbius context. |
| \(\operatorname{NetHist}\) | Proposed multi-wire symmetric monoidal category or PROP | STRUCTURAL PROPOSAL; needed before “Network AEG” is a theorem. |
| \(B_n(a,v)\) | Affine–Appell family \(e^{-n\widetilde v}a^n\) | PARTIALLY PROVED as an algebraically stable family; owned by Paper II. |
| \(\mathcal K_g\) | Gaussian curvature of a selected model | Replaces ambiguous use of \(K\), which remains the base field. |
| \(\Omega_{\mathrm{coeff}}=\mu\lambda\) | Coefficient of the Paper I affine contact bracket | Not a general information curvature. |

## 4. Development of the argument

### 4.1 Complexity belongs to realizations, not endpoints alone

A computation passes through several equality levels:

\[
\text{marked trace}
\longrightarrow
\text{factorized network}
\longrightarrow
\text{operator or tensor}
\longrightarrow
\text{function or endpoint}.
\]

Two histories may share an endpoint but induce different operators.  Two
factorizations may induce the same operator but create different intermediate
objects.  Two schedules may execute the same network with different live
configurations.  A complexity statement must therefore specify:

\[
\text{semantic target}
+
\text{admissible realization fiber}
+
\text{operational model}
+
\text{schedule}.
\]

This agrees with the established projective forgetful tower

\[
\text{marked history}
\to
G
\to
G/H
\to
G/B,
\]

but does not prove that every computational quotient has this group form.
The tower is an algebraic prototype for information-forgetting maps.

### 4.2 From spinal histories to multi-wire networks

Paper I's marked spinal history has one evolving accumulator.  FFT, tensor
contraction, automatic differentiation, and proof DAGs have multiple inputs,
fan-out, merging, and shared subcomputations.  The discussion therefore
proposed an extension

\[
\mathsf{Hist}_{\mathrm{spinal}}
\hookrightarrow
\operatorname{NetHist},
\]

where objects are wire arities or typed interfaces and morphisms are networks
of local gates.

At minimum, this extension requires:

- ports and types;
- local gate semantics;
- tensor or parallel composition;
- sequential gluing;
- an evaluation functor to maps \(K^m\to K^n\);
- a schedule semantics;
- a restriction theorem recovering marked spinal histories.

Without these data, a \(2\times2\) matrix coincidence between a butterfly and
\(\operatorname{PGL}_2\) arithmetic is suggestive but not a categorical
identification.

### 4.3 The first cut model and its failure

The discussion first represented a schedule by down-closed sets

\[
\varnothing=I_0\subset I_1\subset\cdots\subset I_T=V(\Gamma)
\]

and a live frontier

\[
L_\Gamma(I)
=
\{u\in I:
\text{a value from }u\text{ is still needed by }V\setminus I\}.
\]

For a no-recomputation, node-value model, this gives the useful provisional
definitions

\[
S_\Gamma(I)
=
\sum_{u\in L_\Gamma(I)}b(u),
\]

\[
S_{\max}
=
\max_tS_\Gamma(I_t),
\qquad
\operatorname{ST}
=
\sum_tS_\Gamma(I_t).
\]

These formulas remain valid for the stated restricted model.  They do not
describe checkpointing or pebbling, because \(I_t\) cannot say whether a
previous value is still stored, has been erased, or is later recomputed.

The corrected operational object is the live-configuration trace

\[
L_0\to L_1\to\cdots\to L_T
\]

with explicit actions.  A down-set may still record causal progress or a
logical interface, but actual space is computed from \(L_t\), not \(I_t\)
alone.

### 4.4 Binary Horner histories and ACS condensation

Work over \(\mathbb Z\), or over a field \(K\) of characteristic zero.  For
\(b_i\in\{0,1\}\), let

\[
h_{b_i}(x)=2x+b_i.
\]

A length-\(n\) chronological word \(b=(b_1,\ldots,b_n)\) evaluates to

\[
\rho(b)(x)
=
h_{b_n}\circ\cdots\circ h_{b_1}(x)
=
2^nx+\sum_{i=1}^{n}2^{n-i}b_i.
\]

If exactly \(m\) digits equal \(1\), every word has ACS charge

\[
\chi(b)=(m,n\ln2).
\]

There are exactly \(\binom nm\) such words, and binary uniqueness makes their
evaluated affine operators distinct:

\[
\left|
\rho\bigl(\chi^{-1}(m,n\ln2)\bigr)
\right|
=
\binom nm.
\]

Thus this is the size of the **operator image of a charge fiber**, not the
size of a fiber of \(\rho\).  Under the uniform distribution on that finite
set, the lost charge-conditioned information is

\[
\log_2\binom nm.
\]

Writing \(p_n=m/n\), Stirling's formula gives

\[
\log_2\binom nm
=
nH_2(p_n)+O(\log n).
\]

In particular, if \(p_n\to p\in(0,1)\), then
\(\log_2\binom nm=nH_2(p)+o(n)\).  The exact count illustrates information
discarded by ACS abelianization.  It does not imply a general runtime or
memory lower bound.

### 4.5 The butterfly torus-coset lemma

Let \(K\) be a field with \(\operatorname{char}K\ne2\), and let
\(\omega\in K^\times\).  Define in \(\operatorname{GL}_2(K)\):

\[
\mathsf B_\omega
=
\begin{pmatrix}
1&\omega\\
1&-\omega
\end{pmatrix},
\qquad
\mathsf B_1
=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
D_\omega
=
\begin{pmatrix}
1&0\\
0&\omega
\end{pmatrix}.
\]

Their determinants are

\[
\det(\mathsf B_\omega)=-2\omega,
\qquad
\det(\mathsf B_1)=-2,
\qquad
\det(D_\omega)=\omega,
\]

so the stated characteristic and nonzero-twiddle hypotheses make all three
matrices invertible.  Direct multiplication gives

\[
\mathsf B_\omega=\mathsf B_1D_\omega.
\]

After projectivization, let \(H\) be the diagonal stabilizer of the ordered
pair \((0,\infty)\).  Since \(D_\omega\in H\),

\[
\mathsf B_\omega H=\mathsf B_1H
\]

for left cosets in \(\operatorname{PGL}_2(K)/H\), equivalently for orbits of
the right \(H\)-action.

This is an exact local linear-algebra statement.  It does not yet prove:

- that the two-wire gate is a one-hole Möbius arithmetic context;
- that a full FFT network is an AEG history;
- that \(D_\omega\) is a canonical process residue;
- that the torus labels define a connection or holonomy.

The safe provisional description is “common torus coset plus a
lift-dependent twiddle label.”

### 4.6 The finite \(\mathbb F_{257}\) NTT calibration

Choose

\[
K=\mathbb F_{257},
\qquad
N\in\{8,16\}.
\]

Because \(N\mid256\), \(K^\times\) contains primitive \(N\)-th roots.  A
fixed breadth-first radix-2 NTT network has

\[
D_{\mathrm{net}}=\log_2N
\]

synchronous butterfly layers and

\[
W_{\mathrm{cell}}
=
\frac N2\log_2N
\]

butterfly cells.

If every layer is invertible and inputs range over \(K^N\), the reachable
layer-state set has cardinality \(q^N\), \(q=257\), and therefore

\[
\log_2|\text{reachable layer states}|
=
N\log_2q.
\]

This is a logarithmic cardinality, and under a uniform input it is Shannon
entropy.  A simple fixed-width binary encoding instead uses

\[
N\lceil\log_2q\rceil=9N
\]

bits.  The two quantities must not be called the same “exact bit size.”

If one time unit is charged per layer, only the \(N\) inter-layer wire values
are counted, and input/output extras, gate-local temporaries, constants, and
communication are excluded, then the information-volume convention is

\[
\operatorname{ST}_{\log}
=
N\log_2N\log_2q.
\]

For \(N=8\), the network has \(12\) cells and \(3\) layers.  These are exact
network counts under the chosen topology.

The full diagonal torus in \(\operatorname{PGL}_2(\mathbb F_{257})\) has
\(256\) elements, hence eight bits of general fiber cardinality.  But an
\(N\)-point NTT uses labels only in \(\mu_N\), giving at most three or four
bits of choice for \(N=8\) or \(16\).  More importantly, in a fixed transform
the twiddles are static algorithm constants, not dynamic input-state entropy.
They belong to the program description, a constant table, or an on-demand
generation procedure.

The proposed experiment compares:

\[
\text{stored twiddle table},
\qquad
\text{primitive root plus exponent table},
\qquad
\text{on-demand recurrence}.
\]

Only after static and dynamic resources are separated may this example test a
storage–reconstruction tradeoff.

### 4.7 Contextual continuation residuals

Fix:

- a typed interface \(C\);
- a set \(P_C\) of admissible past states reaching \(C\);
- a common continuation class \(\mathsf{Cont}(C)\);
- an observable \(\operatorname{Obs}\);
- a convention for undefined or inadmissible continuations.

Define provisionally

\[
p\equiv_Cp'
\quad\Longleftrightarrow\quad
\forall\eta\in\mathsf{Cont}(C),\;
\operatorname{Obs}(p;\eta)
=
\operatorname{Obs}(p';\eta).
\]

Then

\[
\mathcal R_C=P_C/{\equiv_C}
\]

is the contextual continuation-residual space.

For finite, deterministic, exact semantics, any online machine state that
supports every continuation must distinguish different residual classes.
Therefore

\[
S_{\mathrm{online}}(C)
\ge
H_C
:=
\left\lceil
\log_2|\mathcal R_C|
\right\rceil.
\]

If \(S_\sigma(t)\) is measured in bits, includes a complete exact online
state at \(C_t\), and one snapshot is charged at every discrete step, then

\[
\operatorname{ST}
\ge
\sum_tH_{C_t}.
\]

Consequently, lower bounds

\[
|\mathcal R_{C_t}|\ge ct^d,
\qquad c>0,\ d>0,
\]

for all sufficiently large \(t\) give

\[
\operatorname{ST}(T)=\Omega(T\log T),
\]

while

\[
|\mathcal R_{C_t}|\ge ca^t,
\qquad c>0,\ a>1,
\]

give

\[
\operatorname{ST}(T)=\Omega(T^2).
\]

The conclusions are lower bounds only.  Corresponding \(\Theta\) statements
require matching upper bounds and the same time discretization.

Residuals are contextual.  With one fixed tensor-network future, two distinct
boundary tensors may be identified if their difference lies in the future
kernel.  If every compatible future tensor is allowed as a test, residual
equivalence may reduce to tensor equality.  There is no absolute residual
attached to a cut without the continuation and observable data.

### 4.8 From semantic lower bound to operational realization

The semantic lower bound does not determine actual workspace.  An operational
model must fix:

- an input family \(F_n\), not merely one hard-codeable finite function;
- a machine, circuit, proof system, or network language;
- uniformity and allowed preprocessing;
- value and program encodings;
- exact, randomized, or approximate semantics;
- atomic actions and their costs;
- live-configuration legality;
- whether constants, tables, input, and output count toward space.

For one realization and trace, define provisionally:

\[
\mathbf C_{\mathcal M}(\Gamma,\sigma)
=
\bigl(
L_{\mathrm{desc}},
W,
T,
D_{\mathrm{caus}},
S_{\max},
\operatorname{ST},
Q
\bigr).
\]

For an input family \(F=(F_n)_{n\ge1}\), let

\[
\operatorname{Adm}^{\mathrm{unif}}_{\mathcal M}(F)
\]

denote the implementation families
\(((\Gamma_n,\sigma_n))_{n\ge1}\) produced by one declared uniform
constructor and satisfying \(\rho(\Gamma_n)=F_n\) for every \(n\).  The
candidate fixed-size slice is then the nondominated achievable set

\[
\mathfrak C^{\mathrm{unif}}_{\mathcal M}(F;n)
=
\operatorname{Pareto}
\left\{
\mathbf C_{\mathcal M}(\Gamma_n,\sigma_n):
((\Gamma_j,\sigma_j))_{j\ge1}
\in
\operatorname{Adm}^{\mathrm{unif}}_{\mathcal M}(F)
\right\}.
\]

If the set is not closed or optima are not attained, its closure may be the
appropriate object.  This remains a STRUCTURAL PROPOSAL.  Taking each
\(\Gamma_n\) independently would define a nonuniform slice and reintroduce
hardcoding; it is not the default here.  A single finite \(F\) is useful as a
calibration but is generally insufficient for complexity theory.

Rewrite distance and filling are kept separate:

\[
d_{\mathcal R}(\Gamma,\Gamma'),
\qquad
\operatorname{Fill}_{\mathcal R}(\ell).
\]

The earlier resource vector included one undifferentiated \(\Delta\).  That
form is superseded because a pairwise rewrite distance or loop filling is not
a coordinate of one realization without a reference object.

### 4.9 Matrix chains and the exactness obstruction

Let

\[
A\in K^{d_0\times d_1},
\quad
B\in K^{d_1\times d_2},
\quad
C\in K^{d_2\times d_3}.
\]

Under ordinary dense matrix multiplication, the two parenthesizations have
scalar-multiplication counts

\[
W_L=d_0d_1d_2+d_0d_2d_3,
\]

\[
W_R=d_1d_2d_3+d_0d_1d_3,
\]

and principal intermediate matrix sizes

\[
R_L=d_0d_2,
\qquad
R_R=d_1d_3.
\]

These \(R\)-values are not complete peak-memory formulas: inputs, output,
temporaries, overwrite policy, and evaluation order also matter.

For four matrices, the five parenthesizations form an associahedral pentagon
(the \(K_n\) index varies by convention).  If a rewrite edge is labelled by
an endpoint potential difference

\[
\omega_C(T\to T')=C(T')-C(T),
\]

then every closed loop satisfies

\[
\sum_{\partial P}\omega_C=0.
\]

This is an exact negative result.  Adding cache or lifetime state usually
means that the true state space must be enlarged.  Positive work accumulated
around a closed plan is action or dissipation; it is not automatically
connection holonomy.

### 4.10 OBDD order as a cut-residual theorem

Consider

\[
\operatorname{EQ}_n(x,y)=\mathbf1[x=y].
\]

Under the block order

\[
x_1,\ldots,x_n,y_1,\ldots,y_n,
\]

the cut after the \(x\)-block exposes the distinct residual functions

\[
g_a(y)=\mathbf1[y=a],
\qquad
a\in\{0,1\}^n.
\]

There are \(2^n\) such residuals, so the OBDD width at that cut is at least
\(2^n\).

Under the interleaved order

\[
x_1,y_1,\ldots,x_n,y_n,
\]

a construction needs at most three live residual states: already mismatched,
or still matching with pending bit \(0\) or \(1\).  Hence the maximum width is
constant and total graph size is \(O(n)\).

For a variable order \(\pi\), define

\[
H_\pi(t)
=
\log_2
\left|
\left\{
F|_\alpha:
\alpha\text{ assigns the first \(t\) variables of }\pi
\right\}
\right|.
\]

Then

\[
H_{\mathrm{block}}(n)=n,
\qquad
H_{\mathrm{interleaved}}(t)=O(1).
\]

Variable restrictions commute as semantic operations, yet cut order changes
residual width exponentially.  Thus exponential cut growth need not arise
from operator noncommutativity.  The online node index
\(\log_2(\text{width})\) and the static OBDD node count remain different
resources.

### 4.11 Reverse AD and the live-configuration correction

For

\[
x_{i+1}=f_i(x_i),
\qquad
\bar x_i=Df_i(x_i)^*\bar x_{i+1},
\]

the reverse sweep requires forward states \(x_i\).

Under unit-cost functions and fixed-size states:

| Schedule | Work/time | Stored forward states |
| --- | --- | --- |
| store every state | \(O(N)\) | \(O(N)\) |
| recompute each needed prefix from the input | \(O(N^2)\) | \(O(1)\) |

Checkpointing interpolates between these extremes; <em>revolve</em> is optimal
under its stated linear uniform-step/checkpoint model and objectives.

This example invalidates a space definition based only on a monotone
completed-node set.  The live configuration must say which checkpoints
currently exist and allow compute, erase, and recompute actions.

The interpretation

\[
\text{checkpoint}=\text{materialized historical condensation},
\qquad
\text{recomputation}=\text{history re-expansion}
\]

is a useful structural proposal.  The AD pullback
\(Df_i(x_i)^*\) is not identical to one global projective inverse transport
for nonlinear \(f_i\).

### 4.12 Tensor contraction and residual object size

For a contracted subnetwork \(U\) with open boundary edges \(\partial U\), a
dense boundary tensor lies in

\[
T_U
\in
\bigotimes_{e\in\partial U}K^{d_e}
\]

and has

\[
D_U=\prod_{e\in\partial U}d_e
\]

scalar entries.  Over \(\mathbb F_q\), the full dense tensor space has
\(q^{D_U}\) elements and logarithmic cardinality \(D_U\log_2q\).

A contraction order

\[
\varnothing=U_0\subset U_1\subset\cdots\subset U_T=V
\]

controls the sizes of intermediate boundary tensors.  In a dense exact model,
large boundary width therefore produces exponential materialized objects.

The residual depends on the allowed future.  It may be:

- the entire boundary tensor when all compatible future tests are allowed;
- a quotient of that tensor by the kernel of one fixed future network;
- a sparse, low-rank, symmetric, or compressed representation when the model
  authorizes one.

The earlier comparison between \(w\log d\) and \(d^w\) confused an index
address with the tensor residual itself.  It is rejected in that form.

### 4.13 Proof space, reversible computation, and e-graphs

In resolution, a clause configuration is a live proof frontier.  Keeping a
derived clause pays clause space; erasing and rederiving it pays length.
Known 6-CNF families have \(O(n)\)-length resolution refutations but require
\(\Omega(n/\log n)\) clause space.  Thus:

\[
\text{short proof}
\not\Rightarrow
\text{small live proof configuration}.
\]

In reversible computation, a many-to-one step cannot discard predecessor
information for free.  Bennett's pebbling construction realizes precise
time–space tradeoffs by storing and reconstructing checkpoints.

E-graphs provide the complementary compression warning.  They share
congruence classes and subexpressions, so many equivalent expressions may be
represented without listing every history.  Hence:

\[
\text{large history fiber}
\not\Rightarrow
\text{large shared quotient representation}.
\]

These are standard external models.  Their AEG interpretations remain
STRUCTURAL PROPOSALS until explicit simulations are defined.

### 4.14 Three order effects, not yet three curvatures

The discussion first used the provisional terms operator curvature, rewrite
curvature, and slicing curvature.  Only the first has an established AEG
curvature analogue.  The corrected taxonomy is:

| Order effect | Meaning | Example |
| --- | --- | --- |
| semantic noncommutation | Order changes the induced operator or endpoint. | affine add/multiply; Horner digit position |
| rewrite-plan variation | Semantics agree but factorization and resources differ. | matrix-chain parenthesization |
| schedule/cut sensitivity | The same computation exposes different residual or live-state sizes. | OBDD order; checkpointing; elimination |

In plain language:

\[
\boxed{
\text{order changes meaning},
\qquad
\text{order changes realization},
\qquad
\text{order changes exposed memory}.
}
\]

The latter two should be called curvature only after a connection, 2-cell
defect, or gauge-controlled holonomy has been defined.

### 4.15 Representation change and fast multiplication

For a transform class \(\mathcal A\), the discussion proposed schematically

\[
\mathcal C(F;\Phi)
=
\mathcal C(\Phi)
+
\mathcal C(\Phi F\Phi^{-1})
+
\mathcal C(\Phi^{-1}),
\]

\[
\mathcal C_{\mathrm{rep}}(F)
=
\inf_{\Phi\in\mathcal A}\mathcal C(F;\Phi).
\]

For a bilinear operator:

\[
\mathcal C(m;\Phi)
=
2\mathcal C(\Phi)
+
\mathcal C(\odot_\Phi)
+
\mathcal C(\Phi^{-1}).
\]

The familiar factorization

\[
F_N^{-1}\circ\odot\circ(F_N\times F_N)
\]

directly describes convolution in a sufficiently large or padded transform
domain.  Integer multiplication additionally requires coefficient encoding,
zero padding or a non-cyclic construction, carry recovery, sufficiently large
moduli or CRT, and bit-complexity analysis.

The safe research principle is:

> Seek representations in which the core operator is sparse, diagonal,
> block-diagonal, or low-bandwidth, while the transform itself has a short,
> stable, and accurately costed factorization.

This is not a definition of every fast algorithm.

### 4.16 The affine–Appell interface

The Paper II analytic prototype uses

\[
B_n(a,v)=e^{-n\widetilde v}a^n.
\]

Under the current horizontal operators, direct calculation gives the formal
relations

\[
D_vB_n=0,
\qquad
D_uB_n=\mu n e^{-\widetilde v}B_{n-1}
\quad(n\ge1),
\qquad
D_uB_0=0.
\]

Thus one direction is absorbed and the other is lowering on the declared
finite algebraic family.  This is structurally parallel to finding
coordinates in which an operator becomes triangular.

The repository establishes only algebraic stability of certain finite spans.
Completeness, convergence, function-space spanning, and spectral significance
remain unproved.  Paper IV may use this as a candidate costed representation
only after Paper II states the relevant span or analytic setting.

### 4.17 The fixed-model radix normalization identity

Let

\[
k=e^\lambda\in\mathbb N,
\qquad
k\ge2,
\qquad
\mathcal K_g=-\lambda^2,
\qquad
\Omega_{\mathrm{coeff}}=\mu\lambda,
\qquad
\mu\ne0.
\]

Define

\[
h_{\mathrm{rep}}=\ln k,
\qquad
\Delta I=\log_2k.
\]

Then:

\[
\boxed{
\frac{|\Omega_{\mathrm{coeff}}|}{|\mu|}
=
\sqrt{-\mathcal K_g}
=
h_{\mathrm{rep}}
=
(\ln2)\Delta I
=
\lambda.
}
\]

This is an exact normalization identity because all terms are definitions or
normalizations of the same parameter \(\lambda\).  It does not show that
curvature produces entropy or that either yields a complexity lower bound.
The step length in the \(v\)-coordinate and all units must remain fixed.

### 4.18 Final three-layer framework

The discussion ends with the following working architecture:

\[
\boxed{
\begin{array}{c}
\textbf{Semantic cut theory}\\
(C,\mathsf{Cont}(C),\operatorname{Obs})
\longmapsto
\mathcal R_C,\ V_C,\ H_C
\end{array}}
\]

\[
\boxed{
\begin{array}{c}
\textbf{Operational realization theory}\\
(\mathcal M,\Gamma,\sigma)
\longmapsto
(L_{\mathrm{desc}},W,T,D_{\mathrm{caus}},S_{\max},\operatorname{ST},Q)
\end{array}}
\]

\[
\boxed{
\begin{array}{c}
\textbf{Rewrite-fiber theory}\\
\rho^{-1}(F),\ \mathcal R
\longmapsto
d_{\mathcal R},\operatorname{Fill}_{\mathcal R},
\text{and only later possible holonomy}
\end{array}}
\]

The missing AEG theorem is a bridge among these layers.  In particular:

\[
\text{When does projective process residue represent,
map to, or bound a continuation residual?}
\]

Until that bridge is proved, History–Residual–Cut is a coherent general
resource framework motivated by AEG, not a consequence of the existing AEG
theorems.

## 5. Established results

### Result R-1: Butterfly torus-coset lemma

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** Under the hypotheses and left-coset convention of §4.5,
\[
\mathsf B_\omega=\mathsf B_1D_\omega,
\qquad
D_\omega\in H,
\qquad
\mathsf B_\omega H=\mathsf B_1H.
\]  
**Hypotheses:** \(\operatorname{char}K\ne2\), \(\omega\ne0\); matrices first
belong to \(\operatorname{GL}_2(K)\); \(H\) is the projective diagonal
ordered-pair stabilizer.  
**Argument or proof location:** Direct multiplication and stabilizer
membership in §4.5.  
**Repository source:** Quotient background in
<code>notes/projective-condensation/bilateral_projective_condensation.tex</code>; butterfly statement
from the current discussion.  
**Relevant theorem nodes:** <code>P2</code>, <code>T2</code>, candidate
<code>PIV-FFT1</code>; Paper IV status 87–90.  
**Paper destination:** Paper IV case study.  
**Remaining integration work:** Define the multi-wire category and retain the
central scalar needed by inverse transforms.

### Result R-2: Binary Horner charge-fiber operator-image count

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:**
\[
\left|
\rho\bigl(\chi^{-1}(m,n\ln2)\bigr)
\right|
=
\binom nm
\]
for length-\(n\) binary Horner words of Hamming weight \(m\).  
**Hypotheses:** The alphabet, chronology, and ACS charges are exactly those of
§4.4; leading length is fixed; evaluation is over \(\mathbb Z\) or a
characteristic-zero field.  
**Argument or proof location:** Binary uniqueness in §4.4.  
**Repository source:** Paper I ACS inputs; finite statement from the current
discussion.  
**Relevant theorem nodes:** <code>G1</code>, candidate
<code>PIV-HOR1</code>, with equality levels from <code>S5</code> as a
supporting interface.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Audit ACS orientation and notation against the
final Paper I convention.

### Result R-3: Contextual-residual state lower bound

**Status:** STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF  
**Statement:** In a finite deterministic exact model, any online state
supporting every common legal continuation at \(C\) uses at least
\[
\left\lceil\log_2|\mathcal R_C|\right\rceil
\]
bits in the worst case.  
**Hypotheses:** Common continuation domain, deterministic exact observations,
finite residual set, lossless state encoding.  
**Argument or proof location:** Different residual classes must map to
different machine states; a \(b\)-bit state has at most \(2^b\) values.  
**Repository source:** No committed residual definition; interfaces with
status 93, 95, and 99.  
**Relevant theorem nodes:** Candidate <code>PIV-HRC2</code>.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Prove equivalence properties and treat partial,
randomized, approximate, and infinite cases separately.

### Result R-4: Residual-growth memory-time corollary

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** Under the snapshot charging convention of §4.7:
\[
\operatorname{ST}(T)
\ge
\sum_{t=0}^{T}
\left\lceil\log_2|\mathcal R_{C_t}|\right\rceil.
\]
Polynomial residual lower growth gives \(\Omega(T\log T)\); exponential lower
growth gives \(\Omega(T^2)\).  
**Hypotheses:** R-3 at each discrete cut; \(S_\sigma(t)\) is measured in bits
and charges the complete exact online state once per time unit; polynomial
growth has \(c>0,d>0\) from some \(t_0\), while exponential growth has
\(c>0,a>1\) from some \(t_0\).  
**Argument or proof location:** Sum R-3 and evaluate elementary logarithmic
sums.  
**Repository source:** Current discussion only.  
**Relevant theorem nodes:** Candidate <code>PIV-HRC2</code> and
<code>PIV-HRC4</code>.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Distinguish lower bounds from matching
asymptotics and relate snapshots to a legal live-configuration model.

### Result R-5: Matrix-chain local cost formulas

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** The work and principal intermediate-size formulas in §4.9 hold
for the two three-matrix parenthesizations.  
**Hypotheses:** Ordinary dense multiplication; work counts scalar
multiplications; \(R_L,R_R\) count only the principal intermediate matrix.  
**Argument or proof location:** Dimension counting.  
**Repository source:** Current discussion.  
**Relevant theorem nodes:** Candidate <code>PIV-RW1</code>; <code>S5</code>
is a supporting interface outside the formal §77 import list.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Add complete liveness and peak-memory
accounting.

### Result R-6: Associahedral exactness obstruction

**Status:** PROVED  
**Statement:** Every rewrite-edge label
\(\omega_C(T\to T')=C(T')-C(T)\) sums to zero on every closed rewrite loop.  
**Hypotheses:** \(C\) is a single-valued endpoint potential taking values in
an additive abelian group or vector space, and the sum is taken along a
finite oriented closed path.  
**Argument or proof location:** Telescoping.  
**Repository source:** Current discussion; analogous proposition in
<code>notes/projective-condensation/bilateral_projective_condensation.tex</code>, “Exact edge labels
 telescope.”  
**Relevant theorem nodes:** Candidate <code>PIV-RW1</code>; Paper IV status
92.  
**Paper destination:** Paper IV rewriting chapter.  
**Remaining integration work:** Keep rewrite distance, action, filling, and
possible connection holonomy distinct.

### Result R-7: Equality-OBDD residual-width separation

**Status:** STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF  
**Statement:** For \(\operatorname{EQ}_n\), the block variable order has width
at least \(2^n\) at the middle cut, while the interleaved order has maximum
width at most \(3\) and total size \(O(n)\).  
**Hypotheses:** Ordered read-once Boolean decision diagrams under a fixed
variable order.  
**Argument or proof location:** Explicit residual functions and construction
in §4.10.  
**Repository source:** No repository proof; standard OBDD background is
external.  
**Relevant theorem nodes:** Candidate <code>PIV-HRC1</code>,
<code>PIV-HRC2</code>, and <code>PIV-CUT1</code>.  
**Paper destination:** Paper IV.  
**Remaining integration work:** State reduction conventions and distinguish
online width from whole-graph storage.

### Result R-8: Radix-2 NTT network and layer-state counts

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** A fixed \(N=2^m\) radix-2 network has \(m\) synchronous layers
and \((N/2)m\) butterfly cells.  If each layer is invertible on
\(\mathbb F_q^N\), its reachable state set has \(q^N\) elements.  
**Hypotheses:** Fixed breadth-first topology, required roots, nonzero
determinants, full input range.  
**Argument or proof location:** Layer/cell counting and invertibility.  
**Repository source:** OQ-058 selects FFT/large-integer multiplication as a
case study; no committed proof.  
**Relevant theorem nodes:** Candidate <code>PIV-NET1</code>,
<code>PIV-NET2</code>, and <code>PIV-FFT2</code>; local quotient comparison
imports <code>T2</code>.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Audit inverse normalization, central scalars,
static constants, actual bit encoding, and communication.

### Result R-9: Fixed-model radix normalization identity

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** The equality in §4.17 holds exactly under its definitions.  
**Hypotheses:** Integer radix \(k=e^\lambda\ge2\), fixed metric/contact
normalization, \(\mu\ne0\), fixed step unit.  
**Argument or proof location:** Direct substitution.  
**Repository source:** Paper I hyperbolic/contact inputs; information-rate
names from the current discussion.  
**Relevant theorem nodes:** Conditional <code>E2</code>, <code>T6</code>,
<code>E3</code>; comparison <code>T15</code>.  
**Paper destination:** Paper IV as a warning-rich calibration.  
**Remaining integration work:** Do not promote it to a causal
curvature–entropy theorem.

### Result R-10: Affine–Appell lowering identities

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** On the declared algebraic family,
\[
D_vB_n=0,
\qquad
D_uB_n=\mu ne^{-\widetilde v}B_{n-1}\quad(n\ge1),
\qquad
D_uB_0=0.
\]  
**Hypotheses:** Current natural-unit definitions of \(D_u,D_v,\widetilde v\),
and \(B_n\).  
**Argument or proof location:** Direct differentiation in the analytic notes.  
**Repository source:** <code>notes/analysis-and-calculus/analysis_01.tex</code> and the sources
mapped by authoritative status item 71.  The displayed identities are the
proved part; the broader analytic basis program remains PARTIALLY PROVED.  
**Relevant theorem nodes:** Paper II analytic candidates; Paper I input
<code>K2</code>.  
**Paper destination:** Paper II; possible costed interface to Paper IV.  
**Remaining integration work:** State the finite span, linear independence,
and any function-space claims separately.

## 6. Structural proposals and conjectures

### 6.1 Structural proposals

#### Proposal S-1: Three-layer HRC framework

Use contextual residuals for semantic distinguishability, live configurations
for operational resources, and rewrite fibers for equal-semantics geometry.

- **Additional data needed:** History category, continuation class,
  observables, machine model, encodings, and rewrite 2-cells.
- **Validating theorem:** One finite formalism instantiating Horner, OBDD, and
  checkpointing without changing the core definitions.
- **Falsification or weakening:** If the examples require incompatible
  residual notions, retain HRC only as comparative vocabulary.
- **Target paper:** Paper IV.

#### Proposal S-2: Network AEG

Extend one-wire marked histories to a symmetric monoidal category or PROP of
multi-wire arithmetic gates.

- **Additional data needed:** Objects, ports, tensor product, local gate
  embedding, central scalars, domains, and spinal restriction theorem.
- **Validating theorem:** A functor to linear maps \(K^m\to K^n\) that
  recovers the butterfly network and interfaces precisely with projective AEG.
- **Falsification or weakening:** If the common \(2\times2\) matrices have no
  structure-preserving interface, the FFT comparison remains ordinary linear
  algebra.
- **Target paper:** Paper IV.

#### Proposal S-3: Pareto resource geometry

Represent the achievable costs of an input family by the nondominated set of
\((L_{\mathrm{desc}},W,T,D_{\mathrm{caus}},S_{\max},\operatorname{ST},Q)\).

- **Additional data needed:** Uniformity, machine simulations, coordinate
  units, preprocessing convention, and closure rules.
- **Validating theorem:** Robustness under a declared class of efficient
  simulations and recovery of a standard time–space tradeoff.
- **Falsification or weakening:** If arbitrary encodings dominate the set,
  keep the object fixed-model only.
- **Target paper:** Paper IV.

#### Proposal S-4: Quotient skeleton plus torus-label field

Record a fixed NTT as wire permutation, local \(G/H\) cosets, and static
torus-valued gate labels.

- **Additional data needed:** Reference lifts, gauge law, central scalar
  bookkeeping, static-storage cost, and reconstruction algorithm.
- **Validating theorem:** A complete network factorization and a proved
  table-versus-regeneration tradeoff.
- **Falsification or weakening:** If all label structure is implementation
  dependent and cost-neutral, retain only R-1.
- **Target paper:** Paper IV.

#### Proposal S-5: Representation-transform optimization

Search over a declared transform class for a low-cost transform plus sparse
core action.

- **Additional data needed:** Admissible transforms, conditioning, precision,
  bit cost, communication, and input family.
- **Validating theorem:** Reproduce a known FFT multiplication bound and one
  nontrivial AEG-native sparse representation.
- **Falsification or weakening:** Transform overhead or instability may erase
  the sparsity advantage.
- **Target paper:** Paper IV, with Paper II analytic input.

#### Proposal S-6: Non-exact rewrite connection

Seek group-valued or otherwise gauge-controlled edge transport on a rewrite
2-complex that is not an endpoint coboundary.

- **Additional data needed:** Rewrite 2-category, edge law, gauge
  transformations, coherence moves, and loop observable.
- **Validating theorem:** One nontrivial closed loop surviving allowed gauge
  change.
- **Falsification or weakening:** If all natural labels telescope, retain only
  rewrite distance and filling.
- **Target paper:** Paper IV or later relation theory.

### 6.2 Conjectures

No AEG-specific conjecture reached a sufficiently stable formal statement.
In particular, none of the following is promoted to CONJECTURE:

- projective process residue is always a complete continuation residual;
- NTT torus labels define a nontrivial connection;
- the radix normalization identity extends to a general curvature–entropy law;
- one scalar representation volume determines time and space;
- an AEG-native representation improves asymptotic computation.

They remain STRUCTURAL PROPOSAL or OPEN PROBLEM items.

### 6.3 Open programs

#### Open program O-1: Residual semantics

Compare contextual residuals with automata residuals, one-way communication
across cuts, tensor boundaries, proof configurations, and sufficient
statistics without identifying their materialization models.

#### Open program O-2: Projective-to-contextual bridge

Determine when an \(H\)-lift, group-valued defect, or projective quotient
fiber is sufficient for, maps to, or bounds a continuation residual.

#### Open program O-3: Rewrite geometry

Separate rewrite distance, filling area, action, and possible holonomy, and
construct the first non-exact finite example before proposing a general
curvature theory.

#### Open program O-4: AEG-native sparse families

Use the Paper II affine–Appell prototype to seek costed transforms with
low-bandwidth operator action.

#### Open program O-5: Rosetta Stone graph families

Use the same small graph topologies across several semantics to identify
which resource quantities are graph invariants and which depend on values,
representations, continuations, or schedules:

| Graph family | Primary calibration | Candidate interpretations |
| --- | --- | --- |
| chain \(P_n\) | retention versus recomputation | spinal AEG, reverse AD, reversible simulation |
| binary tree \(T_h\) | parenthesization and temporary intermediates | expression evaluation, matrix-chain subproblems, proof trees |
| diamond or pyramid \(D_h\) | shared subcomputation | memoization, black pebbling, proof reuse |
| grid \(G_{m\times m}\) | cut and boundary growth | tensor contraction, variable elimination, communication |
| butterfly \(B_N\) | factored transform and layered communication | FFT/NTT, torus labels, network schedules |

This benchmark family is a STRUCTURAL PROPOSAL.  A shared graph does not make
the domain-specific residual objects or cost models equal.  Each
interpretation must still declare its state space, quotient, encoding,
observable, and measured resource.

## 7. Rejected or superseded formulations

### Rejected formulation 1

**Earlier formulation:** Representation volume is the number of microscopic
states, and space complexity is its logarithm.  
**Problem:** This only describes a finite online residual-index lower bound.
It does not equal materialized workspace or static data-structure size.  
**Counterexample, contradiction, or missing hypothesis:** A dense boundary
tensor, an OBDD node index, and the whole OBDD have different sizes.  
**Replacement formulation:** Separate \(V_C\), \(H_C\), live workspace, and
static representation size.  
**Files or passages still using the old form:** Historical resource notes,
especially <code>notes/projective-condensation/note_09.tex</code>,
<code>notes/computation-and-resources/note_13.tex</code>, and
<code>notes/computation-and-resources/note_15.tex</code>, require audit.

### Rejected formulation 2

**Earlier formulation:** Space complexity is the logarithm of hyperbolic
volume.  
**Problem:** No coding map, history/AES quasi-isometry, or simulation theorem
has been proved.  
**Counterexample, contradiction, or missing hypothesis:** OQ-057 states the
missing bridge.  
**Replacement formulation:** Use only fixed finite model identities and seek
explicit comparisons.  
**Files or passages still using the old form:** No file is asserted to contain
this exact equation.  Broader complexity-to-hyperbolicity motivation in
<code>notes/projective-condensation/note_06.tex</code> and
<code>notes/projective-condensation/note_09.tex</code> requires audit.

### Rejected formulation 3

**Earlier formulation:** Noncommutativity is the source of exponential
representation growth.  
**Problem:** Noncommutative systems may have polynomial growth, while
commuting restrictions can expose exponential cut width.  
**Counterexample, contradiction, or missing hypothesis:** Discrete Heisenberg
group and the equality OBDD.  
**Replacement formulation:** Separate semantic noncommutation, quotient
growth, and schedule sensitivity.  
**Files or passages still using the old form:** Authoritatively excluded by
status 96 and theorem-graph §66.3.

### Rejected formulation 4

**Earlier formulation:** A monotone down-closed cut sequence is sufficient for
checkpointing and pebbling.  
**Problem:** It does not record erasure or recomputation.  
**Counterexample, contradiction, or missing hypothesis:** Reverse AD can have
the same causal chain and different live checkpoint sets.  
**Replacement formulation:** Use explicit live-configuration traces.  
**Files or passages still using the old form:** The initial discussion
formulation; resource notes require audit.

### Rejected formulation 5

**Earlier formulation:** \(w\log d\) bits for a boundary assignment illustrate
the state complexity of a \(d^w\)-entry boundary tensor.  
**Problem:** The first encodes a component address; the second is the residual
function itself.  
**Counterexample, contradiction, or missing hypothesis:** Over
\(\mathbb F_q\), dense tensors have up to \(q^{d^w}\) possible values.  
**Replacement formulation:** State the residual object and continuation class
before counting.  
**Files or passages still using the old form:** Current discussion only.

### Rejected formulation 6

**Earlier formulation:** Endpoint resource differences around a rewrite loop
produce holonomy.  
**Problem:** They are exact coboundaries and telescope.  
**Counterexample, contradiction, or missing hypothesis:** R-6 on the
associahedral pentagon.  
**Replacement formulation:** Keep distance/filling separate; require an
independent connection before holonomy.  
**Files or passages still using the old form:** Compare the endpoint transport
in <code>notes/projective-condensation/bilateral_projective_condensation.tex</code>.

### Rejected formulation 7

**Earlier formulation:** All butterflies have one \(G/H\) concept, so FFT is
already a Network AEG theorem.  
**Problem:** The butterfly is a two-wire linear gate in
\(\operatorname{GL}_2\), while established projective AEG uses one-hole
Möbius actions; the full FFT lies in \(\operatorname{GL}_N\).  
**Counterexample, contradiction, or missing hypothesis:** No monoidal network
category or interface theorem exists.  
**Replacement formulation:** R-1 is a local torus-coset lemma; Network AEG is
a structural proposal.  
**Files or passages still using the old form:** No committed FFT source.

### Rejected formulation 8

**Earlier formulation:** The twiddle residue is FFT runtime-state
information.  
**Problem:** In a fixed transform, twiddles are static constants; actual
labels lie in \(\mu_N\), not arbitrary \(H\).  
**Counterexample, contradiction, or missing hypothesis:** The same NTT input
state varies while its twiddle table remains fixed.  
**Replacement formulation:** Charge labels to description/table/generation
cost, separately from layer-state entropy.  
**Files or passages still using the old form:** Current discussion only.

### Rejected formulation 9

**Earlier formulation:** Time, space, and representation complexity are
literally equal.  
**Problem:** Work, makespan, depth, peak space, memory-time integral, and
description size differ and trade off.  
**Counterexample, contradiction, or missing hypothesis:** Checkpointing and
reversible pebbling.  
**Replacement formulation:** Use a fixed-model Pareto resource set and seek
inequalities.  
**Files or passages still using the old form:** Status 99 marks this an open
research hypothesis.

### Rejected formulation 10

**Earlier formulation:** Fast algorithm means sparse representation.  
**Problem:** Transform overhead, precision, carry recovery, communication, and
conditioning may dominate; some fast algorithms use other mechanisms.  
**Counterexample, contradiction, or missing hypothesis:** No universal
transform class or cost model.  
**Replacement formulation:** Treat sparse representation as a costed search
principle.  
**Files or passages still using the old form:** OQ-058 lists FFT only as a
candidate case.

### Rejected formulation 11

**Earlier formulation:** The affine–Appell family is already a complete
basis.  
**Problem:** Completeness, convergence, spanning, and spectral significance
are unproved.  
**Counterexample, contradiction, or missing hypothesis:** Authoritative status
71.  
**Replacement formulation:** Call it an algebraically stable family or a
basis only of a declared finite span.  
**Files or passages still using the old form:** <code>notes/analysis-and-calculus/analysis_01.tex</code>
and older analytic sources.

### Rejected formulation 12

**Earlier formulation:** Operator, rewrite, and slicing effects are already
three curvatures.  
**Problem:** Only the affine/contact case has an established curvature form;
the other two lack connections or invariant loop defects.  
**Counterexample, contradiction, or missing hypothesis:** Endpoint rewrite
labels telescope.  
**Replacement formulation:** Use the neutral term “three order effects.”  
**Files or passages still using the old form:** Current discussion only.

### Rejected formulation 13

**Earlier formulation:** ProofScaffold proof space is resolution clause space.
**Problem:** Metamath replay, compressed proofs, stack state, substitutions,
and disjointness contexts need an independent model.  
**Counterexample, contradiction, or missing hypothesis:** No simulation
between the two proof systems has been defined.  
**Replacement formulation:** Treat resolution as a calibration and build a
ProofScaffold-specific cost model.  
**Files or passages still using the old form:** No repository theorem
identified.

## 8. Decision register

| ID | Decision | Status | Consequence | Paper/file affected |
| --- | --- | --- | --- | --- |
| D-01 | Use semantic residual, operational configuration, and rewrite fiber as three distinct layers. | provisionally adopted | The unification claim becomes a bridge problem. | Paper IV; this note |
| D-02 | Separate four representation quantities. | adopted | Residual bits, workspace, and data-structure size are not conflated. | Paper IV |
| D-03 | Separate causal interfaces from live configurations. | adopted | Compute/erase/recompute traces become expressible. | Paper IV |
| D-04 | Use a Pareto resource set only inside a fixed model and input family. | provisionally adopted | Nonuniform hardcoding and arbitrary units are exposed. | Paper IV |
| D-05 | Rename the FFT result “butterfly torus-coset lemma.” | adopted | It is not presented as a full Network AEG theorem. | Paper IV |
| D-06 | Call \(D_\omega\) a torus or twiddle label before a connection is defined. | adopted | Static and dynamic information are separated. | Paper IV |
| D-07 | Use “three order effects,” not “three curvatures.” | adopted | Curvature terminology has an explicit re-entry condition. | Paper IV |
| D-08 | Keep rewrite distance and filling outside the per-realization resource vector. | adopted | The earlier undifferentiated \(\Delta\) coordinate is superseded. | Paper IV |
| D-09 | Use Horner and OBDD as the first semantic calibrations. | adopted | One tests charge condensation; one tests cut sensitivity. | Paper IV |
| D-10 | Use checkpointing as the first operational calibration. | adopted | Live configuration is tested immediately. | Paper IV |
| D-11 | Keep affine–Appell work in Paper II. | adopted by authoritative scope | Paper IV imports only proved, costed statements. | Papers II–IV |
| D-12 | Exclude all complexity consequences from Paper I. | adopted by authoritative scope | Paper I contains only imports and a forward reference. | Paper I |
| D-13 | Decide the projective-process/continuation-residual bridge. | unresolved | HRC is not yet an AEG consequence. | Paper IV |
| D-14 | Decide uniformity, encodings, and static-storage conventions. | deferred | All resource results remain model-specific. | Paper IV |

### Adopted

- Four-way representation distinction.
- Causal cut/live configuration separation.
- Local GL/PGL butterfly lemma before Network AEG semantics.
- Static twiddle labels separated from dynamic layer entropy.
- Three order effects with no premature curvature terminology.
- Exact finite calibrations before general claims.

### Rejected

- Raw history count as memory or runtime.
- Hyperbolic volume as a machine-space theorem.
- Endpoint cost difference as holonomy.
- Literal time–space–representation equality.
- Automatic identification of external resource models with AEG.

### Deferred

- A machine-independent residual-object complexity.
- A full Network AEG category.
- A gauge-controlled rewrite connection.
- A canonical Paper IV chapter structure.

### Still open

- Common continuation domains for partial ordinary/projective semantics.
- The bridge from projective process residue to continuation residual.
- Robustness under encoding and simulation.
- The first non-exact rewrite loop.
- An AEG-native representation with a proved algorithmic advantage.

## 9. Mathematical dependency map

### 9.1 Imported nodes

The authoritative Paper IV import boundary is the following interface set:

    PAPER_IV
      <== S3  marked spinal histories
      <== S4  mirror, reversal, and path-inverse distinctions
      <== P2  projective evaluation
      <== T2  bilateral generation of PGL2(K)
      <== P3  affine/Borel sector
      <== T3, T4  affine cocycles
      <== A3  relative affine defect
      <== G1  ACS charge map and paths
      <== T12 torsion–Stokes theorem

These lines record imports, not direct theorem arrows between adjacent listed
nodes.  Their full dependency closures remain those of the authoritative
graph.

Conditional metric-example inputs form a second set:

    RADIX_MODEL
      <== E2  invariant affine metric
      <== T6  basic hyperbolic AES
      <== E3  curvature calculation

Candidate comparison nodes form a third set:

    COMPARISON_ONLY
      <== K1, T15, K3, T17

This last line is not a dependency chain.  In particular, the authoritative
graph gives T15 its own C2 and K2 dependencies, and K3 its C0, K2, and T15
dependencies.  None of these comparison nodes implies a resource or
information theorem.

### 9.2 Modified or clarified nodes

    S3 marked spinal histories
      ==> candidate multi-wire network extension
      -/-> arbitrary DAG already belongs to Paper I

    P2 projective evaluation
      ==> local butterfly left-coset comparison after projectivization
      -/-> GL_N network semantics
      -/-> canonical H-coordinate

    G1 ACS charge map
      ==> Horner charge-fiber calculation
      -/-> charge-fiber count is a runtime lower bound

    T6 and E3 hyperbolic model
      ==> radix normalization example
      -/-> history/AES quasi-isometry
      -/-> complexity lower bound

    T15 contact bracket
      ==> supplies Omega_coeff in the fixed model
      -/-> general information curvature

### 9.3 New candidate nodes

These labels are local to this note and are not in the authoritative graph.

    PIV-HRC1  Contextual continuation-residual equivalence
    PIV-HRC2  Finite residual-state lower bound
    PIV-HRC3  Live-configuration execution semantics
    PIV-HRC4  Fixed-model Pareto resource set
    PIV-NET1  Multi-wire network-history category
    PIV-NET2  Network evaluation and spinal restriction
    PIV-FFT1  Butterfly torus-coset lemma
    PIV-FFT2  F_257 NTT resource audit
    PIV-HOR1  Binary Horner charge-fiber operator-image theorem
    PIV-RW1   Rewrite distance and filling
    PIV-RW2   Non-exact rewrite connection gate
    PIV-CUT1  Equality-OBDD residual-width theorem
    PIV-AD1   Checkpoint live-configuration theorem
    PIV-TN1   Contextual tensor-boundary residual theorem
    PIV-PF1   Proof-system resource bridge

### 9.4 Forbidden dependencies

    local PGL2 butterfly identity
      -/-> Network AEG
      -/-> FFT complexity theorem

    history-fiber cardinality
      -/-> workspace
      -/-> static quotient size

    residual bit lower bound
      -/-> materialized data-structure size

    endpoint cost difference
      -/-> holonomy

    hyperbolic volume growth
      -/-> complexity lower bound

    tensor boundary index width
      -/-> tensor residual size

    monotone completed-node set
      -/-> checkpoint or pebbling space

    commuting semantic restrictions
      -/-> schedule-independent residual width

    short proof
      -/-> small proof space

    sparse operator action
      -/-> fast stable transform

These refine the authoritative prohibited edges and status items 95–101.

## 10. Paper-series allocation

### Paper I

Paper I supplies marked spinal histories, equality distinctions, projective
evaluation, the affine/Borel sector, affine cocycles, ACS, the basic
hyperbolic model, and affine/contact torsion.

Paper I must exclude:

- the HRC framework;
- multi-wire network complexity;
- representation entropy or lower bounds;
- FFT/NTT and large-integer multiplication;
- checkpointing and time–space tradeoffs;
- claims from curvature or noncommutativity to hardness.

Only a forward reference to later quotient-information work is appropriate.

### Paper II

Paper II owns:

- affine–Appell algebraic and analytic development;
- horizontal analytic operators;
- completeness, convergence, spectral, or transform theorems;
- candidate AEG-native sparse operator families.

Paper IV may import only a precisely stated and costed result.

### Paper III

This discussion produces no multi-zero, tube, braid, or knot theorem.  Paper
III may later use a defined transport or resource decoration, but no
dependency is presently required.

### Paper IV

Paper IV owns:

- history categories, evaluation fibers, and kernel pairs;
- projective condensation and process residue;
- contextual residuals and causal interfaces;
- live-configuration execution and resource models;
- representation, work, time, depth, memory, communication, and static
  description costs;
- rewriting distance, filling, and any future connection;
- Horner, OBDD, matrix chain, checkpointing, tensor, proof, reversible, e-graph,
  FFT/NTT, and multiplication calibrations;
- all model-specific comparison and lower-bound theorems.

### Beyond Papers I–IV

A general rewriting 2-category with gauge-controlled holonomy may require a
later relation-theory or ProofGeometry paper.  A ProofScaffold resource model
also requires its own simulation theorem.  Computational mass,
thermodynamics, and physical spacetime remain archival or motivational until
formal equations and invariants exist.

| Material | Destination | Status | Dependency | Re-entry condition |
| --- | --- | --- | --- | --- |
| Three-layer HRC framework | Paper IV | STRUCTURAL PROPOSAL | OQ-047–055 | Formal residual and live-configuration definitions |
| Butterfly torus-coset lemma | Paper IV | PROVED WITH STATED HYPOTHESES | P2, T2 | Convention and category audit |
| Network AEG | Paper IV | STRUCTURAL PROPOSAL | Multi-wire category | Evaluation and spinal restriction theorem |
| NTT resource count | Paper IV | PROVED WITH STATED HYPOTHESES in a fixed model | OQ-058 | Reproducible F_257 audit |
| Multiplication representation principle | Paper IV | STRUCTURAL PROPOSAL | Transform cost model | Padding, carry, modulus, and bit-cost theorem |
| Affine–Appell lowering family | Paper II / IV interface | PARTIALLY PROVED | Paper II status 71 | Declared span and transform cost |
| Rewrite connection | Paper IV / beyond | STRUCTURAL PROPOSAL | Rewrite 2-complex | Non-exact gauge-controlled loop |
| OBDD cut theorem | Paper IV | STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF | Fixed OBDD model | Formal proof and citation |
| Checkpoint interpretation | Paper IV | STRUCTURAL PROPOSAL with standard external model | Live trace | Cost-preserving correspondence |
| General time–space–representation identity | Paper IV | OPEN PROBLEM | OQ-055 | Model-specific bidirectional inequalities |
| Computational mass/thermodynamics | Archive / beyond | UNSUPPORTED AND EXCLUDED as theorem | None | Formal field or cost law |

## 11. Repository source map

This section records where the present note obtained its scope, terminology,
status, and mathematical ingredients.  A source listed here is not thereby an
authority for every claim it contains.  The files under
governance/00-authoritative-scope.md through
governance/08-open-questions.md control the current editorial state.

### 11.1 Authoritative and editorial sources

| Source file | Relevant material | Current status | Target destination | Required action |
| --- | --- | --- | --- | --- |
| AGENTS.md | Repository workflow, reading order, and preservation rules | Operative repository instruction | This discussion artifact | Apply.  The root-level AGENTS.md named in the task specification is absent on the audited main branch. |
| README.md | Historical repository orientation | Legacy orientation under rewrite | Repository root | Read for provenance; do not use it to override the four-paper architecture. |
| governance/README.md | Purpose of the restructuring layer and relation to legacy sources | Current restructuring orientation | Restructuring layer | Apply subordinate to the numbered authoritative files. |
| governance/00-authoritative-scope.md | Paper boundaries, authority order, and allowed complexity scope | Authoritative scope | Papers I–IV | Apply; it controls the Paper IV destination of this note. |
| governance/01-paper-series-architecture.md | Paper IV §§8, 12, 23, 40, and 48: chapter sequence, imports, complexity names, and cost-model requirements | Authoritative architecture | Paper IV | Apply; retain the order from histories and quotients to representation and cost. |
| governance/02-paper-I-outline.md | Paper I sequence, theorem boundary, and exclusions | Authoritative Paper I outline | Paper I | Audit this note against the Paper I exclusion boundary; do not migrate HRC material into Paper I. |
| governance/03-theorem-dependency-graph.md | §77 imports S3, S4, P2, T2, P3, T3, T4, A3, G1, and T12 | Authoritative dependency graph | Papers I and IV interface | Import only the listed nodes; keep HRC and Network AEG nodes unregistered candidates. |
| governance/04-current-to-target-map.md | Destinations of legacy resource notes and affine–Appell material | Authoritative migration map | Papers II and IV | Apply extraction and migration destinations; preserve legacy sources. |
| governance/05-mathematical-status.md | Items 82–102 on histories, quotients, condensation, complexity, growth, and pebble models | Authoritative status ledger | Paper IV | Apply to every theorem-strength statement in Sections 5–7. |
| governance/06-editorial-rules.md | Exact status vocabulary, cost-model discipline, and forbidden implication patterns | Authoritative editorial rules | All papers and notes | Apply throughout. |
| governance/07-acceptance-checklist.md | Paper I exclusions and Paper IV destination tests | Authoritative acceptance gate | Papers I and IV | Apply in Section 10 and before any later migration. |
| governance/08-open-questions.md | OQ-047–OQ-058 | Authoritative question register | Paper IV | Reference in Section 15; do not modify or duplicate silently. |

### 11.2 Working and legacy repository sources

| Source file | Relevant material | Current status | Target destination | Required action |
| --- | --- | --- | --- | --- |
| governance/discussions/three-branch-arithmetic-tubes-and-complexity.md | Earlier complexity taxonomy, projective-condensation questions, and rejected general implications | Subordinate working note | Paper IV discussion provenance | Audit and narrow; the present note corrects its resource-geometry branch. |
| governance/discussions/aeg-tube-braid-markov-invariants.md | Fiber, transport, loop-data, and status terminology | Subordinate working note | Paper III / cross-paper provenance | Audit terminology only; do not extract tube or braid claims into this note. |
| notes/projective-condensation/bilateral_projective_condensation.tex | History groupoid, evaluation, quotient tower, bivaluation, process residue, associativity 2-cell, and the formula “exact edge labels telescope” | SPLIT; status items 82–92 control | Paper IV | Extract and rewrite with explicit quotient side, reference lift, and gauge caveat. |
| notes/projective-condensation/note_06.tex | Projective compactification and broader complexity-to-hyperbolicity motivation | SPLIT | Paper IV / archive | Extract projective motivation; reject any unproved implication that complexity makes hyperbolicity unavoidable; preserve the original. |
| notes/projective-condensation/note_09.tex | Canonical forms, condensation, and early space-from-time intuition | MOVE to Paper IV; preserve original | Paper IV / archive | Extract definitions; reject unproved growth lower-bound implications; archive original. |
| notes/computation-and-resources/note_10.tex | Early space-as-curvature and computational-mass language | Archival or motivational | Archive / beyond Paper IV | Preserve and cite only in the superseded trajectory. |
| notes/computation-and-resources/note_13.tex | Resource Geometry of Turing Machines; checkpointing and recomputation | HOLD pending semantic audit | Paper IV candidate | Audit and rewrite using live configurations before reuse. |
| notes/computation-and-resources/note_14.tex | Y-shaped DAG, pebbling, waiting, and recomputation | HOLD pending semantic audit | Paper IV candidate | Audit examples; do not treat ghost waiting as a canonical completion. |
| notes/computation-and-resources/note_15.tex | Complexity, torsion, volume, representation, time, space, and filling distinctions | Legacy Paper IV proposal | Paper IV | Audit, split into model results/proposals/rejections, and rewrite. |
| notes/computation-and-resources/note_16.tex | Computational spacetime and time–space duality proposals | HOLD pending semantic audit | Paper IV candidate | Preserve as motivation; require a computational model before extraction. |
| notes/thermodynamics-and-renormalization/rg_en.tex and notes/thermodynamics-and-renormalization/rg_zh.tex | Earlier resource-geometry programs | MOVE / ARCHIVE | Paper IV / archive | Compare versions, extract one audited line, and preserve both originals. |
| notes/analysis-and-calculus/analysis_01.tex | Affine–Appell formula \(B_n=e^{-n\widetilde v}a^n\) and lowering action | Legacy analytic prototype | Paper II | Extract the finite-span calculation; rewrite all function-space claims. |
| sections/sec07.tex and sections/sec08.tex | Affine–Appell formulas and analytic prototypes | SPLIT / MOVE | Paper II | Source-audit and migrate only after analytic hypotheses are fixed. |
| sections/sec02-01.tex, sections/sec05.tex, sections/sec09.tex, and sections/sec12.tex | Free histories, equality levels, ACS, loops, and quotient material | SPLIT / REWRITE under the migration map | Papers I and IV | Extract only through authoritative node boundaries; preserve current sources. |

The repository audit found no pre-existing FFT or butterfly proof in the
active authoritative layer.  The formulas in Sections 4.5–4.6 and 5 therefore
trace to the present discussion and their displayed elementary verification,
not to an invented repository theorem.

### 11.3 External calibration sources

External work is used to calibrate definitions and examples.  It does not
establish an AEG identification without an additional comparison theorem.

| External source | Imported fact or role | Boundary in this note |
| --- | --- | --- |
| R. E. Bryant, [Graph-Based Algorithms for Boolean Function Manipulation](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf), 1986 | Ordered BDDs, reduction, canonicity at fixed order, and order sensitivity | The equality example still receives its own residual proof obligation. |
| A. Griewank and A. Walther, [Algorithm 799: Revolve](https://dl.acm.org/doi/10.1145/347837.347846), 2000 | Optimal checkpoint scheduling in its stated sequential checkpoint model | Not claimed to give the Pareto frontier for every reverse-AD system. |
| I. Markov and Y. Shi, [Simulating Quantum Computation by Contracting Tensor Networks](https://arxiv.org/abs/quant-ph/0511069) | Tensor-network contraction and width-based simulation bounds | Does not make every tensor-network cost an AEG theorem; graph and line-graph conventions require care. |
| E. Ben-Sasson and J. Nordström, [Short Proofs May Be Spacious](https://jakobnordstrom.se/docs/publications/ShortProofs_FOCS.pdf) | Separation between resolution length and clause space | Imported as a proof-complexity calibration, not as a ProofScaffold theorem. |
| C. H. Bennett, [Time/Space Trade-Offs for Reversible Computation](https://epubs.siam.org/doi/10.1137/0218053), 1989 | Reversible simulation and pebbling tradeoffs | Supports the need for compute, erase, and recompute actions; no direct AEG equivalence is assumed. |
| M. Willsey et al., [egg: Fast and Extensible Equality Saturation](https://arxiv.org/abs/2004.03082) | Compact congruence representation of many equivalent expressions | Serves as a counter-calibration to raw history-fiber counting. |
| D. J. Rose, R. E. Tarjan, and G. S. Lueker, [Algorithmic Aspects of Vertex Elimination on Graphs](https://i.stanford.edu/pub/cstr/reports/cs/tr/75/531/CS-TR-75-531.pdf) | Elimination order and fill structure | Supports an elimination-order case family, not a universal width theorem here. |
| J. W. Cooley and J. W. Tukey, [An Algorithm for the Machine Calculation of Complex Fourier Series](https://web.stanford.edu/class/cme324/classics/cooley-tukey.pdf) | Classical factored Fourier-transform algorithm | Used only as historical calibration for the explicitly defined radix-2 network. |

The attached Arithmetic Expression Geometry Discussion Note Task(2).pdf is a
construction specification for this artifact.  It determines the required
front matter, section structure, source discipline, and completion report; it
is not a mathematical source for any result.

## 12. Proof obligations

Each obligation below names the exact deliverable required before a claim may
be promoted.  A repository destination is included to prevent a proof task
from silently changing authoritative files.

### PO-01: Contextual residual equivalence

**Target statement:** For one typed interface, common continuation class,
observable, and partial-domain convention, \(\equiv_C\) is an equivalence
relation and the kernel pair of the complete continuation-behavior map.  
**Known special cases:** Total deterministic set-valued behavior maps, where
equality of behavior functions immediately gives a kernel equivalence.  
**Available argument:** Reflexivity, symmetry, and transitivity follow from
equality of all defined observations; the working definition is a STRUCTURAL
PROPOSAL.  
**Missing step:** Construct the typed continuation object and specify how
undefined evaluations compare.  
**Required hypotheses:** Common \(\mathsf{Cont}(C)\), typed pasts, exact
observable, and an explicit undefined-value convention.  
**Dependencies:** OQ-047, OQ-048, OQ-051, DD-01, and the future Network AEG
category.  
**Failure consequence:** A residual class is not well-defined and R-3 cannot
be used.  
**Recommended next action:** Prove the set-level finite case in the Task 1
calculation, then formulate its categorical lift for Paper IV.

### PO-02: Residual-state lower bound

**Target statement:** In a finite deterministic exact model, every online
machine state sufficient for every allowed future distinguishes all elements
of \(\mathcal R_C\), so a fixed-width binary state uses at least
\(\lceil\log_2|\mathcal R_C|\rceil\) bits.  
**Known special cases:** Finite automata residuals and the explicit OBDD
equality cut.  
**Available argument:** If two distinct residuals share one deterministic
state, a continuation distinguishing them produces a contradiction; this is
a STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF.  
**Missing step:** Write the injection from residual classes to reachable
machine states and delimit variable-length, randomized, approximate, and
infinite cases.  
**Required hypotheses:** PO-01, finite residual set, exact observation,
deterministic transitions, and injective state encoding.  
**Dependencies:** DD-01, DD-03, DD-04, OQ-052, and OQ-055.  
**Failure consequence:** Residual log-cardinality remains descriptive and
cannot support a memory lower bound.  
**Recommended next action:** Give the one-page injection proof and a
counterexample outside each excluded hypothesis.

### PO-03: Live-configuration execution model

**Target statement:** A typed trace with compute, erase, and recompute actions
faithfully represents a selected chain-checkpoint model and black-pebbling
model with stated cost distortion.  
**Known special cases:** Linear reverse-AD checkpoint schedules and ordinary
black pebbling on finite DAGs.  
**Available argument:** Map stored checkpoints or pebbles to live objects and
each legal evaluation/deletion move to an action; the general bridge is a
STRUCTURAL PROPOSAL.  
**Missing step:** Give both simulations, including inputs, outputs, value
sizes, and the exact relation between action count and imported time.  
**Required hypotheses:** Fixed dependency graph, live-object encoding,
legality rules, action costs, and input/output convention.  
**Dependencies:** DD-02, DD-04, DD-05, status item 100, and OQ-055.  
**Failure consequence:** Checkpointing, proof space, and recomputation cannot
share one operational resource definition.  
**Recommended next action:** Enumerate all legal traces for small chains and
compare them with small black-pebbling schedules.

### PO-04: Binary Horner charge-fiber theorem

**Target statement:** Over \(\mathbb Z\) or a characteristic-zero field, the
\(\binom nm\) length-\(n\) binary Horner words of Hamming weight \(m\) have one
ACS charge and distinct affine operator images.  
**Known special cases:** Direct enumeration for small \(n\); the displayed
closed formula in Section 4.4.  
**Available argument:** Expand
\(h_{b_n}\circ\cdots\circ h_{b_1}\) and apply uniqueness of the integer
binary coefficient string; R-2 is PROVED WITH STATED HYPOTHESES at
working-note level.  
**Missing step:** Audit word orientation, chronology, leading-zero treatment,
and ACS normalization against the final Paper I conventions.  
**Required hypotheses:** Fixed length, \(b_i\in\{0,1\}\),
characteristic-zero evaluation, and the stated charge map.  
**Dependencies:** G1, the supporting equality levels in S5, and DD-10 for the
optional entropy interpretation.  
**Failure consequence:** In finite characteristic the operator-image count
can collapse, so the stated \(\binom nm\) theorem would be false.  
**Recommended next action:** Add a characteristic-\(p\) collision table and
then extract the characteristic-zero proof into the Paper IV case study.

### PO-05: Butterfly \(GL_2/PGL_2\) audit

**Target statement:** For \(\operatorname{char}K\ne2\) and
\(\omega\ne0\), \(\mathsf B_\omega=\mathsf B_1D_\omega\), both factors are
invertible, and \(\mathsf B_\omega H=\mathsf B_1H\) under the stated
left-coset and diagonal-stabilizer
convention.  
**Known special cases:** Direct symbolic multiplication and every nonzero
twiddle over \(\mathbb F_{257}\).  
**Available argument:** Determinants and diagonal-stabilizer membership prove
the local lemma; R-1 is PROVED WITH STATED HYPOTHESES.  
**Missing step:** Audit quotient side, ordered reference pair, projective
scalar, inverse normalization, and the absent spinal-to-network interface.  
**Required hypotheses:** Field \(K\), \(\operatorname{char}K\ne2\),
\(\omega\in K^\times\), first working in \(GL_2(K)\), and explicitly chosen
\(H\).  
**Dependencies:** P2, T2, status items 87–90, DD-06, and DD-07.  
**Failure consequence:** The coset identity may remain valid, but it cannot be
described as Network AEG or as a canonical process residue.  
**Recommended next action:** Produce a convention-audit table before any
network-level claim.

### PO-06: \(\mathbb F_{257}\), \(N=8,16\) NTT audit

**Target statement:** Give primitive-root choices, \(N\)-th roots, twiddle
subgroups, inverse normalization, cell count, causal depth, reachable
layer-state cardinality, and explicit storage conventions for two transforms.  
**Known special cases:** The topology gives 12 cells and 3 layers for \(N=8\);
\(|\mathbb F_{257}^{\times}|=256\).  
**Available argument:** Elementary finite-field and network calculations;
the complete audit is an OPEN PROBLEM.  
**Missing step:** Select and verify concrete roots, inverse maps, static
tables or generation schedules, and fixed-width bit encodings.  
**Required hypotheses:** A declared radix-2 topology, full input range,
invertible layers, and separate static/dynamic and field/bit cost models.  
**Dependencies:** PO-05, PO-10, DD-04–DD-07, and OQ-058.  
**Failure consequence:** \(\operatorname{ST}_{\log}\) remains only a
convention-level information count, not an implementation cost.  
**Recommended next action:** Create a reproducible finite calculation under
governance/calculations/; do not edit Paper IV prose first.

### PO-07: OBDD equality separation

**Target statement:** The block order for \(EQ_n\) has middle width at least
\(2^n\), while the interleaved order admits width at most \(3\) and \(O(n)\)
nodes.  
**Known special cases:** Bryant's fixed-order OBDD framework and direct small
\(n\) diagrams.  
**Available argument:** Exhibit
\(y\mapsto\mathbf1[y=a]\) for all \(a\in\{0,1\}^n\), then construct failure
and pending-bit states; the result is a STANDARD CONSEQUENCE REQUIRING AN
IN-PAPER PROOF.  
**Missing step:** Fix reduced versus unreduced conventions and write the
all-\(n\) width and node-count proof.  
**Required hypotheses:** Deterministic ordered read-once BDD, fixed variable
order, exact Boolean semantics, and an explicit width convention.  
**Dependencies:** PO-01, PO-02, DD-03, and OQ-058.  
**Failure consequence:** The flagship example for cut sensitivity would be
only an analogy.  
**Recommended next action:** Enumerate small instances and extract the
residual proof with separate online-width and static-size statements.

### PO-08: Associahedral exactness theorem

**Target statement:** Every additive edge label
\(\omega_C(T\to T')=C(T')-C(T)\) sums to zero on every closed rewrite loop,
including the four-matrix associahedron.  
**Known special cases:** The five-cycle and, by the same telescoping
calculation, every finite closed path.  
**Available argument:** Direct cancellation proves R-6; its status is PROVED
at working-note level.  
**Missing step:** Integrate the result with the chosen rewrite category and
state separately the definitions of distance, filling, action, and possible
connection.  
**Required hypotheses:** One globally defined endpoint potential and additive
edge transport.  
**Dependencies:** Status item 92 and OQ-047; PO-11 governs any later
non-exact connection comparison.  
**Failure consequence:** Any proposed resource holonomy built only from
endpoint cost differences is trivial.  
**Recommended next action:** Write the five parenthesizations and all edge
labels as a finite negative-calibration table.

### PO-09: Tensor continuation-residual theorem

**Target statement:** Characterize the continuation residual of a contracted
subnetwork for both a fixed remaining network and the class of all compatible
future tests.  
**Known special cases:** A fixed linear future identifies boundary tensors
modulo its kernel; a separating class of all dual tests distinguishes every
dense boundary tensor.  
**Available argument:** Express contextual equivalence as a kernel relation;
the representation-sensitive theorem remains an OPEN PROBLEM.  
**Missing step:** Fix the field, tensor and boundary types, future-test class,
observable, and dense, sparse, or factored representation.  
**Required hypotheses:** Typed boundary, exact contraction, common futures,
and declared representation cost.  
**Dependencies:** PO-01, DD-01, DD-03, DD-09, and OQ-052–OQ-055.  
**Failure consequence:** Boundary index width may again be confused with the
size of a residual function or tensor.  
**Recommended next action:** Prove the two kernel characterizations before
introducing treewidth or contraction-cost claims.

### PO-10: Network cost model

**Target statement:** Define a uniform family of network implementations with
separate description, work, scheduled time, causal depth, peak workspace,
memory-time, and communication coordinates.  
**Known special cases:** Fixed radix-2 gate counts, sequential Horner traces,
and finite checkpoint schedules.  
**Available argument:** The candidate resource vector in Section 4.8 is a
STRUCTURAL PROPOSAL.  
**Missing step:** Fix the family, uniformity, gate set, encodings,
preprocessing, constants, schedule, and exact or approximate semantics, then
prove invariance or simulation bounds.  
**Required hypotheses:** One explicit computational model and compatible
units for every comparison.  
**Dependencies:** DD-04, DD-05, DD-08, OQ-054, and OQ-055.  
**Failure consequence:** The proposed Pareto set changes arbitrarily with
encoding and cannot support a paper-level comparison.  
**Recommended next action:** Instantiate the model on the finite HRC,
Horner, and NTT calculations before seeking generality.

### PO-11: Rewrite-connection gate

**Target statement:** Before holonomy language is promoted, construct a
rewrite 2-complex, group-valued edge transport, composition and gauge laws,
and a closed-loop class that is not an endpoint coboundary.  
**Known special cases:** Exact potential transport is trivial by PO-08;
ordinary positive path cost can be nonzero on a loop but is action, not
holonomy.  
**Available argument:** The telescoping obstruction supplies the negative
test; a non-exact connection is an OPEN PROBLEM.  
**Missing step:** Construct any natural edge law surviving gauge change and
coherence moves.  
**Required hypotheses:** Fixed rewrite generators and 2-cells, target group,
orientation, gauge transformations, and closed-loop observable.  
**Dependencies:** PO-08, OQ-047, OQ-049, OQ-054, and DD-07.  
**Failure consequence:** Rewrite geometry retains distance and filling but no
projective holonomy claim.  
**Recommended next action:** Test the associahedron first and a
Cooley–Tukey factorization complex only after the exact labels are excluded.

### PO-12: ProofScaffold application bridge

**Target statement:** Give a cost-aware simulation between a specified
Metamath proof trace/configuration model and a selected proof-space or
pebbling model.  
**Known special cases:** Resolution clause blackboards and DAG pebbling have
standard external definitions; ProofScaffold currently has a distinct replay
and substitution semantics.  
**Available argument:** The analogy between retained lemmas and live objects
motivates an OPEN PROBLEM; no simulation theorem is available.  
**Missing step:** Define statement encoding, substitutions, disjointness
context, stack replay, lemma retention, compressed proofs, and verification
cost.  
**Required hypotheses:** Fixed proof system on both sides and a declared
resource-preserving translation.  
**Dependencies:** PO-03, PO-10, OQ-058, and the future ProofScaffold cost
model.  
**Failure consequence:** Resolution space cannot be cited as ProofScaffold
space or as an AEG theorem.  
**Recommended next action:** Defer the bridge beyond the four-paper core
unless Paper IV first supplies a sufficiently general proof-history instance.

## 13. Definition decisions

The blocking scale follows governance/08-open-questions.md: P0 blocks Paper I
and P3 is later-program work.  Because every new decision here belongs to
Paper IV, every item is P3 even when it is locally first in the HRC
dependency order.  “Local order” below is therefore descriptive, not a new
priority vocabulary.  These are working defaults, not edits to the
authoritative restructuring or notation conventions.

### DD-01: Data defining a continuation residual

**Competing formulations:** A residual intrinsic to a down-set; a residual
relative to one fixed suffix; a residual relative to all typed future
contexts.  
**Current evidence:** Tensor kernels and partial-domain examples show that
different continuation classes identify different pasts.  
**Recommended default:** Use a typed interface \(C\), common
\(\mathsf{Cont}(C)\), observable, and undefined-value convention.  
**Examples that must be tested:** Binary Horner, \(EQ_n\), a fixed tensor
future, and all separating tensor tests.  
**Affected theorem nodes:** Candidate PIV-HRC1 and PIV-HRC2; OQ-047, OQ-048,
and OQ-051.  
**Blocking level:** P3; local order first for every residual theorem.

### DD-02: Causal progress versus live memory

**Competing formulations:** A monotone completed down-set; one moving cut;
an ever-computed set plus a live configuration; a complete machine state.  
**Current evidence:** Deletion and recomputation in checkpointing and
pebbling cannot be recovered from a monotone down-set.  
**Recommended default:** Use a typed causal interface for dependency and a
separate action trace \(L_0\to\cdots\to L_T\) for live resources.  
**Examples that must be tested:** Linear checkpointing, diamond DAG
pebbling, clause deletion, and reversible uncomputation.  
**Affected theorem nodes:** Candidate PIV-HRC3 and PIV-AD1; status item 100.  
**Blocking level:** P3; local order first for operational claims.

### DD-03: Four representation quantities

**Competing formulations:** One representation volume; residual
log-cardinality; actual workspace; whole-program or graph size.  
**Current evidence:** OBDD width versus node count and tensor index width
versus dense tensor size separate these quantities.  
**Recommended default:** Keep residual cardinality, online state width,
materialized workspace, and static representation size distinct.  
**Examples that must be tested:** \(EQ_n\), dense and factored boundary
tensors, e-graphs, and a finite-state machine.  
**Affected theorem nodes:** Candidate PIV-HRC2, PIV-HRC3, and PIV-HRC4;
OQ-052 and OQ-055.  
**Blocking level:** P3; local order before any time–space comparison.

### DD-04: Uniform computational object and encoding

**Competing formulations:** A single finite function \(F\); a nonuniform
circuit family; a uniform algorithm or network family; an advice model.  
**Current evidence:** A single finite map can be hard-coded, while bit and
field-operation costs change with encoding.  
**Recommended default:** State an input family, uniformity, encoding,
preprocessing and constant-storage convention, and exact or approximate
semantics.  
**Examples that must be tested:** Binary Horner families, radix-2 NTT
families, and fixed \(N=8,16\) calibrations.  
**Affected theorem nodes:** Candidate PIV-HRC4 and PIV-FFT2; OQ-054, OQ-055,
and OQ-058.  
**Blocking level:** P3; local order before asymptotic complexity language.

### DD-05: Time, depth, and the resource vector

**Competing formulations:** One time coordinate; gate count as time;
intrinsic depth; scheduled makespan; a vector also containing rewrite defect.  
**Current evidence:** Parallel networks and recomputation traces separate
work, scheduled time, and causal depth; rewrite distance refers to a pair, not
one implementation.  
**Recommended default:** Use
\((L_{\rm desc},W,T,D_{\rm caus},S_{\max},\operatorname{ST},Q)\) for one
implementation and keep rewrite distance and filling separate.  
**Examples that must be tested:** One NTT layer schedule, a sequential
Horner trace, checkpoint schedules, and matrix-chain rewrites.  
**Affected theorem nodes:** Candidate PIV-HRC3, PIV-HRC4, and PIV-RW1;
OQ-054 and OQ-055.  
**Blocking level:** P3; local order before Pareto comparisons.

### DD-06: \(GL_2\), \(PGL_2\), and the network interface

**Competing formulations:** Treat the butterfly directly as a Möbius
context; projectivize the local gate and discard scalars; first define a
multi-wire linear category and then compare it with spinal AEG.  
**Current evidence:** The local matrix factorization is exact, but its
two-wire semantics differs from one-hole arithmetic and inverse transforms
need scalar normalization.  
**Recommended default:** Work first in \(GL_2(K)\), specify the map to
\(PGL_2(K)\), left-coset convention, ordered reference pair, and \(H\);
require a separate Network AEG bridge.  
**Examples that must be tested:** One butterfly, a two-layer network, inverse
NTT normalization, and a spinal restriction.  
**Affected theorem nodes:** P2, T2, candidate PIV-NET1, PIV-NET2, and
PIV-FFT1; OQ-048 and OQ-049.  
**Blocking level:** P3; local order before any Network AEG theorem.

### DD-07: Torus label versus connection

**Competing formulations:** Phase, process residue, \(H\)-coordinate, torus
label, or group-valued connection.  
**Current evidence:** A coordinate depends on a reference lift, and endpoint
cost labels telescope; no gauge-controlled loop transport has been built.  
**Recommended default:** Use torus, diagonal, or twiddle label for
\(D_\omega\); reserve connection and holonomy until PO-11 is met.  
**Examples that must be tested:** Reference-lift changes, the associahedron,
and a Cooley–Tukey factorization loop.  
**Affected theorem nodes:** Candidate PIV-FFT2 and PIV-RW2; status items 88,
90, and 92.  
**Blocking level:** P3; local order before holonomy language.

### DD-08: Operator and representation complexity notation

**Competing formulations:** Treat \(C_{\rm op}\) and \(C_{\rm rep}\) as
synonyms; reserve the first for operator/factorization encoding and the
second for broader runtime or static representations.  
**Current evidence:** The architecture uses both symbols without an
authoritative equality, while the examples require distinct objects.  
**Recommended default:** Use \(C_{\rm op}\) for an operator or
factorization encoding and \(C_{\rm rep}\) for broader representations; use
\(\mathsf B_1\) for the butterfly skeleton, \(W\) for work,
\(D_{\rm caus}\) for depth, \(D_\omega\) for the diagonal matrix, \(H\) for
the stabilizer, and \(H_C\) for residual log-cardinality.  
**Examples that must be tested:** NTT constant tables, OBDD graphs, and
affine–Appell transform descriptions.  
**Affected theorem nodes:** Complexity taxonomy status item 93 and candidate
PIV-HRC4.  
**Blocking level:** P3; revisit when an authoritative convention decision is
made.

### DD-09: Entropy and tensor-size conventions

**Competing formulations:** Call every log-cardinality entropy; encode one
tensor index and call it the residual size; charge a dense, sparse, or
factored tensor.  
**Current evidence:** Shannon entropy requires a distribution, and an
arbitrary \(D_C\)-component tensor has up to \(q^{D_C}\) values even though
one index costs only \(\sum_e\log_2d_e\) bits.  
**Recommended default:** Use log-cardinality unless a probability measure is
declared; state the tensor representation and charge component count,
addresses, and coefficients separately.  
**Examples that must be tested:** Uniform and nonuniform NTT inputs, dense
boundary tensors, and low-rank factorizations.  
**Affected theorem nodes:** Candidate PIV-HRC2 and PIV-TN1; OQ-052.  
**Blocking level:** P3; local order before information or tensor-space claims.

### DD-10: Partial equality and Pareto closure

**Competing formulations:** Identify domain, relation, ordinary-evaluation,
projective-evaluation, and observational equality; or keep them separate.
For resource sets, take minima, nondominated points, or their closure.  
**Current evidence:** Partial histories and projectivization produce
different kernel pairs; achievable resource sets need not attain limiting
points.  
**Recommended default:** Keep all equality levels explicit.  At fixed input
size and model, take the nondominated costs of the \(n\)-th members of
declared admissible uniform implementation families; use closure only when
its need is stated.  
**Examples that must be tested:** Undefined continuations, scalar-equivalent
but numerically distinct transforms, and a family with an unattained tradeoff
limit.  
**Affected theorem nodes:** S5 as a supporting interface, candidate PIV-HRC1,
PIV-HRC4, and PIV-RW1; OQ-047, OQ-048, and OQ-054.  
**Blocking level:** P3; local order before quotient or Pareto theorems.

## 14. Mathematical and editorial risks

| Risk | Severity | Affected claim | Detection method | Mitigation |
| --- | --- | --- | --- | --- |
| Hidden partial-domain mismatch | High | PO-01 and every residual quotient | Compare the legal continuation sets of each proposed pair of pasts | Type the interface and common continuation class before defining \(\equiv_C\). |
| Composition-order or characteristic error | High | R-2 Horner count | Expand small words in both composition conventions and reduce in several characteristics | Fix chronology and use \(\mathbb Z\) or characteristic zero for the stated theorem. |
| Semantic category change | High | R-1 to Network AEG bridge | List input/output types before comparing the two \(2\times2\) actions | Keep the butterfly lemma local and require Network AEG plus a spinal restriction theorem. |
| Projective orientation error | High | Left-coset identity \(\mathsf B_\omega H=\mathsf B_1H\) | Multiply representatives and test left versus right quotient conventions | State the ordered reference pair, quotient side, and stabilizer explicitly. |
| Reverse-mode variance error | Medium | Comparison between AD and projective transport | Verify \(\langle\bar x_{i+1},Df_i\,\delta x_i\rangle=\langle Df_i^*\bar x_{i+1},\delta x_i\rangle\) and track arrow direction | Call the AD map a pullback and do not identify it with a global group inverse. |
| Cut/configuration collapse | High | Checkpointing and pebbling interpretation | Compare runs with the same ever-computed set but different live values | Maintain separate causal progress and live action trace. |
| Residual/address confusion | High | Tensor residual-size claim | Count both one multi-index and all dense coefficient values | Name component count, index width, and representation format separately. |
| Static/dynamic information mixing | High | NTT storage and entropy claims | Hold input variable and inspect which values change across runs | Charge algorithm description or constant storage separately from dynamic wire state. |
| Nonuniform hard-coding | High | Pareto complexity of one finite map | Allow an answer-table implementation and observe the collapse | State an input family and uniformity convention. |
| Bit/arithmetic-cost substitution | High | FFT/NTT work and multiplication claims | Recompute the bound after expanding each field operation into bit operations | Give encoding, field-size behavior, and arithmetic implementation. |
| Approximation and precision leakage | High | Transform-based integer multiplication | Trace padding, wraparound, rounding, reconstruction, and carry | State modulus or precision and prove exact reconstruction. |
| Schedule-unit ambiguity | Medium | \(T\), \(D_{\rm caus}\), and \(\operatorname{ST}\) | Re-evaluate one network under sequential and parallel schedules | Define the time unit and every charged snapshot. |
| Entropy without a measure | Medium | Horner and layer-state information | Ask whether a probability law is present | Declare the distribution or retain the log-cardinality name. |
| Section/gauge dependence | High | Projective process residue | Change the reference lift and calculate the \(H\)-coordinate transformation | State section or gauge, transformation law, and invariant class. |
| False holonomy | High | Rewrite-connection proposal | Sum edge labels on the associahedron and test for telescoping | Require PO-08 and PO-11 before curvature language. |
| Metric dependence | High | Rewrite distance, filling, and geometric cost | Change generators or edge weights and compare the numerical result | Fix the state graph, generators, metric, and simulation class. |
| Width-parameter transfer | Medium | Tensor, elimination, and proof width comparisons | Identify the exact primal, dual, incidence, or line graph in each theorem | Prove each graph-parameter comparison rather than transfer the name. |
| External-model overreach | High | Cross-domain HRC unification | Fill a model card with state, quotient, encoding, and cost for every domain | Treat examples as calibrations until each receives a cost-preserving bridge. |
| Unproved uniqueness or canonicity | High | Condensation representative and process residue | Change section, normal form, or encoding and look for multiple representatives | Separate existence, computability, shortestness, and gauge invariance. |
| Analytic-basis overstatement | Medium | R-10 affine–Appell interpretation | Test linear independence, function-space span, completeness, and convergence separately | Keep the result in Paper II and state only the finite lowering identities. |
| Finite-example generalization | High | \(\mathbb F_{257}\), \(N=8\), and \(N=16\) calculations | Compare the finite statement with the claimed asymptotic quantifiers | Label finite calculations and provide an independent family theorem. |
| Overwriting authoritative state | High | Candidate nodes and open questions | Search files 00–08 for an actual registered ID or decision | Keep candidate material explicitly non-authoritative. |

The highest-risk sentence pattern is still a causal verb connecting geometry
to complexity without a comparison theorem.  Phrases such as “curvature
causes memory,” “hyperbolic volume forces time,” or “projective residue is the
runtime state” are excluded from theorem-level prose.

## 15. Open questions

### 15.1 Existing authoritative Paper IV questions

The identifiers and status below are not changed by this working note.  All
remain Paper IV questions and do not block Paper I.

| ID | Question as used by this note | Priority | Blocks Paper I? | Required evidence | Likely destination | Relation to governance/08-open-questions.md |
| --- | --- | --- | --- | --- | --- | --- |
| OQ-047 | What is the exact category of histories? | P3 | No | Objects, partial arrows, composition, and relation or 2-cell structure | Paper IV | Existing OQ-047; referenced without change |
| OQ-048 | How are ordinary and projective histories separated? | P3 | No | Domain labels, separate categories or localization, and an evaluation comparison | Paper IV | Existing OQ-048; referenced without change |
| OQ-049 | Is projective process residue canonical? | P3 | No | A section-independent invariant or an explicit gauge law; a bare \(H\)-coordinate is insufficient | Paper IV | Existing OQ-049; referenced without change |
| OQ-050 | What semantic meaning, if any, should bivaluation receive? | P3 | No | An interpretation theorem beyond the algebraic projector correspondence | Paper IV | Existing OQ-050; referenced without change |
| OQ-051 | What exactly is condensation? | P3 | No | One explicit map or quotient at a time, with domain, codomain, and a universal property only if proved | Paper IV | Existing OQ-051; referenced without change |
| OQ-052 | Which measure quantifies lost information? | P3 | No | A selected fiber cardinality, orbit dimension, entropy, coding length, shortest representative, or stabilizer measure with hypotheses | Paper IV | Existing OQ-052; referenced without change |
| OQ-053 | When do canonical, computable, and shortest representatives exist? | P3 | No | Separate existence, algorithm, and optimality theorems | Paper IV | Existing OQ-053; referenced without change |
| OQ-054 | When does a geometric metric compare with computational cost? | P3 | No | State graph, encoding, generators, transition costs, simulation, and a proved comparison such as quasi-isometry | Paper IV | Existing OQ-054; referenced without change |
| OQ-055 | Can representation geometry organize time and space? | P3 | No | Model-specific lower and upper inequalities relating semantic residuals, live configurations, recomputation, and costs | Paper IV | Existing OQ-055; referenced without change |
| OQ-056 | What growth occurs in explicit AEG groups or semigroups? | P3 | No | Fixed generators and a proved polynomial, exponential, or intermediate growth result; no inference from noncommutativity alone | Paper IV | Existing OQ-056; referenced without change |
| OQ-057 | Is a history graph quasi-isometric to the hyperbolic AES model? | P3 | No | Explicit metrics, maps, and two-sided coarse bounds | Paper IV | Existing OQ-057; referenced without change |
| OQ-058 | Which case studies support actual cost theorems? | P3 | No | Explicit state space, metric, encoding, model, and reproducible result for each selected family | Paper IV | Existing OQ-058; referenced without change |

### 15.2 Candidate new questions from this discussion

Every row below has the required label “Candidate new open question; not yet
added to 08-open-questions.md.”  The candidate IDs are local handles only.

| Candidate | Question | Priority | Blocks Paper I? | Required evidence | Likely destination | Relation to governance/08-open-questions.md | Registration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CNOQ-01 | What categorical object represents a typed causal interface and all compatible continuations? | P3 | No | A network-history category or operadic/PROP formulation with partial-domain semantics | Paper IV definitions | Refines OQ-047, OQ-048, and OQ-051 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-02 | Under what conditions does projective process residue give a sufficient representation, quotient, or computable projection of a continuation residual? | P3 | No | A comparison map and a proof of soundness, completeness, or quantified information loss | Paper IV projective/HRC bridge | Refines OQ-049, OQ-051, and OQ-052 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-03 | What live-configuration semantics covers checkpointing, pebbling, proof blackboards, and reversible uncomputation without erasing domain-specific costs? | P3 | No | Cost-preserving simulations and counterexamples to over-unification | Paper IV operational model | Refines OQ-055 and OQ-058 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-04 | What symmetric monoidal category, PROP, or related structure defines Network AEG, and how does marked spinal AEG embed or restrict? | P3 | No | Typed ports, local gates, tensor/composition, evaluation, and a spinal comparison theorem | Paper IV network chapter | Refines OQ-047 and OQ-048 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-05 | How should static torus labels, generated constants, central scalar normalization, and dynamic states be charged in an FFT/NTT resource model? | P3 | No | Two finite audits and an asymptotic uniform-family convention | Paper IV case study | Refines OQ-054, OQ-055, and OQ-058 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-06 | Does any non-exact rewrite connection survive the telescoping obstruction on an explicit factorization 2-complex? | P3 | No | Group-valued transport with a gauge law and a computed closed-loop invariant | Paper IV or later relation theory | Refines OQ-047, OQ-049, and OQ-054 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-07 | Which tensor-contraction residuals are separated by all compatible future tests, and how do factored representations change materialization cost? | P3 | No | Kernel characterization and representation-sensitive bounds | Paper IV tensor case | Refines OQ-052, OQ-054, OQ-055, and OQ-058 | Candidate new open question; not yet added to 08-open-questions.md |
| CNOQ-08 | Which parts of HRC are new AEG structure rather than restatements of automata, communication, branching-program, and pebbling principles? | P3 | No | Formal translations, nontrivial invariants, and a case where projective data sharpens an existing bound | Paper IV framing | Refines OQ-054, OQ-055, and OQ-058 | Candidate new open question; not yet added to 08-open-questions.md |

## 16. Recommended next tasks

The tasks are ordered by dependency.  None authorizes a change to the
authoritative files 00–08; promotion requires a separate task and review.

### Task 1: Build the finite HRC calibration

**Goal:** Define one finite deterministic typed system with explicit pasts,
continuations, observables, residual classes, live configurations, and
compute/erase/recompute costs.  
**Allowed files:** One new calculation note under
governance/calculations/, preferably
governance/calculations/finite-hrc-model.md.  
**Forbidden files:** All paper bodies, README files, existing notes, and
governance/00-authoritative-scope.md through
governance/08-open-questions.md.  
**Theorem nodes:** Candidate PIV-HRC1, PIV-HRC2, PIV-HRC3, and PIV-HRC4,
explicitly non-authoritative.  
**Expected output:** Formal definitions, residual partition, state lower-bound
proof, at least two schedules, and exact
\(W,T,D_{\rm caus},S_{\max},\operatorname{ST}\) table.  
**Validation:** Exhaustive finite enumeration plus an independent hand proof.  
**Blocking questions:** PO-01–PO-03, DD-01–DD-05, OQ-047, OQ-048, OQ-051,
OQ-052, and OQ-055.

### Task 2: Run the Horner/OBDD dual calibration

**Goal:** Test loss of order under an ACS charge and exposure of residual
width under a variable order as two distinct mechanisms.  
**Allowed files:** The Task 1 calculation note or one dedicated new
calculation note approved at task time.  
**Forbidden files:** Paper bodies, README files, existing authoritative files
00–08, and unrelated discussion notes.  
**Theorem nodes:** G1 as the formal import; S5 as a supporting interface
outside the §77 export list; candidate PIV-HOR1, PIV-HRC2, and PIV-CUT1.  
**Expected output:** Characteristic-zero Horner charge-fiber count, formal
\(EQ_n\) block lower bound, explicit interleaved construction, and a table
separating residual cardinality, online state width, and static graph size.  
**Validation:** Enumerate small \(n\), test finite-characteristic collisions,
and prove the all-\(n\) statements.  
**Blocking questions:** PO-04, PO-07, DD-01, DD-03, and DD-09.  Neither
mechanism may be called curvature.

### Task 3: Audit the local butterfly and \(\mathbb F_{257}\) transforms

**Goal:** Close PO-05 and the finite part of PO-06 without claiming Network
AEG.  
**Allowed files:** One new reproducible calculation note and, if needed,
small scripts in a calculation-specific directory.  
**Forbidden files:** Paper bodies, authoritative files 00–08, existing legacy
notes, and the theorem dependency graph.  
**Theorem nodes:** P2 and T2 as imports; candidate PIV-NET1, PIV-NET2,
PIV-FFT1, and PIV-FFT2.  
**Expected output:** Determinant and left-coset verification, primitive-root
and root-of-unity table, \(N=8,16\) twiddle subgroup, inverse normalization,
cell/depth/state/storage table, and static/dynamic separation.  
**Validation:** Direct finite-field computation plus hand-checkable tables
and an independent inverse-transform test.  
**Blocking questions:** PO-05, PO-06, PO-10, DD-04–DD-07, CNOQ-04, and
CNOQ-05.  Use torus label, not phase connection.

### Task 4: Make the associahedron a negative calibration

**Goal:** Formalize endpoint-potential exactness and separate it from rewrite
distance, filling, action, and connection transport.  
**Allowed files:** One new calculation note or a new appendix to this
discussion note under a separately approved task.  
**Forbidden files:** Authoritative files 00–08, paper bodies, and unrelated
notes.  
**Theorem nodes:** Candidate PIV-RW1 and PIV-RW2; status item 92 as the
authoritative interface.  
**Expected output:** Five parenthesizations, dense-model costs, all local
rewrites, telescoping proof, and an example showing that positive accumulated
work is not holonomy.  
**Validation:** Symbolic edge-sum check on every orientation of the
five-cycle.  
**Blocking questions:** PO-08, PO-11, OQ-047, and CNOQ-06.

### Task 5: Validate the live-configuration layer

**Goal:** Compare one reverse-AD chain schedule with a selected black-pebble
game.  
**Allowed files:** One new calculation note and a small exhaustive scheduler
under a calculation-specific directory.  
**Forbidden files:** Authoritative files 00–08, paper bodies, and changes to
external-model definitions.  
**Theorem nodes:** Candidate PIV-HRC3, PIV-HRC4, and PIV-AD1; status item 100
as an interface.  
**Expected output:** Typed action traces, simulations, checkpoint and
recomputation accounting, and a Pareto table for small chains.  
**Validation:** Exhaustive optimal schedules for small \(N\), plus a precise
statement of the external checkpoint theorem imported.  
**Blocking questions:** PO-03, PO-10, DD-02, DD-05, CNOQ-03, and OQ-055.
Causal down-set, ever-computed set, and live set must stay separate.

### Task 6: Audit tensor, proof, reversible, and e-graph calibrations

**Goal:** Determine which examples instantiate contextual residuals and which
only motivate quotient compressibility or operational tradeoffs.  
**Allowed files:** One new literature-and-model audit note under
governance/calculations/ or governance/discussions/, chosen explicitly at
task time.  
**Forbidden files:** Authoritative files 00–08, paper bodies, external source
copies, and unrelated legacy notes.  
**Theorem nodes:** Candidate PIV-HRC1, PIV-HRC3, PIV-TN1, and PIV-PF1; no new
authoritative node.  
**Expected output:** One source-exact model card per domain with state space,
quotient, encoding, cost model, imported theorem, and missing AEG bridge.  
**Validation:** Primary-source checks and one counterexample to every proposed
over-generalization.  
**Blocking questions:** PO-09, PO-12, DD-01–DD-04, CNOQ-03, CNOQ-07,
CNOQ-08, and OQ-058.

### Task 7: Attempt rewrite transport only after Tasks 1–6

**Goal:** Test whether an explicit Cooley–Tukey factorization complex supports
a non-exact projective transport.  
**Allowed files:** One new calculation note and calculation-specific scripts
after Tasks 1–6 have reviewable outputs.  
**Forbidden files:** Authoritative files 00–08, Paper I, and any existing
theorem statement before the finite loop is verified.  
**Theorem nodes:** Candidate PIV-NET1, PIV-NET2, PIV-FFT2, and PIV-RW2; these
remain non-authoritative.  
**Expected output:** Rewrite 2-complex, edge labels, composition and gauge
laws, central-scalar treatment, loop calculation, and comparison with exact
endpoint labels.  
**Validation:** Gauge-change test, orientation reversal, explicit telescoping
control, and independent recomputation of the loop product.  
**Blocking questions:** PO-08, PO-11, DD-06, DD-07, CNOQ-06, OQ-047,
OQ-049, and OQ-054.  If all natural labels are coboundaries, record the
negative result and stop.

The immediate recommended task is Task 1.  It gives the framework a small
complete model before the more seductive FFT and geometric interpretations
are allowed to carry theoretical weight.

## 17. Source trace

### 17.1 Discussion trace

The mathematical source of this note is the ChatGPT discussion thread
immediately preceding the repository task, principally the following topic
blocks:

| Note section or claim | Discussion source | Related repository source |
| --- | --- | --- |
| §§2, 4.17, 7, and 9: volume, growth, and curvature limits | Topic block “representation volume, noncommutative order, and hyperbolic growth”; general volume-to-space inference rejected | notes/projective-condensation/note_06.tex, notes/projective-condensation/note_09.tex, notes/computation-and-resources/note_15.tex, and status items 95–99 |
| §§3, 4.2, 4.5, 6, and 13: projective process residue | Topic block “projective condensation and the \(G/H\) process residue”; noncanonical-section warning retained | notes/projective-condensation/bilateral_projective_condensation.tex and status items 82–92 |
| §4.4, R-2, and PO-04: binary Horner charge-fiber count | Topic block “binary Horner/ACS count”; characteristic-zero and probability qualifications added | G1 in governance/03-theorem-dependency-graph.md and ACS material mapped from sections/sec05.tex |
| §§4.5–4.6, R-1, R-8, PO-05, and PO-06: butterfly/NTT | Topic block “FFT/NTT butterfly and \(\mathbb F_{257}\) proposal”; local torus-coset lemma retained and static/dynamic data separated | OQ-058; no prior repository butterfly proof was located |
| §§4.15, 6, and 7: transform-dependent complexity | Topic block “representation-dependent complexity and large-integer multiplication”; padding, reconstruction, carry, precision, and bit cost added as gates | Complexity status items 93–99 and OQ-054–OQ-058 |
| §4.9, R-5, R-6, and PO-08: matrix chain and exactness | Topic block “matrix chain and associativity 2-cells”; endpoint differences shown to telescope | notes/projective-condensation/bilateral_projective_condensation.tex and status item 92 |
| §4.10, R-7, and PO-07: OBDD equality | Topic block “OBDD equality and variable order”; online width separated from static graph size | No repository proof; Bryant primary source is in §11.3 |
| §4.11, PO-03, and Task 5: reverse AD checkpointing | Topic block “reverse AD and checkpointing”; monotone cut replaced by live actions | notes/computation-and-resources/note_13.tex, notes/computation-and-resources/note_14.tex, status item 100, and the revolve source in §11.3 |
| §4.12 and PO-09: tensor residuals | Topic block “tensor contraction and boundary residuals”; index address separated from the complete residual tensor | OQ-052–OQ-055 and the Markov–Shi source in §11.3 |
| §4.13: proof space, reversible computation, and e-graphs | Topic block with the same name; retained as calibrations, not AEG equivalences | notes/computation-and-resources/note_13.tex, status item 100, and primary sources in §11.3 |
| §4.14 and Rejected formulation 12: order effects | Topic block “three proposed kinds of curvature”; renamed pending connection data | notes/projective-condensation/bilateral_projective_condensation.tex and status item 92 |
| §6.3 O-5, §13, and §16: Rosetta Stone graphs and Pareto costs | Topic block “Rosetta Stone graph family and resource Pareto object”; time/depth and rewrite geometry separated | notes/computation-and-resources/note_14.tex, notes/computation-and-resources/note_15.tex, and OQ-054–OQ-058 |
| §§1, 3, 4.18, 6, and 18: final HRC synthesis | Final discussion synthesis; rebuilt as semantic cut, operational realization, and rewrite fiber | Paper IV architecture in governance/01-paper-series-architecture.md and open questions OQ-047–OQ-058 |

The task context contained a compacted export rather than stable external
message identifiers for every earlier turn.  This note therefore uses
topic-level source markers and the discussion period in the front matter; it
does not fabricate message IDs or quotations.

### 17.2 Repository and external trace

The exact repository provenance is the source map in Section 11.  The status
of every established result is controlled by
governance/05-mathematical-status.md and the allowed vocabulary in
governance/06-editorial-rules.md.  Existing questions retain their
authoritative OQ-047–OQ-058 identifiers; CNOQ-01–CNOQ-08 are local candidates
only.

External results and their primary links are collected and cited in Section
11.3.  No secondary survey is used to promote a claim.
The attached task PDF is traced only as the artifact specification.

### 17.3 Transformations made during consolidation

The consolidation made the following material changes to the discussion:

1. replaced the proposed identity of representation, time, and space by
   comparison questions between semantic and operational layers;
2. replaced a single monotone cut schedule by causal interfaces plus live
   configurations;
3. split representation complexity into four quantities;
4. corrected the tensor boundary example;
5. changed butterfly fiber theorem to a local torus-coset lemma;
6. separated \(GL_2\), \(PGL_2\), and full \(GL_N\) network semantics;
7. separated static twiddle data from dynamic NTT states;
8. changed three curvatures to three order effects;
9. removed rewrite defect from a single implementation's resource vector;
10. promoted the telescoping obstruction to a central negative calibration;
11. added uniform-family, encoding, time-unit, and bit-cost gates;
12. kept all strong geometry-to-complexity implications in the rejected
    record.

These transformations are deliberate corrections, not merely editorial
shortening.

## 18. Final working position

The discussion supports a disciplined Paper IV program, not a theorem that
representation, time, space, curvature, and hardness are already one
quantity.

At the semantic layer, a typed causal interface together with an allowed
continuation class and an observable defines continuation residuals.  In a
finite deterministic exact model, their cardinality gives an information
lower bound on any online state that must support every allowed future.  The
bound is continuation-dependent and does not by itself measure an entire data
structure or physical workspace.

At the operational layer, a fixed uniform model explains how residual
information is encoded, materialized, retained, deleted, communicated, and
recomputed.  Work, scheduled time, causal depth, peak space, memory-time
volume, static description, and communication are distinct coordinates of a
model-dependent resource frontier.

At the rewrite layer, equal evaluations form an implementation fiber.
Rewrite distance and filling require their own generators and metric.
Endpoint cost differences are exact and cannot produce nontrivial holonomy;
any future connection must carry independent, gauge-controlled transport.

Binary Horner histories, the butterfly torus-coset lemma, matrix-chain
exactness, OBDD equality, and fixed radix-2 counts supply finite strict
calibrations.  Checkpointing, tensor contraction, proof space, reversible
computation, and e-graphs supply important external tests.  They have not yet
been proved to be instances of one AEG theorem.

The next blocking result is therefore a finite HRC model combining contextual
residuals with live configurations and exact resource accounting.  Only after
that calibration should Network AEG, FFT factorization loops, or projective
rewrite holonomy be promoted beyond structural proposals.
