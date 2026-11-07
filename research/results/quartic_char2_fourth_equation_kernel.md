---
id: STCI-R-0031
type: result
title: Characteristic-two fourth normal equation and canonical kernel identification
scope: "#scope"
statement: "#statement"
proofs:
  - name: two-chart fourth-order lifts and filtered comparison
    at: "#proof"
    using: [STCI-R-0020, STCI-R-0057, STCI-R-0030]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Fourth normal equation in characteristic two

## Scope

Let \(k\) have characteristic two. Fix \(C=C_0=[s^4:s^3t:st^3:t^4]\)
in \(\mathbf P^3_k\) and the prescribed quartics
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3.
\]
Put \(Z=V(F,G)\), \(I=\mathcal I_C\), \(J=(F,G)\) as an ideal sheaf,
and \(K=I/J\) in \(\mathcal O_Z\). All line bundle degrees below refer to
\(C\simeq\mathbf P^1_k\), so \(\mathcal O_{\mathbf P^3}(d)|_C=\mathcal O_C(4d)\).

## Statement

Set \(E=I/I^2\), \(S=\operatorname{gr}_I\mathcal O_{\mathbf P^3}=\operatorname{Sym} E\),
\(H=\operatorname{in}_I(J)\) and \(Q_n=H_n/(S_+H)_n\), with \(S_+\) the
positive-degree ideal. Let \(D=J/IJ\) and let \(\phi:D\to E\) be the first
conormal map. Then \(D\simeq\mathcal O_C(-16)^{\oplus2}\) and
\[
M=\operatorname{im}\phi\simeq\mathcal O_C(-8),\qquad
L=\operatorname{coker}\phi\simeq\mathcal O_C(-6),\qquad
\ker\phi\simeq\mathcal O_C(-24).
\]
The line \(M\) differs from the conormal line of the containing quadric
\(x_0x_3-x_1x_2=0\). One has \(Q_1=M\) and
\(Q_4\simeq L^{\otimes4}\simeq\mathcal O_C(-24)\); all other \(Q_n\)
vanish.

For \(F^nD=((J\cap I^n)+IJ)/IJ\), the intrinsic filtration satisfies
\[
F^0D=F^1D=D,\qquad F^2D=F^3D=F^4D=\ker\phi,\qquad F^5D=0.
\]
The comparison defect \(\Delta=\operatorname{in}_I(IJ)/(S_+H)\)
vanishes. In degree four the canonical comparison is
\(Q_4\to F^4D/F^5D=\ker\phi\), and its inverse identifies
\(\ker\phi\) with \(Q_4\).

The intersection has reduced support \(C\), generic transverse length four
and \(K^4=0\). The first-order transition omits nonlinear terms in the
actual gluing of \(Z\).

## Proof

On \(x_0\ne0\), write \(a=x_1/x_0,\ u=x_2/x_0-a^3,\ v=x_3/x_0-a^4\).
On \(x_3\ne0\), write \(b=x_2/x_3,\ A=x_0/x_3-b^4,\ B=x_1/x_3-b^3\).
Use \(V,U\) for the conormal classes of \(v,u\), and
\(\bar A,\bar B\) for those of \(A,B\). The charts cover \(Z\) since
\(x_0=x_3=0\) forces \(x_1=x_2=0\) on its support. The chart ideals of
\(I\) are \((v,u)\) and \((A,B)\).

Write \(F_0,G_0\) for dehomogenization by \(x_0^4\), and
\(F_\infty,G_\infty\) for dehomogenization by \(x_3^4\).
Expanding in characteristic two gives
\[
\begin{aligned}
F_0&=v, & G_0&=u^4+a^8v+a^4v^2+v^3,\\
G_\infty&=A, & F_\infty&=B^4+b^8A+b^4A^2+A^3 .
\end{aligned}
\]
Thus \(J=(v,u^4)\) and \(J=(A,B^4)\) on the two charts. Both are
regular-sequence ideals, and the displayed changes of generators are
invertible. In particular \(F_0,G_0\) and \(F_\infty,G_\infty\) freely
generate \(D\) over the respective chart rings on \(C\). Indeed \(J/J^2\)
is free on the classes of the regular sequence over \(\mathcal O_Z\),
and tensoring with \(\mathcal O_C\) gives \(J/IJ\). Write
\(e_{F,0},e_{G,0}\) and \(e_{F,\infty},e_{G,\infty}\) for these frames.
Since \(x_3/x_0=a^4\) on \(C\), both equation frames transform by
\(a^{-16}\).

### First symbols and full initial ideal

In the conormal frames of
[R-0020](quartic_conormal_characteristic_jump.md) the quadric symbol on
the first chart is \(V-aU\), with transition \(a^{-8}\), and the
complementary \(U\)-direction has transition \(a^{-6}\). In the frames
used here this gives \(\bar A=a^{-8}V,\ \bar B=a^{-6}U\). Indeed, the
quadric symbol on the second chart is \(\bar A-b\bar B\), so substituting
\(b=a^{-1}\) on \(C\) cancels the complementary terms. The first symbols
of the quartics, with columns in order \(F,G\), are
\[
\phi_0=\begin{pmatrix}1&a^8\\0&0\end{pmatrix},
\qquad
\phi_\infty=\begin{pmatrix}b^8&1\\0&0\end{pmatrix}.
\]
Consequently \(M\) has frames \(V,\bar A\) and \(L\) has frames given by
\(U,\bar B\) modulo \(M\). The two sublines with symbols \(V\) and
\(V-aU\) differ on \(a\ne0\). The kernel has frames
\[
r_0=a^8e_{F,0}+e_{G,0},\qquad
r_\infty=e_{F,\infty}+b^8e_{G,\infty}=a^{-24}r_0 .
\]

[R-0057](quartic_normal_initial_base_change.md), using the prescribed
family of R-0021, gives the full ideals \(H=(V,U^4)\) and
\(H=(\bar A,\bar B^4)\) in the symmetric algebra on the two charts.
Hence \(Q_1=M\). Every higher term of \(H\) is a multiple of \(V\) or
\(U^4\) on the first chart, with the analogous generators on the second.
Only the new degree-four generator survives modulo \(S_+H\) in degrees
\(n\ge2\). Projection \(S\to\operatorname{Sym}L\) gives a canonical
isomorphism \(Q_4\to L^{\otimes4}\): in degree four the kernel on \(H_4\)
is precisely the submodule of multiples of the degree-one generator.
The classes of \(U^4,\bar B^4\) give the frames and their transition is
\(\bar B^4=a^{-24}U^4\).

### Canonical comparison and corrected lifts

In the first chart \(IJ=(v^2,vu,u^5)\); in the second it is
\((A^2,AB,B^5)\). These monomial ideals in the normal variables are
homogeneous in normal degree, so their initial ideals have the same
monomial generators in \(S\). On the first chart
\((V^2,VU,U^5)=(V,U)(V,U^4)\), since \(VU^4\) is a multiple of \(VU\).
On the second chart
\((\bar A^2,\bar A\bar B,\bar B^5)=(\bar A,\bar B)(\bar A,\bar B^4)\)
by the same divisibility. This proves \(\operatorname{in}_I(IJ)=S_+H\)
along all of \(C\).

Apply the quotient comparison in
[R-0030](local_filtration_comparison_defect.md) to the regular-sequence
ideal \(J\subset I\). The canonical surjection
\(Q_n\to F^nD/F^{n+1}D\) sends an initial symbol of an element of
\(J\cap I^n\) to the filtered class of that element in \(D\).
Its kernel is \(\Delta_n=0\). Directly, \(F^2D=\ker\phi\), and
\[
(a^8+a^4v+v^2)F_0+G_0=u^4,\qquad
F_\infty+(b^8+b^4A+A^2)G_\infty=B^4 .
\]
The corrections to the coefficients of \(r_0,r_\infty\) lie in \(I\).
Thus both kernel frames lift to normal order four and
\(F^2D=F^3D=F^4D\). Each monomial of normal degree at least five is in
\(IJ\) on either chart, giving \(F^5D=0\).
The canonical degree-four map takes the classes of \(U^4,\bar B^4\) to
\(r_0,r_\infty\), respectively. Their transitions agree, so the local
inverse identifications glue. In particular the identification uses the
actual corrected lifts and the comparison quotient.

### Embedded gluing

The first chart of \(Z\) has algebra \(k[a,u]/(u^4)\), where \(K=(u)\).
The opposite chart has algebra \(k[b,B]/(B^4)\), where \(K=(B)\).
These give reduced support \(C\), transverse length four and \(K^4=0\).
On their overlap in \(Z\), \(x_3/x_0=a^4\), so
\[
b=a^{-1}+a^{-4}u,\qquad
B=a^{-3}-b^3=a^{-6}u+a^{-9}u^2+a^{-12}u^3.
\]
The conormal transition records the \(a^{-6}\) linear coefficient of
\(B\) over \(b=a^{-1}\) on \(C\). The nilpotent correction to \(b\) and
the quadratic and cubic terms of \(B\) enter the embedded gluing.

## Limitations

This calculation concerns the prescribed characteristic-two pair. It
gives no general comparison for arbitrary characteristic-two pairs and
establishes neither a characteristic-zero lift nor an STCI obstruction.
The graded identification alone does not recover the nonlinear chart
gluing of this embedded intersection.

## Review

The Phase 5 nonauthor reviewer accepted the two-chart proof for this
prescribed pair using R-0020, R-0057 and R-0030. The reviewer checked the
first conormal transitions, the monomial \(IJ\) calculations, both
corrected lifts and the filtration jumps, and verified that the canonical
map sends the fourth-order symbols to the matching kernel frames. The
review also checked the support, length and nonlinear overlap in the two
actual chart algebras.

The [October 23 independent review](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#quartic-kernel-and-global-compatibility)
checked the overlap determinant, the balanced characteristic-zero frames,
both conormal matrices and the characteristic-zero cokernel lengths.
For characteristic two it checked the kernel and fourth-generator
transitions, the exact corrected lifts, the filtration jumps and the
invertibility of the canonical comparison in degree four. The
[source argument](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#7-explicit-rational-quartic-audit)
keeps the characteristic-zero calculation separate from the conclusion here.

The [October 23 Python certificate](../computations/verify_ideal_filtration_quartic_lifting_2026_10_23.py)
checks finite Laurent-polynomial identities over \(\mathbf Q,\mathbf Z\)
and \(\mathbf F_2\), including the chart expansions, first-normal
transitions, conormal matrices, exact lifts and nonlinear overlap
formula. All 27 identity checks passed in the Phase 5 replay. Support
exhaustion and the intrinsic comparison require the mathematical argument.
