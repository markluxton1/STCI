# Degree-one moving linear relations: the cubic obstruction

Date: 2026-10-14. Status: new exact cubic calculation, independently accepted in the
[sign/frame audit](2026-10-14-moving-linear-cubic-independent-audit.md). The accepted embedded chart and the independently established
quadratic obstruction locus are premises; neither is re-audited here.

The calculation below eliminates the nonquadric members of the quadratic
obstruction-zero locus. Precisely, among basepoint-free moving linear relation
lines `O(-8) -> N_C0^*=O(-7)^2`, the only line admitting a compatible relation
through cubic normal degree is the line of the actual quadric. This is a
classification of the specified relation-lifting problem. A relation with
torsion or poles, a first relation of higher order, and an additional relation
in the relevant degree are separate problems.

## 1. Accepted inputs and the next target

Use the frames and coefficients from the [independent quadratic
audit](2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md):

    a=A+Cz, b=B+Dz, Delta=AD-BC != 0,
    f0=a u+b v,
    f1=(Aw+C)u'+(Bw+D)v'.

The relation line is `W=O(-8)` and its quotient is `M=O(-6)`. The quotient is
normalized by `(u,v) -> (b,-a)q`; on the other chart its frame is
`q1=z^-6 q0`. The next relation obstruction therefore lies in

    Hom(W,Sym^3 M)=O(-10).

In the chart-zero frame, its Cech class retains exactly the coefficients of
`z^-1,...,z^-9`. Nonnegative exponents and exponents at most `-10` are
coboundaries. There is no extra power of `z` after evaluating a cubic expression
at `(u,v)=(b,-a)`.

The accepted quadratic class vanishes precisely at the three diagonal points

    [A:B:C:D]=[t:0:0:1],
    (t-2)(3t^2-4t+12)=0,

and on the open conic

    A=2D, BC=8D^2, D!=0.

The conic is normalized below by `D=1, B=t, C=8/t`, with `t!=0`.

## 2. Canonical quadratic correction and the unit term

Let `T` be the accepted quadratic discrepancy evaluated at `(b,-a)`. On its
obstruction-zero locus, split it uniquely as

    T=T_plus+T_minus,
    supp(T_plus) contained in {0,1,...},
    supp(T_minus) contained in {...,-5,-4}.

There is no remaining quotient-level quadratic lifting freedom because
`H^0(O(-4))=0`. Define

    ell0=(-C u-D v)/Delta,
    ell1=(A u'+B v')/Delta,
    q0=T_plus,
    q1(w)=-z^4 T_minus(z),
    F0=f0+q0 ell0^2,
    F1=f1+q1(w)ell1^2.

On the reduced curve, `ell0(b,-a)=1`. On the other chart the corresponding
evaluation is `ell1=z^-6` in the first quotient frame. Consequently the
quadratic part of `z^8 F1-F0` evaluates to zero. The coefficient pair `(a,b)`
is unimodular, so this part is exactly divisible by the relation:

    [z^8 F1-F0]_2=f0 L2,

where `L2` has normal degree one. The degree-one term of the unit comparing
the two local generators is thus `L2`. Its contribution in degree three is
`L2 q0 ell0^2`. The evaluated cubic remainder is

    R=[z^8 F1-F0]_3(b,-a)-q0 L2(b,-a).

Local additions to either quadratic correction that are multiples of `f`
change the local generator by a unit. They change the cubic calculation by
the corresponding unit contribution and a cubic coboundary. Thus they do not
introduce another compatibility parameter. The unspecified degree-two term
of the comparison unit multiplies `f0` and vanishes in the quotient.

## 3. Exact chart calculation

The accepted chart is expanded only through normal degree three:

    b_orig=u+(3/2)zv, a_orig=v,
    inv=(z^4+b_orig)^-1,
    W=(z^3+v)inv,
    a'=z inv-W^3,
    b'=inv-W^4,
    u'=a'/2,
    v'=-3W a'+2b'.

In the second-chart corrections above, the coefficient variable `w` is
substituted by the actual `W`, including its normal terms. In particular,
the derivative of `q1(w)` is retained. The source uses the exact finite series

    inv=sum_(j=0)^3 (-b_orig)^j z^(-4j-4) modulo (u,v)^4.

All arithmetic uses `fractions.Fraction`, sparse Laurent polynomials in `t,z`,
and truncation only in the normal variables `u,v`. There is no sampling,
floating-point calculation, or generic-parameter saturation. The two nonreal
diagonal points are handled together in the exact field
`Q[t]/(3t^2-4t+12)`; negative powers of `t` use
`t^-1=1/3-t/4` there.

At the accepted quadric point `t=2`, both quadratic corrections vanish and

    L2(b,-a)=4 z^-3,
    [R]=0 in H^1(O(-10)).

The actual quadric equation is an accepted all-orders lift.

At either other diagonal point,

    q0=q1=0,
    L2(b,-a)=(2t-4)z^-3,
    [R]=(64/27)(3-t)z^-5.

Since `3t^2-4t+12` has value `27` at `t=3`, this cohomology class is nonzero
at both points. Thus neither diagonal relation extends compatibly through
cubic normal degree.

On the entire open conic, the exact corrections are

    q0=-96/t^2-192z/t^3,
    q1(w)=-6t^2-3t^3 w.

The comparison-unit evaluation is

    L2(b,-a)=64/t^3+16z^-1/t^2+20z^-2/t+4z^-3
                 -3t z^-4+t^2 z^-5+t^3 z^-6.

Its cubic class is exactly

    [R]=512z^-1/t^4-384z^-2/t^3+64z^-3/t^2
           +4t^2 z^-7-6t^3 z^-8+2t^4 z^-9.

The `z^-1` coefficient is nonzero for every allowed `t`. Hence no member of
the open conic extends through cubic normal degree. The points in the conic's
closure with `D=0` have `Delta=0`, so they are outside the basepoint-free
degree-one relation problem and are not discarded by a saturation here.

## 4. Conclusion and scope

The complete basepoint-free degree-one quadratic zero locus has now been
tested in the next normal degree. Only the actual quadric relation survives.
Equivalently, a primitive length-four structure on `C0` with a single
compatible relation line `O(-8)` and quotient conormal `O(-6)` must use the
quadric relation line. This statement fixes the line, not an arbitrary
higher-order thickening or an STCI presentation.

For a moving linear relation of movement degree `e`, the cubic target is
generally `O(4e-14)`. The new calculation concerns `e=1`; it does not exclude
`e=2` or `e=3`, whose cubic cohomology can still be nonzero, or `e>=4`, for
which this particular cohomology group vanishes. It also does not justify
taking an `r`th root of a higher-order pure-power first relation.

A useful further consequence concerns an actual primitive length-four
structure `Y` with this first quotient conormal, rather than a formal relation
alone. The relation's quotient-level corrections in degrees two and three
are unique once they exist: the differences of two compatible lifts are
sections of `Hom(W,Sym^j M)=O(8-6j)`, which have no global sections for
`j=2,3`. Multiples of the relation merely change its local generators.
Therefore the compatible ideal of `Y` modulo `I_C0^4` agrees with that of
the accepted actual quadric, and its quadric equation lies in `I_Y`.

In particular, if `Y` is the full symbolic length-four structure on an
integral normal degree-eight carrier, then the quadric section vanishes to
order at least four along `C0`. Its complete-intersection cycle has degree
`2*8=4*4`. There is no residual curve and no isolated component, because the
ambient complete intersection is pure. The quadric and that carrier would
have set-theoretic intersection `C0`, contradicting the accepted low-carrier
exclusion. Thus a normal degree-eight carrier cannot have an everywhere
primitive symbolic quadruple with free conormal `O(-6)`. This uses the full
symbolic quadruple hypothesis, not merely its generic first symbol.

The exact [new computation](../computations/moving_linear_cubic_compatibility_2026_10_14.py)
and [full coefficient output](../validation/2026-10-14-moving-linear-cubic/cubic-results.json)
preserve the complete discrepancy and the retained obstruction for all three
strata. No inherited accepted computation was rerun.
