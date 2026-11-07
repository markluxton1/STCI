# Projection contact, conductor budgets, and actual phase tests

Fix characteristic zero. A primitive upstairs Cartier ray is not a mate until
its powers descend through the **entire** conductor. This chapter owns the
projective contact test, its canonical weighted bounds, actual projection
coordinates, and controls showing why scalar phases remain a separate problem.
The [full family theorem](PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#actual-families-and-their-finite-phase-image)
owns specialization, logarithmic equations, and the finite phase cover; its
proof retains every admissibility and nilpotent condition. The
[universal unit-descent algebra](CONDUCTOR_DESCENT_ALGEBRA.md) owns the full
Artinian logarithm/Kummer proof. These links are theorem dependencies, not an
assertion that either phase image has been computed for the fixed quartic.

**Review.** The scoped contact, budget and split-control arguments have
inherited independent source review. The later audited family theorem replaces
the preliminary finite-phase construction, including its specialization repair.
Independent replacement review accepted the corrected proof preservation,
controls, constants, and scope. No material finding remains.

<a id="2026-10-14-generalization-projection-ray-and-split-phase-model"></a>

## Actual projection spaces and the one-ray membership problem

### 1. The finite-dimensional projection spaces

The [Cartier-lift theorem](FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md)
leaves three fixed-C0 models after accepted quartic exclusion:

    smooth quadric, H=(2,2), c=(1,1);
    quadric cone, H=2c, c smooth Cartier conic;
    plane, H=4h, c a line.

All have a primitive normalized section `Q in H0(S,H)` with divisor
`2c` or `4c`, respectively. The normal mate ray is precisely `Q^b`.
This is already a reduction of all mate degrees to one distinguished
section, but descent of its powers remains a global problem.

Fix the isomorphism of `c` with the literal C0 parametrization, and
write `W=span(s^4,s^3t,st^3,t^4)` in `H0(c,O(4))`. For a smooth
quadric, restriction

    H0(S,O(2,2)) -> H0(c,O(4))

is surjective and has kernel `H0(O(1,1))`, of dimension four. For
the plane with `H=4h`, its kernel is `ell H0(O(3))`, of dimension
ten, where `ell=0` is `c`. The same cone dimension is four, obtained
from its Cartier sequence. Once a splitting of restriction is fixed,
every four-coordinate subspace mapping isomorphically to `W` is the
graph of a linear map from `W` to this kernel. Thus the parameter
spaces before quotienting surface symmetries have affine dimensions
16 for either degree-eight model and 40 for the degree-sixteen model.

Four sections must have no base point. Since `H` is ample, their
resulting morphism is automatically finite: a positive-dimensional
fiber would have zero `H` degree. Birationality onto the image is an
additional condition. On that locus the model is the actual finite
normalization, and the image degrees are eight or sixteen.

The full support condition is exact and finite-dimensional: pull back
the actual generators of `I_C0` through the four sections and require
the radical of their sheaf ideal on `S` to be `I_c`. This retains every
extra isolated inverse point and every extra prime. It is not implied
by the fixed restriction to `c`.

### 2. Exact section-ring condition and what it does not bound

Let

    B=direct_sum_(b>=0) H0(S,bH),
    R=k[U0,U1,U2,U3] subset B,

where the four actual projection sections generate `R`. The carrier
is a hypersurface in P3, so its ambient degree-`b` forms supply all
sections of `O_X(b)`, by `H1(P3,O(b-a))=0`. Consequently

    a mate of degree b exists iff Q^b belongs to R_b.        (1)

When the projection is finite birational, `B` is a finite graded
module over `R` (it is the section module of the finite coherent
normalization algebra), and `Q` lies in the common fraction field.
The intermediate algebra `R[Q]` is finite birational. Thus (1) is an
actual power-membership condition in one finite ambient module,
equivalently the full conductor descent of one primitive ray.

The conductor theorem compresses single-field residual algebras.
Split residual products instead retain scalar root-of-unity phases.
Finite-dimensional parameter spaces or a finite normalization module
do not by themselves bound the orders of those phases. The exact
example below preserves full support and a smooth degree-one lift,
so these hypotheses cannot silently remove the phase problem.

<a id="2026-10-14-generalization-projection-contact-phase-criterion"></a>
<a id="2026-10-14-generalization-projection-contact-phase-independent-review"></a>

## Entire contact divisors and residual phases

### 1. Exact contact criterion

Let `nu:S->X` be a finite birational normalization of an integral
projective surface over an algebraically closed characteristic-zero
field `k`. Assume `X` is Cohen--Macaulay for the global descent
conclusions in Section 5; the residual contact criterion itself does
not require this extra hypothesis. Let `C subset X` be integral, with full reduced inverse
image a single smooth Cartier curve `c` mapped isomorphically to `C`.
Let `H=nu*L`, where `L` is ample on `X`, and assume that an upstairs
section `Q of H` has divisor

    div(Q)=m c,    m>0.                                    (1)

In particular `c` is ample. Let `eta` be a generic conductor point
whose curve is different from `C`. Write the actual reduced
normalization conductor algebra there as

    E=product_i E_i,    K=k(eta),

where each `E_i/K` is finite and separable. `Q` is a unit in the
entire conductor algebra at `eta`, because its zero divisor is
supported only on `c`.

For every component of the reduced geometric-pair correspondence
above `eta` whose two geometric entries differ, take its projective
closure in `S x_X S` and its normalization `T`. The projections
`p_1,p_2:T->S` are finite onto curves. There is a canonical
identification

    p_1*H=p_2*H,

because `nu p_1=nu p_2`. Thus the ratio

    rho_T=p_1*Q/p_2*Q

is a nonzero rational function on the proper integral normal curve
`T`, with exact divisor

    div(rho_T)=m(p_1*c-p_2*c).                             (2)

**Theorem.** The residual class of `Q` in `E*/K*` is torsion if and
only if, on all these finitely many correspondences:

    p_1*c=p_2*c as entire effective divisors;               (3)
    the resulting constant rho_T belongs to mu_infinity(k). (4)

Diagonal pair components have ratio one and require no test. An
off-C unibranch conductor with residual field `E=K` therefore has no
residual obstruction; its full nilpotent obstruction can still be
nonzero. Components dominating `C` are deliberately excluded from
this unit criterion. The accepted conductor theorem handles their
vanishing by a sufficiently large positive power. Consequently this
part of the theorem allows the carrier to be generically singular
along `C`; generic regularity is needed only in Section 3 below.

Proof. The divisor formula follows from (1) and the canonical
line-bundle identification. A rational function on a proper normal
integral curve over `k` has zero divisor exactly when it is a
nonzero constant: it and its inverse are then regular, and proper
integrality gives `H0(T,O_T)=k`. This proves the equivalence between
constant ratios and (3).

Choose a rational frame of `L` at `eta`, and write the residues of
`Q` as `alpha=(alpha_i) in E*`. A power `alpha^N` belongs to the
diagonal `K*` if and only if all its geometric values agree. In
characteristic zero, base change to a separable algebraic closure
of `K` identifies these values with the factors of `E tensor_K
Kbar`; the equality test consists exactly of the geometric-pair
ratios above. Hence residual torsion implies every `rho_T^N=1`.
Conversely, if all ratios are roots of unity, their finitely many
orders have a common multiple `N`. All geometric values of
`alpha^N` agree; faithful scalar descent then puts `alpha^N` in
`K*`. This is the desired residual torsion. No reduced test is used
to claim full conductor descent.

### A sharper single-field consequence

If `E` is one field, condition (3) on every conjugate-pair
correspondence already implies (4). To see this, pass to a finite
Galois closure `K'/K` and a representative `alpha in K'`. Constant
conjugate ratios give

    sigma(alpha)/alpha=chi(sigma) in k*.

Galois automorphisms fix `k`, so `chi` is a homomorphism from a finite
group to `k*`; its values are roots of unity. Thus the single-field
residual test is just equality of contact divisors. For several
fields, the constants comparing different field factors need not
be roots of unity. These relative split phases remain a real
condition and can have unbounded finite orders.

### 2. All residual information is read at contact points

Every `T` above meets `c` under either projection, since its image
is a curve and `c` is ample. Full inverse support implies

    supp(p_1*c)=supp(p_2*c).                               (5)

Indeed `p_1(t) in c` implies `nu p_2(t) in C`, so `p_2(t) in c`;
the reverse implication is identical. As `nu|c` is an isomorphism,
each such pair equals `(P,P)` for one point `P in c`.

Equality of supports (5) does not imply equality of multiplicities
in (3). An unequal contact order is an immediate all-power
exclusion: `rho_T` has a zero or pole, and no positive power can
become a constant. If the orders agree, one contact point suffices
to evaluate the constant ratio.

More precisely, choose a local equation `q` of `c` at `P`, a
uniformizer `z` on `T` at `t`, and write

    q(p_1(z))=beta_1 z^r+...,   q(p_2(z))=beta_2 z^r+...,
    beta_1 beta_2 != 0.

Using the same local frame of `O_S(c)` at the common point `P`,
equation (1) and the canonical `H` frame show

    rho_T(t)=(beta_1/beta_2)^m.                            (6)

The unit multiplying `q^m` has the same value at `p_1(t)=p_2(t)=P`
and cancels. Formula (6) is coordinate independent as a ratio. Thus
one computes the correspondence and its contact orders once, then
reads a residual phase from local leading terms; one does not
solve a separate power-membership problem for every mate degree.

For a component joining branch curves `D_i,D_j` with projection
degrees `e_1,e_2`, a useful necessary numerical test from (3) is

    e_1(c.D_i)=e_2(c.D_j).                                (7)

This total-degree equality is weaker than the required pointwise
contact-divisor equality and must not replace it.

### 3. Every contact lies at transverse degeneracy

Now also assume `X subset P3` and that `X` is regular at the generic
point of `C`. The accepted
transverse theorem supplies the generically nonzero map

    alpha:O_c(c)->N_C/P3

and its entire effective common-zero divisor `A`. Every contact
point of an off-C conductor correspondence lies in `supp(A)`.

Here is a local proof of the new assertion. If `alpha(P)!=0`, the
map `S->P3` is immersive at `P`: its tangent on `c` is injective,
and its transverse normal image is nonzero. The fibre of `nu` over
`nu(P)` is a singleton, by full inverse support and the isomorphism
on `c`. Let `R=O_X,nu(P)` and let `B` be the finite local
normalization algebra above it. Cotangent surjectivity from the
immersion gives `m_R B=m_B` by Nakayama. Thus `B/m_R B=k`; another
application of Nakayama to the finite `R`-module `B` says that `1`
generates `B`, so `R->B` is surjective. It is also injective, hence
an isomorphism. There is therefore no conductor curve through `P`
upstairs. Any contact with an off-C conductor curve forces
`alpha(P)=0`.

For the three accepted fixed-C0 Cartier-lift models this puts all
residual correspondence contacts at at most five or six points:

| Normalization and polarization | `m` | Maximum `deg(A)` |
|---|---:|---:|
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | 2 | 5 |
| Quadric cone, `H=2c`, `c` a Cartier conic | 2 | 5 |
| `P2`, `H=4h`, `c` a line | 4 | 6 |

These are numbers of possible distinct contact sites, bounded by
the degree of the **entire** degeneracy divisor. They do not bound
the number of correspondence branches, their contact orders, or
the orders of their constant phases. At a cone vertex the lift
curve does not pass through the singularity, because a smooth
Cartier curve forces the surface smooth along it; the proof above
is consequently valid in all three models.

### 4. A literal sixteen-parameter quadric correspondence

On `S=P1_(s:t) x P1_(u:v)`, put

    q=sv-tu,    c=(q=0),    Q=q^2,
    P0=s^2 u^2,
    P1=su(sv+tu)/2,
    P2=tv(sv+tu)/2,
    P3=t^2 v^2.

These restrictions to `c` are the prescribed literal quartic
coordinates `(s^4,s^3t,st^3,t^4)`. Every four-coordinate lift with
these fixed restrictions is uniquely

    U_i=P_i+q L_i,  0<=i<=3,
    L_i=a_i su+b_i sv+c_i tu+d_i tv.                       (8)

The sixteen coefficients are the entire projection family before
quotienting automorphisms. On the basepointfree finite birational
locus the image is an integral degree-eight hypersurface. This
parameterization uses the accepted restriction-sequence reduction;
the symmetric `P_i` make the two projections in the fibre product
particularly explicit.

### The first jets are precisely an arbitrary pair of quintics

The universal family has an explicit linear first-jet quotient. On
the chart `s=u=1`, write `t=x,v=x+n`, so `q=n`, and put

    f_i(x)=L_i|c=a_i+l_i x+d_i x^2,    l_i=b_i+c_i.

Normalize the image coordinates by `U0`. Their transverse derivative
at `n=0` is

    v1=1/2+f1-x f0,
    v2=(3/2)x^2+f2-x^3 f0,
    v3=2x^3+f3-x^4 f0.

Taking the derivatives of the two local normal equations
`X2-X1^3` and `X3-X1^4` gives

    a=f2-3x^2 f1+2x^3 f0,
    b=f3-4x^3 f1+3x^4 f0.

The balanced pair is

    A=a=f2-3x^2 f1+2x^3 f0,
    B=2b-3x a=2f3-3x f2+x^3 f1.                          (8a)

Both have degree at most five. This is an actual balanced normal
frame, including infinity. On the reciprocal source chart take
`x'=1/x` and `n'=1/(x+n)-1/x`; the reciprocal target curve
coordinate is `X2/X3`. Direct differentiation of the analogous
normal equations gives

    A_infinity=-x^(-5) B,    B_infinity=-x^(-5) A.          (8b)

The constant interchange of the frame does not change the common
zero divisor. Thus the homogenizations

    A_h(s,t)=s^5 A(t/s),    B_h(s,t)=s^5 B(t/s)

represent the entire normal map `O(2)->O(7)^2`, and its degeneracy
divisor is exactly the homogeneous gcd divisor of `A_h,B_h`, with
full multiplicity and infinity retained. When they are not both
zero its degree is at most five. When both vanish the projection
is generically nonimmersive along `c` and belongs to the separate
thick-carrier boundary.

The twelve coefficients `(a_i,l_i,d_i)` map **isomorphically** to
the twelve coefficients of the arbitrary pair `(A,B)`. In fact,
if `A=sum A_j x^j` and `B=sum B_j x^j`, the explicit inverse is

    d0=A5/2,         l0=(A4+3B5)/2,   a0=(A3+3B4)/2,
    d1=B5,           l1=B4,           a1=-(B3+3A2)/8,
    d2=-(A2+3B3)/8,  l2=A1,           a2=A0,
    d3=(B2+3A1)/2,   l3=(B1+3A0)/2,   a3=B0/2.             (8c)

Direct coefficient extraction also checks the inverse without a rank heuristic:

    A=(a2,l2,d2-3a1,2a0-3l1,2l0-3d1,2d0),
    B=(2a3,2l3-3a2,2d3-3l2,a1-3d2,l1,d1).

On the reciprocal source chart, n'=-n/x²+O(n²). The two unbalanced target
normal derivatives against the old n are x^-7(2b-3xa), x^-8(3b-4xa).
Multiplying by -x² and balancing gives precisely (8b). Thus the source
normal factor and target-coordinate scale are both retained.

The other four parameters `b_i-c_i` vary the coefficients of
`q^2` in the four `U_i`; they affect second and later jets while
leaving (8a) unchanged. This surjectivity is a statement about the
entire lift vector space. It does not say that every quintic pair
has a basepointfree, birational, full-support admissible projection,
or that a first-jet pair determines its conductor. Equations
(8a)--(8c) make the degree-one-through-five gcd strata and their
four independent higher-jet parameters explicit for further work.

The actual equality-of-image locus in `S x S` is defined by all six
minors

    U_i(P)U_j(P')-U_j(P)U_i(P'),    0<=i<j<=3.             (9)

For the residual test, remove the diagonal locus and take the
projective closure, then normalize each curve component dominating
an off-C conductor curve. Its contact divisors are obtained by
pulling back `q(P)=0` and `q(P')=0`. Under the canonical matching
of `H`, the ratio is

    rho_T=q(P)^2/q(P')^2,                                 (10)

with the equality-of-image scale included through that line-bundle
identification. If homogeneous representatives are used with
`U_i(P')=lambda U_i(P)`, the scalar version of (10) is
`lambda q(P)^2/q(P')^2`; omitting this factor would give the wrong
invariant. In a common target-coordinate frame, the formula is the
ratio of `q^2/U_i` on the two branches. At a contact point, the
scalar factor tends to one in the common source frame, yielding
the square of the contact leading-coefficient ratio in (6).

Taking the closure retains all contact points on the diagonal.
Reducing and normalizing (9) is used only for the residual-field
test; it does **not** compute the full conductor or its nilpotent
logarithmic defect. Full support is separately imposed by the
pullback ideal of literal `C0`, retaining every possible isolated
inverse point. The basepoint, finite-birational, full-support, and
entire conductor conditions remain mandatory throughout (8).

### 5. Exact integration with full conductor descent

For a fixed projection satisfying these hypotheses, with `X`
Cohen--Macaulay as in every hypersurface model here:

1. Compare the finitely many full contact divisors on the actual
   residual correspondences. Any mismatch excludes every mate.
2. Evaluate the resulting constant phases by (6). A non-root-of-
   unity split phase excludes every mate. Single-field components
   require no additional root-of-unity test after all conjugate
   contacts match.
3. If all residual classes are torsion, compute the full Artinian
   conductor logarithmic defects from the accepted conductor
   theorem. Each must vanish. A reduced correspondence cannot
   replace this step.
4. If the defects vanish, the conductor theorem gives eventual
   descent. When `X` is an integral hypersurface in `P3`,
   `L=O_X(1)`, and the carrier is generically regular along `C`, the
   minimum ambient mate degree is the exact residual order of `Q`.
   For the general polarized surface, the statement concerns the
   least descending tensor exponent rather than an ambient degree.

This is a finite geometric criterion on a **chosen** projection,
not an effective algorithm over arbitrary unspecified coefficient
fields, and not a proof that every parameter stratum is covered.
Root-of-unity membership still depends on the coefficient field;
its orders can be unbounded in a family. The accepted affine split
phase example is consistent with (6): arbitrary ratios of branch
slopes give arbitrary finite phases after squaring or taking fourth
powers. The new projective gain is that every residual component
must meet the ample lift and its entire function-field ratio is
controlled by its contact divisor and a leading coefficient at one
of at most five or six degeneracy points. This is a structural
target across all mate degrees, rather than a mate-degree search.

### 7. A uniform mate bound in the single-field sublane

There is a quantitative consequence for all projections in each
fixed model, rather than only one carrier. If `nu:S->X subset P3`
is finite with `nu*O_X(1)=H` and `H^2=a`, then at any point with
residue field `K` its normalization residue degrees obey

    sum_i [E_i:K] <= a.                                  (11)

Indeed, over `K`, choose a line through the corresponding `K`-point
of `X_K` that is not contained in `X_K`. Two target hyperplanes
cutting that line pull back to a proper zero-dimensional
intersection of two `H_K` divisors, of total length `H^2=a`.
The entire scheme fibre is a closed subscheme of that intersection,
so its length is at most `a`; its reduced residue degrees have at
most that sum. The infinite field `K` ensures such a line can be
chosen. This proof does not assume that the finite normalization
is flat.

Suppose now the carrier is generically regular along `C`, every
off-C generic conductor residual algebra consists of a **single**
field, and a mate exists. The accepted characteristic-zero theorem
then makes each exact local descent order divide its field degree.
Vanishing of the full logarithmic defects follows from actual mate
existence. The minimum mate degree is their least common multiple,
so (11) gives the uniform divisibility bounds

    degree-eight models:     b_min divides lcm(1,...,8)=840;
    degree-sixteen model:    b_min divides lcm(1,...,16)=720720. (12)

These are conservative uniform bounds, not assertions that those
large degrees are necessary or that checking them is a practical
computation. In particular, in this sublane it is enough to test
one fixed power `Q^840` or `Q^720720` on the **full** conductor,
rather than arbitrary powers: an existing mate forces that power
to descend, and descent of that power constructs a mate. This
last equivalence retains the nilpotent defect. A single reduced
test still cannot decide it.

The hypothesis that the carrier is generically regular along `C`
removes the separate conductor vanishing threshold on `C`. No
bound in (12) is asserted here for the thick-on-C boundary. No
split-conductor phase is bounded by (11): even two degree-one
residual fields can have an arbitrary-order relative root of
unity. The contact criterion in Sections 1--3 remains the exact
replacement for that false inference.

### 8. A deliberately preserved failed global phase construction

The [opposite-ruling normal form](PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md#the-opposite-ruling-pairing-and-its-complete-coefficient-freedom)
gives the entire coefficient family for the specified pairing
`(x,0)<->(0,a x)` through one diagonal point. It retains arbitrary
four-vectors `D,E`; its branchwise phase is `a^(-2)`. This is a
new exact incidence subfamily and imposes no phase-order bound.

The especially sparse coefficient choice `D=W2,E=u W2` yields a
basepointfree finite projection, but the [full-support failure
shield](CYCLIC_COVER_AND_MOVING_LINEAR_RIGIDITY.md#2026-10-14-quadric-opposite-ruling-phase-family-failure)
shows that it always has an extra off-diagonal inverse point above
the infinite endpoint of literal C0. The two boundary obstructions
would require simultaneously `u=0` and `u=1` to disappear.
Consequently it supplies no admissible fixed-C0 carrier. This
failure does not exclude the full `D,E` normal form: linearly
independent projected coefficient pairs can remove that particular
boundary obstruction. The entire full-support and nilpotent
descent problem remains for that broader family.

<a id="2026-10-14-generalization-projection-conductor-contact-budget"></a>
<a id="2026-10-14-generalization-projection-conductor-budget-independent-review"></a>

## Canonical conductor and ordered contact budgets

### 1. General theorem

Let `nu:S->X subset P3` be a finite birational normalization of an
integral degree-`a` hypersurface over an algebraically closed field of
characteristic zero. Let `C subset X` be a smooth degree-`d`, genus-`g`
curve with full reduced inverse image a
single smooth ample Cartier curve `c`, mapped isomorphically to `C`.
Assume `X` is regular at the generic point of `C`. The Cartier-lift
lemma makes `S` regular along `c`. Put `H=nu*O_X(1)` and `k=c^2`.

Finite duality identifies the **actual** upstairs conductor ideal with
`omega_S tensor nu*omega_X^(-1)`. A normal surface is Cohen--Macaulay,
and its canonical sheaf is rank-one reflexive. Thus the conductor is
the divisorial ideal of an effective Weil divisor `B`:

    conductor O_S = O_S(-B),
    B ~ (a-4)H-K_S,
    N := B.c = d(a-4)+k-(2g-2).                    (1)

This statement identifies the actual ideal, not only its double dual;
there is no discarded zero-dimensional ideal defect. Globally `B`
need not be Cartier. It is Cartier near `c`, because `S` is regular
there, and this is enough to define `B|c` and its degree. Adjunction
near `c` proves the formula for `N`. If `S` is Gorenstein, `B` is
Cartier globally.

Write its effective Weil divisor as `B=sum_i m_i D_i`, with the `D_i`
distinct prime curves and `m_i>=1`. No `D_i` equals `c`, because the
normalization is an isomorphism at the generic point of `C`. Then

    sum_i m_i (D_i.c) = N.                          (2)

Every `D_i.c` is a strictly positive integer since `c` is ample.
Consequently:

* There are at most `N` prime conductor curves, and each generic
  conductor multiplicity `m_i` is at most `N`.
* If `D_i^nor` is the normalization of `D_i`, the sum of the vanishing
  orders of `c` on all its branches is `D_i.c`. Thus every such branch
  contact order, and the number of branches meeting `c`, is at most
  `N`; their sum with weights `m_i` is exactly `N`.
* The exact first-symbol bridge is

      Z(F_1) = B|c + A,                             (3)

  where `A` is the entire zero divisor of the normalization normal
  differential. In particular (2) concerns the full conductor contact,
  including multiplicities, rather than only its reduced support.

Here `F_1` is the actual first normal symbol of the carrier equation.
The local proof below establishes (3). The contact graph bounds (1)--(2)
use finite duality directly and do not depend on that differential identity.

### Proof of the actual conductor and first-symbol identity

For a finite birational extension `A subset B` with common fraction field,
every `A`-linear map `B->A` is multiplication by a fraction. Consequently
`Hom_A(B,A)` is the actual conductor `{q:q B subset A}`, not merely its
reflexive hull or its divisorial support. Since `A` is Gorenstein and `B`
is Cohen--Macaulay, finite canonical duality gives

    omega_B = Hom_A(B,A) tensor_A omega_A.

On a Gorenstein normalization the conductor is invertible globally. On a
normal normalization it is the actual rank-one reflexive canonical ideal;
smoothness near c still makes it invertible there. The local argument below
therefore applies near c without assuming global Gorensteinness.

The new local bridge was independently reconstructed in completed regular
coordinates. Take source coordinates `(t,u)`, with `c=(u=0)`, and ambient
coordinates `(x,y,z)` with `C=(y=z=0)` and `nu*x=t`. Write `nu=(t,Y,Z)`.
If `h` generates the actual conductor and `eta=dx wedge dy/F_z` generates
the hypersurface dualizing module, then `h nu*eta` is a generator of
`omega_S`. Hence there is one common unit `epsilon` satisfying

    F_z composed with nu=epsilon h Y_u,
    F_y composed with nu=-epsilon h Z_u.

At least one of these rational residue expressions is available generically:
the map is birational and is an isomorphism at the generic point of the
hypersurface. The equalities extend in the regular local ring. Restriction
to `u=0` gives the exact DVR-ideal equality

    (F_y|C,F_z|C)=(h|c)(Y_u|c,Z_u|c).

Taking orders proves the entire divisor identity

    Z(F_1)=B|c+A.

This argument uses the actual invertible conductor before restricting to
`c`; it avoids the possible codimension-two error in restricting only a
Weil-divisor or reflexive-hull identity. It also keeps isolated zeros of
the transverse differential. Smoothness along `c` follows from the accepted
smooth Cartier-curve lemma. The quadric cone is Gorenstein and its smooth
Cartier conic avoids the vertex, so that model satisfies the hypotheses.

### 2. A bound on the entire off-diagonal pair correspondence

For every image conductor curve `Delta subset X`, let

    K=k(Delta),    E=product_(i over Delta) E_i,
    E_i=k(D_i),   d_Delta=sum_i [E_i:K].

The accepted fiber-degree argument gives `d_Delta<=a`. Characteristic
zero makes each extension separable. Fix a prime `D_i` over `Delta`.
The reduced generic algebra of all pairs with first entry on `D_i` is

    E_i tensor_K E,

of rank `d_Delta` over `E_i`. Its diagonal component is one factor
`E_i`, of rank one. Removing it leaves total rank `d_Delta-1`.
Normalizing and taking projective closures therefore gives finitely
many integral off-diagonal pair curves `T`, with finite first projection
`p_1:T->D_i`, satisfying the exact equality

    sum_(T with first image D_i) deg(p_1) = d_Delta-1 <= a-1. (4)

This includes conjugate pairs on one irreducible conductor curve as
well as pairs between different conductor curves. When `E=K` there
are no off-diagonal curves, consistent with (4). Generic nilpotents
are deliberately absent from this pair construction, but are retained
in the conductor divisor `B` and in the final full descent condition.

Pullback of the Cartier divisor `c` to each proper normal curve `T`
has total degree `deg(p_1)(D_i.c)`. Summing (4) over all first images
and then using (2) gives the uniform bound

    sum_T deg(p_1*c)
      = sum_i (d_(image D_i)-1)(D_i.c)
      <= (a-1) sum_i D_i.c
      <= (a-1)N.                                    (5)

The index `T` in (5) means the integral components of the **ordered**
off-diagonal pair correspondence. In particular a component invariant
under exchange is counted once as an integral component, rather than
being artificially doubled. The equality is the decomposition of
the finite algebra over each fixed first image, so there is no missing
conjugate-pair degree or extra factor of two.

Because `c` is ample, every `p_1*c` is a nonzero effective divisor.
Hence (5) bounds all of the following by `(a-1)N`: the number of pair
components, the number of their contact branches counted with
multiplicity, and any single contact order on their normalizations.
These quantities were not bounded by the size of the degeneracy
support alone.

### 3. The three surviving fixed-C0 models

The accepted normal splitting `N_C0/P3=O(7)^2` and transverse theorem
place every conductor contact in the support of `A`, whose degree
is at most five or six. Equations (1)--(5) supply the additional
global weighted bounds:

| Normalization and polarization | `B` class | `N=B.c` | `deg A` bound | Ordered pair contact budget |
| --- | --- | ---: | ---: | ---: |
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | `(10,10)` | 20 | 5 | 140 |
| Quadric cone, `H=2c`, `c` a smooth conic | `10c` | 20 | 5 | 140 |
| `P2`, `H=4h`, `c=h` | `51h` | 51 | 6 | 765 |

The quadric cone is Gorenstein, and `c` avoids its vertex. Thus its
global conductor class is Cartier and its local contact calculation
occurs entirely in the smooth locus. No resolution at the vertex is
being silently inserted.

These inequalities put the incidence into finitely many **combinatorial
weighted contact graph types**. Vertices can record the at most five or
six sites on `c`, the prime conductor branches and their positive
integer weights. Edges record ordered pair branches and their positive
contact orders, with total edge weight bounded by 140 or 765. The
actual curves, contact locations, correspondence maps and leading
coefficients still vary in families. Finitely many graph types do not
mean finitely many projection parameters or finitely many phase values.

### 4. Consequence for the general strategy and retained boundaries

The accepted projective criterion requires, on every pair curve `T`,
equality of the entire divisors `p_1*c` and `p_2*c`, followed by a
root-of-unity test on the resulting constant ratio. The new theorem
bounds the amount of integer contact data needed to formulate these
tests uniformly on each normalization model. It does not require
enumerating possible mate powers.

There is still no bound here on the order of a split scalar phase.
Even one edge with contact order one can carry an arbitrary-order
root of unity in the local split model. Canonical conductor duality
constrains that edge's integer contact data, not its scalar label.
The entire nilpotent logarithmic conductor defect must also vanish;
the reduced correspondence and (1)--(5) do not prove this vanishing.

The theorem applies more generally to any smooth ample Cartier lift
on a normal projective-hypersurface normalization, with the uniform
quantity `N` in (1). Global Gorensteinness is unnecessary: the actual
reflexive conductor ideal and smoothness along `c` suffice. For
non-Cartier lifts the contact divisor needs replacement; for a lift
through singular points of the normalization the local bridge needs
replacement; and for carriers generically
singular along `C`, the conductor can contain `c`, so its restriction
in (2) is not defined as an effective finite divisor. Those strata
are not covered by this theorem. It does not resolve the universal
integral-curve STCI problem or the unrestricted fixed-C0 problem.



## Split-phase controls and a five-coordinate construction interface

### 3. An entire split-conductor affine example with unbounded phase order

Choose nonzero distinct `alpha,beta` in an algebraically closed
characteristic-zero field. Set `lambda=alpha+beta`, `mu=alpha beta`,

    B=k[u,v],
    y=v^2-lambda u v,
    h=y+mu u^2=(v-alpha u)(v-beta u),
    z=v h,
    A=k[u,y,z] subset B.

Put `R0=k[u,y]`. The equation `v^2-lambda u v-y=0` makes `B`
finite free of rank two over `R0`, and

    B=R0 direct_sum R0 v,
    A=R0 direct_sum h R0 v.

The latter is closed under multiplication because
`(hv)^2=yh^2+lambda u h(hv)`. Away from `h=0`, `v=z/h`, so the
extension `A subset B` is finite birational; normal `B` is its
normalization. The actual integral affine carrier is the hypersurface

    z^2-lambda u h z-y h^2=0,    h=y+mu u^2.                 (2)

Its conductor is exactly `hB`. To see this, an element `a+bv` belongs
to `A` exactly when `b in hR0`; requiring its product with `v` to
belong to `A` then forces `a+b lambda u in hR0`, hence `a in hR0`.
Thus the entire conductor square is

    A/hB=k[u],
    B/hB=k[u,v]/((v-alpha u)(v-beta u)),

with downstairs ideal `(h,z)` and upstairs divisor the two actual
lines `v=alpha u` and `v=beta u`. The upstairs curve is reducible,
with the two lines meeting at `(0,0)`; no nilpotent or intersection
data is dropped. Their maps to the downstairs line agree in the
coordinate `u`.

Let `C` downstairs be `y=z=0`. Its full reduced inverse image is
exactly the smooth line `c:v=0`, mapped isomorphically by `u`.
Indeed if `v!=0`, the first equation forces `v=lambda u`, and the
second then forces `mu u^2=0`, contradicting `mu!=0` and `v!=0`.
At `u=0` the only inverse point is still `v=0`; no isolated extra
normalization point appears.

For any fixed positive integer `q`, put `Q=v^q`. Modulo the entire
conductor its two restrictions are

    alpha^q u^q,   beta^q u^q.

Therefore the exact full-ring criterion is

    Q^n in A iff alpha^(q n)=beta^(q n).                      (3)

For sufficiency, if the two constants agree, the conductor residue
is the diagonal polynomial `alpha^(qn)u^(qn)` in `k[u]`; subtracting
it leaves an element of `hB subset A`. Necessity is immediate from
the two generic restrictions. Thus (3) includes the intersection
point and the entire conductor, not just a generic unit test.

Choose `alpha/beta` to be a root of unity of order `N`, with
`gcd(N,q)=1`. Then the smallest descending positive power is exactly
`n=N`, which is unbounded while the formulas (2) have fixed degrees
and the smooth singleton lift is unchanged. The primitive-like
orders `q=2` or four therefore do not bound split phases locally.

This is an affine example with a line support. It is **not** a
projective fixed-C0 carrier or a counterexample to any accepted
projective theorem. It proves that a proposed global argument must
use global projectivity, polarization or the actual fixed-C0
projection geometry in addition to these local support conditions.

### 4. Five-coordinate viewpoint: a concrete global lead

Adjoin `Q` to the four projection sections. Since the original four
generate `H`, the five also do, and their map has a finite image

    Y subset P4,  coordinates [U0:U1:U2:U3:Q].

Projection from the fifth-coordinate point is finite birational
`Y->X`. The hyperplane `Q=0` has scheme pullback `2c` or `4c`, and
the reduced curve there is the prescribed fixed C0.

For any scalar `zeta`, let `T_zeta` scale just the fifth coordinate.
At a split conductor identification where the `U_i` agree and the
two `Q` values have ratio `zeta`, the corresponding branch curves
are contained in `Y intersect T_zeta(Y)`. A mate requires these
phase ratios to be constant roots of unity and requires full
Artinian conductor membership as well.

This is a geometric reformulation, **not a proved exclusion**.
The shared hyperplane curve occurs for every `zeta`, so a naive
intersection-degree count must first separate that forced common
component from the additional branch curve. The local example above
shows why neither low coordinate degree nor isolated ramification
alone makes all `zeta` have bounded order. A useful new theorem
would have to couple the extra common curves to the actual
hyperplane multiplicity, global canonical/conductor divisor, or
prescribed C0 parametrization.

The separately written [transverse differential/socle theorem](NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-transverse-differential-socle-bound)
already supplies one global coupling: on a generically regular
carrier, every surviving projection requires a nonzero common-zero
divisor of the transverse differential, with bounded degree five
or six and a quantitative conductor-contact budget. Classifying
those root strata while preserving the split phase model is the
next structural target. No mate-power search has been started.

<a id="2026-10-14-generalization-projection-finite-phase-space"></a>

## Finite phase covers and their remaining arithmetic

For a finite-type family of actual admissible projections, the corrected
[family theorem](PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#actual-families-and-their-finite-phase-image)
constructs a finite surjective phase cover Z->T0 and a map Z->G_m^D.
T0 imposes full nilpotent logarithmic equations and constancy of all geometric
pair ratios. Ordered roots of the characteristic polynomial of multiplication
by rho in E tensor_K E give the phase coordinates, including conjugate and
split comparisons; repeated roots are permitted. Eventual descent holds exactly
when the resulting tuple is torsion. The corrected proof uses monic finiteness
of the entire conductor quotient before rational localization, so specialized
conductor curves are not lost. Common ideals need not be the largest conductor.

The finite-algebra criterion is u=v exp(w), with u^n in A exactly when
w is in nil(A) and rho^n=1. Characteristic zero is essential to remove the
factor n from the logarithmic membership test. The theorem's full algebraic
proof is owned by [unit descent](CONDUCTOR_DESCENT_ALGEBRA.md); the family
construction and its specialization proof are owned by the linked family
theorem. No finite normalization module alone bounds split phase orders.

The mate locus
need not itself be constructible: even the finite algebra family
`A=F` diagonally in `B=F times F`, `u=(1,t)`, over `t in G_m`, has eventual
descent exactly for `t in mu_infinity(k)`. In characteristic zero this is
infinite and has infinite complement, whereas constructible subsets of
`G_m` are finite or cofinite.

There is a useful exact one-phase dichotomy. Suppose, after a finite
refinement, the phase image lies in a fixed torsion translate of a
one-dimensional subtorus, parameterized as

    z_i=xi_i lambda^(m_i), xi_i fixed roots of unity,
    m_i integers, gcd(m_1,...,m_d)=1.                      (11)

The admissible `lambda` image is constructible in `G_m`. If it is finite,
only finitely many phase tuples can occur. If it is infinite, it is
cofinite. It consequently contains roots of unity of arbitrarily large
orders; every such value is realized by an admissible parameter and gives
a mate. Phase orders are unbounded: if `M` kills all `xi_i` and the phase
tuple has order `e`, Bezout on the `m_i` gives `lambda^(M e)=1`, hence
`e >= order(lambda)/M`.

The hypothesis (11) must be proved for the actual phase image. It cannot
be replaced by positive dimension. The curve

    {(lambda,2 lambda): lambda in G_m} subset G_m^2

is positive dimensional and contains no torsion point in characteristic
zero. Thus a multiphase image retains a substantive torsion-intersection
problem even after every contact and logarithmic condition has been made
algebraic.

For the fixed-C0 projective families this yields a concrete structural
target: construct the finite phase image after imposing the entire
nilpotent equations, and determine its torus relations. A surviving
one-phase torsion translate with infinite image would prove existence,
whereas a phase image with no torsion point would exclude the full family
at every mate degree. Neither alternative has yet been established.

## Characteristic boundary

The equalizer, entire contact-divisor formula and finite-module geometry need
no characteristic-zero logarithm; residual-field arguments require separable
extensions. Characteristic zero supplies separability here, the derivative
constancy test, finite logarithms with invertible integer coefficients, and the
single-field Kummer order theorem. Frobenius can kill a nilpotent obstruction in
positive characteristic, so the exponent-free logarithmic criterion is not
imported there. The first-jet formulas use 2 invertible; the three normalization
models and low-degree pruning are inherited characteristic-zero hypotheses.
For the fixed quartic, the [every-positive-characteristic quartic-carrier
construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
remains the separate existence control. No uniform positive-characteristic
extension of these phase bounds is asserted.
