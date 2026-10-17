# Independent audit of the degree-one moving linear cubic obstruction

Date: 2026-10-14. Status: **PASS**, exact independent derivation of the new
cubic calculation. The accepted embedded chart and [quadratic
audit](2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md)
are premises. Their earlier computations were not re-audited. The owner's
[cubic note](2026-10-14-moving-linear-cubic-compatibility.md) was first read
after this audit's separate expansion had produced its answer.

## 1. Frame and correction signs

Write `W=O(-8)`, `M=O(-6)`,

    a=A+Cz, b=B+Dz, Delta=AD-BC != 0,
    f0=a u+b v,
    f1=(Aw+C)u'+(Bw+D)v'.

On the reduced overlap the quotient frame transforms by `q1=z^-6 q0`,
whereas the relation frame transforms by `W1=z^-8 W0`. Consequently the
cubic target is `Hom(W,Sym^3 M)=O(-10)`. Its first-chart coefficient is
obtained by evaluating at `(u,v)=(b,-a)`, with no additional factor of `z`.
Exactly `z^-1,...,z^-9` survive in its Cech cohomology; exponents at least
zero and at most `-10` are coboundaries.

Let `T` denote the accepted evaluated quadratic discrepancy. On its zero
locus write `T=T_plus+T_minus`, with exponent supports at least zero and
at most `-4`, respectively. Set

    ell0=(-C u-D v)/Delta,
    ell1=(A u'+B v')/Delta,
    q0=T_plus,
    q1(w)=-z^4 T_minus(z),
    F0=f0+q0 ell0^2,
    F1=f1+q1(w)ell1^2.

The quotient evaluations are `ell0=1` and `ell1=z^-6`. Thus the second
degree quotient discrepancy is `T+z^-4 q1-q0=0`; this fixes both correction
signs. The remaining second-degree expression is `f0 L2`. The gluing unit
therefore has first normal term `L2`, and

    z^8 F1=(1+L2+L3)F0 modulo normal degree four.

After evaluating in the quotient, the third-degree remainder is precisely

    R=[z^8 F1-F0]_3(b,-a)-q0 L2(b,-a).

The minus sign comes from the third-degree product `L2 q0 ell0^2`.
The term `L3 f0` vanishes in the quotient.

## 2. Independent expansion method and exact output

The independent source changes normal variables before expanding:

    u=b e+(D/Delta) h,
    v=-a e-(C/Delta) h.

Then `f0=h` and `ell0=e` exactly. In particular the coefficient of `e h`
in the second-degree overlap is directly `L2(b,-a)`. This avoids copying
the owner's binary-polynomial division or cubic output.

Put `p=u+(3/2)zv` and `k=u+(1/2)zv`. Direct expansion of the exact embedded
chart gives the new third-degree terms

    [u']_3=(1/2)z^-15(-p^3+3p^2k+6pk^2+k^3),
    [v']_3=z^-16(p^3+5p^2k-12pk^2-4k^3).

The second-chart base coordinate is the actual
`W=(z^3+v)/(z^4+p)`. Its normal terms are retained in the coefficients
of `f1` and `q1(W)`. In particular, the normal derivative of `q1` contributes
to degree three. Expanding the inverse through degree three is exact modulo
`(e,h)^4`; all arithmetic is over rational Laurent polynomials in the
indeterminate parameters `z,t`.

For the diagonal `A=t,B=C=0,D=1`, the accepted quadratic-zero condition is
`(t-2)(3t^2-4t+12)=0`. Both local quadratic corrections are zero. The raw
cubic quotient is

    R=(-10+22t-16t^2+(13/2)t^3-(11/8)t^4)z^-5.

At `t=2` it vanishes. In the exact field `Q[t]/(3t^2-4t+12)` it is

    R=(64/27)(3-t)z^-5.

This is nonzero at both nonquadric diagonal points, since the quadratic
has value `27` at `t=3`. The comparison unit at those points evaluates to
`(2t-4)z^-3`; at the quadric point it evaluates to `4z^-3`.

On the open conic `A=2,B=t,C=8/t,D=1`, with `t!=0`, the exact local
quadratic corrections are

    q0=-96/t^2-192z/t^3,
    q1(w)=-6t^2-3t^3 w.

The independently computed comparison unit is

    L2(b,-a)=t^3z^-6+t^2z^-5-3tz^-4+4z^-3
              +20t^-1z^-2+16t^-2z^-1+64t^-3.

After the required subtraction, the complete cubic quotient is

    R=3t^6z^-11+9t^5z^-10+2t^4z^-9-6t^3z^-8+4t^2z^-7
       +64t^-2z^-3-384t^-3z^-2+512t^-4z^-1
       +9216t^-5+12288t^-6z.

Its retained cohomology class is therefore

    [R]=2t^4z^-9-6t^3z^-8+4t^2z^-7
         +64t^-2z^-3-384t^-3z^-2+512t^-4z^-1.

The `z^-1` coefficient is nonzero at every allowed point. These are
identities over the parameter Laurent ring, not tests at finitely many
parameters. They agree with the owner's calculation term for term.

## 3. Lifting freedom and primitive length-four scope

Two quotient-level quadratic lifts of the same leading line differ by a
global section of `Hom(W,Sym^2 M)=O(-4)`, whose `H^0` is zero. Thus the
quadratic correction is unique modulo changes of the local relation
generator by units. Adding `f P` in local normal degree two is such a unit
change to that order. Its induced degree-three product is a local correction,
so the corresponding change of the cubic remainder is a Cech coboundary.
The unrestricted degree-two part of a comparison unit multiplies `f0` and
vanishes in the quotient. Hence no extra quadratic parameter or unit
parameter can remove a nonzero class above. Local cubic corrections remove
exactly the displayed cubic coboundaries.

A primitive curvilinear structure of length four has `I_C^4` in its ideal,
and locally its ideal modulo `I_C^4` is generated by its first relation.
There is no independent initial relation in normal degrees one, two, or
three. Its local first-relation generators must therefore pass this cubic
compatibility problem. The owner's conclusion is valid: with the specified
line `O(-8)` and quotient conormal `O(-6)`, its line must be the actual
quadric line. The calculation does not apply when torsion or poles are
allowed, or when another independent relation enters in the relevant
degree. It does not take a root of a higher-order pure-power relation and
does not assert an STCI exclusion on its own.

The independent [source](../computations/moving_linear_cubic_independent_audit_2026_10_14.py)
and [complete stdout](../validation/2026-10-14-moving-linear-cubic/independent-audit/stdout.txt)
preserve the new derivation and its exact field reductions.
