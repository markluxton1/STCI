# The equation filtration, conormal torsion and specialization

For a smooth codimension-two curve C in a smooth threefold, retain the marked pair C subset Z=V(f,g), permitting residual components. The [local comparison R-0030](../results/local_filtration_comparison_defect.md) distinguishes minimal full initial equations from the filtered module of actual equations. The [normal Koszul argument](../arguments/normal_koszul_cancellation.md) gives the comparison by cancellation page and the recursive family. The [punctual comparison argument](../arguments/punctual_comparison_defects.md) gives the conormal-entry annihilator and the two local examples. This supplement retains the extended Rees and normal-cone regularity proofs, with links to the migrated Results and their source reviews. The transverse-specialization proofs are in the [transverse specialization argument](../arguments/transverse_specialization.md).

The organization follows the mechanisms: first the exact comparison and higher cancellation, then the scheme supporting the defect, then its realization as deformation torsion, and finally the separate problem of slicing along the marked curve. All example families and necessary local hypotheses survive. The removed reports repeated these proofs; their substantive corrections are incorporated in the statements below.

<a id="delta-embedding-geometry-report"></a>

## 1. Exact hypotheses, retained inputs, and authority

For the geometric statements, \(C\) is a smooth integral curve in a smooth threefold \(P\), over a field of arbitrary characteristic. Locally
\[
R=\mathcal O_{P,p},\quad I=I_C=(x,y),\quad B=R/I,
\quad A_X=(f),\quad A_Y=(g),\quad J=A_X+A_Y\subset I,
\]
where \(f,g\) form a regular sequence. Distinct integral hypersurfaces give this situation; several algebraic results below have weaker hypotheses, stated in their individual notes. No rational-quartic classification, sole-support theorem, or STCI exclusion is a premise.

The [comparison construction](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd) and [normal-Koszul continuation](#delta-singular-locus-continuation) include comparison proof and reviewed source-level continuations. Their exact claims are retained as premises, without replaying inherited certificates. In particular,
\[
S=\operatorname{gr}_I R=\operatorname{Sym}_B E,\quad E=I/I^2,
\quad H=\operatorname{in}_I J,\quad T=\operatorname{in}_I(IJ),
\]
\[
D=J/IJ,\quad F^nD=((J\cap I^n)+IJ)/IJ,
\quad Q=H/S_+H,\quad G=\operatorname{gr}_F D,
\]
\[
0\longrightarrow\Delta=T/S_+H\longrightarrow Q
\longrightarrow G\longrightarrow0. \tag{1}
\]
All initial ideals are **full** initial ideals. A list of carrier symbols cannot replace \(H\) or \(T\).

The comparison result is stated in R-0030; the further mechanisms below retain their independently reconstructed source-level scope.

## 2. Retain the entire embedding and its maps

The data remain the actual schemes and inclusions
\[
C\subset Z\subset X,Y\subset P,
\]
including the original Cartesian square \(Z=X\times_PY\), all composites, and both labelled carrier ideals. The nine ideal-power filtrations and seven transitivity sequences are retained as specified in the predecessor, section 2. In particular, on \(C\),
\[
M_X=A_X/IA_X,\qquad M_Y=A_Y/IA_Y,
\qquad D=M_X\oplus M_Y,
\]
\[
\phi=(\alpha,\beta):D\longrightarrow E,
\qquad
0\to F^2D\to D\xrightarrow{\phi}E
\to N^*_{C/Z}\to0. \tag{2}
\]
The quotients \(E/\operatorname{im}\alpha\), \(E/\operatorname{im}\beta\), and \(E/\operatorname{im}\phi\) describe the paths through \(X,Y,Z\); their maps and image intersections remain part of the diagram. For projective carriers of degrees \(d,e\), the source lines in (2) are \(\mathcal O_C(-d),\mathcal O_C(-e)\). None is replaced by an abstract pair of unlabelled generators in questions about the original carriers.

The full quotient \(R/J\), its multiplication, and its Rees algebra retain the embedded scheme and extension information. The normal algebra \(S/H\), the filtration quotients, or \(\Delta\) alone do not reconstruct that scheme. Changing generators preserves the marked ideal \(J\subset I\), but can change the labelled intermediate hypersurfaces and their comparison maps.



<a id="delta-singular-locus-continuation"></a>
<a id="delta-singular-locus-review"></a>

<a id="normal-koszul-cancellation-and-the-actual-equation-filtration"></a>

## The singular-locus defect: normal Koszul differentials, degrees, and length

The October 24 investigation records independent reconstructions of the normal Koszul comparison, the generic count and DVR length criterion, and the punctual and recursive families. The migrated Results record the scope of the [normal Koszul review](../results/normal_koszul_comparison_defect.md#review), the [recursive-family review](../results/recursive_normal_koszul_cancellation.md#review), the [punctual-family review](../results/punctual_comparison_defect_family.md#review), and the separate [supported-quadruple calculation](../results/supported_quadruple_equation_filtration.md#review).

This continues the [independent filtration investigation](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd), especially its question about
\(\Delta=\operatorname{in}_I(IJ)/(S_+\operatorname{in}_I(J))\) at simultaneous singular points. The predecessor's quotient comparison and smooth-carrier support proposition are used as reviewed premises rather than reproved.

Scope: local algebra along a smooth codimension-two marked curve \(C\) in a smooth threefold, with a two-generator regular-sequence ideal \(J\subset I_C\). The entire reduced support may be \(C\), or \(C\) may be a proper marked component. The distinction matters in the examples. No new unrestricted STCI proof or global pair for the fixed rational quartic is asserted.

### 1. Main advances

1. The module \(Q\) is canonically a Tor module. A filtered Koszul complex on the **normal parameters**, rather than the carrier equations, identifies \(\Delta\) exactly with accumulated incoming higher differentials.
2. Over a generic transverse field,
   \[
   \dim\Delta=\mu(\operatorname{in}J)-2.
   \]
   The degrees and spectral-sequence pages refine this excess count.
3. If the generic defect vanishes, a punctual defect is precisely the torsion of \(Q\) lost in the comparison with the filtered equation module. A DVR length formula makes this exact.
4. For every \(d\ge3\) and \(r\ge1\), integral local carriers realize a defect \(k[[t]]/(t^r)\) concentrated in degree \(d\). This example has actual residual support, which is proved separately.
5. A second family has arbitrarily many generic defect generators and explicitly prescribed cancellation page. It admits integral algebraic carriers.
6. A supported quadruple has torsion in \(Q\) but zero defect: torsion alone is insufficient. Whether nonzero punctual defect can occur for a supported, generically defect-free complete intersection remains unresolved here.

### 2. Notation and the intrinsic comparison

Locally write
\[
B=R/I,\quad M=R/J,\quad K=I/J,\quad
S=\operatorname{gr}_IR,\quad A=\operatorname{gr}_KM=S/H,
\]
\[
H=\operatorname{in}_I(J),\quad T=\operatorname{in}_I(IJ),\quad
Q=H/S_+H,\quad\Delta=T/S_+H.
\]
The equation module \(\mathcal D=J/IJ\) has
\[
F^n\mathcal D=((J\cap I^n)+IJ)/IJ.
\]
The predecessor proves
\[
0\to\Delta_n\to Q_n\to G_n\to0,\qquad
G_n=\operatorname{gr}_F^n\mathcal D=H_n/T_n.
\tag{1}
\]
For a regular-sequence \(J=(f,g)\), \(\mathcal D\) is free of rank two over \(B\). On a curve these constructions sheafify; all torsion and ranks below are taken over the actual base \(B=\mathcal O_C\), not over a transverse field unless explicitly specified.

### 3. The correct spectral sequence for the defect

[R-0065](../results/normal_koszul_comparison_defect.md) states the comparison,
its hypotheses, and the filtration of the defect. The complete proof is in
[the normal Koszul argument](../arguments/normal_koszul_cancellation.md#normal-koszul-comparison-and-degree-bounds).

#### 3.1 A canonical Tor description

[Graded Tor and the normal Koszul shifts](../arguments/normal_koszul_cancellation.md#graded-tor-and-the-shifted-normal-filtration) ·
[Convergence and the homology filtration](../arguments/normal_koszul_cancellation.md#stabilization-and-the-induced-homology-filtration)

#### 3.2 The target filtration is exactly the previous one

[The R-0030 comparison on representatives](../arguments/normal_koszul_cancellation.md#the-comparison-on-representatives)

#### 3.3 The higher differentials recover the entire defect

[Incoming images and degree bounds](../arguments/normal_koszul_cancellation.md#incoming-images-and-degree-bounds)

### 4. Generic generator counts and punctual length

#### 4.1 The exact generic count

Let \(R=L[[x,y]]\), \(I=(x,y)\), and let \(J\) be an \(I\)-primary two-generator complete intersection. Write \(h=\mu(H)=\dim_LQ\). Since \(\dim_L\mathcal D=2\), summing (1) proves
\[
\boxed{\dim_L\Delta=h-2.}
\tag{8}
\]
Degreewise it is \(\dim_L\Delta_n=\dim_LQ_n-\dim_LG_n\).

The [consecutive cancellation argument](../arguments/normal_koszul_cancellation.md#consecutive-cancellations-over-a-transverse-field)
refines this count by degree and page, from graded Betti totals
\((1,h,h-1)\) to \((1,2,1)\), and proves the degree-four lower bound
for a nonzero transverse-field defect.

#### 4.2 Exact torsion formula on a smooth curve

Suppose \(\Delta\) vanishes generically on an integral smooth curve. Then it is a torsion submodule of \(Q\). In particular
\[
Q\text{ torsion free and }\Delta_\eta=0\quad\Longrightarrow\quad\Delta=0.
\tag{9}
\]

At a point, let \(B\) be the corresponding DVR. The surjection \(Q_n\to G_n\) has equal generic ranks. On torsion-free quotients it is a surjection between free modules of the same rank, hence an isomorphism. Consequently
\[
0\to\Delta_n\to\operatorname{tors}Q_n
\to\operatorname{tors}G_n\to0,
\]
\[
\boxed{
\operatorname{length}_B\Delta_n
=\operatorname{length}_B\operatorname{tors}Q_n
-\operatorname{length}_B\operatorname{tors}G_n.
}
\tag{10}
\]
The generic-vanishing hypothesis is essential. Torsion in the filtered equation quotients must be subtracted; torsion in \(Q\) alone is not the defect.

### 5. Arbitrary punctual degree and length, with integral carriers

[R-0068](../results/punctual_comparison_defect_family.md) states the
characteristic-zero family and its support and specialization properties.

#### 5.1 Full initial ideal, rather than a chosen-generator approximation

[Integral carriers, all symbol syzygies, and full initial ideal of \(J\)](../arguments/punctual_comparison_defects.md#integral-carriers-and-the-full-initial-ideal)

#### 5.2 Defect, annihilator, and conormal rank

[Full initial ideal of \(IJ\), exact defect, and degree bound](../arguments/punctual_comparison_defects.md#filtered-equation-module-exact-defect-and-degree-bound)

#### 5.3 Actual fibres and residual support

[Actual closed algebra and specialization](../arguments/punctual_comparison_defects.md#actual-closed-algebra-and-specialization) ·
[Finite flat algebra and genuine residual support](../arguments/punctual_comparison_defects.md#finite-flat-algebra-and-genuine-residual-support)

### 6. Arbitrarily many generic defects and a prescribed cancellation page

[R-0066](../results/recursive_normal_koszul_cancellation.md) states the
recursive family and its prescribed page. The
[proof](../arguments/normal_koszul_cancellation.md#the-recursive-family-and-its-cancellation-page)
computes both full initial ideals and identifies the strict shifted resolution
with the normal Koszul spectral sequence from the first page onward.

#### Integral algebraic carriers

The [integral perturbations](../arguments/normal_koszul_cancellation.md#integral-carriers-along-the-affine-line)
preserve the completed ideal along a marked affine line. The
[projective closures](../arguments/normal_koszul_cancellation.md#projective-scope)
permit residual components.

### 7. A supported quadruple: torsion in Q is not enough

[R-0069](../results/supported_quadruple_equation_filtration.md) states the
supported quadruple. The [full calculation](../arguments/punctual_comparison_defects.md#a-supported-quadruple-torsion-in-q-is-not-enough)
uses the normal powers in \(R/J\) and \(R/IJ\) to track both torsion
generators through the comparison.

### 8. What has been settled, and the remaining question

The proposed connection with higher Koszul cancellation now has a theorem, including the actual filtration and pagewise subquotients. Generic defect is exactly generator excess, while punctual defect is a loss of torsion measured by (10). There is no bound on punctual degree or length under the broader marked-component hypotheses, nor on generic defect rank even with integral carriers.

The positive punctual examples have residual support. The supported quadruple proves that simultaneous singularity and torsion in \(Q\) are not sufficient for a defect. This investigation does not yet decide:

> If \(J=(f,g)\) is a complete intersection with \(\sqrt J=I_C\), \(C\) smooth, and \(\Delta_\eta=0\), can \(\Delta\) be nonzero at isolated points? If so, what is its smallest supported example; if not, which duality or support condition forces vanishing?

This is a strictly narrower question than the unrestricted STCI problem. It retains actual support and all local equations. The family in section 5 must not be used as an answer to it.

The literature already studies the generic tangent-cone generator and cancellation problem; [Mandal–Rossi, The tangent cone of a local ring of codimension 2](https://arxiv.org/abs/1402.2756) is another relevant primary source. No novelty claim is made here. The useful research interface is the precise relative defect, its torsion, and its relation to supported versus residual intersection geometry.



<a id="delta-conormal-annihilator-proposal"></a>
<a id="delta-annihilator-review"></a>

<a id="scheme-theoretic-annihilation"></a>

## A scheme-theoretic annihilator for the filtration defect

[R-0067](../results/conormal_entry_annihilator.md) gives the general theorem
and the separate cubic sharpness family. Its [review passage](../results/conormal_entry_annihilator.md#review)
records the precise October 24 and Phase 5 scopes.

### 1. Claim and its intrinsic meaning

[Entry ideal, scheme structure, and DVR bound](../results/conormal_entry_annihilator.md#statement)

### 2. Elementary proof

[Entrywise annihilation identities](../arguments/punctual_comparison_defects.md#entrywise-annihilation)

### 3. Koszul interpretation

[Actual Koszul cycles and boundaries](../arguments/punctual_comparison_defects.md#koszul-interpretation-of-the-entry-identities)

### 4. Sharpness of the scheme structure

[Full cubic initial ideals and equality of annihilators](../arguments/punctual_comparison_defects.md#sharpness-over-a-dvr)

<a id="delta-rees-specialization-proposal"></a>
<a id="delta-rees-specialization-review"></a>

<a id="deformation-torsion-and-its-persistence"></a>

## Delta as the specialization of equation-module torsion

Date: 2026-10-24. Status: **proved local arguments independently reconstructed by agent review**.

This note continues the [merged ideal-filtration investigation](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd) and [normal-Koszul continuation](#delta-singular-locus-continuation). It studies the marked embedding \(C\subset Z=X\cap Y\), without imposing \(Z_{\mathrm{red}}=C\). All claims below concern the marked embedding and its deformation; residual components are permitted.

### 1. Exact scope and retained dependencies

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

The inherited comparison \(0\to\Delta_n\to Q_n\to\operatorname{gr}_F^nD\to0\) is used within its reviewed scope. Its predecessor has the proof and review scope stated there. The present note does not use any rational-quartic classification or STCI exclusion. No novelty claim is made for extended Rees modules, conormal specialization, or parameter-torsion removal.

For terminology, the [Stacks normal-cone construction](https://stacks.math.columbia.edu/tag/062Z) defines the normal cone from the full ideal-power algebra, and [conormal functoriality](https://stacks.math.columbia.edu/tag/01R1) supplies the inclusion-induced maps. The statements below are proved directly.

### 2. Keep the deformation, then restrict its conormal module

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

### 3. The intrinsic torsion module whose special fibre is Delta

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

### 4. What vanishing does and does not say

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

**This is not a statement of flatness over \(B[u]\).** Filtration pieces on the curve may fail to be saturated even when \(D\) is locally free and \(\Delta=0\). The [supported quadruple](../results/supported_quadruple_equation_filtration.md) has precisely this behaviour: its associated filtered pieces retain torsion on the curve. Thus there are separate directions of variation, the deformation parameter and the marked-curve parameter; they must not be merged into a single flatness assertion.

Likewise \(\Delta=0\) does not imply that the original embedding is determined by its associated graded algebra, or that its normal cone is a complete intersection, or that the carrier normal cones meet scheme-theoretically in that normal cone.

### 5. Preserve the carrier maps: a distinct saturation defect

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

### 6. The torsion duration refines Delta: an exact family

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

### 7. Consequences, limits, and next questions

The geometric meaning is now precise: \(\Delta\) detects the failure of the conormal module, restricted to the fixed marked curve, to vary flatly in deformation to the normal cone. The flat algebra of the embedded deformation and all carrier maps remain necessary context. The module \(\mathscr E\), not merely its special fibre \(\Delta\), additionally records how long a spurious special conormal equation persists under the deformation parameter.

Promising questions are therefore intrinsic and separate:

1. Determine the \(u\)-power filtration of \(\mathscr E\) as sheaves on \(C\), and its precise relation to the incoming normal-Koszul differential filtration already identified in the predecessor. Over a transverse field one has elementary-divisor blocks; over \(\mathcal O_C[u]\) there need not be a compatible splitting.
2. Study curve-parameter base change of the exact sequence (8). Formation of \(\Delta\) can fail to commute with specialization on \(C\); this should be expressed using explicit Tor terms rather than inferred from deformation-parameter flatness.
3. Compare the distinct modules \(\mathscr V\) and \(\mathscr E\) while preserving the carrier source lines and all conormal maps. The smooth-carrier example proves that one cannot replace either invariant by the other.
4. Investigate local freeness of \(\mathscr N\) over \(\mathcal O_C[u]\), which is stronger than \(\Delta=0\), and identify the additional saturation conditions on the filtered equation bundle that it requires.

No assertion here reconstructs \(Z\) from \(\Delta\), determines unmarked components, or resolves unrestricted STCI. The core advance is an exact intrinsic interpretation of the existing invariant and a finer module that retains deformation duration.


The [conormal entry ideal](../results/conormal_entry_annihilator.md) also
bounds persistence. The identities \(\mathfrak a\Delta=0\) and
\(\Delta=\mathscr E/u\mathscr E\) give
\(\mathfrak a\mathscr E\subset u\mathscr E\). Where \(u^N\mathscr E=0\),
iteration gives \(\mathfrak a^N\mathscr E=0\). The persistence module
can require a larger exponent than its special fiber. This bound is local
unless \(N\) is uniform.


<a id="delta-normal-geometry-proposal"></a>

## Delta, normal-cone regularity, and the labelled carrier square

Date: 2026-10-24. Status: **research with an independent agent reconstruction**.

### Scope and retained inputs

Let \(p\) be a closed point of a smooth integral curve \(C\) in a smooth threefold \(P\), over a field of arbitrary characteristic. Put \(R=\mathcal O_{P,p}\), \(B=\mathcal O_{C,p}\), \(I=I_C\), and \(J=(f,g)\subset I\), where \(f,g\) form a regular sequence. The labelled principal ideals \(A=(f), B_Y=(g)\) are retained; the letter \(B\) denotes the curve ring, not the second carrier ideal. There is **no assumption** that \(\sqrt J=I\). All statements concern the marked embedding, not classification of any additional components. The examples are local algebraic examples, not constructions for the fixed projective rational quartic.

Use the reviewed comparison from [the merged investigation, section 4](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd):
\[
S=\operatorname{gr}_I R=\operatorname{Sym}_B(I/I^2),\quad
H=\operatorname{in}_I J,\quad Q=H/S_+H,\quad D=J/IJ\simeq B^2,
\]
\[
F^nD=((J\cap I^n)+IJ)/IJ,\quad
0\longrightarrow\Delta_n\longrightarrow Q_n\longrightarrow G_n\longrightarrow0,
\qquad G_n=F^nD/F^{n+1}D. \tag{1}
\]
The [continuation](#delta-singular-locus-continuation) is the source for the generic generator count and the supported quadruple used below. Those inherited proofs and scripts are not replayed here. The standard definition of regular immersion is recalled in [Stacks, regular immersions](https://stacks.math.columbia.edu/tag/0638).

### 1. Two separate obstructions to regularity of the normal-cone embedding

Write \(\mathfrak n=(\mathfrak m_B,S_+)\). The following conditions are equivalent:

1. \(C_{C/Z}=\operatorname{Spec}(S/H)\hookrightarrow N_{C/P}=\operatorname{Spec}S\) is a regular immersion on a neighborhood of the zero section over \(p\).
2. \(Q\) is a free \(B\)-module of rank two.
3. \(\Delta=0\), and every \(G_n\) is \(B\)-torsion-free.
4. \(\Delta=0\), and every \(F^nD\) is saturated in \(D\), meaning that \(D/F^nD\) is torsion-free.

This is a criterion for the **embedding of the normal cone in the ambient normal bundle**. It is neither a flatness criterion for the cone over \(C\) nor a regular-immersion criterion for \(C\hookrightarrow Z\).

**Proof.** The associated graded dimension theorem for a proper ideal in a noetherian local ring gives
\[
\dim\operatorname{gr}_{I/J}(R/J)=\dim(R/J)=1.
\]
Consequently \(H_{\mathfrak n}\) has height two in the regular local ring \(S_{\mathfrak n}\) of dimension three. This dimension input is essential: the abstract homogeneous ideal \((tX,tY)\subset B[X,Y]\) has \(Q\simeq B^2\) but height one, and cannot be substituted for the full initial ideal in this argument.

Moreover
\[
Q/\mathfrak m_BQ\simeq H_{\mathfrak n}/\mathfrak nH_{\mathfrak n}.
\]
If the immersion is regular near the zero section, this vector space has dimension two. Choose two homogeneous lifts \(h_1,h_2\in H\) of a minimal generating set. Nakayama over \(B\), followed by graded Nakayama over \(S\), shows \(H=(h_1,h_2)\). A height-two ideal generated by two elements in a regular ring is a regular sequence. Its syzygies are generated by \((-h_2,h_1)\). Since \(h_i\in S_+\), reducing the presentation modulo \(S_+\) gives
\[
Q\simeq B(-a)\oplus B(-b),\qquad a=\deg h_1,\ b=\deg h_2.
\]
Conversely, a homogeneous basis of a free rank-two \(Q\) lifts by graded Nakayama to two generators of \(H\), which form a regular sequence by the same height argument. This proves 1 \(\Longleftrightarrow\) 2.

At the generic point of \(C\), \(J\) becomes primary to the transverse maximal ideal: a prime contained in the height-two prime \(I\) and containing the height-two regular-sequence ideal \(J\) must be \(I\) itself. The finite filtration of \(D_\eta\simeq k(C)^2\) therefore has total graded dimension two. If \(Q\) is free of rank two, summing (1) gives \(\Delta_\eta=0\). Hence \(\Delta\) is torsion; its inclusion in the torsion-free module \(Q\) forces \(\Delta=0\). Now (1) identifies each \(G_n\) with \(Q_n\), so all are free. Conversely, condition 3 identifies \(Q\) with a direct sum of free graded pieces; their total generic rank is two. Finally, for a finite filtration of a finite free module over a DVR, all successive quotients are torsion-free if and only if every filtration stage is saturated. For the forward direction build the quotients \(D/F^nD\) successively by extensions of free modules. For the reverse direction \(G_n\) is a submodule of the free module \(D/F^{n+1}D\). This proves all equivalences. \(\square\)

The local statement sheafifies on a smooth curve. The filtration and its quotients are intrinsic; no preferred splitting of \(D\), or of its filtration, is asserted. In particular, \(\Delta=0\) leaves a separate possible failure: initial equation classes can be retained in \(G_n\) as torsion arising from nonsaturated filtration stages.

### 2. The labelled carrier square has a stronger condition

Let \(f^*,g^*\in S\) denote the first nonzero normal symbols of the **original labelled equations**. Since \(S\) is a domain, normal order is additive on nonzero products, so
\[
\operatorname{in}_I(A)=(f^*),\qquad
\operatorname{in}_I(B_Y)=(g^*).
\]
There is a natural diagram
\[
C_{C/Z}\longrightarrow C_{C/X},\ C_{C/Y}\longrightarrow N_{C/P}.
\]
Its scheme-theoretic fibre product has coordinate algebra \(S/(f^*,g^*)\), and the actual normal cone has algebra \(S/H\). Thus the natural inclusion is measured by the exact sequence
\[
0\longrightarrow H/(f^*,g^*)\longrightarrow S/(f^*,g^*)
\longrightarrow S/H\longrightarrow0. \tag{2}
\]
The normal-cone square is Cartesian if and only if \(H=(f^*,g^*)\), which holds if and only if \(f^*,g^*\) form a regular sequence in \(S\).

For sufficiency, take \(j=uf+vg\). If the lowest weighted terms of the two summands cancel, their coefficients form a homogeneous syzygy of \(f^*,g^*\). Regularity makes it a Koszul syzygy. Lift its multiplier and modify \((u,v)\) by an actual multiple of \((g,-f)\); this leaves \(j\) unchanged and strictly raises the canceled weighted order. Only finitely many such steps are needed to reach the fixed normal order of nonzero \(j\). Its symbol is therefore in \((f^*,g^*)\). Necessity follows from height two. This is the elementary two-generator standard-basis argument; it does not require a choice of formal splitting of the ambient ring.

The condition in (2) retains the maps through both carriers and is stronger than regularity of \(C_{C/Z}\hookrightarrow N_{C/P}\). It differs from \(\Delta\): (2) compares the **two labelled principal carrier ideals with their sum**, whereas \(\Delta\) compares **the full initial ideal with the intrinsic filtered equation module**. Changing \((f,g)\) by a generator transformation preserves \(J,D,F,\Delta\), but can change the labelled carrier ideals and the quotient in (2).

For example, for \(m\ge2\),
\[
f=x,\qquad g=x+y^m,\qquad I=(x,y),\qquad J=(x,y^m),
\]
both labelled carriers are smooth and integral. The full initial ideal is \(H=(X,Y^m)\), with
\[
Q=B(-1)\oplus B(-m),\quad \Delta=0,\quad
F^2D=\cdots=F^mD=B(e_g-e_f),\quad F^{m+1}D=0.
\]
But \((f^*,g^*)=(X)\), and the carrier normal cones intersect in a line bundle, larger than the actual normal cone. Replacing \(g\) by \(g-f=y^m\) adapts the generators but changes the labelled carrier; it must not be used to declare the original normal-cone square Cartesian.

### 3. Two geometric distinctions that Delta alone cannot settle

First, take two smooth integral algebraic carriers
\[
f=y,\qquad g=y+tx,\qquad I=(x,y),\qquad J=(y,tx).
\]
Here
\[
H=(Y,tX),\quad Q=B(-1)^2,\quad F^2D=0,\quad\Delta=0.
\]
The first conormal map has columns \(Y\) and \(Y+tX\); it is injective with cokernel \(B/(t)\). The cone embedding is a regular immersion, while
\[
S/H\simeq B[X]/(tX)
\]
has \(t\)-torsion and is not flat over \(B\). This example is permitted by the marked-embedding scope. No component-classification objective is attached to it.

Second, the [supported quadruple](../results/supported_quadruple_equation_filtration.md)
\[
J=(x^2,y^2+tx),\quad
H=(tX,X^2,XY^2,Y^4)
\]
has \(\Delta=0\), but \(Q_2\simeq Q_3\simeq B/(t)\). These torsion classes survive in \(G_2,G_3\). The normal-cone embedding is therefore not a regular immersion. This is exactly the additional filtration-saturation obstruction in section 1, and the example does not require residual support.

Finally, regularity of \(C\hookrightarrow Z\) itself is much stronger: it is equivalent to \(C=Z\) locally at \(p\). Indeed, both local rings have dimension one and \(R/J\) is Cohen–Macaulay; a regular sequence cutting out \(C\) in \(Z\) must have length zero. Equivalently, the central conormal map \(D\to I/I^2\) is surjective; Nakayama applied to \(I/J\) then gives \(I=J\). A regular normal-cone embedding can coexist with an arbitrarily thick marked curve.

### 4. Next directions and evidence boundary

The full embedding framework now separates three questions: whether degeneration preserves the labelled carrier fibre product; whether the actual normal cone is regularly embedded in the ambient normal bundle; and whether its structural map to the marked curve is flat. Formula (2), the two conditions in section 1, and \(B\)-torsion of \(S/H\) address these respectively. Their distinctions should be retained in future examples and global constructions.

The most useful next local question is how the nonsaturated stages \(F^nD\) interact with the algebra filtration of \(\mathcal O_Z\), especially when \(\Delta\) vanishes. A second question is to identify global bundle/extension data obstructing locally adapted normal equations from coming from the original global carriers. Neither question is resolved by the local criteria here.

Independent audit: agent `geometry_maps/audit_cone_criterion` independently reconstructed all four equivalences, the labelled-square criterion, both elementary examples, and the distinction between regular cone embedding and flatness over \(C\). It specifically checked the homogeneous local Nakayama step and flagged the essential height-two input. This is an agent proof audit, not external acceptance. No new finite computation is needed for the general proofs; the supported quadruple is inherited evidence, not a newly replayed calculation. No result/question record or accepted proof is changed.

<a id="delta-base-change-proposal"></a>

## Delta, transverse specialization, and normal flatness

The [transverse specialization argument](../arguments/transverse_specialization.md)
now gives the full local development. The
[DVR power-quotient criterion](../results/normal_cone_slice_specialization.md)
computes the specialization kernel of a normal cone. The
[formal two-equation theorem](../results/normal_flat_comparison_specialization.md)
uses the two normal algebras for \(J\) and \(IJ\) to specialize the comparison
of [R-0030](../results/local_filtration_comparison_defect.md).
The [supported length-four family](../results/supported_quadruple_equation_filtration.md)
and the [length-five family](../results/supported_length_five_defect_specialization.md)
separate vanishing of the comparison defect from specialization of the
normal cone and of the defect itself.

The October 24 source records an independent agent reconstruction of the
local specialization development. It uses the October 23
[comparison and smooth-carrier arguments](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd)
and the earlier continuation's punctual family and supported quadruple as
reviewed inputs. The October 26 [local audit](#local-filtration-audit-and-scope-boundary--2026-10-26)
addresses the underlying comparison, generic count, torsion criterion and
smooth-carrier support. The Results specify the scope of their separate
proof reviews.

### Evidence scope and the remaining geometric bridge

The normal-Koszul edge filtration, generic count, punctual torsion family and recursive cancellation family were independently reconstructed in the inherited source state. The annihilator and full Rees-persistence arguments received separate reconstructions, including the exact entry ideal, all syzygies and the distinction between k[u]-flatness and O_C[u]-flatness. The supported quadruple's full initials were checked against its displayed free base-module basis; sampled Rees computations are supplemental rather than the arbitrary-parameter proof. Exact implementations remain in the [conormal-annihilator checker](../computations/verify_delta_conormal_annihilator_2026_10_24.m2), [Rees equation-module checker](../computations/verify_delta_rees_equation_module_2026_10_24.m2), [singular identity checker](../computations/verify_delta_singular_identities_2026_10_24.py), and [singular-family checker](../computations/verify_delta_singular_families_2026_10_24.m2).

There is no established general sheaf-level identification between the u-power filtration of the persistence module and each page of the incoming normal-Koszul differential filtration. The [extended Rees duration family](#6-the-torsion-duration-refines-delta-an-exact-family) proves its own page/duration match. Over O_C[u] the persistence module need not split into compatible elementary blocks. Nor does local realization supply actual homogeneous equation source lines on P3. In particular the supported, generically defect-free punctual question remains open, as stated with the exact examples above.

### Characteristic reach

The exact equation-module comparison, normal-Koszul filtration, conormal-entry annihilator, extended-Rees quotient and Tor specialization sequences are integral local algebra constructions with the displayed noetherian/regular-sequence hypotheses; no characteristic-zero division or separability is used. The explicit families retain their individual restrictions: for example the punctual-family special-fiber length computation uses a unit of constant2 when m=2, so that assertion was stated in characteristic zero and requires a separate characteristic2 calculation. The scalar coefficient-vanishing and nilpotent lengths in examples may change on reduction. The intrinsic defect construction remains available in positive characteristic, and the prescribed characteristic2 quartic illustrates higher cancellation with zero comparison defect. It is compatible with [the every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier); no defect here is a universal STCI obstruction.


---

<a id="source-2026-10-26-filtration-local-proof-auditmd"></a>

## Local filtration audit and scope boundary — 2026-10-26

Status: mathematical review of local statements, not an independent executable replay, not a global sheafification certification, and not a new theorem. Sources: RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md and the October 23–24 investigation and independent review notes.

### 1. Exact comparison from ideals

Let R be a noetherian local ring, I an ideal, J subset I, S=gr_I(R), H=in_I(J), B=in_I(IJ), and S_+ its positive part. The inclusion S_+H subset B is immediate by multiplying representatives and taking leading terms, even when cancellations make B larger. The filtration F^n on D=J/IJ is the image of J intersect I^n. Its nth graded quotient is (J intersect I^n)/(J intersect I^(n+1) + IJ intersect I^n). The initial-symbol identification therefore gives gr_F^n D=H_n/B_n. Consequently

0 -> B_n/(S_+H)_n -> H_n/(S_+H)_n -> H_n/B_n -> 0

is exact. In particular the comparison map is a surjection from Q to gr_F D, not the reverse. This argument is local and requires no global splitting.

### 2. Generic generator excess

At the generic point of a smooth curve, suppose R is a regular transverse two-dimensional local ring and J is a two-generator parameter ideal. Then D=J/IJ is a two-dimensional vector space over the residue field. The induced finite filtration is exhaustive and separated; hence dim gr_F D=2. The initial ideal H is a finite-colength homogeneous ideal in a polynomial ring in two variables, and Q=H/S_+H has dimension mu(H). Summing the exact comparison gives dim Delta=mu(H)-2. This does not imply Delta vanishes whenever J is a complete intersection: the initial ideal can need extra generators.

### 3. Punctual torsion criterion

On a smooth curve, suppose the graded comparison is an isomorphism generically. Each Delta_n is torsion. Over a local DVR, Q_n -> G_n is surjective with equal generic rank. The induced map of torsion-free quotients is an isomorphism (the target is free and the source quotient has equal rank), so there is an exact torsion sequence 0 -> Delta_n -> tors(Q_n) -> tors(G_n) -> 0. Length Delta_n equals length tors(Q_n) minus length tors(G_n). Thus torsion in Q is necessary but not sufficient for a punctual defect. If Q is torsion-free, the defect vanishes.

### 4. Smooth-carrier support and its precise logical role

The independent October 23 review reconstructs the completed-local straightening of a smooth carrier and concludes Delta_p=0 wherever at least one carrier has nonzero first normal symbol. Therefore Supp Delta is contained in C intersect Sing(F) intersect Sing(G), under the regular ambient and two-generator CI hypotheses. Containment is not an existence assertion. The argument is local, and no global line-bundle twist is needed for this support inclusion.

### 5. What the examples do and do not show

The October 24 punctual family has Delta concentrated in one degree with arbitrary torsion length, but its actual complete intersection has residual support, so it does not address radical(J)=I. The supported quadruple J=(x^2,y^2+tx) has radical I and torsion in Q, but Delta=0. These are opposite controls, not a solution to the supported punctual-defect question.

### 6. Still unverified

The characteristic-two quartic claim ker(D -> I/I^2) is isomorphic to O(-24) and to Q_4 relies on global chart frames and transitions; it is supported by the prior independent audit, but has not been rechecked in this turn. The normal-Koszul spectral sequence requires its filtered-complex indexing, convergence and incoming-differential identifications to be retained exactly as in the source; no simplified global spectral-sequence theorem is proved here. The case radical(J)=I with generic Delta=0 and nonzero isolated Delta remains open.

### Decision

The local exact comparison, generic excess, torsion criterion and support containment have independently reviewed proofs and are suitable for a *separately scoped local-algebra* result after schema/path validation. Do not infer CR-13's global O(-24) assertion or a general supported-defect vanishing theorem from this note. This review does not perform a fresh executable replay.
