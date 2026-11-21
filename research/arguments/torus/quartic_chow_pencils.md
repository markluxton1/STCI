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

## Hilbert--Burch and first-normal interpretation

For the normalized exceptional support \(Y=C_+\cup C_-\)
over a field of characteristic different from two,
\(C_\pm=C_{1,\pm1}\), the saturated reduced ideal is
\[
 I_Y=(A,B,D),\qquad
 0\longrightarrow S(-5)^2
 \xrightarrow{\left(\begin{smallmatrix}
 x_2^2&x_3^2\\ x_0^2&x_1^2\\ x_1&x_2
 \end{smallmatrix}\right)}
 S(-3)^2\oplus S(-4)\longrightarrow I_Y\longrightarrow0.
\]
The signed maximal minors, in the order of the three summands,
are \((-A,-B,D)\), and the final surjection has these entries.
The minors have height two: \(A\) and \(B\) are distinct
irreducible cubic forms, hence coprime. Hilbert--Burch therefore
makes the displayed quotient Cohen--Macaulay and its homogeneous
ideal saturated. Its Hilbert series follows *from the resolution*:
\[
 H_{S/(A,B,D)}(q)
 =\frac{1-2q^3-q^4+2q^5}{(1-q)^4}.
\]
The numerator has a double zero at \(q=1\), with second
derivative \(16\); the corresponding Cohen--Macaulay curve has
degree eight. The ideal contains both distinct smooth quartics
\(C_+\) and \(C_-\), whose degrees already total eight.
The quotient is therefore generically reduced and has no
additional components. Cohen--Macaulayness implies Serre's
\(S_1\) condition, hence it is reduced, so this saturated
ideal is exactly \(I_Y\).

There is also a geometric check of the transverse normal
parameters used below and in the sextic argument:
the complete intersection \((A,B)\) has degree nine, contains
\(Y\) of degree eight, and contains the residual coordinate
line \(L=V(x_1,x_2)\) of degree one. Since \(A,B\)
are coprime, these three distinct components exhaust Bézout
degree, each with multiplicity one. Thus \(A,B\) form
a regular system of transverse parameters at the generic
points of \(C_+\) and \(C_-\). No Jacobian-rank table
is needed for this fact.

In degree four the resolution gives
\[
 H^0(I_Y(4))
 =A\,S_1\oplus B\,S_1\oplus kD,\qquad
 h^0(I_Y(4))=4+4+1=9.
\]
This replaces the weight-and-parity monomial enumeration in
the classification by the geometry of an arithmetically
Cohen--Macaulay union and its Hilbert--Burch presentation.

Inside \(\operatorname{Gr}(2,I_Y(4))=\operatorname{Gr}(2,9)\),
a pencil \(W\) has generic intersection multiplicity at least two
on each \(C_\epsilon\) precisely when its first-normal-symbol map
\[
 W\otimes\mathcal O_{C_\epsilon}\longrightarrow
 N^\vee_{C_\epsilon/\mathbf P^3}(4)
\]
has generic rank at most one, i.e. its determinant vanishes identically.
For a **proper** quartic pencil this condition on both components,
together with degree \(4\cdot4=2\cdot4+2\cdot4\), forces the
cycle \(2[C_+]+2[C_-]\). On the smooth locus of either component away from the two
intersection endpoints, this is the familiar local
**Ferrand doubling** condition: in two regular transverse
parameters a proper pencil with rank-one first normal class
has local ideal \((u,v^2)\), after changing generators and
coordinates. See Bănică--Forster,
[*Multiplicity Structures on Space Curves*, §1](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf).
That classical result describes the double structure locally;
it does not supply the compatibility across the two marked
endpoints or the global two-generator restriction.
This identifies the classical geometric degeneracy
locus. The [canonical-module rigidity proof below](#two-translates-with-coinciding-cubic-jets)
shows that **its proper-pair points are exactly (1)**,
using linkage and the residual coordinate line. The
even-eight divisor class below explains a doubled divisor
on a fixed carrier, but alone does not prove uniqueness.

## Self-linkage and the canonical conormal quotient

There is a further established geometric structure behind the
normal-rank condition. Let \(Y=C_+\cup C_-\) in characteristic
different from two. Its Hilbert--Burch resolution above gives
\[
 \deg Y=8,\qquad P_Y(n)=8n-6,\qquad p_a(Y)=7.
\]
Moreover **\(Y\) is locally a complete intersection**, even
at its two marked singularities. At \(p_0\), eliminate \(x_2\)
using \(A\) in the affine chart \(x_0=1\): the ideal becomes
\((x_2-x_1^3,\ x_3^2-x_1^8)\).
At \(p_\infty\), similarly eliminate \(x_1\) using \(B\)
on \(x_3=1\): the ideal becomes
\((x_1-x_2^3,\ x_0^2-x_2^8)\).
Thus the endpoints are two planar \(A_7\) singularities,
each consisting of two smooth branches with intersection
multiplicity four. The dualizing sheaf \(\omega_Y\)
is therefore invertible, and on either component
\[
 \omega_Y|_{C_\pm}
 =\omega_{C_\pm}(4p_0+4p_\infty)
 \simeq\mathcal O_{\mathbf P^1}(6).
\]

Now let \(Z=V(F,G)\) be a **proper** \((4,4)\) complete
intersection with cycle \(2[C_+]+2[C_-]\).
The ideal \(I_Z\) lies inside \(I_Y\), and at each generic
component point its local ring is a length-two quotient of
a two-dimensional regular local ring. The residual scheme
\(Y'=(I_Z:I_Y)\) is Cohen--Macaulay by the
Peskine--Szpiro complete-intersection linkage theorem
because \(Y\) is arithmetically Cohen--Macaulay.
At each generic point, a length-two local complete
intersection has residual length one, so
\(Y'\) has the same reduced support and generically
the same reduced structure as \(Y\).
It has degree \(16-8=8\), with no embedded components.
Hence \(Y'=Y\) scheme-theoretically:
\[
 \boxed{\ I_Z:I_Y=I_Y,\qquad I_Y^2\subset I_Z.\ }
\]
The standard linkage duality identifies the nilpotent
ideal of this self-linkage,
\[
 \boxed{\
 I_Y/I_Z\simeq\omega_Y(4-4-4)=\omega_Y(-4).\ } \tag{SL}
\]
Consequently every such pencil determines a **surjection**
\[
 I_Y/I_Y^2\twoheadrightarrow\omega_Y(-4).
\]
This is the canonical Ferrand self-doubling description,
rather than merely a pair of dependent normal jets
on the separate smooth components. It includes
the endpoint gluing encoded by \(\omega_Y\).

It also gives two **intrinsic finite-dimensional tests**
on the actual homogeneous equations. Since \(Y\)
is Gorenstein of degree eight and genus seven,
Riemann--Roch and Serre duality give
\[
 h^0(\omega_Y(-1))=2,\qquad
 h^0(\omega_Y)=7.
\]
Indeed \(\chi(\omega_Y(-1))=-2\) and
\(h^1(\omega_Y(-1))=h^0(\mathcal O_Y(1))=4\).
For the self-linkage quotient, taking sections in degrees
three and four yields
\[
 \begin{aligned}
 H^0(I_Y(3))&\xrightarrow{\ \sim\ }H^0(\omega_Y(-1)),
       && \dim=2,\\
 H^0(I_Y(4))&\twoheadrightarrow H^0(\omega_Y),
       && \dim(\ker)=2. \tag{SL2}
 \end{aligned}
\]
The first map is an isomorphism because a \((4,4)\)
CI has no cubic equation; the second is surjective
because its ideal has vanishing first cohomology,
and its kernel is precisely the actual quartic
pencil \(W\). Thus the classification can be phrased
as classifying the appropriate conormal quotient maps
for which these section conditions and properness hold.
The [geometric uniqueness argument below](#two-translates-with-coinciding-cubic-jets)
combines this duality with the explicit canonical-module
presentation furnished by Hilbert--Burch, the absence
of common quadrics, and restriction to the residual line.
The abstract section dimensions (SL2) **alone** would
not classify the quartic pencils or obstruct STCI.
See [Bănică--Forster, *Multiplicity Structures on Space Curves*,
§1](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf)
and [Franco--Kleiman--Lascu, *Gherardelli linkage and complete
intersections*](https://arxiv.org/abs/math/0003075).
For a numerical check, the line bundle
\(\omega_Y(-4)\) has degree
\(2p_a(Y)-2-4\deg Y=12-32=-20\), so
\(P_{\omega_Y(-4)}(n)=8n-26\).
Together with \(P_Y(n)=8n-6\) this recovers
the CI polynomial \(P_Z(n)=16n-32\).

**Scope.** A Ferrand doubling alone does not ensure
that its global homogeneous ideal has two quartic
generators. The classification below now supplies
the missing bridge **for this particular union**:
self-linkage makes the cubic generators map to a basis
of \(H^0(\omega_Y(-1))\); the canonical module relations
and the residual line then force exactly the displayed
proper pencils. This is a geometric uniqueness proof
using established liaison and Hilbert--Burch theory.
It does not classify arbitrary Ferrand doublings or
resolve unrestricted higher-degree STCI.

## Two translates with coinciding cubic jets

Let \(Y=C_+\cup C_-\), where \(C_\pm=C_{1,\pm1}\), in
characteristic zero. The [Hilbert--Burch resolution](#hilbert--burch-and-first-normal-interpretation)
gives
\[
 I_Y=(A,B,D),\quad I_Y(3)=kA\oplus kB,\quad
 I_Y(4)=AS_1\oplus BS_1\oplus kD. \tag{HB}
\]
There is **no common containing quadric** for the two
curves: their unique quadrics are
\(x_1x_2\mp x_0x_3=0\), so \(I_Y(2)=0\).
If a proper quartic pencil \(W\) has cycle supported on
both components, its multiplicities are positive and sum to
four by Bézout. The coordinate line
\(\Lambda=V(x_1,x_2)\) is not a component, while \(A,B\)
vanish identically on \(\Lambda\). Thus \(W\) cannot be
contained in \(AS_1+BS_1\). Choose a basis
\[
 F=AL+BM,\qquad G=D+AN+BP,\qquad
 L,M,N,P\in S_1. \tag{*}
\]

### Residual genus excludes the triple branches

Let \(Z=V(F,G)\) and \(Y'=(I_Z:I_Y)\) be the
complete-intersection residual to \(Y\). The reduced
union \(Y\) is an arithmetically Cohen--Macaulay
locally complete-intersection curve of degree eight and
genus seven, as established above by its Hilbert--Burch
resolution and planar endpoint equations.
Peskine--Szpiro linkage gives that \(Y'\) is locally
Cohen--Macaulay of degree \(16-8=8\). Moreover the
standard liaison exact sequence
\[
 0\longrightarrow\omega_Y(-4)
 \longrightarrow\mathcal O_Z
 \longrightarrow\mathcal O_{Y'}\longrightarrow0
\]
gives \(P_{Y'}(n)=8n-6\), and hence \(p_a(Y')=7\):
indeed \(P_Z(n)=16n-32\) and
\(P_{\omega_Y(-4)}(n)=8n-26\).

The residual has generic multiplicities
\((n_+-1,n_--1)\). If \(Z\) had \((3,1)\),
then \(Y'\) would be a locally Cohen--Macaulay
**double of the smooth rational quartic** \(C_+\).
The classical Ferrand description gives an
invertible conormal quotient. To see the needed hypotheses
directly, at the generic point of \(C_+\) a length-two
local Artin algebra has square-zero maximal ideal.
Thus \(I_{C_+}^2\subset I_{Y'}\) generically.
Since \(Y'\) has no embedded points, a subsheaf of
\(\mathcal O_{Y'}\) supported at finitely many points
must vanish, so the inclusion holds everywhere.
The nilpotent ideal \(I_{C_+}/I_{Y'}\) is torsion-free
of rank one on the smooth curve \(C_+\), hence is
a line bundle \(\mathcal L\), giving
\[
 N^\vee_{C_+/\mathbf P^3}\twoheadrightarrow
 \mathcal L=I_{C_+}/I_{Y'},\qquad
 0\to\mathcal L\to\mathcal O_{Y'}
   \to\mathcal O_{C_+}\to0.
\]
The genus \(p_a(Y')=7\) requires
\(\mathcal L=\mathcal O_{\mathbf P^1}(-8)\), since
\(p_a(Y')=-\deg\mathcal L-1\). But the
[established balanced normal bundle](../curve/fixed_quartic_geometry.md)
is \(N^\vee_{C_+/\mathbf P^3}=\mathcal O(-7)^{\oplus2}\).
It admits no map to \(\mathcal O(-8)\).
The reversed argument excludes \((1,3)\).
Thus the sole possibility is
\[
 \boxed{n_+=n_-=2.} \tag{M}
\]
This uses standard liaison and Ferrand double-structure
theory, not third-order derivative calculations.
See [Bănică--Forster, *Multiplicity Structures on Space
Curves*, §1](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf)
and [Eisenbud--Van de Ven, *On the normal bundles
of smooth rational space curves*](https://eisenbud.github.io/papers/pdfs/1981-001.pdf).

### Canonical-module rigidity of the pencil

In the \((2,2)\) case the residual \(Y'\) has
the same reduced generic cycle and degree as \(Y\);
being Cohen--Macaulay, it equals \(Y\)
scheme-theoretically. The
[self-linkage isomorphism](#self-linkage-and-the-canonical-conormal-quotient)
therefore supplies the quotient map
\[
 q:I_Y\twoheadrightarrow I_Y/I_Z
        \simeq\omega_Y(-4). \tag{SL}
\]
In degree three it induces an isomorphism
\[
 H^0(I_Y(3))\xrightarrow{\sim}
 H^0(\omega_Y(-1)), \tag{S3}
\]
since the \((4,4)\) CI has no cubic equation
and \(H^1(I_Z(3))=0\).

Use **the dual Hilbert--Burch presentation**.
The graded canonical module
\(\mathcal K=\operatorname{Ext}^2_S(S/I_Y,S(-4))\)
has two generators \(e_1,e_2\) of degree \(-1\),
with relations
\[
 x_2^2e_1+x_3^2e_2=0,\qquad
 x_0^2e_1+x_1^2e_2=0,\qquad
 x_1e_1+x_2e_2=0. \tag{CM}
\]
Their degree-\(-1\) parts form a basis of
\(H^0(\omega_Y(-1))\). As (S3) is an
isomorphism, for an invertible constant matrix
\(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\)
we may write
\[
 q(A)=ae_1+be_2,\qquad
 q(B)=ce_1+de_2,\qquad ad-bc\ne0. \tag{U}
\]
On the dense open \(x_1\ne0\), the last
relation in (CM) gives \(e_1=-x_2e_2/x_1\).
Put
\[
 \ell_1=bx_1-ax_2,\qquad
 \ell_2=dx_1-cx_2.
\]
Then \(q(A)=\ell_1e_2/x_1\) and
\(q(B)=\ell_2e_2/x_1\) on both generic branches.
From \(q(F)=0\), the quadric
\(\ell_1L+\ell_2M\) vanishes on \(Y\).
Since \(I_Y(2)=0\), it is identically zero.
The independent linear forms \(\ell_1,\ell_2\)
have only the Koszul linear syzygy; after
rescaling \(F\),
\[
 F=-\ell_2A+\ell_1B. \tag{F}
\]

Now use the Hilbert--Burch relation
\(x_1D=x_2^2A+x_0^2B\) and \(q(G)=0\).
They imply
\[
 (x_1N+x_2^2)q(A)
 +(x_1P+x_0^2)q(B)=0.
\]
The canonical module is generically rank one
on each reduced component. Therefore
\[
 E=\ell_1(x_1N+x_2^2)+
   \ell_2(x_1P+x_0^2)
\]
vanishes on \(Y\); it lies in
\(I_Y(3)=kA+kB\). Restrict to \(x_1=0\),
where \(A=-x_0^2x_2\) and \(B=x_2^3\):
this determines the two coefficients and yields
\(E=cA-aB\). Expanding only this identity,
and canceling the factor \(x_1\), gives
\[
 \ell_1N+\ell_2P
 =cx_1^2+ax_3^2-bx_2^2-dx_0^2. \tag{Q}
\]
The left side lies in \((x_1,x_2)\).
**Restricting to the residual line**
\(\Lambda=V(x_1,x_2)\) makes the right
side \(ax_3^2-dx_0^2\). Thus
\[
 \boxed{a=d=0,\qquad bc\ne0.} \tag{R}
\]
This is the decisive geometric restriction,
replacing the long coefficient and derivative test.

Now (F) gives \(F=cx_2A+bx_1B\), and (Q)
simplifies to
\[
 bx_1N-cx_2P=cx_1^2-bx_2^2.
\]
The Koszul syzygy of \((x_1,x_2)\)
shows that, for some \(\tau\in k\),
\[
 N=(c/b)x_1+\tau c x_2,\qquad
 P=(b/c)x_2+\tau b x_1.
\]
Replacing \(G\) by \(G-\tau F\) and scaling
\(F\) by \(b^{-1}\) gives the unique form
\[
 \boxed{\;
 W=\left\langle
 \lambda x_2A+x_1B,\
 D+\lambda x_1A+\lambda^{-1}x_2B
 \right\rangle,\qquad\lambda=c/b\in k^\times .
 \;}
\]
This is precisely the family (1). Thus **all** proper quartic pencils with this
two-component support are the displayed orbit.
This is a proof by canonical modules, linkage,
the absence of common quadrics and restriction
to a line—not a computational elimination.

### Properness and generic cycle

Conversely, on the line \(V(x_0,x_3)\)
the two displayed quartics restrict to
\[
 x_1x_2(\lambda x_1^2+x_2^2),\qquad
 \lambda x_1^4+x_1^2x_2^2+\lambda^{-1}x_2^4.
\]
They have no common projective zero, so the
two surfaces have no common factor.

On either \(C_\epsilon\), the Hilbert--Burch
relation \(x_1D=x_2^2A+x_0^2B\)
expresses the first normal class of \(D\)
in the transverse frame \((A,B)\).
The two normal rows of the displayed pencil are
\[
 (\lambda x_2,x_1),\qquad
 (\lambda x_1+x_2^2/x_1,\
  \lambda^{-1}x_2+x_0^2/x_1).
\]
Their determinant is
\(\lambda(x_0^2x_2/x_1-x_1^2)=0\)
on each component since \(A=0\). Therefore
both generic intersection multiplicities
are at least two, and degree sixteen
forces exactly \(2[C_+]+2[C_-]\) with
no additional projective components.
The two generators have disjoint intrinsic
weight sets \(\{6,10\}\) and
\(\{4,8,12\}\), so there is no eigenform
in the pencil. The member with zero
\(D\)-coefficient recovers \(\lambda\).

This completes the **characteristic-zero**
classification of the exceptional support.
The characteristic-two **single-support construction**
below is a separate statement proved by direct identities.
The present linkage/normal-bundle argument does **not**
establish a full quartic-pencil classification in
positive characteristic, including odd primes.

## Two-sided contact and the nodal even-eight carrier

Two distinct translates have the same cubic graph coefficient at
\(p_0\) exactly when their \(u\)-parameters agree. Reversal sends
\(u\) to \(u'=v^2/u^3\), so matching cubic coefficients at **both**
endpoints gives \(u_1=u_2\) and \(v_1^2=v_2^2\).
In characteristic different from two, distinctness is equivalent
to \(v_2=-v_1\). Thus the exceptional support is exactly the
two-support configuration with coincident endpoint cubic jets in
both directions. The [endpoint different](chow_endpoint_different.md)
measures the resulting normalization-colength jump from \(3\)
to \(4\), and different-saturation length from \(12\) to \(14\).

The carrier \(T=V(G_1)\) in characteristic zero has a classical
K3-surface description. Put
\[
 P=x_1x_2+x_0^2,\qquad Q=x_1x_2+x_3^2,\qquad
 R=x_1^2+x_2^2.
\]
Direct expansion gives \(G_1=R^2-PQ\). Its singular locus consists
of the eight reduced solutions of \(P=Q=R=0\) and the two
marked endpoints \(p_0,p_\infty\). At each of the first eight
the three quadrics are local parameters and the equation is
\(R^2-PQ\); at the endpoints the tangent quadratic is,
up to sign, \(x_1x_2+x_3^2\) or \(x_1x_2+x_0^2\) in the
corresponding affine chart. All ten singularities are ordinary
nodes, and the minimal resolution \(\pi:X\to T\) is a K3 surface.

Let \(h=\pi^*H\), let \(\Gamma_\pm\) denote the strict transforms of
\(C_\pm\), write \(E_0,E_\infty\) for the endpoint exceptional curves
and \(E_1,\dots,E_8\) for the others. Since
\(F_1|_T=2C_++2C_-\), its Cartier pullback is \(4h\).
The order of \(F_1\) at each of the eight interior nodes is one:
indeed
\(F_1=2x_1x_2R-x_2^2P-x_1^2Q\) and \(x_1x_2\ne0\) there.
At \(p_0,p_\infty\) its quadratic initial form is respectively
\(-x_2^2\) and \(-x_1^2\); the order on each exceptional curve
is two. The total-transform equality gives
\[
 4h\sim 2\Gamma_++2\Gamma_-+2E_0+2E_\infty
                 +\sum_{i=1}^8 E_i,
 \qquad
 \boxed{\ \sum_{i=1}^8E_i\sim
 2(2h-\Gamma_+-\Gamma_--E_0-E_\infty).\ } \tag{E8}
\]
Thus the *interior eight* are an even eight on the resolved K3;
the endpoint exceptional curves contribute integral corrections.
The image of the half-eight under
\(\operatorname{Pic}(X)\to\operatorname{Cl}(T)\) is
\(2H-C_+-C_-\). Equivalently,
\[
 2(C_++C_--2H)=0\quad\text{in }\operatorname{Cl}(T).
\]
This is nonzero two-torsion: if \(C_++C_-\sim2H\),
a section of \(\mathcal O_T(2)\) would cut out both curves;
it lifts to an ambient quadric, contrary to their distinct unique
containing quadrics. This is precisely the even-eight class, not
an additional unrelated torsion phenomenon.
The direct identity (E8) is the proof; for the established framework
see [Barth, *Even Sets of Eight Rational Curves on a K3-surface*](https://doi.org/10.1007/978-3-642-56202-0_1)
and [Casnati--Catanese, *Even sets of nodes are bundle symmetric*](https://arxiv.org/abs/alg-geom/9602024).
The symmetric determinant here has **quadratic** entries, and
is not thereby a linear quartic symmetroid.

This explains doubled divisors on an exceptional
**fixed carrier**; by itself it does not classify the
moving \(\lambda\)-orbit. The orbit's uniqueness is now
proved separately by [liaison and canonical-module rigidity](#two-translates-with-coinciding-cubic-jets).
The two geometric mechanisms are complementary.

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

The identification of the entire special ideal and its Hilbert
function can be proved by **Hilbert--Burch and an exact sequence**,
without a Gröbner order or monomial count. Put
\[
 I'=(B,A^2,D_0),\qquad T=(x_1,x_2,x_0^2),\qquad
 H_5=2x_0^2x_1^2x_2-x_1^5.
\]
The two relations
\[
 x_0^4B-x_2A^2-x_1D_0=0,\qquad
 H_5B-x_3^2A^2-x_2^2D_0=0
\]
are the columns of the Hilbert--Burch matrix
\[
 \Phi=
 \begin{pmatrix}
 x_0^4&H_5\\
 -x_2&-x_3^2\\
 -x_1&-x_2^2
 \end{pmatrix}. \tag{FL1}
\]
Its signed maximal minors are precisely \(B,A^2,D_0\).
Since \(A\) and \(B\) are coprime, \(I'\) has height two.
Hilbert--Burch gives
\[
 0\longrightarrow S(-7)\oplus S(-8)
 \xrightarrow{\Phi}S(-3)\oplus S(-6)^2
 \longrightarrow I'\longrightarrow0. \tag{FL2}
\]
In particular, \(S/I'\) is arithmetically Cohen--Macaulay,
and its Hilbert series is
\[
 H_{S/I'}(q)=
 \frac{1-q^3-2q^6+q^7+q^8}{(1-q)^4}. \tag{FL3}
\]
Geometrically, this is the **pure doubled divisor** supported on
\(C_+\cup C_-\) inside the cubic carrier \(B=0\):
away from the endpoints, the relation
\(x_1D_0+x_2A^2=x_0^4B\) makes \(I'=(B,A^2)\);
the two curves are regular and \((A,B)\) give transverse parameters.
Their multiplicities are two, accounting for all sixteen degrees
of the Cohen--Macaulay determinantal curve. The Hilbert polynomial
of this pure quotient is \(16n-34\).

The five-generator ideal (4) is \(J_0=(A^2,D_0)+BT\).
The Hilbert--Burch relations in (FL2) identify
\[
 (A^2,D_0):B=(x_0^4,H_5)\subset T,\qquad
 J_0:B=T.
\]
Consequently multiplication by \(B\) gives a short exact
sequence of graded modules
\[
 0\longrightarrow (S/T)(-3)
 \xrightarrow{\ \cdot B\ } S/J_0
 \longrightarrow S/I'\longrightarrow0. \tag{FL4}
\]
Here \(S/T\simeq k[x_0,x_3]/(x_0^2)\) is the structure
module of a length-two scheme at \(p_\infty\).
Thus (FL4) geometrically exhibits the embedded
endpoint correction and gives
\[
 \begin{aligned}
 H_{S/J_0}(q)
 &=\frac{1-q^3-2q^6+q^7+q^8}{(1-q)^4}
   +\frac{q^3(1+q)}{1-q}\\
 &=\frac{(1-q^4)^2}{(1-q)^4},
 \end{aligned} \tag{FL5}
\]
the Hilbert series of a \((4,4)\) complete intersection.
The first and last terms of (FL4) are Cohen--Macaulay of
dimensions one and two, respectively. The depth lemma
gives \(\operatorname{depth}(S/J_0)\ge1\); hence \(J_0\)
is already saturated.

The generators in (4) come from the parameter-saturated
family, so \(J_0\) is contained in its special ideal.
The generic fiber is a proper \((4,4)\) complete intersection,
and each degree of the parameter-saturated family is a
torsion-free finite module over the parameter DVR, hence free.
Its special fiber therefore has the same Hilbert function as
the generic fiber. Equation (FL5) forces equality of the
special ideal with \(J_0\). This proves the **full scheme**
limit, not only its cycle or pure hull.

Reversal sends
\(\lambda\) to \(\lambda^{-1}\), giving the other full limit and embedded
length two at \(p_0\). The cycles agree throughout this family.
For a separate invariant of the original pairs, see the
[endpoint different](chow_endpoint_different.md#colength-and-finite-detection).

## Hilbert over Chow, and the characteristic-two collision

For a fixed exceptional cycle, the ideals \((F_\lambda,G_\lambda)\)
give a nonconstant \(H\simeq\mathbf G_m\)-orbit in the Hilbert
fiber over a **single Chow point**. The two saturated opposite limits
are fixed Hilbert points above that same cycle. The original pairs
are proper complete intersections; their limiting ideals have extra
generators and embedded endpoint length two, despite having the
unchanged fundamental cycle. Thus the Chow polytope (indeed the
entire Chow point) cannot recover the vertical Hilbert orbit.
The appropriate classical comparison is the Hilbert-state-polytope
and Gröbner-degeneration theory of
[Bayer--Morrison, *Standard bases and geometric invariant theory I*](https://doi.org/10.1016/S0747-7171(88)80043-9).
No explicit projected state polytope or general conservation law
equating different jumps to embedded length is asserted.

There is also a **single-support** phenomenon in characteristic two,
which must not be confused with the multi-support classification.
Specialize (1) at \(\lambda=1\) and reduce modulo two:
\(F=x_2A+x_1B,\ G=D+x_1A+x_2B\).
Direct expansion gives
\[
 A^2=(x_0^2+x_1x_2)F+x_1^2G,\qquad
 B^2=(x_1x_2+x_3^2)F+x_2^2G
 \quad(\operatorname{char}k=2).
\]
The reduced support of \(V(A,B)\) is \(C_0\) together with
\(L=V(x_1,x_2)\). On \(L\), \(G=x_0^2x_3^2\),
so the only points of \(L\) retained by the pair are
\(p_0,p_\infty\in C_0\). Thus \(\sqrt{(F,G)}=I_{C_0}\).
The pair is proper since a common surface factor of \(F,G\)
would divide both \(A^2,B^2\), whereas \(A,B\) are coprime.
Its ideal is non-invariant, as the distinct intrinsic weights of
both generators show. This is a characteristic-two
\((4,4)\) STCI presentation with a \((2,2)\) generic-characteristic
support splitting; it is different from the familiar four-distinct-
translate binomial splitting \((1,1,1,1)\).
This explicit characteristic-two construction makes
**no claim** to classify all multi-support quartic pencils
in that characteristic. The full uniqueness theorem
above is stated and proved in characteristic zero.

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

The surface \(V(T)\) is regular at the two generic points.
The first-normal rows computed above are proportional on
each component, with quotient
\[
 \frac{\operatorname{in}_1(G_\lambda)}
      {\operatorname{in}_1(F_\lambda)}
 =\frac{\lambda^{-1}x_2+x_0^2/x_1}{x_1}
 =t^{-2}+\lambda^{-1}t^2
 \quad\text{on }C_\pm\cap\{x_0=1\}.
\]
This rational function is nonconstant in characteristic zero.
Hence no nonzero constant linear combination of
\(F_\lambda,G_\lambda\) can lose its first normal symbol
identically along either component. Every retained carrier
is therefore regular at both generic points.
It is also \(S_2\), being a hypersurface.

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
