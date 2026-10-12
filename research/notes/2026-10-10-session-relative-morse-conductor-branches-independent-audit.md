# Relative formal Morse splitting preserves the actual conductor branches

Date: 2026-10-10. Author: `relative_morse_axis_audit`.
Status: **PROVED HERE / independent local audit**. This verifies the local
claim in section 4 of the
[nonendpoint trisecant obstruction](2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md).
It does not by itself verify that note's global hypotheses or remaining
steps. No canonical frontier file is edited.

## 1. Precise statement

Let k be an algebraically closed field of characteristic zero. In the
completion of a smooth threefold at a closed point take coordinates
`u,v,r`. Suppose a surface germ is given by

    F = uv + r h(u,v,r) = 0,

and the Cartier divisor cut out by `r=0` has the two actual reduced
branches `(u,r)` and `(v,r)`. Suppose the surface is smooth or has a Du Val
singularity. Then it is smooth or of type A_n. In the latter case the
strict transforms of the two specified branches meet opposite ends of
the minimal crepant exceptional chain, transversely. For A_1 they meet
the same exceptional curve at two distinct points.

The assertion concerns these specified branch ideals, rather than two
arbitrary smooth curves on an A_n surface. The parameter-preserving
argument below supplies precisely that distinction.

## 2. A direct parameter-preserving splitting algorithm

The power series ring `k[[u,v,r]]` is complete for the r-adic topology.
Suppose at some stage, with coordinates `x,y,r`, the equation has the
form

    F = xy + g(r) + r^N H(x,y,r),       N >= 1.

Decompose the error exactly as

    H(x,y,r) = a(r) + x A(x,y,r) + y B(x,y,r).

This is always possible by separating the constant term in x,y and
then allocating each remaining monomial to x or y. Set

    X = x + r^N B(x,y,r),
    Y = y + r^N A(x,y,r).

These are invertible formal coordinates with r fixed: their x,y
Jacobian is the identity modulo the maximal ideal. An exact identity
gives

    F = XY + g(r) + r^N a(r) - r^(2N) A(x,y,r)B(x,y,r).

After expressing x,y in the new coordinates, the last term is still
divisible by `r^(2N)`. Thus each step absorbs the constant error into
g and at least doubles the r-adic error order. Starting with `N=1`,
the coordinate changes and g converge in the r-adic topology. Their
limits give invertible formal coordinates satisfying

    x = u mod r,       y = v mod r,
    F = xy + g(r).

In particular the original branch ideals are exactly

    (u,r) = (x,r),       (v,r) = (y,r).

There is no appeal here to a splitting lemma that might silently
change the divisor `r=0` or its branch labels.

If the surface is singular, the linear part of F vanishes, so g has
order at least two. Also g cannot be identically zero: `xy=0` has a
nonisolated singular locus and is not a Du Val surface. Write

    g(r) = r^m epsilon(r),       m >= 2,       epsilon(0) != 0.

Multiplication of the defining equation by a unit, followed by
rescaling one of x,y by a unit, gives `xy=r^m` (a constant sign is
absorbed too). This final normalization need not be the identity
modulo r, but it leaves the two branch ideals `(x,r)` and `(y,r)`
unchanged. Hence the pair consisting of the surface and its specified
two branches is the standard A_(m-1) pair. If g has order one, the
surface is smooth. The normal-form classification agrees with
[Reid's Du Val notes, Table 1 and section 2.2](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).

## 3. Explicit resolution and branch endpoints

For `xy=r^m`, the standard minimal resolution is covered by m smooth
charts with coordinates `(a_i,b_i)`, indexed by `i=0,...,m-1`, and
map

    x = a_i^(i+1) b_i^i,
    y = a_i^(m-i-1) b_i^(m-i),
    r = a_i b_i.

The transition from chart i to i+1 is

    a_(i+1) = 1/b_i,
    b_(i+1) = a_i b_i^2.

Each displayed monomial formula is compatible with this transition
and satisfies `xy=r^m`. These charts are the regular toric subdivision
of the original cone: in the quotient lattice
`N=Z^2+(1/m)(1,-1)Z`, subdivide between `(0,1)` and `(1,0)` by the rays
`(j/m,1-j/m)`, `j=1,...,m-1`. Adjacent rays form a lattice basis, and
the subdivided fan has the same support, so its map to the original
affine toric surface is proper and birational.

The exceptional curves form a chain of m-1 curves. The j-th one is
`a_(j-1)=0` in chart j-1 and `b_j=0` in chart j; its normal-coordinate
transition is the square of the coordinate on its P1, giving degree
-2. The residue canonical form pulls back as

    (dx/x) wedge dr = da_i wedge db_i,

so the resolution is crepant. With only (-2) exceptional curves it is
minimal. Thus it is the minimal crepant A_(m-1) resolution.

The branch `y=r=0` has strict transform `b_0=0` in chart 0 and meets
the first exceptional curve `a_0=0` transversely at that chart's
origin. The branch `x=r=0` has strict transform `a_(m-1)=0` in the last
chart and meets the last exceptional curve `b_(m-1)=0` transversely
at that chart's origin. Neither strict transform meets any other
exceptional component. For m=2 the two chart origins are distinct
points on the single exceptional P1.

## 4. Audit conclusion and small wording qualification

The local all-length A-chain assertion used by the nonendpoint
trisecant argument passes. In particular a transverse crossing of the
two reduced actual conductor branches cannot lead to a D_n or E_n
configuration, and the branch belonging to B attaches at an endpoint
of the A-chain for every n.

The only wording qualification is that one first obtains
`xy+g(r)`, with coordinate changes exactly zero modulo r. Replacing g
by a pure power uses a harmless unit rescaling (or a reparameterization
of r); it preserves the specified branch ideals. This qualification
does not alter the geometric endpoint conclusion or any subsequent
intersection calculation.
