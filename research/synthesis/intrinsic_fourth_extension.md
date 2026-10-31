# An intrinsic fourth-extension obstruction for the fixed rational quartic

**Status: independently reviewed provisional classification and alternative proof; no new canonical result is promoted.** Work over an algebraically closed field of characteristic zero with
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). The classification below proves that every embedded quasiprimitive locally complete-intersection quadruple with the two saturated numerical types allowed for a `(4,4)` complete intersection is the primitive structure \(4C\subset Q\), where \(Q=(x_0x_3-x_1x_2=0)\). In particular no defective type occurs. The argument computes the obstruction to **extending an embedded triple**, without a matrix of ambient quartics or an orbit list. The universal transition identities and the displayed elimination supply the argument.

Dependencies: [quartic-pair obstruction](quartic_pair_obstruction.md), §§1–2 for the allowed types and §6 for the torsion-free contact-module sequence; balanced conormal [R-0020](../results/quartic_conormal_characteristic_jump.md). The primitive extension criterion is Bănică–Forster, *Multiplicity Structures on Space Curves*, Proposition 2.4; the quasiprimitive extension framework and equal-defect local model are Proposition 3.7 and §3.9(i), [author-hosted text](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf). The local proofs below supply the needed equal-defect specialization rather than invoking a stronger unstated classification.

## 1. What the contact extension detects

For a pure quasiprimitive embedded triple \(T\) with ideal \(J\), first layer \(L\), second layer \(E_2=L^2(D)\), and \(M=\ker(E\twoheadrightarrow L)\), set
\[
\mathcal M_T=(J/I_CJ)/\mathrm{tors},\qquad
0\longrightarrow K:=LE_2\longrightarrow\mathcal M_T\longrightarrow B:=M(-D)\longrightarrow0.\tag{1}
\]
This extension splits if and only if \(T\) admits an embedded quasiprimitive l.c.i. quadruple whose multiplication map \(L E_2\to E_3\) is an isomorphism, equivalently with the same actual defect divisor at its second and third layers. This is stronger than merely requiring linearly equivalent divisors.

Indeed, a retraction \(\beta:\mathcal M_T\to K\) defines \(I_Z=\ker(J\to K)\). At a primitive point write \(J=(m,l^3)\); its kernel is \((m-cl^3,l^4)\). At a defect write \(J=(x^2-ay,xy,y^2)\), where \(a\) cuts out \(D\). The torsion class of \(y^2\) maps to zero, and a retraction takes \([xy]\) to its chosen generator and \([x^2-ay]\) to \(c\) times that generator. The kernel is
\[
(y^2,x^2-ay-cxy).
\]
Its quotient is free of rank four over the support parameter ring, with basis \(1,x,y,xy\); it is a complete intersection, and its second and third defects both equal \(\operatorname{div}(a)\). Conversely, the quotient \(J/I_Z=LE_2\) of such a quadruple kills torsion and restricts to the identity on the product subline \(LE_2\subset\mathcal M_T\). It is a retraction. These constructions are inverse. Any two retractions differ by \(\operatorname{Hom}(B,K)\).

In both allowed quartic types \(K=\mathcal O(-18)\):
\[
(e,D)=(0,\deg D=3): B=\mathcal O(-10),\quad
(e,D)=(1,0):B=\mathcal O(-8).
\]
Thus the obstruction lies in \(H^1(\mathcal O(-8))\) or \(H^1(\mathcal O(-10))\), respectively. If an extension exists, it is unique because the respective \(H^0\)'s vanish.

There is also a source interpretation. For any extension \(0\to K\to V\to B\to0\), two sections of \(V\otimes A\) whose images generate \(B\otimes A\) and whose wedge is zero force the extension to split: wherever one quotient section is a unit, divide its lift by that section; zero wedge makes these local splittings agree. For the quartic types \(K(16)=\mathcal O(-2)\), so a split extension conversely forces the wedge of every pair of global sections of \(\mathcal M_T(16)\) to vanish. Under the exact fixed-divisor condition of a hypothetical `(4,4)` pair, its first-symbol sections generate \(B(16)\). This explains why the extension class is a sufficient intrinsic target; it does not infer anything about arbitrary source images from numerical degrees alone.

## 2. Charts and coverage of embedded triples

On \(x_0=1\) use
\[
z=x_1,\quad V=x_2-z^3,\quad U=x_3-z^4-\tfrac32zV.
\]
On \(x_3=1\), put
\[
W=x_2/x_3,\quad a_*=x_1/x_3-W^3,\quad b_*=x_0/x_3-W^4,
\quad U'=a_*/2,\quad V'=-3Wa_*+2b_*.
\]
Along \(C\), \(W=z^{-1}\), \(U'=z^{-7}U+O(I_C^2)\), and \(V'=z^{-7}V+O(I_C^2)\). These two actual ambient charts cover all of \(C\), including both endpoints. All calculations below retain the nonlinear support coordinate \(W\).

A quotient \(E\twoheadrightarrow\mathcal O(e-7)\) is specified by a pair \((A,B)\) of degree-\(e\) binary forms without a common zero, with the normal direction \((U,V)=(Ay,By)\). This describes the complete quotient parameter space, not a selected orbit. For \(e=0\), write \((A,B)=(a,b)\ne(0,0)\); for \(e=1\), write
\[
A=a_0+a_1z,\ B=b_0+b_1z,\quad d=a_0b_1-a_1b_0\ne0.
\]
The double is determined by this quotient. The possible triple lifts are governed by its quadratic transition cocycle. Once its defect section is fixed, the space of differences between two lifts is
\(H^0(\operatorname{Hom}(M,L^2(D)))=H^0(\mathcal O(-4))=0\) in both cases. Consequently the regular corrections extracted below are exhaustive, when they define pure triples. This is the standard extension construction: the local images of \(m\) and \(y^2\) in the second layer must generate that line bundle. Failure of that local surjectivity is failure of purity, not a new allowed triple.

For checking the expansions, write
\[
 x_3=z^4+Py+Qy^2,\quad V=By+V_2y^2.
\]
Then
\[
\begin{split}
w_1&=B/z^4-P/z^5,\\
w_2&=V_2/z^4-BP/z^8+P^2/z^9-Q/z^5,\\
w_3&=B(P^2/z^{12}-Q/z^8)-V_2P/z^8+2PQ/z^9-P^3/z^{13}
\end{split}\tag{2}
\]
are the coefficients of \(W=z^{-1}+w_1y+w_2y^2+w_3y^3\). If \(U'=u_1y+u_2y^2+u_3y^3\), \(V'=v_1y+v_2y^2+v_3y^3\), then \(u_1=A/z^7,v_1=B/z^7\), and
\[
\begin{split}
u_2&=(P^2/z^{11}-Q/z^7-3w_2/z^2-3w_1^2/z)/2,\\
u_3&=(2PQ/z^{11}-P^3/z^{15}-3w_3/z^2-6w_1w_2/z-w_1^3)/2,\\
v_2&=-P^2/z^{12}+Q/z^8+3w_1P/z^7+w_2/z^3+6w_1^2/z^2,\\
v_3&=-2PQ/z^{12}+P^3/z^{16}-3w_1P^2/z^{11}+3w_1Q/z^7
       +3w_2P/z^7+w_3/z^3+12w_1w_2/z^2+4w_1^3/z.
\end{split}\tag{3}
\]
These follow by expanding \(W=(z^3+V)/x_3\), \(U'=(z/x_3-W^3)/2\), and the useful identity \(V'=(2-3zW)/x_3+W^4\).

## 3. The defective type has a nonzero fourth-extension class

For constant \((a,b)\), the quadratic cocycle for \(m=bU-aV\), with normal direction \((U,V)=(ay,by)\), is
\[
h_2=-\frac{3(2a+bz)(4a^2+b^2z^2)}{8z^5}.
\]
A degree-three defect section \(\delta\) must make the coefficients of \(z^{-1},z^{-2},z^{-3}\) in \(\delta h_2\) vanish. If \(ab\ne0\), the kernel is one-dimensional and
\[
\delta=z(bz-2a),\qquad \delta h_2=6a^4z^{-4}-3b^4/8.\tag{4}
\]
For example, the three equations are the rows of
\[
\begin{pmatrix}
0&-3b^3/8&-3ab^2/4&-3a^2b/2\\
-3b^3/8&-3ab^2/4&-3a^2b/2&-3a^3\\
-3ab^2/4&-3a^2b/2&-3a^3&0
\end{pmatrix};
\]
the kernel vector is \((0,-2a/b,1,0)\). The divisor in (4), as a degree-three section, has zeros \(0,2a/b,\infty\). Thus no missing nonreduced divisor partition survives the quadratic compatibility equations for \(ab\ne0\).

If \(a=0,b\ne0\), the annihilators are \(z^2(\alpha+\beta z)\). The lower-chart second-layer coefficient of \(m\) is a nonzero scalar times \(\alpha+\beta z\), and the upper-chart coefficient is zero. When \(\alpha\ne0\), the upper defect section \(\alpha W+\beta\) has a zero at which both generating coefficients vanish. When \(\alpha=0\), the lower coefficients have the common zero \(z=0\). No pure triple of defect degree three results. If \(b=0,a\ne0\), the annihilators are \(\alpha+\beta z\), with zero lower correction. For \(\beta\ne0\) there is a lower common zero; for \(\beta=0\), the upper defect is \(\alpha W^3\) while its correction is a nonzero scalar times \(\alpha W\), again a common zero. These are all boundary directions.

It remains to compute the fourth-extension class of the unique pure triple (4). Put \(y=V/b\), \(\gamma=3b^4/8\), \(\gamma'=6a^4\), and
\[
g_0=\delta m-\gamma y^2,\qquad h_0=ym/\gamma.
\]
On the upper chart use \(m'=bU'-aV'\), \(y'=V'/b\),
\(\delta'(W)=bW-2aW^2\), and
\[
g_\infty=\delta'(W)m'-\gamma'(y')^2,\qquad h_\infty=y'm'/\gamma'.
\]
These are frames for \(\mathcal M_T\). The first-symbol transition of \(g\) is \(z^{-10}\); the kernel transition of \(h\) is \(z^{-18}\). Evaluate \(g_\infty\) at the generic triple substitution
\(m=(\gamma/\delta)y^2\). Since \(h_0\) becomes \(y^3/\delta\), the normalized extension cocycle is
\(\eta=z^{10}\delta[y^3]g_\infty\). To identify the calculation with the extension class, the frame law in the torsion-free contact module is
\[
 [h_\infty]=z^{-18}[h_0],\qquad
 [g_\infty]=z^{-10}[g_0]+\mu[h_0].
\]
The substitution kills \(g_0\) and sends \(h_0\) to \(y^3/\delta\). After localization every element of \(I_CJ\) maps into \((y^4)\), so \(\mu=\delta[y^3]g_\infty\) is well defined. The Laurent expression below extends across the defect on the overlap. Torsion freeness of the contact module therefore establishes this frame law globally from the generic computation; the normalized cocycle is \(z^{10}\mu\).

Equations (2)–(3), with
\(A=a,B=b,V_2=0,P=a+3zb/2,Q=\gamma/(b\delta)\), give
\[
\eta=\frac{72a^7}{bz^8}+\frac{4a^6}{z^7}
-\frac{2a^5b}{z^6}-\frac{a^4b^2}{z^5}
-\frac{a^3b^3}{2z^4}-\frac{a^2b^4}{4z^3}
-\frac{ab^5}{8z^2}+\frac{b^6}{16z}.\tag{5}
\]
The apparent division by \(\delta\) cancels: (5) is a Laurent polynomial regular on the chart overlap. In \(H^1(\mathcal O(-8))\), the powers \(z^{-1},\ldots,z^{-7}\) form the Čech basis; the \(z^{-8}\) term is a coboundary. The coefficient \(b^6/16\) is nonzero. Therefore the contact extension does not split, and this triple admits no equal-defect l.c.i. quadruple.

## 4. The primitive split locus is exactly the quadric direction

Use \(m=BU-AV\) and \(y=(b_1U-a_1V)/d\). The upper direction forms are \(A'=a_1+a_0W\), \(B'=b_1+b_0W\), and
\(m'=B'U'-A'V'\), \(y'=(-b_0U'+a_0V')/d\).
The quadratic cocycle is
\[
h_2=-\frac{(2A+zB)(12A^2+3z^2B^2+4z^2(A_zB-AB_z))}{8z^5}.
\]
Write \(h_2=\sum_{j=-5}^{1}c_jz^j\). Triple existence means
\(c_{-1}=c_{-2}=c_{-3}=0\). Let
\[
\gamma=c_0+c_1z=-3b_1^2(2a_1+3b_0+b_1z)/8,
\qquad \gamma'(W)=-c_{-4}-c_{-5}W.
\]
The unique triple has \(g_0=m+\gamma y^2\), \(g_\infty=m'+\gamma'(W)(y')^2\). Its first-symbol transition is \(z^{-8}\), and its kernel generator \(y^3\) transitions by \(z^{-18}\). In the contact module the exact frame law is
\[
 [g_\infty]=z^{-8}[g_0]+\nu[y^3],\qquad
 [(y')^3]=z^{-18}[y^3].
\]
Substitution kills \(g_0\); extracting the cubic coefficient determines \(\nu\) modulo \(I_CJ\), and the normalized cocycle is \(z^8\nu\). Consequently its fourth-extension cocycle is
\[
\eta=z^8[y^3]\{m'+\gamma'(W)(y')^2\}
\quad\text{after}\quad
U=Ay+(a_1/d)\gamma y^2,\ V=By+(b_1/d)\gamma y^2.\tag{6}
\]
For hand reconstruction, use (2)–(3) with \(V_2=b_1\gamma/d\), \(P=A+3zB/2\), \(Q=(a_1+3zb_1/2)\gamma/d\). Then
\[
\begin{split}
[m']_3={}&(b_1+b_0/z)u_3+b_0w_1u_2+b_0w_2u_1\\
&-(a_1+a_0/z)v_3-a_0w_1v_2-a_0w_2v_1,\\
[y']_1={}&z^{-6},\qquad [y']_2=(-b_0u_2+a_0v_2)/d,\\
\eta={}&z^8\bigl([m']_3+2(-c_{-4}-c_{-5}/z)z^{-6}[y']_2-c_{-5}w_1z^{-12}\bigr).
\end{split}\tag{7}
\]
Only three of the nine Čech coefficients are needed. Set \(p=a_0b_1,c=a_1,f=b_0\), and let \(K_i=d[z^{-i}]\eta\). Expansion gives
\[
\begin{split}
K_1&=\frac{b_1^4}{32}(8p+72c^2+118cf+63f^2),\\
K_9&=a_0^4(4p+126c^2+59cf+9f^2),\\
K_5\big|_{a_0=b_1=0}&=-\frac{cf}{8}(2c+f)(40c^3+68c^2f+30cf^2+11f^3).
\end{split}\tag{8}
\]
These are coefficients of the contact-extension class, not source determinants. Zero class forces all of (8) to vanish. The triple equations are
\[
b_1P=0,\quad(2c+f)Q=0,\quad a_0R=0,\tag{9}
\]
where
\(P=2p+12c^2+16cf+9f^2\),
\(Q=8p+12c^2+4cf+3f^2\),
\(R=2p+36c^2+16cf+3f^2\).

Here is a direct elimination, without a list of triple orbits or any assumption about quartic source spaces.

* If \(a_0b_1\ne0\), then \(P=R=0\), so \((2c-f)(2c+f)=0\). The alternatives \(c=f/2\) and \(c=-f/2\) force \(p=-10f^2\) and \(p=-2f^2\), respectively. The bracket in \(K_1\) becomes \(60f^2\) or \(6f^2\); either vanishing forces \(p=0\), a contradiction.
* If \(a_0=0,b_1\ne0\), then \(d=-cf\ne0\). The equations \(P=0,K_1=0\) imply \(f(22c+9f)=0\). Substitution \(c=-9f/22\) into \(P\) gives \(540f^2/121\ne0\), a contradiction.
* If \(a_0\ne0,b_1=0\), again \(cf\ne0\). Twice the bracket in \(K_9\) minus \(7R\) is \(3f(2c-f)\). Thus \(c=f/2\), but \(R=20f^2\ne0\).
* Therefore \(a_0=b_1=0\), with \(cf\ne0\). If \(2c+f\ne0\), (9) and \(K_5=0\) imply \(12c^2+4cf+3f^2=0\) and \(40c^3+68c^2f+30cf^2+11f^3=0\). The remainder of the latter modulo the former is \(8f^2(2c-3f)/9\), giving \(c=3f/2\), where the former is \(36f^2\ne0\).

Thus the only possible split direction has \(a_0=b_1=0\), \(a_1=-b_0/2\). It is \(A=-fz/2,B=f\). Here \(\gamma=0\), and \(m=f(U+zV/2)=fq\) on the lower chart. The unique triple is \(3C\subset Q\). The existing \(4C\subset Q\) is its unique fourth extension by §1. This identifies the entire split locus, including the open and boundary parameter strata, without enumerating possible actual quartic pencils.

## 5. The embedded-neighborhood proof and its scope

The allowed Gorenstein quadruple must therefore be \(4C\subset Q\). Every quartic containing this scheme is divisible by \(q\), since on \(Q\)
\[
H^0(\mathcal O_Q(4,4)\otimes\mathcal I_{4C/Q})
=H^0(\mathcal O_Q(0,-8))=0.
\]
Hence two such quartics cannot intersect properly. This supplies an embedded-neighborhood proof of the `(4,4)` exclusion with only the elementary quadric restriction at the final source step. It does not use the global surface rank bound, an all-degree carrier theorem, or a claim that first symbols exhaust all quartic source sections. It does not address arbitrary higher-degree STCI pairs.

The [exact universal cocycle derivation](../computations/quartic_fourth_extension_cocycles.py) works directly in the truncated algebra \(k(z,\mathrm{parameters})[y]/(y^4)\) using the rational ambient chart definitions. It reconstructs the defective class, both kernel transitions and the three primitive coefficients independently of equations (2)--(3). The displayed formulas and hand elimination establish the full parameter claim; numerical samples are not used for exhaustion.

## Independent reconstruction

Independent review reconstructed the extension correspondence and multiplication identification, the full quotient parameter spaces and failed-purity boundaries, and the contact-module frame laws after removing defect torsion. A separate derivation from the rational ambient charts verified the universal coefficients before imposing triple compatibility, and review checked all four branches of the hand elimination. No material defect remained. The classification is confined to the two stated saturated quadruple types on this embedding in characteristic zero. The resulting alternative proof of R-0022 uses neither the all-degree carrier theorem nor a global surface bound and does not address arbitrary higher-degree STCI pairs.
