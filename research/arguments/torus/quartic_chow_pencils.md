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
degrees are precisely the powers modulo that carrier described in the
[fixed-carrier geometry](quartic_exceptional_carrier_geometry.md#all-mate-degrees-on-a-retained-exceptional-carrier).

The proof has two distinct parts. **Support reduction** uses the
distinguished torus weights and the geometry at the two fixed endpoints
to isolate the opposite-sign pair. **Rigidity of actual equations**
then comes from the reduced union \(Y=C_+\cup C_-\): it is an
arithmetically Cohen--Macaulay, locally complete-intersection curve
with two planar \(A_7\) singularities. Its Hilbert--Burch resolution
determines both the quartic equation space and a small canonical
module. Linkage and the balanced conormal bundle exclude asymmetric
multiplicities; for the doubled pair, the canonical-module relations
and restriction to the residual line determine the global generators.
Thus the *exceptional uniqueness proof* is geometric, while the
initial support reduction retains its special torus coordinates.

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

The Hilbert polynomial is \(P_Y(n)=8n-6\), hence
\(p_a(Y)=7\). The endpoint geometry also makes the
dualizing sheaf particularly tractable.

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

There is also a geometric check of the transverse normal
parameters used below and in the sextic argument:
the complete intersection \((A,B)\) has degree nine, contains
\(Y\) of degree eight, and contains the residual coordinate
line \(L_{\mathrm{res}}=V(x_1,x_2)\) of degree one. Since \(A,B\)
are coprime, these three distinct components exhaust Bézout
degree, each with multiplicity one. Thus \(A,B\) form
a regular system of transverse parameters at the generic
points of \(C_+\) and \(C_-\).

In degree four the resolution gives
\[
 H^0(I_Y(4))
 =A\,S_1\oplus B\,S_1\oplus kD,\qquad
 h^0(I_Y(4))=4+4+1=9.
\]
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
[even-eight divisor class](quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
explains a doubled divisor on a fixed carrier, but alone does not prove uniqueness.

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
four by Bézout. The residual line
\(L_{\mathrm{res}}\) is not a component, while \(A,B\)
vanish identically on \(L_{\mathrm{res}}\). Thus \(W\) cannot be
contained in \(AS_1+BS_1\). Choose a basis
\[
 F=AL+BM,\qquad G=D+AN+BP,\qquad
 L,M,N,P\in S_1. \tag{*}
\]

### Residual genus excludes the triple branches

Let \(Z=V(F,G)\) and \(Y'=(I_Z:I_Y)\) be the
complete-intersection residual to \(Y\). Peskine--Szpiro linkage gives that \(Y'\) is locally
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
This is the residual-genus obstruction to asymmetric multiplicities.
See [Bănică--Forster, *Multiplicity Structures on Space
Curves*, §1](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf)
and [Eisenbud--Van de Ven, *On the normal bundles
of smooth rational space curves*](https://eisenbud.github.io/papers/pdfs/1981-001.pdf).

## Self-linkage and the canonical conormal quotient

The reduced union \(Y=C_+\cup C_-\) is locally a complete
intersection and arithmetically Cohen--Macaulay, as seen above.
The residual to \(Y\) in a proper \((4,4)\) complete intersection
has already been constructed in the residual-genus argument.
For the symmetric partition, this residual is a self-linkage.

For the \((2,2)\) multiplicity partition proved above, the
linked residual \(Y'=(I_Z:I_Y)\) is Cohen--Macaulay of
degree eight and generically reduced along the two
components. It has no embedded components, so
\(Y'=Y\) scheme-theoretically:
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

It gives two finite-dimensional tests
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
The canonical-module relations and the absence of a common
quadric will turn these necessary section conditions into
a determination of the actual quartic pencil. The dimensions
alone do not impose global two-generator liftability.
See [Bănică--Forster, *Multiplicity Structures on Space Curves*,
§1](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf)
and [Franco--Kleiman--Lascu, *Gherardelli linkage and complete
intersections*](https://arxiv.org/abs/math/0003075).
A conormal quotient does not by itself guarantee two
global quartic generators. The next step uses the
canonical-module relations and restriction to the
residual line to impose precisely that global condition
for this union. No analogous conclusion is asserted
for arbitrary Ferrand doublings.

### Canonical-module rigidity of the pencil

Write \(q:I_Y\twoheadrightarrow\omega_Y(-4)\)
for the self-linkage quotient (SL). Its degree-three
map is the isomorphism in (SL2).

Dualizing the Hilbert--Burch presentation gives the
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
\(H^0(\omega_Y(-1))\). By (SL2), for an
invertible constant matrix
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
**Restricting to \(L_{\mathrm{res}}\)** makes the right
side \(ax_3^2-dx_0^2\). Thus
\[
 \boxed{a=d=0,\qquad bc\ne0.} \tag{R}
\]
This restriction on the residual line determines the
canonical-module framing.

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

## Existence and orbit parameter

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
classification of the exceptional two-support case.
The characteristic-two **single-support construction**
is proved separately in the [Hilbert-over-Chow account](quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision).
The present linkage/normal-bundle argument does **not**
establish a full quartic-pencil classification in
positive characteristic, including odd primes.

## Related exceptional-family developments

The classification proof above is the canonical proof owner. Two separable
consequences now have focused owners:

- [fixed-carrier geometry](quartic_exceptional_carrier_geometry.md), including
  simultaneous endpoint contact, the ten-nodal K3/even-eight identity, and the
  classification of translated mates on a retained exceptional carrier;
- [Hilbert-over-Chow limits](quartic_hilbert_chow_limits.md), including Chow
  nonclosure, both saturated flat limits, the vertical Hilbert fiber, and the
  characteristic-two single-support collision.

These developments use the classified family but are not steps in the
liaison/canonical-module uniqueness proof.
