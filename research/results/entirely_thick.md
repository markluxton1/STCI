# Entirely-thick numerical restrictions

Let \(C\subset\mathbf P^3\) be a smooth rational quartic on a smooth quadric
\(Q\) over an algebraically closed field \(k\). Assume its normal bundle is
balanced, \(N_{C/\mathbf P^3}\simeq\mathcal O_{\mathbf P^1}(7)^{\oplus2}\).
Let \(F_a,G_b\) be a proper homogeneous pair of degrees \(a,b\) and exact
generic normal orders \(p,q\ge2\) along \(C\). Assume their intersection has
sole reduced support \(C\).

On the blowup along \(C\), the strict-transform intersection cycle is
effective and supported on the exceptional \(\mathbf P^1\times\mathbf P^1\).
Its bidegrees give
\[
ab\ge4pq,
\]
\[
7ab+28pq\ge16(aq+bp).
\]
The nonzero restrictions to \(Q\), after removing \(pC\) and \(qC\), give
\[
a\ge3p,\qquad b\ge3q.
\]

Writing \(\alpha=a/p,\beta=b/q\), the second inequality is
\[
\frac{7}{4}\alpha\beta+7\ge4(\alpha+\beta),\qquad \alpha,\beta\ge3.
\]
In particular, \(\alpha=3\) forces \(\beta\ge4\), excluding \((3,3)\).
The [supported-cycle proof](../arguments/normal-geometry/rees_and_vertical_controls.md#supported-cycle-bidegrees-and-the-universal-numerical-restriction)
derives these bounds.

## The exact \((3,4)\) boundary

For the fixed \(C_0=[s^4:s^3t:st^3:t^4]\) and \(\operatorname{char}k\ne2\),
retain the proper-pair, sole-support and balanced-normal-bundle hypotheses.
If \(a=3p\) and \(b=4q\), the exceptional intersection cycle is
\(2pq[T]\) on one constant section \(T\). The divisor cut by \(F_a\)
on \(Q\), after subtracting \(pC_0\), is a single ruling of
multiplicity \(2p\). The divided mate cuts that ruling at one point
with multiplicity \(q\). This sharpens the
[cycle count](../arguments/normal-geometry/rees_and_vertical_controls.md#the-exact-supported-3p4q-boundary-and-distinct-residual-roots)
by [connectedness of the strict intersection](connected_normal_directions.md#the-equality-boundary-on-the-first-blowup).

The [higher-order Rees question](../frameworks/formal-normal-geometry/open_normal_geometry.md#higher-order-rees-data-for-entirely-thick-pairs)
concerns the remaining entirely-thick branch.
