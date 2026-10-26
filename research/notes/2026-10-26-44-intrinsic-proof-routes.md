# Curve-centered proof routes for multiplicity four

Date: 2026-10-26. Status: exploratory synthesis, an explicit reformulation of an existing proof, and new negative controls; independently reviewed in the [audit](2026-10-26-44-intrinsic-proof-routes-audit.md). No canonical promotion.

## 1. Question and honest distinction

For the fixed characteristic-zero rational quartic
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\]
can multiplicity four in a proper quartic pair be excluded by an argument intrinsic to the marked curve, without a classification of K3 surface singularities?

Two requests should be distinguished. The singularity classification can be removed completely: the equations forced by the marked neighborhood admit direct blowup calculations, and Noether's formula and Hodge theory finish the same global surface obstruction. This is a complete reformulation of the [existing independently audited proof](2026-10-23-intrinsic-44-k3-proof-proposal.md), retaining its [audit](2026-10-23-intrinsic-44-k3-independent-audit.md). It is not a new obstruction or a purely curve-only proof.

A proof using only the embedded infinitesimal neighborhoods and actual quartic source, with no global surface-rank bound, remains missing. Sections 4--6 give concrete reasons why genus, conormal degrees, the quadric restriction, and numerical positivity alone cannot supply it, and state a precise sufficient nonvanishing theorem.

The accepted balanced conormal [R0020](../results/quartic_conormal_characteristic_jump.md), the unique smooth quadric and its ruling classes, and rank-four finite-flat Gorenstein duality are retained. Neither R0001 nor R0022 is used to establish the multiplicity-four contradiction. No inherited proof or certificate is rerun.

## 2. What the marked neighborhood already forces

The hypothetical complete intersection W has degree sixteen and generic multiplicity four along C. Purity and degree imply sole reduced support C. The elementary unique-quadric argument excludes any quartic pencil member of normal order at least two: it would be a multiple of q² and could not yield sole support C on the quadric. Thus the generic algebra is curvilinear of length four.

The existing local multiplication and duality argument gives
\[
L=\mathcal O(e-7),\quad E_2=L^2(D),\quad
E_3=L^3(D)=\mathcal O(-18),\quad \deg D=3-3e.
\]
Here degrees are on the normalization \(C\simeq\mathbf P^1\), with ambient \(\mathcal O_C(4)=\mathcal O(16)\). Effectivity leaves e=1,D=0 or e=0,deg D=3. The common fixed divisor of the actual first normal symbols is exactly D, and the moving pencil has degree \(6+2e\).

At primitive points the exact ambient local ideal is \((m,\ell^4)\). At a defect of multiplicity d it is \((x^2,y^2-t^d x)\). These are derived from rank-four multiplication, not from a classification of surface singularities. The primitive moving-zero calculation gives a general carrier equation \(uv-t^4\). At a defect, the parametric Morse calculation gives \(uv-t^{2d}\). Only exponents 2,4,6 occur. Bertini gives smoothness outside C. These conclusions, including arbitrary local coefficient functions, are proved in the preserved [local-algebra note](2026-10-23-intrinsic-quadruple-local-algebra.md).

## 3. Direct blowups and a classification-free surface bound

Consider the local equation
\[
uv-t^r=0,\qquad r\in\{2,4,6\}.
\]
Blow up the origin in its smooth ambient threefold. In the u-chart, put v=u v1,t=u t1; the strict transform is
\[
v_1-u^{r-2}t_1^r=0,
\]
which is smooth. The v-chart is similar. In the t-chart put u=t u1,v=t v1; the equation is
\[
u_1v_1-t^{r-2}=0.
\]
For r=2 the exceptional curve is a smooth conic. For r>2 the exceptional curve consists of two projective lines; the only remaining singular point lies at their intersection in the t-chart. Repeating this calculation inserts the exceptional curves of the exponent r-2 equation between the two lines. Hence the final exceptional curves form a chain, with counts
\[
N(2)=1,\qquad N(r)=2+N(r-2),\qquad N(r)=r-1.
\]
This directly gives one, three, and five curves for r=2,4,6. No surface-singularity classification is invoked.

Every blowup center is an ambient point at which the strict surface has multiplicity two. If \(\pi\) is such an ambient blowup, its canonical discrepancy is 2E and its strict surface is \(\pi^*S-2E\). Adjunction therefore gives
\[
K_{S'}=\pi^*K_S.
\]
Thus the full explicit resolution is crepant. The original integral quartic has trivial dualizing sheaf by hypersurface adjunction, so the smooth projective resolution \(\widetilde S\) has trivial canonical line bundle, without appealing to a K3 classification or a theorem recognizing rational double points. Integrality and normality follow as in the original proof from the finite singular locus; they are not input assumptions.

The exceptional components are smooth rational curves. Adjunction on the resolution makes their self-intersections -2. The tridiagonal chain matrix is negative definite, with nonzero determinant of absolute value r; the r-1 classes are independent. Different singular points give disjoint chains.

For completeness, the needed global bound can also be derived without naming the surface type. Work over the complex numbers after descent from a finitely generated characteristic-zero coefficient field. Put \(q=h^1(\mathcal O_{\widetilde S})\). Since the canonical line bundle is trivial, \(p_g=1\) and \(\chi(\mathcal O)=2-q\). Noether's formula and Hodge decomposition give
\[
c_2=12(2-q),\qquad
b_2=c_2-2+4q=22-8q,\qquad
h^{1,1}=b_2-2p_g=20-8q\le20.
\]
These are general smooth projective surface identities, not a classification theorem; see [Hacking's surface notes](https://paulhacking.github.io/surfaces.pdf), sections 2,5,6. The pullback hyperplane class has square four and is orthogonal to the exceptional chains. Thus the total exceptional rank is at most \(h^{1,1}-1\le19\).

The marked-neighborhood calculation, however, requires
\[
3(6+2e)+\sum_{p\in\operatorname{Supp}D}(2d_p-1)
=24-\#\operatorname{Supp}D\ge21.
\]
This is a contradiction. It is a complete exclusion with direct local blowups and general Hodge/Noether theory. Its remaining global surface input should not be advertised as a purely C-intrinsic proof.

## 4. A real quadruple with the right lower invariants

Let \(Q\simeq\mathbf P^1\times\mathbf P^1\) be the unique quadric, with C of type (1,3), and take the actual Cartier divisor
\[
Y=4C\subset Q.
\]
It has degree sixteen and
\[
p_a(Y)=1+\tfrac12(4,12)\cdot(2,10)=33.
\]
Its primitive nilpotent layers are
\[
\mathcal O_C,\quad\mathcal O(-6),\quad
\mathcal O(-12),\quad\mathcal O(-18).
\]
Thus it has exactly the Hilbert polynomial and graded-layer degrees of the primitive hypothetical (4,4) structure. Those data cannot alone exclude a quadruple.

Of course Y is not a proper (4,4) intersection: every quartic through it contains Q, since \((4,4)-4(1,3)=(0,-8)\) has no sections. Explicitly,
\[
H^0(\mathcal I_Y(4))=qH^0(\mathcal O_{\mathbf P^3}(2)).
\]
This is already enough to exclude this particular candidate, not all possible marked quadruples.

There is also an intrinsically infinitesimal failure of complete-intersection adjunction. One has
\[
\omega_Y=\mathcal O_Q(2,10)|_Y,\qquad
\omega_Y\otimes\mathcal O_Y(-4)=\mathcal O_Q(-2,6)|_Y.
\]
The discrepancy is trivial on C, but nontrivial even on 2C in characteristic zero. Here is a direct cohomological proof. Put \(M=\mathcal O_Q(-2,6)\). The sequence
\[
0\to\mathcal O_Q(-4,0)\xrightarrow{c_C^2}M\to M|_{2C}\to0
\]
identifies \(H^0(M|_{2C})\) with the kernel of multiplication by \(c_C^2\) on H1. In Segre coordinates C has equation \(ad^3-bc^3\). In natural Cech bases the three-dimensional source maps to the span of
\[
d^6,\quad -2c^3d^3,\quad c^6
\]
in \(H^0(\mathcal O_{\mathbf P^1}(6))\). These sections are independent in characteristic zero, so the map is injective and \(H^0(M|_{2C})=0\). A trivial line bundle would have a nonzero section. Thus the full dualizing sheaf fails to match even though its restriction to C matches. The vanishing of the middle coefficient in characteristic two is informative but is not used as a proof of existence there.

This control shows why a stronger intrinsic proof must retain the nonlinear marked neighborhood and its line-bundle gluing, not only restriction to the reduced C. It gives no assertion that an arbitrary hypothetical W lies in Q.

## 5. The quadric restriction forgets transverse multiplicity

There is a sharper negative control for a proof using only the two residual (3,1) divisors on Q. Set
\[
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,
\quad q=x_0x_3-x_1x_2.
\]
For the actual triple example from the [preceding note](2026-10-26-44-multiplicity-three-forces.md), take \(12r^2+4r+3=0\) and put
\[
a=r+3/2,\quad b=r+1/2,\quad
c=1/6-r,\quad d=r-7/6.
\]
Its equations satisfy the direct identities
\[
R_0=bF+ax_0^2q,\qquad R_1=cG-dx_3^2q.
\]
Hence their restricted pencils on Q are identical up to nonzero basis scalars. Nevertheless \(m_C(V(F,G))=1\), while \(m_C(V(R_0,R_1))=3\). The same residual ruling divisors and base scheme on Q can therefore have different transverse multiplicities in projective space. Restriction to Q loses precisely some of the necessary normal lifting information.

## 6. The exact C-neighborhood target

The existing [intrinsic cubic-contact construction](2026-10-23-intrinsic-cubic-contact-construction.md) formulates a genuinely marked-neighborhood obstruction. For a quasiprimitive triple T with ideal J define
\[
\mathcal M_T=(J/I_CJ)/\mathrm{torsion}.
\]
The actual two-dimensional source W of quartic equations gives
\[
\rho_T:W\otimes\mathcal O_C\longrightarrow\mathcal M_T(4).
\]
Its determinant is a section of degree four or six in the two adjunction-allowed cases. At generic contact at least three, with a nonzero first symbol,
\[
\det\rho_T\ne0\iff m_C(V(W))=3.
\]
A fully C-neighborhood proof would show that every proper actual quartic source in the allowed types has nonzero determinant, using the full embedded transition and without enumerating triple directions or quartic pencils. This is a precise sufficient statement, not a proved new theorem here. The established coordinate contact proof proves it using those classifications; the intrinsic construction alone does not.

Positivity of the determinant line is insufficient. The contact note gives abstract models \(\mathcal M_T(4)=\mathcal O(2)^2\) or \(\mathcal O(3)^2\), with the relevant exact-sequence degrees, in which two independent sections lie in a single summand and have zero wedge. Such models are not claimed realizable by the actual embedding. They identify why the actual source is indispensable.

For the primitive e=1 branch there is also a geometric normal-bundle formulation. After three successive blowups along C and its prescribed normal-direction sections, the remaining reduced base curve C3 is isomorphic to C. The transformed quartic line bundle restricts to \(\mathcal O_C(-2)\). Two actual generators of its ideal would force
\[
N_{C_3/X_3}\simeq\mathcal O(-2)^2.
\]
The numerical normal sequence is only
\[
0\to\mathcal O(-10)\to N_{C_3/X_3}\to\mathcal O(6)\to0,
\]
which permits that balanced middle bundle. Proving the actual extension from this embedding cannot be balanced would be a sufficient intrinsic obstruction in this primitive branch; the defective branch would still require its own treatment. Numerical splitting or positivity cannot be assumed. This is an alternative necessary condition, not an equivalence to global quartic realization.

## 7. Status and continuation

The direct-resolution reformulation is complete and avoids the classification of surface singularities and of K3 surfaces, while retaining a global Hodge/Noether bound. It is a refinement of the existing proof's exposition, not a stronger scope result. The marked-neighborhood-only nonvanishing remains unresolved by these deductions. The negative controls and normal-bundle criterion make that missing implication explicit. No canonical exclusion is reopened or promoted, no inherited experiment is rerun, and no all-degree STCI conclusion follows.
