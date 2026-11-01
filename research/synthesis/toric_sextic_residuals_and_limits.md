# Invariant sextic geometry: orbit closures, residual boundaries, and Hilbert limits

**Status and scope.** This is a provisional mathematical proof home for
explicit proper sextic intersections and their torus limits, over an
algebraically closed field \(k\). Independent review reconstructed the new
examples, residual bound and full-limit proofs in this written text;
they remain provisional and no canonical result is promoted. The inherited actual-source and
sole-support sextic results are cited with their existing status in the
last section. All displayed cycle calculations are characteristic free
unless a narrower hypothesis is stated.

Fix
\[
 C=[s^4:s^3t:st^3:t^4],\qquad
 \lambda\cdot x=(x_0,\lambda x_1,\lambda^3x_2,\lambda^4x_3).
\]
Write \(L_{ij}\) for the coordinate line on which only \(x_i,x_j\)
may be nonzero, and \(p_0=[1:0:0:0]\), \(p_\infty=[0:0:0:1]\).
An eigenform means homogeneous for the **integer character weights**
\((0,1,3,4)\); those characters are not reduced modulo the characteristic.
Every proper sextic pair considered here is a complete intersection of
degree 36, with
\[
 P_Z(n)=36n-144,\qquad
 H_{S/I_Z}(z)=\frac{(1-z^6)^2}{(1-z)^4}.                 \tag{1}
\]
It is Cohen–Macaulay and has no embedded associated components. Equal
degree alone never identifies its scheme structure or residual ideal.

The [torus quotient and endpoint companion](toric_quotients_and_endpoint_descent.md)
owns the general product and endpoint-descent discussion. This home keeps
actual projective equations, cycles and full flat ideals. The joint
[exact verifier](../computations/verify_toric_quotients_and_residual_limits.py)
is supporting evidence; the proofs below specify what its identities
measure and do not treat a successful run as a substitute for family
coverage or saturation.

## 1. Orbit families and the residual boundary

A \(T\)-invariant curve meeting the dense coordinate torus is an orbit
closure, and a finite quotient of that torus records a finite family
of such closures with generic multiplicities. The **projective boundary**
is a different geometric object: coordinate lines or other invariant
curves can occur there without appearing in the finite quotient.

For a proper sextic intersection the total degree is 36. Each
quartic orbit closure consumes four units of degree per unit of
generic multiplicity. The difference between 36 and that moving
degree is the boundary cycle. This explains the degree accounting
before any primary decomposition is performed.

On the dense coordinate torus use
\[
 x=(1,t,t^3u,t^4v),\qquad t,u,v\in k^\times.
\]
An eigenform restricts to a power of \(t\) times a Laurent polynomial
in \(u,v\). Thus a proper eigenpair has dense-torus intersection
\[
 \operatorname{Spec}B\times\mathbf G_m,\quad
 B=k[u^{\pm1},v^{\pm1}]/(f,g),
\]
where \(B\) is finite dimensional (or zero). Properness rules out a
positive-dimensional quotient. The local length at a quotient point is
the generic multiplicity of its orbit closure. For \((\epsilon,\zeta)\)
in the quotient torus this closure is the smooth rational quartic
\[
 C_{\epsilon,\zeta}
 =[s^4:s^3t:\epsilon st^3:\zeta t^4].                 \tag{2}
\]
Consequently the total degree of components meeting the dense torus,
counting generic multiplicities, is \(4\dim_kB\). Other components lie
on the projective coordinate boundary and need a separate calculation.
The quotient algebra does not record their multiplicities or attachment.

### 1.1 Eight quotient points and a quadruple residual line

Set
\[
 I_8=(x_1^6-x_0^4x_2^2,\ x_2^6-x_1^2x_3^4).
                                                               \tag{3}
\]
Its quotient algebra is
\[
 B_8=k[u^{\pm1},v^{\pm1}]/(u^2-1,v^4-1),\qquad\dim B_8=8.
\]
Indeed the raw second equation is \(u^6-v^4\), and \(u^2=1\)
reduces it to \(1-v^4\). If \(\operatorname{char}k\ne2\), the eight
points are simple and the cycle is
\[
 [V(I_8)]=\sum_{\epsilon^2=1,\ \zeta^4=1}
 [C_{\epsilon,\zeta}]+4[L_{03}].                     \tag{4}
\]
In characteristic two the quotient is supported at \((1,1)\), with
local algebra \(k[a,b]/(a^2,b^4)\), so the cycle is
\(8[C]+4[L_{03}]\). In particular length eight need not be curvilinear.

The boundary support follows directly from (3). If one coordinate
vanishes, the equations force \(x_1=x_2=0\), apart from the endpoints
already on this line. At its generic point put \(x_0=1,x_3=z\), and
\(a=x_1,b=x_2\). Then
\[
 (a^6-b^2,b^6-z^4a^2)=(a^2,b^2)
 \quad\text{in }k(z)[a,b]_{(a,b)}.                   \tag{5}
\]
For \(b^2=a^6\), the second equation gives
\(a^2(a^{16}-z^4)=0\); its parenthesis is a unit. This proves the
line multiplicity four in every characteristic. The exact homogeneous
line-primary component is \((x_1^2,x_2^2)\): its generic localization
is (5), it is \(L_{03}\)-primary, and contraction from that generic
localization gives this ideal. The other primary components are the
contractions of the local factors of the torus saturation
\(I_8:(x_0x_1x_2x_3)^\infty\). There are no additional embedded
components because (3) is a proper complete intersection.

For clarity, the endpoint schemes are not replaced by their cycles.
On \(x_0=1\), with \(x_1=t,x_2=y,x_3=z\), the ideal is exactly
\[
 (y^2-t^6,\ t^2(t^{16}-z^4)).                        \tag{6}
\]
On \(x_3=1\), with \(x_0=a,x_1=b,x_2=c\), it is
\[
 (b^2-c^6,\ c^2(c^{16}-a^4)).                        \tag{7}
\]
These identities exhibit the attachment of the quartics to the line,
including inseparable collisions, without inventing embedded components.

### 1.2 Six quotient points and a twelvefold residual line

Set
\[
 I_6=((x_0x_3)^3-(x_1x_2)^3,\ x_1^6-x_0^4x_2^2).
                                                               \tag{8}
\]
Now
\[
 B_6=k[u^{\pm1},v^{\pm1}]/(u^2-1,v^3-u^3),
 \qquad\dim B_6=6.                                  \tag{9}
\]
When the characteristic is neither two nor three, its points are
\((\epsilon,\epsilon\omega)\), with \(\epsilon^2=1,\omega^3=1\),
and are simple. In characteristic three, the points \((1,1)\) and
\((-1,-1)\) each have length three. In characteristic two the three
points \((1,\omega)\) each have length two. Accordingly the torus
part of the cycle is respectively six simple quartics, two triple
quartics, or three double quartics. In every case the remaining term is
\[
 12[L_{23}].                                        \tag{10}
\]
To see its multiplicity, take \(x_2=1,x_3=z,x_0=a,x_1=b\) at the
generic point of \(L_{23}\). The local equations are
\[
 a^3z^3-b^3,\qquad b^6-a^4.
\]
Their lowest forms have degrees three and four and are coprime,
including in characteristics two and three. The regular-local-ring
intersection length is therefore \(3\cdot4=12\). Setting coordinates
to zero in (8) shows that this is the only boundary curve. This also
proves properness and accounts for all 36 degrees.

The endpoint equations, in the charts used above, are
\[
 (z^3-t^3y^3,t^6-y^2)\quad\text{at }p_0,
 \qquad(a^3-b^3c^3,b^6-a^4c^2)\quad\text{at }p_\infty.
                                                               \tag{11}
\]
They retain data absent from the length-six algebra (9).

### 1.3 A noncurvilinear quotient of the same length

Put
\[
 q=x_0x_3-x_1x_2,\qquad A=x_0^2x_2-x_1^3,
 \qquad I_{\mathrm{th}}=(q^3,A^2).                  \tag{12}
\]
The quotient is
\[
 k[u^{\pm1},v^{\pm1}]/((v-u)^3,(u-1)^2),             \tag{13}
\]
a length-six local algebra of embedding dimension two in every
characteristic. It is noncurvilinear, while its projective cycle is
\[
 6[C]+12[L_{23}].                                   \tag{14}
\]
For a direct geometric proof use the Segre coordinates
\[
 x=(ac,ad,bc,bd),\qquad D=bc^3-ad^3.
                                                               \tag{15}
\]
Then \(Q=V(q)\) is smooth, \(C=V_Q(D)\) has type \((1,3)\), and
\(A|_Q=a^2D\). The divisor of \(A^2|_Q\) is
\(2C+4\{a=0\}\), and \(\{a=0\}=L_{23}\). The triple quadric
multiplies these generic multiplicities by three, proving (14).
All generators of (3), (8), and (12) are eigenforms. Their full weight
initial ideals equal the ideals themselves; no generator information is
lost in taking these particular limits.

## 2. Fixed-point incidence forces residual boundary for eigenpairs

The geometric obstruction is an incidence constraint among invariant
curves and the coordinate fixed points. If nine quartic orbit closures
exhausted a sextic complete intersection, there would be no boundary
curve. In particular, the intersection would miss the two fixed points
\(e_1,e_2\), which lie on none of those quartics. Avoiding each fixed
point forces a pure-power term in one of the equations. The resulting
two torus characters then force a coordinate line into both surfaces,
contradicting the assumed absence of boundary components.

The following proof expresses this incidence argument through integer
weights. Its scope is **eigenform pairs**; it does not exclude arbitrary
supported sextic complete intersections or their invariant full flat
limits.

**Proposed theorem.** For any proper pair of sextic eigenforms over an
algebraically closed field of any characteristic, let \(n\) be the
length of its finite dense-torus quotient. Then
\[
 n\le8,\qquad \deg(\text{boundary cycle})=36-4n\ge4.  \tag{16}
\]
This includes pairs containing \(C\); containing \(C\) is not needed
for the proof. The bound is attained by (3). It concerns two eigenforms,
not arbitrary mixed-weight sextic pairs or their full initial ideals.

The degree calculation gives \(n\le9\). Suppose \(n=9\). Every
one-dimensional component is then the closure of a dense-torus orbit,
with its generic scheme multiplicity. Proper complete intersections are
pure and have no embedded associated points. Hence the whole scheme is
the scheme-theoretic closure of its torus restriction: there is no
additional component supported on the coordinate boundary. In particular
its support omits \(e_1=[0:1:0:0]\) and \(e_2=[0:0:1:0]\), since
every orbit closure (2) has only \(p_0,p_\infty\) on that boundary.

At least one equation must therefore have a nonzero \(x_1^6\)
coefficient, and at least one must have a nonzero \(x_2^6\)
coefficient. These pure powers have distinct integer weights six and
eighteen, so they occur in different eigenforms; the two equation
weights are precisely six and eighteen. But a monomial surviving on
\(L_{03}\) has weight divisible by four. Neither six nor eighteen is
divisible by four. Both equations consequently vanish identically on
\(L_{03}\), a contradiction. This proof works in every characteristic:
distinct torus characters remain distinct in positive characteristic.

Geometrically, finite quotient length counts a moving family of quartic
orbit closures, while the two missing coordinate fixed points force
weights incompatible with avoiding the remaining coordinate line.
The argument supplies a residual floor on this actual eigenpair source;
it does not provide an ambient all-pair residual bound.

## 3. Residual curves move before they acquire boundary support

Residual curves of an arbitrary intersection need not be invariant.
A torus degeneration of the **whole intersection scheme** can send
those curves to invariant boundary cycles, even when the original
residual curves avoid the fixed endpoints. The ruled-quadric
description makes this movement visible as degeneration of divisors
on \(Q\). The explicit equations below are certificates for that
geometric specialization, not a classification of all residual curves.

On \(Q\) use (15), with the action \(b\mapsto\lambda^3b\),
\(d\mapsto\lambda d\). Define quartics
\[
 r_{\mathrm{lo}}=x_0^3x_2-x_0x_1^3,\qquad
 r_{\mathrm{hi}}=x_2^3x_3-x_1x_3^3,\qquad r=r_{\mathrm{lo}}+r_{\mathrm{hi}}.
\]
Their weights are three and thirteen, and
\[
 r|_Q=D(a^3c+b^3d).
\]
Set
\[
 G=(x_0+x_3)^2r,\qquad F=q^3+G.                     \tag{17}
\]
The ideal is \((q^3,G)\), a proper sextic complete intersection, since
\[
 G|_Q=(ac+bd)^2D(a^3c+b^3d)\ne0.
\]
Let \(H=V_Q(a^3c+b^3d)\), of type \((3,1)\), and
\(K=V_Q(ac+bd)\), of type \((1,1)\). These are smooth rational
curves: each equation is linear in \(c,d\) with coefficient pair
having no common zero. They have projective degrees four and two,
respectively. The cycle of (17) is
\[
 3[C]+3[H]+6[K].                                    \tag{18}
\]
Both residual curves avoid \(p_0,p_\infty\). In characteristic zero
their attachments to \(C\), under \(a=s^3,b=t^3,c=s,d=t\), are
respectively
\[
 s^{10}+t^{10}=0,\qquad s^4+t^4=0.                  \tag{19}
\]
Each divisor is reduced, and the two divisors are disjoint. The cycle
formula is valid in every characteristic, but the distinctness assertion
in (19) is made only in characteristic zero. At either endpoint \(G|_Q\)
is a unit times \(D\); the local complete intersection is a pure triple
structure on \(C\), locally of the form \((q^3,D)\).

Here and below the multiplicity rule used for \((q^3,f)\) is
\[
 \ell\bigl(R/(f,q^3)\bigr)=3\operatorname{ord}(f|_Q)
                                                               \tag{20}
\]
at a generic component of the divisor on \(Q\). Indeed \(R/(f)\)
is a one-dimensional Cohen–Macaulay local ring, \(q\) is a parameter
and a nonzerodivisor, and its three successive quotients have equal
length. Thus (20) is a scheme calculation, not an inference from degrees.

### 3.1 Specializing divisors, not attracting individual points

Use maximal weight for the \(\lambda\to0\) initial convention. A full
one-parameter ideal for (17) is
\[
 \bigl(q^3,(x_3+h^4x_0)^2
                (r_{\mathrm{hi}}+h^{10}r_{\mathrm{lo}})\bigr).
                                                               \tag{21}
\]
For \(h\ne0\) this is the corresponding torus translate. Its special
fiber is
\[
 (q^3,x_3^3(x_2^3-x_1x_3^2)).                        \tag{22}
\]
The two special generators are coprime. All fibers are proper complete
intersections, so the total complete intersection is \(h\)-torsion free;
(21) is \(h\)-saturated and flat. It is the full limit, retaining (1).
The raw initial forms of both \(F\) and \(G\) coincide. They miss the
additional degree-six initial generator \(q^3\), supplied by \(F-G\).

On \(Q\), the limiting divisors are
\[
 H\rightsquigarrow3\{b=0\}+\{d=0\},\qquad
 K\rightsquigarrow\{b=0\}+\{d=0\}.
\]
Here \(\{b=0\}=L_{01}\) and \(\{d=0\}=L_{02}\). Thus the special
cycle is
\[
 3[C]+15[L_{01}]+9[L_{02}].                          \tag{23}
\]
Its residual cycle misses \(p_\infty\), although its generic residual
curves missed both endpoints. Point attraction alone cannot describe a
flat limit of projective curves: dimensions and Hilbert polynomials
force the full divisors appearing in (23).

### 3.2 Absorption changes the decomposition into marked and residual cycles

There is also a proper flat family
\[
 (q^3,A(A+h^3x_0^3)).                                \tag{24}
\]
On \(Q\), its second equation is
\[
 a^4D(D+h^3ac^3).
\]
For \(h\ne0\), the curve \(H_h=V_Q(D+h^3ac^3)\) is a smooth
\((1,3)\) graph distinct from \(C\): its coefficient pair in \(a,b\)
is \((-d^3+h^3c^3,c^3)\), with no common zero. Consequently
\[
 [Z_h]=3[C]+3[H_h]+12[L_{23}],\qquad
 [Z_0]=6[C]+12[L_{23}].                              \tag{25}
\]
The special ideal is exactly (12). Coprimeness with \(q\) proves
properness of every fiber and the same complete-intersection argument
as for (21) proves saturation and flatness. This is a genuine transfer
of residual multiplicity onto \(C\), in every characteristic.

It also shows why extracting the residual cycle need not commute with
specialization. For \(h\ne0\) that cycle contains \(3H_h\), whose
limit is \(3C\); after specialization this term belongs to the marked
multiplicity of \(C\), rather than to the residual cycle. The example
leaves the twelvefold line and proves no iteration to sole support.

## 4. The Hilbert-scheme limit remembers relations between equations

The torus acts on the Hilbert scheme of curves with the complete-
intersection Hilbert polynomial. Taking a limit there means
specializing the **saturated ideal and all its relations**, not
independently taking extreme terms of two chosen equations.
Consequently a flat limit of a complete intersection can have more
than two minimal generators, even while its Hilbert polynomial stays
unchanged. The following determinantal family exhibits this
phenomenon explicitly; its degree-ten generator is the algebraic
trace of a relation that survives the limit.

Extra initial generators can occur in higher degree as well. Put
\[
 B_3=x_0x_2^2-x_1^2x_3,\quad
 a_6=x_0^2x_3A,\quad b_4=x_0^3x_2,
\]
and take
\[
 F=q^3+a_6,\qquad G=q^3+x_0^2x_1B_3.
\]
The identity \(G-F=-b_4q\) identifies the original proper ideal with
\[
 (q^3+a_6,b_4q).                                    \tag{26}
\]
A full torus family is
\[
 J=(q^3+h^5a_6,\ b_4q,\ a_6b_4).                    \tag{27}
\]
For \(h\ne0\) the third generator is redundant, because
\[
 b_4(q^3+h^5a_6)-q^2(b_4q)=h^5a_6b_4.
\]
Its three generators are the maximal minors, up to signs, of
\[
 \begin{pmatrix}
 b_4&0\\ -q^2&a_6\\ -h^5&-q
 \end{pmatrix}.                                    \tag{28}
\]
The height is two, and every fiber has height two: off zero this is
the proper pair (26), while at zero \(q\nmid a_6b_4\) excludes a
common divisor of all generators. The Hilbert–Burch determinantal ideal
is therefore perfect and Cohen–Macaulay. Every \(h-h_0\) is regular,
since adding it raises the height to three; hence the family is flat
over \(k[h]\), is \(h\)-saturated, and gives the full initial ideal
\[
 I_0=(q^3,b_4q,a_6b_4).                              \tag{29}
\]
The degree-ten generator is minimal: the two degree-six generators are
divisible by \(q\), whereas \(a_6b_4\) is not. Thus (29) is not a
complete intersection. Its minimal syzygy degrees are ten and twelve,
read from (28) at \(h=0\), and its Hilbert numerator is nevertheless
\[
 1-2z^6-z^{10}+z^{10}+z^{12}=(1-z^6)^2.              \tag{30}
\]
The limit retains the complete-intersection Hilbert series, without
retaining two generators. Raw initial forms do not capture (29).

### 4.1 How the boundary cycle changes in the full limit

The original cycle of (26) is
\[
 [C]+13[L_{23}]+13[L_{13}]+2[L_{01}]+[L_{02}]+[T],    \tag{31}
\]
where \(T=V(x_2,x_0x_3^2-x_1^3)\) is an irreducible plane cubic.
Here is a direct derivation. In the hypersurface \(F=0\), intersection
with \(b_4q\) is the sum of intersection with \(q\) and with \(b_4\),
counting scheme multiplicity. On \(Q\),
\[
 a_6|_Q=a^4bc^2dD,\qquad b_4|_Q=a^3bc^4.             \tag{32}
\]
Thus intersection with \(q\) contributes
\(C+4L_{23}+L_{01}+2L_{13}+L_{02}\).
For the other contribution, \(b_4=x_0^3x_2\). On \(x_0=0\),
\(F=-x_1^3x_2^3\); multiplied by the exponent three of \(x_0\),
this contributes \(9L_{23}+9L_{13}\). On \(x_2=0\),
\[
 F=x_0^2x_3(x_0x_3^2-x_1^3),
\]
which contributes \(2L_{13}+L_{01}+T\). Adding gives (31).
All these factorizations and multiplicities are characteristic free.

The special cycle is
\[
 [C]+13[L_{23}]+14[L_{13}]+4[L_{01}]+[L_{02}].        \tag{33}
\]
One check is the full divisor limit
\(T\rightsquigarrow L_{13}+2L_{01}\), because the maximal-weight
term of its cubic equation is \(x_0x_3^2\). An independent ideal check
uses the exact colon sequence for multiplication by \(q\):
\[
 I_0:q=(q^2,b_4),\qquad I_0+(q)=(q,a_6b_4).
\]
The colon identity follows from coprimeness of \(q\) and \(a_6b_4\).
At any generic component of their divisor on \(Q\), the two terms in
the colon sequence give respectively \(2\operatorname{ord}(b_4|_Q)\)
and \(\operatorname{ord}(a_6|_Q)+\operatorname{ord}(b_4|_Q)\).
The total multiplicity is therefore
\[
 \operatorname{ord}(a_6|_Q)+3\operatorname{ord}(b_4|_Q).
\]
Inserting (32) yields (33), including the coefficient one on \(C\).
Both (26) and (29) restrict on the dense torus to the reduced curve
\(C\cap T_{\mathrm{dense}}\), so their finite quotient is just \(k\).
It misses boundary degree 32, and it cannot distinguish the cycles
(31) and (33), much less their full ideals.

## 5. The geometry of invariant curve strata

A reduced irreducible invariant curve meeting the dense coordinate torus
is a single orbit closure and hence a quartic of the form (2). More
generally an orbit with nonzero coordinate index set \(J\), containing
at least two indices, has degree
\[
 \frac{\max_{j\in J}w_j-\min_{j\in J}w_j}
 {\gcd\{w_i-w_j:i,j\in J\}},\qquad w=(0,1,3,4).     \tag{34}
\]
Indeed divide the exponent differences by their gcd to obtain the
primitive monomial parametrization. A general hyperplane cuts its
Laurent polynomial in exactly the exponent width, after that division;
the primitive parametrization has degree one onto its image. This is
valid in positive characteristic as well, with inseparable stabilizer
degree included by the gcd before passing to the image.

Thus invariant reduced curves can also be coordinate boundary lines or
cubics; their presence cannot be read from dense-torus points alone.
For example the three-coordinate sets of weights \(\{0,1,3\}\) and
\(\{1,3,4\}\) have degree three. A noninvariant residual curve is not
classified by (34). The smooth curves \(H,K\) above already show that
such residual curves can avoid both endpoints while their full limits
become unions of coordinate lines. Taking limits of individual points
records attraction to fixed points; it does not compute these flat
curve limits or their multiplicities.

## 6. From invariant examples to the supported-CI Hilbert locus

The correct ambient question is not whether the original two sextics
can be chosen as eigenforms. Every hypothetical sole-supported
complete intersection has a \(T\)-fixed **full flat limit** with the
same Hilbert polynomial and sole reduced support \(C\), but that
limit need not be generated by two equations. The examples in this
chapter mostly have residual curves, so they demonstrate mechanisms
rather than supply a candidate sole-supported fixed point.

To turn the invariant viewpoint into an obstruction, one must
understand which fixed supported ideals lie in the closure of the
supported complete-intersection locus. Actual sextic source spaces
and conormal restrictions are essential inputs to that question,
not optional coordinate refinements.

The unrestricted characteristic-zero STCI question remains open. These
examples concern actual proper intersections containing \(C\), including
residual support, rather than defining pairs with sole reduced support.
There are two useful links to the established sextic investigation.

First, the full degree-six polynomial source consists of the 84 ambient
monomials. In the torus coordinates above write each such monomial as
\(t^w u^i v^j\), with constant coefficient \(c_{w,i,j}\). Vanishing
to order at least two along \(C\) is equivalent, separately in every
integer weight, to
\[
 \sum_{i,j}c_{w,i,j}=0,\qquad
 \sum_{i,j}i c_{w,i,j}=0,\qquad
 \sum_{i,j}j c_{w,i,j}=0.                            \tag{35}
\]
These are the value and two first normal coefficient conditions at
\((u,v)=(1,1)\). They define a global sheaf-power condition: the first
infinitesimal neighborhood has a filtration with locally free quotients
on \(C\), so a section vanishing on its dense open vanishes everywhere.
No endpoint torsion is discarded.
The weight dimensions in weights six through eighteen are
\[
 (1,1,2,2,2,2,3,2,2,2,2,1,1),
\]
with total 23. This is an explicit coefficient presentation of the
already reviewed characteristic-free source
\(H^0(\mathcal I_C^2(6))\), not a new ambient classification; its
full proof and higher-degree formulas are owned by
[actual homogeneous equation spaces](../supplements/ACTUAL_EQUATION_SPACES.md).
The verifier supplies a finite implementation check of (35).

The familiar equations become
\[
 q=t^4(v-u),\quad A=t^3(u-1),\quad
 B_3=t^6(u^2-v),\quad D_3=t^9(u^3-v^2),
 \qquad D_3=x_2^3-x_1x_3^2.
\]
On \(Q\), where \(v=u\), every degree-six double section restricts
in this chart to
\[
 t^6(u-1)^2R(t^3u),\qquad \deg R\le4.                \tag{36}
\]
This is the actual divisor restriction \(D^2\) times a section of
\(\mathcal O_Q(4,0)\). It links quotient coefficients to a global
quadric linear system; it does not make higher embedded lifts automatic.
The [actual-source rank and unique-lift account](rank_strata_and_sextic_lifts.md)
retains the additional cubic matching conditions and its own reviewed
characteristic-zero hypotheses.

Second, the existing [sole-support sextic reduction](../supplements/SEXTIC_PAIR_REDUCTION.md)
is independently reviewed provisional evidence in characteristic zero or
\(p\ge7\). For **every** proper \((6,6)\) pair with reduced support
\(C\), its proof obtains generic curvilinear length nine and the full
necessary divisor profiles. Neither statement is reproved here or
inferred from a constant quotient algebra. In particular the length-six
noncurvilinear example (13) has residual support and contradicts none of
those conclusions. Their proof uses the global quadric restriction,
the balanced-normal-bundle graph bound and actual saturated duality,
not just the finite quotient.

Finally, the endpoint Smith orders three and four in the companion are
characteristic free. They do not determine the conormal splitting:
[R-0020](../results/quartic_conormal_characteristic_jump.md) proves the
actual characteristic-two jump from \(\mathcal O(-7)^2\) to
\(\mathcal O(-8)\oplus\mathcal O(-6)\) through its extension class.
Endpoint lattice orders, quotient lengths, full projective ideals and
conormal extension classes retain different information. No comparison
proved here identifies them or excludes all mixed sextic pairs.

## 7. Parameter spaces: pencils, fixed loci, and deformation strata

A Grassmannian of equation pencils and a Hilbert scheme of their
intersection schemes answer different geometric questions. The former
retains a chosen two-dimensional space of equations; the latter
retains the full ideal through degeneration. The dimension counts
below locate specific linear conditions on pencils, but do not
compute codimensions of arbitrary Hilbert-scheme boundary strata
or of all increased-multiplicity loci.

For equal degrees the symmetric space of pencils is
\(\operatorname{Gr}(2,H^0(\mathcal I_C(d)))\). Since the embedded quartic
has Hilbert function \(4d+1\) for \(d\ge2\),
\[
 h^0(\mathcal I_C(4))=18,\qquad h^0(\mathcal I_C(6))=59.
\]
The two Grassmannians therefore have dimensions 32 and 114, respectively.
The 23-dimensional double-sextic source cuts out the closed sub-Grassmannian
\(\operatorname{Gr}(2,23)\), of dimension 42 and codimension 72 in
\(\operatorname{Gr}(2,59)\). This is exactly the condition that the entire
pencil consists of double sextics. It is not a computation of the
codimension of every locus with increased generic multiplicity along \(C\):
dependence of first normal symbols over \(k(C)\) need not come from a
constant linear combination of the two equations.

The existing [quartic root pencil](root_pencil_geometry.md#3-three-ways-the-pencil-leaves-the-open-arrangement)
has polynomial \(z^4-\eta z+\eta-1\) and discriminant
\[
 (\eta-4)^2(-27\eta^2+40\eta-16)
\]
in characteristic zero. Its marked-root collision, residual-root collision,
root escaping the quotient torus at \(\eta=1\), and boundary at
\(\eta=\infty\) are different codimension-one events in that parameter line.
The root at zero is separable, so the discriminant does not detect that
embedded boundary. These slice calculations give no ambient classification
or codimension of general conductor, quotient-type or residual strata.

**Independent review.** Reconstruction checked the explicit endpoint
and primary calculations, the all-characteristic eigenpair argument,
the full-family saturation and determinantal limit, and both derivations
of the special cycle multiplicities. The finite verifier checks the
stated arithmetic and polynomial identities separately. The inherited source-space,
sole-support reduction and conormal results retain their linked review
and canonical status. This text introduces no canonical promotion and
no new all-pair STCI conclusion.
