# Projection support and differential obstructions

Work over an algebraically closed characteristic-zero field with the fixed embedded curve `C0=[s^4:s^3t:st^3:t^4]`. The examples below separate two independent failure mechanisms in the necessary Cartier singleton models of [R-0002](../results/cartier_singleton_lift.md): actual full inverse support can pass while infinitesimal descent fails; another actual projection can fail because of isolated inverse points. Neither family exhausts its normalization model.

The plane result and its broader two-fixed-coordinate sublane are [R-0017](../results/singleton_plane_conductor_descent.md). The quadric families have completed independent source reconstruction and retain their stated review scopes. The exposition integrates the original proofs and the audit's unique denominator and extra-corner corrections. No symbolic computation is a premise.

## Plane normalization: actual support but no descending power

## 1. An explicit finite normalization

On `P2_(s:t:z)` put `c=(z=0)`, and define

    U0=s^4,
    U1=s^3 t,
    U2=s t^3+z^4,
    U3=t^4+s^3 z.                                      (1)

The four sections are basepoint free. If `s!=0`, `U0!=0`; if `s=0`,
the two possibly nonzero coordinates are `z^4,t^4`, which cannot vanish
together at a projective point. Thus they define a morphism

    f:P2 -> P3,             f*O(1)=O(4).

This morphism is finite. A positive-dimensional projective fiber contains
a curve, but `O(4)` would have degree zero on that curve, contradicting
ampleness. Properness and finite fibers imply finiteness.

On `s!=0`, write `x=t/s`, `n=z/s`, and use the target chart `X0!=0`.
Then

    f(x,n)=(x, x^3+n^4, x^4+n),
    x=X1/X0,
    n=X3/X0-(X1/X0)^4.                                 (2)

In particular the map is birational and is an isomorphism on this affine
chart. Its integral image `X` is a hypersurface, and the finite birational
map from normal `P2` is its normalization. The degree formula gives
`deg X=O(4)^2=16`.

For a completely explicit equation put

    A=X0^3 X3-X1^4,
    B=X0^2 X2-X1^3.

Then the image is exactly

    F=A^4-X0^13 B=0.                                   (3)

Indeed its dehomogenization at `X0=1` is

    (X3-X1^4)^4-X2+X1^3=0,

an irreducible polynomial linear in `X2`. Equation (3) is its degree-sixteen
homogenization, with no factor `X0` since `F|X0=0=X1^16`. This also checks
the degree and the signs directly. On the source,

    f*A=s^15 z,             f*B=s^8 z^4.

## 2. Full reduced inverse support, including infinity

Restriction to `z=0` gives exactly `C0`. Its parametrization is an
isomorphism: the coordinates `X1/X0=t/s` and `X2/X3=s/t` provide the
two endpoint parameters.

On `s!=0`, membership of the image in `C0` forces

    x^3+n^4=x^3,            x^4+n=x^4,

so `n=0`. On `s=0`, the image is `[0:0:z^4:t^4]`. The only point of
`C0` with its first coordinate zero is `[0:0:0:1]`; thus the image lies
on `C0` exactly when `z=0`. Consequently

    (f^-1 C0)_red=c,             f|c:c -> C0 is an isomorphism. (4)

There are no isolated extra inverse points. This is an actual realization
of the full-singleton plane normalization model before the mate condition.

## 3. Every positive mate degree is excluded

Suppose a homogeneous form `G` of positive degree `b` cut out exactly
`C0` set-theoretically on `X`. Its pullback is a nonzero section of
`O_P2(4b)` whose zero support, by (4), is exactly `c`. Its divisor must
therefore be `4b c`, and

    G(U0,U1,U2,U3)=lambda z^(4b),       lambda in k*.     (5)

Rescale `G` to make `lambda=1`. Set `s=0`. Since the map
`[t:z] -> [z^4:t^4]` is surjective onto `P1`, equation (5) forces the
polynomial identity

    G(0,0,Z,T)=Z^b.                                    (6)

Differentiate (5) in `s` and set `s=0`. The first, second, and fourth
coordinates in (1) have zero derivative there. The third has derivative
`t^3`; by (6), `G_X2|X0=X1=0=b X2^(b-1)`. Thus

    0=b t^3 z^(4b-4),                                  (7)

an impossible polynomial identity in characteristic zero.

**Conclusion (R-0017):** the integral degree-sixteen carrier (3) contains
literal `C0`, has the required Cartier singleton degree-one inverse lift,
and has no set-theoretic mate in any positive degree.

This excludes this carrier, not all integral degree-sixteen carriers.

## 4. An eleven-parameter family with the same obstruction

Let `alpha!=0` and let `P(s,t,z)` be an arbitrary homogeneous cubic. Replace
(1) by

    U0=s^4,
    U1=s^3 t,
    U2=s t^3+alpha z^4,
    U3=t^4+z P(s,t,z).                                 (8)

There are eleven affine coefficients before quotienting coordinate
equivalences: one for `alpha` and ten for `P`. Every member is basepoint
free and finite by exactly the preceding argument. Its restriction to
`c` is the literal `C0`. On `s!=0`, the third coordinate forces `n^4=0`
for any inverse point over `C0`, hence `n=0`. On `s=0`, `U2=alpha z^4`
forces `z=0` for an image on `C0`. Thus every member has full reduced
inverse support exactly `c`; birationality is considered separately below.

The boundary map is

    [t:z] -> [alpha z^4 : t^4+zP(0,t,z)].                (9)

It is basepoint free and has degree four. In particular it is surjective.
If (5) held for (8), restriction to `s=0` would force

    G(0,0,Z,T)=(Z/alpha)^b.                             (10)

The derivative `G_X3` therefore vanishes on the entire boundary plane
`X0=X1=0`. Thus the arbitrary value of `zP_s(0,t,z)` contributes zero
when differentiating the pullback identity. The same calculation gives

    0=(b/alpha)t^3 z^(4b-4),                            (11)

again impossible. Every member of (8), including the nonbirational
members, has no mate on its image. Only its birational members belong to
the degree-sixteen normalization model in STCI-Q-0001.

## 5. Exact birational locus of (8)

Write uniquely

    P=A3(s,t)+zB2(s,t)+z^2 C1(s,t)+delta z^3.

Over `K=k(x)`, where `x=t/s`, the target function field is generated by

    n^4,
    A3(1,x)n+B2(1,x)n^2+C1(1,x)n^3+delta n^4.           (12)

The extension `K(n)/K(n^4)` is Galois with group `mu4`, acting by
`n -> zeta n`. The fixed subgroup of the second generator in (12)
consists precisely of those `zeta` for which every nonzero coefficient
of `n^j` has `zeta^j=1`. Therefore

- If `A3!=0` or `C1!=0`, the map is birational, and its image has degree 16.
- If `A3=C1=0` and `B2!=0`, its generic degree is 2 and image degree is 8.
- If `A3=B2=C1=0`, its generic degree is 4 and image degree is 4.

These degrees refer to the function-field degree of `P2` over its image.
For the second and third cases `P2` is not the normalization of the image;
they are not extra normalizations in STCI-R-0002. The first case is the
nonempty explicitly determined open locus of actual normalizations within
this family. The all-degree obstruction (11) holds throughout that locus.

## 5a. Every full-singleton projection with the first two coordinates fixed

There is a stronger exclusion than the explicit family (8). Consider any
four sections of `O_P2(4)` with

    U0=s^4,              U1=s^3 t,
    U2=s t^3+z A3(s,t,z),
    U3=t^4+z B3(s,t,z),                                (15)

where `A3,B3` are arbitrary cubics. Suppose they are basepoint free and
have full reduced inverse support of `C0` exactly `c=(z=0)`. Then no
positive-degree mate exists on their image. If the map is birational,
this is a degree-sixteen normalization exclusion within STCI-Q-0001.

Proof. On the line `D=(s=0)`, every point with `z!=0` must have `U2!=0`.
Otherwise its image, whose first two coordinates vanish, would either be
the forbidden extra inverse point `[0:0:0:1]` or fail to be defined.
Thus the binary cubic `A3(0,t,z)` has no projective zero except possibly
`z=0`. Over the algebraically closed field this forces

    A3(0,t,z)=alpha z^3,              alpha!=0.

Write `A3=alpha z^3+s C2(s,t,z)`. Restricting a hypothetical identity
`G(U)=z^(4b)` to `D` again forces (10), because its boundary map is
basepoint free of degree four. Differentiating in `s` now gives

    0=(b/alpha)z^(4b-4)[t^3+z C2(0,t,z)].               (16)

The bracket is nonzero: its coefficient of `t^3` is one, while its
second term is divisible by `z`. This proves the all-degree exclusion.

The condition fixing `U0,U1` is literal and restrictive; no claim is made
that an arbitrary plane normalization can be put into (15) while
preserving literal `C0`. The surviving full-support locus inside (15)
is not classified here. The proof only shows that its members all fail
the required descent.


## A reduced-trivial phase with a nonzero nilpotent defect

The following generic local calculation includes arbitrary localized denominators; testing polynomial generators alone would not prove nonmembership.

### B. Generic local ring and denominator check

For a birational member of the explicit eleven-parameter family (8), let `D=(s=0)`, and work in
the source chart `z=1` with coordinates `r=s/z,y=t/z`. The source local
ring at the generic point of `D` is the DVR

    B=k[r,y]_(r)=k(y)[r]_(r),    E=B/(r)=k(y).

The target affine coordinate ring in the chart `X2!=0` is the subring
`A=k[a0,a1,w]` of its function field, with

    a0=r^4/(alpha+r y^3),
    a1=r^3 y/(alpha+r y^3),
    w=(y^4+P(r,y,1))/(alpha+r y^3).

The image line `ell` has prime `p=(a0,a1)` and `A/p=k[w]`: it is indeed
the entire line, because the boundary morphism to it is surjective. Its
residue coordinate pulls back to

    w0=g(y)/alpha,    g(y)=y^4+P(0,y,1).

The polynomial `g` has degree exactly four because `P` has total degree
three. Thus `w0` is transcendental over `k`, and the target residue field
`K=k(w0)` embeds in `E` with degree four. The nontrivial residue extension
proves nonnormality at the generic point of `ell`, so `D` is a conductor
prime. Also `f^{-1}(ell)` has reduced support only `D`, since `U0=s^4`;
there is no second inverse prime over the generic point of the line.

Take an arbitrary element of the target local ring `A_p`. Write it as

    N(a0,a1,w)/M(a0,a1,w),    M notin p,

using polynomial representatives. The denominator's restriction
`M(0,0,W)` is a nonzero polynomial. Substitution `W=w0` is injective, so
this denominator has nonzero residue and is invertible in `B/(r^2)`.
Because `a0,a1` vanish modulo `r^2`, the image of this localized element
in `B/(r^2)` is exactly

    R(w),    R(W)=N(0,0,W)/M(0,0,W) in k(W).

This establishes the asserted form for all localized elements, including
those with denominators; no polynomial-only assumption is hidden. If its
residue is the constant `alpha^(-b)`, injectivity of `k(W)->E`,
`W->w0`, forces the rational function `R` itself to be that constant.
Consequently the element has zero coefficient of `r` modulo `r^2`.

In contrast,

    q^b=(alpha+r y^3)^(-b)
       =alpha^(-b)-b alpha^(-b-1)y^3 r mod r^2,

has nonzero linear coefficient for every positive `b`. Thus `q^b` is not
in `A_p`, even though its residue `alpha^(-b)` lies in `K*` and is the
identity class of `E*/K*`. This is an exact first-order obstruction at the
actual generic conductor prime. It does not require knowing which power
of `(r)` equals or lies in the conductor ideal.

For the explicit member (1) the affine chart `s!=0` is an isomorphism, by
the explicit inverse already checked. The generic nonnormality along
`D`, together with this isomorphism off `D`, proves that the entire
conductor support upstairs is `D`. No scheme multiplicity is inferred,
and no analogous entire-support assertion is justified here for arbitrary
`P`.

The differential lemma and this generic local calculation are therefore
independently reviewed with the literal hypotheses above. Their scope is
an obstruction and an explicit family calculation, not a computation of
the full plane-model phase image or a general exclusion of that model.


For the explicit member (1), the differential test in [full conductor algebra, §6](CONDUCTOR_DESCENT_ALGEBRA.md#6-differential-obstruction-on-a-prescribed-cartier-ray) applies at `(r,y)=(0,1)` with frame U2. There `q=1/(1+ry^3)`, the target differentials satisfy `da0=da1=0`, `dw=-dr+4dy`, and `v=partial_r+(1/4)partial_y` has `dq(v)=-1`. This geometric proof and the polynomial derivative proof detect the same obstruction at different levels and are both retained.

## Smooth quadric: isolated inverse points prohibit every mate

On `S=P1_(s:t) x P1_(u:v)`, put `q=sv-tu`, `p=sv+tu`, `c=(q=0)`, and `H=O(2,2)`. The two systems are

    U0=s^2u^2+q tv/2, U1=su p/2, U2=tv p/2,
    U3=t^2v^2+kappa q^2,
    kappa!=0, kappa^3!=-1/64;

and the companion family

    V0=s^2u^2+q tv/2+gamma q^2, V1=su p/2,
    V2=tv p/2, V3=t^2v^2, gamma!=0.

Both restrict on c to the literal C0. Both are finite normalizations of integral degree-eight hypersurfaces, but c is not the full inverse support. The following proves every parameter boundary, the rational inverses, and the isolated-point obstruction.

## 1. Basepoint-free locus and finiteness of the kappa family

Write `p=sv+tu`, `q=sv-tu`. Vanishing of both middle coordinates gives
either `p=0`, or `su=tv=0`. The latter locus consists of exactly the two
cross-corners

    ((0:1),(1:0)),       ((1:0),(0:1)).

At both, `q!=0`, and `U3=kappa q^2`. Thus these are not basepoints when
`kappa!=0`; both are basepoints when `kappa=0`.

The antidiagonal `D=(p=0)` is parametrized globally by
`(s:t)=(a:b), (u:v)=(a:-b)`. Its nonzero coordinate candidates are exactly

    U0=a^4+ab^3,           U3=b^4+4kappa a^2b^2.

At `a=0` or `b=0`, one of these is nonzero. Otherwise putting `x=b/a`
gives a simultaneous zero precisely when

    x^3=-1,               x^2=-4kappa.

These imply `kappa^3=-1/64`; conversely `x=1/(4kappa)` solves both
equations on that parameter locus. Hence the two stated exclusions are
the exact basepoint-free conditions, including all boundary charts.

The resulting projective morphism pulls back `O(1)` to the ample bundle
`O(2,2)`. A positive-dimensional fiber would contain a complete curve on
which this ample bundle has degree zero, which is impossible. Properness
and zero-dimensional fibers therefore give finiteness.

## 2. Birationality and degree of the kappa family

On `s=u=1`, set `x=t`, `y=v`, `r=xy`, `d=y-x`, `P=x+y`. Direct
substitution independently gives

    (U0,U1,U2,U3)=(1+dr/2,P/2,rP/2,r^2+kappa d^2).

For `z_i=Ui/U0`, `lambda=U0`, and `r z1!=0`, one has

    r=z2/z1,  P=2lambda z1,  d=2(lambda-1)/r.

Using `P^2-d^2=4r` produces

    (1-r^2 z1^2)lambda^2-2lambda+1+r^3=0.

The fourth coordinate then gives

    4kappa z1^2 lambda^2-z3 lambda+r^2-4kappa r=0.

Eliminating the quadratic term yields

    lambda=[(1-r^2 z1^2)(r^2-4kappa r)-4kappa z1^2(1+r^3)]
           /[(1-r^2 z1^2)z3-8kappa z1^2],

with denominator `(1-r^2z1^2)z3-8kappa z1^2`. At `x=0,y=1`, this
rational function is defined and equals `-kappa`. Although `r=0` there,
this evaluation is used solely to prove nonidentity of the denominator;
it is not asserted to lie in the inverse chart. Because `S` is integral,
the simultaneous nonvanishing inverse conditions have a nonempty dense
intersection. Recovering `x=(P-d)/2`, `y=(P+d)/2` proves birationality for
every nonzero `kappa`; no further exceptional parameter occurs.

The finite birational morphism from normal `S` is the finite normalization
of its integral image. Finiteness makes the image a surface, hence an
integral hypersurface in `P3`. The degree formula gives
`deg X=H^2=(2,2)^2=8`.

## 3. Full inverse-support obstruction in the kappa family

Restriction to `c` gives the prescribed four quartic coordinates. The
parametrization of `C0` is an isomorphism: on the two endpoint charts its
local parameters are respectively `X1/X0=t/s` and `X2/X3=s/t`.

On `D`, the two degree-four sections above have no common zero on the
admissible parameter locus. They define a degree-four map to
`L=(X1=X2=0)`. Characteristic zero ensures four distinct geometric points
in its generic fiber. Its degree-four residue extension means the finite
normalization is not an isomorphism at the generic point of `L`; therefore
`D` belongs to the actual conductor support. This is a curve on `S`
mapping to a curve on `X`, not a vertical exceptional divisor.

The two roots of `b^2+4kappa a^2=0` give two distinct off-diagonal points
on `D` over `[1:0:0:0]`. The three roots of `a^3+b^3=0` give three
distinct off-diagonal points on `D` over `[0:0:0:1]`. Each has `ab!=0`,
and the other nonzero coordinate follows from basepoint-freeness. Thus the
claimed lower bound of five is valid for every admissible `kappa`.
Additionally, the two cross-corners from the basepoint calculation also map to
`[0:0:0:1]`, giving seven forced endpoint extras. The source's lower bound
does not claim an exact total count.

To check that no other inverse curve absorbs these points, take any
nonendpoint target `[1:z:z^3:z^4]`. Then `z!=0`, `U1,U2!=0`, so all four
source coordinates are nonzero, and the affine calculation applies. For
an off-diagonal inverse point one has `r=z^2`, `d!=0`, `lambda!=1`, and

    kappa d^2=(lambda-1)r^2,
    d^2=4r(lambda^2-1),
    d=2(lambda-1)/r.

Cancelling only the already nonzero factors gives

    r=4kappa(lambda+1),
    lambda-1=64kappa^3(lambda+1)^4,
    z^2=r.

The polynomial in `lambda` is nonzero for every `kappa!=0`. It admits
only finitely many values of `lambda`, and then only finitely many `z`.
Boundary points with `su=0` have `U1=0` and cannot lie over a nonendpoint.
Every curve in the inverse support of `C0` must map onto `C0`, because
the morphism is finite. Hence `c` is the sole curve component, and the
extra points outside it are isolated in the full inverse support. This
argument is uniform on the entire stated parameter locus.

## 4. Companion family: exact full inverse support

For the companion family, `V3=0` forces `t=0` or `v=0`. At `t=0`, the equation `V1=0`
forces `uv=0`; the respective nonzero coordinates are `s^2u^2` or
`gamma s^2v^2`. At `v=0`, the two cases similarly give `s^2u^2` or
`gamma t^2u^2`. Thus every `gamma!=0` is basepoint-free, with no further
condition. Ampleness again gives finiteness.

On the affine chart the coordinates are

    (1+dr/2+gamma d^2,P/2,rP/2,r^2).

Recover successively

    r=z2/z1, lambda=r^2/z3, P=2lambda z1,
    D=P^2-4r, d=2(lambda-1-gamma D)/r.

Since `D=d^2` on the image, this proves the rational inverse
without any square-root choice. Its nonvanishing conditions are dense;
for example `x=y=1` satisfies them for every `gamma`. Thus every
`gamma!=0` gives the claimed degree-eight integral carrier and finite
normalization.

For every nonendpoint point `[1:z:z^3:z^4]`, these identities force
`r=z^2`, `lambda=1`, `P=2z`, `D=d=0`. Its unique inverse point is on
`c`; the boundary cannot occur because `V1,V2` are nonzero.

Over `[1:0:0:0]`, the preceding boundary calculation gives exactly the
diagonal endpoint and the two cross-corners. Over `[0:0:0:1]`, `tv!=0`
and `V2=0` force `p=0`; the antidiagonal parametrization gives exactly
the diagonal endpoint `a=0` and the roots

    1+4gamma x^2+x^3=0,           x=b/a.

All roots are finite and nonzero. The discriminant is
`-256gamma^3-27`. If it vanishes, the repeated root is `x=-8gamma/3`,
and the second derivative there is `-8gamma!=0`, so it is exactly
double. There are therefore exactly three distinct extra points from
this cubic, or exactly two when `gamma^3=-27/256`. Together with the two
cross-corners, this proves the asserted entire reduced inverse support:
five isolated extras ordinarily, and four on the exceptional parameter
locus. In particular `gamma=1` has exactly five.

On `D`, the sections `a^4+ab^3+4gamma a^2b^2` and `b^4` have no common
zero. The degree-four map to `L` and the conductor-prime conclusion
follow exactly as in the preceding conductor calculation.

## 5. Every mate degree and the precise frontier boundary

If a homogeneous form `G` of positive degree `b` cut out exactly `C0`
on either carrier, its restriction and pullback would be nonzero sections.
The zero support of the pullback on smooth `S` would be the complete
inverse support of `C0`, including its isolated points. A nonzero section
of a line bundle on a smooth integral surface defines an effective
Cartier divisor, whose support has pure codimension one. This is
impossible. Equivalently, since `c` is the only inverse curve, the
pullback divisor must be `m c`; in `Pic(S)=Z^2`, comparison with
`bH=(2b,2b)` gives `m=2b`, and this divisor misses every off-`c` point.
Thus the exclusions hold in every positive mate degree.

The first-jet claim also checks directly: in both families
`L0|c=x^2/2`, while `L1|c=L2|c=L3|c=0`. The balanced formulas give
`A=x^5`, `B=0`, with homogeneous common-zero divisor `5(t=0)`.
The inverse-support conclusions above use the actual maps and do not
follow merely from these jets.

These explicit subfamilies provide actual carrier constructions and
completed, reviewed all-degree exclusions within their stated parameter
sets. They neither exhaust the sixteen-parameter smooth-quadric family
nor decide either other model in STCI-R-0002. No surviving full-support
conductor phase image is computed. STCI-Q-0001 and the unrestricted
characteristic-zero question remain open.


## Characteristic boundary

The map and support identities are polynomial geometric calculations. The plane all-power contradiction uses the nonvanishing of the positive degree b in the field. In characteristic p it excludes only degrees prime to p (indeed all b not divisible by p); the differential of a p-th power is zero. Thus this proof supplies no all-degree positive-characteristic exclusion. The two quadric inverse formulas and support calculations require 2 invertible; their displayed parameter separability and root counts must additionally be checked in any selected positive characteristic. The complete characteristic-zero families remain the reviewed statements. The [positive-characteristic construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) uses a quartic carrier for this fixed curve. The [arithmetic plane-source treatment](ARITHMETIC_EQUATIONS_AND_JET_GAPS.md) also proves actual Frobenius descent on the explicit degree-sixteen plane carrier, retaining its full conductor multiplicity. Thus the all-degree plane exclusion is specific to characteristic zero.

## The opposite-ruling pairing and its complete coefficient freedom

This separate source calculation retains the full coefficient family for a prescribed pairing, and explains why its sparse failed subfamily is not an exclusion of that whole family. It is not an exhaustion of arbitrary smooth-quadric projections.

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
