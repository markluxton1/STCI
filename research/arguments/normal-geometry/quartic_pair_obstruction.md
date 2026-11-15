# The quartic-pair obstruction: local algebra, global surfaces, and actual equations

Let (k) be algebraically closed of characteristic zero and fix
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]
There are no homogeneous quartics (F,G) with (V(F,G)_{\rm red}=C), including reducible and nonreduced defining equations. This is the scope of [R-0022](../../results/quartic_44_filtered_exclusion.md). It is narrower than the [all-mate-degree quartic-carrier theorem R-0001](../../results/quartic_carrier_exclusion.md), which is not an input to any proof here. The unrestricted characteristic-zero STCI question remains open.

There are three completed mechanisms. The [intrinsic fourth-extension proof](intrinsic_fourth_extension.md) classifies the embedded quadruples of the two allowed saturated types through their contact-extension classes; the only survivor is 4C on the containing quadric, which cannot lie in a proper quartic pair. The filtered-contact proof instead tests the complete vector spaces of quartic equations through possible triples. The surface proof turns the first-symbol pencil and its defects into too many exceptional curves on a resolved quartic; its direct-blowup presentation avoids surface-singularity classification. The intrinsic proof uses explicit embedded transition calculations but no ambient quartic source matrices or global surface bound.

Throughout, \(\mathcal O(j)\) means degree \(j\) on \(C\simeq\mathbf P^1\); ambient \(\mathcal O_C(a)=\mathcal O(4a)\). The embedding-specific input is the [balanced conormal R-0020](../../results/quartic_conormal_characteristic_jump.md),
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

For the principal direction \(S=4/3,T=1/6,\gamma=192z+96\), that matrix has rank thirty-three. The two explicit homogeneous kernel vectors \(P_0,P_1\) are defined in the retained [primitive-triple verifier](../../computations/audit_mf6_e1_primitive_2026_10_07.py) as `F0,F1`. This is a necessary computational dependency of this proof route. Direct expansion gives, in its convention \(T_H=-\tau_H\),
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

The exact finite rank/kernel assertions and contact identities are supported by [the complete-source calculation](../../computations/verify_44_filtered_contact_2026_10_23.py), [the independent Taylor calculation](https://github.com/markluxton1/STCI/blob/f2f5c4dbe5bef0eeb5112d402ffeb513133b43bc/research/computations/audit_44_filtered_contact_2026_10_23.py), and [the primitive-direction calculation](../../computations/audit_mf6_e1_primitive_2026_10_07.py). The last script also contains all-degree arguments beyond the assertions used here. The geometric and cohomological reductions above supply coverage; script success alone does not. These inherited calculations need not be rerun to use the separate surface proof.

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

**Intrinsic resolution for the allowed quartic types.** The [fourth-extension proof](intrinsic_fourth_extension.md) now supplies the embedded-transition argument. A determinant-zero pencil generating the quotient line forces this contact extension to split. Its class never vanishes in the defective type, and in the primitive type it vanishes only for 3C on Q, whose unique equal-defect fourth extension is 4C on Q. Every containing quartic then has the factor q. Thus a proper quartic pair is excluded without enumerating its source matrices or using the surface bound. The target-module construction alone still proves no general nonvanishing theorem. Positive determinant degree is insufficient: in abstract models \(\mathcal M_T(16)=\mathcal O(2)^2\) or \(\mathcal O(3)^2\), two independent global sections can both lie in one summand and have zero wedge. They can even have the required exact-sequence shapes
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
Two actual generators of the remaining center ideal would force \(N_{C_3/X_3}=\mathcal O(-2)^2\). This balanced middle bundle is compatible with (15); degrees alone do not exclude it. This normal-bundle condition remains necessary rather than equivalent to global realization. The fourth-extension classification above settles the actual quartic-pair problem by a different intrinsic contact-extension calculation, covering both primitive and defective types without asserting that numerical degrees exclude this middle-bundle splitting.

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
Properness follows since \(R_0\), primitive and linear in \(x_3\), is irreducible, and \(R_1\) is not proportional to it. The identified cycles exhaust degree sixteen; purity excludes further support. A general member has eight moving germs \(uv-t^3\), giving exceptional rank sixteen rather than twenty-four. This explains why the surface budget specifically obstructs length four and is compatible with residual length-three geometry. The historical exact residual-example computation checked the polynomial factorization, the endpoint intersection lengths (three at each endpoint), and the nowhere-zero first-symbol vector; properness and degree supply the global argument. In the quadratic field defined by 12r^2+4r+3=0, its first-symbol pencil is grad(R0)=s^8 v and grad(R1)=(2r+2/3)t^8 v, with v=(-2r t^4,(-a+4b)s t^3,-a s^3 t,s^4), nowhere zero. A general member has eight simple first-symbol zeros. These finite identities do not themselves prove the global cycle decomposition.

**Characteristic boundary.** The characteristic-two pair \(F,G\) has local ideal \((U,V^4)\) and sole support \(C\); in characteristic zero the same displayed pair has further reduced components. The conormal splitting changes in characteristic two, local simplification used division by two, and a positive-characteristic pencil map can be inseparable. Consequently neither the eight-simple-zero count nor the characteristic-zero surface bound applies unchanged. This is an actual existence construction at the different characteristic, not a contradiction to R-0022.

## 8. Dependencies and the open bridge

The direct-resolution proof uses R-0020, the smooth-quadric geometry, complete-intersection duality, the rank-four Frobenius calculation in §2, Bertini and formal coordinate changes in §3, explicit point blowups, and the verified surface identities in (6). It uses no inherited orbit classification, no all-degree carrier theorem, and no computer calculation. The K3 presentation replaces the last two geometric arguments by the literature on rational double points and K3 resolutions; it has the same local input and the same scope.

The filtered-contact route additionally depends on the exact complete-source matrices and their retained scripts. Its orbit exhaustion and correction uniqueness are proved in §5. The module construction in §6 is a reusable interpretation, not an independent proof of the needed nonvanishing. The quadric quadruple and residual examples explain which tempting numerical or restriction-only strengthenings fail.

The common mechanism is **actual-source compatibility across successive layers**: the first symbols leave a rank-one direction, Gorenstein duality constrains its defects, and the next equations must lift through the marked embedding. The filtered route measures the failure as a nonzero cubic-contact determinant; the surface route converts the same hypothetical fourth-layer compatibility into an excessive exceptional configuration. This is a proved parallel of consequences of a hypothetical pair, not an asserted equality of the two obstruction classes. Neither mechanism has been shown here to cover arbitrary higher degrees.

The embedded-neighborhood argument has its own [complete proof and reviewed scope](intrinsic_fourth_extension.md). It adds a third mechanism for the same fixed characteristic-zero quartic-pair exclusion; the filtered-contact and surface proofs remain useful alternative arguments.


## Consolidated historical supplement: `research/supplements/INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md`

# INTRINSIC 44 MULTIPLICITY AND GENUS BUDGETS

## Cross-supplement synthesis: distinct (4,4) obstruction routes (editorial, not a new audit)

The historical material contains several arguments with different inputs and different logical targets. They should not be conflated:

| Route | Retained location | What it supplies | Limitation |
| --- | --- | --- | --- |
| Filtered quartic-contact calculation | [Filtered proposal and independent audit](https://github.com/markluxton1/STCI/blob/ca33958696fdc4f06a1c39b160aa13d097f24146/research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd) | A classification- and calculation-dependent route through the two saturated numerical types and actual cubic-contact constraints | Its computational exhaustiveness and inherited hypotheses remain attached to the original audit; this synopsis is not an independent rerun |
| First-symbol pencil and surface singularities | [Intrinsic K3 proposal](#4-direct-blowups-and-the-global-contradiction) and [audit](#4-direct-blowups-and-the-global-contradiction) | A different route from the defect algebra and first-symbol divisor to moving singularities and an exceptional-rank contradiction | Characteristic-zero and K3-specific; preserve as historical reviewed evidence, not a new result |
| Explicit local multiplication and defect types | [Intrinsic quadruple local algebra](quartic_pair_obstruction.md) | The local normal form and identification of the fixed divisor, with coefficient-function qualifications | Local algebra does not by itself prove global realizability or a global STCI exclusion |
| Genus and torsion budgets | [Degeneration genus budgets](#44-degeneration-genus-budgets) and [normal torsion spectral budget](curvilinear_genus_and_defects.md#normal-torsion-spectral-genus-budget) | Numerical bookkeeping, boundary divisors, and explicit reduced/nonreduced comparison examples | Necessary conditions and examples are not sufficient to exclude all pairs |

**Shared starting point.** The fixed quartic curve, its conormal bundle and the generic transverse length-four hypothesis belong to the common setup. The filtered and surface-singularity arguments then diverge: one analyzes actual quartic lifting/contact spaces; the other counts singularities of a general pencil member. The genus-budget work instead studies what numerical restrictions survive under degeneration. The local-algebra source is a bridge between the two obstruction routes, not a replacement for either global step.

**Preservation rule.** Keep the explicit triple-multiplicity plus residual-quartic examples in [the multiplicity-three construction](#44-multiplicity-three-forces), the negative control where quadric restrictions fail to determine normal multiplicity in [the proof-routes discussion](#44-intrinsic-proof-routes), and the nonreduced degeneration examples in [the genus-budget section](#44-degeneration-genus-budgets). These prevent the stronger-looking arguments from being incorrectly extended to lower generic multiplicity, arbitrary residual support, or higher degrees. The source audits and their epistemic qualifications remain authoritative for their own claims.

---


Permanent subject consolidation. All source mathematical detail retained with its original conditional and audited status.


---

## 44-intrinsic-proof-routes

[Complete proof routes and negative controls](quartic_pair_obstruction.md), including the [completed embedded fourth-extension proof](intrinsic_fourth_extension.md).

## 44-multiplicity-three-forces-audit

# Independent audit: what multiplicity at least three forces in (4,4)

Date: 2026-10-26. Reviewer: independent `triple_classification` agent. Reviewed document: [multiplicity-three deductions](#44-multiplicity-three-forces). **Outcome: the stated deductions pass independent reconstruction at their stated scopes.**

## Scope and accepted premises

The field is algebraically closed of characteristic zero, the curve is the fixed embedding \(C=[s^4:s^3t:st^3:t^4]\), and the quartic pair is proper. The audit read the research index and the literal statements of [R0001](../../results/quartic_carrier_exclusion.md), [R0020](../../results/quartic_conormal_characteristic_jump.md), and [R0022](../../results/quartic_44_filtered_exclusion.md). Their accepted proofs and certificates are premises, not verification tasks. The earlier [smooth-carrier deduction](#44-degeneration-genus-budgets) and the accepted source-level conjugate pencil in the [filtered proof](https://github.com/markluxton1/STCI/blob/ca33958696fdc4f06a1c39b160aa13d097f24146/research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd) were consulted at their recorded scope.

The reviewer independently derived the conjugate example's factorization and branch geometry before reading the new verifier. The [new script](https://github.com/markluxton1/STCI/blob/0a35730b2f5e046705b8a7570ebc52c2a726da52/research/computations/verify_44_triple_residual_example_2026_10_26.py) was inspected as finite polynomial evidence. Its successful execution is recorded separately in the linked validation directory; the audit does not equate execution with a global proof.

## 1. Maximum multiplicity and integrality of every pencil member

Degree gives \(m_C\le4\). Equality exhausts degree sixteen, and complete-intersection purity then gives sole reduced support C, contradicting R0022. Thus \(m_C=3\) and the actual residual cycle has degree four. This reasoning does not imply residual integrality or rationality.

The all-members-integral argument uses R0001 essentially and is correct. If a quartic member has a quadratic factor carrying C, that factor is q. The mate is not divisible by q by properness, and its restriction to Q has class (4,4). The class (2,-2) rules out a second C component, so the local intersection with q has multiplicity one. A second quadratic carrying factor is necessarily q again; it doubles the multiplicity to two. Other quadratic factors are units at the generic point of C. Therefore this case cannot give multiplicity three.

Any remaining reducible quartic carrying C has the form \(A\ell\), with A an integral cubic and the plane factor a unit generically on C. If the mate is integral quartic, \(V(A,G)\) is proper of degree twelve and already contains 3C; purity gives sole support C, contrary to the precise integral-quartic/all-mate-degree statement of R0001. If the mate is reducible, the same quadratic exclusion leaves an integral cubic carrying factor B. Properness rules out A=B, and degree nine cannot accommodate 3C. This accounts for repeated factors as well as reduced factorizations.

## 2. First-symbol divisor and moving singularities

Generic transverse length three forces a nonzero linear normal relation: two equations of normal order at least two would have local intersection length at least four. The generic algebra is therefore curvilinear, \(K[\epsilon]/(\epsilon^3)\). Saturating the common first-symbol line in \(E=\mathcal O(-7)^2\) gives a subbundle \(M=\mathcal O(-7-e)\), with e nonnegative and locally free quotient \(\mathcal O(e-7)\).

The two actual first symbols are \(h_0m,h_1m\), with \(h_i\in H^0(\mathcal O(9-e))\). A constant dependence would produce a nonzero pencil member in \(H^0(\mathcal I_C^2(4))=kq^2\), already impossible at multiplicity three. Hence e lies between zero and eight. Removing the common divisor B gives a basepoint-free nonconstant pencil of degree \(n=9-e-\deg B\ge1\).

The saturated direction has no zero in any fiber of E. Since each carrier vanishes on C, its ambient differential restricted to C is its first normal symbol. Consequently its singular subscheme restricted to C is exactly the zero divisor of the corresponding scalar section. General fibers of the resulting map to the pencil line are simple in characteristic zero. They avoid any prescribed finite subset of C. The resulting fixed-plus-moving divisor statement is valid; neither a common singular point nor absence of other singularities is inferred.

## 3. The moving singularities are A2

Remove the finite loci of residual attachment and nonprimitive triple behavior. On the remaining open set the actual ideal is locally \((x,y^3)\), with curve parameter t. This follows by spreading the generic curvilinear normal form; it asserts no global primitive structure.

For a generating pencil pair, the coefficient matrix relative to x and y³ is invertible. At a simple moving first-symbol zero of a member H, its x coefficient vanishes simply in t, whereas another generator has unit x coefficient. The determinant condition forces H's y³ coefficient to be a unit. Writing \(H=xA+y^3B\), one has \(A_t(0)\ne0\) and \(B(0)\ne0\). Use A as a coordinate and apply the formal splitting lemma to its nondegenerate hyperbolic pair with x; the remaining one-variable term has order three with nonzero coefficient. Thus the surface germ is \(tx+y^3\), of type A2. This validates the n moving A2 points for a general carrier, while retaining the note's limitations concerning fixed singularities, other singularities, and normality.

## 4. Explicit example and its global cycle

For \(12r^2+4r+3=0\), put \(a=r+3/2\), \(b=r+1/2\), \(c=1/6-r\). Direct reduction in the quadratic field gives \(b^3=r/9-1/6\) and
\[
(ap-b)^3+(r-7/6)p(ap-b)^2+cp^4=(p-1)^3(cp+b^3).
\]
The residual root is the stated \(\kappa=(2r-3)/(18r-3)\), with residual x3 coefficient \(-\kappa/3\). The root is nonzero, simple, and distinct from one. Nonzero diagonal scaling makes its projective parametrization a smooth rational quartic of degree four. The script's field multiplication, inverse, polynomial arithmetic, and factor check match this calculation.

The properness proof is genuinely global: R0 is primitive and linear in x3 over \(k[x_0,x_1,x_2]\), with relatively prime coefficient and constant term, so Gauss's lemma makes it irreducible. R1 is not proportional to R0. The pair is consequently a regular sequence. The dense-chart components already account for degree twelve plus four; complete-intersection purity excludes further components or isolated embedded points. The full cycle is therefore \(3C+C_\kappa\).

On each endpoint chart the ideal of one reduced branch restricted to the other has nonzero cubic and quartic terms in its parameter, giving intersection length three. There are no other intersections. The reduced support has genus five.

The new global gradient calculation was reconstructed by differentiating both displayed quartics. With \(h=2r+2/3\), the gradient of R0 restricted to C is \(s^8v\), where \(v=(-2rt^4,(-a+4b)st^3,-as^3t,s^4)\). For R1 its four coefficients agree with \(ht^8v\): the first identity is \(-2rh=1\), and the remaining ones follow by substituting \(r^2=-r/3-1/4\). The vector v has no projective zero, because its final component is nonzero when s is nonzero and its first component is nonzero when s is zero. Thus the global singularity divisor is exactly \(\alpha s^8+\beta h t^8\), with no common base point and eight simple roots for \(\alpha\beta\ne0\). The local A2 argument applies at these roots. This is an actual example and does not classify all residual quartics.

## 5. Liaison and filtration arithmetic

The saturated C-primary triple T and its residual D are locally Cohen--Macaulay curves with no common component. Residual duality in the (4,4) Gorenstein curve gives \(\mathcal I_{T/W}\simeq\omega_D(-4)\). Since D has degree four, its twisted dualizing Euler characteristic is \(4n+p_a(D)-17\). Subtracting from \(16n-32\) yields \(p_a(T)=p_a(D)+16\). The union sequence then gives intersection length \(18-2p_a(D)\). These identities remain valid when D is nonreduced.

For the stated saturated triple filtration, summing Euler characteristics of \(\mathcal O_C,L,L^2(D_2)\) gives \(p_a(T)=19-3e-d_2\), hence \(p_a(D)=3-3e-d_2\). The note correctly keeps this conditional on that filtration and does not import the sole-support quadruple's restricted numerical types. In the displayed primitive e=1 example the values are sixteen, zero, and eighteen, while the reduced attachment length is six.

## Review decision

No substantive mathematical correction is required. The attained maximum, forced residual degree, integral-pencil deduction using R0001, moving singularity divisor, general moving A2 structure, and explicit example all reconstruct at the stated hypotheses. The note explicitly leaves the classification of all degree-four residual schemes open. The verifier establishes only its listed finite identities; global properness, purity, liaison, and singularity interpretation are supplied by the arguments above.



---

## 44-multiplicity-three-forces

# What multiplicity at least three forces in a (4,4) intersection

Date: 2026-10-26. Status: new deductions and explicit residual calculation, independently reviewed in the [audit](#44-multiplicity-three-forces-audit).

## 1. Exact question, inputs, and answer

Let k be algebraically closed of characteristic zero, let
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\]
and let \(W=V(F,G)\) be a proper complete intersection of two quartics containing C. Suppose its generic transverse multiplicity \(m_C(W)\) is at least three. The conclusion is:

1. The multiplicity is exactly three and \([W]=3[C]+R\), with R an effective degree-four cycle having no C component.
2. Every nonzero member of the quartic pencil is integral. This conclusion uses the accepted all-mate-degree quartic-carrier exclusion R0001.
3. Every member is singular somewhere on C. There is a nonconstant pencil map on C whose fibers give moving singular points; a common singular point is not forced.
4. At the general moving points the carrier singularities are \(A_2\). In particular, this case has a different singularity budget from the previously excluded multiplicity-four case.
5. The case occurs: an explicit proper pair has cycle \(3C+C_\kappa\), with \(C_\kappa\) a distinct smooth rational quartic. For this example a general pencil member has eight moving \(A_2\) points on C and there are no fixed common singular points on C.

This closes the multiplicity/residual-existence question in degree (4,4): the maximum multiplicity is three, it is attained, and at that maximum the residual degree is exactly four. It does not classify every possible degree-four residual scheme.

Premises, used without rerunning their proofs:

- [R0022](../../results/quartic_44_filtered_exclusion.md): no proper quartic pair has sole reduced support this C in characteristic zero.
- [R0001](../../results/quartic_carrier_exclusion.md): no integral quartic carrier through this C admits any homogeneous mate with sole support C.
- [R0020](../../results/quartic_conormal_characteristic_jump.md): \(N^*_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(-7)^2\).

The elementary identity \(H^0(\mathcal I_C^2(4))=kq^2\), for \(q=x_0x_3-x_1x_2\), and the new [smooth-carrier lemma](#44-degeneration-genus-budgets) are already independently reviewed. The displayed conjugate pencils below are inherited accepted source-level evidence from [October 7, section 4](mf6_and_nonnormal_structures.md#source-2026-10-07-session-mf6-e1-independent-auditmd) and [the October 23 filtered proof](https://github.com/markluxton1/STCI/blob/ca33958696fdc4f06a1c39b160aa13d097f24146/research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-quartic-44-filtered-proof-proposalmd). Their residual factorization and geometric interpretation are the new calculation here. No exhaustiveness assertion from the multiplicity-four classification is transferred to arbitrary multiplicity-three pairs.

## 2. Exactly triple, with a real degree-four residual

Bézout gives \(4m_C(W)\le16\), so \(m_C(W)\le4\). If equality held, purity of the complete intersection and degree exhaustion would imply \(W_{\mathrm{red}}=C\), contrary to R0022. Hence
\[
\boxed{m_C(W)=3,\qquad [W]=3[C]+R,\qquad\deg R=4.}
\]
The degree-four cycle R is downstairs in projective space; no exceptional component on a blowup is being counted as a residual curve. Its being integral, reduced, smooth, or rational does not follow from this degree argument.

The generic transverse algebra is necessarily curvilinear. In a transverse regular local surface, a length-three complete intersection cannot have embedding dimension two: if both equations had order at least two, local intersection multiplicity would be at least four. Thus over \(K=k(C)\), after completion,
\[
\widehat{\mathcal O}_{W,\eta_C}\simeq K[\epsilon]/(\epsilon^3).
\]

## 3. Every carrier in the pencil is integral

First, no pencil member can have a quadratic factor carrying C. That factor must be the unique quadric q. A quartic mate not divisible by q restricts to a divisor of type (4,4) on \(Q\simeq\mathbf P^1\times\mathbf P^1\), while C has type (1,3). C occurs at most once, since (4,4)-2(1,3)=(2,-2) is not effective. Thus a member q times a quadratic not carrying C gives multiplicity one; the only repeated quadratic carrying case \(q^2\) gives multiplicity two. Both contradict m=3.

If a quartic member H were reducible, C would therefore lie on an integral cubic factor A, with \(H=A\ell\) and the plane \(\ell=0\) not containing C. For another basis member G,
\[
m_C(A,G)=3.
\]
If G is integral, the proper intersection \(V(A,G)\) has degree twelve and already contains the degree-twelve cycle 3C. Purity gives sole support C, contradicting R0001 with G as the integral quartic carrier and A as its mate. This uses the literal statement of R0001, rather than assuming R0022 covers degrees (3,4).

If G is reducible, the quadratic case is already excluded, so its carrying factor is an integral cubic B and its remaining factor is a plane. Properness excludes A=B; Bézout gives degree nine for \(V(A,B)\), which cannot contain 3C of degree twelve. This also contradicts m=3. Therefore
\[
\boxed{\text{Every nonzero member of the pencil is an integral quartic.}}
\]
This conclusion is not claimed independently of the accepted R0001 premise.

## 4. A moving singularity divisor on C

Write \(E=N^*_{C/\mathbf P^3}=\mathcal O(-7)^2\). At generic multiplicity three, the two first normal symbols are dependent. Their saturated common image line is
\[
M=\mathcal O(-7-e)\subset E,\qquad e\ge0,
\]
with locally free quotient \(L=\mathcal O(e-7)\). Saturation is important: a local generator of M has no zero in E.

After twisting by \(\mathcal O_C(4)=\mathcal O_{\mathbf P^1}(16)\), write
\[
\sigma_F=h_0m,\qquad\sigma_G=h_1m,\qquad
h_0,h_1\in H^0(\mathcal O_{\mathbf P^1}(9-e)).
\]
The sections \(h_0,h_1\) are linearly independent. Otherwise a nonzero constant pencil combination would have zero first symbol, hence would be a nonzero multiple of q², which section 3 has excluded. Consequently
\[
0\le e\le8.
\]

Let B be the common zero divisor of \(h_0,h_1\), and put \(b=\deg B\). Removing B gives a basepoint-free, nonconstant pencil on C, of degree
\[
\boxed{n=9-e-b\ge1.}
\]
Equivalently, it gives the nonconstant map from a curve point to the pencil member singular there. Its degree is n. For \(H=\alpha F+\beta G\), the scheme of singular points of H restricted to C is the zero divisor of \(\alpha h_0+\beta h_1\). This follows because H vanishes identically on C and its differential along C is precisely its normal symbol; the saturated direction m is nonzero in every fiber.

Every member thus has a singularity divisor of degree \(9-e\) on C, counting the vanishing orders of the first symbol. For a general member, this consists of the fixed divisor B plus n distinct moving points. Characteristic-zero separability is used for generic simplicity. In particular, every member is singular somewhere on C, and the moving part has positive degree even when B is nonempty. The assertion does not force B to be nonempty.

## 5. The general moving singularities are A2

Remove the finite subset of C where the primary triple is nonprimitive or where the residual scheme meets C. Locally on the remaining open set, the actual complete-intersection ideal is
\[
I_W=(x,y^3)
\]
in smooth ambient coordinates (t,x,y), with \(C=(x,y)\). This is an open normal form for the generic curvilinear triple, not a global normal-flatness assertion.

The two quartics generate this ideal, so their coefficient matrix relative to the generators x and y³ is invertible. At a simple moving first-symbol zero for H, its x coefficient vanishes simply in t. A second pencil generator has unit x coefficient there; invertibility forces the y³ coefficient of H to be a unit. Thus
\[
H=xA(t,x,y)+y^3B(t,x,y),\qquad
\partial_t A(0)\ne0,\quad B(0)\ne0.
\]
A formal coordinate change using A as a coordinate, followed by a unit adjustment, gives
\[
\boxed{H=tx+y^3,\quad\text{an }A_2\text{ surface singularity}.}
\]
The general moving fibers avoid the finite removed subset and the branch values of the pencil map. Hence a general carrier has n moving A2 singularities on this open subset of C. It may have additional fixed singularities or singularities elsewhere. Normality or a global K3 resolution is not asserted for every such pencil.

This explains the change from the hypothetical multiplicity-four mechanism: a local triple \((x,y^3)\) produces A2 at a simple moving zero; the analogous quadruple \((x,y^4)\) produces A3. Their exceptional-rank budgets differ.

## 6. An explicit genuine 3C plus a rational quartic

Choose r satisfying \(12r^2+4r+3=0\) and define
\[
\begin{aligned}
R_0&=x_0^3x_3-(r+3/2)x_0^2x_1x_2+(r+1/2)x_1^4,\\
R_1&=x_0x_3^3+(r-7/6)x_1x_2x_3^2+(1/6-r)x_2^4.
\end{aligned}
\]
Set \(a=r+3/2\), \(b=r+1/2\), \(c=1/6-r\). On \(x_0=1\), take \(x_1=z\), \(x_2=pz^3\), \(x_3=qz^4\). The first equation gives \(q=ap-b\), and the second gives the exact factorization
\[
q^3+(r-7/6)pq^2+cp^4=(p-1)^3(cp+b^3).
\]
The residual root is
\[
\kappa=\frac{2r-3}{18r-3},\qquad q=-\frac\kappa3,
\qquad27\kappa^2-14\kappa+3=0.
\]
The constants \(\kappa\) and \(-\kappa/3\) are nonzero, and \(\kappa\ne1\). Therefore
\[
C_\kappa=[s^4:s^3t:\kappa st^3:-(\kappa/3)t^4]
\]
is a distinct smooth rational quartic, obtained by a diagonal projective transformation of C. The simple residual root and triple root yield
\[
\boxed{[V(R_0,R_1)]=3[C]+[C_\kappa].}
\]

For global properness, R0 is a primitive linear polynomial in x3 over k[x0,x1,x2]: its coefficient x0³ is coprime to its constant coefficient because \(b\ne0\). Gauss's lemma makes R0 irreducible. R1 is not proportional to it, so the intersection is proper. The identified cycle already has degree sixteen, and purity rules out further cycle or isolated components. The calculation establishes an actual global pair, beyond a transverse formal model.

The residual quartic lies on \(3x_0x_3+x_1x_2=0\), not on the original Q. It meets C only at the endpoints, with intersection length three at each: on the finite chart the differences are \((\kappa-1)z^3\) and \((-\kappa/3-1)z^4\); the opposite chart gives the same minimum order. Thus the reduced union \(C\cup C_\kappa\) has arithmetic genus five. Its genus is different from that of the full (4,4) scheme.

The inherited first-symbol coefficients on the finite chart are
\[
h_{R_0}=1,\qquad h_{R_1}=(2r+2/3)z^8,
\]
as sections of \(\mathcal O_{\mathbf P^1}(8)\). This also follows directly from the global gradients: put \(h=2r+2/3\) and
\[
v=(-2rt^4,(-a+4b)st^3,-as^3t,s^4).
\]
Then \(\nabla R_0|_C=s^8v\), \(\nabla R_1|_C=ht^8v\), and v is nowhere zero. Thus the singularity divisor on C of \(\alpha R_0+\beta R_1\) is
\[
\alpha s^8+\beta h t^8=0.
\]
There is no common projective zero: R0 is smooth at every finite point of C, and R1 is smooth at infinity. For \(\alpha\beta\ne0\), there are eight distinct moving zeros, hence eight moving A2 points. No common singular point on C is forced by multiplicity three. Eight A2 configurations have total exceptional rank sixteen, which by itself causes no K3 rank contradiction.

The standard-library [verifier](https://github.com/markluxton1/STCI/blob/0a35730b2f5e046705b8a7570ebc52c2a726da52/research/computations/verify_44_triple_residual_example_2026_10_26.py)
replayed the fifteen exact factorization and chart checks and reproduced the
[saved output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/44-triple-residual-2026-10-26/checks.json) byte for byte.
The geometric argument above supplies global purity and properness. To
replay the finite identities, run

The archived command uses [verify_44_triple_residual_example_2026_10_26.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/verify_44_triple_residual_example_2026_10_26.py) from the pinned repository snapshot.

```sh
python3 research/computations/verify_44_triple_residual_example_2026_10_26.py --output /tmp/stci-44-triple-residual.json
```

## 7. Residual genus and what is not classified

Let T be the saturated C-primary triple and D the residual scheme. They are locally Cohen--Macaulay curves linked in W, of degrees twelve and four. Liaison gives
\[
p_a(T)-p_a(D)=16.
\]
For completeness, the duality sequence has kernel
\(\mathcal I_{T/W}\simeq\omega_D(-4)\). Its Euler characteristic is \(4n+p_a(D)-17\); subtracting from \(\chi(\mathcal O_W(n))=16n-32\) gives \(p_a(T)=p_a(D)+16\). The union sequence then gives
\[
\operatorname{length}(T\cap D)=18-2p_a(D).
\]

If the saturated quasiprimitive triple filtration is written
\[
\mathcal O_C,\quad L=\mathcal O(e-7),\quad
L^2(D_2),\qquad d_2=\deg D_2,
\]
its Euler characteristic yields
\[
p_a(T)=19-3e-d_2,\qquad
\boxed{p_a(D)=3-3e-d_2.}
\]
This formula uses the stated triple filtration, not the Gorenstein graded pairings of a sole-support quadruple. The restrictions e=0,d2=3 or e=1,d2=0 from the excluded multiplicity-four problem cannot be asserted for every multiplicity-three pair.

In the displayed primitive e=1 example, \(p_a(T)=16\), \(p_a(D)=0\), and \(\operatorname{length}(T\cap D)=18\). The reduced intersection \(C\cap D\) has length six. The previously derived eighteen-unit boundary for a reduced marked component must not be applied to this nonreduced W by replacing T with C.

The forced residual cycle has degree four, but the present argument does not prove it always integral, reduced, rational, or on a fixed quadric. A complete residual classification would require controlling all actual quartic source spaces for the possible defective triple structures. The accepted multiplicity-four proof classifies only its forced types. This additional classification is not needed to close the maximum-multiplicity and residual-existence assertions proved here.

## 8. Review and frontier impact

The independent review reconstructs the new deductions, checks the explicit global example, and retains the stated accepted premises. The new verifier proves its listed finite polynomial identities only. The exclusions remain premises and are not retested. No record, proof, or unrestricted STCI status changes. The new conclusion is the attained maximum three, the forced residual degree four, and the singularity structure of the entire integral pencil at that maximum.

## 9. An independent route to the multiplicity-four bound

The [complete rank-four surface proof](#1-a-common-numerical-reduction) excludes multiplicity four without R-0001 or R-0022 as inputs. Thus it supplies an independent proof of the maximum-multiplicity assertion here. The all-members-integral assertion for arbitrary multiplicity-three pencils in section 3 retains its separate R-0001 dependency.

## 44-intrinsic-proof-routes-audit

[Reviewed mathematical replacement: direct blowups, controls and contact geometry](quartic_pair_obstruction.md).

## 44-degeneration-genus-budgets

# Degenerating a (4,4) curve: cycles, gluing, and nilpotent genus

Date: 2026-10-26. Status: exploratory synthesis and new elementary deductions; independent review is recorded in the [audit](#44-degeneration-genus-budgets-audit).

## 1. Question and scope

What can a smooth complete-intersection curve of type (4,4) in projective three-space degenerate into, and what does the fixed Hilbert polynomial actually constrain? First allow all proper pairs; then retain the marked curve
\[
C=[s^4:s^3t:st^3:t^4].
\]
The field is algebraically closed of characteristic zero; statements about ordinary topology use the associated complex curve. A proper pair has no common surface component. Throughout, a cycle means the fundamental effective one-cycle of an actual scheme, not the full scheme structure.

Completion of this move means deriving the genus and componentwise boundary constraints, giving actual smoothable examples at several extremes, and isolating the additional information needed when a component acquires multiplicity. It does not mean classifying all degree partitions or all embedded limits.

inputs are [R0021](../../results/quartic_mu4_degeneration.md), for the prescribed four-quartic configuration, and the precise scope of [R0022](../../results/quartic_44_filtered_exclusion.md), for the already established fixed-curve (4,4) exclusion. Neither exclusion proof is rerun. The [previous cycle notebook](../torus/root_pencil_geometry.md) and [conductor/topology note](../torus/root_pencil_geometry.md), with their linked audits, supply reviewed geometry. The smooth-carrier dichotomy in section 7 is a new elementary deduction, independently reconstructed during this move.

## 2. What is conserved

The Koszul resolution of a proper pair of degrees (a,b) gives
\[
P_W(n)=abn-\frac{ab(a+b-4)}2,\qquad
p_a(W)=1+\frac{ab(a+b-4)}2.
\]
Adjunction gives the additional, stronger constraint
\[
\omega_W\simeq\mathcal O_W(a+b-4).
\]
These assertions hold for nonreduced complete intersections too. Such a curve is pure, Cohen--Macaulay, and Gorenstein; the Koszul resolution also gives \(H^0(\mathcal O_W)=k\), hence connectedness and \(h^1(\mathcal O_W)=p_a(W)\).

For (4,4), these become
\[
\deg W=16,\quad P_W(n)=16n-32,\quad p_a(W)=33,
\quad\omega_W=\mathcal O_W(4).
\]
The open locus of proper pencils in \(\operatorname{Gr}(2,H^0(\mathcal O_{\mathbf P^3}(4)))\) carries a flat universal complete-intersection family, and smooth members form a dense open subset. Every proper pair discussed here can therefore be smoothed by a general perturbation. A specialization acquiring a common surface leaves this open locus: its two specialized equations need not describe the flat curve limit.

For general flat projective families, constancy of Euler characteristics of twists follows from [Stacks, Lemma 36.32.2](https://stacks.math.columbia.edu/tag/0B9T), applied to the structure sheaf and its twists. This is coherent Euler characteristic, not ordinary topological Euler characteristic. A cycle alone does not have a specified arithmetic genus: the gluing and nilpotent structure are essential.

## 3. The reduced genus budget and the graph

Let W be reduced, with r integral components, normalization genera \(g_i\), and local delta invariants \(\delta_p\). The normalization exact sequence gives
\[
33=\sum_i g_i+\delta(W)-r+1,
\qquad \delta(W)=\sum_p\delta_p.
\]
Thus \(\delta=32+r-\sum g_i\). For definitions and finite normalization quotients see [Stacks, delta invariant](https://stacks.math.columbia.edu/tag/0C3Q).

For nodal curves this is the familiar graph identity
\[
33=\sum_i g_i+b_1(\Gamma).
\]
For arbitrary reduced curves, use the bipartite graph of normalized components and singular points, with an edge for each local branch. If \(r_p\) is the number of branches at p, put
\[
b=\sum_p(r_p-1)-r+1,\qquad
u=\delta-\sum_p(r_p-1).
\]
Then
\[
33=\sum_i g_i+b+u.
\]
Here b counts graph loops, while u measures gluing beyond identifying the branch origins. In characteristic zero these are the abelian, toric, and unipotent dimensions of the generalized Jacobian, as explained in the earlier conductor/topology note. In particular, tangencies can contribute arithmetic genus without adding the same number of topological loops.

For the complex reduced curve,
\[
b_1(W)=2\sum_i g_i+b,\quad b_2(W)=r,
\quad\chi_{\rm top}(W)=2r-2\sum_i g_i-\sum_p(r_p-1).
\]
The smooth fiber has Euler characteristic -64. The local complete-intersection Milnor formula
\(\mu_p=2\delta_p-r_p+1\) gives
\[
\chi_{\rm top}(W)=-64+\sum_p\mu_p.
\]
The local formula is [Dimca--Greuel, Theorem 2.1(1), p. 115](https://www.journalofsing.org/volume18/dimca-greuel.pdf), attributing it to Buchweitz--Greuel. These reduced isolated-singularity formulas do not apply by simply reducing a generically nonreduced fiber.

## 4. Actual reduced configurations

### Sixteen lines: all genus in graph loops

Choose eight planes \(A_i,B_j\), \(1\le i,j\le4\), in general linear position and set
\[
F=\prod_i A_i,\qquad G=\prod_j B_j.
\]
The sixteen lines \(L_{ij}=V(A_i,B_j)\) meet precisely when they share a row or column. General position rules out fourfold plane intersections and hence triple points of the curve. There are
\[
4\binom42+4\binom42=48
\]
ordinary nodes, so the rook graph has \(48-16+1=33\) loops. Each line has six attachments. This is a complete intersection with genus allocation \((\sum g_i,b,u)=(0,33,0)\).

It also gives the sharp upper bound for total delta among reduced (4,4) curves:
\[
\delta=32+r-\sum_i g_i\le48,
\]
since \(r\le16\). This comparison allows all proper pairs, without retaining the fixed quartic.

### Four plane quartics

Keep F a product of four general planes but choose G a general smooth quartic surface. Each plane section is smooth of genus three. Every pair meets at four points, giving twenty-four nodes in total. Thus
\[
33=4\cdot3+24-4+1=12+21.
\]

### Retaining the fixed rational quartic

The reviewed notebook supplies a general member
\[
W=C\cup D,\qquad \deg D=12,\quad g(D)=16,
\quad\operatorname{length}(C\cap D)=18,
\]
with D smooth and eighteen ordinary attachments. The allocation is \((16,17,0)\).

At the prescribed pair
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3,
\]
there are four smooth rational quartics, with pairwise contact three at each of two endpoints. Each endpoint has four branches, delta eighteen, and Milnor number thirty-three. Therefore
\[
33=0+36-4+1=0+3+30.
\]
Its ordinary Betti numbers are \((b_0,b_1,b_2)=(1,3,4)\), and its Euler characteristic is two. The two endpoints account for the change \(-64+66=2\) under smoothing. Its delta thirty-six is not maximal, even in the marked-C class: the earlier notebook contains an independently checked eight-rational-component example with delta forty.

## 5. Adjunction gives a constraint on each component

On the normalization of a component of degree e and genus g, with map \(\nu_i:\widetilde C_i\to W\), its conductor divisor \(B_i\) satisfies
\[
\nu_i^*\omega_W=\omega_{\widetilde C_i}(B_i),\qquad
\deg B_i=(a+b-4)e-2g+2.
\]
This concerns reduced Gorenstein curves. For a smooth component in a reduced union, \(B_i\) measures its scheme-theoretic attachment to the rest. In a nodal curve it counts the marked branches of nodes; a self-node contributes twice on its normalized component.

For (4,4), a proposed component of degree e and normalization genus g must carry conductor degree \(4e-2g+2\). In particular, a rational line has six units, a smooth plane quartic has twelve, and a rational quartic has eighteen. These are stronger constraints than the total genus equation alone, though they still do not imply global realizability.

For \(W=C\cup D\) reduced and C smooth of degree e and genus g, put \(s=a+b-4\). The attachment and residual formulas are
\[
\operatorname{length}(C\cap D)=se-2g+2,
\quad\deg D=ab-e,
\quad p_a(D)=g+\frac{s(ab-2e)}2.
\]
They follow from duality on C and the union exact sequence. For the fixed rational quartic in degree (d,d), they specialize to
\[
\deg D=d^2-4,\quad p_a(D)=(d-2)(d^2-8),
\quad\operatorname{length}(C\cap D)=8d-14.
\]
The residual genus is arithmetic; smoothness and irreducibility require separate existence arguments. At d=4 the reviewed notebook supplies those arguments. At other degrees these formulas alone do not supply them.

## 6. Nonreduced limits: an explicit nilpotent calculation

Take independent linear forms L,M and
\[
W=V(L^4,M^4).
\]
This is a proper complete intersection with cycle \(16[V(L,M)]\). A complementary choice of coordinates gives a finite projection to the support line and
\[
\pi_*\mathcal O_W=\bigoplus_{0\le i,j\le3}
\mathcal O_{\mathbf P^1}(-i-j).
\]
Consequently
\[
P_W(n)=\sum_{i,j}(n-i-j+1)=16(n+1)-48=16n-32.
\]
Its reduced topology is a sphere, while the twisted nilpotent layers account for arithmetic genus thirty-three. There are no additional residual components.

Even a pure multiplicity-four degree-four support occurs in characteristic zero: \(V(L^4,G_4)\) has cycle \(4[D]\) when \(D=V(L,G_4)\) is a smooth plane quartic. Its four layers \(\mathcal O_D(-j)\), \(0\le j\le3\), have polynomials \(4n-4j-2\), whose sum is again \(16n-32\).

These examples show that fixed Hilbert polynomial, arithmetic genus, subcanonical duality, and smoothability permit pure multiple cycles, including rational support. The excluded fixed cycle \(4[C]\) needs the actual rational-quartic embedding; its exclusion is the scope of R0022, not a consequence of the general topology budget.

## 7. A sharper marked-curve deduction when a carrier is smooth along C

**Proposed lemma.** Suppose a proper quartic pencil contains C and has a member F smooth at every point of C. If its generic intersection multiplicity along C is at least two, then the pencil contains \(q^2\), where \(q=x_0x_3-x_1x_2\). More precisely,
\[
W=V(F,q^2),\qquad [W]=2[C]+2[C'],
\]
where C' is the residual divisor of type (3,1) to C of type (1,3) on the smooth quadric Q. The divisor C' has no C component. Thus the generic multiplicity of C is exactly two. The residual divisor C' need not be irreducible or reduced for a special F.

**Proof.** The first normal symbols f,g of F,G are sections of \(N^*_{C/\mathbf P^3}(4)\). Generic multiplicity at least two forces their wedge to vanish generically, hence everywhere. Smoothness of F along all of C makes f nowhere zero, so it defines a subbundle \(\mathcal O_C\). The symbol g belongs to this subbundle, giving \(g=\lambda f\) with \(\lambda\in H^0(\mathcal O_C)=k\). Thus
\[
G-\lambda F\in H^0(\mathcal I_C^2(4)).
\]
Here the square is the ideal-sheaf square, so saturation issues are not suppressed. The known elementary quartic calculation gives this space as \(kq^2\): restriction of a twice-vanishing quartic to Q would have residual type (2,-2), so is zero; after division by q, its quadratic factor must be the unique quadric through C. Properness makes \(G-\lambda F\) nonzero. Finally, C' has type (3,1); subtracting C leaves type (2,-2), so C' cannot contain C. This proves the stated cycle and multiplicity.

For an explicit smooth example take the displayed F,G from section 4 and \(S=V(F+G)\). Its partial derivatives show S smooth in characteristic zero. Under Segre coordinates \((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\),
\[
(F+G)|_Q=(ad^3-bc^3)(a^3d-b^3c).
\]
Both factors define smooth rational quartics C,C', with ten transverse intersections (the endpoints and eight other points). Hence
\[
V(F+G,q^2)\quad\hbox{has cycle }2C+2C'.
\]
Its reduced support D is the (2,4) curve \(C\cup C'\), of genus nine. On S, W is the double Cartier divisor 2D. The sequence
\[
0\longrightarrow\mathcal O_D(-2)\longrightarrow
\mathcal O_{2D}\longrightarrow\mathcal O_D\longrightarrow0
\]
gives polynomials \((8n-24)+(8n-8)=16n-32\).

There is also an actual flat pencil retaining C between the four-quartic member and this double member:
\[
W_{[u:v]}=V(F+G,\ uF+vq^2).
\]
No nonzero combination \(uF+vq^2\) is a multiple of F+G, so every parameter is a proper complete intersection on S. At [1:0] it is the four-quartic arrangement; at [0:1] it is 2D. No assertion that the other members of this particular pencil have smooth residual curves is needed.

On any smooth quartic carrier the same calculation is compatible with the K3 intersection lattice:
\[
H^2=4,\quad H\cdot C=4,\quad C^2=-2,
\quad C'=2H-C,\quad C\cdot C'=10.
\]
This explains why reduced quartics in a (4,4) arrangement carry eighteen attachment units, while the support quartics in the doubled (2,4) member carry ten. Reduction has changed the adjunction problem.

For general equal degree d and any smooth connected projective marked curve, the first part of the argument still applies: if one carrier is smooth everywhere along C and the multiplicity is at least two, a constant change of the two generators produces a nonzero member of \(H^0(\mathcal I_C^2(d))\). At d=4 its one-dimensionality makes the conclusion especially rigid. In higher degrees this source space grows, and its image on the smooth carrier must be studied rather than assumed to consist of a single square.

## 8. General patterns and the remaining question

For (d,d),
\[
P_W(n)=d^2n-d^2(d-2),\qquad g=1+d^2(d-2).
\]
Products of d general planes on each side yield \(d^2\) lines with \(d^2(d-1)\) nodes, so all genus becomes graph loops. The opposite example \(V(L^d,M^d)\) has cycle \(d^2[L\cap M]\) and layers \(\mathcal O_L(-i-j)\), \(0\le i,j<d\), yielding the same polynomial. For (a,b), the corresponding grid has ab lines and \(a\binom b2+b\binom a2\) nodes, whose graph genus is exactly \(1+ab(a+b-4)/2\).

The most useful classification data therefore consist of component degrees and multiplicities, normalization genera, incidence and branch contacts, componentwise conductor divisors in the reduced case, and nilpotent filtrations in the nonreduced case. Numerical conditions are necessary; an actual pair of global forms remains an additional realization requirement.

For the fixed quartic, the new smooth-carrier dichotomy isolates a precise difficult stratum: multiplicity at least three requires that every pencil member be singular somewhere on C. It does not assert a common singular point for all members, and does not classify that stratum. In higher degrees, studying \(H^0(\mathcal I_C^2(d))\) on a smooth carrier is a concrete continuation of the same question. No unrestricted STCI conclusion or new record is claimed.

## 9. Evidence and review boundary

All new product examples, genus allocations, nilpotent calculations, and the smooth-carrier lemma have elementary proofs above and independent agent reconstruction in the linked audit. No inherited certificate was rerun. External sources were inspected for flat-family coherent Euler characteristic, the delta definition, and the local Milnor formula, at the precise links above; no literature novelty claim is made. The unresolved work is a classification or realization theorem beyond these examples and the stated smooth-carrier stratum.



---

## 44-degeneration-genus-budgets-audit

# Independent audit: (4,4) degeneration and genus budgets

Date: 2026-10-26. Reviewer: independent `genus_topology` agent. Reviewed document: [degeneration and genus budgets](#44-degeneration-genus-budgets). **Outcome: the stated elementary deductions pass independent reconstruction at the scopes below. This is an evidence audit.**

## Scope and inputs

The ambient space is projective three-space over an algebraically closed field of characteristic zero. Ordinary topology refers to the associated complex curve. Defining pairs are proper: their forms have no common surface component. The marked curve is the fixed embedding
\[
C=[s^4:s^3t:st^3:t^4].
\]
The reviewer read the research index, the reviewed note, records [R0021](../../results/quartic_mu4_degeneration.md) and [R0022](../../results/quartic_44_filtered_exclusion.md), and the relevant [conductor/topology evidence](../torus/root_pencil_geometry.md). The prescribed four-quartic decomposition and the fixed-curve exclusion were retained at their recorded scope; their inherited proofs and certificates were not rerun. The earlier generic smooth residual and eight-component competitor remain reviewed inputs with the provenance stated in the main note.

## Reconstruction of the scheme and reduced-curve budgets

1. The Koszul resolution gives the displayed polynomial and genus for every proper pair, including nonreduced pairs. Intermediate line-bundle cohomology on projective three-space gives \(H^1(\mathcal I_W)=0\), hence \(H^0(\mathcal O_W)=k\). Thus the claimed connectedness and equality \(h^1(\mathcal O_W)=p_a(W)\) also hold for these nonreduced complete intersections. Purity, Cohen--Macaulayness, Gorensteinness, and the adjunction formula follow from the regular sequence.

2. On the open parameter locus of proper pairs, the universal Koszul family is flat. Smooth complete intersections form a dense open subset. A general coefficient line through a prescribed proper pair has a smooth generic fiber after restricting the base to retain properness. This proves smoothability of every proper pair under discussion. It does not identify a flat curve limit when specialized forms gain a common factor, and it does not require that a smoothing retain the marked curve.

3. For reduced fibers, the finite normalization sequence independently yields
\[
p_a(W)=\sum_i g_i+\delta-r+1.
\]
The bipartite branch-incidence graph has first Betti number \(b=\sum_p(r_p-1)-r+1\). The dimension left after identifying branch origins is \(u=\delta-\sum_p(r_p-1)\), giving the stated decomposition into normalization, toric, and unipotent contributions in characteristic zero. The notation in the reviewed source is \(u\), consistently with its later formulas.

4. The normalization is topologically quotiented by identifying the finitely many branch origins. It follows that \(b_1=2\sum g_i+b\), \(b_2=r\), and the stated Euler characteristic formula holds. Substitution of the normalization genus identity gives \(\chi_{\mathrm{top}}(W)=-64+\sum_p(2\delta_p-r_p+1)\). The identification of the local summand with the Milnor number is valid for the reduced isolated complete-intersection curve germs. The main note correctly avoids applying this reduced formula to a generically nonreduced fiber merely by taking its reduction. The cited [Dimca--Greuel paper](https://www.journalofsing.org/volume18/dimca-greuel.pdf), Theorem 2.1(1), supplies the local formula.

5. In the plane-product grid, a node occurs exactly at the intersection of two lines sharing a row or column. General linear position excludes points lying on four planes and excludes three curve branches meeting. Hence there are sixteen lines and forty-eight ordinary nodes, with graph genus thirty-three. Since every reduced component has positive integral degree, \(r\le16\); therefore \(\delta\le48\), attained by this example. For four general plane sections of a smooth quartic, the twelve normalization-genus units and twenty-four nodes give genus thirty-three as claimed. The general \((a,b)\) grid counts likewise reconstruct directly.

## Componentwise conductor and nonreduced checks

For a reduced Gorenstein curve with normalization \(\nu\), finite duality gives
\[
\omega_{\widetilde W}=\mathfrak c\otimes\nu^*\omega_W,
\]
where the conductor extended to the normalization is \(\mathfrak c=\mathcal O_{\widetilde W}(-B)\). Restricting to an individual normalized component therefore yields the asserted degree \((a+b-4)e-2g+2\). This restriction, rather than a conductor formula for nonreduced fibers, is the correct hypothesis. For a smooth component of a reduced union, the conductor ideal on that component is the ideal of its scheme-theoretic intersection with the complementary reduced curve. The attachment-length formula follows. The union exact sequence then gives the stated residual arithmetic genus, without an assumption of residual irreducibility or smoothness. The note marks those existence questions separately.

The nonreduced examples reconstruct independently. For \(V(L^4,M^4)\), complementary homogeneous coordinates exhibit the rank-sixteen module with shifts \(-i-j\); summing the sixteen linear polynomials gives \(16n-32\). For \(V(L^4,G_4)\) with smooth plane-quartic reduction, the powers of the regular parameter \(L\) have layers \(\mathcal O_D(-j)\), \(0\le j\le3\), and give the same polynomial. Thus the examples really have the stated pure multiple cycles. They establish no analogous existence for the fixed rational-quartic embedding.

## Independent reconstruction of the new smooth-carrier lemma

Suppose a quartic pencil has a member \(F\) smooth everywhere along \(C\). Its first normal symbol \(f\) is a nowhere-zero section of \(N^*_{C/\mathbf P^3}(4)\). If the generic intersection multiplicity is at least two, the second first symbol \(g\) has zero wedge with \(f\). The subbundle generated by \(f\) is \(\mathcal O_C\), so \(g=\lambda f\) with a globally regular function \(\lambda\), necessarily a constant. Thus \(G-\lambda F\) belongs to the actual ideal-sheaf square in degree four. This argument needs neither a pointwise constant ratio assumption nor a splitting of the conormal bundle.

On the smooth quadric \(Q\), the marked curve has type \((1,3)\). Restricting a quartic from \(\mathcal I_C^2\) to \(Q\) gives a section of \(\mathcal O_Q(2,-2)\), which vanishes. Divide by \(q\): the residual quadratic must vanish on \(C\), and restriction to \(Q\) leaves type \((1,-1)\), again with no sections. Hence the residual quadratic is a scalar multiple of \(q\), proving \(H^0(\mathcal I_C^2(4))=kq^2\). Properness makes the new pencil member nonzero.

The divisor of \(F|_Q\) is \(C+C'\) with \(C'\) of type \((3,1)\). Since \((3,1)-(1,3)=(2,-2)\) is not effective, \(C'\) has no \(C\) component. Intersecting with \(q^2\) doubles this divisor, giving \([W]=2[C]+2[C']\), where \([C']\) retains its possible component multiplicities. The multiplicity of \(C\) is exactly two. This confirms the lemma and its contrapositive: multiplicity at least three forces every pencil member to be singular somewhere on \(C\), without forcing a common singular point.

The first-symbol argument for equal degree \(d\) and an arbitrary smooth connected projective marked curve is valid under the same smooth-carrier hypothesis. Its conclusion is membership of a nonzero pencil member in \(H^0(\mathcal I_C^2(d))\); the quartic one-dimensionality cannot be carried into higher degrees without new information.

## Explicit smooth surface, double member, and pencil

For the displayed prescribed \(F,G\), write \(S=F+G=x_1^4+x_2^4-x_0^3x_3-x_0x_3^3\). Its partial derivatives in \(x_1,x_2\) force \(x_1=x_2=0\) at a singular point. The remaining equations would force either all coordinates zero or simultaneously \(x_0^2=-3x_3^2\) and \(3x_0^2=-x_3^2\), impossible in characteristic zero. Thus \(S\) is smooth, and in particular integral.

In Segre coordinates, direct multiplication verifies
\[
S|_Q=(ad^3-bc^3)(a^3d-b^3c).
\]
Each factor defines a graph of a degree-three map of projective lines, hence a smooth rational quartic. Restricting the second factor to the first curve gives \(st(s^8-t^8)\), whose ten distinct zeros prove the stated transverse intersections. Hence the reduced divisor \(D=C\cup C'\) has degree eight and genus nine. On \(S\), it is the Cartier divisor cut by \(q\), so \(\mathcal O_D(-D)=\mathcal O_D(-2)\). The double-divisor exact sequence gives the two polynomials \(8n-24\) and \(8n-8\), with sum \(16n-32\).

The forms \(F,q^2\) are linearly independent modulo \(S\): comparing the coefficients of \(x_1^4\) and \(x_2^4\) in a supposed relation first kills the \(F\) and \(S\) coefficients and then kills the \(q^2\) coefficient. Since \(S\) is integral, every nonzero member cuts a proper Cartier divisor. The resulting family over the full projective pencil is flat and has the two endpoints claimed. This argument does not assert that the remaining residual members of this pencil are smooth.

Finally, adjunction on the smooth quartic gives \(C^2=-2\), and \(C'=2H-C\) gives \(C\cdot C'=10\), agreeing independently with the explicit intersections. The change from eighteen boundary units for a component of a reduced \((4,4)\) curve to ten for a component of the reduced \((2,4)\) support is correctly distinguished.

## Review decision and limitations

No substantive mathematical correction was required. Componentwise normalization notation was suggested for clarity in section 5. All new elementary claims reconstructed above are independently reviewed evidence. The inherited reviewed inputs retain their pre-existing status. This audit proves neither a classification of possible embedded limits nor realization of arbitrary numerical data, and it supplies no unrestricted STCI conclusion.



---
