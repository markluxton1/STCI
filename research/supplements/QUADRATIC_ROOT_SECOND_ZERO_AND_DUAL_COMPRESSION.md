# quadratic root second zero and dual compression

Permanent mathematical dossier preserving complete arguments, assumptions, characteristic boundaries, counterexamples and unresolved claims. No new theorem promotion is implied.

---

## 2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry

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


---

## 2026-10-15-generalization-quadratic-root-torsion-second-zero-independent-audit

# Independent review of torsion geometry on the second zero locus

Date: 2026-10-15. Reviewer: `universal_root_obstruction`.
Status: **PASS for the stated structural Picard, determinant, and
specified-component dimension claims**. The universal first incidence,
its accepted seed differential, and the actual second section's accepted
nonzero value are premises. No accepted certificate was replayed and no
new seed was evaluated.

Reviewed proof:
[torsion divisors and the second zero locus](2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry.md).

## 1. Intrinsic torsion and its ambient divisors

For a smooth `(2,2)` curve, both ruling systems have degree two. With an
origin on its elliptic normalization, the deck involution of a divisor
class with sum `a` is `p -> a-p`. Therefore the product of the two deck
involutions is translation by the degree-zero difference `eta=B-A`.
Its exact order is exactly the order of `eta`. This statement concerns
automorphisms of the root curve; it does not lift them to the ambient
formal neighborhood.

The local-moduli argument in the proposal is valid after an etale choice
of an origin with `A=O(2O)` and suitable finite level structure. The data
are an elliptic modulus, a nonzero Picard point `eta`, and two projective
coordinate frames. The two distinct degree-two systems give an embedding:
a pair of identified points would be interchanged by both ruling deck
involutions and force their centers, hence the systems, to agree;
a simultaneous ramification point forces the same equality. Thus this
parameter description covers the smooth root open locally with its
correct eight dimensions.

For fixed `n`, multiplication by `n` is etale on the relative elliptic
Picard curve in characteristic zero. Its kernel is finite etale, and
pullback along the free Picard parameter gives a smooth codimension-one
torsion condition. No transversality to the first compatibility scheme
follows from this ambient statement alone. Distinct exact-order strata
are open and closed within the fixed `n`-torsion condition, explaining
the stated equality of local germs at the order-two seed for each fixed
even `n`.

## 2. The cubic determinant is exactly the order-two locus

The equivalence `eta^2=1 <=> det M=0` is correct on the smooth root open.
If `eta^2=1`, the first ruling deck involution preserves the second
line bundle. It induces a nontrivial projective involution on the second
ruling: a trivial induced involution would fix both coordinates of the
embedded curve and hence the curve itself pointwise. A constant direction
coordinate change diagonalizes this involution. The odd quadratic
eigenspace consists only of multiples of `uv`, which cannot cut a smooth
`(2,2)` divisor. The root equation is therefore even, so its coefficient
matrix has rank at most two.

Conversely, rank one is excluded by basepoint freeness: all coefficient
quadratics would be proportional and have a common homogeneous base
zero. Rank two puts the fiber quadratics in a pencil. A degenerate
annihilator of that pencil is evaluation at a direction point, so it
means a common direction root. The corresponding fixed direction section
meets the remaining `(2,1)` component in degree two, contradicting
smoothness. A nondegenerate annihilator can be taken by a constant
projective direction change to the annihilator of `span(u^2,v^2)`.
The diagonal equation then gives `A^2=B^2` by its zero divisors.
The two line bundles are unequal for an embedded smooth `(2,2)` root,
so the order is exactly two.

All determinant-zero matrices on this open have rank exactly two.
The determinant hypersurface is smooth at every rank-two matrix, so
the proposal's global smooth-divisor statement on this open is justified.

## 3. The dimension drop is proved on the named component

At the accepted seed, the determinant differential is `12 delta b1`.
The variation `delta b1=1, delta c0=4` is killed by the accepted first
quotient differential: the only potentially nonzero rows are `4-4`
and `2-2`. It is not scalar variation of the seed. The determinant
functional takes value twelve on it. Thus the smooth four-dimensional
first compatibility component is transverse to the order-two divisor
at this seed. Their intersection has one smooth three-dimensional local
component there, whose reduced global irreducible component is the
specified `D`.

The actual second section is already known to be nonzero at the same
point. Its restriction to `D` is therefore not identically zero. The
support of its zero scheme is a proper closed subset of the irreducible
three-dimensional variety `D`, and hence has dimension at most two.
This is an actual dimension bound, not a dimension expectation from a
rank-sixteen vector bundle.

This argument does not control other components of the torsion
intersection or exact orders greater than two. It applies to the local
branch through the seed for fixed even spectral degrees, including eight
and twelve. It does not bound the entire torsion union, prove emptiness
of the second zero locus, or supply an actual CI. The proposal preserves
all those boundaries, as well as `s>4` in its stated CI application.

No commit or memory update was made.


---

## 2026-10-15-generalization-quadratic-root-global-second-dual-compression

# A chart-free complete 25-pairing test for the universal second obstruction

Date: 2026-10-15. Author: `universal_root_obstruction`.
Status: **NEW GLOBAL REDUCTION; independent review passed.** Accepted
first/second ambient class constructions, the exact embedded chart, and
their earlier seed certificates are premises. None is rerun. This note
compresses the entire second obstruction into one polynomial family with
no coefficient chart, then exports a single bounded-elimination input.
It does not yet assert that the second zero scheme is empty.

## 1. The global dual presentation removes 39 unit variables

Let `f=a(z)u²+b(z)uv+c(z)v²` have base degree two. Throughout this
section assume only that its three homogeneous base coefficients have
no common zero; the root divisor can be singular or nonreduced. The
transpose of multiplication by `f` in the direction ruling is

```
        [ a b c 0 0 ]
T_f  =  [ 0 a b c 0 ] : O_P1^5 -> O_P1(2)^3.
        [ 0 0 a b c ]
```

It is surjective on every base fiber: its transpose is multiplication
by a nonzero binary quadratic from degree two to degree four, which is
injective. Thus `W=ker T_f` is a rank-two vector bundle with
`det W=O(-6)`.

The complete Serre-dual space of the actual second obstruction consists
of polynomial vectors `q=(q0,...,q4)`, of degree at most ten, such that

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0,
    a q2+b q3+c q4=0.                                 (1)

It is exactly `H0(P1,W(10))`, of dimension sixteen. This is the dual of
`coker[H1 O(-14,2) --f--> H1 O(-12,4)]`; no first-order normal-symbol
replacement is made.

Dualizing the exact sequence defining `W`, and using the canonical
rank-two identification `W*=W tensor(det W)^-1`, gives

    0 -> O(-2)^3 -> O^5 -> W(6) -> 0.                 (2)

After twisting by `O(4)`, the left term is `O(2)^3` and has no `H1`.
Consequently

    H0(O(4))^5 -> H0(W(10)) -> 0                     (3)

is surjective. Its source dimension is twenty-five and its kernel
dimension is nine. Thus twenty-five scalar pairings give a complete
test for all sixteen actual obstruction coordinates. This works on
the entire basepoint-free family, including every splitting-jump locus.
It makes no choice of an invertible coefficient or matrix minor.

For an explicit polynomial version, form a skew `5 by 5` matrix `P_f`.
With zero-based indices `0,...,4`, put for `i<j`

    (P_f)_ij=(-1)^(i+j+1) det(T_f with columns i,j deleted),
    (P_f)_ji=-(P_f)_ij,    (P_f)_ii=0.                (4)

Then `T_f P_f=0`. Its five columns are the five generating sections of
`W(6)` in (2), written as signed complementary maximal minors. Each
entry has degree at most six in the affine base coordinate and is cubic
in the coefficients of `f`.

Let `R4` be any Cech representative of the actual second class, with
quartic direction components `r0,...,r4` and Laurent powers retained in
`z^-11,...,z^-1`. The second obstruction vanishes if and only if

    coefficient_z^-1 [ z^j sum_i (P_f)_i,l r_i ]=0
                for l=0,...,4 and j=0,...,4.          (5)

The criterion is scheme-theoretic. Indeed the family version of (3) is
a surjection of vector bundles; the twenty-five pairings generate the
same zero ideal as the rank-sixteen second section. It follows that
(5) does not lose exceptional coefficient strata or retain only generic
rank information.

For projective coefficient space `U`, the universal matrix is
`O^5 -> O(2) tensor O_U(1)^3`. Thus
`det W=O(-6) tensor O_U(-3)`, and the globally correct version of (2)
is

    0 -> O(-2) tensor O_U(-1)^3
      -> O^5
      -> W(6) tensor O_U(3) -> 0.

After the same base twist by four and pushforward, (3) becomes an
everywhere-surjective bundle map from `O_U^25` onto
`p_*W(10) tensor O_U(3)`. The dual of the actual second obstruction
bundle is `p_*W(10) tensor O_U(-1)`. Twisting the displayed surjection
by `O_U(-4)` therefore gives a surjection from `O_U(-4)^25` onto that
dual. This verifies the scheme-theoretic claim and the homogeneous
coefficient degree four of the scalar pairings. On the affine coefficient
cone the representatives are exactly (4); the cubic coefficient degree
of the Plucker vectors is a twist, not a denominator.

## 2. A single actual-chart model supplies R4 universally

The accepted full embedded transition is used as input:

```
den=z⁴+u+(3/2)zv, w=(z³+v)/den,
a'=z/den−w³, b'=1/den−w⁴,
u'=a'/2, v'=−3w a'+2b'.
```

Write `f1` for the second-chart root equation obtained by reversing each
quadratic coefficient polynomial:

    f1=(a2+a1w+a0w²)u'²
       +(b2+b1w+b0w²)u'v'
       +(c2+c1w+c0w²)v'².

Expand only through normal degree four. Let

    beta=-2z^-4u-z^-3v,
    h=sum_(k=-6)^(-1) (h_(u,k)u+h_(v,k)v)z^k,
    L1=h+beta,
    S3=[z^16 f1]_3-L1*f.                             (6)

Its sixteen middle Laurent coefficients, on `z^-4,...,z^-1` times
binary cubics, are the universal first equations. They are equivalent
to the accepted `A_f h=d_f`. No new first-incidence rank claim is needed.

Define the local cubic corrections by their regular Cech parts:

    G0 = the z>=0 part of S3,
    z^-5 G1(z^-1;u,v) = - the z<=-5 part of S3.       (7)

All coefficients of `G0` have degree at most one in `z`, and those of
`G1` have degree at most one in `w`; these bounds follow from the finite
supports in (6), with no coefficient open imposed. On the first zero
scheme, (7) gives the exact cubic patch identity

    [z^16(f1+G1)]_3-G0-L1*f=0.

The universal representative used in (5) is

    R4=pr_(z^-11,...,z^-1)
         ( [z^16(f1+G1)]_4 - L1*G0 ).                (8)

Here `G1` is substituted using the full nonlinear coordinates `w,u',v'`.
The base derivative, the first equation unit, and its product with the
first correction are all retained. The unknown next equation unit is
a multiple of `f`; it disappears under every pairing (1). Unknown
quartic local corrections are Cech coboundaries. Therefore no thirty-nine
quartic unit variables are required in the final system.

The model has the nine coefficient variables of `f` and twelve variables
of `h`. Its sixteen first equations are bilinear. Its twenty-five second
equations have total degree at most six, homogeneous degree four in the
coefficients of `f` and degree at most two in `h`. There is one affine
model for the full coefficient cone. Scale of `f` is harmless on the
smooth open and need not be normalized by a coefficient chart.

## 3. The smooth open is one homogeneous binary-quartic discriminant

Put

    Delta(z)=b(z)^2-4a(z)c(z)=d0+d1z+d2z²+d3z³+d4z⁴,

regarded throughout as the binary quartic
`d0 Y⁴+d1 XY³+d2 X²Y²+d3 X³Y+d4 X⁴`.
Define

    I=12d4d0-3d3d1+d2²,
    J=72d4d2d0+9d3d2d1-27d4d1²-27d3²d0-2d2³,
    Disc=(4I³-J²)/27.                                (9)

In characteristic zero this is the homogeneous binary-quartic
discriminant. It is homogeneous of degree twelve in the nine coefficients
of `f`.

The condition `Disc!=0` is exactly the smooth-root condition. A common
base zero of `a,b,c` gives a common homogeneous linear factor and forces
its square to divide `Delta`, so it makes `Disc=0`. Thus the open already
implies basepoint freeness. On that open the double-cover discriminant
is the branch divisor; it has four simple roots exactly when the root
curve is smooth. Conversely every smooth `(2,2)` root gives a finite
separable degree-two map with four simple branch points, so its binary
discriminant is nonzero.

No leading affine coefficient is inverted. In particular `d4=0` with
`d3!=0` represents a simple branch point at infinity and is allowed by
(9). A second zero at infinity gives vanishing discriminant, as required.
The formula does not silently discard degree-drop cases.

The single global smooth-family ideal is therefore generated by the
sixteen equations from (6), the twenty-five pairings (5), and

    smoothInverse*Disc-1.                             (10)

It is the full smooth `K2` incidence, not a finite set of samples or a
union missing coefficient charts. Proving it is the unit ideal would
prove `K2` empty on the entire smooth `(2,2)` family. Failure to finish
an elimination proves nothing about emptiness.

## 4. Exact export and one bounded prospect

The new standard-library sparse generator is
[global second-model generator](../computations/generalization_quadratic_root_global_second_model.py).
It exports
[one characteristic-zero M2 model](../computations/generalization_quadratic_root_global_second_model.m2)
and [its term/count metadata](../computations/generalization_quadratic_root_global_second_model.json).
The new algebraic consistency check verifies `T_f P_f=0` identically;
no accepted seed or previous rank verifier is invoked.

The exported system has twenty-two variables including `smoothInverse`,
sixteen first equations, twenty-five complete dual second equations, and
one discriminant inverse equation. The second equations have at most
535 terms each; the homogeneous discriminant has 1010 terms. These counts
are exact export metadata, not complexity or solvability claims.

The new proof and the exported generator algorithm passed
[the independent compression audit](2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md).
Exactly one bounded M2 launch was made, with the heavy quintic window
held separately. Its supervisor hit a sandbox `PermissionError` when
invoking `/bin/ps` for RSS monitoring. The M2 child had a 45-second CPU
limit. Its PID `32960` was subsequently confirmed absent with authorized
process inspection; the original exit code was not recoverable after the
supervisor failed. Captured stdout contains `MODEL_READY`, but no
`GB_COMPLETE` or unit-ideal marker. Thus the run supplies no elimination
result and no mathematical conclusion.

The input, exact source/supervisor snapshots, hashes, captured logs, and
terminal PID check are in
[the execution record](../validation/2026-10-15-quadratic-root-global-second/attempt-01-QQ-full-smooth-family/execution-record.json).
The future supervisor now checks monitor availability before launching
any child and stops safely if monitoring later fails; it was not rerun.
The quintic owner received confirmation that this process was absent
before using the next heavy computation window. No extra coefficient
chart, seed, profile, or second global launch was opened.

The accepted all-orders formal nonexistence theorem proves an existential
empty stage on the smooth family. This compression does not supply a
value of that stage. In particular no `N<=5`, all-smooth second
nonvanishing, actual-CI exclusion, or unrestricted STCI conclusion is
claimed until an exact global certificate or a new geometric proof exists.
No commit or memory update was made.


---

## 2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit

# Independent audit of the twenty-five global second-obstruction tests

Date: 2026-10-15. Author: `geometric_locus`.

Status: **THE GLOBAL COMPRESSION, UNIVERSAL MODEL ALGORITHM, AND
HOMOGENEOUS SMOOTHNESS CRITERION PASS INDEPENDENT REVIEW.** Accepted first and second obstruction
constructions are inputs. No accepted seed computation, verifier, or
profile calculation is repeated. This audit uses bundle duality,
Laplace identities, and a local double-cover calculation.

Companion note:
`2026-10-15-generalization-quadratic-root-global-second-dual-compression.md`.
The final companion note and
`../computations/generalization_quadratic_root_global_second_model.py`
were read after this mathematical audit was drafted. Their algorithm
was compared with the proof; no old verifier, seed test, or CAS was run.

## 1. The correct dual bundle on the whole basepoint-free locus

Fix a homogeneous basepoint-free triple `a,b,c` of degree two on `P1`.
Let `f=a u^2+b uv+c v^2` and consider

              [ a b c 0 0 ]
    T_f =     [ 0 a b c 0 ] : O^5 -> O(2)^3.
              [ 0 0 a b c ]

At every base point this is the transpose of multiplication by the
nonzero binary quadratic `f` from binary quadratics to binary quartics.
Multiplication by a nonzero polynomial is injective, so the fiber rank
is three everywhere. Therefore

    0 -> W -> O^5 -> O(2)^3 -> 0

is exact with `W` a rank-two vector bundle and `det W=O(-6)`.
Neither smoothness nor reducedness of the root divisor is needed.

The second Cech target has quartic coefficients and powers
`z^-11,...,z^-1`. Its dual consists of five polynomials of degree at
most ten. An element annihilates multiplication by `f` exactly when

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0,
    a q2+b q3+c q4=0.

Thus the full sixteen-dimensional dual obstruction space is
`H0(P1,W(10))`, with the monomial-dual pairing given by the coefficient
of `z^-1` in `sum q_i r_i`. There are no binomial factors in these
formulas for the specified coefficient bases.

## 2. Rank-two duality supplies a global generating presentation

For a rank-two bundle, the exterior pairing gives a canonical
isomorphism

    W^* = W tensor (det W)^-1 = W(6).

Dualizing the exact sequence in Section 1 and using this isomorphism
gives

    0 -> O(-2)^3 -> O^5 -> W(6) -> 0.

Twisting by `O(4)` gives

    0 -> O(2)^3 -> O(4)^5 -> W(10) -> 0.              (1)

Since `H1(P1,O(2))=0`, global sections of (1) are surjective onto
`H0(W(10))`. In particular the twenty-five sections obtained from the
five displayed generators and the five degree-four base monomials
span the entire dual obstruction space. The kernel on global sections
has dimension nine and the target has dimension `25-9=16`.

This proves spanning uniformly; no splitting choice, minor
localization, or denominator is used. It therefore includes splitting
jumps, repeated direction factors, singular roots, and nonreduced
roots, subject only to the basepoint-free hypothesis.

## 3. The signed complementary minors give those five generators

Index rows and columns of a skew five-by-five matrix `K` by
`0,...,4`. For `i<j`, put

    K_ij=(-1)^(i+j+1) det(T_f with columns i,j omitted),
    K_ji=-K_ij, K_ii=0.                              (2)

Every nonzero entry is a homogeneous degree-six base polynomial and a
homogeneous cubic in the equation coefficients. The Laplace expansion
of a four-by-four determinant with one repeated row gives `T_f K=0`.
Thus each column is a section of `W(6)`.

These are exactly the five generators in the dual presentation, up
to the harmless common sign from choosing the determinant orientation.
Indeed the complementary-minor bivector is the exterior dual of the
three rows of `T_f`; contraction identifies the quotient of `O^5`
by the transpose image with `W tensor (det W)^-1`. At a local frame
where `T_f=[I3 | 0]`, formula (2) has `K_34=1`, `K_43=-1`, and all
other entries zero. It is the required nondegenerate rank-two
alternating pairing on the kernel. Change of frames proves the
identification everywhere.

Formula (2), together with skew symmetry, is necessary: assigning
the same complementary-minor sign to both `K_ij` and `K_ji` would
generally destroy the kernel identity. An overall common sign, or
using rows in place of columns with the corresponding sign, does not
change the zero tests.

On the affine base chart, the twenty-five full dual generators are

    z^k K_column_i, 0<=i<=4, 0<=k<=4.

Homogeneously, `z^k` means the basis
`Z1^k Z0^(4-k)` of `H0(O(4))`; consequently the construction includes
base infinity.

## 4. Exact equivalence with the second class and parameter degrees

Let `R4=sum r_i(z)u^(4-i)v^i` be the actual second discrepancy after
retaining the accepted first cubic correction and equation unit.
Its second class vanishes if and only if all twenty-five scalars

    coefficient_z^-1[ z^k sum_j K_ji r_j ]

vanish. One direction follows because every displayed vector
annihilates multiplication and coboundaries. The converse follows
from the spanning theorem of Section 2 and nondegeneracy of the
finite-dimensional Cech/Serre pairing. This removes the thirty-nine
unknown quartic unit coefficients without replacing the quotient
by a smaller test space.

On projective coefficient space, each `K` entry has coefficient degree
three. Thus there is a fiberwise surjective bundle map

    25 O(-3) -> Q2^*.

Pairing with the accepted canonical section in `Q2(1)` produces
twenty-five sections of `O(4)` on the first compatibility incidence.
When that incidence is written with equation coefficients `f` and
the unique first correction coordinates `h`, these tests can be
written polynomially in `f,h` after the actual first-patch formulas
are exported. The bundle argument does not require a choice of
quartic correction variables. It does not itself compute the
universal `R4` or prove that the twenty-five equations have no smooth
solutions.

The parameter twists in the companion note agree with this statement.
Write `H=O_U(1)`. The universal map is
`O^5 -> (O(2) tensor H)^{direct sum 3}`,
so `det W=O(-6) tensor H^-3`. Rank-two duality gives
`W^*=W(6) tensor H^3`. The pushed-forward generating presentation is

    O_U^25 -> p_*W(10) tensor H^3 -> 0.

Here `Q2^*=p_*W(10)`. The actual obstruction bundle is
`V2=Q2 tensor H`, so its dual is `p_*W(10) tensor H^-1`.
Twisting the last surjection by `H^-4` gives exactly the companion
note's `25 H^-4 -> V2^*`. This is the same as the earlier
`25 H^-3 -> Q2^*`; it introduces no extra coefficient factor or
denominator. In particular the scalar tests have coefficient degree
four, as required.

## 5. The homogeneous quartic discriminant detects smoothness

Let

    Delta=b^2-4ac in H0(P1,O(4)).

For a basepoint-free triple over an algebraically closed field of
characteristic zero, the root divisor `Z_f` is smooth if and only if
the homogeneous binary quartic `Delta` has four distinct zeros, or
equivalently its binary-quartic discriminant is nonzero.

To see this locally, first suppose `a` is a unit. The fiber point
`v=0` is absent there, and the equation in `x=u/v` becomes

    y^2=Delta, y=2a x+b.

The analogous chart works when `c` is a unit. At a zero of `Delta`,
basepoint freeness forces at least one of `a,c` to be a unit, so
these charts cover every possible ramification point. The double
cover is smooth at such a point exactly when the local vanishing
order of `Delta` is one: in the local equation `y^2-Delta(t)=0`,
the fiber derivative vanishes at `y=0`, and the base derivative is
nonzero precisely for a simple zero. Away from `Delta=0`, the cover
is etale and smooth. If only `b` is a unit and `a=c=0` at a base
point, then `Delta=b^2` is nonzero there and the two direction roots
are distinct, so no omitted singularity occurs.

This argument uses a local parameter at every point of the base,
including infinity. The quartic must remain homogeneous: dropping
its apparent affine degree and ignoring its zero at infinity would
not be a valid smoothness test. An identically zero discriminant
section gives a generically nonreduced cover and is excluded.

Conversely, a common base zero of `a,b,c` forces `Delta` to vanish
to order at least two there. Thus a nonzero binary-quartic
discriminant already implies basepoint freeness. The entire smooth
`(2,2)` open is consequently described by this one nonvanishing
condition. The discriminant has degree six in the quartic
coefficients and degree twelve in the original nine coefficients.

The companion note's raw-coefficient formulas

    I=12d4d0-3d3d1+d2^2,
    J=72d4d2d0+9d3d2d1-27d4d1^2-27d3^2d0-2d2^3,
    Disc=(4I^3-J^2)/27

use the correct binary-quartic normalization for
`d0Y^4+d1XY^3+d2X^2Y^2+d3X^3Y+d4X^4`. They do not require
`d4!=0`. In particular a simple root at infinity is retained.

## 6. The universal model algorithm matches the geometric construction

The new generator was inspected without executing it. Its coefficient
ring uses exact rational sparse polynomials; its normal monomials are
truncated only above total normal degree four. The inverse of
`z^4+u+(3/2)zv` is expanded through the fourth power of its linear
correction, which is sufficient for all retained terms. The accepted
chart substitutions for `w,u',v'` are implemented literally.

For coefficient `a_j,b_j,c_j`, the reversed second-chart base factor
is `w^(2-j)`. The generator uses this factor and normalizes by `z^16`.
Its first discrepancy is exactly

    S3=[z^16 f1]_3-(h+beta)f.

The sixteen middle coefficients give the first incidence. Its
nonnegative part is `G0`. A negative term `p z^k u^i v^j`, with
`k<=-5`, gives the second-chart correction
`-p w^(-k-5)u'^i v'^j`. Since `i+j=3`, its normalized leading pullback
is precisely `-p z^k u^i v^j`. Thus the generator's first-patch split
has the correct sign and exponent. The finite support is from `-6`
through `1`, so the two local cubic corrections have base degree at
most one, as claimed.

The quartic representative is then

    pr_-11..-1([z^16(f1+G1)]_4-(h+beta)G0),

which retains nonlinear base motion, the first equation unit, and
its product with the first correction. Unknown second units and
quartic local coboundaries are exactly the terms removed by the dual
quotient. The code forms the signed complementary minors of `T_f`
and pairs their columns after shifts `0,...,4` using coefficient
index `-1-shift-z`. This is the required residue and accounts for
all twenty-five tests.

The resulting discrepancy is linear in the coefficients of `f` and
has degree at most two in `h`. Its pairing with the cubic Plucker
vectors therefore has coefficient degree four in `f`, degree at
most two in `h`, and total degree at most six. The first equations
are linear in `f` and affine linear in `h` (equivalently a bilinear
term minus a linear term). Finally the generator appends
`smoothInverse*Disc-1`, which represents precisely the homogeneous
smooth open. No coefficient chart is omitted. This verifies the
algorithmic model underlying the proposed single global elimination;
it does not evaluate that elimination.

## 7. Scope

The twenty-five equations are a globally valid replacement of the
second quotient-membership test, not a proof of emptiness. The
accepted formal nonexistence theorem supplies an existential finite
empty stage; it does not imply that this second stage is empty.
Any effective elimination must still retain the homogeneous smooth
open and the actual first cubic patches and equation units.

No commit or memory update was made.
