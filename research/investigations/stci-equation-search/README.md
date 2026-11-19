# Search for two homogeneous equations

Work over an algebraically closed field of characteristic zero with
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Completion requires an
actual defining pair or an obstruction covering every bidegree and every
proper homogeneous pair. The repository's [degree bound](../../results/quartic_carrier_exclusion.md)
and the [literature status](../../literature/README.md#current-status-and-general-bounds)
leave that question open.

## Construction with a known divisor upstairs

The [marked toric quintic](../../arguments/carriers/quintic_non_gorenstein_toric_sources.md)
has an explicit section with divisor five times the marked quartic. Search
for a projection for which a power descends. The inputs are the
[remaining center equations](../../arguments/carriers/quintic_toric_center_incidence.md#4-three-exceptional-curves-and-the-uncompleted-locus)
and their [exact coefficients](../../computations/quintic_toric_finite_centers.json).
Retain every nonvanishing condition in (3).

Write \(W=\sum_{i=0}^5 w_i t^i\), \(h=dt^2-2ct+b\). A prospective
center on this locus must satisfy \(hW'=(5dt+L)W\). Comparing the two
highest coefficients gives \(w_5 L=-10cw_5-dw_4\). Thus one can test the
six remaining polynomial coefficients without dividing by a parameter that
might specialize to zero. Use a univariate resultant with the parameter
equation \(M=0\) and retain all exceptional fibers. If a center survives,
check its full inverse support, projection admissibility and the descent
of the actual section. A failed center supplies no conclusion about other
sources.

The [exact elimination](toric_centers.py) finds four possible factors
for \(m\). At \(m=-2\) the only common root is \(n=1\), on the
diagonal. At \(m=-2/3\) there is no common root. The cubic factor
forces \(4n=m^2\), and the quintic factor forces \(d=0\). Both are
outside (3). An independent replay checked the coefficient signs, the
resultant projection and all four specialized fibers. This source has
no admissible center on which to descend the upstairs equation.

The [elliptic double inverse construction](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations)
gives a separate positive target. There the upstairs section is the quadric
\(Q_0\), and a homogeneous identity (8) on a basepoint-free birational
fiber produces a mate. No such identity has been verified.
