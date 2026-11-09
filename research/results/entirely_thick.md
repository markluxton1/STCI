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
The [supported-cycle proof](../synthesis/rees_and_vertical_controls.md#supported-cycle-bidegrees-and-the-universal-numerical-restriction)
derives these bounds.

## The exact \((3,4)\) boundary

For the fixed \(C_0=[s^4:s^3t:st^3:t^4]\) and \(\operatorname{char}k\ne2\),
retain the proper-pair, sole-support and balanced-normal-bundle hypotheses.
If \(a=3p\) and \(b=4q\), the exceptional intersection cycle is a sum of
constant sections. The divisor cut by \(F_a\) on \(Q\), after subtracting
\(pC_0\), consists of \(2p\) rulings counted with multiplicity. At most
\(\min(p,q)\) are distinct, so at least one is repeated. This is a necessary
restriction on the exact boundary. See the
[proof of the ruling count](../synthesis/rees_and_vertical_controls.md#the-exact-supported-3p4q-boundary-and-distinct-residual-roots).

The [higher-order Rees question](../FRONTIER.md#higher-order-rees-data-for-entirely-thick-pairs)
concerns the remaining entirely-thick branch.
