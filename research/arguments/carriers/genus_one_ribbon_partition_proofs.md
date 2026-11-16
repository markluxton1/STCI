# Genus-one ribbon: repeated-contact partition exclusions

The [ribbon conormal-net proof](genus_one_ribbon_conormal_net_proof.md) and [uniform projection conditions](genus_one_uniform_projection_analysis.md) are upstream assumptions. This proof treats the repeated-contact partitions **[4], [3,1], and [2,2]**, including endpoints and direction boundaries, and does not claim to handle the distinct [2,1,1] stratum. Its [independent certificate](#genus-one-ribbon-repeated-partition-independent-certificates) checks coverage and conductor/power obstructions with exact ideal computations. Retain the original case calculations and the independent audit as distinct evidence, not interchangeable summaries.

---

Permanent detailed mathematical record, including all proofs, calculations, counterexamples and explicit unresolved conditions.

Date: 2026-10-09. Author: `ribbon_repeated_root_strata`.
Status: **PROVED HERE conditional on the accepted genus-one ribbon-net
and entire-conductor reductions**. This note covers every parameter in
these three contact partitions, including parameter endpoints, every
direction-coordinate boundary, and all values of the coefficient invisible
to the omitted-coordinate derivative. It edits no frontier file.
The unrestricted STCI problem is not resolved by this bounded theorem.

The inputs are the
[independent ribbon-net proof](genus_one_ribbon_conormal_net_proof.md),
[actual-coordinate full-fiber conditions](genus_one_uniform_projection_analysis.md),
and [entire conductor calculation](../../frameworks/carrier-normalization/quartic_proof_interfaces.md).
The separate [partition [2,1,1] proof](GENUS_ONE_211_PROJECTION_PROOF.md)
is outside this note's independently computed coverage. Combining all four
partitions requires accepting that separate proof and the preceding inputs;
agreement between owners is not the proof.

## 1. Exact coordinates and the necessary conditions

Work over an algebraically closed field of characteristic zero. A
hypothetical genus-one quartic carrier has an integral normal complete
intersection surface `S` in `P4`, containing the smooth rational normal
quartic

    c=[U^4:U^3V:U^2V^2:UV^3:V^4].

Its projection to the fixed `C0` deletes `Y2`, and the projection center
`[0:0:1:0:0]` lies outside `S`. Use the actual quadrics

    E0=Y0Y2-Y1^2,       E1=Y0Y3-Y1Y2,
    E2=Y0Y4-Y1Y3,       E3=Y1Y3-Y2^2,
    E4=Y1Y4-Y2Y3,       E5=Y2Y4-Y3^2.

The accepted Cartier double `2c` is a complete-intersection ribbon. Its
quadratic net has the equations

    M(d) eta=0,
    M(d)=[[d0,d1,d2],[d1,d2+d3,d4],[d2,d4,d5]],
    eta=(eta0,eta1,eta2),       eta1^2-eta0 eta2 != 0.

The discriminant-zero directions have a cubic surface as net base locus
and cannot define the assumed integral degree-four surface. The matrix
equations above therefore cover all permitted direction charts.

Normalize the surface pencil so that `Q2` has `d3=0` and `Q1` has `d3=1`.
This is possible because its omitted-coordinate square coefficient is
nonzero for some member, as the center lies outside `S`. On `c` the
omitted-coordinate derivative of any quadric is

    D_d=d0 U^4-d1 U^3V-2d3 U^2V^2-d4 UV^3+d5 V^4.

Thus `L=D_Q2` is a nonzero binary quartic with zero middle coefficient.
The full inverse-support condition for a mate gives

    rad(L) divides D_Q1.

This is support divisibility. No stronger multiplicity divisibility is
assumed. The coefficient `d2` is invisible in this derivative and must
remain in the matrix equations; discarding it would lose algebraic
branches in both [3,1] and [2,2].

Only diagonal reparametrizations and coordinate reversal are used below.
They preserve the actual omitted-middle center. An arbitrary `PGL2`
reparametrization would move that center and is not used for the
projection classification.

## 2. Partition [4]: both endpoints and every direction

Write `L=(aU+bV)^4`, up to a nonzero scalar. Its missing middle
coefficient is `6a^2b^2`, so `ab=0`. Its unique root is a parameter
endpoint. Coordinate reversal `Yi <-> Y_(4-i)` fixes the deleted-middle
center and exchanges the two endpoints. It suffices to normalize `L=U^4`.

Keep the invisible coefficient `k`: then

    Q2=E0+kE2,
    det M(Q2)=-k^3.

The nonzero direction kernel forces `k=0`. Hence `eta0=0`, and the
off-conic condition gives `eta1!=0`. Scale it to one and write
`eta=(0,1,lambda)`, with every `lambda`, including zero, retained.

The singleton condition at `U=0` gives `d5(Q1)=0`. The net equations then
give `d4=0`, `d2=-1`, `d1=lambda`, while `d0` is free. Subtracting its
multiple of `Q2`, the pencil is

    Q2=E0,       Q1=lambda E1-E2+E3.

Both quadrics vanish on the line `Y0=Y1=Y2=0`. The gradient of `Q2` is
identically zero on that line. The complete intersection is singular
along a curve, contradicting normality of `S`. Reversal covers the other
endpoint. This proves exclusion of all of [4].

This reconstruction independently agrees with the
[technical proof of the single root of order four](../../frameworks/carrier-normalization/quartic_proof_interfaces.md),
which was read and accepted here. No isolated-ramification assertion is
used: the singular locus contains an actual entire line.

## 3. Partition [3,1]: endpoints and the hidden algebraic branches

Write `L=(aU+bV)^3(cU+dV)` with independent linear factors. Its middle
coefficient is

    3ab(ad+bc).

If the triple root is an endpoint, reversal allows
`L=U^3(aU+bV)` with `b!=0`. Then

    Q2=aE0-bE1+kE2,
    det M(Q2)=-k^3.

The determinant forces `k=0`. The first two rows have the nonzero minor
`-b^2`, so the kernel is exactly `eta=(0,0,1)`. That direction lies on
the excluded intrinsic conic. This includes the opposite-endpoint simple
root `a=0` and all other endpoint-triple cases.

If the triple root is not an endpoint, both `a,b` are nonzero and the
middle-coefficient condition gives `ad+bc=0`. Both simple-root coefficients
are then nonzero too. A diagonal change, preserving the projection center,
normalizes the quartic to

    L=(U-V)^3(U+V).

Retaining the invisible coefficient gives

    Q2=E0+2E1+kE2-2E4-E5,
    det M(Q2)=-k(k^2+9).

At every one of these three determinant roots the matrix has rank two:
the minor `-(1+k^2)` never vanishes there. Its entire unique direction
kernel is represented polynomially by

    eta=(A,B,C)=(2(1-k),-(1+k^2),2(1+k)).

This vector does not vanish anywhere on the determinant locus, and its
intrinsic discriminant `k^4+6k^2-3` is nonzero there. Thus neither
discarding a direction chart nor appealing to the off-conic condition
removes the two roots `k^2=-9`; those roots must be checked directly.

The necessary support condition is divisibility by `U^2-V^2`. For
`d3(Q1)=1` it makes the general first coefficient vector

    Q1=(a,b,g,1,-b,2-a).

The remaining net equations are the three-by-three affine system

    N (a,b,g)^t=(0,-B,-2C)^t,
    N=[[A,B,C],[0,A-C,B],[-C,-B,A]].

Its determinant and the third entry of its adjugate times the right side are

    det N=-4k(k^2+1)(k^2+9),
    (adj(N) rhs)_3=4k(k^2-3)^2.

On the determinant locus, the latter reduces to `576k`. Consistency
therefore forces `k=0`, including exclusion of both roots `k^2=-9`.

At `k=0`, the entire affine solution is

    (a,b,g)=(b/2+1,b,-1).

After subtracting `(b/2)Q2`, the pencil contains

    T=E0-E2+E3+E5
     =(Y0-Y2)(Y2-Y4)-(Y1-Y3)^2.

The singular line of this rank-three quadric is

    Y0=Y2=Y4,       Y1=Y3.

`Q2` vanishes identically on this entire line. The complete intersection
is singular along it and cannot be normal. This excludes all of [3,1].

The endpoint and nonendpoint branches together are exhaustive because
the displayed middle-coefficient equation has exactly those alternatives.
No parameter or direction-coordinate boundary is omitted.

## 4. Partition [2,2]: complete reduction to one pencil

Write `L=q^2`, up to a nonzero scalar, where
`q=aU^2+bUV+cV^2` has two distinct roots. Its missing middle coefficient
is `b^2+2ac=0`. If `b=0`, this would force `ac=0` and make `q` have only
one root, contradicting this partition. Thus all of `a,b,c` are nonzero.
Changing `U` diagonally by `b/a` and rescaling `q` gives

    q=U^2+UV-V^2/2,       L=q^2.

This transformation preserves the actual middle-coordinate center and
covers every [2,2] quartic. The normalized `q` has discriminant three,
so its two roots remain distinct; neither is an endpoint.

Keep the invisible coefficient `x`. The complete second quadric is

    Q2=E0-2E1+xE2+E4+E5/4,
    M(Q2)=[[1,-2,x],[-2,x,1],[x,1,1/4]],
    det M(Q2)=-(2x+1)(2x^2-x+8)/4.

Its adjugate first column is

    eta=(x/4-1,x+1/2,-x^2-2).

The first entry is nonzero at every determinant root, since `x=4` is
not such a root. Thus the matrix has rank exactly two there and this
column covers the entire unique kernel. Its off-conic discriminant is
`(x-1)(x^2+x+7)/4` and is nonzero at all three roots. In particular the
boundary `eta1=0` at `x=-1/2` is retained explicitly.

Write the normalized first quadric coefficients as
`(a0,a1,a2,1,a4,a5)`. Dividing its omitted-coordinate derivative by
`q(1,t)=1+t-t^2/2`, the two remainder equations are

    -a1-6a4+16a5=4,
    a0-4a4+12a5=4.

Together with `M(Q1) eta=0`, these form a five-by-five affine linear
system `A v=rhs`, in the ordered variables `(a0,a1,a2,a4,a5)`. On
`2x^2-x+8=0` its determinant vanishes, whereas the augmented minor
using columns `(a1,a2,a4,a5,rhs)` is

    -243x/4   modulo 2x^2-x+8.

The two roots are nonzero, so both hidden algebraic branches are
inconsistent. This is an exact certificate at both roots, rather than
a test at one complex numerical approximation.

At the remaining root `x=-1/2`, the coefficient matrix has rank four
and the entire solution family is

    (a0,a1,a2,a4,a5)=(4a5,2-8a5,-2a5,4a5-1,a5).

After subtracting `4a5 Q2`, the unique remaining surface pencil is

    Q1=2E1+E3-E4,
    Q2=E0-2E1-E2/2+E4+E5/4,
    eta=(1,0,2).

This completes the reduction, including every coefficient boundary.
Unlike [4] and [3,1], this pencil cannot be dismissed merely by the
singleton-fiber test. It requires actual conductor descent.

## 5. The sole [2,2] pencil has no descending power

Write retained coordinates `(x0,x1,x2,x3)` and `z=Y2`. The displayed
surface equations are

    Q1=-z^2+A z+R1,       Q2=Lz+R,
    A=-2x1+x2,
    R1=2x0x2+x1x2-x1x3,
    L=x0+2x1-x2+x3/4,
    R=-x1^2-2x0x2-(x0x3-x1x2)/2+x1x3-x2^2/4.

The third quadric `Q=E3` is independent of the surface pencil in the
net `eta=(1,0,2)`. By the accepted ribbon-net theorem its divisor on
the normal surface is exactly `2c`. Modulo `Q1`, it is

    Q=ell z+q,       ell=2x1-x2,       q=-2x0x2+x1x3.

The entire downstairs conductor is the conic `Gamma=V(L,R)`. Substituting
`x0=-2x1+x2-x3/4` gives

    R_Gamma=-x1^2+(9/2)x1x2+2x1x3-(9/4)x2^2+x3^2/8.

Its symmetric matrix has determinant `243/128`, so it is a smooth
integral conic. The entire upstairs conductor is the finite flat
quadratic algebra

    O_Gamma[z]/(z^2-Az-R1),       sigma(z)=A-z.

Its generic discriminant `A^2+4R1` is nonzero, so its generic algebra
is either a quadratic field extension or a split étale algebra. The
trace and norm of `Q` in it are

    T=2q+A ell,       N=q^2+Aq ell-R1 ell^2.

Here is a certificate independent of the root's coefficient minor.
Restrict `Gamma` to `x2=0`, `x3=1`, and put `x1=a`. The two points
satisfy

    a^2-2a-1/8=0.

At both points, `N=a^2!=0` and `T=a(-4a+2)`. Consequently

    T^2/N=(-4a+2)^2=16a+6

modulo that quadratic. Its roots are distinct, of discriminant `9/2`,
and the displayed linear coefficient is nonzero. Thus `T^2/N` takes
two distinct values and is not constant on `Gamma`. Equivalently the
two values are `22+12 sqrt(2)` and `22-12 sqrt(2)`.

If any positive power `Q^n` descended to the quartic, its restriction
to the actual conductor would be fixed by `sigma`. In the generic
quadratic algebra `N!=0`, so `rho=sigma(Q)/Q` is a unit and satisfies
`rho^n=1`. In a quadratic field its root of unity belongs to `k`; in a
split algebra its two values are roots of unity exchanged with their
reciprocals. In either case

    T^2/N=2+rho+rho^(-1)

is constant over `k`. This contradicts the two-point certificate.
The argument treats every exponent, including arbitrarily large ones,
and does not assume the conductor cover is irreducible.

The preceding D5 torsion reduction requires every hypothetical mate to
have even degree `2n`. Its pullback has divisor `2nc`, so it is a scalar
multiple of `Q^n`: the quotient has zero Weil divisor on the normal
projective integral surface and is a constant global unit. Thus no mate
of any degree exists for this last pencil. This excludes all of [2,2].

The [root's bounded [2,2] proof](GENUS_ONE_RIBBON_PARTITION_PROOFS.md)
was read and independently accepted here. Its separate quotient-ring
certificate has coefficients `(114,336)` for `T^2` and `(1,4)` for `N`,
with nonzero minor 120. The two-point calculation above supplies a
different exact verification. Neither proof imposes an unjustified
even-valuation claim at singular normalization points or uses the
isolated-rank-one differential obstruction.

## 6. Evidence, dependency boundary, and completion status

The exact companion
[verify_session_ribbon_repeated_partitions_2026_10_09.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_ribbon_repeated_partitions_2026_10_09.py)
contains the 72 exact identity checks supporting this proof.

The checks verify the literal RNC ideal, omitted-coordinate derivative,
center-preserving reversal, every determinant and direction kernel,
both augmented-system exclusions, complete remaining affine solution
families, both actual singular lines, and the entire-conductor
trace/norm certificate. They are exact identities supporting the
preceding proofs; a `PASS` does not replace their geometric reasoning.

The exact bounded task is complete: **[4], [3,1], and [2,2] all excluded
under the stated accepted inputs**. The independent ideal and conductor certificates below supplement the main proof; the separate [2,1,1] case is treated in its focused argument. This note itself makes
no claim about genus-two normalizations,
higher quartic ancestors, arbitrary higher carrier degrees, or the
universal STCI question.



## Independent ideal and conductor certificates

These complementary calculations check the nonendpoint [3,1] ideal, the [2,2] ideal, and all-power conductor descent without replacing the geometric argument above. They assume the same characteristic-zero ADE del Pezzo projection and complete conormal net.

### 4. Independent complete ideal certificate for nonendpoint [3,1]

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

### 5. Independent complete ideal certificate for [2,2]

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

### 6. The actual conductor and an independent obstruction for every power

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

