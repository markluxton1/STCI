# Normalization and conductor support

Let \(X\) be an integral hypersurface carrier, \(\nu:S\to X\) its finite normalization, and
\[
W=(\nu^{-1}(C))_{\mathrm{red}}
\]
the full reduced inverse image, including isolated points.

If \(C\) has an STCI mate on \(X\), then \(W\) is the support of an effective Cartier divisor on \(S\). Consequently an isolated zero-dimensional component of the full inverse image excludes every mate on that fixed carrier.

If all nonnormality of \(X\) is supported on \(C\), then existence of some STCI mate on \(X\) is equivalent to existence of an effective Cartier divisor \(A\) on \(S\) with support \(W\) and
\[
O_S(A)\cong O_S(bH)
\]
for some \(b>0\). A sufficiently high power of its canonical section descends through the conductor. This removes a separate asymptotic conductor obstruction in this support-contained case; it does not produce the required divisor or linear equivalence.

For integral quintics with toric normalization, the center
classification forces an extra inverse point for every admissible
projection of the marked source required by a mate. This excludes all
mate degrees. In the marked elliptic
double-cover construction the inverse away from the elliptic curve is
the off-curve part of a length-twelve scheme. If its entire support lies
on that curve, the remaining question on a birational fiber is descent
of a pure power in the four projection coordinates.
[Toric quintics](toric_quintic_carrier_exclusion.md) ·
[Elliptic double cover](elliptic_inverse_support.md)

## Proof and characteristic range

The [full fixed-carrier theorem](../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#4-an-exact-fixed-carrier-criterion-including-thick-support) proves this support-contained corollary in arbitrary characteristic. Every branch over C has positive vanishing order, so a sufficiently large power enters the full conductor over C; there are no off-C unit phases. Purity then gives global descent. This does not remove the need to produce the actual upstairs divisor and polarization relation.

The [local conductor algebra](../arguments/carriers/conductor_descent_algebra.md) explains the characteristic-zero versus Frobenius distinction when off-C unit phases are present.
