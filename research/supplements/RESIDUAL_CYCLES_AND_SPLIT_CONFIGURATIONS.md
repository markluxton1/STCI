# Residual cycles, split cases, and Type A configurations

Consolidated mathematical source material with calculations and qualifications preserved.

---

## 2026-10-05-residual-cycle-audit


The complete mathematical statement and proof are consolidated in [the focused proof home](../synthesis/quasiprimitive_residual_cycles.md). The hypotheses, divisor/cycle distinction, and independent review scope are retained there; this source block adds no distinct argument.

---

## 2026-10-05-residual-cycle


The complete mathematical statement and proof are consolidated in [the focused proof home](../synthesis/quasiprimitive_residual_cycles.md). The hypotheses, divisor/cycle distinction, and independent review scope are retained there; this source block adds no distinct argument.

---

## 2026-10-05-split-sextic

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
Run with `python3` in the present checkout.

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


---

## 2026-10-05-split4-nonramified

# Split sextics with nonramified quadruple residual roots

Work in characteristic zero on the monomial quartic C0, with the reduced,
content-free, no-vertical hypotheses of P-020 and the residual-root reduction
of P-030.  This note supplies complete first-normal parameter charts for the
nonramified [4] locus, excludes one allocation, and fixes the selected-root
surface singularity in the surviving charts.  It does not exclude every
surviving carrier or produce an STCI mate.

Use the balanced frame ξ=b−3za/2, η=a, so the quadric direction is
ξ+zη/2.  Write the low and high factors as pξ+rη and uξ+vη.
Their evaluations on that direction are

    A_low=r−zp/2,       B_high=v−zu/2.

The C0 automorphisms z↦cz and z↦1/z allow a nonramified ruling root to be
normalized to a1/a0=1.  Its three preimages are 1,ω,ω², where ω³=1 and
ω≠1.  The residual evaluation is then (z³−1)^4.  Independent rescaling
of the two factors normalizes A_low to the monic expressions below.

## Exact charts and a new vertical-content exclusion

For d=0 the unique selected preimage can be taken to be 1.  Then

    A_low=z−1,  p=−2,  r=−1,
    B_high=(z−1)^3(z²+z+1)^4,
    v=B_high+zu/2,

with u of degree at most ten.  The eleven image equations and the degree
bound on v are equivalent to

    u1=u2+2,  u4=u5−6,  u7=u8+6,  u10=−2.

The seven coefficients u0,u2,u3,u5,u6,u8,u9 are free.  Put

    U0=u0+u3+u6+u9,   U2=u2+u5+u8.

The high factor is content-free exactly when

    (U0+2U2)(U0−U2) ≠ 0.

There is no content at infinity because u10=−2.

For d=1, first suppose both selected evaluation zeros are the same preimage.
After normalization they are at 1, and the complete chart is

    A_low=(z−1)^2,
    p=P−2z,  r=1+(P/2−2)z,
    B_high=(z−1)^2(z²+z+1)^4,
    v=B_high+zu/2,
    u0=2u1−u2+8−3P,
    u3=2u4−u5+6P−18,
    u6=2u7−u8+12−3P,
    u9=−2.

The six coefficients u1,u2,u4,u5,u7,u8 are free.  Put

    S1=u1+u4+u7,    S2=u2+u5+u8.

The precise content-free conditions are

    P≠2,       S1(S1−S2)≠0.

The first condition is the low-factor resultant; the second follows by
reducing u modulo z³−1:

    u ≡ (2S1−S2)+S1z+S2z².

At z=1 its value is 3S1, while at either other cubic root its value is
(S1−S2)(2+z).  In particular the chart is nonempty: P=0,u1=1 and all
other free coefficients zero gives a content-free normal form.

The other possible allocation puts the two selected zeros at distinct
preimages.  Normalize them to ω,ω².  Then

    A_low=z²+z+1,
    p=P−2z,  r=1+(P/2+1)z,
    B_high=(z−1)^4(z²+z+1)^3,
    u0=−u1−u2+2,
    u3=−u4−u5−6,
    u6=−u7−u8+6,
    u9=−2.

These equations force u(1)=0.  Since B_high(1)=0 as well, v(1)=0.
Thus the high coefficient pair has a common factor z−1 at the unselected
third preimage.  It has forbidden vertical content.  **Every d=1,[4]
survivor with a nonramified ruling root therefore has a double selected
preimage.**  Together with P-041's totally ramified exclusion, this gives
one explicit finite parameter family for the entire remaining d=1,[4]
locus on C0.

The equation matrices have fixed nonzero four-by-four minors.  In each d=1
chart the minor with rows 3,6,9,11 and columns u0,u3,u6,u9 has determinant
16.  There is no hidden rank boundary requiring separate treatment.

## Proved: the selected point is always an ordinary A3

For either surviving nonramified [4] chart put

    T=A−2B+D,      F=T²+qK.

This expression exists by P-041.  On the affine quadric write
X=x2, z=x1, x3=zX.  Here the C0 equation is h=X−z³, and

    T|Q=h(X−1)²,     K|Q=h J(X,z),

where J has degree at most three in X and at most one in z.  This follows
from the bidegree (3,1) of K/h on Q.  Consequently J is determined by its
restriction J(z³,z), since the eight monomials X^i z^j, 0≤i≤3,0≤j≤1,
have distinct restrictions z^(3i+j).

In the blowup chart a=e,b=e(z+n), one has q=en and X=z³+e.  The first
strict transform of T is

    T/e=(z³−1)(z³−1−2z²n)      modulo e.

Thus the factor parameterization determines J by

    J(z³,z)=A_low*u+p*B_high
                 −2(z³−1)²[−2z²(z³−1)].

Exact substitution gives the derivative at fixed X:

    d=0:  J_z(1,1)=U0−U2,
    d=1:  J_z(1,1)=−3(S1−S2).

Both are nonzero under the content-free conditions above.  Now set
v_local=X−1.  The strict-transform surface equation can be written exactly

    f=v_local^4+nY,

where Y|n=0=J(X,z)+terms divisible by v_local².  At the selected point
(n,v_local,z−1)=(0,0,0), the derivative of Y in z while X is fixed is
J_z(1,1)≠0.  Hence (n,Y,v_local) are formal local coordinates.  The
surface germ is the ordinary A3 equation nY+v_local^4=0.  This argument
works for every carrier lift F and every value of its q³ kernel parameter.

The low branch has valuation one on n in d=0 and valuation two in d=1.
Thus its local A3 class is respectively 1 or 2 up to reversing the chain.
The contribution to its numerical-pullback self-intersection is
α(4−α)/4: 3/4 for d=0 and 1 for d=1.  These are universal selected-point
corrections.

In d=0 the other branch meets the opposite end of the A3 chain, and their
local Mumford intersection is exactly 1/4.  In d=1 both branches meet the
middle component.  Their local Mumford intersection is 1 plus the ordinary
intersection of their strict transforms on the resolution.  It equals 1
when the selected collision has its minimal multiplicity two.  The
exceptional higher-collision locus is

    3S1=81(P−2).

Do not replace the unconditional self-intersection correction with the
generic branch-intersection value on this exceptional locus.

## An additional [2,2] chart for continuation

For the locus with one selected preimage over each residual ruling, scale
the first selected preimage to z=1 and write the second as z=t.  Then
t³≠1; t=0 includes one totally ramified ruling.  Coordinate reversal
handles a selected point at infinity.  The two-totally-ramified boundary
is the separate family in 2026-10-05-split-sextic.md.

Set

    residual=((z³−1)(z³−t³))²,
    A_low=(z−1)(z−t),
    p=P−2z,  r=t+(P/2−1−t)z,
    B_high=residual/A_low,  v=B_high+zu/2.

The complete first-normal image equations in this chart are

    u0=(t+1)u1−t u2+C0,
    u3=(t+1)u4−t u5+C3,
    u6=(t+1)u7−t u8+C6,
    u9=−2,

where

    C0=t³[−P(t²+t+1)+2(t³+t²+t+1)],
    C3=P(1+t+...+t⁵)−2(1+t+...+t⁶)−4t³,
    C6=−P(t²+t+1)+4t³+2t²+2t+4.

The six other u coefficients are free.  The low factor is content-free
exactly when (P−2)(P−2t)≠0; the high factor is content-free exactly when
gcd(u,(z³−1)(z³−t³))=1.  The same fixed minor has determinant 16, including
t=0.  This is a chart statement; it does not silently classify allocations
whose low evaluation has two zeros over only one of the two residual
rulings.  Such allocation questions must be checked against full Cartier
clusters rather than inferred from visible reduced roots alone.

## Verification and continuation boundary

Run research/computations/verify_split4_nonramified.py with the existing
python3.  It verifies all displayed affine
image equations, proves the fixed rank minors, checks the content and
selected-point derivative formulas, and independently reconstructs the
rank-22 ambient normal map.  It checks a symbolic ambient lift with all
six high coefficients and P still free.  Its lift_normal function supplies
an ambient carrier for any target in the normal image; P-022 supplies the
full lift fiber F0+λq³.

The surviving d=0 and d=1-double families still have nine and eight units,
respectively, of unselected collision multiplicity available.  An STCI
mate would have to satisfy the global Mumford intersections 19/4 and 17/5,
the relevant Cartier multiple with its positive scale, and full conductor
descent.  The universal A3 correction is a usable constraint for the
normal-sheaf/Jacobian-divisor route, but it does not itself close that route.


---
