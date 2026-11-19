# Search for two homogeneous equations

Work over an algebraically closed field of characteristic zero with
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Completion requires an
actual defining pair or an obstruction covering every bidegree and every
proper homogeneous pair. The repository's [degree bound](../../results/quartic_carrier_exclusion.md)
and the [literature status](../../literature/README.md#current-status-and-general-bounds)
leave that question open.

## Construction with a known divisor upstairs

The [toric quintic computation](../../arguments/carriers/quintic_toric_center_incidence.md#exact-elimination-on-m0)
exhausted the admissible projection centers in that construction. The
[elliptic double inverse construction](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations)
has a different source. There the upstairs section is the quadric
\(Q_0\), and a homogeneous identity (8) on a basepoint-free birational
fiber produces a mate. The [residual scheme on that fiber](../../arguments/carriers/elliptic_double_inverse_construction.md#a-length-twelve-scheme-testing-every-basepoint-free-fiber)
has length twelve. Equation (9) tests whether all of its support lies on
the elliptic curve.

The [characteristic-zero search](elliptic_center_line.m2) fixes \(\mu=2\)
and \(\rho_0=\rho_1=\rho_3=0\), and allows every value of \(p=\rho_4\).
If a basepoint-free fiber has full inverse support, the length-twelve
scheme must meet \(E\). To test this, the script restricts its three
divided equations to \(E\), eliminates the source coordinates in each
of the four projective charts, and intersects the resulting parameter
ideals. The image has a squarefree degree-six equation over
\(\mathbf Q(i)\). Over these six parameters the script checks the
undivided inverse equations on \(Q_0=1\). Their elimination gives
the same parameter ideal. Since the parameter set is finite, every
geometric point of this image has a preimage. All six fibers are
basepoint-free and each has an extra inverse point. Thus this
entire one-parameter search yields no defining pair.

To find a candidate to lift, the [finite-field search](elliptic_centers.m2)
specializes the four section rows at \(i=2\) over \(\mathbf F_5\).
It tests both smooth rational parameters \(\mu=2,3\) and each of the
\(5^4\) lift tuples on each quadric. The chart \(Q_0=1\) meets the lift
of every off-curve projective point after adjoining a square root.
A basepoint on the chart also satisfies the inverse equations. For each
tuple the script checks whether (7) contains 1, using a Gröbner basis
in the actual specialized ring. All 1,250 ideals were proper, so the
search yielded no lift candidate. This calculation concerns rational
parameter tuples in this reduction, with geometric inverse points.
The characteristic-zero support incidence and pure-power identity are open.

Both searches replay from the repository root.

```sh
M2 --script research/investigations/stci-equation-search/elliptic_center_line.m2
M2 --script research/investigations/stci-equation-search/elliptic_centers.m2
```
