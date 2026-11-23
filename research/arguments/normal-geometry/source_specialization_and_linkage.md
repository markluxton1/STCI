# Actual sources under specialization: sections, linkage and attachment

The section defect of an invariant pure hull, the failure of a colon to
commute with specialization, and the normal-equation comparison defect
are different constructions. The exact sequences below retain their
actual family sources. They do not identify those defects or force any
one of them to be nonzero. The specialization sequences and the local
colon control were independently reconstructed during the November 23,
2026 synthesis; the linked comparison and attachment results retain
their own stated review scopes.

## Sections after the pure-hull correction

Let \(V\) be a DVR with uniformizer \(t\) and residue field \(k\).
Put \(B_V=V[z,w]\), \(B=k[z,w]\) and \(\mathfrak m=(z,w)\).
Let \(A\) be a finite graded \(B_V\)-algebra, flat over \(V\),
and write \(A_0=A/tA\). Suppose
\[
0\longrightarrow T\longrightarrow A_0\longrightarrow E\longrightarrow0
\tag{SS1}
\]
is the actual pure-hull quotient: \(E\) is the saturated coordinate
algebra of a pure projective curve whose projection center is disjoint
from its support. Thus \(E\) is finite and torsion-free over \(B\),
and \(\dim_B T\le1\). The kernel includes any removed projective
embedded points and any cone-vertex torsion; it need not have finite
length over \(B\).

For the finite free section hull \(N=E_B^{**}\), the
[section-hull argument](../torus/chow_section_parity_defect.md#1-the-finite-free-section-hull)
identifies
\[
D=N/E=H^1_{\mathfrak m}(E).
\]
This \(D\), unlike \(T\), has finite length. Flatness of \(A\) gives
the exact sequence
\[
0\longrightarrow
P:=H^1_{\mathfrak m}(A)/tH^1_{\mathfrak m}(A)
\longrightarrow H^1_{\mathfrak m}(A_0)
\longrightarrow R:=H^2_{\mathfrak m}(A)[t]
\longrightarrow0.                                      \tag{SS2}
\]
Here \(M[t]=\ker(t:M\to M)\). This is the long exact local-cohomology
sequence of \(0\to A\xrightarrow{t}A\to A_0\to0\);
no base-change isomorphism for local cohomology is assumed.

Since \(H^0_{\mathfrak m}(E)=0\) and
\(H^2_{\mathfrak m}(T)=0\), (SS1) gives
\[
0\longrightarrow W:=H^1_{\mathfrak m}(T)
\longrightarrow H^1_{\mathfrak m}(A_0)
\longrightarrow D\longrightarrow0.                    \tag{SS3}
\]
It also gives \(H^0_{\mathfrak m}(T)=H^0_{\mathfrak m}(A_0)\).
Regard \(P,W\) as submodules of the middle term of (SS2). Taking
its quotient by \(W\) yields the canonical comparison
\[
0\longrightarrow P/(P\cap W)
\longrightarrow D
\longrightarrow R/\operatorname{im}(W\to R)
\longrightarrow0.                                      \tag{SS4}
\]
In particular, there is no uncorrected map \(D\to R\) supplied by
these sequences unless the image of \(W\) in \(R\) is zero.

For the equivariant statements take \(V=k[[t]]\) or \(k[t]_{(t)}\)
and a \(k\)-linear action. The sequences respect an involution fixing
\(t,z,w\). More generally, if a weighted family has
\(g(t)=\chi(g)t\), multiplication by \(t\) is equivariant as
\(A\otimes_k k_\chi\to A\). The right term of (SS2)
is then \(R\otimes k_\chi\), with the same character twist in
(SS4). This twist must be retained for parity statements; an intrinsic
torus involution can send \(t\) to \(-t\). In characteristic different
from two, the resulting involution eigenspace sequences are exact.

For a sign-invariant translated cycle with nonzero first moment, the
[parity theorem](../torus/chow_section_parity_defect.md#2-opposite-signs-in-the-same-degree)
requires a nonstandard-sign class in \(D/\mathfrak mD\).
Equations (SS2)--(SS4) locate its possible sources in the actual family
after the embedded correction. They do not show that such a class
cannot survive, and a nonstandard head class is not a converse to
nonzero moment. This comparison retains CI origin when \(A\) is an
actual CI degeneration; replacing \(E\) by an arbitrary free algebra
would discard it.

## Once linkage and the special colon

Let \(\mathcal R\) be a Noetherian \(V\)-algebra, let \(I\subset\mathcal R\)
be the ideal of the fixed mark, and let \(A\) be a finite
\(\mathcal R\)-algebra flat over \(V\). Set
\[
P_C=\operatorname{Ann}_A(I)
   =\operatorname{Hom}_{\mathcal R}(\mathcal R/I,A).
\]
Applying this Hom functor to multiplication by \(t\) gives
\[
0\longrightarrow P_C/tP_C
\longrightarrow\operatorname{Ann}_{A_0}(I)
\longrightarrow
\operatorname{Ext}^1_{\mathcal R}(\mathcal R/I,A)[t]
\longrightarrow0.                                      \tag{SL1}
\]
If \(ta\in P_C\), then \(tIa=0\), and regularity of \(t\) on \(A\)
implies \(Ia=0\). Hence \(P_C\) is \(t\)-saturated in \(A\), so
\(A/P_C\) is torsion-free, and therefore flat, over the DVR. Its
special fiber maps onto the actual special colon quotient, with
\[
0\longrightarrow
\operatorname{Ext}^1_{\mathcal R}(\mathcal R/I,A)[t]
\longrightarrow (A/P_C)\otimes_V k
\longrightarrow A_0/\operatorname{Ann}_{A_0}(I)
\longrightarrow0.                                      \tag{SL2}
\]
These are also statements about sheaf Hom and sheaf Ext, checked
stalkwise on a projective family. For an equivariant \(k\)-linear
family with parameter character \(\chi\), the Ext terms in
(SL1)--(SL2) carry the factor \(k_\chi\), as in (SS2).

If the generic fiber is a proper CI containing \(C\), then
\(A/P_C\) is the flat closure of its once-linked curve, locally over
this trait. Its special fiber equals the special colon precisely when
the displayed Ext torsion vanishes. The
[relative proper-CI theorem](../residuals/residual_liaison.md#21-the-once-linked-curve-is-flat-through-multiplicity-jumps)
proves this compatibility when every fiber remains a proper CI. It
cannot be applied to a full Hilbert limit merely because the generic
fiber is a CI. Neither (SL1) nor (SL2) identifies a full-primary
component through an absorption jump.

### A flat local control with unequal special colons

The [existing marked-family control](../residuals/marked_deformation_and_absorption.md#11-the-full-primary-component-is-not-a-flat-witness-at-absorption)
has the completed local form
\[
\mathcal R=V[[s,x,y]],\qquad
A=\mathcal R/(x^2-ty,xy,y^2),\qquad I=(x,y).
\]
It is free on \(1,x,y\) over \(V[[s]]\): the reductions
\(x^2=ty,xy=y^2=0\) define commuting multiplication operators and
give that basis. For \(a+bx+cy\), annihilation by \(y\) first gives
\(a=0\), and annihilation by \(x\) then gives \(tb=0\). Thus
\[
P_C=V[[s]]y,\qquad
\operatorname{Ann}_{A_0}(x,y)=k[[s]]x\oplus k[[s]]y.
\]
The generic ideal is the CI \((x^2-ty,x^3)\) after inverting \(t\).
The special ideal is \((x,y)^2\), which is not Gorenstein.
The flat once-link limit is
\(A_0/(y)=k[[s,x]]/(x^2)\), whereas the actual special colon quotient
is \(A_0/(x,y)=k[[s]]\). The Ext torsion in (SL1) is exactly
\(k[[s]]x\). It is supported along the marked curve, not a finite
section/Rao defect at a cone vertex. This local control constructs no
global pair for the rational quartic.

## Normal cancellation is not actual residual attachment

For a proper CI with ideal \(L\), full \(C\)-primary ideal \(J\),
and \(I=I_C\), the actual first attachment quotient is
\[
Q_1=J/(L+IJ).
\]
The [attachment theorem](../residuals/residual_capacity_and_constructions.md#full-primary-equation-module-and-exact-attachment-divisor)
and [local duality](../local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers)
concern this actual source cokernel. In contrast, R-0030's \(\Delta\)
compares the full normal initials of the CI ideal \(L\) with its
filtered actual equation module. Two local controls in a smooth
threefold separate their vanishing conditions.

First take \(\mathcal R=k[[s,x,y]]\), \(I=(x,y)\), and
\(L=(x^a+y^b,xy)\), \(2\le a<b\). This is a sole-supported CI,
so its full primary is \(J=L\) and \(Q_1=0\). Nevertheless the
[full Rees calculation](rees_equation_persistence.md#6-the-torsion-duration-refines-delta-an-exact-family)
gives a nonzero free \(k[[s]]\)-summand of \(\Delta\), in normal
degree \(b+1\), and parameter-torsion duration \(b-a\).

Conversely let \(L=(x,sy)\) with the same mark. Then
\[
L=(x,y)\cap(x,s),\qquad J=(x,y),\qquad
Q_1\simeq k[[s]]/(s).
\]
The first carrier is smooth, so \(\Delta=0\) by the
[smooth-carrier comparison](../../results/local_filtration_comparison_defect.md#statement).
Thus neither vanishing implication holds in general local smooth
threefold geometry. These controls leave open comparisons subject to
additional actual homogeneous-source hypotheses for the fixed quartic.

## Section parity and relative coregularity have different supports

The finite module \(D=H^1_{(z,w)}(E)\) in (SS3) measures failure of
global sections at the cone vertex. The relative module
\(H_{I_C}^1(S/(f,g))\) measures extension from the residual complement;
under the stated first-coregularity and ambient vanishing hypotheses
it is the shifted second-coregularity defect. The
[actual-pair proof](../local-cohomology/actual_pair_coregularity.md)
retains those hypotheses and its projective annihilator-layer comparison.

The reduced quartic already has finite section defect \(kh\ne0\),
as computed in the [section-parity control](../torus/chow_section_parity_defect.md#3-the-single-quartic-control-and-the-remaining-question),
but \(H_{I_C}^1(S/I_C)=0\), since \(I_C\) annihilates \(S/I_C\).
In the other direction, an actual projective CI has zero Rao module,
while a genuine residual meeting \(C\) gives nonzero relative local
cohomology at an attachment. Locally the model \((x,sy)\) above has
\[
H_{(x,y)}^1(k[[s,y]]/(sy))
   =k((y))/k[[y]]\ne0.
\]
Neither a finite Rao defect nor \(\Delta\) can therefore be substituted
for the actual attachment annihilator layers. Equations (SS1)--(SL2)
provide actual-family comparisons without asserting such a substitution
or a universal obstruction to sole support.
