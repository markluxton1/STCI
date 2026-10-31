# Genus-two quintic normalizations: a marked toric source and inverse support

Date: 2026-10-31. Status: **independently reviewed provisional structural
restriction, exhaustive toric-source reduction and fixed-projection exclusion**. Work over
an algebraically closed field of characteristic zero, with
`C0=[u^4:u^3v:uv^3:v^4]`. The relative-center continuation in §7 remains
an investigation, not an excluded family. No canonical promotion is made.

## 1. Why this source remains relevant

The [Gorenstein-normalization theorem](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
excludes every mate for an integral nonnormal quintic with Gorenstein
normalization. The accepted [structural audit, §§5–6,9](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
already excludes sectional genus zero, proves rationality through genus
three, and forces Gorenstein normalization at genus one. Thus the first
remaining low-genus cases are two and three; genus one with non-Gorenstein
normalization is not an additional open case.

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

Apply the accepted [direct adjoint proof, §§1–2](2026-10-09-session-genus-two-adjoint-conic-model.md)
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

The [exact certificate](../computations/quintic_genus_two_toric_projection.py)
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

Suppose a hypothetical integral quintic carrier has normal projective
toric normalization X. Its ample Cartier hyperplane bundle H is
torus-linearizable and has a lattice polygon P of normalized area
`H^2=5`. If B is the boundary lattice count, toric intersections give
`K_X.H=-B`; adjunction on a general smooth hyperplane gives

    pi=(7-B)/2 <= 2.

The inherited genus-zero exclusion and genus-one reduction followed
by the Gorenstein-normalization exclusion remove pi=0,1. A normal
quintic image would have pi=6, so it is also impossible here. Thus
pi=2, B=3, and P is a triangle with three primitive edges.

After a lattice change and translation its vertices are
`(0,0),(1,0),(p,5)`. Shears change p by multiples of five, and the
other edges are primitive exactly when p is 2,3 or4 modulo five.
Exchanging the base endpoints sends p to 1-p; choosing another edge
as base sends p to its inverse modulo five. These operations identify
all three values. Therefore (X,H) is isomorphic to the polarized
surface (5). Its ample toric bundle gives the complete P4 embedding,
with exactly the five lattice points displayed above.

This is an exhaustive reduction for toric normalizations of quintic
mates, using the stated earlier exclusions. It is not a reduction of
all non-Gorenstein normalizations to toric ones.

### 4.2. The marked curve is unique up to a source automorphism

Let c' be any smooth H-degree-four curve on (5) that projects
isomorphically to fixed C0. It must span P4. Otherwise its span is a
P3 on which projection is a linear isomorphism. The restriction of
the rank-three quadric Q is nonzero, since Q contains no P3, and
has rank at most three. This contradicts the unique smooth
rank-four quadric containing C0. Thus the five coordinate restrictions
are a basis of `H0(P1,O(4))`.

Factor `BD=C^2` in the binary-form UFD, absorbing constant units:

    B=f p^2, C=f p q, D=f q^2,
    gcd(p,q)=1, deg(p)=deg(q)=r, deg(f)=4-2r.

Independence excludes r=0. Equation R gives `AE p=f^2 q^5`, so
r=2 is impossible. For r=1, p divides f, hence `f=p h` with h
linear and `AE=p h^2 q^5`. If h is proportional to q, all five
coordinates have a common zero at q=0. If h is proportional to p,
basepoint-freeness forces one of A,E to equal q^4 and the other to
be proportional to C. Both cases fail.

Now p,q,h are distinct. At h=0, A and E cannot both vanish, so the
entire h^2 factor belongs to one of them. Up to exchanging A,E,
degree allocation leaves

    (A,E)=(q^4,p h^2 q)  or  (p q^3,h^2 q^2).

Writing `h=alpha p+beta q`, the first case makes E a linear
combination of C,D. Only the second remains. Its coordinate units
satisfy the multiplicative identities of (5), so an inverse diagonal
automorphism removes them. After `u'=alpha p, v'=beta q`, rescaling
`(A,B,C,D,E)` by

    (alpha beta^3, alpha^3, alpha^2 beta, alpha beta^2, beta^2)

preserves (5) and yields (6). Exchanging A and E alone also preserves
(5). Hence all such marked curves are in the Aut(X)-orbit of c.

Sections 4.1–4.2 make the remaining relative-center problem exhaustive
for toric quintic normalizations. They do not solve that center problem.

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

The accepted [full-conductor/support criterion](../results/fixed_carrier_conductor_criterion.md)
rules out every mate on this S. A pulled-back nonzero Cartier divisor
on the normal surface cannot have those isolated zeros in addition
to its curve support. Equivalently, q vanishes at the marked point
of each offending fiber and is nonzero at its other point, which
prevents every q^N from descending. This excludes the center (7),
not all projections of X or all genus-two carriers.

## 7. Bounded continuation and independent evidence

The remaining test on this source varies the projection center while
requiring the image of the marked rational normal quartic to remain
projectively equivalent to fixed C0. Sections 4.1–4.2 show that this
covers every toric quintic normalization of a hypothetical mate.
It must retain exceptional
center loci and both endpoints of c. The calculation (8) does not
establish a generic or universal center exclusion.

The literature crosswalk was checked independently by
`/root/nonnormal_existing_evidence` against the primary article's
pp.197–205 and 210–213. That reviewer also independently reconstructed
§§4.1–4.2, including toric linearization, primitive-edge equivalences,
the span argument, all UFD factor allocations and diagonal source
automorphisms. Its two wording slips were corrected before preservation:
basepoint-freeness requires A,E not to vanish simultaneously, and the
needed exchange is A,E alone. No B,D exchange is used.
The reviewer then checked the written §§4.1–4.2 and their §7 scope
and confirmed that the toric-source reduction does not assert a
completed center exclusion.
Reviewer `/root/nonnormal_quintic_boundary`
reconstructed the source geometry, marked embedding, root divisor,
projection and support contradiction. It also independently checked
§§2–3, including minimality, the direct fixed/moving-part proof,
effectivity of Z and the horizontality argument. Its initially
overstated linear equivalence D2~D3 was corrected to the actual
five-torsion relation before writing this note; the displayed root
proof uses the principal divisor directly.
The same reviewer then checked this integrated written state and
accepted its exact scope, notation, endpoint coverage and general
bound with no unresolved material issue.

Reviewer `/root/conductor_incidence_code_review` independently checked
the exact implementation and executed it once with Python 3.15.2 and
SymPy 1.14.0; exit zero. The canonical copy changes only its docstring
and execution-command metadata, and the reviewer confirmed identical
mathematical content. Current SHA-256:

    5df5fa92c9311a44067ef7efd47a33bf40dfb00aacca088dd3a288cd5d4d8db7

Reproduction with the available SymPy environment:

    PYTHONPATH=/private/tmp/stci-symbolic python3 research/computations/quintic_genus_two_toric_projection.py

The exact code is preserved; its mathematical interpretation is the
full inverse scheme in (8), not an ambient residual-curve calculation.
The construction demonstrates compatibility of non-Gorenstein index
five, the fixed marked curve and an actual quartic root upstairs.
It also identifies the projection condition that this first example
fails. The unrestricted STCI question remains open.
