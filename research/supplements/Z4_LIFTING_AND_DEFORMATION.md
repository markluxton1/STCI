# The prescribed characteristic-two quadruple: arithmetic nonlifting

Let \(R=\mathbf Z_{(2)}\) or \(\mathbf Z_2\), with fraction field \(K\), and fix \(C_R=[s^4:s^3t:st^3:t^4]\). The special embedded scheme is exactly
\[
Z_4=V(x_1^4-x_0^3x_3,\ x_2^4-x_0x_3^3)\subset\mathbf P^3_{\mathbf F_2}.
\]
The promoted [R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) states that no flat embedded family with this special fiber has generic reduced support \(C_K\). The proof has two essential parts: every hypothetical flat deformation supplies a canonical primitive triple; the exhaustive integral triple obstruction is nonzero. Neither part uses the characteristic-zero quartic-carrier theorem.

The exact special filtered algebra, the deformation reduction and the complete integral cocycle are given below. Their independent source reconstruction agreed with the separately assembled integer calculation; the consolidation changes exposition, not this theorem's hypotheses. The marked arithmetic theorem does not extend to arbitrary ramified DVRs or arbitrary characteristic-zero thickenings. The [intrinsic mechanism](Z4_INTRINSIC_ARITHMETIC_MECHANISM.md) separates reusable extension theory from those scope limits.

## The special filtered algebra

The saturated homogeneous ideal of C, over Q and over F2, is

    I_C = (q,f,h,g),
    q = x0*x3-x1*x2,
    f = x1^3-x0^2*x2,
    h = x1^2*x3-x0*x2^2,
    g = x2^3-x1*x3^2.

The generator h is missing from the proposed homogeneous presentation.
It is not in (q,f,g), but saturation of that ideal is I_C. Thus the three
stated equations give the correct ideal sheaf. The four identities
x0*h=x1^2*q+x2*f, x1*h=x3*f+x0*x2*q,
x2*h=-x0*g-x1*x3*q, and x3*h=-x1*g-x2^2*q exhibit the saturation issue.
Kernel elimination independently confirms the ideal in both characteristics.
The two charts x0!=0 and x3!=0 cover C and Z4: their complement would force
all four homogeneous coordinates to vanish.

On U write u=x1/x0, X=x3/x0-u^4, Y=x2/x0-u^3. On V write
c=x2/x3, A=x0/x3-c^4, B=x1/x3-c^3. In characteristic two the exact ideals are

    Z4|U: (X,Y^4),       Z4|V: (A,B^4).

On their overlap, with Y^4=0, the full transitions are

    c = u^-1+u^-4*Y,
    A = 0,
    B = u^-6*Y+u^-9*Y^2+u^-12*Y^3.

The inverse is u=c^-1+c^-4*B,
Y=c^-6*B+c^-9*B^2+c^-12*B^3. In particular the proposed cubic term is correct.
For J=I_C O_Z4, J=(Y) on U, J=(B) on V, J^4=0, and

    J^i/J^(i+1) = O_P1(-6i),  0<=i<=3.

The multiplication maps are the actual local products Y^i*Y^j=Y^(i+j),
respectively B^i*B^j=B^(i+j), truncated at power four. On the overlap
B^2=u^-12*Y^2 and B^3=u^-18*Y^3. The filtered algebra is glued by the full
nilpotent base-coordinate change c, as well as by B; its graded line bundles
alone do not determine it. The companion local-structure note gives the
complete coefficient substitution formula through cubic order using Hasse
derivatives. It even checks that the special ribbon has no retraction to C;
no global retraction is assumed anywhere in the lifting proof.

The saturated ideals of all four stages are computed from
((F,G)+I_C^n)^sat. Their Hilbert polynomials are respectively
4m+1, 8m-4, 12m-15, 16m-32. The full (F,G) is saturated, has radical I_C,
and contains I_C^4 but not I_C^3. These assertions are independently
checked by exact homogeneous computations.

Detailed evidence: [local and global structure](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-20-z4-local-structuremd).

## Deformation persistence and canonical intermediate stages

## Proposition 1: every flat embedded lift is a global (4,4) complete intersection

Let \(R=\mathbf Z_{(2)}\) or \(R=\mathbf Z_2\), let \(K=\operatorname{Frac}(R)\),
and let \(X=\mathbf P^3_R\). Suppose \(Z\hookrightarrow X\) is closed and
\(R\)-flat and its special fiber, as an embedded scheme, is exactly the complete
intersection \(Z_0=V(F_0,G_0)\), where \(F_0,G_0\) are the prescribed quartics.
Then there are homogeneous quartics \(F',G'\in R[x_0,x_1,x_2,x_3]_4\), reducing
respectively to \(F_0,G_0\), for which
\[
 Z=V(F',G').
\]
They form a regular sequence. In particular the generic fiber is automatically
a global complete intersection of two quartics. The pair \(F',G'\) is a basis
of \(H^0(X,\mathcal I_Z(4))\); all other bases differ by \(\mathrm{GL}_2(R)\).

### Proof

Write \(\mathcal I=\mathcal I_Z\). From
\(0\to\mathcal I\to\mathcal O_X\to\mathcal O_Z\to0\) and \(R\)-flatness,
\(\mathcal I\) is \(R\)-flat and its special-fiber restriction is
\(\mathcal I_0\), not merely an ideal mapping onto \(\mathcal I_0\). Hence
\[
0\longrightarrow\mathcal I(4)\xrightarrow{2}\mathcal I(4)
 \longrightarrow\mathcal I_0(4)\longrightarrow0.                 \tag{1}
\]
The special Koszul sequence, twisted by four, is
\[
0\longrightarrow\mathcal O_{\mathbf P^3_k}(-4)
 \longrightarrow\mathcal O_{\mathbf P^3_k}^{\oplus2}
 \longrightarrow\mathcal I_0(4)\longrightarrow0.
\]
The vanishing of intermediate line-bundle cohomology on \(\mathbf P^3\) gives
\[
H^0(\mathcal I_0(4))=kF_0\oplus kG_0,
\qquad H^1(\mathcal I_0(4))=0.                               \tag{2}
\]
The long exact sequence of (1) shows that multiplication by 2 on
\(H^1(X,\mathcal I(4))\) is surjective. This module is finite over \(R\) by
properness, so Nakayama gives \(H^1(X,\mathcal I(4))=0\). Therefore
\[
H^0(X,\mathcal I(4))/2H^0(X,\mathcal I(4))
 \simeq H^0(\mathcal I_0(4)).                                \tag{3}
\]
The left-hand module before reduction is finite and torsion-free over the DVR,
hence free; (3) shows that its rank is two. Choose lifts \(F',G'\) of the exact
ordered basis \(F_0,G_0\). They are a basis by Nakayama. The inclusion
\(H^0(\mathcal I(4))\subseteq H^0(\mathcal O_X(4))=R[x]_4\) identifies them
with quartic polynomials.

Consider evaluation \(\mathcal O_X(-4)^2\to\mathcal I\), with coherent
cokernel \(\mathcal Q\). Its reduction modulo 2 is surjective because
\(F_0,G_0\) generate \(\mathcal I_0\), so \(\mathcal Q/2\mathcal Q=0\).
Nakayama kills \(\mathcal Q\) at every point of the special fiber. If its
support were nonempty, its proper image in \(\operatorname{Spec}R\) would be
a nonempty closed subset containing the generic point and therefore also the
closed point. This contradicts the empty special-fiber support. Thus
\(\mathcal Q=0\), proving \(Z=V(F',G')\) globally. This properness argument
excludes components or generators that exist only in the generic fiber.

For completeness, regularity can be checked directly. The polynomial ring
\(S=R[x_0,x_1,x_2,x_3]\) is a UFD. A common irreducible homogeneous factor of
\(F',G'\) cannot be 2. Any other common factor and its complementary factors
can be chosen primitive over \(R\), so their nonzero reductions give a common
positive-degree factor of \(F_0,G_0\). This contradicts the special regular
sequence. Thus \(F',G'\) are coprime. Since \(S\) is a domain and a UFD,
\(F'\) is regular and multiplication by \(G'\) is injective modulo \(F'\).
They form a regular sequence. The resulting projective Koszul resolution is
\[
0\to\mathcal O_X(-8)\to\mathcal O_X(-4)^2
 \to\mathcal I_Z\to0.                                      \tag{4}
\]
In particular its generic fiber is Cohen--Macaulay of pure dimension one.
The global homogeneous ideal is the saturated ideal \((F',G')\): twist (4)
by any integer and use \(H^1(\mathbf P^3_R,\mathcal O(n))=0\).
\(\square\)

There is also a direct verification of flatness for arbitrary quartic lifts.
If \(2h=aF'+bG'\), the reduced regular-sequence syzygy implies
\(\bar a=-\bar tG_0\), \(\bar b=\bar tF_0\). Lift \(\bar t\), write
\(a=-tG'+2a_1\), \(b=tF'+2b_1\), and cancel 2 in \(S\) to obtain
\(h=a_1F'+b_1G'\). Thus 2 is a non-zero-divisor in \(S/(F',G')\), proving
flatness over the DVR. This assertion alone says nothing about its generic
support.

## Proposition 2: the fourth normal power is forced, not an extra restriction

Let \(C_R\) be the displayed relative rational quartic. In addition to
Proposition 1, suppose the reduced support of \(Z_K\) is exactly \(C_K\),
with generic multiplicity four. Then, as ideal sheaves on \(\mathbf P^3_R\),
\[
 \mathcal I_{C_R}^{\,4}\subseteq\mathcal I_Z
 \subseteq\mathcal I_{C_R}.                                 \tag{5}
\]
Consequently the full truncated normal neighborhood of order four contains
every admissible lift in the question. An analysis within that neighborhood
does not discard any lift, provided it still allows all ideals and all
embedding/gluing data inside it.

### Proof

The family \(C_R\) is flat: on its two standard parameter charts it is
\(\operatorname{Spec}R[u]\) and \(\operatorname{Spec}R[c]\), with
\(c=u^{-1}\). A section of \(\mathcal I_Z\) restricts to zero on \(C_K\).
Its restriction to \(\mathcal O_{C_R}\) is therefore killed locally by some
power of 2. Torsion-freeness of \(\mathcal O_{C_R}\) makes that restriction
zero. This proves the second inclusion.

By Proposition 1 the generic fiber is Cohen--Macaulay of pure dimension one.
Its unique reduced component is \(C_K\), so it has exactly one associated
prime, the generic prime of \(C_K\); in particular it has no associated
points supported at isolated closed points. The natural map from
\(\mathcal O_{Z_K}\) into its localization at that generic prime is
injective. The target is an Artin local algebra of length four. Its maximal
ideal has fourth power zero: before the chain of its powers becomes zero,
every inclusion is strict by Nakayama, and four nonzero strict quotients
already account for length four. Thus \(\mathcal I_{C_K}^{\,4}\) vanishes in
that localization and, by injectivity, in \(\mathcal O_{Z_K}\) everywhere.

Finally the image of \(\mathcal I_{C_R}^{\,4}\) in \(\mathcal O_Z\) becomes
zero after inverting 2. Each local image section is killed by a power of 2,
whereas \(\mathcal O_Z\) is \(R\)-flat and torsion-free. The image is zero,
which proves the first inclusion in (5). \(\square\)

The multiplicity-four hypothesis in this proposition is redundant once the
support hypothesis is imposed: the (4,4) complete intersection has degree
16, and its unique reduced curve has degree four. The degree formula forces
generic length \(16/4=4\). Keeping the hypothesis explicit makes the source
of the nilpotence bound transparent.

## Corollary 3: relative primitiveness and the first conormal quotient are forced

Suppose the hypotheses of Propositions 1 and 2 hold, and use the independently
checked special local structure \(\mathcal O_{Z_0}=\mathcal O_{C_k}[y]/(y^4)\)
on the two indicated affine charts. Let
\(J=\mathcal I_{C_R}/\mathcal I_Z\subseteq\mathcal O_Z\). Then
\(J^4=0\), and \(L=J/J^2\) is an invertible sheaf on \(C_R\).

Indeed, the conormal presentation is the cokernel of
\[
 \mathcal O_{C_R}(-4)^{\oplus2}
 \longrightarrow\mathcal I_{C_R}/\mathcal I_{C_R}^2,
                                                               \tag{6}
\]
where the right side has rank two and is \(N^*\). Its special-fiber matrix
has rank exactly one everywhere by the prescribed primitive local model.
The rank-zero locus of (6) is closed on the proper curve \(C_R\) and misses
the special fiber; hence it is empty. At the generic point of \(C_K\) its
rank cannot be two: two independent normal linear terms would make the
generic Artin algebra length one, contradicting length four. Thus its
determinant vanishes at the generic point of the integral \(C_R\), and
vanishes identically. Matrix (6) has constant rank exactly one. Locally an
invertible matrix entry reduces it to \(\operatorname{diag}(1,0)\); its
cokernel \(L\) is therefore a line bundle.

Because \(J\) is nilpotent, a local lift of a generator of \(J/J^2\)
generates \(J\): from \(J=(y)+J^2\), iteration gives \(J=(y)\). Thus the
primitive property itself is forced, and is not an assumption about the
generic thickening.

### The full relative local model and the flatness of every canonical stage

In fact there is a stronger local assertion, which is useful if one seeks an
obstruction already in the double or triple stage. At every point of \(C_R\)
there is a relative smooth surface \(W\subseteq X\), containing \(Z\) locally,
such that \(C_R\) is a Cartier divisor \(\ell=0\) on \(W\), and
\[
 \mathcal I_{Z/W}=(\ell^4).                                  \tag{7}
\]

Here is a proof that does not assume the flatness of the intermediate stages.
Choose a local conormal frame \((a,b)\) of \(\mathcal I_{C_R}\). The
constant-rank-one assertion for (6) says that some local combination
\(H=\lambda F'+\mu G'\) has a conormal coefficient that is a unit. Choose
the combination so that \((\lambda,\mu)\) is unimodular; one may simply
choose one of \(F',G'\) whose conormal coefficient is a unit at the point.
After possibly interchanging \(a,b\), write \(H=\alpha a+\beta b\) with
\(\alpha\) a unit. Then \((H,b)=(a,b)=\mathcal I_{C_R}\) locally. Moreover
\(H\) has a nonzero relative normal differential at that point. Since both
\(X/R\) and \(C_R/R\) are smooth, the conormal sequence shows that
\(W=V(H)\) is smooth over \(R\) near the point. The image \(\ell=b|_W\)
generates the ideal of \(C_R\) on \(W\) and is a non-zero-divisor there.
This also follows directly from the regular sequence \((H,b)\) in the
regular local ring of \(X\).

The quotient \(\mathcal O_W/(\ell^4)\) is \(R\)-flat. Indeed its four-step
filtration has quotients
\(\ell^i\mathcal O_W/\ell^{i+1}\mathcal O_W\), \(0\le i\le3\), which
are invertible \(\mathcal O_{C_R}\)-modules and hence \(R\)-flat. Thus both
\(\mathcal I_{Z/W}\) and \((\ell^4)\) are 2-saturated ideals in
\(\mathcal O_W\): their quotient modules have no 2-torsion.

On the generic fiber, the first ideal is principal, because \(H\) is part
of a local basis of the two generators of \(\mathcal I_Z\). Its quotient is
Cohen--Macaulay, its only reduced component is the Cartier curve \(\ell=0\),
and its generic multiplicity is four. It equals \((\ell^4)\) on \(W_K\).
For an explicit local verification, Proposition 2 gives
\((\ell^4)\subseteq\mathcal I_{Z_K/W_K}\); in a regular local ring of the
smooth surface \(W_K\), a principal ideal dividing \((\ell^4)\) and having
radical \((\ell)\) is generated by a unit times \(\ell^r\). The generic
length forces \(r=4\). There are no isolated residual or embedded points,
by complete intersection and the prescribed support.

Two 2-saturated ideals in the same ring that become equal after inverting 2
are equal: if \(h\) belongs to the first, then \(2^n h\) belongs to the
second for some \(n\), and saturation gives membership already before
multiplication. Apply the argument in both directions. This proves (7)
over \(R\).

Consequently multiplication induces canonical isomorphisms
\[
 L^{\otimes i}\xrightarrow{\sim}J^i/J^{i+1},\qquad 0\le i\le3,
 \qquad L=J/J^2,
\]
and the associated graded algebra is
\[
 \operatorname{gr}_J\mathcal O_Z
 \simeq\mathcal O_{C_R}\oplus L\oplus L^{\otimes2}\oplus L^{\otimes3},
\]
with its truncated symmetric-algebra multiplication. These assertions follow
from (7), where multiplication is literally multiplication of powers of
\(\ell\), so they concern the multiplication maps and not just abstract
isomorphism classes of graded pieces. All \(J^i\), all these graded pieces,
and all \(\mathcal O_Z/J^n\) are \(R\)-flat, by their filtrations by line
bundles. Reduction modulo 2 therefore commutes with all the indicated
quotients and powers. In particular
\[
 Z_n=\operatorname{Spec}_{Z}(\mathcal O_Z/J^n),\qquad 1\le n\le4,
\]
is a canonical flat embedded lift of the prescribed \(n\)-fold stage. An
obstruction to the canonical triple stage therefore rules out a full lift;
this implication does not assume a triple lift chosen independently of the
quadruple. The associated-graded statement does not assert that the filtered
algebra is globally split: the quadratic and cubic terms of its transition
functions remain essential data.

The special transition of \(J/J^2\) is
\(B=u^{-6}Y\); hence \(L_k\simeq\mathcal O_{\mathbf P^1_k}(-6)\).
Using \(\operatorname{Pic}(\mathbf P^1_R)\simeq\mathbf Z\), one gets
\(L\simeq\mathcal O_{\mathbf P^1_R}(-6)\). This observation does not by
itself construct the nonlinear multiplication or gluing through cubic order.

## Exhaustive integral triple obstruction

## Raw integral normal coordinates

Write `u=x1/x0`, `X=x3/x0-u^4`, `Y=x2/x0-u^3` and on the other chart
`c=x2/x3`, `A=x0/x3-c^4`, `B=x1/x3-c^3`.  Expansion of the exact rational
coordinate change gives

```
c = u^-1 + (u^-4 Y-u^-5 X) + (u^-9 X^2-u^-8 XY) + O((X,Y)^3),
A = 3u^-8 X-4u^-7 Y-9u^-12 X^2+16u^-11 XY-6u^-10 Y^2 + O(3),
B = 2u^-7 X-3u^-6 Y-5u^-11 X^2+9u^-10 XY-3u^-9 Y^2 + O(3).
```

The linear transition has determinant `-u^-14`.  At characteristic two it is
diagonal of degrees `-8,-6`; this integral frame avoids division by two in a
characteristic-zero balanced frame.

Trivialize the quotient line `L=O(-6)` by `epsilon` on U and `eta` on V,
with `eta=u^-6 epsilon` to first order.  Put `X=p(u)epsilon`,
`Y=q(u)epsilon`.  The opposite direction is

```
P(u^-1)=3u^-2 p-4u^-1 q,
Q(u^-1)=2u^-1 p-3q.
```

Requiring all four expressions to be regular on their charts gives exactly

```
p=a+b u+3h u^2,       q=d+2h u,
P=3a c^2+(3b-4d)c+h, Q=2a c+(2b-3d).
```

To see exhaustiveness, the equations on positive Laurent powers first imply
`2p_(j+1)-3q_j=0` and `3p_(j+2)-4q_(j+1)=0` for `j>0`.
Their coefficient determinant is a unit (`9-8=1`), eliminating all higher
terms.  The remaining relation `2p_2=3q_1` has exactly the parameterization
`p_2=3h,q_1=2h`, since three is a unit.  Thus all quotient variations are
included, before imposing the basepoint-free open condition.  The prescribed
special ribbon requires `a,b,h in 2R` and `d in R^times` with `d=1 mod 2`
after scalar trivialization.  The impossibility below holds on this entire
parameter space, so imposing basepoint-freeness adds no loophole.

## Exact triple cocycle and all quadratic corrections

Set `m_U=qX-pY`, `m_V=Q(c)A-P(c)B`.  Its linear transition is
`m_V=-u^-8 m_U`.  For a general local primitive triple write

```
X=p epsilon+r epsilon^2, Y=q epsilon+s epsilon^2,
eta=u^-6 epsilon+t epsilon^2, epsilon^3=0.
```

Here `r,s,t` are arbitrary local functions.  Equivalently the two local
equations for the line kernel are `m_U=gamma_U epsilon^2` and
`m_V=gamma_V eta^2`.  The exact ambient transition gives

```
m_V = -u^-8 m_U + Kfull epsilon^2,
u^8 Kfull = gamma_U(u)+u^-4 gamma_V(u^-1).
```

The quadratic remainder `m_V+u^-8 m_U`, denoted `Kfull epsilon^2`,
is independent of `r,s`; the quadratic parameter
change `t` disappears because it is multiplied by an additional epsilon.
The functions `gamma_U,gamma_V` range over the whole local correction
space.  Consequently the actual obstruction is the class of `K=u^8 Kfull`
in

```
R[u,u^-1] / (R[u]+u^-4 R[u^-1]) = H^1(P1_R,O(-4)),
```

with free basis `u^-1,u^-2,u^-3`.  It is the extension class for the kernel
line `M=O(-8)` against `L^2=O(-12)`; the sheaf is derived here from the
explicit embedded transition rather than postulated.

The complete Laurent expression is

```
K = 3a^3/u^5 + (9a^2b-12a^2d)/u^4
    + C3/u^3+C2/u^2+C1/u+3bh^2+3h^3u,
C1 = h(ah+3b^2-5bd+3d^2),
C2 = (b-d)(4ah+3b^2-8bd+6d^2),
C3 = a(ah+9b^2-23bd+15d^2).
```

For `a,b,h` even and `d` odd, `C2` is congruent to `2` modulo four: its
second factor is `2` modulo four and its first factor is odd.  Thus this
free cohomology class cannot vanish over `Z_(2)` or `Z_2`, over either of these specified bases. Ramified DVRs with a different
uniformizer are outside the stated parity argument.  Even the
necessary equations over `Z/4` are inconsistent.  This is one finite
integral identity, not a sequence of inconclusive lifts.

Changing the generator of `L` scales the cocycle by a unit and may change
its representative by the displayed coboundaries.  Every local quadratic
coordinate change is already covered by `r,s,t,gamma_U,gamma_V`.  Therefore
these freedoms cannot remove the obstruction.  Generator changes of the
full ideal have no effect on this intrinsic quotient and its extension.

## Global coefficient coverage and a lifting ribbon

The unrestricted global coefficient check uses **all 35 quartic monomials**.
A monomial x0^i0*x1^i1*x2^i2*x3^i3 restricts on C to u^(i1+3i2+4i3).
For a quartic H to contain C, the coefficient sums for each exponent
0,...,16 must vanish. These are 17 independent integral equations; choosing
one monomial per exponent supplies an integral 18-column difference basis
for every quartic in I_C(4). Since the original F,G already vanish on C_R,
all corrections F1,G1 of an admissible lift lie in this full module. No
monomial, coefficient, or generator mixing is restricted beyond necessity.
The combined value/first-normal map on all 35 columns has rank 34 over Q;
the first-normal image on I_C(4) has rank 17 with kernel Q*q^2.
These checks corroborate the coefficient space, but the proof of
nonexistence uses the stronger exhaustive quotient-and-gluing contradiction,
so it needs no remaining nonlinear quartic elimination.

The prescribed ribbon really does lift. On U use the ideal (X,Y^2); on V
use (A-(4/3)cB,B^2). These agree on the overlap: the exact square-zero
transitions are

    c=u^-1+u^-4*Y,  B=-3u^-6*Y,  A=-4u^-7*Y,
    u=c^-1-(1/3)c^-4*B,  Y=-(1/3)c^-6*B.

Both local rings are polynomial square-zero algebras over R, hence flat;
their embedded ideals glue, have support C_R, and specialize exactly to Z2.
Here 3 is a unit in both requested bases. This example has a=b=h=0,d=1,
for which C2=-6. Allowing every other permitted ribbon deformation still
gives C2=2 mod 4. Thus the first failure is the triple extension rather than
the ribbon, and the forced canonical-stage argument proves the full theorem.

## Divided powers as a local arithmetic precursor

## Integral equation on U

Put x0=1, x1=u, x3=u^4+X, x2=u^3+Y. Then exactly

F=-X,
G=4u^9Y+6u^6Y^2+4u^3Y^3+Y^4-3u^8X-3u^4X^2-X^3.

Thus the fourth-power defect contributes 6u^6Y^2 mod normal degree 3, and survives mod 4 as 2u^6Y^2. But the cubic power of x3 contributes -3u^4X^2 and the opposite chart has moving c; isolating 6 in this chart is not an intrinsic construction.

The independently audited quadratic ambient transitions are
c=u^-1+u^-4Y-u^-5X+u^-9X^2-u^-8XY+O(3),
A=3u^-8X-4u^-7Y-9u^-12X^2+16u^-11XY-6u^-10Y^2+O(3),
B=2u^-7X-3u^-6Y-5u^-11X^2+9u^-10XY-3u^-9Y^2+O(3).
The -6u^-10Y^2 term in A is a direct binomial-fourth-power contribution; the complete obstruction also uses the nonlinear change c and both normal equations.

## Full Cech reduction

For a=2alpha, b=2beta, h=2gamma, d=1+2delta, the audited expressions give

C1=h(ah+3b^2-5bd+3d^2) = 2gamma (mod 4),
C2=(b-d)(4ah+3b^2-8bd+6d^2) = 2 (mod 4),
C3=a(ah+9b^2-23bd+15d^2) = 2alpha (mod 4).

Hence [ob] = 2gamma[u^-1]+2[u^-2]+2alpha[u^-3] (mod 4) in H^1(P1_R,O(-4)), in the fixed audited trivializations. The proposed stronger equality [ob]=2[u^-2] (mod 4) is FALSE for general first quotients. The middle coordinate remains universally nonzero. For the distinguished quotient a=b=h=0,d=1, the exact class is -6[u^-2].

The controlling sheaf is Hom(M,L^2)=O(-4), M=O(-8), L=O(-6). Quadratic normal-coordinate and generator corrections contribute Cech coboundaries. A coordinate-dependent coefficient projection is not by itself an intrinsic morphism from divided-power defects.

## General p^r

For 0<j<p^r, v_p(binomial(p^r,j))=r-v_p(j), because binomial(p^r-1,j-1) is a p-adic unit (Lucas). Therefore the first j with valuation one is p^(r-1). Mod p,
D_(p^r)(a,b)=D_p(a^(p^(r-1)),b^(p^(r-1))),
where D_n=((a+b)^n-a^n-b^n)/p for n=p^r, and D_p is interpreted similarly. In particular D4 mod 2=a^2b^2.

A local valuation-one polynomial does not imply a nonzero global obstruction. A well-defined map to the obstruction sheaf, coordinate/generator invariance, and a nonzero resulting Cech class must be established separately. The numerical coincidence with -6 is evidence of a contribution, not proof of a canonical identification.

## Exact computational support and scope

The [raw obstruction verifier](../computations/verify_z4_quartic_obstruction_2026_10_20.py) reconstructs the rational coordinate changes, arbitrary quadratic corrections, all Laurent coefficients and the universal congruence modulo four. The independently assembled [integer Macaulay2 verifier](../computations/audit_z4_lift_2026_10_20.m2) supplies a distinct implementation where present; the proof uses the exhaustive quotient parameterization, the canonical-stage reduction, and the Laurent quotient rather than a rank total alone. The local-structure and integral fourth-power scripts retain exact chart/multiplication checks. Existing execution evidence was reused; no fresh execution is claimed by this consolidation.

The first failed stage is the triple, and the ribbon really does lift. Arithmetic variation of the quotient cannot cancel the middle class for any permitted first quotient over either stated base. A different characteristic-zero defining pair need not specialize to this exact embedded structure; indeed its complete-intersection Hilbert polynomial will in general prevent that specialization. The theorem supplies no universal nonexistence bridge.
