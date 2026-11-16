# Global postulation and residual support

[Framework orientation](index.md) · [Original section addresses](weights_and_limits.md)

## V. Global constraints

### Postulation and support

For a proper homogeneous pair \((F,G)\), the Koszul resolution gives
\[
 \operatorname{Hilb}_{S/J}(z)=\frac{(1-z^a)(1-z^b)}{(1-z)^4},
 \qquad
 H_{S/J}(d)=b_3(d)-b_3(d-a)-b_3(d-b)+b_3(d-a-b),
\]
where \(b_3(j)=\binom{j+3}{3}\) for \(j\ge0\), and \(0\) otherwise.
For large \(d\) this is
\[
 P_Y(d)=ab\,d+\frac{ab(4-a-b)}2,\qquad
 p_a(Y)=1+\frac{ab(a+b-4)}2.
\]
The regular sequence makes \(S/J\) Cohen–Macaulay of dimension two,
so \(J\) is saturated and \(Y\) is pure with no embedded points.
Its fundamental cycle is
\[
 [Y]=m_C[C]+R,\qquad ab=4m_C+\deg R,
\]
where \(R\) is effective and has no \(C\)-component. For this proper
pair, sole reduced support is equivalent to \(\deg R=0\), or
\(m_C=ab/4\). In particular \(4\mid ab\) is necessary for sole
support. If a proposed subscheme is already contained in \(Y\),
equality of degrees also forces scheme equality by purity. This is
the degree-exhaustion step in the exact CI criterion for a constant
embedded quotient, after finding two coprime forms in its actual
homogeneous kernel. [Koszul polynomial](../../arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test) ·
[Pure-curve degree exhaustion and equation criterion](../../arguments/torus_embedded_quotients.md#pure-curve-degree-exhaustion).

The constant image of Part IV has polynomial
\(4nd+n-\delta_0-\delta_\infty\) and genus
\(1-n+\delta_0+\delta_\infty\). Indeed its finite modification has
Euler characteristic \(n(4d+1)\) in twist \(d\), and the endpoint
cokernels subtract a constant. For the moving finite modification
of an actual sole-support CI, put \(e=\deg\mathcal B\). Subtracting
\(\chi(\mathcal O_Y)\) from \(\chi(\mathcal B)=m_C+e\) gives
\[
 \delta_0+\delta_\infty=e+m_C(2a+2b-7).
\]
These lengths contribute to the constant term, whereas generic lengths
and residual curve degrees contribute to the linear coefficient.
For \((6,6)\), the CI polynomial is \(36d-144\), the genus is \(145\),
and sole support would give \(m_C=9\) and total endpoint index \(e+153\).
[Constant image polynomial](../../arguments/torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial) ·
[Moving endpoint budget](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification).

### Normal contact and residual cycles

For an actual sole-support pair, suppose the first symbols were
generically coprime, so \(m_C=r_Fr_G\). At each point of \(C\),
complete and choose a parameter lift for a transverse slice. Sole
support makes the completed algebra finite over the parameter DVR,
and the CM property makes the parameter a nonzerodivisor. The slice
has length \(m_C\), the rank of that free module. Its two orders are
at least \(r_F,r_G\) by the global sheaf-power condition. Equality in
the plane intersection inequality forces both orders to stay
\(r_F,r_G\) and their symbols to stay coprime. The resultant would be
nowhere zero. Its degree from Part II and the sole-support degree
formula would give
\[
 \frac{a}{r_F}+\frac{b}{r_G}=\frac{7}{2}, \qquad
 \frac{ab}{r_Fr_G}=4.
\]
The sum is at least four by the arithmetic–geometric mean inequality.
Thus sole support forces common generic normal directions and
\(m_C>r_Fr_G\). This restriction concerns the first normal symbols.
[Global resultant obstruction](../../arguments/normal-geometry/formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant).

Common factors have different roles in the two filtrations. A common
normal factor is a generic direction of continued contact on the
blowup. Residual curves are the strict intersection components off
the exceptional divisor, pushed down to \(\mathbf P^3\). A vertical
exceptional component pushes down to a point. In the raw extreme
fiber \(V(h_\pm A,h_\pm B)=V(h_\pm)\cup V(A,B)\), so a common
weight factor gives a surface.
Cancellation equations in the full limit can cut that surface down
to curves. For the sextic example below, the colon by \(q\) and the
restriction modulo \(q\) compute the residual divisor cycle on \(Q\),
while the full ideal retains its endpoint scheme. [Blowup and residual
cycle](../residual-construction/two_surfaces.md#22-the-common-graph-and-its-two-contractions) ·
[Colon and divisor-cycle proof](../../arguments/torus_sextic_residuals.md#a-colon-formula-for-divisor-cycles).

The dense-torus quotient controls only the part of the cycle seen
there. For a proper eigenpair the quotient on \(\Omega/T_C\) is
finite. Each of its points closes to a quartic orbit with multiplicity
equal to its local quotient length. For total quotient length \(n\)
the remaining cycle on the coordinate boundary has degree \(ab-4n\).
Identifying the marked orbit also requires its point \((1,1)\) and
its own local length. For mixed-weight pairs the generic normal
algebra is taken over \(k(C)\) and the product description by a
constant quotient requires an extra hypothesis. [Orbit curves and
quotient multiplicities](../../arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree).

### What the Hilbert function controls

The Hilbert function counts dimensions of graded pieces. ACM requires
depth two for the saturated coordinate ring, equivalently vanishing of
the Rao module \(\bigoplus_d H^1(\mathcal I_Y(d))\) for a pure curve.
For an ACM curve, multiplying its Hilbert series by \((1-z)^2\)
gives the Hilbert series after quotienting by a regular sequence of
two general linear forms. Thus a negative coefficient excludes ACM.
For the reduced quartic \(C\) the Hilbert function starts \(1,4,9,13\)
and equals \(4d+1\) for \(d\ge2\). The degree-two weight sums fill
\(0,\ldots,8\), and adding weights \(0\) and \(4\) inductively fills
\(0,\ldots,4d\) in every higher degree. The resulting numerator is
\(1+2z+2z^2-z^3\).
The CI Hilbert series follows from the Koszul resolution, whose
regular-sequence hypothesis proves ACM. The same series can arise
with different Betti numbers and depth. For a numerical check even
with a saturated ideal, in \(k[x,y,v,w]\) the quotient by
\((x^2,xy,xv^2,y^4)\) has Hilbert series
\[
 \frac{1-z^4}{(1-z)^3}+\frac{z+z^2}{1-z}
 =\frac{(1-z^2)^2}{(1-z)^4}.
\]
The first summand counts terms without \(x\), and the second counts
\(x,xv\) times powers of \(w\). The variable \(w\) is regular, proving
saturation, but modulo \(w\) the class of \(xv\) lies in the socle,
so the ring has depth one. This illustrates the distinction between
numerical and actual ACM. In Part VI the special fiber is ACM by
Hilbert–Burch and shares the CI series with its general fiber while
requiring three generators. [Migliore–Nagel, numerical ACM and the
Hilbert function](https://arxiv.org/abs/1202.2275) ·
[Sextic special-fiber resolution](../../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit).

