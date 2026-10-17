# Independent written review of the symbolic-ribbon generalization

Date: 2026-10-14. Reviewer: `global_structure`, distinct from the author
`ribbon_general`. Status: **NEW CONDITIONAL THEOREM REVIEWED; root
acceptance remains separate**. This is mathematical review of a new
written proof. No accepted repository statement or verifier was rerun.

The reviewed source is
[the symbolic-ribbon criterion](2026-10-13-generalization-ribbon-numerical-criterion.md).
I independently reconstructed its sheaf arguments, multiplication maps,
Euler identity and all displayed numerical specializations. The theorem
is sound under its stated normality, smooth curve, actual Cartier
relation, finite normalized-carrier map and degree-one-lift hypotheses.
Its conormal inequality additionally requires the stated generically
nonzero first-layer map; the valuation version instead measures its
first surviving layer.

## 1. What makes the symbolic double an entire ribbon

On a normal surface every divisorial ideal `I_i=O(-ic)` is reflexive
and has depth two at closed points. The quotient of `I_i` by
`I_(i+1)` has depth at least one by the depth lemma. The quotient is
annihilated by the reduced curve ideal `I_1`, has generic rank one
on `c`, and has no finite-point torsion. Because `c` is smooth it is
therefore a line bundle `E_i`, including at singular points of the
ambient normal surface.

The defining valuation inequalities prove `I_1^2 subset I_2` and
`sqrt(I_2)=I_1`. Hence `O/I_2` has square-zero nilideal `E_1` and
is Cohen--Macaulay of generic length two. This is the entire symbolic
ribbon; no Cartierness of `2c` has entered. The corresponding assertion
for ordinary ideal squares would not follow from this proof.

## 2. Multiplication and the actual Cartier relation

Products of representatives descend to

    E_i tensor E_j -> E_(i+j)

because changing a representative introduces a product in
`I_(i+j+1)`. This is an `O_c`-linear map, generically an isomorphism,
and therefore an injection of line bundles. Its zero divisor is
effective. Associativity verifies the coefficientwise defect
inequality in the author's note.

If `rc~bH` is Cartier, the equality of divisorial sheaves is

    I_(i+r)=I_i tensor O(-rc).

It gives `E_r=O_c(-bH)` and the stated periodicity. Multiplying a
layer until its index is a multiple of `r` gives

    deg E_j <= -j d^2/a,

since `rd=ba`. This is independent of whether any ambient first
normal direction survives.

## 3. The Euler identity and conormal bounds

The hyperplane Euler difference computes

    chi(O_S(mH))=(a/2)m^2-(kappa/2)m+chi(O_S).

For the carrier application a general Cartier hyperplane section
avoids the isolated normal-surface singularities. The arithmetic
Euler difference also works without requiring its geometric
smoothness. Subtracting the value at `m=-b` from that at zero and
using the symbolic filtration yields

    sum_(i=0)^(r-1) deg E_i
      =-(ab^2+b kappa)/2-r(1-g).

Thus the arbitrary surface Euler constant cancels. The inequality
`deg E_i>=i ell`, for `ell=deg E_1`, gives exactly the author's
bound for `r>=2`. For `r=2` no higher multiplication defect remains,
so the bound is an equality.

A generically nonzero map `N_C*->E_1` gives a generically injective
dual map `E_1^{-1}->N_C`. Saturating this line can only increase
its degree. Therefore `ell>=-M` whenever `M` bounds all line
subbundle degrees of `N_C`. The larger splitting degree supplies
the exact `M` on `P1`; semistability supplies the separate claimed
slope bound on an arbitrary smooth curve.

The valuation refinement is also valid globally. If `q` is the
minimum generic valuation of the pulled-back ambient curve ideal,
that ideal lies in `I_q` by its defining valuation, and its square
lies in `I_(2q) subset I_(q+1)`. Passing to `E_q` therefore gives
a map from the ambient conormal bundle. It is generically nonzero
by the definition of `q`, so the periodicity and saturation argument
give `q d^2<=a M`. This does not manufacture singleton support or
an isomorphic lift; those remain assumptions.

## 4. Numerical scope and one corrected sentence

Substitution of `M=2d-1,g=0,kappa=2pi-a-2` gives

    r[d^2-a(2d-1)]+2d(pi-1)+a(d+1)<=0.

At `a=d` it reduces to `2pi<=(r-1)(d-1)`. At `r=2,a=d`, the
nilbundle has degree exactly `-d-2pi`. This proves the all-degree
balanced-rational Cartier-double obstruction `2pi>d-1`, conditional
on the actual double relation and nonzero first conormal map.

The accepted quintic input gives only `ell<=-7/2`, hence
`-7<=ell<=-4`; the new criterion does not exclude it. The existing
quartic bisection instance is used as an accepted specialization,
not reverified.

During review I found one overbroad monotonicity sentence: increasing
`r` need not weaken the Euler bound merely because `pi>=g` when
`a` and `d` differ. The author corrected this before finalization.
Writing the upper bound as

    -A-(A+B)/(r-1),
    A=d^2/a, B=d kappa/a+2(1-g),

shows that enlargement weakens it precisely when `A+B>=0`.
For `a=d` this sign is `2(pi-g)`. No theorem conclusion depended
on the former broad sentence.

This review accepts the stated conditional inequalities and ribbon
construction. It supplies no global Cartier-index bound, no
classification of the multiplication defects, no exclusion for
multiple normalization primes, and no unrestricted STCI resolution.
