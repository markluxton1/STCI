---
id: STCI-A-0005
type: argument
title: Filtered equations and the information lost by normal grading
status: complete
scope: "#scope"
conclusion: "#conclusion"
---
# Filtered equations and the information lost by normal grading

## Scope

Let \(J\subset I\) be the ideal of an intersection in a Noetherian ambient
ring \(R\), with \(I\) the ideal of a marked subscheme \(C\). In the geometric
setting the carriers are distinct integral hypersurfaces in a smooth
threefold. Their local defining equations form a regular sequence along
their intersection. The curve \(C\) can be a component of the reduced
intersection with residual support elsewhere. The local comparison is an
ideal identity. The dimension, length, and smooth-carrier conclusions have
the separate hypotheses given below.

The two local controls are in characteristic zero. The
[prescribed quartic application](../results/quartic_char2_fourth_equation_kernel.md)
uses \(C_0=[s^4:s^3t:st^3:t^4]\) in characteristic two. The
[marked embedding diagram](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2-the-complete-embedding-and-conormal-diagram)
specifies the carrier maps and the bases of the nine conormal algebras.

## Local comparison and the punctual defect

### Full normal equations and the actual equation module

Set \(S=\operatorname{gr}_I R\), \(K=I/J\subset R/J\), and
\(H=\operatorname{in}_I(J)\). By definition \(H_n\) is the image of
\(J\cap I^n\) in \(I^n/I^{n+1}\). The kernel of
\[
I^n/I^{n+1}\longrightarrow (I^n+J)/(I^{n+1}+J)
\]
is \(H_n\), since an element of \(I^n\) in \(I^{n+1}+J\) differs from an
element of \(J\cap I^n\) by an element of \(I^{n+1}\). Hence \(S/H\) is the
full normal graded algebra \(\operatorname{gr}_K(R/J)\). For a regular
embedding \(C\hookrightarrow P\), \(S=\operatorname{Sym}_{R/I}(I/I^2)\).
Writing \(S_+\) for the positive ideal, \(Q_n=H_n/(S_+H)_n\) records minimal
initial equations in degree \(n\). Over a curve this module can have torsion.
The first symbols of the two displayed equations can generate only part of
\(H\), even when the embedding and the intersection are regular.
The [form-ideal calculation and first-symbol product map](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#3-the-central-normal-cone-sequence)
also relate this sequence to the Valabrega–Valla form ring.

Put \(D=J/IJ\) and give it the decreasing filtration
\[
F^nD=\big((J\cap I^n)+IJ\big)/IJ,\qquad n\ge1.
\]
Then \(F^1D=D\), and \(F^2D=\ker(\phi:D\to I/I^2)\) for the first conormal
map. Artin–Rees gives \(J\cap I^n=I^{n-c}(J\cap I^c)\) for some \(c\) and all
\(n\ge c\). Thus \(F^nD=0\) for \(n>c\).

For any finite free presentation \(\pi:P_0\twoheadrightarrow J\) with
kernel \(L\), put \(P_n=\pi^{-1}(I^n)\). Since \(\pi(IP_0)=IJ\) and
\(\pi(P_n)=J\cap I^n\), the induced maps give compatible exact sequences
\[
0\longrightarrow L/(L\cap IP_0)
\longrightarrow (P_n+IP_0)/IP_0
\longrightarrow F^nD\longrightarrow0.
\]
Indeed a lift that maps into \(IJ\) differs from an element of \(IP_0\) by an
element of \(L\), which lies in every \(P_n\). For a regular sequence \(f,g\)
the syzygy \((-g,f)\) lies in \(IP_0\) in the two-generator presentation.
Hence \(P_0/IP_0\simeq D\) and the coefficient filtration is the intrinsic
one. For a redundant presentation the constant syzygies occur at every
stage and cancel from successive quotients. Adding a zero generator, for
example, adds \(R/I\) to each stage.

Write \(B=\operatorname{in}_I(IJ)\). The denominator of the \(n\)-th graded
piece of \(D\) is obtained by intersecting \(J\cap I^n\) with
\((J\cap I^{n+1})+IJ\). Subtracting the \(I^{n+1}\) term leaves an element of
\(IJ\cap I^n\), so
\[
G_n=\operatorname{gr}_F^nD
=\frac{J\cap I^n}{(J\cap I^{n+1})+(IJ\cap I^n)}
=H_n/B_n.
\]
Multiplication of representatives gives \(S_+H\subset B\subset H\).
Taking the quotient by \(B_n\) gives the canonical exact sequence
\[
0\longrightarrow\Delta_n=\frac{B_n}{(S_+H)_n}
\longrightarrow Q_n
\longrightarrow G_n
\longrightarrow0.
\]
The comparison is an isomorphism in every degree precisely when
\(B=S_+H\). In degree one \(B_1=(S_+H)_1=0\). The defect records minimal
initial equations formed by combinations with coefficients in \(I\).
Passing to \(D\) erases such combinations. Even when all \(\Delta_n\)
vanish, comparison identifies graded pieces and supplies no splitting of
\(\ker\phi\). The canonical identification with a single \(Q_m\), for
\(m\ge2\), follows when \(\Delta_m=0\), \(F^2D=\cdots=F^mD\), and
\(F^{m+1}D=0\).

### Generic count and length over a DVR

At the generic point of a smooth integral marked curve in a smooth
threefold, assume \(J\) is a two-generator parameter ideal in the regular
transverse local ring with maximal ideal \(I\). The residue field is
\(\kappa(\eta)\). The two regular generators give a basis of \(D\) over
\(\kappa(\eta)\). Finiteness of \(F^\bullet D\) therefore gives
\(\sum_n\dim G_n=2\). Since \(S\) is a polynomial ring in two normal
variables over that field, homogeneous Nakayama identifies
\(\sum_n\dim Q_n\) with the minimal homogeneous generator count \(\mu(H)\).
The comparison sequence gives \(\dim\Delta_n=\dim Q_n-\dim G_n\) in each
degree. Summing gives \(\dim\Delta=\mu(H)-2\).

Now assume \(\Delta_\eta=0\) on a smooth integral curve. At a closed point
the local ring of the curve is a DVR. The surjection \(Q_n\to G_n\) of
finite modules induces a surjection between their torsion-free quotients,
which are free of equal rank by generic vanishing. It is an isomorphism.
Every preimage of a torsion element of \(G_n\) is therefore torsion, giving
\[
0\longrightarrow\Delta_n\longrightarrow\operatorname{tors}Q_n
\longrightarrow\operatorname{tors}G_n\longrightarrow0.
\]
Consequently \(\ell\Delta_n=\ell\operatorname{tors}Q_n-
\ell\operatorname{tors}G_n\). Under generic vanishing, torsion-free \(Q\)
implies \(\Delta=0\).

### Smooth-carrier vanishing

Let \(C\) be smooth of codimension two in a smooth equicharacteristic
threefold, and \(J=(f,g)\subset I_C\) a regular sequence. At a point of
\(C\) where the fiber conormal symbol of \(f\) is nonzero, extend \(f\)
to two generators of \(I_C\) and then to regular parameters. Equivalently,
the carrier \(V(f)\) is smooth there, by the conormal sequence of the
smooth curve in the smooth ambient space. In the completed local ring we
can write \(\widehat R=D_0[[x,y]]\) with \(x=f\), \(\widehat I=(x,y)\),
and \(D_0\) a complete regular local domain of dimension one (a field
at the generic point). This uses the equicharacteristic coefficient field
and the chosen regular parameters.

Reduce \(g\) modulo \(x\) to obtain \(h\in D_0[[y]]\). It is nonzero by
regularity of the sequence. Write \(h=y^m a(y)\), with \(m\ge1\) and
\(a_0=a(0)\ne0\). The coefficient \(a_0\) may be a nonunit. The
\(x\)-free part of \(J\widehat R=(x,h)\) consists of multiples of \(h\).
For \(IJ\widehat R=(x^2,xy,yh)\) its \(x\)-free part consists of
multiples of \(yh\). The \(x\)-containing parts are respectively in
\((x)\) and \((x^2,xy)\). As \(D_0\) is a domain, nonzero products of
\(x\)-free terms have additive \(y\)-order. With \(X,Y\) the normal
classes of \(x,y\), this gives the full initial ideals
\[
H=(X,a_0Y^m),\qquad B=(X^2,XY,a_0Y^{m+1})=S_+H
\]
after completion. Flatness preserves the finite intersections defining
each initial piece, and faithful flatness descends their equality.
Interchanging the carriers gives the same vanishing when the conormal
symbol of \(g\) is nonzero. Thus \(\operatorname{Supp}\Delta\subset
C\cap\operatorname{Sing}V(f)\cap\operatorname{Sing}V(g)\). If either
carrier is generically smooth on a projective integral curve, any
remaining defect has finite support. [Faithfully flat completion](https://stacks.math.columbia.edu/tag/00MC)

## A minimal initial equation erased by the comparison

Work in \(R=k[x,y]_{(x,y)}\) over a field of characteristic zero, and
set \(I=(x,y)\), \(f=x^2+y^3\), \(g=xy+x^3+y^3\), \(J=(f,g)\).
The coprime exponents of the cusp equation give geometric irreducibility.
For the cubic \(g\), a factorization over an algebraic closure would give
an affine line factor. The substitution \(y=ax+b\) forces \(b=0\) from
the constant term and then \(a=0\) from the quadratic term, leaving the
nonzero cubic \(x^3\). A vertical line \(x=b\) leaves a monic cubic in
\(y\). These distinct integral equations form a regular sequence.

There is an identity with both coefficients in \(I\)
\[
(y+x^2)f+(-x+y^2)g
=y^4+x^2y^3+x^3y^2+y^5.
\]
Thus \(Y^4\in B=\operatorname{in}_I(IJ)\), where \(X,Y\) denote the
normal variables. To check fullness of the initial ideal, let
\(w=1-y^2\) in \(R/J\). The equations give \(x^2=-y^3\) and
\(xyw=-y^3\). Multiplying the latter by \(x\) gives \(y^4w=xy^3\).
Using \(xyw=-y^3\) again gives \(y^4(w^2+y)=0\).
The factor \(w^2+y\) is a unit. It follows that \(y^4=0\) and
\(xy=-y^3\), so \(1,x,y,y^2,y^3\) span \(R/J\).
These five vectors also define a quotient model with unit, the ordinary
products of \(y\) modulo \(y^4\), \(x^2=xy=-y^3\), and
\(xy^2=xy^3=0\). The products involving \(x\) are associative since
\(y^3\) annihilates the maximal ideal and the assignments agree with
multiplication by powers of \(y\). The model satisfies \(f=g=0\)
and is local with residue field \(k\), giving the reverse dimension bound.
Therefore \(R/J\) has length five. The monomial ideal
\((X^2,XY,Y^4)\) lies in \(H\) and has colength five, so it is the full
initial ideal.

In degree four every element of \((S_+H)_4\) is divisible by \(X\).
Consequently \(Q_4=kY^4=\Delta_4\). Both equations start in degree two,
so \(\phi=0\) and \(F^2D=D=k^2\). Independence of the quadratic initials
\(X^2,XY\) means that only the zero class of \(D\) lifts to order three.
In particular \(F^3D=0\) and \(G_4=0\).

The cancellation can also be read in the filtered Koszul complex on
\((f,g)\) with generator weights two. On its first homology page,
\(H_1(K(X^2,XY))=k[Y](Y e_f-X e_g)\) since the linear syzygy is
killed by \(X\) modulo the Koszul syzygy. Lifting the linear syzygy
gives \(yf-xg=y^4-x^4-xy^3\). Its degree-four term modulo the
quadratic initial equations is \(Y^4\). The first higher differential
is multiplication by \(Y^4\) on that \(k[Y]\)-module, hence injective.
The coefficients \(y,-x\) vanish on \(C\), which explains why this
additional equation disappears in \(D\).

Adjoining a parameter \(t\) and taking \(I=(x,y)\) gives the same
example along the smooth reduced \(t\)-axis in a smooth threefold.
The products and initial ideals extend over the coefficient ring
\(k[t]_{(t)}\) at the origin, and the defect remains nonzero over \(k(t)\).

## Conclusion

The [local comparison](../results/local_filtration_comparison_defect.md)
measures which minimal full initial equations survive the filtration of
the actual equation module. The
[degree-four counterexample](../results/initial_equation_cancellation_counterexample.md)
exhibits a generator erased by that comparison. The
[restricted-diagram counterexample](../results/restricted_normal_diagram_counterexample.md)
shows a second loss of information. Even identical normal graded algebras
and all the carrier maps after restriction to the marked curve can come
from nonisomorphic intersection algebras. The ambient quotient map in
the full based diagram would recover the actual ideal \(J\) in degree zero.

For the prescribed quartic pair one carrier is smooth on each of the
two marked charts, so the comparison is an isomorphism there in both
characteristics zero and two. In characteristic two the
[canonical quartic identification](../results/quartic_char2_fourth_equation_kernel.md)
also uses the full filtration and the overlap of the actual equation
frames. In characteristic zero the normal filtration concerns a marked
component of a residual intersection.

The [length-five specialization control](../results/supported_length_five_defect_specialization.md)
has zero relative defect and nonzero actual defect on the transverse
closed fiber. The [transverse specialization argument](transverse_specialization.md)
gives the normal-flat comparison theorem. The
[punctual comparison proofs](punctual_comparison_defects.md#statements-and-proofs)
include examples with residual and sole support. The
[punctual relative-defect question under sole support](../FRONTIER.md#punctual-relative-defect-under-sole-support)
remains open.

## Source proofs and review scope

The October 23 independent review reconstructed the filtered denominator,
constant syzygies, comparison direction, and smooth-carrier calculation.
It checked the five-dimensional model and the first higher Koszul
differential, as well as the separate nine-object restricted comparison
and its intrinsic nonisomorphism test. The finite scripts checked the
explicit arithmetic and algebra models. Irreducibility and the general
comparison were checked in the written proofs.
[October 23 independent review](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-reviewmd)

R-0030 records the [October 24 source and independent review](../results/local_filtration_comparison_defect.md#review)
of the generic count and DVR length calculation, and the
[October 26 local audit and its scope](../results/local_filtration_comparison_defect.md#october-26-local-audit).
