---
id: STCI-R-0074
type: result
title: Full Chow-polytope rigidity for the fixed quartic
scope: "#scope"
statement: "#statement"
proofs:
  - name: endpoint support and separating-face degree exhaustion
    at: "research/arguments/equations/chow_polytope_rigidity.md#scope-and-statement"
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

Independent reconstruction checked invariance, endpoint support, the reduced
line exception, characteristic-independent face identities, and degree
exhaustion. The integration review checked the proper-pair and Laurent
quotient scope separately. [PR #152 review](https://github.com/markluxton1/STCI/pull/152#pullrequestreview-5976576647)
supported the mathematics and requested the conceptual integration recorded
here. This record resolves H15 only, not H16 or unrestricted STCI.

## Limitations

The full unshifted weight polytope is essential. The theorem classifies
fundamental cycles, not scheme structures or homogeneous generators.
Distinct translates remain possible, and Laurent quotients alone do not
exclude projective boundary components.
