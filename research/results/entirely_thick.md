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


## Curvilinear recovery and primitive graph structures

On the exact \((3p,4q)\) edge, the [first-graph recovery and primitive arithmetic](../arguments/residuals/blowup_residual_geometry.md#recovering-generic-curvilinearity-in-all-orders-on-a-subset-of-the-edge) extends the second-blowup bound: for \(p=2\) and every mixed direction the strict sextic is generically regular along the unique section; endpoint directions have generic curvilinearity when \(2\le q<6\). Across the whole edge the first strict CI can be primitive everywhere only for five necessary order pairs. Its divided exceptional resultant and finite transfer to \(V_5\) are given by [the pointwise defect comparison](../arguments/residuals/blowup_residual_geometry.md#socle-defects-on-the-two-presentations-of-the-first-graph). The [marked-line obstruction ML9](../arguments/residuals/blowup_residual_geometry.md#all-orders-the-marked-line-comparison-by-interpolation) eliminates primitivity at the prescribed marked point for every mixed \((3p,4q)\) edge pair with \(2\le p\le q\), without ADE or normality assumptions. Thus the globally primitive mixed \((6,8)\) row is excluded, not merely conditionally: only the mixed slope-four and endpoint slope-five rows remain there, with positive marked defect in the mixed row. Of the five necessary global primitive order pairs on the full edge, mixed directions survive this test only at \((10,4),(21,3)\); endpoint directions remain subject to their separate splitting and line contact. The [full marked finite-modification lattice](../arguments/residuals/blowup_residual_geometry.md#full-marked-finite-modification-lattice-in-the-primitive-at-the-point-stratum) identifies the completed image ideal for \(q=2\) in the primitive graph stratum as \((y^2-x^2t,t^{2p})\), with multiplication defects \(D_j=2\lfloor j/2\rfloor\); for a generically regular image carrier the local index is two (marked \(D_{2p+1}\)) or \(4p\) (multiplicity at least three). The opposite [smooth marked image-carrier lane](../arguments/residuals/blowup_residual_geometry.md#the-opposite-marked-stratum-a-smooth-image-carrier-and-a-forced-graph-defect) gives strict equations \(xv=t^{2p},v^q=0\), defects \(D_j=\lfloor j/(2p)\rfloor\) and marked index \(2p\) on the strict carrier. A degree-two image mate there would descend to an original degree-four mate by exact conic trace cancellation, so is excluded. For \(q=2\) and an integral smaller image carrier its minimal image mate degree is therefore four; for \(p=2\) an actual index-eight point away from the smooth marked point is forced. These deductions await independent review. These new deductions use the R-0077 hypotheses and await independent review.
