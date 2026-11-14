# The Hyperbolic Tropical Wavefront–Residual Core (HTWR Core): Spacetime Duality from the Minimal Quantale to a Nonlinear Arithmetic Language

> **Document nature**: research notes on the foundational architecture and the axiomatics of a nonlinear language of Arithmetic Expression Geometry (AEG).
> **Date**: 2026-11-13
> **Remark**: the core ideas, the derivational thread, and the axiom system of this note were formed in critical dialogue and collaborative derivation with **Google Gemini (Carbon build)**.

---

## I. Origin of the problem: distilling the Quantale

Christopher Mulvey introduced the Quantale (quantum lattice) to seek a pointless-topology (locale) spectral duality for non-commutative $C^*$-algebras. But because non-commutative multiplication destroys the idempotence of the meet ($a \wedge a = a$), the geometric intuition that "algebraic elements correspond to regions of space" is obstructed, and the programme stalls on spectral reconstruction. Conversely, the Quantale finds a redundancy-free home in generalised metric geometry (Lawvere metric spaces) and in resource/program logic (Lambek calculus, Hoare weakest preconditions). Its true core is **not** "reconstructing the points of a space", but rather: **the distributivity of non-commutative process composition over the extrema ($\bigvee/\inf$) is equivalent to the existence of two-sided resources residuals ($a \backslash c,\ c / b$)**.

Introducing the standard Quantale into AEG to characterise resource complexity and the computational spacetime duality produces three redundancies and conflicts:

1. **Over-axiomatised complete lattice**: demanding arbitrary joins ($\bigvee$) at a discrete finite syntactic layer forces a single arithmetic expression to degenerate into a formal power set, masking the concrete geometric tree/graph structure.
2. **Conflation of scalar cost and non-commutative curvature**: scalar cost accumulation is commutative, whereas AEG's core non-commutativity stems from the Lie-bracket defect ($[A, M] \neq 0$) of the affine generators (addition and multiplication); a single semigroup multiplication cannot carry both at once.
3. **A single multiplication cannot separate the spacetime dimensions**: one-dimensional semigroup composition only encodes serial temporal composition, and cannot endogenously represent the cutting-interface width (Space / Cut Capacity) of multi-branch suspension.

One must therefore strip the pointless-topology shell of the traditional Quantale, and, combining it with AEG's vision of a **native nonlinear language**, rebuild a minimal algebraic-geometric duality kernel.

---

## II. The core dialectic and the five-step derivational thread

The convergence of this axiom system passed through a rigorous examination and adjudication of five key theoretical forks:

1. **Logical anchoring of spacetime duality (history-context adjunction first)**
   Take the two-ended evaluation pairing (Chu construction / Galois polarity) of prefix evaluation history $\mathcal{H}$ (Time) and suffix context / cutting interface $\mathcal{K}$ (Space) as the first-principles base. No complete lattice is presupposed; the residual-closure fixed points auto-generate the complete-lattice structure. The cross-section geometry of a continuous contact manifold then emerges endogenously from this discrete adjoint structure under a state metric.
2. **Native nonlinear syntax and the crisis of the linear distributivity law**
   Abandon the traditional "pure-tree syntax plus patches" route; natively allow multiple fan-out of directed acyclic graphs ($\Delta: u \mapsto (u, u)$) in the definition of the cutting interface (Cut $[m]$). The derivation shows: once a context internally contains nonlinear reuse (e.g. $k(\square) = \square \times (\square + 1)$), the evaluation pairing produces a diagonal coupling that directly breaks the syntactic-level linear distributivity $\langle h_1 \vee h_2, k \rangle = \langle h_1, k \rangle \vee \langle h_2, k \rangle$. The way out is to lift the pairing to a **tropical wavefront function module** over the cross-section state space, recovering strict distributivity by operator-presheaf linearisation.
3. **First-class fan-out singularities and the condensation phase transition**
   Refuse to treat variable reuse as a zero-cost syntactic wire; establish the fan-out $\Delta: [1] \to [2]$ and the erasure $\epsilon: [1] \to [0]$ as basic generators carrying positive action cost. This yields the **condensation phase-transition criterion (the holographic scissors gap)** of the nonlinear language: only when the history action $\mathcal{A}(f)$ preparing some state exceeds its instantaneous fan-out cost $c_\Delta(u)$ does the system condense a high-curvature DAG sharing hub (corresponding to a two-dimensional worldsheet handle, genus $g \ge 1$); shallow trivial computations ($\mathcal{A}(f) < c_\Delta(u)$) spontaneously crack back into zero-curvature local pure trees ($g = 0$).
4. **Semantic quotient calibration and the automatic emergence of contact geometry**
   Fix the wire states to live in the **minimal semantic quotient space** $\mathbb{P}^1(\mathbb{Q})$, and charge both the fan-out node $\Delta$ and the arithmetic nodes $(+, \times)$ in proportion to the input state's information height $I(u)$ (logarithmic Weil height). This single decision solves three problems at once:
   * **Closing the physical loopholes**: it terminates both the BSS unit-cost "free lunch" of repeated squaring fabricating exponential bit-width, and the "free $\gcd$ cancellation loophole" on the quotient space, by charging at the arithmetic-gate entrance in proportion to the full tube diameter.
   * **Forcing contact geometry**: because the downstream fan-out cost depends on the input state, the suffix context $k$ loses its fixed scalar cost and becomes a state-dependent residual potential functional $\mathcal{W}_k(u)$. The total-action extremal variation $\delta(z + \mathcal{W}_k(u)) = 0$ directly induces the contact $1$-form $dz + p\,dI = 0$ on the cross-section, where the conjugate momentum $p = \partial \mathcal{W}_k / \partial I$ exactly measures the fan-out load amplification of the downstream context on the current wire's bit-width.
   * **Revealing the associativity metric defect**: the value space $\mathbb{Q}$ obeys strict associativity, but the context space $\mathcal{K}_m$ — because different bracketing orders inflate the intermediate tube diameter or collapse by early cancellation — produces a nonzero action torsion (Associator Defect), forming a non-strict Lax $2$-category.

5. **Hyperbolic holographic calibration and the scattering-wormhole picture (single hyperbolic base $\beta_1$)**
   Facing the fractal obstacle that the Weil height $I(p/q)$ is everywhere discontinuous on the Euclidean real axis, refuse both the introduction of an external error parameter for artificial smoothing and the inflation to an infinite-dimensional Adelic product space. Instead anchor the semantic boundary directly in a **single real hyperbolic upper half-plane $\mathbb{H}^2$** (and its unit cotangent contact manifold $S^*\mathbb{H}^2$). The information $I(u)$ is natively geometrised as the smooth radial geodesic distance from the hyperbolic centre to the cusp Ford limit circle; unary Möbius transformations correspond to isometric flows of the bulk space, while binary addition/multiplication and common-factor cancellation are honestly represented as discrete scattering vertices on the hyperbolic worldsheet and as cross-scale "arithmetic wormholes".

---

## III. The formal axiom system: the Hyperbolic Tropical Wavefront–Residual Core (HTWR Core)

Let the scalar cost structure be the minimal Lawvere tropical semiring $\mathcal{Q} = ([0, \infty], \ge, +, 0)$ (order direction: $\inf$ as join, $+$ as tensor). The resource and spacetime duality of AEG is characterised by the following four axioms:

### Axiom I: Semantic quotient state and hyperbolic holographic calibration (State & Hyperbolic Calibration)

1. **Markov semantic state**: the single-channel state space is the projective rational quotient set $X := \mathbb{P}^1(\mathbb{Q}) = \mathbb{Q} \cup \{\infty\}$. Any reduced element $u = p/q \in X$ ($\gcd(p,q)=1$) completely determines its subsequent evolution cost, with no redundancy from path history.
2. **Hyperbolic–contact geometric anchoring**: endow the upper half-plane $\mathbb{H}^2$ with the standard hyperbolic metric $ds^2 = (dx^2 + dy^2)/y^2$ and the base point $z_0 = i$. Each boundary cusp $u \in X$ is uniquely associated with its tangent Ford limit circle $C_u \subset \mathbb{H}^2$ (lifted to the standard Legendrian curve in the unit cotangent sphere bundle $S^*\mathbb{H}^2 \cong \mathrm{PSL}(2, \mathbb{R})$).
3. **Information tube diameter (radial depth)**: the intrinsic information of a state $u$ is calibrated by the hyperbolic geodesic distance from the base point to the limit circle $C_u$:

$$I(u) := \frac{1}{2} d_{\mathbb{H}^2}(i, C_u) + c_0 \asymp \ln \max(\vert{}p\vert{}, \vert{}q\vert{})$$

where the constant $c_0$ is normalised so that the trivial states satisfy $I(0), I(\pm 1), I(\infty) \ge 0$.

### Axiom II: Rigged worldsheet syntax with metric, and the local area action (Rigged Worldsheet Syntax)

1. **Graded cross-section spaces and flux**: the transverse interface of a computation is a graded object $[m]$ carrying $m$ live wires (state space $X^m$). The instantaneous spatial complexity (total transverse flux) of a cross-section state tuple $\mathbf{u} = (u_1, \dots, u_m) \in X^m$ is the sum of fat-tube circumferences:

$$\Sigma(\mathbf{u}) := \sum_{j=1}^m I(u_j)$$

2. **First-class topological generators**: the nonlinear DAG syntax category is generated by four kinds of directed pair-of-pants (cobordisms) under serial welding ($\rhd$) and parallel juxtaposition ($\otimes$):
   * **geodesic propagator** $\gamma \in \mathrm{PSL}(2, \mathbb{Z})$: $[1] \to [1]$, evolving along an isometric flow of $\mathbb{H}^2$;
   * **binary scattering pants** $\star \in \{+, \times, \div\}$: $[2] \to [1]$, performing arithmetic composition and the potential common-factor cancellation transition;
   * **nonlinear fan-out pants** $\Delta$: $[1] \to [2]$, $u \mapsto (u, u)$, producing a worldsheet handle (genus $g \ge 1$) and cross-channel coupling;
   * **thermodynamic erasure cap** $\epsilon$: $[1] \to [0]$, releasing a live wire at the end of its life cycle.

3. **Local worldsheet area action**: any basic generator $g: [r] \to [s]$ at input state $\mathbf{u}_{\text{in}} \in X^r$ consumes a strictly positive local action:

$$c_g(\mathbf{u}_{\text{in}}) := \epsilon_0 + \alpha_g \sum_{j=1}^r I(u_j) \qquad (\epsilon_0 > 0,\ \alpha_g > 0)$$

The total action $\mathcal{A}$ of a general nonlinear network is the sum of the local actions of all its internal generators (a shared upstream node is counted once).

### Axiom III: Tropical wavefront module and entangling linearisation (Tropical Wavefront Linearization)

1. **Prefix wavefront collapse**: the set $\mathcal{H}_m = \mathrm{Hom}([0], [m])$ of all prefix histories of output width $m$ is collapsed, by the least-action principle, into the **preparation wavefront functional (Eikonal Wavefront)** in the free $\mathcal{Q}$-module $\mathcal{Q}^{X^m}$:

$$V_m(\mathbf{u}) := \inf \big\{ \mathcal{A}(h) \;\big\vert{}\; h \in \mathcal{H}_m,\ \mathrm{val}(h) = \mathbf{u} \big\}$$

* a pure-tree juxtaposition with no shared ancestor corresponds to a **tropical separable product state**: $V(\mathbf{u}_1, \mathbf{u}_2) = V_1(\mathbf{u}_1) + V_2(\mathbf{u}_2)$;
* a nonlinear DAG containing a $\Delta$ fan-out corresponds to a **tropical entangled state** concentrated on a low-dimensional algebraic subvariety (e.g. $(\mathcal{T}_\Delta V)(u_1, u_2) = V(u_1) + c_\Delta(u_1)$ when $u_1 = u_2$, and $+\infty$ otherwise).

2. **Context Bellman transfer operator**: any nonlinear suffix context $k \in \mathcal{K}_m = \mathrm{Hom}([m], [1])$ induces a semantic map $f_k: X^m \to X$ and a state-dependent residual potential $\mathcal{W}_k: X^m \to [0, \infty)$, lifted to a module homomorphism $\mathcal{T}_k : \mathcal{Q}^{X^m} \to \mathcal{Q}^X$:

$$(\mathcal{T}_k V)(y) := \inf_{\substack{\mathbf{u} \in X^m \\ f_k(\mathbf{u}) = y}} \big\{ V(\mathbf{u}) + \mathcal{W}_k(\mathbf{u}) \big\}$$

$\mathcal{T}_k$ preserves strict distributivity over pointwise infima: $\mathcal{T}_k(\inf_\alpha V_\alpha) = \inf_\alpha \mathcal{T}_k(V_\alpha)$.

### Axiom IV: Bellman–Galois two-sided residual and spacetime conservation (Spacetime Residual Duality)

1. **Residual adjoint envelope**: by the order-preservation of $\mathcal{T}_k$, given a target state $y^* \in X$ and a total-action budget $B \in [0, \infty)$, one uniquely induces the reverse residual operator (maximal admissible prefix-cost envelope):

$$\mathcal{R}_{k, y^*}(B)(\mathbf{u}) := \begin{cases} B - \mathcal{W}_k(\mathbf{u}), & \text{if } f_k(\mathbf{u}) = y^* \\ -\infty \ (\text{unreachable}), & \text{if } f_k(\mathbf{u}) \neq y^* \end{cases}$$

The prefix wavefront and the suffix residual satisfy the duality solvability criterion: the target $y^*$ is reachable within budget $B$ iff there exists a cross-section state $\mathbf{u} \in X^m$ with $V_m(\mathbf{u}) \le \mathcal{R}_{k, y^*}(B)(\mathbf{u})$. By the Diophantine-geometric **Northcott theorem**, the effective residual support set $\{\mathbf{u} \mid \mathcal{R}_{k, y^*}(B)(\mathbf{u}) \ge 0\}$ is strictly finite for any finite budget.
2. **Endogenous spacetime tradeoff law**: when the spatial cross-section flux constraint $\Sigma(\mathbf{u}) \le \Sigma_{\max}$ is imposed, any deep hub state $u$ that satisfies the condensation condition $\mathcal{A}(f) > c_\Delta(u)$ but exceeds the residual flux quota cannot survive crossing the cross-section; it is forced to be erased by $\epsilon$ and recomputed after unfolding in the downstream context — thereby quantitatively converting the compression of the transverse spatial flux into a rigid growth of the longitudinal total action $\mathcal{A}$ (time).

---

## IV. Core geometric corollaries and subsequent research targets

| phenomenon | geometric mechanism in the HTWR core | concrete mathematical problem to attack |
| --- | --- | --- |
| **Associativity defect and geodesic routing** | $(a+b)+c$ and $a+(b+c)$ are semantically equal, but intermediate common-factor cancellation (funnel collapse) makes the tube-area integral of different bracketing paths differ by $\Theta(N)$; the associator carries nonzero action torsion. | characterise the local curvature criterion and the greedy-failure boundary of optimal bracketing order in rational add/multiply networks. |
| **Wormhole interpretation of algebraic simplification** | routing through the hyperbolic abyss (e.g. the difference of squares $(x-1)(x+1) = x^2 - 1$, or repeated squaring) and then jumping back to shallow water via cancellation; the full-tube-diameter entrance charge ensures no violation of the second law of thermodynamics, the net gain coming from the exponential compression of shallow linear geodesic steps by a high-genus handle. | rigorously prove the minimal genus threshold at which a "Catalytic Wormhole" beats the pure shallow $\mathrm{PSL}(2, \mathbb{Z})$ continued-fraction flow. |
| **The spacetime Pareto frontier** | constraining the maximal cross-section flux $\Sigma_{\max}$ forces a high-genus worldsheet to degenerate and unfold into a low-genus long tube, forming a convex envelope in the $(\mathcal{A}, \Sigma)$ plane. | choose typical test sequences (e.g. $2^N - 1$, the Fibonacci rational-approximation sequence, or the Sylvester sequence) and compute exactly the first nontrivial $(\mathcal{A}, \Sigma)$ Pareto curve. |
