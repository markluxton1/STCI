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
