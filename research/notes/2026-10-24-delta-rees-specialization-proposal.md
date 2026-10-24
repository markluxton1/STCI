# Delta as the specialization of equation-module torsion

Date: 2026-10-24. Status: **proved local arguments independently reconstructed by agent review; provisional research evidence, not a promoted result**.

This note continues the [merged ideal-filtration investigation](2026-10-23-ideal-filtrations-independent-investigation.md) and [normal-Koszul continuation](2026-10-24-delta-singular-locus-continuation.md). It studies the marked embedding \(C\subset Z=X\cap Y\), without imposing \(Z_{\mathrm{red}}=C\). All claims below concern the marked embedding and its deformation; residual components are permitted.

## 1. Exact scope and retained dependencies

Let \(R\) be a noetherian \(k\)-algebra, \(I\subset R\), and \(J\subset I\). Put
\[
B=R/I,\quad S=\operatorname{gr}_I R,\quad H=\operatorname{in}_I J,
\quad D=J/IJ,
\]
\[
F^nD=((J\cap I^n)+IJ)/IJ,\qquad
Q=H/S_+H,\qquad
\Delta=\operatorname{in}_I(IJ)/S_+H.
\]
Set \(I^n=R\) and \(F^nD=D\) for \(n\le0\). The local algebra below does not require smoothness or a complete-intersection hypothesis. For the geometric application, \(R\) is the local ring of a smooth ambient threefold, \(I=I_C\) for a smooth marked curve, and \(J=(f,g)\subset I\) is a regular-sequence ideal. Then \(D\) is locally free of rank two on \(C\).

The inherited comparison \(0\to\Delta_n\to Q_n\to\operatorname{gr}_F^nD\to0\) is used within its reviewed scope. Its predecessor remains research evidence, not an ID-bearing canonical result. The present note does not use any rational-quartic classification or STCI exclusion. No novelty claim is made for extended Rees modules, conormal specialization, or parameter-torsion removal.

For terminology, the [Stacks normal-cone construction](https://stacks.math.columbia.edu/tag/062Z) defines the normal cone from the full ideal-power algebra, and [conormal functoriality](https://stacks.math.columbia.edu/tag/01R1) supplies the inclusion-induced maps. The statements below are proved directly.

## 2. Keep the deformation, then restrict its conormal module

Introduce a deformation parameter \(u\), independent of parameters on \(C\), and define
\[
\mathscr R=R[u,I/u]
=\bigoplus_{n\in\mathbf Z}I^nu^{-n}
\subset R[u,u^{-1}].
\]
This indexing assigns weight \(n\) to \(I^nu^{-n}\); multiplication by \(u\) lowers weight by one. Define the induced ideal
\[
\mathscr J=\bigoplus_{n\in\mathbf Z}(J\cap I^n)u^{-n}
=J R[u,u^{-1}]\cap\mathscr R.
\tag{1}
\]
The quotient \(\mathscr R/\mathscr J\) is the extended Rees algebra of \(R/J\) for \(K=I/J\). Its fibres are \(R/J\) at \(u=1\), and \(S/H\) at \(u=0\). These are actual algebras, with their maps; the special algebra alone does not reconstruct the former.

There is a canonical zero section
\[
\mathscr R\twoheadrightarrow B[u],\qquad
L=\ker(\mathscr R\to B[u])=(I/u)\mathscr R.
\tag{2}
\]
No splitting \(B\to R/J\) of the canonical quotient, or scheme retraction \(Z\to C\), is assumed: (2) is simply reduction of coefficients modulo \(I\), sending every positive normal generator \(a/u\) to zero. Since \(J\subset I\), one has \(\mathscr J\subset L\). Consequently
\[
\boxed{\mathscr N=\mathscr J/L\mathscr J}
\tag{3}
\]
is the conormal module of the deformed \(Z\) in the deformed ambient space, restricted to \(C\times\mathbf A^1\). Indeed restricting \(\mathscr J/\mathscr J^2\) to this zero section gives exactly (3).

Its fibres are canonically
\[
\mathscr N/(u-1)\mathscr N=D,
\qquad
\mathscr N/u\mathscr N=Q.
\tag{4}
\]
The second equality follows from \(\mathscr J/u\mathscr J=H\), using the induced filtration, and \(L\bmod u=S_+\). Thus \(Q\) really is a special conormal fibre of the actual embedded deformation.

## 3. The intrinsic torsion module whose special fibre is Delta

Define the Rees module of the filtered equation module by
\[
\mathscr D=\bigoplus_{n\in\mathbf Z}F^nD\,u^{-n}
\subset D[u,u^{-1}].
\tag{5}
\]
Taking the class modulo \(IJ\) gives a canonical surjection
\[
\mathscr N\twoheadrightarrow\mathscr D.
\]
This is well defined because \(L\mathscr J\) maps to zero. Its kernel is
\[
\mathscr E=
\frac{\bigoplus_n(IJ\cap I^n)u^{-n}}{L\mathscr J}.
\tag{6}
\]
In coefficient form, these modules are especially explicit:
\[
\mathscr N_n=\frac{J\cap I^n}{I(J\cap I^{n-1})},\qquad
\boxed{\mathscr E_n=\frac{IJ\cap I^n}{I(J\cap I^{n-1})}.}
\tag{7}
\]
To verify the denominator, \(L\) is generated in weight one by \(I/u\). Equivalently, every term \(I^a(J\cap I^{n-a})\), \(a\ge1\), lies in \(I(J\cap I^{n-1})\), and the \(a=1\) term gives equality. Multiplication \(u:\mathscr E_n\to\mathscr E_{n-1}\) is induced by inclusion of the numerators.

**Proposition.** There is a canonical exact sequence of finite graded \(B[u]\)-modules
\[
0\longrightarrow\mathscr E\longrightarrow\mathscr N
\longrightarrow\mathscr D\longrightarrow0,
\tag{8}
\]
where \(\mathscr E\) is exactly the submodule of elements killed by a power of \(u\). Moreover
\[
\boxed{\Delta\simeq\mathscr E/u\mathscr E.}
\tag{9}
\]
In weight \(n\), the denominator in (9) is the image of \(u\mathscr E_{n+1}\).

**Proof.** Surjectivity and the kernel formula follow degree by degree from (5)–(7). The target \(\mathscr D\) embeds in \(D[u,u^{-1}]\), so multiplication by \(u\) is injective. After inverting \(u\), both middle and target modules become \(D[u,u^{-1}]\), and their map is the identity. Thus every kernel element is killed by a power of \(u\), and every such element of \(\mathscr N\) lies in the kernel.

The induced Rees ideal \(\mathscr J\) is a finite ideal of the noetherian ring \(\mathscr R\). Hence \(\mathscr N\), \(\mathscr D\), and \(\mathscr E\) are finite over \(B[u]=\mathscr R/L\). One can also see uniform nilpotence directly: \(\mathscr E_n=0\) for \(n\le1\), while Artin–Rees gives \(J\cap I^n=I(J\cap I^{n-1})\) for large \(n\). Thus only finitely many weights occur in \(\mathscr E\).

Tensor (8) with \(B[u]/(u)=B\). Its possible left obstruction is \(\operatorname{Tor}_1^{B[u]}(\mathscr D,B)\), which is the kernel of multiplication by \(u\) on \(\mathscr D\), hence zero. Since \(\mathscr D/u\mathscr D=\operatorname{gr}_FD\), this gives
\[
0\to\mathscr E/u\mathscr E\to Q\to\operatorname{gr}_FD\to0.
\]
The map sends the symbol of \(j\in J\cap I^n\) to its class in \(F^nD/F^{n+1}D\), exactly the inherited comparison map. Its kernel is \(\Delta\), proving (9). \(\square\)

This identifies the defect intrinsically: it is the special fibre of the parameter-torsion in the restricted conormal module. It is not torsion in the algebra \(\mathscr R/\mathscr J\), which is already parameter-torsionfree.

## 4. What vanishing does and does not say

Uniform \(u\)-nilpotence and (9) imply
\[
\Delta=0\iff\mathscr E=0
\iff\mathscr N\xrightarrow{\sim}\mathscr D.
\tag{10}
\]
For instance \(\mathscr E=u\mathscr E\) would imply \(\mathscr E=u^N\mathscr E=0\) for a sufficiently large \(N\).

Since \(k\) is a field, this is also equivalent to **flatness over the deformation parameter**:
\[
\boxed{\Delta=0\iff\mathscr N\text{ is flat over }k[u].}
\tag{11}
\]
Indeed (10) makes \(\mathscr N\) a submodule of \(D[u,u^{-1}]\), which is torsionfree over the PID \(k[u]\); torsionfree modules over this PID are flat. Conversely a \(k[u]\)-flat module has no \(u\)-torsion. Equivalently, any polynomial torsion in \(\mathscr N\) must already be \(u\)-power torsion, since its localization away from \(u\) is \(D[u,u^{-1}]\).

**This is not a statement of flatness over \(B[u]\).** Filtration pieces on the curve may fail to be saturated even when \(D\) is locally free and \(\Delta=0\). The supported quadruple in the predecessor has precisely this behaviour: its associated filtered pieces retain torsion on the curve. Thus there are separate directions of variation, the deformation parameter and the marked-curve parameter; they must not be merged into a single flatness assertion.

Likewise \(\Delta=0\) does not imply that the original embedding is determined by its associated graded algebra, or that its normal cone is a complete intersection, or that the carrier normal cones meet scheme-theoretically in that normal cone.

## 5. Preserve the carrier maps: a distinct saturation defect

Write \(A=I_X\), \(B_Y=I_Y\), so \(J=A+B_Y\). The different notation \(B_Y\) avoids confusing the carrier ideal with the base ring \(B=R/I\). Form their induced Rees ideals \(\mathscr A\), \(\mathscr B_Y\) by (1). All inclusions and quotient maps remain:
\[
C\times\mathbf A^1\subset\mathscr Z\subset
\mathscr X,\mathscr Y\subset\mathscr P.
\]
The two routes through the carriers commute with the direct embeddings. However, the original Cartesian square need not remain Cartesian at the special fibre:
\[
\boxed{\mathscr J=(\mathscr A+\mathscr B_Y):u^{\infty}.}
\tag{12}
\]
The right side is the contraction after inverting \(u\), where the sum is simply \(J R[u,u^{-1}]\). This proves (12). Thus \(\mathscr Z\) is the flat closure of the generic carrier intersection, and maps as a closed subscheme to \(\mathscr X\times_{\mathscr P}\mathscr Y\). Their difference is measured by
\[
\mathscr V=\mathscr J/(\mathscr A+\mathscr B_Y),
\tag{13}
\]
not by \(\Delta\). In particular, \(\mathscr V\) is parameter torsion of the carrier-intersection algebra; \(\mathscr E\) is parameter torsion of a restricted conormal module for the already saturated \(\mathscr Z\).

An elementary distinction is \(J=(x,x+y^m)=(x,y^m)\), \(m\ge2\), with \(I=(x,y)\). Both displayed carriers are smooth. In normal coordinates \(X=x/u,Y=y/u\), their deformed intersection has ideal
\[
(X,X+u^{m-1}Y^m)=(X,u^{m-1}Y^m),
\]
whose saturation is \((X,Y^m)\). The carrier cone intersection at \(u=0\) has ideal \((X)\), while the actual normal cone has ideal \((X,Y^m)\). Nonetheless \(\mathscr N\) is freely generated over \(B[u]\) by the classes of \(X,Y^m\), so \(\Delta=0\). Carrier-intersection saturation and conormal specialization therefore measure different failures.

These vertical features belong to the deformation and do not by themselves establish an extra component of the original \(Z\).

## 6. The torsion duration refines Delta: an exact family

Work locally with \(R=B[x,y]_{(\mathfrak m_B,x,y)}\), where \(B=k[t]_{(t)}\), and set
\[
I=(x,y),\qquad J=(x^a+y^b,xy),\qquad 2\le a<b.
\tag{14}
\]
Its quotient is free over \(B\) with basis
\[
1,x,\ldots,x^{a-1},y,\ldots,y^b,
\]
using \(xy=0\), \(x^a=-y^b\), and \(y^{b+1}=0\). The ideal is a regular-sequence ideal and is supported on the marked curve in this local neighbourhood. The example is used only to examine the invariant; no support condition is imposed in the general theorems.

Put \(r=b-a>0\). In deformation coordinates, the full induced Rees ideal is
\[
\mathscr J=(F,G,T),\quad
F=X^a+u^rY^b,\quad G=XY,\quad T=Y^{b+1}.
\tag{15}
\]
To see fullness, this ideal has the correct localization at \(u\), and its quotient is free over \(B[u]\) on the analogous displayed basis. The reduction rules \(X^a=-u^rY^b,XY=0,Y^{b+1}=0\) are compatible: their only nontrivial overlap is \(YF-X^{a-1}G=u^rT\). Hence the ideal is \(u\)-saturated and is exactly (1).

All syzygies of the three generators are generated by
\[
(Y,-X^{a-1},-u^r),\qquad (0,Y^b,-X).
\tag{16}
\]
Here is a direct completeness check. In a relation \(A_0F+B_0G+C_0T=0\), reduction modulo \(Y\) forces \(A_0\) to be divisible by \(Y\). Subtracting that multiple of the first relation eliminates its \(F\)-coefficient. Dividing the resulting relation by \(Y\) leaves \(X B_1+Y^b C_1=0\), and the regular polynomial pair \(X,Y^b\) gives the second relation. Localization preserves the presentation.

Modulo \(L=(X,Y)\), (16) gives just \(u^r[T]=0\). Therefore
\[
\boxed{\mathscr N\simeq
B[u]\,e_F\oplus B[u]\,e_G\oplus
\bigl(B[u]/(u^{b-a})\bigr)e_T,}
\tag{17}
\]
with weights \(a,2,b+1\), respectively. Thus
\[
\mathscr E\simeq(B[u]/(u^{b-a}))e_T,
\qquad
\boxed{\Delta\simeq B e_T\text{ in weight }b+1.}
\tag{18}
\]
For fixed \(b\), varying \(a\in\{2,\ldots,b-1\}\) leaves this graded defect unchanged but changes the parameter-torsion exponent \(b-a\). The full equation module also records the surviving weights \(a,2\); the claim of unchanged data concerns \(\Delta\), not all filtered invariants.

This duration matches the normal-Koszul cancellation weight gap: the relation \(YF-X^{a-1}G\) has source weight \(a+1\), the killed equation has weight \(b+1\), and their gap is \(b-a\). Here the explicit calculation establishes the match; no general classification of all relative torsion modules by spectral-sequence pages is claimed.

If integral algebraic carriers are desired, the same local ideal is realized by
\[
\widetilde f=x^a+y^b+t y^{b+1},\qquad
\widetilde g=\widetilde f+xy.
\tag{19}
\]
Both are primitive linear polynomials in \(t\), with relatively prime coefficient \(y^{b+1}\) and constant coefficient, hence irreducible in \(k[t,x,y]\). They are distinct. Since
\(y\widetilde f-x^{a-1}xy=y^{b+1}(1+ty)\), and \(1+ty\) is a unit at the origin, their localized ideal contains \(y^{b+1}\), then \(x^a+y^b\). Conversely \(y^{b+1}\) already belongs to the model ideal in (14). Thus the ideals agree locally. This is a local marked-line realization, not a new global projective pair for the fixed rational quartic.

## 7. Consequences, limits, and next questions

The geometric meaning is now precise: \(\Delta\) detects the failure of the conormal module, restricted to the fixed marked curve, to vary flatly in deformation to the normal cone. The flat algebra of the embedded deformation and all carrier maps remain necessary context. The module \(\mathscr E\), not merely its special fibre \(\Delta\), additionally records how long a spurious special conormal equation persists under the deformation parameter.

Promising questions are therefore intrinsic and separate:

1. Determine the \(u\)-power filtration of \(\mathscr E\) as sheaves on \(C\), and its precise relation to the incoming normal-Koszul differential filtration already identified in the predecessor. Over a transverse field one has elementary-divisor blocks; over \(\mathcal O_C[u]\) there need not be a compatible splitting.
2. Study curve-parameter base change of the exact sequence (8). Formation of \(\Delta\) can fail to commute with specialization on \(C\); this should be expressed using explicit Tor terms rather than inferred from deformation-parameter flatness.
3. Compare the distinct modules \(\mathscr V\) and \(\mathscr E\) while preserving the carrier source lines and all conormal maps. The smooth-carrier example proves that one cannot replace either invariant by the other.
4. Investigate local freeness of \(\mathscr N\) over \(\mathcal O_C[u]\), which is stronger than \(\Delta=0\), and identify the additional saturation conditions on the filtered equation bundle that it requires.

No assertion here reconstructs \(Z\) from \(\Delta\), determines unmarked components, or resolves unrestricted STCI. The core advance is an exact intrinsic interpretation of the existing invariant and a finer module that retains deformation duration.

## 8. Review and reproducibility boundary

The preceding proofs are local algebraic arguments, not inferences from sampled computations. Agent `audit_rees` independently reconstructed the degreewise quotients, torsion kernel, specialization sequence, flatness qualification, carrier saturation, full family ideal, and complete syzygies, then read this note in full. Its [independent review](2026-10-24-delta-rees-specialization-review.md) records the exact scope and the correction of the splitting terminology. This is an agent proof audit, not external acceptance or canonical promotion.

The [new Macaulay2 script](../computations/verify_delta_rees_equation_module_2026_10_24.m2) independently computes full saturated Rees ideals and full syzygy modules for four parameter pairs, and the labelled-square example. The [validation record](../validation/delta-embedding-2026-10-24/README.md) captures its run and computational boundaries. No inherited proof or existing certificate is changed.
