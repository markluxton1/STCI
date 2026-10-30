# projection singleton and antidiagonal

Complete mathematical dossier preserving the actual investigations, calculations, exact conditions, negative results, and unresolved boundaries. Administrative commentary is retained pending editorial consolidation, not treated as proof authority.

---

## 2026-10-19-singleton-projection-investigation

# A full-singleton plane normalization with a first-order descent obstruction

Date: 2026-10-19. Investigator: `projection_geometry`.

**Status:** new proposal, independently reviewed for the explicit maps and
all-degree exclusions in Sections 1--5 by
[the separate audit](2026-10-19-singleton-plane-projection-independent-audit.md).
The reusable differential lemma and the local conductor interpretation in
Sections 6--7 are independently checked in that audit's addendum. The broader
two-fixed-coordinate exclusion in Section 5a is a separate new proposal.
No canonical result or question record is edited or promoted by this note.

## Scope and authority

The ground field is algebraically closed of characteristic zero. The literal
embedded curve is

    C0=[s^4:s^3t:st^3:t^4] in P3.

[STCI-R-0002](../results/cartier_singleton_lift.md) identifies the necessary
plane model `S=P2`, `c` a line, `H=O(4)`, `deg X=16`, under its stated
Cartier, full singleton degree-one lift, and actual-mate hypotheses.
It does not assert the existence of projections or mates. The question
[STCI-Q-0001](../questions/cartier_projection_models.md) asks whether such
models admit actual projections with full inverse support and conductor
descent. This note constructs actual projections meeting the full inverse
support condition, then excludes a mate on every one of these particular
carriers. It does not classify all projections in the plane model.

The mate exclusion below is elementary and does not require the uncomputed
phase image from [STCI-R-0004](../results/projection_phase_reduction.md),
nor a replay of the accepted quartic-carrier exclusion. In particular it
separates actual full inverse support from actual descent.

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

**Proposed conclusion:** the integral degree-sixteen carrier (3) contains
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

## 6. A reusable differential obstruction on a Cartier ray

**Proposed lemma.** Let `nu:S->X` be a finite birational projective
normalization over an algebraically closed characteristic-zero field. Let
`H=nu*L`, and suppose a smooth ample Cartier curve `c` has full reduced
inverse support of an embedded integral curve `C`, with `nu|c` an
isomorphism. Suppose `Q` is a section of `H` with divisor `m c`.
Let `p` be a smooth point of `S` outside `c`, and let `h` be a local
nonvanishing frame of `L` at `nu(p)`, so

    q=Q/(nu*h)

is a regular nonzero function near `p`. If there is a tangent vector
`v in ker(dnu_p)` with `dq_p(v)!=0`, no positive power of `L` has a
section with zero support exactly `C`.

Proof. A hypothetical section of `L^b` pulls back to a section with
divisor `r c`, for some positive integer `r`. Comparison with `Q^b`
gives a linear equivalence `(r-mb)c~0`. Intersecting with an ample
divisor gives `r=mb`. Their ratio is then a nowhere vanishing regular
function on integral projective `S`, hence a constant. After dividing
by `h^b`, a function descending from `X` is a nonzero scalar multiple
of `q^b`. Its differential kills every vector in `ker(dnu_p)`, while

    d(q^b)_p(v)=b q(p)^(b-1)dq_p(v)!=0.

This contradiction proves the claim. The argument uses characteristic
zero precisely to ensure that the positive integer `b` is nonzero in `k`.
Changing the frame `h` multiplies `q` by a descending unit; its derivative
on `ker(dnu_p)` is zero, so nonvanishing is frame independent.

For the primitive map (1), take the chart `z=1`, source coordinates
`r=s/z`, `y=t/z`, target frame `U2`, and `p=(r,y)=(0,1)`. Then

    q=1/(1+r y^3),
    X0/X2=r^4/(1+r y^3),
    X1/X2=r^3 y/(1+r y^3),
    X3/X2=(y^4+r^3)/(1+r y^3).

The target differential has kernel generated by

    v=partial_r+(1/4)partial_y,

and `dq_p(v)=-1`. This gives a local geometric reconstruction of the
global polynomial obstruction. The point lies outside `c`, so this is
an actual obstruction to off-`C0` descent, rather than a vanishing
threshold along `C0`.

## 7. Trivial reduced residue with a nonzero first nilpotent defect

Let a member of (8) be birational, and let `D=(s=0)` upstairs. Its image
is the line `ell=(X0=X1=0)`. The boundary map (9) has degree four, so
the normalization has residual degree four at the generic point of this
line; `D` is an actual conductor prime. It maps onto a curve downstairs.

Use the target frame `U2`, and put `r=s/z`, `y=t/z`. At the generic point
of `D`, with residue field `E=k(y)`,

    q=Q/U2=1/(alpha+r y^3),            Q=z^4.

Its residue is the constant `1/alpha`. Thus its class in the reduced
residual quotient `E*/K*` is trivial, where

    K=k(g(y)/alpha),    g(y)=y^4+P(0,y,1).

Nevertheless no positive power of `q` belongs to the actual image local
ring. Here is a direct first-order proof, without computing a conductor
ideal. In the target chart `X2!=0`, its affine coordinate ring is
generated by `a0=X0/X2`, `a1=X1/X2`, `w=X3/X2`. In the source DVR,

    a0=0 mod r^2,
    a1=0 mod r^2,
    w=g(y)/alpha+r h(y) mod r^2                       (13)

for an explicit rational function `h` whose value is immaterial.
Every element of the target ring localized at the generic point of
`ell` is, modulo `r^2`, a rational function `R(w)` with `R in k(w)`;
its denominator is nonzero at that generic point. If it had residue
`alpha^(-b)`, the transcendence of `g(y)/alpha` would force `R` to be
that constant. Such an element has zero coefficient of `r` in (13).
But

    q^b=alpha^(-b)-b alpha^(-b-1)y^3 r mod r^2,          (14)

whose linear coefficient is nonzero for every positive `b`. Hence
`q^b` cannot descend at this conductor prime, although its reduced
residual class is already the identity. This is the needed first
nilpotent defect. Reduced contact or root-of-unity tests alone cannot
decide descent even on these actual full-support carriers.

For the primitive map, the affine isomorphism (2) shows that the
normalization is an isomorphism away from `D`; thus `D` is its entire
conductor support. This support assertion does not compute its scheme
multiplicity. No such entire-support assertion is made for arbitrary `P`,
whose affine image may have additional conductor curves.

## Frontier impact and outstanding review

The concrete new output is a nonempty eleven-parameter family with an
exact birational locus of actual degree-sixteen normalizations, full
singleton inverse support, and an all-positive-degree mate exclusion.
The primitive member also provides an explicit degree-sixteen equation.
These conclusions passed independent reconstruction in the separate
audit, as did the differential lemma and the local nilpotent interpretation
in its addendum. The broader two-fixed-coordinate exclusion in Section 5a
also passed the independently reconstructed closing review. No phase image or torsion
coset for the full plane model is computed, and this family does not
exhaust its projection parameters. The two degree-eight models, the
other plane projections, non-Cartier and multiple lifts, and unrestricted
characteristic-zero STCI for `C0` remain open.


---

## 2026-10-19-singleton-plane-projection-independent-audit

# Independent audit: a plane normalization with singleton inverse support and no mate

Date: 2026-10-19. Reviewer: `projection_geometry/plane_support`.

**Outcome: PASS for the displayed map and the broader family in Section 5,
their full singleton inverse support, the precise birationality criterion,
and their exclusion of a set-theoretic mate in every positive degree.** This
is an independently reconstructed proof and review evidence, not a
canonical promotion. No canonical result/question record or accepted proof
was edited, and no inherited exclusion was rerun.

## Exact claim, scope, and dependencies

Let `k` be algebraically closed of characteristic zero. Use homogeneous
coordinates `(s:t:z)` on `S=P2`, let `c=(z=0)`, and define

    U0=s^4,   U1=s^3 t,   U2=s t^3+z^4,   U3=t^4+s^3 z,
    f=(U0:U1:U2:U3): P2 -> P3.

Then `f` is the finite birational normalization map of an integral
degree-sixteen hypersurface `X`; its restriction to `c` is an isomorphism
onto the literal embedded rational quartic

    C0=[s^4:s^3t:st^3:t^4].

The full reduced inverse support of `C0` is exactly `c`. Nevertheless,
there is no homogeneous polynomial `G` of any positive degree with
`(X intersect V(G))_red=C0`.

[STCI-R-0002](../results/cartier_singleton_lift.md) identifies the model
`(P2,c a line,H=O(4))` as a necessary possibility under its own hypotheses.
This audit constructs an actual normalization with full singleton support
inside that model, and proves that this carrier has no mate. The proof
below is direct and does not assume a conductor classification, a computed
phase image, or the existence of a mate. The question being informed is
[STCI-Q-0001](../questions/cartier_projection_models.md); that question
remains open for the rest of its projection families.

## 1. Basepoints, finiteness, birationality, and normalization

If `s!=0`, then `U0!=0`. If `s=0`, the last two coordinates are `z^4,t^4`,
which cannot both vanish at a projective point. Thus the four sections
are basepoint free and `f^*O(1)=O_P2(4)`.

Every positive-dimensional fiber of a projective morphism from `P2`
contains a complete curve. On such a curve the pullback of `O(1)` would
have degree zero, contradicting the ampleness of `O(4)`. Hence `f` is
finite onto its image.

On `s!=0`, put `x=t/s`, `y=z/s`. In the target chart `X0!=0` the map is

    (x,y) -> (X1/X0,X2/X0,X3/X0)=(x,x^3+y^4,x^4+y).

The inverse on its image is

    x=X1/X0,   y=X3/X0-(X1/X0)^4.

Thus the map is an isomorphism onto its image on this entire affine chart,
and in particular it is birational. Its image is integral, and the degree
formula gives `deg X=(4 line)^2=16`. A finite birational morphism from the
normal surface `P2` is the normalization of its integral image.

One can also verify the image equation directly:

    F=(X0^3 X3-X1^4)^4-X0^13 (X0^2 X2-X1^3).

Both terms have degree sixteen. Under substitution,

    U0^3 U3-U1^4=s^15 z,
    U0^2 U2-U1^3=s^8 z^4,

so `F(U)=0` identically. As a polynomial in `X2`, its coefficient is
`-X0^15`, while its constant coefficient is not divisible by `X0` because
its restriction at `X0=0` is `X1^16`. The polynomial is therefore primitive
and linear over `k(X0,X1,X3)`, and is irreducible. Consequently `X=V(F)`.

## 2. Literal restriction and full inverse support, including the boundary

At `z=0`, the map is exactly the displayed parametrization of `C0`, with
no projective change of coordinates. That parametrization is a closed
immersion: on `s!=0` its parameter is `X1/X0=t/s`; at `s=0,t=1` the
coordinate `X2/X3=s` gives a nonzero tangent parameter. In particular,
`f|c` is an isomorphism onto `C0`.

On `s!=0`, the equations for `C0` in the target affine chart are

    X2/X0=(X1/X0)^3,   X3/X0=(X1/X0)^4.

The second equation forces `y=0`, and the first then follows. Thus the
inverse support on this chart is exactly `z=0`.

On `s=0`, the image is `[0:0:z^4:t^4]`. The only point of `C0` with
`X0=0` is `[0:0:0:1]`; its inverse points in this boundary satisfy `z=0`
and `t!=0`. This adds just `(0:1:0)`, already on `c`. Therefore

    (f^{-1}(C0))_red=c

globally, with no isolated inverse point or additional inverse curve.

## 3. All-positive-degree mate obstruction

Suppose that a homogeneous `G` of degree `b>=1` satisfies
`(X intersect V(G))_red=C0`. Its pullback `G(U)` is a nonzero homogeneous
polynomial of degree `4b` whose projective zero support is exactly `c`.
Unique factorization gives

    G(U)=lambda z^(4b),   lambda!=0.

Divide `G` by `lambda`. At `s=0` the identity becomes

    G(0,0,z^4,t^4)=z^(4b).

The substitution `k[Z,T] -> k[z,t]`, `Z->z^4,T->t^4`, is injective, so

    G(0,0,Z,T)=Z^b.                                      (1)

Now differentiate the pullback identity with respect to `s` and set
`s=0`. The derivatives of `U0,U1,U3` vanish at `s=0`, while
`dU2/ds=t^3`. The chain rule and (1) therefore give

    0=t^3 G_X2(0,0,z^4,t^4)=b t^3 z^(4b-4).

This is impossible over a field of characteristic zero for every integer
`b>=1`. The calculation is a uniform proof in `b`; no bounded-degree search
or unexecuted computation is involved. It requires neither irreducibility
of `G` nor any genericity assumption on its coefficients.

## 4. Adversarial checks and exact frontier impact

The most consequential boundary checks are `s=0` and its point `z=0`.
The boundary maps with degree four to the line `X0=X1=0`; its sole point
mapping to the endpoint of `C0` is already on `c`. Thus a proposed general
argument that every plane projection in this model must have a second
inverse point is refuted by this example.

At the reduced boundary, the required restriction `z^(4b)` is compatible
with descent through `(z:t)->(z^4:t^4)`, since it is the pullback of `Z^b`.
The contradiction occurs in the first transverse derivative. Accordingly,
checking only reduced boundary values would miss this obstruction. This
observation does not compute the full conductor ideal or identify an
entire phase image, and no such computation is needed for the proof.

The proof establishes the existence of an actual degree-sixteen
normalization with literal `C0` and full singleton inverse support, and
excludes every mate for that carrier. Section 5 extends the argument to
an explicit parameter family. It does not exclude all maps from
`P2` with polarization `O(4)`, either degree-eight normalization model, or
any non-Cartier/multiple/nonisomorphic lift. It does not settle the
unrestricted characteristic-zero STCI problem.

## 5. Broader audited family and exact birational locus

Fix `alpha!=0`, let `P(s,t,z)` be any homogeneous cubic, and replace the
four sections by

    U0=s^4,   U1=s^3t,   U2=st^3+alpha z^4,   U3=t^4+zP(s,t,z).

These are basepoint free: `U0` handles `s!=0`, while at `s=0` the coordinate
`U2=alpha z^4` handles `z!=0` and `U3=t^4` handles `z=0`. The same ample
pullback argument proves finiteness. The restriction to `c` remains the
literal `C0`. On `s!=0`, membership in `C0` forces
`U2/U0=(U1/U0)^3`, hence `alpha(z/s)^4=0` and `z=0`. On `s=0`, membership
in the endpoint `[0:0:0:1]` likewise forces `z=0`. Thus the full inverse
support is `c` for every member of this family, without a birationality
assumption.

Write uniquely

    P=A3(s,t)+z B2(s,t)+z^2 C1(s,t)+delta z^3,

where the subscripts are the binary degrees. Set `K=k(x)`. On `s=1` the
image function field inside `K(y)` is

    K(y^4,p(y)),
    p(y)=A3(1,x)y+B2(1,x)y^2+C1(1,x)y^3+delta y^4.

The extension `K(y)/K(y^4)` is cyclic Galois with group `mu4`, acting by
`y->zeta y`. Its subgroup fixing `p(y)` is trivial exactly when `A3!=0`
or `C1!=0`. Indeed a nonzero linear or cubic coefficient forces
`zeta=1`; if both vanish and `B2!=0`, the stabilizer is `{1,-1}`; if all
three vanish, it is all of `mu4`. Consequently the finite map has degree

    1 if A3!=0 or C1!=0;
    2 if A3=C1=0 and B2!=0;
    4 if A3=B2=C1=0.

The image degrees are respectively sixteen, eight, and four. In the first
case the map is the normalization, and realizes the same necessary
degree-sixteen model. This field argument uses characteristic zero and
the algebraically closed ground field, so the fourth roots of unity are
present and the extension is separable.

Finally, every member has the same all-degree mate obstruction, including
the nonbirational members. A hypothetical mate again yields, after scalar
normalization,

    G(U)=z^(4b).

At `s=0` consider the morphism

    P1_(t:z) -> P1_(Z:T),
    (t:z) -> (alpha z^4:t^4+zP(0,t,z)).

It is basepoint free and has pullback `O(4)`, hence is nonconstant and
surjective. Pullback of a nonzero homogeneous polynomial in `(Z,T)` is
therefore nonzero. The restriction identity forces

    G(0,0,Z,T)=(Z/alpha)^b.

In particular `G_X3(0,0,Z,T)=0`. Differentiate with respect to `s` at
`s=0`. The derivatives of `U0,U1` vanish; the derivative of `U2` is `t^3`;
and the potentially nonzero derivative `zP_s(0,t,z)` of `U3` is multiplied
by the identically zero restricted `G_X3`. The resulting identity is

    0=(b/alpha)t^3 z^(4b-4),

which is impossible. This proves a uniform all-positive-degree exclusion
for precisely the displayed family, and an explicit family of actual
degree-sixteen singleton-support normalizations when `A3!=0` or `C1!=0`.
It does not classify arbitrary four-coordinate quartic systems.

**Review status:** independently audited proposal/evidence, pending any
separate canonical promotion decision.

## Addendum: independent audit of the differential lemma and generic local descent

The reviewer separately reconstructed Sections 6--7 of the
[source investigation](2026-10-19-singleton-projection-investigation.md).
**Outcome: PASS**, with the lemma understood for an integral projective
surface and its finite normalization, as in the surrounding investigation.
This addendum supplies independent review evidence; it does not promote a
canonical result or compute a conductor multiplicity.

### A. Differential-kernel obstruction

Let `nu:S->X` and the data `L,H,c,C,Q,m,p,h,v` satisfy the source lemma.
In particular `S` is normal and projective, `c` is a nonzero smooth ample
Cartier curve, `div(Q)=m c`, the full reduced inverse support of `C` is
`c`, and `p` lies outside `c` in the smooth locus. Suppose a nonzero section
`sigma` of `L^b`, with `b>=1`, had zero support exactly `C`.

Its pullback has divisor `r c` for a positive integer `r`. Since this
pullback and `Q^b` are sections of the same line bundle, their divisor
classes give `(r-mb)c~0`. Intersecting with an ample divisor, which has
positive intersection with `c`, proves `r=mb`. Their ratio is a rational
function of divisor zero. Normality implies that this function and its
inverse are globally regular, and projectivity and integrality imply that
it is a nonzero scalar. Hence, in the frame `h^b`, the pullback of `sigma`
is `lambda q^b`, where `q=Q/(nu*h)` and `lambda!=0`.

Every function pulled back from `X` has differential zero on
`ker(dnu_p)`. But on the specified vector `v`,

    d(lambda q^b)_p(v)=lambda b q(p)^(b-1)dq_p(v)!=0.

Here `q(p)!=0` follows from `p` lying outside `c`, and `b!=0` in the field
uses characteristic zero. This proves the obstruction. No smoothness of
`X` at `nu(p)` is needed: its Zariski tangent space and differentials of
local functions suffice. If the frame is changed by a local unit `u` on
`X`, then `q` changes to `q/(nu*u)`; the extra differentiated term vanishes
on `ker(dnu_p)`. Thus the nonvanishing condition is frame independent.

For the primitive map, in source coordinates `(r,y)=(s/z,t/z)` and target
frame `X2`, take `p=(0,1)`. The target affine coordinates are

    a0=r^4/(1+r y^3),
    a1=r^3 y/(1+r y^3),
    w=(y^4+r^3)/(1+r y^3).

At `p`, `da0=da1=0` and `dw=-dr+4dy`. Therefore
`v=partial_r+(1/4)partial_y` belongs to the differential kernel, while
`q=1/(1+r y^3)` has `dq_p(v)=-1`. This point lies outside `c=(z=0)` and
gives a valid local obstruction to descent of every power.

### B. Generic local ring and denominator check

For a birational member of the broader family, let `D=(s=0)`, and work in
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

For the primitive member the affine chart `s!=0` is an isomorphism, by
the explicit inverse already checked. The generic nonnormality along
`D`, together with this isomorphism off `D`, proves that the entire
conductor support upstairs is `D`. No scheme multiplicity is inferred,
and no analogous entire-support assertion is justified here for arbitrary
`P`.

The differential lemma and this generic local calculation are therefore
independently reviewed with the literal hypotheses above. Their scope is
an obstruction and an explicit family calculation, not a computation of
the full plane-model phase image or a general exclusion of that model.

## Closing independent review of the two-fixed-coordinate sublane

Reviewer: root investigator, independently reconstructing Section 5a of
the proposal after its author stopped work. Outcome: PASS under the literal
basepoint-free, full-singleton-support, characteristic-zero hypotheses.

On s=0, a point with z nonzero and A3(0,t,z)=0 would have U0=U1=U2=0.
Basepoint freeness then gives U3 nonzero, so its image would be the C0
endpoint, contrary to the assumed full inverse support. Therefore the
polynomial A3(0,t,1) has no zero over the algebraically closed ground field.
It is a nonzero constant alpha, proving A3(0,t,z)=alpha z^3. Thus
U2=st^3+alpha z^4+szC2. The boundary morphism is basepoint free with
pullback O(4), hence surjective onto the target line. A hypothetical mate
forces G(0,0,Z,T)=(Z/alpha)^b. Its X3 derivative is zero on the line,
while its X2 derivative gives (b/alpha)z^(4b-4). The chain rule in s
therefore forces that nonzero factor times t^3+zC2(0,t,z) to vanish.
The latter polynomial has t^3 coefficient one and cannot be zero.
This excludes every positive mate degree throughout this exact sublane.

This check does not put arbitrary plane projections into that coordinate
sublane, classify its support-admissible locus, or remove the hypotheses.


---

## 2026-10-19-quadric-antidiagonal-fourfold-line-proposal

# An explicit degree-eight quadric-normalization family with a fourfold residual line

Date: 2026-10-19. Author: `carrier_models`.
Status: **INDEPENDENTLY REVIEWED PROPOSAL; audit PASS; not promoted.**
Review: [separate carrier audit](2026-10-19-quadric-antidiagonal-fourfold-line-independent-audit.md).

## Exact question and scope

Work over an algebraically closed field `k` of characteristic zero. The embedded curve is the literal fixed curve

    C0=[s^4:s^3 t:s t^3:t^4] in P3.

This note constructs actual integral degree-eight hypersurfaces whose finite normalization is the smooth quadric `S=P1 x P1`, with polarization `H=O(2,2)` and with a diagonal curve `c` mapped isomorphically to `C0`. It then proves that every basepoint-free member of this particular one-parameter family has **extra inverse points of C0**, so no member has a set-theoretic mate for C0 in any degree.

This is a completed exclusion for the explicitly defined subfamily below, not an exclusion of all smooth-quadric projections or of either other normalization model in STCI-R-0002. It supplies an actual residual-conductor construction illustrating why full inverse support is an essential extra condition in STCI-Q-0001.

Dependencies used as navigation/premises: [STCI-R-0002](../results/cartier_singleton_lift.md), [STCI-R-0003](../results/fixed_carrier_conductor_criterion.md), [STCI-Q-0001](../questions/cartier_projection_models.md), and the literal universal projection family in [the October 14 contact-phase note, Section 4](2026-10-14-generalization-projection-contact-phase-criterion.md). The argument below is elementary and does not rerun an inherited certificate or use the phase-reduction conclusion.

## 1. The family

On `S=P1_(s:t) x P1_(u:v)` write

    q=sv-tu,                 c=(q=0),
    p=sv+tu.

For `kappa in k` put

    U0=s^2 u^2 + (1/2) q t v,
    U1=(1/2) s u p,
    U2=(1/2) t v p,
    U3=t^2 v^2 + kappa q^2.                         (1)

All four sections have bidegree `(2,2)`. Restriction to `c`, using `(u:v)=(s:t)`, gives exactly the four displayed coordinates of `C0`.

**Proposition.** If

    kappa != 0,          kappa^3 != -1/64,             (2)

then (1) gives a basepoint-free finite birational morphism

    f_kappa:S -> X_kappa subset P3,

where `X_kappa` is an integral degree-eight hypersurface and `f_kappa` is its finite normalization. The full inverse support of `C0` contains at least five distinct points outside `c`. Consequently no homogeneous form can cut out exactly `C0` set-theoretically on `X_kappa`.

The particularly simple member `kappa=1` satisfies (2). In the balanced first-normal-jet coordinates of the October 14 contact-phase note, this family has `A(x)=x^5`, `B(x)=0`: here `L0|c=x^2/2` and the other three `L_i|c` vanish. Thus it lies in the maximal degree-five common-zero stratum, with its entire differential degeneracy concentrated at `t=0`. The calculation below uses the actual projection, rather than inferring inverse support from these first jets.

## 2. Basepoint-freeness, including the boundary charts

If `U1=U2=0`, either `p=0` or `su=tv=0`.

In the second case the only possible points of `S` are

    ((0:1),(1:0)),        ((1:0),(0:1)).

At either point `q!=0` and `U3=kappa q^2!=0` when `kappa!=0`.

The curve `D=(p=0)` is a smooth `(1,1)` curve with parametrization

    (s:t)=(a:b),         (u:v)=(a:-b).

On `D` the four sections become

    U0=a^4+a b^3,
    U1=U2=0,
    U3=b^4+4 kappa a^2 b^2.                         (3)

At `a=0` the last section is nonzero, and at `b=0` the first is nonzero. At any other simultaneous zero set `x=b/a`. The necessary and sufficient equations are

    x^3=-1,             x^2=-4 kappa.

They have a solution exactly when `kappa^3=-1/64`. Indeed the forward implication follows on cubing the second equation; conversely `x=1/(4 kappa)` satisfies both when this relation holds. This proves basepoint-freeness under (2), with no chart omitted. Since `f_kappa^*O(1)=H` is ample, a curve cannot be contracted, so the morphism is finite.

## 3. An explicit rational inverse on a dense open set

Work on `s=u=1` and put

    x=t,       y=v,      r=xy,      d=y-x,      P=x+y.

Then

    (U0,U1,U2,U3)=(1+dr/2, P/2, rP/2, r^2+kappa d^2). (4)

Let `z_i=Ui/U0` be the target affine coordinates for `i=1,2,3`, and let `lambda=U0`. On the dense open set with `r z1!=0`,

    r=z2/z1,          P=2 lambda z1,
    d=2(lambda-1)/r.

The identity `P^2-d^2=4r` and the last coordinate of (4) give

    (1-r^2 z1^2) lambda^2 -2 lambda +1+r^3=0,
    4 kappa z1^2 lambda^2-z3 lambda+r^2-4 kappa r=0.

Set `A=1-r^2 z1^2`. Eliminating `lambda^2` yields

    lambda = [A(r^2-4 kappa r)-4 kappa z1^2(1+r^3)]
             /[A z3-8 kappa z1^2].                   (5)

The denominator is not identically zero on `S`: at `x=0,y=1` its value is `-kappa`. Evaluating there is only a nonidentity check; the actual inverse is used on the dense open set where all displayed denominators are nonzero. Finally

    x=(P-d)/2,            y=(P+d)/2.

Thus `f_kappa` is birational for every nonzero `kappa`. On (2) it is finite birational from the normal surface `S`, hence is the normalization of its integral image. The image is a surface in `P3`, therefore an integral hypersurface, and its degree is

    H^2 / deg(f_kappa) = (2,2)^2 = 8.

## 4. The residual fourfold line and five forced extra inverse points

The curve `D` maps to the line

    L=(X1=X2=0) subset P3.

By (3) and basepoint-freeness, `f_kappa|D:D=P1 -> L=P1` has pullback `O_L(1)=O_P1(4)` and consequently degree four. Its generic fiber therefore has four geometric points in characteristic zero. In particular `D` is an actual off-`c` conductor prime over `L`, with residual field degree four. This is residual geometry on the actual projective carrier, not an exceptional divisor of a blowup.

The diagonal and antidiagonal meet only at `b=0` and `a=0`. But the two points

    b^2+4 kappa a^2=0,       ab!=0,

also have `U1=U2=U3=0` and `U0!=0`. They are distinct, lie outside `c`, and both map to the endpoint `[1:0:0:0]` of `C0`.

Likewise the three distinct points

    a^3+b^3=0,              ab!=0,

have `U0=U1=U2=0` and `U3!=0`. They lie outside `c` and map to the other endpoint `[0:0:0:1]` of `C0`. The nonvanishing assertions follow from the already established absence of common zeros. Thus at least five distinct extra normalization points occur for every admissible parameter (2).

## 5. Why this excludes every mate degree on these carriers

We first verify that `c` is the **only inverse prime** over `C0`; finite birationality alone would not justify this statement. Apply (4) to a generic target point `[1:z:z^3:z^4]` with `z!=0`. Then `r=z^2`. If the inverse point is off the diagonal, `d!=0` and `lambda!=1`. The identities in Section 3 reduce to

    r=4 kappa(lambda+1),
    lambda-1=64 kappa^3(lambda+1)^4,
    z^2=r.                                             (6)

For completeness, `U3=lambda z^4` first gives `kappa d^2=(lambda-1)r^2`, while `P=2 lambda z` gives `d^2=4r(lambda^2-1)`. Cancelling `lambda-1` gives the first equation of (6); using `d=2(lambda-1)/r` then gives the second. Thus only finitely many constants `lambda`, and consequently only finitely many target values `z`, admit off-diagonal inverse points. Boundary points with `s u=0` have `U1=0`, so cannot map to a generic point of `C0`. The sole inverse prime over `C0` is therefore `c`; every extra inverse point is isolated.

Suppose an ambient form `G` of positive degree `b` cuts out exactly `C0` on `X_kappa`. Its nonzero pullback section has an effective Cartier zero divisor on the smooth integral surface `S`. Its support must equal the entire inverse support of `C0`. Since a principal zero locus on a smooth surface has pure codimension one, this support cannot contain isolated points. Equivalently, since `c` is the sole inverse prime, the pullback divisor would be `m c`; the class relation `m c~bH=2b c` gives `m=2b`, so its support would omit the five explicit isolated points from Section 4. This is impossible. The exclusion holds in every positive mate degree.

## 6. Frontier impact and remaining boundary

This produces actual degree-eight carriers with the expected normalization and polarization and an isomorphic diagonal lift, together with an explicit residual conductor prime. The extra inverse points prevent full singleton support and hence exclude a mate in all degrees on this subfamily.

The calculation does not prove that full-support parameters are absent from the sixteen-parameter smooth-quadric family. It does not test the quadric-cone or plane families and does not compute any surviving conductor phase image. It leaves STCI-Q-0001 and the unrestricted fixed-`C0` STCI question open. The proposition remains unpromoted until independent review reconstructs the basepoint calculation, rational inverse, generic inverse-prime calculation (6), and all-degree support argument.

## Verification record

No inherited mathematical certificate was rerun. All displayed identities are exact polynomial/rational identities proved above. A planned SymPy convenience check was not executed because neither the system Python nor the bundled Python has SymPy and the older `/private/tmp/stci-cas-venv` interpreter is absent in this session; no mathematical assertion depends on that attempted check.

## Appendix A. A simpler companion family with the entire inverse support computed

The following companion family has no exceptional parameter condition beyond `gamma!=0`:

    V0=s^2 u^2 +(1/2)q t v + gamma q^2,
    V1=(1/2)s u p,
    V2=(1/2)t v p,
    V3=t^2 v^2,                         gamma!=0.       (A1)

Again the diagonal maps to the literal `C0`, with balanced first jets `A=x^5,B=0`. This appendix is a second provisional proposition with an especially direct inverse-support calculation.

**Basepoint-freeness.** Since `V3=0` forces `t=0` or `v=0`, it is enough to consider those two boundaries. If `t=0`, the equation `V1=0` forces `uv=0`. At `v=0`, `V0=s^2u^2!=0`; at `u=0`, `V0=gamma s^2v^2!=0`. The argument at `v=0` is symmetric: its two boundary possibilities give either `V0=s^2u^2!=0` or `V0=gamma t^2u^2!=0`. Thus (A1) has no basepoint. As before ampleness makes the map finite.

**Birationality.** On `s=u=1`, with `r=xy`, `P=x+y`, `d=y-x`, the coordinates are

    (V0,V1,V2,V3)=(1+dr/2+gamma d^2, P/2, rP/2, r^2).

For target ratios `z_i=Vi/V0` and `lambda=V0`, an explicit rational inverse on a dense open set is

    r=z2/z1,                 lambda=r^2/z3,
    P=2 lambda z1,           D=P^2-4r,
    d=2(lambda-1-gamma D)/r,
    x=(P-d)/2,               y=(P+d)/2.                (A2)

Here `D=d^2` on the actual image; there is no extraction of a square root in the inverse. Thus the finite map is birational, its image is an integral degree-eight hypersurface, and `S` is its actual normalization.

**Entire inverse support.** For a target point `[1:z:z^3:z^4]` with `z!=0`, equations (A2) force

    r=z^2,       lambda=1,       P=2z,       D=0,       d=0.

Boundary points with `su=0` have `V1=0` and cannot map to such a point. Consequently the unique inverse point of every nonendpoint point of `C0` is its point on `c`.

Over `[1:0:0:0]`, the equation `V3=0` again forces `t=0` or `v=0`, and direct substitution gives precisely three inverse points: the diagonal point at `t=v=0`, and the two off-diagonal corners

    A=((1:0),(0:1)),         B=((0:1),(1:0)).

Both corners have image `[1:0:0:0]` because only `V0=gamma q^2` is nonzero there.

Over `[0:0:0:1]`, one has `tv!=0` and `V2=0`, so `p=0`. Parametrize `D=(p=0)` by `(s:t)=(a:b),(u:v)=(a:-b)`. Then

    (V0,V1,V2,V3)=(a^4+a b^3+4gamma a^2b^2,0,0,b^4).

The point `a=0` is the diagonal inverse point at infinity. The remaining inverse points are exactly the roots, with `x=b/a`, of

    1+4gamma x^2+x^3=0.                              (A3)

Every root is finite and nonzero, hence lies outside `c`. There are three distinct such points unless `256gamma^3+27=0`, when there are two distinct points (one double root). A triple root is impossible: the polynomial has nonzero constant term and zero linear coefficient. Thus the full reduced inverse support is exactly `c`, the two corners, and the two or three points from (A3). In particular for `gamma=1` it is exactly `c` plus five isolated extra points.

The same pure-divisor argument from Section 5 excludes a mate in every positive degree on every carrier in (A1). The antidiagonal again maps with degree four to `L`, since its two nonzero coordinate sections in the displayed formula have degree four and no common root. Hence it is an actual conductor prime with residual field degree four.

**Audit target.** The cleanest single explicit example is `gamma=1` in (A1), for which the full inverse support has the exact five isolated points just described. The first family (1), with condition (2), and the companion family (A1), with `gamma!=0`, are the two claims of this note. No larger projection-parameter claim is proposed.


---

## 2026-10-19-quadric-antidiagonal-fourfold-line-independent-audit

# Independent audit of the quadric-normalization fourfold-line families

Date: 2026-10-19. Reviewer: `carrier_model_audit`, with a separate
Section 5 microaudit by `inverse_branch_microaudit`.

**Outcome: PASS for the two explicitly stated families and their all-degree
mate exclusions.** This is independent review evidence for the
[source proposal](2026-10-19-quadric-antidiagonal-fourfold-line-proposal.md),
not a canonical promotion. No accepted mathematics or canonical record was
edited, and no inherited quartic proof or certificate was rerun.

## Scope and dependencies

The checked ground field is algebraically closed of characteristic zero.
The literal embedded curve is

    C0=[s^4:s^3t:st^3:t^4] in P3.

The source surface is the smooth quadric `S=P1_(s:t) x P1_(u:v)`, with
diagonal `c=(sv-tu=0)` and polarization `H=O(2,2)`. The review covers:

1. Family (1) of the proposal, for precisely
   `kappa!=0` and `kappa^3!=-1/64`.
2. Companion family (A1), for every `gamma!=0`.

For each, the four displayed sections define an actual finite
normalization of an integral degree-eight hypersurface. The diagonal maps
isomorphically to `C0`, but the full reduced inverse support contains
isolated points outside `c`, excluding a mate in every positive degree.
The antidiagonal is an actual conductor prime mapping with residual degree
four to the line `(X1=X2=0)` downstairs.

[STCI-R-0002](../results/cartier_singleton_lift.md) is used only to identify
the relevant necessary normalization model; neither family meets its full
singleton-support hypothesis.
[STCI-R-0003](../results/fixed_carrier_conductor_criterion.md) supplies the
promoted isolated-inverse-point obstruction. This review also reconstructs
that elementary obstruction directly, without invoking the remaining
conductor descent lattice theorem. The balanced first-jet formulas are read
from Section 4 of the
[October 14 projection note](2026-10-14-generalization-projection-contact-phase-criterion.md).
The projection-phase reduction is not needed as a premise.

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

Eliminating the quadratic term yields exactly formula (5) of the source,
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
Additionally, the two cross-corners from Section 1 also map to
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

For (A1), `V3=0` forces `t=0` or `v=0`. At `t=0`, the equation `V1=0`
forces `uv=0`; the respective nonzero coordinates are `s^2u^2` or
`gamma s^2v^2`. At `v=0`, the two cases similarly give `s^2u^2` or
`gamma t^2u^2`. Thus every `gamma!=0` is basepoint-free, with no further
condition. Ampleness again gives finiteness.

On the affine chart the coordinates are

    (1+dr/2+gamma d^2,P/2,rP/2,r^2).

Recover successively

    r=z2/z1, lambda=r^2/z3, P=2lambda z1,
    D=P^2-4r, d=2(lambda-1-gamma D)/r.

Since `D=d^2` on the image, this proves the rational inverse (A2)
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
follow exactly as in Section 3.

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
characteristic-zero question remain open. Canonical promotion, if any,
requires its own recorded scope-preserving change.

## Verification record

The reviewer independently reconstructed every displayed identity,
boundary alternative, parameter exception, and divisor-support argument
above. The separate microaudit independently confirmed the kappa-family
inverse-prime calculation and all-degree obstruction. No CAS calculation
or finite numerical sample is used as a mathematical premise, and none
of the conclusions relies on rerunning an inherited proof.
