# Split sextics: exact ambient lift of the missed ramified boundary

## Scope and starting point

Work over an algebraically closed field of characteristic zero, on the smooth
monomial rational quartic

\[
 C_0=[s^4:s^3t:st^3:t^4],\quad
 q=x_0x_3-x_1x_2,\quad
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad D=x_2^3-x_1x_3^2.
\]

Retain P-020's reduced, content-free split exceptional divisor and no vertical
component hypotheses.  For type \(d=1\), an STCI mate of any degree would
have orders/degree \(k(11,1,8)\), with \(k>0\), and necessarily

\[
 \Gamma_{\rm low}\Gamma_{\rm high}=17/5,
 \qquad \Gamma_{\rm low}^2=13/5
\]

for Mumford numerical pullbacks on the normalization.  No cancellation of
\(k\) in a local class group is used below.

## Proved: the fixed P-041 boundary normal form has no STCI carrier

The content-free first-normal survivor in
`verify_split22_boundary_survivor.py` is

\[
 \ell=\xi+\tfrac32z\eta,\qquad
 m=(1-3z^4+z^8)\xi+
       (z/2-z^5/2+z^9/2)\eta.
\]

Here \(z=x_1/x_0\), \(a=x_2-z^3\), \(b=x_3-z^4\),
\(\eta=a\), and \(\xi=b-\tfrac32za\).  The factors in the affine
\((a,b)\)-frame therefore are

\[
 b,\qquad (1-3z^4+z^8)b-z(1-4z^4+z^8)a.
\]

Its ambient sextic lifts are exactly

\[
 \boxed{F_\lambda=B^2+q^2(x_0^2-4x_0x_3+3x_3^2)
                   +q(x_1A+x_2D)+\lambda q^3.}
\]

The displayed form has the required quadratic normal form by direct exact
expansion.  P-022's kernel computation
\(H^0(I_{C_0}^{(3)}(6))=kq^3\) proves that these are all lifts; scaling
the whole normal form scales the carrier and changes no geometry.

In the \(a=e,b=ew\) blowup chart, the strict transform is
\(f_\lambda=F_\lambda/e^2\).  At the endpoint \(z=0,e=w=0\), its
quadratic term is

\[
 e^2+w^2-wz.
\]

In the reversed affine chart \(x_3=1\), put
\(x_2=z,x_1=z^3+e,x_0=z^4+ew\).  The quadratic term at the other
endpoint is

\[
 e^2+3w^2-7wz+4z^2.
\]

Both Hessian determinants are \(-2\), independently of \(\lambda\).
Thus both endpoint germs are ordinary \(A_1\) surface singularities.
The two branch curves have distinct tangent directions on each tangent
quadric.  Resolving the node separates their strict transforms and introduces
one \((-2)\)-curve meeting each once, so their local Mumford intersection
is \(1/2\).

The other eight branch collisions have \(w=e=0\) and

\[
 z^8-4z^4+1=0.
\]

These roots are simple.  The derivative in the exceptional normal direction
at such a collision is

\[
 \left.\frac{\partial f_\lambda}{\partial e}\right|_{e=w=0}
       =-z^3(\lambda+6z^4-4).
\]

The surface is smooth unless \(\lambda=4-6z^4\).  Its two branch curves
then intersect transversely in the smooth surface, contributing one.  When
that derivative vanishes, compute the full three-variable Hessian **before**
substituting the value of \(\lambda\).  Modulo the collision polynomial its
determinant is

\[
 1536(23-86z^4).
\]

It never vanishes: if \(r=z^4\), then \(r^2-4r+1=0\), and
\(\operatorname{Res}_r(r^2-4r+1,23-86r)=13\ne0\).
Consequently these singular germs also are \(A_1\), with local branch
intersection \(1/2\).  For each of the two exceptional values
\(\lambda=-8\pm6\sqrt3\), exactly four interior collisions are nodes;
the other four are smooth.  For every other \(\lambda\), all eight are
smooth.  No further branch intersection occurs, because the two exceptional
sections have intersection divisor of total degree ten.

The strict transform is normal in a neighborhood of the exceptional curves:
it is smooth away from these isolated nodes.  Its normalization therefore
does not change this calculation.  The resulting **global** Mumford branch
intersections are

\[
 8+2(1/2)=9\quad\hbox{or}\quad4+6(1/2)=7.
\]

Neither equals \(17/5\).  Hence no integral sextic with this particular
quadratic normal form can have an STCI mate, of any degree or scale.  This is
a higher-jet exclusion of the fixed first-normal survivor, not an exclusion
of every ramified-root \([2,2]\) carrier.

**Exact certificate:**
`research/computations/verify_split22_boundary_lift.py`.
Run with `/private/tmp/stci-cas-venv/bin/python` in the present checkout.

## Exact parameterization of the larger two-ramified-root boundary

The fixed survivor sits in a larger family.  If the low branch has its two
quadric-direction zeros at the totally ramified rulings, normalize its
coefficients and the high evaluation as

\[
 \ell=\xi+hz\eta,\qquad
 m=u(z)\xi+\bigl(zu(z)/2+z^5\bigr)\eta.
\]

The eleven P-022 image equations reduce exactly to

\[
 u_1=u_7=0,\qquad (2h-1)u_4+4h=0,
\]

with free \(u_0,u_2,u_3,u_5,u_6,u_8\).  Content-freeness at the endpoints
requires \(u_0u_8\ne0\); the low factor and its evaluation require
\(h\ne0,1/2\).  Since the high evaluation is nonzero at every other base
point, these conditions also ensure high content-freeness.

Put \(a_h=h-1/2\).  An exact lift is

\[
 F=a_hB^2+q^2S_2+a_hqK_3+\lambda q^3,
\]

where

\[
\begin{aligned}
 S_2={}&u_0x_0^2+u_3x_0x_2
       -\frac{(2h+1)^2}{2(2h-1)}x_0x_3+u_2x_1^2\\
      &+\frac{2h+1}{2}(u_5x_1x_3+u_6x_2^2)+2hu_8x_3^2,\\
 K_3={}&u_0x_1A+u_2x_2A+u_3x_3A
                     +u_5x_2B+u_6x_3B+u_8x_2D.
\end{aligned}
\]

The low branch in the finite blowup chart is
\(e=0,w=(3/2-h)z\).  Its endpoint quadratic term is

\[
 u_0(w+(h-3/2)z)(w-z)+a_hu_2e(w-z)+a_he^2.
\]

Its Hessian determinant is
\(-u_0^2(2h-1)^3/4\ne0\).  The reversed endpoint determinant has the
same expression with \(u_8\).  Thus the two selected residual-root points
are always nodes throughout this larger boundary family.  The interior
collision polynomial is

\[
 R(z)=a_hu_0+a_hu_2z^2+a_hu_3z^3-(2h+1)z^4
                     +a_hu_5z^5+a_hu_6z^6+a_hu_8z^8.
\]

Let \(g\) be the derivative \(\partial f/\partial e\) along the low
branch.  Exact expansion gives

\[
\begin{aligned}
 g(z)={}&-a_h^2u_2z+a_h^3u_3z^2
 +\frac{a_h}{8}(8h^3-4h^2+6h+5-8a_h^2\lambda)z^3\\
 &-\frac{a_h^2}{4}(4h^2+3)u_5z^4
 +\frac{a_h^3}{2}(2h+3)u_6z^5
 -\frac{a_h^2}{4}(12h^2-4h+3)u_8z^7.
\end{aligned}
\]

This is concrete higher-jet data for the continuation.  An interior collision
is singular exactly when it is a zero of \(g\).  A mate would have to
produce enough nonordinary singularity correction to lower the total
intersection from ten to \(17/5\); the fixed survivor fails this test.

## Failed shortcut and possible normal-sheaf reduction

The smooth curve \(\Gamma_{\rm low}\) has the normal sequence in the ambient
blowup

\[
 0\longrightarrow O_{\mathbf P^1}(2)
 \longrightarrow N_{\Gamma/B}
 \longrightarrow O_{\mathbf P^1}(6)\longrightarrow0.
\]

It is incorrect to treat this as a chosen split sum.  The affine function
\(g\) above has degree seven: its change of local trivialization can mix with
the collision derivative, because the normal extension need not split.
Thus a proposed uniform bound on the Jacobian common divisor by six is
**withdrawn**.

One potentially useful reduction is the inequality
\(\Gamma^\#{}^2\le\deg N_{\Gamma/D}^{\rm tf}\), which still needs an
independent proof in the required normal-hypersurface scope.  The Jacobian
map \(N_{\Gamma/B}\to O(12)\), if its zero divisor has length \(\delta\),
would give \(\deg N_{\Gamma/D}^{\rm tf}=\delta-4\).  The mate's
\(\Gamma^\#{}^2=13/5\) would then force \(\delta\ge7\).  Together with
the displayed \(R,g\), this suggests finite common-factor equations.  It is
an open route here, not a theorem currently used in the fixed-survivor proof.
