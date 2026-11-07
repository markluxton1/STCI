# Quasiprimitive multiplicity five: formal and global-source obstructions

This owner retains the complete numerical classification, corrected moving-coordinate extension calculation, exact type-B Fitting divisor and conditional ambient finite-jet method for a hypothetical degree(4,5) pair on fixed C0 in characteristic zero. The global quartic-carrier theorem R-0001 closes the existence question for this degree pair, but these arguments retain distinct mechanisms for multiple structures, nonflat extension corners and global jet images. They are not reopened as current arbitrary-mate cases.

The numerical classification assumes actual sole support and a generically curvilinear multiplicity-five complete intersection; its two types are necessary, not realizations. The formal proof must retain every chart, epimorphism and finite-flatness condition. The ambient linear method has a separate regular-ratio assumption, explicitly disproved for arbitrary pairs by the local model below. Current authority for arbitrary quartic carriers remains [R-0001](../results/quartic_carrier_exclusion.md).


## the exact quasiprimitive \((4,5)\) classification

<a id="p-016"></a>

For the monomial quartic, the known \((4,4)\) exclusion and the
Craighero--Gattazzo exclusion of every cubic carrier made \((4,5)\) the first
unresolved degree pair before [the full formal extension calculation](#p-025) and [the degree-pair proof assembly](#p-040) closed it.  More generally,
[the low-degree thick-carrier lemma](../synthesis/formal-normal-intersection.md#low-degree-surfaces-singular-along-the-whole-quartic) says that both a quartic and a
quintic carrier have generic normal order one.  [the coprime-symbol resultant criterion](../synthesis/formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant) makes their first normal
forms proportional, so a hypothetical complete intersection of generic
multiplicity

\[
 \frac{4\cdot5}{\deg C}=5
\]

is quasiprimitive.

The Bănică--Forster filtration, together with Boratyński's lci duality for a
quasiprimitive multiplicity-five curve, has graded pieces

\[
 \mathcal O_C,\quad L,\quad L^2(D),\quad
 L^3(2D),\quad L^4(2D),
\]

where \(D\) is effective.  Hence, writing \(l=\deg L\) and \(d=\deg D\),

\[
 \chi(\mathcal O_X)=5+10l+5d.
\]

A \((4,5)\) complete intersection has arithmetic genus

\[
 1+\frac{20(4+5-4)}2=51,
\]

so \(\chi(\mathcal O_X)=-50\), and therefore

\[
 2l+d=-11.
\]

The first layer is a line-bundle quotient
\(N_C^*=\mathcal O(-7)^2\twoheadrightarrow L\), which forces \(l\ge-7\),
while \(d\ge0\).  There are exactly two solutions:

\[
 \boxed{(l,d)=(-7,3)\quad\text{or}\quad(-6,1).}
\]

The [primitive-triple obstruction](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#primitive-triples-on-smooth-rational-quartics) does not by itself remove these cases:
the positive defect divisor \(D\) is precisely the finite locus where both
carriers may be singular.  Jaffe's disjoint-singular-locus theorem likewise
shows only that such a pair must have common singular points.  Thus the two
displayed types, rather than arbitrary multiplicity-five structures, are the
correct finite formal-neighborhood target.

## the type-B Fitting divisor is exactly \(2D\)

<a id="p-038"></a>

Let \(X=V(F_4,F_5)\) be a hypothetical type-B multiplicity-five complete
intersection supported on \(C=C_0\).  Put

\[
 J=\mathcal I_C,\qquad I=\mathcal I_X.
\]

The first-normal map is

\[
 \phi:I/JI\longrightarrow J/J^2=N_C^*.
\]

It has generic rank one.  In a local conormal basis adapted to the primitive
horizontal line, if the two first forms are \(h\ell,k\ell\), its matrix is

\[
 \begin{pmatrix}h&k\\0&0\end{pmatrix}.
\]

Thus the divisor-valued Fitting ideal is

\[
 \operatorname{Fitt}_1(\operatorname{coker}\phi)
 =(h,k)=O_C(-A),
\]

where \(A=(h)_0\wedge(k)_0\).  The index is \(1\), not \(0\), because the
cokernel has generic rank one.  This Fitting ideal is invariant under all
source, target, and primitive-line basis changes.

For type B the filtration is

\[
 O_C,\quad L,\quad L^2(D),\quad L^3(2D),\quad L^4(2D),
\]

with ideals

\[
 J=I_0\supset I_1\supset I_2\supset I_3\supset I_4=I.
\]

At a point where \(D\) has local equation \(a=t^d\), the corrected
Bănică--Forster local form is

\[
 J=(x,y),\qquad I_1=(x,y^2),\qquad B=ax-y^2,
\]

\[
 I_3=(P,Q,R),\qquad
 P=aB-xy,\quad Q=yB,\quad R=x^2.
\]

Modulo \(J^2\), only \(P\equiv a^2x\) remains, so

\[
 \operatorname{Im}(I_3\to J/J^2)=a^2M,\qquad M=I_1/J^2.
\]

The available typeset reprint prints \(y(a-y^2)\) for the second generator,
dropping the \(x\) in \(y(ax-y^2)\).  Read literally that ideal is not flat
and is generically multiplicity one, whereas the corrected \(Q=yB\) is forced
by the preceding extension construction and gives length four.  All uses here
refer to this flat corrected formula.

The final extension is an epimorphism

\[
 \beta:I_3/JI_3\twoheadrightarrow L^4(2D),
 \qquad \ker\beta=I_4/JI_3,
\]

compatible with the natural inclusion \(L^4\hookrightarrow L^4(2D)\).  The
exact identity

\[
 y^4=a^2R-yR-xP-yQ
\]

gives \(\eta(y^4)=a^2\bar R\) modulo \(JI_3\).  Compatibility and cancellation
in the locally free target imply \(\beta(\bar R)\) is a unit.  If
\(\beta(\bar P)=\alpha\beta(\bar R)\), then a lift
\(T\in I_4\) of \(\bar P-\alpha\bar R\) satisfies

\[
 T\equiv P\equiv a^2x\pmod{J^2}.
\]

Together with \(I_4\subset I_3\), this proves the equality

\[
 \operatorname{Im}(I_4\to J/J^2)=a^2M.
\]

It globalizes to \(\operatorname{Im}\phi=M(-2D)\), so locally

\[
 \operatorname{coker}\phi\simeq O_C\oplus O_C/(a^2),\qquad
 \operatorname{Fitt}_1(\operatorname{coker}\phi)=O_C(-2D).
\]

Comparison with \(O_C(-A)\) yields the scheme-theoretic identity

\[
 \boxed{A=2D.}
\]

Since type B has \(\deg D=1\), P-031's notation becomes

\[
 \boxed{c=2,\qquad p_{\mathrm{pole}}=6,\qquad \deg Z=10.}
\]

Thus the earlier conjectural direction \(A\le D\) was false; the correct
relation is \(D<A=2D\), with equal support.  This is a sharp first-normal
structural identity; by itself it is a reduction rather than an exclusion.
The separate higher-neighborhood argument in [the full formal extension calculation](#p-025), summarized in [the degree-pair proof assembly](#p-040),
excludes the degree pair.

## formal-neighborhood exclusion of the two \((4,5)\) types

<a id="p-025"></a>

The Bănică--Forster transition calculation was carried through separately for
the two types in [the two-type classification](#p-016) on the explicit curve \(C_0\).

For type A, \((\deg L,\deg D)=(-7,3)\), the lower extension and epimorphism
conditions exhaust all parameter strata.  The unique epimorphic route through
multiplicity four has final obstruction in \(H^1(O(-9))\) with coordinates

\[
 \left(-\frac{15}{512},-\frac5{256},\frac5{128},-\frac5{64},
 \frac5{32},-\frac5{16},\frac58,\frac{15}{4}\right),
\]

which is nonzero.  Therefore type A cannot support a \((4,5)\) complete
intersection on \(C_0\).

For type B, \((\deg L,\deg D)=(-6,1)\), a crucial correction is that transition
coefficients must be evaluated at the moving ambient coordinate

\[
 W=\frac{z^3+a}{z^4+b},
\]

not frozen at \(1/z\).  On the dense chart \(b_0b_1\ne0\), normalized by
\(b_0=b_1=1\) with parameters \((r,s)=(a_0,a_1)\), the second-neighborhood
class has Laurent coefficients \(c_1,c_2,c_3\).  Its required rank-one
condition is

\[
 c_1c_3-c_2^2=0.
\]

Exact elimination through the next extension gives the eliminant

\[
 (2s-1)^3(2s+1)(12s^2+20s+11)^3.
\]

After the corresponding chart and epimorphism checks, the only dense-chart
point reaching multiplicity four is

\[
 (r,s)=(0,-1/2).
\]

At that point one may take

\[
 \delta_U=-4z,\quad\delta_V=-4,
\]

\[
 \gamma_U=\tfrac32z^2+3z+2,\quad\gamma_V=0,
\]

\[
 \rho_U=-(36z^4+108z^3+136z^2+72z+16),\quad\rho_V=0.
\]

The required final generator on the other chart is not the old \(E_V\) but
\(F_V=-64m_V\).  Put

\[
 Q=3z^2+6z+4
\]

and

\[
\begin{aligned}
 P={}&81z^8+486z^7+1341z^6+2160z^5+2204z^4\\
    &+1464z^3+656z^2+224z+64.
\end{aligned}
\]

Exact moving-\(W\) reduction modulo the multiplicity-four ideal gives the
final cocycle

\[
 h_4=-\frac{8P(z)}{Q(z)z}.
\]

If

\[
 R=81z^7+486z^6+1341z^5+2160z^4+2204z^3
   +1464z^2+608z+128,
\]

then \(P-16Q=zR\), so

\[
 h_4+\frac{128}{z}=-\frac{8R}{Q}.
\]

On the cover \(D(Q)\subset\mathbb A^1_z\) and
\(\mathbb P^1\setminus\{z=0\}\), the right-hand term is regular on the first
chart and no second-chart coboundary can remove \(z^{-1}\).  Hence

\[
 [h_4]=[-128z^{-1}]\ne0\quad\text{in }H^1(O(-12)).
\]

This independently audited computation excludes the unique dense survivor.

On the boundary \(b_0=0\), normalize \(a_0=b_1=1,a_1=t\).  The exact
second-neighborhood rank equation is

\[
 q(t)=1-8t^2+12t^4-72t^6=0.
\]

A separate exact moving-\(W\) implementation through the next neighborhood
gives a class in \(H^1(O(-7))\) whose first coordinate is

\[
 H_1=-24t(36t^4+3t^2+1).
\]

With \(x=t^2\), the identity

\[
 3(20x+3)(1-8x+12x^2-72x^3)
 +4(30x^2-3x+2)(36x^2+3x+1)=17
\]

shows that \(H_1\) is a unit on the full rank-one boundary scheme in
characteristic zero.  Thus every point with \(b_0=0\) is excluded.  The
durable script [the boundary transition verifier](../computations/verify_typeb45_boundary.py) reproduces the full
moving-frame calculation and all six Cech coordinates.

One former conclusion was nevertheless false: the coordinate-reversing
involution does not simply reverse the quotient coefficients in the canonical
split frames.  Its actual action is, up to common scale,

\[
 (a_0,a_1,b_0,b_1)\longmapsto
 \left(\frac{b_1}{2},\frac{b_0}{2},2a_1,2a_0\right).
\]

It sends the part of \(b_1=0\) with \(a_0\ne0\) into the now-excluded dense
chart, but preserves the genuine corner

\[
 a_0=b_1=0,\qquad a_1b_0\ne0.
\]

Normalize \(b_0=1,a_1=t\).  Its second-neighborhood class has

\[
 c_1=c_3=0,\qquad
 c_2=\frac{(2t+1)(12t^2+4t+3)}8.
\]

Therefore exactly three rank-zero parameters remain:

\[
 \boxed{t=-\frac12\quad\text{or}\quad12t^2+4t+3=0.}
\]

The involution fixes the first and exchanges the two quadratic roots by
\(t\mapsto1/(4t)\).  At each of these three parameters the raw
second-neighborhood representative \(h_2\) vanishes identically, not merely
in cohomology.  Let \(\delta\in H^0(O(1))\) be any nonzero proposed killing
section for the double-to-triple extension.  In the exact moving frames the
compatible correction satisfies

\[
 \delta_Uh_2+\gamma_U=z^{-3}\gamma_V.
\]

Thus \(\gamma_U=z^{-3}\gamma_V\) is a global section of \(O(-3)\), so
\(\gamma_U=\gamma_V=0\).  Every nonzero section of \(O(1)\) has a zero
\(P\).  At that point the proposed transverse triple has ideal

\[
 (m\ell,m^2,\ell^3),
\]

whose quotient has basis \(\{1,m,\ell,\ell^2\}\) and length four.  Away from
\(P\), \(\delta\) is a unit and the quotient has the required basis
\(\{1,\ell,\ell^2\}\) and length three.  The unavoidable length jump means
that the extension map is not epimorphic and the proposed triple is not flat.
No one of the three rank-zero corner points therefore extends to an
admissible triple.  This closes the corner and excludes type B on all charts.

The durable script [the rank-zero corner verifier](../computations/verify_typeb45_corner.py) reproduces the
full moving-\(W\) second-order coefficient, the rank-zero factorization, and
the special-fiber length calculation.  Its finite-degree \(\gamma\) and
hard-coded monomial checks are only witnesses; the exhaustive proof is the
line-bundle argument \(H^0(O(-3))=0\) and the displayed quotient basis.  The
older frozen-frame `typeb_generic.py` remains invalid,
and the rejected simple coefficient-reversal argument must not be reused.

## a conditional ambient finite-jet reduction for \((4,5)\)

<a id="p-026"></a>

There is a complementary reduction directly in the ambient quartic and
quintic coefficient spaces.  In the balanced frame \((U,V)\), a quartic first
normal form is

\[
 P(z)U+Q(z)V,\qquad \deg P,\deg Q\le9.
\]

Its image has rank 17 and is cut out by

\[
 P_1=2Q_2,\qquad P_4=2Q_5,\qquad P_7=2Q_8.
\]

The quintic first-normal map is surjective onto
\(H^0(O(13))^2\), with seven-dimensional kernel \(qI_C(3)\).  [the two-type classification](#p-016) becomes
the following two quartic strata:

\[
 \begin{array}{c|c|c}
 \text{type}&L_1&\gcd(P,Q)\text{ degree}\\\hline
 A&O(-7)&9\\
 B&O(-6)&8.
 \end{array}
\]

Write the proportional first normal forms as \(f_1=hL\) and \(g_1=kL\).
The previous version asserted, without proving the necessary vertical-divisor
inequality, that after subtracting an ambient linear multiple of the quartic a
genuine mate must satisfy

\[
 g_1=z^2f_1.
\]

That assertion is valid only on the sublocus where the rational quotient
\(k/h\) is regular and can be normalized by ambient linear sections.  It is
not automatic.  The local multiplicity-five model

\[
 F=tu+v^5,\qquad G=u
\]

has radical \((u,v)\), constant transverse length five, and first-normal
ratio \(1/t\).  Proper residual intersection on the quadric constrains the
total intersection divisor but does not force \(h\mid k\); multiplicity may
concentrate at vertical order jumps.  Consequently the universal P-026
reduction is disproved, while the calculation below remains exact on its
regular-ratio sublocus.

On that sublocus the factor \(z^2\) represents the unique missing section in
\(H^0(C,O_C(1))/H^0(\mathbf P^3,O(1))\).  Once a quintic with this first form
is chosen, all others are obtained by adding seven coefficients in
\(qI_C(3)\).  Eliminating the quartic formally, contact at least five is
equivalent to a finite linear system in those seven variables, with the
coefficients of the transverse terms \(t^2,t^3,t^4\) as equations.  The
conditional problem is therefore equality of the ranks of this matrix and its
augmented matrix, including lower-rank boundary strata.  The missing
nonregular-ratio strata require a separate vertical-divisor parameterization.

The exact verifier proves three family exclusions by explicit augmented
minors:

\[
 F=x_1A+\lambda q^2:\quad 2\lambda^3,
\]

\[
 f_1=(z^9+1)U:\quad -72,
\]

\[
 f_1=(z^8+1)(U+zV):\quad -48.
\]

Thus every nonreducible member of each displayed family in the normalized
sublocus fails order-five contact.  These certificates neither establish the
normalization for an arbitrary pair nor replace elimination within the
conditional strata.  The durable script is
[the conditional ambient-jet verifier](../scratch/degree6/verify_mixed45_reduction.py), with recorded SHA-256
`862ec150664459fc94187164bcaa1d25e87c5f815e589fff1608a28efc6a89d5`.

## no degree-\((4,5)\) presentation of \(C_0\) in characteristic zero

<a id="p-040"></a>

Let the base field be algebraically closed of characteristic zero.  Suppose
that quartic and quintic forms \(F,G\) cut out \(C_0\) set-theoretically.
They have no common surface factor, so \(X=V(F,G)\) is an unmixed
complete-intersection curve of degree \(20\), supported on the degree-four
curve \(C_0\).  Its generic multiplicity along \(C_0\) is therefore five.

By [the low-degree thick-carrier lemma](../synthesis/formal-normal-intersection.md#low-degree-surfaces-singular-along-the-whole-quartic), neither degree-\(<6\) carrier can be thick along all of \(C_0\);
[the coprime-symbol resultant criterion](../synthesis/formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant) makes their first normal forms proportional, so the generic transverse
algebra is curvilinear of length five.  The multiplicity-five lci structure
is consequently quasiprimitive.  [the two-type classification](#p-016)'s
exhaustive Bănică--Forster/Boratyński filtration and Euler-characteristic
calculation leave exactly the two numerical types

\[
 (\deg L,\deg D)=(-7,3)\quad\text{or}\quad(-6,1).
\]

[the full formal extension calculation](#p-025) excludes the first type by its terminal nonzero
\(H^1(O(-9))\) class.  It excludes the second on a complete parameter-chart
cover.  If the quotient is represented by
\((a_0+a_1z,b_0+b_1z)\), epimorphy requires
\(\Delta=a_0b_1-a_1b_0\ne0\).  The cases \(b_0b_1\ne0\), \(b_0=0\),
\(b_1=0,a_0\ne0\), and \(a_0=b_1=0,a_1b_0\ne0\) are respectively the
dense chart, the audited boundary, its involutive image, and the residual
corner.  The unique dense survivor has terminal class
\([-128z^{-1}]\ne0\) in \(H^1(O(-12))\); the \(b_0=0\) boundary has an
obstruction coordinate which is a unit on its rank-one scheme; the
coordinate-reversing involution covers the remaining \(b_1=0,a_0\ne0\)
part; and the three rank-zero points in the residual
\(a_0=b_1=0\) corner fail the required double-to-triple epimorphism and
flatness.

Both exhaustive types are impossible.  Hence

\[
 \boxed{\text{\(C_0\) has no characteristic-zero STCI presentation of
 degrees \((4,5)\).}}
\]

This is a degree-pair exclusion.  It does not rule out a presentation in
higher degrees and therefore is not a proof that \(C_0\) is not an STCI.
It is proved internally here; no novelty or priority claim is made.

## Characteristic boundaries and reusable lessons

The direct local Gorenstein duality, Fitting ideal and finite-flatness mechanisms are algebraic; individual formulas have their stated coefficient restrictions. The characteristic-zero type classification and elimination are not transplanted wholesale to a prime. The type-A final obstruction has a factor5, the type-B chart calculations invert2, and a boundary Bezout identity has constant17; reduction at such primes can change which loci are excluded. Characteristic2 additionally changes the fixed-quartic conormal. The [quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) is the required control alongside the characteristic-zero exclusion.

The examples explain two general failure mechanisms. A cohomologically zero correction may still fail an epimorphism or flatness condition at a zero of its killing section. A globally regular quotient of first-normal symbols is an extra constraint on actual homogeneous sources; proper residual intersection does not make that quotient regular. The exact type-B Fitting divisor2D also prevents replacing an ordinary conormal defect by the smaller filtration divisorD. These observations are useful beyond the closed degree pair, with their exact hypotheses retained.


<a id="2026-10-05-typea-audit"></a>

## Complete type-A quotient and extension calculation

# Independent reconstruction of the type-A multiplicity-five exclusion

Date: 2026-10-05. Scope: characteristic zero, the monomial smooth rational
quartic `C0`, and the Bănică--Forster numerical type

\[
L=O_{\mathbf P^1}(-7),\qquad D_2=D,\quad D_3=D_4=2D,\qquad \deg D=3.
\]

This audit reconstructs all parameter charts and the terminal extension
obstruction underlying the type-A part of P-025. It supplies the previously
missing durable derivation and exact computation. It confirms that exclusion;
it does not establish non-STCI, or a statement about arbitrary multiple-curve
types. The Bănică--Forster description and the numerical classification in
P-016 are the inputs.

The independent verifier is
`research/computations/verify_typea45.py`. It starts with the exact embedded
chart transition, derives the killing-section rank matrix, computes both
exceptional quotient lines, and computes all higher cocycles from the moving
coordinate. Run it with any SymPy-equipped Python, for example:

```
python3 research/computations/verify_typea45.py
```

## 1. Every double-to-triple quotient stratum

Use the P-010 split frames

\[
u=b-\frac32za,\quad v=a,\qquad
u'=\tfrac12a',\quad v'=-3Wa'+2b',
\]

where

\[
W=\frac{z^3+a}{z^4+b},\qquad
 a'=\frac z{z^4+b}-W^3,\qquad
 b'=\frac1{z^4+b}-W^4.
\]

For the finite quotient chart set \(m=u+\theta v,\ell=v\). Both linear
frames have transition \(z^{-7}\). The exact quadratic coefficient is

\[
h_2=3\theta^3z^{-5}-\frac32\theta^2z^{-4}
       +\frac34\theta z^{-3}-\frac38z^{-2}
       \in H^1(O(-7)).
\]

A triple of defect divisor \(D\) requires a nonzero section
\(\delta=d_0+d_1z+d_2z^2+d_3z^3\in H^0(O(3))\) killing this class in
\(H^1(O(-4))\). The three equations, multiplied by \(8/3\), have matrix

\[
\begin{pmatrix}
0&-1&2\theta&-4\theta^2\\
-1&2\theta&-4\theta^2&8\theta^3\\
2\theta&-4\theta^2&8\theta^3&0
\end{pmatrix}.
\]

Its minor on columns \(0,1,3\) is \(-16\theta^4\). For \(\theta\ne0\),
its unique projective kernel is

\[
(d_0,d_1,d_2,d_3)=(0,2\theta,1,0),\qquad
\delta_U=z(z+2\theta),\quad \delta_V=w+2\theta w^2.
\]

Although \(\delta_U\) has affine degree two, it is a section of \(O(3)\):
its divisor includes the point at infinity. The exact identity

\[
\delta_U h_2=6\theta^4z^{-4}-\frac38
\]

uniquely gives

\[
\gamma_U=\frac38,\qquad\gamma_V=6\theta^4,
\qquad \delta_Uh_2+\gamma_U=z^{-4}\gamma_V.
\]

There is no global ambiguity because \(H^0(O(-4))=0\).
The triple ideal on either chart is

\[
I_3=(A,B,C,T),\quad
 A=\delta m-\gamma\ell^2,\quad B=m\ell,
 \quad C=m^2,\quad T=\ell^3.
\]

The required triple epimorphism fails wherever \(\delta=\gamma=0\):
there the transverse ideal is \((m\ell,m^2,\ell^3)\), of colength four
instead of three. This elementary flatness test closes the two exceptional
quotient strata:

* At \(\theta=0\), the rank is two and every killing section is
  \(\delta_U=z^2(d_2+d_3z)\). Its unique gluing solution is
  \(\gamma_U=3(d_2+d_3z)/8,\gamma_V=0\). The remaining homogeneous linear
  factor is a common zero of \(\delta,\gamma\), including the case when
  that zero is at infinity.
* At the missing quotient point use \(m=v,\ell=u\). Direct expansion gives
  \(h_2=3z^{-5}\), so killing requires \(d_2=d_3=0\).
  Then \(\delta_U=d_0+d_1z\),
  \(\delta_V=w^2(d_0w+d_1)\), \(\gamma_U=0\), and
  \(\gamma_V=3(d_0w+d_1)\). Again the homogeneous linear factor supplies
  a common zero.

This covers all of the quotient projective line. For \(\theta\ne0\), the
ambient automorphism

\[
[x_0:x_1:x_2:x_3]\longmapsto[x_0:cx_1:c^3x_2:c^4x_3]
\]

preserves \(C_0\), scales \((z,u,v)\) by \((c,c^4,c^3)\), and carries the
kernel parameter to \(\theta/c\). Taking \(c=\theta\) reduces every
remaining case to \(\theta=1\). Thus the following computation is exhaustive,
not a test of one isolated quotient point.

## 2. The unique triple-to-quadruple extension

Henceforth

\[
\delta_U=z(z+2),\quad\gamma_U=\frac38,
\qquad\delta_V=W+2W^2,\quad\gamma_V=6.
\]

Coefficient functions on the second chart are evaluated at the **moving**
coordinate \(W\), through the necessary normal degree, throughout.
The first normal coefficient of \(A_V\) is
\(p_3\delta_Um\) with \(p_3=z^{-10}\). Let \(q_B,q_T\) be the
coefficients of \(m\ell,\ell^3\) in \(A_V-p_3A_U\).
The prescribed next layer is \(L^3(2D)=O(-15)\), and the intrinsic
conormal map has values

\[
A\mapsto\rho,\quad B\mapsto\gamma\delta,
\quad C\mapsto0,\quad T\mapsto\delta^2.
\]

Its gluing obstruction is

\[
h_3=\frac{q_B\gamma_U\delta_U+q_T\delta_U^2}{p_3}
    =\frac z{16}+\frac14+8z^{-5}-64z^{-6}-144z^{-7}.
\]

There are no coordinates in the nontrivial Cech range
\(z^{-1},\ldots,z^{-4}\) for \(H^1(O(-5))\). The unique local corrections
are

\[
\rho_U=-\frac{z+4}{16},\qquad
\rho_V=8-64w-144w^2,
\qquad\rho_U+h_3=z^{-5}\rho_V(1/z).
\]

Their uniqueness uses \(H^0(O(-5))=0\). Epimorphism holds: at the two finite
zeros of \(\delta_U\), \(\rho_U\) equals \(-1/4,-1/8\), and at infinity
\(\rho_V(0)=8\). Equivalently each chart has
\(\gcd(\delta,\rho)=1\).

The quadruple ideal is generated locally by

\[
E=\delta A-\frac\rho\gamma B
 =\delta^2m-\delta\gamma\ell^2-\frac\rho\gamma m\ell,
\quad F=m^2,\quad H=\delta m\ell-\gamma\ell^3,
\quad J=\ell^4.
\]

Here \(\gamma\) is a unit on both full standard charts. To see that these
are the complete kernel, the syzygies of the row
\((\rho,\gamma\delta,\delta^2)\) are generated by
\((\delta,-\rho/\gamma,0)\) and \((0,\delta,-\gamma)\), since
\((\delta,\rho)=1\). The remaining generators of \(I_C I_3\) also lie
in this ideal. For example

\[
\ell E-\delta H=-\frac\rho\gamma m\ell^2,
\qquad \ell H+\gamma J=\delta m\ell^2.
\]

These two identities and \((\delta,\rho)=1\) put \(m\ell^2\) in the
kernel ideal everywhere. The other normal multiples follow directly.
Thus no extra local ideal generators or parameter strata have been omitted.

## 3. Terminal obstruction and descent across the defect divisor

The fifth layer is \(L^4(2D)=O(-22)\). A local reference conormal map has
values

\[
\phi(E)=0,\qquad\phi(F)=\gamma^2,
\qquad\phi(H)=\rho,\qquad\phi(J)=\delta^2.
\]

Over the generic point these values can be computed by the formal
substitution

\[
m=\frac\gamma\delta\ell^2+
  \frac\rho{\delta^3}\ell^3+
  \frac{\rho^2}{\gamma\delta^5}\ell^4\pmod{\ell^5},
\]

which solves \(E=0\). Evaluate any ideal generator, extract its
\(\ell^4\) coefficient, and multiply by \(\delta^2\).

The denominators in this substitution do **not** remove the defect points
from the proof. All four assigned generator images are regular functions on
the full chart. Every relation among the generators is sent to zero over the
generic point, hence everywhere, because the target line bundle is
torsion-free over the integral base curve. Consequently these assignments
define actual homomorphisms on the full charts, including \(D\). The rational
substitution is only a device for calculating those regular homomorphisms.
Also \(\phi(F)=\gamma^2\) is a unit, so these reference maps are epimorphisms.

The verifier checks that the second-chart generator images satisfy precisely

\[
\phi_U(F_V)=z^{-22}\gamma_V^2,\qquad
\phi_U(H_V)=z^{-22}\rho_V(1/z),\qquad
\phi_U(J_V)=z^{-22}\delta_V(1/z)^2.
\]

Thus their discrepancy factors through the remaining generator line.
The leading coefficient of \(E_V\) relative to \(E_U\) is
\(p_4=z^{-13}\). Since
\(\operatorname{Hom}(O(-13),O(-22))=O(-9)\), the obstruction to gluing the
local maps is

\[
h_4=\frac{\phi_U(E_V)}{p_4}\in H^1(O(-9)).
\]

Exact moving-coordinate computation gives

\[
\begin{aligned}
h_4={}&-\frac5{384}-\frac5{64}z^{-1}-\frac5{96}z^{-2}
 +\frac5{48}z^{-3}-\frac5{24}z^{-4}+\frac5{12}z^{-5}\\
 &-\frac56z^{-6}+\frac53z^{-7}+10z^{-8}
 -\frac{124}3z^{-9}+168z^{-10}+432z^{-11}.
\end{aligned}
\]

The constant term and powers at most \(-9\) are standard Cech coboundaries.
The eight remaining coordinates are

\[
\left(-\frac5{64},-\frac5{96},\frac5{48},-\frac5{24},
 \frac5{12},-\frac56,\frac53,10\right).
\]

This vector is exactly \(8/3\) times the vector in P-025; a common scalar
change of generator frame accounts for the normalization. Its first coordinate
is already nonzero in characteristic zero. Therefore the unique epimorphic
quadruple route cannot extend to the prescribed multiplicity-five type.
Together with the exhaustive quotient analysis, this confirms the type-A
exclusion in P-025 on every chart.

## Validation and limits

The script passed on 2026-10-05 using SymPy and exact rational arithmetic.
It independently reconstructs the entire type-A claim rather than accepting
its previously recorded terminal vector as an input. No approximate
root-finding, finite-field scan, or frozen transition coefficient is used.
The original Bănică--Forster classification of the relevant structures remains
the theoretical input. The conclusion excludes the stated multiplicity-five
type on `C0`; it imposes no bound on other degree pairs.
