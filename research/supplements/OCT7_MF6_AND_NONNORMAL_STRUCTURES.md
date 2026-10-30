# Historical mathematical source compilation

Full original mathematical text retained below. Original hypotheses, failures, qualifications and unresolved cases retain their source status; this compilation is not an independent correctness audit.

---

## Source: 2026-10-07-session-mf6-e1-d1-endpoints.md

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


---

## Source: 2026-10-07-session-mf6-e1-defective-structural.md

# Structural continuation for the defective e=1 MF6 triples

Date: 2026-10-07. Fixed C0, characteristic zero. Status: **PROVED
NECESSARY REDUCTIONS; REMAINING INCIDENCE OPEN**. This follows the
all-degree primitive-triple exclusion in
[`2026-10-07-session-mf6-e1-independent-audit.md`](2026-10-07-session-mf6-e1-independent-audit.md).
No exclusion of MF6 types `(d2,d3)=(1,3),(2,2)` is claimed here.
The subsequent bounded endpoint work is now proved in
[`2026-10-07-session-mf6-e1-d1-endpoints.md`](2026-10-07-session-mf6-e1-d1-endpoints.md):
all six degree-one endpoint orbits in section 4 admit no mate, for any
mate degree. The principal direction locus and type (2,2) remain open.

## 1. Intrinsic module and the correct twist of the cubic residue

Retain `L=O(-6)`, `M=O(-8)`. At a point of the canonical triple with
positive second defect, choose a DVR R and regular normal parameters
`m,y`. Its ideal has the form

    J=(delta*m-gamma*y^2, m*y, m^2, y^3),

where delta is a local equation of D2 and gamma is a unit at its zeros.
This unit condition is the finite-flatness condition for the embedded
triple. Near such a point y^3 is redundant, since

    gamma*y^3=delta*m*y-y*(delta*m-gamma*y^2).

Writing the first three generators as `g1,g2,g3`, the two syzygies are

    m*g1+gamma*y*g2-delta*g3=0,
    m*g2-y*g3=0.

Their matrix has maximal minors g1,g2,g3 (up to signs), and is the
Hilbert--Burch presentation of this height-two triple ideal. After
restricting to C, it gives

    J/(I_C*J)=R*g1 + R*g2 + (R/(delta))*g3.

The torsion generator is g3. The relation for y^3 becomes
`[y^3]=(delta/gamma)[g2]` in the torsion-free quotient. At a point
where delta is a unit, the primitive presentation gives the same
torsion-free module. Thus the global torsion-free ideal-generator
bundle V fits the exact sequence

    0 -> P=L^3(D2) -> V -> Q=M(-D2) -> 0.             (1)

The quotient is the image of J in the first conormal: its generator has
symbol delta*m, so the image is M(-D2). The subline P contains the
ordinary third power L^3 with zero divisor D2. These identifications
are intrinsic and survive a change of regular normal frame.

In a hypothetical fourth saturated layer, functions in J map into
`E3=L^3(D3)`. Multiplication by I_C sends them into the next step,
so this defines a map `V -> E3`; torsion maps to zero. Its restriction
to P is the canonical section with zero divisor `D3-D2`. Therefore
the extension class

    c in Ext1(Q,P)=H1(L^3*M^-1(2D2))

must be killed by the section of `O(D3-D2)`. For e=1 this is

    c in H1(O(-10+2*d2)),
    c maps to zero in H1(O(-10+d2+d3)).               (2)

This includes the nonprimitive correction to the kernel bundle; using
M rather than M(-D2) would lose one D2 twist and give the wrong matrix.

There is also a direct valuation check. If the generic formal root is
`m=f2*y^2+f3*y^3` and `val(f2)=-a<0`, the exact third-piece lattice
gives

    ord D3=max(a,-a-val(f3)),
    ord(D3-D2)=max(0,-2a-val(f3)).

Hence the normalized cubic residue is delta^2*f3, up to a regular
unit and a regular change of splitting. That is exactly the twist in
(1)--(2), rather than delta*f3 or f3 alone. For the previously accepted
e=0,d2=4,d3=5 branch, (2) becomes
`H1(O(-6)) -> H1(O(-5))`, agreeing with its four-by-two linear
annihilator certificate. This is a consistency check, not the proof of
the new sequence.

## 2. Exact annihilator sizes for the two remaining MF6 types

For `(d2,d3)=(1,3)`, the class c is in H1(O(-8)). Write it as
`sum(c_i*z^-i,i=1,...,7)`. A nonzero quadratic section
`l0+l1*z+l2*z^2` must kill it in H1(O(-6)). Thus the exact necessary
condition is a nonzero kernel for

    [c1 c2 c3]
    [c2 c3 c4]
    [c3 c4 c5].                                     (3)
    [c4 c5 c6]
    [c5 c6 c7]

Equivalently all ten three-by-three minors of this five-by-three
matrix vanish. The coefficients l0,l1,l2 are homogeneous sections of
O(2), so an infinity point or a doubled point is included; no fixed
finite support is assumed. The cubic class must be computed using the
actual defective triple and moving support/frame transition.

For `(d2,d3)=(2,2)`, the map P->E3 is an isomorphism. The class is
already in H1(O(-6)), and the exact necessary condition is simply

    c1=c2=c3=c4=c5=0.                                (4)

A determinant alone would be weaker and inappropriate. Conditions
(3)--(4) are necessary for the fourth layer. Their satisfaction alone
does not establish quartic containment, finite-flat higher layers, a
sextic mate, or STCI.

## 3. The preceding defective-triple incidence is much smaller

For the quotient direction `A=a0+a1*z,B=b0+b1*z`, let c1,c2,c3 be
the three quadratic cocycle coordinates already independently derived:

    c1=-b1*(2*a0*b1+12*a1^2+16*a1*b0+9*b0^2)/8,
    c2=-(2*a1+b0)*(8*a0*b1+12*a1^2+4*a1*b0+3*b0^2)/8,
    c3=-a0*(2*a0*b1+36*a1^2+16*a1*b0+3*b0^2)/4.

Basepoint freedom is `a0*b1-a1*b0!=0`.

When d2=1, a linear defect section `delta0+delta1*z` kills the
quadratic class in H1(O(-3)), so its complete killing matrix is

    [c1 c2]
    [c2 c3].                                        (5)

Away from c=0 it has rank one and a unique projective kernel. The
base direction must satisfy the sextic `c1*c3-c2^2=0`. Setting
`p=a0*b1,t=a1,b=b0`, its numerator after multiplication by 64 is

    8p^3-(64t^2+128tb+16b^2)p^2
    +(96t^4+512t^3b+592t^2b^2+128tb^3+6b^4)p
    -(576t^6+960t^5b+880t^4b^2+544t^3b^3
      +220t^2b^4+60tb^5+9b^6).                     (6)

This is a compact torus-invariant polynomial specification, not an
irreducibility claim or a solved parameter curve. It includes
`a0*b1=0` boundaries, which must not be dropped by the invariant p.

When d2=2, the quadratic defect section has coefficients
`delta0,delta1,delta2`, and the complete quadratic-class killing
condition in H1(O(-2)) is the one linear equation

    delta0*c1+delta1*c2+delta2*c3=0.                  (7)

It has a projective line of possible sections away from c=0. In both
cases the finite and infinity corrections are unique because
`H0(O(-4+d2))=0`. The correction is obtained by splitting
`delta*h2` into its Laurent coboundary pieces. Finite-flatness still
requires delta and the local correction gamma to have no common zero.

In fact the primitive obstruction-zero locus cannot support a genuine
positive D2 of degree at most three. If h2 is already a coboundary,
its unique primitive correction is gamma0. Multiplication by delta
gives a correction delta*gamma0. Because
`H0(O(-4+d2))=0` for `d2<=3`, there is no alternate correction.
At every zero of delta the two coefficients delta and gamma share
that zero, violating triple finite-flatness. Thus the four primitive
direction orbits of the preceding audit can be removed from these
defective incidences. Together with the quartic-specific uniform
bound `d2<=3`, this applies to all mate degrees in the e=1 lane.

## 4. Six complete boundary triples for d2=1

The two boundaries of (6) can be retained as six finite test fibers.

If `a0=0,b1!=0`, basepoint freedom says `a1*b0!=0`. Then c3=0,
so (5) requires c2=0. Removing the primitive c=0 locus, c1!=0 and
the unique defect section is delta=z. Actual torus and quotient
scaling yield the representatives

    A=r*z, B=1+z, delta=z,
    r=-1/2 or 12r^2+4r+3=0.

The two quadratic roots have c1!=0, as does r=-1/2, so these are
genuine distinct boundary directions, not the primitive B=1 fibers.
If `b1=0,a0!=0`, similarly c1=0,c2=0,c3!=0, and the unique
defect section is the homogeneous section whose finite polynomial is
delta=1 (its zero is infinity). The representatives are

    A=1+r*z, B=1, delta=1,
    r=-1/2 or 12r^2+4r+3=0.

At the respective defect points the other coefficient is a unit, so
the boundary triples pass that flatness check. The subsequent endpoint
note reconstructs their complete quartic fibers and proves the six
bounded exclusions. The principal `a0*b1!=0` portion of the sextic
remains unsolved.

## 5. Continuation-ready next calculation

The highest-value next step is the intrinsic class in (2), calculated
on the actual triple incidence (5) or (7), with delta/gamma flatness
and complete ambient quartic containment. For type (2,2), test the
five coefficients directly. For type (1,3), test the actual quadratic
annihilator matrix (3) on the remaining principal direction sextic.
The six boundary fibers above have now been checked and excluded in
the separate endpoint proof.

The companion
[`verify_mf6_e1_defective_structural.py`](../computations/verify_mf6_e1_defective_structural.py)
checks the local syzygies, the normalized third-layer valuation formula,
the killing matrices, the exact sextic and boundary directions, and the
two target twists. It does not compute the universal cubic class or
prove either remaining type empty. The universal STCI question and the
unrestricted char-zero status of C0 remain open.


---

## Source: 2026-10-07-session-mf6-e1-independent-audit.md

# Independent audit and all-degree exclusion of primitive e=1 quartic triples

Date: 2026-10-07. Fixed
`C0=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of
characteristic zero. Status: **PROVED HERE, EXACTLY AND INDEPENDENTLY
AUDITED** for the primitive-triple lane. The root agent reconstructed
the classification and normalization argument separately. The further
adversarial normalization audit is
[`2026-10-07-session-nonnormal-mf6-independent-audit.md`](2026-10-07-session-nonnormal-mf6-independent-audit.md),
which independently accepts the full-inverse-support and branch-value
obstruction. This note does not assert that C0 is not
STCI, and it does not cover `D2>0`, `e=0`, `e=2`, carriers of higher
degree, or the branch with both equations thick along the curve.

## 1. Verdict and dependencies

The proposed exclusion of MF6 type `e=1,(d2,d3)=(0,4)` passes. Its
complete primitive-direction classification and every quartic pencil
member, including both moving infinity members, are retained. A further
argument excludes the four pure quartics left by the uniform BF bound.
Consequently the stronger statement is proved under the existing
quartic/quasiprimitive inputs:

> A characteristic-zero pair `(F4,Gb)` with reduced projective support
> C0 cannot have first quotient `L=O(-6)` and `D2=0`, for any mate degree
> `b>=4`.

The earlier inputs are the balanced conormal bundle `O(-7)^2`, the
quartic generic-order-one theorem P-011, and the directly audited BF
filtration/duality in
[`2026-10-06-session-uniform-audit.md`](2026-10-06-session-uniform-audit.md),
sections 2--4. P-011 and the balanced conormal theorem are not reproved
here. The **quartic-specific** all-degree bound `d3<=5` is proved again
in section 6; the bound 17 for arbitrary defining degrees is a different
statement and is not used.

The independent verifier
[`audit_mf6_e1_primitive_2026_10_07.py`](../computations/audit_mf6_e1_primitive_2026_10_07.py)
uses no imported research verifier or generated JSON. It reconstructs
the complete ambient spaces directly in the 35 homogeneous quartic
monomials, imposing vanishing on C0 and the two normal coefficients.
This removes a shared-generator-coordinate dependency from the rank
checks. It checks exact identities over Q and Q(sqrt(-2)), the two
infinity expansions, the normalization and full-support identities, and
the conjugate coordinate reversal. The accompanying JSON records the
source hash and scope. These exact checks support the proof below;
script agreement alone is not its proof.

## 2. Every basepoint-free primitive triple direction

Let `L=O(-6)` and `M=O(-8)` be the quotient and kernel of the balanced
conormal. Write the quotient direction in the first moving frame as

    A=a0+a1*z, B=b0+b1*z, d=a0*b1-a1*b0 !=0.

The actual change of ambient chart, including its support coordinate,
is

    W=(z^3+V)/(z^4+U+3*z*V/2),
    a'=z/(z^4+U+3*z*V/2)-W^3,
    b'=1/(z^4+U+3*z*V/2)-W^4,
    U'=a'/2, V'=-3*W*a'+2*b'.

In the second frame put `A'=a1+a0*W,B'=b1+b0*W`.
Substituting `U=A*y,V=B*y` into `B'*U'-A'*V'` and retaining degree two
gives the cocycle

    h2=-(2*A+z*B)*(12*A^2+3*z^2*B^2
                  +4*z^2*(A_z*B-A*B_z))/(8*z^5).

The obstruction is in `H1(Hom(M,L^2))=H1(O(-4))`; it vanishes exactly
when the coefficients at `z^-1,z^-2,z^-3` vanish. They are

    -b1*(2*a0*b1+12*a1^2+16*a1*b0+9*b0^2)/8,
    -(2*a1+b0)*(8*a0*b1+12*a1^2+4*a1*b0+3*b0^2)/8,
    -a0*(2*a0*b1+36*a1^2+16*a1*b0+3*b0^2)/4.

For completeness the classification can be checked without a saturation
claim. Set `p=a0*b1,c=a1,d0=b0` and denote the three bracket polynomials
by

    P=2p+12c^2+16c*d0+9d0^2,
    Q=8p+12c^2+4c*d0+3d0^2,
    R=2p+36c^2+16c*d0+3d0^2.

If `a0*b1!=0`, then `P=R=0`, so
`R-P=6(2c-d0)(2c+d0)=0`. The alternative `c=d0/2` gives
`p=-10d0^2`, and the middle equation `(2c+d0)Q=0` then gives
`d0=0`, contradicting `p!=0`. Thus `c=-d0/2` and
`p=-2d0^2`, with `d0!=0`.

If `a0!=0,b1=0`, basepoint freedom implies `c*d0!=0`. If
`2c+d0=0`, then `R=4d0^2!=0`. Otherwise `Q=R=0`, but
`R-3Q=4d0(c-3d0/2)` and `Q(3d0/2)=36d0^2`, a contradiction.
If `a0=0,b1!=0`, similarly `2c+d0=0` makes `P=4d0^2!=0`;
otherwise `P=Q=0` and `P-Q=6d0(2c+d0)` contradicts that alternative.
Thus both mixed boundaries are empty.

The last case `a0=b1=0` gives `c*d0!=0`. After quotient scaling
`d0=1`, its directions are

    A=r*z, B=1, (2r+1)*(12r^2+4r+3)=0.

The principal branch is a single actual torus orbit. The ambient symmetry
`(x0,x1,x2,x3)->(x0,lambda*x1,lambda^3*x2,lambda^4*x3)` gives
`z_new=lambda*z,U_new=lambda^4*U,V_new=lambda^3*V`; after the quotient
parameter is scaled by `lambda^3`, it carries `(A,B)` to
`(lambda*A(z_new/lambda),B(z_new/lambda))`. Scaling so `b0=-2`
makes `a1=1,a0*b1=-8`; then `lambda=1/a0` gives

    A=1+z, B=-2-8z.

The three ratios `r` on the boundary are invariant under this torus.
Thus there are exactly four retained torus orbits. No arbitrary GL2
change of the split conormal frame or PGL2 change of support is assumed.
Since `H0(Hom(M,L^2))=H0(O(-4))=0`, a primitive embedded triple in a
specified direction, when it exists, is unique.

## 3. Exact third-piece lattice, including a singular carrier point

At a point of C0 choose an ambient lifted support parameter and complete
over `R=k[[t]]`, with fraction field K. The hypothetical CI algebra B is
finite free over R. Its saturated quotient by the fourth step embeds in
`K[y]/(y^4)` and is generated over R by the images of the two ambient
normal parameters `m,y`.

Because `D2=0`, in the specified regular primitive-triple frame

    m=-gamma*y^2+f3*y^3 modulo y^4,

with `gamma` regular. Replacing m by `m+gamma*y^2` is an allowed
integral change of generators. The only degree-three coefficient vectors
are then generated by `y^3` and `f3*y^3`; the products `y*m` supply
only the already regular coefficient `-gamma`, and higher words vanish
modulo y^4. Therefore the actual saturated third-layer coefficient
ideal is `R+R*f3`, giving

    ord(D3)=max(0,-val(f3)).

This is exact, including repeated zeros and singular points of F4. A
mate equation cannot supply extra words: the actual quotient is already
generated by the ambient normal parameters and R.

For a quartic jet
`F=h*m+gamma*h*y^2+E*m*y+K*y^3+...`, formal implicit elimination at
the generic point gives

    m=-gamma*y^2+(T/h)*y^3+..., T=gamma*E-K.

Thus in each regular chart
`ord(D3)=max(0,ord(h)-ord(T))`. The first symbol h is nonzero for every
nonzero member of each two-dimensional pencil below. The quadric-factor
orbit is handled separately, including its order-two quartics.

## 4. Complete ambient pencils and their polar bounds

In the principal direction the Bezout pair is `s=4/3,t=1/6`, and
`gamma=192z+96`. The complete degree-four matrix on all 35 ambient
monomials has rank 33. Its complete kernel is the pencil
`F=alpha*F0+beta*F1` displayed explicitly in the independent verifier.
In the frame `m=B*U-A*V,y=s*U+t*V`, the first and cubic coefficients
are

    h=(4z^2+2z+1)*(64alpha*z^3+64beta*z^6+8beta*z^3+beta)/1024,
    T=(2z+1)*(1536alpha*z^5+1152alpha*z^4+448alpha*z^3
         +48alpha*z^2-24alpha*z+4alpha
         +1536beta*z^8+1152beta*z^7+448beta*z^6+240beta*z^5
         +120beta*z^4+60beta*z^3+30beta*z^2+15beta*z+8beta).

For `beta!=0`, normalize beta to one. The first symbol has degree eight
and

    Res_z(h,T)=-27*(8alpha-1)*(8alpha+3)^3/2^26.

Away from the two roots its gcd degree is zero. At `alpha=1/8` the
gcd has degree one; at `alpha=-3/8` it has degree two. Thus the finite
polar degree is respectively eight, seven, or six, retaining all
multiple-root multiplicities. For `beta=0`, the finite polar degree is
three. Direct expansion of the homogeneous F0 on the actual second
ambient chart uses

    x3=1, x2=w, x1=w^3+2U', x0=w^4+V'/2+3wU',
    A'=1+w, B'=-8-2w, s'=-1/3, t'=-1/6, gamma'=3w+6.

It gives

    h'=w^3*(w^2+2w+4)/16,
    T'=-(w+2)*(w^2+2w+4)*(3w^3+3w^2-4w+2)/16.

T' is a unit at zero, so infinity adds exactly three pole units. Every
nonzero member in the principal orbit consequently has `d3>=6`.

At `r=-1/2`, the complete 35-column matrix has rank 25, and its full
ten-dimensional kernel is exactly
`q*H0(P3,O(2))`, where `q=x0*x3-x1*x2`. A quartic with this factor
cannot occur in a defining pair supported on C0. If the mate also has
the factor q, the pair has a common surface. Otherwise it cuts an
effective divisor of class `(b,b)` on the smooth quadric. Such a divisor
cannot have sole support C0 of class `(1,3)`: it would have class
`n(1,3)`, inconsistent with `(b,b)` for positive b,n. This applies to
the factor regardless of the quartic's other factor or normal order.

For either root `12r^2+4r+3=0`, the quadratic cocycle is identically
zero on both charts. Exact rank 33 over Q(sqrt(-2)), together with two
independent checked kernel vectors, proves that the complete pencil is

    R0=x0^3*x3-(r+3/2)*x0^2*x1*x2+(r+1/2)*x1^4,
    R1=x0*x3^3+(r-7/6)*x1*x2*x3^2+(1/6-r)*x2^4.

In `m=U-r*z*V,y=V`, its coefficients are

    h=alpha+beta*(2r+2/3)*z^8, T=beta*(8r/9)*z^3.

Both r and `2r+2/3` are nonzero. If `alpha*beta!=0`, all eight finite
zeros of h are away from zero and T is a unit at them, so `d3>=8`.
For `alpha=0,beta!=0`, the pole degree at zero is exactly five.
For `beta=0`, no finite pole appears; the actual second chart has
`A'=r,B'=w`, with `U'=r*y',V'=w*y'-m'/r`. Direct expansion gives

    h'=w^8, K'=(16r/27+4/9)*w^3, T'=-K'.

The nonzero scalar leaves exactly five infinity pole units. The
calculation is modulo the irreducible quadratic, so neither root is
omitted. All primitive directions therefore either have an inadmissible
quadric factor or satisfy `d3>=5`. This already excludes MF6 type
`(d2,d3)=(0,4)`.

## 5. New normalization obstruction to all four surviving pure members

The only algebraic pencil members whose bound does not exceed five are
R0 and R1 themselves. Set

    kappa=r+1/2, a=kappa+1,
    S=V(x0^3*x3-a*x0^2*x1*x2+kappa*x1^4),
    3*kappa^2-2*kappa+1=0.

In the affine chart `x3=1`, put `v=x2`. Its finite birational
normalization is the smooth affine plane `B=k[u,v]`, with

    X1=u^2*(a*v-u)/kappa, X0=u*X1, X2=v.

Indeed the displayed surface equation vanishes identically. On the open
`x1!=0`, u is `x0/x1`, giving birationality. The relation
`u^3-a*v*u^2+kappa*x1=0` is monic; since `B=A[u]`, the map is finite.
The surface is irreducible: after localizing at x1, its equation reduces
to this polynomial, linear in x1 with nonzero coefficient kappa, and
the original polynomial has no x1 factor. Since B is normal, finite and
birational, it is the integral closure of A.

The full inverse image of the affine C0 is exactly the diagonal `v=u`.
To check this including the endpoint, the affine ideal of C0 is
`(x1-v^3,x0-v^4)`. With `delta=v-u` and
`Q=kappa*v^2+kappa*u*v-u^2`, its pullback is

    (X1-v^3,X0-v^4)=(delta*Q,delta*v^3).

The equality is up to a nonzero scalar and an elementary generator
change: `X1-v^3=-delta*Q/kappa` and
`X0-v^4-u*(X1-v^3)=-delta*v^3`. The cofactor ideal `(Q,v^3)` has
radical `(u,v)`. This point already belongs to the diagonal, so there
is no extra isolated point or curve in the full inverse set.

Suppose any homogeneous mate G has reduced intersection support C0 on
S. Its affine pullback g is nonzero and has zero set exactly the
diagonal. In the UFD `k[u,v]`, over the algebraically closed field,

    g=c*(v-u)^n, c in k*, n>0.

No nonconstant unit or other irreducible factor is available in this
affine ring. The two points `(u=0,v)` and `(u=a*v,v)` map to the same
point `(x0,x1,x2)=(0,0,v)` on the singular line of S. The pulled-back
polynomial must agree on them, hence

    c*v^n=c*(1-a)^n*v^n=c*(-kappa)^n*v^n,
    (-kappa)^n=1.

This is impossible in characteristic zero. The irreducible polynomial
`3*kappa^2-2*kappa+1` gives the conjugate
`kappa*=2/3-kappa` and norm `kappa*kappa*=1/3`. If
`kappa^n=(-1)^n`, apply the nontrivial automorphism of Q(kappa) and
multiply the two equalities to obtain `(1/3)^n=1`, a contradiction for
positive n in characteristic zero. This argument uses neither a complex
absolute value nor an unproved conductor descent claim.

Finally `R1(r)` is the coordinate reversal
`x0<->x3,x1<->x2` of `R0(r*)`, where `r*=-r-1/3` is the other root.
C0 is invariant under this reversal. The same obstruction therefore
excludes both R1 members as well. This is a fixed-carrier obstruction;
it is not a statement about all quartics or all curves.

## 6. Uniform conclusion and the corrected three-degree corollary

For a quartic pair, BF gives generic length b, top index `s=b-1`, and
at e=1 the exact top degree

    d_s=2*s-6=2*b-8.

Write `s=3q+r0`, where `q>=1,0<=r0<=2`. Superadditivity implies
`q*d3<=d_s=6q+2r0-6<6q`, so the integral degree satisfies
`d3<=5` for **every** b>=4. The principal orbit and all mixed members
of the two algebraic pencils are therefore excluded. Section 5 excludes
their pure members; section 4 excludes the unique-quadric orbit. This
proves the all-degree `e=1,D2=0` exclusion.

Even before the normalization argument, the lower bound five excludes
the requested small degrees, with these precise BF deductions:

| Mate degree | BF deduction when D2=0 | Bound |
|---:|---|---:|
| 6 | D2+D3=D5 | d3=4 |
| 7 | 2D3=D6 | d3=3 |
| 8 | D3+D4=D7 and D4>=D3 | d3<=4 |

The shorthand `d3<=b-4` is false at b=6 and must not replace this table.
Each correct bound is below five. No assertion about positive D2 follows
from these arguments: the primitive triple is the essential hypothesis.

## 7. Reproduction and boundaries

Run:

    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/audit_mf6_e1_primitive_2026_10_07.py
    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_mf6_e1_primitive_type04.py

The second source passed on 2026-10-07 in this audit. Its imported
`verify_mf6_defect12` module also prints earlier e=0 results; those
messages are dependency output and are not separate e=1 audit claims.
The first source is self-contained and exports a durable JSON beside
itself. The proof depends on complete exact rank computations for the
two-dimensional pencils; the normalization obstruction and BF upper
bound have direct proofs above.

The remaining e=1 quartic types in the MF6 degree-six problem are
`(d2,d3)=(1,3),(2,2)`. In larger mate degrees, positive D2 likewise
requires defective-triple gluing rather than the primitive direction
equations used here. This record preserves that open boundary.


---

## Source: 2026-10-07-session-mf6-e1-progress.md

# MF6 e=1 primitive-triple frontier

Date: 2026-10-07. Fixed C0, characteristic zero. **Status: structural
reconstruction and exact exploratory quartic data; no full e=1 exclusion
claimed at this checkpoint.** This continues the accepted e=0 type(4,5)
exclusion in `2026-10-06-session-mf6-progress.md`.

For e=1 the quotient of the balanced conormal bundle O(-7)^2 has
L=O(-6), kernel M=O(-8), and is specified by coprime homogeneous linear
sections A=a0+a1z, B=b0+b1z. Its projective basepoint-free condition is
`d=a0*b1-a1*b0 !=0`.

The exact moving-chart quadratic cocycle is

    h2=-(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5).

Its primitive triple obstruction lies in H1(O(-4)), so it vanishes iff
the coefficients of z^-1,z^-2,z^-3 vanish. These are

    -b1(2a0b1+12a1^2+16a1b0+9b0^2)/8,
    -(2a1+b0)(8a0b1+12a1^2+4a1b0+3b0^2)/8,
    -a0(2a0b1+36a1^2+16a1b0+3b0^2)/4.

Exact saturation by d supplies the relations
`a0(2a1+b0)=b1(2a1+b0)=0`. On the locus where at least one of a0,b1
is nonzero, both must be nonzero and the complete solution is

    a1=-b0/2, a0b1=-2b0^2, b0!=0.

After quotient scaling and the actual ambient torus symmetry, this is
represented by `A=1+z,B=-2-8z`. The torus acts on the split frame by
`U_new=lambda^4 U,V_new=lambda^3 V,z_new=lambda z`; after scaling the
quotient parameter this transports `(A,B)` to
`(lambda A(z_new/lambda),B(z_new/lambda))`, justifying the normalization
without assuming an arbitrary frame GL2 or support PGL2 symmetry.

On the remaining boundary a0=b1=0, basepoint freedom says a1b0!=0.
After b0=1 the solutions are

    A=r z,B=1,
    (2r+1)(12r^2+4r+3)=0.

Thus all primitive e=1 triples lie in four torus orbits. This
classification's quadratic cocycle and saturation are still to be added
to a standalone verifier and independently audited; do not generalize
the finite representative calculations to e=1 triples with positive D2.

On each primitive direction the embedded triple is unique, since
H0(Hom(M,L^2))=H0(O(-4))=0. In the first chart let gamma be the
nonnegative Laurent part of h2 and use the constant Bezout gauge
`s A+t B=1`, where `s=b1/d,t=-a1/d`. The actual triple embedding is

    U=A y-t gamma y^2,
    V=B y+s gamma y^2.

The full 18-dimensional quartic ideal basis, reconstructed from the
original homogeneous generators, gives the following complete spaces:

- At A=1+z,B=-2-8z, gamma=192z+96 and the space of quartics containing
  the triple has dimension two. Its full matrix and two quartics are in
  `../scratch/session-mf6-e1-primitive.json`.
- At A=-z/2,B=1, gamma=0 and the complete quartic space is
  `q*H0(P3,O(2))`, dimension ten. Every such carrier has the unique
  quadric factor; the retained unique-quadric STCI obstruction excludes
  this primitive direction from a defining pair.
- The two conjugate roots of 12r^2+4r+3 are being checked over the exact
  quadratic field. No conclusion for these roots is claimed yet.

The next question is the cubic pole divisor for the two-dimensional
quartic pencil of the first orbit, followed by the full conjugate-root
fibers. The MF6 type `(d2,d3)=(0,4)` permits cubic poles of total degree
four. Both moving support charts must be included. The types `(1,3)`
and `(2,2)` still require defect-killed triple incidence and are open.

## Complete classification without relying on the saturation output

Here is a direct case argument for completeness. Write
`p=a0*b1`, and retain `d!=0`.

If a0 and b1 are both nonzero, the first and third obstruction brackets
must vanish. Subtracting them gives
`6(2a1-b0)(2a1+b0)=0`. If `a1=b0/2`, the first bracket gives
`p=-10b0^2`, while the middle bracket then gives `b0=0`, contradicting
p!=0. Hence `a1=-b0/2`, and the remaining brackets give
`p=-2b0^2`; in particular b0!=0.

If a0!=0,b1=0, basepoint freedom gives a1*b0!=0. The third bracket and
the middle equation require either `2a1+b0=0`, which makes the third
bracket `4b0^2!=0`, or both quadratic brackets

    36a1^2+16a1b0+3b0^2=0,
    12a1^2+4a1b0+3b0^2=0.

Subtracting three times the second from the first forces
`a1=3b0/2`, which contradicts the second. Thus this case is empty.
If a0=0,b1!=0, the first bracket and middle equation similarly require
both `12a1^2+16a1b0+9b0^2=0` and
`12a1^2+4a1b0+3b0^2=0`, unless `2a1+b0=0` already contradicts the first.
Subtracting the two forces that same excluded relation. This case is
also empty. The remaining a0=b1=0 case gives exactly the three r roots
already displayed. Thus no basepoint-free primitive direction is omitted.

On the principal branch scale the quotient so b0=-2 and a1=1. Then
`a0*b1=-8`. The ambient torus sends a0 to lambda*a0 and b1 to
b1/lambda. Taking lambda=1/a0 gives the specified representative. On
the boundary the ratio r=a1/b0 is unchanged by that torus, so its three
roots are retained individually.

## Complete generic-orbit pencil and all cubic poles

At `A=1+z,B=-2-8z` the constant Bezout pair is
`s=4/3,t=1/6`. The complete coefficient matrix obtained by substituting
`U=A*y-t*gamma*y^2,V=B*y+s*gamma*y^2` into all eighteen quartics and
requiring the y and y^2 coefficients to vanish has rank sixteen. Its
full kernel is a pencil `F=alpha*F0+beta*F1`; the exact bases are
reconstructed rather than assumed in
`../computations/verify_mf6_e1_primitive_type04.py`.

Use `m=B U-A V`, `ell=s U+t V`. Their inverse transformation is
`U=t m+A ell,V=-s m+B ell`. The quartic first coefficient h and cubic
coefficient T, defined by

    m=-gamma ell^2+(T/h)ell^3+...,
    T=gamma E-K,

are exactly

    h=(4z^2+2z+1)(64alpha z^3+64beta z^6+8beta z^3+beta)/1024,
    T=(2z+1)(1536alpha z^5+1152alpha z^4+448alpha z^3
              +48alpha z^2-24alpha z+4alpha
              +1536beta z^8+1152beta z^7+448beta z^6
              +240beta z^5+120beta z^4+60beta z^3
              +30beta z^2+15beta z+8beta).

Since D2=0 and the primitive quadratic root is regular, the exact local
third-piece lattice lemma gives `ord D3=max(0,ord h-ord T)` in this
chart. This includes repeated zeros with their actual multiplicities.

For beta!=0 normalize beta=1. Then h has degree eight and

    Res_z(h,T)=-27(8alpha-1)(8alpha+3)^3/2^26.

Every parameter except `alpha=1/8,-3/8` has gcd degree zero, giving
finite polar degree eight. At alpha=1/8 the exact gcd is proportional
to `2z+1`, degree one, giving degree seven. At alpha=-3/8 it is
proportional to `(2z-1)^2`, degree two, giving degree six. These are all
exceptional pencil parameters, and each already exceeds the required
four without an infinity inference.

At beta=0 normalize alpha=1. The finite h has degree five and its gcd
with T has degree two, giving finite polar degree three. A direct second
chart is required because h, as an O(8) section, has an infinity zero.
Here

    A_infinity=1+w, B_infinity=-8-2w,
    s_infinity=-1/3,t_infinity=-1/6,
    gamma_infinity=3w+6.

Substitute into the actual ambient chart

    U'=t_infinity m'+A_infinity ell',
    V'=-s_infinity m'+B_infinity ell',
    x3=1,x2=w,x1=w^3+2U',x0=w^4+V'/2+3wU'.

The quartic has

    h_infinity=w^3(w^2+2w+4)/16,
    T_infinity=-(w+2)(w^2+2w+4)(3w^3+3w^2-4w+2)/16.

The second numerator is a unit at w=0, so infinity adds three exact pole
units and `deg D3=6`. The generic orbit therefore satisfies
`deg D3>=6` for every nonzero quartic containing its primitive triple.

## The quadric-factor orbit

At r=-1/2 the full coefficient matrix has rank eight, and its
complete kernel is `q*H0(P3,O(2))`, dimension ten. This also contains
some order-two forms, but every form has the unique quadric factor and
none can occur in a defining pair for C0. If q divides the mate the
pair has a common surface. Otherwise the mate cuts a nonempty divisor
on the smooth quadric of class `(b,b)`. If its support were the integral
C0 of quadric class `(1,3)`, it would have to be a positive multiple of
that class, which is impossible. This is the retained unique-quadric
obstruction, applied to a factor rather than only to a degree-two
carrier.

## The two algebraic direction orbits

Let `q_r=12r^2+4r+3=0`; its roots are nonzero and distinct in
characteristic zero. They are two conjugate directions, not identified
by the torus. Their exact quadratic cocycle is identically zero, so
both primitive triple charts have gamma=0.

Over the exact quadratic field the full eighteen-column triple matrix
has rank sixteen. Its kernel is the complete pencil spanned by

    F0=x0^3x3-(r+3/2)x0^2x1x2+(r+1/2)x1^4,
    F1=x0x3^3+(r-7/6)x1x2x3^2+(1/6-r)x2^4.

The rank assertion is over Q(sqrt(-2)); conjugation verifies the other
root. Every displayed polynomial identity is checked modulo q_r, so
no special root or extra kernel is omitted.

In the finite frame `m=U-r z V,ell=V`, the pencil has

    h=alpha+beta(2r+2/3)z^8,
    T=beta(8r/9)z^3,
    m=(T/h)ell^3+... .

Both r and `2r+2/3` are units modulo q_r. If alpha*beta!=0, h has no
zero at z=0 and T has no zero away from zero, so the total finite cubic
polar degree is eight. If alpha=0,beta!=0 it is five at z=0.

The last member beta=0 has h=1 in the finite chart, so its entire pole
calculation is on the moving second chart. Now

    A_infinity=r,B_infinity=w,
    U'=r ell', V'=w ell'-m'/r.

Direct expansion of F0 gives

    h_infinity=w^8,
    K_infinity=(16r/27+4/9)w^3,
    T_infinity=-K_infinity.

The scalar `16r/27+4/9` is a unit modulo q_r, so infinity contributes
exactly five pole units. Thus every member of either algebraic direction
orbit satisfies `deg D3>=5`.

## Result, precise scope, and current audit status

Together the four complete primitive direction orbits either force an
inadmissible unique-quadric factor or have `deg D3>=5`. Therefore the
MF6 numerical type `e=1,(d2,d3)=(0,4)` is excluded on fixed C0, subject
to the independent audit now in progress. No e=1 direction with positive
D2 is covered by this proof: those triples are not primitive and need
additional defect-killing sections.

The full verifier reconstructs the universal moving-chart quadratic
cocycle, checks the primitive-direction constraints and their coprime
boundary, derives every complete quartic fiber, proves the exact finite
resultant and exceptional gcds, and expands both infinity boundary
members directly. Its assertions are exact over Q or the quadratic
field, with all roots and all pencil members retained. The companion
stdout is `../scratch/session-mf6-e1-primitive-type04-output.txt`.
The source is being freshly rerun after replacing a structural equality
comparison of two differently arranged resultant expressions by their
zero polynomial difference. That correction changes no mathematical
input or assertion. Root delegated an independent audit to the
`dx1_saturation` agent; its outcome will be appended here.

The types `(1,3),(2,2)` remain open. A useful next analogue is the
intrinsic annihilator of their cubic residue: their permitted excess
`deg(D3-D2)` is two and zero respectively. The degree-one normal quotient
changes the second-frame complement by a kernel multiple, so its cubic
transition can contain a quadratic f2 term; the constant-direction
transition must not be transferred verbatim.


---

## Source: 2026-10-07-session-nonnormal-mf6-independent-audit.md

# Independent arbitrary-degree exclusion for four MF6 boundary carriers

Date: 2026-10-07. Status: **PROVED under the displayed coefficient and
characteristic hypotheses; independent algebraic audit**. This is a
fixed-carrier exclusion. It makes no claim that all nonnormal quartic
carriers, or the unrestricted C0 problem, have been excluded.

Let k be algebraically closed of characteristic zero, let

    P(b)=3b^2-2b+1=0, a=b+1,
    F0(b)=x0^3 x3-a x0^2 x1 x2+b x1^4,
    C0=[s^4:s^3t:st^3:t^4].

Neither b nor a vanishes. The two choices of b, and their coordinate
reversals, give the four carriers audited here. This note audits the
obstruction independently of the jet classification that produced them.

## 1. Finite birational normalization on the affine chart

On x3=1 put v=x2 and define a homomorphism into B=k[u,v] by

    x2=v,
    x1=u^2(a v-u)/b,
    x0=u x1.

Substitution annihilates F0. The affine F0 is primitive linear in x2:
the coefficient -a x0^2 x1 has greatest common divisor one with
x0^3+b x1^4. Therefore F0 is irreducible. The map's image has dimension
two: v is in the image, u is algebraic over its fraction field by the
monic equation below, and B has transcendence degree two. Thus its kernel
is exactly (F0), and its image is the coordinate ring A of this affine
surface.

The equation

    u^3-a v u^2+b x1=0

shows that B=A[u] is finite over A. On the dense open x1!=0 one has
u=x0/x1, so the map is birational. B is integrally closed. Moreover every
element of the common fraction field integral over A is integral over B
and hence belongs to B. Consequently B is exactly the normalization of
A. The argument uses a genuine finite normalization, rather than an
unverified parametrization.

## 2. The full inverse image of C0

On this chart I(C0)=(x1-v^3,x0-v^4). Write

    K=u^2-buv-bv^2.

The exact pullbacks satisfy

    x1-v^3=-(u-v)K/b,
    x0-v^4=u(x1-v^3)+(u-v)v^3.

Hence the full pulled-back ideal is (u-v)(K,v^3). The cofactor ideal
(K,v^3) has radical (u,v), since v=0 forces K=u^2. That residual point
already lies on u=v. Thus the **entire** reduced inverse image of C0 on
this affine chart is the diagonal u=v. No isolated point or additional
curve has been dropped. The diagonal maps isomorphically to C0 here:
its coordinates are (v^4,v^3,v).

## 3. A mate would violate equality on a normalization fiber

Suppose a homogeneous surface G of any positive degree is an STCI mate
for F0 and C0. Its affine restriction pulls back to a nonzero polynomial
g in B. It cannot vanish identically: this affine open is dense in the
integral carrier and a mate cannot contain that whole carrier. The
support equality from section 2 gives V(g)=V(v-u). Unique factorization
in k[u,v], and the fact that its only units are nonzero constants, force

    g=c(v-u)^n, c in k*, n>0.

For every v the two normalization points (0,v) and (a v,v) have exactly
the same original coordinates (0,0,v). Since g belongs to the original
coordinate ring A, it has equal values at these points. Therefore

    c v^n=c(-b v)^n, and (-b)^n=1.

The polynomial P is irreducible over Q, has discriminant -8, and its
other root is b*=2/3-b. Its quadratic-field norm is b b*=1/3.
Conjugating b^n=(-1)^n and multiplying yields (1/3)^n=1. This is
impossible for a positive integer n in characteristic zero. The
conjugation is used only inside Q(b); no automorphism of the whole
algebraically closed field is assumed.

Thus F0(b) admits no mate of any degree. This is stronger than the
degree-six cubic-defect obstruction for these particular carriers.

## 4. The other two carriers and exact verification

The displayed second pencil member is

    F1(b)=x0 x3^3+(b-5/3)x1 x2 x3^2+(2/3-b)x2^4.

It is exactly the coordinate reversal of F0(b*), interchanging
(x0,x1,x2,x3) with (x3,x2,x1,x0). The reversal preserves C0 by
interchanging s and t. Both roots b* again satisfy P. Therefore the
same obstruction excludes both F1 carriers.

The companion
[exact verifier](../computations/verify_session_nonnormal_mf6_fiber_obstruction.py)
checks the monic equation, pullback, primitive coefficient gcd,
full-support ideal identities, duplicate fiber coordinates, quadratic
norm and exact reversal identity. The argument for arbitrary n is the
symbolic norm proof in section 3, not a finite power search.

These statements require characteristic zero. Reduction modulo primes
can make b a root of unity; that possibility is intentionally retained.
The obstruction does not cover a general member alpha F0+beta F1 with
alpha beta!=0, or a different nonnormal carrier on C0.


---

## Source: 2026-10-07-session-nonnormal-structural-progress.md

# Nonnormal quartic carriers: smooth-locus reduction and ordinary projections

Date: 2026-10-07. Status: **PROVED lemmas and conditional exclusions;
classification scope and surviving singular strata retained**. The
unrestricted nonnormal-quartic lane remains open. No canonical frontier
file is edited by this note.

Throughout the proved lemmas, k is algebraically closed of characteristic
zero. Let X be an integral quartic containing a smooth rational curve C
of degree four, and assume X is regular at the generic point of C. This
includes the displayed MF6 carriers in the
[separate arbitrary-degree audit](2026-10-07-session-nonnormal-mf6-independent-audit.md).
Write nu:S->X for its finite normalization and H=nu*O_X(1).

## 1. Full support makes the lifted curve an embedded copy of C

Over the generic point of C the normalization is an isomorphism.
Consequently the full inverse image has exactly one curve component c,
finite and birational over C, together with possible isolated points.
The reduced curve c is isomorphic to C: an integral finite birational
extension of the integrally closed coordinate ring of a smooth curve
inside its function field is that coordinate ring itself.

If a mate G exists, its nonzero pullback is an effective Cartier divisor
whose full support is (nu^{-1}(C))_red. The
[full-support argument](2026-10-06-session-conductor-support.md) excludes
isolated inverse-image points. Therefore this entire support is c.
Every fiber above C has exactly one point, and nu|c is an isomorphism.

Write div_S(nu*G)=m c. If b=deg G, intersection with H gives

    4m=H.(m c)=H.(bH)=4b, hence m=b.

Thus b c is Cartier and linearly equivalent to bH as a Weil divisor.
This conclusion retains the support and finite-map hypotheses; it does
not assume all nonnormal carriers have a unique curve above C.

## 2. Smoothness is needed only along c

**Lemma.** If c lies entirely in the smooth locus of S, existence of a
mate forces the normalization's hyperplane sectional genus to be zero.

The divisor c is Cartier: near c the surface is smooth, and outside c
its defining ideal is the unit ideal. Thus b(c-H) is linearly trivial
and c is numerically equivalent to H. Choose a resolution sigma:M->S
which is an isomorphism near c, and let c# be its strict transform.
Then c# is a smooth rational curve and is numerically equivalent to
sigma*H. In particular c#^2=H^2=4. Adjunction gives

    K_M.c#=-6, so K_M.sigma*H=-6.

A general member of |H| is smooth, irreducible and avoids the finitely
many singular points of S; its inverse image in M has class sigma*H.
Its genus is therefore 1+(4-6)/2=0. This argument does **not** require S
to be globally smooth. No ADE or semi-log-canonical assumption is used.

**ADE variant.** Suppose instead that S has only ADE singularities and
take its minimal crepant resolution. Write its numerical pullback as
c#+Z equivalent to sigma*H, with Z the rational exceptional correction.
Put q=-Z^2=c#.Z. Since K_M is orthogonal to all exceptional curves,
K_M.c#=K_M.sigma*H. If pi is the hyperplane sectional genus, adjunction
gives

    c#^2=4-2pi, and q=2pi.

The formula is a necessary numerical condition. The existence of the
mate ensures that the correction is a rational divisor; no assertion of
Cartierness of c at the ADE points is made. Strict transforms of the
smooth curve stay isomorphic to C: the point-center ideals restrict to
nonzero invertible ideals on C during a resolution.

## 3. Source-scoped quartic classes

[Ducat, Quartic surfaces up to volume preserving equivalence (2024),
Proposition 3.3 and Table 3](https://d-nb.info/1317691679/34), pp.12-13,
records the following rational **semi-log-canonical** nonnormal classes,
using a smooth resolution M and H=d h-sum m_i e_i:

| Class | Double curve | H on M | K_M.H | pi |
|---|---|---|---:|---:|
| B1 | line | 4h-2e1-e2-...-e9 | -2 | 2 |
| B2 | conic | 3h-e1-...-e5 | -4 | 1 |
| B3 | twisted cubic | 3h-2e1-e2 | -6 | 0 |
| B4 | three concurrent lines | 2h | -6 | 0 |

These genera are derived here from H^2=4 and adjunction. Hence a B1 or
B2 carrier whose lifted C avoids normalization singularities is excluded
in every mate degree. For ADE normalizations the necessary values are
q=4 and q=2. The B3 normalizations are quartic rational scrolls; B4 uses
P2 polarized by O(2). The source theorem assumes semi-log-canonical
singularities over C; it is not an exhaustive theorem for arbitrary
nonnormal quartics. The original Urabe DOI/Project Euclid endpoints were
not readable in this audit, so broader classification is not promoted.

Two tempting transfers are invalid without further proof. A section of
a smaller degree on S need not descend through the conductor to X, so
the normal-carrier compressed mate exclusions cannot simply be reused.
An ADE singularity of S lying on its conductor is not an ADE local
hypersurface point of X; Jaffe's first-normal orders for X cannot be
assigned to it merely from the normalization graph.

## 4. Ordinary pinches force transverse conductor passage

In the ordinary pinch model the normalization is

    (u,v) -> (x,y,z)=(uv,u,v^2),
    X: x^2-y^2 z=0, D: u=0 upstairs.

At the pinch point the derivative of the image of a parametrized lifted
curve is (0,u',0). A smooth embedded image therefore requires u'!=0.
The lift meets D transversely, with local intersection multiplicity one.
At an ordinary double point there are two points in the normalization
fiber, contrary to section 1. The same full-support obstruction removes
ordinary triple points.

Consequently, if every singleton normalization fiber on the conductor
of a smooth normalized surface occurs at an ordinary pinch, and no
other singleton degeneration can meet C, a mate requires

    H.D <= number of ordinary pinch points.

This is an **ordinary-singularity hypothesis**, not a bound for all
semi-log-canonical degenerations.

For a projected quartic scroll with smooth anticanonical conductor D
mapping two-to-one onto its smooth twisted-cubic double curve, H.D=6.
The conductor is elliptic, and Riemann-Hurwitz gives four branch points.
If those points are ordinary pinches, section 4 requires six distinct
pinches and gives a contradiction. Thus this ordinary projected-scroll
subclass has no mate of any degree.

## 5. Ordinary projected Veronese surfaces

Suppose S=P2, H=O(2), and the normalization map is given by four
basepoint-free quadrics q0,...,q3. Assume its conductor is a reduced
anticanonical cubic and its singleton conductor fibers are ordinary
pinches; assume the homogeneous ideal of the maximal minors of the
4-by-3 derivative matrix has height two and defines reduced points.
These hypotheses describe the ordinary projection subclass. They do
not assert that every projected Veronese has ordinary singularities.

A mate forces the lifted c to be a conic: b c is linearly equivalent to
2b times a line and Pic(P2) is torsion free. Its conductor intersection
has degree six. Full inverse support and section 4 force six distinct
pinch preimages on c.

Let J=(partial q_i/partial x_j). Euler's formula gives J(x,y,z)^T=2q.
Since q never vanishes simultaneously, rank(J)<3 is exactly failure of
the projective differential to have rank two. Thus its maximal minors
cut out the ramification scheme R. The height-two hypothesis permits
the Hilbert-Burch resolution

    0 -> O_P2(-4)^3 -> O_P2(-3)^4 -> I_R -> 0.

It gives length R=6 and H0(I_R(2))=0. For example its Hilbert numerator
is 1-4t^3+3t^4, whose coefficient after division by (1-t)^2 at t=1
is six. Twisting the displayed sheaf resolution by two also directly
gives the no-conic assertion, since H1(P2,O(-2))=0. The
[author-hosted Hilbert-Burch statement with proof](https://ssather.people.clemson.edu/DOCS/HomAlgBook.pdf),
Theorem III.B.5.10, supplies this standard algebraic input.

The six distinct pinches are all six points of the reduced R. A conic
through them would contradict H0(I_R(2))=0. Therefore every carrier
meeting these ordinary-projection hypotheses is excluded in every
mate degree.

An explicit independent control is the standard Roman normalization

    [x:y:z] -> [yz:zx:xy:x^2+y^2+z^2].

This map is finite because its pullback O(1)=O(2) is ample and there is
no basepoint. On xyz!=0 its first three coordinates recover [x:y:z],
so it is birational and P2 is its normalization. The coordinate axes
are the conductor lines; their double maps have precisely the six
fixed points

    (0,1,+/-1), (1,0,+/-1), (1,+/-1,0).

The coordinate vertices have a common image and cannot meet C. Each
axis has exactly its two ordinary fixed pinches as singleton fibers.
A conic through the six fixed points has all cross coefficients zero
and its diagonal coefficients satisfy A+B=A+C=B+C=0. In characteristic
zero it is the zero form. Thus the explicit Roman carrier has no mate
for a smooth rational quartic, independently of the general resolution
calculation.

## 6. Why nodal conductor degenerations remain

At a degenerate pinch the normalization can be smooth with coordinates
(w,z) and map

    Y=-(w^2+z^2), X=wY, Z=z,
    X^2+Y^2(Y+Z^2)=0.

This is a finite birational normalization: w satisfies the monic
equation w^2+Y+Z^2=0 and equals X/Y in the common function field;
k[w,z] is integrally closed. The original hypersurface polynomial is
irreducible, for its expression as a quadratic in X has nonsquare
coefficient -(Y+Z^2) after removing the square factor Y^2.

The conductor upstairs is the nodal divisor w^2+z^2=0. Its two branches
map onto Y=X=0 with the same coordinate z, and the point w=z=0 has a
single normalization preimage. For every integer k>=2, the lifted curve
w=i z+z^k maps to a smooth curve, since Z=z is its parameter, but its
conductor intersection multiplicity is k+1. It has full inverse-image
support equal to that lifted curve locally: writing w_c=i z+z^k, the
pulled-back image ideal is

    (w-w_c)(w+w_c,Y_c), Y_c=-(w_c^2+z^2).

The cofactor's support at this germ is only (w,z)=(0,0), already on the
curve. Thus conductor contact at
a singleton degeneration can be arbitrarily large even for a smooth
embedded image.

This exact countermodel prevents replacing the hypotheses in sections
4-5 with just a count of branch-point supports, or replacing containment
of the full ramification scheme by passage through its reduced support.
The nonreduced ramification strata, degenerate cusps, singular
normalizations and non-semi-log-canonical carriers remain unresolved.

The companion [exact control verifier](../computations/verify_session_nonnormal_structural.py)
checks the four source-table genus calculations, Roman Euler/minor and
no-conic identities, and the degenerate-pinch contact calculation.
