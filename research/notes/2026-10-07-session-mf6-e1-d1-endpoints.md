# Six e=1 degree-one endpoint triples: complete fibers and mate obstruction

Date: 2026-10-07. Fixed C0, algebraically closed characteristic-zero field.
Status: **PROVED BOUNDED ENDPOINT EXCLUSION, EXACTLY AND INDEPENDENTLY
AUDITED**. The complete standalone verifier passed. The root agent and
the nonnormal-carrier auditor each independently accepted the localized
unit, full inverse support and branch-value obstruction. The former
explicitly checked that finiteness is not required for this parametrization.
No universal exclusion of e=1 positive D2 is claimed.

This continues section 4 of
[`2026-10-07-session-mf6-e1-defective-structural.md`](2026-10-07-session-mf6-e1-defective-structural.md).
The six directions are the entire `a0=0` or `b1=0` boundary of the
degree-one killing determinant, after removing the primitive class-zero
locus. The principal direction locus `a0*b1!=0` remains open.

## 1. Actual defective triples and complete quartic spaces

Put `q_r=12r^2+4r+3`. The finite-endpoint directions are

    A=r*z, B=1+z, delta=z, r=-1/2 or q_r=0.

The finite Bezout gauge is `s=-1/r,t=1`, with `s*A+t*B=1`. The
unique correction obtained by splitting delta*h2 has

    Gamma_U=-(q_r+12r+6+(6r+9)z+3z^2)/8,
    Gamma_infinity=0.

The generic triple relation is `m=-Gamma_U*y^2/delta`, where
`m=B*U-A*V,y=s*U+t*V`. At z=0 the correction is a unit for all three
retained r values, so the defect is exactly one finite endpoint.

The infinity-endpoint directions are

    A=1+r*z, B=1, delta=1, r=-1/2 or q_r=0.

Their finite correction is zero. On the actual other ambient chart
`x3=1,x2=w,x1=w^3+2U',x0=w^4+V'/2+3wU'`, use

    A'=r+w, B'=w, s'=1/r, t'=-1/r, delta'=w,
    Gamma'=(36r^2+16r+3)/4+(9r+3/2)w+3w^2.

The constant term is nonzero for the retained r values, so this is one
infinity defect. These formulas follow from the full quadratic cocycle
and its Laurent coboundary splitting, retaining the actual support
coordinate W. They are not obtained by freezing the normal transition.

The complete quartic equations are reconstructed on all 35 ambient
homogeneous monomials. In the finite frame write

    F=h*m+Q*y^2+E*m*y+K*y^3+... .

Vanishing on the defective triple imposes the support coefficient, the
linear y coefficient, and `delta*Q-Gamma*h=0`. The exact coefficient
matrices and the explicit kernel vectors give the following full spaces:

| Endpoint | Direction root | Full matrix rank | Complete quartic space |
|---|---|---:|---|
| finite | r=-1/2 | 31 | C_L times H0(P3,O(1)) |
| infinity | r=-1/2 | 31 | C_R times H0(P3,O(1)) |
| finite | either q_r root | 34 | the one-dimensional span of F_L(r) |
| infinity | either q_r root | 34 | the one-dimensional span of F_R(r) |

Here

    C_L=2x0*x3^2-2x1*x2*x3+x1*x3^2-x2^3,
    C_R=x0^2*x2-x0^2*x3+x0*x1*x2-x1^3,

and, with the earlier primitive pencils R0,R1,

    R0=x0^3*x3-(r+3/2)x0^2*x1*x2+(r+1/2)x1^4,
    R1=x0*x3^3+(r-7/6)x1*x2*x3^2+(1/6-r)x2^4,
    F_L=R1-(r+1/3)x3*(x2^3-x1*x3^2),
    F_R=R0-x0*(x0^2*x2-x1^3).

The ranks at q_r roots are exact over Q(sqrt(-2)); conjugation covers
the second root. The displayed nonzero forms are checked in the kernel,
and their dimensions equal 35 minus the matrix rank. Thus no additional
quartic or special pencil parameter is omitted. No generated quartic
JSON is an input to the final verifier.

Every nonzero member of either rational-root space has a plane factor.
It cannot occur in a pair with sole reduced support the integral,
nonplanar C0: a mate either shares the plane or cuts a nonempty curve
on it. This excludes those two endpoint directions for every mate degree.

## 2. Exact cubic excess: already enough for MF6

For a defective triple h is divisible by delta. Write `h=delta*S` and

    T=Gamma*E-delta*K,
    f3=T/(delta^2*S).

The exact third-piece lattice formula gives

    ord(D3-D2)=max(0,ord(S)-ord(T)).

At the finite algebraic endpoint, direct expansion gives

    h=(2/3)(3r+1)z^8, S=(2/3)(3r+1)z^7,
    ord_0(T)=4, coeff_(z^4)(T)=8r/9.

Both r and 3r+1 are units modulo q_r, so the excess at zero is exactly
three. There are no other zeros of S on P1. At the infinity algebraic
endpoint, the actual other chart gives

    h'=w^8, S'=w^7,
    ord_0(T')=4, coeff_(w^4)(T')=-4(4r+3)/27.

The latter scalar is a unit modulo q_r. This excess is again three.
Thus these unique endpoint quartics have total `d3=4`, while MF6 type
`(d2,d3)=(1,3)` requires excess two. This excludes all six endpoint
orbits in that type independently of the further mate obstruction.
The value d3=4 alone would not exclude every larger mate degree.

## 3. Stronger all-degree obstruction for the unique F_R carriers

Set `kappa=r+1/2,a=kappa+1`; then
`3*kappa^2-2*kappa+1=0`. The unique right carrier is

    F_R=x0^3*x3-a*x0^2*x1*x2+kappa*x1^4
        -x0^3*x2+x0*x1^3.

Consider the explicit morphism from the localized affine plane

    B=k[u,v,(u+kappa)^(-1)]

to its `x3=1` chart, given by

    X1=u^2*((u+a)*v-u)/(u+kappa),
    X0=u*X1, X2=v, X3=1.                            (1)

Substitution into F_R is identically zero. The morphism is dominant and
birational: where X1 is nonzero, u=X0/X1 and v=X2. Equivalently after
localizing the equation at x1, it is linear in x1 with coefficient
u+kappa and numerator relatively prime to that coefficient. At
u=-kappa the numerator is kappa^2(v+kappa), which is not the zero
polynomial, so the surface is irreducible. **No claim that this open
map is finite, or is the full normalization, is needed.**

The full preimage of the affine C0 under (1) is exactly the diagonal
on this open plane. If v!=0, `X1=v^3,X0=v^4` gives u=v. If v=0,
`X1=-u^3/(u+kappa)=0` gives u=0. This includes all points of the open
preimage. An exact ideal check uses delta=v-u and

    Q=u*v*(u+v)+kappa*v^2+kappa*u*v-u^2.

It gives

    (u+kappa)*(X1-v^3)=-delta*Q,
    X0-v^4-u*(X1-v^3)=-delta*v^3.

Since `Q(u,0)=-u^2`, the residual cofactor ideal has sole zero (0,0),
already on the diagonal. There is no extra curve or isolated point away
from the required inverse support.

If a homogeneous mate has sole intersection support C0, its nonzero
pullback g has zero set exactly this diagonal. The localized ring B is
a UFD with units exactly `c*(u+kappa)^k`, c in k*, k in Z. Therefore

    g=c*(v-u)^n*(u+kappa)^k, n>0.                   (2)

Unlike the earlier affine-plane obstruction, nonconstant units are
available here and must be retained; ignoring them would leave a gap.

For generic v, the two points

    u=0, u=a*v/(1-v)

belong to the open plane and map to the same singular-line point
`(x0,x1,x2,x3)=(0,0,v,1)`. At the second branch,

    u+kappa=(v+kappa)/(1-v),
    v-u=-v*(v+kappa)/(1-v).

The equality of values of (2) on the two branches therefore gives

    1=(-1)^n*kappa^(-k)*((v+kappa)/(1-v))^(n+k).     (3)

The rational function `(v+kappa)/(1-v)` is nonconstant because
kappa!=-1. Its divisor has distinct zero and pole, so (3) forces
`k=-n`. The remaining scalar condition is `(-kappa)^n=1`. As in the
primitive audit, applying the conjugation of Q(kappa) gives the
contradiction `(1/3)^n=1`, since kappa has norm 1/3 and n>0.
Thus neither F_R carrier admits a mate of any positive degree.

## 4. Transfer to the two F_L carriers

Let `r*=-r-1/3` be the conjugate root. Coordinate reversal
`x0<->x3,x1<->x2` carries `F_R(r*)` to `R1(r)+x3*D`, where
`D=x2^3-x1*x3^2`. The ambient torus with parameter lambda=r*
has weight 12 on R1 and weight 13 on x3*D. After the scalar lambda^12
is removed, it gives

    R1(r)+r* x3*D=F_L(r).

The parameter is nonzero modulo q_r. Reversal and this torus preserve
C0, so the no-mate statement transfers to both F_L carriers. This
proves the **all-degree exclusion of all six degree-one endpoint
orbits**, with exactly the stated fixed-C0, e=1,d2=1 boundary scope.

## 5. Evidence and unresolved boundary

The exact independent source is
[`verify_mf6_e1_d1_endpoints.py`](../computations/verify_mf6_e1_d1_endpoints.py).
It reconstructs complete degree-four matrices from the 35 ambient
monomials, checks both fixed-cubic fibers and both algebraic unique
fibers, computes the actual endpoint cubic valuations, and checks (1),
the inverse-support identities and the reversal/torus identity.
The branch-value argument (2)--(3) and its norm contradiction are proved
above; a passing symbolic substitution alone is not that proof.

The exploratory discovery script and its large exact quadratic-field
bases remain in
[`session-mf6-e1-d1-boundaries.py`](../scratch/session-mf6-e1-d1-boundaries.py)
and its JSON for provenance. The final source uses the simplified
explicit quartics and complete rank checks instead.

Remaining: the principal `a0*b1!=0` portion of the d2=1 direction
sextic, and the entire d2=2 defective triple/cubic incidence. They still
require the five-by-three quadratic annihilator or five-coordinate
vanishing condition from the structural note. No statement excluding
those loci, arbitrary quartics, or unrestricted STCI follows here.
