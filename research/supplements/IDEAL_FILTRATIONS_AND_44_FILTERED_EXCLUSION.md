# Intrinsic local algebra and characteristic-zero quartic geometry

Full mathematical investigations retained by subject. Proposals, independent reviews, limitations and rejected mathematical approaches retain their original epistemic status. This compilation is not a new proof audit.


---

## 2026-10-23-ideal-filtrations-independent-investigation.md

# Independent investigation: ideal filtrations and the nine-embedding diagram

Date: 2026-10-23. Status: **research proposal and independent assessment; not a promoted canonical result**.

Scope: distinct integral hypersurfaces \(X,Y\subset P=\mathbf P^3_k\), their scheme intersection \(Z\), and a specified reduced closed subscheme \(C\subset Z\). Distinguish \(C=Z_{\mathrm{red}}\) from a marked component \(C\subsetneq Z_{\mathrm{red}}\). Statements identifying \(\operatorname{Sym}(I/I^2)\) with \(\operatorname{gr}_I\mathcal O_P\) additionally assume \(C\hookrightarrow P\) regular. The explicit marked rational quartic is smooth. Local counterexamples are local examples, not global constructions for that fixed projective quartic.

The original request specified no repository edits. The subsequent instruction, “pls save your work in a branch,” authorizes this report and its evidence on a separate branch. No accepted proof, canonical result, or canonical question is changed.

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

Use \(D=J/IJ\), with decreasing filtration
\[
F^nD=\frac{(J\cap I^n)+IJ}{IJ},\qquad n\ge1.
\tag{10}
\]
Then \(F^1D=D\), \(F^2D=\ker\phi\).

Let \(\pi:P_0\twoheadrightarrow J\) be any finite free presentation, \(L=\ker\pi\), \(P_n=\pi^{-1}(I^n)\). Because \(\pi(IP_0)=IJ\), there is for every \(n\) a compatible exact sequence
\[
0\to L/(L\cap IP_0)
\to(P_n+IP_0)/IP_0
\to F^nD\to0.
\tag{11}
\]
The same constant-syzygy module occurs at every stage.

For a regular sequence \(f,g\), its syzygy module is generated by \((-g,f)\), which lies in \(IP_0\). Thus \(P_0/IP_0=D\), \(T=P_2/IP_0=\ker\phi\), and the proposed filtration is intrinsic under this identification. A change of regular generators changes coordinates, not the filtered sheaf.

A redundant presentation can add extra constant syzygies. Adding a zero generator adds \(R/I\) to every stage. The successive quotients still cancel that same extra module and remain intrinsic. Formula (10) removes the issue altogether. In the noetherian case Artin–Rees shows \(F^nD=0\) locally for large \(n\), since eventually \(J\cap I^n\subset IJ\).

### 4.2 The denominator, and the direction of the canonical map

Write
\[
B_n=\operatorname{in}_n(IJ)
=\operatorname{image}(IJ\cap I^n\to I^n/I^{n+1}).
\]
There is a canonical identification
\[
\operatorname{gr}_F^nD
=\frac{J\cap I^n}{J\cap I^{n+1}+(IJ\cap I^n)}
=H_n/B_n.
\tag{12}
\]
Indeed, for an element of \(J\cap I^n\) lying in \((J\cap I^{n+1})+IJ\), subtract its \(I^{n+1}\) part; the remaining \(IJ\) part lies in \(I^n\). This proves the denominator without assuming strictness.

Multiplication of symbols gives \((S_+H)_n\subseteq B_n\subseteq H_n\). Consequently
\[
Q_n\twoheadrightarrow\operatorname{gr}_F^nD
\]
has kernel \(\Delta_n=B_n/(S_+H)_n\), as in (1). There is generally no canonical reverse map.

The proposed equality is therefore correct as a criterion:
\[
\operatorname{in}_I(IJ)=S_+H
\iff
Q_n\longrightarrow\operatorname{gr}_F^nD
\text{ is an isomorphism for every }n.
\tag{13}
\]
Degree one is automatic. The equality is false as an unconditional assertion.

Even if (13) holds, it identifies filtration pieces rather than canonically splitting \(\ker\phi\) into the \(Q_n\). An isomorphism \(\ker\phi\simeq Q_m\) additionally needs \(F^2D=\cdots=F^mD\), \(F^{m+1}D=0\). These extra conditions do hold for the characteristic-two pair.

The defect \(\Delta_n\) measures minimal initial equations created by combinations with every coefficient vanishing on \(C\), and therefore erased by passing to \(J/IJ\). Its construction belongs to standard filtered-module theory; no novelty claim is made for naming this quotient.

### 4.3 A proved sufficient condition: one smooth carrier

There is a useful general explanation for the favorable quartic calculation.

**Proposition (new assessment, independently reviewed; not canonically promoted).** Let \(C\) be a smooth curve of codimension two in a smooth equicharacteristic ambient threefold. Let \(J=(f,g)\subset I_C\) be a two-generator regular-sequence ideal. At any \(p\in C\) where at least one carrier has a nonzero fiber conormal symbol, \(\Delta_p=0\). Equivalently in this smooth setting, either carrier being smooth at \(p\) suffices. Consequently
\[
\operatorname{Supp}\Delta\subset
C\cap\operatorname{Sing}X\cap\operatorname{Sing}Y.
\tag{13a}
\]

**Proof.** Complete the regular local ambient ring at \(p\). Compatible regular parameters, including the nonzero conormal equation as \(x=f\), give
\(\widehat R=D_0[[x,y]]\), \(\widehat I=(x,y)\), where \(D_0\) is a complete regular one-dimensional local domain (a field at the generic point). Subtract an \(x\)-multiple from \(g\) to obtain \(h\in D_0[[y]]\). It is nonzero because \(f,g\) is a regular sequence. Write
\[
h=y^m a(t,y),\quad m\ge1,\quad a_0=a(t,0)\ne0.
\]
The coefficient \(a_0\) need not be a unit at \(p\). Since \(D_0\) is a domain, \(y\)-order is additive for nonzero products. Therefore
\[
\operatorname{in}_I(J)=(X,a_0Y^m).
\]
Moreover
\[
IJ=(x^2,xy,yh).
\]
Its \(x\)-free part consists of multiples of \(yh\); every \(x\)-containing part is in \(x(x,y)\). Reducing modulo this homogeneous monomial ideal and using the same additive-order argument gives
\[
\operatorname{in}_I(IJ)
=(X^2,XY,a_0Y^{m+1})
=S_+\operatorname{in}_I(J).
\]
Flat completion preserves the finite intersections defining each initial piece, and faithful flatness descends \(\Delta_n=0\). This proves the proposition.

In particular, if the two carriers have no common singular point on \(C\), the comparison in (13) is an isomorphism everywhere. If at least one is generically smooth on a projective integral \(C\), any defect has finite support. The counterexample in section 5 lies entirely in the simultaneous singular locus, so it is consistent with this proposition.

For the explicit quartic, \(F\) is smooth along \(C\cap\{x_0\ne0\}\), and \(G\) is smooth along \(C\cap\{x_3\ne0\}\). These opens cover \(C\). Thus (13a) explains the equality of initial ideals globally in both characteristics. Characteristic two additionally satisfies (25), which is what singles out \(Q_4\) and identifies it with the entire kernel.

## 5. Counterexample to the general first-order/higher-generator correspondence

Work in \(R=k[x,y]_{(x,y)}\), characteristic zero, \(I=(x,y)\), and put
\[
f=x^2+y^3,\qquad g=xy+x^3+y^3,\qquad J=(f,g).
\]
Both polynomial hypersurfaces are integral and \(f,g\) are a regular sequence. The cusp polynomial is irreducible. A cubic factorization of \(g\) over an algebraic closure would have a line factor. Substitution \(y=ax+b\) forces \(b=0\) from the constant term, then \(a=0\) from the quadratic term, leaving \(x^3\ne0\); vertical lines also fail.

The following identity has both coefficients in \(I\):
\[
(y+x^2)f+(-x+y^2)g
=y^4+x^2y^3+x^3y^2+y^5.
\tag{14}
\]
Its initial form is \(Y^4\), so \(Y^4\in\operatorname{in}_I(IJ)\).

The full initial ideal is
\[
H=(X^2,XY,Y^4).
\tag{15}
\]
To prove fullness independently of a standard-basis guess, in \(R/J\) put \(w=1-y^2\), a unit. Then \(x^2=-y^3\), \(xyw=-y^3\), and multiplying and eliminating gives \(y^4(w^2+y)=0\). Its second factor is a unit. Hence \(y^4=0\), \(xy=-y^3\), and the quotient has basis
\[
1,x,y,y^2,y^3,\qquad x^2=xy=-y^3,\quad y^4=0.
\]
These relations also define an associative five-dimensional algebra satisfying \(f=g=0\), so the dimension is exactly five. The ideal in (15) lies in \(H\) and has colength five, proving equality.

But \(Y^4\notin S_+H\): lower generators contain \(X\), and a positive-degree multiple of \(Y^4\) starts at degree five. Thus \(Q_4=kY^4\), \(\Delta_4=Q_4\ne0\).

On the other hand \(\phi=0\), so \(F^2D=D=k^2\). The degree-two initials \(X^2,XY\) are linearly independent over \(k\); no nonzero constant combination lifts to order three. Hence \(F^3D=0\) and
\[
\operatorname{gr}_F^4D=0\ne Q_4.
\]
Adjoining a parameter \(t\) and taking \(I=(x,y)\) gives the same example along a smooth reduced curve in a smooth threefold. It is a local counterexample, not a global pair for the fixed projective quartic.

The filtered Koszul complex explains the mechanism. Give both generators normal weight two. Then
\[
H_1(K(X^2,XY))=k[Y](Y e_f-X e_g).
\]
The first higher differential sends this class to \(Y^4\) modulo \((X^2,XY)\), since
\[
yf-xg=y^4-x^4-xy^3.
\]
This injective differential adds the missing initial equation. The coefficients \(y,-x\) lie in \(I\), which explains why passing to \(J/IJ\) erases this mechanism.

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

Let \(R=k[t,u,v]_{(t,u,v)}\), characteristic zero, \(I=(u,v)\). Consider integral hypersurfaces
\[
f_0=u^2+v^5,\quad f_1=u^2+v^3,\quad g=v^4+u^5.
\]
Coprime binomial exponents give irreducibility. Put \(J_i=(f_i,g)\). For \(f_i=u^2+v^r\),
\[
u^5=f_i(uf_i-2uv^r)+uv^{2r},
\]
so modulo \(f_i\), \(g=v^4(1+uv^{2r-4})\), a unit times \(v^4\). Consequently
\[
J_0=(u^2,v^4),\qquad J_1=(u^2+v^3,v^4).
\tag{17}
\]
Both have radical \(I\), and for \(D_0=k[t]_{(t)}\) both have
\[
S=D_0[U,V],\quad H=(U^2,V^4),\quad
\operatorname{gr}_K(R/J_i)=D_0[U,V]/(U^2,V^4).
\tag{18}
\]
Their first conormal maps are zero and their minimal initial equations \(Q_2,Q_4\) agree.

Nevertheless they are not abstractly isomorphic. In \(R/J_0\), \(u^2=0\) and \(u\notin K^2\). In \(R/J_1\), no square-zero element has nonzero class in \(K/K^2\). Indeed use the free \(D_0\)-basis
\[
1,v,v^2,v^3,u,uv,uv^2,uv^3,\qquad u^2=-v^3,\quad v^4=0.
\]
If \(h\bmod K^2=\alpha u+\beta v\) and \(h^2=0\), its degree-two \(v^2\) coefficient forces \(\beta=0\). Its coefficient of the basis vector \(v^3\) is then \(-\alpha^2\), forcing \(\alpha=0\). This is an intrinsic property of the nilradical.

In fact restricting all nine graded algebras to \(C\) gives identical diagrams:

| Embedding | Graded algebra after restriction to \(C\) |
|---|---|
| \(C\to P\) | \(D_0[U,V]\) |
| \(C\to X_i\) | \(D_0[U,V]/(U^2)\) |
| \(C\to Y\) | \(D_0[U,V]/(V^4)\) |
| \(C\to Z_i\) | \(D_0[U,V]/(U^2,V^4)\) |
| \(X_i\to P\) | \(D_0[T_f]\) |
| \(Y\to P\) | \(D_0[T_g]\) |
| \(Z_i\to P\) | \(D_0[T_f,T_g]\) |
| \(Z_i\to X_i\) | \(D_0[T_g]\) |
| \(Z_i\to Y\) | \(D_0[T_f]\) |

The degree-preserving maps are the same quotient maps, summand inclusions/projections, and zero maps. Equation variables map to zero in degree one of \(S\); even higher leading equations \(U^2,V^4\) agree. This example concerns the diagrams after restriction to \(C\). The unrestricted diagrams distinguish their original degree-zero bases.

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

The currently promoted [R0020](../results/quartic_conormal_characteristic_jump.md) and [R0021](../results/quartic_mu4_degeneration.md) cover the splitting and explicit degeneration. Their [geometry/symbol audit](2026-10-23-quartic-geometry-symbol-independent-audit.md) was consulted. The chart calculations below independently reconstruct the requested formulas and lifting compatibility; unrelated accepted exclusions are not rerun.

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

Here
\[
J=(v,u^4),\quad H=(V,U^4),\quad
\operatorname{gr}_K\mathcal O_Z|_{U_0}=k[a,U]/(U^4).
\tag{24}
\]
Globally \(\operatorname{im}\phi=M=\mathcal O(-8)\), with frames \(V,A\), and \(\operatorname{coker}\phi=L=\mathcal O(-6)\), with frames \(U,B\). Thus
\[
Q_1=M,\qquad Q_4=L^{\otimes4}=\mathcal O(-24),
\]
and other \(Q_n\) for \(n\ge2\) vanish. The first-symbol subline \(M\) is distinct from the subline generated by the quadric \(V-aU\).

The equation module is \(D=\mathcal O(-16)^2\), both quartic frames transforming by \(a^{-16}\). Kernel frames satisfy
\[
r_0=a^8e_{F,0}+e_{G,0},\qquad
r_\infty=e_{F,\infty}+b^8e_{G,\infty}=a^{-24}r_0.
\]
Hence \(\ker\phi=\mathcal O(-24)\).

In the local model (24),
\[
IJ=(v^2,vu,u^5),\qquad \operatorname{in}_I(IJ)=S_+H,
\]
and
\[
F^2D=F^3D=F^4D=\ker\phi,\qquad F^5D=0.
\tag{25}
\]
The canonical comparison \(Q_4\to F^4D/F^5D\) is an isomorphism; its inverse gives the canonical \(\ker\phi\to Q_4\).

Explicitly the lift \((a^8+a^4v+v^2,1)\) of \(r_0\) satisfies
\[
(a^8+a^4v+v^2)F_0+G_0=u^4
\quad\text{in characteristic two}.
\]
At infinity \((1,b^8+b^4A+A^2)\) maps to \(B^4\). Modulo lower initial generators \(B^4=a^{-24}U^4\), exactly the kernel transition. This proves compatibility of the canonical construction on the two charts.

Generic transverse length is four and globally \(K^4=0\). Nonlinear gluing still carries information absent from the graded algebra. On the overlap
\[
b=a^{-1}+a^{-4}u\pmod{(v,u^4)},
\]
and \(B\) also has quadratic and cubic terms. Keeping only (21) discards those terms.

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

The nine-object table, master sequence (2), central sequence (8), and filtered equation module (10) suffice for most immediate calculations. They preserve carrier symmetry, identify noninjective maps, and avoid imposing nonexistent exactness on a large diagram. The invariants are familiar; the contribution is disciplined compatibility and scope.

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

1. Strengthen (13a) by describing the defect at simultaneous singular points, with precise hypotheses and counterexamples.
2. Construct a global sheaf-level filtered standard-basis or Koszul calculation retaining homogeneous source spaces, and identify its higher differentials with actual symbol corrections across overlaps.
3. For a prescribed normal graded algebra, specify the algebra-extension and nonlinear gluing classes needed to reconstruct an embedded finite thickening, separating that reconstruction from the existence of global integral carrier equations.
4. Show that one of these constructions supplies a new obstruction, completes a finite calculation, or simplifies a proof in a scope not already covered. Notation or a larger diagram alone would not establish that usefulness.

The direction is worthwhile as rigorous organizational and computational language. Its demonstrated value here is the exact distinction between first-order relations, higher initial generators, and filtered extension data, together with the general support bound explaining the favorable quartic case. This does not establish novelty of the construction or a new global STCI consequence.

## 10. Evidence, authority, and review boundary

Retrieval followed research/INDEX.md to the smallest relevant canonical records, with research/AUTHORITY.md and research/CONTRIBUTING_AGENT.md governing status.

| Promoted input | Exact claim used | Scope retained |
|---|---|---|
| [R0020](../results/quartic_conormal_characteristic_jump.md) | Conormal splitting | Fixed embedding; characteristic not two versus two |
| [R0021](../results/quartic_mu4_degeneration.md) | Explicit reduced/nonreduced degeneration | Prescribed equations; geometric components over splitting field |

Both were reconstructed at the chart level requested by this audit. No broader STCI exclusion, arithmetic nonlifting theorem, or canonical promotion is inferred. The older explanatory note's provisional wording is historical; the current result records establish the present promoted scopes.

The general identities, comparison direction, counterexamples, completeness distinctions, and recommendation are the assessment here. Independent workers separately reconstructed the lifting algebra, quartic charts, completeness examples, and derived diagrams. The accompanying review record states what was checked and corrected. Review within this investigation is not canonical acceptance.

See the [independent review record](2026-10-23-ideal-filtrations-independent-review.md) and [validation commands and outputs](../validation/ideal-filtrations-2026-10-23/README.md).

Exact finite arithmetic is supplied by the [higher-generator counterexample script](../computations/verify_ideal_filtration_counterexamples_2026_10_23.py), [completeness counterexample script](../computations/verify_ideal_filtration_completeness_2026_10_23.py), and [quartic conormal/lifting identity script](../computations/verify_ideal_filtration_quartic_lifting_2026_10_23.py). They check stated polynomial identities, finite algebra models, and transition formulas. They prove no global projective existence or nonexistence statement and do not replace the general arguments.

Continuation: the [October 24 singular-locus investigation](2026-10-24-delta-singular-locus-continuation.md) identifies the defect with filtered normal-Koszul cancellations, derives generic counts and punctual length formulas, and supplies parameter families. It remains a separate reviewed research proposal; this note's mathematical statements and status are unchanged.



---

## 2026-10-23-ideal-filtrations-independent-review.md

# Independent review record: ideal filtrations investigation

Date: 2026-10-23.

Target: [independent investigation](2026-10-23-ideal-filtrations-independent-investigation.md).

Status: **independent mathematical review completed within the scopes below; proposal only, no canonical promotion**. The reviewers are independent agents in this investigation, not human referees or external acceptance authorities. A PASS means that the stated derivation was independently checked within its assigned scope. It is not evidence that a computation by itself proves the mathematics.

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

This is a support containment, not equality. Both carriers being singular does not force a nonzero defect. Generic smoothness only confines the defect to special points; it does not settle those points. The proposition is independently reviewed new material in this proposal and is not a promoted result.

## Corrections made before saving the final package

1. Required \(m\ge2\) in the family \((x,x+y^m)\) when asserting identical first-order diagrams and a higher differential \(d_{m-1}\).
2. Named \(k[a]\) as the tensor base for the characteristic-zero endpoint slice, avoiding an implicit retraction \(Z\to C\).
3. Qualified the recommendation: the insufficient objects are the \(C\)-restricted normal data and graded spectral-sequence limits. The full based nine-graded diagram remains sufficient through its degree-zero data.
4. Replaced potentially ambiguous “integral closures” language by scheme-theoretic closures of an open piece.
5. Narrowed the next research question to the remaining simultaneous-singular locus after proving the smooth-carrier criterion.

## Evidence and limits

The [validation directory](../validation/ideal-filtrations-2026-10-23/README.md) records the exact commands and captured outputs.

The scripts verify finite local identities and algebra models. The proof audit separately checks the general algebra, gluing, and scope arguments. No unrestricted characteristic-zero STCI theorem, new global pair, or novelty claim is certified. Canonical result and question records remain unchanged.



---

## 2026-10-23-quartic-44-filtered-proof-proposal.md

# A shorter normal-algebra proof for characteristic-zero (4,4)

Date: 2026-10-23. **Independently reviewed proof proposal; not canonically promoted.**
This does not replace STCI-R-0001, and it does not assert a new general STCI
exclusion. The contribution is a shorter proof of its much narrower (4,4)
consequence, using the multiple-curve algebra and actual quartic contact.

## Exact proposed claim

Let k be algebraically closed of characteristic zero and
C=[s^4:s^3t:st^3:t^4] in P3. There are no homogeneous quartics F,G with
V(F,G)_red=C. Reducible or nonreduced quartics are included. The proof assumes
the accepted balanced conormal and quasiprimitive/Gorenstein filtration
lemmas described below; it does not invoke the complete quartic-carrier
exclusion itself.

## Inherited premises and scope

1. N_C^*=O(-7)^2, and C is contained in its unique smooth quadric
   q=x0*x3-x1*x2. O_C(1)=O_P1(4).
2. H0(I_C^2(4))=k*q^2. This follows by restricting to the quadric:
   I_(C/Q)^2(4,4)=O_Q(2,-2), up to interchanging the rulings; hence a
   quartic vanishing twice on C is divisible by q, and the remaining
   quadric must be proportional to q.
3. A complete-intersection curve supported on C with at least one generic
   normal order one has a saturated quasiprimitive filtration
   E_i=L^i(D_i), L=O(e-7), e>=0, with effective D_i, D_0=D_1=0.
   Its Gorenstein duality gives D_i+D_(m-1-i)=D_(m-1) and
   E_(m-1)=omega_C tensor (omega_Z|C)^-1.
   See research/results/order_one.md and its stated proof dependency
   research/notes/2026-10-05-mf6-pairing-audit.md. The general statement is
   finite-flat/quasiprimitive and not a hypothesis of global primitiveness.
4. The accepted e=1 primitive-triple classification and complete quartic
   pencils in research/notes/2026-10-07-session-mf6-e1-independent-audit.md,
   sections 2 and 4. These are preserved accepted evidence rather than a
   separately promoted canonical result record. Only the stated fixed-C,
   characteristic-zero scope is used.

Premises 1 and 3 are accepted mathematics, not verification tasks here.
Premise 2 is also checked by another workstream. The NEW e=0 calculation
is reconstructed in all 35 quartic monomials. The e=1 calculation only
extracts a simpler simultaneous-pair consequence of existing contact
identities; it does not re-run their accepted classification.

## Reduction to two numerical types

If F,G had a common factor, their zero set would contain a surface. Hence
they form a regular sequence and Z=V(F,G) is a pure degree-16
complete-intersection curve with generic length m=4 along C and
omega_Z=O_Z(4).

A quartic of generic normal order at least two is in H0(I_C^2(4)) because
Sym^j N_C^* is torsion-free: the lower normal symbol vanishes everywhere
when it vanishes generically. Thus it is a multiple of q^2. If one equation
is q^2, the other cuts a divisor of class (4,4) on Q, which cannot have
sole support C of class (1,3). If both are q^2, the pair has a common
surface. Therefore any hypothetical pair has generic normal order one,
and the quasiprimitive filtration applies.

Adjunction gives E_3=O(-18). Since E_3=L^3(D_3),

    deg D_3 = 3-3e.

The duality relation at i=1 is D_2=D_3. Effectivity and e>=0 leave
exactly:

- e=0, L=O(-7), deg D_2=deg D_3=3;
- e=1, L=O(-6), D_2=D_3=0.

The second type is globally primitive. The first permits the two quartics
to be singular at common points on C; it is not omitted.

## A common pencil criterion

Over K=k(C), choose ambient normal parameters m,ell so a common triple
has m=f2*ell^2 modulo ell^3. Write a quartic H as

    H=h_H*m+k_H*ell^2+e_H*m*ell+c_H*ell^3+O(normal order4).

Containing the triple means k_H+h_H*f2=0. After the local change
m=f2*ell^2+m_new, its cubic contact is

    tau_H=c_H+e_H*f2.

Two independent quartics H0,H1 can have generic intersection length at
least four only if

    h_H0*tau_H1-h_H1*tau_H0=0 in K.

Otherwise eliminate m_new with one equation: the other equation is a
unit times ell^3 plus higher terms, so the quotient has length exactly
three. Replacing the basis of a two-dimensional quartic pencil scales
this determinant by a nonzero constant. This is an obstruction for every
pair in the pencil, not a test of one special pair.

## e=0: three orbits, one nonzero cubic-contact determinant

Use the balanced ambient coordinates on x0=1:

    z=x1,
    V=x2-z^3,
    U=x3-z^4-(3/2)*z*V.

A quotient N_C^* -> O(-7) is constant in this frame. Its finite chart is
U=-theta*ell,V=ell; the other endpoint is U=ell,V=0. The actual ambient
torus (x0,x1,x2,x3)->(x0,lambda*x1,lambda^3*x2,lambda^4*x3)
changes (z,U,V) to (lambda*z,lambda^4*U,lambda^3*V), so theta changes
to lambda*theta. Thus exactly three orbits suffice: theta=0, infinity,
and theta=1. This uses an actual projective automorphism preserving C,
not an arbitrary change of the embedded conormal frame.

Put m=U+theta*V in the finite chart. The double-to-triple obstruction is
h_theta in H1(O(-7)). A defect section delta of O(3) must annihilate it
in H1(O(-4)). Once delta is fixed, all regular quadratic corrections
form a torsor under

    H0(Hom(O(-7),O(-14)(D))) = H0(O(-4)) = 0.

Therefore there are no omitted free correction parameters. This is the
pushout of the standard double-to-triple extension by L^2 -> L^2(D).
The condition that the resulting structure be pure can only shrink this
parameter space; we allow all annihilators in the exclusion.

On the opposite ambient chart put

    W=x2/x3,
    a=x1/x3-W^3,
    b=x0/x3-W^4,
    U'=a/2,
    V'=-3*W*a+2*b.

Expanding this exact coordinate change through degree two produces:

    h_1=3/z^5-3/(2z^4)+3/(4z^3)-3/(8z^2),
    h_0=-3/(8z^2),
    h_infinity=3/z^5.

For theta=1 the multiplication matrix from delta=sum_(j=0)^3 d_j*z^j
to the Laurent coefficients z^-1,z^-2,z^-3 of delta*h_1 is

    [    0   -3/8    3/4   -3/2 ]
    [ -3/8    3/4   -3/2     3  ]
    [  3/4   -3/2     3      0  ].

Its kernel is k*(0,2,1,0), so delta=z(z+2), understood as a section
of O(3); its full divisor includes infinity. Moreover

    delta*h_1 = -3/8 + 6/z^4.

With the sign convention m=gamma/delta*ell^2, gamma=3/8. Thus a quartic
H, expanded at U=-ell,V=ell, contains the triple exactly when

    H|C=0,
    [ell]H=0,
    delta*[ell^2]H + gamma*[U]H=0.

These are polynomial coefficient equations in the 35 ambient quartic
monomials. Their matrix has rank 33. A compact basis of its full kernel
is the following. Put

    q=x0*x3-x1*x2,
    A=x0^2*x2-x1^3,
    B=x0*x2^2-x1^2*x3,
    D=x2^3-x1*x3^2.

Then

    F0=-(x2+x3)*(16*A+(16*x0+8*x1)*q)
          +(4*x2+x3)*B-x2^2*q,

    F1=x2*D-256*x1*A
          -4*q*(64*x0*x1+16*x0*x2+4*x0*x3+32*x1^2
                +4*x1*x2+4*x1*x3+2*x2^2+x2*x3).

In coordinates U=m-ell,V=ell, set f2=3/(8z(z+2)). The exact first
and cubic contacts are

    h0=-2*z^3*(z+2)^3,
    h1=-2*z*(z+2)*(z^2+4)*(z^4+16),
    tau0=-(z+4)/8,
    tau1=-(z^5+2*z^4+16*z^2-16*z+96)/(8*z*(z+2)).

Their determinant is

    h0*tau1-h1*tau0 = 32*z*(z-2)*(z+2) != 0.

Hence every independent pair in the full quartic pencil has generic
intersection length three, not four. This excludes the open quotient
orbit.

At theta=0 every annihilator is delta=z^2*(a+b*z). The regular correction
is gamma=(3/8)*(a+b*z), so the common factor cancels from the quartic
containment equations. Those equations have complete solution space
D*H0(O_P3(1)), of dimension four. At infinity every annihilator is a+b*z;
its common factor likewise cancels, and the complete quartic space is
A*H0(O_P3(1)). Both cases force a common cubic surface in any pair.
This excludes both endpoint orbits without asserting that each annihilator
actually defines a pure triple.

## e=1: existing pencils fail the same cubic-contact test

The existing accepted classification gives four torus orbits of primitive
triple directions. One is the quadric direction and every quartic through
it is q times a quadric. It cannot provide a proper (4,4) pair.

The principal orbit has normalized quotient A=1+z,B=-2-8z and a complete
two-dimensional quartic pencil H=alpha*P0+beta*P1. In the accepted audit's
coordinates m=B*U-A*V, ell=(4/3)*U+(1/6)*V, the triple is
m=-gamma*ell^2, gamma=192*z+96. Its audit defines T=gamma*e-c,
so T=-tau in the common criterion above. The explicit h,T formulas in
section 4 of that audit give the new simultaneous-pair identity

    h_P0*T_P1-h_P1*T_P0
      =(2*z-1)^3*(2*z+1)*(4*z^2+2*z+1)/256 != 0.

Thus its two independent quartics have generic intersection length three.

The other two orbits are the conjugate directions A=r*z,B=1 with
12*r^2+4*r+3=0. Their complete pencil has basis

    R0=x0^3*x3-(r+3/2)*x0^2*x1*x2+(r+1/2)*x1^4,
    R1=x0*x3^3+(r-7/6)*x1*x2*x3^2+(1/6-r)*x2^4.

The accepted exact contact formulas are

    h_R0=1, T_R0=0,
    h_R1=(2*r+2/3)*z^8, T_R1=(8*r/9)*z^3.

Their determinant (8*r/9)*z^3 is nonzero for both roots. Again generic
intersection length is three. This exhausts e=1 and proves the proposed
(4,4) exclusion from the inherited premises.

## Characteristic comparison and exact interpretation

This gives a coherent algebraic explanation of the characteristic-zero
failure: adjunction and Gorenstein duality leave only two types, and the
actual quartic relations cannot agree through the fourth layer. The
associated symmetric algebra alone does not contain the nonlinear
quadratic cocycle or the cubic contact determinants. The calculation
uses the filtered embedded algebra together with the global quartic
source.

The characteristic-two pair x1^4-x0^3*x3, x2^4-x0*x3^3 has local algebra
k[z,Y]/(Y^4), first quotient O(-6), and graded pieces O(-6i). Its
characteristic-zero numerical analogue is the e=1 primitive type above.
Frobenius permits exactly the fourth transverse power; in characteristic
zero the permitted triple directions and their global quartic pencils
have the nonzero cubic determinants above. This is a sharper comparison
than asserting that every O(-6) triple is obstructed: some exist even in
characteristic zero, including the thickening inside Q.

This does not establish a uniform obstruction to pairs of arbitrary
higher degree, and it does not replace the stronger all-mate-degree
quartic-carrier theorem.

## Evidence, independent-review requirements, and failed shortcuts

Certificate: research/computations/verify_44_filtered_contact_2026_10_23.py. Run with
/tmp/stci-z4-env/bin/python. It reconstructs the new e=0 cocycles,
all three degree-three annihilator spaces, full 35-column quartic contact
spaces, and the exact cubic determinant. It separately checks the new
e=1 determinants from inherited accepted h,T expressions. Expected final
output includes PASS for e=0 and e=1 determinants; it explicitly retains
the inherited status of e=1 completeness.

The [independent audit](2026-10-23-quartic-44-filtered-proof-independent-audit.md) checks the degree3 defect pushout and correction
uniqueness; the signs in m=gamma/delta*ell^2; the ambient torus action;
the exhaustiveness of quartic source matrices; and the passage from a
nonzero cubic determinant to generic intersection length three. It also checks that the inherited BF and e=1 classification hypotheses match
this application.

Two rejected shortcuts are preserved here:

- Global primitiveness cannot be assumed from generic order one. The
  e=0, D2=D3 degree3 type is essential and is covered explicitly.
- The early e1 jet-rebuild note claims fixed ruling lines in all nonquadric
  pencils, but that assertion conflicts with the later exact R0,R1
  pencil above: restricting those to Q gives common factor only C. This
  proposed proof uses the later independently audited complete pencils
  and flags the older line assertion as an unreconciled legacy passage.

The first exploratory e=0 script used the wrong sign in its quadratic
contact constraint and produced a false zero-dimensional quartic source.
Correcting the sign to delta*k+gamma*h=0 yields the two-dimensional source
and agrees with the exact gluing equation. The clean certificate states
this convention explicitly. No failed exploratory result is used.

Independent review outcome: PASS under the listed inherited inputs, with
finite-defect and global-realization hypotheses explicitly checked. The new
independent direct-Taylor certificate is
`research/computations/audit_44_filtered_contact_2026_10_23.py`. See the
[execution record](../validation/44-conormal-2026-10-23/README.md) for logs.



---

## 2026-10-23-quartic-44-filtered-proof-independent-audit.md

# Independent mathematical audit of the proposed short (4,4) exclusion

Date: 2026-10-23. Scope: the fixed C0=[s^4:s^3t:st^3:t^4] over an algebraically closed field of characteristic zero. This audits `research/notes/2026-10-23-quartic-44-filtered-proof-proposal.md`, with the NEW e=0 computation in `research/computations/verify_44_filtered_contact_2026_10_23.py`. It does not audit or reopen the accepted all-mate-degree integral-quartic theorem STCI-R-0001.

**Verdict: the proposed narrow (4,4) proof passes independent mathematical review, under its explicitly listed inherited conormal, saturated quasiprimitive/Gorenstein, and e=1 classification inputs.** It is a provisional proof contribution and is not a separately promoted canonical result. It gives a useful shorter derivation of a known consequence, not a replacement proof for arbitrary quartic mate degree.

## 1. Scope and inherited authority

Read research/INDEX.md first. Checked research/results/quartic_carrier_exclusion.md, research/results/order_one.md, and the underlying saturated pairing audit research/notes/2026-10-05-mf6-pairing-audit.md for hypotheses. The accepted full quartic-carrier exclusion is not used as an input to this argument.

The e=1 completeness statements are inherited from research/notes/2026-10-07-session-mf6-e1-independent-audit.md, sections 2 and 4. That file is independently audited accepted proof evidence, rather than a separately ID-bearing promoted result. The proposal says this explicitly. Its fixed-C0, characteristic-zero, primitive-triple hypotheses agree exactly with the current e=1 branch. I did not rerun this inherited classification.

## 2. Numerical and thick-branch reductions

A pair with sole reduced support C0 has no common surface factor, so is a proper complete intersection of degree16. Its generic transverse length is4 and adjunction gives omega_Z=O_Z(4). Thus the last saturated piece is E3=omega_C tensor omega_Z|C^-1=O_P1(-18).

The conormal quotient E1=L=O(e-7) has e>=0 because N_C^*=O(-7)^2 surjects onto it. With E3=L^3(D3), deg D3=3-3e. The audited perfect multiplication E1 tensor E2 -> E3 gives equality of actual divisors D2=D3, not merely numerical equivalence. Effectivity therefore leaves exactly e=0 with d2=d3=3, and e=1 with both zero. No positive-defect e=0 branch has been discarded.

The order-one hypothesis is justified without the full quartic exclusion. On the unique smooth Q, C has class(1,3), up to ruling order. A quartic with generic normal order at least2 restricts to a section in H0(Q,O(2,-2))=0, so it is q times a quadric; that quadric must vanish on C and is proportional to q. Such a quartic is a scalar multiple of q^2. A mate restricted to Q has class(4,4), which cannot be supported solely on C, while a mate divisible by q gives a common surface. Hence a hypothetical pair has order-one equations. The argument also shows why an entirely-thick branch has not been silently omitted.

## 3. e=0: exhaustiveness and correction freedoms

The quotient to O(-7) is constant in the fixed balanced conormal frame. The ambient torus of weights(0,1,3,4), which preserves C0, acts transitively on the finite nonzero quotient parameters. The endpoints are separate. This justifies three orbits; no arbitrary GL2 normal-frame transformation or PGL2 support transformation is being used.

For a degree3 defect divisor D, multiplication by its section delta pushes the actual double-to-triple extension class from H1(O(-7)) into H1(O(-4)). In fixed ambient coordinates the only remaining quadratic correction is a section of Hom(M,L^2(D)), M=O(-7), whose global section space H0(O(-4)) is zero. Thus a fixed annihilator determines at most one embedded candidate. The moving support coordinate is already included in the exact ambient transition used to obtain the cocycle; no global retraction or splitting of the filtered algebra is assumed.

In the nonzero orbit the killing matrix has one-dimensional kernel (0,2,1,0), yielding the full homogeneous degree3 divisor with affine section delta=z(z+2), including infinity. The gluing identity delta*h=-3/8+6/z^4 gives gamma=3/8 in the convention delta*m-gamma*ell^2=0. Consequently the containment equation is delta*k+gamma*h_H=0. The positive sign is essential and agrees with m=(gamma/delta)*ell^2. The current clean note and script have this convention consistently.

At theta=0 the kernel is delta=z^2(a+bz), gamma=(3/8)(a+bz), hence the rational correction is independent of the extra linear factor. At the missing endpoint gamma_U=0 and delta=a+bz. The proposal allows these supersets even when a common zero prevents the putative triple from being pure. Enlarging the candidate space is safe for an exclusion. Their complete quartic spaces are respectively D_cubic*S1 and A_cubic*S1, so any pair has a common cubic surface. There is no omitted endpoint, repeated divisor, infinity divisor, or extra regular correction parameter.

## 4. The cubic determinant is the correct obstruction

For H=h*m+k*ell^2+e*m*ell+c*ell^3+O(normal degree4), substitute m=f2*ell^2+m_new. The common triple condition k+h*f2=0 leaves cubic coefficient tau=c+e*f2. Terms involving m^2 only start at order4 after this substitution. If the first derivative h is nonzero, formal elimination of m_new shows that the residual other equation begins with (h0*tau1-h1*tau0)/h0 times ell^3. A nonzero determinant gives transverse length exactly3.

Every proper pair in a two-dimensional complete quartic source must be an independent basis. Its determinant differs by a nonzero constant from that of the displayed basis. Therefore checking the determinant once excludes every independent pair in the pencil. Scalar-dependent pairs already have a common surface.

For the new e=0 open-orbit pencil the exact determinant is 32*z*(z-2)*(z+2), which is nonzero in k(C0). Its vanishing at some individual closed points does not invalidate the generic length argument and need not be divided out or classified. Every nonzero pencil member has a nonzero first symbol, so elimination is available.

## 5. e=1 and the rejected fixed-line shortcut

The inherited primitive-triple classification is exhaustive over exactly four actual torus orbits. The quadric orbit has entire quartic space q*S2 and cannot provide a proper pair.

Using the h,T expressions in the accepted audit, I independently expanded the principal-orbit determinant and obtained

    h_P0*T_P1-h_P1*T_P0
      =(2z-1)^3*(2z+1)*(4z^2+2z+1)/256.

It is nonzero. In those conventions T=-tau, so this is the same obstruction up to sign. For either algebraic boundary root 12r^2+4r+3=0, the inherited formulas give h_R0=1,T_R0=0,h_R1=(2r+2/3)z^8,T_R1=(8r/9)z^3, and determinant (8r/9)z^3 is nonzero because r!=0. Constant rescalings of a displayed basis or simultaneous trivialization change alter these determinant formulas by a nonzero scalar; only nonvanishing is needed.

The proposal correctly rejects the older assertion that every nonquadric e=1 pencil has fixed ruling lines on Q. The later exact algebraic boundary pencil restricts to Q with gcd only C; that old shortcut must not be cited as evidence. The present cubic argument does not need it.

## 6. New independent computational check and limits

The structural certificate reconstructs every e=0 quartic source in all35 homogeneous degree4 monomials, checks the kernel dimensions and displayed bases, and verifies the cubic determinants. Its new e=1 arithmetic is only a consequence of inherited h,T expressions; it does not independently establish e=1 classification completeness.

A separate audit script `research/computations/audit_44_filtered_contact_2026_10_23.py` constructs direct Taylor substitutions along x2=z^3+ell, x3=z^4+(3z/2-1)ell+3ell^2/(8z(z+2)). It does not import the proposal's code or data. It checks the full rational Taylor identities for both displayed forms and the generic cubic determinant. Its rank lower bound uses exact rational evaluations followed by Gaussian elimination modulo1009; rank33 modulo the prime proves rank at least33 in characteristic zero. Two independent forms satisfying the full rational identities prove rank at most33. Thus finite evaluation is used only for a rigorous rank lower bound, not to infer a polynomial identity from sampling.

The first attempted independent rank computation with direct generic SymPy rational elimination was interrupted because it was unnecessarily slow. It produced no mathematical conclusion and is not evidence. The replacement modular rank calculation is the meaningful independent check.

This proof explains a failure of actual embedded quartic relations through the fourth transverse layer. Sym(N_C^*) alone records first-order bundle data; it does not encode the ambient nonlinear extension cocycle or the global quartic source. The characteristic-two prescribed pair has a primitive O(-6) first quotient and fourth transverse power by Frobenius. The characteristic-zero e=1 analogue is numerically allowed, but its actual quartic source cannot have simultaneous fourth contact. No conclusion about pairs of higher degrees follows.

The independent script completed with exit0 on 2026-10-23 and printed:

    independent necessary evaluation rank modulo1009 33
    full rational-function contact identities: PASS
    cubic determinant 32*z*(z-2)*(z+2)
    Generic contact for any independent pair is exactly three: PASS
    e1 principal cubic determinant: PASS

