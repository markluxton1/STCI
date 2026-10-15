# Torsion divisors and the second zero locus on quadratic root compatibility

Date: 2026-10-15. Author: `geometric_locus`.

Status: **NEW STRUCTURAL PROOFS; independent review passed.** The
accepted universal first incidence, its smooth seed and differential,
and the accepted canonical second obstruction and its nonzero seed value
are premises. None of those computations is rerun. This note proves a
Picard-theoretic description of the torsion loci and a dimension bound
on one specified torsion branch of the second zero locus. No additional
seed or coefficient profile is computed.

## 1. Setup and scope

Let `U_sm` be the open subset of `P8` parametrizing smooth divisors

    Z_f=(f=0) in P1 x P1,
    f=a(z)u^2+b(z)uv+c(z)v^2,

of type `(2,2)`. Write

    A=O_Z(1,0), B=O_Z(0,1), eta=B tensor A^-1.

Both `A` and `B` have degree two, and `eta` is nontrivial. Indeed if
the two line bundles were isomorphic, their complete degree-two linear
systems would identify the two projections up to a projective
automorphism, forcing the image to be a graph.

Let `C` be the reduced irreducible component of the accepted first
compatibility scheme `K` through

    f0=(z^2+4)u^2+(z^2-8)v^2.

The accepted results give: `C` is smooth of dimension four at `[f0]`;
the second obstruction is a canonical section `sigma2` of the rank
sixteen bundle `Q2(1)` on `K`; and `sigma2(f0)!=0`. Put

    Y=Z(sigma2) intersect C.

In particular `Y` is a proper closed subscheme of `C`, with support
of dimension at most three. The question here is what torsion adds.
Any application to the first-principal-ideal CI lane keeps the accepted
restriction `s>4` and the hypotheses of the actual-CI-to-root-curve bridge.

## 2. The ruling involutions encode the Picard torsion exactly

Let `i_A` and `i_B` be the deck involutions of the two degree-two
projections of the elliptic curve `Z`. Choose an origin temporarily and
identify degree-two divisor classes with their sums in the elliptic
group law. If the sums for `A,B` are `a_A,a_B`, then

    i_A(p)=a_A-p, i_B(p)=a_B-p.

It follows that

    tau=i_B i_A: p -> p+(a_B-a_A)=p+eta.

This identity is independent of the temporary origin. Consequently

    eta has exact order n  <=>  tau has exact order n.

Thus the spectral torsion requirement is a finite-order condition on a
canonical automorphism of the root curve. It is not an assertion that
an ambient coordinate involution exists for every torsion order.

For fixed `n>=2`, define

    T[n]={f in U_sm : eta^n=O_Z}.

These are algebraic relative-Picard zero loci. In characteristic zero
they are smooth divisors of `U_sm`, of dimension seven; exact-order
strata are unions of components of these divisors. Here is a local
moduli proof of this assertion.

After an etale choice of an origin with `A=O_Z(2O)` and, if desired,
level structure to remove finite automorphisms, a smooth `(2,2)`
embedding is specified by an elliptic curve, a nonzero point `eta` of
its degree-zero Picard curve, and frames of the two degree-two linear
systems. Conversely, two distinct degree-two systems embed an elliptic
curve into `P1 x P1`: if two points have the same images, they are
interchanged by both deck involutions, forcing `A=B`; simultaneous
ramification would likewise force `A=B`. The frames give the six
projective-coordinate parameters. The local moduli parameters are
therefore the elliptic modulus and the one-dimensional Picard parameter
`eta`, together with those six coordinate parameters.

Multiplication by `n` on a relative elliptic Picard curve is finite
etale in characteristic zero: its tangent map is multiplication by
the invertible integer `n`. Its torsion subgroup is finite etale over
the elliptic-modulus base. Thus the fixed torsion condition removes
exactly the Picard parameter and is smooth of codimension one. This
also shows that exact torsion order is locally constant inside `T[n]`.

This ambient divisor statement gives no automatic transversality to
`K` or to the second zero scheme. For an irreducible four-dimensional
compatibility component, a fixed torsion divisor either contains the
component or cuts a divisor (possibly empty). Further dimension drops
need further evidence.

## 3. Exact order two is a coefficient determinant

Write

    a=a0+a1 z+a2 z^2, b=b0+b1 z+b2 z^2,
    c=c0+c1 z+c2 z^2,

and form the coefficient matrix

              [ a0 a1 a2 ]
    M(f) =    [ b0 b1 b2 ].
              [ c0 c1 c2 ]

On `U_sm` one has the exact equivalence

    eta has order two  <=>  det M(f)=0.                 (1)

For the forward implication, the deck involution `i_A` acts on
`Pic^2(Z)` by

    i_A^*L=A^2 tensor L^-1.

When `eta^2=O`, it therefore preserves `B`. Its action on `H0(B)`
induces a projective involution on the second `P1`. This involution
is nontrivial: if it were trivial then `i_A` would also be the deck
involution of the second projection, forcing `A=B`. Diagonalize it
in characteristic zero. The root equation is then an eigenvector for
`[u:v] -> [-u:v]`. The odd eigenspace of binary quadratics is the
one-dimensional span of `uv`, which would give a reducible singular
divisor. Therefore the equation lies in the even eigenspace spanned
by `u^2,v^2`, so the coefficient matrix has rank at most two.

Conversely, basepoint freeness excludes rank at most one: then `f`
would have a common homogeneous quadratic factor in the base
coefficients, with a base zero. At rank two, the binary fiber
quadratics of `f` lie in a two-dimensional pencil. If the annihilator
of this pencil is a degenerate binary quadratic, the pencil has a
common direction root, so `f` has a fixed linear direction factor.
The remaining factor meets that fixed section in degree two, contrary
to smoothness. The annihilator is consequently nondegenerate. A
constant change of direction coordinates takes this pencil to the
span of `u^2,v^2`. Thus `f` becomes diagonal. On a smooth diagonal
curve, the defining equation gives `A^2=B^2`: the zero divisor of a
coefficient section of `A^2` is twice the zero divisor of a direction
section of `B`. Since `A!=B`, the order is exactly two. This proves (1).

Thus `T[2]` is the cubic determinantal hypersurface `det M=0` on the
smooth root open. It is smooth there because all of its matrices have
rank exactly two. This provides a concrete equation for the relevant
Picard divisor, independently of any second-obstruction computation.

## 4. The first compatibility component meets this divisor transversely

At the accepted seed,

    M(f0)=[ [4,0,1], [0,0,0], [-8,0,1] ].

Therefore

    d(det M)_(f0)=12 delta b1.                        (2)

Use the already accepted quotient differential of the first obstruction,
in coefficient order `(a0,a1,a2,b0,b1,b2,c0,c1,c2)`:

```
     [  0    2   0   1/4  0   2    0   -2    0  ]
     [  1    0   8    0   4   0   -1    0  -20  ]
R =  [ -5/2  0   4    0   2   0  -1/2   0    2  ].
     [  0    8   0    1   0  -4    0    4    0  ]
```

The coefficient variation

    delta f=zuv+4v^2

has `delta b1=1`, `delta c0=4`, with all other coefficients zero.
It lies in `ker R`, since its four image entries are

    0, 4-4, 2-2, 0.

It is a genuine projective tangent direction, not the scalar direction
of `f0`. Since the accepted first incidence is smooth here, it is a
tangent direction of `C`. Equation (2) evaluates to `12`, not zero.
Thus `C` and `T[2]` meet transversely at `[f0]`.

It follows that their intersection is smooth of dimension three in a
neighborhood of `[f0]`. Let `D` denote the reduced irreducible component
of `C intersect T[2]` through that point; this component is unique at
the seed and has dimension three.

## 5. A proved bound on the torsion-two part of the second zero locus

The accepted scalar pairing for the canonical second section gives
`sigma2(f0)!=0`. Therefore `sigma2|D` is not identically zero. Its zero
scheme is a proper closed subscheme of the irreducible three-dimensional
variety `D`. Consequently

    dim support(Y intersect D) <= 2.                  (3)

Equivalently, a nonempty open subset of this three-dimensional
torsion-two branch fails the second ambient lifting step. Bound (3)
uses a proved torsion equation, a proved tangent direction, and a
known nonzero section value; it is not an expected-dimension argument
from the rank sixteen target.

For every fixed even `n`, the local germ of `T[n]` at the seed equals
the germ of `T[2]`. Indeed the `n`-torsion subgroup of the relative
Picard curve is finite etale, and the order-two component through the
seed is open and closed in it. Equivalently, after writing `n=2m`,
the zero component of `[m]` can be isolated etale-locally near
`[2]eta=0`. Thus the same bound applies to the local torsion branch
through the seed for the fixed spectral degrees `8` and `12`.

Other components of `C intersect T[2]`, exact torsion orders greater
than two, and other components of `Y` are not controlled by (3).
In particular this does not prove that `Y` is empty, nor that its
entire intersection with any fixed torsion divisor has dimension at
most two. A different torsion component could be contained in `Y`.

For unbounded second-relation degree, the union of all torsion orders
is a countable union of algebraic loci, not one fixed torsion divisor.
Noetherianity alone does not replace that union by finitely many
orders. The separate finite-type theorem for a uniquely liftable
higher-obstruction tower concerns its closed zero schemes; it does
not justify such a replacement of torsion loci or an algebraization
to projective equations.

Independent review is recorded in
[the structural torsion audit](2026-10-15-generalization-quadratic-root-torsion-second-zero-independent-audit.md).
No commit or memory update was made.
