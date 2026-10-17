# Nonendpoint quintics: exact pole filtration and a ramified-line subfamily

Date: 2026-10-12. Author: root, completing the saved calculations of
`oct11_nonendpoint_quadric_structure` after its explicit usage-limit stop.

Status: **DIRECT STRUCTURAL PROOF AND BOUNDED ALL-POWER OBSTRUCTION;
separate mathematical proof audit remains outstanding**. Seven supporting
identities now pass in a captured repaired execution. This is not an
exclusion of the entire nonendpoint family or of all quintic carriers.
Work over an algebraically closed field of characteristic zero.

## 1. The full nonendpoint parameter and actual sections

Use the accepted genus-one normalization pair in the
[intrinsic classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and [explicit model](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
On S minus ell use r,T with

    U=(1,r,r^2,r^3-rT,r^4-(2r^2+r)T+T^2), h=T.

The A4 point on c is r=infinity. Translate the two finite double roots
of the projection-center binary quartic to 0,delta, where delta!=0.
Here delta is their difference, rather than the half-separation used
in the midpoint convention of the classification. It cannot be scaled
to one by an automorphism of the pair. The four lift parameters a,b,g,d
give actual sections

    X0=U4+a h,
    X1=U4-delta U3+b h,
    X2=U4-3delta U3+3delta^2 U2-delta^3 U1+g h,
    X3=U4-4delta U3+6delta^2 U2-4delta^3 U1+delta^4 U0+d h.

On c these restrict to r^4, r^3(r-delta), r(r-delta)^3,
(r-delta)^4. They give fixed C0 with target parameter z=(r-delta)/r.
The intrinsic A4 point maps to the nonendpoint z=1. A line center
must still avoid S for an admissible normalization projection.

## 2. All pole sections along ell, with no cancellation shortcut

Put t=T-r^2 and v=t^2-r^3. The affine coordinate ring of S minus ell
is k[r,t], equivalently

    k[r,t,v]/(t^2-r^3-v).

The relation is monic in t, so the monomials r^i t^j v^k, with
i,k>=0 and j=0 or 1, are a vector-space basis. In the genuine fourth
blowup chart (x,u), the rational functions in the U0 frame are

    r=x^(-2)/(1+xu),
    t=x^(-3)/(1+xu),
    v=u*x^(-5)/(1+xu)^3.

Their pole orders along ell are 2,3,5. The leading coefficient of
r^i t^j v^k is u^k and its weight is 2i+3j+5k. At any fixed weight,
distinct basis monomials have distinct k: for fixed k the equality
2i+3j=2i'+3j' with j,j' in {0,1} forces i=i',j=j'. Thus their leading
coefficients are independent polynomials in u. There is no cancellation
among the terms of maximal weight in any nonzero linear combination.

Every rational section of O_S(n ell) restricts to a polynomial on the
complete open A2. Conversely a polynomial whose pole order along ell is
at most n has no other codimension-one pole and is a section of this
Weil divisor sheaf, by its definition on a normal surface. Consequently
the displayed weight filtration is exhaustive. In particular

    H0(S,O(6ell))=span{1,r,t,r^2,rt,v,r^3}.

The separately completed [low-pole-spaces proof](2026-10-11-session-a4-low-pole-spaces.md)
gives the same filtration and an exhaustive classification of prime equations
of degrees two, three and four. Root read and reconstructed that saved proof;
it was completed before its parent worker stopped. No CAS run is claimed for
its geometric section-space argument.

This is a seven-dimensional space of Weil-divisor sections, not a claim
that O(6ell) is Cartier or that these are anticanonical sections.

## 3. The exact residual divisor of the pulled quadric

Set A=a+d-b-g and B=ad-bg. For q=X0 X3-X1 X2, direct expansion in the
U0 frame gives q=T F, with

    F=A v-3delta^2 r^3
      +((4a-3b-g)delta-3delta^3-A)rt
      +(B+(6a-3b)delta^2+3delta^3)r^2
      +(B+delta^4)t+((-4a+b)delta^3-delta^4)r+a delta^4.

Its unique weight-six term is -3delta^2 r^3, so its pole order is
exactly six for every nonzero delta and all four lift parameters.
Since div(U0)=5ell and div(T)=c-4ell, the actual section q of 2H has

    div(q)=c+D, D=div(F)+6ell.

D is effective of degree six and does not contain ell. In the actual
fourth-chart frame the restriction of q to ell is -3delta^2, also
showing that ell is not a divisor of q. Dividing the affine normalized
function by T does not make F a section of H: division by the actual
hyperplane h would have a pole along ell. The endpoint factorization
into two anticanonical sections cannot be transferred here.

The accepted unique degree-one prime on S is ell. Since D excludes it,
the possible degree partitions of its prime components, counting
multiplicities, are exactly

    6; 2+4; 3+3; 2+2+2.

These are possible numerical partitions, not an assertion that each is
realized. Their genera, A4 contacts and full inverse support still need
analysis.

## 4. Entire-line ramification forces an all-power obstruction

Use the fourth chart with B0=1+xu, C0=1+x+x^2u. Here
Q=B0^2 C0^5 is the actual section of 4H with divisor 5c. On ell:x=0,
the four actual projection sections restrict to

    (u-1, u-1+delta, u-1+3delta, u-1+4delta).

The generic target differential has rank one exactly when

    g+3delta^2+2a-3b=0,
    d+6delta^2+3a-4b=0.                     (R)

One can obtain these equations by subtracting the first two rows from
the raw projective tangent matrix (section values, their u derivatives,
their x derivatives). Its 3x3 minors generate precisely the ideal
delta times the two left sides. Since delta!=0, vanishing at generic u
is equivalent to (R). The differential has rank at least one: in the
patch X0!=0, the u derivative of X1/X0 is -delta/(u-1)^2.

Put lambda=(b-a)/delta. On (R), the transverse derivation at generic ell

    K=partial_x+(u^2+lambda u-lambda-a)partial_u

annihilates all three actual target affine ratios X1/X0,X2/X0,X3/X0.
For example the x derivative of X1/X0 is
delta*(u^2+lambda u-lambda-a)/(u-1)^2, so its u derivative cancels;
the other two ratios give precisely the two conditions (R).
The chain rule and quotient rule therefore make K annihilate every
pulled-back downstairs local function.

Use the actual downstairs frame X0^4. At generic ell, X0=u-1 is a unit,
and q0=Q/X0^4 is a unit. Direct logarithmic differentiation gives

    K(log Q)|ell=2u+5,
    K(log X0)|ell=u+lambda,
    K(q0)/q0|ell=5-2u-4lambda.

Here log differentiation means the algebraic expression K(f)/f, with
no analytic logarithm assumption. For every positive k,

    K(q0^k)|ell=k*q0^k|ell*(5-2u-4lambda) != 0.

The last factor has u coefficient -2, and characteristic zero makes
-2k nonzero. Every mate would pull back to a nonzero scalar times Q^k,
so its normalized affine function would have both zero and nonzero
K derivative. Therefore every admissible nonendpoint projection
satisfying (R) has no mate in any positive degree.

This excludes a precisely specified subfamily. The generic unramified
family is open; a first derivative at isolated points is not promoted
to an obstruction for every projection.

## 5. Saved failure history and exact supporting evidence

The [supporting source](../computations/verify_session_quintic_nonendpoint_structure_2026_10_11.m2)
passes seven conditions in
[root repair attempt 05](../validation/2026-10-11-quintic-nonendpoint-structure/attempt-05-root-name-repair/execution-record.json).
The final source SHA-256 is
`24ae9f4b3b2092bf7870f4f09e17307b2feda84000ad91eb6087c022b4892738`.
The record binds its copied source, actual exit zero and separate raw
stdout/stderr. Eight printed PASS lines consist of seven conditions and
one final PASS ALL label; they are not eight mathematical checks.

Attempts 01--03 remain saved from before the worker stopped. Attempt 03
failed the residual-expression assertion because a multiline expression
was parsed incompletely. Root attempt 04 wrapped the intended expression
in parentheses, passed the first two checks, and then failed on the
protected Macaulay2 variable hh. Attempt 05 renamed that variable and
passed all seven conditions. Both repairs and both captured root runs
are retained. These are repaired executions of one checker lineage,
not independent geometric proofs. A separate mathematical audit of the
written filtration and subfamily obstruction remains outstanding.
