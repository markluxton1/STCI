# Dual incidence and the involution secant scroll

Date: 2026-10-24. Author/reviewer role: `dual_incidence`, independent derivation for the special-line investigation.

**Status: provisional research evidence, not a canonical result or an STCI obstruction.** Throughout, the field is algebraically closed of characteristic zero and the embedded curve is exactly
\[
 c(u)=[1:u:u^3:u^4],\qquad c(\infty)=[0:0:0:1].
\]
The calculations below reconstruct this embedding directly. No quartic-carrier exclusion, normal-bundle splitting, or earlier normal-direction inequality is used. The index and authority/contribution rules were consulted. The geometric labels in this note refer to the fixed embedding, not arbitrary smooth rational quartics.

## 1. The hyperplane system and its two discriminant curves

The hyperplane system is the basepoint-free four-dimensional subspace
\[
 V=\langle s^4,s^3t,st^3,t^4\rangle\subset H^0(\mathbf P^1,\mathcal O(4)).
\]
Thus its intrinsic discriminant consists of sections with a multiple zero. In the affine coordinate \(v=t/s\), its sections are binary quartics with zero \(v^2\)-coefficient. The osculating section with a triple zero at \(u\) must have the form
\[
 (v-u)^3(v-r).
\]
Its missing coefficient is \(3u(u+r)\), giving \(r=-u\) away from the endpoints. Homogeneous continuation gives the involution \(\iota(u)=-u\), with fixed points \(0,\infty\), and
\[
 H_u:\quad -u^4x_0+2u^3x_1-2ux_2+x_3=0,
 \qquad H_u\cdot C=3c(u)+c(-u).
\]
At the endpoints this is \(4c(0)\) or \(4c(\infty)\). The normalization map of the osculating curve in dual projective space is
\[
 [s:t]\longmapsto[-t^4:2st^3:-2s^3t:s^4].
\]

A bitangent section is the square of a quadratic. Write that quadratic as \(v^2-wv+z\). The missing coefficient condition is \(w^2+2z=0\), so its section is
\[
 (v^2-wv-w^2/2)^2
   =v^4-2wv^3+w^3v+w^4/4.
\]
Consequently the bitangent curve in dual space is another rational quartic, parametrized by
\[
 B_w=[w^4/4:w^3:-2w:1].
\]
For \(w\ne0,\infty\) its contact points have parameters
\[
 u=\frac{1+\sqrt3}{2}w,\qquad
 v=\frac{1-\sqrt3}{2}w.
\]
Their ratio is one of \(-2\pm\sqrt3\), rather than \(-1\). Equivalently the ordered bitangent correspondence is
\[
 u^2+4uv+v^2=0,
\]
homogenized separately in the two factors of \(C\times C\). It is the union of the graphs of the mutually inverse automorphisms \(u\mapsto\rho u\), where \(\rho=-2+\sqrt3\). In particular, involution pairs are not bitangent pairs. The involution takes the bitangent plane \(B_w\) to \(B_{-w}\).

The two bitangent contacts merge at each endpoint to a quadruple contact; there is no tangent plane with contact divisor \(2c(0)+2c(\infty)\), because \(s^2t^2\notin V\). The osculating and bitangent curves in dual space meet only at these two quadruple-root sections. In the affine chart with last coefficient one near the first endpoint, equality of their coefficients imposes
\[
 u=w,\quad 2u^3=w^3,\quad -u^4=w^4/4.
\]
Their scheme-theoretic intersection there has length three, and similarly at infinity. They share their tangent and quadratic jet, then separate at cubic order.

The dual surface \(C^\vee\subset\mathbf P(V)\) is the restricted binary-quartic discriminant, a reduced irreducible surface of degree six. Its **reduced singular locus** is the union of the osculating and bitangent quartics and the two lines of endpoint triple-contact planes,
\[
\ell_0=\{[0:0:C:D]\},\qquad
\ell_\infty=\{[A:B:0:0]\}.
\]
At a nonendpoint triple root the residual point is forced to be its involution partner, giving the osculating quartic. At zero, however, every section \(v^3(C+Dv)\) has a triple root; the reversed chart supplies the second line. The extra lines are essential. At a quartic with exactly one double root and two other distinct roots, the full discriminant is smooth, and its differential is a nonzero multiple of evaluation at that double root. Restriction to \(V\) cannot annihilate this differential because \(V\) is basepoint free. Thus the hyperplane section introduces no additional singularities at simple double-root quartics. The remaining singular quartics have a triple root or two double roots, exhausted by these four components. This is a statement about the singular set, not the scheme structure of its singular ideal. The usual discriminant degree six follows from the resultant of a quartic and its derivative after removing its leading coefficient.

**Independent-review correction:** the initial draft omitted the two endpoint pencil lines by identifying every triple-root section with a limiting generic osculating plane. Reviewer geometry_final_audit identified the endpoint jet-rank failure. The four-component description above replaces that false two-component description. This correction does not affect the formulas for either quartic or their mutual intersection lengths.

## 2. The paired osculating line is the paired secant

For \(u\ne0,\infty\), both \(H_u\) and \(H_{-u}\) contain \(c(u)\) and \(c(-u)\). They are distinct, so their intersection is exactly
\[
 S_u=\langle c(u),c(-u)\rangle,
 \qquad x_2=u^2x_1,\quad x_3=u^4x_0.
\]
The unordered family is parametrized by the involution quotient \(z=u^2\). Its limiting members at \(z=0,\infty\) are
\[
 L_0=V(x_2,x_3),\qquad L_\infty=V(x_0,x_1).
\]
They are the endpoint tangent lines and have length-three intersection with \(C\). The general paired secant has two distinct simple contacts. It is not a trisecant.

The union of the lines \(S_u\) is the irreducible cubic ruled surface
\[
 R=V(x_0x_2^2-x_1^2x_3).
\]
Indeed its parametrization on this affine ruling chart is
\[
 [A:B]\longmapsto[A:B:zB:z^2A].
\]
Conversely the cubic equation reconstructs \(z=x_2/x_1\) when \(x_1\ne0\), and closure gives the entire surface. Its singular double directrix is \(V(x_1,x_2)\). The two hyperosculating points are its pinch points: at the first endpoint its equation is \(x_2^2=x_1^2x_3\), and the other endpoint has the analogous equation.

This surface supplies a useful geometric identity:
\[
 T_{c(u)}R=H_u\qquad(u\ne0,\infty).
\]
For verification,
\[
 \nabla(x_0x_2^2-x_1^2x_3)|_{c(u)}
 =u^2[u^4:-2u^3:2u:-1],
\]
which gives exactly that tangent plane. **The ruled cubic is not a developable surface.** Along a fixed ruling its tangent plane varies; it is merely the osculating plane along this distinguished section \(C\).

The first normal symbol of its equation has zeros of order two at each endpoint. This can be checked without choosing a conormal splitting. Near \(c(0)\) put
\[
 u=x_1,\qquad a=x_2-u^3,\qquad b=x_3-u^4.
\]
Then
\[
 R=2u^3a-u^2b+a^2,
\]
whose linear normal part is \(u^2(2ua-b)\); the parenthetical direction remains primitive at \(u=0\). The infinity chart is symmetric. This is an explicit surface and a direction calculation, not a hypothetical common-normal constraint for all STCI pairs.

## 3. The unique quadric, rulings, and polarity

On the smooth quadric \(Q=V(x_0x_3-x_1x_2)\), use the Segre coordinates
\[
 (x_0,x_1,x_2,x_3)=(ac,ad,bc,bd).
\]
The curve is the divisor \(bc^3-ad^3=0\) of class \((1,3)\), and the restriction of the ruled cubic factors as
\[
 R|_Q=ab(bc^3-ad^3).
\]
Hence, as Cartier divisors on \(Q\),
\[
 R\cap Q=C+L_0+L_\infty.
\]
This is a concrete residual divisor, not a vertical exceptional component.

The ambient involution extending \(u\mapsto-u\) is
\[
 A=\operatorname{diag}(1,-1,-1,1).
\]
It preserves \(Q\), its two rulings, and \(R\). On the Segre factors it acts as \(([a:b],[c:d])\mapsto([a:-b],[c:-d])\). Its fixed projective lines are the two eigenspace lines \(V(x_1,x_2)\) and \(V(x_0,x_3)\), and every paired secant joins a point of one fixed line to a point of the other.

For clarity, polarity with respect to \(Q\) sends the plane with coefficients \([a_0:a_1:a_2:a_3]\) to \([a_3:-a_2:-a_1:a_0]\). Thus the pole of \(H_u\) is
\[
 P_u=[1:2u:-2u^3:-u^4].
\]
The pole quartic lies on \(4x_0x_3-x_1x_2=0\); it meets \(Q\) only at the two endpoints, with intersection order four at each. The polar of the paired secant is a **different** line:
\[
 S_u^\perp=T_{c(u)}Q\cap T_{c(-u)}Q
 =V(x_3+u^4x_0,\ x_2+u^2x_1).
\]
In particular one should not identify \(H_u\) with the tangent plane of \(Q\) at \(c(u)\). For general \(u\), \(H_u\cap Q\) is a smooth conic meeting \(C\) in \(3c(u)+c(-u)\). At each endpoint that conic degenerates into the two quadric rulings through the point, contributing lengths three and one respectively.

## 4. Universal plane incidences and their actual compatibility content

On the product of the osculating parameter line and \(C\), the universal plane section is the Cartier divisor
\[
 D_{\mathrm{osc}}=3\Delta+\Gamma_\iota.
\]
This follows from the full factorization \(H_u(c(v))=(v-u)^3(v+u)\), including homogeneous continuation. It has bidegree \((4,4)\), as does the universal bitangent section
\[
 D_{\mathrm{bit}}=2\Gamma_{c_+}+2\Gamma_{c_-},
 \qquad c_\pm=(1\pm\sqrt3)/2.
\]
The endpoint mergers are already included in these Cartier divisors; they do not add vertical components.

Suppose now that \(Z=V(F,G)\) is a projective complete intersection with sole reduced support \(C\), degrees \(d,e\), generic multiplicity \(m\), and \(de=4m\). Either universal plane family defines
\[
 W=(Z\times\mathbf P^1)\cap\mathcal H\longrightarrow\mathbf P^1.
\]
This is finite flat of rank \(de\). Indeed every fiber is a zero-dimensional proper plane section of the Cohen--Macaulay curve \(Z\), of length \(de\). Projectivity and zero-dimensional fibers give finiteness. The universal plane is a nonzerodivisor on the two-dimensional Cohen--Macaulay product, so \(W\) is Cohen--Macaulay of dimension one; its nonconstant irreducible components dominate the smooth base, giving torsion-freeness and hence flatness. More directly the constant fiber length criterion for finite modules on a smooth curve gives the same conclusion.

The fundamental cycles are therefore
\[
 [W_{\mathrm{osc}}]=m(3\Delta+\Gamma_\iota),\qquad
 [W_{\mathrm{bit}}]=2m(\Gamma_{c_+}+\Gamma_{c_-}).
\]
These identities are on the reduced incidence support in the ambient product. The scheme \(W\) generally has a nilpotent structure and is not identified with a divisor on the reduced product. At the endpoints, distinct support branches merge and the entire fiber has length \(de\).

There is also a bundle-level numerical identity, rather than just a support cycle. For any degree-\(k\) family of planes having finite intersection with \(Z\) at every parameter, let \(E=f_*\mathcal O_W\). Then
\[
 \operatorname{rk}E=de,\qquad
 \deg E=-\frac{kde(d+e-2)}2.
\]
In particular both degree-four plane families above give \(\deg E=-2de(d+e-2)\). To verify this without smoothness assumptions on \(Z\), its complete-intersection Hilbert polynomial gives
\[
 \chi(\mathcal O_Z)=de(4-d-e)/2,\qquad
 \chi(\mathcal O_Z(-1))=de(2-d-e)/2.
\]
The universal plane exact sequence on \(Z\times\mathbf P^1\) is
\[
 0\to\mathcal O_Z(-1)\boxtimes\mathcal O(-k)
 \to\mathcal O_{Z\times\mathbf P^1}\to\mathcal O_W\to0.
\]
Taking Euler characteristics yields
\[
 \chi(\mathcal O_W)=de\left(1-\frac{k(d+e-2)}2\right),
\]
and \(\chi(E)=\operatorname{rk}E+\deg E\) on the base gives the formula. It is automatic for an actual complete intersection, so it becomes an obstruction only if some additional argument independently prevents an algebra with these data and the prescribed gluing.

This organizes a genuine family-level compatibility requirement: any actual pair has to produce these finite flat families, with their gluing across the two mergers. The cycles and flatness themselves follow formally from the actual complete intersection and the chosen plane family. They do not establish an extra numerical inequality or rule out its existence. A useful next question is whether the full scheme gluing can impose a constraint not already encoded by the ambient equations. This note has not proved such a constraint. Formal local models or length cycles alone cannot answer that global realization question.

## Verification boundary and research impact

All displayed geometric formulas have direct algebraic proofs above; they are new derivations for this investigation and remain provisional pending the parent investigation's independent review. In particular, the ruled cubic, polarity, and dual discriminant organize the geometry but do not replace any canonical STCI theorem. No normal-bundle calculation or quartic exclusion has been re-run. No assertion is made about arbitrary degrees, unrestricted STCI nonexistence, or a universal bound on common normal directions.
