# Intrinsic local algebra and characteristic-zero quartic geometry

## Integration guide: first symbols, complete filtrations, and (4,4) exclusion

The [ideal-filtration investigation](#2026-10-23-ideal-filtrations-independent-investigationmd) records the full marked embedding and an explicit failure of the proposed general first-order-to-higher-generator correspondence. The [filtered (4,4) proposal](#2026-10-23-quartic-44-filtered-proof-proposalmd) and [independent audit](#2026-10-23-quartic-44-filtered-proof-independent-auditmd) instead use additional specific numerical, classification, and global quartic-contact input. These are not contradictory: a special filtered exclusion may hold without the false general correspondence.

The alternative [surface-singularity route](../synthesis/quartic_pair_obstruction.md#4-direct-blowups-and-the-global-contradiction) replaces the global contact determinant with a characteristic-zero exceptional-rank contradiction, while retaining the local defect algebra. [The genus-budget synthesis](INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md#cross-supplement-synthesis-distinct-44-obstruction-routes-editorial-not-a-new-audit) contrasts both approaches with lower-multiplicity residual examples. [Delta embedding](DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-embedding-geometry-report) and [normal flatness](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness) give broader filtration frameworks, each with independent scope restrictions.

Keep the original computational checks, correction freedoms, counterexample, and audit status below. This guide does not extend any (4,4) conclusion to arbitrary degrees.

---


Full mathematical investigations retained by subject. Proposals, independent reviews, limitations and rejected mathematical approaches retain their original epistemic status. This compilation is not a new proof audit.


---

## 2026-10-23-ideal-filtrations-independent-investigation.md

# Independent investigation: ideal filtrations and the nine-embedding diagram

Date: 2026-10-23. Status: **research proposal and independent assessment**.

Scope: distinct integral hypersurfaces \(X,Y\subset P=\mathbf P^3_k\), their scheme intersection \(Z\), and a specified reduced closed subscheme \(C\subset Z\). Distinguish \(C=Z_{\mathrm{red}}\) from a marked component \(C\subsetneq Z_{\mathrm{red}}\). Statements identifying \(\operatorname{Sym}(I/I^2)\) with \(\operatorname{gr}_I\mathcal O_P\) additionally assume \(C\hookrightarrow P\) regular. The explicit marked rational quartic is smooth. Local counterexamples are local examples, not global constructions for that fixed projective quartic.

The original request specified no repository edits. The subsequent instruction, “pls save your work in a branch,” authorizes this report and its evidence on a separate branch. No accepted proof, result, or question is changed.

## 1. Verdict and scope corrections

The framework is useful as a coordinated study of **the actual filtered intersection and its normal degeneration**. Most constructions are standard conormal, normal-cone, standard-basis, Rees, Koszul, and cotangent-complex mathematics. This investigation does not establish novelty.

The strongest completeness formulation is tautological: retaining the actual nine-embedding scheme diagram already retains \(Z\hookrightarrow P\). Even retaining all nine graded algebras with their original bases and ambient quotient maps retains \(\mathcal O_Z\) in degree zero. The substantive question is whether reduced normal data determine the filtered intersection. They do not, even for local intersections of integral hypersurfaces with smooth reduced support.

The lifting filtration is sound after an intrinsic reformulation. Its comparison with minimal initial equations is a canonical surjection, with an explicit defect:
\[
0\longrightarrow\Delta_n\longrightarrow Q_n
\longrightarrow\operatorname{gr}^n_F(J/IJ)\longrightarrow0,
\qquad
\Delta_n=\frac{\operatorname{in}_n(IJ)}{(S_+H)_n}.
\tag{1}
\]
A two-generator complete intersection can have a nonzero \(Q_4\) invisible in this filtered equation module. Section 5 proves this.

For the prescribed characteristic-two quartic pair, the special equality \(\operatorname{in}_I(IJ)=S_+H\) does hold. There is a canonical isomorphism
\[
\ker\phi\simeq Q_4\simeq\mathcal O_{\mathbf P^1}(-24).
\]
The transition calculation verifies compatibility, rather than merely matching degrees.

More generally, section 4.3 proves that the comparison defect is supported only where both carriers are singular along the smooth curve. This explains the favorable behavior of the prescribed pair without treating it as a universal first-order principle.

Three scope corrections are essential:

1. Require \(X\ne Y\). Integral hypersurfaces can coincide. Distinctness makes \(F,G\) a regular sequence; \(Z\) is then a pure one-dimensional Cohen–Macaulay complete intersection. It has no embedded associated components, although it may be nonreduced. Embedded or vertical features in a normal cone are different assertions.
2. The characteristic-zero example uses a marked component. Its smooth quartic \(C\) is one of four geometric components of \(Z_{\mathrm{red}}\). Using the whole reduced union changes \(I\), its conormal sheaf, and its graded algebra.
3. Regularity of \(C\hookrightarrow P\) is additional. A general reduction can be singular or reducible. There is always a surjection \(\operatorname{Sym}(I/I^2)\twoheadrightarrow\operatorname{gr}_I\mathcal O_P\), but it need not be an isomorphism.

The unrestricted characteristic-zero STCI question is outside this investigation. No new proof of it is attempted or implied.

## 2. The complete embedding and conormal diagram

### 2.1 All nine ideals and their bases

Use sheaves throughout; affine expressions denote local realizations. Set
\[
R=\mathcal O_P,\quad A=I_X,\quad B=I_Y,\quad
J=A+B,\quad I=I_C,\quad A,B\subset J\subset I.
\]

The diagram has five immediate arrows and four composites:

~~~mermaid
flowchart TD
    C["C"] --> Z["Z"]
    Z --> X["X"]
    Z --> Y["Y"]
    X --> P["P"]
    Y --> P
    C --> X
    C --> Y
    C --> P
    Z --> P
~~~

The square \(Z\to X,Y\to P\) is Cartesian. Every triangle using a composite arrow commutes. Both length-four routes from \(C\) to \(P\) agree with the direct arrow.

| Embedding | Ideal in its actual ambient ring | Conormal sheaf | Base |
|---|---|---|---|
| \(X\hookrightarrow P\) | \(A\subset R\) | \(A/A^2\) | \(X\) |
| \(Y\hookrightarrow P\) | \(B\subset R\) | \(B/B^2\) | \(Y\) |
| \(Z\hookrightarrow P\) | \(J\subset R\) | \(J/J^2\) | \(Z\) |
| \(C\hookrightarrow P\) | \(I\subset R\) | \(I/I^2\) | \(C\) |
| \(Z\hookrightarrow X\) | \(J/A\subset R/A\) | \(J/(J^2+A)\) | \(Z\) |
| \(Z\hookrightarrow Y\) | \(J/B\subset R/B\) | \(J/(J^2+B)\) | \(Z\) |
| \(C\hookrightarrow X\) | \(I/A\subset R/A\) | \(I/(I^2+A)\) | \(C\) |
| \(C\hookrightarrow Y\) | \(I/B\subset R/B\) | \(I/(I^2+B)\) | \(C\) |
| \(C\hookrightarrow Z\) | \(K=I/J\subset R/J\) | \(I/(I^2+J)\) | \(C\) |

Each row carries its own full ideal-power filtration. For example, degree \(n\) for \(Z\hookrightarrow X\) is \((J^n+A)/(J^{n+1}+A)\), on \(Z\). For \(C\hookrightarrow Z\) it is \((I^n+J)/(I^{n+1}+J)\), on \(C\). These are different filtrations.

### 2.2 Every composable triple and its precise exactness

For ideals \(L\subset M\subset Q\), the chain
\(\operatorname{Spec}(Q/M)\hookrightarrow\operatorname{Spec}(Q/L)\hookrightarrow\operatorname{Spec}Q\)
gives
\[
0\to\frac{L\cap M^2}{LM}
\to\frac{L}{LM}\to\frac{M}{M^2}
\to\frac{M}{M^2+L}\to0.
\tag{2}
\]
This follows by taking the kernel and cokernel of the inclusion-induced map \(L/LM\to M/M^2\). The middle three terms form the usual right-exact conormal sequence. See [Stacks, conormal transitivity](https://stacks.math.columbia.edu/tag/01R1) and [exactness qualifications](https://stacks.math.columbia.edu/tag/06BB).

There are exactly seven strict triples:

| Chain \((U,V,W)\) | Ambient ring \(Q\) | \(L=I_{V/W}\) | \(M=I_{U/W}\) |
|---|---|---|---|
| \((Z,X,P)\) | \(R\) | \(A\) | \(J\) |
| \((Z,Y,P)\) | \(R\) | \(B\) | \(J\) |
| \((C,X,P)\) | \(R\) | \(A\) | \(I\) |
| \((C,Y,P)\) | \(R\) | \(B\) | \(I\) |
| \((C,Z,P)\) | \(R\) | \(J\) | \(I\) |
| \((C,Z,X)\) | \(R/A\) | \(J/A\) | \(I/A\) |
| \((C,Z,Y)\) | \(R/B\) | \(J/B\) | \(I/B\) |

Substituting in (2) determines every first-arrow kernel, image, and cokernel. The two length-four chains give their naturality compatibilities.

For the first two rows regularity of \(F,G\) gives, on \(Z\),
\[
J/J^2\simeq(A/A^2)|_Z\oplus(B/B^2)|_Z.
\tag{3}
\]
For example \(A\cap J^2=AJ\), so the first map for \(Z\to X\to P\) is injective. Analogous maps involving \(C\) need not be injective.

### 2.3 The central first-order diagram

On \(C\), put
\[
M_A=A/IA,\quad M_B=B/IB,\quad
D=J/IJ=(J/J^2)|_C,\quad E=I/I^2.
\]
Then \(D=M_A\oplus M_B\). If \(d=\deg F,e=\deg G\), these source lines are \(\mathcal O_P(-d)|_C,\mathcal O_P(-e)|_C\). Let
\(\alpha:M_A\to E,\ \beta:M_B\to E\). The central map is \(\phi=(\alpha,\beta)\), with exact defects
\[
\ker\phi=\frac{J\cap I^2}{IJ},\qquad
\operatorname{coker}\phi=\frac{I}{I^2+J}=N^*_{C/Z}.
\tag{4}
\]

Write \(E_X=I/(I^2+A)\), \(E_Y=I/(I^2+B)\), \(E_Z=I/(I^2+J)\). Naturality gives
\[
\begin{array}{ccccc}
M_A&\longrightarrow&D&\longrightarrow&M_B\longrightarrow0\\
\Vert&&\downarrow\phi&&\downarrow\bar\beta\\
M_A&\xrightarrow{\alpha}&E&\longrightarrow&E_X\longrightarrow0,
\end{array}
\tag{5}
\]
and the symmetric diagram. The top row is split exact; the bottom is right exact. The sequence \(M_B\to E_X\to E_Z\to0\) is the chain \(C\to Z\to X\); its first kernel is
\[
\frac{A+(J\cap I^2)}{A+IJ}.
\]
The other route is symmetric.

For an exact diagram use the images \(U=\operatorname{im}\alpha\), \(V=\operatorname{im}\beta\). The quotient square
\[
\begin{array}{ccc}
E&\longrightarrow&E/U=E_X\\
\downarrow&&\downarrow\\
E/V=E_Y&\longrightarrow&E/(U+V)=E_Z
\end{array}
\]
is a pushout of modules. Its failure to be a pullback is measured by \(U\cap V\):
\[
0\to U\cap V\to E\to E_X\oplus E_Y\to E_Z\to0,
\tag{6}
\]
where the last arrow is the difference of quotient maps. There is a genuine exact \(3\times3\) diagram whose rows are
\[
(U\cap V,\ U,\ (U+V)/V),\quad
(V,\ E,\ E/V),\quad
(V/(U\cap V),\ E/U,\ E/(U+V)).
\]
Each row and column is short exact. Replacing \(U,V\) by their source lines without retaining \(\ker\alpha,\ker\beta\) invalidates this.

### 2.4 Higher maps and exactness

There is no reason all natural arrows form one complex. The following formulas cover the relevant families.

For \(L\subset M\), the degree-\(n\) map \(\operatorname{gr}_LQ\to\operatorname{gr}_MQ\) has kernel
\((L^n\cap M^{n+1})/L^{n+1}\) and image
\((L^n+M^{n+1})/M^{n+1}\). After restricting the source to \(Q/M\), its source is \(L^n/ML^n\) and kernel
\[
\frac{L^n\cap M^{n+1}}{ML^n}.
\tag{7}
\]
For passage to an ambient quotient \(Q/L\), the induced \(M\)-filtration gives the quotient by the full initial ideal of \(L\), not just by initials of chosen generators.

Multiplication \(M^r/M^{r+1}\otimes M^s/M^{s+1}\to M^{r+s}/M^{r+s+1}\) is canonical; its kernels are relations and no injectivity is automatic. Restriction is tensor product and is right exact. For a short exact sequence its possible new left kernel is the image of a \(\operatorname{Tor}_1\) connecting map. Section 7 exhibits this explicitly.

## 3. The central normal-cone sequence

Set \(S=\operatorname{gr}_IR\) and
\[
H_n=\frac{J\cap I^n}{J\cap I^{n+1}}\hookrightarrow S_n.
\]
Multiplication makes \(H=\bigoplus H_n\) a homogeneous ideal. Since \(K^n=(I^n+J)/J\), taking the kernel of \(I^n/I^{n+1}\to(I^n+J)/(I^{n+1}+J)\) proves
\[
0\to H_n\to S_n\to K^n/K^{n+1}\to0,\qquad
0\to H\to S\to\operatorname{gr}_K(R/J)\to0.
\tag{8}
\]
No regularity assumption on \(I\) is needed.

This is an excellent organizing sequence and also the classical form-ideal sequence. Valabrega–Valla, *Form rings and regular sequences*, §1, pp. 94–95, already gives this kernel description and an intersection criterion for initials of chosen generators to generate the full form ideal ([original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F91724E40BE6AE7101C7A959AFC3DA05/S0027763000018225a.pdf/form-rings-and-regular-sequences-1.pdf)). The framework should use that established theory.

If \(C\to P\) is regular, \(S=\operatorname{Sym}E\); geometrically (8) embeds \(C_{C/Z}\) in \(N_{C/P}\). See [Stacks, normal cones](https://stacks.math.columbia.edu/tag/062Z).

For \(n\ge1\),
\[
Q_n=H_n/(S_+H)_n,\qquad
(S_+H)_n=\sum_{i=1}^{n-1}S_iH_{n-i}
\tag{9}
\]
is the module of minimal initial equations. It need not be locally free. Over a nonfield base its rank alone does not determine its local generators. It does not retain the syzygies among the equations.

For regular \(J\), the map in the question is
\[
\operatorname{Sym}^nD=J^n/IJ^n\longrightarrow S_n.
\]
Its image is \((\operatorname{im}\phi)^n=(H_1)^n\): products of \(n\) first-order symbols. This is neither all of \(H_n\) nor necessarily \(S_{n-1}H_1\). Its kernel is (7) for \(L=J,M=I\). In characteristic two these maps see powers of \(V\) and miss the new equation \(U^4\).

## 4. Lifting filtration: intrinsic form and exact comparison

### 4.1 The intrinsic filtered equation module

The [intrinsic filtration and the presentation-syzygy proof](../arguments/filtered_equation_comparison.md#full-normal-equations-and-the-actual-equation-module)
use the actual ideal module \(J/IJ\).

### 4.2 The denominator, and the direction of the canonical map

The [denominator and canonical surjection](../arguments/filtered_equation_comparison.md#full-normal-equations-and-the-actual-equation-module)
give the exact comparison (1). [R-0030](../results/local_filtration_comparison_defect.md)
states the local claim and separates its generic count and punctual length formula.

### 4.3 A proved sufficient condition: one smooth carrier

The [smooth-carrier proof](../arguments/filtered_equation_comparison.md#smooth-carrier-vanishing)
straightens one carrier and computes both full initial ideals over the
completed local coefficient domain.

## 5. Counterexample to the general first-order/higher-generator correspondence

The [length-five quotient and filtered Koszul calculation](../arguments/filtered_equation_comparison.md#a-minimal-initial-equation-erased-by-the-comparison)
give the degree-four initial equation erased by passage to \(J/IJ\).
See the exact [counterexample statement](../results/initial_equation_cancellation_counterexample.md).

## 6. Completeness: exactly which data suffice?

### 6.1 Actual ideals and the literal full graded diagram

Actual inclusions \(A,B\subset R\) determine \(J=A+B\) and the embedded \(Z\). A filtered \(\mathcal O_P\)-algebra with its actual underlying algebra, quotient map, and multiplication also retains that algebra.

For “only graded data,” observe
\[
(\operatorname{gr}_JR)_0=R/J.
\tag{16}
\]
If the full nine-graded diagram includes the original bases and \(R\to(\operatorname{gr}_JR)_0\), its kernel is \(J\). If only an abstract graded algebra is retained, degree zero still gives abstract \(Z\), but the embedding needs the ambient map. If the actual scheme diagram is retained, completeness precedes all filtration constructions.

Thus different embedded intersections cannot have isomorphic full nine-graded diagrams over the identity of fixed \(P\), with all degree-zero quotient maps retained. A same-initial-ideal example cannot disprove this stronger assertion.

### 6.2 Different intersections with identical graded diagrams after restriction to \(C\)

The [restricted normal diagram counterexample](../results/restricted_normal_diagram_counterexample.md)
gives both integral hypersurface presentations, the nine graded algebras
and their maps after restriction to \(C\), and the intrinsic square-zero
distinction between the actual intersection rings.

### 6.3 Compatible actual neighborhoods and completions

If \(C=Z_{\mathrm{red}}\), noetherian quasi-compactness gives \(K^N=0\), equivalently \(I^N\subset J\), for some uniform \(N\); see [Stacks, nilpotent ideals](https://stacks.math.columbia.edu/tag/00IM). Thus the actual embedded tower
\[
Z_n=V(J+I^{n+1})\subset P
\tag{19}
\]
stabilizes at \(Z\) for \(n+1\ge N\). The compatible tower with its algebra structures determines \(Z\); its maps to \(P\) determine the embedding. Graded layers do not.

No universal finite truncation exists without a nilpotence bound. Smooth integral hypersurfaces \(X=V(v)\), \(Y_m=V(v+u^m)\) have \(J_m=(v,u^m)\). For fixed \(N<m,m'\), their towers through order \(N\) agree although generic transverse lengths are \(m,m'\).

A formal closed thickening whose ideal contains \(\widehat I^N\) already defines a coherent ideal in the algebraic finite neighborhood \(V(I^N)\), hence a closed subscheme of \(P\). A blanket algebraization warning is therefore wrong for this finite supported case. This reconstruction does not supply global integral hypersurface generators of specified degrees.

If \(C\) is only a marked proper component, completion of \(J\) alone can miss components away from \(C\). For example \((v,u)\) and \((v,u(u-1))\) have equal completions along \((u,v)\); the latter has an extra disjoint line. Each is an intersection of integral smooth affine hypersurfaces, using \((v,u)\) and \((v,v+u(u-1))\).

This does not make the full completed hypersurface-pair diagrams identical. In the stated integral setting, the completed ideals of each hypersurface inside the same fixed completed ambient \(P\) determine the global hypersurfaces uniquely. Faithful completion gives equality of stalks at \(p\in C\); local prime ideals contract to equal primes in an affine neighborhood. The hypersurfaces share an open piece and their scheme-theoretic closures in \(P\) coincide. Apply separately to \(A,B\). The required facts are [faithful flatness of completion](https://stacks.math.columbia.edu/tag/00MC) and [exactness on finite modules](https://stacks.math.columbia.edu/tag/00MB).

This is uniqueness for algebraic pairs with fixed ambient marking. It does not say arbitrary formal hypersurfaces algebraize, or formal ambient automorphisms extend globally.

### 6.4 The missing information and its repair

Passing to the normal graded object loses the compatible algebra extensions assembling the layers: higher equation terms and nonlinear transition functions. The central normal cone along \(C\) alone does not reconstruct the filtered intersection.

The smallest practical repair is to retain actual compatible neighborhood algebras and their embedded gluing. A uniform package is the extended Rees construction
\[
\widetilde{\mathcal R}_I(R)=\sum_{n\in\mathbf Z}I^nt^{-n}
\subset R[t,t^{-1}],\qquad I^n=R\ (n\le0),
\]
with induced ideal \(\widetilde J=\sum(J\cap I^n)t^{-n}\). There is an exact Rees sequence
\[
0\to\widetilde J\to\widetilde{\mathcal R}_I(R)
\to\widetilde{\mathcal R}_K(R/J)\to0.
\tag{20}
\]
Its fiber at \(t=0\) is (8); its fiber at \(t=1\) is \(0\to J\to R\to R/J\to0\). This is the algebra of deformation to the normal cone; see [Vakil, Intersection Theory class 14, §3](https://math.stanford.edu/~vakil/245/245class14.pdf).

Completeness of this package is built in because a nonzero fiber includes the original algebra. Its value is compatible bookkeeping. Retain the labelled subideals \(A,B\) if the carriers matter. Their induced \(I\)-filtrations differ from their own ideal-adic filtrations. Naively homogenizing only displayed generators may require saturation by the deformation parameter to recover cancellation-generated equations.

## 7. Explicit rational quartic audit

Every \(\mathcal O(n)\) here means \(\mathcal O_{\mathbf P^1}(n)\); ambient \(\mathcal O_P(d)|_C=\mathcal O(4d)\). The curve is \([s:t]\mapsto[s^4:s^3t:st^3:t^4]\) and the equations are \(F=x_1^4-x_0^3x_3\), \(G=x_2^4-x_0x_3^3\).

[R0020](../results/quartic_conormal_characteristic_jump.md) and [R0021](../results/quartic_mu4_degeneration.md) cover the splitting and explicit degeneration. The [prescribed family argument](../arguments/quartic_specialization_and_symbols.md#the-prescribed-mu4-intersection-and-actual-quartic-symbols) retains the scope of the geometry/symbol audit consulted here. The chart calculations below independently reconstruct the requested formulas and lifting compatibility; unrelated accepted exclusions are not rerun.

### 7.1 Exact equations and overlap

On \(x_0\ne0\), use \((a,u,v)\) from the request:
\[
F_0=-v,\qquad
G_0=u^4+4a^3u^3+6a^6u^2+4a^9u-3a^8v-3a^4v^2-v^3.
\]
Thus \(J=(v,h)\), \(h=(a^3+u)^4-a^{12}\).

On \(x_3\ne0\), put \(b=x_2/x_3\), \(A=x_0/x_3-b^4\), \(B=x_1/x_3-b^3\). Then \(G_\infty=-A\) and
\[
F_\infty=B^4+4b^3B^3+6b^6B^2+4b^9B-3b^8A-3b^4A^2-A^3.
\]
These charts cover \(Z\): \(x_0=x_3=0\) forces \(x_1=x_2=0\).

Writing \(V,U\) for the conormal classes of \(v,u\), the first-order overlap is
\[
\begin{pmatrix}A\\B\end{pmatrix}
=\begin{pmatrix}3a^{-8}&-4a^{-7}\\2a^{-7}&-3a^{-6}\end{pmatrix}
\begin{pmatrix}V\\U\end{pmatrix}.
\tag{21}
\]
The determinant is \(-a^{-14}\). In characteristic zero choose
\[
w_0=V-\tfrac32aU,\ z_0=U,\quad
w_\infty=B/2,\ z_\infty=2A-3bB.
\]
Then \((w_\infty,z_\infty)=a^{-7}(w_0,z_0)\). In characteristic two (21) is diagonal, \((A,B)=(a^{-8}V,a^{-6}U)\). This recovers \(E=\mathcal O(-7)^2\) in characteristic zero and \(E=\mathcal O(-8)\oplus\mathcal O(-6)\) in characteristic two.

### 7.2 Characteristic zero

The conormal matrices in frames \((V,U)\), respectively \((A,B)\), are
\[
\phi_0=\begin{pmatrix}-1&-3a^8\\0&4a^9\end{pmatrix},
\qquad
\phi_\infty=\begin{pmatrix}-3b^8&-1\\4b^9&0\end{pmatrix}.
\tag{22}
\]
Thus \(\ker\phi=0\), and near the first endpoint
\(\operatorname{coker}\phi=(k[a]/a^9)U\), with length nine also at infinity. Its total length is eighteen, determinant divisor \(9p_0+9p_\infty\).

The full initial ideal and relative algebra are
\[
H|_{U_0}=(V,a^9U),\qquad
\operatorname{gr}_K\mathcal O_Z|_{U_0}=k[a,U]/(a^9U).
\tag{23}
\]
For fullness, eliminate \(v\). In the domain \(k[a]\), the lowest \(u\)-term of any nonzero multiple of \(h\) is the product of the lowest terms. Lifting back adds \(V\). The ideal is generated in degree one, so \(Q_n=0\) for \(n\ge2\).

At generic \(C\), \(a\) is invertible and there is no positive graded part: the generic transverse length is one. Every global positive graded piece is torsion of length nine at each endpoint. The vertical normal-cone directions are not extra curve components downstairs.

Over a splitting field, the actual intersection is the reduced union
\[
C_\zeta=[s^4:s^3t:\zeta st^3:t^4],\qquad\zeta^4=1.
\]
Complete-intersection purity and generic reducedness on these four degree-four components rule out further nilpotent or embedded structure. Each branch has \(v=0,u=(\zeta-1)a^3\); at infinity \(A=0,B=(\zeta-1)b^3\). Each pair meets with length three at each endpoint. The marked curve meets the other three jointly in \(9p_0+9p_\infty\). Four smooth plane branches give \(\delta=6\cdot3=18\) at each endpoint, hence arithmetic genus \(36-4+1=33\). Without fourth roots in \(k\), geometric components are grouped by Galois action.

Although the kernel sheaf in (22) is zero, its endpoint fiber map has a one-dimensional kernel. Tensor product introduces a kernel through the torsion cokernel. Similarly, taking the ambient slice \(a=0\) gives
\[
\operatorname{gr}_K(\mathcal O_Z|_{U_0})\otimes_{k[a]}k=k[U],
\quad
\operatorname{gr}_{(u,v)}(\mathcal O_Z|_{U_0}\otimes_{k[a]}k)=k[U]/(U^4),
\]
where \(k[a]\to k\) sends \(a\) to zero. Normal associated graded formation does not commute with this base change. The tensor product here uses the ambient chart projection to \(\operatorname{Spec}k[a]\); no intrinsic retraction \(Z\to C\) is assumed.

### 7.3 Characteristic two and the canonical fourth-order identification

The [characteristic-two fourth equation proof](../results/quartic_char2_fourth_equation_kernel.md#proof)
gives both exact corrected lifts, the comparison in degree four, and the
nonlinear overlap on the full embedded intersection.

### 7.4 Invariants that distinguish the fibers

| Invariant relative to marked \(C\) | Characteristic zero | Characteristic two |
|---|---|---|
| Geometric reduced support | Four quartics | Fixed quartic |
| Generic transverse length | \(1\) | \(4\) |
| Kernel sheaf of \(\phi\) | \(0\) | \(\mathcal O(-24)\) |
| Cokernel sheaf | Length \(9+9\) torsion | \(\mathcal O(-6)\) |
| Full initial ideal on first chart | \((V,a^9U)\) | \((V,U^4)\) |
| Higher minimal equations | None after degree one | \(Q_4=\mathcal O(-24)\) |
| \(K\)-adic filtration | Not nilpotent | \(K^4=0\) |

These explain the prescribed pair. Characteristic-zero normal data record combined residual contact, not the individual residual equations or their factorization. They do not decide arbitrary other global pairs.

## 8. Organizational alternatives

### 8.1 Ordinary exact diagrams

The nine-object table, master sequence (2), central sequence (8), and [filtered equation module](../arguments/filtered_equation_comparison.md#full-normal-equations-and-the-actual-equation-module) suffice for most immediate calculations. They preserve carrier symmetry, identify noninjective maps, and avoid imposing nonexistent exactness on a large diagram. The invariants are familiar; the contribution is disciplined compatibility and scope.

### 8.2 Filtered Koszul complexes

The global Koszul complex has terms
\[
\mathcal O_P(-d-e)\longrightarrow
\mathcal O_P(-d)\oplus\mathcal O_P(-e)\longrightarrow\mathcal O_P
\]
and resolves \(\mathcal O_Z\). Equip it with compatible \(I\)-filtrations; locally shift generator weights by their normal orders when appropriate. Its associated graded complex can fail to resolve \(\operatorname{gr}_K\mathcal O_Z\). Higher differentials express cancellations and new initial equations.

For a transparent example take \(f=x,g=x+y^m\), \(m\ge2\), along \(I=(x,y)\). The C-restricted first-order and relative cotangent diagrams are independent of \(m\), but intersection length is \(m\). Assign both generators weight one. The graded Koszul complex sees \((X,X)\); its relation has first nonzero higher differential
\[
d_{m-1}(e_g-e_f)=Y^m
\]
using \(E_0=\operatorname{gr}\), \(E_1=H(E_0)\). The limit recovers \(S/(X,Y^m)\). This is a concrete reason to retain the filtered complex.

At a fixed finite truncation the filtrations are finite and convergence is elementary. For an untruncated formal statement require separatedness, completeness, and the relevant convergence hypotheses. A spectral-sequence limit gives the graded target; its pages alone do not solve the remaining extension problem. See [Stacks, filtered complexes](https://stacks.math.columbia.edu/tag/012K).

Standard bases already organize lifting of leading syzygies and correction terms; see Robbiano, *On the theory of graded structures*, introduction and §3 ([original preprint](https://archive.mpim-bonn.mpg.de/2939/1/preprint_1985_17.pdf)). Global calculations must also retain actual homogeneous source spaces and twists. Calculating only over \(k(C)\) can lose special-point torsion and need not produce global equations.

### 8.3 Cotangent complexes and transitivity

For each composable triple there is a triangle
\[
Li^*L_{V/W}\longrightarrow L_{U/W}\longrightarrow L_{U/V}
\longrightarrow Li^*L_{V/W}[1].
\]
The triangles are compatible with both routes through \(X,Y\). These are standard constructions: [Stacks, fundamental triangle](https://stacks.math.columbia.edu/tag/08QR), [lci cotangent complex](https://stacks.math.columbia.edu/tag/08SH).

When \(C\to P\) and \(Z\to P\) are regular,
\[
L_{C/Z}\simeq[D\xrightarrow{\phi}E]
\quad\text{in cohomological degrees }-2,-1.
\tag{26}
\]
Indeed \(L_{Z/P}=(J/J^2)[1]\), \(L_{C/P}=E[1]\); take the transitivity cone. Thus
\(\mathcal H^{-2}=\ker\phi\), \(\mathcal H^{-1}=\operatorname{coker}\phi\).
This retains the lost left defect and supplies obstruction theory. It does not recover higher \(Q_n\) or nonlinear gluing: the family \((x,x+y^m)\) has identical (26).

The whole configuration can be organized in an enhanced derived category with compatible filtrations. The enhancement supplies coherent transitivity, not a completeness theorem for ranks, homology sheaves, or isolated Ext groups. Algebra structure and compatible extension data remain necessary.

### 8.4 Ordinary versus derived intersections

The derived intersection is \(\mathcal O_X\otimes_{\mathcal O_P}^{\mathbf L}\mathcal O_Y\). Here higher Tor vanishes: resolve one hypersurface by its one-equation resolution; its equation remains a nonzerodivisor on the other distinct integral hypersurface. Thus the derived intersection equals ordinary \(Z\), including its multiplicities.

For coincident components, nonproper intersections, or base-change problems, higher Tor can matter. Derived self-intersections also can have higher Tor even though this \(X,Y\) intersection is Tor-independent. These are different questions.

### 8.5 Rees, multigrading, and homotopy diagrams

The Rees package (20) is the simplest uniform comparison of actual intersection with normal degeneration retaining extension data. Attach cotangent triangles to deformation questions and filtered Koszul to cancellation calculations.

Multi-Rees constructions can record products \(I^rA^sB^t\), but do not automatically encode intersection filtrations \(J\cap I^n\); these must be supplied or recovered with the appropriate saturation. Extra gradings are not needed for the findings here.

Homotopy pullbacks or totalizations give no demonstrated additional invariant for this Tor-independent pair. They should be introduced only after specifying which descent, compatibility, or obstruction problem they solve. A single diagram in \(D(\mathcal O_C)\) would discard the original bases explicitly required here; work with the diagram of ringed spaces or with sheaves of derived algebras on \(P\) if such an enhancement is needed.

## 9. Recommendation and the smallest next question

Retain the actual scheme diagram and labelled ideals \(A,B,J,I\). Use the strict filtered sequence \(0\to J\to R\to R/J\to0\), equivalently its Rees form (20), as the main object. Its normal fiber (8) is the calculable degeneration. Attach the intrinsic filtered equation module, comparison (1), and cotangent triangles when needed.

Retain the bases \(X,Y,Z,C\). Replace presentation-based \(T^{(n)}\) by intrinsic \(F^nD\). Abandon the unconditional correspondence of first-order kernels with all higher initial equations. Do not treat the \(C\)-restricted normal graded algebras, spectral-sequence graded limits, or lists of bundle degrees as reconstructions of the embedded intersection.

The smooth-carrier proposition already supplies a geometric vanishing criterion. The most focused remaining question is:

> At the simultaneous singular points of two carriers along a smooth marked curve, what local conditions determine \(\Delta=\operatorname{in}_I(IJ)/(S_+H)\), and can its length and degrees be read from the filtered Koszul cancellations?

This investigation proves vanishing off that locus and failure even for integral local hypersurfaces on it. A useful next result should describe this remaining defect, beyond another isolated degree calculation.

The following precise tasks would establish further usefulness:

1. Refine [smooth-carrier vanishing](../arguments/filtered_equation_comparison.md#smooth-carrier-vanishing) by describing the defect at simultaneous singular points, with precise hypotheses and counterexamples.
2. Construct a global sheaf-level filtered standard-basis or Koszul calculation retaining homogeneous source spaces, and identify its higher differentials with actual symbol corrections across overlaps.
3. For a prescribed normal graded algebra, specify the algebra-extension and nonlinear gluing classes needed to reconstruct an embedded finite thickening, separating that reconstruction from the existence of global integral carrier equations.
4. Show that one of these constructions supplies a new obstruction, completes a finite calculation, or simplifies a proof in a scope not already covered. Notation or a larger diagram alone would not establish that usefulness.

The direction is worthwhile as rigorous organizational and computational language. Its demonstrated value here is the exact distinction between first-order relations, higher initial generators, and filtered extension data, together with the general support bound explaining the favorable quartic case. This does not establish novelty of the construction or a new global STCI consequence.

## 10. Evidence, authority, and review boundary

Retrieval followed research/INDEX.md to the smallest relevant records, with research/AUTHORITY.md and research/CONTRIBUTING_AGENT.md governing status.

| input | Exact claim used | Scope retained |
|---|---|---|
| [R0020](../results/quartic_conormal_characteristic_jump.md) | Conormal splitting | Fixed embedding; characteristic not two versus two |
| [R0021](../results/quartic_mu4_degeneration.md) | Explicit reduced/nonreduced degeneration | Prescribed equations; geometric components over splitting field |

Both were reconstructed at the chart level requested by this audit. No broader STCI exclusion or arithmetic nonlifting theorem is inferred. The current result records establish the present scopes.

The general identities, comparison direction, counterexamples, completeness distinctions, and recommendation are the assessment here. Independent workers separately reconstructed the lifting algebra, quartic charts, completeness examples, and derived diagrams. The accompanying review record states what was checked and corrected. Review within this investigation is not external acceptance.

See the [independent proof review](#2026-10-23-ideal-filtrations-independent-reviewmd) and the exact arithmetic programs linked below.

Exact finite arithmetic is supplied by the [higher-generator counterexample script](../computations/verify_ideal_filtration_counterexamples_2026_10_23.py), [completeness counterexample script](../computations/verify_ideal_filtration_completeness_2026_10_23.py), and [quartic conormal/lifting identity script](../computations/verify_ideal_filtration_quartic_lifting_2026_10_23.py). They check stated polynomial identities, finite algebra models, and transition formulas. They prove no global projective existence or nonexistence statement and do not replace the general arguments.

The [generic count and DVR length argument](../arguments/filtered_equation_comparison.md#generic-count-and-length-over-a-dvr)
continues the local comparison. The
[normal Koszul argument](../arguments/normal_koszul_cancellation.md)
proves that incoming differentials filter the defect and gives the recursive
family that realizes the prescribed page. The
[punctual comparison argument](../arguments/punctual_comparison_defects.md#statements-and-proofs)
gives the residual and supported examples.



---

## 2026-10-23-ideal-filtrations-independent-review.md

# Independent review record: ideal filtrations investigation

Date: 2026-10-23.

Target: [independent investigation](#2026-10-23-ideal-filtrations-independent-investigationmd).

Status: **independent mathematical review completed within the scopes below; proposal only**. The reviewers are independent agents in this investigation, not human referees or external acceptance authorities. A PASS means that the stated derivation was independently checked within its assigned scope. It is not evidence that a computation by itself proves the mathematics.

## Review assignments and findings

| Reviewer task | Scope independently reconstructed | Outcome |
|---|---|---|
| lifting_audit | Initial-ideal exact sequence; intrinsic equation-module filtration; presentation syzygies; quotient denominator; direction of comparison; integral local counterexample; filtered Koszul explanation | PASS after the report explicitly retained the quotient direction \(Q_n\twoheadrightarrow\operatorname{gr}_F^nD\) |
| quartic_audit | Both exact chart expansions; first-order overlap; splitting frames; conormal matrices; characteristic-zero kernel/cokernel and contact; characteristic-two global transitions, corrected lifts, and canonical fourth-order identification | PASS, with endpoint tensor base clarified |
| completeness | Full based nine-graded data versus restricted data; local integral-hypersurface counterexample and intrinsic nonisomorphism; compatible finite towers; completed-pair uniqueness; Rees repair | PASS after removing an unqualified claim that all graded data fail reconstruction |
| diagrams_derived | Nine ideal/conormal bases; seven composable triples; exact kernels; image-sheaf 3×3; higher graded maps; cotangent placement; filtered differential; convergence qualifications; derived intersection | PASS with the indicated regularity and distinctness hypotheses |

The primary agent read all three new arithmetic scripts, checked their stated scope against their calculations, and applied the review corrections. Each script was rerun in the final validation step.

## Specific substantive checks

### Filtered equation module

The reviewers reconstructed
\[
F^nD=\frac{J\cap I^n+IJ}{IJ},\qquad
\operatorname{gr}_F^nD
=\frac{J\cap I^n}
 {J\cap I^{n+1}+IJ\cap I^n}.
\]
In particular the intersection \(IJ\cap I^n\) in the denominator is essential.

Writing \(B=\operatorname{in}_I(IJ)\), multiplication gives \(S_+H\subset B\subset H\), hence
\[
0\to B_n/(S_+H)_n\to Q_n\to H_n/B_n\to0.
\]
This fixes the direction of comparison. It does not canonically split the first-order kernel into the higher pieces.

The regular-sequence presentation has syzygy \((-g,f)\in IP_0\), so the original two-generator \(T\) is intrinsic under the stated hypotheses. Redundant presentations add a fixed constant-syzygy module to every step; the graded quotients still cancel it.

### Higher-generator counterexample

For \(f=x^2+y^3\), \(g=xy+x^3+y^3\), independent checks established:

- Both carriers are integral polynomial hypersurfaces and form a local regular sequence.
- The quotient has basis \(1,x,y,y^2,y^3\), with \(x^2=xy=-y^3\), \(y^4=0\).
- Therefore \(H=(X^2,XY,Y^4)\).
- An explicit combination with both coefficients in \(I\) has initial term \(Y^4\), so \(\Delta_4=Q_4=k\).
- Independence of the quadratic initials gives \(F^3D=0\), hence \(\operatorname{gr}_F^4D=0\).
- The first higher filtered Koszul differential produces this same \(Y^4\).

The exact script checks the polynomial identities, associative five-dimensional model, filtration dimensions, and monomial comparison. Irreducibility and the general filtered-module statements are proved in the text, not inferred from that script.

### Completeness counterexample

The two intersections reduce locally to
\[
J_0=(u^2,v^4),\qquad J_1=(u^2+v^3,v^4),
\]
each originally presented by two integral hypersurfaces. Both have the same normal graded algebra \(D_0[U,V]/(U^2,V^4)\). The review checked every entry of the table after all nine graded objects are restricted to \(C\).

The intrinsic distinction is the existence of a square-zero element outside the square of the nilradical. It holds for \(J_0\) and fails for \(J_1\). The eight-dimensional models and exact square-coefficient identities support that proof.

This example is explicitly not a counterexample to the full nine-graded diagram with original bases and ambient degree-zero quotient maps. Such data already recover \(J\).

### Quartic kernel and global compatibility

The review independently checked the conormal overlap determinant \(-a^{-14}\), the characteristic-zero balanced frames, both conormal matrices, and the torsion cokernel lengths \(9+9\).

In characteristic two, the kernel frames and fourth-generator frames both transform by \(a^{-24}\). The corrected lifts map exactly to \(u^4\), respectively \(B^4\), and the intrinsic filtration has
\[
F^2D=F^3D=F^4D,\qquad F^5D=0.
\]
Thus the canonical comparison is invertible in degree four and supplies the claimed kernel-to-\(Q_4\) isomorphism. Equal line-bundle degrees alone were not used as proof.

### Additional smooth-carrier proposition

The primary agent proposed the general support statement after the initial review. Both lifting_audit and diagrams_derived independently checked it:

> Along a smooth codimension-two curve in a smooth equicharacteristic ambient threefold, for a two-generator regular-sequence ideal, a nonzero fiber conormal symbol of either carrier at \(p\) implies \(\Delta_p=0\). Therefore \(\operatorname{Supp}\Delta\subset C\cap\operatorname{Sing}X\cap\operatorname{Sing}Y\).

Both reviewers reconstructed the completed local calculation. After straightening the smooth equation,
\[
\widehat R=D_0[[x,y]],\quad I=(x,y),\quad
J=(x,h),\quad h=y^m a(t,y),\quad a(t,0)\ne0.
\]
The initial ideals are
\[
H=(X,a_0Y^m),\qquad
\operatorname{in}(IJ)=(X^2,XY,a_0Y^{m+1})=S_+H.
\]
The coefficient \(a_0\) may vanish at the closed point; it only needs to be nonzero in the domain \(D_0\). The proof uses additive \(y\)-order, not invertibility of \(a_0\). Flatness preserves the defining finite intersections and faithful flatness descends each vanishing defect piece.

This is a support containment, not equality. Both carriers being singular does not force a nonzero defect. Generic smoothness only confines the defect to special points; it does not settle those points. The proposition is independently reviewed new material in this proposal .

## Corrections made before saving the final package

1. Required \(m\ge2\) in the family \((x,x+y^m)\) when asserting identical first-order diagrams and a higher differential \(d_{m-1}\).
2. Named \(k[a]\) as the tensor base for the characteristic-zero endpoint slice, avoiding an implicit retraction \(Z\to C\).
3. Qualified the recommendation: the insufficient objects are the \(C\)-restricted normal data and graded spectral-sequence limits. The full based nine-graded diagram remains sufficient through its degree-zero data.
4. Replaced potentially ambiguous “integral closures” language by scheme-theoretic closures of an open piece.
5. Narrowed the next research question to the remaining simultaneous-singular locus after proving the smooth-carrier criterion.

## Evidence and limits

The scripts verify finite local identities and algebra models. The proof audit separately checks the general algebra, gluing, and scope arguments. No unrestricted characteristic-zero STCI theorem, new global pair, or novelty claim is certified. Result and question records remain unchanged.



---

## 2026-10-23-quartic-44-filtered-proof-proposal.md

[Complete filtered-contact proof and exact computational dependencies](../synthesis/quartic_pair_obstruction.md#5-the-distinct-proof-through-filtered-contact).

## 2026-10-23-quartic-44-filtered-proof-independent-audit.md

[Reviewed mathematical replacement: filtered-contact proof](../synthesis/quartic_pair_obstruction.md#5-the-distinct-proof-through-filtered-contact).

