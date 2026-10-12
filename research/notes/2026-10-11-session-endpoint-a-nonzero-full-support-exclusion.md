# Endpoint quintic projections with a nonzero: complete support exclusion

Date: 2026-10-11 (executions continued through 2026-10-12 UTC).
Author: `oct11_endpoint_a_nonzero_support`.
Status: **COMPLETE PROOF PROPOSED, pending independent global audit**.

Work over an algebraically closed field of characteristic zero. This proof
concerns only the displayed endpoint projection of the degree-five A4
normalization. The applicability to that intrinsic endpoint lane uses the
[pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and the [explicit model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
It does not exclude nonendpoint projections or all quintic surfaces.
The [quadric-factor audit](2026-10-11-session-quintic-endpoint-factor-independent-audit.md)
supplies the preceding geometric reductions, but the proof below establishes
an actual off-curve inverse point rather than relying on a first-normal
contact count. No frozen canonical source or existing seal is changed.

## 1. Claim and projective boundary

On the actual open normalization chart S minus ell=A2(r,T), let c be T=0
and consider

    X0=1+aT,
    X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-2r^2-r)T+T^2,             a!=0.

Assume the projection center is disjoint from S. Then at least one point
off c maps into fixed C0. Consequently the full inverse-support condition
required by a mate fails in every mate degree.

Define the two parameter polynomials

    Cb=a^2*g-a*b-b^3,
    Db=a^3*d-a^2*b-2*a*b^2-b^4-a^2.

At (r,T)=(b/a,-1/a), the first two X coordinates vanish, while
X2=-Cb/a^3 and X3=-Db/a^4. If Cb=0 and Db=0 the point is a
projection base point, forbidden by center avoidance. If Cb=0 and Db!=0
it is an actual off-c point mapping to C0 at infinity, [0:0:0:1].
Thus a hypothetical full-support projection must have Cb!=0. No saturation
at X0 discards this boundary; it has been settled explicitly.

## 2. Exact target-parameter residual equations

For a finite target point [1:z:z^3:z^4], the equation X1=z X0 gives
r=z+(az-b)T. Put

    A=az-b,
    U=2az^3-3bz^2-z+g,
    V=3az^4-4bz^3-2z^2-z+d,
    h=az^3+z-g-1,
    J=A V-(Az-1)U.

After substitution, the remaining two equations, with their common factor
T removed, are

    P=U+(3zA^2-A)T+A^3 T^2,
    R=V+(6z^2A^2-4zA-A+1)T+(4zA^3-2A^2)T^2+A^4 T^3.

The exact linear remainder is

    A R-(A^2 T+Az-1)P=A^2 h T+J.

Define the target septic

    E=J^2-(3zA-1)hJ+A U h^2.

Its leading coefficient is a Cb, so Cb!=0 makes its degree exactly seven.
The fixed-degree Sylvester identity is Res_T(P,R)=A^7 E, as checked in
the separately preserved [subresultant source](../computations/verify_session_quintic_endpoint_subresultant_2026_10_11.m2).
We use the explicit remainder to retain all exceptional fibers.

At A=0 one has E=az^3+z-g. There z=b/a and
a^2 E=b^3+ab-a^2g=-Cb, so no septic root has A=0.
Also the exact cleared evaluation is

    a^2 P(-1/a)=Cb.

Thus no common residual solution can have X0=1+aT=0 on Cb!=0.
Every residual solution constructed below is a genuine finite target
fiber with a defined image.

## 3. Every septic root is a common U,V root under full support

Suppose the projection has no off-c inverse point over C0. Let rho be a
root of E. By the preceding section A(rho)!=0.

If h(rho)!=0, the actual value T=-J/(A^2 h) solves P=0, because

    A^4 h^2 P(-J/(A^2 h))=A^3 E.

The linear remainder then gives R=0. The X0 boundary is impossible, so
absence of an off-c inverse point forces T=0. Consequently U(rho)=V(rho)=0.

If h(rho)=0, the equation E=0 gives J(rho)=0. The linear remainder
now shows every root of the quadratic P solves R. Its leading coefficient
A^3 is nonzero, and no root can have X0=0. Therefore all its roots must
be T=0. This requires U=0 and 3rho A-1=0. The identity
h=3rho^2 A-1-U gives rho=1 and A=1/3. J=0 then gives V=0, hence

    b=a-1/3,       g=a,       d=a+5/3.

At this exceptional contact the first two coefficients of E at z=1
vanish and its quadratic coefficient is exactly 1/9. The septic root
therefore has order exactly two. Every other h-zero septic fiber already
contains an off-c point.

Thus under full support all seven roots counted with multiplicity must
lie among the common geometric roots of U,V. There are at most three such
points, since U has degree exactly three.

## 4. Actual higher jets bound each root by four

At a common root rho, set k=a rho-b. The coefficient of z-rho in E is

    -(3rho^2 k-1)*(6rho^2 k^2+3rho k^2-6rho k+1).

We have already settled h=0, where the only support-compatible root has
order two. Assume h=3rho^2 k-1!=0. A repeated septic root must satisfy

    6rho^2 k^2+3rho k^2-6rho k+1=0.

In particular rho and k are nonzero. Put q=k rho and

    D=6q^2-6q+1,       B=3q^2+3q-1.

The repeated-root condition is equivalent to

    k=-D/(3q),       rho=q/k.

Here q,D are nonzero. Moreover

    h=-(3q-1)B/D,

so h!=0 excludes both 3q-1=0 and B=0. At fixed q, the coefficient
e2 of (z-rho)^2 is linear in a, and its a coefficient is

    -3q B(3q-1)^2/D^2.

It is nonzero throughout this remaining stratum. Thus order at least
three forces the unique value

    a=-D^2*(54q^4-72q^3+15q^2-3q+1)/(27q^3(3q-1)^2).

At this value the next two coefficients are

    e3=-B D N9/(81q^4(3q-1)^3),
    e4=-D^2 N11/(81q^4(3q-1)^3),

where

    N9=8748q^9-20412q^8+18954q^7-8262q^6+1458q^5
       -252q^4+180q^3-66q^2+12q-1,

    N11=17496q^11-46656q^10+39366q^9-16848q^8+12123q^7
        -12231q^6+8316q^5-2934q^4+612q^3-129q^2+25q-2.

Exact polynomial arithmetic gives

    gcd(numerator(e3),numerator(e4))=D       up to nonzero scalars.

D!=0 makes simultaneous vanishing impossible. Thus every support-compatible
septic root has order at most four. This is a bound obtained from the
full third and fourth jets of the actual residual equation, not from
first-normal data. An earlier provisional message saying order at most
three was incorrect and was withdrawn before acceptance: N9 can vanish,
so order four must be retained.

## 5. An order-four root prevents every second common point

At a common root rho the exact polynomials after removing z-rho are

    U/(z-rho)=2a(z^2+rho z+rho^2)-3b(z+rho)-1,

    V/(z-rho)=3a(z^3+rho z^2+rho^2 z+rho^3)
              -4b(z^2+rho z+rho^2)-2(z+rho)-1.

At the unique a value in the preceding section, form their degree-(2,3)
Sylvester determinant Delta over QQ(q). Exact arithmetic gives

    gcd(numerator(e3),numerator(Delta))=D     up to nonzero scalars.

Consequently an order-four root (which requires e3=0) has Delta!=0.
The two quotient polynomials share no root. In particular U,V have no
second common geometric point. This also retains repeated roots at rho;
none were removed by a squarefree assumption.

There cannot be just one common point under full support: its order is at
most four but E has degree seven. There cannot be just two common points:
an order-four point would prohibit the second, while otherwise their total
order is at most six. The only remaining possibility is three distinct
common roots.

## 6. The three-common-root family is excluded

Three distinct common roots force U to divide V. Direct long division gives

    a=3b^2/2,       g=1/(9b)-2/3,       d=1/(54b^2)-1/(9b),

with b!=0. In this family Cb=-3b^3(2b+3)/4, so b!=-3/2 as well.
Write E=U S. The [independent shifted-variable support certificate](2026-10-11-session-endpoint-three-common-roots-shifted-replay.md)
proves S is a genuine quartic and cannot have all its roots among the roots
of U: its collision resultant with U and its derivative resultant have
coprime parameter factors. The separate
[original-variable audit](2026-10-11-session-three-common-roots-residual-quartic-independent-audit.md)
reconstructs the same certificate. The contradiction retains repeated
roots and all allowed parameters, with no unresolved finite exceptional set.

The three cases for the number of common geometric roots are exhaustive.
Thus the supposition of full inverse support is impossible. There is an
actual off-c point over C0 for every admissible displayed a!=0 endpoint
projection, and no mate in any degree can exist for that projection.

## 7. Evidence and scope

The dedicated [target-jet checker](../computations/verify_session_endpoint_a_nonzero_target_jets_2026_10_11.m2)
passes sixteen exact assertions. They check the leading coefficient,
projective boundary evaluations, exceptional h-zero root order, first
jet, rational parameter reduction, solved second jet, exact third/fourth
jets, and both polynomial-gcd certificates. Its source hash and actual
execution, including the failed coefficient-ring comparison development
attempt, are preserved in the
[execution record](../validation/2026-10-11-endpoint-a-nonzero-support/execution-record.json).
Earlier exploratory coefficient outputs and a fraction-field construction
failure are preserved separately in the same attempt history; they are
leads, not additional certificate implementations.

This is a proposed complete support proof for a!=0 in the intrinsic
endpoint lane. Independent global proof audit must verify the rational
coefficient quantifiers and the exceptional fibers before canonical
promotion. The a=0 support/jet lanes, the nonendpoint parameter family,
other sectional genera and unrestricted quintic/higher carrier degrees
remain separate mathematical obligations.
