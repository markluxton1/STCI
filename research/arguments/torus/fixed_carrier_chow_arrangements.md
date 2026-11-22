# Fixed-carrier Chow arrangements and collisions

**Review, November 20, 2026:** independent review checked the descent
criterion, parameter spaces, collision, reduced-generator bridge and quadric
comparison below.
The statements concern specified toric carriers, rather than arbitrary
complete intersections whose reduced cycle support lies on those surfaces.

## The fixed quartic and its translated sections

Let \(k\) be algebraically closed, of arbitrary characteristic, and put
\[
 A=x_2^4-x_0x_3^3,\qquad X=V(A),\qquad
 C_a=[s^4:a s^3t:st^3:t^4]\quad(a\in k^\times).
\]
Thus \(C_1=C_0\). Write \(h=s^3t\). The
[canonical normalization proof](../arithmetic/positive_characteristic_constructions.md#normalization-and-its-fibers)
gives the finite normalization
\[
 \nu:\mathbf P(1,1,4)\longrightarrow X,\qquad
 [s:t:z]\longmapsto[s^4:z:st^3:t^4],
\]
with homogeneous image ring \(R[z]\), where
\(R=k[s^4,st^3,t^4]\). It is an isomorphism over the dense coordinate
torus; the set-theoretic inverse image of \(C_a\) is \(V(z-ah)\). The
[semigroup calculation](../arithmetic/positive_characteristic_constructions.md#exact-semigroup-and-characteristic-criteria)
says \(h^j\in R\) exactly when \(j\in\langle3,4\rangle\), whose positive
gaps are \(1,2,5\).

## Exact realization by a mate on \(X\)

Fix \(N>0\) and a multiset of \(N\) nonzero scalars, written as distinct
\(a_i\) with positive multiplicities \(n_i\), where \(\sum_i n_i=N\).
Let
\[
 P(T)=\prod_i(T-a_i)^{n_i}
     =T^N+\sum_{j=1}^N c_jT^{N-j}.
\]
Then the following are equivalent:

1. A homogeneous degree-\(N\) form \(G\) gives a proper intersection
   with exact fundamental cycle
   \([V(A,G)]=\sum_i n_i[C_{a_i}]\).
2. \(c_j=0\) for every \(j\in\{1,2,5\}\) with \(j\le N\).

Equivalently, the elementary symmetric functions \(e_1,e_2,e_5\) of the
multiset vanish whenever their index is at most \(N\). When these conditions
hold, the embedded ideal \((A,G)\) is unique: \(G\) is determined modulo
\(A S_{N-4}\) and multiplication by a nonzero scalar, with \(S_d=0\) for
\(d<0\).

**Proof.** A proper complete intersection is pure. Thus its specified
cycle leaves no further projective support of any dimension. Pulling back
\(G\) gives a nonzero weighted homogeneous polynomial whose zero set is
precisely the union of the divisors \(z-a_i h=0\). Unique factorization gives
\[
 \nu^*G=\gamma\prod_i(z-a_i h)^{n_i}
 =\gamma\left(z^N+\sum_{j=1}^N c_jz^{N-j}h^j\right),\qquad
 \gamma\in k^\times.
\]
The exponents equal the cycle multiplicities because the normalization is
an isomorphism over the dense torus, where these divisors are distinct.
Membership in \(R[z]\) is coefficientwise. A nonzero coefficient
\(c_jh^j\) belongs to \(R\) exactly when \(j\in\langle3,4\rangle\), proving
necessity and the descent criterion.

Conversely, descent supplies a homogeneous lift \(G\). Its pullback has
exactly those divisors, so finite surjectivity of \(\nu\) excludes any other
projective support. The polynomial is nonzero on \(X\), so \(A,G\) are
coprime and give a proper complete intersection. The generic lengths are
the exponents \(n_i\). Finally the pullback map on the coordinate ring of
\(X\) is injective, so two normalized lifts differ by an \(A\)-multiple.
This also proves uniqueness. \(\square\)

This statement requires \(A\) as one actual generator. Merely assuming
that another, possibly nonreduced CI has its reduced support on \(X\)
does not put \(A\) in its ideal; that case needs a separate bridge.
The [restriction and relation interface](fixed_surface_restriction_lifts.md)
ties translate coordinates to coefficients of arbitrary equations and
identifies what restricted syzygies recover about their normal extensions.

Every classified ideal, including repeated cycles, is invariant under the
intrinsic torus of coordinate weights \((0,1,3,4)\): it preserves \(A\)
and each \(C_a\), so uniqueness fixes the ideal. Explicitly, a monomial
lift of \(h^j\) has weight \(j\), so \(G\) can have weight \(N\) while
\(A\) has weight twelve. A non-invariant lift of such a cycle supported
on \(X\) therefore cannot retain \(A\) as an actual generator.

## Parameter space and characteristic dependence

The multiset coordinates identify \(\operatorname{Sym}^N\mathbf G_m\)
with monic degree-\(N\) polynomials having nonzero constant term.
The explicit realization parameter space is the coordinate locus
\(c_1=c_2=c_5=0\), omitting indices larger than \(N\), with \(c_N\ne0\).
It is empty for \(N=1,2,5\); otherwise it is
\[
 \begin{cases}
 \mathbf A^{N-3}\times\mathbf G_m,&N=3,4,\\
 \mathbf A^{N-4}\times\mathbf G_m,&N\ge6.
 \end{cases}
\]
Its dimensions are \(1,2,N-3\), respectively. This coefficient model does
not assert a scheme-theoretic identification with a locus in the full
Chow scheme.

The reduced-cycle locus is the squarefree open subset. It is nonempty in
every characteristic for the allowed degrees \(N=3,4\) or \(N\ge6\),
except \(N=3\), \(\operatorname{char}k=3\).
Indeed \(T^N+d\), \(d\ne0\), is squarefree when the characteristic does
not divide \(N\). If \(p\mid N\), choose \(j\in\{3,4\}\) with \(j<N\)
and \(p\nmid j\). Then \(T^N+cT^{N-j}+d\), with \(c,d\ne0\), has
derivative a nonzero monomial and has no zero root. Such a \(j\) exists for
\(N\ge6\), and for \((N,p)=(4,2)\) take \(j=3\).
For \((N,p)=(3,3)\), every allowed polynomial is \(T^3+d\).

In characteristic zero, Newton's identities rewrite the missing
coefficients as
\[
 \sum_i n_i a_i=\sum_i n_i a_i^2=\sum_i n_i a_i^5=0.
\]
Every realized cycle therefore has at least three distinct components.
One component contradicts the first identity. For two components with
multiplicities \(r,s>0\), the first gives \(b=-ra/s\), and the second gives
\(r(r+s)a^2/s=0\), impossible in characteristic zero. This excludes full
coalescence and every two-support partition on this fixed carrier; it
allows partial collisions involving three or more supports.

For the single-support polynomial \(P(T)=(T-a)^N\), the criterion
recovers the
[existing exact Frobenius degree sets](../arithmetic/positive_characteristic_constructions.md#theorem-and-its-scope):
there is no characteristic-zero mate, while in characteristic \(p>0\)
descent is equivalent to \(p^{v_p(N)}\in\langle3,4\rangle\).

## An actual partial collision in characteristic zero

For \(c\ne-1\), take the proper quartic pair
\[
 A=x_2^4-x_0x_3^3,\qquad
 G_c=x_1^4+c x_0^2x_1x_2-(1+c)x_0^3x_3.
\]
Its normalized polynomial is \(P_c(T)=T^4+cT-(1+c)\), which always has
the root \(T=1\). Generic \(c\) gives four distinct translated components:
squarefreeness is open and holds at \(c=0\). At \(c=-4\),
\[
 P_{-4}(T)=(T-1)^2(T^2+2T+3),
\]
so the actual intersection cycle is
\[
 2[C_0]+[C_{-1+\sqrt{-2}}]+[C_{-1-\sqrt{-2}}].
\]
The remaining roots are distinct, nonzero and different from \(1\).
Thus another translate can collide with \(C_0\) in characteristic zero
inside the proper CI locus. The fixed-carrier obstruction concerns
complete coalescence, rather than an absence of collisions.

The family is flat over \(c\ne-1\): its fibers are proper complete
intersections of fixed type \((4,4)\), so relative regular-sequence
flatness applies. The marked multiplicity of \(C_0\) rises from one
generically, with residual-cycle degree twelve, to two at \(c=-4\), with
residual-cycle degree eight: this is actual marked absorption in a flat
proper-CI family. Throughout the fixed-\(A\), \((4,4)\) translated-arrangement
locus containing \(C_0\), at least three distinct supports force marked
multiplicity at most two and residual degree at least eight, attained here.

## All-order primary structure and attachment on the classified carrier

**New application, pending independent review.** The arrangement
semigroup criterion above already solves the fixed-carrier existence
question. It does not by itself describe the full embedded primary
structures when a root repeats. The following gives that description
in characteristic zero, including their attachment to the other
translated components. This is a testbed joining the formal normal,
finite-image, residual-attachment and arithmetic frameworks, not
another exclusion of this already classified carrier.

Fix a realized polynomial of degree \(N\) above and choose a root
of multiplicity \(m\). By scaling \(x_1\) take the marked root to be
\(1\), so its support is \(C=C_0\). Let \(T_m\) be the full primary
component on \(C\) of the actual CI \(Y=V(A,G)\).
It is independent of the other roots and of \(N\):
it is the scheme image of the Cartier thickening
\((z-h)^m=0\) on the normalization. Indeed that scheme is
pure, avoids the singular vertex of the weighted plane,
and has generic length \(m\) on \(C\). Its finite image
is pure (its structure sheaf injects into the finite
pushforward of a pure curve with the same support), is
contained scheme-theoretically in \(Y\), and agrees there
with the generic primary algebra. A pure scheme with this
single smooth support is determined by its generic ideal
via saturation, so the image is exactly the full primary
component. This does not require the image itself lci.

### The numerical semigroup determines every saturated layer

The normalization is smooth along the inverse curve,
and the Cartier equation there is a section of
\(\mathcal O_{\mathbf P(1,1,4)}(4)\).
Its restriction to the reduced inverse curve is
\(\mathcal O_{\mathbf P^1}(4)\), so the normalized
primitive thickening has free first conormal
\(\mathcal O(-4)\).
At \(p_\infty=[0:0:0:1]\) the carrier \(A=0\)
is smooth and the normalization is an isomorphism.
At \(p_0=[1:0:0:0]\), the local inclusion in
normalization coordinates is
\[
 k[[t^3,t^4,z]]\ \longrightarrow\ k[[t,z]].
\]
The normalized thickening is \((t-z)^m=0\).
Use \(x=z\) as the lifted curve parameter and
\(\epsilon=t-z\). Then the actual completed image
algebra is
\[
 B_m=k[[x]][(x+\epsilon)^s:s\in S]
   \ \subset\ k[[x]][\epsilon]/(\epsilon^m),
 \qquad S=\langle3,4\rangle ,
\]
where the algebra denotes its complete image.

There is a more general elementary numerical
semigroup calculation here. For any numerical
semigroup \(S=\{s_0=0<s_1<s_2<\cdots\}\)
and the same image algebra, the elements
\((x+\epsilon)^{s_i}\), \(0\le i<m\), form
a \(k[[x]]\)-basis. After factoring the column
weights \(x^{s_i}\) and row weights \(x^{-j}\)
over \(k((x))\), the coefficient matrix is
\((\binom{s_i}{j})_{0\le j,i<m}\). Its determinant
is the Vandermonde determinant of the \(s_i\)
divided by \(\prod_{j=0}^{m-1}j!\), nonzero in
characteristic zero because \(\binom{s}{j}\)
has degree \(j\) and leading coefficient \(1/j!\).
For any later exponent \(s\in S\), expansion
in this constant matrix expresses its monomial
as a linear combination with coefficients
\(c_i x^{s-s_i}\in k[[x]]\), so these first \(m\)
columns span the entire image. The completed
image has the same span since this is a finite
full lattice in a complete free DVR module.

Eliminating the lower \(\epsilon\)-coefficients
of column \(i\) using the first \(i\) columns
(with integral powers \(x^{s_i-s_j}\))
produces a saturated-flag basis with leading term
a unit times \(x^{s_i-i}\epsilon^i\). Since the
initial square minors on the first \(i+1\) rows
and columns are nonzero by the same determinant,
these leading terms describe the actual graded
submodules, not just their product determinant.
Consequently the finite modification to the
primitive thickening has layer indices
\(s_i-i\), total length \(\sum_{i<m}(s_i-i)\),
and multiplication defects in the image
\[
 \boxed{D_i=(i s_1-s_i)[p_0].}                           \tag{TS1}
\]
The free first conormal has changed by
\(-(s_1-1)[p_0]\).
For a general numerical semigroup this last
description is local; the global line bundle
requires its actual normalized ambient model.
The determinant calculation also works in
characteristic \(p>s_{m-1}\) for \(m\ge2\);
in small characteristic the minors must be
rechecked, not reduced as if their determinants
were units.

There is established related literature on
semigroups and higher jet matrices:
[Yasuda, *Higher Nash blowups*, §3.2,
Lemma 3.4](https://doi.org/10.1112/S0010437X0700276X),
and Chávez-Martínez--Duarte--Giles Flores,
[*A higher-order tangent map and a conjecture
on the higher Nash blowup of curves*](https://doi.org/10.1007/s00209-020-02579-5).
Their objects are higher Nash blowups of curves;
we use the elementary jet interpolation calculation
on the actual primary image, not a claim that
this image is a higher Nash blowup. The latter
would be a different construction.

For our semigroup, \(s_i=0,3,4,6,7,\ldots\),
with \(s_i=i+3\) for \(i\ge3\). Thus for \(m\ge2\)
\[
 \mathcal L_m=\mathcal O(-6),\qquad
 D_0=D_1=0,\quad D_2=2[p_0],\quad
 D_i=(2i-3)[p_0]\ (i\ge3),
                                                               \tag{TS2}
\]
where only \(i<m\) is retained. The length
of the finite normalization-induced modification
is \(0,2,3m-5\) for \(m=1,m=2,m\ge3\),
respectively. In particular the repeated-root
primary structure is a ribbon for \(m=2\)
and is nonprimitive at \(p_0\) for \(m\ge3\);
this is about the embedded **primary structure**,
not the entire proper CI. The purely arithmetic
all-mate criterion above is unchanged.

### Exact residual-attachment distributions

Write \(R\) for the linked residual without the
marked component, and \(H_0=C\cap R\).
All attachment is at the two endpoints because
the distinct translates are disjoint on the
dense torus. At the smooth endpoint \(p_\infty\),
the actual polynomial in the local carrier
coordinates is a product of
\((x_1-a_i x_2^3)^{n_i}\);
hence the residual restriction on \(C\) has
order \(3(N-m)\) there.
The [signed top-class identity LA4](../residuals/residual_capacity_and_constructions.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component)
gives
\[
 \deg H_0=4N+2-6(m-1)+\deg D_{m-1}
\]
for \(m\ge2\). For \(m=1\) the same formula
holds with the zero exponent term and \(D_0=0\),
by ordinary reduced-component linkage.
Together these give the exact two-point divisor
\[
 \begin{array}{c|c|c}
 m & H_0(p_0)&H_0(p_\infty)\\ \hline
 1&N+5&3(N-1)\\
 2&N+2&3(N-2)\\
 3&N+1&3(N-3)\\
 \ge4&N-m+3&3(N-m)
 \end{array}                                             \tag{TS3}
\]
for actual realized arrangements. These numbers
are meaningful only for the allowed multiplicities
of the classified polynomial. The finite residual
attachment in the full thickening has every layer
given by LA1 and TS2. For example, at the smooth
endpoint every layer has length \(3(N-m)\).
At \(p_0\), for \(m\ge3\) the sum of its
attachment-layer lengths is \(m(N-m)+10\).
For \(m=1,2\) that sum is respectively
\(N+5\), \(2(N+2)\).
The global full-attachment length for \(m\ge3\)
is therefore \(4m(N-m)+10\). This also follows
from the finite-image genus, since for \(m\ge3\)
the normalized primitive thickening has genus
\(1-m+2m(m-1)\), and its image genus is
\(2m^2-4\). The two arguments agree; the genus
check is not a second independent obstruction.

For the actual \((4,4)\) collision \(c\to-4\)
described above, TS3 shows that the reduced
attachment changes from \(9p_0+9p_\infty\)
to \(6p_0+6p_\infty\), whereas the full
attachment length changes from \(18\) to \(24\).
The residual degree drops from twelve to eight.
The primary double at the collision is primitive
of conormal degree \(-6\). The two different
attachment measures thus move in opposite
directions under an actual absorption; flatness
of the *full primary extraction* cannot be
assumed across that multiplicity jump.
By [the local-cohomology comparison LC-A1](../local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers),
the two reduced attachment coefficients are
also the lengths of the first local annihilator
layers of actual-pair local cohomology, with
its canonical duality twist.

This is an all-degree calibration of the
residual/normal/local-cohomology comparison
on the existing exactly classified carrier.
It explains why primary normal defects and
full conductor or attachment lengths should
not be treated as interchangeable monotone
quantities in torus or arithmetic collisions.
It does not generalize the characteristic-zero
matrix calculation to the Frobenius collision
in characteristic two: the necessary minors
there can vanish, compatible with the known
primitive fourfold image. The arithmetic
control continues to use its actual equations.

The classical local quasiprimitive triple
normal form of Bănică--Forster also makes
the observed equality in TS7 universal
within the **generically curvilinear
triple stratum**: the
[TR2 conormal-torsion identity](../residuals/residual_capacity_and_constructions.md#triples-the-full-attachment-has-only-two-independent-divisors)
gives \(\tau=D_2\) for any such full
primary. Combined with the actual
equation determinant \(\eta\), the
[TR3 two-divisor theorem](../residuals/residual_capacity_and_constructions.md#triples-the-full-attachment-has-only-two-independent-divisors)
gives attachment layers
\((\tau+\eta,\eta,\tau+\eta)\).
For TS5--TS7 this is \((7,5,7)\)
and \((9,9,9)\). The proof explicitly
uses BF and ordinary Hilbert--Burch,
not an extrapolation from one
example. The characteristic-zero
semigroup basis used earlier has
a different characteristic scope
from this formal local triple
argument.

### A fixed auxiliary quadric detects the same punctual defect at every collision

The retained \((4,4)\) family and its arbitrary-degree
classified relatives permit an **independent actual-equation check**
of LA5--LA6. Let
\[
 Q=x_0x_3-x_1x_2,\qquad
 Y_N=V(A,G_N)
\]
be any classified degree-\((4,N)\) arrangement
containing \(C_0\) with marked multiplicity \(m\ge1\).
The quadric \(Q\) contains \(C_0\), but no
other translated \(C_a\) with \(a\ne1\).
The scheme \(Y_N\cap Q\) is one-dimensional
with reduced curve \(C_0\); let \(B_Q\) be
its maximal punctual torsion length divisor
on that reduced curve. Then
\[
 \boxed{\quad
 B_Q=3(N-3)[p_0]+(N-1)[p_\infty].
 \quad}                                                 \tag{TS4}
\]
In particular it is **independent of the marked
multiplicity** \(m\) and of every other root
or collision partition, provided the polynomial
satisfies the fixed-carrier realization criterion.

This can be proved directly, without
assuming any of the new attachment duality.
At the smooth endpoint \(p_\infty\) use
\(z=x_2/x_3,\epsilon=x_1/x_3-z^3\)
on \(A=0\), with \(x_3=1\). Then
\(Q=-z\epsilon\) (up to unit), while
\[
 G_N|_{A=0}=
  \epsilon^m\prod_{a\ne1}
   (\epsilon+(1-a)z^3)^{n_a}
\]
up to a unit. Modulo \(z\epsilon\),
every mixed term containing \(z\) and
\(\epsilon\) vanishes; the term without
\(\epsilon\) is zero because \(m\ge1\).
Thus
\[
 \mathcal O_{Y_N\cap Q,p_\infty}
 \simeq k[[z,\epsilon]]/(z\epsilon,\epsilon^N),
\]
whose punctual torsion has length \(N-1\).

At the cuspidal endpoint \(p_0\), put
\(x_0=1,\ z=x_1,\ w=x_2\), eliminate
\(x_3=zw\) using \(Q=0\), and put
\(v=w-z^3\). The actual restricted
carrier is
\[
 A|_Q=w^3v.
\]
The actual mate restricts as \(G_N|_Q=vH(z,w)\)
because it vanishes along \(C_0\).
Its leading coefficient on the triple
ruling line \(w=0\) is \(G_N(z,0,0)=z^N\);
hence
\[
 H(z,0)=-z^{N-3}.
\]
Multiplication by the nonzerodivisor
\(v\) gives
\[
 0\to k[[z,w]]/(w^3,H)
   \xrightarrow{\cdot v}
 k[[z,w]]/(w^3v,vH)
   \to k[[z,w]]/(v)\to0.
\]
The last term is \(k[[z]]\), while the
first is finite over \(k[[z]]\).
Since \(k[[z,w]]/(w^3)\) is free of
rank three over \(k[[z]]\), multiplication
by \(H\) has determinant \(H(z,0)^3\),
so its finite cokernel has length
\(3(N-3)\). This proves TS4.

To compare with the intrinsic formulas,
the reduced attachment divisor TS3 has
the displayed endpoint lengths.
Multiplication by \(Q\) on the residual
primary algebra has length
\(4(N-m)\) at each endpoint:
over the local curve parameter its
generic determinant is the product of
the reduced values \((1-a)t^4\),
each repeated \(n_a\) times.
For \(m\ge2\) the free conormal of \(T_m\)
is \(\mathcal O(-6)\), and the first
symbol of \(Q\) has the tangency divisor
\(\Theta=[p_0]+[p_\infty]\);
at \(p_0\) this follows from the
normalized expansion \(t^3(t-z)\),
whose first free symbol has one extra
\(z\)-factor above the generator
\(z^2(t-z)\). At \(p_\infty\) it is
the factor \(z\epsilon\).
Thus [LA6](../residuals/residual_capacity_and_constructions.md#cutting-the-residual-pair-rather-than-just-its-primary-part)
gives
\[
 \begin{aligned}
 B_Q&= B_{T_m}+[R\cap Q]-H_0,\\
 B_{T_m}&=(m-1)([p_0]+[p_\infty])
                     +D_{m-1}.
 \end{aligned}
\]
Substitution of TS2--TS3 gives
\(B_Q(p_0)=3N-9,\ B_Q(p_\infty)=N-1\),
exactly TS4. For \(m=1\) the marked
primary is reduced and \(B_{T_1}=0\);
the same formula holds by the ordinary
union sequence. This is a nontrivial
**independent consistency check** of the
signed attachment correction, not a
second proof of LA1 in general.

For \(N=4\), both the four-component
generic fiber and the doubled-component
collision have
\[
 B_Q=3[p_0]+3[p_\infty].
\]
The residual degree, reduced attachment
and full attachment all change, while
this particular finite quotient remains
constant. Consequently neither its
total length nor its distribution can
measure absorption in that family
without the primary normal and
attachment information. This is
another precise warning against
promoting a fixed toric resultant,
conductor or punctual torsion
number into a universal residual
monotone. The argument uses actual
restricted equations on \(Q\);
it is not an inference from Chow
cycles alone.

### An actual non-lci curvilinear triple: the conormal torsion is visible

The all-order formulas above admit a particularly useful
**explicit proper intersection** in characteristic zero.
Take the realized degree-six root polynomial
\[
 P_6(T)=(T-1)^3(T^3+3T^2+6T+2)
       =T^6-8T^3+9T^2-2,
\]
and the actual equations
\[
 \begin{aligned}
 A&=x_2^4-x_0x_3^3,\\
 G_6&=x_1^6-8x_0^2x_1^3x_2
             +9x_0^3x_1^2x_3-2x_0^4x_2^2.
 \end{aligned}                                          \tag{TS5}
\]
All three missing semigroup coefficients
\(c_1,c_2,c_5\) vanish. The residual
cubic has discriminant \(-216\) and nonzero
constant term, so the actual fundamental
cycle is \(3[C_0]\) plus three distinct
other translated quartics. Its total
degree is 24; its genuine residual degree
is 12. This is an example with residual
support, not a characteristic-zero STCI.

At \(p_0\) let \(x=x_1/x_0,\ w=x_2/x_0,\ h=x_3/x_0\),
and change regular ambient coordinates to
\[
 X=(w-x^3)/3,\qquad
 Z=(h-x^4)-(4x/3)(w-x^3).
\]
On the normalized **triple** set
\(t=x+\epsilon,\ \epsilon^3=0\). Then
\[
 X=x^2\epsilon+x\epsilon^2,\qquad
 Z=2x^2\epsilon^2.
\]
The actual full \(C_0\)-primary image
has completed ideal
\[
 \boxed{\quad
 J=(X^2-\tfrac12x^2 Z,\ XZ,\ Z^2)
 \subset k[[x,X,Z]].\quad}                              \tag{TS6}
\]
The quotient is \(k[[x]]\)-free on
\(\{1,X,Z\}\), and its injective map
to \(k[[x]][\epsilon]/\epsilon^3\)
has precisely the semigroup lattice
indices \((0,2,2)\).
In particular the generic algebra
is curvilinear of length three, but
the primary is **not lci at \(p_0\)**.

Let \(f_1=X^2-\tfrac12x^2Z,\ f_2=XZ,\ f_3=Z^2\).
The two Hilbert--Burch syzygies are
\[
 Zf_1-Xf_2+\tfrac12x^2 f_3=0,\qquad
 Zf_2-Xf_3=0.
\]
Reducing these modulo \(I_C=(X,Z)\)
gives the exact primary conormal module
\[
 \boxed{\quad
 J/I_CJ\simeq k[[x]]^2\oplus k[[x]]/(x^2).
 \quad}                                                 \tag{TS7}
\]
The torsion has length **two**,
equal here to the first nonprimitive
multiplication defect \(D_2(p_0)=2\).
This is an explicit instance in the
curvilinear generic branch of the
non-lci torsion correction in the
[full-primary attachment determinant](../residuals/residual_capacity_and_constructions.md#full-primary-equation-module-and-exact-attachment-divisor).

For the actual pair TS5, the reduced
marked attachment is
\[
 H_0=7[p_0]+9[p_\infty],
\]
and its three thick layers at
\(p_0\) have lengths \((7,5,7)\),
while those at \(p_\infty\) are
\((9,9,9)\). The full attachment
length is therefore \(19+27=46\).
The torsion correction \(\tau\)
is \(2[p_0]\) by TS7, so the
determinant of the *actual two-equation
map* has divisor
\[
 \operatorname{div}\theta
   =5[p_0]+9[p_\infty].
\]
Equivalently, the first actual
local-cohomology annihilator layers
of the pair have lengths 7 and 9,
via [LC-A1](../local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers).
On the auxiliary quadric, TS4 gives
\(B_Q=9[p_0]+5[p_\infty]\).
Thus this *one explicit pair* simultaneously
tests the source-polynomial classification,
saturated normal layers, genuine residual
attachment, conormal non-lci torsion,
the dual annihilator layer, and the
signed proper-cut formula.

The equality \(\tau(p_0)=D_2(p_0)=2\)
is now identified as an instance of
the [general triple identity TR2](../residuals/residual_capacity_and_constructions.md#triples-the-full-attachment-has-only-two-independent-divisors):
it holds for any generically curvilinear
primary *triple*, but has not been
established for arbitrary higher
multiplicity or noncurvilinear
primaries. The
Hilbert--Burch and local-duality inputs
are classical; the displayed calculation
is a calibration of their combined use.
Independent mathematical review pending.

## When a reduced fundamental cycle supplies the quartic equation

Suppose an arbitrary proper homogeneous pair has reduced fundamental
cycle consisting of distinct \(C_{a_i}\), all on this fixed \(X\).
Then it has type \((4,N)\), up to swapping, and its ideal admits \(A\)
as a minimal generator. Hence the preceding classification applies.

**Proof.** Purity and generic reducedness make the CI scheme the reduced
union \(Y\), so its saturated homogeneous ideal contains \(A\). Order its
generator degrees as \(d\le e\). Since \(A\in I_Y(4)\), \(d\le4\).
There is no linear equation on any \(C_a\). Each \(C_a\) has the unique
quadric \(x_1x_2-a x_0x_3\): the ten quadratic monomials restrict to nine
distinct binary exponents, only \(x_1x_2,x_0x_3\) coinciding.
Distinct parameters therefore have no common quadric. For a single
component, Bézout would force a hypothetical degree-two pair to be
\((2,2)\), requiring two independent quadrics. Thus \(d\ne1,2\).

If \(d=3\), Bézout gives \(4\mid e\). For \(e>4\), membership
\(A\in I_Y(4)\) makes the irreducible quartic \(A\) a multiple of the
cubic generator, a contradiction. Hence \(e=4\), and \(A\), being
independent of cubic multiples, can replace the quartic generator.
If \(d=4<e\), the degree-four generator is a scalar multiple of \(A\);
if \(d=e=4\), a linear change of the generator basis includes \(A\).
These exhaust the possibilities. \(\square\)

The reducedness hypothesis is essential to this bridge. For repeated
cycles, support on \(X\) only implies that some power of \(A\) belongs to
the ideal. Classifying those thickenings is a different realization problem.

## Comparison with the fixed smooth quadric

Put \(Q=V(x_0x_3-x_1x_2)\). In the quotient coordinates of the
[Chow account](../equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle),
the translates lying on \(Q\) have \(u=v\).
The quartic \(X\) has \(u^4=v^3\), so their dense tori intersect
scheme-theoretically in \(u=v=1\), exactly \(C_0\cap\Omega\), in every
characteristic: \((u-v,u^4-v^3)=(u-1,v-1)\) in the Laurent ring.
This does not describe the whole projective intersection. In Segre coordinates
\([x_0:x_1:x_2:x_3]=[AU:AV:BU:BV]\), the quartic restricts to
\(B^3U(BU^3-AV^3)\), giving cycle
\([C_0]+3[V(x_2,x_3)]+[V(x_0,x_2)]\).
The translated quartics on \(Q\) all have ruling class \((1,3)\), up to swapping:
the diagonal maps \(\operatorname{diag}(1,1,u,u)\) preserve each ruling.
By the [canonical quadric argument](../equations/global_equations_and_constructions.md#p-004-why-the-quadric-cannot-be-one-of-two-equations),
a degree-\(N\) mate cuts class \((N,N)\). It cannot have divisor cycle
\(\sum_i n_i[C_i]\), whose class is \((m,3m)\), \(m=\sum_i n_i>0\).
Thus no actual pair \((Q,G)\) has sole support on these translates, in any
characteristic. Any reduced CI union of them would have \(Q\) in its ideal;
nonplanarity forces minimal generator degree two, so \(Q\) could replace
that generator, contradicting the class calculation. Repeated cycle
support alone does not supply this generator bridge.
