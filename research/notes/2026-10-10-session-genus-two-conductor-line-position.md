# Genus-two conductor line: complete positions on the fixed rational quartic

Date: 2026-10-10. Author: `oct10_line_position_mate`.
Status: **PROVED HERE explicit curve geometry; conditional application to
the proposed blowup lift; independent audit requested**.
No canonical frontier file is edited. No mate exclusion is asserted by
this note alone. No claim of novelty is made.

Work over an algebraically closed field of characteristic zero, with

    C0=[s^4:s^3t:st^3:t^4],
    q=x0*x3-x1*x2.

The accepted [entire-conductor audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md)
gives the actual reduced conductor line `Gamma`. The accepted
[mate-stratum audit](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md)
gives `f.c#=2` for lambda zero and `f.c#=1` for lambda one. The
identification of `f` with the plane-through-line pencil is supplied by
the [proposed blowup proof](2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md),
and remains conditional here until that separate proof is accepted.

## 1. Actual intersection length, including nonreduced intersections

Assume the proposed lift proof. For independent actual equations
`t0,t1` of `Gamma`, that proof gives

    t_i=g*s_i,
    div(g)=D_M ~ -K_M,

where `s0,s1` are a basis of the complete basepoint-free adjoint pencil
`|f|`. Since `c# -> C0` is an isomorphism under the mate hypothesis,
the restrictions `t_i|c#` are the literal ambient line forms in
`O_P1(4)`. Their common-zero divisor is precisely the scheme-theoretic
intersection `C0 intersect Gamma`. The restrictions of `s_i` have no
common zero. Consequently

    tau := length(C0 intersect Gamma) = D_M.c# = 4-f.c#.

Thus the two accepted mate strata become exactly

    lambda=0: tau=2,          lambda=1: tau=3.

This identity counts orders in the local ring of the smooth curve.
It does not require transverse intersections, smoothness of S at a
contact point, or reducedness of the upstairs conductor.

## 2. The unique quadric and all trisecants

The ten degree-two coordinate monomials restrict to the nine binary
monomials of degree eight. Their only repeated exponent is that of
`x0*x3` and `x1*x2`. Hence `q` spans all quadrics containing `C0`.
It is smooth, with Segre coordinates

    [x0:x1:x2:x3]=[u0*v0:u0*v1:u1*v0:u1*v1],
    [u0:u1]=[s^3:t^3],        [v0:v1]=[s:t].

The equation of C0 on this quadric is `u0*v1^3-u1*v0^3=0`, so its
bidegree is `(1,3)` in this convention. A ruling with fixed `u` meets
the curve in length three; a ruling with fixed `v` meets it in length
one.

If any line has intersection length at least three with C0, then its
restriction of `q` has at least three zeros counted with multiplicity.
A nonzero section of `O_line(2)` cannot do so. The line must lie on
the quadric, hence it is one of the length-three rulings. In particular
no line meets C0 in length four or more.

The complete trisecant family is

    Gamma_kappa: x2-kappa*x0=x3-kappa*x1=0,    kappa in k,
    Gamma_infinity: x0=x1=0.

For finite kappa the two restricted forms are

    s*(t^3-kappa*s^3),        t*(t^3-kappa*s^3).

Their common divisor has degree three, and their quotient gives
the identity map `[s:t]`. For nonzero finite kappa the three roots of
`t^3-kappa*s^3` are distinct. For kappa zero the intersection is the
length-three fat point at `[s:t]=[1:0]`; for infinity it is the
length-three fat point at `[0:1]`. These two lines are the tangent
lines of contact order three at the two endpoints. There is no
trisecant with partition `[2,1]` for this fixed curve.

Consequently the lambda-one conductor must be a literal member of this
ruling, including these two endpoint boundaries. Its adjoint ruling
restricts to an isomorphism on C0.

## 3. Every length-two position

A length-two intersection of a line with a smooth curve consists of
two distinct points or a double point. The corresponding line is the
secant or the unique tangent line. The preceding ruling computation
shows that no line contained in q has intersection length two.

In the affine parameter r=t/s put

    P(a)=[1:a:a^3:a^4].

For distinct finite a,b, the secant is contained in q exactly when

    a^2+a*b+b^2=0,

equivalently `a^3=b^3`. Indeed

    q(l*P(a)+m*P(b))
       = l*m*(a-b)^2*(a^2+a*b+b^2).

Thus all finite ordinary bisecants have `a != b` and
`a^2+a*b+b^2 != 0`. For the tangent at finite a,

    q(l*P(a)+m*P'(a)) = -3*a^2*m^2.

The tangent has length two exactly when a is nonzero; at zero it is
the endpoint trisecant. The reversed endpoint at infinity is also a
trisecant. Every secant joining infinity to a finite point is an
ordinary bisecant, including the line joining the two endpoints.

For finite a,b (allowing a=b != 0 for tangent positions), use the actual
line forms

    T0=x2-(a^2+a*b+b^2)*x1+a*b*(a+b)*x0,
    T1=x3-(a+b)*(a^2+b^2)*x1+a*b*(a^2+a*b+b^2)*x0.

After dividing the common degree-two factor `(t-a*s)*(t-b*s)`, their
restrictions are

    s*(t+(a+b)*s),
    t^2+(a+b)*s*t+(a^2+a*b+b^2)*s^2.

These two quadrics have no common zero precisely when
`a^2+a*b+b^2 != 0`. They give the actual degree-two map on C0.
For a secant through infinity, the forms

    T0=x1-a*x0,       T1=x2-a^3*x0

have common divisor `s*(t-a*s)` and residual quadrics

    s^2,             t^2+a*s*t+a^2*s^2,

which have no common zero. This records the infinity chart explicitly.
Hence the lambda-zero conductor is exactly an ordinary bisecant or a
tangent at a nonendpoint point, with no missing coordinate boundary.

## 4. A useful unique-anticanonical-section lemma

Under the proposed lift, `g` supplies a nonzero section of `-K_M`.
In fact `h0(M,-K_M)=1`. The basepoint-free pencil sequence for f,
tensored with `-K_M`, is

    0 -> O(-K_M-f) -> O(-K_M)^2 -> O(L) -> 0.

An effective divisor in `-K_M-f` would write `L=2f+T` with T
effective. The three sections `s_T*s0^2`, `s_T*s0*s1`,
`s_T*s1^2` then impose a quadric equation on the actual quartic image,
the already accepted quadratic-product contradiction. Thus
`H0(-K_M-f)=0`. If `h0(-K_M)>=2`, the four products of two independent
anticanonical sections and `s0,s1` are independent and form a basis
of the four-dimensional `H0(L)`. Their Segre determinant is again a
nonzero quadric equation on the quartic image. This contradiction
proves the lemma.

It does **not** prove `h0(-nK_M)=1` for every n. In particular it does
not allow one to replace an effective rational anticanonical cycle by
the unique integral anticanonical divisor. The mate correction Z can
have denominators. That tempting stronger deduction is deliberately
not used.

## 5. A real obstruction to a naive branch-count argument

In the normal strict-transform model, the exceptional divisor of the
ambient blowup is `E=P1_Gamma x P1_f`; its intersection with T has
bidegree `(2,2)`. A horizontal exceptional section B maps to a whole
fiber over a point of Gamma, giving a factor of this divisor.

The accepted lambda-one marked analysis forces the special
degree-zero horizontal prime `B=e0-e_i-e_j` to be present and gives
`c#.B=0`. This does **not** imply that the image c_T avoids B_T.
A vertical ADE chain can join c# to B; after that chain contracts,
c_T and B_T meet at a singular point. Moreover B_T contracts in
`T -> S`. Two distinct residual-conductor points over the same Gamma
point can then become the same point of S. The actual finite-flat
conductor fiber can have singleton support without the residual
degree-two cover being ramified there.

Therefore three distinct C0/Gamma intersections cannot immediately be
declared three branch points of the residual cover. The contacts away
from the images of horizontal sections do give genuine singleton
residual fibers, and this provides a structural route. A separate
worker is checking its irreducible and reducible residual cases, with
the endpoint trisecants kept distinct. No full lambda-one exclusion
has been established by this note.

## 6. Evidence and continuation

The algebra in sections 2--3 is independently executable in
`verify_session_genus_two_line_positions_2026_10_10.m2`. The script
checks homogeneous restriction identities, the secant and tangent
quadric restrictions, and residual-map boundary controls. It is an
exact identity certificate, not a mate search or parameter sampling.

The final source passed **17 exact checks** with Macaulay2, exit zero,
tool chunk `7d156d`, wall time 0.521006917 seconds. The source SHA-256
is `731203f95f4bd7fdde1c8c4511f3db3946f8c9eb1839ef6457e69a7a66d43b17`.
The [execution record](../validation/2026-10-10-genus-two-line-positions/execution-record.json)
also retains the two development failures (protected function name and
list-argument syntax), rather than treating them as missing mathematical
parameter strata. This observed execution is not an isolated replay.

The structural priority is to audit the normal blowup lift, then use
the `(2,2)` entire exceptional divisor to handle all residual support
types. Preserve both endpoint trisecants, all singularities at the
contact points, and all powers of a hypothetical mate. The lambda-zero
bisecant lane and the unrestricted STCI problems remain open.
