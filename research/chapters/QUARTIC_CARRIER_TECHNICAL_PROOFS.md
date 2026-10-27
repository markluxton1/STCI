# Quartic-carrier exclusion: technical proof mechanisms

**Scope.** The fixed rational quartic is \(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), over an algebraically closed field of characteristic zero. This appendix supports the [carrier and conductor chapter](CARRIER_AND_CONDUCTOR_GEOMETRY.md) and the canonical [R-0001 theorem](../results/quartic_carrier_exclusion.md). It is **not** an independent rerun of the full theorem. Original detailed proofs and audits remain authoritative for steps not reproduced below.

## 1. What the six lanes actually need

| Lane | Essential exact input | Technical proof home |
|---|---|---|
| Normal quartic | Reduced and nonreduced exceptional graphs; normal-sheaf bounds; final passage coefficients | [normal global audit](../notes/2026-10-07-session-normal-global-adversarial.md), [nonreduced audit](../notes/2026-10-07-session-normal-nonreduced-independent-audit.md) |
| Genus zero | Vanishing and four minimal-degree models; cone ruling and local-unit obstruction; complete scroll/Veronese cases | [genus-zero audit](../notes/2026-10-09-session-normalization-genus-zero-independent-audit.md) |
| Genus one | ADE degree-four del Pezzo; \(D_5\) lattice saturation; full conductor; ribbon-net and five partitions | [genus-one interface audit](../notes/2026-10-10-session-genus-one-interface-independent-audit.md), [repeated-partition audit](../notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md) |
| Genus two, bisection | Second-pencil integral correction, Cartier double, nilideal and global conormal map | [bisection audit](../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md) |
| Genus two, nonendpoint | Complete effective-divisor split; all-length chain formula | [nonendpoint audit](../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md) |
| Genus two, endpoint | Full quartic ideal identity; coefficient-zero cases, local A/D types, doubled-horizontal ADE roots | [endpoint full audit](../notes/2026-10-10-session-genus-two-endpoint-full-independent-audit.md) |

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
The off-conic condition \(\eta_1^2\ne\eta_0\eta_2\) is necessary for the surface to remain an integral two-quadric intersection. The derivative binary quartic then has exactly the partitions \([1,1,1,1]\), \([2,1,1]\), \([2,2]\), \([3,1]\), \([4]\). The first two are excluded by the fixed-center argument; the other three by universal ideal calculations. In particular, the invisible \(d_2\)-coefficient and all kernel-direction boundaries must be retained. The [independent repeated-partition audit](../notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md) contains the actual ideal certificates and successful Macaulay2 check, not just sample pencils.

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
It is free of rank two over \(C_\Gamma\), including over doubled or reducible conics. The trace-zero generator \(w=z-A/2\) satisfies \(w^2=A^2/4+R_1\). This derivation, including the sign in \(Rz=AR-LR_1\), is independently checked in the [algebra audit](../notes/2026-10-09-session-genus-one-entire-conductor-algebra-independent-audit.md). The [owner proof](../notes/2026-10-09-session-genus-one-entire-conductor.md) also gives the six exact fixed-curve quadrics and their coefficient restrictions, which remain necessary for the root-partition arguments.

## 3. Nonendpoint trisecant: exact all-length contradiction

The normal conic model has an exceptional divisor of bidegree \((2,2)\) on \(\mathbf P^1\times\mathbf P^1\), with distinguished horizontal \(B\) of class \((1,0)\). Multiplicity two on \(B\) leaves two ruling fibers and violates singleton inverse support. With multiplicity one, the residual class is \((1,2)\). Every reducible residual is either a \((1,1)\) curve plus a ruling fiber or a second horizontal plus two ruling fibers, including doubled fibers; the [audit](../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md) handles the coefficient-zero horizontal boundary. The remaining integral residual is a rational graph, meeting \(B\) in two transverse points.

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
which gives every relevant quartic as \(F=qQ+DL_0\) (notation defined in the [full reduction](../notes/2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md)). The independent coverage audit exhausts the coefficient regimes \(c_0\ne0\), \(a_1\ne0\), \(a_1=0,b_1\ne0\), and \(a_1=b_1=0,c_1\ne0\). This includes the second horizontal fiber at infinity and doubled components.

In the distinct-crossing case the same all-length inequality as Section 3 applies. At triple contact the actual local models include endpoint \(A_n\) chains, an internal \(A_n\) attachment with coefficient \(2/(n+5)<1\), and a \(D_4\) configuration with coefficient \(1/4\); multiplicity three is incompatible with the accepted ADE model. These are **realized local positions in the full equation**, not arbitrary graph possibilities.

For the doubled-horizontal divisor \(2B+2F_0\), the normal derivative along \(B\) is a nonzero section
\[
h(b)=b(A+B_1b+Cb^2)\in H^0(B,\mathcal O_B(3)).
\]
Its zeros, including infinity and repeated roots, have total multiplicity three. For any ADE block, write \(Q=(-E_i\cdot E_j)\), \(v_i=B\cdot E_i\), and \(g_{BB}=v^tQ^{-1}v\). At a root away from the curve contact, the exact crepant residue and divisor calculation gives
\[
2g_{BB}=\operatorname{ord}(h).
\]
The correction equation with \(z_B=1\) requires total block contribution three. If \(A\ne0\), the contact contributes strictly below two and the other roots contribute one; if \(A=0\), the contact order is \(k=2\) or \(3\), the contact contributes at most \((k+2)/2\), and the remaining roots contribute \((3-k)/2\), totaling at most \(5/2\). Both contradict three. This argument handles arbitrary ADE blocks, not just short \(A\)-chains. Its local-coordinate proof and hypotheses remain in the [endpoint independent audit](../notes/2026-10-10-session-genus-two-endpoint-full-independent-audit.md).

## 5. Two earlier proof paths: exact overlap and unique content

The following comparison is based on reading the original notes, not just their titles or status labels. It determines **mathematical redundancy**, not yet safe file deletion.

**Earlier endpoint irreducible-residual note.** The [conditional irreducible-conic proof](../notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md) assumes \(D_T=B_T+R\) with \(R\) irreducible of class \((1,2)\). It identifies the endpoint blowup chart \(a=r,b=r,y=r^3\), writes \(aR(a,b)+yH=0\), and uses the cubic contact to force \(R(r,r)\) to vanish to order at least two. The graph \(a=\phi(b)\) then has \(\phi(0)=0,\phi'(0)=1\), so the degree-two map \(R\to\Gamma\) is unramified at the endpoint. Its two transverse crossings yield the same all-length inequality reproduced in Section 3. The later [full endpoint reduction](../notes/2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md) and [coverage audit](../notes/2026-10-10-session-genus-two-endpoint-full-independent-audit.md) handle **all** residual types. The earlier note's distinct value is the short geometric derivation of the irreducible graph's transverse crossings. This derivation is not yet reproduced in full in the permanent exposition; **retain the note pending extraction**. Its conditional theorem is subsumed, but that alone is not a reason to delete its proof.

**Earlier bisection quadratic-descent note.** The [quadratic compression proof](../notes/2026-10-10-session-genus-two-bisection-quadratic-descent.md) derives \(2Z=\sum_t k_tF_t-2R\) from four blowups (including infinitely near centers), so \(2c\sim2H\). It then studies the entire conductor sequence
\[
0\to\mathcal O_X\to\nu_*\mathcal O_S\to\mathcal O_\Gamma(-2)\to0
\]
and its rank-two algebra \(p_*\mathcal O_D=\mathcal O_\Gamma\oplus\mathcal O_\Gamma(-2)\), with trace-zero generator \(w\) satisfying \(w^2=\delta\). The compressed quadratic section has conductor restriction \(Q|_D=m+w\), with \(m\in H^0(\Gamma,\mathcal O(2))\). If \(m=0\), \(Q^2\) descends to an ambient quartic, contradicting the independent \((4,4)\) exclusion. For \(m\ne0\), power descent forces \(\delta=r^2\) and \(m=\alpha r\); the split branches have \(Q_\pm=(\alpha\pm1)r\), and descent of \(Q^n\) requires
\[
\left(\frac{\alpha+1}{\alpha-1}\right)^n=1.
\]
These are exact **conductor-power** constraints, not merely a weaker statement that the bisection lane is impossible. The later [global conormal proof](../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md) excludes the lane more efficiently but does not make the root-of-unity and split-conductor calculations mathematically empty. They are reusable for other normalization/descent problems. **Retain these calculations as a separate conditional lemma**; the source's formerly open possibilities are superseded by the conormal contradiction.

The two sources therefore have different retention status: the endpoint note is a **candidate for retirement after its geometric graph argument is extracted**, whereas the bisection note contains **independent conductor algebra worth retaining** even though its mate-existence motivation has closed.

### Endpoint irreducible graph: extracted geometric argument

The earlier conditional endpoint note's distinct geometric step can be recorded precisely. In the blowup chart \(x_0=1\), set \(a=x_1/x_0\), \(y=x_2/x_0\), \(x_3/x_0=yb\). The strict transform of \(C\), parametrized by \(r=t/s\), is
\[
a=r,\qquad b=r,\qquad y=r^3.
\]
For an irreducible residual \(R\) of class \((1,2)\), the transformed surface has local equation \(aR(a,b)+yH(a,b,y)=0\). Restriction to \(C\) forces \(R(r,r)\) to vanish to order at least two. Since an irreducible \((1,2)\) curve is a graph \(a=\phi(b)\) and cannot contain the ruling fiber \(b=0\), it follows that \(\phi(0)=0\) and \(\phi'(0)=1\). The degree-two map \(R\to\Gamma\) is therefore unramified over the endpoint, with two distinct inverse points (the second possibly in the opposite chart). Both intersections with \(B=\{a=0\}\) are transverse. This supplies the geometric input for the all-length chain calculation in Section 3.

This extraction captures the earlier note's mathematical argument and its precise **irreducible-residual** hypothesis; the later full endpoint proof remains necessary for reducible and doubled residuals. The [original conditional note](../notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md) can now be treated as a **candidate for archival retirement**, subject to a repository-wide inbound-reference and unique-evidence check. No source deletion is performed here.

## 6. Evidence and retention

The exposition above reproduces the short universal inequalities and identifies the longer exact calculations. It does not re-execute Macaulay2, independently establish the classical classification theorems, or replace the source audits. The [independent assembly audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md) checks that the normal and nonnormal lanes cover every integral quartic and that the final lower-degree argument is noncircular.

**Retain for now:** all canonical theorem records, primary owner proofs, independent mathematical audits, exact computational certificates and failed-approach explanations with distinct mathematical content. Only duplicate orientation or narrative files should be considered for removal after their claims are mapped to these permanent sections.
