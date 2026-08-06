# Three-Branch Projective Arithmetic, Tubes, and Complexity

**File:** `three-branch-arithmetic-tubes-and-complexity.md`  
**Status:** Working research note  
**Version:** 1.0  
**Date:** 2026-08-05  
**Discussion period:** 2026-07-25–2026-08-05  
**Primary topic:** The proposed relation among constant-curvature projective arithmetic, arithmetic-history tubes and knot questions, and representation-complexity growth  
**Primary paper interface:** CROSS-PAPER  
**Relevant theorem nodes:** `P2`, `T2`, `P3`, `P5`, `T5`, `T6`, `Z5`, `T8`, `Z6`, `T15`, `K3`, `T17`  
**Authority:** Subordinate to `restructure/00–08`; not itself authoritative

> This note condenses a research discussion into a reusable working document.
> It contains intermediate ideas, rejected formulations, and open questions.
> When it conflicts with the authoritative restructuring files, the latter prevail.

## 1. Executive summary

The discussion asked whether three recent AEG directions can be understood as different scales of one process-sensitive theory:

1. a flat–hyperbolic–spherical family of projective arithmetic;
2. parameter tubes, threading, braids, and possible knot invariants;
3. representation growth and its possible relation to computational complexity.

The strongest current conclusion is organizational, not theorem-level. The three directions can be arranged as

\[
\boxed{
\text{local process geometry}
\longrightarrow
\text{global topological transport}
\longrightarrow
\text{asymptotic history growth}.
}
\]

The proposed common theme is the information retained above a condensed result: locally it may appear as a connection defect or curvature; around a closed parameter path it may appear as monodromy or holonomy; asymptotically it may appear as the growth and normalization cost of history fibers. No theorem currently proves that one cocycle controls all three levels.

The decisive correction is that several superficially similar structures must remain separate:

- the affine AEG generators \(E=\partial_z\) and \(H_{\mathrm{Lie}}=z\partial_z\) are not the symmetric primitive pair of the proposed three-branch completion; that proposal instead uses \(E\) and \(F=z^2\partial_z\), with \(H_{\mathrm{Lie}}\) produced by \([E,F]=2H_{\mathrm{Lie}}\);
- the constant-curvature quotient \(G_c/L_c\), whose isotropy is rotation-like, is not the same quotient as the ordered-pair stabilizer quotient in the bilateral condensation note;
- a history fiber over an operator or quotient state is not the same object as the total zero set of a parameterized assignment family;
- a local-section residue is not yet a canonical holonomy, and a threaded tube is not yet a knot invariant;
- growth, equivalence proof cost, search cost, time, and space are distinct quantities.

The paper consequence is clear. Paper I supplies only the affine, zero-set, and contact foundations. The full three-real-form and process-residue theory belongs primarily to Paper IV; analytic operators on the branches belong to Paper II; tubes, braids, threading, and knot questions belong to Paper III; explicit complexity metrics and cost comparisons belong to Paper IV.

The first blocking mathematical problem is the negative-curvature comparison. One must show, by an explicit Cayley transform and Iwasawa-type calculation, whether the proposed \(U(1)\)-valued frame residue is related by a well-defined bundle or connection map to the existing affine/contact defects of AEG. Without that bridge, the three-branch construction is an adjacent projective arithmetic geometry, not yet a unification of current AEG.

## 2. Starting intuition

The initial intuition was that the hyperbolic growth law already present in AEG,

\[
a(s)=\frac{\mu}{\lambda}\sinh(\lambda s),
\]

suggests a flat–hyperbolic–spherical trichotomy. The limiting or formally continued expressions

\[
\sinh(\lambda s),\qquad s,\qquad \sin(\kappa s)
\]

look like three curvature branches of one mechanism. The intended payoff was not merely a uniform PDE, but a common arithmetic process whose different real forms produce the three geometries.

The first proposed mechanism treated addition and multiplication as the common primitive directions and varied the multiplicative parameter through real, zero, and imaginary values. At that stage, the implication

\[
\lambda\mapsto i\kappa
\quad\Longrightarrow\quad
\text{spherical arithmetic}
\]

had not been proved. The discussion later rejected it as insufficient: a complex affine update \(z\mapsto e^{i\kappa t}z+b\) gives a Euclidean rotation–translation structure, not the sphere.

The corrected projective intuition was to complete the affine Lie algebra

\[
E=\partial_z,
\qquad
H_{\mathrm{Lie}}=z\partial_z
\]

to the projective triple

\[
E=\partial_z,
\qquad
H_{\mathrm{Lie}}=z\partial_z,
\qquad
F=z^2\partial_z.
\]

At the symmetric level, the candidate displacement direction is

\[
P_\xi^c=\xi E+c\bar\xi F,
\]

where the discussion used \(K\) for the real curvature parameter. This note renames that parameter \(c\) because the repository already uses \(K\) for the base field in \(PGL_2(K)\), while \(\kappa\) is also used for the quadratic coefficient in the Riccati flow.

The tube intuition arose independently. A parameterized family of assignment functions may form a total zero set, and branch transport may produce permutations, braids, or threaded closures. The intended payoff was an AEG-specific topological object or invariant, not merely a visual realization of a known knot.

The complexity intuition was that expression histories proliferate before they are condensed to operators, normal forms, or endpoint values. The intended payoff was a representation geometry from which search, time, and space costs might be derived. The initial implicit assumptions—that noncommutativity forces exponential growth, that exponential growth forces hyperbolicity, and that hyperbolicity signals computational hardness—were subsequently rejected as general implications.

The final strategic intuition is therefore more restrained:

> AEG may study how process information is forgotten by evaluation, how some of it survives closed transport, and how the remaining fibers grow with history length.

This is a research program. The local, global, and asymptotic manifestations have not yet been identified as one mathematical invariant.

## 3. Objects and notation

The table distinguishes notation adopted only for this note from established repository notation.

| Object | Meaning | Status | Paper owner | Notes |
| --- | --- | --- | --- | --- |
| \(\Bbbk\) | Base field for projective arithmetic | `PROVED WITH STATED HYPOTHESES` as imported projective data | Papers I and IV | The authoritative files normally write this field as \(K\). The temporary symbol \(\Bbbk\) prevents collision with the discussion's curvature parameter. |
| \(c\in\mathbb R\) | Curvature/deformation parameter | `STRUCTURAL PROPOSAL` | Paper IV | Written as \(K\) in the discussion. Sign convention: \(c>0\) spherical, \(c=0\) flat, \(c<0\) hyperbolic. This convention requires audit against metric normalization. |
| \(E,H_{\mathrm{Lie}},F\) | Projective vector fields \(\partial_z,z\partial_z,z^2\partial_z\) | `PROVED` as the local projective Lie-algebra basis; full geometry incomplete | Papers I and IV | Paper I owns only the affine slice \(\operatorname{span}\{E,H_{\mathrm{Lie}}\}\); Paper IV owns the full completion. |
| \(\mathbb A_c\) | \(\mathbb R[\jmath_c]/(\jmath_c^2+c)\) | `STRUCTURAL PROPOSAL` with an exact one-dimensional product identity | Paper IV | This is a one-dimensional geodesic/addition model. It does not by itself produce the two-dimensional Hermitian model. |
| \(\mathsf T_\xi^c\) | \(z\mapsto (z+\xi)/(1-c\bar\xi z)\) | `STRUCTURAL PROPOSAL`; exact where the denominator and matrix class are defined | Paper IV | Ordinary arithmetic and projective continuation must remain distinguished. |
| \(M_c(\xi)\) | \(\begin{psmallmatrix}1&\xi\\-c\bar\xi&1\end{psmallmatrix}\) | `PROVED WITH STATED HYPOTHESES` as an exact matrix representative for \(\mathsf T_\xi^c\) | Paper IV | Normalization, determinant restrictions, and composition order require explicit conventions. |
| \(G_c\) | Proposed orientation-preserving isometry group of the constant-curvature branch | `STRUCTURAL PROPOSAL` until defined precisely | Paper IV | If defined as \(\langle M_c(\xi)\rangle\), the flat case gives only translations. To obtain \(SE(2)\), rotation isotropy must be added or \(G_c\) must be defined independently as the full isometry group. |
| \(L_c\) | Isotropy subgroup of a basepoint in \(G_c\), expected to be \(SO(2)\simeq U(1)\) | `STRUCTURAL PROPOSAL` | Paper IV | This replaces the ambiguous use of \(H\) for the constant-curvature stabilizer. |
| \(H_{\mathrm{pair}}\) | Stabilizer of an ordered distinct point pair in the bilateral quotient tower | `PROVED WITH STATED HYPOTHESES` as a homogeneous-space identification | Paper IV | Generally split-torus-like; it is not \(L_c\). |
| \(X_c=G_c/L_c\) | Constant-curvature homogeneous surface | `STRUCTURAL PROPOSAL` pending the group definition | Paper IV; analytic use in Paper II | Must not be identified without proof with the bilateral ordered-pair quotient. |
| \(r_c(\xi,\eta)\) | Two-step local-section residue \((1-c\xi\bar\eta)/(1-c\bar\xi\eta)\) | `PROVED WITH STATED HYPOTHESES` as an exact algebraic factor | Paper IV | The discussion wrote \(\rho_c\), but \(\rho\) is reserved for history evaluation. The factor is \(U(1)\)-valued for real \(c\), but is not yet a canonical holonomy or curvature invariant. |
| \(g_c\) | Candidate metric \(4\lvert dz\rvert^2/(1+c\lvert z\rvert^2)^2\) | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` for the metric identities; AEG interpretation remains a `STRUCTURAL PROPOSAL` | Papers II and IV | Standard constant-curvature metric on its appropriate chart/domain; normalization and AEG compatibility remain to be integrated. |
| \(a_c\) | Candidate assignment \(2\mu\operatorname{Im}z/(1+c\lvert z\rvert^2)\) | `STRUCTURAL PROPOSAL` | Cross-paper bridge | The \(c<0\) branch is intended to recover \(a=-x/y\) after a Cayley transform; the bridge is not written in the repository. |
| \(D_u,D_v\) | Existing horizontal lifts \(\partial_u+\mu\partial_a\), \(\partial_v+\lambda a\partial_a\) | `PROVED` | Paper I | Their bracket is \([D_u,D_v]=\mu\lambda\partial_a\). |
| \(\mathsf{Hist}\) | Marked arithmetic histories or a future history groupoid | `STRUCTURAL PROPOSAL` beyond the marked-history core | Papers I and IV | Objects, arrows, domains, and equality levels must be fixed. |
| \(\rho:\mathsf{Hist}\to G\) | Evaluation from histories to operators | `STRUCTURAL PROPOSAL` as a functor; individual evaluations exist | Paper IV | This retains the bilateral-note notation and is distinct from \(r_c\). |
| \(\mathcal Z\) | Total zero set \(\{(p,t):a_t(p)=0\}\) | `STRUCTURAL PROPOSAL` as a family object; regularity is a `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | Papers I and III | This is the parameter-family object underlying a possible zero tube. |
| thread | A section, embedded curve, zero branch, marked history, or decoration | `OPEN PROBLEM` | Paper III | OQ-044 records that no canonical definition has been selected. |
| \(W(n)\) | Number of raw histories of length at most \(n\) | `STRUCTURAL PROPOSAL` | Paper IV | Requires a finite alphabet or another finiteness convention. |
| \(N_\rho(n)\) | Number of distinct evaluated operators/process states; written \(G(n)\) in the discussion | `STRUCTURAL PROPOSAL` | Paper IV | Renamed here to avoid collision with group notation. |
| \(M_\rho(n)\) | Maximum history-fiber multiplicity; written \(F(n)\) in the discussion | `STRUCTURAL PROPOSAL` | Paper IV | Renamed here to avoid collision with the projective generator \(F\). |
| \(D_{\mathcal R}(n)\) | Rewriting or filling cost for an explicitly chosen relation system \(\mathcal R\) | `STRUCTURAL PROPOSAL` | Paper IV | Must be distinguished from algorithm runtime and from a group Dehn function unless the definitions coincide. |

Three maps must remain visibly distinct:

\[
\mathsf{Hist}
\longrightarrow
G
\longrightarrow
G/H_{\mathrm{pair}}
\longrightarrow
G/B,
\]

and

\[
G_c
\longrightarrow
G_c/L_c=X_c,
\]

and

\[
\mathcal Z
\xrightarrow{\ \pi\ }
\Lambda.
\]

The first forgets process information through operator and quotient maps. The second is the proposed constant-curvature frame bundle. The third is a parameterized zero-locus family. A future theorem may relate them through real-form orbit decompositions, pullbacks, or comparison functors, but they are not the same fibration by definition.

## 4. Development of the argument

### 4.1 From affine AEG to a symmetric projective completion

Paper I's continuous theory uses the affine generators

\[
E=\partial_z,
\qquad
H_{\mathrm{Lie}}=z\partial_z,
\]

and the flow

\[
\dot a=\mu\cos\theta+\lambda a\sin\theta.
\]

The bilateral note places this affine theory in the Borel sector of projective arithmetic and supplies the missing quadratic direction

\[
F=z^2\partial_z.
\]

The exact local bracket is

\[
[E,F]=2H_{\mathrm{Lie}}.
\]

This led to the corrected structural proposal: the symmetric displacement primitives are \(E\) and an inversion-conjugate direction \(F\), while the affine scaling direction \(H_{\mathrm{Lie}}\) is recovered as their commutator. This does not invalidate the add–multiply description inside the affine chart; it changes the primitive pair only at the proposed three-branch projective level.

**Status:** The Lie-algebra identity is `PROVED`. Its interpretation as the common arithmetic origin of all three branches is a `STRUCTURAL PROPOSAL`.

### 4.2 One-dimensional quadratic-algebra model

The discussion proposed

\[
\mathbb A_c
=
\mathbb R[\jmath_c]/(\jmath_c^2+c).
\]

The exact multiplication

\[
(1+q\jmath_c)(1+r\jmath_c)
=
(1-cqr)+(q+r)\jmath_c
\]

gives, after projective normalization by \(1-cqr\neq0\),

\[
q\oplus_c r
=
\frac{q+r}{1-cqr}.
\]

This is an exact algebraic identity on the stated chart. For \(c>0\), \(c=0\), and \(c<0\), the quadratic algebra is respectively complex-like, dual-number-like, and split-complex-like after rescaling.

**Correction:** This one-dimensional law does not itself yield the full two-dimensional Möbius displacement with complex parameter \(\xi\). The latter additionally uses complex conjugation and a Hermitian real form. The passage from \(\mathbb A_c\) to the two-dimensional homogeneous surface remains to be defined.

### 4.3 Two-dimensional Möbius displacement

The proposed displacement is

\[
\mathsf T_\xi^c(z)
=
\frac{z+\xi}{1-c\bar\xi z},
\qquad
M_c(\xi)
=
\begin{pmatrix}
1&\xi\\
-c\bar\xi&1
\end{pmatrix}.
\]

For a small real parameter \(t\),

\[
\mathsf T_{t\xi}^c(z)
=
z+t\bigl(\xi+c\bar\xi z^2\bigr)+O(t^2),
\]

so the infinitesimal direction is

\[
P_\xi^c
=
\xi E+c\bar\xi F.
\]

Consequently,

\[
[P_\xi^c,P_\eta^c]
=
2c(\xi\bar\eta-\eta\bar\xi)H_{\mathrm{Lie}}.
\]

The expansion is local and asymptotic in \(t\). The bracket identity is exact in the projective Lie algebra after the vector fields and bracket convention are fixed.

The determinant

\[
\det M_c(\xi)=1+c|\xi|^2
\]

must be tracked. In the hyperbolic branch \(c<0\), the standard disk chart excludes the degeneracy locus \(|\xi|=1/\sqrt{-c}\). Ordinary domains, projective charts, and boundary points must be stated separately.

### 4.4 Bilateral realization

The Möbius displacement is not an operation added from outside the existing bilateral language. The authoritative projective-generation theorem states that translations, nonzero dilations, and inversion generate \(PGL_2(\Bbbk)\). For real \(t\), \(ct\neq0\), \(1+ct^2\neq0\), and the right-to-left function-composition convention, the discussion recorded the exact decomposition

\[
\mathsf T_t^c
=
A_{-1/(ct)}
\circ
D_{(1+ct^2)/(c^2t^2)}
\circ
J
\circ
A_{-1/(ct)},
\]

where

\[
A_b(z)=z+b,
\qquad
D_s(z)=sz,
\qquad
J(z)=-\frac1z.
\]

This is an exact chart formula. It establishes existence of a bilateral word for this real-axis case, not a canonical or shortest history. The complex-parameter version, ordinary admissibility of every intermediate step, minimal word length, and compatibility with the final chronological convention remain open integration tasks.

### 4.5 Two-step residue

Direct multiplication gives

\[
M_c(\xi)M_c(\eta)
\sim
M_c(\xi\oplus_c\eta)
\begin{pmatrix}
r_c(\xi,\eta)&0\\
0&1
\end{pmatrix},
\]

with

\[
\xi\oplus_c\eta
=
\frac{\xi+\eta}{1-c\bar\xi\eta},
\qquad
r_c(\xi,\eta)
=
\frac{1-c\xi\bar\eta}{1-c\bar\xi\eta}.
\]

For real \(c\), the numerator and denominator are complex conjugates, so

\[
|r_c(\xi,\eta)|=1
\]

when the denominator is nonzero. Its small-increment expansion is

\[
r_c(\xi,\eta)
=
1-2ic\,\operatorname{Im}(\xi\bar\eta)
+O(|\xi\eta|^2).
\]

For \(\xi=r\), \(\eta=ir\),

\[
r_c(r,ir)
=
\frac{1+icr^2}{1-icr^2}
=
\exp\!\bigl(2i\arctan(cr^2)\bigr).
\]

The matrix factorization is exact under the displayed multiplication convention. The expansion is asymptotic. The phrase “curvature is the frame residue” is not yet a theorem. The factor \(r_c\) is the section-composition factor for the chosen local section \(\xi\mapsto M_c(\xi)\); a change of section changes the open two-step residue. Whether it satisfies an appropriate twisted or nonabelian cocycle identity remains a proof obligation. A connection and its gauge law must be specified before extracting canonical curvature or closed-loop holonomy.

### 4.6 Candidate three branches

The proposed homogeneous-space classification is

\[
\begin{aligned}
c>0 &: \quad G_c\simeq PSU(2),\\
c=0 &: \quad G_c\simeq SE(2),\\
c<0 &: \quad G_c\simeq PSU(1,1)\simeq PSL_2(\mathbb R),
\end{aligned}
\qquad
X_c\simeq G_c/L_c,
\]

with \(L_c\simeq SO(2)\). This formulation repairs two ambiguities in the discussion:

1. \(E(2)\) includes orientation-reversing isometries, while the connected projective family naturally suggests \(SE(2)\);
2. the matrices \(M_0(\xi)\) alone generate only translations, so rotations must be explicitly included or \(G_0\) must be defined as the full orientation-preserving isometry group from the outset.

The candidate metric and assignment are

\[
g_c
=
\frac{4|dz|^2}{(1+c|z|^2)^2},
\qquad
a_c(z)
=
\frac{2\mu\operatorname{Im}z}{1+c|z|^2}.
\]

On the appropriate chart, direct coordinate calculation gives

\[
K_{g_c}=c,
\qquad
|\nabla a_c|_{g_c}^2=\mu^2-ca_c^2,
\qquad
\Delta_{g_c}a_c=-2ca_c,
\]

where the final sign uses \(\Delta=\operatorname{div}\nabla\). These calculations have not yet been integrated as AEG results; the canonical regular-AES definition remains open.

They have the intended qualitative behavior:

- \(c=0\): affine accumulation on the plane;
- \(c<0\): disk geometry with boundary growth;
- \(c>0\): a spherical chart, bounded assignment, chart passage through \(\infty\), and periodic frame behavior.

These qualitative readings are proposals until the domain, metric normalization, AES equation, global chart behavior, and group action are verified. In particular, the bare complex group \(PGL_2(\mathbb C)\) does not distinguish the compact and split real forms. Complex conjugation, a Hermitian form, or an equivalent involution is additional data. The occurrence of \(\bar\xi\) records that extra structure; it must not be identified with operand-slot mirror.

### 4.7 The negative-branch bridge

The proposed three-branch family becomes an extension of current AEG only if the branch \(c<0\) recovers the established affine/hyperbolic model and its process defects.

The base-space part of the comparison is an exact derivable calculation. Let \(c=-\lambda^2\), let \(w\) be the disk coordinate, set \(\zeta=\lambda w\), and put

\[
Z=X+iY=\frac{x}{\mu}+i\frac{y}{\lambda},
\qquad
\zeta=\frac{Z-i}{Z+i}.
\]

Then one obtains

\[
\frac{4|dw|^2}{(1-\lambda^2|w|^2)^2}
=
\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
\]

and

\[
\frac{2\mu\operatorname{Im}w}{1-\lambda^2|w|^2}
=
-\frac{x}{y}.
\]

These identities were identified in the discussion audit but have not been written into a repository proof. They recover the metric and assignment layers of the basic upper-half-plane model.

They do not recover the process layer automatically. The current arithmetic-grid maps are naturally expressed as right actions in affine \(AN\) coordinates, while standard Iwasawa \(N\), \(A\), and rotation components are often read through a left action. Symmetric-space transvections have brackets in compact isotropy; the established affine arithmetic directions bracket inside the solvable algebra. The next calculation must therefore compare the left/right conventions and explicitly intertwine the generators before comparing contact or finite-holonomy data.

The central category mismatch remains:

- the new two-step residue is rotation- or phase-valued in \(L_c\simeq U(1)\);
- the existing contact bracket is vertical in the assignment fiber,
  \([D_u,D_v]=\mu\lambda\partial_a\);
- the existing affine/ACS defects are translation-valued after compatible linear parts are fixed.

No equality among these quantities is authorized. A comparison bundle map, connection morphism, or common infinitesimal representation must be constructed. Success would make the three branches a genuine projective completion of AEG; failure would leave a mathematically coherent neighboring theory.

### 4.8 From local geometry to tube topology

For a smooth family \(a_t\), the total zero set is

\[
\mathcal Z
=
\{(p,t):a_t(p)=0\}.
\]

Paper I may establish only the regular-value and projection-submersion statements. Properness, boundary control, and singularity analysis are required before \(\mathcal Z\to\Lambda\) becomes a locally trivial tube. A braid requires collision-free transport of embedded branches over loops in the discriminant complement. A knot requires a closure construction and the appropriate equivalence theorem.

The discussion's strategic judgment was that this direction has the highest AEG-specific originality ceiling. The three-branch construction largely reorganizes classical elliptic–parabolic–hyperbolic and real-form material unless it is derived internally from arithmetic history. By contrast, an arithmetic-history transport that is intrinsically selected and proved choice-independent, and that yields a Markov-stable quantity, could produce a genuinely new external mathematical result.

That ceiling is not yet realized. The current status remains:

\[
\text{tube intuition}
\longrightarrow
\text{threading proposal}
\longrightarrow
\text{invariance obligations},
\]

not a knot invariant.

### 4.9 From history growth to complexity

Let \(B_n\) denote histories of length at most \(n\) in a finitely specified history language. The discussion proposed four different quantities:

\[
W(n)=|B_n|,
\]

\[
N_\rho(n)=|\rho(B_n)|,
\]

\[
M_\rho(n)
=
\max_g|\rho^{-1}(g)\cap B_n|,
\]

and a rewriting or filling cost

\[
D_{\mathcal R}(n)
=
\max_{\substack{\rho(u)=\rho(v)\\|u|+|v|\le n}}
\ \min
\bigl\{
\operatorname{cost}_{\mathcal R}(u\Rightarrow v)
\bigr\},
\]

provided the maxima and minima exist. This is a candidate pairwise rewrite definition; it equals a group Dehn function only under additional presentation-specific identifications.

They ask different questions:

| Quantity | Question |
| --- | --- |
| \(W(n)\) | How many histories can be written? |
| \(N_\rho(n)\) | How many operator or process states remain distinguishable? |
| \(M_\rho(n)\) | How many histories can condense to one state? |
| \(D_{\mathcal R}(n)\) | What proof, rewriting, or filling cost is needed to identify equivalent histories? |

This repairs the earlier conflation of syntactic branching, quotient growth, equality proof, search, and runtime. All four definitions still depend on a generating set, encoding, domain, and equality relation. With continuous operands the cardinalities may be infinite, so a finite alphabet, bounded encoding, measure-theoretic version, or metric entropy must be selected.

The recommended calibration family is

\[
\mathbb Z^2,
\qquad
\text{the discrete Heisenberg group},
\qquad
F_2,
\qquad
BS(1,2).
\]

These separate commutativity from growth, noncommutativity from exponential growth, exponential growth from word-problem hardness, and affine scaling distortion from free branching. Time and space comparisons require an additional computational model, such as an explicit state graph or pebble game.

### 4.10 Proposed synthesis

The discussion ended with the following cross-paper program:

\[
\text{infinitesimal defect}
\quad\rightsquigarrow\quad
\text{closed transport residue}
\quad\rightsquigarrow\quad
\text{history-fiber growth}.
\]

At present, \(\rightsquigarrow\) denotes a research interface, not an implication. The objects on the three levels live in different categories, and no common cocycle has been constructed. The synthesis will be substantive only if a single defined process cocycle, or a functorially related family of cocycles, yields:

1. the local affine/contact curvature already present in Paper I;
2. a well-defined tube or braid holonomy in Paper III;
3. a controlled orbit or fiber-growth quantity in Paper IV.

If the three levels remain analogical, they should be presented as separate but mutually motivating directions.

## 5. Established results

This section records only exact calculations completed in the discussion, imported authoritative results, or standard consequences whose missing integration proof is explicitly acknowledged. None of the items below proves the strong three-scale unification.

### Result R-1: Bilateral generation of projective transformations

**Status:** `PROVED WITH STATED HYPOTHESES`  
**Statement:** Non-degenerate projective evaluations of bilateral arithmetic spinal histories generate \(PGL_2(\Bbbk)\).  
**Hypotheses:** Field and non-degeneracy assumptions from `T2`; nonzero determinant; separately treated cases \(C=0\) and \(C\neq0\); adopted matrix action and chronological composition conventions.  
**Argument or proof location:** The decomposition
\[
\frac{Az+B}{Cz+D}
=
T_{A/C}\circ D_{(AD-BC)/C^2}\circ J\circ T_{D/C}
\]
for \(C\neq0\), together with the affine case \(C=0\).  
**Repository source:** `../../notes/bilateral_projective_condensation.tex`, “Projective evaluation”; status audited in `../05-mathematical-status.md`, §16.  
**Relevant theorem nodes:** `P1`, `P2`, `T2`.  
**Paper destination:** Concise theorem in Paper I; full projective use in Paper IV.  
**Remaining integration work:** Resolve OQ-002–OQ-004; audit characteristic two, signs, scalar equivalence, and ordinary intermediate domains. The theorem gives existence of a word, not a canonical or shortest history.

### Result R-2: Affine/Borel sector and local Riccati completion

**Status:** `PROVED`  
**Statement:** The stabilizer of \(\infty\) in \(PGL_2(\Bbbk)\) is the affine group, and the local projective vector fields
\[
E=\partial_z,
\qquad
H_{\mathrm{Lie}}=z\partial_z,
\qquad
F=z^2\partial_z
\]
span the local Riccati flow
\[
\dot z=\beta+\alpha z+\kappa z^2.
\]
**Hypotheses:** The exact history sublanguage and action domain must be stated; the geometric completion beyond the Lie algebra is not included.  
**Argument or proof location:** The affine stabilizer calculation and the inversion-conjugated translation expansion \(JT_sJ^{-1}(z)=z/(1-sz)=z+sz^2+\cdots\).  
**Repository source:** `../../notes/bilateral_projective_condensation.tex`; `../05-mathematical-status.md`, §§17 and 20.  
**Relevant theorem nodes:** `P3`, `P5`, `F1`.  
**Paper destination:** Paper I for the affine sector and brief Riccati placement; Paper IV for the full projective geometry.  
**Remaining integration work:** Do not infer a projective AES, projective metric, contact connection, or three-real-form theorem from this local statement.

### Result R-3: Projectivized quadratic-algebra addition law

**Status:** `PROVED WITH STATED HYPOTHESES`  
**Statement:** In \(\mathbb A_c=\mathbb R[\jmath_c]/(\jmath_c^2+c)\),
\[
(1+q\jmath_c)(1+r\jmath_c)
=
(1-cqr)+(q+r)\jmath_c,
\]
and, on the chart \(1-cqr\neq0\), projective normalization gives
\[
q\oplus_c r=\frac{q+r}{1-cqr}.
\]
**Hypotheses:** \(c,q,r\in\mathbb R\); the normalizing scalar is nonzero; points at which it vanishes require a separate projective chart.  
**Argument or proof location:** Exact multiplication displayed in the three-branch discussion.  
**Repository source:** Current discussion only; no pre-existing repository source was found.  
**Relevant theorem nodes:** No registered node; conceptually adjacent to `P5`.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Define its relation to bilateral syntax and to the two-dimensional Hermitian displacement model. This one-dimensional identity does not establish the three-branch surface theory.

### Result R-4: Infinitesimal projective displacement and bracket

**Status:** `PROVED WITH STATED HYPOTHESES`  
**Statement:** For
\[
\mathsf T_{t\xi}^c(z)=\frac{z+t\xi}{1-ct\bar\xi z},
\]
the first-order vector field is
\[
P_\xi^c=\xi E+c\bar\xi F,
\]
and
\[
[P_\xi^c,P_\eta^c]
=
2c(\xi\bar\eta-\eta\bar\xi)H_{\mathrm{Lie}}.
\]
**Hypotheses:** Local chart away from the denominator pole; real \(t\) near zero; the stated vector-field bracket convention.  
**Argument or proof location:** First-order expansion and \([E,F]=2H_{\mathrm{Lie}}\).  
**Repository source:** Current discussion; the \(E,H_{\mathrm{Lie}},F\) basis is imported from `../../notes/bilateral_projective_condensation.tex`.  
**Relevant theorem nodes:** `P5`.  
**Paper destination:** Paper IV; at most a short outlook in Paper I.  
**Remaining integration work:** Determine whether these vector fields arise from specified arithmetic history primitives rather than only from projective dynamics.

### Result R-5: Real-axis bilateral realization of the displacement

**Status:** `PROVED WITH STATED HYPOTHESES`  
**Statement:** Under right-to-left function composition,
\[
\mathsf T_t^c
=
A_{-1/(ct)}
\circ
D_{(1+ct^2)/(c^2t^2)}
\circ
J
\circ
A_{-1/(ct)}.
\]
**Hypotheses:** \(c,t\in\mathbb R\), \(ct\neq0\), and \(1+ct^2\neq0\). The last condition is the determinant/nonzero-dilation condition and excludes the hyperbolic-chart boundary.  
**Argument or proof location:** Specialization of the `T2` Möbius decomposition.  
**Repository source:** Current discussion, using the proof pattern in `../../notes/bilateral_projective_condensation.tex`.  
**Relevant theorem nodes:** `T2`.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Treat \(c=0\), \(t=0\), and complex \(\xi\) separately; audit ordinary admissibility and composition order; do not call this word canonical or minimal.

### Result R-6: Exact two-step section-composition residue

**Status:** `PROVED WITH STATED HYPOTHESES`  
**Statement:** Put
\[
d=1-c\bar\xi\eta,
\quad
n=1-c\xi\bar\eta,
\quad
\zeta=\frac{\xi+\eta}{d},
\quad
r_c(\xi,\eta)=\frac nd.
\]
Then
\[
M_c(\xi)M_c(\eta)
=
d\,M_c(\zeta)
\begin{pmatrix}
r_c(\xi,\eta)&0\\
0&1
\end{pmatrix}.
\]
For real \(c\) and \(d\neq0\), \(|r_c|=1\).  
**Hypotheses:** Exact displayed matrix convention; \(d\neq0\); projective matrices non-degenerate; multiplication order fixed.  
**Argument or proof location:** Direct matrix multiplication in the discussion.  
**Repository source:** Current discussion only.  
**Relevant theorem nodes:** No registered node; adjacent to `P2`, `P5`, and Paper IV status entries §§83 and 88.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Derive the transformation under a change of local section; decide whether the invariant object is an element, a conjugacy class, a curvature form, or only a closed-loop quantity. No cocycle or holonomy status is yet authorized.

### Result R-7: Constant-curvature metric and assignment identities

**Status:** `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`  
**Statement:** On the chart where
\[
g_c=\frac{4|dz|^2}{(1+c|z|^2)^2},
\qquad
a_c=\frac{2\mu\operatorname{Im}z}{1+c|z|^2}
\]
are defined, direct coordinate calculation gives
\[
K_{g_c}=c,
\qquad
|\nabla a_c|_{g_c}^2=\mu^2-ca_c^2,
\qquad
\Delta_{g_c}a_c=-2ca_c
\]
for the convention \(\Delta=\operatorname{div}\nabla\).  
**Hypotheses:** Real \(c\); the disk domain \(|z|<1/\sqrt{-c}\) when \(c<0\); a separate spherical chart at \(\infty\) when \(c>0\); fixed Laplacian sign; sufficient smoothness.  
**Argument or proof location:** Standard conformal-coordinate calculation identified during the discussion; not yet written as a repository proof.  
**Repository source:** None for the three-branch family. The target negative-branch identities are consistent with `../../sections/sec04.tex`.  
**Relevant theorem nodes:** `E1`, `F3`, `T6`, `E3`, subject to OQ-001.  
**Paper destination:** Paper IV for the projective family; Paper II for analytic use; comparison statement at the Paper I/IV interface.  
**Remaining integration work:** Write the calculation, state domains and global extension, and prove the framed-flow axioms rather than only the eikonal identity. This item is not yet an AEG theorem because the primitive regular-AES definition remains open.

### Result R-8: Exact negative-branch base-space comparison is derivable

**Status:** `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`  
**Statement:** Let \(c=-\lambda^2\), let \(w\) be the disk coordinate, set \(\zeta=\lambda w\), and use dimensionless upper-half-plane coordinate
\[
Z=X+iY=\frac{x}{\mu}+i\frac{y}{\lambda},
\qquad
\zeta=\frac{Z-i}{Z+i}.
\]
Then the following exact identities are derivable:
\[
\frac{4|dw|^2}{(1-\lambda^2|w|^2)^2}
=
\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
\]
and
\[
\frac{2\mu\operatorname{Im}w}{1-\lambda^2|w|^2}
=
-\frac{x}{y}.
\]
**Hypotheses:** \(\mu\lambda\neq0\); consistent Cayley orientation and coordinate scaling; disk and upper-half-plane interiors.  
**Argument or proof location:** Algebraic calculation identified during the discussion but not inserted into a repository source.  
**Repository source:** Target comparison with `../../sections/sec04.tex`, basic upper-half-plane model.  
**Relevant theorem nodes:** `T6`, `E3`; the process comparison also interfaces with `P3`, `T5`, `T15`, and `T17`.  
**Paper destination:** Paper IV comparison theorem, with a short Paper I forward reference after proof.  
**Remaining integration work:** This establishes only the metric-and-assignment layer. It does not identify arithmetic right actions with symmetric-space transvections, nor does it compare contact forms or finite defects.

### Result R-9: Existing affine contact curvature

**Status:** `PROVED`  
**Statement:** For
\[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a,
\]
one has
\[
[D_u,D_v]=\mu\lambda\partial_a.
\]
**Hypotheses:** Smooth scalar state space; fixed coordinate and bracket convention.  
**Argument or proof location:** Direct vector-field bracket.  
**Repository source:** `../../sections/sec06.tex`; `../05-mathematical-status.md`, §59.  
**Relevant theorem nodes:** `K2`, `T15`.  
**Paper destination:** Paper I.  
**Remaining integration work:** T17 still must separate affine endpoint defect, ACS area, finite commutator holonomy, and infinitesimal curvature. No comparison with \(r_c\) has been proved.

### Result R-10: Regular total-zero-set theorem is conditional and local

**Status:** `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`  
**Statement:** If \(A(p,t)=a_t(p)\) satisfies \(d_pa_t\neq0\) at every zero, then \(\mathcal Z=A^{-1}(0)\) is a smooth codimension-one submanifold and \(\pi:\mathcal Z\to\Lambda\) is a submersion. A proper submersion is locally trivial under the appropriate smooth and boundary hypotheses.  
**Hypotheses:** Smooth family, spatial regularity at zeros, and—only for local triviality—properness or an applicable substitute plus boundary control.  
**Argument or proof location:** Regular-value theorem and Ehresmann-type theorem.  
**Repository source:** `../03-theorem-dependency-graph.md`, `T8` and `Z6`; `../05-mathematical-status.md`, §§45–46 and 76–77.  
**Relevant theorem nodes:** `Z5`, `T8`, `Z6`.  
**Paper destination:** Minimal regular-value result in Paper I; tube theorem and applications in Paper III.  
**Remaining integration work:** Verify properness for every explicit AEG family; distinguish local triviality, ambient isotopy, monodromy, braid closure, and knot invariance.

### Result R-11: The bilateral quotient skeleton and telescoping obstruction

**Status:** `PARTIALLY PROVED`  
**Statement:** The bilateral note contains the homogeneous quotient skeleton
\[
\mathsf{Hist}\longrightarrow G\longrightarrow G/H_{\mathrm{pair}}\longrightarrow G/B
\]
and proves in a working construction that endpoint-anchored increments of the form \(h_th_{t-1}^{-1}\) telescope around a closed lifted path. Such exact endpoint transport cannot by itself retain history-sensitive holonomy.  
**Hypotheses:** The stated group action, selected stabilizers and reference data, and the exact endpoint-increment ansatz.  
**Argument or proof location:** “History before quotient,” quotient/frame sections, and “transport obstruction” in the bilateral note.  
**Repository source:** `../../notes/bilateral_projective_condensation.tex`; source extraction still required by `../05-mathematical-status.md`, §§87–92.  
**Relevant theorem nodes:** `P2`, `T2`, `P3`; no Paper IV node graph yet exists.  
**Paper destination:** Paper IV.  
**Remaining integration work:** Fix the history category, partial domains, stabilizers, and gauge data. The constant-curvature bundle \(G_c/L_c\) is a different quotient and must not be substituted for \(G/H_{\mathrm{pair}}\).

### Result R-12: The general noncommutativity–growth–hardness chain is false

**Status:** `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`  
**Statement:** Noncommutativity does not imply exponential group growth; exponential growth does not by itself imply a hard word problem; hyperbolicity does not imply general computational hardness.  
**Hypotheses:** The claims concern the general implications, not a particular AEG language with additional hypotheses.  
**Argument or proof location:** The discrete Heisenberg group supplies a noncommutative polynomial-growth calibration; free and hyperbolic groups separate exponential volume growth from word-problem cost.  
**Repository source:** The rejection is authoritative in `../05-mathematical-status.md`, §§96–98 and rejection R10. A dedicated literature citation audit remains necessary.  
**Relevant theorem nodes:** Forbidden edge §66.3 of the theorem dependency graph.  
**Paper destination:** Paper IV as calibration and claim discipline.  
**Remaining integration work:** Cite standard sources and compute the proposed AEG quantities on explicit finitely generated examples.

## 6. Structural proposals and conjectures

### 6.1 Structural proposals

#### Proposal S-1: Arithmetic origin of the three real forms

The projective displacement language, supplemented by an explicit involution or Hermitian form, may produce compact, flat, and split real forms from one signed parameter \(c\).

- **Additional data needed:** A definition of \(G_c\), \(L_c\), the preserved form, normalization of \(M_c(\xi)\), and the contraction at \(c=0\).
- **Validating theorem:** A syntax-to-group construction followed by a real-form classification and a proof that \(X_c=G_c/L_c\) has curvature \(c\).
- **Falsification or weakening:** If the real form must be selected externally and is not constrained by arithmetic syntax, the result is an interpretation of classical EPH geometry rather than an internal AEG classification.
- **Target paper:** Paper IV.

#### Proposal S-2: Isotropy-valued section residue as process information

The factor \(r_c(\xi,\eta)\) may record process information discarded by the compressed displacement \(\xi\oplus_c\eta\).

- **Additional data needed:** Local sections, gauge transformations, a connection, loop composition, and an invariant extraction rule.
- **Validating theorem:** A well-defined closed-loop holonomy or curvature form independent of allowed choices.
- **Falsification or weakening:** If every candidate closed residue telescopes or is gauge-trivial, retain only the exact two-step factorization.
- **Target paper:** Paper IV.

#### Proposal S-3: Three-branch metric/assignment family

The pair \((g_c,a_c)\) may be a uniform family of constant-curvature assignment models, with the negative branch recovering the basic upper-half-plane model.

- **Additional data needed:** Global domains, charts, metric normalization, framed-flow equations, critical and zero sets, and projective continuation rules.
- **Validating theorem:** Exact verification of the selected AES definition on each branch and the negative-branch Cayley comparison.
- **Falsification or weakening:** If only the eikonal equation is shared, while the arithmetic directions fail to intertwine, present the family as a PDE/geometric model rather than an AEG process unification.
- **Target papers:** Paper IV for geometry; Paper II for analysis; Paper I only as a forward reference.

#### Proposal S-4: Coupling history transport to zero-tube monodromy

A history or frame bundle pulled back over a parameterized zero family may carry holonomy that refines the permutation of zero components.

- **Additional data needed:** A proper zero family, discriminant complement, selected bundle over \(\mathcal Z\), connection or discrete transport, and homotopy-invariance rules.
- **Validating theorem:** A representation of the parameter-space fundamental group whose braid or closure invariant is independent of presentation choices.
- **Falsification or weakening:** If the decoration is arbitrary or can encode any knot by hand, it is not an intrinsic AEG construction.
- **Target paper:** Paper III; the process-bundle input may be imported conditionally from Paper IV.

#### Proposal S-5: Four-level growth taxonomy

The tuple \((W,N_\rho,M_\rho,D_{\mathcal R})\) may separate raw syntax, operator-image growth, condensation-fiber multiplicity, and equivalence proof cost.

- **Additional data needed:** A finite generating alphabet or weighted encoding, length, evaluation relation, rewrite presentation, and cost convention.
- **Validating theorem:** Model-specific inequalities relating these quantities to canonical forms, search width, memory, or runtime.
- **Falsification or weakening:** If the functions are infinite, presentation-dependent without a declared invariance class, or fail to distinguish the calibration examples, the taxonomy must be revised.
- **Target paper:** Paper IV.

### 6.2 Conjectures

No genuinely AEG-specific conjecture reached a sufficiently stable formal statement in this discussion. In particular, the following were not promoted to conjectures:

- that the arithmetic syntax uniquely selects the three real forms;
- that \(r_c\) equals the existing affine/contact torsion;
- that tube holonomy yields a Markov invariant;
- that one cocycle controls local curvature, knot topology, and complexity growth.

Each lacks a fixed category, coefficient object, or invariance statement. They remain `STRUCTURAL PROPOSAL` or `OPEN PROBLEM` items until those definitions are supplied.

### 6.3 Open programs

#### Open program O-1: Negative-branch process bridge

Go beyond the exact base metric/assignment comparison by intertwining the current arithmetic right actions in affine \(AN\) coordinates with the symmetric-space displacement fields. Then compare contact forms, brackets, and finite residues.

#### Open program O-2: Arithmetic-history tube invariant

Construct an intrinsic thread or lifted process decoration over a proper zero tube; derive braid monodromy; prove conjugation and stabilization behavior; compare the normalized result with Alexander, Burau, twisted Alexander, and character-variety data.

#### Open program O-3: Representation-growth theory

Define history and quotient growth on finite systems; compute calibration examples; prove only model-specific relations to time and space resources.

#### Open program O-4: Strong cross-scale unification

Find a common coefficient system or functor relating affine/contact curvature, projective or tube holonomy, and history-fiber growth. If the value groups and functorial maps cannot be aligned, retain the weaker local–global–asymptotic architecture without claiming a single invariant.

## 7. Rejected or superseded formulations

### Rejected formulation 1

**Earlier formulation:** Addition \(E\) and multiplication \(H_{\mathrm{Lie}}\) are the common primitive directions of all three branches.  
**Problem:** This describes the established affine/Borel slice. The symmetric projective proposal uses \(E\) and \(F\) as displacement directions, with \(H_{\mathrm{Lie}}=[E,F]/2\).  
**Counterexample, contradiction, or missing hypothesis:** The spherical mechanism requires the quadratic direction; imaginary affine scaling alone remains Euclidean-motion-like.  
**Replacement formulation:** Retain \(E,H_{\mathrm{Lie}}\) as affine AEG directions; provisionally use \(E,F\) only as projective Lie generators until their syntactic origin is established.  
**Files or passages still using the old form:** The Paper I affine sources correctly use add/multiply and should not be globally rewritten; only three-branch discussions require the distinction.

### Rejected formulation 2

**Earlier formulation:** Substituting \(\lambda\mapsto i\kappa\), or observing \(\sinh\mapsto\sin\), produces spherical arithmetic.  
**Problem:** This changes affine dilation into rotation but does not construct the spherical homogeneous space.  
**Counterexample, contradiction, or missing hypothesis:** \(z\mapsto e^{i\kappa t}z+b\) is of Euclidean rotation–translation type.  
**Replacement formulation:** Add the reciprocal quadratic direction \(F\) and select the compact real form through an involution/Hermitian structure.  
**Files or passages still using the old form:** No committed three-branch source was found; historical discussion only.

### Rejected formulation 3

**Earlier formulation:** Bare \(\mathbb C\) or \(PGL_2(\mathbb C)\) distinguishes the spherical and hyperbolic branches.  
**Problem:** The compact and noncompact branches are different real forms of the same complexified group.  
**Counterexample, contradiction, or missing hypothesis:** Complexification removes the real-eigenvalue versus imaginary-eigenvalue distinction.  
**Replacement formulation:** Include complex conjugation, a Hermitian form, or an equivalent involution as explicit data. Do not identify \(\bar\xi\) with operand-slot mirror.  
**Files or passages still using the old form:** Current discussion only.

### Rejected formulation 4

**Earlier formulation:** The family \(\{M_c(\xi)\}\) is itself the full branch group, with \(c=0\) giving \(E(2)\).  
**Problem:** Products acquire an isotropy factor, and at \(c=0\) these matrices give translations only.  
**Counterexample, contradiction, or missing hypothesis:** \(M_0(\xi)M_0(\eta)=M_0(\xi+\eta)\) contains no rotations.  
**Replacement formulation:** Define \(G_c\) as the full orientation-preserving isometry group or explicitly adjoin \(L_c\); use \(SE(2)\), not the reflection-containing full \(E(2)\), unless reflections are intended.  
**Files or passages still using the old form:** Current discussion only.

### Rejected formulation 5

**Earlier formulation:** The two-step phase \(r_c\) is already canonical curvature or holonomy.  
**Problem:** It is initially a factor associated with a chosen local section and an open two-step composition.  
**Counterexample, contradiction, or missing hypothesis:** Its gauge transformation law, connection, loop closure, and cocycle identity have not been defined.  
**Replacement formulation:** Call it an isotropy-valued section-composition residue. Promote only a gauge-controlled closed-loop or curvature quantity.  
**Files or passages still using the old form:** Current discussion used “frame residue” and “curvature” heuristically; the distinction must be retained in future notes.

### Rejected formulation 6

**Earlier formulation:** One quotient \(G/H\) simultaneously describes regular bivaluations, constant-curvature points, and all process residue.  
**Problem:** The bilateral ordered-pair stabilizer \(H_{\mathrm{pair}}\) and the compact isotropy \(L_c\) are different subgroups and generally not conjugate.  
**Counterexample, contradiction, or missing hypothesis:** In the negative branch, the ordered-pair stabilizer is split-torus-like while point isotropy is rotation-like. `PSU(2)` is also not transitive on all ordered distinct pairs because spherical distance is preserved.  
**Replacement formulation:** Distinguish \(G/H_{\mathrm{pair}}\), \(G_c/L_c\), and \(G/B\); relate them only through an explicit complexification, real-form orbit decomposition, or correspondence space.  
**Files or passages still using the old form:** Potential ambiguity in the cross-paper discussion; `../../notes/bilateral_projective_condensation.tex` itself must retain its own stabilizer meaning.

### Rejected formulation 7

**Earlier formulation:** The disjoint union of branches over \(c\) is automatically a smooth tube or fiber bundle.  
**Problem:** The spherical, flat, and hyperbolic domains have different global topology, and \(c=0\) is a contraction limit.  
**Counterexample, contradiction, or missing hypothesis:** No total-space topology, smooth structure, proper projection, or local triviality has been supplied.  
**Replacement formulation:** Treat \(c\) as a deformation or stratified/contraction parameter until a total-space theorem is proved.  
**Files or passages still using the old form:** Current discussion's informal “three branches of one mother theory.”

### Rejected formulation 8

**Earlier formulation:** Scalar holomorphicity at weight zero yields a new and distinct function theory on each branch.  
**Problem:** In real dimension two, scalar conformal holomorphicity locally reduces to ordinary complex analysis; on the compact sphere global scalar holomorphic functions are constant.  
**Counterexample, contradiction, or missing hypothesis:** Nontrivial spherical holomorphic objects require meromorphic functions or line-bundle sections, and bundle weights may be quantized by characters.  
**Replacement formulation:** Put branch-sensitive analytic content in weighted connections, line bundles, frame dependence, operator domains, and curvature terms.  
**Files or passages still using the old form:** Future Paper II proposals only; no theorem source located.

### Rejected formulation 9

**Earlier formulation:** Base-space Cayley equivalence automatically identifies the new phase residue with the existing affine/contact torsion.  
**Problem:** The process generators and value groups differ. Existing AEG arithmetic maps are naturally described as right actions in \(AN\) coordinates, while standard Iwasawa components often enter through a left action; symmetric transvections have brackets in compact isotropy, whereas affine directions bracket inside the solvable algebra.  
**Counterexample, contradiction, or missing hypothesis:** Matching \((g_c,a_c)\) does not intertwine generators, contact forms, projections, or finite holonomy.  
**Replacement formulation:** Split the bridge into base equivalence, left/right generator comparison, and contact/finite-residue comparison.  
**Files or passages still using the old form:** No committed three-branch source; the risk applies to future migration.

### Rejected formulation 10

**Earlier formulation:** A smooth total zero set is a global tube, and a threaded tube defines a knot invariant.  
**Problem:** Properness, local triviality, embedding, thread definition, isotopy invariance, and Markov behavior are separate obligations.  
**Counterexample, contradiction, or missing hypothesis:** Topology may change by boundary escape or failure of properness; an arbitrary section can encode a knot by hand.  
**Replacement formulation:** Preserve the strict chain
\[
\text{total zero set}
\to
\text{regular zero surface}
\to
\text{locally trivial zero family}
\to
\text{threaded tube}
\to
\text{braid closure}
\to
\text{knot invariant}.
\]
**Files or passages still using the old form:** Historical tube passages in `../../archive/paper4p/aeg.tex`, `../../notes/note_02.tex`, and exploratory knot notes require audit or archival classification.

### Rejected formulation 11

**Earlier formulation:** A Laurent factor such as \(t^2-1\) in the scalar reversal torsion is a new knot invariant.  
**Problem:** The factor can arise from Laurent-unit normalization and reversal shift.  
**Counterexample, contradiction, or missing hypothesis:** Presentation, Markov, and choice independence were not proved; existing calculations remain at Alexander/Fox-like or representation-variety levels.  
**Replacement formulation:** Move to group-valued holonomy or a precisely normalized representation-level quantity and compare against known invariants.  
**Files or passages still using the old form:** `../../knots/knots_03.tex`; related tables in `../../knots/results.tex` retain computational provenance but not invariant status.

### Rejected formulation 12

**Earlier formulation:** Noncommutativity implies exponential representation growth, which forces hyperbolicity and computational hardness.  
**Problem:** Each arrow fails in general.  
**Counterexample, contradiction, or missing hypothesis:** The discrete Heisenberg group is noncommutative with polynomial growth; free/hyperbolic groups can have exponential growth with tractable word problems.  
**Replacement formulation:** Define and separately measure raw word growth, quotient/operator growth, fiber multiplicity, filling cost, search, time, and space. Prove only model-specific comparisons.  
**Files or passages still using the old form:** `../../notes/note_06.tex`, `../../notes/note_09.tex`, and other resource-geometry notes contain motivational or overstrong versions; authoritative rejection R10 controls them.

### Rejected formulation 13

**Earlier formulation:** A parameterized history space, a process quotient bundle, and a zero tube are the same object.  
**Problem:** Their bases, fibers, regularity hypotheses, and equivalence relations differ.  
**Counterexample, contradiction, or missing hypothesis:** A history fiber can be large over a single operator even when no assignment zero family is present; a zero family can exist without any chosen history lift.  
**Replacement formulation:** Keep the three maps separate and formulate an explicit pullback or comparison functor if one exists.  
**Files or passages still using the old form:** The unifying diagram in the discussion was heuristic and is superseded by the three-map architecture in this note.

### Rejected formulation 14

**Earlier formulation:** Local Darboux/contact equivalence proves the AEG contact model is the same as the canonical contact structure associated with the hyperbolic branch.  
**Problem:** A local contactomorphism need not preserve arithmetic generators, Maurer–Cartan data, base projection, or finite process residues.  
**Counterexample, contradiction, or missing hypothesis:** No intertwining map has been constructed.  
**Replacement formulation:** Require a bundle-level comparison that matches the relevant fields, bracket, projection, and finite transport.  
**Files or passages still using the old form:** `../../notes/bilateral_projective_condensation.tex` contains only an open contact-comparison proposal.

## 8. Decision register

| ID | Decision | Status | Consequence | Paper/file affected |
| --- | --- | --- | --- | --- |
| D-01 | Use the weak local–global–asymptotic architecture as the cross-paper research map. | adopted | It organizes work without claiming one invariant. | Cross-paper; this note |
| D-02 | Treat the strong “same cocycle” statement as an open program. | adopted | No theorem or abstract may claim the three scales are already unified. | Papers III–IV; future series synthesis |
| D-03 | Rename the discussion's curvature parameter \(K\) to \(c\) in this note. | adopted | Avoids conflict with the base field in \(PGL_2(K)\). | Paper IV notation planning |
| D-04 | Distinguish \(H_{\mathrm{pair}}\), \(L_c\), and \(H_{\mathrm{Lie}}\). | adopted | Prevents false identification of quotient spaces and Lie generators. | Papers I and IV |
| D-05 | Call \(r_c\) a section-composition residue, not canonical holonomy or curvature. | adopted | Gauge and connection obligations remain explicit. | Paper IV |
| D-06 | Record the negative-branch metric/assignment comparison separately from the process/contact bridge. | adopted | Base equivalence may be proved first without overstating unification. | Paper I/IV interface |
| D-07 | Finish only a minimal three-branch algebraic package before expanding function theory. | provisionally adopted | Prevents the project from becoming a general EPH survey. | Paper IV; Paper II conditional |
| D-08 | Treat the tube/knot direction as the highest AEG-specific originality opportunity, subject to strict invariance gates. | provisionally adopted | Main creative effort should target an intrinsic, Markov-stable quantity. | Paper III |
| D-09 | Replace the noncommutativity–hyperbolicity–hardness chain by explicit growth and cost quantities. | adopted | Complexity work begins with definitions and calibration systems. | Paper IV |
| D-10 | Keep history quotients, constant-curvature frame bundles, and zero-family projections distinct. | adopted | Any relationship must be expressed by an explicit map or pullback. | Papers III–IV |
| D-11 | Exclude full three-branch, tube/knot, and complexity developments from Paper I. | adopted by authoritative scope | Paper I contains only their minimal interfaces. | Paper I |
| D-12 | Do not stabilize a knot claim until conjugation, stabilization, choice independence, and comparison with known invariants are proved. | adopted by authoritative scope | Existing knot calculations remain experiments or provenance. | Paper III and `../../knots` |
| D-13 | Do not create a compulsory Paper III \(\to\) Paper IV dependency yet. | deferred | Tube holonomy may be an optional Paper IV case study until Paper III supplies a theorem. | `../01-paper-series-architecture.md` remains unchanged |
| D-14 | Decide whether \(E,F\) are arithmetic syntax primitives or only Lie generators. | unresolved | The originality claim of the three-branch construction depends on this. | Paper IV |

### Adopted

- Use the weak local–global–asymptotic architecture.
- Keep all three quotient/fibration structures distinct.
- Separate exact algebra, standard coordinate consequences, structural proposals, and open bridges.
- Place tube/knot work in Paper III and real-form/complexity work in Paper IV.
- Use explicit growth and cost models; reject general hardness implications.

### Rejected

- Imaginary affine scaling as a complete spherical mechanism.
- Bare complexification as a real-form selector.
- Open section residue as canonical curvature or holonomy.
- Total zero set or knot-like drawing as a knot invariant.
- Noncommutativity, exponential growth, hyperbolicity, and hardness as an unconditional chain.

### Deferred

- Full branchwise function theory and weighted line bundles.
- A compulsory Paper III \(\to\) Paper IV dependency.
- Any final terminology identifying all finite and infinitesimal defects as “torsion.”

### Still open

- The internal arithmetic derivation of the real forms.
- The left/right Iwasawa and contact comparison in the negative branch.
- The definition of an intrinsic thread and a Markov-stable quantity.
- The exact finite-alphabet definitions of the four growth functions.
- The existence of a common coefficient system for strong unification.

## 9. Mathematical dependency map

### 9.1 Imported nodes

```text
P1 Projective semantics of one-hole contexts
  ==> P2 projective evaluation
  ==> T2 bilateral PGL2 generation

T2 bilateral PGL2 generation
  ==> P3 affine/Borel sector
  ==> P5 Riccati placement

F1 affine Lie algebra
  ==> T5 continuous affine flow
  ==> T6 basic hyperbolic AES

K2 horizontal lifts
  ==> T15 horizontal curvature bracket
  ==> K3 finite commutator formulas

Z5 smooth parameter families
  ==> T8 regular total-zero-set theorem
  ==> Z6 properness warning
```

### 9.2 Modified or clarified nodes

```text
P5 Riccati completion
  ==> supplies E, H_Lie, F as local projective fields
  -/-> full projective AES
  -/-> three-real-form classification

T6 basic hyperbolic AES
  ==> target of the negative-branch base comparison
  -/-> process-generator equivalence without a left/right intertwiner

T15 horizontal curvature bracket
  ==> existing local vertical defect
  -/-> equality with the U(1)-valued section residue

T17 local-global torsion synthesis
  ==> affine/contact synthesis remains internal to Paper I
  -/-> projective, tube, or complexity synthesis without new theorems

T8 regular total-zero-set theorem
  ==> smooth total zero set and projection submersion
  -/-> proper tube, braid, or knot invariant
```

### 9.3 New candidate nodes

The following are candidates only. They have not been added to the authoritative graph.

```text
PIV-C1  Signed quadratic-algebra law
PIV-C2  Hermitian displacement and domain theorem
PIV-C3  Three-real-form classification and c=0 contraction
PIV-C4  Section-residue factorization and gauge law
PIV-C5  Negative-branch Cayley base theorem
PIV-C6  Arithmetic right-action / symmetric-transvection comparison
PIV-C7  Contact and finite-residue comparison

PIII-C1 Proper AEG zero-tube theorem
PIII-C2 Discriminant-complement monodromy
PIII-C3 Intrinsic threading definition
PIII-C4 Braid and Markov invariance
PIII-C5 Comparison beyond Alexander/Burau

PIV-X1  Finite history-growth definitions
PIV-X2  Calibration computations
PIV-X3  Model-specific resource inequalities
SERIES-C1 Cross-scale cocycle comparison
```

### 9.4 Forbidden dependencies

```text
P5 local Riccati completion
  -/-> full projective AES or three-real-form theorem

PGL2(C) complexification
  -/-> compact/noncompact real-form selection

M_c two-step factor
  -/-> canonical holonomy, curvature, or knot invariant

G/H_pair bivaluation quotient
  -/-> G_c/L_c constant-curvature point space

base Cayley equivalence
  -/-> arithmetic generator or contact intertwining

T8 smooth total zero set
  -/-> proper tube
  -/-> braid
  -/-> knot invariant

noncommuting generators
  -/-> negative curvature
  -/-> exponential quotient growth
  -/-> computational hardness

large history fiber
  -/-> time or space lower bound without a computational model
```

## 10. Paper-series allocation

### Paper I

Paper I must retain the minimal foundations required by all three directions:

- marked spinal histories and projective evaluation;
- `T2` projective generation and `P3` affine/Borel identification;
- `P5` only as concise Riccati placement;
- affine cocycles, `T5`, and the basic upper-half-plane model `T6`;
- regular-zero and total-zero-set interfaces `T7` and `T8`;
- ACS, contact form, `T15`, `K3`, and a carefully separated `T17` synthesis.

Paper I must exclude the full signed-curvature family, real-form classification, weighted branchwise analysis, tube topology, braid/knot claims, and complexity conclusions. It may add a short outlook after the negative-branch bridge is independently proved.

### Paper II

Paper II owns any analytic theory on \((X_c,g_c)\), including a possible weighted operator \(\bar\partial_{c,m}\), associated line bundles, measures, domains, adjoints, boundary problems, and branchwise solution families. It must not assume that the contact form alone fixes a complex structure. A full flat–hyperbolic–spherical function theory would expand the present authoritative Paper II scope and therefore requires an explicit architecture decision before migration.

### Paper III

Paper III owns:

- singular and stratified AES definitions;
- multi-zero constructions and discriminants;
- proper total-zero families and zero tubes;
- topology change and singular fibers;
- component monodromy and braid lifts;
- the definition of threading;
- braid closure, Markov normalization, and conditional knot invariants;
- comparison with Alexander, Burau, twisted Alexander, character varieties, and related established data.

Three-branch models may enter only after their domain, metric, assignment, singular set, and flow equations are verified.

### Paper IV

Paper IV owns:

- the full history category or groupoid;
- projective evaluation and all relevant quotient maps;
- the distinction among \(G/H_{\mathrm{pair}}\), \(G_c/L_c\), and \(G/B\);
- the signed-curvature displacement algebra and real-form classification;
- gauge-controlled process residues and projective holonomy;
- condensation fibers, normal forms, and rewriting;
- \(W,N_\rho,M_\rho,D_{\mathcal R}\) or their eventual replacements;
- growth calibration and model-specific complexity/cost theorems.

### Beyond Papers I–IV

The strong assertion that one process cocycle controls Paper I contact curvature, Paper III knot holonomy, and Paper IV representation complexity should remain a series-level open program until the individual Paper III and IV structures exist. If it becomes a theorem, the architecture may need a new required Paper III \(\to\) Paper IV dependency.

| Material | Destination | Status | Dependency | Re-entry condition |
| --- | --- | --- | --- | --- |
| Signed quadratic law and \(M_c\) displacement | Paper IV | `STRUCTURAL PROPOSAL` with exact calculations | `T2`, `P5` | Domain, group, and real-form theorem |
| Negative-branch base comparison | Paper IV / Paper I interface | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | `T6`, `E3` | Written Cayley and normalization proof |
| Process/contact bridge | Paper IV | `OPEN PROBLEM` | `P3`, `T5`, `T15`, `K3`, `T17` | Left/right and bundle intertwining theorem |
| Weighted branchwise analysis | Paper II | `STRUCTURAL PROPOSAL` | Verified \((X_c,g_c)\) and analytic data | Line bundle, weight, domain, and nontrivial theorem |
| Proper zero tube | Paper III | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` for each model | `Z5`, `T8`, `Z6` | Properness and boundary verification |
| Thread/braid transport | Paper III | `STRUCTURAL PROPOSAL` | Proper tube and discriminant | Intrinsic thread and homotopy-invariant monodromy |
| Knot invariant | Paper III | `OPEN PROBLEM` | Braid transport | Markov and choice invariance |
| New information beyond Alexander/Burau | Paper III | `OPEN PROBLEM` | Defined knot invariant | Explicit comparison pair or theorem |
| Growth quartet | Paper IV | `STRUCTURAL PROPOSAL` | History category and evaluation | Finite encoding and cost definitions |
| Time/space relation | Paper IV | `OPEN PROBLEM` | Growth quantities plus computation model | Simulation or model-specific inequalities |
| Common cross-scale cocycle | Beyond I–IV / future synthesis | `OPEN PROBLEM` | Results from Papers I, III, IV | Common coefficient object and comparison functors |

## 11. Repository source map

No committed source for the signed-curvature three-branch construction was found. Its formulas are new discussion material. The repository sources below supply its affine/projective seed, its tube and knot precedents, and its complexity precedents.

| Source file | Relevant material | Current status | Target destination | Required action |
| --- | --- | --- | --- | --- |
| `../AGENTS.md` | Repository-wide research discipline, process-before-result tower, affine/projective and regular/singular distinctions | Applicable instruction file in the target subtree | Repository governance | Preserve; note that the root `../AGENTS.md` requested by the task does not exist. Audit its stated hierarchy against `../00-authoritative-scope.md` §2. |
| `../../README.md` | Older public summary; calls the upper-half-plane model \(\mathfrak E_1\) and uses strong torsion language | Subordinate and partly stale | Future public README revision | Do not use to settle numbering or status; OQ-012 governs model numbering. |
| `../../README.md` | Current four-paper overview and mathematical frontier | Current restructuring overview | Cross-paper | Preserve; use as the operational overview. |
| `../00-authoritative-scope.md` | Binding Paper I–IV ownership and prohibited inferences | Authoritative scope | Cross-paper | No change in this task. |
| `../01-paper-series-architecture.md` | Export interfaces, quotient/complexity notation, dependency direction | Authoritative architecture | Cross-paper | No change; revise later only if a required Paper III \(\to\) IV dependency is adopted. |
| `../02-paper-I-outline.md` | Paper I placement of Riccati outlook, zero-family lemma, contact synthesis, later-paper interfaces | Authoritative outline | Paper I | No change. |
| `../03-theorem-dependency-graph.md` | `T2`, `P3`, `P5`, `T5`, `T6`, `T8`, `Z6`, `T15`, `K3`, `T17`; forbidden edges | Authoritative Paper I graph | Paper I and exports | No change; candidate later-paper nodes in this note are not authoritative. |
| `../04-current-to-target-map.md` | File migration and strict tube taxonomy; complexity migration | Authoritative migration map | Cross-paper | No change. |
| `../05-mathematical-status.md` | Claim statuses, rejection register, Paper III/IV frontier | Authoritative status register | Cross-paper | No change; this note does not promote any status. |
| `../06-editorial-rules.md` | Status wording, notation, local/global and exact/asymptotic discipline | Authoritative editorial rules | Cross-paper | No change. |
| `../07-acceptance-checklist.md` | Paper I acceptance gates and source controls | Authoritative checklist | Paper I | No change. |
| `../08-open-questions.md` | OQ-001–070, especially OQ-007, OQ-022, OQ-037–058, OQ-068 | Authoritative open-question register | Cross-paper | Reference existing IDs; candidate new questions remain unregistered. |
| `../../notes/bilateral_projective_condensation.tex` | “Marked spinal expressions”; “Projective evaluation”; affine cocycles and Maurer–Cartan forms; Riccati completion; quotient/frame tower; transport obstruction | Mixed: proved algebraic core plus structural proposals | Split: Papers I and IV | Extract `P1`–`P5` and cocycles; migrate quotient/process-residue material; audit left/right and composition conventions; preserve the telescoping negative result. |
| `../../sections/sec03.tex` | \(da/ds=\mu\cos\theta+\lambda a\sin\theta\), Pfaffian and eikonal forms | Foundational but requires definition and convention audit | Paper I Chapters 4–5 | Rewrite under OQ-001 and final left/right convention; keep Riccati only as interface. |
| `../../sections/sec04.tex` | Basic upper-half-plane metric and assignment; eikonal and Laplacian; singular disk model; historical tube paragraph | Mixed foundational and later-paper material | Split: Paper I Chapters 6–7 and Paper III | Extract basic model; audit curvature, Laplacian, and naming; migrate tube material. |
| `../../sections/sec05.tex` | ACS evaluation, boundary integral, weighted area | Partially proved; sign/orientation audit required | Paper I Chapter 8 | Rewrite and test scale/charge compatibility. |
| `../../sections/sec06.tex` | Contact form, horizontal fields, bracket, finite defects | Stable core with composition/sign audit | Paper I Chapter 9 | Keep; separate open two-path, closed-loop, and infinitesimal quantities. |
| `../../sections/sec07.tex` | \(\delta_H\), curvature-sensitive square, analytic extensions | Scalar core proved; analytic material later | Split: Papers I and II | Keep scalar horizontal formula in I; move analysis to II. |
| `../../sections/sec08.tex` | Arithmetic Cauchy–Riemann and factorization proposals | Later analytic theory | Paper II | Move; do not use to prove Paper I. |
| `../../archive/paper4p/aeg.tex` | “Tube structure”: \(\bigsqcup_{\lambda>0}E_1^{(\lambda)}\), sections \(P(e^\lambda)\), and acknowledgement that the basic zero tube is trivial | Historical, outdated naming, conjectural topology | Paper III history / archive | Extract the parameter-family intuition and negative observation; rewrite, then archive original. |
| `../../notes/note_02.tex` | Distinction between algebraic/evaluation-parameter and geometric-family meanings of tube | Useful conceptual distinction with old naming | Paper III notes | Extract distinction; archive source after provenance is secured. |
| `../../notes/affine_torus.tex` | Discrete affine holonomy toy model and weighted Stokes formula | Computational/structural example; sign audit needed | Paper IV or conditional Paper III example | Extract only after recalculation; do not call it a knot invariant. |
| `../../knots/knots_01.tex` | Figure-eight relator experiment; Alexander-polynomial specialization | Reproducible experiment candidate, not invariant | Paper III notes / supplement | Audit scripts and presentation dependence; preserve computation. |
| `../../knots/knots_02.tex` | Solvable-group formulas for several knots | Exploratory | Paper III archive or notes | Audit group/action definition before reuse. |
| `../../knots/knots_03.tex` | Scalar reverse-path torsion and Laurent factor | Explicitly experimental; proposed novelty not established | Archive with provenance | Preserve tables; reject invariant interpretation without normalization and Markov proof. |
| `../../knots/results.tex` | Relator/torsion tables for several knots | Raw dataset | Paper III supplement | Preserve; locate or reconstruct generation scripts; audit presentation invariance. |
| `../../notes/note_11.tex` | Affine matrices and Fox-like cocycle analogy | Structural analogy, overstrong conclusions | Papers III–IV bridge note | Extract cocycle calculation; weaken or reprove identification claims. |
| `../../notes/loop_01.tex` | Figure-eight operator-loop examples | Example only; old notation | Paper III/IV notes | Extract after notation audit; no invariant status. |
| `../../notes/note_03.tex`, `../../notes/note_04.tex` | Hyperbolic knot-complement and HNN attempts | Structural proposals and a recorded non-faithfulness failure | Archive / Paper III exploratory note | Preserve negative path and determinant calculations; do not migrate as theorem. |
| `../../notes/note_05.tex` | Claim that a two-generator lattice in \(\mathbb R^2\) is dense | Mathematically incorrect | Archive / rejection record | Reject the two-dimensional density claim; only a one-dimensional projection may be dense. |
| `../../notes/rg_en.tex`, `../../notes/rg_zh.tex` | Early resource geometry and time–space proposals | Motivational, partly duplicated | Paper IV notes / archive | Make English version canonical after audit; preserve Chinese provenance; add cost models. |
| `../../notes/note_06.tex` | Projective boundary, hyperbolicity, combinatorial complexity | Mixed motivation and overclaim | Paper IV motivation / archive | Extract homogeneous/projective ideas; reject “complexity makes hyperbolicity unavoidable” as theorem. |
| `../../notes/note_09.tex` | Free-group complexity, condensation, canonical forms, computational mass/curvature analogies | Structural proposals plus unsupported analogies | Paper IV / archive | Extract quotient and normalization questions; archive physical overclaims. |
| `../../notes/note_10.tex` | Catalan/binary-expression experiment program | Experiment agenda | Paper IV experiments | Define state and cost model before use. |
| `../../notes/note_12.tex` | Rewrite graph and a mod-2 Thue–Morse cochain | Proposed theorem is incorrect for \(DT=T^2D\) | Archive / corrected rewrite scaffold | Reject the cochain claim; salvage only the 2-cell framework after correction. |
| `../../notes/note_13.tex`, `../../notes/note_14.tex` | Weighted resource plane and pebble-game toy calculations | Structural/computational proposals | Paper IV experiments | Audit realizability, pebble legality, scheduling, and meaning of \(M\). |
| `../../notes/note_15.tex` | Staged representation/time/space/filling program with explicit cautions | Most mature complexity working note | Paper IV active note | Use as the primary complexity seed; retain all warnings. |
| `../../notes/note_16.tex` | Path/2-groupoid, cohomology, ACS/contact pairings | Structural proposal requiring proof audit | Paper IV | Migrate selectively; reprove cohomological statements. |
| `../../archive/peddle/peddle_lab.html` | Interactive pebble-game experiment | Supplement only | Paper IV experiments | Validate before treating outputs as evidence; consider correcting directory name in a separate task. |

No verifiable general \(E_k\), \(E_{\log}\), multi-zero construction file, intrinsic threading definition, braid lift, or Markov-normalized invariant was located. Their absence must not be filled by inference from the status documents.

## 12. Proof obligations

### PO-01: Convention and domain table for signed-curvature arithmetic

**Target statement:** A single table fixing the base field, curvature parameter, matrix action, chronological composition, left/right multiplication, determinant conditions, poles, and ordinary versus projective domains.  
**Known special cases:** `T2` conventions; real-axis four-step decomposition.  
**Available argument:** Existing matrices and formulas.  
**Missing step:** Resolve OQ-002–OQ-004 and propagate the convention through every formula.  
**Required hypotheses:** Field, characteristic, invertibility, chart, and parameter restrictions.  
**Dependencies:** `C0`, `C1`, `P1`, `P2`, `T2`.  
**Failure consequence:** Signs, product order, and residue formulas remain ambiguous.  
**Recommended next action:** Produce a symbolic convention audit before any theorem prose.

### PO-02: Definition and classification of \(G_c\) and \(L_c\)

**Target statement:** Precisely define the full orientation-preserving branch group and isotropy, prove the compact/flat/split classification, and treat \(c=0\) as a contraction with rotations included.  
**Known special cases:** Standard constant-curvature isometry groups; exact \(M_c\) matrices.  
**Available argument:** Hermitian-form normalization and standard real-form theory.  
**Missing step:** Specify the preserved form, normalized representatives, determinant restrictions, and relation to arithmetic histories.  
**Required hypotheses:** Real \(c\), selected involution, orientation, connected component, chart/domain.  
**Dependencies:** `P5`, PO-01.  
**Failure consequence:** The “three branches” remain an externally chosen analogy.  
**Recommended next action:** Write a standalone real-form proposition with citations and a separate arithmetic-origin question.

### PO-03: Gauge law for the section-composition residue

**Target statement:** Determine how \(r_c(\xi,\eta)\) transforms when the local section \(M_c(\xi)\) is replaced by \(M_c(\xi)h(\xi)\), and determine the appropriate cocycle or associator identity.  
**Known special cases:** Exact two-step matrix factorization.  
**Available argument:** Principal-bundle local-section algebra.  
**Missing step:** Define the group action on the displacement coordinate and calculate the twisted composition law.  
**Required hypotheses:** Precise \(G_c/L_c\), local section, overlap, and action convention.  
**Dependencies:** PO-01, PO-02.  
**Failure consequence:** No canonical residue or curvature claim can be made.  
**Recommended next action:** Compute the gauge transformation and a three-step associativity diagram.

### PO-04: Negative-branch Cayley base theorem

**Target statement:** Prove the exact pullback identities between \((g_{-\lambda^2},a_{-\lambda^2})\) and the basic upper-half-plane \((g_{\mu,\lambda},-x/y)\).  
**Known special cases:** The formulas in Result R-8.  
**Available argument:** Direct complex-coordinate algebra.  
**Missing step:** Write and check the proof under the repository's metric, sign, and naming conventions.  
**Required hypotheses:** \(\mu\lambda\neq0\), disk interior, upper-half-plane interior, fixed Cayley orientation.  
**Dependencies:** `T6`, `E3`, PO-01.  
**Failure consequence:** The three-branch family lacks even a base-level link to current AEG.  
**Recommended next action:** Complete this calculation before the harder process bridge.

### PO-05: Arithmetic right actions versus symmetric transvections

**Target statement:** Identify, or prove the absence of, an intertwiner between current arithmetic-grid/right-action generators and the \(P_\xi^c\) symmetric-space displacement fields after the Cayley transform.  
**Known special cases:** Current affine actions in `../../sections/sec04.tex`; standard Iwasawa coordinates.  
**Available argument:** Explicit \(KAN/NAK\) decomposition and left/right Maurer–Cartan formulas from the bilateral note.  
**Missing step:** Track the actual vector fields and action side rather than only the base metric.  
**Required hypotheses:** Final composition convention, coordinate charts, normalization, and chosen group action.  
**Dependencies:** `P3`, `T5`, PO-01, PO-02, PO-04.  
**Failure consequence:** The family is geometrically equivalent at the base but not an arithmetic-process extension.  
**Recommended next action:** Work out \(c=-1\), \(\xi=r\), \(\eta=ir\) completely.

### PO-06: Contact and finite-residue comparison

**Target statement:** Construct a bundle map or contactomorphism that intertwines the arithmetic contact form, relevant generators, base projection, bracket, and finite transport with the negative branch.  
**Known special cases:** `T15`, `K3`, the standard contact structure on a unit tangent/frame bundle, and the open comparison proposal in the bilateral note.  
**Available argument:** Pull back contact/Maurer–Cartan forms after PO-05.  
**Missing step:** Match coefficient objects and distinguish \(U(1)\) rotation from assignment translation.  
**Required hypotheses:** Smooth bundle map, gauge choice, orientation, and flow normalization.  
**Dependencies:** `T15`, `K3`, `T17`, PO-03–PO-05.  
**Failure consequence:** The decisive AEG unification claim fails; only an adjacent projective geometry remains.  
**Recommended next action:** Test infinitesimal and finite formulas separately.

### PO-07: Full branchwise AES verification

**Target statement:** Verify the selected regular-AES definition, not merely the eikonal identity, for \((X_c,g_c,a_c)\) on every branch.  
**Known special cases:** Constant-curvature, gradient, and Laplacian coordinate identities; negative-branch base comparison.  
**Available argument:** Direct frame calculations.  
**Missing step:** Choose the primitive regular-AES definition and construct compatible additive/multiplicative directions.  
**Required hypotheses:** OQ-001 resolution, domains, smoothness, non-degeneracy, and global chart data.  
**Dependencies:** `E1`, `F3`, `T6`, PO-02, PO-04.  
**Failure consequence:** The three branches remain geometric PDE models rather than AEG spaces.  
**Recommended next action:** Delay theorem status until OQ-001 is resolved.

### PO-08: From infinitesimal area to finite holonomy

**Target statement:** Relate the leading phase \(-2c\operatorname{Im}(\xi\bar\eta)\) to a connection curvature and determine an exact geodesic-polygon area/holonomy formula where valid.  
**Known special cases:** Two-step asymptotic expansion and standard constant-curvature holonomy formulas.  
**Available argument:** Connection curvature and Stokes/Gauss–Bonnet methods.  
**Missing step:** Choose the connection, close the loop, and track gauge and orientation.  
**Required hypotheses:** Smooth loop/polygon, branch domain, chosen lift, and no pole crossing except controlled chart changes.  
**Dependencies:** PO-02, PO-03.  
**Failure consequence:** “Curvature as residue” remains only a local analogy.  
**Recommended next action:** Compute one small rectangle and one exact geodesic triangle.

### PO-09: Weighted branchwise \(\bar\partial\) theory

**Target statement:** Define \(\bar\partial_{c,m}\) on an associated line bundle and state the admissible weights, domains, and curvature term.  
**Known special cases:** Ordinary scalar complex analysis at weight zero and standard line bundles on the sphere/disk.  
**Available argument:** Associated-bundle characters and covariant Cauchy–Riemann operators.  
**Missing step:** Fix the bundle, connection, weight set, analytic domain, and nontrivial theorem.  
**Required hypotheses:** Verified branch geometry and compatible complex structure.  
**Dependencies:** PO-02, PO-03, PO-07; Paper II analytic data.  
**Failure consequence:** The three-branch function theory collapses to classical scalar complex analysis or remains undefined.  
**Recommended next action:** Postpone until the algebraic and negative-branch packages close.

### PO-10: Proper AEG zero-tube theorem for an explicit family

**Target statement:** For one explicit multi-zero family, prove smoothness, projection submersion, properness, boundary control, and local triviality.  
**Known special cases:** `T8` and the conditional Ehresmann consequence.  
**Available argument:** Regular-value and proper-submersion theorems.  
**Missing step:** No verifiable general multi-zero or \(E_{\log}\) source was located.  
**Required hypotheses:** Explicit domain, metric, assignment, parameter space, singular set, and compactness/properness conditions.  
**Dependencies:** `Z3`, `Z5`, `T8`, `Z6`; OQ-037–OQ-042.  
**Failure consequence:** There is no rigorous tube on which to build monodromy.  
**Recommended next action:** Locate the original source or construct the smallest fully auditable family.

### PO-11: Intrinsic definition of threading

**Target statement:** Select whether the thread is a zero branch, a section, a marked-history lift, an independent embedded curve, or a monodromy-carried decoration, and define its equivalence.  
**Known special cases:** Historical sections \(P(e^\lambda)\) and exploratory loop/knot examples.  
**Available argument:** Candidate objects in OQ-044.  
**Missing step:** Intrinsic selection and choice-independence.  
**Required hypotheses:** A proper tube and a specified ambient category.  
**Dependencies:** PO-10; OQ-044.  
**Failure consequence:** Any knot can be inserted by hand, so the construction carries no AEG-specific content.  
**Recommended next action:** Compare the five candidate definitions on one minimal family.

### PO-12: Monodromy and braid lift

**Target statement:** Construct a homotopy-invariant representation from the discriminant complement to \(S_n\) and, under embedding data, to \(B_n\).  
**Known special cases:** Standard monodromy of finite collision-free configurations.  
**Available argument:** Configuration-space topology.  
**Missing step:** Finite branch count, collision-free embedding, global labeling or local system, and parameter-homotopy invariance.  
**Required hypotheses:** Proper family, discriminant complement, embedded moving branches.  
**Dependencies:** PO-10, PO-11; OQ-037, OQ-043.  
**Failure consequence:** No braid object is defined.  
**Recommended next action:** Build the smallest two- or three-branch loop and compute its monodromy.

### PO-13: Markov invariance and normalization

**Target statement:** Convert a braid-level quantity to a knot-level quantity invariant under conjugation and stabilization, with all auxiliary choices controlled.  
**Known special cases:** Classical Markov theorem and trace normalizations.  
**Available argument:** Depends on the eventual representation or holonomy.  
**Missing step:** Both Markov moves, normalization, and presentation independence.  
**Required hypotheses:** A well-defined braid quantity from PO-12.  
**Dependencies:** PO-12; OQ-045.  
**Failure consequence:** The quantity is not a knot invariant.  
**Recommended next action:** Treat stabilization as an early falsification test, not a final polish step.

### PO-14: Comparison beyond known knot data

**Target statement:** Prove that the normalized AEG quantity is not determined by Alexander/Burau or another specified lower-level invariant.  
**Known special cases:** Existing figure-eight and low-crossing scalar calculations appear Alexander/Fox-like.  
**Available argument:** Low-crossing computation and pairs sharing known data.  
**Missing step:** A defined invariant, reproducible scripts, and a separating pair or comparison theorem.  
**Required hypotheses:** PO-13 and an explicit comparison class.  
**Dependencies:** OQ-046.  
**Failure consequence:** The outcome should be presented as a new realization or interpretation of an existing invariant, not a new invariant.  
**Recommended next action:** Audit `../../knots/results.tex` and generation provenance before new computation.

### PO-15: Finite history-growth definitions and calibration

**Target statement:** Define \(W,N_\rho,M_\rho,D_{\mathcal R}\) on a fixed finite history system and compute them, or sharp asymptotics, for \(\mathbb Z^2\), the discrete Heisenberg group, \(F_2\), and \(BS(1,2)\).  
**Known special cases:** Standard group growth and filling theory.  
**Available argument:** Cayley graphs, normal forms, and finite presentations.  
**Missing step:** Choose alphabet, encoding, length, equality, relation system, and invariance class.  
**Required hypotheses:** Finite generation/presentation or a declared weighted replacement.  
**Dependencies:** OQ-047–OQ-056.  
**Failure consequence:** Counts may be infinite or compare presentations rather than processes.  
**Recommended next action:** Start with a definition note and tiny exhaustive computations.

### PO-16: Resource comparison inequalities

**Target statement:** Under an explicit computational model, prove inequalities—not unqualified equalities—relating operator growth, fiber multiplicity, filling cost, search width, memory, and runtime.  
**Known special cases:** State-graph shortest paths, word-problem algorithms, and pebble-game time–space tradeoffs.  
**Available argument:** Simulation theorems and model-specific upper/lower bounds.  
**Missing step:** Encoding, transition cost, algorithm, and simulation relation.  
**Required hypotheses:** A fixed machine or state-graph model.  
**Dependencies:** PO-15; OQ-054–OQ-058.  
**Failure consequence:** Representation complexity remains motivational and cannot support computational claims.  
**Recommended next action:** Select one case study after PO-15, preferably \(BS(1,2)\) or a pebble-game DAG.

### PO-17: Strong cross-scale comparison

**Target statement:** Define a common coefficient object or functor that relates Paper I local curvature, Paper III closed tube/braid residue, and Paper IV history-fiber growth.  
**Known special cases:** Separate affine/contact, monodromy, and growth structures.  
**Available argument:** None beyond the weak architecture and possible representation functors.  
**Missing step:** Compatible categories, maps, coefficient groups, and a theorem at each scale.  
**Required hypotheses:** Successful PO-06, PO-13, and PO-15 at minimum.  
**Dependencies:** Papers I, III, and IV.  
**Failure consequence:** The program remains a useful analogy rather than one mathematical theory.  
**Recommended next action:** Defer until the component theories produce actual invariants.

## 13. Definition decisions

### DD-01: Curvature and field notation

**Competing formulations:** \(K\) for both ground field and curvature; \(\kappa\) for curvature despite its Riccati use; new symbol \(c\).  
**Current evidence:** The existing paper uses \(K\) as field and \(\kappa\) as a Riccati coefficient.  
**Recommended default:** Use \(\Bbbk\) for the field in this program note and \(c\in\mathbb R\) for signed curvature; preserve old notation in provenance.  
**Examples that must be tested:** Every formula combining \(PGL_2(\Bbbk)\) with \(M_c\).  
**Affected theorem nodes:** `T2`, `P5`.  
**Blocking level:** P0

### DD-02: Stabilizers and quotients

**Competing formulations:** One generic \(H\); ordered-pair stabilizer \(H_{\mathrm{pair}}\); constant-curvature isotropy \(L_c\); Borel \(B\).  
**Current evidence:** The quotient spaces and subgroup types differ.  
**Recommended default:** Use all three named subgroups and prohibit bare \(G/H\) in cross-interface statements.  
**Examples that must be tested:** \(PSL_2(\mathbb R)/A\), \(PSL_2(\mathbb R)/SO(2)\), and \(PSL_2(\mathbb R)/B\).  
**Affected theorem nodes:** `P3`, Paper IV §§87–90.  
**Blocking level:** P0

### DD-03: Definition of \(G_c\)

**Competing formulations:** Group generated only by \(M_c(\xi)\); group generated with isotropy; full orientation-preserving isometry group.  
**Current evidence:** The first option fails to give rotations at \(c=0\) and is not closed as pure displacements for \(c\neq0\).  
**Recommended default:** Define the full orientation-preserving isometry group and separately prove what the arithmetic displacement set generates.  
**Examples that must be tested:** \(c>0,0,<0\), including determinant boundary.  
**Affected theorem nodes:** Candidate `PIV-C3`.  
**Blocking level:** P0

### DD-04: Section residue terminology and gauge class

**Competing formulations:** frame torsion; curvature; holonomy; phase residue; isotropy-valued section-composition residue.  
**Current evidence:** Only the last description matches the proved open two-step factorization without extra structure.  
**Recommended default:** Use `section-composition residue` until PO-03 and PO-08.  
**Examples that must be tested:** Change of local section and a closed three- or four-step loop.  
**Affected theorem nodes:** `K3`, `T17`, Paper IV §88.  
**Blocking level:** P0

### DD-05: Meaning of arithmetic torsion

**Competing formulations:** Endpoint order defect, affine relative defect, ACS weighted area, finite commutator holonomy, horizontal curvature, projective residue.  
**Current evidence:** These are related in parts but not literally equal at finite scale.  
**Recommended default:** Follow OQ-007 and use qualified terms; do not add the projective residue to the torsion family until a comparison theorem exists.  
**Examples that must be tested:** Two-step square, closed contact loop, charge-compatible ACS pair.  
**Affected theorem nodes:** `A4`, `T10`–`T12`, `K3`, `T15`–`T17`.  
**Blocking level:** P0

### DD-06: Status of \(E\) and \(F\)

**Competing formulations:** Primitive arithmetic syntax operations; infinitesimal projective Lie generators; inversion-conjugate displacement directions.  
**Current evidence:** Only the Lie-generator statement is established.  
**Recommended default:** Call them projective Lie generators until a syntax-to-flow theorem is proved.  
**Examples that must be tested:** Canonical marked spinal histories realizing \(F\) and their ordinary domains.  
**Affected theorem nodes:** `T2`, `P5`.  
**Blocking level:** P1

### DD-07: Tube and thread objects

**Competing formulations:** Total zero set, locally trivial zero tube, parameterized history space, pulled-back frame bundle, external thread, zero branch, history decoration.  
**Current evidence:** The repository contains several historical meanings and no settled threading definition.  
**Recommended default:** Reserve `zero tube` for a locally trivial parameterized zero family; name all other bundles explicitly.  
**Examples that must be tested:** Historical \(P(e^\lambda)\) section and a collision-free two-branch family.  
**Affected theorem nodes:** `T8`, `Z6`; OQ-044.  
**Blocking level:** P1

### DD-08: History category and equality

**Competing formulations:** Free category of partial contexts, action groupoid, path groupoid, rewriting 2-category; ordinary versus projective domains.  
**Current evidence:** Different choices support different fibers and filling costs.  
**Recommended default:** Resolve OQ-047 and OQ-048 before defining complexity functions.  
**Examples that must be tested:** Undefined ordinary intermediate step with valid projective continuation; two distinct histories with one operator.  
**Affected theorem nodes:** `S3`, `P2`; Paper IV §§82–90.  
**Blocking level:** P1

### DD-09: Growth and filling functions

**Competing formulations:** Raw counts \(W,G,F,D\); renamed \(W,N_\rho,M_\rho,D_{\mathcal R}\); metric entropy for continuous parameters.  
**Current evidence:** Raw cardinalities are infinite for unrestricted real or complex operands.  
**Recommended default:** Begin with a finite alphabet/presentation; add weighted or entropy variants only after the discrete theory is calibrated.  
**Examples that must be tested:** \(\mathbb Z^2\), Heisenberg, \(F_2\), \(BS(1,2)\).  
**Affected theorem nodes:** No Paper IV node graph; OQ-052–OQ-058.  
**Blocking level:** P1

### DD-10: Analytic weight and bundle

**Competing formulations:** Scalar functions, arbitrary real weight \(m\), integral character weight, meromorphic sections.  
**Current evidence:** The sphere has no nonconstant global scalar holomorphic functions; associated bundles impose representation/character constraints.  
**Recommended default:** Do not write \(\bar\partial_{c,m}\) as a global operator until the associated bundle and allowed weights are fixed.  
**Examples that must be tested:** Weight zero on the disk, \(O(m)\) on the sphere, flat/Fock-type limit.  
**Affected theorem nodes:** Paper II interface only.  
**Blocking level:** P2

## 14. Mathematical risks

| Risk | Severity | Affected claim | Detection method | Mitigation |
| --- | --- | --- | --- | --- |
| Ground-field \(K\), curvature \(K\), Riccati \(\kappa\), and stabilizer/generator \(H\) collide | Critical | Nearly every three-branch formula | Repository-wide notation audit | Adopt \(\Bbbk,c,H_{\mathrm{Lie}},H_{\mathrm{pair}},L_c\) before migration |
| Matrix multiplication reverses the intended chronological history order | Critical | \(\xi\oplus_c\eta\), sign of \(r_c\), bracket orientation | Test two explicit numerical matrices against function composition | Resolve OQ-002/OQ-003; state convention beside every product |
| Determinant or pole restrictions are omitted | Critical | \(M_c\), four-step realization, hyperbolic boundary | Symbolic determinant and denominator checks | State \(1+c\lvert\xi\rvert^2\neq0\), chart domains, and ordinary admissibility |
| Complex conjugation is conflated with syntax mirror or reversal | High | Claimed arithmetic origin of \(\bar\xi\) | Trace definitions through marked histories | Treat the involution as real-form data; keep mirror/reversal/inverse separate |
| \(M_0\) is incorrectly said to generate \(SE(2)\) | High | Flat branch classification | Compute products at \(c=0\) | Add isotropy explicitly or define the full isometry group independently |
| Section residue is gauge-dependent | Critical | Curvature/holonomy/process-residue claims | Change local section and recompute | Prove gauge law; use closed-loop/conjugacy/curvature data only after definition |
| Infinitesimal area coefficient is promoted to exact finite holonomy | High | “Curvature equals arithmetic area” | Compare small expansion with finite triangle/loop | Label exact vs asymptotic; prove finite formula separately |
| \(G/H_{\mathrm{pair}}\) and \(G_c/L_c\) are conflated | Critical | Quotient tower and negative bridge | Compare stabilizers and orbit dimensions/invariants | Use separate notation and a correspondence-space theorem if available |
| Restricting the complex quotient to a real form is assumed to preserve transitivity | High | Three-branch derivation from bilateral bivaluations | Check real-form orbit decomposition; note spherical distance invariant | Prove orbit classification rather than “restrict the group” |
| Base conformal/isometric equivalence is mistaken for process equivalence | Critical | Claim that current AEG is recovered | Push forward actual arithmetic vector fields and right actions | Split base, generator, and contact bridge theorems |
| Sphere chart hides behavior at \(\infty\) | High | Global zero set and periodicity | Use a second stereographic chart | State chart transition; verify assignment extension and critical points globally |
| Scalar holomorphicity trivializes the spherical branch | High | Paper II novelty | Apply compact Riemann-surface facts | Use meromorphic functions or associated line-bundle sections |
| Line-bundle weights are treated as arbitrary | Medium | \(\bar\partial_{c,m}\) | Check isotropy characters and Chern class | Specify admissible representations/weights |
| The family over \(c\) is called a smooth tube despite topology change/contraction | High | Three-branch “mother space” | Examine global domains and \(c=0\) neighborhood | Use deformation/stratified-family language until proved |
| Properness or boundary escape is ignored | Critical | Zero-tube topology | Test inverse images of compact parameter sets and boundary behavior | Verify model by model; include non-proper and chart-transition discriminant strata |
| An arbitrary thread encodes topology by hand | Critical | AEG-specific knot claim | Vary section/decoration while fixing arithmetic family | Require intrinsic selection and choice independence |
| Markov stabilization is postponed | Critical | Knot invariant | Apply first positive/negative stabilization | Use stabilization as an early falsification gate |
| Candidate reproduces Alexander/Fox/Burau data | High | Novelty claim | Compare known polynomials and representation varieties | State realization theorem honestly; find a separating pair before novelty claims |
| Infinite operand alphabet makes \(W,N_\rho,M_\rho\) infinite | Critical | Complexity taxonomy | Count length-one histories | Fix finite/encoded alphabet or define entropy/volume alternative |
| Rewrite cost depends on presentation | High | \(D_{\mathcal R}\) as intrinsic complexity | Compare Tietze-equivalent presentations | State invariance class or keep presentation in notation |
| Exponential growth is read as algorithmic hardness | Critical | Complexity conclusions | Calibrate on hyperbolic groups and easy word problems | Require explicit algorithm and cost theorem |
| Different scales use incompatible coefficient groups | High | Strong common-cocycle program | List value groups and proposed comparison maps | Construct representation functors or downgrade to weak architecture |
| Root instruction file is missing and hierarchy wording conflicts | Medium | Reproducibility of future tasks | Compare `../AGENTS.md` with `00` §2 | Record the conflict; do not alter governance files inside a math task |

## 15. Open questions

### 15.1 Existing registered questions

The following questions already exist in `../08-open-questions.md`. This note refines their interfaces but does not duplicate or resolve them.

| Existing issue | Priority | Blocks Paper I? | Evidence required by this discussion | Likely destination |
| --- | --- | --- | --- | --- |
| OQ-001 — Canonical definition of a regular AES | P0 | Yes | Equivalence or compatibility among eikonal, framed-flow, and combined definitions; branchwise examples | Paper I, with later-paper consequences |
| OQ-002, OQ-003, OQ-004 — Composition, matrix action, and field hypotheses | P0 | Yes | One checked convention table and explicit tests of `T2`, \(M_c\), and residue product order | Paper I conventions; Paper IV reuse |
| OQ-006 — Positive affine component versus full real affine group | P1 | Yes for final affine placement | Component and reflection audit; relation to \(SE(2)\) in the flat branch | Paper I / Paper IV interface |
| OQ-007 — Meaning of “torsion” | P0 | Yes | A hierarchy separating finite affine, ACS, contact, and future projective quantities | Paper I, then Paper IV |
| OQ-013, OQ-014 — Invariant metric and curvature normalization | P1 | Yes | Explicit invariant-metric derivation and normalization comparison with \(g_c\) | Paper I |
| OQ-022 — Local-global synthesis theorem | P1 | Yes | Separate exact affine/ACS identity, exact finite contact formula, and common infinitesimal limit | Paper I |
| OQ-031, OQ-032 — Horizontal metric and almost-complex structure | P3 | No | Chosen analytic data and compatibility; no inference from contact form alone | Paper II |
| OQ-037–OQ-042 — Discriminant, \(E_k\), singular normal forms, and properness | P3 | No, except optional Paper I example | One explicit family with domain, metric, assignment, singularity, and properness proofs | Paper III |
| OQ-043 — From zero-component permutation to braid | P3 | No | Collision-free embedded transport and homotopy-invariant braid lift | Paper III |
| OQ-044 — Definition of threading | P3 | No | Intrinsic object and equivalence relation; comparison of candidate definitions | Paper III |
| OQ-045 — Markov invariance | P3 | No | Conjugation and stabilization theorem with normalization | Paper III |
| OQ-046 — New information beyond Alexander/Burau | P3 | No | Separating example or comparison theorem | Paper III |
| OQ-047, OQ-048 — History category and ordinary/projective groupoids | P3 | No | Objects, arrows, partial domains, equality, and evaluation functor | Paper IV |
| OQ-049, OQ-051, OQ-052 — Process residue, condensation, and information loss | P3 | No | Gauge-controlled quotient fibers and a declared measure of loss | Paper IV |
| OQ-053, OQ-054 — Canonical representatives and geometric cost | P3 | No | Normal-form computability plus simulation/quasi-isometry theorem | Paper IV |
| OQ-055, OQ-056 — Representation complexity and growth | P3 | No | Finite definitions and calibration on contrasting groups | Paper IV |
| OQ-057, OQ-058 — History/AES quasi-isometry and case studies | P3 | No | Explicit state graph, metric, encoding, and selected test family | Paper IV |
| OQ-068 — Riccati control and projective dynamics literature | P2 | No | Primary-source literature audit positioning the three-real-form proposal | Paper IV and Paper I outlook |

### 15.2 Candidate new open questions

#### Candidate new open question CNOQ-1: Internal derivation of signed-curvature real forms

**Priority:** P2  
**Blocks Paper I:** No.  
**Question:** Does bilateral arithmetic syntax plus a specified involution determine the compact, flat, and split real forms and their displacement sections, or are those choices external geometric input?  
**Required evidence:** A syntax-to-group construction, Hermitian-form theorem, and \(c=0\) contraction.  
**Likely paper destination:** Paper IV.  
**Relation to `../08-open-questions.md`:** Extends OQ-004, OQ-006, and OQ-068; no dedicated issue currently exists.  
**Status:** Candidate new open question; not yet added to `../08-open-questions.md`.

#### Candidate new open question CNOQ-2: Negative-branch process intertwiner

**Priority:** P2  
**Blocks Paper I:** No; it blocks the claim that the three-branch family unifies Paper I.  
**Question:** After the exact Cayley base equivalence, is there an explicit map intertwining affine arithmetic right actions, symmetric-space transvections, contact forms, brackets, and finite residues?  
**Required evidence:** PO-04–PO-06.  
**Likely paper destination:** Paper IV comparison chapter.  
**Relation to `../08-open-questions.md`:** Refines OQ-007, OQ-022, OQ-049, and the unnumbered projective-contact bridge in the Paper I outline.  
**Status:** Candidate new open question; not yet added to `../08-open-questions.md`.

#### Candidate new open question CNOQ-3: Gauge-invariant content of \(r_c\)

**Priority:** P3  
**Blocks Paper I:** No.  
**Question:** Under allowed changes of section, what invariant survives: an element, conjugacy class, loop phase, curvature form, or no nontrivial quantity?  
**Required evidence:** Gauge law, loop composition, and at least one nontrivial closed example.  
**Likely paper destination:** Paper IV.  
**Relation to `../08-open-questions.md`:** A concrete refinement of OQ-049.  
**Status:** Candidate new open question; not yet added to `../08-open-questions.md`.

#### Candidate new open question CNOQ-4: Cross-scale coefficient system

**Priority:** P3  
**Blocks Paper I:** No.  
**Question:** Can the local contact defect, a Paper III closed transport invariant, and Paper IV history-fiber growth be related through one coefficient object or representation functor?  
**Required evidence:** Individually established invariants and explicit comparison maps.  
**Likely paper destination:** Beyond Papers I–IV or a later synthesis.  
**Relation to `../08-open-questions.md`:** Extends OQ-022, OQ-045, OQ-049, and OQ-055; too early to register as a theorem target.  
**Status:** Candidate new open question; not yet added to `../08-open-questions.md`.

## 16. Recommended next tasks

### Task 1: Signed-curvature symbolic and convention audit

**Goal:** Verify every exact formula for \(\mathbb A_c\), \(M_c\), \(\mathsf T_\xi^c\), \(r_c\), determinants, poles, product order, and real-axis bilateral realization.  
**Allowed files:** Create only `restructure/calculations/three-branch-symbolic-audit.md`.  
**Forbidden files:** `../../aeg-paper.tex`, `../../sections`, Papers I–IV sources, `restructure/00–08`.  
**Theorem nodes:** `P2`, `T2`, `P5` as imports only.  
**Expected output:** A formula/domain/convention table plus hand or CAS checks for two numerical examples.  
**Validation:** Independent recomputation of matrix action and chronological composition; verify all denominators and determinants.  
**Blocking questions:** OQ-002–OQ-004; DD-01–DD-04.

### Task 2: Negative-branch Cayley base proof

**Goal:** Turn Result R-8 into a complete exact coordinate proof for metric, assignment, eikonal, Laplacian, and curvature normalization.  
**Allowed files:** Create only `restructure/calculations/negative-branch-cayley-base.md`.  
**Forbidden files:** Paper body and authoritative files.  
**Theorem nodes:** `T6`, `E3`.  
**Expected output:** A self-contained calculation with hypotheses and both Cayley orientations checked.  
**Validation:** Symbolic differentiation and pullback calculation; compare directly with `../../sections/sec04.tex`.  
**Blocking questions:** OQ-001, OQ-013, OQ-014.

### Task 3: Iwasawa and process-generator comparison

**Goal:** Determine whether the current affine arithmetic directions intertwine with the negative-branch symmetric displacements.  
**Allowed files:** Create only `restructure/calculations/negative-branch-iwasawa-process-test.md`.  
**Forbidden files:** Paper body, analytic theory, tube/knot files.  
**Theorem nodes:** `P3`, `P5`, `T5`, with `T15` as later interface.  
**Expected output:** Explicit \(KAN/NAK\) decomposition for \(c=-1\), \(\xi=r\), \(\eta=ir\), including left/right vector fields and a pass/fail conclusion.  
**Validation:** Matrix multiplication, pushforward of vector fields, and comparison with the arithmetic-grid maps.  
**Blocking questions:** OQ-002, OQ-003, CNOQ-2.

### Task 4: Section-residue gauge and loop test

**Goal:** Compute the gauge law of \(r_c\), the three-step associator, and one closed-loop residue.  
**Allowed files:** Create only `restructure/calculations/section-residue-gauge-test.md`.  
**Forbidden files:** Paper body and knot claims.  
**Theorem nodes:** No new authoritative node; imports `P2`, `P5`.  
**Expected output:** Local-section formulas, gauge transformation, and classification of what—if anything—is invariant.  
**Validation:** Recompute after at least two nonconstant section changes.  
**Blocking questions:** OQ-049, CNOQ-3.

### Task 5: Tube-source and properness recovery

**Goal:** Locate the missing multi-zero/\(E_{\log}\)/\(E_k\) source or choose one minimal replacement family, then test the Paper III entry conditions.  
**Allowed files:** Create only `restructure/audits/tube-source-and-properness.md`; read historical notes.  
**Forbidden files:** Paper body, authoritative files, and knot invariant claims.  
**Theorem nodes:** `Z3`, `Z5`, `T8`, `Z6`.  
**Expected output:** Exact source provenance or a fully specified candidate family, with a properness checklist.  
**Validation:** Domain, metric, assignment, singular set, flow, zero topology, parameter range, and projection properness all addressed.  
**Blocking questions:** OQ-037–OQ-042; missing source filename.

### Task 6: Minimal braid monodromy and early Markov falsification

**Goal:** Build the smallest intrinsic braid-level example and immediately test conjugation and stabilization behavior.  
**Allowed files:** A new Paper III experiment note and reproducible script directory selected in the task prompt.  
**Forbidden files:** Paper III main theorem source until invariance passes; Paper I.  
**Theorem nodes:** Future Paper III candidates only.  
**Expected output:** Explicit parameter loop, braid word, transported decoration, and stabilization comparison.  
**Validation:** Homotopic loops agree; positive and negative stabilizations are tested; every choice is listed.  
**Blocking questions:** OQ-043–OQ-045; PO-10–PO-13.

### Task 7: Growth calibration on four groups

**Goal:** Fix finite definitions of \(W,N_\rho,M_\rho,D_{\mathcal R}\) and compute or bound them on \(\mathbb Z^2\), Heisenberg, \(F_2\), and \(BS(1,2)\).  
**Allowed files:** Create a Paper IV research note and a small exhaustive-computation script directory selected in the task prompt.  
**Forbidden files:** Paper I and any general time/space theorem.  
**Theorem nodes:** No Paper IV graph yet; import the history/evaluation interface only.  
**Expected output:** Definitions, presentation dependence, tables for small \(n\), known asymptotics with citations, and a falsification report.  
**Validation:** The definitions distinguish noncommutative polynomial growth from free exponential growth and do not equate growth with word-problem cost.  
**Blocking questions:** OQ-047–OQ-056; DD-08, DD-09.

### Task 8: Model-specific resource bridge

**Goal:** For one calibrated example, prove a precise inequality relating a history/normalization quantity to search, memory, or runtime in a fixed model.  
**Allowed files:** Create one Paper IV case-study note; modify no foundational source.  
**Forbidden files:** General complexity claims and physical analogies.  
**Theorem nodes:** Future Paper IV candidate only.  
**Expected output:** State graph, encoding, transition costs, algorithm, simulation map, and proved inequalities.  
**Validation:** Change the encoding or generating set and report which conclusions survive.  
**Blocking questions:** OQ-054–OQ-058; completion of Task 7.

The strong cross-scale synthesis should not be a standalone implementation task until Tasks 3–4, 6, and 7 have produced stable mathematical objects.

## 17. Source trace

The mathematical discussion was supplied in the current ChatGPT thread and was not provided as a repository transcript file. The uploaded `Pasted markdown(20260805-202809).md` is the note-construction specification, not a mathematical source. Provenance below therefore uses discussion-topic markers rather than fabricated file locations.

| Note section or claim | Discussion source | Related repository source |
| --- | --- | --- |
| §§1–2, strategic ordering of the three directions | 2026-08-05 exchange, “meaning assessment of three branches, tube, and complexity” | `../00-authoritative-scope.md`, §§13–18; `../05-mathematical-status.md`, §§74–102 |
| §4.1, replacement of \(E,H_{\mathrm{Lie}}\) by \(E,F\) at the symmetric level | 2026-08-05 three-branch derivation, generator discussion | `../../notes/bilateral_projective_condensation.tex`, Riccati completion; status `P5` |
| §§4.2–4.3, \(\mathbb A_c\), \(M_c\), \(P_\xi^c\), and brackets | 2026-08-05 three-branch derivation | No committed three-branch file; projective Lie seed in the bilateral note |
| §4.4, four-step bilateral realization | 2026-08-05 three-branch derivation, bilateral-history section | `../../notes/bilateral_projective_condensation.tex`, projective generation theorem |
| §4.5, two-step residue and small-area expansion | 2026-08-05 three-branch derivation, frame-residue section | No committed source; compare Paper IV status §§83, 88, 90 |
| §§4.6–4.7, real forms, metrics, assignment, and negative branch | 2026-08-05 three-branch derivation and subsequent significance review | `../../sections/sec04.tex`; `P5`, `T6`, `E3`; no committed three-branch theorem |
| §4.8, tube/knot success criterion | Tube and threading discussions, 2026-07-25–2026-07-29; 2026-08-05 significance review | `../../archive/paper4p/aeg.tex`; `../../notes/note_02.tex`; `../../knots`; status §§74–81 |
| §4.9, four growth quantities and calibration family | Complexity discussion, 2026-07-28; 2026-08-05 significance review | `../../notes/note_15.tex`; `../../notes/rg_en.tex`; status §§93–100 |
| §4.10, weak versus strong unification | 2026-08-05 final synthesis | `../../README.md`, research frontier; `T17`; Paper IV quotient/complexity status |
| Results R-1, R-2, R-9–R-11 | Imported authoritative repository results, not new discussion discoveries | `../../notes/bilateral_projective_condensation.tex`; `../../sections/sec06.tex`; `restructure/03`, `05` |
| Rejected knot formulations | 2026-08-05 significance review plus source audit | `../../knots/knots_01.tex`–`knots_03.tex`, `../../knots/results.tex`, `../../notes/note_11.tex` |
| Rejected complexity implications | 2026-07-28 and 2026-08-05 discussions | `../../notes/note_06.tex`, `note_09.tex`, `note_15.tex`; authoritative rejection R10 |
| Repository instruction and source-map findings | Current GitHub read-only audit | Root `../AGENTS.md` absent; `../AGENTS.md`, `../../README.md`, `../../README.md`, `restructure/00–08` read |

Where the exact earlier chat message boundary is unavailable, provenance is intentionally marked by topic and date rather than an invented message identifier.

## 18. Final working position

The discussion has produced a disciplined research architecture and several exact algebraic calculations, but not a completed unified theory. The signed-curvature formulas supply a credible projective family: the quadratic addition law, Möbius displacement, infinitesimal \(E/F\) generators, and two-step isotropy residue are exact under stated conventions. The negative branch can also recover the existing upper-half-plane metric and assignment by an explicit Cayley calculation. These facts support further work.

What was corrected is equally important. Imaginary affine scaling does not by itself produce the sphere; bare complexification does not choose a real form; the flat displacement matrices do not contain rotations; the two-step section factor is not yet canonical holonomy; the bilateral bivaluation quotient, constant-curvature frame bundle, and parameterized zero tube are different structures; and noncommutativity, growth, hyperbolicity, and computational hardness cannot be identified.

What is actually proved remains layered. Paper I's projective generation, affine/Borel sector, affine flow, basic hyperbolic model, and contact bracket are the established foundation. The new three-branch algebraic identities are exact but not integrated. Proper tube, braid, Markov, knot, and complexity bridges remain conditional or open.

The next blocking step is not more general theory. It is the negative-branch process test: first write the Cayley base proof, then compare left/right Iwasawa generators, and finally attempt the contact and finite-residue intertwiner. Paper IV owns that development. If it succeeds, Paper III can test the resulting transport on a proper zero tube; if it fails, the three-branch construction should be retained as an adjacent projective arithmetic geometry rather than presented as a unification of AEG.
