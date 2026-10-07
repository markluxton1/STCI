# Entirely-thick branch: generic normalization valuation filter

Date: 2026-10-07
Status: EXACT LOCAL NECESSARY CONDITION / NO GLOBAL EXCLUSION

## 1. Why no carrier-specific APic computation was made

The current canonical frontier does not contain a surviving explicit integral nonnormal carrier with normalization data sufficient for a Pic/APic lattice computation.

The retained cubic pinch-surface normalization is a control example already excluded because the full inverse image of C contains an isolated point. The normal quartic B1/B2/B3/D frontier has trivial normalization and is a different problem.

Therefore introducing an ad hoc nonnormal carrier would not advance the audited STCI frontier.

## 2. Generic local setup

Let X be an integral surface carrier containing C and let
    nu:S -> X
be its normalization. At the generic point eta of C, let Gamma_1,...,Gamma_t be the height-one points of S lying over eta. Their DVR valuations are v_1,...,v_t.

For a mate g whose reduced common zero set with X is C, the pullback of g to S has divisor along the branches
    div_S(g) = sum_j n_j Gamma_j + B,
where n_j=v_j(g)>0 and B has no component mapping dominantly to C.

If the mate has no additional common curve on X, any component of B relevant over the carrier must be excluded by the global support condition. In the clean situation the divisor supported over C is therefore
    A_g=sum_j n_j Gamma_j.

This is an effective Cartier divisor because it is locally principal, cut by the pulled-back mate.

## 3. Hyperplane relation

If g has ambient degree b, then on S
    O_S(div(g)) = O_S(bH).
Hence whenever the full zero divisor on the carrier is supported over C,
    sum_j n_j [Gamma_j] = b[H]
in Pic(S), or in the appropriate divisor class group if S is not smooth.

Thus the branch valuation vector
    n(g)=(v_1(g),...,v_t(g))
must lie in the positive integral kernel of the quotient map
    Z^t -> Pic(S)/<H>,
    e_j |-> [Gamma_j].

This is the generic normalization valuation filter.

## 4. Relation to Rees data

The Rees valuations of the pair ideal (f,g) in the ambient transverse two-dimensional regular local ring are not automatically the same as the branch valuations v_j on the normalization of the single carrier X=(f=0).

However, once a carrier f is fixed, the valuations v_j(g) are generator-sensitive data naturally visible in any resolution/normalized blowup dominating the normalization of X.

Therefore the correct bridge is not
    section coefficient c_i = branch coefficient n_j,
which has not been proved,
but rather:
    resolve the fixed carrier -> identify divisors/branches dominating C -> read v_j(g) -> impose the Pic/APic lattice relation.

## 5. Local APic contribution

When X is nonnormal along C, the class of a divisor supported on C is more naturally an almost-Cartier class. Hartshorne-Polini's normalization framework relates APic(X) to Pic(S) and local data along the conductor/singular locus.

Accordingly the full filter has two layers:

1. global normalization condition:
       sum n_j[Gamma_j] belongs to <H> in Pic(S);
2. local gluing condition:
       the associated local APic/conductor class is compatible with descent.

In the special case where all nonnormality is supported on C and only existence of some mate degree is sought, the repository's conductor-power theorem shows that sufficiently high powers remove the separate descent obstruction once the required Cartier support and hyperplane relation upstairs exist.

## 6. Immediate corollaries

For a fixed carrier:

- If no positive vector n has sum n_j Gamma_j proportional to H, the carrier is excluded for every mate degree.
- If the solution cone is one-dimensional, all mate branch multiplicities have a fixed rational ratio.
- If the solution monoid is finitely generated, comparison with possible valuation vectors becomes a finite semigroup problem.
- An isolated point in the full inverse image remains an immediate exclusion before this lattice calculation.

## 7. What this says about the entirely-thick program

The generic Rees/cluster invariant becomes useful only after fixing enough geometry of one carrier to map its valuations to normalization branches.

Thus there is no carrier-independent APic inequality analogous to the first-blowup inequality presently justified.

The next effective use of APic should occur when an explicit nonnormal carrier survivor emerges from the split/thick classification. At that point the normalization lattice test should be applied immediately rather than after a long local jet analysis.

## 8. Literature boundary

Hartshorne and Polini's divisor-class-group work already provides the general APic-via-normalization framework and applies it to STCI questions. The generic valuation filter above is a direct specialization/repackaging of standard divisor pullback plus the repository's conductor criterion; no novelty is claimed.

The project-specific open problem is to identify the coefficient vectors forced by the entirely-thick carrier geometry and show that they miss the admissible Pic/APic lattice for a nontrivial carrier family.
