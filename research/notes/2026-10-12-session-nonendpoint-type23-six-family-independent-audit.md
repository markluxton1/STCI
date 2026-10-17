# Independent audit: all six Type 2/Type 3 quartic-residual families are excluded

Date: 2026-10-12. Auditor: `oct12_type1_two_family_audit`.

Status: **PASS: independently reconstructed all-mate exclusion for the two
Type 2 and four Type 3 branches.** Together with the separate
[Type 1 independent audit](2026-10-12-session-nonendpoint-type1-two-family-independent-audit.md),
this excludes the entire residual partition 2+4 in the accepted nonendpoint
genus-one quintic family. The integral and cubic-pair residual cases, other
quintic normalizations and higher-degree carriers remain outside this result.
The fixed C0 and the universal STCI problem remain open.

The frozen [owner proof](2026-10-12-session-nonendpoint-type23-six-family-exclusion.md)
was read at SHA-256
`11c13ba7201b84e02cf1a2ab1d6b42d8cf5fbcbaf15b51e95d5c75c65f7de48d`.
No owner, canonical or old seal-bound file was changed. The audit is separate
from the earlier Type 1 audit and has a new independent checker lineage.

## 1. Exact scope and independent algebraic branch coordinates

Work over an algebraically closed field of characteristic zero, on the
accepted degree-five A4 normalization pair (S,c) with c mapping isomorphically
to C0. Retain every nonzero delta. Under an admissible normalization projection
and a hypothetical mate in any degree, full inverse support (SUP) holds:
the reduced inverse image of C0 is exactly c, without isolated extra points.

The eight necessary conic-plus-quartic families were reconstructed in the
[residual reduction audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md),
SHA `db72f936486253cf91e82645de9c3b6b23562dac9da49eee6ee31f0cb94b5322`,
binding the owner reduction SHA
`d0efa3d74b5b8b59f9f5790b7323404765793905e3553b4e84f5ef865597fc44`.
The present families have u=x delta^2, w=3u, b=a-u, g=a-3u, d=a-4u.

The independent checker uses different algebraic coordinates from the owner:

    Type 2: epsilon^2=3, x=(epsilon+3)/6, tau=1/2,
            a=2u+(delta-delta^2)/2.
    Type 3: theta^2=3, zeta^2=6,
            tau=(theta+3)/6, x=(theta+zeta+3)/6,
            a=(6tau-1)u+tau delta-(3tau-2/3)delta^2.

For Type 2 this is equivalent to 6x^2-6x+1=0. For Type 3 the substitution
is equivalent to 6tau^2-6tau+1=0 and
3x^2-6tau x-1+3tau=0: the latter says (x-tau)^2=1/6.
Thus the reduced coefficient algebras retain all two or four branches over
an algebraically closed field; no numerical square root or selected root is
used. The tau inverse is exactly 2 for Type 2 and 6(1-tau) for Type 3.

The graph denominator is

    j=3(2x-1)delta^3.

In the independent coordinates it equals epsilon delta^3 for Type 2 and
(theta+zeta)delta^3 for Type 3. Epsilon^2=3, while
(theta+zeta)(theta-zeta)=-3. Thus j has no root for delta!=0 in any branch.
Adjoining its inverse in the checker loses no candidate, and center
avoidance is never assumed generically in place of checking an exceptional
parameter: the argument applies to any admissible center with these values.

## 2. Source curve, intrinsic contact and target contact

The actual factor reconstruction gives D=D2+D4, where

    t=(3delta^2 r^2+M r+N)/j,
    M=-(p2-3delta^2 rho), rho=tau delta,
    p2=-3u^2+(3a+3u)delta^2+3delta^3,
    N=(a/tau)delta^3,
    T=[(j+3delta^2)r^2+Mr+N]/j.

Its nonzero t quadratic coefficient makes D4 a smooth intrinsic rational
normal quartic, including its point p at infinity on the singular A4
surface. This statement is unaffected by a degree drop of T. Under (SUP),
the upstream map-degree proof gives D4 a finite birational map to the
smooth Q-curve R4 of class (3,1), hence a curve isomorphism.

At finite r the actual restricted curve ideal is (T). At p its accepted
A4 generators restrict to T/v and -r^3 T/v^2, where v=t^2-r^3 has pole four.
The ratio -r^3/v is regular and vanishes at p, so T/v generates there.
The checker proves degree T is always two or one, with all drop parameters
retained. Therefore finite intrinsic lengths total deg T, the infinity
length is 4-deg T, and total intrinsic length is exactly four.

The actual target intersection degree is C0.R4=(1,3).(3,1)=10. Under
(SUP), all ten local target lengths occur over c. The pullback of the
target ideal is contained in the reduced source ideal I_c; thus each
target length is at least its corresponding intrinsic length. The total
excess required is six. The next two sections prove the excess is at most
three without imposing a degree bound on the hypothetical mate.

## 3. Every possible finite excess and its actual higher jets

I reconstructed P,J directly from the unexpanded conormal expressions and
the actual projection derivatives. Their cubic terms vanish on these six
families; their quadratic coefficients differ by 4delta^3. Hence they
cannot both vanish identically at any retained parameter, and have at most
two common finite points for a fixed parameter.

At a finite c point with P or J nonzero, the actual target cotangent map is
surjective, including r=0 in the reversed frame. Under (SUP) the fiber is a
single point with equal residue field. The finite local Nakayama argument
in the [conormal/conductor audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md)
makes the surface projection a local isomorphism. The actual reduced curve
ideals then agree, so such a point contributes zero excess. First symbols
are used here to prove a local ring equality, not to bound later contact.

All possible finite excess belongs to the complete incidence

    I=(P,J,N4):delta^infinity,
    N4=(j+3delta^2)r^2+Mr+N.

The independent Type 2 identity is

    I=(5(delta+epsilon)^2(delta+epsilon/5),
           4r-(epsilon+2)delta-1).

The scheme has length six across both branches, including the doubled
parameter component. For each fixed delta its support has at most one
point. The independent Type 3 parameter-only eliminated ideal is exactly

    (delta^2+(2theta+4zeta)delta/3+1),

equivalent to the owner's H3. The full source incidence has length twelve
across all four branches. The actual incidence, rather than just this
parameter polynomial, is retained throughout the finite jet check.

Both independent finite algebras are explicitly checked nonzero. Only
delta and the already proved j units are inverted. On the full incidence,
r=0 is absent and X0 at the point is a unit; therefore the finite target
chart covers every possible exceptional point, without losing an opposite
frame. The actual sections Xi are directly evaluated at r=r0+e and the
graph T(r). Their Q equation holds identically, and T(r0)=0. Write

    f(e)=X0(e)^2 X2(e)-X1(e)^3.

Its constant and linear coefficients are zero in both full incidence
algebras. In Type 2 the independent exact ideal equalities are

    ([e^2]f)=(delta+epsilon),
    ([e^2]f,[e^3]f)=(1).

The intrinsic first T coefficient together with [e^2]f also generates
the unit ideal. Thus on delta=-epsilon the target order is exactly three,
the intrinsic order exactly one, and the excess exactly two. At the other
retained value delta=-epsilon/5 the target order is exactly two and excess
at most one. The second coefficient is genuinely not a unit on the whole
Type 2 incidence; its degeneration is retained, including the nonreduced
parameter component.

For Type 3, [e^2]f is a unit on the entire incidence. The actual target
order is exactly two at every exceptional finite point, hence the excess
is at most one per point. The at-most-two common-root bound gives at most
two finite excess lengths. Because X0 is a unit, dividing f by X0^3 to
obtain the actual Cartier equation of C0 on Q does not change any order.

## 4. Infinity: actual third and fourth jets retain the degree drop

Put q=1/r and W=q^2 T. Independently homogenizing the actual affine
sections gives Fi=q^4 Xi(1/q,W/q^2), with

    F0=1-2W+W^2-qW+a q^2 W,
    F1=F0-delta q(1-W)+(b-a)q^2 W,
    F2=F0-3delta q(1-W)+3delta^2 q^2-delta^3 q^3+(g-a)q^2 W,
    F3=F0-4delta q(1-W)+6delta^2 q^2-4delta^3 q^3+delta^4 q^4
          +(d-a)q^2 W.

This uses actual sections, independently of the owner's j^2-scaled
expressions. The complete delta-open coefficient algebras are explicitly
checked nonzero. F0(0)=9delta^4/j^2 is a unit, and the Q equation holds.
Let f_inf=F0^2 F2-F1^3. Its first three coefficients, through q^2, vanish.
The independently reconstructed cubic coefficient identity is

    [q^3]f_inf=54delta^9(j+3delta^2)/j^4.

Outside j+3delta^2=0 this is nonzero. T has degree two, so intrinsic order
at p is two and actual target order is three: excess one.

The complete degree-drop ideal in the delta-open algebra is

    Type 2: (delta+epsilon),
    Type 3: (delta+zeta-theta).

These are exactly the owner's delta+6x-3 and delta+6x-12tau+3 relations.
On each complete ideal the middle numerator M is a unit; no constant or
zero T stratum exists. The independent actual fourth coefficient satisfies

    [q^4]f_inf=-2delta^3 M/j
          modulo (j+3delta^2),

and is a unit there. Thus T has degree one, intrinsic order at p is three,
and actual target order is four. The excess is again exactly one. These
third/fourth-jet identities cover every nonzero delta and all six algebraic
branches; the zero cotangent determinant at p is never turned into an
unsupported later-contact bound.

## 5. Contradiction, source bindings and preserved failures

For Type 2 the complete incidence gives at most one finite excess point,
with excess at most two. For Type 3 there are at most two finite excess
points, with excess at most one each. The infinity excess is always one.
Every other intersection is at a local-isomorphism point and gives zero
excess. Total excess is therefore at most three, contradicting the six
required by the exact intrinsic and target lengths. This proves no mate
in any degree on all six families. Combining this with the already frozen
Type 1 audit excludes all eight necessary 2+4 families and therefore the
entire 2+4 residual partition in this nonendpoint normalization family.

The independent [checker](../validation/2026-10-12-type23-six-family-independent-audit/verify_type23.m2)
has final SHA-256
`33cb06e8fa2c0bc2ec44aab1992df03296254c6640008eb74891b323c77c3a5e`.
The [final captured run](../validation/2026-10-12-type23-six-family-independent-audit/attempt-05/execution-record.json)
passed 58 distinct checks, exited zero and had empty stderr. Its stdout
SHA is `be967c3ea87013ebcb4e99274fd8be52b1fa5f3c79b81d92d91686958b3031e4`.
The five saved independent development runs are one failed and four
successful executions of this single lineage. The initial run genuinely
failed its first tau-inverse assertion because my template applied the
Type 3 expression 6(1-tau) to Type 2's tau=1/2. The corrected value is 2;
that failed source and streams are retained. Subsequent successful versions
added the no-j-denominator-loss identities, exact finite degeneration and
parameter elimination, and full degree-drop ideal and nonzero-algebra
checks. They are not counted as independent proofs.

I freshly matched all eighteen source/stdout/stderr bindings of the owner's
six executions 11--16. All match. There are five exit-zero and one nonzero
executions, as claimed. The final live owner source hashes match attempts
15,16,13 respectively:

    incidence: 3e38399e9e235fb0bf99d26ecf45c7c5496ac8a159cbc6de04223b58b5907616
    finite jets: 9137a847ba2d6fa271047c0d103fe8cb62f8f451cf61f20cd367f3b4689502df
    A4 jets: 366c242c57f43cd94792c81fd0ad13c00b8b2d7f17e3635ea775c8fd3196d092

The owner's failed quotient-ring elimination call in attempt 14 and its
repaired polynomial-ring elimination in attempt 15 remain separate captures.
The Type 2 second-jet degeneration is a mathematical parameter stratum,
not a setup failure. The proof above depends on actual higher jets, exact
ideal equalities and the curve intersection count, not agreement among
agents or a generic symbolic run.
