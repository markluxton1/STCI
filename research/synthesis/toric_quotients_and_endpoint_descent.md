# Orbit-closure families, endpoint gluing, and projective equations

Fix an algebraically closed field \(k\), the embedding
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and the coordinate weights
\((0,1,3,4)\). Unless a characteristic is specified, the statements below
work in arbitrary characteristic. A finite quotient of the transverse torus
produces an actual projective curve scheme, with its nilpotents retained.
It need not produce a complete intersection. Its two endpoint lattices
measure exactly what the finite parametrization adds to that image.

**Status and scope.** The prescribed quartic pair is described in [R-0021](../results/quartic_mu4_degeneration.md). The constant-quotient
formulation and examples below are deductions: independent
review reconstructed the written image, endpoint, proper-pair and flat-collision
arguments, including the characteristic-three calculation. The finite
determinant and index computations were checked separately.
The [full tropical modification](tropical_thickenings_and_endpoint_duality.md)
owns the moving-family theorem, and [endpoint valuation fans](endpoint_valuations.md)
owns the benchmark's contact and cancellation analysis. The calculations here
are a source reformulation and degree-exhaustion test, not a new unrestricted
STCI obstruction. Exact finite calculations are retained in the
[quotient and residual verifier](../investigations/torus-residual-controls/verify.py).

## Geometry of a finite family of orbit closures

The dense coordinate torus of \(\mathbf P^3\) carries the one-dimensional
subtorus \(T\) whose orbit closure through \((1,1,1,1)\) is \(C\).
The quotient of the dense torus by \(T\) is a two-dimensional torus.
A finite subscheme of that quotient therefore describes a finite,
possibly nonreduced, family of quartic orbits. The geometric question is
not merely how many orbits occur: it is how their closures assemble into
one projective scheme at the two common fixed endpoints.

The natural construction is the **scheme-theoretic image** of the family
of parametrized orbit closures. It retains nilpotent directions, and
unlike a reduced union it has a well-defined finite modification. The
coordinate kernel below constructs that image, rather than defining a
new kind of quotient intrinsically.

Let
\[
 B=k[u^{\pm1},v^{\pm1}]/J,\qquad n=\dim_kB>0,
\]
and put \(S=k[x_0,x_1,x_2,x_3]\). Give \(s,t\) degree one and define
\[
 K=\ker\bigl(S\longrightarrow B[s,t]\bigr),\qquad
 (x_0,x_1,x_2,x_3)\longmapsto(s^4,s^3t,ust^3,vt^4).
 \tag{1}
\]
The grading on the target is read in degrees divisible by four. Then
\(Z_B=\operatorname{Proj}(S/K)\) is the saturated scheme-theoretic closure
of \(\mathbf G_m\times\operatorname{Spec}B\) under
\([1:r:ur^3:vr^4]\). Its finite parametrization is
\[
 \nu:\mathbf P^1_B\longrightarrow Z_B,
 \quad [s:t]\longmapsto[s^4:s^3t:ust^3:vt^4].
 \tag{2}
\]
It is an isomorphism over the dense torus. It is not called a normalization
when \(B\) is nonreduced.

Here are the scheme-theoretic points in the assertion. Multiplication by
\(s^4\) on \(B[s,t]\) is injective, so \(K:x_0=K\) and \(K\) is
irrelevant-saturated. Inverting the projective coordinates recovers both
\(u,v\) and the parameter \(r=t/s\), giving exactly the asserted torus
restriction. The kernel in (1) also contracts from that restriction:
localizing by \(st\) is injective on \(B[s,t]\). Thus the closure retains
all relations and nilpotents, rather than just its closed points.

The two source charts have coordinate rings \(B[r]\) and \(B[z]\), where
\[
 z=x_2/x_3=(u/v)(s/t),\qquad
 \alpha=v^2/u^3,\qquad\beta=v^3/u^4.
 \tag{3}
\]
Their image rings are respectively
\[
 k[r,r^3u,r^4v]\subset B[r],\qquad
 k[z,z^3\alpha,z^4\beta]\subset B[z].
 \tag{4}
\]
Both inclusions are finite: a fixed finite \(k\)-basis of \(B\) generates
the right side over the left side, which already contains the indicated
parameter. The source is proper, so its scheme image is closed; (4)
therefore describes the charts of \(Z_B\). Its boundary consists only of
the two endpoint schemes supported at \(p_0=[1:0:0:0]\) and
\(p_\infty=[0:0:0:1]\). There are no boundary curves.

For each point \((c,d)\) of \(\operatorname{Spec}B_{\mathrm{red}}\), the
reduced image is the smooth rational quartic
\([s^4:s^3t:cst^3:dt^4]\). Distinct such points give distinct torus
components, and their closures meet only at the endpoints. In particular,
\(C\subset (Z_B)_{\mathrm{red}}\) precisely when \((1,1)\) is in that
finite support, and sole reduced support \(C\) means support only there.
This is separate from the scheme thickness recorded by \(B\).

The rings in (4) are finite torsion-free modules over \(k[r]\) and
\(k[z]\), respectively. Consequently they are Cohen--Macaulay of
pure dimension one, including at the endpoints. This excludes embedded
endpoint points as well as extra boundary components.

## The two endpoints as a finite gluing defect

Away from the two fixed endpoints the finite parametrization is an
isomorphism. All failure of the orbit-family modification to be an
isomorphism is consequently concentrated at those endpoints. This is
the geometric reason that **two finite-length defects** control the
difference between the Hilbert polynomial of the source family and
that of its projective image.

These defects are cokernel lengths of the structure-sheaf inclusion,
not automatically conductor lengths, and not degrees of residual curves.
The following completed algebras are concrete presentations of that
finite gluing problem.

Completing (4) at their endpoints gives the exact image algebras
\[
 A_0=k[[r]][r^3u,r^4v]\subset B[[r]],\qquad
 A_\infty=k[[z]][z^3\alpha,z^4\beta]\subset B[[z]].
 \tag{5}
\]
The brackets denote the finite module algebra, equivalently its completed
image; these are not merely first-normal symbols. Subtracting constants
from \(u,v\), or from \(\alpha,\beta\), gives the same algebra when useful.

Both quotients in (5) have finite length. Indeed, positive monomials in
\(u,v\) span \(B\): invertibility and a polynomial relation with nonzero
constant coefficient express each inverse as a polynomial in the original
unit. Choose a monomial basis \(u^iv^j\), \(i,j\ge0\). For
\(N\ge\max(3i+4j)\),
\[
 r^N B[[r]]\subset A_0.
 \tag{6}
\]
The transformation in (3) is invertible on the transverse torus:
\[
 u=\beta^2/\alpha^3,\qquad v=\beta^3/\alpha^4.
 \tag{7}
\]
Hence \(\alpha,\beta\) generate the same finite algebra by positive
monomials, and the identical argument supplies a conductor tail at infinity.
This proves finiteness without reducedness or separability assumptions.

Write
\[
 \delta_0=\dim_k(B[[r]]/A_0),\qquad
 \delta_\infty=\dim_k(B[[z]]/A_\infty).
\]
The finite map has the exact sequence
\[
 0\longrightarrow\mathcal O_{Z_B}\longrightarrow
 \nu_*\mathcal O_{\mathbf P^1_B}\longrightarrow
 Q_0\oplus Q_\infty\longrightarrow0,
 \quad\ell(Q_i)=\delta_i.
 \tag{8}
\]
The four sections in (2) have no common zero and pull back
\(\mathcal O_{Z_B}(1)\) to \(\mathcal O_{\mathbf P^1_B}(4)\).
Twisting (8), taking Euler characteristics and using
\(\chi(\mathcal O_{\mathbf P^1_B}(4d))=n(4d+1)\) gives
\[
 \boxed{P_{Z_B}(d)=4nd+n-\delta_0-\delta_\infty.}
 \tag{9}
\]
In particular \(\deg Z_B=4n\) and
\(p_a(Z_B)=1-n+\delta_0+\delta_\infty\).
The defects measure functions lost when endpoint fibers are contracted;
they do not measure residual curves.

## When does the compactified family have two global equations?

The finite orbit family and its endpoint gluing determine a projective
curve scheme. Whether it is a complete intersection is a separate
**global presentation** question. In codimension two, the combination
of a proper pair of containing hypersurfaces and degree exhaustion
answers this question exactly. The genus equality obtained from endpoint
defects is only a necessary numerical shadow of this presentation test.

For positive integers \(a,b\), the following criterion is exact:
\[
 Z_B\text{ is a scheme CI of type }(a,b)
 \iff ab=4n\text{ and there exist }F\in K_a,G\in K_b
 \text{ with }\gcd(F,G)=1.
 \tag{10}
\]
The forward implication is immediate. For the converse, the gcd condition
makes \(X=V(F,G)\) a pure Cohen--Macaulay complete-intersection curve
containing \(Z_B\). Its degree equals \(4n\), so the inclusion is an
equality at every generic point: a positive generic kernel would contribute
a positive degree. The remaining kernel
\(\mathcal I_{Z_B}/\mathcal I_X\subset\mathcal O_X\) is supported at
finitely many points. A pure Cohen--Macaulay curve has no nonzero submodule
with such support, so the kernel vanishes as a sheaf. The homogeneous
ideal \((F,G)\) is saturated, as is \(K\), proving \(K=(F,G)\).
Thus equality of degrees is used together with containment, properness and
purity; equal degrees alone would not suffice.

The spaces in (10) have a direct finite coefficient description. For each
monomial \(x^e\) of total degree \(d\), put
\(w=e_1+3e_2+4e_3\). Its image is
\(u^{e_2}v^{e_3}s^{4d-w}t^w\). Distinct integer weights have distinct
binary monomials, even in positive characteristic. Therefore
\[
 H_{S/K}(d)=\sum_{w=0}^{4d}
 \dim_k\operatorname{span}\{u^{e_2}v^{e_3}: |e|=d,
                         \ e_1+3e_2+4e_3=w\}.
 \tag{11}
\]
Within each weight, the coefficient kernel supplies exactly the corresponding
part of \(K_d\). This is a finite construction of equation spaces, not a
proof that their elements contain a proper pair.

If (10) holds, comparing (9) with the CI genus formula yields the necessary
identity
\[
 \delta_0+\delta_\infty=n(2a+2b-7).
 \tag{12}
\]
Its converse has not been asserted: the actual gcd-one equation pair remains
necessary. Numerically compatible endpoint defects do not establish ACMness,
Gorensteinness, or two homogeneous generators.

## The fourth-root family: four branches versus one thick branch

The quartic benchmark has a uniform geometric interpretation: four
transverse quotient points in characteristic zero give four quartic
branches meeting at the two fixed endpoints, while in characteristic
two their quotient becomes one nonreduced point and the projective
image becomes a thickening of \(C\). The endpoint modification persists
in both settings, but the conductor of a **nonreduced modification**
must not be confused with the normalization conductor of the reduced
curve. The calculations below make that distinction exact.

Take \(B=k[u]/(u^4-1)\), \(v=1\), so \(n=4\). The prescribed equations
\[
 F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3
\]
belong to \(K\), have gcd one, and exhaust degree sixteen. Thus (10)
identifies their scheme with \(Z_B\). The statement and its full
integral flatness and support proof are
[R-0021](../results/quartic_mu4_degeneration.md) and
[its proof home](../arguments/quartic_specialization_and_symbols.md#1-what-actually-coalesces).

At zero, \(v=1\) makes the weight-four generator redundant. A DVR basis is
\(1,r^3u,r^6u^2,r^9u^3\), so \(\delta_0=18\). At infinity,
\(\alpha=u^{-3}=u\), \(\beta=u^{-4}=1\), and the same calculation gives
\(\delta_\infty=18\). At either endpoint the conductor into the finite
modification is exactly \(r^9B[[r]]\), with \(z\) replacing \(r\) at
infinity. For characteristic zero this is the ordinary four-branch
conductor, also described by the pairwise order-three contacts in the
existing proof. Equivalently, in the cyclic basis, no nonzero ideal of
\(B\) lies in the span of \(1,u,u^2\): multiplication by \(u\) and the
nondegenerate coefficient-of-\(u^3\) pairing prove this directly.
Thus no coefficient below order nine can belong to the conductor.

In characteristic two put \(u=1+\epsilon\), \(\epsilon^4=0\). The same
finite-modification lattice has basis
\(1,r^3\epsilon,r^6\epsilon^2,r^9\epsilon^3\), index eighteen and
conductor \(r^9B[[r]]\). This is the conductor of an inclusion of
nonreduced rings. The reduction of the image is the smooth curve \(C\),
whose normalization has defect zero and conductor equal to its full ring
(zero conductor divisor). These two conductors must not be identified.
The [valuation fan](endpoint_valuations.md) continues to own the distinct
contact and initial-polynomial descriptions.

## Why the embedded quotient matters more than its abstract algebra

Two isomorphic finite parameter schemes can have different projective
images: the chosen map into the quotient torus determines how orbit
branches meet and which functions descend at infinity. The following
comparison is a geometric counterexample to classifying the image by
the abstract quotient algebra alone. Its determinants certify the
different endpoint gluing.

In characteristic zero compare two embeddings of the abstract algebra
\(k^4\). The roots-of-unity embedding just used has genus thirty-three.
Instead let \(u\) have values \(1,2,3,4\) and set \(v=1\). At zero the
weighted basis is still \(1,r^3u,r^6u^2,r^9u^3\), so \(\delta_0=18\).
At infinity put \(\alpha=u^{-3}\), \(\beta=u^{-4}\). The evaluation matrix
with rows \((1,u^{-3},u^{-4},u^{-6})\), in the order \(u=1,2,3,4\), has
\[
 \det=\frac{1505}{7962624}\ne0.
 \tag{13}
\]
Consequently the exact weighted lattice basis is
\(1,z^3\alpha,z^4\beta,z^6\alpha^2\). Before weights \(3,4,6\),
respectively, there are no further generating monomials, so its index is
\(3+4+6=13\). Formula (9) gives
\[
 P(d)=16d-27,\qquad p_a=28.
 \tag{14}
\]
It cannot be a \((4,4)\) CI, whose genus is thirty-three. Thus the abstract
finite algebra, even with four reduced points, omits the transverse coordinate
embedding that controls descent at the second endpoint.

There is an exact one-point collision with the same smaller genus. Let
\[
 B=k[\epsilon]/(\epsilon^4),\qquad u=1+\epsilon,\qquad v=1
 \quad(\operatorname{char}k=0).
\]
Again \(\delta_0=18\). At infinity subtract the constant terms and write
\[
 \begin{aligned}
 a&=u^{-3}-1=-3\epsilon+6\epsilon^2-10\epsilon^3,\\
 b&=u^{-4}-1=-4\epsilon+10\epsilon^2-20\epsilon^3.
 \end{aligned}
\]
Then
\[
 b=\tfrac43a+\tfrac29a^2-\tfrac4{81}a^3,
 \qquad \det(a,b,a^2)_{(\epsilon,\epsilon^2,\epsilon^3)}=36.
 \tag{15}
\]
Thus the infinity lattice has basis \(1,z^3a,z^4b,z^6a^2\), index thirteen,
and once more (14). All products of generators at weights at least six
reduce in that basis without negative powers of \(z\); below those weights
the displayed independent elements exhaust the possibilities.

This endpoint also detects more than the genus mismatch. Modulo the regular
parameter \(z\), put \(x=[z^3a]\), \(y=[z^4b]\). Their square \(x^2\)
is the fourth basis vector; higher products reduce with a positive factor of
\(z\). Hence
\[
 A_\infty/zA_\infty\simeq k[x,y]/(x^3,xy,y^2).
 \tag{16}
\]
Its socle has basis \(x^2,y\), so it has type two. Since \(z\) is regular,
the endpoint is not Gorenstein and cannot be a local complete intersection.
The collision retains sole reduced support \(C\), but it does not retain
the required local algebra of a CI.

## Colliding orbit families inside the Hilbert scheme

Collision of transverse quotient points does not by itself produce a
flat family of their projective images: endpoint gluing can jump.
Here the endpoint lattices stay locally free with constant defect,
which supplies the missing flatness argument. Thus this example is
best understood as a **Hilbert-scheme degeneration of compactified orbit
families**, with the marked quartic retained, rather than simply a
specialization of four roots.

The preceding nilpotent image is an actual flat limit of four-component
images of genus twenty-eight. In characteristic zero use
\[
 B_h=k[h,\epsilon]/\bigl(\epsilon(\epsilon-h)
                         (\epsilon-2h)(\epsilon-3h)\bigr),
 \quad u=1+\epsilon,\quad v=1.
 \tag{17}
\]
Restrict the parameter line to an open neighborhood of zero on which the
norm of \(1+\epsilon\) and the determinant of \((1,a,b,a^2)\) are units,
where \(a=(1+\epsilon)^{-3}-1\), \(b=(1+\epsilon)^{-4}-1\).
This neighborhood exists by (15). Denote its coordinate ring by \(R\).
The source algebra is free of rank four over \(R\). The zero-endpoint
lattice has the constant weighted basis
\(1,r^3\epsilon,r^6\epsilon^2,r^9\epsilon^3\); the infinity lattice has
\(1,z^3a,z^4b,z^6a^2\). Their endpoint quotients are free \(R\)-modules
of ranks eighteen and thirteen. For example each weighted basis vector of
weight \(q\) contributes the free quotient \(R[z]/(z^q)\); independence
and closure follow from the unit coefficient determinant and the weights.

Away from the endpoints the image equals the source torus. Consequently the
relative version of (8) has a flat source sheaf and flat endpoint quotient;
its kernel, the image's structure sheaf, is flat over \(R\). This proves
flatness of the image family itself, rather than assuming that scheme images
commute with arbitrary base change. The weighted bases show that the fiber
images agree with these fibers. Every image has polynomial \(16d-27\).
For \(h\ne0\) the four roots are distinct, while at zero their full length
four coalesces. The quotient \(\epsilon=0\) gives \(u=v=1\) throughout,
so the fixed embedded curve \(C\) is retained.

This family is not a flat deformation of the genus-thirty-three
fourth-root benchmark through these projective images. Its Hilbert polynomial
precludes that assertion. The existing
[root pencil](root_pencil_geometry.md#3-three-ways-the-pencil-leaves-the-open-arrangement)
already gives actual partial CI coalescence, including a doubled marked
component; the novelty claimed here is only the explicit contrasting
constant-quotient collision and its endpoint calculation.

## Characteristic changes the endpoint gluing

The underlying length-four local quotient can be written in the same
way in different characteristics. Its projective image nevertheless
changes because the power maps defining the two endpoint embeddings
have characteristic-dependent linear relations. The comparison is
therefore about **embedded multiple curves and their gluing**, not
merely about whether roots become inseparable.

Form the image separately over each algebraically closed field using
\(B=k[\epsilon]/(\epsilon^4)\), \(u=1+\epsilon\), \(v=1\).
At zero the index is eighteen in every characteristic. The infinity
calculation is as follows:

| Characteristic | Infinity coefficient data and weighted basis | \(\delta_\infty\) | \(p_a\) |
| --- | --- | ---: | ---: |
| \(0\), or \(p>3\) | determinant (15) is a unit; weights \(0,3,4,6\) | 13 | 28 |
| \(2\) | \(a=\epsilon,b=0\); basis \(1,z^3\epsilon,z^6\epsilon^2,z^9\epsilon^3\) | 18 | 33 |
| \(3\) | \(a=-\epsilon^3,b=2\epsilon+\epsilon^2+\epsilon^3\); basis \(1,z^3a,z^4b,z^8b^2\) | 15 | 30 |

In characteristic three, \(a,b,b^2\) are independent and \(ab=a^2=0\),
so weights \(3,4,8\) are exact. In characteristic two \((1+\epsilon)^4=1\),
so this image is exactly the prescribed benchmark CI. The other displayed
genera rule out type \((4,4)\). These are images formed in the indicated
fields; no commutation of scheme image with reduction of a characteristic-zero
model is claimed. The variation illustrates why the full embedded quotient,
not just its length, matters in arithmetic comparison.

## From constant orbit families to genuinely moving transverse structure

Binomial equations provide a transparent class of finite transverse
schemes, but their abstract Smith invariants do not determine the
projective image. More importantly, a hypothetical supported complete
intersection need not arise from a **constant** finite quotient.
The full transverse structure can vary along \(C\), and its endpoint
descent must then be studied together with that movement. The lattice
calculation below identifies the tractable constant case and the
precise boundary of its applicability.

For a compatible rank-two lattice of binomial relations
\(u^{\ell_1}v^{\ell_2}=c_\ell\), algebraic closedness permits rescaling
\(u,v\) to remove the constants. If \(L\subset\mathbf Z^2\) is the exponent
lattice, the resulting finite quotient is the group algebra
\(k[\mathbf Z^2/L]\). Smith normal form gives
\[
 B\simeq k[U^{\pm1},V^{\pm1}]/(U^{d_1}-1,V^{d_2}-1),
 \quad d_1\mid d_2,\quad n=d_1d_2.
 \tag{18}
\]
In characteristic \(p>0\), write \(d_i=p^{a_i}m_i\), \(p\nmid m_i\).
There are \(m_1m_2\) reduced points, each with local algebra
\(k[\eta_1,\eta_2]/(\eta_1^{p^{a_1}},\eta_2^{p^{a_2}})\)
and length \(p^{a_1+a_2}\). In characteristic zero all \(n\) points
are reduced. This is the classical roots-and-nilpotents mechanism expressed
in the present coordinates, not a new classification of arbitrary finite
quotients or homogeneous defining pairs. The original \(u,v\) embeddings
must still be carried through (5); Smith invariants alone do not recover
those endpoint algebras.

The [sextic residuals and limits](toric_sextic_residuals_and_limits.md)
apply this language to actual residual curves and to a full saturated limit.
They do not enlarge the constant-quotient framework to arbitrary supported
complete intersections. For such an actual pair of degrees \((a,b)\), the
[entire finite modification](tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification)
is a generally moving embedded quotient over \(\mathbf P^1\), with rank
\(m=ab/4\), degree \(e\), and
\[
 \delta_0+\delta_\infty=e+m(2a+2b-7).
 \tag{19}
\]
That source proves \(e>0\) in characteristic zero and when \(p\nmid ab\).
For sole-support type \((6,6)\), this means rank nine and
\(\delta_0+\delta_\infty=e+153\), with positive \(e\) in that range.
A constant \(B\) has \(e=0\) and therefore cannot represent every such pair.

The remaining interfaces are precise: construct and test actual gcd-one
pairs in (10) for a declared finite quotient; classify which embedded
quotients permit the two endpoint descents; or move to the full positive-degree
quotient family in (19) and recover its two global homogeneous generators.
The examples show that abstract algebra, total length, endpoint indices and
flat collision each omit some of that information. No assertion here excludes
all moving families, gives a new unrestricted obstruction, or resolves the
characteristic-zero STCI question.
