# Actual endpoint equations and exceptional attachments

These two local arguments are inputs to the
[full endpoint proof](GENUS_TWO_ENDPOINT_PROOF.md). Work in characteristic
zero with its actual normal ADE strict transform, crepant resolution,
and mate correction. No result here asserts that an arbitrary ADE graph
occurs for this quartic. The exact formal factorizations determine the
attachment positions needed in the global correction equation.
The two bounded arguments were independently accepted in their stated scope.

## 1. Triple residual contact

### 1.1. Inputs and the precise local statement

Work over an algebraically closed field of characteristic zero. The
ambient blowup and crepant normal ADE conic-model theorem is an input;
this note does not re-prove it. Put

    Gamma={x2=x3=0}, a=x1/x0, y=x2/x0, b=x3/x2.

The literal quartic lifts as `(a,b,y)=(r,r,r^3)`. In the endpoint
triple conductor configuration the full strict-transform equation is

    F = a*b*(u*(b-a)-v*a*b)
        + y*((b-a)*(A+beta*b+gamma*b^2)
              +v*a-a*b^2*(d+e*b))
        + y^2*(d+e*b),                                  (1)

with `u!=0`; the coefficient `v` is the coefficient named `c` in the
parent's formula. The conductor component is `B_T={a=y=0}`. Assume
its strict transform B on the crepant minimal resolution has `B^2=-3`,
and that the strict transform C of the literal curve is disjoint from B.
Assume the S-exceptional fiber containing B has no other horizontal
prime. Its other vertices are precisely the ADE exceptional primes
above singular points of T on B_T.

The mate correction Z is orthogonal to pullback L, so its coefficients
on this graph are uniquely determined by

    Z.E = -C.E,       Z.B = -C.B = 0.                     (2)

The embedded smoothness/uniformizer input gives exactly one transverse
C contact with one exceptional prime, of intersection one. The global
lambda-one reduction requires `z_B=coeff_B(Z)=1` when B is the sole
contributing horizontal prime. Under these inputs (1) instead forces
`z_B<1`, in every parameter case. The cases below preserve all higher
terms of (1).

### 1.2. Only one singular point on B_T is possible

The restriction to the ambient exceptional surface `y=0` is

    a*b*(u*(b-a)-v*a*b).

After removing B_T, the residual conductor restricted to B_T is
`u*b^2`, globally a binary quadratic on the b-projective line. It has
only the double zero `b=0`; it is nonzero at infinity. At every other
point of B_T the derivative of F in the a direction is nonzero.
Consequently T is smooth there. Thus the entire ADE graph attached to
B comes from the single point `(a,b,y)=(0,0,0)`.

No additional invisible vertical chain is allowed: under the stated
crepant normal-model input, vertical (-2)-curves contract precisely to
ADE singular points of T. This paragraph is where the full global
binary quadratic on B_T is used, rather than its affine germ alone.

### 1.3. A nonzero A: B attaches an endpoint of an A_n chain

The quadratic part of (1) is

    y*(A*b+(v-A)*a)+d*y^2.

If `A!=0`, it has rank two. Formal splitting in characteristic zero
gives `X*Y=z^(n+1)` for some finite `n>=1`, because the point is ADE.
Here X has linear term `A*b+(v-A)*a+d*y`, and Y has linear term y;
the remaining linear coordinate z parametrizes the Hessian kernel.

Along B_T, X has order one. A smooth branch of `XY=z^(n+1)` for
which X has order one attaches an end of the A_n resolution chain.
Equivalently, its first blowup direction is off the Hessian kernel,
on the corresponding smooth component of the rank-two tangent cone.
This conclusion remains valid if z has higher order on B_T.

Label the chain so B meets E_1. By the uniformizer condition C meets
one E_j transversely with multiplicity one, `1<=j<=n`. If R_n is the
positive A_n Cartan matrix, then

    (R_n^-1)_(1,1)=n/(n+1),
    (R_n^-1)_(1,j)=(n+1-j)/(n+1).

Eliminating the chain coefficients from (2) gives

    z_B = ((n+1-j)/(n+1)) / (3-n/(n+1)) < 1/2.            (3)

In particular this is incompatible with `z_B=1`. No bound on n,
and no assumption that C attaches an end, is used.

### 1.4. A=0 and v nonzero: the internal A_n position is controlled

This is the case where saying merely "rank-two quadratic part" would
leave a dangerous internal attachment. The actual full equation
controls it. Define power series in b (in fact polynomials)

    P=-u*b-v*b^2,
    Q=v-beta*b-(gamma+d)*b^2-e*b^3,
    R=beta*b^2+gamma*b^3,
    S=d+e*b.

Then exactly, with no omitted term,

    F=P*a^2+Q*a*y+S*y^2+u*b^2*a+R*y.                    (4)

Choose the formal square root `q=sqrt(Q^2-4*P*S)` with `q(0)=v`.
This is a unit. Put `alpha=(Q+q)/2` and `t=P/alpha`; alpha is a
unit. The following linear change in (a,y) has unit determinant q:

    X=alpha*a+S*y,       Y=y+t*a,
    a=(X-S*Y)/q,        y=(alpha*Y-t*X)/q.

The quadratic part of (4) is exactly XY. For

    ell_X=(u*b^2-R*t)/q,
    ell_Y=(R*alpha-u*b^2*S)/q,
    X'=X+ell_Y,         Y'=Y+ell_X,

the entire equation is

    F=X'*Y'-ell_X*ell_Y.                                 (5)

The orders are decisive: `ord_b(ell_X)=2`, with leading coefficient
`u/v`, and `ord_b(ell_Y)>=2`. If ell_Y vanished identically, (5)
would be reducible in the completed local ring, contrary to normal
ADE. Thus for finite `m=ord_b(ell_Y)>=2`, absorbing a unit turns
(5) into `X'*Y'=b^(n+1)`, with `n=m+1>=3`.

Along B_T one has exactly `(X',Y')=(ell_Y,ell_X)`, so the respective
orders are `(n-1,2)`. Along C, `a=b=r,y=r^3` gives `ord_r(X')=1`,
since its linear term is `v*r`; (5) then gives `ord_r(Y')=n`.
Both branches have b as a uniformizer. The standard toric charts of
the A_n resolution therefore show

    B meets E_(n-1),       C meets E_1,

once, away from exceptional crossings. For example, the chart at E_i
has monomials `X'=s^i*t^(i-1)`, `Y'=s^(n+1-i)*t^(n+2-i)`, `b=s*t`;
the nonzero t coordinate gives precisely these valuations.

The inverse Cartan entries are now

    (R_n^-1)_(n-1,n-1)=2*(n-1)/(n+1),
    (R_n^-1)_(n-1,1)=2/(n+1).

Equation (2) consequently forces the exact coefficient

    z_B = [2/(n+1)] / [3-2*(n-1)/(n+1)]
        = 2/(n+5) < 1.                                  (6)

This excludes every internal A_n configuration arising from (1),
including parameter cancellations of arbitrary order. An arbitrary
internal A_n attachment, divorced from (4), has not been excluded.

### 1.5. A=v=0 and d nonzero: the graph is D4, with distinct outer contacts

The quadratic part is `d*y^2`, and the cubic part in the tangent
plane is `u*a*b*(b-a)`, with three distinct linear factors. A direct
blowup gives the exact resolution graph and contact positions without
discarding the higher terms. In the b-chart put `a=b*z,y=b*w`.
After division by b^2, the equation is

    (d+e*b)*w^2 + u*b*z*(1-z)
      + w*(beta*b*(1-z)+gamma*b^2*(1-z)
           -b^2*z*(d+e*b)).                               (7)

The reduced exceptional line is `b=w=0`, parametrized by z. Its only
singular points are `z=0,1,infinity`. At z=0 the quadratic part is
`d*w^2+u*b*z+beta*b*w`, which is nondegenerate; at z=1 it is
`d*w^2-u*b*(z-1)`, also nondegenerate. The a-chart gives the same
nondegenerate quadratic part at infinity. Resolving these three A1
points produces the D4 graph, with a central (-2)-curve and three
outer (-2)-curves.

B follows z=0,w=0 and meets its A1 exceptional outer arm. C follows
z=1,w=b^2 and meets a different outer arm. At each A1 blowup their
direction is the b-axis; the central component has the z-axis
direction. Thus both contacts are transverse and away from the
central/outer intersections.

For the positive D4 Cartan matrix, an outer diagonal entry of the
inverse is 1, and the entry between distinct outer arms is 1/2.
The B equation in (2) therefore yields

    3*z_B=z_B+1/2,       z_B=1/4.                         (8)

The graph is specifically D4. A numerical D7 example obtained by
allowing arbitrary ADE graphs is not realized by these parameters.

### 1.6. A=v=d=0 is incompatible with the normal ADE model

In this case every quadratic term vanishes, while the nonzero term
`u*a*b*(b-a)` survives in degree three. The surface has multiplicity
three at the origin. A hypersurface ADE point has multiplicity two,
so this case is incompatible with the structural input.

## 2. The doubled-horizontal divisor

### 2.1. Inputs and the actual equation

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

The global degree calculation also controls the other curve's chart.
On the ambient blowup exceptional surface E, with product coordinates
(conductor line, plane pencil), one has

    H|E=O(1,0),       E|E=O(1,-1),
    T|E=O(2,2),      (T-E)|E=O(1,3).

Thus the derivative normal to E restricts to degree three on B_T and
degree one on F_T. On F_T it is a*(c-A). Normality forces A!=c,
since otherwise the whole affine open of F_T would be singular.
Its only zero on the complete F_T is therefore the endpoint contact;
there is no unseen additional zero in the other affine chart. The
three roots on B_T, including repeated roots, still require the full
ADE calculations below.

For an ADE exceptional block put `Q=(-E_i.E_j)` and let the vector
`v` have entries `B.E_i`. Define its contribution

    g_BB = v^t*Q^(-1)*v.

If the contact of `c#` is on that block at node `j`, put
`g_BC=v^t*Q^(-1)*e_j`. The equations above and `coeff_B(Z)=1` imply

    sum_blocks g_BB + g_BC = 3.                 (1)

Only the endpoint block has the `g_BC` term. Blocks outside `B` do not
change this equation. We now bound its left side strictly below three.

### 2.2. Exact contribution of every root away from the contact

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

### 2.3. Contact with a simple root: A is nonzero

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

### 2.4. Contact with a repeated root: exact formal factorization

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
