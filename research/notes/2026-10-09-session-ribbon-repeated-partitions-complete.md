# Complete exclusion of contact partitions [4], [3,1], and [2,2]

Date: 2026-10-09. Author: `ribbon_repeated_root_strata`.
Status: **PROVED HERE conditional on the accepted genus-one ribbon-net
and entire-conductor reductions**. This note covers every parameter in
these three contact partitions, including parameter endpoints, every
direction-coordinate boundary, and all values of the coefficient invisible
to the omitted-coordinate derivative. It edits no canonical frontier file.
The unrestricted STCI problem is not resolved by this bounded theorem.

The inputs are the
[independent ribbon-net proof](2026-10-09-session-genus-one-ribbon-net-independent-audit.md),
[actual-coordinate full-fiber conditions](2026-10-09-session-genus-one-uniform-projection-adversarial.md),
and [entire conductor calculation](2026-10-09-session-genus-one-entire-conductor.md).
The separate [partition [2,1,1] proof](2026-10-09-session-ribbon-211-projection-independent-audit.md)
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
[root proof of [4]](2026-10-09-session-ribbon-4-root-independent-proof.md),
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

The [root's bounded [2,2] proof](2026-10-09-session-ribbon-22-bounded-power-obstruction.md)
was read and independently accepted here. Its separate quotient-ring
certificate has coefficients `(114,336)` for `T^2` and `(1,4)` for `N`,
with nonzero minor 120. The two-point calculation above supplies a
different exact verification. Neither proof imposes an unjustified
even-valuation claim at singular normalization points or uses the
isolated-rank-one differential obstruction.

## 6. Evidence, dependency boundary, and completion status

The exact companion
[verify_session_ribbon_repeated_partitions_2026_10_09.py](../computations/verify_session_ribbon_repeated_partitions_2026_10_09.py)
checks 72 identities. Its terminal replay returned exit zero and `PASS`
on 2026-10-09, wall time `0.679139` seconds, with source SHA256
`25a0ffcc2d4d46f1fec158ed6bde86b1b939725fe9396a57446e1c6ff4d182d8`.
The JSON record is
[session-ribbon-repeated-partitions-2026-10-09.json](../scratch/session-ribbon-repeated-partitions-2026-10-09.json).

The checks verify the literal RNC ideal, omitted-coordinate derivative,
center-preserving reversal, every determinant and direction kernel,
both augmented-system exclusions, complete remaining affine solution
families, both actual singular lines, and the entire-conductor
trace/norm certificate. They are exact identities supporting the
preceding proofs; a `PASS` does not replace their geometric reasoning.

The independent helper `single_triple_root_linear_check` supplied the
[4] and [3,1] algebra before hitting the account usage limit; it did not
save a finished note. This owner reconstructed all its formulas, kept
the omitted `E2` coefficient, and verified them in the durable source
above. No helper-final success or unsaved assertion is used as proof.

The exact bounded task is complete: **[4], [3,1], and [2,2] all excluded
under the stated accepted inputs**. The next reviewing step is an
independent audit of the exhaustiveness of these three reductions and
its integration with the separate [2,1,1] proof. This note itself makes
no canonical promotion and no claim about genus-two normalizations,
higher quartic ancestors, arbitrary higher carrier degrees, or the
universal STCI question.
