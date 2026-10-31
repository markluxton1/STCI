# The quartic-pair obstruction: local algebra, global surfaces, and actual equations

Let (k) be algebraically closed of characteristic zero and fix
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]
There are no homogeneous quartics (F,G) with (V(F,G)_{\rm red}=C), including reducible and nonreduced defining equations. This is the scope of [R-0022](../results/quartic_44_filtered_exclusion.md). It is narrower than the [all-mate-degree quartic-carrier theorem R-0001](../results/quartic_carrier_exclusion.md), which is not an input to any proof here. The unrestricted characteristic-zero STCI question remains open.

There are two distinct completed mechanisms and three presentations. The filtered-contact proof tests the actual vector spaces of quartic equations through possible triples. The surface proof turns the first-symbol pencil and its defects into too many exceptional curves on a resolved quartic. The direct-blowup presentation proves the latter without a classification of surface singularities. A proposed proof confined to embedded neighborhoods and actual equation spaces, avoiding both orbit enumeration and a global surface bound, remains incomplete.

Throughout, \(\mathcal O(j)\) means degree \(j\) on \(C\simeq\mathbf P^1\); ambient \(\mathcal O_C(a)=\mathcal O(4a)\). The embedding-specific input is the [balanced conormal R-0020](../results/quartic_conormal_characteristic_jump.md),
\[
E=I_C/I_C^2=\mathcal O(-7)^2.
\]
The unique containing quadric is the smooth surface \(Q=(q=0)\), \(q=x_0x_3-x_1x_2\), and \(C\) has class \((1,3)\), up to interchanging rulings. These geometric inputs, not the abstract rational curve alone, are essential.

## 1. A common numerical reduction

Assume a hypothetical pair exists. It has no common surface factor, so \(Z=V(F,G)\) is a pure Gorenstein complete-intersection curve of degree sixteen with
\[
\omega_Z=\mathcal O_Z(4),\qquad m_C(Z)=4.
\]
Purity excludes additional isolated support; sole support and degree give the transverse length four.

**The order-two lemma.** One has \(H^0(\mathcal I_C^2(4))=kq^2\). Indeed, the restriction of an order-two quartic to \(Q\) lies in
\(H^0(\mathcal O_Q((4,4)-2(1,3)))=0\). Write it as \(qH\); its first symbol is \(H|_C\) times the nonzero first symbol of \(q\). Thus \(H\) is a quadric through \(C\), hence a scalar multiple of \(q\). Generic order at least two implies everywhere order at least two since the lower normal symbols are sections of vector bundles on the smooth curve.

No nonzero member of the hypothetical pencil can be \(q^2\): a mate without the factor \(q\) cuts a divisor of class \((4,4)\) on \(Q\), which cannot be supported on a curve of class \((1,3)\); a mate with that factor gives a common surface. Thus every nonzero pencil member has generic normal order one. The first symbols of \(F,G\) are dependent over \(k(C)\), since independent symbols would give length one. The generic transverse algebra is consequently \(k(C)[y]/(y^4)\).

Let \(N_i\) be the saturated nilpotent-power filtration on \(\mathcal O_Z\): locally, with \(B\) finite flat over a curve-parameter DVR \(R\),
\[
N_i=B\cap(y^i)B_{k(C)},\quad N_0=B,\quad N_4=0.
\]
The quotients \(E_i=N_i/N_{i+1}\) are line bundles. Put \(L=E_1\). The quotient \(E\twoheadrightarrow L\) implies \(L=\mathcal O(e-7)\), \(e\ge0\). Duality and the perfect saturated multiplication pairing proved below give
\[
E_3=\operatorname{Ann}_{\mathcal O_Z}(I_C\mathcal O_Z)
=\omega_C\otimes(\omega_Z|_C)^{-1}=\mathcal O(-18),
\]
\[
E_2=L^2(D),\qquad E_3=L^3(D),\qquad D\ge0.
\tag{1}
\]
Hence \(\deg D=3-3e\), and only two types survive:

| Type | \(L\) | \(\deg D\) | Meaning |
| --- | --- | --- | --- |
| \(e=0\) | \(\mathcal O(-7)\) | 3 | nonprimitive points are allowed |
| \(e=1\) | \(\mathcal O(-6)\) | 0 | globally primitive |

Generic order one does not imply global primitiveness; omitting the first row would invalidate an exclusion.

## 2. Rank-four Gorenstein algebra and the fixed divisor

This local argument applies to any smooth supported curve with generic curvilinear length four in a smooth threefold, under the complete-intersection hypothesis and with two invertible. It is not specific to the chosen monomial coordinates.

Complete at a point of the support, choose a lift of a parameter \(t\), and put \(R=k[[t]]\). The completed algebra \(B\) is finite over \(R\) because its special fiber is Artinian; the parameter is a nonzerodivisor by Cohen--Macaulayness. Thus \(B\) is free of rank four. This local coefficient ring does not assert a global retraction to \(C\).

Choose a saturated basis \(1,y,x,z\), of respective filtration weights \(0,1,2,3\), and write \(yx=cz\). All products of weight at least four vanish. A relative Frobenius functional \(\lambda:B\to R\) exists because \(B\) is finite flat Gorenstein. The determinant of its multiplication-pairing matrix is
\[
c^2\lambda(z)^4.
\]
It is a unit. Thus \(c\) is a unit, proving that \(E_1E_2\to E_3\) is perfect, including at defects. Take \(z=xy\) and write \(y^2=a(t)x+b(t)xy\). Replacing \(y\) by \(y-bx/2\) yields
\[
B=R[x,y]/(x^2,y^2-a(t)x),\qquad \operatorname{ord}_t(a)=d_p:=\operatorname{mult}_pD.
\tag{2}
\]
The four displayed basis elements prove this is an algebra isomorphism, not merely a list of relations. They also prove (1): the zero divisor of \(L^2\to E_2\) is exactly \(D\), while \(L E_2\to E_3\) is perfect.

If \(d_p>0\), the images of \(t,x,y\) are independent modulo the square of the maximal ideal. Their lifts are regular ambient parameters; the ambient completed ideal is exactly
\[
I_Z=(x^2,y^2-a(t)x)\subset k[[t,x,y]].
\tag{3}
\]
Indeed the surjection from this power-series quotient sends its free \(R\)-basis to a basis of \(B\). If \(d_p=0\), eliminate \(x\) instead: the ambient ideal is \((m,l^4)\). Applying the two-parameter defect model at a primitive point would be incorrect.

Let \(M=\ker(E\twoheadrightarrow L)=\mathcal O(-7-e)\). The actual first symbols of \(F,G\) are \(h_F,h_G\in H^0(M(16))\). Their common divisor is **exactly** \(D\). At a defect, express the actual generators \(F,G\) in the minimal generators of (3). The coefficient matrix is invertible. Their first symbols are the coefficients of \(y^2-ax\), restricted to \(C\), times \(-a\bar x\); these coefficients generate the unit ideal. The common vanishing order is therefore \(d_p\). At a primitive point the same argument with \((m,l^4)\) gives no common zero.

Removing \(D\) gives a basepoint-free pencil in
\[
M(16)(-D)=\mathcal O(n),\qquad n=6+2e.
\tag{4}
\]
Because \(n>0\), the two sections cannot be proportional. The induced morphism \(C\to\mathbf P^1\) is separable in characteristic zero. A general member therefore has \(n\) distinct zeros, avoiding the finite defect support. This uses the pencil supplied by the hypothetical equations, not surjectivity of an arbitrary jet map.

## 3. From the marked neighborhood to surface equations

Take a general quartic \(S=V(\alpha F+\beta G)\). Bertini gives smoothness off \(C\), the reduced base locus. At a primitive point use \(I_Z=(m,l^4)\). At a simple moving zero from (4), take another pencil member with unit \(m\)-coefficient as the parameter \(m\). The selected equation has form
\[
A(t,m,l)m+U(t,m,l)l^4,
\quad U(0)\ne0,\quad A_t(0)\ne0.
\]
The invertible change \(T=A/U\) identifies this germ, up to a unit, with \(Tm+l^4\). Thus there are \(n\) moving germs of the form \(uv-t^4\).

At a defect of multiplicity \(d=d_p\), a general member has equation
\[
\alpha(t,x,y)x^2+\beta(t,x,y)(y^2-a(t)x),
\qquad \alpha(0)\beta(0)\ne0.
\]
The generality assertion follows from the invertible generator matrix at each of finitely many defects. Divide by \(\beta\), and put \(u=\alpha/\beta\). The Hessian of \(ux^2+y^2-ax\) in \(x,y\) is invertible. Its critical point over \(k[[t]]\) satisfies
\[
x_c=\frac{a}{2u(t,0,0)}+O(a^2),\quad y_c=O(a^2),\quad
f(t,x_c,y_c)=-\frac{a^2}{4u(t,0,0)}+O(a^3).
\]
The formal Morse lemma with parameter \(t\), followed by extracting a unit root, gives the equation \(uv-t^{2d}\). The order is exactly \(2d\), even when the coefficients depend on all three variables. Since \(\sum d_p\le3\), only exponents \(2,4,6\) occur. These and the moving exponent-four germs are all the singularities; away from their first-symbol zeros \(S\) is smooth on \(C\).

The singular locus is finite. A repeated surface component is singular along that component, and distinct projective surface components meet in a curve where their union is singular. Consequently \(S\) is integral. The hypersurface is Cohen--Macaulay and regular in codimension one, hence normal.

## 4. Direct blowups and the global contradiction

The following calculation supplies the resolution and the exceptional intersection matrix directly. It removes reliance on a classification label.

For \(uv-t^r=0\), \(r\in\{2,4,6\}\), blow up the ambient origin. The \(u\)-chart has equation
\(v_1-u^{r-2}t_1^r=0\) and is smooth; the \(v\)-chart is similar. The \(t\)-chart has equation \(u_1v_1-t^{r-2}=0\). For \(r=2\) the exceptional curve is a smooth conic. For \(r>2\) it is two lines meeting at the unique remaining singular point. Iteration inserts the configuration for exponent \(r-2\) between the two lines: their strict transforms attach at opposite axis directions, so the configuration is a chain. Its component count is
\[
N(2)=1,\quad N(r)=2+N(r-2)=r-1.
\]
All components are smooth rational curves. Each blowup center has surface multiplicity two. The ambient canonical discrepancy \(2E\) is canceled by the strict transform \(\pi^*S-2E\); hypersurface adjunction gives \(K_{S'}=\pi^*K_S\), also at the intermediate Gorenstein surfaces. Completion commutes with these point blowups, and smoothness can be checked after faithful flat completion, so using formal normal forms introduces no algebraization assumption.

The resulting smooth connected projective resolution \(\widetilde S\) has trivial canonical line bundle because a quartic has trivial dualizing sheaf. Adjunction makes every exceptional rational curve have square \(-2\). The chain matrix has diagonal \(-2\), adjacent entries one, and determinant of absolute value \(r\), hence is negative definite. Different points give disjoint chains. Therefore their independent classes have total rank
\[
R=3n+\sum_{p\in\operatorname{Supp}D}(2d_p-1)
=24-\#\operatorname{Supp}D\ge21.
\tag{5}
\]

Here is the precise global input. For a smooth complex projective surface with trivial canonical bundle put \(q_S=h^1(\mathcal O)\). Then \(p_g=1\), \(\chi(\mathcal O)=2-q_S\); Noether's formula and Hodge decomposition give
\[
c_2=12(2-q_S),\quad b_2=22-8q_S,\quad h^{1,1}=20-8q_S\le20.
\tag{6}
\]
The literature being applied is the general surface identities in [Hacking, *583C Lecture notes*](https://paulhacking.github.io/surfaces.pdf), §2 and Theorem 5.4; §6 gives the Hodge index interpretation. Their hypotheses hold for the smooth projective resolution just constructed. The pullback hyperplane class has square four and is orthogonal to the exceptional chains. Its positive square makes it independent of their negative-definite span. Thus \(R+1\le h^{1,1}\le20\), or \(R\le19\), contradicting (5). No classification of K3 surfaces or of their singularities is needed.

For an arbitrary algebraically closed characteristic-zero field, descend the equations to the algebraic closure of a finitely generated coefficient field and embed that field into \(\mathbf C\). Sole reduced support descends by faithful flatness. Construct a general pencil member and its finite resolution over this subfield; the normal forms, smoothness and intersection matrices persist under algebraically closed base extension. The complex contradiction applies without an embedding of the whole original field into \(\mathbf C\).

### The K3 presentation of the same surface mechanism

The equations \(uv-t^r\) are the rational double points \(A_{r-1}\). A quartic with only these singularities has a K3 resolution, and in characteristic zero its Picard rank is at most twenty. The exceptional rank (5) already contradicts this weaker bound; including the hyperplane gives nineteen. [Morrison, *The Geometry of K3 Surfaces*](https://web.math.ucsb.edu/~drm/conferences/ITP99/morrison/cortona.pdf), printed pp. 5–6, supplies the local forms, exceptional chains, and K3 interpretation. Here integrality, normality and the complete list of singularities were verified in §3 before applying that interpretation.

This is a useful alternate presentation of the surface proof, not a third independent obstruction. Direct blowups replace its singularity-classification input, while (6) replaces identification of the surface type. Both still use a global surface bound. Neither is a proof using only the abstract curve, or only a finite neighborhood of it.

### A reusable rank-four pencil budget

The proof separates a general implication from the fixed embedding. If a complete-intersection pencil of quartics has smooth sole support, generic curvilinear length four, saturated data \(L,E_2=L^2(D),E_3=L^3(D)\), and a separable basepoint-free first-symbol pencil of positive degree \(n\) after removing its exact fixed divisor \(D\), the same local calculations force
\[
3n+2\deg D-\#\operatorname{Supp}D\le19.
\tag{7}
\]
For arbitrary \(d_p\), the direct-blowup induction works for every even exponent \(2d_p\). This conditional budget uses no balanced splitting or rational parameterization of the support. Those special inputs are used here to obtain \(n=6+2e\), \(\deg D=3-3e\), violating (7). It is a necessary condition, not a criterion constructing a pencil, and is a consolidation deduction requiring review at precisely these hypotheses.

## 5. The distinct proof through filtered contact

This route avoids the global surface bound. It instead uses the nonlinear chart transitions of the embedding and exact spaces of homogeneous equations. The matrices and polynomial identities specified below are retained as exact computational support; their ranks alone do not prove orbit exhaustion.

At the generic point, write a triple in normal parameters as \(m=f_2 l^2\) modulo \(l^3\), and expand
\[
H=h_Hm+k_Hl^2+e_Hml+c_Hl^3+O_{\mathrm{wt}}(4).
\]
Here the remainder has weighted order at least four for weights \(\operatorname{wt}(m)=2,\operatorname{wt}(l)=1\); in particular omitted terms such as \(m^2\) become order at least four after the triple substitution. Containing the triple means \(k_H+h_Hf_2=0\). After replacing \(m\) by \(m-f_2l^2\), the cubic coefficient is \(\tau_H=c_H+e_Hf_2\). Thus for two independent equations
\[
\Delta=h_0\tau_1-h_1\tau_0\ne0
\quad\Longrightarrow\quad m_C(V(H_0,H_1))=3.
\tag{8}
\]
To prove (8), eliminate the normal parameter with nonzero first coefficient; the other relation is a unit times \(l^3\) modulo higher powers. Changing the pencil basis scales \(\Delta\) by a nonzero constant, so this excludes every independent pair in that pencil.

### The \(e=0\) triples and their complete quartic sources

On \(x_0=1\) use
\[
z=x_1,\quad V=x_2-z^3,\quad U=x_3-z^4-\tfrac32zV.
\]
A quotient \(E\twoheadrightarrow\mathcal O(-7)\) is constant in this balanced frame. Its direction is \(U=-\theta l,V=l\), or \(U=l,V=0\). The actual projective torus preserving \(C\) acts by \((z,U,V)\mapsto(\lambda z,\lambda^4U,\lambda^3V)\); thus the quotient directions have three orbits \(\theta=0,1,\infty\). This is not an arbitrary conormal-frame automorphism.

The opposite chart has
\[
W=x_2/x_3,\quad a=x_1/x_3-W^3,\quad b=x_0/x_3-W^4,
\quad U'=a/2,\quad V'=-3Wa+2b.
\tag{9}
\]
Its quadratic transition cocycles for the three directions are
\[
h_1=3z^{-5}-\tfrac32z^{-4}+\tfrac34z^{-3}-\tfrac38z^{-2},
\quad h_0=-\tfrac38z^{-2},\quad h_\infty=3z^{-5}.
\]
An allowed defect section \(\delta\in H^0(\mathcal O(3))\) must kill this class under multiplication \(H^1(\mathcal O(-7))\to H^1(\mathcal O(-4))\). There are no free regular corrections, since \(H^0(\operatorname{Hom}(M,L^2(D)))=H^0(\mathcal O(-4))=0\). It suffices to allow all annihilators, even if some do not produce pure triples.

For \(\theta=1\), the matrix on \(\delta=\sum_{j=0}^3d_jz^j\), taking coefficients of \(z^{-1},z^{-2},z^{-3}\), is
\[
\begin{pmatrix}0&-3/8&3/4&-3/2\\-3/8&3/4&-3/2&3\\3/4&-3/2&3&0\end{pmatrix}.
\]
Its kernel is \(k(0,2,1,0)\), so \(\delta=z(z+2)\) as a degree-three section, including its zero at infinity. Since \(\delta h_1=-3/8+6z^{-4}\), the generic triple is \(m=\gamma l^2/\delta\) with \(m=U+V\), \(\gamma=3/8\). Containment of an ambient quartic is exactly
\[
H|_C=0,\quad [l]H|_{U=-l,V=l}=0,\quad
\delta[l^2]H|_{U=-l,V=l}+\gamma[U]H=0.
\tag{10}
\]
These equations, expanded in all thirty-five quartic monomials, have rank thirty-three. A full kernel basis is obtained by putting
\[
A=x_0^2x_2-x_1^3,\quad B=x_0x_2^2-x_1^2x_3,\quad D_0=x_2^3-x_1x_3^2
\]
and taking
\[
\begin{split}
F_0={}&-(x_2+x_3)(16A+(16x_0+8x_1)q)+(4x_2+x_3)B-x_2^2q,\\
F_1={}&x_2D_0-256x_1A-4q(64x_0x_1+16x_0x_2+4x_0x_3+32x_1^2\\
&\hspace{38mm}+4x_1x_2+4x_1x_3+2x_2^2+x_2x_3).
\end{split}
\]
In \(U=m-l,V=l\), their first and cubic coefficients are
\[
\begin{split}
h_0&=-2z^3(z+2)^3,&\tau_0&=-(z+4)/8,\\
h_1&=-2z(z+2)(z^2+4)(z^4+16),&
\tau_1&=-\frac{z^5+2z^4+16z^2-16z+96}{8z(z+2)}.
\end{split}
\]
Thus \(\Delta=32z(z-2)(z+2)\ne0\), excluding the open orbit by (8).

For \(\theta=0\), all annihilators are \(z^2(a+bz)\), with correction \(\gamma=3(a+bz)/8\). The common factor cancels from the containment equations, whose full quartic solution is \(D_0H^0(\mathcal O_{\mathbf P^3}(1))\). At infinity the annihilators are \(a+bz\); the same calculation gives \(AH^0(\mathcal O_{\mathbf P^3}(1))\). Every pair in either space has a common cubic factor. This excludes both endpoint orbits.

### The \(e=1\) primitive directions

Write the direction as \(U=A(z)y,V=B(z)y\) with \(A=a_0+a_1z\), \(B=b_0+b_1z\), \(a_0b_1-a_1b_0\ne0\). The determinant condition is precisely basepoint freedom on \(\mathbf P^1\). Substitution in (9), including the changed support coordinate \(W\), gives the quadratic cocycle
\[
h_2=-\frac{(2A+zB)(12A^2+3z^2B^2+4z^2(A_zB-AB_z))}{8z^5}.
\]
Its \(z^{-1},z^{-2},z^{-3}\) coefficients vanish exactly when
\[
b_1P=0,\qquad(2a_1+b_0)Q=0,\qquad a_0R=0,
\tag{11}
\]
where, with \(p=a_0b_1,c=a_1,d=b_0\),
\[
P=2p+12c^2+16cd+9d^2,\quad
Q=8p+12c^2+4cd+3d^2,\quad
R=2p+36c^2+16cd+3d^2.
\]
If \(p\ne0\), then \(P=R=0\) and \(R-P=6(2c-d)(2c+d)\). The choice \(c=d/2\) forces \(p=-10d^2\), and the middle equation then forces \(d=0\), a contradiction. Thus \(c=-d/2\), \(p=-2d^2\), \(d\ne0\). Quotient scaling and the actual ambient torus normalize this single orbit to \(A=1+z,B=-2-8z\).

If \(a_0\ne0,b_1=0\), basepoint freedom implies \(cd\ne0\). The choice \(2c+d=0\) makes \(R=4d^2\ne0\); otherwise \(Q=R=0\), whereas \(R-3Q=4d(c-3d/2)\) and \(Q|_{c=3d/2}=36d^2\), impossible. If \(a_0=0,b_1\ne0\), the same two alternatives use \(P=4d^2\) or \(P-Q=6d(2c+d)\), again impossible. Finally \(a_0=b_1=0\) gives, after scaling, \(A=rz,B=1\) with
\[
(2r+1)(12r^2+4r+3)=0.
\]
These are exactly four actual torus orbits. The correction is unique because \(H^0(\operatorname{Hom}(\mathcal O(-8),\mathcal O(-12)))=0\).

For each direction, complete quartic containment is an exact finite linear problem: choose \(S,T\) with \(SA+TB=1\); in \(m=BU-AV\), \(y=SU+TV\), a triple \(m=-\gamma y^2\) is parametrized by
\[
U=Ay-T\gamma y^2,\qquad V=By+S\gamma y^2.
\tag{12}
\]
Set the coefficients of \(1,y,y^2\) in each ambient quartic to zero. The complete thirty-five-column matrix, rather than an assumed subfamily of quartics, is used.

For the principal direction \(S=4/3,T=1/6,\gamma=192z+96\), that matrix has rank thirty-three. The two explicit homogeneous kernel vectors \(P_0,P_1\) are defined in the retained [primitive-triple verifier](../computations/audit_mf6_e1_primitive_2026_10_07.py) as `F0,F1`. This is a necessary computational dependency of this proof route. Direct expansion gives, in its convention \(T_H=-\tau_H\),
\[
h_{P_0}T_{P_1}-h_{P_1}T_{P_0}
=\frac{(2z-1)^3(2z+1)(4z^2+2z+1)}{256}\ne0.
\]
For \(r=-1/2\), (12) has rank twenty-five and complete kernel \(qH^0(\mathcal O(2))\), inadmissible by the quadric divisor argument. For either root of \(12r^2+4r+3\), \(\gamma=0\), and the matrix has rank thirty-three over the exact quadratic field. A complete kernel basis is
\[
\begin{split}
R_0&=x_0^3x_3-(r+3/2)x_0^2x_1x_2+(r+1/2)x_1^4,\\
R_1&=x_0x_3^3+(r-7/6)x_1x_2x_3^2+(1/6-r)x_2^4.
\end{split}
\]
Its coefficients are \(h_{R_0}=1,T_{R_0}=0\), \(h_{R_1}=(2r+2/3)z^8,T_{R_1}=(8r/9)z^3\). The determinant is nonzero for both roots. This exhausts (11), proves length three for every independent pair in the nonfactored pencils, and completes the filtered-contact proof.

The exact finite rank/kernel assertions and contact identities are supported by [the complete-source calculation](../computations/verify_44_filtered_contact_2026_10_23.py), [the independent Taylor calculation](../computations/audit_44_filtered_contact_2026_10_23.py), and [the primitive-direction calculation](../computations/audit_mf6_e1_primitive_2026_10_07.py). The last script also contains all-degree arguments beyond the assertions used here. The geometric and cohomological reductions above supply coverage; script success alone does not. These inherited calculations need not be rerun to use the separate surface proof.

## 6. What a neighborhood-only proof still needs

The module lemma, determinant construction, transformation laws and generic two-blowup criterion in this section have wider scope: let a smooth curve \(C\) lie in a smooth threefold over any algebraically closed field, and let \(T\) be a pure quasiprimitive triple with a surjective conormal quotient \(E\twoheadrightarrow L\) and saturated second layer \(E_2=L^2(D)\). They work in every characteristic; no Gorenstein hypothesis on the triple is needed. For a general hypersurface line bundle \(A\), replace the twists \((16)\) by tensoring with \(A|_C\), and \((32)\) by \((A|_C)^2\). The numerical target degrees and the assertion about actual quartic-source nonvanishing specialize to the fixed characteristic-zero embedding.

There is an intrinsic target for (8), relative to the **embedded triple**, not the abstract curve. Let \(T\) be an allowed triple with ideal \(J\), and define
\[
\mathcal M_T=(J/I_CJ)/\operatorname{tors}_C.
\]
For its saturated data \(L,E_2=L^2(D)\), and \(M=\ker(E\to L)\), there is an exact sequence
\[
0\to L E_2\to\mathcal M_T\to M(-D)\to0,
\quad \det\mathcal M_T=\det(E)L^2.
\tag{13}
\]
At a defect, lift a generator of the first saturated layer to \(x\), and a generator of the second to \(y\). Since the embedding generates the triple algebra and the first generator has square zero in the defect fiber, the second ambient normal parameter must supply \(y\). Saturated weights give \(x^2=ay\), \(xy=y^2=0\); the rank-three basis \(1,x,y\) proves that the exact ambient completed ideal is \(J=(x^2-ay,xy,y^2)\). Independence of the two normal parameters in the defect fiber ensures their ambient validity, as in the rank-four argument. Its Hilbert--Burch relations are
\(y(x^2-ay)-x(xy)+ay^2=0\), \(y(xy)-xy^2=0\). Modulo \(I_CJ\), the only relation is \(a[y^2]=0\); removing torsion leaves the free generators \([x^2-ay],[xy]\). Their first-symbol image is \(M(-D)\), and the kernel has transition \(L E_2\). This identification is canonical: multiply lifts of a first-layer and a second-layer section. Changing either lift by \(J\) adds an element of \(I_CJ\); changing the first-layer lift by a second-layer lift adds a product represented by \(y^2\), which is torsion and disappears in \(\mathcal M_T\). At primitive points use \(J=(m,l^3)\). These computations prove (13) and explain why its determinant loses the defect divisor even though its extension class retains embedded information.

An actual two-dimensional source \(W\subset H^0(\mathcal I_T(4))\) induces
\[
\rho_T:W\otimes\mathcal O_C\to\mathcal M_T(16),\quad
\det\rho_T\in H^0(\det(W)^*\otimes\det(E)L^2(32)).
\tag{14}
\]
The line has degree four for \(e=0\), six for \(e=1\). Generically the matrix is exactly \((h_i,\tau_i)\). With a nonzero first symbol and contact at least three, nonvanishing is equivalent to generic intersection length three. Adapted target changes scale its local expression by a unit; changing the triple's fourth lift adds a multiple of \(h_i\) to \(\tau_i\) and leaves the determinant unchanged. Thus this is a geometric section, not a coordinate-dependent numerical test.

For clarity, the exact adapted-basis law at the generic point is
\[
n'=an+bl^3,\qquad (l')^3=d^3l^3\pmod{I_CJ},\qquad
h_i'=h_i/a,\quad \tau_i'=(\tau_i-bh_i/a)/d^3,\quad
\Delta'=\Delta/(ad^3).
\tag{16}
\]
Here \(a,d\in k(C)^\times\); the factor is the transition of the determinant line, not an assertion that a chosen polynomial is invariant. A source-basis change multiplies \(\Delta\) by its determinant. Replacing \(n\) by \(n-rl^3\) keeps the triple ideal fixed and adds \(rh_i\) to \(\tau_i\), leaving the wedge unchanged. Changing \(f_2\) itself changes the embedded triple and the quartic containment conditions.

There is also a geometric interpretation in the generic normal slice \(k(C)[[m,l]]\). Choose a pencil basis with both first coefficients nonzero. Blow up the origin using \(m=lm_1\), then its common infinitely near point using \(m_1=lm_2\). At \(u=m_2-f_2\), the twice-transformed equations are
\[
H_i/l^2=h_i u+\tau_i l+\text{terms in }(u,l)^2.
\]
Thus \(\Delta\) is the wedge of their tangent covectors. Its nonvanishing means transverse intersection at the second infinitely near point; the successive contributions are \(1,1,1\), giving length three. Algebraically, solve one equation for \(n=m-f_2l^2\); the other has leading coefficient \(\Delta/h_0\) at \(l^3\). For finite colength and the stated nonzero first symbol,
\[
\Delta\ne0\iff\operatorname{length}=3,\qquad
\Delta=0\iff\operatorname{length}\ge4.
\]
Vanishing does not specify length exactly four or a global fourth extension. The formal local pair \((n,n+l^4)\) has zero determinant and length four, showing directly that formal contact compatibility is possible. It is not a pair of actual global quartics on the fixed embedding. The blowup charts are valid off the triple's defect divisor; poles of \(f_2\) can prevent their extension over a defect, whereas the module map (14) remains defined there. No exceptional vertical locus in these blowups is being identified with a residual component downstairs.

With weights \(\operatorname{wt}(n)=3,\operatorname{wt}(l)=1\), the displayed leading forms are \(h_i n+\tau_i l^3\). A nonzero determinant makes them generate \((n,l^3)\). If they align, their cancellation must be continued: after solving one equation exactly, the **full** initial ideal is \((n_0,l^r)\), where \(r\) is the actual generic length. The separate leading forms do not determine it. A scalar ideal valuation can give the same minimum on \((n,l^3)\) and \((n,l^4)\); the determinant records independence in a residue graded piece and therefore retains coefficient data beyond the minimum value. The contact module, transformation laws and two-blowup interpretation themselves involve no division by two and apply over any coefficient field; characteristic enters through the allowed embedded triples and actual global source.

**Missing implication.** Prove nonvanishing of (14) for every proper actual quartic source in the two allowed types directly from the embedded transition data, without enumerating (10)--(12) and without the surface bound. The target construction does not prove this. Positive determinant degree is insufficient: in abstract models \(\mathcal M_T(16)=\mathcal O(2)^2\) or \(\mathcal O(3)^2\), two independent global sections can both lie in one summand and have zero wedge. They can even have the required exact-sequence shapes
\[
0\to\mathcal O(-2)\to\mathcal O(2)^2\to\mathcal O(6)\to0,
\qquad
0\to\mathcal O(-2)\to\mathcal O(3)^2\to\mathcal O(8)\to0,
\]
by using pairs of degree-four or degree-five polynomials without common zero for the respective left maps. These examples are not asserted to arise from the actual quartic embedding. They show why actual-source realizability must enter the proof.

For the primitive branch there is a second necessary condition. Three successive blowups along \(C\) and the prescribed direction sections leave a reduced base curve \(C_3\simeq C\). The successive transformed quartic restrictions have degrees \(10,4,-2\). The normal sequences have degree pairs \((2,6),(-4,6),(-10,6)\); finally
\[
0\to\mathcal O(-10)\to N_{C_3/X_3}\to\mathcal O(6)\to0.
\tag{15}
\]
Two actual generators of the remaining center ideal would force \(N_{C_3/X_3}=\mathcal O(-2)^2\). This balanced middle bundle is compatible with (15); degrees alone do not exclude it. Showing that the actual extension cannot have this splitting would obstruct the primitive branch, while the defective branch would still need treatment. It is a necessary condition, not an equivalence to global realization.

## 7. Controls and geometric limits

**A genuine quadruple with the right lower invariants.** On \(Q\), let \(Y=4C\). It has degree sixteen, arithmetic genus thirty-three and primitive layers \(\mathcal O,\mathcal O(-6),\mathcal O(-12),\mathcal O(-18)\), exactly matching the primitive numerical type. Yet
\(H^0(\mathcal I_Y(4))=qH^0(\mathcal O(2))\), because \((4,4)-4(1,3)=(0,-8)\) has no sections. Thus lower layer data and the Hilbert polynomial do not characterize an actual quartic complete intersection.

The full adjunction discrepancy detects more: \(\omega_Y\otimes\mathcal O_Y(-4)=\mathcal O_Q(-2,6)|_Y\). This restricts trivially to \(C\), but not even to \(2C\). Indeed with \(M_Q=\mathcal O_Q(-2,6)\), the sequence
\[
0\to\mathcal O_Q(-4,0)\xrightarrow{c_C^2}M_Q\to M_Q|_{2C}\to0
\]
identifies \(H^0(M_Q|_{2C})\) with the kernel of a map whose source has dimension three. If \(c_C=ad^3-bc^3\) in Segre coordinates, its images in Cech bases are \(d^6,-2c^3d^3,c^6\), independent in characteristic zero. Thus that kernel vanishes; a trivial line bundle would have a nonzero section. The essential data can live in line-bundle gluing beyond the reduced curve. This does not put an arbitrary candidate quadruple inside \(Q\).

**Identical quadric restrictions, different transverse lengths.** Put \(F=x_1^4-x_0^3x_3\), \(G=x_2^4-x_0x_3^3\). For the conjugate pair above, write \(a=r+3/2,b=r+1/2,c=1/6-r,d=r-7/6\). Then
\[
R_0=bF+ax_0^2q,\qquad R_1=cG-dx_3^2q.
\]
Their restricted pencils on \(Q\) agree up to nonzero basis scalars. In characteristic zero, however, \((F,G)\) has length one along \(C\), while \((R_0,R_1)\) has length three by (8). Restricting to \(Q\) forgets normal lifting data.

The latter is an actual residual example, not a formal model. On \(x_0=1\), set \(x_1=z,x_2=pz^3,x_3=q'z^4\). Eliminating \(q'=ap-b\) gives
\[
(ap-b)^3+(r-7/6)p(ap-b)^2+cp^4=(p-1)^3(cp+b^3).
\]
The simple residual root is \(\kappa=(2r-3)/(18r-3)\), with \(27\kappa^2-14\kappa+3=0\), \(\kappa\ne0,1\). It yields
\[
[V(R_0,R_1)]=3[C]+[C_\kappa],\quad
C_\kappa=[s^4:s^3t:\kappa st^3:-(\kappa/3)t^4].
\]
Properness follows since \(R_0\), primitive and linear in \(x_3\), is irreducible, and \(R_1\) is not proportional to it. The identified cycles exhaust degree sixteen; purity excludes further support. A general member has eight moving germs \(uv-t^3\), giving exceptional rank sixteen rather than twenty-four. This explains why the surface budget specifically obstructs length four and is compatible with residual length-three geometry. The [exact residual-example verifier](../computations/verify_44_triple_residual_example_2026_10_26.py) checks the polynomial factorization; properness and degree supply the global argument.

**Characteristic boundary.** The characteristic-two pair \(F,G\) has local ideal \((U,V^4)\) and sole support \(C\); in characteristic zero the same displayed pair has further reduced components. The conormal splitting changes in characteristic two, local simplification used division by two, and a positive-characteristic pencil map can be inseparable. Consequently neither the eight-simple-zero count nor the characteristic-zero surface bound applies unchanged. This is an actual existence construction at the different characteristic, not a contradiction to R-0022.

## 8. Dependencies and the open bridge

The direct-resolution proof uses R-0020, the smooth-quadric geometry, complete-intersection duality, the rank-four Frobenius calculation in §2, Bertini and formal coordinate changes in §3, explicit point blowups, and the verified surface identities in (6). It uses no inherited orbit classification, no all-degree carrier theorem, and no computer calculation. The K3 presentation replaces the last two geometric arguments by the literature on rational double points and K3 resolutions; it has the same local input and the same scope.

The filtered-contact route additionally depends on the exact complete-source matrices and their retained scripts. Its orbit exhaustion and correction uniqueness are proved in §5. The module construction in §6 is a reusable interpretation, not an independent proof of the needed nonvanishing. The quadric quadruple and residual examples explain which tempting numerical or restriction-only strengthenings fail.

The common mechanism is **actual-source compatibility across successive layers**: the first symbols leave a rank-one direction, Gorenstein duality constrains its defects, and the next equations must lift through the marked embedding. The filtered route measures the failure as a nonzero cubic-contact determinant; the surface route converts the same hypothetical fourth-layer compatibility into an excessive exceptional configuration. This is a proved parallel of consequences of a hypothetical pair, not an asserted equality of the two obstruction classes. Neither mechanism has been shown here to cover arbitrary higher degrees.
