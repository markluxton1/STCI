# A non-Gorenstein toric quintic source with a marked quartic

Work over an algebraically closed field of characteristic zero. The
full proofs below construct a normal non-Gorenstein degree-five surface,
its marked rational normal quartic and an actual quartic root upstairs.
They prove the general conic-ruling restriction and exhaust the possible
polarized toric normalizations and marked curves of a quintic mate.
One explicit projection is excluded by its entire inverse scheme.
The [relative-center calculation](quintic_toric_center_incidence.md)
excludes every admissible projection center by full inverse support.
Thus the conic-ruling and source classification below exclude every
mate on an integral quintic with toric normalization.

## 1. Why this source remains relevant

The [Gorenstein-normalization theorem](quintic_gorenstein_normalizations.md)
excludes every mate for an integral nonnormal quintic with Gorenstein
normalization. The structural audit
[excludes sectional genus zero](quintic_conormal_and_factor_geometry.md#9-the-sectional-genus-zero-exclusion-also-passes),
[proves rationality through genus three](quintic_conormal_and_factor_geometry.md#5-low-sectional-genus-the-ruled-argument-audited)
and [forces Gorenstein normalization at genus one](quintic_conormal_and_factor_geometry.md#6-sectional-genus-one-forces-a-single-a4-normalization).
The first remaining low-genus cases are two and three.

Andreatta–Sommese, [Theorems B–C, p.198, and §0.5](https://journals.msp.org/mscand/article/download/1351/1350/1382),
classify the polarized normalization of a possibly singular complex
projective surface by the genus of its general normalized hyperplane
section. This is the repository's sectional genus, not the genus of
the special marked curve. After the accepted rationality restriction,
their genus-two description is a Gorenstein conic bundle over P1 followed
by contraction of at most two sections. Their genus-three alternatives
include the original degree-five image and do not supply a complete
marked normalization model. Neither theorem places C0 or specifies
its projection center. The concrete construction below supplies those
missing data for one source. The direct proof in §2 does not depend on
the external classification.

## 2. Every genus-two quintic mate marks a section of the conic ruling

Let S be an integral quintic with a hypothetical sole-supported mate,
X its normalization, and `sigma:M->X` its minimal smooth resolution.
Put `L=sigma*nu*O_S(1)`. Suppose the normalization sectional genus is two.
The accepted structural audit gives rational M and the actual relation

    L^2=5,  K_M.L=-3,  L.c#=4,
    c#+Z == (4/5)L,  Z>=0,  L.Z=0.                    (1)

Here `==` denotes numerical equivalence, c# is the smooth strict
transform of C0, and Z is the effective exceptional part of the
pulled-back mate divisor after its multiplicity is divided out.
Minimality excludes a smooth rational (-1)-curve of L-degree zero.

Apply the accepted [direct adjoint proof, §§1–2](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-adjoint-conic-modelmd)
with the changed numerical inputs. For `A=K_M+L`, nef-big vanishing
and Riemann–Roch give `h0(A)=2` and `A.L=2`. If A had negative
intersection with a prime, that prime would be a negative fixed curve.
Adjunction leaves only a rational (-1)-curve, and minimality gives its
L-degree at least one, a contradiction. Thus A is nef, and Hodge gives

    0 <= A^2 <= 4/5,   hence A^2=0.

For `|A|=|P|+D`, nefness gives `A.P=A.D=0`. Moving intersection gives
`P^2>=0`; Hodge gives the reverse inequality and numerical
proportionality to A. Consequently |P| is a basepoint-free pencil.
Its Stein base is P1 because M is rational, and `h0(P)=2` makes P
a connected fiber. Adjunction gives `L.P=2`. Comparing with `L.A=2`
makes D numerically trivial, so the effective divisor D is zero.
Therefore

    F=K_M+L,  |F| is a connected rational ruling,
    F^2=0,  L.F=2,  K_M^2=1.                          (2)

The curve c# cannot be a fiber component, whose L-degree is at most
two. Intersect (1) with the nef fiber class. Its positive integral
ruling degree is at most 8/5, so

    c#.F=1,  Z.F=3/5,
    (c#)^2=1,  c#.Z=11/5,  Z^2=-11/5.                (3)

The last three identities follow from `K_M=F-L`, adjunction on c#,
and `(c#+Z).Z=0`. Thus the marked quartic is a section of the conic
ruling. Some exceptional curve is horizontal, since `Z.F>0`.
The ruling on M consequently cannot be assumed to descend through
normalization. Its contracted horizontal curves account for the
fractional part of the mate's intersection with a general conic.

## 3. A general fiber-degree bound

More generally, let an integral degree-a surface be generically
regular along a smooth curve C of degree d and admit an actual
sole-supported mate. On a smooth resolution of its normalization,
the full inverse-support result gives

    c#+Z == (d/a)L,  Z>=0 exceptional,  L.c#=d.

Suppose that resolution has a morphism to a smooth curve with
connected general fiber F of hyperplane degree `r=L.F<d`.
Then c# is horizontal: every component of a fiber has L-degree at
most r. The positive integer `n=c#.F` therefore satisfies

    1 <= n <= dr/a,   hence a<=dr.                     (4)

This follows by intersecting the actual total-transform relation with
F and retaining the nonnegative term `Z.F`. It needs no Gorenstein
normalization or genus hypothesis, but it does need the actual
fibration and effective pullback. In particular, for C0 a conic-fiber
normalization model cannot be a carrier of degree at least nine.
This is a reusable form of the earlier ruled-degree comparison, not
a classification of arbitrary higher-degree carriers.

## 4. An actual non-Gorenstein degree-five source

In P4 with coordinates `(A,B,C,D,E)`, take the projective toric surface
with all lattice points of the triangle

    A=(0,0), B=(1,0), C=(1,1), D=(1,2), E=(2,5).

Its full homogeneous ideal is

    Q=BD-C^2,  R=AEC-D^3,  T=ABE-CD^2.                (5)

The [exact certificate](https://github.com/markluxton1/STCI/blob/3a50e7675d965bd5fa15084189aaab750620bca3/research/computations/quintic_genus_two_toric_projection.py)
verifies both ideal containments after eliminating the monomial map
`(A,B,C,D,E)=(S,Sx,Sxy,Sxy^2,Sx^2y^5)`. It includes the toric boundary.

The triangle has area 5/2 and three boundary lattice points. The
five triangles ABC, ACD, ADE, BCE and CDE are unimodular and cover
it, so its lattice-point semigroup is normal. Consequently X is
normal, `H^2=5`, `K_X.H=-3`, and its general hyperplane has genus two.
The inward primitive rays are

    (0,1), (-5,1), (5,-2).

All adjacent determinants have absolute value five. The cone between
the first two rays has an integral height-one functional and gives
an A4 point. The other two have canonical index five. This X is
therefore outside the Gorenstein-normalization exclusion.

Set h=u+v and mark the curve

    c(u,v)=(uv^3, u^3h, u^2hv, uhv^2, h^2v^2).       (6)

Substitution satisfies (5). Its five coordinates have coefficient
determinant -1 in the basis `(u^4,u^3v,u^2v^2,uv^3,v^4)`, so (6)
is an embedded rational normal quartic. This supplies an actual
smooth marked curve, beyond the numerical requirements (1).

### 4.1. This is the only remaining polarized toric normalization

Over an algebraically closed field of characteristic zero, let `S`
be any integral quintic in P3 containing the fixed
`C0=[u^4:u^3v:uv^3:v^4]`, and let `nu:X->S` be its finite normalization,
assumed toric. Suppose a homogeneous form `G` of positive degree `b`
meets S properly with zero support exactly C0. Set `H=nu*O_S(1)`,
an ample Cartier bundle with `H^2=5` by birationality.

The surface S is regular at the generic point of C0. Otherwise its
equation has order at least two there. Restricting to the unique
smooth containing quadric would give either zero or a divisor of
class `(5,5)` containing twice the curve of class `(1,3)`. The
residual class `(3,-1)` is ineffective, and a zero restriction would
make the quadric a factor of the quintic.
[Fixed containing quadric](../curve/fixed_quartic_geometry.md#12-three-different-incidence-spaces-and-their-markings)

Thus there is just one branch c above the generic point of C0. Its
reduced closure maps finitely and birationally to the smooth C0 and
therefore is isomorphic to C0, with `H.c=4`. The support of the
effective Cartier divisor of `nu*G` is the whole inverse of C0.
Finiteness gives no other one-dimensional component and the principal
ideal theorem excludes isolated zeros. Consequently

    (nu^-1(C0))_red = c,   div(nu*G)=5N c,   b=4N,  N>0.             (*)

where the coefficient and degree follow by intersecting with H.
These are the normalization hypotheses for the low-genus reductions.
[Structural normalization audit](quintic_conormal_and_factor_geometry.md#direct-quintic-normalization-and-global-source-constraints)

The toric linearization of H gives a lattice polygon P of normalized
area `H^2=5`. If B is its boundary lattice count, the sum of its edge
lattice lengths is B, and the intersection of H with each toric
boundary curve is the corresponding edge length. Hence `K_X.H=-B`.
A general pulled-back hyperplane is a smooth integral curve by Bertini
for the basepoint-free system defining the birational morphism `nu`.
It avoids the finite singular locus of X. Adjunction on this curve
gives its genus

    pi=(7-B)/2 <= 2.

If S itself were normal, a general plane section would be a smooth
plane quintic of genus six, contrary to this bound. The genus-zero
exclusion applies to the finite birational hyperplane model and the
smooth degree-four lift in (*). It excludes the two smooth quintic
scrolls by the nonintegral square `c_num^2=16/5` imposed by (*), and the
quintic scroll cone by the effective curve classes on its resolution.
[Genus-zero exclusion](quintic_conormal_and_factor_geometry.md#9-the-sectional-genus-zero-exclusion-also-passes)

At genus one the same actual lift gives rationality of the minimal
resolution `sigma:M->X`, and the genus-one reduction shows
`K_M=-sigma*H`. The contraction is crepant with ADE singularities, so
X is Gorenstein. The Gorenstein-normalization theorem excludes every
positive mate degree on this integral nonnormal S in characteristic
zero. Thus `pi=2`, `B=3`, and P is a triangle with three primitive
edges. [Low-genus rationality](quintic_conormal_and_factor_geometry.md#5-low-sectional-genus-the-ruled-argument-audited) ·
[Genus-one reduction](quintic_conormal_and_factor_geometry.md#6-sectional-genus-one-forces-a-single-a4-normalization) ·
[Gorenstein-normalization exclusion](quintic_gorenstein_normalizations.md)

After a lattice change and translation its vertices are
`(0,0),(1,0),(p,5)`. Shears change p by multiples of five, and the
other edges are primitive exactly when p is 2,3 or4 modulo five.
Exchanging the base endpoints sends p to `1-p`. To use `(p,5)`
as the base direction, extend it to a determinant-one lattice basis
by a vector `(i,j)` satisfying `pj-5i=1`. The first coordinate of
the old base endpoint `(1,0)` in this basis is `j`, which is the
inverse of p modulo five. Reflection in the second coordinate puts
the third vertex back at height five. These operations connect all
three values to `p=2`, the triangle of (5). Therefore (X,H) is
isomorphic to that polarized surface. Its complete system gives the
displayed P4 embedding, with one section for each of its five lattice
points.

The four pulled-back coordinate sections from P3 are independent,
since S spans P3, and basepoint-free on X. In this complete P4
embedding they define projection from a point outside X. The
projection is `nu` up to target coordinates and carries the lift c
in (*) isomorphically to C0.

### 4.2. The marked curve is unique up to a source automorphism

Let c' be the smooth degree-four lift from (*), viewed on (5).
Since its image C0 spans P3, the linear span of c' has dimension at
least three. If it were a P3, projection on that P3 would be
surjective and hence a linear isomorphism. The rank-three quadric Q
contains no P3, since its equation would then be divisible by a
linear form and have rank at most two. Its nonzero restriction to
the span of c' would give a quadric of rank at most three containing
C0, contrary to the unique rank-four containing quadric. Thus c'
spans P4. As `c'` is isomorphic to P1 and `H|c'` has degree four,
the five coordinate restrictions are a basis of `H0(P1,O(4))` with
no common zero.

Factor `BD=C^2` in the binary-form UFD. After taking the common gcd
of B, C and D into f, each irreducible factor of the remaining B
or D occurs to even order, and those two forms are coprime.
Absorbing the constant units into p and q gives

    B=f p^2, C=f p q, D=f q^2,
    gcd(p,q)=1, deg(p)=deg(q)=r, deg(f)=4-2r.

The nonzero forms B and D have degree four, so `r<=2`, and
independence excludes `r=0`. After cancellation R gives
`AE p=f^2 q^5`. For `r=2` this would force p to divide a power of
the coprime q, since f is constant. Thus `r=1`, and coprimality
forces `f=p h` with h linear. Then `AE=p h^2 q^5`. The cases of
coincident factors are as follows.

- If h is proportional to q, `AE` is a scalar times `p q^7`.
  Each degree-four factor A and E is divisible by q, as are B, C
  and D. This gives a common zero at `q=0`.
- If h is proportional to p, `AE` is a scalar times `p^3 q^5`, and
  B, C and D all vanish at `p=0`. To avoid a common zero, one of
  A, E must be a multiple of `q^4`. The other must be proportional
  to `p^3 q`, which is C up to a scalar. This contradicts independence.

Now p,q,h are distinct. At h=0, A and E cannot both vanish, so the
entire h^2 factor belongs to one of them. Up to exchanging A,E,
degree allocation leaves

    (A,E)=(q^4,p h^2 q)  or  (p q^3,h^2 q^2).

These are all degree allocations because the factor without h has
degree four and the exponent of p in `AE` is one. Writing
`h=alpha p+beta q`, the first case makes `E=alpha C+beta D` up to
a scalar. In the second, the two scalar factors in A and E are
inverse because `AE=p h^2 q^5`, and inverse scaling of A and E
preserves (5) and removes them. Both alpha and beta are nonzero
because h is proportional to neither p nor q. After
`u'=alpha p, v'=beta q`, rescaling
`(A,B,C,D,E)` by

    (alpha beta^3, alpha^3, alpha^2 beta, alpha beta^2, beta^2)

preserves (5) and yields (6). Exchanging A and E also preserves (5).
Hence the marked source is unique up to a polarized source automorphism.

Under this identification, (*) makes the curve in (6) the entire
reduced inverse support required by a mate. The center-orbit argument
identifies all projections of this marked source with image C0 up to
target coordinates.
[Projection-center orbit](quintic_toric_center_incidence.md#1-geometric-object-and-scope)

## 5. The quartic root exists on the normalization

On the torus in A=1, write `x=B, y=C/B`. The marked curve is

    psi=1+y-xy^3=0.

Let D1,D2,D3 be the toric boundary divisors for the rays above.
Their valuations give

    H~5D2,
    div(psi)=c-2D2-2D3,
    div(x^2)=-10D2+10D3.

Thus the rational function

    q=x^2 psi^5

defines an actual section of 4H, with entire divisor `5c`. This
statement includes the boundary. It does not use `D2~D3`: only
`5(D3-D2)=div(x)` is principal, and their difference is nontrivial
five-torsion in the class group.

For any finite birational quintic projection taking c isomorphically
to C0, a sole-supported mate of degree b must have `b=4N` and pull
back to a scalar multiple of q^N. Whether a power descends remains
an actual projection/conductor question. The next section exhibits
a projection where every power fails despite this root relation.

## 6. One actual quintic projection has five extra inverse points

Project from `P=[0:0:1:1:1]` using

    X0=B-C+D-A, X1=C-D+A, X2=A, X3=E-D-A.             (7)

These forms have rank four, their common center satisfies `Q(P)=-1`,
and their restriction to (6) is exactly C0. The morphism is finite
because its pullback of O(1) is ample. Its image is nonplanar, and
the product of its degree and image degree is five; hence it is
birational onto an integral quintic S. Normal X is its normalization.

On v=1 put t=u/v. A complete inverse fiber over `[t^4:t^3:t:1]`
has coordinates

    A=t, B=t^4+t^3, C=t^3+z-t, D=z, E=1+z+t.

The certificate computes the entire affine inverse ideal as

    ((z-z0)(z-z1), t(t+1)(z-z0) f5(t)),
    z0=t^2+t,  z1=t^4-t^3-t^2+t,
    f5=t^5-2t^4+t^3+t^2-t+1.                         (8)

The marked graph is z=z0. The polynomial f5 is squarefree and is
coprime to `t(t+1)(t-2)`, while

    z1-z0=t^2(t-2)(t+1).

Each of its five roots therefore gives a distinct reduced extra
point z=z1 outside c. At t=0,-1 the fiber has length two supported
on c. At the remaining target point v=0, the fiber ideal is (z),
so only the marked point occurs. Thus the entire reduced inverse
of C0 consists of c and five additional isolated points.

The accepted [full-conductor/support criterion](../../results/fixed_carrier_conductor_criterion.md)
rules out every mate on this S. A pulled-back nonzero Cartier divisor
on the normal surface cannot have those isolated zeros in addition
to its curve support. Equivalently, q vanishes at the marked point
of each offending fiber and is nonzero at its other point, which
prevents every q^N from descending. This excludes the center (7),
not all projections of X or all genus-two carriers.

<a id="the-remaining-relative-center-problem"></a>

## Exclusion of all relative centers

The [relative-center proof](quintic_toric_center_incidence.md) varies
the center while requiring the marked rational normal quartic to map
projectively to fixed C0. Sections 4.1–4.2 make this reduction exhaustive
for toric quintic normalizations of a hypothetical mate. The proof
excludes the entire one-infinity chart, the general finite centers and
all exceptional finite loci, retaining both marked endpoints, parameter
poles and degree drops. The [last elimination](quintic_toric_center_incidence.md#exact-elimination-on-m0)
excludes every parameter on the remaining M locus. Every admissible center
therefore fails full inverse support, which prevents descent of every
power of the upstairs section. Non-toric, non-Gorenstein normalizations
remain open.

## Exact support, characteristic and review scope

The unchanged
[toric projection certificate](https://github.com/markluxton1/STCI/blob/3a50e7675d965bd5fa15084189aaab750620bca3/research/computations/quintic_genus_two_toric_projection.py)
retains both toric ideal containments including the boundary, the
marked coefficient determinant, the full inverse ideal, the squarefree
and coprimality checks and both exceptional endpoints. Its source had
independent implementation review and a successful exact execution.
This transfer reuses that evidence without a new run.

Independent source reviews reconstructed the direct adjoint/fixed-moving
proof, effectivity of Z and the horizontal-curve conclusion; the primitive
edge classification, all binary UFD factor allocations and the exact
diagonal automorphisms; and the root divisor and finite projection.
The class-group statement is the actual five-torsion relation,
not D2~D3. The needed coordinate exchange is A,E alone; no B,D exchange
is used. The earlier source-geometry integration has independent mathematical
preservation and scope review. The additional relative-center material is
preserved from the reviewed source commit identified in its companion;
independent preservation and scope review of that addition passed without a
material finding, by direct comparison to the fixed source and its exact
support files. No fresh CAS replay was made. Its conclusions remain
within the review scope stated above.

The toric semigroup construction, integer polygon data, unimodular
triangulation, lattice divisor identities and marked determinant-1
identity have algebraic meaning in every characteristic. The stated
exhaustive mate reduction uses characteristic-zero surface classification
and vanishing. The five distinct extra points and exact exceptional
fiber conclusions are the checked characteristic-zero calculation;
they are not silently specialized through bad primes. Nothing here
transports the characteristic-zero quintic exclusions to positive
characteristic.

The construction shows that canonical index five, the fixed marked
quartic and a global root with divisor 5c can coexist on a normalization.
Full inverse support fails for every admissible projection of this
marked source.
