# Nonendpoint quintics: residual factor loci, curve maps, and eight excess contacts

Date: 2026-10-12. Author: `nonendpoint_pole_spaces`.

Status: **DIRECT NEW STRUCTURAL REDUCTIONS; INDEPENDENT PROOF AUDIT
OUTSTANDING**. This note excludes a residual degree partition and gives
necessary finite parameter and contact reductions in the remaining
nonendpoint genus-one quintic projection family. It does not exclude the
entire family or any other quintic normalization lane. No CAS execution is
claimed here; all identities used below follow from the saved exact model.

The field is algebraically closed of characteristic zero. Use the
[intrinsic A4 pair](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md),
the [exact low-pole spaces](2026-10-11-session-a4-low-pole-spaces.md), and the
[actual nonendpoint sections and residual divisor](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md).
The two double roots are 0,delta, where delta is arbitrary and nonzero.
It is not normalized to one. The four lift parameters are a,b,g,d.

Throughout, an admissible projection means a line center avoiding S and
the resulting finite birational normalization map `nu:S->X` onto an integral
quintic. Every mate forces the full inverse-support condition

    (nu^(-1)(C0))_red=c.                     (SUP)

The restriction `nu|c:c->C0` is an isomorphism, including the A4 point p of c,
which maps to the nonendpoint target parameter z=1. Consequently (SUP)
permits only p as a normalization point above that target point.

## 1. Reducibility has only two parameter hyperplanes

Put `t=T-r^2`, `v=t^2-r^3`, and define coefficients

    A=a+d-b-g, B=ad-bg,
    J=(4a-3b-g)delta-3delta^3-A,
    E=B+delta^4,
    P2=B+(6a-3b)delta^2+3delta^3,
    L=(-4a+b)delta^3-delta^4, N=a delta^4.

The residual D is the actual Weil divisor `div(F)+6ell`, where

    F=A t^2+(J r+E)t+(-3delta^2-A)r^3+P2 r^2+L r+N.          (1)

It excludes ell. Its only possible prime-degree partitions, including
multiplicities, are 6,2+4,3+3,2+2+2.

If `A!=0,-3delta^2`, the discriminant of (1), viewed as a quadratic in t,
is the cubic

    Delta(r)=(J r+E)^2
      -4A[(-3delta^2-A)r^3+P2 r^2+L r+N],                 (2)

with nonzero leading coefficient `4A(A+3delta^2)`. A nonzero polynomial of
odd degree is not a square in k(r): its valuation at infinity is odd.
The quadratic is therefore irreducible over k(r), and is primitive over
k[r] because its t^2 coefficient is a nonzero constant. Thus F is
irreducible in k[r,t] and D is integral and reduced.

On `A=0`, write

    F=(J r+E)t+P(r),
    P(r)=-3delta^2 r^3+P2 r^2+L r+N.                      (3)

If J is nonzero, the sole reducibility condition is

    rho=-E/J, P(rho)=0.                                  (4)

Then F factors into a degree-two prime `r-rho` and a degree-four prime
whose t coefficient is J. The latter is integral, since it is a graph
over r. If J=0 and E!=0, F is an irreducible graph. If J=E=0, F is a
cubic polynomial in r and the partition is 2+2+2, with repetitions allowed.

On `A=-3delta^2`, the r^3 coefficient vanishes. Reducibility occurs precisely
when the degree-at-most-two discriminant (2) is a square in k[r], including
the zero square. The resulting factors have degree three, and coincide
when the discriminant is zero. If the discriminant is not square, D is
integral. These two exceptional hyperplanes are retained in full; they are
not covered by the genus-one argument below.

## 2. Cycle pushforward, including conductor components

On the target smooth quadric Q, the quintic equation cuts C0 plus a residual
divisor R of class (4,2): C0 has class (1,3), while the quintic restriction
has class (5,5). Therefore

    nu_*D=R, class(R)=(4,2).                              (5)

This equality counts both component multiplicities and possible degrees
greater than one of the maps of curve components. It remains valid when
the generic point of a component belongs to the conductor. Indeed at a
codimension-one point of X, let the finite birational inclusion of local
one-dimensional rings be A0 subset B0, and M=B0/A0. For a nonzero local
equation q, M has finite length and multiplication by q has equal kernel
and cokernel lengths. The exact sequence with multiplication by q then
shows `length(A0/qA0)=length(B0/qB0)`, with residue-field degrees included
when B0 is semilocal. This proves the cycle equality without assuming
normality along the target residual.

## 3. No degree-two or degree-three prime can collapse to a ruling line

A degree-two prime on S is the closure of `r=rho`. Its normalization is P1,
and its support on c consists exactly of p and the finite point `T=0,r=rho`.
This follows directly from its anticanonical parametrization: as t tends to
infinity, Z0=t^2-rho^3 dominates and the limit is the A4 point p.

Its degree-two polarization permits image degree two with mapping degree
one, or image degree one with mapping degree two. In the latter case its
image line contains both target points C0(1) and C0(zrho), where

    zrho=(rho-delta)/rho

and zrho is interpreted as infinity when rho=0. These two points are
distinct for delta!=0. A ruling line through both of them must be the
trisecant ruling, and meets C0 in three distinct points. Explicitly, its
fixed Segre coordinate is z^3=1, so the points are the three cube roots of
unity. A surjective curve map to that line must have preimages of all
three points, whereas (SUP) allows only the two points of this prime on c.
This is impossible. Thus every degree-two prime in D satisfying (SUP)
maps birationally to a smooth plane conic of class (1,1) on Q.

A degree-three prime has affine equation `t+B1 r+C1=0`, and its
normalization is P1. Its anticanonical parametrization is the complete
cubic system on that P1: the coordinate functions span 1,r,r^2,r^3.
Its support on c has at most three points, namely p and the roots of
`-r^2+B1 r+C1`. At least one of those roots is finite. Its image can have
degree three birationally, or degree one with mapping degree three.

If the image is the ruling line meeting C0 only once, that point is C0(1),
but the finite point of the prime on c maps to a distinct target point,
which is impossible. If it is the trisecant ruling, (SUP) requires each of
its three distinct C0 points to have a singleton fiber in the normalization
of the prime. A degree-three map P1->P1 would then be totally ramified at
three different source points. These contribute at least six to the
ramification divisor, whereas Riemann-Hurwitz gives degree four. This is
again impossible. Thus a degree-three component must map birationally to
a smooth cubic of class (2,1) or (1,2) on Q.

These arguments include repeated components of D: repetition changes the
cycle multiplicity, not the map or its point fibers.

## 4. A complete partition exclusion and a five-value conic reduction

The partition 2+2+2 is impossible under (SUP). By section 3 all its components
push forward as plane conics, with repetitions counted. Their total class
would be (3,3), contradicting (5).

In the partition 2+4, the conic has class (1,1). The remaining pushforward
must consequently have class (3,1). The degree-four prime cannot map four
times to a line: its graph equation has a nonzero r^2 and a nonzero t
coefficient, and its anticanonical coordinate functions consequently span
1,r,r^2,r^3,r^4. Its intrinsic coordinate span has dimension five, and
restriction of the four-dimensional projection system has dimension at
least three (its kernel is at most the two-dimensional kernel of the
projection system in the full six-dimensional anticanonical space).
Nor can it map twice to a conic, whose pushforward class would be (2,2).
Thus the quartic maps birationally to the smooth rational Q-curve (3,1).

There is a small exact parameter restriction on the conic `r=rho`.
Its image is a smooth plane conic. Its intersection with C0 is therefore
the plane section of C0, a binary quartic supported, by (SUP), only at
z=1 and z=zrho. A plane equation restricted to

    C0(z)=[1:z:z^3:z^4]

has no z^2 coefficient. For finite zrho different from 1, a binary quartic
with the stated support is, up to scalar,

    (z-1)^m(z-zrho)^(4-m), m=1,2,3.

Its z^2 coefficients are respectively

    3 zrho(zrho+1), zrho^2+4 zrho+1, 3(zrho+1).

For zrho=infinity the polynomial has degree m, and its z^2 coefficient
vanishes only for m=1. These cases give precisely the necessary values

    rho/delta in {0,1,1/2,(3-sqrt(3))/6,(3+sqrt(3))/6},        (6)

or equivalently

    rho(rho-delta)(2rho-delta)
       (6rho^2-6delta rho+delta^2)=0.                         (7)

In particular the reducible A=0 locus, if it could have a mate, must satisfy
J!=0, the two conditions (4), and the finite restriction (7). This preserves
the arbitrary nonzero modulus delta and all four lift parameters; it does
not assert that any of these five possibilities succeeds.

In the partition 3+3, section 3 and (5) force both cubics to have class
(2,1). This includes the case of a doubled cubic. The corresponding conic
and cubic contact arguments do not yet exclude 2+4 or 3+3 in their entirety.

### 4a. The conic-plus-quartic locus reduces to eight one-parameter families

The plane condition also gives one linear relation in the lift parameters.
If `H(z)=h0+h1 z+h2 z^3+h3 z^4` is the required plane quartic, the conic
parametrization is

    X(T)=T^2(1,1,1,1)+T(L0,L1,L2,L3)+C0(zrho),

up to the scalar r^4 in the last term, with its homogeneous meaning at
rho=0. The coefficient vector in T is

    (a,b,g,d)+(-2rho^2-rho)(1,1,1,1)
                +delta rho(0,1,3,4).

Because H(1)=0, the plane contains this conic precisely when

    h0 a+h1 b+h2 g+h3 d+delta rho H'(1)=0.                 (8a)

Use coordinates on the hyperplane A=0 given by

    u=a-b, w=a-g,
    b=a-u, g=a-w, d=a-u-w, B=-uw.

Write `rho=tau delta`. The two literal factor conditions in (4) are
equivalent to

    uw=tau(3u+w)delta^2+(1-3tau)delta^4,                 (8b)

    0=a(3tau^2-3tau+1)
      +u(-3tau^3+3tau^2-tau)-w tau^3
      +delta(-3tau^3+3tau^2-tau)
      +delta^2 tau^2(3tau-1).                           (8c)

The second equality is P(rho)=0 after using the first, and dividing by
delta^4; delta is nonzero throughout. No lift variable is divided out.

For tau=0, the allowed plane polynomial is z-1. Equation (8a) says b=a,
whereas the constant factor condition gives a=0. Then b=0 and the other
factor condition would require `B+delta^4=delta^4=0`, impossible.
For tau=1, the allowed polynomial is z^4-z^3. Its plane equation gives
`b=a-delta^2`. Hence `u=delta^2`, `B=delta^2(g-a)`, and
`J=(a-g)delta`. The factor condition `J delta+E=0` again reads
`delta^4=0`. Thus neither tau=0 nor tau=1 survives.

For tau=1/2, there are exactly two allowed contact patterns. They produce
the following necessary families, with delta arbitrary and nonzero:

* Contact multiplicities (1,3) at (1,-1): set `u=x delta^2`, where
  `2x^2-2x-1=0`; set `w=(u+4delta^2)/3`; then
  `a=(u+w+delta-delta^2)/2`.
* Contact multiplicities (3,1) at (1,-1): set `u=x delta^2`, where
  `6x^2-6x+1=0`; set `w=3u`; then
  `a=(u+w+delta-delta^2)/2`.

Indeed the two plane polynomials are respectively
`z^4+2z^3-2z-1` and `z^4-2z^3+2z-1`; (8a) gives
`3w=u+4delta^2` and `w=3u`. Substitution in (8b)--(8c) gives exactly
the displayed quadratics and a expressions.

For either root tau of `6tau^2-6tau+1=0`, the contact pattern is (2,2).
Write `zrho=1-1/tau`. Its plane polynomial is
`(z-1)^2(z-zrho)^2`. Reducing its coefficients by
`zrho^2+4zrho+1=0`, (8a) gives `w=3u`. Equations (8b)--(8c) then give

    u=x delta^2,
    3x^2-6tau x-1+3tau=0,
    w=3u,
    a=(6tau-1)u+tau delta-(3tau-2/3)delta^2.               (8d)

The quadratic in x has nonzero discriminant six. There are two choices
of x for each of the two choices of tau. Finally recover b,g,d from the
displayed u,w formulas. Thus the entire 2+4 locus compatible with the
conic's full target support lies in eight explicit one-parameter families:
two of the first type, two of the second, and four of type (8d).

These families are only necessary. Center avoidance, the quartic component's
ten target contacts, and full conductor descent remain to be tested. No
family is declared admissible or successful. The parameters in (8a)--(8d)
are direct equations from the actual model, not a broad resultant run.

## 5. Off the two factor hyperplanes, the integral residual has genus one

Assume now `A!=0,-3delta^2`. Complete the square in (1) by putting

    y=2A t+J r+E.

The affine residual is `y^2=Delta(r)`, where Delta is a cubic with nonzero
leading coefficient. Its plane cubic compactification has one smooth
point p_infinity. It is integral of arithmetic genus one even when Delta
has a repeated root; its geometric genus can then be zero. At p_infinity
r has pole two and t has pole three. The leading relation is

    t^2 ~ kappa r^3, kappa=(A+3delta^2)/A,

where kappa and kappa-1 are nonzero. Hence v has pole six.

The six anticanonical coordinate functions on this cubic are

    [Z0:Z1:Z2:Z3:Z4:Z5]=[v:rt:t:r^2:r:1].                  (8)

They extend using the frame O(6 p_infinity), with Z0 nonzero at infinity;
there is no base point. The resulting morphism is the already defined
map to S on the affine chart. Near infinity, in the Z0=1 chart, its local
coordinates are

    a0=rt/v, b0=t/v, c0=r^2/v.

Their vanishing orders are 1,3,2. In particular a0 is a uniformizer with
nonzero leading coefficient. The finite birational curve map is therefore
an isomorphism near infinity: the completed image ring contains k[[a0]],
which equals the completed source DVR. It is also an isomorphism on the
affine chart. Thus the actual integral Weil curve D is this plane cubic
compactification, has arithmetic genus one, and is smooth at the A4 point p.
No assumption of nonsingularity at its affine points is made.

## 6. A degree-two map of this integral residual contradicts full support

If this integral D maps to its reduced image R0 with generic degree e, (5)
forces `e[R0]=(4,2)`. Thus e is one or two. If e=2, R0 has class (2,1),
is an integral curve of arithmetic genus zero, and is therefore smooth.

At p, the tangent of D is the a0 direction. The same is true for c: the
local equations of c in the A4 chart are

    b0+c0=0, (1-a0)c0-a0^2=0.                             (9)

Since nu|c is an isomorphism onto the smooth C0, the target derivative of
the a0 direction is nonzero. The map D->R0 is consequently unramified at p.
A degree-two finite map to a smooth curve then has another point in the
fiber of nu(p). One may justify the degree count by torsion-freeness over
the target DVR, which makes the finite map flat, or by its normalization.
But (SUP) and the isomorphism c->C0 permit only p in this fiber. This is a
contradiction. Therefore

    D -> R is finite birational,
    class(R)=(4,2), pa(R)=3, pa(D)=1.                      (10)

The curve-model quotient `nu_*O_D/O_R` has total length two. That number is
not an upper bound on subsequent contact lengths.

## 7. Exactly eight excess contact lengths are required on this locus

The intrinsic ideal of c restricted to D is locally principal. At finite
points of c the surface is smooth and the ideal is generated by T.
The finite part of its zero scheme has length four because substitution
`t=-r^2` into (1) gives

    F|c=A r^4+(-3delta^2-A-J)r^3+(P2-E)r^2+L r+N,

whose leading coefficient A is nonzero. All repeated roots are counted.

At p use (9). The ratios computed from (8) satisfy

    c0/a0^2 = v/t^2 -> 3delta^2/(A+3delta^2),
    b0/a0^2 -> 0.

The limiting c0 coefficient is nonzero and differs from one. Each generator
in (9) thus has order exactly two on the smooth D at p, so their image
ideal is `(a0^2)`. The intrinsic ideal zero scheme consequently has total
length `4+2=6` on D.

The target intersection C0.R has length fourteen by (10). Its Cartier
equation on the smooth Q pulls back to a nonzerodivisor phi on D. The total
zero length of phi is also fourteen: the finite-length quotient in (10)
has equal multiplication-kernel and multiplication-cokernel lengths,
exactly as in section 2. By (SUP), these zeros all occur on c.

Locally write the intrinsic ideal on D as `(tau)`. The target equation
vanishes on c scheme-theoretically after pullback, so `phi=tau*w` with w
regular. The nonnegative local excess is `length(O_D/(w))`. Additivity for
products of nonzerodivisors, including at singular affine points of D,
gives the exact necessary condition

    sum local excess lengths = 14-6 = 8.                 (11)

This is a full contact requirement. It does not bound these excesses by
the degree or number of first-normal roots, by the two curve-model quotient
lengths, or by a generic differential calculation. The factor hyperplanes
A=0 and A=-3delta^2 are outside (10)--(11), and all higher-jet exceptional
strata on the present locus remain open.

## 8. Continuation boundary

The new completed deductions, subject to independent audit, are the factor
hyperplane reduction, the exclusion of the complete 2+2+2 partition, the
five-value necessary conic parameter restriction in 2+4, the map-degree
restrictions for 2+4 and 3+3, and the exact eight-excess requirement for the
integral residual off the two hyperplanes. The next work is to compare (11)
with the actual finite conormal cancellation loci, and to analyze the five
conic cases and the cubic-pair discriminant locus with full target fibers.
Neither the nonendpoint family nor the unrestricted STCI question is
resolved by these statements.
