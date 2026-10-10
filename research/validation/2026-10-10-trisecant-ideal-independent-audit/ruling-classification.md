# Independent audit: lines meeting the fixed rational quartic in length at least three

Date: 2026-10-10. Status: **PROVED by the elementary argument below**, independently of any ideal-intersection calculation. Scope: the fixed curve

\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3
\]

over an algebraically closed field of characteristic zero, with the arbitrary-field caveat stated at the end.

## Scheme-theoretic classification

The parametrization \(\nu:\mathbf P^1\to C_0\) is an isomorphism: its inverse coordinates on \(x_0\ne0\) and \(x_3\ne0\) are respectively \(t/s=x_1/x_0\) and \(s/t=x_2/x_3\). The curve lies on the smooth quadric

\[
Q=V(x_0x_3-x_1x_2).
\]

Let \(L\) be an ambient line and \(Z=C_0\cap L\), with its actual scheme structure. If \(q|_L\), where \(q=x_0x_3-x_1x_2\), is nonzero, its zero scheme on \(L\simeq\mathbf P^1\) has length two. Since \(q\) vanishes on \(C_0\), the scheme \(Z\) is a closed subscheme of that length-two zero scheme. Hence \(\operatorname{length}Z\ge3\) forces \(q|_L=0\), so \(L\subset Q\). This implication applies to repeated intersections as well as reduced ones.

Under the Segre identification

\[
([u_0:u_1],[v_0:v_1])\longmapsto
[u_0v_0:u_0v_1:u_1v_0:u_1v_1],
\]

the curve is \([s:t]\mapsto([s^3:t^3],[s:t])\). Every line on \(Q\) fixes one factor. Indeed, if rank-one matrices \(u\otimes v\) and \(u'\otimes v'\) span a line of rank-one matrices, the determinant of their linear combinations forces \((u\wedge u')(v\wedge v')=0\). Thus one factor is fixed.

Fixing the first factor at \([1:a]\) gives

\[
\Gamma_a=V(x_2-a x_0,x_3-a x_1),\qquad
\Gamma_\infty=V(x_0,x_1).
\]

The pulled-back generators for finite \(a\) are \(s(t^3-a s^3)\) and \(t(t^3-a s^3)\). Since \(s,t\) locally generate the unit ideal on \(\mathbf P^1\), the pulled-back ideal sheaf is exactly \((t^3-a s^3)\). Thus \(C_0\cap\Gamma_a\) has length exactly three. At infinity the corresponding ideal sheaf is \((s^3)\).

Fixing the second factor at \([1:b]\) instead gives

\[
\Lambda_b=V(x_1-b x_0,x_3-b x_2).
\]

Its pulled-back ideal sheaf is \((t-bs)\), since its generators are \(s^3(t-bs)\) and \(t^3(t-bs)\). Thus its intersection has length one; the endpoint \(\Lambda_\infty=V(x_0,x_2)\) likewise has ideal sheaf \((s)\) and length one. This exhausts all lines on \(Q\), proving the claimed classification and the exact length-three assertion.

## Endpoint contacts and equivalence

In characteristic zero, for \(a\ne0,\infty\), the divisor \(V(t^3-a s^3)\) is geometrically reduced. The endpoint divisors are

\[
C_0\cap\Gamma_0=3[1:0:0:0],\qquad
C_0\cap\Gamma_\infty=3[0:0:0:1].
\]

Consequently there is no double-point-plus-simple-point trisecant stratum.

The ambient projectivity \(T_r=\operatorname{diag}(1,r,r^3,r^4)\) preserves \(C_0\) and sends \(\Gamma_a\) to \(\Gamma_{r^3a}\). Algebraic closure supplies \(r^3=b/a\) for any nonzero \(a,b\). Coordinate reversal \([x_0:x_1:x_2:x_3]\mapsto[x_3:x_2:x_1:x_0]\) also preserves \(C_0\), sends \(a\mapsto1/a\), and exchanges the endpoints. There are therefore exactly two geometric orbits in characteristic zero: nonendpoint lines and endpoint lines. Their intersection schemes distinguish them.

## Precise arbitrary-field caveat

Over any characteristic-zero field \(k\), the classification still holds for \(k\)-defined lines, with \(a\in\mathbf P^1(k)\); nonendpoint intersection schemes have degree three and are geometrically reduced but their points need not be individually \(k\)-rational. For \(a,b\in k^\times\), ambient equivalence over \(k\) is exactly

\[
\Gamma_a\sim_k\Gamma_b
\quad\Longleftrightarrow\quad
b/a\in(k^\times)^3\ \text{or}\ ab\in(k^\times)^3.
\]

For necessity, \(Q\) is the unique quadric through \(C_0\): the ten quadratic monomial products restrict to nine distinct binary monomials, with only the duplicate \(x_0x_3=x_1x_2\). Any ambient stabilizer preserves \(Q\). It cannot exchange the two ruling families because the two projections of \(C_0\) have degrees three and one. Its product action \((\phi,\psi)\) satisfies \(\phi\circ f=f\circ\psi\) for \(f(z)=z^3\). The ramification locus of \(f\) is exactly \(\{0,\infty\}\), so \(\psi\) preserves that pair, hence \(\psi(z)=rz\) or \(r/z\) with \(r\in k^\times\). Thus its action on \(a\) is \(r^3a\) or \(r^3/a\). The explicit diagonal and reversal transformations prove sufficiency. For example, \(\Gamma_1\) and \(\Gamma_2\) are inequivalent over \(\mathbf Q\), but equivalent over \(\overline{\mathbf Q}\).

The quadric/ruling length classification does not require characteristic zero. In characteristic three, however, the nonendpoint degree-three divisors are inseparable, so the reducedness and two-orbit conclusions above must not be transferred there.
