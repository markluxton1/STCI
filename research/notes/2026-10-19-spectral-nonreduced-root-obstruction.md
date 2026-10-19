# A doubled-divisor obstruction to nonreduced moving spectral roots

Date: 2026-10-19. Author: primary research agent.
Status: **independently reviewed proposal; audit PASS**. The review
reconstructed the full argument and component corollaries. This file
does not promote a canonical result.

## 1. Exact question, accepted inputs, and scope

Work over an algebraically closed field `k` of characteristic zero. Write
`S=P1_base x P1_direction`, with projections `p,q`, and use
`O_S(a,b)=p*O(a) tensor q*O(b)`. A full root divisor is an effective
Cartier divisor `Z` finite flat of degree `r` over the base, of bidegree
`(epsilon,r)`. In particular, it has no vertical component.

The accepted [spectral criterion STCI-R-0008](../results/spectral_root_picard_criterion.md)
says, for a saturated first relation in a balanced split conormal bundle,
that an everywhere-coprime second **quotient** graded relation of degree
`s>r` exists if and only if

    O_Z(0,s) = p*O(n)|Z                              (1)

for an integer `n`. It retains the full, possibly nonreduced scheme `Z`.
No lifting of the second quotient line to a global polynomial line is
assumed here. The accepted
[moving-power result STCI-R-0009](../results/moving_purepower_boundary.md)
already excludes (1) for a multiple of a moving section. The new argument
excludes (1) for **every nonreduced moving root divisor**, including
repeated irreducible multisections and mixtures of components.

The primary STCI application has `C=C0`, `N_C=O(7)^2`. The proof below
concerns the spectral ruled surface and does not use an assertion about
the actual ambient formal neighborhood or arbitrary defining surfaces.

## 2. Differential restriction lemma

**Lemma 1.** Let `X` be a smooth scheme over a field, `D` an effective
Cartier divisor, and `L` a line bundle. If `L|2D` is trivial, then the
Hodge first Chern class

    c1(L) in H1(X,Omega_X)

restricts to zero in `H1(D,Omega_X|D)`.

**Proof.** Let `I=I_D`. On a sufficiently fine affine cover of `D`, choose
frames of `L` lifting a fixed trivialization on `2D`. Such frames exist
after shrinking ambient open sets: a lift of a unit modulo `I^2` is a
unit near `D`. The resulting transition functions satisfy
`g_ij=1 mod I^2`. The Leibniz rule gives `d(I^2) subset I Omega_X`.
Consequently `(dg_ij)/g_ij` restricts to zero in `Omega_X|D`.
These logarithmic differentials represent the restriction of `c1(L)`,
proving the claim. Equivalently, differentiation of a lift defines a
map `O_2D -> Omega_X|D`, independent of the lift because
`d(I^2) subset I Omega_X`, and it annihilates the transition cocycle of
a trivial line bundle. This argument does not require `D` to be smooth
or reduced. Square.

The use of **ambient** differentials restricted to `D`, rather than
`Omega_D`, is essential. Triviality only on `D` would not prove the lemma.

## 3. Picard injectivity on a doubled ample divisor

**Theorem 2.** Let `D subset S=P1 x P1` be an effective Cartier divisor of
bidegree `(a,b)` with `a,b>0`, over characteristic zero. Then

    Pic(S) -> Pic(2D)

is injective. More explicitly, if `O_S(u,v)|2D` is trivial, then
`u=v=0`. The divisor `D` may be singular, reducible, or nonreduced.

**Proof.** The restriction sequence for ambient differentials is exact:

    0 -> Omega_S(-D) -> Omega_S -> Omega_S|D -> 0.

Since

    Omega_S(-D)=O(-a-2,-b) direct sum O(-a,-b-2),

Kunneth and the usual cohomology of `P1` give
`H1(S,Omega_S(-D))=0`. Indeed, each Kunneth summand contributing to `H1`
has an `H0(P1,O(c))` factor with `c<0`. Hence

    H1(S,Omega_S) -> H1(D,Omega_S|D)

is injective. By Lemma 1, triviality on `2D` forces
`c1(O_S(u,v))=0` in `H1(S,Omega_S)`.

For completeness, `H1(S,Omega_S)=k direct sum k`, one summand for each
ruling. On a standard two-chart cover of `P1`, the transition `z` of
`O(1)` gives the nonzero Cech class `dz/z` in `H1(P1,Omega_P1)`.
The two ruling classes therefore form a basis, and
`c1(O_S(u,v))=(u,v)` in this basis, up to simultaneous conventions for
sign. Characteristic zero implies `u=v=0` as integers. Square.

This is a restriction theorem for line bundles on `S`. It is not an
assertion that all line bundles on `2D` come from `S`.

## 4. Nonreduced moving roots cannot have spectral descent

**Theorem 3.** Let `Z subset S` be an effective Cartier divisor, finite
flat over `P1_base`, of bidegree `(epsilon,r)` with `epsilon>0`.
Suppose there are integers `s>0,n` satisfying (1). Then:

1. `n r=s epsilon`, in particular `n>0`.
2. Every irreducible component `D_i` of `Z`, written with its reduced
   structure and bidegree `(a_i,b_i)`, satisfies
   `a_i>0`, `b_i>0`, and `s a_i=n b_i`.
3. `Z` is reduced as a divisor on `S`.

**Proof.** Write `Z=sum m_i D_i`, with `m_i>=1`. Finite flatness excludes
a vertical component, so `b_i>0`. Restricting (1) to the integral curve
`D_i` and taking degree gives

    s a_i=n b_i.                                      (2)

The degree computations are intersection computations on the smooth
surface: `deg O_Di(0,1)=a_i` and `deg O_Di(1,0)=b_i`.
Multiplying (2) by `m_i` and summing yields
`s epsilon=n r`. This proves `n>0`, hence `a_i>0` in (2).

If `m_i>=2` for any `i`, then `2D_i` is a closed subscheme of `Z`:
locally the equation of `Z` is divisible by the square of the equation
of `D_i`, so `I_Z subset I_Di^2`. Thus

    O_S(-n,s)|2D_i is trivial.

Theorem 2 applies to `D_i`, since both of its bidegrees are positive,
and forces `n=s=0`, contrary to `s>0`. All `m_i` equal one. An effective
Cartier divisor on a smooth surface with every prime multiplicity one
is reduced, so the claim follows. Square.

**Corollary 4 (graded obstruction).** Under the hypotheses of
STCI-R-0008 over the rational base in characteristic zero, a moving
first relation (`epsilon>0`) with nonreduced full root cannot have an
everywhere-coprime second quotient graded relation of any degree
`s>r`. Equivalently, the class of `O_Z(0,1)` has infinite order in
`Pic(Z)/p*Pic(P1)` for such a nonreduced moving root.

This includes repeated irreducible multisections, not only powers of
linear binary forms. It works uniformly in `epsilon,r,s`, and uses no
smoothness or irreducibility assumption on the root.

## 5. Reduced roots: a component bound and the movement-two boundary

The same proof records more than reducedness. Put

    g=gcd(epsilon,r),  epsilon0=epsilon/g,  r0=r/g.

If (1) holds, each component is of bidegree

    (a_i,b_i)=t_i (epsilon0,r0),  t_i a positive integer,
    sum t_i=g.                                       (3)

Indeed (2) gives the common slope, and coprimality of `epsilon0,r0`
gives integrality of `t_i`. Reducedness then gives the sum in (3).
In particular the number of irreducible components is at most `g`.
If `g=1`, the full root is integral.

For movement `epsilon=2`, any spectral-descent survivor therefore has
one of the following forms:

- an integral reduced divisor of class `(2,r)`, which may be singular;
- if `r` is even, a reduced union of two distinct divisors of class
  `(1,r/2)`.

An integral divisor of class `(1,k)` is smooth and rational: its
projection to the direction ruling is finite of degree one, and hence
is an isomorphism to the normal curve `P1`. The two components in the
second alternative have intersection length `r`; their intersections
and the full gluing data still enter the Picard descent test. No
torsion computation or ambient liftability is claimed for this locus.

## 6. Limits and precise STCI consequence

Theorem 3 eliminates **generic repeated factors** in a moving spectral
root whenever the uniform second-quotient-relation hypotheses hold.
It does not eliminate multiple roots occurring only in special fibers:
an integral ramified cover can have a nonreduced fiber while its total
root divisor is reduced.

For a hypothetical actual STCI on `C0`, if its full normal algebra has
a saturated moving first relation and a globally defined second
quotient generator coprime in every fiber as in STCI-R-0008, its root
must be reduced and satisfy (3). In particular, this excludes actual
pairs in that precisely specified uniform graded class with repeated
generic moving roots. It does **not** prove that an arbitrary actual
pair satisfies this uniformity assumption. Special-point initial-ideal
degeneration, nonsaturation, and additional initial generators remain
possible. No common singular point of the original surfaces is
assumed or deduced.

The separate [actual filtered-algebra bridge](2026-10-19-saturated-first-relation-spectral-bridge.md)
proves that an actual lci thickening with a saturated actual first
relation and full generic binary CI initial ideal satisfies precisely
the uniform graded hypotheses used here. Combining the two arguments
therefore excludes **actual** thickenings of `C0` in that class when the
full first root is moving and nonreduced. Saturation and the generic
two-generator initial-ideal pattern remain essential hypotheses.

If `epsilon=0`, the root is constant and may be nonreduced; the positivity
step above fails as it must. In positive characteristic, the final
Chern-class argument detects the integer bidegrees only modulo the
characteristic. No positive-characteristic exclusion is asserted.

## 7. Evidence, review, and continuation

The proofs above are conceptual; no finite parameter scan is used.
The standard Hodge Chern class via `dlog` and its Cech representative
are documented in the primary reference
[Stacks Project, Section 50.9, tag 0FLE](https://stacks.math.columbia.edu/tag/0FLE).
The line-bundle cohomology input is
[Stacks Project, Lemma 30.8.1, tag 01XS](https://stacks.math.columbia.edu/tag/01XS),
combined with the elementary Kunneth decomposition on the product.
The double-divisor restriction argument and spectral application are
proved here; the cited sources are inputs, not claims that this exact
STCI application was previously established.

Independent reconstruction and failure tests are recorded in
[the separate audit](2026-10-19-spectral-nonreduced-root-independent-audit.md).
The review outcome is PASS, including the component bound and the
movement-two dichotomy. This remains an unpromoted research proposal;
canonical promotion is a separate repository action.

The most valuable next bridge is to derive uniformity, or a sufficiently
controlled replacement for it, from the actual filtered Gorenstein
algebra. The component classification also reduces the movement-two
spectral boundary to integral singular curves and equal-slope pairs
of rational components, without discarding ramification or gluing.
