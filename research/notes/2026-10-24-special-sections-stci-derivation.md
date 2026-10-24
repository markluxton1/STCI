# Special plane and line sections: independent STCI derivation

Date: 2026-10-24. Author: independent agent `stci_sections`.

**Status:** supporting research proposal, not a canonical result or promotion.
All claims below concern the fixed embedded curve
\(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of characteristic
zero. The section-length arguments work more generally. Their elementary proofs
are included so that the new geometric interpretation does not depend on a
historical bound on common normal directions.

## 1. Proper intersections first; sole support is an additional hypothesis

Let \(F,G\) have positive degrees \(d,e\), vanish on \(C\), and have no common
surface component. Then \(Z=V_+(F,G)\) is a pure one-dimensional
Cohen--Macaulay complete intersection. Write

\[
[Z]=m[C]+R,\qquad de=4m+\deg R,
\]

where \(R\) is effective and has no component \(C\). The integer \(m\) is
the length of the generic transverse algebra at \(C\). If a plane \(H\)
contains no component of \(Z\), intersection with \(H\) gives the effective
zero-cycle

\[
[Z\cap H]=m[C\cap H]+R\cdot H.
\tag{1}
\]

Residual components may meet \(H\) at points of \(C\); their contribution
must not be discarded on the basis of support of a single section.
If \(H\) contains a residual component, its restricted equations have an
improper intersection, and this finite-section formula is inapplicable.

Now impose the additional hypothesis \(Z_{\mathrm{red}}=C\). It implies
\(R=0\), \(de=4m\), and every plane is a proper section, because \(C\)
is nonplanar. Neither restricted equation \(F_H,G_H\) vanishes identically:
otherwise a positive-degree plane curve \(V_H(G_H)\), or the whole plane,
would lie in \(Z\). They have no common plane curve component either.

## 2. Exact local lengths of the plane complete intersections

For every \(p\in C\cap H\), put
\(r_p=\operatorname{ord}_p(H|_C)\). Then

\[
\boxed{
 i_p(F_H,G_H)
 =\operatorname{length}\mathcal O_{\mathbf P^3,p}/(F,G,H)
 =m r_p.}
\tag{2}
\]

Here the length is that of the actual zero-dimensional plane complete
intersection, not merely a total degree. For completeness, let
\(B=\mathcal O_{Z,p}\) and let \(h\) define \(H\). The ring \(B\) is
one-dimensional Cohen--Macaulay, its only minimal prime is the ideal of
\(C\), and \(h\) is a nonzerodivisor. Use a prime filtration of \(B\)
and additivity of the finite Euler characteristic
\(\chi_h(M)=\ell(M/hM)-\ell(\ker h|_M)\).
Factors supported at the closed point have Euler characteristic zero.
The unique dimension-one factor \(\mathcal O_{C,p}\) appears \(m\)
times and has Euler characteristic \(r_p\). This proves (2). Standard
intersection theory identifies the same length with local plane intersection
multiplicity; see [Stacks, tag 0B06](https://stacks.math.columbia.edu/tag/0B06).

Consequently an ordinary osculating plane with section \(3p+\iota(p)\)
gives lengths \(3m,m\); a hyperosculating plane gives one local length
\(4m=de\); and a nondegenerate bitangent plane with section \(2p+2q\)
gives lengths \(2m,2m\). Any other special plane uses its actual divisor
\(H|_C\) in the same formula.

This does **not** identify the plane ideal or the Hilbert function. For a local
test, set \(C=V(x,y)\subset\operatorname{Spec}k[[t,x,y]]\) and
\(H_r=V(y+t^r)\). The supported CIs

\[
J_1=(x,y^4),\qquad J_2=(x^2,y^2)
\]

both have generic length four and give plane-section length \(4r\), but
their plane algebras are
\(k[[t]]/(t^{4r})\) and \(k[[t,x]]/(x^2,t^{2r})\). For \(r\ge2\)
the embedding dimensions are respectively one and two.

## 3. Tangencies that do follow, and singularities that do not

For two plane germs of multiplicities \(a_p,b_p\), equation (2) implies
\(a_pb_p\le mr_p\). Equality holds exactly when their tangent cones
have no common linear factor. The number \(mr_p\) alone does not specify
\(a_p,b_p\), smoothness, or a tangent cone.

If both plane germs are smooth, they have a common tangent precisely when
their intersection multiplicity is greater than one. If an ambient surface
\(X\) is smooth at \(p\), its tangent plane contains \(T_pC\). For a
plane \(H\supset T_pC\) with \(H\ne T_pX\), the section \(X\cap H\)
is smooth with tangent line \(T_pC\). If both surfaces satisfy these
conditions, the plane sections share that tangent and have the exact contact
order \(mr_p\). When \(H=T_pX\), the plane section can be singular;
its tangent cone requires additional information.

Concentration at a hyperosculating point does not force an ambient surface
singularity. The local model

\[
F=x,\quad G=x+y^m,\quad H_r=y+t^r
\tag{3}
\]

has two smooth ambient surfaces, sole reduced support \(C\), and two smooth
plane curves
\(x=0\), \(x+(-1)^m t^{rm}=0\) with contact exactly \(rm\).
It realizes every \(r\), including \(r=4\). This is a local test, not
a projective realization for the fixed quartic.

There is nevertheless a standard **global smooth-carrier restriction**.
If \(X\) were smooth at every point of \(C\), then in a neighborhood
of \(C\) the Cartier divisor cut out by \(G\) on \(X\) would be
\(mC\). Restriction to \(C\) would give
\(4e=m\deg N_{C/X}=m(14-4d)\), where the last equality follows from
the normal sequence and the accepted degree \(\deg N_{C/\mathbf P^3}=14\).
Combining with \(de=4m\) gives
\(16=d(14-4d)\), impossible: for positive integral \(d\) the right side
is at most twelve. Thus **every hypothetical defining surface is singular
somewhere on \(C\)**. This standard adjunction calculation is stronger
than the bare plane-section length identity; it locates neither those
singularities nor a new all-degree obstruction. The local smooth examples
above show why it is essential that smoothness was assumed along the whole
projective curve.

If \(m>1\), the first conormal symbols satisfy
\(\sigma_F\wedge\sigma_G=0\) identically on \(C\): independent
linear terms would generate the maximal ideal of the transverse regular
local ring and give generic length one. At a point where both symbols are
nonzero, the ambient tangent planes therefore coincide. If a symbol is zero,
the corresponding surface is singular there; wedge vanishing in this case
does not describe two smooth tangent surfaces. Entirely thick equations have
zero first symbols and supply no first-order tangent-plane field.

## 4. Lines have a different intersection problem

Let \(L\) be a line, and \(Z_L=C\cap L\) its finite intersection scheme.
If neither restriction vanishes, then

\[
\gcd(F|_L,G|_L)\ \text{has divisor at least }Z_L,
\qquad \deg\gcd(F|_L,G|_L)\le\min(d,e).
\]

Under sole support its support is exactly the support of \(Z_L\); its
multiplicities can exceed those of \(Z_L\). Individual restricted forms
can have additional zeros away from \(C\), provided these zeros are not
common. If \(L\subset X\), then \(L\not\subset Y\) and the degree
\(e\) divisor of \(G|_L\) is entirely supported on \(C\cap L\).
For a line meeting \(C\) only at one point, this is an \(e\)-fold root.
In particular it applies to a contained endpoint tangent trisecant.

There is no line analogue \(\ell(Z\cap L)=m\ell(C\cap L)\) in general.
Even locally, in model (3) a line germ with normal coordinates
\(x=t^r,y=t^r\) gives length \(r\), while the reduced curve intersection
has length \(r\) and the transverse thickness is \(m\). This germ need
not be a linear line in the straightened coordinates; it demonstrates the
missing local algebra implication. For an actual transverse line, take
\(t=y=0\), giving length one for every \(m\).

## 5. Residual divisors on the unique quadric

Write

\[
Q=V(q),\quad q=x_0x_3-x_1x_2,\quad
[x_0:x_1:x_2:x_3]=[ac:ad:bc:bd].
\]

The equation of \(C\) on \(Q\cong\mathbf P^1\times\mathbf P^1\)
is \(c_C=bc^3-ad^3\), so \(C\) has class \((1,3)\) and a hyperplane
has class \((1,1)\). A fibre of the first projection, class \((1,0)\),
is a trisecant; a fibre of the second, class \((0,1)\), is unisecant.

Under sole support, \(q\) cannot divide \(F\): otherwise
\(V_Q(G|_Q)\) would be supported only on \(C\), forcing
\((e,e)=b(1,3)\), which is impossible for \(e>0\). The same holds
for \(G\). Hence there are well-defined effective divisors

\[
\operatorname{div}F_Q=aC+R_F,\quad R_F=(d-a,d-3a),\quad
1\le a\le\lfloor d/3\rfloor,
\]

and similarly \(\operatorname{div}G_Q=bC+R_G\). The orders \(a,b\)
are orders on \(Q\), not automatically the ambient normal orders.
The residual divisors have no common component, since neither contains
\(C\) and any other common curve would be a residual component of \(Z\).
Their proper zero-dimensional intersection is supported on \(C\), with

\[
\boxed{\deg(R_F\cdot R_G)
=2de-4(db+ea)+6ab\ge0.}
\tag{4}
\]

Also \(R_F\cdot C=4d-6a\), and similarly for \(G\). These are
necessary divisor-class and support constraints. They provide no automatic
scheme description of \(R_F\cap R_G\), nor an equality with a first-normal
defect divisor without further hypotheses. The promoted
[STCI-R-0019](../results/quasiprimitive_residual_cycles.md) supplies a stronger
length-cycle identity only with its finite-flat curvilinear algebra, saturated
invertible flag, nonzero generic auxiliary first class, and proper residual
intersection hypotheses. We do not assume those hypotheses here.

If \(d=3a\), then \(R_F=(2a,0)\) is a union of trisecant fibres.
On each fibre component \(L\), the mate restricts to a polynomial all of
whose zeros lie on the degree-three scheme \(L\cap C\). At a generic
fibre these are three distinct points and the zero multiplicities are an
integer allocation of \(e\); at a ramified endpoint fibre all \(e\)
zeros lie at one point. These are interpolation constraints, not an
emptiness proof.

## 6. A precise normal-direction coincidence count

Use the accepted conormal degree/splitting
\(E=N^*_{C/\mathbf P^3}=\mathcal O(-7)^2\) from
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md), without
reproving it. A first symbol of a degree-\(d\) form is a section of
\(E(4d)\). If nonzero generically, write its common zero divisor as
\(A_F\), with degree \(a_F\); its saturated direction line is
\(L_F=\mathcal O(a_F-4d)\subset E\).

The osculating plane at affine parameter \(u\) has coefficient vector
\([-u^4:2u^3:-2u:1]\), since its restriction to \(C\) is
\((t-u)^3(t+u)\). Homogenizing gives a degree-four, everywhere nonzero
plane vector. A plane tangent to \(C\) gives an element of \(E(4)\),
so this field defines an everywhere saturated line
\(L_{\rm osc}=\mathcal O(-8)\subset E\).

If \(L_F\ne L_{\rm osc}\) generically, the wedge of their two
inclusions has an effective coincidence divisor of degree

\[
\boxed{4d-6-a_F.}
\tag{5}
\]

This follows directly from
\(\deg\operatorname{Hom}(L_F\otimes L_{\rm osc},\det E)
=-14-(a_F-4d)-(-8)\).
At a singular point the count uses the saturated limiting field, not an
actual smooth tangent plane. If the fields agree identically, their wedge
is identically zero and there is no finite coincidence divisor.

For two nonzero proportional first symbols, saturation yields the same
line and therefore
\(4d-a_F=4e-a_G\). Formula (5) then gives the same coincidence divisor
for both equations. This is a global compatibility identity involving actual
first-normal data; special plane-section cycle identities alone do not
determine those data.

## 7. Explicit counterexample to a naive bound of two

Any proposed universal bound of two on such coincidences needs hypotheses
beyond the special-plane geometry. Here is an exact test with residual curves:

\[
\begin{aligned}
F&=x_0^2x_2-x_1^3+x_1x_3^2-x_2^3,\\
G&=x_0F+q^2.
\end{aligned}
\tag{6}
\]

The cubic \(F\) is smooth at every point of \(C\). At finite parameter
\(u\), its gradient is

\[
(2u^3,-3u^2+u^8,1-3u^6,2u^5),
\]

which cannot vanish: if its first coordinate is zero, then \(u=0\) and
the third is one. At infinity the gradient is \(dx_1\). The first
symbols of \(F,G\) are proportional generically. Their saturated common
plane field coincides with the osculating field at exactly the six simple
points \(u^6=-1\), in agreement with (5) for \(d=3,a_F=0\).

This is **not** an STCI counterexample. Indeed

\[
(F,G)=(F,q^2),\qquad
F|_Q=(a^2-b^2)(bc^3-ad^3).
\]

Its support is \(C\) together with the two distinct trisecant fibres
\(a^2-b^2=0\). At the generic point of \(C\), the gradients of
\(F,q\) are independent, so \(m=2\); the residual cycle has degree
\(12-4\cdot2=4\), namely twice each of the two lines.
Thus (6) refutes an inference from proportional first symbols and the
incidence geometry to a bound of two. It does not refute a theorem retaining
additional supported-CI, saturation, degree, or defect hypotheses.

## 8. Moving sections and the remaining global question

For the osculating-plane family over its parameter \(B\cong\mathbf P^1\),
the incidence subscheme \(\mathcal D_Z\subset Z\times B\) is a relative
effective Cartier divisor and is finite flat of degree \(de\) over \(B\):
all fibres are finite, the product is flat, and the section is a
nonzerodivisor on every fibre. On \(C\times B\), its reduced-carrier
equation defines the divisor \(3\Delta+\Gamma_\iota\). Its fundamental
cycle after replacing \(C\) by \(Z\) is
\(m(3\Delta+\Gamma_\iota)\). In particular the hyperosculating
collision of lengths \(3m\) and \(m\) is compatible with flatness.

The open issue is whether this family, its actual embedded scheme structure,
and the normal-direction/divisor data can be shown incompatible with global
homogeneous equations in all remaining degrees. Neither (2), (4), (5), the
flat family, nor the counterexample tests prove such incompatibility.
The established quartic-carrier exclusion and its scope are retained from
[STCI-R-0001](../results/quartic_carrier_exclusion.md); no part of that
accepted proof or the accepted normal-bundle computation was rerun here.
