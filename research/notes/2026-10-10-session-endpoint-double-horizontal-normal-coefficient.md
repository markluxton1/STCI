# Endpoint double-horizontal normal coefficient

Date: 2026-10-10. Author: `bisection_weighted_normalization`.
Status: **PROVED HERE / bounded auxiliary observation**. This records a
normality restriction in the endpoint section/trisecant investigation;
it does not itself exclude that entire stratum.

Use the accepted actual normal ADE strict transform T in
Bl_Gamma(P3). At the endpoint trisecant Gamma=(x2,x3), use the affine
blowup chart

    a=x1, y=x2, b=x3/x2, x0=1,
    C0: a=b=r, y=r^3.

The double-horizontal residual case has actual equation

    T=-c1 a^2 b^2
      +y[(b-a)(A+B b+C b^2)+c1 a-a b^2(c2+c3 b)]
      +y^2(c2+c3 b)=0,
    c1!=0.

Its exceptional intersection is 2B0+2F0, where

    B0=(a=y=0),      F0=(b=y=0).

Here B0 is the horizontal section contracted in T->S, and F0 is a
line in the endpoint conic fiber. The letters B,C inside the coefficient
polynomial denote constants, not these curve names.

Along F0 all first partial derivatives of T vanish except possibly

    partial T/partial y = a(c1-A).

Consequently A=c1 would make the entire nonempty affine open of F0
singular on T. A normal surface is regular in codimension one, so the
accepted normality of T excludes this equality. Thus

    A!=c1.

This eliminates a potential radical-alignment exception in the A!=0
contact calculation using the actual global fiber, rather than imposing
a generic coefficient hypothesis.

There is also exact global degree bookkeeping for the first normal
coefficient. Write E for the exceptional divisor of the ambient blowup,
whose product coordinates are (Gamma, plane-pencil). Then

    H|E=O(1,0),       E|E=O(1,-1),
    T|E=O(2,2),      (T-E)|E=O(1,3).

The derivative in the normal direction to E is a section of O(1,3).
Its restrictions to the displayed B0 and F0 are respectively

    h_B=b(A+B b+C b^2),       h_F=a(c1-A).

Their complete degrees are three on B0 and one on F0. Hence, after the
normality restriction A!=c1, the only zero of h_F on the complete F0
is its endpoint contact. This excludes an additional unseen singular
point at the other affine chart of F0. The three zeros of h_B, counted
with multiplicity, must still be treated scheme-theoretically; repeated
zeros do not justify assuming only A1 surface singularities.

Possible contact A3/A5/A7 attachments and the resulting rational
correction cycle are separate obligations of the endpoint local audit.
No torsion-two relation or final section-case exclusion is asserted
merely from these derivative and degree observations.
