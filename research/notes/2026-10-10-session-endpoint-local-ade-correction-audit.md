# Endpoint triple conductor contact: local ADE and correction audit

Date: 2026-10-10. Author: `trisecant_endpoint_research/local_endpoint_ade`.
Status: **PROVED HERE CONDITIONALLY; parent/global coverage audit pending**.
No canonical record is edited by this note. This is a local statement for
the displayed full equation, not an exhaustion of all quartic carriers.

## 1. Inputs and the precise local statement

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

## 2. Only one singular point on B_T is possible

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

## 3. A nonzero A: B attaches an endpoint of an A_n chain

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

## 4. A=0 and v nonzero: the internal A_n position is controlled

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

## 5. A=v=0 and d nonzero: the graph is D4, with distinct outer contacts

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

## 6. A=v=d=0 is incompatible with the normal ADE model

In this case every quadratic term vanishes, while the nonzero term
`u*a*b*(b-a)` survives in degree three. The surface has multiplicity
three at the origin. A hypersurface ADE point has multiplicity two,
so this case is incompatible with the structural input.

## 7. Scope and verification

Equations (3), (6), and (8) exhaust the four coefficient cases of
(1) and contradict `z_B=1`. This closes the displayed endpoint
triple-contact configuration, conditional on the global reduction to
(1), the normal crepant conic model, B^2=-3, the absence of other
horizontal primes in this fiber, and the embedded smooth contact
input. It does not establish the full endpoint or lambda-one theorem
until those inputs and coverage are independently audited.

The formal splitting and ADE terminology agree with the primary
reference [Miles Reid, The Du Val singularities](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
especially its A_n/D_n equations and resolution graphs. The key
internal attachment computation here is the exact factorization (4)
and (5), not a cited generic-rank argument. The D4 contact calculation
is the explicit blowup (7).

Companion exact identity checker:
[verify_session_endpoint_local_ade_2026_10_10.m2](../computations/verify_session_endpoint_local_ade_2026_10_10.m2).
It verifies polynomial identities, the symbolic A_n Schur complement,
and the D4 inverse-matrix entries. Those algebraic checks supplement
the written resolution/contact proof and do not substitute for it.

Final checker execution: **PASS, 16 exact identities over QQ**, exit
zero, source SHA256
`cbe568f673086ed5f4084aedba3e4075470938c5b0bef223de75f7d65c8337d4`.
The [execution record](../validation/2026-10-10-endpoint-local-ade/execution-record.json)
preserves three failed setup/parser attempts, the preceding passing
execution with mechanically altered print labels, and the final passing
execution. A [separate diagnostic record](../validation/2026-10-10-endpoint-local-ade/diagnostic-record.json)
preserves two exploratory calls, including one failed debug run. None
of these attempts changes the frozen historical 97-source/110-run index.
