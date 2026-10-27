# Actual sextics on the retained endpoint-four chart

Started 2026-10-25; completed 2026-10-26. Status: exact new linear realization, independently reproduced fixed-carrier jet certificate, and independently audited local scope bridge; no canonical promotion.

## Scope and accepted inputs

The curve is the fixed characteristic-zero quartic
\(C=[s^4:s^3t:st^3:t^4]\). The family construction starts in the conditional degree-\((6,16)\) lane with full generic ordinary initial CI \((2,12)\), saturated actual first relation, and movement two. [STCI-R-0014](../results/movement_two_six_rows.md) makes it a necessary numerical row under those hypotheses; it does not assert existence. The final fixed-carrier corollary is stated separately and does not require those initial-ideal or saturation hypotheses.

The [October 21 conductor/chart independent review](2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md), section 6, retains the endpoint-four root chart with

\[
\begin{aligned}
a(z)&=a_0+2b_2z+z^2,\\
b(z)&=b_1z+b_2z^2,\\
c(z)&=(b_1/2-a_0/4)z^2,\\
f&=a(z)u^2+b(z)uv+c(z)v^2,\qquad a_0\ne0.
\end{aligned}
\]

Its normalization is \(4f(-z/2,1)=z^4\). On the retained integral-nodal open its actual Picard modulus is

\[
\rho=2b_1/a_0-1,\qquad \rho^{12}=1,\quad\rho\ne1.
\]

The root and torsion reductions are reviewed, unpromoted evidence. They are not an emptiness result. The [saved sextic symbol computation](2026-10-20-conditional-2-12-symbol-map.md) supplies the actual source \(H^0(I_C^2(6))\), its rank-22 second-symbol image, and the one-dimensional kernel \(kq^3\). Those accepted computations are used as premises, not rerun here.

The exact balanced normal frame is

\[
(x_0,x_1,x_2,x_3)
=(1,z,z^3+v,z^4+u+\tfrac32zv).
\]

All coefficients below are global constants. No free \(k(C)\)-coefficients are introduced into the homogeneous source.

## Every prescribed second symbol has an actual sextic lift

Put

\[
q=x_0x_3-x_1x_2,\qquad D=x_2^3-x_1x_3^2.
\]

The multiplier forced by this endpoint chart is proportional to \(z^8\); fix its nonzero scalar by requiring the target second symbol to be \(z^8f\). The complete affine family of actual sextics with this target is

\[
\boxed{
F_6=(2b_1-a_0)q^2x_3^2+(b_1-a_0)qDx_2
       -b_2qDx_3+\tfrac14D^2+\kappa q^3.
}
\]

Here \(a_0,b_1,b_2,\kappa\) are parameters over \(\mathbf Q\); the nodal/torsion open is imposed afterward. The affine freedom in \(\kappa\) is precisely the accepted kernel. This is a complete description of the second-symbol lifting problem on the stated target, rather than a selection of examples.

To reconstruct the formula, solve four new right-hand sides in the saved image matrix. In the target order \(P_0,\ldots,P_{10},Q_0,\ldots,Q_{10},R_0,\ldots,R_{10}\), the nonzero entries are

\[
P_8=a_0,\quad P_9=2b_2,\quad P_{10}=1,
\quad Q_9=b_1,\quad Q_{10}=b_2,
\quad R_{10}=b_1/2-a_0/4.
\]

The resulting ambient source combinations are

| Parameter block | Actual sextic |
| --- | --- |
| \(a_0\) | \(-q^2x_3^2-qDx_2\) |
| \(b_1\) | \(2q^2x_3^2+qDx_2\) |
| \(b_2\) | \(-qDx_3\) |
| constant | \(D^2/4\) |
| \(\kappa\) | \(q^3\) |

A direct polynomial substitution independently checks the answer. In the balanced frame,

\[
q_1=u+zv/2,\qquad D_1=-2z^5u.
\]

Using these first symbols in the displayed sextic gives exactly \(z^8f\). The verifier additionally checks that the zeroth and first normal symbols vanish and that every ambient block has homogeneous degree six. It saves the full normal expansion, including all higher terms, for subsequent mate calculations.

This establishes actual sextic realizability of the prescribed **second symbol**. It does not establish compatibility with a prescribed higher formal root correction, membership in every earlier ambient-obstruction incidence, integrality of every member, or existence of \(G_{16}\).

## The normalization \(a_0=1\) uses the actual torus

Projective root scaling alone cannot set \(a_0=1\), because the coefficient of \(z^2\) has already been fixed. There is, however, a valid ambient normalization. The actual \(C\)-preserving torus is

\[
T_\lambda=\operatorname{diag}(1,\lambda,\lambda^3,\lambda^4).
\]

It gives \(q\mapsto\lambda^4q\), \(D\mapsto\lambda^9D\), and

\[
\lambda^{-18}F_6(T_\lambda x)
=F_6(\lambda^{-2}a_0,\lambda^{-2}b_1,
       \lambda^{-1}b_2,\lambda^{-6}\kappa).
\]

After the finite étale square-root cover \(\lambda^2=a_0\), one obtains \(a_0=1\) without changing the \(D^2/4\) coefficient or the endpoint normalization. The invariant modulus is \(\rho\). The remaining \(\mu_2\) changes the sign of the normalized \(b_2\) and fixes \(\kappa\). Equivalently, the squared normalized parameter is \(b_2^2/a_0\), and the normalized kernel parameter is \(\kappa/a_0^3\).

Thus subsequent exact computations may work over cyclotomic fields with
\(b_1=(\rho+1)/2\), but must record this cover. The universal formula above retains \(a_0\) free and needs no extension field.

## An additional geometric flag: a triple line on the carrier

Let \(L_0=V(x_2,x_3)\). Since \(q\in I_{L_0}\) and \(D\in I_{L_0}^2\), every sextic in the family vanishes to order at least three on \(L_0\). The generic order is exactly three when \(\kappa\ne0\), because the other four parameter blocks have order four. When \(\kappa=0\), the retained torsion chart has generic order exactly four: the quartic normal coefficient of \(x_1^2x_2^2x_3^2\) is

\[
3b_1-2a_0=a_0(3\rho-1)/2,
\]

which cannot vanish for a root of unity \(\rho\) with \(a_0\ne0\).

This is a singular line on the sextic carrier. It is not automatically a component of the intersection with a proposed mate. The line meets \(C\) only at \([1:0:0:0]\), with pullback ideal \((z^3,z^4)\). If a mate has sole support \(C\), its restriction to \(L_0\) must consequently be a nonzero scalar times \(x_1^{16}\); an identically zero restriction would make \(L_0\) a residual component. This provides a separate necessary global condition, not a completed family exclusion.

For another useful algebraic form, put \(L=(b_1-a_0)x_2-b_2x_3\). Then

\[
F_6=(D/2+qL)^2
 +q^2\bigl((2b_1-a_0)x_3^2-L^2+\kappa q\bigr).
\]

This identity may help future normalization or conductor calculations. No normality claim is inferred from it.

## One selected carrier: a completed necessary jet exclusion

The current investigation tests only

\[
\rho=-1,\quad a_0=1,\quad b_1=b_2=0,\quad\kappa=1,
\]

so

\[
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3.
\]

Any actual \(G_{16}\) in the scoped full generic initial-\((2,12)\) problem must satisfy

\[
G_{16}\in(F_*)+(u,v)^{12}
\quad\text{over }\mathbf Q(z)[[u,v]].
\]

This is only a necessary condition. Its coefficient space is nevertheless finite: all 969 coefficients of a homogeneous degree-sixteen form remain constants. The 286 forms \(F_*H_{10}\) satisfy it and cannot be proper mates.

The [fixed-carrier M2 certificate](../computations/endpoint4_fixed_m2_2026_10_25.m2) evaluates the actual normal substitution at \(z=1,\ldots,30\) modulo the prime 65521. At each point it uses

\[
\mathbf F_{65521}[u,v]/(F_*|_z,(u,v)^{12}),
\]

a 23-dimensional quotient. It stacks the resulting \(23\times969\) constant-coefficient matrices. The final \(690\times969\) matrix has rank 683. It also independently constructs the coefficient matrix of all 286 degree-ten multiples of \(F_*\), verifies their rank 286, and verifies that the stacked matrix annihilates them.

The modular rank gives a characteristic-zero lower bound, not merely a numerical heuristic. Every sample has \(z\ne0\) and \(1+z^2\ne0\) modulo the prime. The \(u^2\) leading coefficient of the carrier's quadratic normal part is \(z^8(1+z^2)\). Formal normal division through degree eleven can therefore be performed with denominators that are units at the chosen prime; a universal rational remainder matrix specializes to the tested finite-field matrix. Equivalently, in the 78-dimensional truncated polynomial module, multiplication by the nonzero order-two carrier on polynomials of degree at most nine has constant rank 55, leaving a free rank-23 quotient over the local coefficient DVR. The modular target thus has the required good reduction.

It follows that the characteristic-zero necessary jet kernel has dimension at most \(969-683=286\). The known multiples already have dimension 286, so

\[
\boxed{
\{G_{16}:G_{16}\in(F_*)+(u,v)^{12}\}
=F_*H^0(\mathbf P^3,\mathcal O(10)).
}
\]

The equality persists under characteristic-zero coefficient-field extension. This first excludes a proper degree-sixteen mate in the scoped full generic initial-\((2,12)\) problem. The following independently audited local argument gives a stronger fixed-carrier conclusion without that initial-ideal assumption.

## Every proper degree-sixteen pair on this carrier has residual degree at least eight

The [nonsplit-node scope audit](2026-10-26-endpoint4-nonsplit-node-scope-audit.md) independently reconstructs the needed local lemma. The generic quadratic normal term of \(F_*\) is

\[
z^8\bigl((1+z^2)u^2-z^2v^2/4\bigr).
\]

Its discriminant square class \(1+z^2\) remains nonsquare in \(k(z)\) after any characteristic-zero extension of the constant field: its geometric zeros are simple. Over \(k(z)(\sqrt{1+z^2})\), the completed curve has two transverse smooth branches exchanged by the quadratic Galois action. A function defined over \(k(z)\) has the same finite vanishing order \(n\) on each branch. The generic intersection length is therefore \(2n\), and division by the prepared quadratic gives

\[
G\in(F_*)+(u,v)^n.
\]

For clarity, the membership follows by writing the prepared remainder as \(a(v)u+b(v)\). Subtracting its restrictions to the two branches, whose difference has order one in \(v\), gives \(\operatorname{ord}a\ge n-1\); then \(\operatorname{ord}b\ge n\). This uses actual conjugate branches and finite intersection length, not just the two initial normal symbols.

If a proper homogeneous degree-sixteen pair \((F_*,G)\) containing \(C\) had \(n\ge12\), the completed jet-kernel certificate would force the global form \(G\) to be a multiple of \(F_*\), contradicting properness. Thus every such pair has

\[
\boxed{m_C=2n\le22,\qquad
\deg\bigl([V(F_*,G)]-m_C[C]\bigr)=96-8n\ge8.}
\]

This fixed-carrier conclusion does not require a prescribed full generic initial CI, a saturated first relation, or the movement-two hypothesis. Those assumptions explain where the carrier came from. The conclusion requires the actual displayed \(F_*\), mate degree sixteen, properness, and characteristic zero. It makes no assertion that the bound is attained. It does not exclude the endpoint-four chart for other \(b_2,\kappa,\rho\), the endpoint-three chart, the orbit-collision chart, other movement rows, or unrestricted STCI presentations.

## Reproduction and review record

Run

```text
python3 research/computations/endpoint4_actual_2026_10_25.py
/opt/homebrew/bin/M2 --script research/computations/endpoint4_actual_2026_10_25.m2
python3 research/computations/endpoint4_fixed_m2_2026_10_25.py
python3 research/computations/endpoint4_fixed_jet_independent_2026_10_26.py
```

The first script records the inherited matrix hash, solves only the new right-hand sides, and performs a direct ambient substitution. The generated [JSON](../computations/endpoint4_actual_2026_10_25.json) includes full ambient and normal expansions, parameter conventions, and the torus action. The generated M2 family file loads successfully.

Independent `endpoint4_formula_audit` reconstructed the second symbol, torus normalization, and exact singular-line orders without rerunning the inherited rank proof. It corrected the initial overly cautious normalization warning: the actual torus does supply the square-root gauge.

The fixed-carrier wrapper saves a [PASS metadata record](../computations/endpoint4_fixed_m2_2026_10_25.json) and [complete M2 output](../computations/endpoint4_fixed_m2_2026_10_25.txt), including source hashes, all sample ranks, the actual degree-six carrier vector, the 969 exponent-column order, and all 286 known-multiple checks. A preliminary M2 implementation failed those checks because an unparenthesized multiline assignment omitted the last two carrier terms. That failure was diagnosed and corrected before the final PASS. Ambient reconstruction and explicit annihilation checks now prevent that mistake from being hidden by the reported rank.

The [independent normal-division script](../computations/endpoint4_fixed_jet_independent_2026_10_26.py) uses recursive normal-degree division in a fixed 23-element basis, followed by separate modular elimination, rather than the M2 quotient Gröbner basis. Its [JSON record](../computations/endpoint4_fixed_jet_independent_2026_10_26.json) independently reports rank 683 and annihilation of all 286 actual multiples at every sample. The nonsplit-node implication is reviewed in the linked scope audit. No canonical result is changed here.

The independent replay uses Python's standard library and a C++17 compiler, selecting clang++ or g++ from the environment. Its temporary rank executable is built outside the repository and removed after the run. Macaulay2 provides the other implementation.
