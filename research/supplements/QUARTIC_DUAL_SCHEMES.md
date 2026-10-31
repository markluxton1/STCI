# Dual discriminant: intersections, singular cycle and endpoint socles

The fixed marked system is \(C=[s^4:s^3t:st^3:t^4]\), over an algebraically closed characteristic-zero field unless a characteristic is explicitly changed. Write dual coordinates [A:B:C:D] for the hyperplane section As4+Bs3t+Cst3+Dt4. The exact polynomial identities determine complete Cartier intersections, while the endpoint Hilbert--Burch calculation determines embedded singular corrections that generic cusp/node models cannot see. The [flag chapter](QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md) supplies the marked incidence interpretation.

<a id="quartic-dual-intersections"></a>

## Three dual surfaces and their full intersection schemes

Dual coordinates \([A:B:C:D]\) mean the hyperplane
\(Ax_0+Bx_1+Cx_2+Dx_3=0\). Its section on the parameter line is
\[
f=A s^4+B s^3t+C st^3+D t^4.
\]
Let
\[
\begin{aligned}
M&=AD-BC,& L&=BC-4AD,\\
K&=AC^2+B^2D,& N&=AC^2-B^2D.
\end{aligned}
\]
The dual quadric is \(Q^\vee=V(M)\). The dual of
\(R=V(x_0x_2^2-x_1^2x_3)\) is \(R^\vee=V(K)\).
Indeed the ruling parametrization \([a:b:zb:z^2a]\) gives Gauss image
\([z^2b:-2z^2a:2za:-b]\), and substitution gives \(K=0\).
This image is two-dimensional; its closure is the irreducible cubic
\(V(K)\). Its finite normalization, distinct from its singular projected
image, is the cubic scroll \(\mathbb F_1\); the
[Gauss-map investigation](CUBIC_SCROLL_AND_RULED_SURFACES.md)
studies that normalization and the resolved Gauss map.

Write \(\Delta\) for the ordinary discriminant of
\(A+Bu+Cu^3+Du^4\), interpreted homogeneously as the binary-quartic
discriminant. Thus \(C^\vee=V(\Delta)\).

## 2. The invariant bridge

**Proposition 1.** There are exact polynomial identities
\[
\boxed{\Delta=-4L^3-27K^2}
\tag{1}
\]
and
\[
\boxed{\Delta=4M(8AD+BC)^2-27N^2.}
\tag{2}
\]

**Proof.** For a binary quartic
\(a t^4+b st^3+c s^2t^2+d s^3t+e s^4\), use the coefficient
normalization
\[
I=12ae-3bd+c^2,
\quad
J=72ace+9bcd-27ad^2-27b^2e-2c^3,
\quad
\Delta=(4I^3-J^2)/27.
\]
For the marked linear system, \((a,b,c,d,e)=(D,C,0,B,A)\), hence
\(I=-3L\) and \(J=-27K\), proving (1).
Furthermore
\[
K^2-N^2=4AB^2C^2D,
\qquad
L^3+27AB^2C^2D=-M(8AD+BC)^2,
\]
or direct expansion gives (2). For verification, the full discriminant is
\[
256A^3D^3-192A^2BCD^2-27A^2C^4
-6AB^2C^2D-27B^4D^2-4B^3C^3.
\]
The invariant formulas give the geometric explanation: the projected
dual cubic is the restriction of the classical locus \(J=0\), while
\(L=0\) is the invariant quadric \(I=0\). The containing dual quadric
\(M=0\) is a different quadric. These are classical binary-quartic
invariants; this note makes no novelty claim. The restriction identifies
the objects in this particular marked embedding. \(\square\)

Equation (1) does not assert that \(C^\vee\) is globally a product of a
cusp with a curve. The map given by the invariant expressions can have
critical loci; local singular-scheme analysis must retain that map.

## 3. Full intersection with the dual cubic

**Proposition 2.** The full projective scheme intersection is
\[
C^\vee\cap R^\vee=V(K,L^3).
\tag{3}
\]
Set \(D_R=V(K,L)\). This is a reduced complete-intersection curve, the
union of the osculating quartic \(O\) and the two endpoint pencil lines
\[
\ell_0=V(A,B),\qquad \ell_\infty=V(C,D).
\]
Consequently (3) is the triple effective Cartier divisor \(3D_R\) on
\(R^\vee\). Its fundamental cycle is
\[
3[O]+3[\ell_0]+3[\ell_\infty].
\]
The equation (3), rather than this cycle alone, specifies all scheme
structure at the hyperosculating endpoints.

**Proof.** Identity (1) gives equality of ideals
\((K,\Delta)=(K,L^3)\), since 4 is invertible. The cubic is integral,
and \(L\) is nonzero on it, so its restriction is a nonzerodivisor and
defines a Cartier divisor.

On \(D=1\), eliminating \(A=BC/4\) from \(L=0\) gives
\[
K=B(B+C^3/4).
\tag{4}
\]
One branch is \(\ell_0\). The other is the osculating quartic,
parametrized on this chart by
\[
[-u^4:2u^3:-2u:1].
\]
The reversed chart \(A=1\) gives the osculating curve and
\(\ell_\infty\). The remaining possible points have \(A=D=0\)
and \(BC=0\); they are the points \([0:1:0:0]\) and
\([0:0:1:0]\), already on the corresponding lines. The complete
intersection \((K,L)\) is Cohen--Macaulay, hence has no embedded
associated points. It is generically reduced on its three support
components by (4), its reversal, and the nonsingular line charts.
A generically reduced Cohen--Macaulay curve is reduced. This also proves
that \((K,L^3)\) has no extra embedded points: it too is a complete
intersection. \(\square\)

At \(H_0=[0:0:0:1]\), equation (4) exhibits two smooth reduced branches
meeting to order three. On the smooth ambient quadric \(L=0\), the
intersection ideal is \((B,C^3)\), of length three. The same holds at
\(H_\infty=[1:0:0:0]\). This contact is part of the reduced Cartier
divisor \(D_R\); the full intersection additionally cubes its principal
ideal inside the singular cubic. One must not replace \((K,L^3)\) by
the cube of the ambient ideal \((K,L)\).

There is a useful complete normalization check. On a chart of the dual
scroll with \(D=-1\), write
\[
[A:B:C:D]=[z^2:-za:a:-1].
\]
Then the hyperplane section of the original curve factors as
\[
z^2-za u+a u^3-u^4
=-(u^2-z)(u^2-au+z),
\tag{5}
\]
and
\[
\nu^*L=z(4z-a^2),\qquad
\nu^*\Delta=4z^3(a^2-4z)^3.
\tag{6}
\]
The three factors of the discriminant product formula are respectively
\(4z\), \(a^2-4z\), and the square of
\(z(4z-a^2)\). Thus the same double-root collision simultaneously
affects a quadratic and the resultant of the two quadratics. This
explains the exponent three through residual divisors.

Globally, on \(\mathbb F_1\), let \(E^2=-1\), let \(f\) be a ruling
fiber, and let \(H=E+2f\) be the dual hyperplane class. The strict
osculating quartic has class \(2E+2f\), and (6), with its reversed chart,
gives the exact Cartier pullbacks
\[
\nu^*D_R=\widetilde O+f_0+f_\infty\sim2H,
\quad
\nu^*(C^\vee\cap R^\vee)
=3\widetilde O+3f_0+3f_\infty\sim6H.
\]
These assertions concern the pullback of the **entire principal divisor**
\(D_R\). They do not identify the full inverse ideal of the individual
curve \(O\) with its divisorial hull. Indeed, on this \(D=-1\) chart,
\[
I_O=(A-C^4/16,\ B+C^3/4),\qquad
I_O\mathcal O_{\mathbb F_1}
=(z-a^2/4)(z,a).
\tag{10}
\]
The last factor is the colength-one endpoint correction. Thus the full
inverse ideal and the strict Cartier curve differ even though the
pullback of their union with the endpoint fibers is principal.

## 4. Full intersection with the dual quadric

**Proposition 3.** The full projective scheme intersection is
\[
C^\vee\cap Q^\vee=V(M,N^2).
\tag{7}
\]
Let \(\Gamma_Q\) denote the image of the quadric-tangent section
\(p\mapsto T_pQ\). Then the reduced complete intersection
\(D_Q=V(M,N)\) equals
\(\Gamma_Q\cup\ell_0\cup\ell_\infty\), and (7) is the double
Cartier divisor
\[
2D_Q=2\Gamma_Q+2\ell_0+2\ell_\infty
\quad\hbox{on }Q^\vee.
\]

**Proof.** Identity (2) gives
\((M,\Delta)=(M,N^2)\). In Segre coordinates
\[
[A:B:C:D]=[ac:ad:bc:bd],
\]
the original hyperplane section and the cubic \(N\) factor as
\[
f=(a s^3+b t^3)(c s+d t),
\qquad
N=ab(bc^3-ad^3).
\tag{8}
\]
The third factor in \(N\) is the smooth graph
\(ad^3=bc^3\); it is the quadric-tangent curve, with parametrization
\[
\Gamma_Q(u)=[u^4:-u^3:-u:1].
\]
The first two factors are the two endpoint pencil lines. They are
distinct reduced divisors, so \(D_Q\) is reduced. Alternatively the
discriminant product formula applied to (8) gives the exact identity
\[
\Delta|_{Q^\vee}=-27a^2b^2(ad^3-bc^3)^2,
\tag{9}
\]
including all boundary points. The repeated factors are forced by the
resultant square and the discriminant \(-27a^2b^2\) of the cubic
factor. This proves the scheme statement, not just its support. \(\square\)

The line \(a=0\) meets \(\Gamma_Q\) at \(c=0\), with intersection
length three; the other line has the reversed endpoint behavior.
The total degree is \(2(4+1+1)=12\), as required for a sextic cut on a
quadric. Equation (3) has degree \(3(4+1+1)=18\). These degree checks
corroborate, but do not substitute for, the exact ideal identities.

For comparison, the third full intersection is
\[
R^\vee\cap Q^\vee=V(M,K).
\]
Its pullback to the same Segre quadric is the reduced divisor
\(ab(bc^3+ad^3)=0\): the two endpoint lines and a different smooth
quartic. The [scroll-duality note](CUBIC_SCROLL_AND_RULED_SURFACES.md)
provides its interpretation and the Gauss maps. The minus and plus
signs in (8) and this last equation cannot be interchanged. In
particular \(\Gamma_Q\), \(O\), and this third quartic are distinct.

## 5. Full dual intersections versus common-point traces

The quadric-tangent section of the conormal surface maps to
\(\Gamma_Q\), while the closure of the Gauss trace of \(R\) along
the smooth part of \(C\) maps to \(O\). These are the distinguished
same-point constructions.

For a general point \([0:0:C:D]\in\ell_0\), the plane section of
\(C\) is \(t^3(Cs+Dt)\), so its contact point on \(C\) is \(p_0\).
The tangency point on the smooth quadric, determined by its polarity,
is
\[
[D:-C:0:0].
\]
This usually differs from \(p_0=[1:0:0:0]\). The endpoint pencil line
in \(C^\vee\cap Q^\vee\) therefore records tangencies at different
points of the two varieties. Only its limiting hyperosculating plane
\([0:0:0:1]\) has the quadric tangency point \(p_0\).

For \(R\), the same endpoint line is a family of limiting tangent
planes at its singular pinch point. A general plane of this pencil is
not obtained by following \(T_pR\) along smooth points \(p\in C\)
as \(p\to p_0\); that particular path selects only the osculating
limit \(H_0\). The reversed statements hold at infinity. Thus the
extra lines are actual components of the full dual intersection, while
the closure of the marked smooth-curve trace is the single quartic
\(O\). They must not be discarded or identified with the distinguished
section.

The reduced common intersection of all three dual surfaces is exactly
\(\ell_0\cup\ell_\infty\). Indeed on \(Q^\vee\), requiring both
\(K=0\) and \(\Delta=0\) away from \(ab=0\) would require
\(bc^3+ad^3=bc^3-ad^3=0\), impossible there in characteristic zero.
This is a support statement only; the equations above retain the full
triple-intersection scheme if it is needed.


<a id="quartic-dual-singular-scheme"></a>

## Jacobian scheme and the two embedded endpoint classes

## 2. A compact global equation and the exact Jacobian ideal

Write a plane section as
\[
f(s,t)=As^4+Bs^3t+Cst^3+Dt^4.
\]
In the dual projective space \(\mathbf P^3_{[A:B:C:D]}\), put
\[
L=BC-4AD,\qquad K=AC^2+B^2D.
\]
The [dual-intersection calculation](QUARTIC_DUAL_SCHEMES.md#quartic-dual-intersections)
uses the classical invariant presentation
\[
\Delta=-4L^3-27K^2
=256A^3D^3-192A^2BCD^2-27A^2C^4
 -6AB^2C^2D-27B^4D^2-4B^3C^3.
\]
For the statements here it suffices to expand the displayed identity;
it does not require a choice of normalization of classical invariants.

Let \(S=k[A,B,C,D]\) and
\[
J=(\Delta_A,\Delta_B,\Delta_C,\Delta_D).
\]
Then
\[
\operatorname{Sing}(C^\vee)=\operatorname{Proj}(S/J).
\]
This is the scheme-theoretic singular locus defined by the relevant
Fitting ideal of differentials. Euler's identity makes \(\Delta\)
redundant in characteristic zero. The four partials, or equivalently
\(-12L^2dL-54K\,dK\), give an exact global definition, including all
endpoints and nilpotents. The replay below verifies that \(J\) is already
irrelevant-ideal saturated. Thus it also gives the homogeneous ideal of
this projective scheme without a hidden saturation step.

The endpoint pencil lines are
\[
\ell_0=V(A,B),\qquad\ell_\infty=V(C,D),
\]
and the two hyperosculating planes, viewed as points of the dual space, are
\[
e_0=[0:0:0:1],\qquad e_\infty=[1:0:0:0].
\]

## 3. Generic transverse structures

**Proposition.** Away from \(e_0,e_\infty\), the singular scheme is a
curvilinear double structure along the osculating quartic and each pencil
line, and is reduced along the bitangent quartic. The transverse surface
singularities are respectively ordinary cusps and ordinary nodes.

**Proof.** For a section having a triple zero and one distinct simple
zero, étale factorization separates the simple root. The discriminant of
the remaining cubic has the ordinary cusp equation
\(4x^3+27y^2=0\), times a unit. Its Jacobian scheme is
\((x^2,y)\). The missing-middle-coefficient condition is transverse to
the triple-root stratum whenever the residual root differs from the
triple root. One can see this on a chart of the stratum by expanding
\((z-u)^3(z-r)\): its middle coefficient is \(3u(u+r)\).
At a nonendpoint point satisfying \(r=-u\), differentiation in \(r\)
is nonzero. At \(u=0,r\ne0\), differentiation in \(u\) is nonzero.
Homogeneous charts cover a residual root at infinity and the opposite
endpoint. Consequently the restriction retains the cusp model, also on
the two pencil lines away from their quadruple-root members.

For a section having two distinct double zeros, étale factorization into
two quadratic factors gives discriminant \(xy\), times a unit, in the
two independent double-root smoothing parameters. The missing coefficient
is transverse to the double-double stratum: on squares of quadratics its
equation is the smooth bitangent conic, and its differential is nonzero
away from the quadruple-root endpoints. Thus the transverse model is a
node, whose Jacobian scheme \((x,y)\) is reduced. These arguments apply
at **every** nonquadruple section on the four components, not only their
generic points. The four components meet only at the two quadruple-root
sections. \(\square\)

The degree of the singular curve, including its generic nilpotent
multiplicities, is therefore
\[
2\deg(\text{osculating quartic})+
\deg(\text{bitangent quartic})+2\deg\ell_0+2\deg\ell_\infty=16.
\]
Zero-dimensional embedded pieces do not change this degree.

## 4. The two embedded endpoint points

Define a homogeneous quintic
\[
h=(BC+8AD)K=(BC+8AD)(AC^2+B^2D),\qquad U=J+(h).
\]

**Proposition.** The ideal sheaf \(\widetilde U\) defines the unmixed
one-dimensional part of the singular scheme. There is an exact sequence
\[
0\longrightarrow k(e_0)\oplus k(e_\infty)
\longrightarrow\mathcal O_{\operatorname{Sing}(C^\vee)}
\longrightarrow\mathcal O_{\operatorname{Proj}(S/U)}
\longrightarrow0.
\]
In particular there is precisely one embedded point of length one at each
hyperosculating plane, and no other embedded associated points.

**Proof.** Three polynomial identities give
\[
Bh=-\frac{2A}{27}\Delta_B-\frac C{54}\Delta_D,
\qquad
Ch=-\frac B{54}\Delta_A-\frac{2D}{27}\Delta_C,
\]
\[
ADh=-\frac{AC}{216}\Delta_B-\frac{BD}{24}\Delta_C
       +\frac{C^2}{108}\Delta_D.
\]
Hence \(U/J\) is supported at \(e_0,e_\infty\), and is at most one
copy of their residue field at each. To establish nonvanishing and
unmixedness, take the chart \(D=1\), with coordinates \(a,b,c\).
The exact local equation is
\[
F=256a^3-192a^2bc-27a^2c^4-6ab^2c^2-27b^4-4b^3c^3.
\]
It is weighted homogeneous of degree 12 for weights \((4,3,1)\).
Set \(g_A=-F_a/6,g_B=-F_b/12,g_C=-F_c/12\), and continue to write
\(h=(bc+8a)(ac^2+b^2)\). Weighted Euler shows that the localized
Jacobian ideal is \((g_A,g_B,g_C)\); no extra equation \(F\) is needed.

The signed maximal minors of
\[
M=\begin{pmatrix}
-b&-ac&ac^2\\
0&-8a-bc&-ac+bc^2\\
-8&c^2&-9b-c^3\\
9c&9b&18a
\end{pmatrix}
\]
are exactly \(9(g_A,g_B,g_C,h)\), in that order. These identities can
be checked directly by four determinants. This ideal has height two:
its support is the same union of curves as that of the Jacobian, because
\(h\) differs from a Jacobian element only at the endpoint. The
Hilbert–Burch theorem now makes the quotient by \((g_A,g_B,g_C,h)\)
Cohen–Macaulay of dimension one. In particular it has no embedded point.
The use here is the standard converse for maximal minors of a matrix
whose ideal has height two; see, for example, the author-hosted paper
[Eisenbud–Huneke, *Cohen–Macaulay Rees Algebras and Their
Specialization*, proof of Theorem 3.4](https://eisenbud.github.io/papers/pdfs/1983-005.pdf)
for the Hilbert–Burch framework. The specific converse used is the standard
Hilbert–Burch theorem for height-two maximal-minor ideals. No novelty
claim is made for this method.

The weights of \(g_A,g_B,g_C,h\) are \(8,9,11,10\).
If \(h\) belonged to \((g_A,g_B,g_C)\), its weight-10 part would be
a linear combination of \(c^2g_A\) and \(cg_B\). Neither contains the
monomial \(ab^2\), whereas \(h\) has coefficient eight on that
monomial. Thus \(h\) is nonzero modulo the Jacobian ideal, including
after localization at the origin. The three displayed identities imply
that its class is annihilated by \((a,b,c)\), so it spans exactly one
copy of \(k(e_0)\).

Coordinate reversal \((A,B,C,D)\mapsto(D,C,B,A)\) preserves \(\Delta\)
and \(h\), so the same proof applies at \(e_\infty\). Away from these
points \(U=J\), and Section 3 excludes embedded structure there. This
proves the assertion. \(\square\)

The residue-field terms carry no preferred trivializations; globally
the generator \(h\) has degree five. At the graded-module level the
exact algebraic statement is
\[
U/J\cong (S/(B,C,AD))(-5),
\qquad J:h=(B,C,AD).
\]
The elementary local proof proves the corresponding sheaf statement;
the exact graded equality is independently checked in the replay.

## 5. A finite global presentation of the unmixed part

For readers who need explicit ideals, set
\[
P_O=(L,\ C^3+4BD^2,\ K,\ B^3+4A^2C),
\]
\[
P_B=(BC+8AD,\ C^3+8BD^2,\ AC^2-B^2D,\ B^3+8A^2C),
\]
and
\[
T_O=(K,\ C^4+8BCD^2-16AD^3,\ L^2,
                 B^4+8A^2BC-16A^3D).
\]
Here \(P_O,P_B\) define the osculating and bitangent quartics. The
following is an **exact computed ideal presentation**, with independent
geometric interpretation provided by Sections 3–4:
\[
U=(A,B^2)\cap(D,C^2)\cap T_O\cap P_B,
\qquad \sqrt{T_O}=P_O.
\]
The replay verifies equality of ideals, the radical, and associated
primes. Thus the endpoint pencil components are the literal planar
double lines \((A,B^2)\) and \((D,C^2)\); the bitangent primary
component is reduced. The osculating component has generic length two.
Together with the preceding short exact sequence this is a complete
scheme description; printing arbitrary embedded primary components
would add noncanonical choices without refining it.

The saturated Jacobian scheme has Hilbert polynomial
\(16n-43\). Its unmixed part has Hilbert polynomial \(16n-45\), and
their difference is the two residue-field contributions. These polynomial
values are exact computational outputs, not deductions from generic
transverse multiplicities alone.


## Characteristic reach and mathematical status

The displayed discriminant polynomial identities are integral and may be specialized as identities. Their geometric interpretation as a reduced dual, Euler redundancy of the discriminant in the Jacobian ideal, generic cusp/node structures, and the stated associated-prime/length decomposition are proved in characteristic zero. Coefficients 2 and 3 participate in that proof, so polynomial specialization is not a positive-characteristic duality or singular-scheme theorem. In characteristic two the actual dual of the primal cubic is a line, even though the specialized characteristic-zero cubic equation still defines a surface; [the scroll proof](CUBIC_SCROLL_AND_RULED_SURFACES.md) computes this directly. The exact [Jacobian verifier](../computations/verify_quartic_dual_singular_scheme_2026_10_24.m2) and its saved exact result support [R-0027](../results/quartic_dual_singular_scheme.md). The full local determinantal proof above, not only the successful computation, explains the two endpoint socles.
