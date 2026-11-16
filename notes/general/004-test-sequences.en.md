# Testbed Sequence Selection and a Unified Metallic-Means View: Pell / Fibonacci / Sylvester / Recamán

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (Part III: testbed-sequence selection, structural comparison, and status labelling for the HTWR core).
> **Prerequisites**: Note I, *The HTWR Core* ([001-htwr-core.md](001-htwr-core.md)); Note II, *The Exact Spacetime Pareto Frontier* ([002-htwr-example.md](002-htwr-example.md)) and its compiled version ([003-htwr-core.tex](003-htwr-core.tex)).
> **Date**: 2026-11-13
> **Remark**: this note positions the four candidate testbeds Pell, Fibonacci, Sylvester and Recamán under the HTWR core, unifying Pell and Fibonacci into the metallic-means family; all identities are independently numerically verified (marked in the text), and the HTWR order-of-magnitude analyses are carried out as structural translations of Axioms I–IV with their status stated explicitly.

---

## I. Purpose and scope

This note continues the task posed in Note I's "Core geometric corollaries and subsequent research targets" (line 121 of [001-htwr-core.md](001-htwr-core.md), line 504 of [003-htwr-core.tex](003-htwr-core.tex)):

> Select typical test sequences (e.g. $2^N-1$, the Fibonacci rational-approximation sequence, or the Sylvester sequence) and compute exactly the first nontrivial $(\mathcal A,\Sigma)$ Pareto curve.

Here we perform a **structural positioning** of the candidate sequences: which sequences fall into the "quadratic-irrational convergent" spectrum of Pell (whose HTWR analysis translates wholesale), which fall into other spectra, and which carry no usable algebraic structure at all. $2^N-1$ is only marked for later. This note **does not** modify Axioms I–IV, nor does it restate their proofs; it only performs structural comparison, identity verification, and status labelling.

---

## II. Status-label conventions

This note follows the authoritative labels of [governance/05-mathematical-status.md](../../governance/05-mathematical-status.md):

- `PROVED` / `PROVED WITH STATED HYPOTHESES`
- `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`
- `COMPUTATIONALLY VERIFIED EXAMPLE`
- `PARTIALLY PROVED`
- `STRUCTURAL PROPOSAL`
- `CONJECTURE` / `OPEN PROBLEM` / `UNSUPPORTED AND EXCLUDED`

One principle (per AGENTS.md): the HTWR Axioms I–IV are themselves an **axiomatic proposal** (`STRUCTURAL PROPOSAL`; see the titles of Notes I and II and their remarks). Hence "theorems proved under Axioms I–IV" are **conditional** conclusions — they hold relative to the axioms but do not thereby automatically become publishable general theorems. This note labels every HTWR order-of-magnitude analysis as `STRUCTURAL PROPOSAL`, and every identity as `COMPUTATIONALLY VERIFIED EXAMPLE` (noting which are classical standard facts).

---

## III. The Pell testbed (review summary)

(The full derivation is in [002-htwr-example.md](002-htwr-example.md); here we list only the anchor elements for comparison.)

- **Object**: $(1+\sqrt2)^n=P_n+Q_n\sqrt2$, $x_n=P_n/Q_n\in\mathbb P^1(\mathbb Q)$, $x_n\to\sqrt2$.
  - $P_n=1,3,7,17,41,99,239,577,\dots$ (the companion Pell / Pell–Lucas half-sequence, OEIS A001333)
  - $Q_n=1,2,5,12,29,70,169,408,\dots$ (**Pell numbers**, OEIS A000129)
- **Depth**: $I(x_n)=\ln P_n=n h_0-\ln2+o(1)$, $h_0=\ln(1+\sqrt2)\approx0.8814$.
- **Three structural elements**:
  1. **norm identity**: $P_k^2-2Q_k^2=(-1)^k$;
  2. **Newton doubling**: $x_{2n}=\frac{x_n^2+2}{2x_n}$ (a Newton step for the equation $x^2-2=0$);
  3. **Möbius big step (catalytic)**: $x_{n+k}=x_k+\dfrac{(-1)^{k+1}}{Q_k^2(x_n+x_k)}$ (the main variable $x_n$ occurs only once).
- **Conclusion**: Theorem 1 (uncertainty lower bound $\mathcal A\ge\frac{\alpha(I_*-\ln2)^2}{2(\sigma_{\max}+\ln2)}$, for any target and any DAG) and Theorem 2 (the two-phase Pareto frontier for Pell convergents).

**Status**: the norm identity and the doubling identity are classical standard facts (`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`); Theorems 1 and 2 are proved under Axioms I–IV (conditional conclusions within the `STRUCTURAL PROPOSAL` framework).

---

## IV. Fibonacci: Pell's isomorphic twin

### 4.1 Object and convergents

Take the Fibonacci numbers $F_0=0,F_1=1,\ F_{n+1}=F_n+F_{n-1}$, and the ratios

$$
y_n:=\frac{F_{n+1}}{F_n}\in\mathbb P^1(\mathbb Q),\qquad y_n\to\varphi=\frac{1+\sqrt5}{2}=[1;\overline1].
$$

$y_n$ is a convergent of the golden-ratio continued fraction $[1;\overline1]$: $1,\ 2,\ \frac32,\ \frac53,\ \frac85,\ \frac{13}{8},\ \frac{21}{13},\dots$, and it obeys the pure continued-fraction fixed-point recursion

$$
y_{n+1}=1+\frac1{y_n},
$$

**without any shift**, because $\varphi=1+\frac1\varphi$.

### 4.2 Element-by-element structural comparison with Pell

| structural element | Pell (silver ratio, $m=2$) | Fibonacci (golden ratio, $m=1$) |
| --- | --- | --- |
| limit / ratio | $\sqrt2$, $\lambda=1+\sqrt2$ | $\varphi=\frac{1+\sqrt5}{2}$ |
| unit-group construction | $(1+\sqrt2)^n=P_n+Q_n\sqrt2$ | $\varphi^n=\frac{L_n+F_n\sqrt5}{2}$ ($L_n$ the Lucas numbers) |
| convergent | $x_n=P_n/Q_n\to\sqrt2$ | $y_n=F_{n+1}/F_n\to\varphi$ |
| continued-fraction fixed point | $u_{n+1}=2+\frac1{u_n}$ | $y_{n+1}=1+\frac1{y_n}$ |
| norm / unit identity | $P_k^2-2Q_k^2=(-1)^k$ | **Cassini**: $F_{n+1}F_{n-1}-F_n^2=(-1)^n$ |
| defect catalyst | $c_k=2-x_k^2=\frac{(-1)^{k+1}}{Q_k^2}$ | $d_k=y_k^2-y_k-1=\frac{(-1)^k}{F_k^2}$ |
| Newton doubling | $x_{2n}=\frac{x_n^2+2}{2x_n}$ (for $x^2-2=0$) | $y_{2n}=\frac{y_n^2+1}{2y_n-1}$ (for $y^2-y-1=0$) |
| Möbius big step | $x_{n+k}=x_k+\frac{(-1)^{k+1}}{Q_k^2(x_n+x_k)}$ | $y_{n+k}=y_k+\frac{(-1)^{k+1}}{F_k(F_k y_n+F_{k-1})}$ |
| single-step depth increment | $h_0=\ln(1+\sqrt2)\approx0.8814$ | $h_0=\ln\varphi\approx0.4812$ |

### 4.3 Three identities (numerically verified)

The following identities are verified term-by-term for $n,k\le 10$ in this note:

1. **Cassini identity**: $F_{n+1}F_{n-1}-F_n^2=(-1)^n$ (all OK for $n=2,\dots,11$). Equivalently, the Lucas version $L_n^2-5F_n^2=4(-1)^n$ ($L_n=F_{n-1}+F_{n+1}$).
2. **Newton doubling**: $y_{2n}=\frac{y_n^2+1}{2y_n-1}$. This is a Newton step for $f(y)=y^2-y-1=0$ (the minimal polynomial of $\varphi$): $y-\frac{f(y)}{f'(y)}=\frac{y^2+1}{2y-1}$. It corresponds exactly to Pell's $x_{2n}=\frac{x^2+2}{2x}$ (for $x^2-2=0$).
3. **Möbius big step (catalytic)**: applying the Fibonacci matrix $M^k=\begin{pmatrix}F_{k+1}&F_k\\F_k&F_{k-1}\end{pmatrix}$ (with $\det M^k=(-1)^k$) to $y_n$ gives
$$
y_{n+k}=\frac{F_{k+1}y_n+F_k}{F_k y_n+F_{k-1}}=y_k+\frac{(-1)^{k+1}}{F_k(F_k y_n+F_{k-1})}.
$$
**Key**: $y_n$ occurs **only once** in this expression (Möbius form) — the Fibonacci version of Pell's "zero-fan-out main wire" catalytic wormhole.

**Status**: the three identities are classical standard facts (Cassini, Newton iteration, Fibonacci matrix powers); this note verifies finitely many terms — `COMPUTATIONALLY VERIFIED EXAMPLE`, promotable to `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`.

### 4.4 HTWR translation (structural observation)

**Depth calibration**: $\gcd(F_n,F_{n+1})=1$ and $F_{n+1}>F_n$, so $I(y_n)=\ln F_{n+1}=(n+1)\ln\varphi-\ln\sqrt5+o(1)$. The intrinsic depth of the target $y_N$ is $I_*=I(y_N)=N\ln\varphi+O(1)$.

Under this model, Pell's three conclusions translate **verbatim**, with only $h_0=\ln(1+\sqrt2)$ replaced by $h_0=\ln\varphi$:

1. **Zero-genus geodesic flow** ($g=0$): $y_{n+1}=1+\frac1{y_n}$ single-wire serial advance, $\mathcal A_{\mathrm{CF}}(y_N)=\Theta\bigl(\frac{I_*^2}{h_0}\bigr)=\Theta\bigl(\frac{I_*^2}{\ln\varphi}\bigr)$.
2. **Catalytic wormhole** ($g\ge1$): resident catalyst $(y_k,d_k)$, $d_k=y_k^2-y_k-1=(-1)^k/F_k^2$ (depth $2\ln F_k\approx2s$); each big-step round consumes $\Theta(\alpha I_*)$-level transverse flux, cumulatively $\mathcal A_{\mathrm{BSGS}}(\sigma_{\max})=\Theta\bigl(\frac{\alpha I_*^2}{\sigma_{\max}}\bigr)$.
3. **Pareto frontier**: the structure of the inverse-tradeoff phase ($0\le\sigma_{\max}<\frac12I_*$) and the Heron linear-saturation phase ($\sigma_{\max}\ge\frac12I_*$) is unchanged, only $h_0$ changes.

**Why the translation is strict**: Theorem 1 holds for **any** target state and DAG, independent of Pell; Theorem 2's proof uses only three ingredients — linear depth growth, a norm identity (providing the cancellation wormhole), and a Möbius big step (main variable occurring once) — and Fibonacci has all three.

**Status**: `STRUCTURAL PROPOSAL` (the full written translation of Theorem 2 is not yet carried out; Theorem 1 applies directly).

---

## V. The unified metallic-means family

The two are the first two members of one family. The metallic means

$$
\sigma_m=[m;\overline m]=\frac{m+\sqrt{m^2+4}}{2},\qquad \sigma_m=m+\frac1{\sigma_m},\qquad \sigma_m^2-m\sigma_m-1=0.
$$

- $m=1$: $\sigma_1=\varphi=[1;\overline1]$ (golden ratio) → Fibonacci;
- $m=2$: $\sigma_2=1+\sqrt2=[2;\overline2]$ (silver ratio) → Pell;
- $m=3$: $\sigma_3=(3+\sqrt{13})/2=[3;\overline3]$ (bronze ratio) → to be analysed.

Uniformly, $\sigma_m^n=\frac{A_n+B_n\sqrt{m^2+4}}{2}$ satisfies the Pell-type equation

$$
A_n^2-(m^2+4)\,B_n^2=4(-1)^n,
$$

and the convergent recursion is $u_{n+1}=m+\frac1{u_n}$, with single-step depth increment $h_0=\ln\sigma_m$.

- $m=1$: $A_n=L_n,\ B_n=F_n$, giving $L_n^2-5F_n^2=4(-1)^n$;
- $m=2$: $A_n=2P_n,\ B_n=Q_n$, giving $P_n^2-2Q_n^2=(-1)^n$.

**Status**: the metallic means and their Pell-type equations are classical standard number theory — `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`. The HTWR Pareto frontier for $m\ge3$ is not yet written: `OPEN PROBLEM` (structurally expected to be isomorphic, but the big-step Möbius decomposition and the cancellation-wormhole coefficients must be checked term by term).

**Magnitude note**: $\ln\varphi\approx0.4812$ is about $54.6\%$ of $\ln(1+\sqrt2)\approx0.8814$; to reach the same target depth $I_*$, Fibonacci needs about $1.83\times$ the number of steps, and the quadratic-barrier constant $\propto1/h_0$ is larger. $\varphi$ is the smallest metallic mean (all continued-fraction entries equal $1$), so Fibonacci is the "slowest" baseline member of this convergent family.

---

## VI. The Sylvester testbed (another spectrum)

(OEIS [A000058](https://oeis.org/A000058), Sylvester's constant [A076393](https://oeis.org/A076393).)

### 6.1 Definition and identities

$$
s(0)=2,\qquad s(n+1)=s(n)^2-s(n)+1=s(n)\bigl(s(n)-1\bigr)+1.
$$

First terms: $2,3,7,43,1807,3263443,10650056950807,113423713055421844361000443,\dots$ (digit counts $1,1,1,2,4,7,14,27,53$, doubling each step).

Three exact identities (verified term-by-term in this note):

1. **product = difference**: $s(n)-1=\prod_{k=0}^{n-1}s(k)$;
2. **Egyptian fraction**: $\sum_{k=0}^{n}\frac1{s(k)}=1-\frac1{s(n+1)-1}\to1$;
3. **pairwise coprime**: $\gcd(s(i),s(j))=1\ (i\neq j)$.

Growth: $s(n)=\lfloor E^{2^{n+1}}+\frac12\rfloor$, $E\approx1.2640847353053011$ ($\ln E\approx0.23434833$); $\ln s(n+1)/\ln s(n)\to2$.

### 6.2 HTWR analysis (structural observation)

The depth $L_n=I(s(n))=\ln s(n)$ satisfies $L_{n+1}=2L_n+O(1)$ (**doubles each step**). With one $\Delta$ fan-out + one $\times$ squaring + a linear correction, a single step costs $\approx4\alpha L_n$, cumulatively

$$
\mathcal A(s(N))\approx4\alpha\sum_{n=0}^{N-1}L_n=\Theta(\alpha L_N)=\Theta(\alpha I_*),
$$

i.e. **linear in the output depth** — no quadratic barrier. The peak transverse flux occurs at the last step: $\sigma_{\max}\approx L_{N-1}=\frac12I_*+O(1)$. Substituting into Theorem 1 gives the lower bound $\Omega(\alpha I_*)$, matching the upper bound up to a constant: Sylvester's naive circuit **automatically** saturates the uncertainty principle in the "fully condensed linear phase".

**The essential difference from Pell/Fibonacci**: Sylvester's terms are pairwise coprime, so there is **no norm identity and no cancellation wormhole** to exploit; the depth doubles by "repeated squaring" rather than by unit-group structure. Its role in the HTWR is to test whether the BSS free-lunch loophole of "repeated squaring fabricating exponential bit-width" is blocked by per-tube-diameter charging (Axioms I.3 + II.3) — internally consistent (the linear lower bound and linear reachability coincide).

Dynamical note: $f(s)=s^2-s+1$ has a parabolic fixed point at $s=1$ ($f(1)=1,\ f'(1)=1$); the orbit of $s(0)=2$ is the whole sequence; it is a genuine quadratic map, not part of the $\mathrm{PSL}(2,\mathbb Z)$ geodesic flow.

**Status**: the three identities `COMPUTATIONALLY VERIFIED EXAMPLE` (also classical standard facts); the HTWR order-of-magnitude analysis `STRUCTURAL PROPOSAL`. Open problem (`OPEN PROBLEM`): whether every term of the sequence is squarefree, and the distribution of primitive prime factors.

---

## VII. The Recamán sequence: counterexample reference

(OEIS [A005132](https://oeis.org/A005132).)

$$
a(0)=0,\qquad a(n)=\begin{cases}a(n{-}1)-n,& \text{if positive and not yet appeared},\\ a(n{-}1)+n,& \text{otherwise (whether or not it has appeared)}.\end{cases}
$$

First 40 terms: $0,1,3,6,2,7,13,20,12,21,11,22,10,23,9,24,8,25,43,62,42,63,41,18,42,17,43,16,44,15,45,14,46,79,113,78,114,77,39,78$.

**Verdict: it does not satisfy the definition of a "Pell sequence" (nor the metallic-means family).** Point by point:

| criterion | Pell / Fibonacci convergents | Recamán | match |
| --- | --- | --- | --- |
| element type | rationals converging to a quadratic irrational | non-negative integers, no limit | ✗ |
| recursion | second-order linear ($S_{n+1}=mS_n+S_{n-1}$) | first-order self-referential greedy (needs full-history membership query) | ✗ |
| monotone / convergent | alternately approaching $\sqrt2$ / $\varphi$ | violently non-monotone, divergent | ✗ |
| number-theoretic origin | Pell-type equation (unit group) | none | ✗ |
| growth | exponential | $\sim n\log n$ (empirical fit) | ✗ |
| injective | yes | no ($42,43,78$ etc. repeat) | ✗ |

**Status**: `COMPUTATIONALLY VERIFIED EXAMPLE` (first 40 terms match OEIS) + `STRUCTURAL PROPOSAL` (the negative judgement "carries no usable algebraic structure" is an observation, not a theorem). Recamán cannot inherit the constructions of Note II (no norm identity, no doubling, no Möbius big step); in the testbed spectrum it serves only as the "unstructured greedy sequence" counterexample reference.

---

## VIII. Four-sequence positioning table

| sequence | spectrum | depth growth | norm / unit identity | cancellation wormhole | HTWR quadratic barrier | testbed role |
| --- | --- | --- | --- | --- | --- | --- |
| **Pell** ($m=2$, silver) | metallic-means convergent | linear $n\ln(1+\sqrt2)$ | $P^2-2Q^2=(-1)^k$ | yes | yes, broken by wormhole | main testbed (Theorems 1/2) |
| **Fibonacci** ($m=1$, golden) | metallic-means convergent | linear $n\ln\varphi$ | $F_{n+1}F_{n-1}-F_n^2=(-1)^n$ | yes | yes, same structure as Pell | the "slowest" baseline of the family |

*(continued)*

| sequence | spectrum | depth growth | norm / unit identity | cancellation wormhole | HTWR quadratic barrier | testbed role |
| --- | --- | --- | --- | --- | --- | --- |
| **Sylvester** | double-exponential | $2^n$ doubling | none | none | none (linear) | "repeated-squaring" control |
| **Recamán** | none (greedy) | $\sim n\log n$ | none | none | n/a | no-structure counterexample |

---

## IX. Notation conflict

The symbols $P_n, Q_n$ are used in this note for the **companion Pell / Pell–Lucas** half-sequence (OEIS A001333) and the **Pell numbers** (A000129), i.e. the numerator and denominator of $x_n=P_n/Q_n$. Some literature instead reserves $P_n$ for the Pell numbers (A000129). This note follows the former convention. Register this conflict in the paper symbol table or the open-questions file.

---

## X. Status summary

| ID | claim | status | note |
| --- | --- | --- | --- |
| F1 | Cassini / Lucas identities | `COMPUTATIONALLY VERIFIED EXAMPLE` → `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | classical; verified in this note |
| F2 | Fibonacci Newton doubling $y_{2n}=(y_n^2+1)/(2y_n-1)$ | `COMPUTATIONALLY VERIFIED EXAMPLE` → `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | corresponds to Pell |
| F3 | Fibonacci Möbius big step (main variable once) | `COMPUTATIONALLY VERIFIED EXAMPLE` | classical matrix power |
| F4 | Fibonacci HTWR translation (Theorems 1/2) | `STRUCTURAL PROPOSAL` | verbatim translation, $h_0$ changed |
| M1 | metallic means $\sigma_m$, Pell-type equation $A_n^2-(m^2+4)B_n^2=4(-1)^n$ | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | classical number theory |
| M2 | $m\ge3$ HTWR Pareto frontier | `OPEN PROBLEM` | expected isomorphic, to be checked |
| S1 | Sylvester three identities (product=difference, Egyptian fraction, coprime) | `COMPUTATIONALLY VERIFIED EXAMPLE` → `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | classical; verified in this note |
| S2 | Sylvester HTWR linear reachability / no quadratic barrier | `STRUCTURAL PROPOSAL` | order-of-magnitude observation |
| R1 | Recamán does not satisfy the Pell definition | `COMPUTATIONALLY VERIFIED EXAMPLE` + `STRUCTURAL PROPOSAL` | negative observation |
| A0 | the HTWR Axioms I–IV framework | `STRUCTURAL PROPOSAL` | see Notes I and II remarks |

---

## XI. Subsequent research targets

1. **(open)** the HTWR Pareto curves of the $m\ge3$ metallic means (bronze ratio, etc.) — check whether the big-step Möbius decomposition and the cancellation-wormhole coefficients hold term by term.
2. **(open)** the HTWR analysis of $2^N-1$ (Mersenne) — it belongs to yet another spectrum ("linear recursion + repeated-squaring speedup"), to be positioned separately.
3. **(open)** write the first rigorous $(\mathcal A,\Sigma)$ Pareto curve for Sylvester (if its "no-cancellation-wormhole" structure collapses the curve to a point/line, state that formally).
4. **(editorial)** register the notation conflict of Section IX in the paper symbol table or the open-questions file.
5. **(editorial)** add the `STANDARD CONSEQUENCE` proofs of F1–F3 and S1 of this note into the main text, so the Fibonacci/Sylvester testbeds have citable identity foundations.
