# Sextic pairs: nonreduced defects and the normal index-nine case

This is an independently reviewed provisional application to the fixed
\(C_0=[s^4:s^3t:st^3:t^4]\), in characteristic zero or \(p\ge7\).
Suppose an arbitrary proper pair \(Z=V(F_6,G_6)\) has reduced support
\(C_0\). Neither equation is assumed integral, normal, or to have a
prescribed first symbol. The following reduction covers every such pair;
it does not exclude all of them.

## Why every pair is generically curvilinear

Put \(q=x_0x_3-x_1x_2\). The containing smooth quadric \(Q=V(q)\)
cannot divide either equation:
the other equation would restrict to a divisor of class \((6,6)\)
supported on the unbalanced \((1,3)\) curve. For either sextic of generic
normal order \(r\), its nonzero restriction to \(Q\) contains the curve
equation to at least power \(r\). The residual class has second component
at most \(6-3r\), so \(r\le2\). Equality of ambient normal order and
restricted multiplicity is not required here.

The [graph bound](../synthesis/blowup_residual_geometry.md#5-integer-strengthening-usefulness-region-and-exact-limitations)
excludes orders \((2,2)\): its value
\(K=16(12+12)-7\cdot36-28\cdot4=20\) gives residual degree
\(\delta\ge4\). Its proof applies in odd characteristic with the
balanced normal bundle. Thus at least one equation has generic normal
order one. The generic transverse algebra is consequently
\(k(C_0)[v]/(v^9)\), because \(ab=36=4\cdot9\).

## The complete necessary divisor profile

Apply the saturated filtration and actual perfect multiplication pairings
in [the curvilinear filtration proof](CURVILINEAR_GENUS_AND_DEFECTS.md).
For the successive line-bundle quotients of that filtration, write
\(E_i=L^i(D_i)\), \(0\le i\le8\), with
\(D_0=D_1=0\). Adjunction and the conormal quotient give
\[
 E_8=\mathcal O_{\mathbf P^1}(-34),\qquad
 \mathcal O(-7)^2\twoheadrightarrow L.
\]
If \(L=\mathcal O(-l)\), then \(l\le7\), while
\(\deg D_8=8l-34\ge0\). Hence \(l\in\{5,6,7\}\).
The actual self-pairing \(E_4^{\otimes2}\simeq E_8\) gives
\(D_8=2T\) as divisors, where \(T=D_4\). With \(A=D_2,B=D_3\),
the entire sequence must be
\[
 (D_0,\ldots,D_8)=(0,0,A,B,T,2T-B,2T-A,2T,2T).
\]
All its effectivity and superadditivity conditions are equivalent to
\[
 \boxed{0\le A\le B\le T,\qquad 2A\le T,\qquad A+2B\le2T.}
\]
These are coefficientwise divisor inequalities, not only degree bounds.
Completeness follows by checking the unordered pairs \(i,j\ge2\) with
\(i+j\le8\); pairs involving index one give monotonicity, and the
remaining pairs give exactly the displayed conditions or complementary
equalities.

The [pointwise torsion identity](CURVILINEAR_GENUS_AND_DEFECTS.md#5-complete-intersection-duality-fixes-a-top-divisor)
therefore gives the following necessary
rows for the **ordinary** nilradical filtration:

| First quotient \(L\) | \(\deg T\) | Total ordinary-layer torsion length |
|---|---:|---:|
| \(\mathcal O(-5)\) | 3 | 27 |
| \(\mathcal O(-6)\) | 7 | 63 |
| \(\mathcal O(-7)\) | 11 | 99 |

The last row has the additional necessary restriction
\[
 \boxed{l=7\quad\Longrightarrow\quad 1\le\deg A\le5.}
\]
Indeed if \(A=D_2=0\), multiplication \(L^{\otimes2}\to E_2\)
is an isomorphism everywhere. In the quotient by the saturated third
ideal \(P_3\), a local lift \(v\) of a generator of \(L\) then gives
the basis \(1,v,v^2\) over a completed curve parameter ring, with
\(v^3=0\). Thus \(\mathcal O_Z/P_3\) is an embedded primitive triple,
including at defective points of the original length-nine structure.
For \(l=7\), the fixed-curve
[P-010 cocycle](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md)
excludes this triple in characteristic zero and every \(p>3\): its
\(-3/8\) coefficient, and the missing quotient line's \(3z^{-5}\)
class, remain nonzero. The upper bound follows from \(2A\le T\).
Independent reconstruction verified the saturated-quotient argument and
the exact positive-characteristic scope of the existing cocycle. No
reducedness of a defect divisor is needed for this restriction.

More precisely, if \(B_j\) is the divisor of local torsion lengths in
\(J^j/J^{j+1}\), where \(J\) is the nilradical of \(\mathcal O_Z\),
then \(\sum_j B_j=9T\) as effective divisors. The support
of \(T\) is exactly where the thickening is not locally contained in a
smooth surface along \(C_0\). Indeed locally primitive structure has
all multiplication divisors zero; conversely \(D_8=0\) forces every
\(D_i=0\), and a lift of a generator of \(L\) then generates the
nilradical by descending the saturated flag. In particular every candidate
has a nonempty finite nonprimitive locus, although its generic transverse
algebra is curvilinear. The number of its distinct points is at most
\(\deg T\) in the corresponding row.

This uses the characteristic-free Frobenius-functional and lattice proofs;
it does not divide by nine or assume the ordinary layers are locally free.
Independent reconstruction checked the all-pair order reduction, the
odd-characteristic graph input, the complete divisor inequalities and
pointwise torsion identity. No degree enumeration or incidence computation
was performed. These three rows do not classify actual embedded structures:
divisor realizability, homogeneous equation lifts and sole support still
have to be established or excluded. In particular the unrestricted
\((6,6)\) question remains open.

## A normal pencil carrier in characteristic zero

In characteristic zero the reduction can retain an actual normal carrier.
Every nonzero pencil member \(H=\alpha F+\beta G\) is integral. Choose
an independent pencil mate \(K\); then \((H,K)=(F,G)\). If an irreducible
factor of \(H\) has degree \(d\), its proper intersection with \(K\)
is a nonempty curve supported on \(C_0\), hence \(4\mid6d\). Thus
\(d\) is even. Degree two is impossible by the quadric argument above,
so every factor has degree at least four. A sextic can have only one such
factor, with multiplicity one. This also rules out nonreduced pencil members.

By [Kleiman's characteristic-zero Bertini corollary, §5](https://numdam.org/item/CM_1974__28_3_287_0.pdf),
a general pencil member is smooth off its base support \(C_0\). At the
generic point of \(C_0\), its first normal symbol is nonzero for all but
at most one pencil parameter, since the two original symbols are not both
zero. Such a member is smooth at the generic point of \(C_0\), so any
remaining singularities form a finite subset of \(C_0\). The integral
hypersurface is Cohen–Macaulay and regular in codimension one, hence normal.
Two independent members in this open set give the same original thick
intersection with both carriers normal.

On either normal sextic \(S\), the mate cuts the Cartier divisor
\[
 \operatorname{div}_S(K)=9C_0,\qquad 9C_0\sim6H_S.
\]
Every actual on-curve local Cartier index therefore divides nine. Its
possibilities are \(1,3,9\), and at least one is nine: otherwise
[R-0035](../results/normal_carrier_bounded_index_exclusion.md) would exclude
this normal integral carrier with its actual supported mate. That promoted
theorem requires no ADE hypothesis; its stated characteristic-zero scope is
retained here.

There is also a concrete torsion class to retain:
\[
 \Delta=3[C_0]-2[H_S]\in\operatorname{Cl}(S)
 \quad\text{has exact order three.}
\]
The mate gives \(3\Delta=0\). If \(\Delta=0\), the effective divisor
\(3C_0\sim2H_S\) would supply a section of \(\mathcal O_S(2)\) with
sole support \(C_0\). It lifts to an ambient quadric because
\(H^1(\mathbf P^3,\mathcal O(2-6))=0\), contradicting the no-quadric-mate
argument. This is a class in the Weil divisor class group, not an assertion
that \(3C_0\) is Cartier.

Independent reconstruction accepted this pencil and index reduction,
including factor support, repeated factors, Bertini's exact use, Serre's
normality criterion, the nonzero order-three class, and the bounded-index
theorem's hypotheses. It leaves
an actual normal sextic with an index-nine point and one of the defect
profiles above as the remaining characteristic-zero target. It does not
classify the singularities or exclude that target. In particular, no
positive-characteristic Bertini conclusion or index-nine necessity is being
deduced from this paragraph; the earlier three-row reduction has its own
separately verified characteristic scope.

## Exact global invariants of the order-three cover

Continue in characteristic zero with a normal pencil carrier \(S\).
Let \(a_2=\deg A=\deg D_2\) and \(t=\deg T=4l-17\).
The connected normal cyclic cover \(\pi:Y\to S\) associated with
\(\Delta=3C_0-2H_S\) has
\[
 \boxed{K_Y^2=72,\qquad
 \chi(\mathcal O_Y)=6l-21-2a_2,\qquad
 q(Y)\ge\max\{0,32-6l+2a_2\}.}
\]
These statements concern the normal covering surface itself, not a
resolution. No rational-singularity or ADE hypothesis is imposed.

To compute the eigensheaves, put \(I_i=\mathcal O_S(-iC_0)\).
They are rank-one reflexive sheaves, hence maximal Cohen–Macaulay on
the normal surface. Since \(I_9=\mathcal O_S(-6H_S)\), the quotient
\(I_i/I_9\) inside \(\mathcal O_Z\) has the generic stalk of the
\(i\)-th nilradical power and a pure quotient. It is exactly its
saturation. Moreover \(I_C I_i\subset I_{i+1}\), and
\(I_i/I_{i+1}\) is pure of rank one on \(C_0\); thus it is the
previously defined line bundle \(E_i\), including at every defective
point. This identification incurs no unknown punctual correction.

The sextic hypersurface formula and the curve layers give, for every
integer \(n\),
\[
 \chi(\mathcal O_S(nH_S))=3n^2-6n+11,\qquad
 \chi(E_i(nH_S))=-il+\deg D_i+4n+1.
\]
Use \(\Delta\sim4H_S-6C_0\) and
\(2\Delta\sim2H_S-3C_0\), which follow from \(9C_0\sim6H_S\).
The divisorial filtrations then yield
\[
\begin{aligned}
 \chi(\mathcal O_S(\Delta))
 &=35+\sum_{i=6}^8\chi(E_i(4H_S))
   =86-21l+6t-a_2=3l-16-a_2,\\
 \chi(\mathcal O_S(2\Delta))
 &=83+\sum_{i=3}^8\chi(E_i(2H_S))
   =137-33l+9t-a_2=3l-16-a_2.
\end{aligned}
\]

Choose a Weil representative of \(\Delta\) and a rational function
whose divisor is three times that representative. Exact order three
makes its Kummer extension a field of degree three. The normalized
cover has the exact eigensheaf decomposition
\[
 \pi_*\mathcal O_Y=
 \mathcal O_S\oplus\mathcal O_S(\Delta)\oplus\mathcal O_S(2\Delta).
\]
This is the integral-divisor case of
[Ambro, §4, Lemmas 4.1–4.2](https://arxiv.org/pdf/1310.3951).
The normalization is already included in this formula. Equivalently,
the reflexive cyclic algebra is \(S_2\) and is normal in codimension
one by the unramified Kummer calculation. Adding the three Euler
characteristics proves the asserted \(\chi(\mathcal O_Y)\).

The cover is étale in codimension one. The resulting equality
\(\omega_Y=\pi^*\omega_S\) extends across the remaining finite set
by reflexivity. Since \(\omega_S=\mathcal O_S(2H_S)\), the cover is
Gorenstein with ample Cartier canonical divisor and
\(K_Y^2=3(2H_S)^2=72\).

Neither nonzero torsion class \(\Delta\) nor \(2\Delta\) has a
nonzero section: such a section would give an effective Weil divisor
of intersection zero with the ample \(H_S\), forcing the class to
be trivial. Hence \(h^0(\mathcal O_Y)=1\). Pullback injects the ten
canonical sections of \(S\) into those of \(Y\), and Serre duality
on the normal Cohen–Macaulay surface gives
\(q(Y)=1+p_g(Y)-\chi(\mathcal O_Y)\ge11-\chi(\mathcal O_Y)\).

For \(l=5\), the possibilities \(a_2=0,1\) force \(q(Y)\ge2,4\),
respectively. For \(l=6,a_2=3\), they force \(q(Y)\ge2\).
These are genuine global constraints, but no incompatible upper bound
on \(q(Y)\) has been obtained. In particular a smooth-surface or
rational-singularity inequality must not be applied to \(Y\) without
establishing its hypotheses.

Independent reconstruction accepted the divisorial-layer identification,
both Euler computations, exact normalized-cover eigensheaves, canonical
pullback and irregularity bound. It covered arbitrary normal singularities
and retained the distinction between \(Y\) and a resolution. This is
reviewed provisional necessary evidence, not an exclusion of the cover.

## The common first-normal divisor must be nonreduced

In characteristic zero, **no supported sextic pair has reduced common
first-normal divisor**. This is a restriction on every pair, rather than
an assumption that its original carriers have ADE singularities.

The conormal quotient has kernel
\[
 0\longrightarrow M=\mathcal O(l-14)
 \longrightarrow N_{C_0}^*=\mathcal O(-7)^2
 \longrightarrow L=\mathcal O(-l)\longrightarrow0.
\]
The first symbols of the two sextics are sections \(f,g\) of
\(M(24)=\mathcal O(l+10)\), not both zero. Let \(B_1\) be their
common zero divisor, of degree \(\beta\). This includes the case in
which one symbol is zero. Its support is exactly the nonprimitive locus:
away from it one equation is smooth along the curve and the supported
intersection is locally a primitive length-nine structure.

Suppose \(B_1\) is reduced. After removing it, the two symbols give a
basepoint-free pencil on \(\mathcal O(l+10-\beta)\). If that degree
is positive, characteristic-zero separability makes a general member's
moving zeros simple and disjoint from \(B_1\). A general coefficient
also avoids cancellation at its finitely many fixed zeros. If the residual
degree is zero, the full zero divisor is just \(B_1\), still reduced.
Choose such a pencil member in the normal, off-curve smooth open set
established above. Its singularities are precisely its first-symbol zeros.

At a simple symbol zero the quadratic term contains a nonzero product of
the curve parameter and a normal parameter. The Hessian has rank at least
two; isolation of the singularity then gives an \(A_{r-1}\) singularity.
The marked smooth curve has end distance one, because its first-symbol
torsion length is one. The local marked classification in
[Ellia, Definition 8 and Lemma 10](https://arxiv.org/html/1409.3801)
therefore gives coordinates
\[
 S:(tu-w^r=0),\qquad C_0:(u,w)=0.
\]
Here the curve's Cartier index is \(r\). The actual mate cuts \(9C_0\),
so \(r\mid9\), and the completed intersection ideal is
\((tu-w^r,u^{9/r})\), up to units and changing the mate modulo the
carrier. At a fixed point of \(B_1\), the mate is also singular, so
\(r\ne9\); singularity of the carrier excludes \(r=1\). Thus every
fixed point is marked \(A_2\), with completed pair
\((tu-w^3,u^3)\). At a moving zero outside \(B_1\), an independent
mate is smooth, giving marked \(A_8\) and a locally primitive structure.
This uses the local classification, not a global theorem assuming that
the whole multiple curve is primitive.

At a fixed point the saturated multiplication divisors have coefficients
\((D_i)_P=\lfloor i/3\rfloor\). Consequently \(T_P=1\) and
\((D_2)_P=0\). All defects vanish elsewhere. In particular
\[
 T=B_1,\qquad \beta=4l-17,\qquad
 N=l+10-\beta=27-3l,
\]
where \(N\) counts moving \(A_8\) points. The residual degree-zero
case would give \(l=9\), which is unavailable. The remaining counts are

| \(l\) | Fixed \(A_2\) points | Moving \(A_8\) points | Exceptional root rank |
|---:|---:|---:|---:|
| 5 | 3 | 12 | 102 |
| 6 | 7 | 9 | 86 |
| 7 | 11 | 6 | 70 |

These are all the singularities of the chosen carrier. Its minimal
resolution has \(K^2=24,p_g=10,q=0,c_2=108,h^{1,1}=86\), the usual
sextic invariants, since every singularity is a rational double point.
The negative-definite exceptional root lattices are independent of the
positive-square hyperplane class, so their rank is at most 85. This excludes
the first two rows.

In the last row \(L=\mathcal O(-7)\) and \(D_2=0\), contradicting
the necessary nonzero-second-defect restriction proved above. Concretely,
at a fixed point the saturated third ideal is \(P_3=(u)\): its quotient
is \(k[[t,w]]/(w^3)\), torsion free over \(k[[t]]\), with the correct
generic stalk. Elsewhere the length-nine structure is already primitive.
Thus \(\mathcal O_Z/P_3\) is the forbidden embedded primitive triple
of type \(\mathcal O(-7)\). The quotient uses the **saturated** third
ideal, not the ordinary cube of the nilradical.

Independent reconstruction accepted the simple-zero reduction, marked
local classification, exhaustion of singularities, defect counts, Hodge
rank bound and actual saturated primitive triple. The conclusion is that
\(B_1\) must have at least one point of multiplicity at least two.
It does not exclude a pair with such a nonreduced divisor, and no
positive-characteristic Hodge argument is asserted.

## A local nonreduced control with a non-ADE carrier

The remaining nonreduced case is compatible with finite flat local
complete-intersection data. Over \(R=k[[t]]\), in characteristic zero
or \(p\ge7\), consider
\[
 B=R[[u,v]]/(t^2u+v^3,u^3).
\]
It is free of rank nine over \(R\), with basis \(u^iv^j\),
\(0\le i,j\le2\), and generic fiber \(k((t))[v]/(v^9)\).
For its nilradical \(J=(u,v)\),
\[
 J/J^2=Rv\oplus(R/(t^2))u,\qquad B_1=2[0],\qquad
 D_i=2\lfloor i/3\rfloor[0].
\]
Hence \(D_2=0,T=D_4=2[0],D_8=4[0]\); total ordinary-layer torsion
has length \(9\deg T=18\). The actual socle is \(Ru^2v^2\), whereas
the ordinary top power is \(Rv^8=t^4Ru^2v^2\). The latter is not the
saturated socle lattice.

For \(\lambda\ne0\), the carrier
\(t^2u+v^3+\lambda u^3=0\) is the cone over a smooth plane cubic:
its three partial derivatives have no common projective zero in these
characteristics. It is normal with a simple elliptic vertex, not an ADE
singularity. The smooth ruling \(C=(u,v)\) satisfies
\(\operatorname{div}(u)=3C\). Blowing up the vertex gives the cubic
exceptional curve \(E\) with \(E^2=-3\), and the strict transform of
\(C\) meets it once. If \(nC\) were Cartier, its pullback would have
intersection zero with \(E\), forcing \(3\mid n\). Thus the actual
Cartier index is three. Its mate \(u^3\) cuts exactly \(9C\), and
the pair defines the same algebra \(B\).

Independent reconstruction verified freeness, the first-layer defect,
socle and carrier index; the displayed lattice distinguishes ordinary
powers from their saturations. This supplies a local control for the
nonreduced case and the failure of an automatic ADE assertion. It is not
a global sextic construction. The related earlier family
\((t^a x-y^2,x^3)\) is retained in
[quasiprimitive residual cycles](../synthesis/quasiprimitive_residual_cycles.md).

## A positive second defect is locally realizable

The necessary \(D_2\ne0\) in the \(l=7\) row cannot be excluded
from finite flatness, the complete-intersection property and sole reduced
support alone. In characteristic zero or \(p\ge7\), put
\[
\begin{aligned}
 R&=k[[t]],\qquad D=t^4+v,\\
 G&=Du+tv^2,\\
 F&=u^4-v^5+t^5u^3-2t^6u^2v-3t^3uv^3,\\
 B&=R[[u,v]]/(F,G).
\end{aligned}
\]
This is a finite flat rank-nine complete intersection with reduced support
\(C=\operatorname{Spec}R\) and generic fiber \(k((t))[v]/(v^9)\).
Its exact saturated multiplication-divisor profile is
\[
 \boxed{(D_0,\ldots,D_8)=(0,0,3,4,6,8,9,12,12)[0].}
\]
In particular \(D_2=3[0]\), \(T=6[0]\), and the total ordinary-layer
torsion has length 54. The common first-normal divisor is \(B_1=4[0]\).
This example distinguishes \(B_1\), \(D_2\) and \(T\) concretely.

For verification, on the generic fiber substitute
\(u=-tv^2/D\). Exact expansion gives
\[
 D^4F=-v^9.
\]
Equivalently \(D^4F+v^9\) is a multiple of \(G\) in the polynomial
ring; the remainder vanishes identically. Thus \(v\) is nilpotent on
the generic fiber, \(D\) is invertible there, and that fiber is exactly
the asserted curvilinear algebra, with no additional generic support.
At \(t=0\) the ideal is \((uv,u^4-v^5)\), of colength nine with basis
\[
 1,u,u^2,u^3,u^4,v,v^2,v^3,v^4.
\]
This makes \(B\) finite over the complete ring \(R\). The two defining
equations and \(t\) form a system of parameters in the regular
three-dimensional ambient ring; hence they form a regular sequence.
In particular \(B\) is a complete intersection and \(t\) is a
nonzerodivisor, proving \(R\)-freeness of rank nine. Injection into the
generic fiber shows \(u,v\) are nilpotent, while \(B/(u,v)=R\),
proving the sole reduced support assertion.

An adapted basis gives the complete saturated flag without an assumed
monomial-generation rule:
\[
\begin{array}{c|l|l}
 i&b_i\text{ in }B&b_i\text{ on the generic fiber}\\ \hline
 0&1&1\\
 1&v&v\\
 2&u&-tv^2/D\\
 3&v^2+t^3u&v^3/D\\
 4&u^2&t^2v^4/D^2\\
 5&v^3-t^4b_3-t^2u^2&v^5/D^2\\
 6&u^3&-t^3v^6/D^3\\
 7&v^4-t^6u^2-2t^4b_5+tu^3&v^7/D^3\\
 8&u^4&t^4v^8/D^4
\end{array}
\]
Their reductions are the displayed special-fiber basis in a different
order, so they form an \(R\)-basis. Their distinct first generic
orders imply
\(B\cap v^iB_{k((t))}=\sum_{j\ge i}Rb_j\).
The leading coefficients have \(t\)-valuations
\((0,0,-3,-4,-6,-8,-9,-12,-12)\). Since \(v\) generates the first
quotient, these are exactly the negatives of the multiplication-divisor
coefficients asserted above.

The carrier is already normal and ADE. Indeed the coordinate change
\[
 V=v+t^4,\qquad U=u+tV-2t^5
\]
gives \(G=UV+t^9\), an \(A_8\) surface, and the marked smooth curve
has \(U=-t^5,V=t^4\). Its first symbol is \(t^4u\), whereas \(F\)
has no linear normal term. The curve therefore occupies an interior
marked position, rather than the end-position model used in the reduced
common-divisor proof.

Independent reconstruction accepted the exact elimination, finite flat
complete-intersection and support assertions, adapted basis, full divisor
profile and carrier coordinate change. The algebraic identities also
passed direct exact coefficient checks. This is a local counterexample to
an automatic zero-second-defect assertion, not an embedded global sextic
pair or a realization of a full global divisor profile. A global obstruction
must use additional embedding or equation information.
