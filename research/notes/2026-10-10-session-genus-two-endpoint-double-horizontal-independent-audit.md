# Endpoint double-horizontal conductor: independent exclusion

Date: 2026-10-10. Auditor: `double_horizontal_endpoint`.
Status: **PROVED HERE CONDITIONALLY on the accepted genus-two conic model and mate correction inputs**.
This note concerns exactly the endpoint stratum `D_T=2B_T+2F_T`.
It does not claim to exclude other conductor divisors or the unrestricted
set-theoretic complete-intersection problem. No canonical frontier file is
edited here.

## 1. Inputs and the actual equation

Work over an algebraically closed field of characteristic zero. The actual
quartic strict transform `T` in the blowup of the conductor line is normal
Gorenstein, has only ADE singularities, and has a crepant resolution
`rho:M -> T`. At the endpoint use the actual chart

    a=x1/x0,   y=x2/x0,   b=x3/x2,
    C_T: (a,b,y)=(r,r,r^3).

The conductor exceptional surface is `y=0`. In the stratum audited here the
surface equation is

    F = -c*a^2*b^2
        +y*((b-a)*(A+B*b+C*b^2)+c*a-a*b^2*(d+e*b))
        +y^2*(d+e*b),                         c != 0.

Consequently `div_T(y)=2B_T+2F_T`, where locally `B_T=(a,y)` and
`F_T=(b,y)`. The second curve is the vertical conductor component at
`b=0`; it has positive ambient hyperplane degree and is not an exceptional
prime of the normalization map to the quartic. The strict horizontal curve
`B` on `M` satisfies

    B^2=-3,   c#.B=0,   coeff_B(Z)=1,

where `Z` is the effective mate correction and `c#` is the strict curve.
The numerical equations for every contracted vertical ADE prime `E_i`
are `Z.E_i=-c#.E_i`; also `Z.B=0`. At the endpoint the smooth embedded
curve meets one vertical prime with intersection one. These are the
supplied genus-two lambda-one mate inputs, not conclusions from a
first-normal approximation.

On `B_T` the normal coefficient is

    h(b)=F_y(0,b,0)=b*(A+B*b+C*b^2).

Globally this is a nonzero section of `O_B(3)`. It cannot vanish
identically, since that would make all of `B_T` singular on `T`,
contrary to normality. Thus the total multiplicity of its zeros,
including infinity in the other blowup chart, is exactly three.

For an ADE exceptional block put `Q=(-E_i.E_j)` and let the vector
`v` have entries `B.E_i`. Define its contribution

    g_BB = v^t*Q^(-1)*v.

If the contact of `c#` is on that block at node `j`, put
`g_BC=v^t*Q^(-1)*e_j`. The equations above and `coeff_B(Z)=1` imply

    sum_blocks g_BB + g_BC = 3.                 (1)

Only the endpoint block has the `g_BC` term. Blocks outside `B` do not
change this equation. We now bound its left side strictly below three.

## 2. Exact contribution of every root away from the contact

Let `p` be a zero of `h` of multiplicity `k`, away from `b=0`. This
includes a possible point in the chart at infinity. The local equation
there has the form

    a^2*v(a,t)+y*h(t)+a*y*u(a,t,y)+y^2*w(a,t,y)=0,

where `t` is a parameter on `B_T` and `v(0,0)` is a unit. In particular
`div_T(y)=2B_T` near `p`.

On the smooth resolution choose coordinates `(u,t)` with `B=(u=0)`;
the parameter `t` can be the pulled-back parameter on `B_T`, because
the strict transform of the smooth curve `B_T` maps isomorphically to it.
Write

    a=u*A0(u,t),   y=u^2*Y0(u,t).

The hypersurface canonical generator is `da wedge dt/F_y`. Its pullback
is a unit times `du wedge dt`, since the resolution is crepant. Therefore

    A0(0,t) = unit*h(t).

Substitute the two expansions into the defining equation, divide by
`u^2`, and restrict to `B`. It follows that

    Y0(0,t) = unit*h(t).

Thus the leading normal coefficient of `y` on the strict curve has
vanishing order exactly `k` at `p`. On the other hand its divisor is

    div_M(y)=2B+sum_i beta_i E_i,
    beta=2*Q^(-1)*v.

Restricting the residual divisor to `B` identifies that same order with
`sum_i beta_i*(B.E_i)`. Hence

    2*g_BB=k.                                  (2)

This argument allows every ADE type, multiple attachments, and repeated
roots. It does not assume an A-chain away from the contact. A root where
`T` is smooth would give zero residual divisor and therefore `k=0`, so
every positive-order root contributes exactly as in (2).

## 3. Contact with a simple root: A is nonzero

First `A=c` is impossible: along the whole vertical curve `b=y=0`,
all first partial derivatives vanish except possibly
`F_y=a*(c-A)`. Thus `A=c` would make `T` singular along a curve,
contrary to normality. In this paragraph we therefore have
`A!=0` and `A!=c`.

The quadratic part at the contact is

    y*(A*b+(c-A)*a+d*y).

It has rank two. In fact the actual equation forces the germ to be
`A3`. To see this set `t=a` and use `z=A*b+(c-A)*a` as the other
linear coordinate, keeping `y` as the third. Its quadratic kernel is

    y=z=0,   b=((A-c)/A)*t.

The leading restriction to this kernel is
`-c*((A-c)/A)^2*t^4`, with nonzero coefficient. Formal elimination
of the nondegenerate `(z,y)` variables does not change this leading
coefficient: the critical value of `z` has order at least two and
that of `y` has order at least three. Indeed the cubic terms all
contain `y`, so their derivative in `z` vanishes on the kernel;
the derivative in `z` of the first term without `y` has order three.
The formal splitting lemma therefore gives `x*w=unit*t^4`.

The tangent
line of `B_T` is `(a,y)=0`; it is outside the kernel of this quadratic
form, since `A!=0`. The tangent line of `C_T` is `(a,b,y)=(r,r,0)`;
it too is outside the kernel, since substitution into the second linear
factor gives `c*r`, and `c!=0`.

For a rank-two `A_n` germ, a smooth curve with tangent outside the
quadratic kernel meets an endpoint of its exceptional chain. This follows
from the form `x*z=t^(n+1)`: one of `x,z` has order one along the curve,
so its attachment index is `1` or `n`. Both `B` and `c#` therefore attach
at the same endpoint: both have nonzero first-order `z` coordinate
and zero first-order `y` coordinate. The inverse `A3` matrix gives

    g_BB = 3/4,
    g_BC = 3/4,
    g_BB+g_BC = 3/2.

The remaining zeros of `h` have total multiplicity two. By (2) their
total contribution is exactly one. Thus the left side of (1) is exactly
`5/2`, a contradiction. The weaker arbitrary-chain endpoint bound
would already suffice; the global normality cut and the actual quartic
equation supply this sharper fixed value.

## 4. Contact with a repeated root: exact formal factorization

Suppose `A=0`. Put

    P(b)=B*b+C*b^2,   D(b)=d+e*b,
    h(b)=b*P(b),      u(b)=c-P(b)-b^2*D(b).

Then the equation is exactly

    -c*b^2*a^2+u(b)*a*y+h(b)*y+D(b)*y^2=0.

The normality condition leaves `k=ord_0(h)` equal to two or three.
Since `u(0)=c!=0`, take the formal square root with constant term `c`,
and set

    s(b)=sqrt(u(b)^2+4*c*b^2*D(b)),
    w(b)=(u(b)+s(b))/2,   v(b)=D(b)/w(b).

Both `s,w` are units. The invertible formal change

    X=a+v*y,    Y=-c*b^2*a+w*y

has determinant `s=w+c*b^2*v`. Its exact identities are

    F=X*Y+h*y,
    y=(Y+c*b^2*X)/s.

Consequently, after translations

    X1=X+h/s,   Y1=Y+c*b^2*h/s,
    X1*Y1=c*b^2*h^2/s^2.

This is an `A_(2k+1)` equation, after rescaling one coordinate by a
formal unit. On `B_T` the orders of `X1,Y1` are exactly `(k,k+2)`.
Therefore `B` meets node `k` of the `A_(2k+1)` chain, with the reversal
of the chain being immaterial. On `C_T`, `a=b=r` and `y=r^3`, the
coordinate `X1` has order one; hence `c#` meets an endpoint.

Writing `N=2k+2`, the inverse-chain formula now gives

    g_BB = k*(k+2)/N,
    g_BC <= (k+2)/N,
    g_BB+g_BC <= (k+2)/2.

For `k=2` this contact contribution is at most two and the remaining
simple root contributes one half. For `k=3` this contact contribution
is at most five halves and there is no other root. In both cases the
left side of (1) is at most `5/2`, again a contradiction.

## 5. Audited conclusion and scope

Under the stated accepted conic-model and mate-correction hypotheses,
the entire endpoint stratum `D_T=2B_T+2F_T` is excluded. The argument
includes all roots of the normal coefficient at infinity, its repeated
roots, and arbitrary ADE blocks away from the curve contact. In fact
those latter blocks have the exact contribution `ord(h)/2`, rather
than an assumed A-chain bound.

The contact is forced to be `A3` with endpoint attachment, `A5` with
attachment `2`, or `A7` with attachment `3`; these are consequences of the exact ambient
equation and formal factorization. Thus an abstract D/E graph at the
contact is not an omitted parameter stratum in this double-horizontal
case. Other endpoint divisor types and every broader genus-two or
global STCI claim require their own arguments.
