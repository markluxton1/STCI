# A global opposite-ruling phase family always has extra inverse points

Date: 2026-10-14. Owner: `quadric_global_phase_geometry`, for
`projection_conductor_ray/quadric_phase_review`.
Status: **EXACT FAILURE SHIELD FOR THE DISPLAYED FAMILY ONLY**.

Let `S=P1 x P1`, with affine coordinates `(x,y)`, diagonal `c:y=x`,
and polarization `H=(2,2)`. For `a!=0,-1` and arbitrary `u`,
homogenize the following four polynomials to bidegree `(2,2)`:

    U0=1,
    U1=(a x+y)/(a+1),
    U2=a^2 x^2+y^2-(a^2+1)xy+u x^2y+(1-u)xy^2,
    U3=x^2y^2.

On the diagonal their restriction is `[1:t:t^3:t^4]`, the literal
fixed C0. On the opposite rulings through `(0,0)`, the points
`(s,0)` and `(0,a s)` have the same projective image. The section
`Q=(y-x)^2` has respective values `s^2` and `a^2 s^2`, so this
branchwise phase is the arbitrary constant `a^{-2}`.

The four sections have no common zero. On the finite chart this
follows from `U0=1`. On the boundary `x=Infinity`, they reduce to

    [0:0:a^2 y0^2+u y0 y1:y1^2],

and on `y=Infinity` they reduce to

    [0:0:x0^2+(1-u)x0 x1:x1^2].

In each case the last two entries have no common zero; at
`(Infinity,Infinity)` the last entry is nonzero. The resulting
morphism is finite because its pulled-back polarization is ample.

However, its entire inverse image of C0 always includes a point
outside the diagonal. If `u!=0`, the point

    (x,y)=(Infinity,-a^2/u)

maps to `[0:0:0:1]`. If `u!=1`, the point

    (x,y)=(-1/(1-u),Infinity)

maps to the same endpoint. Both displayed finite coordinates are
nonzero, so these are actual boundary points outside `c`.
At least one exists for every `u`: avoiding both would require
simultaneously `u=0` and `u=1`.

Therefore this family never satisfies the full inverse-image
support condition `nu^{-1}(C0)_red=c`. In particular it supplies
no global fixed-C0 mate-admitting carrier and no counterexample to
the accepted projective frontier. The argument does not require
birationality and places no restriction on the order of `a^{-2}`.

It also does not exclude general opposite-ruling pairs. The
[complete coefficient normal form](2026-10-14-quadric-opposite-ruling-phase-normal-form.md)
contains arbitrary vectors `D,E in k^4` in place of the restricted
choice `D=W2,E=u W2`; those coefficients can remove this particular
boundary obstruction. No general phase-order bound or full
four-section family exclusion follows from this calculation.
