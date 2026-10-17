# A uniformly excluded A3+2A1 family containing fixed C0

Date: 2026-10-09. Author: `normal_global_adversarial`.
Status: **PROVED HERE for the displayed family**, characteristic zero.
Every member below is an integral quartic containing fixed C0 with
normalization singularity type A3+2A1, and admits no mate of any degree.
The family does not exhaust every pair or middle-coordinate projection
in this ADE stratum. No canonical frontier file is edited.

## 1. The normal anticanonical model

In P4[a:b:c:d:e], let

    S=V(ab-c^2, cd-e^2).

The two equations form a complete intersection. On c nonzero it is
integral: a,b are nonzero, b=c^2/a and d=e^2/c. The closed set c=0
has also e=0 and ab=0, and has affine-cone dimension two, smaller
than the three-dimensional complete intersection. Thus no component
is contained there. The complete intersection has no embedded
components and is generically reduced, so its ring is a domain.

The Jacobian drops rank exactly at the three coordinate vertices a,b,d.
On the a chart the local equation is cd=e^2, an A1 point; the b chart
is identical. On d=1, eliminate c=e^2 and obtain ab=e^4, an A3 point.
All singularities are isolated, so the complete intersection is normal
by S2 and R1. Its degree is four and its dualizing sheaf is O_S(-1).

## 2. A rational normal quartic and the actual coordinate change

Choose parameters alpha,beta,gamma,delta with

    gamma delta Delta nonzero,       Delta=alpha delta-beta gamma.

Set D0=gamma s+delta t and N0=alpha s+beta t. The five binary quartics

    a=s^2 D0^2,       b=t^2 D0^2,       c=st D0^2,
    d=st N0^2,        e=-st D0 N0

satisfy both equations of S. Their coefficient matrix in the basis
(s^4,s^3t,s^2t^2,st^3,t^4) has determinant

    gamma^2 delta^2 Delta^3.

It is invertible, so the curve is a rational normal quartic. Explicitly
the projective coordinate change from Y0,...,Y4 is

    a=gamma^2 Y0+2gamma delta Y1+delta^2 Y2,
    b=gamma^2 Y2+2gamma delta Y3+delta^2 Y4,
    c=gamma^2 Y1+2gamma delta Y2+delta^2 Y3,
    d=alpha^2 Y1+2alpha beta Y2+beta^2 Y3,
    e=-alpha gamma Y1-(alpha delta+beta gamma)Y2-beta delta Y3.

At t=0 the curve meets the a A1 vertex, at s=0 the b A1 vertex, and
at D0=0 it meets the d A3 vertex. These are three distinct parameters
by gamma delta Delta nonzero. Deleting Y2 projects the curve to exactly

    C0=[s^4:s^3t:st^3:t^4].

## 3. Finite birational quartic projection and every extra fiber

Let p be the projection center Y2. In the a,b,c,d,e coordinates,

    p=(delta^2,gamma^2,2gamma delta,2alpha beta,-M),
    M=alpha delta+beta gamma.

For Q1=ab-c^2 and Q2=cd-e^2,

    Q1(p)=-3gamma^2 delta^2,       Q2(p)=-Delta^2.

In particular p lies outside S, and the projection is finite. Let
T_i be the derivative of Q_i in the omitted Y2 direction, restricted
to the rational normal quartic. Direct expansion gives

    T1=D0^2(gamma^2 s^2-4gamma delta st+delta^2 t^2),
    T2=-2Delta^2 s^2t^2.

The member Q1(p)Q2-Q2(p)Q1 has zero Y2^2 coefficient and linear
coefficient along the curve

    L_c=Q1(p) T2-Q2(p) T1
       =Delta^2 P4,
    P4=gamma^4 s^4-2gamma^3 delta s^3t
       -2gamma delta^3 st^3+delta^4 t^4.

This is nonzero, so the projection is birational on the nonempty
linear-coefficient open. Its integral image has degree four by the
hyperplane degree formula, and S is its finite normalization.

The endpoint coefficients of P4 are nonzero. Every zero therefore has
st nonzero, where T2 is nonzero. At such a point the projection-line
equations have, besides the displayed curve point, a distinct second
point of S: simultaneous coincidence would require T1=T2=0.
Equivalently, on the line c(s,t)+lambda p the restrictions are

    Q_i=lambda T_i+lambda^2 Q_i(p),

and L_c=0 supplies the common root
lambda=-T2/Q2(p)=-2s^2t^2, which is nonzero. Since the first curve
point projects isomorphically onto C0, this second point lies off it.

In fact P4 has four distinct roots. With r=gamma s/(delta t), its
affine polynomial is r^4-2r^3-2r+1, of discriminant -1728. The
four distinct extra points occur in four distinct fibers. Generic
uniqueness above C0 means no second curve component lies over C0;
these are isolated extra points of the full reduced inverse image.

A pulled-back mate section would have zero support exactly that
inverse image. On the integral surface its nonzero local equations
cannot have isolated zeros, so this is impossible. Every displayed
quartic is excluded for every positive mate degree.

## 4. Scope and exact control

Alpha or beta may be zero; only gamma delta Delta is required nonzero.
The determinant and all projection calculations are universal in these
parameters. They are checked in the independent
[uniform projection checker](../computations/verify_session_genus_one_projection_2026_10_09.py)
and its [JSON record](../scratch/session-genus-one-projection-checks-2026-10-09.json).

This construction binds one three-parameter family of pairs to the
specific deleted-middle-coordinate projection. It does not identify
every admissible projection of an A3+2A1 pair. Parameter changes moving
the three singular passages also transform the projection center;
see the [uniform adversarial note](2026-10-09-session-genus-one-uniform-projection-adversarial.md).
The global C0 problem and the complete A3+2A1 projection stratum remain
open at this record's scope.
