# Picard lifting on multiple quadrics and a prescribed punctual defect

Date: 2026-10-31. Status: **independently reviewed provisional deduction**.
The [independent audit](2026-10-31-punctual-quadric-lifting-audit.md) records
the exact reviewed scope. These are applications of standard lifting and
coherent-extension methods, with no claim of literature novelty or of an
unrestricted STCI conclusion.

## 1. Precise statements

Let k be algebraically closed, Q=V(q) a smooth split quadric in P3, and
X_n=V(q^n) for a finite integer n≥2. Identify Q with P1×P1 and write
L=O_Q(a,b). Fix any closed point z of Q.

**Picard statement.** Restriction Pic(X_n)→Pic(Q)=Z² is injective.
In characteristic zero its image is exactly the diagonal. In
characteristic p>0 its image is

\[
\{(a,b):p^e\mid a-b\},\qquad
e=\min\{j\ge0:p^j\ge n\}. \tag{1}
\]

**Punctual extension statement.** In every characteristic and for every
L there is a coherent sheaf M_n on X_n, generically free of rank one,
maximal Cohen–Macaulay at every point, and invertible away from z, such that

\[
\bigl(M_n\otimes_{\mathcal O_{X_n}}\mathcal O_Q\bigr)^{**}
\simeq L. \tag{2}
\]

The double dual in (2) is over O_Q. If L is outside the Picard image,
the nonfree locus of M_n is exactly {z}. No bound on the scheme length,
local number of generators or complexity of that defect is asserted.
If L is in the Picard image, an invertible global extension can be used.

The statements are uniform in n and in the chosen point. In particular
z may be either marked endpoint of the fixed quartic C0. They impose no
global arithmetically Cohen–Macaulay condition on M_n and supply no
two-generator homogeneous presentation or defining equation column.

## 2. The first obstruction and its characteristic-independent normalization

The ideal of Q in X_2 is J=O_Q(-2,-2)=K_Q. The square-zero units sequence
gives

\[
H^1(Q,J)\to\operatorname{Pic}(X_2)\to\operatorname{Pic}(Q)
\xrightarrow{\delta}H^2(Q,J).
\]

This is [Stacks, Lemma 37.4.1](https://stacks.math.columbia.edu/tag/0C6Q).
Künneth gives H1(J)=0 and H2(J)=k. The first restriction is injective.

Here is a direct computation of the obstruction, valid also in
characteristic two. Write the Segre coordinates as

    x0=A0B0, x1=A0B1, x2=A1B0, x3=A1B1.

For the ruling bundle O_Q(1,0), lift the transitions A1/A0 using x2/x0
on the B0 strip and x3/x1 on the B1 strip. The discrepancy around the
product-cover square is

\[
\frac{x_0x_3}{x_1x_2}=1+\frac q{x_1x_2}. \tag{3}
\]

On x0≠0 put r=x2/x0, t=x1/x0 and use q/x0² as the local frame of J.
The coefficient in (3) is 1/(rt), representing the nonzero generator
γ of H2(O_Q(-2,-2)) in product Čech cohomology. Since O_Q(1,1)
extends from P3 and δ is a group homomorphism,

\[
\delta(O_Q(a,b))=(a-b)\gamma. \tag{4}
\]

In characteristic zero this immediately gives the diagonal image.
An invariant interpretation uses

\[
0\to K_Q\to\Omega_{\mathbf P^3}|_Q\to\Omega_Q\to0.
\]

The restricted Euler sequence gives H1(ΩP3|Q)=k and H2(ΩP3|Q)=0;
the image in H1(ΩQ)=k² is the diagonal hyperplane class. Its boundary
applied to c1(L) is (4), the line-bundle Atiyah/conormal obstruction.
[Arinkin–Căldăraru, Proposition 2.10](https://arxiv.org/pdf/1007.1671)
provides that obstruction interpretation. The explicit units calculation
(3) is the argument used here in arbitrary characteristic.

## 3. Every finite order and the characteristic-p lattice

The ideal for X_j⊂X_(j+1) is O_Q(-2j,-2j). Its H1 is zero, so every
successive Picard restriction is injective. In characteristic zero,
restriction through X2 and the ambient extensions of O_Q(a,a) finish
the statement for every n.

In characteristic p, put P=p^e. If n≤P, the coordinate power map

\[
[x_0:x_1:x_2:x_3]\longmapsto[x_0^P:x_1^P:x_2^P:x_3^P]
\]

maps X_n to Q, since the target quadric equation pulls back to q^P.
Pullback of a ruling bundle gives a lift of O_Q(P,0). Together with
ambient diagonal twists, this proves sufficiency in (1).

For necessity write d=a−b≠0 as d=P u, with P=p^v and p not dividing u.
Lift transition functions of O_Q(1,0) arbitrarily through order P+1.
Their cocycle discrepancies start with 1+q c modulo q², representing γ.
Raising these transitions to P-th powers gives a genuine cocycle modulo
q^P, whose obstruction at the next order is the Frobenius image

\[
F^{v*}\gamma\in H^2(Q,O_Q(-2P,-2P)).
\]

In the product Čech description it is represented by r^(-P)t^(-P).
This monomial is nonzero: the basis ranges for H2(O(-2P,-2P)) are
r^(-i)t^(-j), with 1≤i,j≤2P−1. Raising also to the u-th power
multiplies this obstruction by the nonzero scalar u in k.

The extension to X_P is unique by the injectivity already proved.
Consequently a different choice of lift cannot evade this next
obstruction. There is no lift to X_(P+1), hence none to any X_n with
n>P. This proves (1), including p=2. The case d=0 is supplied by
ambient hyperplane powers.

The geometric contrast is exact: Frobenius kills the transition
discrepancies through a finite order, while characteristic zero already
detects every nonzero ruling imbalance at the first thickening.
This does not transport an STCI construction between characteristics.

## 4. Removing one point, then extending coherently

Set U=Q\{z}. After a product automorphism, z=(∞,∞), and

\[
U=(\mathbf A^1\times\mathbf P^1)\cup
(\mathbf P^1\times\mathbf A^1),
\]

with intersection A2. Each product open has quasi-coherent cohomological
dimension at most one by its affine projection to P1; the intersection
is affine. Mayer–Vietoris gives H2(U,F)=0 for every quasi-coherent F.
Thus every successive units obstruction on U vanishes. Any L|U lifts
to an invertible sheaf L_n on X_n\{z}, for each finite n. The punctured
lifts can be chosen compatibly as n increases.

Choose a coherent extension N_n of L_n to X_n and set

\[
M_n=\mathcal Hom_{X_n}
\bigl(\mathcal Hom_{X_n}(N_n,\mathcal O_{X_n}),\mathcal O_{X_n}\bigr).
\]

A coherent extension exists by the finite-type extension results in
[Stacks, §28.23](https://stacks.math.columbia.edu/tag/01PD).
One may take a suitable finite-type subsheaf of the quasi-coherent
pushforward from the punctured open; the pushforward itself is not
asserted coherent.

To check depth at z, let R be its two-dimensional Cohen–Macaulay local
ring on the hypersurface X_n. A finite presentation of any finite
R-module N gives

    0 → N* → R^r → R^s.

The image in R^s has depth at least one when nonzero, since a regular
element of R is regular on every submodule of a free module. The
[depth lemma](https://stacks.math.columbia.edu/tag/00LX) gives depth(N*)≥2
when the dual is nonzero; the zero-image case is immediate. Applying
this to the second dual proves M_n is MCM at z. Off z it remains the
original line bundle. Generic rank one is preserved.

The reduction of M_n has rank one and equals L off z. On the smooth
surface Q its double dual is therefore a line bundle, and it is L:
restriction Pic(Q)→Pic(Q\{z}) is an isomorphism. Finite-support torsion
in the reduction disappears under this double dual. If M_n were also
free at z, it would be a global line bundle lifting L, proving the
asserted necessity of a nonfree point when L lies outside (1) or the
characteristic-zero diagonal.

This establishes (2). It does not assert that the coherent extensions
M_n can be chosen compatibly under reduction as n varies. No formal
or algebraized infinite-thickening module is constructed.

## 5. An explicit comparison with the sextic normal correction

For the fixed C=C0=[s4:s3t:st3:t4] of class (1,3) on Q, the
[sextic source calculation](2026-10-31-quadric-modification.md) produces
the class of 4s^11t^11 in a quotient of H0(O_C(22)) by the actual
normal-correction image. Project first to the larger correction quotient

\[
W=H^0(O_C(22))\big/
\big(s^{12}H^0(O_C(10))+t^{12}H^0(O_C(10))\big).
\]

There is an explicit comparison, not merely a numerical resemblance.
The exact Koszul sequence

\[
0\to O_C(-2)\xrightarrow{(t^{12},-s^{12})}
O_C(10)^2\xrightarrow{(s^{12},t^{12})}O_C(22)\to0
\]

identifies W with H1(O_C(-2))=H1(ω_C). On the two standard opens,
lift 4s^11t^11 using (4t^11/s,0) and (0,4s^11/t). Their difference
gives the Čech class ±4/(st).

Next use the adjunction sequence

\[
0\to K_Q\to K_Q(C)=O_Q(-1,1)\to\omega_C\to0.
\]

Its middle term is acyclic. The boundary H1(ω_C)→H2(K_Q) is therefore
an isomorphism, trace-dual to the restriction of constants from Q to C.
With compatible residue and Čech conventions, the composite carries
the displayed normal-correction class to ±4γ. For example, on the
quadric chart r=A1/A0, t=B1/B0, the curve is t³−r=0 and the residue
of dr∧dt/(t³−r) is −dt, with no factor three.

Consequently this explicit linear comparison identifies the nonzero
displayed class, up to its fixed sign convention, with the Picard
obstruction δ(O_Q(2,6))=−4γ. It does **not** identify the two deformation
problems or make a line-bundle lift equivalent to an actual defining
pair. It applies to the obstruction calculated for that specified
sextic source. No corresponding map for arbitrary pair corrections
has been asserted.

## 6. Effect on the STCI problem

The localization sequence makes the mechanism visible: removing z
allows the entire Picard obstruction to come from local cohomology
supported at z. The resulting object is a line bundle away from that
point and a rank-one MCM sheaf everywhere. The number of support points
is one, but the amount of local defect has not been measured or bounded.

The earlier [double-quadric matrix example](2026-10-31-simultaneous-equation-geometry.md)
has a global ACM two-generator presentation and two endpoint defects,
with diagonal reduced hull O_Q(1,1). The present construction supplies
every ruling class and any prescribed point, on every finite multiple
quadric, but does not give that stronger presentation. Neither result
substitutes for the other's hypotheses.

The comparison in §5 gives an intrinsic cohomological interpretation
of the preceding source obstruction. The punctual extension theorem
explains why bare nonlifting cannot be promoted directly to an
unrestricted obstruction once nonfree sheaves are allowed.

**Stopping decision:** bare Picard nonlifting, even together with a
nonfree locus confined to C0 or to one of its endpoints, cannot exclude
these MCM objects. A next STCI argument must constrain the actual
homogeneous presentation, its normal action and its distinguished
equation column, or bound the amount of defect those data can carry.
The construction does not provide those constraints and does not
construct an STCI. No module classification or thickness enumeration
is selected. The unrestricted characteristic-zero question remains open.
