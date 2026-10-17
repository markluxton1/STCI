# Independent review of the projective contact and phase criterion

Date: 2026-10-14. Reviewer: `quadric_phase_review`. Scope: the new arguments in
[the projection contact and phase note](2026-10-14-generalization-projection-contact-phase-criterion.md).
Previously accepted Cartier-lift, conductor, and transverse differential results
are premises; none of their certificates was replayed.

Status: **PASS for the new residual criterion and its stated refinements**, with
the ambient `P3` hypotheses made explicit wherever an ambient normal bundle or
mate degree is used. This is a fixed-carrier reduction, not an exclusion of all
projection parameters or a bound on split-phase orders.

## 1. Proper pair curves and the divisor calculation

For an off-`C` generic conductor point, the distinct geometric pairs in the
reduced algebra are represented by the components of the reduced fiber product
`S x_X S` that dominate the corresponding conductor curve. Their projective
closures are proper; normalizing each integral curve component produces a
proper integral normal curve `T`. Each projection to `S` is finite because the
normalization map `S->X` is finite and both projections of the fiber product
are finite. The common composite to `X` canonically identifies `p1*H` and
`p2*H`.

Consequently the nonzero section ratio is a rational function, and

    div(rho_T)=m(p1*c-p2*c).

The entire contact divisors must agree, not just their degrees or supports. On
a proper integral normal curve over an algebraically closed field, a rational
function with zero divisor and its inverse are regular; hence it is a constant
in `k*`. This establishes the equivalence between contact-divisor equality and
constancy without a degree-of-mate search.

In characteristic zero, the finite residual fields are separable. After a
separable scalar extension the equality of all geometric values of a tuple
`alpha in product E_i*` is exactly the condition that it belong to the diagonal
`K*`. Thus all pair ratios being roots of unity is equivalent to some positive
power of the tuple being diagonal: take a common multiple of the finitely many
orders and descend the equality of geometric values. This checks both
directions of the residual torsion criterion.

Components lying over `C` are excluded from this unit test. Their images of
`Q` in the generic normalization conductor quotient are nilpotent, since
`div(Q)=m c`, and all sufficiently large powers vanish there. For the subsequent
global descent assertion, require `X` Cohen--Macaulay, as in the accepted
conductor theorem; this is automatic for the integral hypersurface models.
The accepted absence of closed-point associated primes in the normalization
quotient then allows generic conductor membership to give global membership.
This does not remove any off-`C` nilpotent obstruction. The residual contact
criterion itself does not require the Cohen--Macaulay hypothesis.

## 2. Single-field refinement and leading coefficients

For one residual field, pass to its finite Galois normal closure `K'/K`.
Constancy of every conjugate-pair ratio gives

    sigma(alpha)/alpha=chi(sigma) in k*.

Every Galois automorphism fixes `k`. Therefore `chi` is a character of the
finite Galois group; its values are roots of unity. The single-field residual
torsion condition is thus precisely equality of all conjugate contact
divisors. The accepted Kummer theorem subsequently gives the sharper order
dividing the actual residue-field degree. Constants comparing different
field factors have no such automatic finite-group constraint.

The ample divisor `c` meets each projected pair curve. Full inverse support
and injectivity of `c->C` imply that contact pairs are `(P,P)` and that the two
effective contact divisors have identical support. Their multiplicities can
still differ. If a local equation of `c` pulls back as

    beta1 z^r+...,  beta2 z^r+...,

then, in the common target frame, the unit in the local expression of `Q`
has the same value at the two projections and cancels. The phase is exactly

    (beta1/beta2)^m.

This formula is invariant under changing the local curve equation, pair-curve
uniformizer, or source frame. It supplies no order bound for a split phase.

## 3. Localization at the transverse zero divisor

Here the surface must be embedded in `P3`, the curve must be smooth there,
and the carrier must be generically regular along `C`, as in the accepted
transverse theorem. If the normal differential is nonzero at `P`, its normal
image is independent of the tangent to `c`; the map to `P3` is immersive at
`P`.

The local normalization algebra above `nu(P)` is finite and local because the
fiber is a singleton. Surjectivity on cotangent spaces gives

    m_R B=m_B

by Nakayama on the finitely generated `B`-module `m_B/m_R B`. Hence
`B/m_R B=k`. A second use of Nakayama, now on the finite `R`-module `B`, says
that `1` generates it. The injective birational map `R->B` is consequently
surjective and an isomorphism. No conductor curve can meet `P`. Every contact
therefore belongs to the support of the entire transverse degeneracy divisor
`A`.

The resulting bounds of five or six distinct sites in the three accepted
Cartier-lift models bound contact sites only. They bound neither numbers of
pair components nor contact multiplicities nor orders of scalar phases.

## 4. The literal quadric family and ambient degrees

The displayed sections `P_i` restrict to the literal four quartic monomials.
The accepted restriction sequence identifies its kernel with `q H0(O(1,1))`,
so `U_i=P_i+q L_i` is the whole sixteen-parameter family, with unique `L_i`.
The six equality-of-image minors define the actual pair locus before taking
off-diagonal closures.

The invariant phase in homogeneous representatives requires the scale factor:
if `U_i(P')=lambda U_i(P)`, then

    rho_T=lambda q(P)^2/q(P')^2.

Indeed a common target-coordinate frame gives
`(q(P)^2/U_i(P))/(q(P')^2/U_i(P'))`. Omitting `lambda` would make the formula
depend on the homogeneous representatives. At a contact pair `(P,P)`,
compatible local source frames make its limiting value one, agreeing with the
leading-coefficient formula.

For a general polarized surface the result gives descending exponents. To
identify the smallest descending exponent with the smallest ambient mate
degree, require an integral hypersurface `X subset P3`, `L=O_X(1)`, the
degree-one normalized section `Q`, generic regularity along `C`, and vanishing
of all off-`C` logarithmic conductor defects. Under these hypotheses the
accepted conductor result identifies the exponent with the common exact
residual order. Ambient forms represent all sections of `O_X(b)`, so this is
the mate degree. These scope restrictions are necessary.

## 5. The exact first-normal-jet map

The new first-jet formulas in the owner note were checked directly, without
calling an inherited certificate. On the chart `s=u=1,t=x,v=x+n`, write
`f_i=L_i|c=a_i+l_i x+d_i x^2`, with `l_i=b_i+c_i`. Normal differentiation in
the target affine chart gives

    a=f2-3x^2 f1+2x^3 f0,
    b=f3-4x^3 f1+3x^4 f0.

Balancing by `A=a`, `B=2b-3x a` cancels the potential degree-six term:

    B=2f3-3x f2+x^3 f1.

In the reciprocal source chart, the normal parameter is
`n'=1/(x+n)-1/x=-n/x^2+O(n^2)`. With target base parameter `Y=X2/X3`,
the corresponding two unbalanced target conormal derivatives, measured
against the old `n`, are

    x^-7(2b-3x a),    x^-8(3b-4x a).

Changing to differentiation against `n'` multiplies both by `-x^2`.
The same balancing in the reciprocal chart gives exactly

    (A_infinity,B_infinity)=-x^-5(B,A).

Thus the two quintics represent the map `O(2)->O(7)^2`, after a fixed
swap of the balanced frame on the reciprocal chart. Both the normal-source
factor and target-coordinate scale are included in this calculation.

For coefficients numbered from zero through five, direct extraction gives

    A=(a2,l2,d2-3a1,2a0-3l1,2l0-3d1,2d0),
    B=(2a3,2l3-3a2,2d3-3l2,a1-3d2,l1,d1).

These equations invert as

    d0=A5/2, l0=(A4+3B5)/2, a0=(A3+3B4)/2,
    d1=B5, l1=B4, a1=-(B3+3A2)/8,
    d2=-(A2+3B3)/8, l2=A1, a2=A0,
    d3=(B2+3A1)/2, l3=(B1+3A0)/2, a3=B0/2.

The twelve-dimensional first-jet map is therefore an isomorphism in
characteristic zero. Its four-dimensional invisible kernel in the sixteen
projection parameters is precisely the four `q^2` variations supplied by
`b_i-c_i`. The homogeneous greatest common divisor of `A,B` supplies the
entire first differential zero divisor, including its point at infinity.
If both quintics vanish identically, the map is not generically transverse;
the zero-pair case must remain separate from a finite-degree gcd stratum.

## 6. Uniform residual-field bound for the fixed normalized models

The additional single-field corollary was independently checked. Suppose a
finite map from the fixed polarized surface to `P3` is birational onto its
integral image, of degree `a=H^2`. At any generic conductor point `eta`, put
`K=k(eta)` and regard that point as a `K`-point of `X_K`. Since `K` is infinite,
one may choose a `K`-line through it that is not contained in `X_K`. Its two
defining hyperplanes pull back to divisors of `H_K` meeting properly in a
zero-dimensional scheme of total length `H^2=a`. The entire scheme fiber above
the chosen point is a closed subscheme of this intersection. Therefore

    sum_i [E_i:K] <= length(fiber) <= a.

This includes possible nonreduced fibers; it bounds the reduced residual
degrees by the entire fiber length and does not identify the two.

For the quadric targets `a=8`, and for the plane target `a=16`. If every
off-`C` residual algebra is a single field, the carrier is generically regular
along `C`, and all full logarithmic defects vanish, the exact minimum
descending exponent is the least common multiple of local residual orders.
Each such order divides an actual residue-field degree at most `a` by the
accepted single-field theorem. Consequently

    b_min divides lcm(1,...,8)=840       (quadric models),
    b_min divides lcm(1,...,16)=720720   (plane model).

This is a conditional uniform bound across those single-field projections,
not an existence assertion. Split residual products are expressly excluded
from this numerical corollary: their relative scalar phases are not bounded
by the reduced fiber degree.

## 7. What remains

The reduced pair correspondence detects residual torsion only. The full
Artinian conductor logarithmic defects, basepoint-free and birational
conditions, and full inverse support—including isolated extra inverse
points—remain mandatory. This review does not replace them by contact
equalities. It confirms a structural criterion across all powers of one
chosen primitive ray; it does not resolve the unrestricted fixed-`C0` or
universal projective-curve STCI questions.
