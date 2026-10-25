# Three dual surfaces and two discriminant identities

Date: 2026-10-24. Author: `dual_intersections` independent investigation.

**Status: new proved propositions in a provisional geometry package; no
canonical promotion and no STCI conclusion.** Work over an algebraically
closed field of characteristic zero throughout. The curve is the fixed
marked embedding
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

## 1. Scope, retained evidence, and conventions

The [research index](../INDEX.md), [contribution checklist](../CONTRIBUTING_AGENT.md),
[discussion reconciliation](2026-10-24-discussion-reconciliation.md),
[earlier dual-incidence derivation](2026-10-24-special-dual-incidence-derivation.md),
and [merged ruled-surface synthesis](2026-10-24-p4-ruled-surfaces-synthesis.md)
are the retrieval route. We retain the earlier identification of
\(C^\vee\) with the restricted binary-quartic discriminant, together with
the two endpoint pencil lines and the osculating quartic. These are
previously reviewed provisional geometry, not promoted canonical results.
The dual cubic equation is also reconstructed below to fix its signs.
No normal-bundle splitting or carrier exclusion is needed.

Dual coordinates \([A:B:C:D]\) mean the hyperplane
\(Ax_0+Bx_1+Cx_2+Dx_3=0\). Its section on the parameter line is
\[
f=A s^4+B s^3t+C st^3+D t^4.
\]
Let
\[
\begin{aligned}
M&=AD-BC,& L&=BC-4AD,\\
K&=AC^2+B^2D,& N&=AC^2-B^2D.
\end{aligned}
\]
The dual quadric is \(Q^\vee=V(M)\). The dual of
\(R=V(x_0x_2^2-x_1^2x_3)\) is \(R^\vee=V(K)\).
Indeed the ruling parametrization \([a:b:zb:z^2a]\) gives Gauss image
\([z^2b:-2z^2a:2za:-b]\), and substitution gives \(K=0\).
This image is two-dimensional; its closure is the irreducible cubic
\(V(K)\). Its finite normalization, distinct from its singular projected
image, is the cubic scroll \(\mathbb F_1\); the
[Gauss-map investigation](2026-10-24-cubic-scroll-gauss-dual.md)
studies that normalization and the resolved Gauss map.

Write \(\Delta\) for the ordinary discriminant of
\(A+Bu+Cu^3+Du^4\), interpreted homogeneously as the binary-quartic
discriminant. Thus \(C^\vee=V(\Delta)\).

## 2. The invariant bridge

**Proposition 1.** There are exact polynomial identities
\[
\boxed{\Delta=-4L^3-27K^2}
\tag{1}
\]
and
\[
\boxed{\Delta=4M(8AD+BC)^2-27N^2.}
\tag{2}
\]

**Proof.** For a binary quartic
\(a t^4+b st^3+c s^2t^2+d s^3t+e s^4\), use the coefficient
normalization
\[
I=12ae-3bd+c^2,
\quad
J=72ace+9bcd-27ad^2-27b^2e-2c^3,
\quad
\Delta=(4I^3-J^2)/27.
\]
For the marked linear system, \((a,b,c,d,e)=(D,C,0,B,A)\), hence
\(I=-3L\) and \(J=-27K\), proving (1).
Furthermore
\[
K^2-N^2=4AB^2C^2D,
\qquad
L^3+27AB^2C^2D=-M(8AD+BC)^2,
\]
or direct expansion gives (2). For verification, the full discriminant is
\[
256A^3D^3-192A^2BCD^2-27A^2C^4
-6AB^2C^2D-27B^4D^2-4B^3C^3.
\]
The invariant formulas give the geometric explanation: the projected
dual cubic is the restriction of the classical locus \(J=0\), while
\(L=0\) is the invariant quadric \(I=0\). The containing dual quadric
\(M=0\) is a different quadric. These are classical binary-quartic
invariants; this note makes no novelty claim. The restriction identifies
the objects in this particular marked embedding. \(\square\)

Equation (1) does not assert that \(C^\vee\) is globally a product of a
cusp with a curve. The map given by the invariant expressions can have
critical loci; local singular-scheme analysis must retain that map.

## 3. Full intersection with the dual cubic

**Proposition 2.** The full projective scheme intersection is
\[
C^\vee\cap R^\vee=V(K,L^3).
\tag{3}
\]
Set \(D_R=V(K,L)\). This is a reduced complete-intersection curve, the
union of the osculating quartic \(O\) and the two endpoint pencil lines
\[
\ell_0=V(A,B),\qquad \ell_\infty=V(C,D).
\]
Consequently (3) is the triple effective Cartier divisor \(3D_R\) on
\(R^\vee\). Its fundamental cycle is
\[
3[O]+3[\ell_0]+3[\ell_\infty].
\]
The equation (3), rather than this cycle alone, specifies all scheme
structure at the hyperosculating endpoints.

**Proof.** Identity (1) gives equality of ideals
\((K,\Delta)=(K,L^3)\), since 4 is invertible. The cubic is integral,
and \(L\) is nonzero on it, so its restriction is a nonzerodivisor and
defines a Cartier divisor.

On \(D=1\), eliminating \(A=BC/4\) from \(L=0\) gives
\[
K=B(B+C^3/4).
\tag{4}
\]
One branch is \(\ell_0\). The other is the osculating quartic,
parametrized on this chart by
\[
[-u^4:2u^3:-2u:1].
\]
The reversed chart \(A=1\) gives the osculating curve and
\(\ell_\infty\). The remaining possible points have \(A=D=0\)
and \(BC=0\); they are the points \([0:1:0:0]\) and
\([0:0:1:0]\), already on the corresponding lines. The complete
intersection \((K,L)\) is Cohen--Macaulay, hence has no embedded
associated points. It is generically reduced on its three support
components by (4), its reversal, and the nonsingular line charts.
A generically reduced Cohen--Macaulay curve is reduced. This also proves
that \((K,L^3)\) has no extra embedded points: it too is a complete
intersection. \(\square\)

At \(H_0=[0:0:0:1]\), equation (4) exhibits two smooth reduced branches
meeting to order three. On the smooth ambient quadric \(L=0\), the
intersection ideal is \((B,C^3)\), of length three. The same holds at
\(H_\infty=[1:0:0:0]\). This contact is part of the reduced Cartier
divisor \(D_R\); the full intersection additionally cubes its principal
ideal inside the singular cubic. One must not replace \((K,L^3)\) by
the cube of the ambient ideal \((K,L)\).

There is a useful complete normalization check. On a chart of the dual
scroll with \(D=-1\), write
\[
[A:B:C:D]=[z^2:-za:a:-1].
\]
Then the hyperplane section of the original curve factors as
\[
z^2-za u+a u^3-u^4
=-(u^2-z)(u^2-au+z),
\tag{5}
\]
and
\[
\nu^*L=z(4z-a^2),\qquad
\nu^*\Delta=4z^3(a^2-4z)^3.
\tag{6}
\]
The three factors of the discriminant product formula are respectively
\(4z\), \(a^2-4z\), and the square of
\(z(4z-a^2)\). Thus the same double-root collision simultaneously
affects a quadratic and the resultant of the two quadratics. This
explains the exponent three through residual divisors.

Globally, on \(\mathbb F_1\), let \(E^2=-1\), let \(f\) be a ruling
fiber, and let \(H=E+2f\) be the dual hyperplane class. The strict
osculating quartic has class \(2E+2f\), and (6), with its reversed chart,
gives the exact Cartier pullbacks
\[
\nu^*D_R=\widetilde O+f_0+f_\infty\sim2H,
\quad
\nu^*(C^\vee\cap R^\vee)
=3\widetilde O+3f_0+3f_\infty\sim6H.
\]
These assertions concern the pullback of the **entire principal divisor**
\(D_R\). They do not identify the full inverse ideal of the individual
curve \(O\) with its divisorial hull. Indeed, on this \(D=-1\) chart,
\[
I_O=(A-C^4/16,\ B+C^3/4),\qquad
I_O\mathcal O_{\mathbb F_1}
=(z-a^2/4)(z,a).
\tag{10}
\]
The last factor is the colength-one endpoint correction. Thus the full
inverse ideal and the strict Cartier curve differ even though the
pullback of their union with the endpoint fibers is principal.

## 4. Full intersection with the dual quadric

**Proposition 3.** The full projective scheme intersection is
\[
C^\vee\cap Q^\vee=V(M,N^2).
\tag{7}
\]
Let \(\Gamma_Q\) denote the image of the quadric-tangent section
\(p\mapsto T_pQ\). Then the reduced complete intersection
\(D_Q=V(M,N)\) equals
\(\Gamma_Q\cup\ell_0\cup\ell_\infty\), and (7) is the double
Cartier divisor
\[
2D_Q=2\Gamma_Q+2\ell_0+2\ell_\infty
\quad\hbox{on }Q^\vee.
\]

**Proof.** Identity (2) gives
\((M,\Delta)=(M,N^2)\). In Segre coordinates
\[
[A:B:C:D]=[ac:ad:bc:bd],
\]
the original hyperplane section and the cubic \(N\) factor as
\[
f=(a s^3+b t^3)(c s+d t),
\qquad
N=ab(bc^3-ad^3).
\tag{8}
\]
The third factor in \(N\) is the smooth graph
\(ad^3=bc^3\); it is the quadric-tangent curve, with parametrization
\[
\Gamma_Q(u)=[u^4:-u^3:-u:1].
\]
The first two factors are the two endpoint pencil lines. They are
distinct reduced divisors, so \(D_Q\) is reduced. Alternatively the
discriminant product formula applied to (8) gives the exact identity
\[
\Delta|_{Q^\vee}=-27a^2b^2(ad^3-bc^3)^2,
\tag{9}
\]
including all boundary points. The repeated factors are forced by the
resultant square and the discriminant \(-27a^2b^2\) of the cubic
factor. This proves the scheme statement, not just its support. \(\square\)

The line \(a=0\) meets \(\Gamma_Q\) at \(c=0\), with intersection
length three; the other line has the reversed endpoint behavior.
The total degree is \(2(4+1+1)=12\), as required for a sextic cut on a
quadric. Equation (3) has degree \(3(4+1+1)=18\). These degree checks
corroborate, but do not substitute for, the exact ideal identities.

For comparison, the third full intersection is
\[
R^\vee\cap Q^\vee=V(M,K).
\]
Its pullback to the same Segre quadric is the reduced divisor
\(ab(bc^3+ad^3)=0\): the two endpoint lines and a different smooth
quartic. The [scroll-duality note](2026-10-24-cubic-scroll-gauss-dual.md)
provides its interpretation and the Gauss maps. The minus and plus
signs in (8) and this last equation cannot be interchanged. In
particular \(\Gamma_Q\), \(O\), and this third quartic are distinct.

## 5. Full dual intersections versus common-point traces

The quadric-tangent section of the conormal surface maps to
\(\Gamma_Q\), while the closure of the Gauss trace of \(R\) along
the smooth part of \(C\) maps to \(O\). These are the distinguished
same-point constructions.

For a general point \([0:0:C:D]\in\ell_0\), the plane section of
\(C\) is \(t^3(Cs+Dt)\), so its contact point on \(C\) is \(p_0\).
The tangency point on the smooth quadric, determined by its polarity,
is
\[
[D:-C:0:0].
\]
This usually differs from \(p_0=[1:0:0:0]\). The endpoint pencil line
in \(C^\vee\cap Q^\vee\) therefore records tangencies at different
points of the two varieties. Only its limiting hyperosculating plane
\([0:0:0:1]\) has the quadric tangency point \(p_0\).

For \(R\), the same endpoint line is a family of limiting tangent
planes at its singular pinch point. A general plane of this pencil is
not obtained by following \(T_pR\) along smooth points \(p\in C\)
as \(p\to p_0\); that particular path selects only the osculating
limit \(H_0\). The reversed statements hold at infinity. Thus the
extra lines are actual components of the full dual intersection, while
the closure of the marked smooth-curve trace is the single quartic
\(O\). They must not be discarded or identified with the distinguished
section.

The reduced common intersection of all three dual surfaces is exactly
\(\ell_0\cup\ell_\infty\). Indeed on \(Q^\vee\), requiring both
\(K=0\) and \(\Delta=0\) away from \(ab=0\) would require
\(bc^3+ad^3=bc^3-ad^3=0\), impossible there in characteristic zero.
This is a support statement only; the equations above retain the full
triple-intersection scheme if it is needed.

## 6. Reproduction, limitations, and next questions

Run

```sh
/tmp/stci-z4-env/bin/python research/computations/verify_quartic_dual_intersections_2026_10_24.py
```

The [verifier](../computations/verify_quartic_dual_intersections_2026_10_24.py)
and its [JSON evidence](../computations/quartic_dual_intersections_2026_10_24.json)
check the discriminant, invariant identities, complete-intersection ideal
equalities, residual factorizations, endpoint contact length, and
normalization-chart restrictions over \(\mathbf Q\). The proofs above
supply the global geometric interpretation and reducedness arguments.

The whole package is restricted to the fixed marked embedding in
characteristic zero. In characteristic two or three, constants used in
the invariant/discriminant identities cease to be units; the conclusions
about reduced divisors and multiplicities cannot be specialized from
these equations without a separate analysis. No claim is made here
about the scheme-theoretic singular locus of \(C^\vee\); that is
addressed in the separate singular-scheme investigation.

The useful next extension is to vary the projection hyperplane
\(V\subset H^0(\mathcal O(4))\). The binary-quartic invariant identity
persists before restriction, whereas the accidental identification of
the restricted cubic \(J=0\) with the dual of this paired-secant scroll
requires a new argument for another center. The residual factorization
on \(Q^\vee\) likewise uses this curve's particular cubic ruling.
These distinctions provide a concrete test for which parts of the
unified construction survive variation of the center.
