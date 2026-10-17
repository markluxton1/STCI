# Opposite ruling phases: the full coefficient normal form and a sparse-family obstruction

Date: 2026-10-14. Owner: `quadric_global_phase_geometry`, within the
projection/conductor continuation. Status: **NEW EXACT ELEMENTARY
REDUCTION; NO GLOBAL MATE OR FULL-SUPPORT CONSTRUCTION CLAIMED**.

Previously accepted Cartier-lift and conductor results are premises.
This calculation concerns only the smooth quadric target
`S=P1 x P1`, `H=(2,2)`, and its diagonal `c`.

## 1. Opposite-ruling gluing with a constant phase

Use affine coordinates `(x,y)` on the quadric with `c:y=x`, and let
`W0,W1,W2,W3` be the four coordinate vectors of the fixed curve

    U(t,t)=W0+t W1+t^3 W2+t^4 W3.

The distinguished section is `Q=(y-x)^2`, homogenized to bidegree
`(2,2)`. Suppose the two opposite rulings through `(0,0)` are paired
by `(x,0) <-> (0,a x)`, where `a!=0`. If the projective images agree
and the ratio of `Q` after that identification is constant, the
projective proportionality factor is constant in this affine
trivialization: the two `Q` values are `x^2` and `a^2 x^2`.
At the common point both coordinate vectors are `W0`, so that
constant factor equals one. Hence

    U(x,0)=U(0,a x).

The degree-one coefficient on the diagonal is `W1!=0`; consequently
`a=-1` is impossible in this form. For `a!=0,-1`, comparison of the
nine bidegree `(2,2)` coefficients gives the complete normal form

    U(x,y)=W0+(a x+y)/(a+1) W1
           +(a^2 x^2+y^2-(a^2+1)xy) D
           +xy[x E+y(W2-E)]+x^2y^2 W3,                 (1)

with arbitrary vectors `D,E in k^4`. Conversely, (1) has the fixed
diagonal restriction and the stated ruling identification. Its
branchwise phase is `a^{-2}` if the ratio is taken from the first
ruling to the second. Thus branchwise gluing alone places no bound
on the root-of-unity order.

This normal form assumes the specified affine scaling pairing.
It does not classify arbitrary conductor components or every
Möbius pairing, and it does not imply basepoint-freeness,
birationality, full support, or complete conductor descent.

## 2. The sparse family fails full support for every parameter

The especially simple family proposed in the phase exploration has

    D=W2, E=u W2,
    U0=1,
    U1=(a x+y)/(a+1),
    U2=a^2x^2+y^2-(a^2+1)xy+u x^2y+(1-u)xy^2,
    U3=x^2y^2.                                        (2)

Homogenize to bidegree `(2,2)` in `[x0:x1]` and `[y0:y1]`.
The four sections have no common zero: on the finite chart `U0=1`;
on `x0=0` the relevant pair is

    U2=a^2 y0^2+u y0 y1,   U3=y1^2,

and on `y0=0` it is

    U2=x0^2+(1-u)x0 x1,    U3=x1^2.

At the common point at infinity, `U3!=0`. This proves a finite
morphism because `H` is ample.

Nevertheless, the entire inverse image of C0 is never just `c`.
If `u!=0`, the boundary point

    x=Infinity,  y=-a^2/u

is finite in the second coordinate, lies outside `c`, and maps to
`[0:0:0:1]`, the infinite endpoint of C0. If `u!=1`, the analogous
point

    y=Infinity,  x=-1/(1-u)

also lies outside `c` and maps to the same endpoint. Avoiding the
first point would require `u=0`; avoiding the second would require
`u=1`. They cannot both be avoided. This argument is valid without
any birationality assumption and rules out full support for all
parameters of (2).

In characteristic zero there is also a useful finite-chart check. For an inverse image of
`[1:t:t^3:t^4]` with `t!=0`, put `l=a x+y=(a+1)t` and `p=xy`.
One has `p=+t^2` or `p=-t^2`. For the negative choice write
`x=r t`, `y=v t`, so

    a r+v=a+1,   rv=-1,
    a r^2-(a+1)r-1=0.

The quadratic coefficient of `U2` is then exactly
`2(a+1)^2`, independently of the selected root. Its cubic
coefficient is `C=-[u r+(1-u)v]`. Thus an extra point occurs at

    t=-2(a+1)^2/(C-1)

whenever `C!=1`. If `a^2+6a+1!=0`, the two roots are distinct.
Making `C=1` at both roots would force `(a+1)u-a=0`, which instead
gives `C=-1`. Hence at least one finite extra point exists in that
stratum. The boundary argument above additionally covers the
double-root stratum and all exceptional finite-chart cases.

## 3. Why this does not eliminate the complete normal form

For (1), the boundary restrictions are the vector-valued conics

    U(Infinity,y) ~ a^2 D+y E+y^2 W3,
    U(x,Infinity) ~ D+x(W2-E)+x^2 W3.                  (3)

Project to `k^4/k W3`. If the projected pairs `(D,E)` and
`(D,W2-E)` are both linearly independent, neither boundary ruling
has an extra finite point mapping to the infinite endpoint of C0.
For example, the coefficient choice `D=W0`, `E=W1` satisfies these
independence conditions. This is only a boundary observation; no
full-support or basepoint-free assertion is made for that choice.

Thus the obstruction in Section 2 comes from its restricted
coefficient choice. Treating it as a phase-order theorem or as an
exclusion of all opposite-ruling conductor pairs would discard
six permitted coefficients. The surviving structural problem is
to impose the full radical inverse-image condition and complete
conductor descent on (1), or on more general paired curves.
