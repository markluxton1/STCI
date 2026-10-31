# A sharp ruled-surface degree criterion in every characteristic

**Status:** independently reviewed mathematical contribution; no new canonical result is promoted.

Let \(k\) be an algebraically closed field of arbitrary characteristic.
Let \(M\) be a smooth projective surface and \(L\) a nef Cartier divisor
such that
\[
 d=L^2>0,\qquad A=-K_ML>0.
\]
A rational curve means an integral curve whose normalization is
\(\mathbf P^1\); it need not itself be smooth. For such a curve \(R\),
put \(\delta=LR\).

**Theorem.** If \(A\delta>d\), then \(M\) is rational. More precisely,
if \(M\) is not rational, then it is birationally ruled over a smooth
projective curve \(B\) of genus \(g\ge1\), and every rational curve of
positive \(L\)-degree satisfies
\[
 \boxed{d\ge A\delta+(2g-2)\delta^2.}                 \tag{R1}
\]
In particular, the criterion in
[the quartic-carrier proof, §2](quartic_carrier_proof.md#2-why-a-nonnormal-normalization-is-rational)
holds in every characteristic: its notation has
\(A=d+2-2\pi\). Neither a mate, a surface embedding, nor a vanishing theorem
is needed for this intrinsic statement.

## Why a ruled model exists

Contract smooth rational \((-1)\)-curves until a smooth minimal surface
\(M_0\) is reached. Nefness descends under each contraction: if
\(p:X\to Y\) blows down \(E\), write
\(L_X=p^*L_Y-mE\), where \(m=L_XE\ge0\). For every integral curve
\(D\subset Y\), with strict transform \(D'\),
\[
 L_YD=L_XD'+m\operatorname{mult}_{p(E)}D\ge0.
\]
The canonical formula gives \(K_XL_X=K_YL_Y+m\). Consequently the
nef pushdown \(L_0\) satisfies \(K_{M_0}L_0<0\). If \(K_{M_0}\)
were nef, its intersection with the nef divisor \(L_0\) would be
nonnegative. Hence it is not nef, so some effective curve has negative
canonical intersection.

The precise surface input is the minimal ruledness theorem: a smooth
projective minimal surface with negative canonical intersection against
an effective divisor is birationally ruled. For positive characteristic,
this is proved directly in Mumford,
[*Enriques' classification of surfaces in char p: I*, §1, pp. 326–330](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969b--EnrClass-I-NC.pdf).
The characteristic-zero version is the same classical minimal-surface
alternative. A supplementary modern positive-characteristic reference is
Tanaka's
[minimal-model theorem, Theorem 1.1](https://arxiv.org/pdf/1201.5699):
with boundary zero it gives a minimal model or a Mori fiber space over
any algebraically closed field of positive characteristic. The argument
here uses the smooth minimal ruledness alternative, not abundance,
Kawamata–Viehweg vanishing, or the classification of the nonnegative
Kodaira-dimension cases.

Thus \(M\) is rational or birational to \(B\times\mathbf P^1\).
If it is not rational, \(g(B)\ge1\). Choose a ruled bundle
\(S=\mathbf P_B(\mathcal E)\), and a common smooth resolution
\[
 W\xrightarrow{\rho}M,\qquad W\xrightarrow{\tau}S.
\]
The second morphism factors as a sequence of point blowups, possibly
at infinitely near points. Replacing \(M,L,R\) by
\(W,\rho^*L,R_W\) preserves \(d,A,\delta\): pullback preserves the
square and the curve degree, and the relative canonical divisor of
\(\rho\) is exceptional and has zero intersection with \(\rho^*L\).
This avoids assuming that the original surface admits a prescribed
blowdown to the selected ruled bundle.

## The multiplicity bound includes infinitely near centers

Write the blowup sequence as
\(S=X_0\leftarrow X_1\leftarrow\cdots\leftarrow X_N=W\).
Let \(L_i\) be the pushdown of the nef divisor on \(W\); every \(L_i\)
is nef by the preceding calculation. At the \(i\)-th blowup,
\[
 L_i=p_i^*L_{i-1}-m_iE_i^{\rm new},\qquad m_i\ge0.
\]
Let \(f\) be the fiber class on \(S\), and set \(a=L_0f\).
All surfaces \(X_i\) map to \(B\), and every complete fiber cycle
has \(L_i\)-degree \(a\). The positivity \(a>0\) follows from
\(L_0^2\ge d>0\): a nef class of positive square cannot be orthogonal
to the nonzero fiber class of square zero, by the Hodge index theorem.

At a center \(x\in X_{i-1}\), select an irreducible component \(D\)
of its actual fiber through \(x\). Write that fiber as
\(F=\sum n_jD_j\). All component degrees are nonnegative, so
\(L_{i-1}D\le a\), even when the fiber is nonreduced. If \(D'\)
is the strict transform, nefness gives
\[
 0\le L_iD'=L_{i-1}D-m_i\operatorname{mult}_xD.
\]
Since \(\operatorname{mult}_xD\ge1\), this proves
\[
 \boxed{0\le m_i\le a.}                             \tag{R2}
\]
The proof uses the fiber on the surface immediately before each blowup,
so no assumption of distinct or ordinary centers is hidden in (R2).

## The identity and the rational-curve bound

Choose a section class \(C_0\) of \(S\), with \(C_0^2=-e\).
Numerically write \(L_0=aC_0+bf\). In the total-transform basis
\(E_i\) on \(W\), the intersection formulas are
\[
 \begin{aligned}
 L&=\tau^*L_0-\sum_i m_iE_i,\\
 d&=a(2b-ae)-\sum_i m_i^2,\\
 -A&=a(2g-2+e)-2b+\sum_i m_i.
 \end{aligned}
\]
Here the total transforms, not the strict exceptional curves, have
\(E_iE_j=-\delta_{ij}\). Eliminating \(b\) gives
\[
 \boxed{d=(2g-2)a^2+Aa+\sum_i m_i(a-m_i).}           \tag{R3}
\]
All summands in the last sum are nonnegative by (R2).

Every rational curve on \(W\) maps constantly to \(B\). Indeed, a
nonconstant map from its normalization \(\mathbf P^1\) would give an
intermediate function field
\(k\subset k(B)\subset k(t)\). Lüroth's theorem makes \(k(B)\)
rational, contradicting \(g\ge1\). Lüroth's theorem has no separability
hypothesis; this also excludes purely inseparable or mixed maps to a
positive-genus base. Equivalently, one can factor off Frobenius maps and
apply separable Riemann–Hurwitz to the remaining map from \(\mathbf P^1\).

Thus \(R_W\) is an irreducible component of an actual complete fiber.
The same component-degree argument gives \(\delta\le a\). For
\(g\ge1\), the function \(At+(2g-2)t^2\) is increasing for
\(t\ge0\). Equation (R3) now gives
\[
 d\ge Aa+(2g-2)a^2\ge A\delta+(2g-2)\delta^2,
\]
proving (R1) and the rationality criterion.

## Sharpness and the characteristic boundary

The bound is sharp for every base genus \(g\ge1\). On
\(M=B\times\mathbf P^1\), let
\(C_0=B\times\{q\}\), \(f=\{p\}\times\mathbf P^1\), and
\(L=aC_0+bf\), where \(a,b\) are positive integers and
\(b>(g-1)a\). This divisor is ample, and
\[
 d=2ab,\quad A=2b-(2g-2)a>0,\quad Lf=a.
\]
The rational fiber \(R=f\) attains equality in (R1). In genus one,
\(A\delta=d\) on a nonrational surface; the strict inequality in the
rationality criterion therefore cannot be weakened to \(A\delta\ge d\).

The conclusion is birational rationality, not a claim that every negative-
Kodaira-dimension surface is itself a ruled bundle. In positive
characteristic, merely being covered by rational curves, or admitting an
inseparable rational parametrization, does not supply this argument's
ruled model. The hypothesis \(K_ML<0\), together with the smooth minimal
ruledness theorem, supplies it.

Only this intrinsic criterion has been extended. In any characteristic,
if a particular quartic normalization resolution is already known to have
\(d=\delta=4\), \(K_ML=2\pi-6\), and \(\pi\le2\), the criterion
proves that resolution rational. Establishing these inputs in a new
characteristic is separate from applying the criterion. The cohomological
refinements, conductor descent, differential cancellation, and the
normal-quartic exclusion retain their individual characteristic
hypotheses. In particular the
[actual positive-characteristic quartic-carrier constructions](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
remain compatible with this theorem. The characteristic table in
[the carrier proof, §8](quartic_carrier_proof.md#8-what-changes-in-positive-characteristic)
can now attribute the ruled criterion to the characteristic-free smooth
minimal-surface alternative, instead of restricting the criterion to
characteristic zero.

## The first positive integral gap

Retain the hypotheses and notation of the criterion above:
\(M\) is a smooth projective surface over an algebraically closed field of
arbitrary characteristic, \(L\) is a nef **Cartier** divisor,
\(d=L^2>0\), \(A=-K_ML>0\), and \(R\) is an integral rational curve
of degree \(\delta=LR\). The integrality of the blowup multiplicities
is essential to this refinement.

**Integral gap theorem.** If \(M\) is not rational and \(\delta\ge2\),
then
\[
 \boxed{d=A\delta\quad\text{or}\quad
        d\ge A\delta+\delta-1.}                    \tag{G1}
\]
Consequently, either \(d<A\delta\) or
\(0<d-A\delta<\delta-1\) forces rationality. The equality case
\(d=A\delta\) remains possible.

**Proof.** Use the common resolution over a ruled bundle as in the degree
criterion. Its integer fiber degree \(a\) and integer blowup
multiplicities \(m_i\) satisfy
\[
 a\ge\delta,\qquad 0\le m_i\le a,\qquad
 d=(2g-2)a^2+Aa+\sum_i m_i(a-m_i).
\]
The genus inequality already gives \(r=d-A\delta\ge0\). Suppose
\(0<r<\delta-1\). If \(g\ge2\), the same inequality gives
\(r\ge2\delta^2\), a contradiction. Thus \(g=1\), and
\[
 q:=\sum_i m_i(a-m_i)=d-Aa
   =r-A(a-\delta),\qquad 0\le q\le r.
\]
For an integer \(m_i\) strictly between zero and \(a\),
\[
 m_i(a-m_i)\ge a-1\ge\delta-1>r.
\]
Therefore every \(m_i\) is zero or \(a\), and \(q=0\).

It remains to use the actual fiber containing \(R\), rather than stop at
the numerical equality \(d=Aa\). Before any blowup, a fiber has its
single component of degree \(a\). If every fiber component on the
preceding surface has degree divisible by \(a\), then after a blowup
at \(x\) its strict transform has degree
\[
 L_iD'=L_{i-1}D-m_i\operatorname{mult}_xD,
\]
again divisible by \(a\); the new exceptional component has degree
\(m_i\), which is zero or \(a\). Induction proves divisibility for
every actual fiber component, including at infinitely near centers.
All degrees are nonnegative and the complete fiber has degree \(a\).
The positive degree \(\delta\) of \(R\) is thus a positive multiple
of \(a\) at most \(a\), so \(\delta=a\). But then
\(d=Aa=A\delta\), contradicting \(r>0\). This proves (G1).

**Sharpness.** Let \(B\) be an elliptic curve,
\(S=B\times\mathbf P^1\), \(C_0=B\times\{q\}\), and
\(f=\{p\}\times\mathbf P^1\). Fix integers \(\delta\ge2\) and
\(b\ge3\). The divisor
\(L_0=\delta C_0+bf\) is very ample: it is the external product of
a degree-\(b\) very ample bundle on \(B\) and
\(\mathcal O_{\mathbf P^1}(\delta)\). Blow up one point,
\(\pi:M\to S\), with exceptional curve \(E\), and take
\(L=\pi^*L_0-E\). Hyperplanes through the point generate this line
bundle on the blowup, so it is nef. For a fiber \(R\) avoiding that
point,
\[
 LR=\delta,\qquad d=2\delta b-1,\qquad A=2b-1,
 \qquad d-A\delta=\delta-1.
\]
The surface is still birationally elliptic ruled and is not rational.
Thus the first permitted positive gap in (G1) is attained in every
characteristic, for every \(\delta\ge2\).

**Higher-degree applications and prior scope.** For a smooth resolution
of a carrier normalization, let \(L\) be its pulled-back hyperplane
divisor and assume the actual resolution contains a rational curve of
\(L\)-degree four. If the numerically established sectional-genus data
are
\[
 L^2=5,\qquad K_ML=2\pi-7,\qquad \pi\le3,
\]
then \(M\) is rational. For \(\pi\le2\) the original strict
criterion suffices; for \(\pi=3\) one has
\((d,A,\delta)=(5,1,4)\) and
\(0<d-A\delta=1<3\), so (G1) supplies the missing case.
This recovers the existing [low-sectional-genus quintic reduction](../supplements/QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#5-low-sectional-genus-the-ruled-argument-audited) as a corollary of the common integer-multiplicity mechanism. It is not a new quintic result or a carrier exclusion.

A further conditional instance for the fixed degree-four curve is
\[
 L^2=10,\qquad K_ML=-2,\qquad LR=4.
\]
Here \((d,A,\delta)=(10,2,4)\) and
\(0<d-A\delta=2<3\), so \(M\) is rational, while the original strict
criterion \(A\delta>d\) does not apply. In carrier language these are
an actual degree-ten normalization-resolution polarization with an
actual rational degree-four lift and the established adjunction value
\(K_ML=2\pi-12=-2\), i.e. \(\pi=5\). The same conclusion holds
for \(\pi\le5\): smaller genus is covered by the strict criterion.
This is a conditional rationality reduction, with no existence or
exclusion assertion about such carriers.

Neither application assumes that every integral carrier is generically
regular along the fixed quartic, that its inverse image is a single
curve, or that a sectional-genus formula has been established merely
from its degree. The actual rational curve and numerical resolution
inputs must be supplied. These results make no STCI exclusion in any
new degree or characteristic.

## Review and application scope

Independent reconstruction checked the smooth minimal ruledness theorem against Mumford, the canonical-intersection signs, nef descent through infinitely near centers, common-resolution invariance, the fiber bound for rational curves in inseparable characteristic, and the sharp product examples. The stated theorem is accepted at these hypotheses. This does not extend the characteristic scope of the quartic-carrier exclusion, its cohomological refinements, or conductor arguments.

Independent review also reconstructed the integral-gap refinement and its sharp elliptic one-point-blowup examples, including nefness by hyperplanes through the center and fiber-component divisibility at infinitely near centers. The degree-ten application assumes an actual rational lift and the displayed numerical resolution data; it supplies no carrier-existence or STCI exclusion.
