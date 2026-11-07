# Residual degree, attachment, and carrier capacity

Fix the embedded quartic \(C=C_0\). For an actual proper homogeneous pair
\(Y=V(F_a,G_b)\), write \([Y]=m[C]+R\) and
\(\delta=\deg R=ab-4m\). Let \(T\) be its **full** \(C\)-primary
component and \(Z\) the residual with no \(C\)-component. Linkage to
reduced \(C\) instead gives \(D_{\rm red}=Y:C\) with cycle \((m-1)[C]+R\).
These three curves must be distinguished before using a degree or attachment
formula.

This chapter consolidates reviewed proofs and counterexamples;
The saturated-flag statement
is [R-0019](../results/quasiprimitive_residual_cycles.md). The fixed-source jet
statement is [R-0025](../results/ci_fixed_sextic_jet_rigidity.md).
The [global-model chapter](residual_global_models.md) owns equation spaces,
prescribed attachments, reverse linkage and the two blowups. The full-primary
attachment-module identity is proved first below. It is not a substitute for
full primary extraction; the deformation account applies it to construction.



## Full-primary equation module and exact attachment divisor

For this section put \(I=I_C\), \(L=I_Y\), and \(J=I_T\), and denote by \(D\) the residual linked to the **full** primary component, \(I_D=L:J\). Thus \([D]=R\) and D has no C-component. This D is distinct from the once-link D_red=Y:C. The primary T and its linked D are pure locally Cohen–Macaulay curves; the empty D case is allowed.

## 2. The attachment module and its exact support

Define coherent \(\mathcal O_C\)-modules

\[
\mathcal E_T=J/IJ,\qquad
\mathcal Q_{Y,C}=J/(L+IJ).
\]

Actual equations give

\[
\rho:\mathcal O_C(-a)\oplus\mathcal O_C(-b)\longrightarrow\mathcal E_T,
\qquad\mathcal Q_{Y,C}=\operatorname{coker}\rho.       \tag{1}
\]

At the generic point of \(C\), \(J=L\); hence \(\rho\) is an isomorphism on the two-dimensional minimal-generator space there. In particular \(\mathcal E_T\) has generic rank two and \(\mathcal Q_{Y,C}\) is torsion.

**Support criterion.**

\[
\operatorname{Supp}\mathcal Q_{Y,C}
=C\cap\operatorname{Supp}D.                          \tag{2}
\]

Indeed, for a closed point \(p\in C\), \(\mathcal Q_p=0\) means \(J_p=L_p+I_pJ_p\). Apply Nakayama to the finite module \(J_p/L_p\), with \(I_p\) inside the local maximal ideal, to obtain \(J_p=L_p\). This says that \(Y\) has only its full marked primary component near \(p\). Conversely that equality gives \(\mathcal Q_p=0\). Since primary decomposition of \(Y\) has no embedded components, equality is equivalent to no residual component passing through \(p\).

For a projective CI, connectedness now gives

\[
\mathcal Q_{Y,C}=0
\quad\Longleftrightarrow\quad
\operatorname{Supp}Y=C.                             \tag{3}
\]

Only this last global equivalence uses connectedness. Formula (2) is local and does not assert every residual component individually meets \(C\).

## 3. Torsion correction to the determinant

Let \(\mathcal T_T=\operatorname{tors}_{\mathcal O_C}\mathcal E_T\), and put

\[
\overline{\mathcal E}_T=\mathcal E_T/\mathcal T_T.
\]

This is a rank-two vector bundle on the smooth \(C\). The induced map

\[
\bar\rho:\mathcal O_C(-a)\oplus\mathcal O_C(-b)
\longrightarrow\overline{\mathcal E}_T
\]

is generically an isomorphism and injective, with determinant

\[
\theta=\det\bar\rho\in
H^0(C,\det\overline{\mathcal E}_T\otimes\mathcal O_C(a+b))
\]

nonzero. The image of \(\rho\) meets \(\mathcal T_T\) trivially, because its composite to the torsion-free quotient is injective. Thus

\[
0\longrightarrow\mathcal T_T\longrightarrow\mathcal Q_{Y,C}
\longrightarrow\operatorname{coker}\bar\rho
\longrightarrow0.                                  \tag{4}
\]

Over each DVR \(\mathcal O_{C,p}\), Smith normal form gives

\[
\boxed{\ \operatorname{length}\mathcal Q_p
=\operatorname{length}(\mathcal T_T)_p+
\operatorname{ord}_p(\theta).\ }                    \tag{5}
\]

Furthermore \(\mathcal T_T\) is supported precisely where \(T\) fails to be locally a complete intersection. If the torsion vanishes at \(p\), \(\mathcal E_T\) is free of rank two there, and its residue fiber shows \(\mu(J_p)=2\). A height-two ideal with these two generators in a regular local ring is a regular sequence. Conversely a local regular-sequence presentation of \(J_p\) makes \(J_p/I_pJ_p\) free of rank two on \(C\), since all Koszul coefficients vanish on \(C\).

Consequently the determinant alone need not detect every attachment: it omits the non-lci contribution from the full primary component.

## 4. Identification with the actual attachment divisor

Classical linkage duality gives

\[
J/L\simeq\omega_D\otimes\omega_Y^{-1}
=\omega_D(4-a-b).
\]

Taking the quotient by \(I\) identifies

\[
\mathcal Q_{Y,C}\simeq
\omega_D(4-a-b)\otimes_{\mathcal O_{\mathbf P^3}}\mathcal O_C.   \tag{6}
\]

One must not replace a canonical module by a structure sheaf without justification. In this particular codimension-two intersection, their **lengths after restriction** agree even when \(D\) is not Gorenstein.

Here is the local proof. Put \(B=\mathcal O_{D,p}\), a one-dimensional CM local ring, and let \(I_CB=(f,g)\). Since \(D\) has no component equal to \(C\), this is primary to the maximal ideal. Over the infinite residue field choose a linear combination of the two generators which is a nonzerodivisor \(f\) on \(B\). Complete it to an invertible change of the two generators. The quotient \(A=B/fB\) is Artinian, and its canonical module is \(\omega_A=\omega_B/f\omega_B\), up to an irrelevant invertible factor. Matlis duality gives

\[
\operatorname{length}(\omega_A/g\omega_A)
=\operatorname{length}\operatorname{Ann}_A(g)
=\operatorname{length}(A/gA).
\]

The second equality is rank-nullity for multiplication by \(g\) on the finite-length module \(A\). Thus (6) implies

\[
\operatorname{length}\mathcal Q_p
=\operatorname{length}\mathcal O_{C\cap D,p}.          \tag{7}
\]

Since every finite subscheme of smooth \(C\) is an effective Cartier divisor, equal pointwise lengths identify their ideal divisors. Write \(\operatorname{div}\mathcal T_T=\sum_p\operatorname{length}(\mathcal T_T)_p[p]\). Combining (5) and (7) gives

\[
\boxed{\ C\cap D=\operatorname{div}\mathcal T_T+\operatorname{div}\theta\ }
                                                               \tag{8}
\]

as **effective divisors on \(C\)**, or equivalently

\[
I_{C\cap D,C}
=\operatorname{Fitt}_0(\mathcal Q_{Y,C})
=\operatorname{Fitt}_0(\mathcal T_T)\,(\theta).
\]

No equality with sums of contacts of individual branches, a conductor boundary of the total curve, or an exceptional cycle is asserted. Those are different invariants. In particular (8) is not a formula for the complete residual scheme.

### Full thick attachment and the marked normal nilpotent contribution

Let \(H=T\cap D\), a finite scheme, and set \(s=a+b-4\). Classical linkage and Euler characteristic give the full attachment budget

\[
\operatorname{length}H=s\deg T-2p_a(T)+2.             \tag{9}
\]

Indeed \(I_D/L\simeq\omega_T(-s)\), so
\(\chi(\mathcal O_Y)=\chi(\omega_T(-s))+\chi(\mathcal O_D)
=-\chi(\mathcal O_T)-s\deg T+\chi(\mathcal O_D)\).
The scheme union exact sequence gives
\(\chi(\mathcal O_Y)=\chi(\mathcal O_T)+\chi(\mathcal O_D)-\operatorname{length}H\);
equating these proves (9) in every characteristic.

Since \(J\subset I\), there is also an exact sequence

\[
0\longrightarrow I\mathcal O_H\longrightarrow\mathcal O_H
\longrightarrow\mathcal O_{C\cap D}\longrightarrow0.
\]

Define \(\epsilon_{\mathrm{normal}}=\operatorname{length}(I\mathcal O_H)\).
This is the marked normal nilpotent contribution, **not the entire nilradical** of \(H\): the scheme \(C\cap D\) can itself be nonreduced along \(C\). Combining (8)–(9) yields

\[
\boxed{\ \operatorname{length}\mathcal T_T+\deg\operatorname{div}\theta
+\epsilon_{\mathrm{normal}}
=(a+b-4)\deg T-2p_a(T)+2.\ }                          \tag{10}
\]

This is an identity for an actual pair and its full primary/residual schemes, not a universal positive lower bound. If the residual vanishes, all three terms vanish. The filtration by powers of \(I\) on \(\mathcal O_H\) retains further normal attachment layers; it terminates since a pure length-\(m\) thickening \(T\) satisfies \(I^m\mathcal O_T=0\).

[Benguş-Lasnier–Rangachev, Theorem B(1)](https://arxiv.org/html/2504.09362v3)
is precisely the full-scheme genus/discrepancy formula (9). Its Cohen–Macaulay,
generically-CI hypotheses permit nonreduced T; no characteristic restriction
is imposed. Its reduced Jacobian/Milnor formulas are separate and are not
applied to T after removing nilpotents. The proof of (9) above independently
fixes the distinction between full T cap D and marked C cap D.

## 5. A sharp control: the determinant can be a unit at a real attachment

This is a local explanatory example, not a global homogeneous realization on the fixed quartic. It is used to test exactly the proposed omission of \(\mathcal T_T\), not to launch a case classification.

In \(k[[t,x,y]]\), mark \(C=(x,y)\) and take

\[
L=(x^2,xy+ty^2),\qquad
J=(x^2,xy+ty^2,y^3).
\]

The quotient by \(J\) is free over \(k[[t]]\), with basis \(1,x,y,y^2\), so \(J\) is \(C\)-primary and CM. At \(t\ne0\), \(y^3\) belongs to \(L\), since

\[
t^2y^3=yx^2+(-x+ty)(xy+ty^2).
\]

Thus it is the full marked primary component. The residual ideal is

\[
K=(x+ty,t^2)=L:J,\qquad L=J\cap K.
\]

A Hilbert--Burch matrix for \(J\) is

\[
\begin{pmatrix}
y&0\\
-x+ty&-y^2\\
-t^2&x+ty
\end{pmatrix}.
\]

Reducing its relations modulo \(I=(x,y)\) gives

\[
\mathcal E_T\simeq k[[t]]^2\oplus k[[t]]/(t^2).
\]

The actual equations \(x^2,xy+ty^2\) map to the two free basis vectors. Hence \(\bar\rho\) is the identity and \(\theta\) is a unit, but

\[
\mathcal Q_{Y,C}\simeq k[[t]]/(t^2),\qquad C\cap D=2[0].
\]

All attachment length sits in the non-lci torsion term. This disproves a determinant-only residual detector for general full primary components.

The full thick attachment is larger: substituting \(x=-ty\) in \(J+K\) gives
\(\mathcal O_H\simeq k[[t,y]]/(t^2,y^3)\), of length six.
The marked normal ideal \(I\mathcal O_H=(y)\) has length four, while
\(\mathcal O_{C\cap D}=k[[t]]/(t^2)\) has length two.
Thus \(\epsilon_{\mathrm{normal}}=4\), illustrating the two distinct attachment quantities in (10).



## Marked attachment controls genuine residual degree

## 1. Exact statement

Let \(Y=V(F_a,G_b)\) be an actual proper homogeneous intersection
containing \(C\). Let \(T\) be its full \(C\)-primary component and
\(Z\) its linked residual, sharing no component with \(C\). Write

\[
[Y]=m[C]+R,\quad [Z]=R,\quad \delta=\deg R=ab-4m,
\qquad A=\operatorname{length}(C\cap Z).
\]

The residual \(Z\) may be nonreduced, disconnected or non-Gorenstein.
It is a pure locally Cohen–Macaulay curve when nonempty. Then

\[
\boxed{\delta\ge\left\lceil\frac A3\right\rceil.}\tag{1}
\]

If no component of \(R\) lies on the unique containing quadric \(Q\),
then

\[
\boxed{\delta\ge\left\lceil\frac A2\right\rceil.}\tag{2}
\]

Neither bound assumes an integral or normal carrier, nor a reduced
residual. The attachment in these formulas is to **reduced marked**
\(C\), not the generally larger full \(T\cap Z\).

## 2. Direct proof and a module-to-degree bridge

The inherited global generation of \(I_C(3)\) lets us choose a cubic
\(h\) through \(C\) containing none of the finitely many components
of \(Z\). Indeed, at the generic point of any component distinct from
\(C\), global generation gives some section nonzero there; avoid the
finite union of proper linear subspaces. Purity makes \(h\) a
nonzerodivisor on \(O_Z\). Thus \(Z\cap V(h)\) is finite of length
\(3\delta\), by the exact Cartier sequence and the Hilbert polynomial.
Since \(h\in I_C\), there is a surjection

\[
O_Z/(h)\twoheadrightarrow O_Z/I_C O_Z=O_{C\cap Z}.
\]

Therefore \(A\le3\delta\). If \(Z\) has no component on \(Q\),
use its quadratic equation instead of \(h\) and get \(A\le2\delta\).
This proof does not reduce \(Z\) or replace it by its normalization.

The [attachment-module identity](residual_capacity_and_constructions.md#full-primary-equation-module-and-exact-attachment-divisor)
makes the numerator accessible from the full primary equation module.
Put \(I=I_C\), \(J=I_T\), and \(E_T=J/IJ\). The actual two equation
classes map into \(E_T\). Let

\[
\tau=\operatorname{length}(\operatorname{tors}E_T),\qquad
\eta=\deg\operatorname{div}\theta,
\]

where \(\theta\) is the determinant of their induced map into the
torsion-free rank-two quotient. Because \(T\) is the **full** primary
component, this determinant is generically nonzero. The inherited identity
is \(A=\tau+\eta\). Consequently

\[
\boxed{\deg R\ge\left\lceil\frac{\tau+\eta}{3}\right\rceil,}
\quad\text{or}\quad
\boxed{\deg R\ge\left\lceil\frac{\tau+\eta}{2}\right\rceil}
\quad(R\text{ has no component on }Q). \tag{3}
\]

This combines an already reviewed module identity with an elementary
scheme-theoretic Bézout estimate. It is not a new assertion of positivity
of \(\tau+\eta\) for every characteristic-zero pair. At a sole-support
endpoint \(Z\) is empty and both vanish. It also does not let one replace
\(A\) by the full attachment: the extra normal-nilpotent length in
\(T\cap Z\) is absent from (3).

## 3. A sharp actual family and the failure of the full-attachment substitution

On \(Q\cong\mathbf P^1\times\mathbf P^1\), use
\(C\sim(1,3)\). For any integer \(s\ge1\), choose a divisor
\(B\in |O_Q(2s,0)|\) consisting of \(2s\) distinct trisecant ruling
lines. The product of its section and the \(s\)-th power of the
Cartier equation of \(C\) is a section of
\(O_Q(3s,3s)=O_Q(3s)\). It lifts to an actual homogeneous form \(G_{3s}\)
because \(H^1(\mathbf P^3,O(3s-2))=0\). The proper pair \((q,G_{3s})\)
has, as a divisor on the smooth quadric,

\[
Y=sC+B,
\quad T=sC,
\quad R=B,
\quad \delta=2s,
\quad A=C\cdot B=6s.
\]

It attains \(A=3\delta\), proving that coefficient three cannot be
improved for arbitrary proper pairs in (1). This reuses the known smooth-
quadric construction principle; it does not reopen a closed STCI case.

The full attachment has length
\(\operatorname{length}(T\cap Z)=sC\cdot B=6s^2\).
For \(s>1\), substituting that length into \(A\le3\delta\) would be
false. This family therefore gives an actual fixed-quartic control for
both sharpness and the necessary marked/full distinction.

## 4. How to use the bound without making it circular

The inequalities are useful when geometry supplies an independent lower
bound \(A\ge A_0\), or a bound on \(\tau+\eta\), for a class of possible
primary structures. If one has already explicitly computed the entire
primary ideal and its degree, then \(m\), hence \(\delta\), is already
known; (3) is then a consistency check. It is not a shortcut around a
completed primary decomposition.

Every bound must also respect \(\delta\equiv ab\pmod4\). For example,
an independent estimate \(A\ge13\) gives \(\delta\ge5\); if
\(ab\equiv0\pmod4\), this strengthens to \(\delta\ge8\).

For any curve whose ideal is generated in twist \(d_0\), the same proof
gives \(\deg R\ge\lceil\operatorname{length}(C\cap Z)/d_0\rceil\).
Any independently known hypersurface through \(C\), avoiding all residual
components, gives its own degree in the denominator. The quartic's quadric
and cubics give the two especially simple alternatives above.



## Full attachment: genus, nilpotents, and low residual degree

In this section assume the genuine linked residual Z is nonempty. Set r=deg Z>0, B=length(T cap Z), and N=a+b-4>0. Here T is the full C-primary component, and Z has no C-component. The two pure locally Cohen–Macaulay schemes share no curve component and are linked by Y. The lower bounds containing max{1,...} use precisely this nonempty hypothesis; a sole-support endpoint has r=0 instead.

## 2. The attachment identity on the genuine residual side

The same standard linkage calculation gives

\[
\boxed{B=Nr-2p_a(Z)+2.}\tag{1}
\]

Indeed adjunction gives \(p_a(Y)=1+Nab/2\), and linkage gives

\[
p_a(T)-p_a(Z)=\frac N2(4m-r).
\]

The scheme-union exact sequence gives
\(p_a(Y)=p_a(T)+p_a(Z)+B-1\), proving (1). These formulas hold for
nonreduced locally Cohen–Macaulay schemes, using their dualizing modules;
they are not formulas for the reduced support or normalization.

Since \(p_a(Z)=1-h^0(\mathcal O_Z)+h^1(\mathcal O_Z)\), equation (1)
also reads

\[
B=Nr+2h^0(\mathcal O_Z)-2h^1(\mathcal O_Z).
\tag{2}
\]

Consequently, if a separate argument supplies \(h^0(\mathcal O_Z)\le h\),
then

\[
\boxed{r\ge\max\{1,\lceil(B-2h)/N\rceil\}.}\tag{3}
\]

This is useful when the full-primary attachment module can be computed
before a residual decomposition. It is conditional on that extra
cohomology information; connected nonreduced support does not imply
\(h^0=1\).

The practical input may instead be an independently proved lower bound
\(B\ge B_0\), or attachment data controlled throughout a proposed family
of primary thickenings. One can replace \(B\) by \(B_0\) in the lower
bounds below. A completed explicit extraction of the full primary ideal
already determines its generic multiplicity and hence \(r=ab-4m\);
these inequalities are not claimed to shortcut that completed computation.
They are constraints on proposed primary families, module budgets, or
partially known decompositions.

Two clean cases need no detailed cohomology calculation:

- If \(Z\) is reduced, it has at most \(r\) connected components, and
  \(h^0(\mathcal O_Z)\) is their number. Thus
  \[
  \boxed{r\ge\max\{1,\lceil B/(a+b-2)\rceil\}.}\tag{4}
  \]
- If \(Z\) is reduced and connected, or more generally
  \(H^0(\mathcal O_Z)=k\), then
  \[
  \boxed{r\ge\max\{1,\lceil(B-2)/(a+b-4)\rceil\}.}\tag{5}
  \]

For (4), the equality \(B=(N+2)r\) forces \(r\) disjoint lines: equality
requires \(h^0=r\) and \(h^1=0\), so each connected component has degree
one. This is an equality characterization for any actual pair attaining
it, not a construction of such a pair for arbitrary degrees.

The variable \(B\) cannot silently be replaced by
\(\operatorname{length}(C\cap Z)\). The full attachment can have an
additional normal-nilpotent contribution even when the marked intersection
has been fixed. Likewise (4) cannot be used after merely reducing \(Z\):
that changes its degree and its Euler characteristic.
If a marked lower bound \(\operatorname{length}(C\cap Z)\ge A_0\) is
known, the containment \(C\cap Z\subset T\cap Z\) does give
\(B\ge A_0\). Thus the **weaker inequalities obtained by substituting the
lower bound \(A_0\)** are legitimate under the same reducedness or
cohomology hypotheses. That use of a lower bound does not identify the
two attachment lengths or turn (1) into a marked-intersection identity.

## 3. Why genus alone does not give an unrestricted degree bound

There are locally Cohen–Macaulay double lines of degree two and arbitrarily
negative arithmetic genus. In coordinates \([x:y:z:w]\), take
\(L=V(x,y)\), choose \(e\ge-1\), and a surjection

\[
\mathcal O_L(-1)^2\xrightarrow{(f,g)}\mathcal O_L(e),
\]

where \(f,g\) have degree \(e+1\) and no common zero on \(L\). The
kernel construction gives the ribbon with ideal

\[
I_Z=(x^2,xy,y^2,gx-fy),
\qquad
0\to\mathcal O_L(e)\to\mathcal O_Z\to\mathcal O_L\to0.
\tag{6}
\]

It has

\[
\deg Z=2,\qquad p_a(Z)=-e-1,\qquad
h^0(\mathcal O_Z)=e+2,\qquad h^1(\mathcal O_Z)=0.
\]

Thus the right side of (1), for fixed \(r=2\), can be arbitrarily large
among unrestricted curve candidates. A reduced integral Castelnuovo bound
cannot be applied to these schemes. Even topological connectedness does
not repair the issue: the extra global functions in (6) are nilpotent.

This is standard ribbon geometry, not a new example. The primary text
[Nollet–Schlesinger, *Hilbert Schemes of Degree Four Curves* (2003)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B62E5E7FF38C897359DE99E647E71DFF/S0010437X03100711a.pdf/hilbert-schemes-of-degree-four-curves.pdf)
uses the displayed homogeneous double-line ideals and genus calculation.
[Bayer–Eisenbud, *Ribbons and their canonical embeddings*](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf)
provides the square-zero extension framework. These sources were inspected
on 2026-10-28; no literature novelty is asserted.

This is a limitation of genus-only reasoning for arbitrary candidates.
It does **not** assert that all these ribbons occur as the full residual
of pairs of two fixed degrees containing \(C\). Actual equations impose
additional bounds, which the next section makes explicit in degree two.

## 4. Actual equations sharply constrain a degree-two residual

Assume \(a\le b\). If the genuine residual degree is one, purity makes
\(Z\) a reduced line. Therefore

\[
\boxed{r=1\ \Longrightarrow\ B=N+2.}\tag{7}
\]

If the genuine residual degree is two, its possible structures are a
plane conic (including intersecting lines and a planar double line), two
skew lines, or a nonplanar double line. In the first two cases,

\[
B=2N+2\quad\text{or}\quad B=2N+4.
\tag{8}
\]

For a double line, (6) gives

\[
B=2N+2e+4.
\tag{9}
\]

For clarity, purity excludes hidden exceptional degree-two schemes in
this list. A component of degree two and multiplicity one is an integral
conic; two components of degree one are lines. With sole support a line,
generic length two makes \(I_L^2\) vanish generically in \(\mathcal O_Z\),
and absence of embedded associated points makes it vanish everywhere.
The resulting square-zero ideal is a torsion-free rank-one module on the
smooth line, hence a line bundle. This gives (6), with \(e\ge-1\) forced
by the globally surjective conormal quotient.

There is now an equation-degree restriction absent from the genus-only
control:

\[
\boxed{e+2\le b.}\tag{10}
\]

To prove it, the conormal sequence of (6) gives

\[
I_Z/I_L^2\simeq\mathcal O_L(-e-2)
\ \subset\ I_L/I_L^2=\mathcal O_L(-1)^2.
\]

The first normal symbol of a degree-\(d\) equation containing \(Z\)
therefore lies in \(H^0(\mathcal O_L(d-e-2))\). If \(a,b<e+2\), both
first symbols vanish. At \(\eta_L\), both equations then lie in the square
of the maximal ideal of the regular two-dimensional normal local ring.
Their quotient has length at least three, since it surjects onto the
length-three quotient by that square. This already contradicts length two
for a full double-line component of \(Y\). Hence at least one first
symbol is nonzero, and its degree is at most \(b\), proving (10).

Combining the cases yields the exact small-degree test

\[
\boxed{
r=2\ \Longrightarrow\
B\text{ is even and }2N+2\le B\le2N+2b.
}\tag{11}
\]

Thus a full-primary calculation giving \(B>2N+2\max(a,b)\) rules out
genuine residual degrees one and two even without a reducedness assumption.
If \(B>0\), it also rules out the empty residual, so it forces \(r\ge3\).
The congruence \(r\equiv ab\pmod4\) may then strengthen this degree
conclusion, separately from the attachment argument.

The lower endpoint in (11) is the planar conic case. Intermediate even
values correspond to a double-line parameter \(e\), but (11) is a necessary
test, not an existence theorem for the corresponding complete intersection
or the fixed quartic partner.

There is also a global algebraic filter. A line or planar conic is ACM, so
linkage forces the full primary \(T\) to be ACM. For \(a,b\ge4\), its
minimal ideal resolution is respectively

\[
\begin{aligned}
0&\to S(-(a+b-1))^2
\to S(-a)\oplus S(-b)\oplus S(-(a+b-2))\to I_T\to0,\\
0&\to S(-(a+b-1))\oplus S(-(a+b-2))
\to S(-a)\oplus S(-b)\oplus S(-(a+b-3))\to I_T\to0.
\end{aligned}\tag{12}
\]

These are the standard dual mapping cones for linking a line or a
\((1,2)\) conic. Thus the small residual alternatives can be tested on
actual primary ideals and syzygies, not only on cycle degrees. Two skew
lines instead have Rao module \(k\) in degree zero, so \(T\) has Rao
module \(k\) in degree \(N\). No classification of all such primary
thickenings of the fixed \(C\) is asserted here.

## 5. Extension to a ribbon on any smooth residual support

The proof of (10) is not peculiar to lines. Suppose the genuine residual
\(Z\) is a ribbon of multiplicity two on a smooth integral support
\(A\subset\mathbf P^3\) of degree \(d\) and genus \(g\), with nilpotent
line bundle \(L\) of degree \(\ell\). Then

\[
0\to M\to N^*_{A/\mathbf P^3}\to L\to0,
\qquad \deg M=-4d-2g+2-\ell.
\]

At least one actual equation has a nonzero first symbol, a section of
\(M(a)\) or \(M(b)\), because \(Z\) is the full generic
multiplicity-two component. Its divisor of zeros is effective, so

\[
\ell\le (b-4)d-2g+2,
\qquad p_a(Z)=2g-1-\ell\ge4g-3-(b-4)d.
\]

Since \(r=2d\), equation (1) gives the conditional quantitative bound

\[
\boxed{B\le(a+2b-8)r-8g+8.}\tag{13}
\]

Whenever the coefficient is positive, this bounds \(r\) from below using
the full attachment and the support genus. For a line it recovers (11)'s
upper bound. The hypotheses require an actual ribbon on smooth support;
one cannot apply (13) to an arbitrary nonreduced residual with several
layers, singular support, or punctual conormal defects.



## A common capacity lemma and its exact limits

The marked-attachment proof has the following useful scope independent of
this quartic. If \(C\subset\mathbf P^3\) has \(I_C(d_0)\) globally
generated, and \(Z\) is a pure residual curve with no component on \(C\),
then \(\ell(C\cap Z)\le d_0\deg Z\). The proof selects a section avoiding
all associated curve components, uses its Cartier sequence on \(Z\), and
surjects its finite zero scheme onto \(C\cap Z\). It therefore works with
nonreduced residuals. An individual hypersurface through \(C\) avoiding all
residual components improves \(d_0\) to its degree. Normalization is neither
needed nor harmless for this finite-scheme assertion.

For a smooth degree-\(c\) curve on an integral carrier of degree \(a\),
a singleton divisorial inverse \(\Gamma\) with residue degree \(f\), ideal
valuation \(e\), and numerical square \(\sigma\), [the normalization proof](normalization_residual_capacity.md)
gives
\[
\deg R\ge\frac{be(c^2f^2-a\sigma)}{d_0cf-e\sigma}
\]
when \(d_0a>cef\). Indeed \(d_0H-Z\) is nef,
\(H\cdot\Gamma^{\rm num}=cf\), and Hodge index makes the displayed
denominator positive. This separates the reusable lemma from the numbers
\((c,d_0)=(4,3)\). If the denominator vanishes retain the undivided nef
inequality. A zero Hodge gap leaves the endpoint open; conductor descent and
actual equation realization still require proof.

There are three different mechanisms here: a finite-scheme quotient bounds
marked attachment by degree; surface positivity bounds the valuation vector
of an actual mate; liaison expresses full attachment through Euler
characteristics. No implication identifies their defect divisors. The ribbon
control shows why connectedness alone does not bound full attachment.
The prescribed A-type family shows why a large local Cartier index alone
neither constructs sole support nor supplies the needed global divisor
relation. In particular its residual cancels the local class and survives
with explicitly different marked and full attachment lengths.

## Literature and verification boundary

The marked-attachment and full-discrepancy proofs above are independent of finite sampling. Standard local canonical-module duality is used with its precise length argument, rather than replacing the residual dualizing module by a structure sheaf. The normal-pullback literature and Hodge argument belong to [normalization capacity](normalization_residual_capacity.md); fixed-twist formal extension belongs to [formal visibility](formal_residual_visibility.md). No inherited computation was rerun here.

## Characteristic reach and limitation

The full-primary module, Matlis length comparison, marked-attachment bounds,
and ribbon equation-symbol tests are characteristic-free over an algebraically
closed field. They neither require nor prove positivity of attachment. In
particular at the [quartic-carrier supported pairs in every positive
characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier),
the genuine residual and all attachment terms vanish. Reducedness assumptions
in the genus bounds remain necessary in every characteristic.


## Compatible families and the exact specialization hypothesis

[Benguş-Lasnier–Gaffney–Rangachev, Theorem 3.1](https://arxiv.org/html/2310.16558v4) applies to a flat embedded complex-analytic curve family X over a smooth base, contained in a flat Gorenstein curve family Y, with no embedded point at the origin and with X a union of full induced components in every fiber. It proves fiberwise residual specialization and flat finite attachment, hence locally constant attachment length. Its ambient reduced-equisingularity discussion does not restrict that full-component flatness theorem to reduced X. The primary theorem and its full-primary-decomposition proof were freshly checked here.

This does not authorize arbitrary full-primary extraction in a changing CI family: if multiplicity along C increases, the degree of the full primary component increases and it cannot be a projective flat family with fixed Hilbert polynomial. A flat lower witness can instead cease to be a full component at the special fiber, failing the theorem's component hypothesis. The once-link family in [reverse liaison](residual_liaison.md) is a different flat object. Neither a reduced-support Milnor invariant nor the constant full-attachment conclusion may be substituted after these hypotheses fail.
