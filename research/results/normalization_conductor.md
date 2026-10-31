# Normalization and conductor support

Canonical status: **PROVED under stated hypotheses**

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

The criterion is carrier-specific.

## Proof and characteristic range

The [full fixed-carrier theorem](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#4-an-exact-fixed-carrier-criterion-including-thick-support) proves this support-contained corollary in arbitrary characteristic. Every branch over C has positive vanishing order, so a sufficiently large power enters the full conductor over C; there are no off-C unit phases. Purity then gives global descent. This does not remove the need to produce the actual upstairs divisor and polarization relation.

The [local conductor algebra](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md) explains the characteristic-zero versus Frobenius distinction when off-C unit phases are present.
