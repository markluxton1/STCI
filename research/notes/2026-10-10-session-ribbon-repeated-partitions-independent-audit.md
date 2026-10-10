# Independent complete audit of the repeated contact partitions [4], [3,1], [2,2]

Date: 2026-10-10. Auditor: `oct10_repeated_coverage_audit`.
Status: **ACCEPTED AS PROVED HERE under the explicit upstream inputs**.
This independently accepts the complete coverage in
[the owner's repeated-partition proof](2026-10-09-session-ribbon-repeated-partitions-complete.md).
No parameter, endpoint, direction chart, invisible quadric coefficient, or
positive mate exponent remains uncovered within these three partitions.
This note changes no canonical state or acceptance file.

The independent exact companion is
[countercheck.m2](../validation/2026-10-10-repeated-partitions-independent-audit/countercheck.m2).
Its successful execution used Macaulay2 1.26.06, returned exit zero, and
checked 29 exact conditions. The universal ideal equalities below provide a
different certificate from the owner's selected augmented minors. The
conductor obstruction below also uses a different conic section.

## 1. Precisely what is assumed, and what is audited here

Work over an algebraically closed field `k` of characteristic zero. The
upstream inputs are:

1. `S` is a normal integral `(2,2)` complete intersection in `P4` containing
   the actual rational normal quartic
   `c=[U^4:U^3V:U^2V^2:UV^3:V^4]`.
2. Projection deletes precisely `Y2`, its center lies outside `S`, and its
   image is the fixed integral quartic carrier of `C0`. The whole inverse
   image of `C0` must have support `c` if a mate exists.
3. The Cartier double `2c` has quadratic net
   `M(d) eta=0`, where

       M(d)=[[d0,d1,d2],[d1,d2+d3,d4],[d2,d4,d5]],
       eta1^2-eta0 eta2 != 0.

   The six actual quadrics are `E0=Y0Y2-Y1^2`, `E1=Y0Y3-Y1Y2`,
   `E2=Y0Y4-Y1Y3`, `E3=Y1Y3-Y2^2`, `E4=Y1Y4-Y2Y3`, and
   `E5=Y2Y4-Y3^2`.
4. A normalized surface pencil has `d3(Q1)=1`, `d3(Q2)=0`. Its actual
   contact polynomial is

       L_C=d0 U^4-d1 U^3V-d4 UV^3+d5 V^4 != 0.

   The necessary whole-support condition is `rad(L_C) | D_Q1`, where
   `D_Q1=d0 U^4-d1 U^3V-2U^2V^2-d4 UV^3+d5 V^4`.
5. For the surviving `[2,2]` pencil, the entire conductor theorem applies:
   `Q1=-z^2+Az+R1`, `Q2=Lz+R`, downstairs conductor `(L,R)`, and upstairs
   finite flat algebra `O_Gamma[z]/(z^2-Az-R1)` with involution `z -> A-z`.
   Every mate has degree `2n` and its pullback is a scalar multiple of the
   `n`th power of the third quadric whose divisor is `2c`.

The implication of these inputs from all genus-one carriers, the separate
`[2,1,1]` proof, and the preceding exclusion of squarefree `L_C` are outside
this audit. They must be accepted separately before promoting a complete
genus-one theorem. Within the three named partitions, the inputs suffice,
and the following coverage is complete. In particular, no stronger
multiplicity divisibility of `D_Q1` by `L_C` is assumed.

## 2. Center-preserving orbit coverage

The middle coefficient of `(aU+bV)^4` is `6a^2b^2`. Hence `[4]` can occur
only at an endpoint. Reversal `Yi <-> Y_(4-i)` preserves the deleted-middle
center and exchanges endpoints; scaling `Q2` then gives `L_C=U^4`.

The middle coefficient of `(aU+bV)^3(cU+dV)` is `3ab(ad+bc)`. Distinct
linear factors give exactly two alternatives. If `ab=0`, the triple root
is an endpoint. Reversal gives `L_C=U^3(aU+bV)` with `b != 0`, including
`a=0`. If `ab != 0`, then `ad+bc=0`, both `c,d` are nonzero, and the
diagonal change `U -> -bU/a` gives a scalar multiple of
`(U-V)^3(U+V)`. These alternatives exhaust `[3,1]`.

For `[2,2]`, write `L_C=(aU^2+bUV+cV^2)^2`, with two distinct roots.
The zero middle coefficient is `b^2+2ac=0`. If `b=0`, then `ac=0` and
the quadratic would have one double root. Consequently `a,b,c` are all
nonzero. The diagonal change `U -> bU/a` gives a scalar multiple of
`q=U^2+UV-V^2/2`; its discriminant is `3`, so its roots remain distinct
and neither is an endpoint.

Every reparametrization just used is a diagonal scaling or reversal. These
induce ambient coordinate transformations that preserve the actual center
`[0:0:1:0:0]` and preserve the projected curve `C0`. No translation or
general `PGL2` change is used to classify a projection.

## 3. The entire [4] family and endpoint [3,1] family

Retaining the invisible coefficient `k`, the `[4]` second quadric is
`Q2=E0+kE2`. Its net matrix determinant is `-k^3`, so its nonzero direction
kernel forces `k=0`. The kernel has `eta0=0`; the off-conic condition forces
`eta1 != 0`, giving `eta=(0,1,lambda)` for every finite `lambda`, including
zero. The support condition at `U=0` gives `d5(Q1)=0`. The net equations
then force `d4=0`, `d2=-1`, `d1=lambda`; the free `d0` is removed by a
multiple of `Q2`. Thus every surface pencil in this family is

    <E0, lambda E1-E2+E3>.

The line `Y0=Y1=Y2=0` lies on both quadrics, and the full gradient of
`E0` vanishes at every point of that line. The Jacobian of the codimension
two complete intersection has rank at most one there. A normal surface
is regular in codimension one, so the entire line of singular points is
impossible. Reversal covers the other endpoint. This uses an actual
singular curve, not an isolated rank-drop assertion.

For endpoint-triple `[3,1]`, retain
`Q2=aE0-bE1+kE2`, `b != 0`. Its determinant is again `-k^3`. At `k=0`,
the first two rows have minor `-b^2`, so the unique direction kernel is
`eta=(0,0,1)`, which lies on the excluded intrinsic conic. This includes
the opposite-endpoint simple root and every other endpoint-triple case.

## 4. Independent complete ideal certificate for nonendpoint [3,1]

The second quadric is

    Q2=E0+2E1+kE2-2E4-E5,
    M2=[[1,2,k],[2,k,-2],[k,-2,-1]],
    det M2=-k(k^2+9).

At every determinant root the minor `-(1+k^2)` is nonzero, hence rank is
exactly two. If a kernel vector had `eta0=0`, its last two rows would give
`(k+4)eta1=0`, then `eta1=eta2=0`, since `k=-4` is not a determinant root.
Thus `eta0 != 0` at every candidate, and the chart `eta=(1,n1,n2)` covers
all three determinant roots and every direction-coordinate boundary.

Write `Q1=(a0,a1,a2,1,a4,a5)` in the `E` basis. The original net equations
and evaluations at the two support roots are exactly the ideal `I31` in
`QQ[k,n1,n2,a0,a1,a2,a4,a5]` generated by

    1+2n1+k n2,       2+k n1-2n2,       k-2n1-n2,
    a0+a1 n1+a2 n2,
    a1+(a2+1)n1+a4 n2,
    a2+a4 n1+a5 n2,
    a0-a1-2-a4+a5,    a0+a1-2+a4+a5.

The independent exact computation establishes equality, in both
directions, with the following linear ideal:

    I31 = (k, n1+1/2, n2-1, a2+1,
           a0-1-a1/2, a4+a1, a5-1+a1/2).

This proves inconsistency of both branches `k^2=-9` simultaneously,
and proves that the remaining affine solution has exactly one parameter.
It includes all invisible-coefficient values; it makes no selection of
one complex representative or one nonzero direction chart without proof.
Since this is equality over `QQ`, it remains equality after extension to
every characteristic-zero field.

Subtracting `(a1/2)Q2` from the surviving `Q1` gives

    T=E0-E2+E3+E5
     =(Y0-Y2)(Y2-Y4)-(Y1-Y3)^2.

Both `T` and `Q2` vanish identically on the line `Y0=Y2=Y4`, `Y1=Y3`.
The full gradient of `T` vanishes there. The same codimension-one
singularity argument excludes normality. All of `[3,1]` is excluded.

For completeness, the off-conic discriminant at the three determinant
roots is nonzero: its numerator is `k^4+6k^2-3`, which is `-3` at `k=0`
and `24` at `k^2=-9`. Thus the hidden branches were not illegitimately
discarded by a direction discriminant condition.

## 5. Independent complete ideal certificate for [2,2]

The second quadric and matrix are

    Q2=E0-2E1+kE2+E4+E5/4,
    M2=[[1,-2,k],[-2,k,1],[k,1,1/4]],
    det M2=-(2k+1)(2k^2-k+8)/4.

The minor `k/4-1` is nonzero at all three determinant roots, proving rank
two. If `eta0=0`, the remaining kernel equations force both
`(k+1/2)eta2=0` and `(1-k/4)eta2=0`. These coefficients generate the unit
ideal, so `eta2=eta1=0`. Again `eta=(1,n1,n2)` covers all possible kernels,
including the essential boundary `eta1=0` at `k=-1/2`.

With the same general `Q1` coefficients, the full net and support ideal is

    I22 = (1-2n1+k n2, -2+k n1+n2, k+n1+n2/4,
           a0+a1 n1+a2 n2,
           a1+(a2+1)n1+a4 n2,
           a2+a4 n1+a5 n2,
           -a1-6a4+16a5-4, a0-4a4+12a5-4).

The last two equations are precisely the remainder of `D_Q1(1,t)` modulo
`1+t-t^2/2`; the two roots are finite, so no infinity root is omitted.
The independent exact computation proves the complete ideal equality

    I22 = (k+1/2, n1, n2-2, a0-4a5,
           a1-2+8a5, a2+2a5, a4+1-4a5).

Consequently both roots of `2k^2-k+8` are inconsistent, and the entire
remaining affine family has exactly one parameter. Subtracting `4a5 Q2`
gives the unique surface pencil

    Q1=2E1+E3-E4,
    Q2=E0-2E1-E2/2+E4+E5/4,
    eta=(1,0,2).

The discriminant of this direction is `-2`. At the other determinant
roots the owner's unnormalized discriminant is
`(k-1)(k^2+k+7)/4`; modulo `2k^2-k+8`, its factors reduce to nonzero
multiples of `k-1` and `k+2`, neither of which vanishes there. Thus every
candidate direction has been explicitly accounted for.

## 6. The actual conductor and an independent obstruction for every power

The third quadric `Q=E3` is independent of this pencil in its net. By the
stated ribbon input, its divisor on `S` is exactly `2c`. Put `z=Y2` and
use retained coordinates `(x0,x1,x2,x3)`. Literal expansion gives

    A=-2x1+x2,             R1=2x0x2+x1x2-x1x3,
    L=x0+2x1-x2+x3/4,
    R=-x1^2-2x0x2-(x0x3-x1x2)/2+x1x3-x2^2/4,
    Q|S=ell z+q,           ell=2x1-x2, q=-2x0x2+x1x3.

The independent checker verifies the reduction sign before using it.
The actual entire conductor is `Gamma=V(L,R)`. Eliminating `x0` gives

    Rc=-x1^2+(9/2)x1x2+2x1x3-(9/4)x2^2+x3^2/8.

Its symmetric matrix has determinant `243/128`, so `Gamma` is a smooth
integral conic. In its finite flat quadratic upstairs algebra the trace
and norm of `Q` are

    T=2q+A ell,             N=q^2+Aq ell-R1 ell^2.

Unlike the owner's `x2=0` slice, use `x1=0`, `x3=1`, `x2=t`. The conductor
equation becomes `18t^2-1=0`. In its quotient ring,

    T=t-5/18,              N=(t/2-1/9)^2,
    T^2/N=22+72t.

The two roots of `18t^2-1` are distinct, and `N` is nonzero at both. The
ratio has two different values, so it is nonconstant on the integral
conic. The generic quadratic discriminant is nonzero as well, checked
already at both points of this independent section.

Suppose `Q^n` descended for any `n>0`. On the generic quadratic conductor
algebra, `Q` is a unit because `N != 0`, and
`rho=sigma(Q)/Q` satisfies `rho^n=1`. A nonsplit quadratic field has all
such roots of unity in the algebraically closed constant field `k`. In
the split algebra the two roots of unity are reciprocal, because
`sigma(rho)=rho^(-1)`. In either case

    T^2/N=2+rho+rho^(-1)

would be constant, contradicting the independent section calculation.
Thus no positive power descends, with no bound on `n` and no assumption
that the conductor cover is irreducible. The mate hypothesis identifies
its pullback with a scalar multiple of `Q^n`, so this unique `[2,2]` pencil
admits no mate in any degree. Combined with the complete ideal reduction,
all of `[2,2]` is excluded.

No even-valuation assertion at surface singularities, reduced-only
conductor replacement, or isolated differential rank-drop claim is used.

## 7. Computation record and failures

The initial proposed Python countercheck could not import SymPy from the
historical CAS virtual environment. Read-only checks also found no SymPy
in Homebrew Python 3.12/3.14 or the bundled Codex Python. No dependency was
installed. The import-failed proposed source is retained as `countercheck.py`;
it is not claimed as a passing certificate.

The M2 reconstruction had two scaffolding failures: the first used the
protected name `check`; the second needed parentheses around a `sub(...)`
call before exponentiation. Neither failure contradicted a mathematical
assertion. The second run had already verified the two full universal
ideal equalities and all singular-line checks before the parser failure.
Both failed source versions and the observed errors are retained in the
isolated audit directory. The namespace version was mechanically
reconstructed from the preserved parser-failed version, and is labeled
as such rather than as a source snapshot made before that run.

The final command was

    /opt/homebrew/bin/M2 --script research/validation/2026-10-10-repeated-partitions-independent-audit/countercheck.m2

It returned exit `0`, tool chunk `d3531b`, wall time `0.533071458` seconds,
and `PASS: 29 independent exact conditions`. Its generated
[result.json](../validation/2026-10-10-repeated-partitions-independent-audit/result.json)
contains the bounded scope and independent conductor section. The
[execution record](../validation/2026-10-10-repeated-partitions-independent-audit/execution-record.json)
binds source, output, input note, and owner-checker hashes. These checks
support the explicit argument above; their passing status does not itself
prove any upstream geometric hypothesis or the universal STCI question.

The assigned audit is complete. Promotion of all genus-one quartic
carriers still requires the separate upstream/interface and `[2,1,1]`
audit; this note makes no canonical promotion.
