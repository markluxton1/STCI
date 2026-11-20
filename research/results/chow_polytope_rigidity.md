---
id: STCI-R-0074
type: result
title: Full Chow-polytope rigidity for the fixed quartic
scope: "#scope"
statement: "#statement"
proofs:
  - name: endpoint support and separating-face degree exhaustion
    at: "research/arguments/equations/chow_polytope_rigidity.md#chow-forms-products-and-the-one-parameter-subgroup"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Full Chow-polytope rigidity for the fixed quartic

## Scope

Over an algebraically closed field of arbitrary characteristic, fix
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), the diagonal torus \(T\),
and the full column-weight Chow polytope in two hyperplane coefficient rows.
Equality is literal, not projected or up to translation. Let \(m\ge1\) be an integer.

## Statement

Among **all effective one-cycles**, with no invariance assumption,
\[
 P_Z=mP_C\iff Z=\sum_jn_j[\lambda_jC],\qquad
 \lambda_j\in T(k),\quad n_j\in\mathbf Z_{>0},\quad\sum_jn_j=m.
\]
Thus this fiber of the Chow-polytope map is rigid; invariance is a conclusion.
For a proper homogeneous pair of degrees \(a,b\) with \(ab=4m\), the
same equivalence applies to its fundamental cycle. It is necessary but
not sufficient for that cycle to be \(m[C]\): other translates are allowed.
No scheme, embedded-point, or two-equation realization claim follows.

## Proof

See the [complete argument](../arguments/equations/chow_polytope_rigidity.md),
including the proper-pair coefficient criterion, the R-0050 connection,
and the boundary and characteristic caveats. The determinant replay is
supporting evidence, not a substitute for the written proof.

## Review

The route is accepted on the `reconstructed` basis in the repository's
[review convention](../MODEL.md#evidence-and-review), not by inheritance
from the historical H15 assertion. Independent mathematical review read the
written argument from its Chow-form invariance deduction through endpoint
support, the reduced-line exception, separating-face identities in arbitrary
characteristic, and width/degree exhaustion. The integer determinant
identities were separately reproduced by symbolic resultants and the retained
standard-library checker. The integration review additionally checked the
proper-pair coefficient criterion and the Laurent quotient and boundary
qualifications; neither computation nor structural validation certifies those
geometric implications.

The [initial PR review](https://github.com/markluxton1/STCI/pull/152#pullrequestreview-5976576647)
supported the cycle theorem and requested integration. The
[follow-up review of ce269db](https://github.com/markluxton1/STCI/pull/152#pullrequestreview-5976823819)
found those substantive requests addressed with no mathematical blocker.
These are reviews of the specified proof route and its scope, not an overall
authority classification or a certification of unrestricted STCI. H16,
scheme structure, and projective equation realization remain outside the
accepted claim.

## Limitations

The full unshifted weight polytope is essential. The theorem classifies
fundamental cycles, not scheme structures or homogeneous generators.
Distinct translates remain possible, and Laurent quotients alone do not
exclude projective boundary components.

The separate [fixed-carrier realization theorem](../arguments/torus/fixed_carrier_chow_arrangements.md)
classifies actual mates and their collision constraints on the named quartic
toric surface, with a contrasting quadric exclusion. These are scoped
realization results, not a classification of all Hilbert lifts of this fiber.
The [general first moment](../arguments/torus/chow_arrangement_moments.md)
further separates the Chow closure of invariant CI cycles, including reduced
arrangements, from the deepest diagonal in characteristic zero. It does not
classify non-invariant repeated-cycle lifts.
