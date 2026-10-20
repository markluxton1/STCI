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
