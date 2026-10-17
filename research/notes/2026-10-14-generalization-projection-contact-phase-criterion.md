# Projective contact divisors detect residual conductor torsion

Date: 2026-10-14. Owner: `projection_conductor_ray`. Status: **NEW
STRUCTURAL REDUCTION; independent review passed** in the
[written review](2026-10-14-generalization-projection-contact-phase-independent-review.md).
This uses the
accepted [Cartier-lift classification](2026-10-14-generalization-cartier-lift-independent-audit.md),
[full conductor theorem](2026-10-13-generalization-conductor-theorem.md),
and [transverse differential theorem](2026-10-14-generalization-transverse-socle-independent-audit.md)
as premises. None of their certificates is rerun. The result below
reduces residual function-field torsion to projective intersection
data and finitely many leading coefficients. It does not eliminate
the nilpotent conductor defect or bound root-of-unity orders.

## 1. Exact contact criterion

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

## 2. All residual information is read at contact points

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

## 3. Every contact lies at transverse degeneracy

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

## 4. A literal sixteen-parameter quadric correspondence

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

## 5. Exact integration with full conductor descent

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

## 6. Evidence and next target

No large CAS job or accepted-certificate replay was launched for
this note. The displayed universal lift is a direct expression of
the accepted restriction sequence. The new assertions are the
contact-divisor torsion criterion, the single-field refinement,
the leading-coefficient formula, localization of contacts at `A`,
and the explicit arbitrary-quintic first-jet quotient. The independent
review checked all of these assertions and requested the explicit
ambient hypotheses adopted in Sections 3 and 5. It separately
reconstructed the reciprocal-chart normal transition and every
coefficient in the first-jet inverse.

The next genuinely global target is to determine whether an
admissible parameter choice in (8) can satisfy **all** contact
equalities while also having vanishing entire nilpotent defect.
One should organize that question by the degree-one-through-five
degeneracy strata and by the actual off-diagonal correspondence,
not by the possible powers of `Q`. The other two normalized models
admit the same contact criterion and retain their explicit
degeneracy bounds. The universal projective-curve STCI problem and
unrestricted fixed-C0 problem remain unresolved.

## 7. A uniform mate bound in the single-field sublane

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

## 8. A deliberately preserved failed global phase construction

The [opposite-ruling normal form](2026-10-14-quadric-opposite-ruling-phase-normal-form.md)
gives the entire coefficient family for the specified pairing
`(x,0)<->(0,a x)` through one diagonal point. It retains arbitrary
four-vectors `D,E`; its branchwise phase is `a^(-2)`. This is a
new exact incidence subfamily and imposes no phase-order bound.

The especially sparse coefficient choice `D=W2,E=u W2` yields a
basepointfree finite projection, but the [full-support failure
shield](2026-10-14-quadric-opposite-ruling-phase-family-failure.md)
shows that it always has an extra off-diagonal inverse point above
the infinite endpoint of literal C0. The two boundary obstructions
would require simultaneously `u=0` and `u=1` to disappear.
Consequently it supplies no admissible fixed-C0 carrier. This
failure does not exclude the full `D,E` normal form: linearly
independent projected coefficient pairs can remove that particular
boundary obstruction. The entire full-support and nilpotent
descent problem remains for that broader family.
