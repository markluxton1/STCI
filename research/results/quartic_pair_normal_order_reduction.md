---
id: STCI-R-0059
type: result
title: Normal-order reduction for proper quartic pairs through the fixed curve
scope: "#scope"
statement: "#statement"
proofs:
  - name: quadric residual class and generic length exhaust the degree
    at: "research/arguments/quartic_specialization_and_symbols.md#5-a-uniform-reduction-of-all-44-candidates"
    using: [STCI-R-0058]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Normal-order reduction for proper quartic pairs

## Scope

Let \(k\) be algebraically closed, in any characteristic, and fix
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). Let \(F,G\) be nonzero
coprime quartic forms through \(C\). Normal order and length are taken at
\(\eta_C\), where the completed ambient local ring is \(K[[X,Y]]\) for
\(K=k(C)\).

## Statement

If \(V(F,G)\) has reduced support \(C\), both normal orders are one.
Indeed, a quartic of order at least two is a scalar multiple of
\((x_0x_3-x_1x_2)^2\). Its proper intersection with a quartic mate
has residual support on the smooth quadric. On that quadric a divisor
of class \((4,4)\) cannot be supported on \(C\) of class \((3,1)\).

For a coprime pair with both orders one, \(V(F,G)\) has reduced
support \(C\) if and only if, after using one equation as a formal
normal parameter and quotienting by it, the first nonzero term of the
other equation in the remaining normal parameter has order four.
In that case the first symbols are dependent over \(K\). The order-four
test measures generic local length, and \(4\deg(C)=16\) exhausts the
degree of the complete intersection.

## Limitations

This is a reduction for proper pairs of actual global quartics. Formal
equations over \(K\) can satisfy the order test without coming from such
a pair. The [Cartier quadruple \(4C\) on the smooth quadric](../arguments/quartic_specialization_and_symbols.md#6-what-the-symmetric-algebra-does-and-does-not-explain)
is an embedded control in every characteristic. Its graded algebra is the
truncated symmetric algebra on \(\mathcal O_{\mathbf P^1}(-6)\) in
degrees zero through three and its Hilbert polynomial is \(16d-32\).
Its ideal contains the quadric, so it is outside the \((4,4)\)
complete-intersection locus.

## Review

The Phase 5 independent reviewer accepted the route for coprime quartics
over an algebraically closed field, using R-0058. The reviewer checked the
quadric divisor-class obstruction, the use of an actual first-order
equation as a formal parameter, and both implications of the cycle-degree
test with complete-intersection purity. The reviewer also reconstructed
the Cartier quadruple and the nonlinear overlap of the prescribed
characteristic-two pair.

The October 23 audit checked the symbol calculations underlying this
reduction. The separate filtered characteristic-zero exclusion has
additional premises and a different proof review. [Source review](../arguments/quartic_specialization_and_symbols.md#source-review-and-verification)
