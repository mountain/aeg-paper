# Paper III Decision Record

**Paper:** *Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes*

**Subtitle:** *Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

**Decision date:** 2026-08-06

**Baseline:** `24c1df0`

**Status:** integrated manuscript decisions

This record fixes the conventions and claim boundary of the canonical Paper III
manuscript.  It is subordinate to the restructuring authorities and should be read
with `paper-III-source-audit.md` and `paper-III-closure-report.md`.

## D3-01 — Historical names are not imported as theorems

The Git history contains no certifiable general `E_k`, `E_log`, or multi-zero AEG
construction.  Paper III therefore uses descriptive names: parallel multi-zero
model, logarithmic-cover model, cylindrical product tube, and helical zero tube.
The old symbols remain provenance labels only.

## D3-02 — Metric realization and rigidity are separate questions

For any surface submersion `a` and background metric `h`, Paper III uses

```text
g_a = |da|_h^2 / (mu^2 + lambda^2 a^2) h.
```

This proves broad existence.  It also shows that the bare singular-AES category is
too flexible to support an AEG-specific singularity classification.  Completeness,
curvature, asymptotics, homogeneity, a fixed metric, or expression-history
naturality must be added before a rigidity claim is made.

## D3-03 — Seven zero-object levels remain distinct

The canonical order is:

1. total zero set;
2. smooth zero incidence;
3. proper zero tube;
4. embedded zero tube;
5. threaded zero tube;
6. braid closure;
7. knot invariant.

Every transition requires new hypotheses or data.  The manuscript never uses a
later name merely because an earlier object has been drawn.

## D3-04 — Tube means proper submersion

A zero incidence is called a tube only when its projection is a surjective proper
submersion, with neat relative hypotheses at a boundary.  Ehresmann then supplies
local triviality.  The historic disjoint union of ambient AEG slices is called an
ambient family, not a certified zero tube.

## D3-05 — Rank controls transport

A real assignment on a surface has rank one and regular zero curves.  A
complex-valued field has real rank two and isolated roots.  Ordinary Artin braid
monodromy belongs to the second setting.  It is not inferred directly from a real
assignment-zero tube.

## D3-06 — The structural discriminant has several mechanisms

The manuscript separates critical-zero, boundary, singular/metric, domain/category,
and nonproper escape loci.  Ordinary projective poles are recorded separately.
The escape family proves that topology can change at infinity without a critical
zero at a finite point.

## D3-07 — Compact real tubes over a circle are zero tori

For boundaryless surface fibers with a smooth global orientation of the vertical
tangent bundle, a proper regular real zero tube over `S^1` is an orientable mapping
torus of finitely many circles.  Each connected component is a torus.  A merely
fiberwise, discontinuous orientation choice is insufficient and can allow a Klein
bottle.  This classifies the abstract total zero surface under the printed
hypotheses; it does not select a knot inside it or classify its embedding.

## D3-08 — The helical family is the central explicit tube

On `[-L,L] x S^1` over `S^1`, Paper III uses

```text
A(x,y,theta) = exp(n x) sin(n y - m theta).
```

The conformal metric, properness, neat boundary, `2n` zero intervals, label shift
`k -> k+2m mod 2n`, `2 gcd(n,m)` annular components, logarithmic deck shift, and
boundary homology class are all proved.  The torus-link name is used only after the
ordered torus coordinates are declared.

## D3-09 — Real Morse events and complex branching are different

The real models `x^2+y^2-tau` and `x^2-y^2-tau` are singular-AES birth/death and
reconnection examples.  The complex model `w^2=tau` is a branched root filling.
Its boundary is collision-free and carries a half-twist; the collision lies in the
filling.  None of these examples is advertised as a universal AEG metric normal
form.

## D3-10 — Every-braid realization is a function-theory theorem, not an invariant

Paper II's arithmetic-holomorphic coordinate allows any configuration loop in a
small disc of the basic hyperbolic AES to be encoded by a monic square-free
polynomial.  This realizes every braid and, by closure, every link.  Because the
construction is universal and chosen, representability alone has no separating
power.

## D3-11 — Logarithmic labels have lift gauge

For moving nonzero roots, individual logarithmic endpoint integers depend on the
initial lifts.  Their gauge law is

```text
k_i -> k_i + m_i - m_{sigma(i)}.
```

Cycle sums and total winding are gauge invariant; the full noncommutative datum
remains the configuration path or annular braid.

## D3-12 — A thread is a declared finite multisection

A finite zero thread over a one-manifold base is a properly embedded
one-dimensional submanifold inside a real zero tube whose projection is a
finite-sheeted covering, with the corresponding relative-boundary condition.  A
transverse slice such as `x=c` in the helical model is a valid thread only with that
probe choice recorded.  Intrinsic threading requires a functorial selection theorem
and remains open.

## D3-13 — Scalar and affine candidates pass a novelty filter

Every stateless additive scalar on a braid group factors through writhe and becomes
trivial under compatible two-sided Markov stabilization.  Fixed-multiplier affine
conjugation is exactly an Alexander quandle, and its ordinary torsion cocycle is a
coboundary.  Variable-multiplier Reidemeister-III defect is only an anomaly formula,
not an associator or higher invariant.

## D3-14 — Resonant twisted torsion is algebraically nonzero but planar-trivial

Over `F_q`, with `t != 1`, quandle parameter and coefficient action both
`alpha=t^{-1}`, the affine torsion

```text
kappa(x,y) = (t-1)(y-x)
```

is a normalized twisted 2-cocycle and is not a coboundary.  The finite-order
recurrence proves the nonzero cohomology class for arbitrary one-cochains.  However,
it is the obstruction cocycle of an explicit Alexander-module extension.  The
standard state sum of every planar classical link consequently equals the Alexander
quandle coloring count.  Cohomological nontriviality is not relabeled as nontrivial
knot detection.

## D3-15 — Knot and beyond-Burau claims remain gated

No new AEG knot invariant is claimed.  A future candidate must prove braid
relations, conjugation, positive and negative stabilization, and independence of
lift, probe, thread, spine, axis, basepoint, and presentation as applicable.  A
claim beyond Alexander/Burau additionally requires an explicit closure-level
separation pair under a declared baseline.

## D3-16 — The figure-eight computation remains a word calculation

Under the printed affine convention, the free word `abbbaBAAB` has translation
`-(t^2-3t+1)`.  It descends to the corresponding knot-group representation only on
the zero locus of that polynomial.  At generic `t` it is a relator failure, not an
intrinsic knot invariant.

## D3-17 — Branched holomorphic pullback is the controlled singular subclass

Paper III distinguishes arbitrary conformal realization from the more constrained
holomorphic-pullback subclass exported by Paper II.  If the local holomorphic degree
is (m\ge2) and the critical value lies on the target zero line, the singular zero
germ has (2m) prongs and the pullback metric completion has cone angle (2\pi m).
The critical point is locally essential because its assignment differential
vanishes while the regular AES eikonal right-hand side is positive.

The result classifies this pullback germ only.  It is not advertised as a
classification of all singular AES germs.

## D3-18 — The order-four apeirogonal model is automorphic and equivariant

Paper III uses a normalized ((2,4,\infty)) Hauptmodul (\beta) as a cited standard
input and derives

[
F^2=\frac{\beta}{1-\beta},
\qquad
W=\frac{F-i}{F+i},
\qquad
a=\frac{\mu}{\lambda}\sinh(\lambda\log|W|),
\qquad
g=\left|\frac{dW}{W}\right|^2.
]

On the regular locus its zero graph is exactly
(\beta^{-1}([0,1])).  Points over the order-four branch value become four-valent
zeros with (4\pi) cone completion; order-two points are ordinary edge midpoints
after the square-root step.  Suppressing those midpoints gives the
(\{\infty,4\}) skeleton.

The exact sign character is

[
\chi(J)=-1,\qquad \chi(JT)=-1,\qquad \chi(T)=+1.
]

The metric and zero graph descend to the full group quotient.  The assignment is
therefore treated either as a scalar on the sign-character kernel or as a real
line-bundle section on the full quotient.  Upstairs, order-four points complete to
(4\pi) cones; the coarse full quotient has angle (\pi) at each elliptic image.  The
full quotient length metric is complete after the finite-distance singular orbit is
adjoined, and its cusp is at infinite distance.  This model-specific metric
completion does not imply universal-cover or finite-index properness, a proper zero
tube, or smooth regular-AES geodesic completeness.

## D3-19 — Arithmetic zero paths are relative prime divisors, not labelled roots

For a family defined over an integral domain, Paper III distinguishes:

1. literal histories and their projective operators;
2. arithmetic irreducibility over (K(B));
3. geometric irreducibility over (\overline K(B));
4. local complex sheets;
5. geometric monodromy;
6. Galois, inertia, reduction, and Frobenius actions.

An irreducible zero-path system is represented by the normalization of a prime
relative divisor, not by one arbitrarily labelled local root.  Transitive complex
monodromy requires geometric irreducibility; arithmetic irreducibility alone is not
silently substituted.

## D3-20 — The general history functor remains open

The desired arrow

[
H\longmapsto P_H\longmapsto (P_H)_0
]

is a structural proposal.  It must preserve a declared history equivalence,
composition, chirality, field of definition, and parameter concatenation before it
can support an AEG-natural braid or invariant.  The (q=4) construction solves a
restricted projective-operator case; it does not solve the general problem.

## D3-21 — Hecke arithmetic and factorization arithmetic are separate

The (q=4) model supplies arithmetic group symmetry, continued-fraction structure,
and automorphic uniformization over (\mathbb Q(\sqrt2)).  It does not supply
nonunique factorization in (\mathbb Z[\sqrt2]).  Any factorization-theoretic
version of inequivalent routes to zero requires a separate integral family with
nontrivial ideal-class or factorization data.

## D3-22 — The sign cover has a precise global link-complement realization

Let (H_4=\ker\chi).  Its orbifold quotient has signature
((0;2;\infty,\infty)).  After coarse completion, the coordinate (W) identifies
the AEG surface with the complete flat cylinder (\mathbb C^\times); this
statement forgets the residual order-two orbifold isotropy.

For the hyperbolic orbifold structure, Paper III uses the standard cusp filling
of the unit tangent bundle.  The full-group compactification is
(L(2,1)=\mathbb {RP}^3), and the index-two cover extends to
(S^3\to\mathbb {RP}^3).  The lifted cusp fiber is the two-component link
(T(2,4)), so

[
T^1(H_4\backslash\mathbb H)\cong S^3\setminus T(2,4).
]

This is a global orbifold, peripheral-cover, and slope calculation.  It is not an
identification of the local four-pronged surface germ with a torus link.

## D3-23 — Hecke histories give knots only after the operator and unit-tangent quotients

For a marked (q=4) history (h) whose projective operator (\rho(h)) is primitive
hyperbolic, Paper III defines the oriented geodesic-flow periodic orbit
(K_{\rho(h)}).  Cyclic word shift changes the operator by conjugacy, path inverse
gives the time-reversed orbit, and every primitive hyperbolic class occurs.  The
map factors through operator conjugacy and therefore collapses (\omega_4) and all
other marked changes invisible to that quotient.

The zero dessin is the Dehornoy--Pinsky coding graph and the barycentric
subdivision of the ideal-quadrilateral dual tree.  A hyperbolic axis is not
contained in that graph.  The three-dimensional template appears only after the
classical admissible-path, roundabout, and visual-direction construction.  The
classical template and cusp-linking theorem are cited inputs; no new knot
invariant is claimed.

## D3-24 — Supplied registers give a minimal divisor naturality model, not the general functor

Paper III fixes the typed register (u^2=t) and proves that a projective operator
(h(z)=(az+b)/(cz+d)) forces the homogeneous quadratic endpoint divisor

[
(dZ-bW)^2-t(aW-cZ)^2=0.
]

It is equivariant under composition.  As an abstract cover it is independent of
(h); as an embedded divisor it recovers the restricted (\Gamma_4) operator, but
it cannot recover a marked word in a (\rho)-fiber.  The time-tagged prefix trace
and ordinary pole divisor retain more: they distinguish the neutral word
(\omega_4) from the empty history and record its bad register parameters
(t=2) and (t=1/2).

The second supplied tower (v^2=3), (u^2=t+v) forces
((u^2-t)^2-3).  It is irreducible over (\mathbb Q(\sqrt2)(t)), splits into two
irreducible components after extending constants, and has explicit discriminant,
local monodromy, and Frobenius cycles.  These results partially resolve the
finite arithmetic/geometric test.  They do not prove that the registers are
canonically generated by unrestricted arithmetic histories.

## D3-25 — A polynomial may relate slices by carrying both a real surface and a root thread

Paper III now treats a supplied parameterized polynomial (P(z,t)) as a
horizontal relation, not merely as a list of independent slice functions.  The
real equation (operatorname{Im}P=0) is its carrier; the complex equation
(P=0) is an embedded finite thread inside that carrier.  Root square-freeness
does not prevent the carrier from changing topology, because a nonroot critical
value may cross the real axis.

For

[
P_m(z,t)=z^2-t^m,qquad t\in S^1,quad m\ge1,
]

on a disc of radius (R>1), the carrier is a compact connected neat surface
with four boundary components, (2m) index-one saddles, Euler characteristic
(-2m), and genus (m-1).  Its slice metrics are singular AES metrics with a
declared essential center and (4pi) cone completion.  The root thread is
(sigma_1^m), with closure (T(2,m)).

The same integer has the proved readings

[
\operatorname{ord}_{0}\operatorname{Disc}P_m
=\frac1{2\pi i}\oint d\log\operatorname{Disc}P_m
=\operatorname{exp}(\sigma_1^m)
=-\operatorname{Fr}_{\Sigma_m}(K_m)
=-\frac12\chi(\Sigma_m)
=m.
]

The framing uses the declared spatial complex trivialization.  For even (m),
the pure-braid coordinate and mutual linking number are (m/2).  Arithmetic
irreducibility, thread connectedness, and knot rather than two-component link
are all equivalent to odd parity in this family.

For (q=4), the already proved lifted median-torus lattice, deck action, and
cusp slope (2m_P+m_Q) force the two-coset Laurent divisor
(u^2=t^4) after an ordered meridian marking and unit normalization.  This is
stronger than matching abstract link types, but weaker than deriving a unique
coordinate polynomial: toric gauges remain, and radial extension to the
genus-three carrier is supplied data.

The marked compactified sign cover provides a stronger intrinsic level.  As a
complex orbifold pair it is (mathbb P(2,1),V(U^2-V^4)); the logarithmic tangent
line is (mathcal O(-1)), and its graded section ring recovers the cusp binomial as
a degree-four section.  Its weighted Hopf circle bundle realizes the standard
cusp filling and (T(2,4)).  The affine cone vertex is not the Hecke order-four
point or the real four-pronged zero germ.  Over (mathbb Q(sqrt2)), the split and
nonsplit quadratic twists require an explicit arithmetic descent choice.

The information loss is governed by

[
1\to P_2\to B_2\to S_2\to1.
]

At (m=4), factorization and root permutation see two fixed sections, while the
kernel retains pure coordinate (2), equal to linking.  This pure-braid
extension is not the unit-tangent central extension: the order-two and order-four
elliptic relators have different unweighted pure-braid residues but the same
unit-tangent fiber rotation.  No Paper I torsion transgression or new Markov
invariant is claimed.

Four strands nevertheless supply an exact calibration: the Garside half-twist
squared and the four-point rotation raised to the fourth power are the same full
twist.  With the printed clockwise convention, their inverse paths identify the
q=4 unit-tangent extension with the pullback of the braid-center extension, and
their normalized discriminant periods equal one negative fiber winding.  The
associated invariant integer character on the free-word operator kernel has LHS
transgression equal to the unit-tangent Euler extension class.  It is a new
projective-relation residue, not Paper I's affine torsion or a transgression over
the circle parameter.  These
root paths are supplied data; their inverse full-twist closure is (T(4,-4)), not
the cusp link (T(2,4)), and no general history-natural coefficient-path functor
follows.

## D3-26 — The sextic LL laboratory is a typed forgetting map, not a curve count

The supplied sparse sextic

[
P_0(x)=x^6-x
]

now gives Paper III one explicit nonabelian laboratory.  Its event polynomial is
the critical-value quintic

[
Q_0(t)=6^{-6}\operatorname{Disc}_x(P_0(x)-t)
=t^5+\frac{5^5}{6^6}.
]

The five local vanishing arcs form a six-vertex spanning star and their
half-twists generate (B_6).  A collision-free parameter loop simultaneously
produces the printed real carrier, the six-root thread, and a genus-two
branched-cover mapping torus.  Carrier saddle walls, root collisions,
critical-value collisions, caustic/Maxwell events, and singular fibers of the
hyperelliptic pencil are retained as distinct strata.

The Lyashko--Looijenga theorem, its degree calculation, the
caustic/Maxwell multiplicities, Birman--Hilden lifting, symplectic monodromy,
and the arithmetic Galois/endomorphism criteria are classical inputs, not AEG
theorems.  In the chosen monic-centered coordinates the regular LL fiber has
(6^4=1296) normalized sheets.  The residual free source rotation by (\mu_6)
gives (216) orbits.  Neither number counts pairwise nonisomorphic genus-two
curves.

Critical-value braiding and six-root braiding are joined only on the typed
mixed configuration space.  Paper III uses

[
1\longrightarrow F_5\longrightarrow B_{5,1}\longrightarrow B_5
\longrightarrow1
]

and its pullback along the LL cover (equivalently, the corresponding Hurwitz
groupoid).  It does not assert a canonical homomorphism (B_5\to B_6) after the
LL sheet has been forgotten.

The full genus-two mapping-class, integral symplectic, mod-two permutation, and
displayed arithmetic-fiber conclusions are available through the stated
specializations.  Nevertheless, the common abstract target
(\operatorname{Sp}_4(\mathbb F_2)\cong S_6) does not canonically identify a
Frobenius element with a topological loop.  The LL--Igusa twin calculation and
the natural selection of an LL sheet or mixed-braid path by an unrestricted AEG
history remain open.  Until those tests are completed, no new moduli invariant,
history-natural knot invariant, or count of nonisomorphic curves is claimed.
