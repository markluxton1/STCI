# Nonendpoint fibers: diagonal conormal identities and an exact degree-eight norm

Date: 2026-10-12. Author: `oct12_restricted_conductor_section/residual_norm_identity`.

Status: **DIRECT AUXILIARY POLYNOMIAL IDENTITIES, WITH A CAPTURED EXACT CHECK**.
This note supplies compact algebraic identities for the actual nonendpoint
family. It does not infer that a polynomial is the conductor merely from
its degree. A separate argument must establish the geometric status of
the five-quadric determinant. No frozen note, canonical file or Git state
is changed.

We work over an algebraically closed field of characteristic zero, with
`delta!=0`. The five actual parameters are `delta,a,B,G,J`, where

    B=b-a, G=g-3b+2a, J=d-2g+2b-a.

Here `J` is the parameter denoted `Jbar` in the conormal note; it is not
the conormal cubic. The actual source, projection-center avoidance and
finite-target equations are those of the
[target-fiber reduction](2026-10-12-session-nonendpoint-target-fiber-reduction-and-bounded-exclusions.md).
The corrected cubics and their two-chart interpretation come from the
[conormal reduction](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md).
All common-root interpretations below require the stated actual center
avoidance. Literal polynomial identities do not require that open condition.

## 1. Compact diagonal evaluations

Write

    Z=Gp(2-p)+J(3-p),
    A=(3delta^2+G)p(2-p)+J(3-p),
    b2=delta[delta^2p(p-3)+3Bp(2-p)+G(2-p)-J],
    c2=delta^2[Bp(p-3)-G],
    A2=Ar^2+b2 r+c2,
    N=delta^2(pr-delta)[3(2-p)r-delta(3-p)],
    M=delta^2[3Jr^2+delta(2G-J)r-delta^2G],
    Psi=p^2Z^2r^4+p^2Z(2r^2+r-a)N+p^2N^2-MZ
        =(pr-delta)C3.

These are literal polynomials; in particular `C3` is the exact polynomial
quotient, not a saturation or a discarded geometric component. Its
coefficient of `r^3` is `pA^2`.

For `p!=0`, set `r0=delta/p` and `Pc=p^2-6p+6`. Define

    V=(3-2p)J+p(4-3p)G+p(delta^2+Bp)Pc,
    W=3J(2-p)+2Gp(3-2p)+p(2delta^2+delta p-ap^2)Pc.

The exact diagonal identities are

    p^2 A2(r0,p)=delta^2 V,
    p^2 C3(r0,p)=delta^3 ZW.                         (1)

For the cubic identity, differentiate `Psi=(pr-delta)C3` in `r`, with
`p` fixed. On the diagonal,

    N(r0)=0,
    N_r(r0)=delta^3 Pc,
    M_r(r0)=delta^3[(6/p-1)J+2G],
    C3(r0)=Psi_r(r0)/p.

Substituting these three expressions gives (1). Differentiating once
more gives `C3_r(r0)=Psi_rr(r0)/(2p)`; this is a product-rule identity,
with no assertion about actual conductor length or a higher-contact bound.

## 2. Exact relation to the corrected conormal cubics

Denote the corrected conormal cubics by `P(r)` and `Jcub(r)`. In the
parameters used here they are

    P=Gr^3+[6delta B+delta^3-3delta^2]r^2
      +[3delta^2(a-B)+2delta^3]r-2a delta^3,
    Jcub=(G+2J)r^3+[3delta(2B+G)+5delta^3-3delta^2]r^2
      +[3(a+B)delta^2+delta^3-delta^4]r-(a+B)delta^3.

Normalize their finite-target evaluations by

    Pt=p^3 P(delta/p)/delta^3
      =G+(6B+delta^2-3delta)p+(3a-3B+2delta)p^2-2ap^3,
    Jt=p^3 Jcub(delta/p)/delta^3
      =G+2J+(6B+3G+5delta^2-3delta)p
        +(3a+3B+delta-delta^2)p^2-(a+B)p^3.

Then

    2V=-(3-p)Pt+(3-2p)Jt,
    2W=(p^2-3p-6)Pt+3(2-p)Jt.                       (2)

The determinant of the displayed two-by-two coefficient matrix is
`2p Pc`. Its possible degeneration at `Pc=0` does not produce an extra
diagonal root on the regular fiber chart `pZ!=0`. Indeed, put

    H12d=G+(3-p)(delta^2+Bp),
    H13d=J-p(2-p)(delta^2+Bp).

The additional exact identities are

    (3-p)V-(3-2p)Z=p Pc H12d,
    (2-p)V-(4-3p)Z=-Pc H13d.                        (3)

At a root of `Pc`, neither `3-p` nor `3-2p` vanishes. Thus `V=0`
forces `Z=0`, outside the stated regular chart. Equations (1)--(3)
therefore prove, everywhere on `pZ!=0`,

    A2(delta/p,p)=C3(delta/p,p)=0
      if and only if P(delta/p)=Jcub(delta/p)=0.      (4)

This includes all possible degree drops of the cubics and quadratic;
there is no normalization `delta=1` and no omission of `p=2` or `p=3`.
The targets `p=0`, `p=infinity` and the locus `Z=0` are retained separately.

## 3. A small Sylvester identity and its false leading-drop factor

Write the exact cubic as

    C3=pA^2 r^3+d2 r^2+e2 r+f2,
    K=d2-pA b2, E=e2-pA c2,
    u=A E-K b2, v=A f2-K c2.

Polynomial subtraction gives

    A C3-(pA^2 r+K)A2=u r+v.                        (5)

Consequently the fixed-degree `(2,3)` Sylvester determinant is

    Res_r(A2,C3)=c2 u^2-b2 uv+A v^2=A Rn,

where the compact polynomial is

    Rn=A c2 E^2-b2 K c2 E-A b2 E f2+b2^2 K f2
       +A^2 f2^2-2A K c2 f2+K^2 c2^2.               (6)

For example, when `A!=0`, evaluate (5) at the two roots of `A2`:
the two factors of `A` in `A C3` cancel the corresponding difference
between the cubic and linear resultant degrees. This proves the first
equality on the dense open `A!=0`, hence as a polynomial identity.
Expanding that first equality proves its factor `A` and (6).

The factor `A` really is a false common-root signal from simultaneous
leading drops, and must be divided before using this determinant on the
affine source chart. To check its removal without discarding a stratum,
put

    L=3delta^2p(2-p), n1=-delta^3(6-p^2).

The exact cubic coefficient identity is

    d2=A[p(2n1+L)+delta A]-pL^2.                    (7)

On `A=0` within `pZ!=0`, we have `Z=-L!=0`, hence `d2=-pL^2!=0`.
Thus `C3` becomes a genuine quadratic. Equation (6) specializes to

    Rn=d2*(d2 c2^2-e2 b2 c2+f2 b2^2).              (8)

If `b2!=0`, the expression in parentheses is the actual resultant of
the linear `b2 r+c2` and this quadratic. If `b2=0,c2!=0`, it is
`d2 c2^2!=0`, correctly recording no common root. If `b2=c2=0`,
the quadratic has a finite root over the algebraically closed field and
the expression vanishes, correctly retaining that case too.
Thus `Rn=0` detects actual affine common roots throughout `pZ!=0`.

Evaluating (5) on the diagonal also gives a denominator-free identity
combining the subresultant and conormal equations:

    p delta u+p^2 v
      =delta^2[A delta ZW-(delta A^2+K)V].           (9)

None of (5)--(9) bounds higher contact by first-normal data.

## 4. The primitive degree-eight polynomial

There is the exact factorization

    Rn=p^2 delta^6 Z^2 F(p),
    Res_r(A2,C3)=A p^2 delta^6 Z^2 F(p).            (10)

Here `F` is a polynomial in `QQ[delta,a,B,G,J,p]`, of formal degree
eight in `p`, with 344 monomials. Equation (6), together with (10), is a
compact definition of it; the exact divisibility is checked, not assumed.
After specialization the degree may drop. Homogenization to degree eight
retains the corresponding root at target infinity.

Since `p,delta,Z` are units on the stated chart, `F(p)=0` is equivalent
there to the existence of an affine common root of `A2,C3`, including
`A=0`. Combining this with (4), full inverse support forces every such
root to be diagonal and consequently a common conormal zero. Conversely,
a common conormal zero can coexist with an additional root. We do not
assert that a diagonal common root ensures full inverse support.

At `p=0`, let `Delta1` be the exact target-`z=1` polynomial from the
target-fiber note:

    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +J[(delta^2-5B)G-3B(delta^2+3B)]-BJ^2.

The exact boundary value is

    F(0)=-3J Delta1.                               (11)

At target infinity, write `F8` for the coefficient of `p^8`. With the
actual two endpoint polynomials

    Pinf=-delta^2r^2+(B^2-delta B+a delta^2)r+a delta B,
    Qinf=(3delta^2+G)r^2+(3delta B-delta^3)r-delta^2B,

we have

    Res_r(Pinf,Qinf)=B^2 delta^2 F8,
    F8|_(B=0)=aG[(3delta^2+G)a-delta^3].            (12)

The first expression's `B^2` factor cannot be interpreted as an actual
off-c inverse point when `B=0`. The endpoint fiber analysis must be used
there: its off-c condition is `a!=0` together with `G=0` or
`(3delta^2+G)a=delta^3`. The case `a=B=0` is also a common conormal zero
at the endpoint. Likewise (11) does not replace the complete `p=0`
fiber analysis when `J=0`. No zero-locus claim for `Z=0` follows solely
from the removed factor `Z^2`; the denominator-free rank equations in
the target-fiber note remain authoritative for that locus.

## 5. Literal identity with the five-quadric determinant

The [accepted model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
gives the actual five quadrics

    Z4^2-Z3 Z5, Z2 Z4-Z1 Z5, Z2 Z3-Z1 Z4,
    Z2^2-Z3 Z4-Z0 Z5, Z1 Z2-Z3^2-Z0 Z4.

Set the target coordinates to `(1,1-p,(1-p)^3,(1-p)^4)` and retain
the two omitted projection variables `h,z`. Use the exact linear inverse

    U3=(X0-X1+B h)/delta,
    U2=(X2-3X1+2X0-G h+delta^3 z)/(3delta^2),
    U0=(X3-2X2+2X1-X0-J h+2delta^3 z)/delta^4,
    Z0=X0-a h-U3, Z1=-U3, Z2=h-U2, Z3=U2, Z4=z, Z5=U0.

For each transformed quadric, take the coefficients of
`h^2,hz,z^2,h,z`, in that order, and place them in one row of a
five-by-five matrix. Denote its determinant, before target substitution,
by `D(X)`. The exact identity checked independently here is

    F(p)=81delta^10 D(1,1-p,(1-p)^3,(1-p)^4).        (13)

The displayed linear inverse follows directly from the actual projection
coordinates. Equation (13) is a literal polynomial identity over
`QQ[delta,a,B,G,J,delta^(-1)]`; it is independent of any presumed
conductor interpretation. The parent research lane is proving that
`D(X)` is the actual conductor quadric via the Cohen--Macaulay
presentation of the projected normalization. That proof, rather than
the degree-eight match, is the required geometric bridge.

## 6. Captured evidence, failures and boundaries

The [checker](../computations/verify_session_nonendpoint_diagonal_norm_2026_10_12.m2)
checks fifteen supporting identities and emits one completion marker.
Its final captured execution is
[20261012T212553449292Z](../validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/execution-record.json):
exit code zero, fifteen individual PASS lines, completion marker, empty
stderr. Source SHA-256 is
`cc188b7ee97b91710f519d4c357184383437b8b492aad97e09c33c3138cd99e2`.
The expanded primitive polynomial is copied into that capture.

Two earlier executions of the final checker are fully captured and
preserved. The first passed three identities before M2's fraction-field
construction changed the effective coefficient-ring context of subsequent
polynomial multiplication. The second passed fourteen identities before
M2 rejected polynomial-ring division into a fraction field over a
nonprimitive coefficient ring. Moving fraction-field construction after
the polynomial identities and multiplying by an explicitly typed inverse
of delta repaired these interface errors. These runs are not successful
fifteen-check executions.

Earlier exploratory code also encountered coefficient-extraction,
protected-symbol and factor-display interface errors. The retained source
snapshots and inventory explicitly state that their original raw tool
outputs were not separately saved to disk. They are debugging history,
not substitute successful execution certificates. The final checker is
one lineage, not fifteen independent proofs.

This auxiliary result leaves `p=0`, target infinity, `Z=0`, rank-one
fibers, actual projection-center avoidance, and all specialized degree
drops visible. It establishes no universal STCI theorem, no full
nonendpoint exclusion, and no first-normal upper bound on conductor
or higher contact multiplicities.
