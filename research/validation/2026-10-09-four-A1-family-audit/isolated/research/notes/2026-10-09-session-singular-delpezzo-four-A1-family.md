# A genus-one four-A1 normalization family for fixed C0

Date: 2026-10-09. Owner: `singular_normalization_next_frontier`.
Status: **PROVED HERE, submitted for independent audit**. Uniform
exclusion of the displayed family in every mate degree; no assertion
that this family exhausts all singular normalizations of genus one.

This note follows the [sectional-genus reduction](2026-10-09-session-normalization-sectional-genus-zero.md).
The remaining quartic normalization lane has pi=1 or pi=2 and a
non-Cartier smooth lifted curve passing through Sing(S). The example
here realizes the genus-one numerical and torsion conditions with
the actual fixed C0, then excludes its projected quartics by their
full inverse-image fibers. Thus existence of those numerical and
torsion conditions is weaker than existence of a mate.

Throughout k is algebraically closed of characteristic zero. Set

    C0=[U^4:U^3 V:U V^3:V^4] subset P3.

## 1. The singular del Pezzo normalization

In P4[a:b:c:d:e], let

    S:  a e=c^2,       b d=c^2.

This is an integral degree-four complete intersection. One direct
description is the quotient of P1[u0:u1] times P1[v0:v1] by the
involution (u1,v1)->(-u1,-v1), with invariant sections of O(2,2)

    a=u0^2 v0^2, b=u0^2 v1^2, c=u0u1v0v1,
    d=u1^2v0^2, e=u1^2v1^2.

They have no common zero, and the resulting map is generically of
degree two: on the torus its invariant function field is
k((u1/u0)^2,(v1/v0)^2,(u1/u0)(v1/v0)). The image is integral of
degree (2,2)^2/2=4 and is contained in the two independent quadrics.
Those quadrics form a codimension-two complete intersection of
degree four, so their scheme is this integral image. Equivalently
one can use the toric ring with relations a e=c^2=b d; its dense
torus and the reduced coordinate boundary give the same conclusion.

The singular points of S are exactly the four coordinate vertices
with nonzero a,b,d, or e. In the a!=0 chart, eliminating e gives
b d=c^2, the A1 surface singularity at its origin; the other three
charts have the same local equation. All other points have independent
quadric gradients. The surface is S2 by the complete-intersection
property and R1 by its isolated singularities, hence normal.

Write H=O_S(1). Adjunction gives K_S=-H and H^2=4. A general
hyperplane section therefore has genus one. This is a singular
normalization outside the accepted smooth F0/F2/P2 lanes.

## 2. A smooth rational quartic with 2c linearly equivalent to 2H

Choose parameters alpha,beta,gamma,delta satisfying

    alpha beta gamma delta Delta != 0,
    Delta=alpha delta-beta gamma,     M=alpha delta+beta gamma.

The odd (2,2) section on the quotient cover is

    f=alpha u0^2v0v1 + beta u0u1v0^2
      + gamma u0u1v1^2 + delta u1^2v0v1.

Its curve is smooth elliptic. For instance, on the torus put
t=u1/u0, u=v1/v0, and r=t/u. Dividing f by u gives

    u^2=-(alpha+beta r)/(r(gamma+delta r)).

The four branch points 0, infinity, -alpha/beta, -gamma/delta
are distinct on the stated parameter open. The connected degree-two
cover has genus one; the integral (2,2) closure already has arithmetic
genus one, so it has no singular defect. Its quotient is a smooth P1.

More concretely, introduce the standard rational normal quartic
coordinates

    Y_i=U^(4-i)V^i,       i=0,...,4.

Its image in S is obtained by the linear transformation

    a=gamma^2 Y1+2 gamma delta Y2+delta^2 Y3,
    b=-alpha gamma Y0-M Y1-beta delta Y2,
    c=-alpha gamma Y1-M Y2-beta delta Y3,
    d=-alpha gamma Y2-M Y3-beta delta Y4,
    e=alpha^2 Y1+2 alpha beta Y2+beta^2 Y3.

The determinant of this transformation is

    alpha beta gamma delta Delta^3.

It is therefore a projective change of coordinates on the whole
parameter open. Substituting the binary quartics into the two equations
of S gives zero. Its image, denoted c, is a smooth rational normal
quartic of degree four passing through all four A1 vertices, at the
four distinct branch parameters recorded above.

The square of the odd section is the invariant quadric section

    Q=alpha^2 a b+beta^2 a d+gamma^2 b e+delta^2 d e
      +2c(alpha beta a+alpha gamma b+beta delta d+gamma delta e)
      +2(alpha delta+beta gamma)c^2.

Its pullback is exactly f^2. On S its divisor is exactly 2c, because
the quotient map is finite and generically unramified over that curve.
Consequently 2c~2H. The curve c is non-Cartier at the four A1 points;
its local class has order two, as in the
[local lift countershield](2026-10-09-session-singular-local-lift.md).
On the minimal resolution the correction is half the sum of the four
disjoint (-2) curves, so q=-Z^2=2. This realizes the surviving identity
q=2pi for pi=1. No descent of Q to a projected quartic is assumed.

## 3. Projection gives integral quartics containing the exact fixed C0

Use the inverse coordinates Y0,...,Y4 of section 2 and project by
deleting Y2. Put

    (x0,x1,x2,x3,z)=(Y0,Y1,Y3,Y4,Y2).

The image of c is exactly the displayed C0. Let Q1=a e-c^2 and
Q2=b d-c^2, now expressed in these coordinates. Their complete
identities are

    Q1=Delta^2(x1 x2-z^2),
    Q2=-A2(x1 x2-z^2)+L z+R,
    A2=-(alpha^2delta^2+alpha beta gamma delta+beta^2gamma^2),

where

    L=alpha^2gamma^2 x0-alpha gamma M x1
      -beta delta M x2+beta^2delta^2 x3,

    R=alpha gamma M x0x2+alpha beta gamma delta x0x3
      -alpha^2gamma^2 x1^2-alpha beta gamma delta x1x2
      +beta delta M x1x3-beta^2delta^2 x2^2.

The center P=(Y0,Y1,Y2,Y3,Y4)=(0,0,1,0,0) has Q1(P)=-Delta^2,
so it is disjoint from S. The projection is a morphism, and is finite
because its pullback O(1)=H is ample. The coefficient of x0 in L
is alpha^2gamma^2!=0. On the dense open L!=0 the equation L z+R=0
recovers z=-R/L. Thus the map S->X subset P3 is birational, not a
degree-two projection onto a quadric.

Since S is normal and the map is finite birational, it is the
normalization of its image X. The image has degree four and is integral.
Its equation, up to a nonzero scalar, is

    F=R^2-x1 x2 L^2.

Indeed eliminating z gives

    resultant_z(Q1,Q2)=Delta^4 F.

The geometric finite-birational degree calculation proves that F is
the actual integral quartic equation; an uncancelled resultant alone
would not suffice to prove that statement. There is no nonzero scalar
specialization in this parameter open that destroys the argument.

## 4. Uniform full-fiber obstruction to every mate

The lifted c is the rational normal quartic with

    (x0,x1,x2,x3,z)
       =(U^4,U^3V,UV^3,V^4,U^2V^2).

The pullback of L to C0 is the nonzero binary quartic

    L_C=alpha^2gamma^2 U^4-alpha gamma M U^3V
        -beta delta M UV^3+beta^2delta^2 V^4.

Its endpoint values are

    L_C(U,0)=alpha^2gamma^2 U^4,
    L_C(0,V)=beta^2delta^2 V^4.

Therefore it has a zero [U:V] over k and every zero has U V!=0.
Repeated roots and special parameter values are allowed here; the
proof does not assume L_C squarefree. At any such zero,

    R_C=-U^2V^2 L_C=0,
    z^2=x1x2=U^4V^4 != 0.

The two distinct points

    [U^4:U^3V:+U^2V^2:UV^3:V^4],
    [U^4:U^3V:-U^2V^2:UV^3:V^4]

both lie on S and project to the same point of C0. Only the plus
point belongs to c. The C0 parametrization is an embedding, so the
four retained coordinates determine [U:V] uniquely; they cannot be
the retained coordinates of a different parameter on c. Characteristic
zero and U V!=0 make the two points distinct.

Thus the entire inverse image of C0 has an additional point outside
its unique curve lift c. A mate would require its entire support to
be exactly c and nu|c to be an isomorphism. Equivalently this
normalization fiber would have to be a singleton. The two explicit
points contradict that necessary condition.

**Theorem.** Every quartic X in the entire parameter open of section
2 is excluded as a carrier of a mate for fixed C0, in every mate
degree. This includes all repeated-root subloci of L_C in that open.

## 5. Exact controls and independent records

The [uniform exact checker](../../computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py)
reconstructs the actual five-by-five transformation, its determinant,
the two quadratic equations, the elimination identity and its scalar,
the C0 coordinate restriction, both normalization points over every
L_C zero, and the quotient-cover equality q*Q=f^2. Its identities
are over Q[alpha,beta,gamma,delta]; it does not replace parameter
coverage by a finite sample. The geometry and proof of the full-fiber
obstruction are the text above.

The first source run was terminal exit zero with PASS in 0.47 seconds.
Source SHA256:

    0e72ced585c9e1135648b5e9a278c09964c6677009f50554aac46a68d3b6cef4

The [report](../scratch/session-singular-delpezzo-four-A1-family-2026-10-09.json)
retains the uniform parameter open and disclaims an unrestricted STCI
claim. An independent auditor is reviewing the family proof and a
separate child reconstruction checks the exact alpha=beta=gamma=1,
delta=2 example, including its actual conductor.

For that example,

    L=x0-3x1-6x2+4x3,
    R=-x1^2-2x1x2+6x1x3-4x2^2+3x0x2+2x0x3,
    L_C=(U^2-4UV+2V^2)(U^2+UV+2V^2).

All its conductor intersections likewise have U V!=0. The actual
conductor calculation is useful evidence but is not needed by the
uniform support proof, which already uses the actual finite
normalization and two distinct fiber points.

## 6. Scope of the progress

The construction proves that pi=1, non-Cartier c through isolated
normalization singularities, b c~bH, and even 2c~2H can occur on
actual integral quartic carriers of the fixed C0. Those facts alone
do not justify a minimal-degree reduction. The complete normalization
fiber condition excludes the displayed family.

Parameters with alpha beta gamma delta Delta=0 make the displayed
five-coordinate transformation singular. They are not part of this
normalization construction, and no claim about quartic carriers
obtained by another construction at those degenerations is made.
Other four-A1 projections, the A3+2A1 torsion configuration, other
genus-one singular normalizations, and genus-two normalizations still
require a structural argument or an exhaustive correctly scoped
classification. No canonical frontier file has been edited by this
owner note.
