# Quartic pencils with the fixed Chow polytope

## Classification

Let \(k\) be algebraically closed of characteristic zero. Write
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\) for \(u,v\ne0\), and let \(H\) act with
weights \((0,1,3,4)\). A proper quartic pencil is a two-dimensional space of
quartics with coprime generators. Its ideal is saturated. By
[Chow-polytope rigidity](../../results/chow_polytope_rigidity.md#statement),
matching \(4P_{C_0}\) means that its cycle is \(\sum n_i[C_{u_i,v_i}]\) with
\(\sum n_i=4\), where the listed curves are distinct.

- The \(H\)-invariant pencils are exactly the
  [line-and-quartic model](../equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts).
- All other pencils have cycle \(2[C_{u,v}]+2[C_{u,-v}]\). Normalize the
  pair of translates to \(C_{1,1},C_{1,-1}\) by a diagonal coordinate
  change, and put
  \[
  A=x_1^3-x_0^2x_2,\qquad B=x_2^3-x_1x_3^2,\qquad
  D=x_1^2x_2^2-x_0^2x_3^2.
  \]
  Then all the pencils in the fiber are
  \[
  F_\lambda=\lambda x_2 A+x_1 B,\qquad
  G_\lambda=D+\lambda x_1 A+\lambda^{-1}x_2 B,\qquad
  \lambda\in k^\times. \tag{1}
  \]

The first Chow moment \(\sum n_i u_i/v_i\) therefore vanishes for **every**
proper quartic pencil in this polytope fiber. The exceptional cycles are
outside the Chow closure of the invariant quartic realizations. The actual
pencils form a single \(H\)-orbit over each such cycle, with embedded
length two at opposite endpoints of the two flat limits.
On any retained member of (1), the translated mates in arbitrary
degrees are precisely the powers modulo that carrier described below.

## Contact at a smooth endpoint

The existing [quartic-pair exclusion](../../results/quartic_44_filtered_exclusion.md)
rules out a single translate in characteristic zero, after diagonal transport.
With at least two translates, their ratios \(u_i/v_i\) are pairwise distinct.
Two sharing a ratio would lie on one smooth quadric
\(x_1x_2=(u_i/v_i)x_0x_3\) in the same ruling class \((1,3)\).
Their sum cannot be part of a \((4,4)\) divisor on that surface. Thus both
quartics would contain the quadric. Also any plane factor of a pencil
member gives a curve of intersection on that plane, which contains none of
the nondegenerate quartics.

If the \(u_i\) vary, the evaluation of the pencil on all the translates
forces terms of weights below four to vanish. In weights zero, one and two
there is just one quartic monomial each, and in weight three the evaluation
has rows \((1,u_i)\). In weight four the evaluation has rows
\((1,u_i,v_i)\), so its kernel has dimension at most one. The pencil
misses the vertex \(x_1\ne0,\ x_0=x_2=x_3=0\). Some member \(F\) therefore
has weight-four part
\[
F_4=d x_1^4+b x_0^2x_1x_2+e x_0^3x_3,\qquad de\ne0.
\]
Here \(e\ne0\) because the \(u_i\) vary. Choose an independent \(G\) with
zero weight-four part.

At \(p_0=[1:0:0:0]\), write \((y,z,w)=(x_1,x_2,x_3)/x_0\). The surface
\(F=0\) is smooth there, and solving for \(w\) gives a formal series in
\(y,z\) of weight at least four whose weight-four part is
\(-(d y^4+b yz)/e\), for weights \(1,3\) on \(y,z\). Its translated
branches have equations \(z=u_i y^3\) in the regular ring \(k[[y,z]]\).
If two \(u_i\) coincided the graph of the same \(w(y,z)\) would force
their \(v_i\) to coincide. Thus the branch equations are distinct. Purity
and the generic multiplicities give
\[
G|_F=\text{unit}\cdot\prod_i(z-u_i y^3)^{n_i}.
\]
The factorization follows in the completed regular local ring, where each
smooth branch stays prime and the generic multiplicity is unchanged by
flat completion. Its weight is twelve. If the first occurring weight of
\(G\) were smaller, its homogeneous initial form would vanish on the
weight-four graph. It would be divisible by \(F_4\) after inverting
\(x_0\), hence also before inverting \(x_0\), since \(F_4\) is irreducible
and \(x_0\nmid F_4\). Equal ordinary degrees would make it a scalar
multiple of \(F_4\), excluded by the choice of \(G\). Therefore the pencil
has a member of weights at least twelve.

Reversal of coordinates replaces \((u_i,v_i)\) by
\((u_i',v_i')=(v_i^2/u_i^3,v_i^3/u_i^4)\) and exchanges the endpoints.
If both \(u_i\) and \(u_i'\) vary, the reversed argument supplies a member
of original weights at most four. The two weight bounds from containment
at the endpoints then give actual eigenforms of weights four and twelve.

If the \(u_i\) vary and all \(u_i'=c\), the member of weights at least
twelve must be a product of a plane equation with
\(B_c=x_2^3-c^{-1}x_1x_3^2\). Indeed the weight-twelve evaluation has rows
\((u_i^4,u_i v_i^2,v_i^3)\). Since \(v_i^2=c u_i^3\) and \(u_i/v_i\)
vary, its kernel is spanned by \(x_2 B_c\). The weight-thirteen kernel is
spanned by \(x_3 B_c\), and each higher weight has a single monomial.
This contradicts proper translated support by the plane-factor test.
Reversal treats the case with only \(u_i'\) varying. When both are
constant and the characteristic is different from two, there are
exactly two translates, normalized to \(C_{1,\pm1}\). In characteristic
two, squaring is injective, so distinct translates cannot occur in
this last case.

## Two translates with coinciding cubic jets

For \(C_{1,\pm1}\) the space of quartics vanishing on both curves is
\(A S_1+B S_1+kD\), with unique coefficients. Group the quartic monomials
by weight and parity of the \(x_3\)-exponent. In each group, containment
means that the coefficients sum to zero, since the two signs are distinct.
The groups with two monomials give one basis vector at each of weights
\(3,4,6,7,8,9,10,12,13\); all other groups have a single monomial.
These basis vectors are the four coordinate multiples of each cubic and
the weight-eight form \(D\). The line \(x_1=x_2=0\) meets the support
only at the endpoints. Since \(A,B\) vanish on the full line, the
\(D\) coefficient occurs in the pencil.
Write
\[
F=A L+B M,\qquad G=D+A N+B P,\qquad L,M,N,P\in S_1.
\]
On \(x_0=1\) the identity \(B=yD-z^2 A\) gives
\[
G=(1+yP)D+(N-z^2P)A,\qquad
(1+yP)F\equiv A K\pmod G,\qquad
K=L-z^2M+y(LP-MN). \tag{2}
\]
On either branch \((y,z,w)=(t,t^3,\epsilon t^4)\), \(\epsilon=\pm1\),
the factor \(1+yP\) is a generic unit, and \(A,G\) are transverse
parameters since \(A,D\) are. A repeated branch therefore satisfies
\(K(t,t^3,\epsilon t^4)=0\). There is at least one repeated branch.
The coefficients of \(t^0,t^{10}\) show that \(l_0=m_3=0\), where
subscripts on \(l,m,n,p\) denote coefficients of \(x_0,\ldots,x_3\)
in \(L,M,N,P\).

In fact \(n_0=0\). If \(n_0\ne0\), \(G\) is smooth at \(p_0\) and on its
formal graph \(z=y^3+\text{terms of weight at least eight}\), by (2).
The restriction of \(A\) to \(G\) cuts the two branches simply near
\(p_0\), since \((A,G)=(A,D)\) there. The restriction of \(K\) to \(G\)
has the two prime factors \(w-\epsilon y^4\) in the complete local
ring, with exponents \(n_\epsilon-1\). Hence its weight is eight in
\(y,w\) of weights \(1,4\).
Thus the terms of \(K(y,y^3,w)\) below weight eight vanish. Its coefficients
of \(w,y^6,y,y^2,y^3,y^4\), in that order, force
\(l_3,m_0,l_1,m_1,l_2,m_2=0\), using \(n_0\ne0\).
This gives \(F=0\). Reversal exchanges \(A,B\) and preserves the two
branches, so it also gives \(p_3=0\).

With these zero coefficients, expansion of \(K\) on the repeated branch
gives
\[
\begin{gathered}
l_1=m_2=0,\quad m_0n_1=0,\quad
l_2=m_1n_1,\quad m_1=l_2p_2,\quad l_3p_2=0,\\
\epsilon l_3-m_0n_2+l_2p_0=0,\qquad
-m_0-\epsilon m_1n_3+\epsilon l_3p_1=0,\\
-\epsilon m_0n_3-m_1n_2+l_2p_1+\epsilon l_3p_0=0. \tag{3}
\end{gathered}
\]
There is no triple branch. At fixed \(y=t\), the parameter \(A\) on \(G\)
has \(z_A=-1\) and
\[
w_A=-\epsilon t+\frac{N-t^6P}{2\epsilon t^4(1+tP)}
\]
along the branch. A triple branch would require \(K_z=w_A K_w\) there.
If \(m_1\ne0\), then \(l_2,n_1,p_2\ne0\), \(l_3=0\), and \(m_0=0\)
by (3), which also forces \(n_3=0\). Hence \(K_w=0\) and \(K_z\) has
constant coefficient \(l_2\ne0\). If \(m_1=0\), then \(l_2=0\).
The remaining equations give \(l_3,m_0,n_2\ne0\) and \(p_2=0\), since
otherwise \(F=0\). In this case \(K_w\) has constant coefficient \(l_3\)
and \(K_z\) is divisible by \(t\). The product \((N-t^6P)K_w\) starts
in degree one or three, because \(n_2\ne0\). Multiplying the derivative
condition by \(2\epsilon t^4(1+tP)\) gives a contradiction by order in \(t\).

Both branches must therefore be double. Taking (3) for both signs gives
\(l_3=m_0=n_3=p_0=0\), \(m_1\ne0\), \(n_1\ne0\),
\(p_1=n_2/n_1\), and \(p_2=1/n_1\). Rescale \(F\) to \(m_1=1\)
and replace \(G\) by \(G-(n_2/n_1)F\) to obtain (1).
Conversely the restrictions of (1) to \(x_0=x_3=0\) are
\(x_1x_2(\lambda x_1^2+x_2^2)\) and
\(\lambda x_1^4+x_1^2x_2^2+\lambda^{-1}x_2^4\), with no common zero.
Every projective surface meets that line, so the pair is proper.
Equation (2) gives \(K=-\lambda A\), proving length two at both
generic branches and exhausting the degree. The pencil contains no
eigenform, since the weights of its two basis elements lie in the
disjoint sets \(\{6,10\}\) and \(\{4,8,12\}\), with all coefficients
nonzero in these weight decompositions. It thus has non-invariant ideal.
The line of \(D\)-coefficient-zero members recovers \(\lambda\).

The multi-support classification works in every characteristic, with
only the invariant case in characteristic two. The single-support
exclusion invoked here uses characteristic zero.

## Chow closure and full opposite limits

The first moment vanishes on (1) by cancellation of the two opposite
ratios. On the invariant family, write \(v=\alpha+\beta u\) and the second
equation as \(u^4+\gamma u v^2+\eta v^3=0\). The root coordinate
\(\rho=u/v\) gives
\(\alpha\rho^4+(\gamma\rho+\eta)(1-\beta\rho)=0\).
The roots and their multiplicities correspond, since \(1-\beta\rho\)
is nonzero at each root. The missing cubic term gives the first moment
by Viète's formula, including in characteristic two. In that characteristic
the first moment also vanishes at a single support since its multiplicity
is four.

The exceptional cycles lie outside the Chow closure of invariant quartic
realizations. Specialize any proposed family along a trait and extend
the two generator lines by projectivity. The projective closure of the
single-translate orbit gives a proper labeling space via its four-fold
product. After finite base change the four labels specialize, and each
degree-four label in the target sum is one of the two prescribed quartics
by positivity and degree. Thus the labeled traits stay in the open
orbit, and polynomial incidence forces both limiting quartics to
contain both translates. For the normalized supports, the limiting
weight-four and weight-twelve lines are necessarily \(k x_1 A\) and
\(k x_2 B\). These forms are coprime, so their intersection is the flat
CI limit. Its cycle contains the line \(x_1=x_2=0\), a contradiction.

The \(H\) action on the exceptional fiber sends \(\lambda\) to
\(h^{-4}\lambda\) when acting on equations by weight substitution.
At \(\lambda=0\), the pencil itself tends to \(\langle x_1B,x_2B\rangle\).
Put \(D_0=x_0^2 D-x_1^2x_2 A\). The **saturated flat limit ideal** is
\[
J_0=(x_1 B,\ x_2 B,\ x_0^2 B,\ A^2,\ D_0). \tag{4}
\]
Indeed use \(G'=\lambda G_\lambda\) and the cancellation
\(x_2F_\lambda-x_1G'=-\lambda(x_0^2B+\lambda x_1^2 A)\).
Writing \(K_0=x_0^2B+\lambda x_1^2 A\), the next cancellations are
\(x_0^2F_\lambda-x_1 K_0=-\lambda A^2\) and
\(x_0^2G'-x_2 K_0=\lambda(D_0+\lambda x_0^2x_1 A)\).
All five generators of (4) therefore specialize from the parameter
saturation.

In lex order \(x_0>x_1>x_2>x_3\), the five leading monomials generate
\[
M=(x_0^4 x_2^2,\ x_3^2(x_0^4,x_0^2x_1,x_1^2,x_1x_2)).
\]
The Hilbert series of \(S/M\), separated by \(x_3\)-degrees below and at
least two, is
\[
(1+q)\frac{1-q^6}{(1-q)^3}
+\frac{q^2}{1-q}\left(\frac{1-q^4}{(1-q)^2}+q+q^2\right)
=\frac{(1-q^4)^2}{(1-q)^4}.
\]
This is the CI series. Each graded piece of the parameter-saturated
quotient at \(\lambda=0\) is free over the parameter DVR. The two
inclusions, from \(J_0\) into the special fiber ideal and from \(M\) into
\(\operatorname{in}_{\rm lex} J_0\), therefore give equality of Hilbert
functions, proving (4) and \(\operatorname{in}_{\rm lex} J_0=M\).
The monomial ideal \(M\) is saturated because a monomial outside \(M\)
with \(x_3\)-exponent at least two stays outside under \(x_3\)-multiplication,
and one with smaller exponent stays outside under \(x_1\)-multiplication.
Taking leading monomials gives saturation of \(J_0\).

The pure quotient is defined by \(J_0+(B)\). Its support misses
\(x_0=x_3=0\) by the equations \(A^2,x_2B\).
On \(x_0=1\) this is the proper local CI \((A^2,D_0)\), using
\(x_1 D_0+x_2 A^2=x_0^4 B\). On \(x_3=1\), reduction modulo
\(B\) sets \(x_1=x_2^3\) and gives \(D_0=-(x_2^8-x_0^2)^2\), with
\(A^2\) a multiple. Thus the quotient is pure across its support. The
submodule generated by \(B\) in \(S/J_0\) is supported projectively at
\(p_\infty\) and has length at most two there by its annihilators
\(x_0^2,x_1,x_2\). At \(p_\infty\) set \(x_3=1,x_2=0\). The resulting
ideal is \((x_0^2x_1,x_1^2,x_0^4)\), where \(B=-x_1\) and \(x_0 B\)
remain independent. The length is exactly two and the pure quotient
has Hilbert polynomial \(16n-34\). Reversal sends
\(\lambda\) to \(\lambda^{-1}\), giving the other full limit and embedded
length two at \(p_0\). The cycles agree throughout this family.
For a separate invariant of the original pairs, see the
[endpoint different](chow_endpoint_different.md#colength-and-finite-detection).

## All mate degrees on a retained exceptional carrier

In characteristic zero, fix any nonzero member \(T\) of an exceptional
pencil (1), and choose an independent member \(T'\) from that pencil.
The proper pairs \((T,Q_b)\) whose whole cycles are made of translates
are exactly
\[
b=4j,\qquad Q_b|_{V(T)}=c\,(T'|_{V(T)})^j,\qquad
j\ge1,\quad c\ne0.
\tag{5}
\]
Their cycles are \(2j[C_{1,1}]+2j[C_{1,-1}]\).
In degree four this recovers the original pencil from any one of its
nonzero members and the condition on the mate's cycle.

In fact the disjoint weight sets in (1) show that the only translates
lying on \(T\) are \(C_{1,\pm1}\). Either a nonzero \(F_\lambda\) part
or the \(G_\lambda\) part forces both \(A=B=0\) on any contained
translate. Also \(T\) is integral. A plane factor is impossible by
properness with \(T'\) and the translated support. A reducible quartic
without a plane factor would have a quadric factor. Such a factor
contains one of the translates from its positive-degree intersection
with \(T'\), and is therefore that translate's unique smooth quadric.
An effective sum of its translated curves, all of the same ruling
class \((1,3)\), cannot be the hypersurface section by \(T'\).

The surface \(V(T)\) is regular at the two generic points. Indeed along
either branch the linear parts of \(F_\lambda,G_\lambda\) in the normal
directions have ratio \(y^2/(1+\lambda^{-1}y^4)\), by (2) with
\(K=-\lambda A\). The denominator is a generic unit and the ratio
is nonconstant. Thus no scalar combination loses both linear parts.
The surface is also \(S_2\) because it is a hypersurface.

Write the cycle of \(Q_b\) on this surface as \(n_+[C_{1,1}]+
n_-[C_{1,-1}]\), allowing zero, so \(b=n_++n_-\). If \(n_+>n_-\),
the rational section \(Q_b^2/(T')^{n_-}\) of degree \(2(n_+-n_-)\)
is regular in codimension one. This follows from the orders on the
two regular branches and from \(T'\) being a unit off their support
in every other codimension-one local ring, in a local trivialization.
The \(S_2\) property extends the section. It lifts to an ambient form
by \(H^1(\mathbf P^3,\mathcal O(d-4))=0\) in its degree \(d\).
Its cycle on \(V(T)\) is supported on the plus translate alone,
contradicting the
[quartic-carrier exclusion](../../results/quartic_carrier_exclusion.md).
The opposite inequality is excluded by exchanging the signs.

If the common multiplicity is odd, \(2j+1\), divide \(Q_b\) by
\((T')^j\) and extend by the same argument. The resulting degree-two
section lifts to a quadric through both translates, impossible since
their unique quadrics are distinct. For common multiplicity \(2j\)
the ratio \(Q_b/(T')^j\) is an everywhere invertible regular function
by the same codimension-one argument applied to the ratio and its
inverse. It is constant by projectivity and integrality. Conversely
each restriction in (5) is nonzero and has the asserted cycle.
