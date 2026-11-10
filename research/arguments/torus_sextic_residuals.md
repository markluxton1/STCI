---
id: STCI-A-0002
type: argument
title: Sextic orbit quotients, residual curves, and full torus limits
status: complete
scope: "#scope"
conclusion: "#conclusion"
---
# Sextic orbit quotients, residual curves, and full torus limits

## Scope

Let \(k\) be algebraically closed, \(S=k[x_0,x_1,x_2,x_3]\), and

\[
C=[s^4:s^3t:st^3:t^4],\qquad
\lambda\cdot x=(x_0,\lambda x_1,\lambda^3x_2,\lambda^4x_3).
\]

Weights always mean integer characters of the algebraic torus, in every
characteristic. Write \(L_{ij}\) for the coordinate line with nonzero
coordinates allowed only in positions \(i,j\), and write

\[
q=x_0x_3-x_1x_2,\quad A=x_0^2x_2-x_1^3,\quad
B_3=x_0x_2^2-x_1^2x_3.
\]

All proper sextic pairs below have degree 36, Hilbert series

\[
\frac{(1-z^6)^2}{(1-z)^4},\qquad P(n)=36n-144.
\]

They are complete intersections and therefore saturated, Cohen–Macaulay,
and without embedded associated components. A flat limit need not remain
a complete intersection. The statements proved here are
[R-0042](../results/eigenform_trace_obstruction.md),
[R-0043](../results/sextic_eigenpair_quotient_bound.md),
[R-0044](../results/local_residual_multiplicity.md),
[R-0045](../results/colon_divisor_cycle.md),
[R-0046](../results/sextic_three_generator_full_limit.md),
[R-0047](../results/sextic_eigenpair_residual_controls.md),
[R-0048](../results/moving_sextic_residual_limit.md),
[R-0049](../results/sextic_residual_absorption.md), and
[R-0050](../results/torus_orbit_curve_degree.md). These nine proof routes have independent acceptance within their stated scopes. Characteristic-zero sole support, arbitrary mixed-weight
sextic pairs, and the supported Hilbert locus are not classified here.

## Orbit curves and finite quotient degree

For any coordinate index set \(J\) with at least two elements, take a
point whose nonzero coordinates have exactly this index set. Put

\[
d_J=\gcd\{w_i-w_j:i,j\in J\},\qquad
D_J=\frac{\max_{j\in J}w_j-\min_{j\in J}w_j}{d_J},
\quad w=(0,1,3,4).
\]

The orbit closure is an irreducible rational monomial curve of degree

\[
\deg \overline{T\cdot x}=D_J.                     \tag{1}
\]

Indeed subtract the least exponent and divide all exponent differences
by \(d_J\). The resulting nonnegative integers have gcd one and range
from zero to \(D_J\). Their monomials give a basepoint-free map from
\(\mathbf P^1\) with pullback of \(\mathcal O(1)\) equal to
\(\mathcal O(D_J)\). Its function field is \(k(t)\), because the gcd
of the exponent differences is one: Bezout combinations of the Laurent
monomials recover \(t\). The map is therefore birational onto the image,
so the image degree is \(D_J\). This proof is valid in positive
characteristic. Dividing by the integer gcd removes the degree of the
original orbit parameter map, including its inseparable part.

An invariant reduced irreducible curve meeting the dense coordinate
torus is one orbit closure. In fact each orbit there has dimension one,
and an orbit through any point of an irreducible invariant curve is a
dense open subset. On that torus write

\[
x=(1,t,t^3u,t^4v),\qquad t,u,v\in k^\times.
\]

The torus acts only on \(t\). If two homogeneous eigenforms restrict to

\[
t^r f(u,v),\qquad t^s g(u,v),
\]

their common zero scheme on the dense torus is

\[
\operatorname{Spec}B\times\mathbf G_m,\qquad
B=k[u^{\pm1},v^{\pm1}]/(f,g).                     \tag{2}
\]

For a proper projective pair \(B\) is finite dimensional, possibly zero:
a positive-dimensional quotient would give a surface component on the
dense torus. For a quotient point \((\epsilon,\zeta)\), the closure is

\[
C_{\epsilon,\zeta}
=[s^4:s^3t:\epsilon st^3:\zeta t^4].              \tag{3}
\]

It is a smooth quartic: it is a diagonal translate of \(C\); alternatively
its endpoint parameters have first powers \(t/s\) and \(s/t\). Its only
coordinate-boundary points are

\[
p_0=[1:0:0:0],\qquad p_\infty=[0:0:0:1].
\]

Localizing (2) at the generic point of this orbit extends the local
Artin quotient factor by the field \(k(t)\). Thus its generic
multiplicity is the length of that factor. If \(n=\dim_kB\), the
fundamental cycle of the components meeting the dense torus has degree

\[
4n.                                                \tag{4}
\]

The quotient does not record components lying entirely on the coordinate
boundary, their attachment, or their scheme structures.

## Trace obstruction for supported pairs

First suppose \(F,G\in S\) are ordinary homogeneous of positive degrees
\(a,b\), with reduced projective zero locus \(C\), and satisfy

\[
F\equiv x_1^a\pmod{x_0^2},\qquad
G\equiv x_2^b\pmod{x_3^2}.                       \tag{5}
\]

No weight assumption is required for this paragraph. Put \(X=x_1\),
\(Y=x_2\), \(A_0=k[x_0,x_3]\), and \(E=S/(F,G)\). The pair has no
common factor, since otherwise it would have a surface component.
It is a regular sequence. Modulo \((x_0,x_3)\), its quotient is
\(k[X,Y]/(X^a,Y^b)\). The monomials

\[
X^iY^j,\qquad 0\le i<a,\quad 0\le j<b            \tag{6}
\]

generate \(E\) over \(A_0\). For completeness, reduce a homogeneous
element modulo \((x_0,x_3)\); subtract its expression in (6); and express
the remainder as \(x_0e_0+x_3e_3\), with smaller ordinary degrees.
Induction proves generation. The free graded \(A_0\)-module on (6)
has Hilbert series

\[
\frac{\sum_{i<a,j<b}z^{i+j}}{(1-z)^2}
=\frac{(1-z^a)(1-z^b)}{(1-z)^4},
\]

which is the regular-sequence Hilbert series of \(E\). Its surjection
onto \(E\) is consequently an isomorphism degree by degree. Thus \(E\)
is finite free of rank \(ab\) over \(A_0\).

The affine cones have the same reduced support, including the origin,
so \(XY-x_0x_3\) is nilpotent in \(E\). After extending to the fraction
field of \(A_0\), its multiplication operator is nilpotent, with zero
trace. Since \(A_0\) injects into that field, the trace already vanishes
over \(A_0\), giving

\[
\operatorname{Tr}_{E/A_0}(XY)=ab\,x_0x_3.          \tag{7}
\]

Trace of a finite free endomorphism commutes with base change. Over
\(\overline A_0=A_0/(x_0^2,x_3^2)\), (5) identifies \(E\) with
\(\overline A_0[X,Y]/(X^a,Y^b)\). Multiplication by \(XY\) has zero
diagonal in (6), and hence zero trace. Reducing (7) therefore gives
\(ab\,x_0x_3=0\) in \(\overline A_0\). The element \(x_0x_3\) is
nonzero there. Consequently

\[
ab=0\text{ in }k.                                  \tag{8}
\]

Now assume both equations are eigenforms for the integer weights.
The points \(e_1=[0:1:0:0]\), \(e_2=[0:0:1:0]\) lie outside \(C\).
At each point one equation is nonzero. An eigenform of positive ordinary
degree \(d\) cannot be nonzero at both points, because \(x_1^d\) and
\(x_2^d\) have distinct integer weights \(d,3d\). Exchange and rescale
the equations so that \(F\) contains \(x_1^a\) with coefficient one and
has weight \(a\), while \(G\) contains \(x_2^b\) with coefficient one
and has weight \(3b\). Ordinary degree and weight give, for a monomial
in \(F\),

\[
e_0=2e_2+3e_3.
\]

Every monomial except \(x_1^a\) is therefore divisible by \(x_0^2\).
Similarly every monomial in \(G\) except \(x_2^b\) has
\(e_3=3e_0+2e_1\ge2\). This proves (5), and hence (8).

It remains to allow just one eigenform \(F\), with arbitrary homogeneous
mate \(G\). Factor \(F=c\prod H_j^{r_j}\), with irreducible factors of
degrees \(a_j\). For a nonzero element of a graded domain, define its
width as its greatest minus least occurring weight. Extreme weight
components multiply without cancellation, so widths add. Every factor
\(H_j\) is an eigenform because \(F\) has width zero. Each pair
\((H_j,G)\) is proper and its support is \(C\): its intersection has a
curve component, lies in the irreducible curve \(C\), and can have no
surface component. In particular \(H_j\) contains \(C\).

In the weight-graded domain \(S/(H_j)\), let \(g\ne0\) be the image of
\(G\). Its principal radical is the homogeneous prime of \(C\) in that
domain. Each nonzero weight component \(g_w\) therefore belongs to
\(\sqrt{(g)}\), so \(g_w^N=gh\) for some \(N>0\) and \(h\ne0\).
Width additivity forces \(g\) to have width zero. The corresponding
ordinary degree-\(b\) weight component \(G_j\) of \(G\) thus satisfies

\[
(H_j,G_j)=(H_j,G).
\]

Applying the two-eigenform proof yields \(a_jb=0\) in \(k\). Multiplying
by \(r_j\) and summing gives \(ab=0\). In characteristic zero a supported
pair with one eigenform is impossible. In characteristic \(p>0\),

\[
p\mid ab,\qquad \max(a,b)\ge p.                  \tag{9}
\]

For odd \(p\), the degree identity \(ab=4m_C\) also gives \(p\mid m_C\)
and \(ab\ge4p\). In characteristic two (8) gives no parity assertion
for \(m_C\). If an equation only has a nonconstant eigenform factor,
applying the argument to that factor and the mate still gives
\(\max(a,b)\ge p\); divisibility for the original degree product is
not implied by this weaker hypothesis.

This is a complete trace proof for the stated source, not a reduction
of arbitrary pairs to that source. The large-prime sharp attainment
using an external positive-characteristic construction is outside this
proof closure and is not asserted as a reconstructed Result here.

## The sharp sextic eigenpair bound

Let \(F,G\) be any proper sextic eigenpair; containing \(C\) is not
required. Equations (2)–(4) give \(4n\le36\), so \(n\le9\).
Suppose \(n=9\). All degree is accounted for by orbit closures (3).
A proper complete intersection is pure with no embedded associated
components. Its support is therefore exactly the union of those orbit
closures; there can be no isolated boundary point or boundary curve.
In particular it misses \(e_1,e_2\).

One equation must have a nonzero \(x_1^6\) coefficient and one a nonzero
\(x_2^6\) coefficient. Their weights six and eighteen are distinct, so
they occur in different eigenforms, whose weights are precisely six
and eighteen. A degree-six monomial surviving on \(L_{03}\) has weight
divisible by four. Neither six nor eighteen is divisible by four.
Both equations vanish on \(L_{03}\), contradicting the absence of a
boundary curve. Thus

\[
n\le8,\qquad \deg(\text{boundary cycle})=36-4n\ge4. \tag{10}
\]

The pair \(I_8\), proved proper with quotient length eight in R-0047
and in the eigenpair controls below, attains the bound in every
characteristic. The proof uses integer
characters, not weights reduced modulo the characteristic. It concerns
actual two-eigenform pairs, not full limits that may need extra generators.

## Local multiplicity and binomial certificates

Let \(R\) be a regular local ring of dimension two, \(q\in R\) such
that \(R/(q)\) is a discrete valuation ring, and \(f\in R\) with
\(0<\operatorname{ord}_{R/(q)}(\bar f)=d<\infty\). Then for every
\(r\ge1\),

\[
\ell_R R/(f,q^r)=rd.                              \tag{11}
\]

Indeed \(q,f\) is a system of parameters. It is a regular sequence in
the regular local ring. Hence \(R/(f)\) is one-dimensional
Cohen–Macaulay and multiplication by \(q\) is injective there. Its
\(q\)-power filtration has \(r\) successive quotients isomorphic to
\(R/(f,q)\), of length \(d\), proving (11). Geometrically this computes
the multiplicity along a divisor of the smooth surface \(V(q)\) when
that surface is replaced by its \(r\)-fold hypersurface thickening.

Two local binomial certificates used below are valid over any field
\(K\), for any \(\gamma,\delta\in K^\times\), in
\(K[a,b]_{(a,b)}\):

\[
(a^6-b^2,b^6-\gamma a^2)=(a^2,b^2),\qquad \ell=4, \tag{12}
\]

\[
(\delta a^3-b^3,b^6-a^4)=(a^4,b^3-\delta a^3),
\qquad \ell=12.                                  \tag{13}
\]

For (12), modulo \(b^2-a^6\) the second generator is
\(a^2(a^{16}-\gamma)\). Its second factor is a unit, giving \(a^2\),
then \(b^2\). The reverse inclusion follows directly. For (13), modulo
\(b^3-\delta a^3\), the second generator is
\(a^4(\delta^2a^2-1)\), again with a unit factor. The quotient is free
of rank three over \(K[a]/(a^4)\), with basis \(1,b,b^2\); its length
is twelve. This is an exact local algebra proof replacing the source's
coprime lowest-form calculation of the same multiplicity. It remains
a geometric reduction with necessary algebra, not an intrinsic
replacement proof of a broader statement.

## A colon formula for divisor cycles

Let \(q\in S\) be irreducible homogeneous, let \(a,b\in S\) be
homogeneous with \(q\nmid ab\), and let \(r\ge1\). Put

\[
I=(q^r,bq,ab).
\]

Primality of \(q\) gives

\[
I:q=(q^{r-1},b),\qquad I+(q)=(q,ab).             \tag{14}
\]

In fact if \(qf=q^ru+bqv+abw\), then \(q\mid w\), because
\(q\nmid ab\). After dividing by \(q\), the last term is a multiple
of \(b\); this proves the nontrivial inclusion in the colon equality.
The reverse inclusion is immediate. Consequently there is an exact
graded sequence

\[
0\longrightarrow S/(q^{r-1},b)(-\deg q)
\xrightarrow{\ q\ } S/I
\longrightarrow S/(q,ab)\longrightarrow0.        \tag{15}
\]

For \(r=1\) the first module is zero. Suppose \(Q=V(q)\subset\mathbf
P^3\) is smooth, and let \(E\) be an irreducible divisor in the support
of \(a|_Q\,b|_Q\). At its generic point the ambient ring is regular
local of dimension two and \(R/(q)\) is a DVR. Localizing (15), then
using (11), shows that the generic length of \(S/I\) along \(E\) is

\[
\operatorname{ord}_E(a|_Q)+r\operatorname{ord}_E(b|_Q). \tag{16}
\]

Thus the fundamental cycle is the divisor cycle
\(\operatorname{div}_Q(a|_Q)+r\operatorname{div}_Q(b|_Q)\).
This formula identifies cycles; it asserts neither that arbitrary such
ideals are saturated nor that cycles determine their endpoint schemes.

## Eigenpair residual controls

The first eigenpair is

\[
I_8=(x_1^6-x_0^4x_2^2,\ x_2^6-x_1^2x_3^4).       \tag{17}
\]

Its quotient is \(B_8=k[u^{\pm1},v^{\pm1}]/(u^2-1,v^4-1)\), of
length eight: the raw second relation \(u^6-v^4\) reduces using \(u^2=1\).
Its torus part is finite, and inspection on coordinate hyperplanes shows
that its only boundary curve is \(L_{03}\). Thus the pair is proper.
At the generic point of \(L_{03}\), put \(x_0=1,x_3=z,x_1=a,x_2=b\).
The local ideal is (12) with \(\gamma=z^4\). It has length four.
The global \(L_{03}\)-primary component is exactly \((x_1^2,x_2^2)\):
this ideal is primary, its localization is the computed local ideal,
and contraction from that localization preserves it. The other primary
components are contractions of the local factors of the torus
saturation. There are no embedded associated components.

If \(\operatorname{char}k\ne2\), the cycle is

\[
\sum_{\epsilon^2=1,\,\zeta^4=1}[C_{\epsilon,\zeta}]
+4[L_{03}].                                        \tag{18}
\]

In characteristic two, \(B_8\simeq k[\alpha,\beta]/(\alpha^2,\beta^4)\)
is supported at \((1,1)\), so the cycle is \(8[C]+4[L_{03}]\). This
length-eight quotient is not curvilinear. Literal endpoint equations
in the charts \(x_0=1\), \(x_3=1\), respectively, are

\[
(y^2-t^6,\ t^2(t^{16}-z^4)),\qquad
(b^2-c^6,\ c^2(c^{16}-a^4)).                     \tag{19}
\]

The second eigenpair is

\[
I_6=((x_0x_3)^3-(x_1x_2)^3,\ x_1^6-x_0^4x_2^2).  \tag{20}
\]

Its quotient

\[
B_6=k[u^{\pm1},v^{\pm1}]/(u^2-1,v^3-u^3)
\]

has length six. Away from characteristics two and three it has six
simple points \((\epsilon,\epsilon\omega)\), with \(\epsilon^2=1\),
\(\omega^3=1\). In characteristic three the two points \((1,1)\),
\((-1,-1)\) each have length three; in characteristic two the three
points \((1,\omega)\) each have length two. The only boundary curve is
\(L_{23}\). Its generic local equations, with \(x_2=1,x_3=z,x_0=a,x_1=b\),
are (13) with \(\delta=z^3\), so its multiplicity is twelve. These
computations prove properness and give the full cycle: six simple,
two triple, or three double quartics, respectively, plus \(12[L_{23}]\).
The exact endpoint chart ideals are

\[
(z^3-t^3y^3,t^6-y^2),\qquad
(a^3-b^3c^3,b^6-a^4c^2).                         \tag{21}
\]

For the third control use the Segre isomorphism

\[
Q=V(q)\simeq\mathbf P^1\times\mathbf P^1,\quad
x=(ac,ad,bc,bd),\quad D=bc^3-ad^3.               \tag{22}
\]

Here \(C=V_Q(D)\) has type \((1,3)\) and \(A|_Q=a^2D\). The eigenpair

\[
I_{\rm th}=(q^3,A^2)                              \tag{23}
\]

is proper; its quotient is the length-six local algebra

\[
k[u^{\pm1},v^{\pm1}]/((v-u)^3,(u-1)^2).
\]

It has embedding dimension two in every characteristic. On \(Q\), the
divisor of \(A^2\) is \(2C+4\{a=0\}\), and \(\{a=0\}=L_{23}\).
The multiplicity rule (11) proves

\[
[V(I_{\rm th})]=6[C]+12[L_{23}].                  \tag{24}
\]

Thus quotient length alone distinguishes neither curvilinearity nor
boundary attachment. The exact global ideal (23), rather than the cycle,
specifies its endpoint schemes. These examples are invariant ideals, so
their full weight limits are themselves.

## Moving residual curves and their full limit

Put

\[
r_{\rm lo}=x_0^3x_2-x_0x_1^3,\quad
r_{\rm hi}=x_2^3x_3-x_1x_3^3,\quad
G=(x_0+x_3)^2(r_{\rm lo}+r_{\rm hi}),\quad F=q^3+G.
\]

Their ideal is \((q^3,G)\). On \(Q\),

\[
G|_Q=(ac+bd)^2D(a^3c+b^3d).
\]

It is nonzero, proving properness. The residual curves

\[
H=V_Q(a^3c+b^3d),\quad K=V_Q(ac+bd)
\]

are smooth rational graphs of types \((3,1)\), \((1,1)\), and degrees
four and two. The coefficient pairs of their equations in \(c,d\)
have no common zero, so their projections to the first factor are
isomorphisms, including in positive characteristic. Formula (11) gives

\[
[V(F,G)]=3[C]+3[H]+6[K].                          \tag{25}
\]

Both residual curves avoid \(p_0,p_\infty\). In characteristic zero their
attachments to \(C\), under \((a,b,c,d)=(s^3,t^3,s,t)\), are the reduced,
disjoint divisors \(s^{10}+t^{10}=0\), \(s^4+t^4=0\). Reducedness follows
by differentiating on either affine chart. For disjointness, a common
nonzero ratio \(\rho=s/t\) would give \(\rho^{10}=\rho^4=-1\), hence
\(\rho^2=-1\) and \(\rho^4=1\), a contradiction in characteristic zero.
At either endpoint \(G|_Q\) is a unit times \(D\). Since \(C\subset
V(G)\), this says \(q,G\) are regular local coordinates normal to \(C\)
there. The endpoint ideal is locally a pure triple structure
\((q^3,G)\), equivalent after choosing a local lift of \(D\) to
\((q^3,D)\).

Use the maximal-weight initial convention
\(f\mapsto h^{\max w(f)}f(x_0,h^{-1}x_1,h^{-3}x_2,h^{-4}x_3)\).
The full family is

\[
\mathcal J_h=\bigl(q^3,(x_3+h^4x_0)^2
                    (r_{\rm hi}+h^{10}r_{\rm lo})\bigr).          \tag{26}
\]

The two generators are coprime in every fiber: their restrictions to
\(Q\) have nonzero product of the displayed factors. The total
regular-sequence quotient is Cohen–Macaulay, and every \(h-c\) raises
the ideal's height by one, so every \(h-c\) is a nonzerodivisor. Over
the PID \(k[h]\), the quotient is torsion free and flat. It is also
\(h\)-saturated; its localization at \(h\ne0\) is the torus translate,
so it is the contraction of that translated ideal. Every fiber is a
graded complete intersection of dimension two, hence saturated.
Thus (26) is the full homogeneous and saturated projective limit, not
merely an equation-wise limit. At zero it is

\[
(q^3,x_3^3(x_2^3-x_1x_3^2)).                     \tag{27}
\]

On \(Q\), \(r_{\rm hi}=b^3dD\), \(x_3=bd\), so the divisor is
\(C+5\{b=0\}+3\{d=0\}\). Here \(\{b=0\}=L_{01}\),
\(\{d=0\}=L_{02}\). Its cycle is therefore

\[
3[C]+15[L_{01}]+9[L_{02}].                        \tag{28}
\]

Separately \(H\rightsquigarrow3\{b=0\}+\{d=0\}\) and
\(K\rightsquigarrow\{b=0\}+\{d=0\}\). The two original chosen sextic
equations \(F,G\) have equal maximal-weight forms; their difference
\(F-G=q^3\) supplies the missing degree-six relation. The example shows
movement of full residual divisors, rather than point attraction.

## Residual absorption in a proper flat family

Consider

\[
\mathcal K_h=(q^3,A(A+h^3x_0^3)).                 \tag{29}
\]

On \(Q\) its second equation is \(a^4D(D+h^3ac^3)\), never identically
zero. Thus every fiber is a proper sextic complete intersection. The
regular-sequence argument just used proves flatness and saturation.
It is also the maximal-weight torus family of the fiber at \(h=1\),
because \(A\) has weight three and \(x_0^3\) weight zero.
For \(h\ne0\),

\[
H_h=V_Q(D+h^3ac^3)
\]

is a smooth graph of type \((1,3)\), distinct from \(C\): the coefficient
pair in \(a,b\) is \((-d^3+h^3c^3,c^3)\), with no common zero. The
divisor on \(Q\) is \(4\{a=0\}+C+H_h\). At zero it is
\(4\{a=0\}+2C\). Applying (11) gives

\[
[Z_h]=3[C]+3[H_h]+12[L_{23}]\quad(h\ne0),\qquad
[Z_0]=6[C]+12[L_{23}].                            \tag{30}
\]

This is characteristic free. The residual term \(3H_h\) specializes
to \(3C\) and becomes part of the marked multiplicity. Hence extracting
the residual cycle relative to \(C\) does not commute with specialization.
The twelvefold residual line survives; no iteration to sole support is
proved.

## The saturated three-generator full limit

Set

\[
a_6=x_0^2x_3A,\qquad b_4=x_0^3x_2,\qquad
F=q^3+a_6,\qquad G=q^3+x_0^2x_1B_3.
\]

The exact identity

\[
G-F=-b_4q
\]

identifies \((F,G)\) with \((q^3+a_6,b_4q)\). This pair is proper:
\(q\nmid a_6\), while neither \(x_0\) nor \(x_2\), the factors of
\(b_4\), divides \(F\). Indeed

\[
F|_{x_0=0}=-x_1^3x_2^3,\qquad
F|_{x_2=0}=x_0^2x_3(x_0x_3^2-x_1^3).
\]

The maximal-weight family is

\[
\mathcal I=(q^3+h^5a_6,\ b_4q,\ a_6b_4)\subset S[h].            \tag{31}
\]

For \(h\ne0\) its third generator is redundant by the identity

\[
b_4(q^3+h^5a_6)-q^2(b_4q)=h^5a_6b_4.             \tag{32}
\]

These three generators, up to signs, are the maximal minors of

\[
M_h=\begin{pmatrix}
b_4&0\\-q^2&a_6\\-h^5&-q
\end{pmatrix}.                                  \tag{33}
\]

Every fiber has height two. For nonzero \(h=c\), the same properness
check as above applies to \(q^3+c^5a_6,b_4q\). At \(h=0\), any common
irreducible divisor of the three generators would divide \(q\) and
\(a_6b_4\), which is impossible. The ideal is contained in a prime of
height two over \((q,a_6b_4)\), so its height is exactly two. Over
\(S[h]\) its height is also two: the generic fiber has height two and
there is no common divisor of all minors. The Hilbert–Burch theorem
for a height-two ideal of maximal minors gives a perfect
Cohen–Macaulay quotient and its free resolution. Since adjoining
\(h-c\) raises height to three, every \(h-c\) is regular on this
quotient. Thus \(S[h]/\mathcal I\) is torsion free and flat over \(k[h]\),
and \(\mathcal I:h^\infty=\mathcal I\).

Each fiber is a height-two perfect graded ideal in four variables.
Its quotient has dimension and depth two. In particular the zeroth
local cohomology at the irrelevant ideal vanishes, so each fiber is
irrelevant-saturated. Because (31) is \(h\)-saturated and agrees with
the torus translate after inverting \(h\), it is its contraction and
therefore the full weight family. Its special fiber is exactly

\[
I_0=(q^3,b_4q,a_6b_4).                            \tag{34}
\]

At \(h=0\), matrix (33) is minimal in the ordinary homogeneous
grading. The generator degrees are \(6,6,10\), and the two syzygy
degrees are ten and twelve. Explicitly the minimal resolution is

\[
0\longrightarrow S(-10)\oplus S(-12)
\longrightarrow S(-6)^2\oplus S(-10)
\longrightarrow S\longrightarrow S/I_0\longrightarrow0.
\]

The degree-ten generator is indispensable: the degree-six generators
are divisible by \(q\), while \(a_6b_4\) is not. The limit is saturated
and ACM but is not a complete intersection. Its Hilbert series is still

\[
\frac{1-2z^6-z^{10}+z^{10}+z^{12}}{(1-z)^4}
=\frac{(1-z^6)^2}{(1-z)^4}.                       \tag{35}
\]

This is a geometric determinantal proof with necessary explicit
identities (32)–(33). It does not infer generation or saturation from
Hilbert data. Equation initials of two chosen generators, the full
weight initial ideal (34), and the normal-cone initial ideal along \(C\)
are different constructions; no identification with the last is made.

### Cycles and endpoint schemes of the three-generator limit

On \(Q\) in (22),

\[
a_6|_Q=a^4bc^2dD,\qquad b_4|_Q=a^3bc^4.           \tag{36}
\]

For the original pair, intersect in the hypersurface \(F=0\) with
\(b_4q\). Additivity of Cartier divisors there splits its cycle into
intersection with \(q\) and with \(b_4\); neither vanishes identically
on a surface component. The first contribution, by (36), is

\[
C+4L_{23}+L_{01}+2L_{13}+L_{02}.
\]

The factor \(x_0^3\) in \(b_4\) contributes \(9L_{23}+9L_{13}\), from
\(F|_{x_0=0}=-x_1^3x_2^3\). The factor \(x_2\) contributes
\(2L_{13}+L_{01}+T\), where

\[
T=V(x_2,x_0x_3^2-x_1^3).
\]

This plane cubic is irreducible in every characteristic. In fact over
\(k(x_0,x_3)\), the cubic \(X^3-x_0x_3^2\) has no root, since the
\(x_0\)-valuation of a cube is divisible by three; a reducible cubic
over a field has a root. Its primitive polynomial is therefore
irreducible over \(k[x_0,x_3]\) as well. The original cycle is

\[
[C]+13[L_{23}]+13[L_{13}]+2[L_{01}]+[L_{02}]+[T]. \tag{37}
\]

For the limit (34), apply (14)–(16) with \(r=3,a=a_6,b=b_4\):

\[
I_0:q=(q^2,b_4),\qquad I_0+(q)=(q,a_6b_4).
\]

The cycle is \(\operatorname{div}_Q(a_6|_Q)+3\operatorname{div}_Q(b_4|_Q)\),
so (36) gives

\[
[C]+13[L_{23}]+14[L_{13}]+4[L_{01}]+[L_{02}].     \tag{38}
\]

There is also an independent divisor check. The cubic \(T\) specializes
under the maximal-weight convention to

\[
V(x_2,x_0x_3^2),\qquad [T_0]=[L_{13}]+2[L_{01}],
\]

because the term \(x_0x_3^2\) has weight eight, compared with weight
three for \(x_1^3\). This is a proper plane-hypersurface flat family,
and insertion in (37) recovers (38).

Both schemes have multiplicity one along \(C\), with residual degree
32. On the dense torus \(b_4\) and \(x_0^2x_3\) are units, so both
ideals reduce to \((q,A)\). Their dense transverse quotient is the
reduced algebra \(k\), despite their different boundary cycles.

To retain endpoint schemes, here are their exact affine chart ideals,
not just their fundamental cycles. On \(x_0=1\), put
\(t=x_1,y=x_2,z=x_3\), \(Q_0=z-ty\). The original and special ideals
are respectively

\[
(Q_0^3+z(y-t^3),\ yQ_0),\qquad
(Q_0^3,\ yQ_0,\ zy(y-t^3)).                       \tag{39}
\]

On \(x_3=1\), put \(\alpha=x_0,\beta=x_1,\gamma=x_2\),
\(Q_\infty=\alpha-\beta\gamma\), \(E=\alpha^2\gamma-\beta^3\).
The two ideals are

\[
(Q_\infty^3+\alpha^2E,\ \alpha^3\gamma Q_\infty),\qquad
(Q_\infty^3,\ \alpha^3\gamma Q_\infty,\ \alpha^5\gamma E).
                                                               \tag{40}
\]

Localizing these charts at their origins gives the complete endpoint
local schemes. No endpoint algebra or embedded structure is replaced
by quotient length. Both original and special schemes have no embedded
associated components by their Cohen–Macaulay proofs.

## Evidence and preservation

The source
[original sextic residual chapter](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md)
supplies §§1–4.1 and the orbit degree statement in §5. Its §§1.1–1.3
survive in **Eigenpair residual controls**; §2 in **The sharp sextic
eigenpair bound**; §§3–3.2 in **Moving residual curves and their full
limit** and **Residual absorption in a proper flat family**; §§4–4.1
in the last two mathematical sections. The multiplicity and colon
arguments have separate reusable Results. The trace proof and its
congruence/factor qualifications come from the first four substantive
sections of
[weight restrictions](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md).
The later extreme-component/two-weight results, sharp large-prime
attainment, and three/two-weight cancellation control remain in that
source; they are not premises silently imported here.

The exact verifier
[finite polynomial identities](../investigations/torus-residual-controls/verify.py)
checks Segre substitutions, the generator-change identity, matrix minors,
the cancellation relation, Hilbert-numerator arithmetic and degree sums.
The proofs above show why those identities establish their claimed
geometric assertions. The verifier does not certify saturation, flatness,
primary decomposition, all-characteristic coverage, or a general
classification. Those conclusions are proved in the text, without
depending on sampled finite-field ranks. The inherited source-space
and sole-support reductions in the [sextic source-space and pencil account](../synthesis/toric_sextic_residuals_and_limits.md#sextic-source-spaces-and-pencils)
retain their existing proof owners.

## Conclusion

The full torus limit of an actual proper sextic intersection can remain
saturated and ACM with the complete-intersection Hilbert series while
acquiring a minimal degree-ten generator. Its residual degree can stay
32 while its boundary cycle changes. Distinct eigenpair controls show
inseparable quotient collisions and noncurvilinear finite algebras;
other full families move residual divisors to the boundary or transfer
their multiplicity onto \(C\). The sharp quotient-length bound eight
applies to proper sextic eigenpairs, and the trace obstruction applies
to supported pairs with the stated congruences or an eigenform equation.
None of these proves coverage of arbitrary mixed-weight pairs or a
deformation preserving sole support. The characteristic-zero STCI
question remains open.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
on November 4, 2026 accepted all nine reconstructed proof routes,
R-0042 through R-0050, within their stated hypotheses. The reviewer
reconstructed the trace obstruction and arbitrary-mate reduction,
integer-character quotient bound, local filtration and unit-factor
length certificates, colon sequence, graph and divisor arguments,
determinantal full-family proof, saturation, cycles and endpoint schemes.
A separate sparse-polynomial implementation over the integers checked
the generator change, three maximal minors, cancellation relation,
Segre restrictions of a6 and b4, moving/absorption/special divisor
factorizations, and original-cycle restrictions.

This independent review accepted preservation of the core source
§§1–4.1 controls and the primitive orbit-degree statement. The source's
§§6–7 inherited investigations and the weight supplement's later
attainment, extreme-component, and cancellation results remain outside
this reconstructed proof closure. Review findings about the moved
verifier link and R-0043's explicit sharpness premise were corrected.
The geometric arguments use necessary exact algebra; the identity
checks do not independently prove flatness, saturation, or coverage.
No blanket classification as an intrinsic replacement proof is made.

Independent acceptance covers the nine reconstructed routes within their stated scopes. It neither proves a deformation preserving sole support nor establishes an unrestricted characteristic-zero STCI theorem. The Argument's complete status
records the completed exposition.
