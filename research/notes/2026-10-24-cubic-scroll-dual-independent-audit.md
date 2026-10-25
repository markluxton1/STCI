# Independent audit: the cubic scroll Gauss map and dual

Date: 2026-10-24. Reviewer role: `scroll_dual_audit`.
**Verdict: the claims below pass in their stated characteristic-zero scope.**
This is evidence for a provisional research package, not canonical promotion.

## Scope and retained input

Work over an algebraically closed field of characteristic zero with
\(R=(x_0x_2^2-x_1^2x_3=0)\) and \(Q=(x_0x_3-x_1x_2=0)\).
I read `research/INDEX.md`, `AUTHORITY.md`, and `CONTRIBUTING_AGENT.md`.
The retained input is the reviewed [normalization](2026-10-24-cubic-scroll-normalization.md):
\[
T=\mathbb F_1,\quad E^2=-1,\quad H=E+2f,\quad
\nu=[Av_0^2:Bv_0:Bv_1:Av_1^2],
\]
with Cox degrees \(\deg A=E,\deg B=E+f,\deg v_i=f\).
The conductor is \(D=(B=0)\sim E+f\), and \(E=(A=0)\).
The retained theorem and its old verification scripts were not rerun.
The new claims were independently reconstructed by differentiation,
intersection theory, and the two endpoint blowup charts, before reading
a completed author note.

## 1. Equation and generic inverse

In dual coordinates \([a:b:c:d]\), substitution in the gradient of \(R\)
has common factor \(B\). Removing it gives
\[
G=[Bv_1^2:-2Av_0v_1^2:2Av_0^2v_1:-Bv_0^2].                 \tag{1}
\]
Its entries have class \(E+3f=2H-D\), and satisfy
\[
F^\vee=ac^2+b^2d=0.                                        \tag{2}
\]
The cubic is irreducible: its coefficients \(c^2,b^2\) as a linear
polynomial in \(a,d\) are coprime. Moreover
\[
\nabla F^\vee(G)=
4Av_0^2v_1^2[Av_0^2:Bv_0:Bv_1:Av_1^2].                     \tag{3}
\]
On a dense open set this is an inverse, so the image has dimension two.
Thus \(R^\vee=V(F^\vee)\), of degree three, and the Gauss map is birational.
Merely exhibiting a containing cubic would not have proved this assertion.

## 2. Complete base scheme and resolution

The common zero scheme of (1) consists exactly of the two reduced points
\(q_0=(B=v_1=0)\) and \(q_\infty=(B=v_0=0)\).
When \(v_0v_1\ne0\), vanishing of the middle coordinates forces \(A=0\)
and then the outer ones force \(B=0\), impossible in the projective bundle.
Near \(q_0\), write \(r=B/A,w=v_1/v_0\); then
\[
\nu=[1:r:rw:w^2],\qquad G=[rw^2:-2w^2:2w:-r].              \tag{4}
\]
The base ideal is exactly \((r,w)\). In the blowup chart \(r=wt\),
division by the exceptional equation gives \([tw^2:-2w:2:-t]\);
in \(w=rz\) it gives \([r^2z^2:-2rz^2:2z:-1]\).
There are no further base points. The exceptional curve maps
isomorphically to \(\ell_0=(a=b=0)\), while the strict old fiber maps
to \([0:0:0:1]\). Reversal gives the other endpoint and
\(\ell_\infty=(c=d=0)\).

Let \(\pi:\widetilde T\to T\) blow up these points, with exceptional
curves \(e_0,e_\infty\). The resolved system has class
\[
M=\pi^*(E+3f)-e_0-e_\infty,\qquad M^2=3.
\]
The two disjoint strict endpoint fibers
\(F_i=\pi^*f-e_i\) are \((-1)\)-curves with \(MF_i=0\).
Contracting them performs two elementary transformations over the same
base. The strict conductor has square \(1-2=-1\) and is disjoint from
both \(F_i\), so it becomes the target negative section.
The source negative section meets each contracted fiber once and its
image has square \(-1+2=1\). The resulting ruled surface is
\(\mathbb F_1\). Its hyperplane pullback is precisely
\[
\rho^*(E^\vee+2f)=\widetilde D+2\pi^*f=M.
\]
On a dense coordinate domain the target normalization is
\[
\nu^\vee=[A'v_1^2:-B'v_1:B'v_0:-A'v_0^2],\qquad
[A':B']=[B:2Av_0v_1].                                      \tag{5}
\]
The first tuple is a coordinate permutation and sign change of the
retained finite normalization of \(R\), hence is the normalization of (2).
This identifies the target morphism and proves the full factorization.

The source conductor \(D\) therefore becomes the target simple directrix;
the source negative section becomes the target conductor. The latter
maps with degree two to the dual double line. Endpoint ruling fibers
are contracted by the Gauss map, whereas general fibers are not.
Birationality must not be strengthened to finiteness.

## 3. Singular scheme, including saturation

The reduced singular line of (2) is \(L^\vee=(b=c=0)\). The homogeneous
Jacobian ideal and its saturation are respectively
\[
J=(c^2,bd,ac,b^2),\qquad
J^{\rm sat}=(b^2,bc,c^2,ac,bd).                             \tag{6}
\]
The extra generator \(bc\) matters when giving a saturated ideal:
multiplication by each homogeneous coordinate puts \(bc\) in \(J\).
The larger monomial ideal is saturated. A monomial outside it either
contains neither \(b,c\), or is \(a^i b\), or is \(c d^j\);
multiplying by a suitable endpoint coordinate keeps it outside.

On \(a=1\), the ideal is \((c,b^2,bd)\). The nilpotent class of \(b\)
is annihilated by \((b,d)\), so the reduced line has one embedded
length-one point at \([1:0:0:0]\). On \(d=1\) there is one at the other
endpoint. Away from them the singular scheme is reduced.
The cubic itself has general double crossings and two pinch points.
Its finite normalization (5) has a degree-two conductor cover branched
at those endpoints. The cubic's singularities and its singular
subscheme are distinct assertions.

## 4. Scheme intersection with the dual quadric

Polarity gives \(Q^\vee=(ad-bc=0)\). On its Segre coordinates
\([a:b:c:d]=[pr:ps:qr:qs]\),
\[
F^\vee|_{Q^\vee}=pq(qr^3+ps^3).
\]
Therefore the scheme intersection is the reduced Cartier divisor
\[
R^\vee\cap Q^\vee=\ell_0+\ell_\infty+K,
\]
where \(K=(qr^3+ps^3=0)\) is a smooth \((1,3)\) quartic.
It is a graph over \([r:s]\); the cubics \(r^3,s^3\) have no common zero.
The three factors are distinct prime divisors on the smooth quadric,
so the scheme is reduced and has no embedded component.
\(K\) meets each line with order three at the relevant pinch endpoint.
Tangential intersection of reduced components does not make the union
nonreduced.

A parametrization is
\[
K=[-t^4:st^3:-s^3t:s^4].
\]
For \(u\ne0,\infty\), its plane \(H_K=[-u^4:u^3:-u:1]\) is tangent to
\(R\) at \([1:2u:2u^3:u^4]\) and to \(Q\) at
\([1:u:-u^3:-u^4]\). The contact points are different.
A general member \([0:0:c:d]\) of \(\ell_0\), with \(c\ne0\),
is only a limiting tangent plane to \(R\) at the first pinch point.
It is not an actual smooth Gauss value: its first gradient coordinate
\(x_2^2=0\) would force its third \(2x_0x_2=0\).
The endpoint exceptional curve supplies precisely these limits.
The reversed assertion holds on \(\ell_\infty\).

## 5. No same-point tangent plane at a common smooth point

Use the retained divisor identity \(R|_Q=C+L_0+L_\infty\).
For \(u\ne0,\infty\), the normalized tangent-plane coefficients along \(C\) are
\[
T_{c(u)}R=[-u^4:2u^3:-2u:1],\quad
T_{c(u)}Q=[u^4:-u^3:-u:1].
\]
They are unequal in characteristic zero. On a smooth point
\([A:B:0:0]\in R\cap L_0\), necessarily \(B\ne0\);
the tangent planes are \([0:0:0:1]\) and \([0:0:-B:A]\),
again unequal. The reversed calculation applies to \(L_\infty\).
The endpoints are singular on \(R\).
Thus no point where both surfaces are smooth has a same-point common
tangent plane, despite the full three-component dual intersection.

## Audit boundary

No counterexample or omitted boundary remains in the stated scope.
The material addition to the initial proposal was the saturation
distinction in (6) and the two embedded points of the singular scheme.
This audit covers no arbitrary cubic-scroll projection, positive
characteristic theorem, separate \(C^\vee\)-intersection calculation,
or STCI implication.

## Follow-up audit: flag restriction and characteristic two

After the core reconstruction I read Section 5 of the author's
[final cubic-duality note](2026-10-24-cubic-scroll-gauss-dual.md).
The identification of its dual normalization with a restriction of the
residual flag also passes.

Indeed, for the degree-two divisor
\(D=(v_0t^2-v_1s^2=0)\), restriction of
\(a s^4+b s^3t+c st^3+d t^4\) gives the conditions
\(a+d w^2=b+c w=0\) on \(v_0=1,w=v_1/v_0\).
The global kernel is therefore the subbundle generated by
\[
(v_1^2,0,0,-v_0^2),\qquad(0,-v_1,v_0,0).
\]
These vectors are everywhere independent, including \(v_0v_1=0\);
their summands are \(\mathcal O(-2)\) and \(\mathcal O(-1)\).
Its projectivization of lines is the plane-through-ruling bundle
\(\mathbb F_1\), with plane map (5).

For any plane section containing \(D\), division by its defining binary
quadratic gives a unique residual quadratic, up to the relevant scalar.
Consequently this plane bundle agrees with
\(\operatorname{pr}_1^{-1}(L_\iota)\) in the residual flag.
At \(D=2p_0,2p_\infty\), restriction is restriction to the full doubled
divisor, so its kernel retains the entire tangent-line pencil.
Thus the identification includes the endpoint schemes; it is not only
a generic comparison of ruling lines.

Finally, in characteristic two the actual gradient of \(R\) is
\([x_2^2:0:0:x_1^2]\), whose reduced scheme image is the line \(b=c=0\).
On \(T\) its common factor is now \(B^2\), and after removing it the
map is \([v_1^2:0:0:v_0^2]\), factoring through the inseparable
degree-two map on the ruling base. The specialized equation
\(ac^2+b^2d=0\) still defines a cubic surface, but it is not the actual
dual of the characteristic-two surface. This directly verifies the
author's characteristic warning without transferring characteristic-zero
Gauss geometry across the fiber.


