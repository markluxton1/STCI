# Quartic-carrier exclusion: technical proof mechanisms

**Scope.** The fixed rational quartic is \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), over an algebraically closed field of characteristic zero. This appendix supports the [carrier and conductor chapter](carrier_descent.md) and the [quartic-carrier exclusion](../../results/quartic_carrier_exclusion.md). The linked proofs and scoped audits supply the steps beyond the arguments developed here.

## 1. What the six lanes actually need

| Lane | Essential exact input | Technical proof home |
|---|---|---|
| Normal quartic | Reduced and nonreduced exceptional graphs; normal-sheaf bounds; final passage coefficients | [normal global audit](../../arguments/carriers/quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing), [nonreduced audit](../../arguments/carriers/quartic_carrier_proof.md#34-nonreduced-support-trees-and-the-actual-maximal-ideal) |
| Genus zero | Vanishing and four minimal-degree models; cone ruling and local-unit obstruction; complete scroll/Veronese cases | [genus-zero audit](../../arguments/carriers/sectional_genus_zero_normalization_proof.md) |
| Genus one | ADE degree-four del Pezzo; \(D_5\) lattice saturation; full conductor; ribbon-net and five partitions | [genus-one interface audit](../../arguments/carriers/quartic_carrier_proof.md#genus-one-interface-review), [repeated-partition audit](../../arguments/carriers/genus_one_ribbon_partition_proofs.md#dependency-guide-independent-certificate-versus-source-proof) |
| Genus two, bisection | Second-pencil integral correction, Cartier double, nilideal and global conormal map | [bisection audit](../../arguments/carriers/genus_two_bisection_proof.md) |
| Genus two, nonendpoint | Complete effective-divisor split; all-length chain formula | [nonendpoint audit](../../arguments/carriers/genus_two_nonendpoint_proof.md) |
| Genus two, endpoint | Full quartic ideal identity; coefficient-zero cases, local A/D types, doubled-horizontal ADE roots | [endpoint full audit](../../arguments/carriers/genus_two_endpoint_proof.md) |

## 2. Genus-one exact algebra that cannot be omitted

On the normal anticanonical model \(S\subset\mathbf P^4\), write \(z=Y_2\) for the coordinate omitted by projection. The two surface quadrics can be arranged as
\[
Q_1=z^2-Az-R_1,\qquad Q_2=Lz+R.
\]
Eliminating \(z\) yields \(F=R^2+ALR-R_1L^2\). The entire conductor is \((L,R)\), **not** its radical. The independent algebra audit establishes the full quotient module before taking annihilators; its upstairs cover is finite flat of rank two even for singular or doubled conics. The singleton-support test at roots of \(L|_C\) concerns the complete projective fiber, with the projection center excluded by basepoint-freeness.

The Cartier double \(2c\) is a \((2,2,2)\) complete intersection in \(\mathbf P^4\), with nilideal \(\mathcal O_{\mathbf P^1}(-6)\). Its ambient conormal quotient is encoded by a nonzero direction \(\eta=(\eta_0,\eta_1,\eta_2)\) annihilated by the symmetric matrix
\[
M(d)=\begin{pmatrix}d_0&d_1&d_2\\d_1&d_2+d_3&d_4\\d_2&d_4&d_5\end{pmatrix}.
\]
The off-conic condition \(\eta_1^2\ne\eta_0\eta_2\) is necessary for the surface to remain an integral two-quadric intersection. The derivative binary quartic then has exactly the partitions \([1,1,1,1]\), \([2,1,1]\), \([2,2]\), \([3,1]\), \([4]\). The first two are excluded by the fixed-center argument; the other three by universal ideal calculations. In particular, the invisible \(d_2\)-coefficient and all kernel-direction boundaries must be retained. The [independent repeated-partition audit](../../arguments/carriers/genus_one_ribbon_partition_proofs.md#dependency-guide-independent-certificate-versus-source-proof) contains the actual ideal certificates and successful Macaulay2 check, not just sample pencils.

### Entire genus-one conductor: proof by graded modules

The conductor identity above admits a short, complete algebraic proof, worth retaining separately from its computational verification. Let \(T=k[x_0,x_1,x_2,x_3]\), \(A_X=T/(F)\), and \(B=T[z]/(Q_1,Q_2)\), where \(Q_1=z^2-Az-R_1\), \(Q_2=Lz+R\), and \(F=R^2+ALR-R_1L^2\). The projection identifies the fraction fields, and the integral degree-four image has equation \(F\), so \(A_X\hookrightarrow B\). The two quadrics form a complete intersection and \(B\) is normal under the genus-one hypotheses.

If \(R\) were divisible by \(L\), the equation \(Q_2\) would factor into linear forms on the integral nondegenerate surface. Hence \(L,R\) form a regular sequence in \(T\), and \(C_\Gamma=T/(L,R)\) is the **entire** coordinate ring of a plane conic, possibly reducible or doubled. In \(B\),
\[
Lz=-R,\qquad Rz=AR-LR_1.
\]
Thus \((L,R)\) annihilates \(B/A_X\), and monicity of \(Q_1\) gives a surjection \(C_\Gamma(-1)\twoheadrightarrow B/A_X\). The Hilbert series are
\[
\operatorname{HS}(B)=\frac{(1+t)^2}{(1-t)^3},\quad
\operatorname{HS}(A_X)=\frac{1+t+t^2+t^3}{(1-t)^3},\quad
\operatorname{HS}(C_\Gamma)=\frac{1+t}{(1-t)^2}.
\]
Since \(\operatorname{HS}(B)-\operatorname{HS}(A_X)=t\operatorname{HS}(C_\Gamma)\), the surjection is an isomorphism **in every graded degree**, not merely after removing finite-length modules. Consequently
\[
B/A_X\cong C_\Gamma(-1),\qquad
\operatorname{cond}(A_X,B)=\operatorname{Ann}_{A_X}(B/A_X)=(L,R).
\]
Moreover, \((L,R)B=(L)\), so the entire upstairs conductor has coordinate ring
\[
B/(L)=C_\Gamma[z]/(z^2-Az-R_1).
\]
It is free of rank two over \(C_\Gamma\), including over doubled or reducible conics. The trace-zero generator \(w=z-A/2\) satisfies \(w^2=A^2/4+R_1\). This derivation, including the sign in \(Rz=AR-LR_1\), is independently checked in the [algebra audit](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-entire-conductor-algebra-independent-auditmd). The [original conductor proof](https://github.com/markluxton1/STCI/blob/93e9ed279535ff0bd2a21855b5757e9bd04127db/research/notes/2026-10-09-session-genus-one-entire-conductor.md) also gives the six exact fixed-curve quadrics and their coefficient restrictions, which remain necessary for the root-partition arguments.

### Ribbon-net completeness and repeated-root certificates

The ribbon-net calculation is intrinsic, rather than a choice of a convenient normal direction. For the rational normal quartic \(c\subset\mathbf P^4\), the six quadratic generators \(E_0,\ldots,E_5\) have conormal classes satisfying three relations on an affine parameter chart. A homomorphism \(I_c/I_c^2\to\mathcal O_c(-6)\) sends these six quadrics to binary quadratics. The relations force all six images to depend on exactly three scalars \((A,B,C)\); the [direct conormal proof](../../arguments/carriers/genus_one_ribbon_conormal_net_proof.md) checks both parameter charts and gives \(I_c/I_c^2\simeq\mathcal O(-6)^3\). Every nonzero direction defines an everywhere-surjective quotient. Its projective orbit is determined by \(\Delta=B^2-AC\). If \(\Delta=0\), the common net base locus contains a cubic surface (a cone over a twisted cubic), so no two quadrics in that net define the required integral quartic. Thus only \(\Delta\ne0\) remains.

The [repeated-partition audit](../../arguments/carriers/genus_one_ribbon_partition_proofs.md#dependency-guide-independent-certificate-versus-source-proof) uses only parameter scalings and reversal, which **preserve the actual projection center**; arbitrary \(\mathrm{PGL}_2\) changes would not justify the reduction. Its exhaustive normal forms include \([4]\) at an endpoint, the endpoint and nonendpoint \([3,1]\) alternatives, and the nonendpoint \([2,2]\) form \(L_c=(U^2+UV-V^2/2)^2\).

For the nonendpoint \([3,1]\) branch the exact determinant is \(-k(k^2+9)\). The independent ideal equality reduces all candidate coefficients to \(k=0\), \(\eta=(1,-1/2,1)\), and a one-parameter pencil equivalent to
\[
T=E_0-E_2+E_3+E_5=(Y_0-Y_2)(Y_2-Y_4)-(Y_1-Y_3)^2.
\]
Its gradient vanishes on the line \(Y_0=Y_2=Y_4,\ Y_1=Y_3\), contradicting normality of the required del Pezzo surface. The two \(k^2=-9\) roots are excluded by the **ideal equality**, not by an arbitrary selection of a preferred kernel chart.

For \([2,2]\), the determinant is \(-(2k+1)(2k^2-k+8)/4\). The complete ideal equality eliminates the quadratic-factor roots and leaves, after changing pencil generators,
\[
Q_1=2E_1+E_3-E_4,\quad
Q_2=E_0-2E_1-E_2/2+E_4+E_5/4,\quad
\eta=(1,0,2).
\]
The missing kernel-coordinate boundary \(\eta_1=0\) is precisely the surviving case, so it must not be discarded. The independent conductor calculation has a smooth integral conic and quadratic trace \(T\), norm \(N\) of the Cartier-double section \(Q=E_3\). On the slice \(x_1=0,x_3=1,x_2=t\), its two points satisfy \(18t^2-1=0\), while
\[
T^2/N=22+72t
\]
takes two different values. If any positive power \(Q^n\) descended, the ratio of its two conjugates would be a root of unity and \(T^2/N\) would be constant. Thus **no positive power descends**, without a finite bound on \(n\). The original audit retains the exact ideals and Macaulay2 evidence; the displayed reductions do not replace that certificate.

**Retention assessment:** the ribbon-net independent audit is the source of the two-chart conormal calculation and orbit classification; the repeated-partition independent audit is the source of the universal ideal equalities and unbounded-power obstruction. Both remain essential verification records, even though their principal mathematical deductions are now represented here. The separate owner proofs should be compared against these exact certificates for unique computational or geometric material before any retirement decision.

### Endpoint [4] derivative partition: direct line-singularity argument

Under the genus-one ribbon-net and fixed-projection hypotheses of Section 2, take the second pencil quadric with vanishing coefficient of \(E_3\). Its derivative on the rational normal quartic is
\[
L_C=c_0U^4-c_1U^3V-c_4UV^3+c_5V^4.
\]
If its zero divisor is \([4]\), writing \(L_C=\lambda(\alpha U+\beta V)^4\) forces \(6\alpha^2\beta^2=0\). In characteristic zero the quadruple root is therefore an endpoint. The coordinate reversal preserves the omitted-middle projection center, so normalize \(L_C=U^4\). Then \(Q_2=E_0+hE_2\), whose net matrix has determinant \(-h^3\); a nonzero kernel direction forces \(h=0\). Thus \(Q_2=E_0\), and the net direction \(\eta=(a,b,c)\) satisfies \(a=0\), \(b\ne0\).

Full singleton support forces the other derivative to vanish at that endpoint, giving \(c_5=0\). The net equations then imply \(c_4=0\), \(c_2=-c_3\), \(c_1=cc_3/b\). Modulo \(Q_2\), the other pencil quadric is a combination of \(E_1\) and \(E_3-E_2\). Both quadrics vanish on the line \(Y_0=Y_1=Y_2=0\), and \(\nabla E_0=0\) there. Their intersection is singular along that line, contradicting normality of the required surface. This excludes the entire \([4]\) partition under the stated hypotheses, independently of the other partitions. The original standalone proof is incorporated here; the complete partition classification remains supported by the repeated-partition audit.

### Explicit trace–norm certificate for the surviving displayed [2,2] pencil

For the displayed pencil in Section 2, set \(Q=E_3\) and write \(Q=\ell z+q\) on the normalized surface. In retained coordinates \((x,y,v,w)\), the full conductor is \(\Gamma=V(L,R)\), with
\[
\begin{aligned}
A&=-2y+v,& R_1&=2xv+yv-yw,\\
L&=x+2y-v+w/4,& R&=-y^2-2xv-(xw-yv)/2+yw-v^2/4,\\
\ell&=2y-v,&q&=-2xv+yw.
\end{aligned}
\]
Eliminating \(x=-2y+v-w/4\) gives the smooth conic
\[
R_c=-y^2+\tfrac92yv+2yw-\tfrac94v^2+\tfrac18w^2=0,
\]
whose symmetric-matrix determinant is \(243/128\). In the entire quadratic conductor algebra \(z^2-Az-R_1=0\), the conjugation is \(\sigma(z)=A-z\), and
\[
T=Q+\sigma(Q)=2q+A\ell,\qquad N=Q\sigma(Q)=q^2+Aq\ell-R_1\ell^2.
\]
Reducing \(T^2,N\) modulo \(R_c\) with lexicographic order \(y,v,w\), the coefficients of \(yv^3,yv^2w\) are respectively \((114,336)\) and \((1,4)\); their minor is \(120\ne0\). Thus \(T^2/N\) is nonconstant. If \(Q^n\) descended for any positive \(n\), the generic ratio \(r=\sigma(Q)/Q\) would satisfy \(r^n=1\), making \(T^2/N=2+r+r^{-1}\) constant (also in the split or nonreduced quadratic cases in characteristic zero). Contradiction. This is a fixed-pencil all-power obstruction, not a classification of all \([2,2]\) pencils. The executable calculation is [verify_session_ribbon_22_bounded_2026_10_09.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_ribbon_22_bounded_2026_10_09.py); the broader partition coverage is supplied separately by the repeated-partition audit.

## 3. Nonendpoint trisecant: exact all-length contradiction

The normal conic model has an exceptional divisor of bidegree \((2,2)\) on \(\mathbf P^1\times\mathbf P^1\), with distinguished horizontal \(B\) of class \((1,0)\). Multiplicity two on \(B\) leaves two ruling fibers and violates singleton inverse support. With multiplicity one, the residual class is \((1,2)\). Every reducible residual is either a \((1,1)\) curve plus a ruling fiber or a second horizontal plus two ruling fibers, including doubled fibers; the [audit](../../arguments/carriers/genus_two_nonendpoint_proof.md) handles the coefficient-zero horizontal boundary. The remaining integral residual is a rational graph, meeting \(B\) in two transverse points.

Write \(a\) for the correction coefficient of \(B\). At the contacted ADE chain, let \(n\ge1\) be its length and \(1\le k\le n\) the contacted node; the other chain has length \(m\ge0\). Solving the inverse Cartan recurrence with virtual boundary \(z_0=a\) gives
\[
z_1=\frac{na+n+1-k}{n+1}.
\]
The other chain contributes \(ma/(m+1)\). The equation \(Z\cdot B=0\) is therefore
\[
a=\frac{(n+1-k)/(n+1)}
{3-n/(n+1)-m/(m+1)}
=\frac{(n+1-k)/(n+1)}
{1+1/(n+1)+1/(m+1)}<1.
\]
But the horizontal correction budget forces \(a=1\). The strict inequality holds for **all** chain lengths, not merely those in a bounded enumeration. The source checks the exact contact geometry that makes these chain attachments valid.

## 4. Endpoint trisecant: why the full family is necessary

The triple-contact endpoint uses the complete degree-four ideal identity
\[
I(C)\cap(x_2,x_3)^2=(q x_2,q x_3,D),
\]
which gives every relevant quartic as \(F=qQ+DL_0\) (notation defined in the [full reduction](../../arguments/carriers/genus_two_endpoint_proof.md)). The independent coverage audit exhausts the coefficient regimes \(c_0\ne0\), \(a_1\ne0\), \(a_1=0,b_1\ne0\), and \(a_1=b_1=0,c_1\ne0\). This includes the second horizontal fiber at infinity and doubled components.

In the distinct-crossing case the same all-length inequality as Section 3 applies. At triple contact the actual local models include endpoint \(A_n\) chains, an internal \(A_n\) attachment with coefficient \(2/(n+5)<1\), and a \(D_4\) configuration with coefficient \(1/4\); multiplicity three is incompatible with the accepted ADE model. These are **realized local positions in the full equation**, not arbitrary graph possibilities.

For the doubled-horizontal divisor \(2B+2F_0\), the normal derivative along \(B\) is a nonzero section
\[
h(b)=b(A+B_1b+Cb^2)\in H^0(B,\mathcal O_B(3)).
\]
Its zeros, including infinity and repeated roots, have total multiplicity three. For any ADE block, write \(Q=(-E_i\cdot E_j)\), \(v_i=B\cdot E_i\), and \(g_{BB}=v^tQ^{-1}v\). At a root away from the curve contact, the exact crepant residue and divisor calculation gives
\[
2g_{BB}=\operatorname{ord}(h).
\]
The correction equation with \(z_B=1\) requires total block contribution three. If \(A\ne0\), the contact contributes strictly below two and the other roots contribute one; if \(A=0\), the contact order is \(k=2\) or \(3\), the contact contributes at most \((k+2)/2\), and the remaining roots contribute \((3-k)/2\), totaling at most \(5/2\). Both contradict three. This argument handles arbitrary ADE blocks, not just short \(A\)-chains. Its local-coordinate proof and hypotheses remain in the [endpoint independent audit](../../arguments/carriers/genus_two_endpoint_proof.md).

## 5. Two earlier proof paths: exact overlap and unique content

The following comparison is based on reading the original notes, not just their titles or status labels. It determines **mathematical redundancy**, not yet safe file deletion.

**Earlier endpoint irreducible-residual note.** The [conditional irreducible-conic proof](https://github.com/markluxton1/STCI/blob/41c48d13819c318b70a51eebf1478b5b7916c925/research/notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md) assumes the normal Gorenstein ambient blowup model, the accepted horizontal correction data, and an irreducible residual of class \( (1,2) \). The [extracted argument](#endpoint-irreducible-graph-extracted-geometric-argument) gives its transverse crossings. The [full endpoint proof](../../arguments/carriers/genus_two_endpoint_proof.md) handles all residual types.

**Earlier bisection quadratic-descent note.** The [quadratic compression proof](../../arguments/carriers/genus_two_bisection_descent.md#1-the-extra-quadratic-section-and-its-entire-conductor-restriction) derives \(2Z=\sum_t k_tF_t-2R\) from four blowups (including infinitely near centers), so \(2c\sim2H\). It then studies the entire conductor sequence
\[
0\to\mathcal O_X\to\nu_*\mathcal O_S\to\mathcal O_\Gamma(-2)\to0
\]
and its rank-two algebra \(p_*\mathcal O_D=\mathcal O_\Gamma\oplus\mathcal O_\Gamma(-2)\), with trace-zero generator \(w\) satisfying \(w^2=\delta\). The compressed quadratic section has conductor restriction \(Q|_D=m+w\), with \(m\in H^0(\Gamma,\mathcal O(2))\). If \(m=0\), \(Q^2\) descends to an ambient quartic, contradicting the independent \((4,4)\) exclusion. For \(m\ne0\), power descent forces \(\delta=r^2\) and \(m=\alpha r\); the split branches have \(Q_\pm=(\alpha\pm1)r\), and descent of \(Q^n\) requires
\[
\left(\frac{\alpha+1}{\alpha-1}\right)^n=1.
\]
These are exact **conductor-power** constraints, not merely a weaker statement that the bisection lane is impossible. The later [global conormal proof](../../arguments/carriers/genus_two_bisection_proof.md) excludes the lane more efficiently but does not make the root-of-unity and split-conductor calculations mathematically empty. They are reusable for other normalization/descent problems. **Retain these calculations as a separate conditional lemma**; the source's formerly open possibilities are superseded by the conormal contradiction.

### Endpoint irreducible graph: extracted geometric argument

The earlier conditional endpoint note's distinct geometric step can be recorded precisely. In the blowup chart \(x_0=1\), set \(a=x_1/x_0\), \(y=x_2/x_0\), \(x_3/x_0=yb\). The strict transform of \(C\), parametrized by \(r=t/s\), is
\[
a=r,\qquad b=r,\qquad y=r^3.
\]
For an irreducible residual \(R\) of class \((1,2)\), the transformed surface has local equation \(aR(a,b)+yH(a,b,y)=0\). Restriction to \(C\) forces \(R(r,r)\) to vanish to order at least two. Since an irreducible \((1,2)\) curve is a graph \(a=\phi(b)\) and cannot contain the ruling fiber \(b=0\), it follows that \(\phi(0)=0\) and \(\phi'(0)=1\). The degree-two map \(R\to\Gamma\) is therefore unramified over the endpoint, with two distinct inverse points (the second possibly in the opposite chart). Both intersections with \(B=\{a=0\}\) are transverse. This supplies the geometric input for the all-length chain calculation in Section 3.

The calculation supplies the crossings for the irreducible-residual case. The [full endpoint proof](../../arguments/carriers/genus_two_endpoint_proof.md) treats reducible and doubled residuals.

## 6. Source evidence and editorial disposition

This appendix preserves mathematical proofs and links to their underlying audits.

## 7. Evidence and retention

The exposition above reproduces the short universal inequalities and identifies the longer exact calculations. It does not re-execute Macaulay2, independently establish the classical classification theorems, or replace the source audits. The [independent assembly audit](../../arguments/carriers/quartic_carrier_proof.md) checks that the normal and nonnormal lanes cover every integral quartic and that the final lower-degree argument is noncircular.

**Retain for now:** all theorem records, primary owner proofs, independent mathematical audits, exact computational certificates and failed-approach explanations with distinct mathematical content. Only duplicate orientation or narrative files should be considered for removal after their claims are mapped to these permanent sections.

## 8. Veronese projection classification

The complete regular and singular symmetric-pencil classification, and the three distinct all-degree mate obstructions, are preserved in [Step 1C Veronese integration](../../arguments/carriers/quartic_carrier_proof.md#4-sectional-genus-zero-finite-normalization-and-descent). The detailed proof owner is [the October 7 classification](../../arguments/curve/veronese_quartic_projections.md), with its October 8 independent audit. This result covers finite birational Veronese-normalized quartic carriers in characteristic zero; it does not exclude every nonnormal quartic. The identically singular pencil has quadric image of generic degree two and is not a birational quartic carrier.

## 9. Genus-two bisection: global ribbon contradiction and distinct conductor algebra

For the bisection lane the second pencil gives an actual Cartier equivalence `2c ~ 2H` on the normal surface, with infinitely-near centers and the entire correction divisor retained. A section Q with divisor 2c defines a pure Cohen–Macaulay double curve R. Its nilradical J is generically square-zero; purity eliminates finite-length subsheaves and makes J square-zero globally and torsion-free rank one on smooth c. The Hilbert polynomial `chi(O_S(mH))=2m²+m+1` yields `chi(O_R)=-6`, hence `chi(J)=-7` and `J=O_P1(-8)`. The actual morphism R to P3 induces a nonzero conormal map `N^*_(C/P3)=O(-7)^2 -> O(-8)`: it is generically nonzero away from the conductor, where normalization is an isomorphism. But `Hom(O(-7),O(-8))=0`, a contradiction. This is the universal bisection exclusion, not a bound on possible mate degrees. [Full independent proof](../../arguments/carriers/genus_two_bisection_proof.md).

The earlier quadratic-descent analysis remains a distinct **conditional conductor-power lemma**: on the entire conductor line, the quadratic algebra has trace-zero generator w with `w²=delta`, and the section Q restricts as `m+w`. A descended power forces, after excluding m=0, `delta=r²`, `m=alpha*r` and `((alpha+1)/(alpha-1))^n=1`, with alpha not 0 or ±1. These equations are necessary under the hypothetical bisection setup, not evidence of surviving mates. The global conormal contradiction supersedes their use as an open-case list; the conductor algebra may still be useful elsewhere.

## 10. Genus-zero normalization: classification and singular-cone mechanism

The sectional-genus-zero audit works on a smooth resolution M with nef and big L of square four and `K_M.L=-6`. Vanishing of `K_M+L` by nefness and Kawamata–Viehweg gives `chi(O_M)=1` and `H¹(O_S)=0`. For a general hyperplane section Y=P1, the sequence `0 -> O_S -> O_S(H) -> O_Y(4) -> 0` gives `h0(S,H)=6`. The complete morphism is finite and birational onto a normal degree-four minimal-degree surface in P5, hence its normalization is one of the scrolls S(2,2), S(1,3), the rational normal quartic cone S(0,4), or the Veronese surface. No smoothness assumption on the normalization was made in this classification.

For the cone, the minimal resolution F4 has negative section E and polarization E+4f. The class group of the cone is generated by f with `[H]=4[f]` and no torsion. The mate relation makes the lifted curve Cartier and hence disjoint from the vertex (a smooth Cartier curve through that vertex would force the surface local ring to be regular). The induced plane rational quartic ruling map must have singleton fibers to respect the entire inverse-support condition. But a rational plane quartic has a singular point; a multi-branch point violates singleton fibers, and a unibranch singular point makes the plane normalization map nonimmersive. The cone morphism then has rank one along the corresponding ruling and violates the local-unit differential lemma at the smooth lifted curve. Thus the singular cone is excluded in every mate degree. The smooth scroll and Veronese cases have their separate complete proofs; the Veronese classification is summarized in Section 8. [Genus-zero audit](../../arguments/carriers/sectional_genus_zero_normalization_proof.md).

## 11. Genus-one ribbon-net interface: why all partitions are reached

For a hypothetical genus-one mate the normalized anticanonical surface is a degree-four ADE del Pezzo, represented by a normal intersection of two quadrics in P4 with the fixed rational normal quartic c. Its actual Cartier double is a pure CM ribbon, with nilideal O(-6); the conormal quotient `I_c/I_c² -> O(-6)` is specified by a nonzero triple eta. The complete net of ambient quadrics is the kernel of the rank-three matrix `M(d)=[[d0,d1,d2],[d1,d2+d3,d4],[d2,d4,d5]]` acting on eta. The original surface pencil lies in this full net, so no direction or pencil is discarded by this passage. The discriminant-zero direction has a cubic common base locus and cannot yield the required integral surface.

The omitted-coordinate derivative map on the six-dimensional quadric space is `D_d=d0 U^4-d1 U³V-2d3 U²V²-d4 UV³+d5 V⁴`. Its one-dimensional kernel is generated by E2, and E2 lies in no allowed net. Thus the two surface quadrics have independent derivative quartics. Their first chosen derivative L_C can have only the five multiplicity partitions `[1,1,1,1]`, `[2,1,1]`, `[2,2]`, `[3,1]`, `[4]`. The squarefree partition contradicts derivative independence and the singleton-support requirement. For `[2,1,1]`, the direction charts and reversal cover all eta, including eta=(0,1,0); the only potential common-basepoint locus is eta=(1,u,u²/4), u nonzero. After center-preserving normalization, its cubic derivative map has only one double fiber, and the forced L_C has an additional fourth zero outside the permitted fiber. The other three partitions are handled by the repeated-partition audit, including the derivative-invisible E2 coefficient. These are exact **fixed-projection** statements, not a classification under arbitrary parameter changes. [Genus-one interface audit](../../arguments/carriers/quartic_carrier_proof.md#genus-one-interface-review).

## 12. Nonrational normalization is impossible without a mate hypothesis

For an integral nonnormal quartic containing the fixed smooth rational degree-four C, generic regularity along C yields a smooth strict transform c# on a resolution M of the normalization, with `L.c#=4`, `L²=4`, and `K_M.L=2pi-6` for sectional genus pi at most two. If M were nonrational, its minimal model would be ruled over a base of genus g at least one. Push L to that model with ruling degree a and infinitely-near blowup multiplicities m_i. Nefness descends through each blowdown and gives `0<=m_i<=a` even at centers on exceptional fiber components. The exact intersection identity is

`4=(2g-2)a²+(6-2pi)a+sum_i m_i(a-m_i)`.

It forces `a<=2`; meanwhile every map c#=P1 to the positive-genus base is constant, so c# lies in a ruling fiber and `4=L.c#<=a`. Contradiction. This excludes nonrational normalizations **without assuming any mate** and is stronger than the mate-conditional genus classification. [Independent audit](../../arguments/carriers/quartic_carrier_proof.md#2-why-a-nonnormal-normalization-is-rational).

## 13. Entire genus-two conductor and ambient conic model

For genus-two normalization, rationality of M and `K_M.L=-2` give rational singularities of S by duality and Leray, without assuming K_S is Cartier or Q-Cartier. Finite duality identifies the **actual** conductor ideal `I=Hom_X(nu_*O_S,O_X)=nu_*omega_S`. Its Hilbert polynomial forces `O_Gamma` to have polynomial `m+1`; maximal Cohen–Macaulay purity eliminates embedded points and nilpotent zero-dimensional additions, so Gamma is a reduced line. Dualizing the conductor sequence gives `nu_*O_S/O_X=omega_Gamma=O_Gamma(-2)` and an entire rank-two finite flat conductor algebra `p_*O_D=O_Gamma+O_Gamma(-2)`, including nonreduced and singular fibers. Its quadratic multiplication is a quartic section on Gamma. These are scheme-level assertions, not a calculation of the reduced Jacobian support. [Entire-conductor audit](../../arguments/carriers/genus_two_entire_conductor_proof.md).

The two ambient line equations t0,t1 identify naturally with the complete adjoint pencil `|K_M+L|`; their ratios agree as rational functions. Since that pencil is basepoint free, the pulled-back line ideal is **exactly** `O_M(-D_M)` for an effective `D_M~-K_M`, with no residual zero-dimensional base scheme. The universal blowup property therefore lifts M to the blowup of P3 along Gamma. The image is the integral strict transform T, of class `4H_B-2E_B` because the quartic has generic order exactly two along Gamma. Adjunction gives `omega_T=O_T(-E_B)` and its pullback is `omega_M`. The proper-trace argument proves T normal; its Gorenstein crepant singularities are ADE. This is a theorem about T, **not** an assertion that the original normalization S is Gorenstein or that its pencil descends through horizontal contractions. [Ambient-model audit](../../arguments/carriers/genus_two_ambient_conic_model_proof.md).

## 14. Exact conductor coordinates and fixed-curve fiber condition

For the genus-one projection of Section 2, the fixed rational normal quartic in retained coordinates \((x_0,x_1,x_2,x_3)\) and omitted coordinate \(z\) is \([U^4:U^3V:UV^3:V^4:U^2V^2]\). Write the six defining quadrics as
\[
\begin{aligned}
E_0&=x_0z-x_1^2,&E_1&=x_0x_2-x_1z,&E_2&=x_0x_3-x_1x_2,\\
E_3&=x_1x_2-z^2,&E_4&=x_1x_3-zx_2,&E_5&=zx_3-x_2^2.
\end{aligned}
\]
For a normalized pair \(Q_1=-E_3-aE_0-bE_1-cE_2-dE_4-eE_5\), \(Q_2=fE_0+gE_1+hE_2+iE_4+jE_5\), the entire conductor algebra from Section 2 has coefficients
\[
\begin{aligned}
A&=ax_0-bx_1-dx_2+ex_3,\\
R_1&=x_1x_2-ax_1^2+bx_0x_2+c(x_0x_3-x_1x_2)+dx_1x_3-ex_2^2,\\
L&=fx_0-gx_1-ix_2+jx_3,\\
R&=-fx_1^2+gx_0x_2+h(x_0x_3-x_1x_2)+ix_1x_3-jx_2^2.
\end{aligned}
\]
With \(z_c=U^2V^2\), restriction to the curve yields \(R_C=-z_cL_C\) and \((R_1)_C=z_c^2-A_Cz_c\). Over a zero of \(L_C\), the two possible omitted coordinates are \(z_c\) and \(A_C-z_c\). The singleton full-inverse-support condition therefore forces
\[
\operatorname{Supp}\operatorname{div}(L_C)\subseteq\operatorname{Supp}\operatorname{div}(A_C-2z_c).
\]
Since \(L_C\) has zero middle coefficient while \(A_C-2z_c\) has middle coefficient \(-2\), a squarefree \(L_C\) is impossible. This is a necessary support condition, not an assertion that all repeated-root strata are excluded by the same argument. The exact symbolic companion is [verify_session_genus_one_entire_conductor_2026_10_09.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_genus_one_entire_conductor_2026_10_09.py).

## 15. Genus-two conductor-line positions on the fixed quartic

Under the accepted genus-two blowup and mate-stratum hypotheses, if \(\Gamma=V(t_0,t_1)\) is the conductor line and \(f\) is the basepoint-free adjoint pencil, then \(t_i=g s_i\) with \(\operatorname{div}(g)=D_M\sim-K_M\). Consequently the scheme-theoretic intersection length is
\[
\tau=\operatorname{length}(C\cap\Gamma)=D_M\cdot c^\#=4-f\cdot c^\#.
\]
The two strata give \(\tau=2\) for \(\lambda=0\) and \(\tau=3\) for \(\lambda=1\), including nonreduced contact.

The unique quadric \(q=x_0x_3-x_1x_2\) restricts to degree two on any line. Thus a line meeting \(C\) in length at least three lies on \(q\), and the complete trisecant family is
\[
\Gamma_\kappa: x_2-\kappa x_0=x_3-\kappa x_1=0\quad(\kappa\in k),\qquad
\Gamma_\infty: x_0=x_1=0.
\]
Their common restriction divisor has degree three: three distinct points for \(\kappa\ne0,\infty\), and a triple endpoint for \(\kappa=0,\infty\). No trisecant has contact partition \([2,1]\); no line meets \(C\) in length four.

For \(P(a)=[1:a:a^3:a^4]\), the secant through distinct finite \(a,b\) lies on \(q\) precisely when \(a^2+ab+b^2=0\), equivalently \(a^3=b^3\). Otherwise it is an ordinary bisecant. At finite \(a\), \(q(\ell P(a)+mP'(a))=-3a^2m^2\), so its tangent has length two for \(a\ne0\), but the endpoint tangent is a trisecant. Ordinary bisecants through infinity are included. Explicit line equations for finite \(a,b\) are
\[
\begin{aligned}
T_0&=x_2-(a^2+ab+b^2)x_1+ab(a+b)x_0,\\
T_1&=x_3-(a+b)(a^2+b^2)x_1+ab(a^2+ab+b^2)x_0.
\end{aligned}
\]
After removing the common factor \((t-as)(t-bs)\), their restrictions are \(s(t+(a+b)s)\) and \(t^2+(a+b)st+(a^2+ab+b^2)s^2\). For a secant through infinity, \(T_0=x_1-ax_0\), \(T_1=x_2-a^3x_0\), with residual quadrics \(s^2\) and \(t^2+ast+a^2s^2\). The exact executable identity check is [verify_session_genus_two_line_positions_2026_10_10.m2](https://github.com/markluxton1/STCI/blob/3a50e7675d965bd5fa15084189aaab750620bca3/research/computations/verify_session_genus_two_line_positions_2026_10_10.m2).

A useful limitation: three intersections of \(C\) with \(\Gamma\) do **not** automatically produce three branch points of the residual degree-two conductor cover. Horizontal components can be connected to the strict curve by ADE chains and contracted, identifying points downstairs. The separate all-length chain arguments must be used instead of naive branch counting. Also, the adjoint pencil argument gives \(h^0(M,-K_M)=1\), not \(h^0(M,-nK_M)=1\) for every \(n\); the mate correction may have fractional coefficients.


## 16. Bisection fiber counts: integral descent and the three-center obstruction

**Scope:** characteristic-zero genus-two bisection under the second-pencil reduction, not an unrestricted STCI statement. On the four-blowup model \(M\to V\), let \(F_t\) be the **entire** fiber, \(k_t\) the number of centers over it, and \(R_t\) the relative canonical contribution. The exact correction is
\[
Z_t=\tfrac{k_t}{2}F_t-R_t,\qquad c\cdot Z_t=k_t,\qquad \sum_t k_t=4.
\]
Every positive component of \(Z\) is a vertical exceptional \((-2)\)-curve. Positivity of intersections and \((c+Z)\cdot E=0\) show that its positive support contains **whole connected exceptional graphs**, not arbitrary subgraphs.

### Bisection with an even fiber count

If \(k_t>0\) is even, \(Z_t\) is an effective integral divisor. The equality
\(c\cdot Z_t=k_t>0\) puts a point of the strict curve on its positive support.
Let \(p\) be the image of a contacted graph. Support closure means that
the whole exceptional fiber over \(p\) has its integral correction
\(Z_p\) in one full \(f\)-fiber. Thus the line bundle
\(N=\mathcal O_M(c+Z_p)\) has degree zero on every exceptional component
over \(p\).

Apply [Kollár, Chapter 2, Proposition 76(1), PDF pp. 35–36](https://web.math.princeton.edu/~kollar/book/chap2.pdf).
The conductor argument establishes rationality of the singularities of
\(S\). The resolution is log minimal with zero boundary since adjunction
gives \(K_M\cdot E=-2-E^2\ge0\) on every exceptional \((-2)\)- or
\((-3)\)-curve. A log resolution refinement preserves degree zero on
every exceptional component, including the newly created ones. The descent
theorem gives \(N=\sigma^*P\) for an invertible \(P\) near \(p\); it does
not require \(K_S\) to be Cartier or \(\mathbf Q\)-Cartier. Away from
\(p\), \(P\) agrees with \(\mathcal O_S(c_S)\), so reflexivity on the
normal surface identifies the sheaves at \(p\) too.

The actual smooth embedded \(c_S\) is therefore Cartier at \(p\).
If \(g\) is its local equation and \(u\) lifts a generator of the maximal
ideal on \(c_S\), then \((g,u)\) generates the surface maximal ideal by
Nakayama. This forces regularity, contradicting the singular point on the
minimal resolution. The counts allow reducible and nonreduced fibers and
infinitely near centers. The excluded partitions are \([4]\), \([2,2]\)
and \([2,1,1]\), leaving \([3,1]\) and \([1,1,1,1]\) in this argument.

The separate parity auditor checked Proposition 76, support closure, the
entire local correction, reflexive extension to the actual curve and
the regular-local-ring contradiction. Acceptance covers every positive even
count under the characteristic-zero second-pencil and smooth-lift
hypotheses. [Proof and independent decision in the historical source](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/GENUS_TWO_BISECTION_EVEN_FIBER_PROOF.md#6-consequences-and-surviving-scope).

**Three-center exclusion (conditional on the same geometric inputs; source originally awaited a separate parent audit).** The nef-anticanonical rational pencil on \(V\) has three possible entire-fiber types: an irreducible smooth component of square zero; a reduced chain with two \((-1)\) ends; or a nonreduced tree with one multiplicity-two \((-1)\) component, two multiplicity-one leaves, and a possibly empty multiplicity-two tail. A blowup of an old \((-2)\) component is forbidden by nefness. For \(k_t=3\), every old \((-1)\) must be hit exactly once, an old square-zero component exactly twice, and a positive-coefficient new exceptional component must finish with square \(-2\). At each new center,
\[
\operatorname{coeff}_{E}(Z_t)=\tfrac32\operatorname{mult}_{E}(F_t)-\operatorname{coeff}_{E}(R_t).
\]
These rules leave exactly the following configurations:

| Original \(V\)-fiber | Forced positive exceptional graph | Obstruction |
| --- | --- | --- |
| Irreducible | \(A_3\) chain, coefficients \(3/2,1,1/2\) | The strict curve has intersection two with the same connected exceptional graph, not one transverse contact |
| Reduced | \(D_4\) star, central coefficient \(2\), leaves \(3/2,3/2,1\) | The strict curve meets both original \((-1)\) ends in one connected graph |
| Nonreduced | \(D_n\), \(n\ge5\), with contact component coefficient \(3\); shortest \(D_5\) correction \(3A+\frac32(B_1+B_2)+2E_1+E_2\) | No positive **integral anti-nef uniformizer cycle** can have coefficient one at the contact component |

The nonreduced case is a substantive near-counterexample to a purely numerical argument: the rational correction is effective and satisfies intersection equations. The obstruction uses a genuine local uniformizer of the smooth downstairs curve. An integral anti-nef cycle with contact coefficient one propagates coefficient one along the \((-2)\) long arm; at the trivalent fork, anti-nefness would demand \(2\ge1+1+1\), impossible. Thus the three-center partition \([3,1]\) is excluded **within the conditional argument**, leaving only \([1,1,1,1]\). Preserve the source's exhaustive center-history proof and status distinction: [three-center fiber analysis](../../arguments/carriers/genus_two_bisection_three_center_proof.md).

## 17. Trisecant carrier ideal and discriminant boundary

For a finite trisecant \(\Gamma_a=(z,w)\), set \(u=x_0\), \(v=x_1\), \(z=x_2-ax_0\), \(w=x_3-ax_1\), \(q=uw-vz\), and
\[
T_a=z^3+auz^2-vw^2
=(x_2^3-x_1x_3^2)-2a(x_0x_2^2-x_1^2x_3)+a^2(x_0^2x_2-x_1^3).
\]
The **entire homogeneous ideal**, not merely its radical or degree-four component, is
\[
I(C)\cap I(\Gamma_a)^2=(qz,qw,T_a).
\]
On the smooth quadric \(q\), the cubic \(T_a\) cuts \(C+2\Gamma_a\). Subtracting its multiple from any section vanishing along \(C\) and twice along \(\Gamma_a\) leaves a multiple of \(q\), whose quotient must lie in \((z,w)\). Alternatively the three generators are maximal minors of
\[
\begin{pmatrix}
w&z^2+auz\\ -z&-vw\\0&-q
\end{pmatrix}.
\]
The quartics through \(C\) and double along \(\Gamma_a\) therefore have the exact form
\[
F=qQ+T_aL_0,\quad Q\in(z,w)_2,\quad L_0\in k[x_0,x_1,x_2,x_3]_1,
\]
an **11-dimensional** space (seven dimensions for \(q(z,w)_2\), four for \(T_aR_1\)). Their divisor on \(q\) is \(C+2\Gamma_a+(q\cap V(L_0))\); the residual conic may split.

**Conditional reduced-discriminant obstruction.** Under the normal ambient blowup/conductor identification, a mate forces the quadratic conductor discriminant to vanish at every \(C\cap\Gamma_a\) contact. For the generic trisecant \(\Gamma_1\), write the first normal quadratic part of \(F\) as \(A_2z^2+B_2zw+C_2w^2\), with
\[
A_2=-v\alpha+u\ell,\quad B_2=u\alpha-v\beta,\quad C_2=u\beta-v\ell,
\]
where \(\alpha=a_0u+a_1v\), \(\beta=b_0u+b_1v\), \(\ell=c_0u+c_1v\). At \(r=v/u\), \(r^3=1\), the discriminant is the square \((\alpha(1,r)+r\beta(1,r)-2r^2\ell(1,r))^2\). Vanishing at all three contacts gives
\[
a_0=2c_1,\quad a_1=-b_0,\quad b_1=2c_0,\qquad
\Delta=4(v^3-u^3)[(c_0^2+b_0c_1)v+(b_0c_0-c_1^2)u].
\]
When \(\Delta\ne0\), a horizontal exceptional section in the correction forces a double root of \(\Delta\), so the three contact roots allow only one such section. Normalizing its contact to \(r=1\) gives \(\Delta=4\kappa(v^3-u^3)(v-u)\) with \(\kappa=c_0^2-c_0c_1+c_1^2\ne0\). The residual conductor meets the horizontal section in two ordinary nodes. Their ADE resolutions yield at most two \(A_n\) arms. The exceptional correction coefficient at the horizontal section is one, but the adjacent chain coefficients cannot satisfy the required intersection equation: without a curve contact an arm contributes \(n/(n+1)<1\), and with one contact it contributes \(n/(n+1)+(n+1-j)/(n+1)<2\). This excludes the **generic-trisecant, nonzero-discriminant** branch under the stated model hypotheses.

**Unresolved boundaries:** \(\Delta\equiv0\), where the residual conductor may be nonreduced; the two endpoint trisecants; and the bisecant lane. Neither the ordinary-node argument nor a three-distinct-contact condition extends automatically to these. The [complete carrier-ideal and conditional discriminant derivation](../../arguments/carriers/genus_two_trisecant_carrier_proof.md) remains useful for its scheme-theoretic proof.


## 18. The genus-one \([2,1,1]\) partition and fixed-center caution

The genus-one net is \(M(d)\eta=0\), with \(\eta_1^2-\eta_0\eta_2\ne0\), and the derivative quartic \(D_d=d_0U^4-d_1U^3V-2d_3U^2V^2-d_4UV^3+d_5V^4\). A hypothetical mate imposes \(\operatorname{rad}(D_{Q_2})\mid D_{Q_1}\). For the \([2,1,1]\) partition, the full net-direction analysis—including reversal and the \(\eta=(0,1,0)\) boundary—reduces the only possible common-basepoint directions to \(\eta=(1,u,u^2/4)\), \(u\ne0\). The associated cubic map has exactly one double fiber. But the omitted-middle coefficient forces the derivative quartic to have a fourth zero outside that fiber, violating full inverse support. The actual projection center is fixed throughout; arbitrary \(\mathrm{PGL}_2\) reparametrizations cannot be used to manufacture an exhaustive classification. This is the distinct \([2,1,1]\) mechanism, not a consequence of the repeated-root \([4]\), \([3,1]\), \([2,2]\) calculations. [Detailed fixed-center proof and exact checker](../../arguments/carriers/genus_one_211_projection_proof.md).

There is also a necessary **ramification countershield**: an isolated rank-one differential of a projection from a smooth surface point does not by itself force a residual curve, a nonnormal surface, or failure of the mate condition. Such an inference requires an actual global fiber, divisor, or conductor obstruction. In particular, two toric model families are not automatically exhaustive when their coordinate changes move the omitted-middle projection center. The uniform projection analysis keeps the complete fibers, including points over singularities and the parameter endpoints, rather than treating a convenient affine chart as global. [Actual-coordinate projection analysis](../../arguments/carriers/genus_one_uniform_projection_analysis.md).

## 19. Genus-two marked section case

### Free-chain proof when the marked prime is absent

Assume that the horizontal prime \(B=e_0-e_i-e_j\) of plane degree zero
is absent. In the plane marking below there is one double center \(p_0\)
and eight simple centers. For the strict exceptional curve
\(D_i=e_i-\sum_{j\succ i}e_j\), nefness gives
\(L\cdot D_i=m_i-\sum_{j\succ i}m_j\ge0\), where \(j\succ i\)
denotes a proximate center, \(m_0=2\) and \(m_i=1\) for \(i>0\).
Each simple center has at most one proximate child. The double center
must be proper and can have at most one proximate child, since two would
produce \(B\). A satellite would require two proximate children at the
older of its two exceptional curves. The clusters are therefore free
chains. A simple cluster with \(N\) centers has null prefix
\(A_{N-1}\), ending at the last center of positive \(L\)-degree.
The chain rooted at \(p_0\) cannot meet a horizontal proper line, which
avoids \(p_0\).

Smooth embedded descent permits at most one \(h\)-positive prime per
connected exceptional graph. The \(h\)-positive exceptional primes
are proper lines. A horizontal one passes through four simple centers
and a vertical one passes through \(p_0\) and two simple centers.
Once a free chain leaves a line it cannot return, since the next center
lies at a different point of the previous exceptional divisor.

At a singular point on the smooth downstairs curve, choose a local
function on \(S\) restricting to a uniformizer on that curve. The
exceptional part \(Y\) of its full pullback has positive integral
coefficients. The proper part has nonnegative intersection with every
exceptional prime, so \(Y\) is anti-nef. The unique transverse contact
has coefficient one, since the pullback has order one on the strict
curve. When a contacted \((-3)\)-curve \(H\) meets the \(s\)-th vertex
of an \(A_{s+t-1}\) chain, write its chain coefficients as \(y_j\),
with \(y_0=y_{s+t}=0\). The differences
\(d_j=y_j-y_{j-1}\) are nonincreasing and have a drop of at least one
at \(s\). Since they are integral, either \(d_s\ge1\) or
\(d_{s+1}\le-1\), so \(y_s\ge\min(s,t)\). At \(H\), the sum of
neighbor coefficients must be at most three.

For a single horizontal line \(H\), a chain of \(s\) centers on it
followed by \(t>0\) centers off it contributes \(st/(s+t)\) to the
Schur complement at \(H\); for \(t=0\) the terminal curve has
positive \(L\)-degree and the cluster contributes no arm. The unique
horizontal line has coefficient one in \(Z\). Its equation
\(Z\cdot H=-1\) and the homogeneous chain equations require the
contributions to sum to two. For the attached clusters
\(A=\sum s\le4\) and \(T=\sum t\le4\).
Cauchy gives \(\sum st/(s+t)\le AT/(A+T)\le2\), with equality only
when \(A=T=4\) and each \(s=t\). The integer chain test then requires
a sum of neighboring coefficients at least four, contradicting three.

Two disjoint horizontal proper lines on the resolution share exactly one
simple plane center and together use seven of the eight simple centers.
The shared cluster follows at most one line, say \(H_1\). It cannot leave
that line, since the resulting null chain would connect both
\(h\)-positive lines in one exceptional graph. Hence its null prefix is an
endpoint \(A_k\) arm on \(H_2\), with \(k\le3\). The one center
outside the lines can create at most one additional endpoint \(A_s\) arm,
\(s\le3\), with the sharper restriction \(s\le3-k\) if the arm is on
\(H_1\). It cannot attach in the shared cluster. The two contributions
are at most \(3/4\) each. The sum of the two horizontal coefficients
\(1/(3-d_i)\), where \(d_i\) is the sum of arms on that line, is at most
\(8/9\) when the arms are split and at most one when they are on the
same line. The required \(K_M\cdot Z=1\) forces the latter bound to
be attained, with \(k=s=3\).

The equality configuration uses two clusters. The shared root follows
\(H_1\) for three more centers. A second root on \(H_2\) follows that
line for two more centers and takes the only center off both lines.
A vertical exceptional line through \(p_0\) cannot contain both
roots, whose joining line is \(H_2\), and cannot contain later centers
at either root because its direction differs from that of the first
child. There is no vertical exceptional proper line. The two horizontal
lines therefore give \(h\cdot Z=1\), contrary to \(h\cdot Z=3\).

Two preliminary bounds fail. Four consecutive on-line centers followed
by four off-line centers give an \(A_7\) arm attached at its middle,
not a four-vertex bound. Its rational coefficient at \(H\) can be
one, but the integral anti-nef cycle requires a neighboring coefficient
of at least four. In the two-line case a shared root followed by three
centers on \(H_1\) gives an \(A_3\) arm on \(H_2\), allowing coefficient
\(4/9\) there and \(1/3\) on the isolated line, so the proposed individual
bound \(2/5\) fails. A second \(A_3\) arm can arise from the remaining
off-line center; the proposed total bound \(19/21\) misses this case.

Independent review accepted both line cases under the characteristic-zero
marked section and smooth descent hypotheses with \(B\) absent. The
integer recurrences and intersection inequalities alone remain available
when those geometric inputs are established in another characteristic.
[Original free-chain proof and negative controls](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/GENUS_TWO_LAMBDA_ONE_HORIZONTAL_LINE_BUDGET.md).

### Marked constraints and the case with the horizontal prime

For the genus-two section stratum \(\lambda=1\), the plane marking gives
\[
c^\#=h,\quad L=4h-2e_0-\sum_{i=1}^8e_i,\quad
f=h-e_0,\quad Z=L-h=3h-2e_0-\sum_{i=1}^8e_i,
\]
with \(Z\) effective, exceptional, \(K\cdot Z=1\), and \(Z^2=-3\). The vertical root lattice is \(D_8\). The marked blowup clusters and proximity relations are part of the geometry: they cannot be replaced by an arbitrary abstract ADE graph. A candidate horizontal degree-zero exceptional prime is \(B=e_0-e_i-e_j\); when it is present, a satellite can attach it to an **internal** vertex of an \(A\)-chain. A blanket three-arm-star classification is therefore false.

Under the additional assumption that \(B\) is **absent**, the free-chain and line-budget analysis excludes the section case. The proof first requires an **integral anti-nef cycle** with contact coefficient one at the unique contacted exceptional prime; rational correction coefficients alone do not suffice. The possible horizontal proper lines through the first center have tightly constrained center incidence. The one-line case fails the integral contact and coefficient budget. In the two-line equality case the two horizontal lines each contain the required marked centers, but no vertical proper exceptional line can supply the missing \(h\)-degree: the total horizontal coefficient gives \(h\cdot Z=1\), contrary to \(h\cdot Z=3\). This two-line conclusion was independently accepted. Consequently any surviving \(\lambda=1\) configuration must contain \(B\). The free-child and one-satellite graphs with \(B\) present remain a separate boundary; neither a reduced-conductor shortcut nor the invalid universal star bound excludes them. [Marked-model derivation](../../arguments/carriers/genus_two_marking_and_section_proof.md).
