# Nonendpoint quintics: cubic conormal direction and generic all-degree obstruction

Date: 2026-10-12. Author: root.

Status: **DIRECT STRUCTURAL REDUCTION AND GENERIC ALL-DEGREE OBSTRUCTION;
separate independent audits requested**.
This concerns the genus-one quintic A4 normalization lane for fixed
`C0=[s^4:s^3t:st^3:t^4]`, over an algebraically closed field of
characteristic zero. It does not exclude all quintic carriers, every
mate degree, or the unrestricted STCI problem. The completed endpoint
exclusion is not reopened. Existing sealed records are unchanged.

## 1. Actual projection and balanced conormal direction

Use the [nonendpoint family](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md)
and the accepted [intrinsic pair](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md).
On the affine normalization chart let `c:T=0` and `delta!=0`. The four
sections restrict to

    (r^4,r^3(r-delta),r(r-delta)^3,(r-delta)^4).

Their T derivatives on c are

    L0=a-2r^2-r,
    L1=b-2r^2-r+delta r,
    L2=g-2r^2-r+3delta r,
    L3=d-2r^2-r+4delta r.

In the target chart x0!=0 write y=x1/x0, z2=x2/x0, w=x3/x0. The
actual balanced conormal coordinates are

    V=z2-y^3, U=w-(3/2)y z2+(1/2)y^4.

On c, y=(r-delta)/r. Direct differentiation, including the moving y,
gives

    V_T=P(r)/r^7, U_T=J(r)/(2r^7),

where

    P=(g-3b+2a)r^3
      +[6delta(b-a)+delta^3-3delta^2]r^2
      +[delta^2(6a-3b)+2delta^3]r-2a delta^3,

    J=(2d-3g+b)r^3
      +[3delta(g-b)+5delta^3-3delta^2]r^2
      +[3b delta^2+delta^3-delta^4]r-b delta^3.

For example P before expansion is
`r^3 L2-3r(r-delta)^2 L1+2(r-delta)^3 L0`;
J is `2r^3 L3-3r^2(r-delta)L2+(r-delta)^3 L1`.
The cancellation of the prospective higher terms is exact, not a
sampled degree observation.

The opposite target chart uses the reversed coordinates. With its raw
balanced coordinates Vraw and Uraw, choose Uop=Vraw/2 and Vop=2Uraw.
Modulo the square of the curve ideal,

    Uop=y^(-7)U, Vop=y^(-7)V.

Thus both first symbols have the same scalar transition. In particular,
on the opposite chart their T derivatives are J/[2(r-delta)^7] and
P/(r-delta)^7. There is no discarded target-infinity stratum at r=0.

For an actual admissible finite birational projection, the image surface
is generically regular along C0. Its conormal kernel is the kernel of
this generic projection-normal functional. The saturated quotient of
the balanced `O(-7)^2` is therefore determined by the rational ratio
`[J/2:P]`. Let Ph,Jh be their degree-three homogenizations in r and let
h be their homogeneous gcd degree, counting roots at infinity. Then

    L=O(e-7), e=3-h.

This follows either from the global balanced transition or the standard
description of a quotient of `O(-7)^2` by a basepoint-free degree-e
binary pair. It does not assume the normalization is immersive at every
point of c, or equate the common first-normal zero divisor with the top
BF defect divisor. P,J cannot both vanish identically: their constants
would force a=b=0, after which the coefficient of r in P is 2delta^3.

## 2. The socle bound for every possible mate exponent

A mate in this lane has degree 4k and generic multiplicity m=5k, by
the [quintic structural audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md).
The all-quartic exclusion makes k>=2. The generic transverse algebra is
curvilinear. The saturated finite-flat Gorenstein pairing gives

    E_(m-1)=L^(m-1)(D_(m-1)),
    deg E_(m-1)=-6-16k,
    deg D_(m-1)=(5k-1)(7-e)-6-16k >= 0.

Here D_(m-1) is effective. This is the same direct algebraic argument
as the [multiplicity-ten audit](2026-10-11-session-multiplicity-ten-filtration-audit.md)
and [uniform order-one bound](2026-10-06-uniform-order-one-frontier.md).
For primary-source context the Gorenstein duality and its quasiprimitive
BF specialization were freshly inspected in
[Manolache, 2023, pp.143-145](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf).
The displayed numerical inequality is derived here from CI adjunction;
it is not attributed verbatim to that paper.

Consequently:

* If Ph,Jh are coprime, e=3 and the top defect degree is 4k-10.
  Thus k=2 is impossible; any mate would have degree at least twelve.
  Nothing here excludes k>=3.
* A possible degree-eight mate requires h>=1. Equivalently the two
  homogeneous cubics have a common zero, including infinity. This is
  a proper closed resultant locus in the five projection parameters,
  restricted to delta!=0 and actual center avoidance.

To verify properness, at delta=1,a=1,b=g=d=0 the pair is
`P=2(r^3-4r^2+4r-1)`, `J=2r^2`, homogenized to degree three.
The only homogeneous roots of J are r=0 and infinity. Neither is a root
of P, so the pair is coprime. This point proves
that the resultant polynomial is nonzero; admissibility of this
particular point is not asserted. The center-avoidance set is a
nonempty open set: the fixed center point lies in the span of c but
outside S (S's hyperplane section there is c+ell), and the line
extensions meeting S form an incidence of dimension at most two in
the four-dimensional extension space. Hence the coprime open meets
the admissible open. This is a generic degree-eight exclusion, not a
full parameter-space or all-mate-degree exclusion.

## 3. An all-degree obstruction from immersion and the actual conductor

Write `Jbar=d-2g+2b-a`. We now prove the stronger statement:

> Every admissible nonendpoint projection with coprime Ph,Jh and Jbar!=0
> has an actual point outside c mapping onto C0. It therefore has no
> mate of any positive degree. A hypothetical mate must satisfy
> `Jbar * Res_h(Ph,Jh)=0`.

This is a proper closed necessary locus, not its exhaustion. No upper
bound on higher contact lengths is deduced from the first symbols.

Suppose full inverse support holds. Every closed point of C0 then has
exactly one point in its normalization fiber, because c->C0 is an
isomorphism and there are no other points over C0. At a finite r, S is
smooth with coordinates r,T. The derivative tangent to c is nonzero
downstairs. The balanced normal projection vector is `[J/2:P]`; the
coprimality hypothesis prevents its two entries from vanishing
simultaneously at any finite r. The opposite chart checks r=0, while
r=delta is regular in the first chart. Thus the target differential
has rank two and the map on cotangent spaces is surjective at every
smooth point of c.

At the remaining A4 point, use the actual chart Z0=1 from the
[independent local-chart audit](2026-10-11-session-dp5-a4-local-chart-independent-audit.md).
Let alpha=Z1/Z0, beta=Z2/Z0, chi=Z3/Z0. These generate the maximal
ideal; the single surface relation has no linear term. Put

    dZ=alpha beta-chi^2,
    eZ=beta^2-alpha beta chi+chi^3, h=beta+chi.

The actual projection sections on this chart are

    X0=1-alpha+a h,
    X1=1+(delta-1)alpha+b h,
    X2=1+(3delta-1)alpha+3delta^2 chi-delta^3 dZ+g h,
    X3=1+(4delta-1)alpha+6delta^2 chi-4delta^3 dZ+delta^4 eZ+d h.

They all have value one at A4. The three target ratios Xi/X0-1 have
linear coefficient matrix in alpha,beta,chi

    [delta,  b-a, b-a]
    [3delta, g-a, g-a+3delta^2]
    [4delta, d-a, d-a+6delta^2].

Its determinant is `-3delta^3 Jbar`, nonzero under the stated hypothesis.
It therefore surjects onto the full three-dimensional source cotangent
space, including the singular A4 point. Smoothness of S at that point
is neither assumed nor required.

Here is the finite local algebra step. For a finite birational
normalization map with a unique point over a closed point, localize the
target ring A and its normalization B there. B is local and finite
over A, and the residue fields agree. Cotangent surjectivity says
`m_B=m_A B+m_B^2`. Nakayama over B on `m_B/m_A B` gives `m_B=m_A B`.
Consequently B/m_A B is generated by the residue of 1. Nakayama over
A makes B generated as an A-module by 1, so B=A. This proves local
isomorphism rather than only injectivity of tangent vectors.

The projection would therefore be a local isomorphism along every
point of c. Its actual conductor ideal is then a unit there. But the
[accepted quintic conductor computation](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
gives an invertible upstairs conductor ideal O_S(-2H), whose effective
Cartier divisor Dc satisfies

    degree(O_S(Dc)|c)=2H.c=8.

If Dc misses c, its defining section restricts to a nowhere-zero
section of this degree-eight line bundle on P1, which is impossible.
Thus full inverse support cannot hold. Finiteness of the normalization
then gives an actual additional point over C0, contradicting any mate.
This is an entire support/conductor argument and applies to all k.

The necessary locus is proper: the coprime example in section 2 has
Jbar=-1. Both required nonvanishings hold there, and the irreducible
parameter space's admissible nonempty open intersects their nonempty
open. The particular example's admissibility remains unasserted.

The remaining parameters with a common homogeneous root or Jbar=0
are genuinely open for this argument. Their actual conductor restriction
to c, of degree eight, must be supported at the finite common-root
points and the A4 point where cotangent rank can fail. No multiplicity
bound on this restriction follows from the first symbols alone.

## 4. An explicit complete incidence cover of the necessary common-root locus

The homogeneous common-root condition can be retained without expanding
a large resultant. For each actual delta!=0 it is exactly the union of:

* r=0: a=b=0;
* r=infinity: g=3b-2a and d=4b-3a;
* a finite nonzero root rho: P(rho)=J(rho)=0.

In the last case one may solve without losing a stratum:

    g=3b-2a-[6delta(b-a)+delta^3-3delta^2]/rho
      -[delta^2(6a-3b)+2delta^3]/rho^2
      +2a delta^3/rho^3,

    d=(3g-b)/2-[3delta(g-b)+5delta^3-3delta^2]/(2rho)
      -[3b delta^2+delta^3-delta^4]/(2rho^2)
      +b delta^3/(2rho^3).

Repeated roots and multiple common roots remain in this incidence
cover. It does not classify actual higher embedded jets or assert any
surviving parameter admits a mate. At a finite smooth source point
where both target chart and source transverse coordinate are regular,+a common root records a transverse projection rank drop along c.
No root-count or contact bound is inferred from that first symbol.

## 5. Evidence and next step

The [supporting checker](../computations/verify_session_nonendpoint_conormal_cubics_2026_10_12.m2)
verifies the two literal cubic identities, the zero and infinity controls,
the nonzero-pair and coprime examples, and the actual opposite target-frame
transition. Captured execution status must be read from its own new
validation directory; a source file alone is not a successful run.
The first captured run passed the P identity but rejected the hand-expanded
J coefficients. The error was the sign of two terms from expanding
delta*r*(r-delta)^3; its source and raw failure are retained. The corrected
coefficients are +5delta^3-3delta^2 at r^2 and delta^3-delta^4 at r.
Two further runs retained fraction-field differentiation interface failures
after the first five conditions passed. The repaired first-neighborhood
ring implementation then passed all seven supporting conditions. These
four executions are one source lineage, not four independent certificates.
The [separate A4 cotangent checker](../computations/verify_session_nonendpoint_a4_cotangent_rank_2026_10_12.m2)
checks three literal local identities; the Nakayama and conductor argument
is a written proof, not a finite numerical extrapolation.
Separate independent auditors have been asked to reconstruct the quotient
identification, full chart scope and all-degree conductor argument. Those
audits are required before this note is promoted to the independently
audited frontier.

Next, combine the common-root incidence with the residual-divisor/fiber
conditions, retaining all denominator and infinity strata. The e=3 open
survives the numerical argument for k>=3, but section 3 excludes it when
Jbar!=0 by the separate support/conductor proof. The remaining closed
locus still needs full conductor power descent or a stronger geometric
obstruction.
