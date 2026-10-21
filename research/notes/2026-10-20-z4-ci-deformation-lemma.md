# Persistence and containment for the prescribed embedded quadruple structure

Status: new lemma, independently reviewed on 2026-10-21; not promoted.
Review: [independent audit](2026-10-20-z4-lift-independent-audit.md).

This note concerns only the curve
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) and the special fiber
\(Z_0=V(x_1^4-x_0^3x_3,x_2^4-x_0x_3^3)\) over \(k=\mathbf F_2\).
It does not use any existing characteristic-zero quartic-carrier exclusion.
The normal-bundle splitting is used as supplied in the assignment and is not
rederived here. The special-fiber regular-sequence and local-structure checks
are explicit hypotheses below; the companion computation verifies them.

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

## Scope and base distinction

All three arguments hold over either stated DVR. Over \(\mathbf Z_2\),
\(K=\mathbf Q_2\); the generic support condition must then mean the base
change \(C_{\mathbf Q_2}\). A nonexistence proof valid over every
characteristic-zero field rules out both DVRs. Existence over \(\mathbf Z_2\)
would not on its own imply algebraization over \(\mathbf Z_{(2)}\), and no
such implication is made here.

These results reduce the full embedded lifting problem to unrestricted
quartic coefficient equations over the DVR. They are reductions, not an
existence or nonexistence theorem for the required lift. No existing accepted
result has been edited or promoted by this note.
