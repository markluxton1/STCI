# Quartic carrier lanes and genus-one algebra

[Carrier Framework](index.md) · [Original section addresses](quartic_proof_interfaces.md)

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

The [conormal-net proof](../../arguments/carriers/genus_one_ribbon_conormal_net_proof.md) establishes \(I_c/I_c^2\simeq\mathcal O_c(-6)^3\) and the complete three-parameter quotient net. Its discriminant-zero orbit has a cubic common base locus, so only \(\Delta=B^2-AC\ne0\) can give the required integral surface.

The [complete repeated-partition proof](../../arguments/carriers/genus_one_ribbon_partition_proofs.md) covers \([4]\), \([3,1]\), and \([2,2]\), including all kernel-direction and center-preserving coordinate boundaries. For nonendpoint \([3,1]\), determinant \(-k(k^2+9)\) and the full ideal equality leave a pencil singular along a line; the roots \(k^2=-9\) are excluded by ideal equality, not chart selection. For \([2,2]\), determinant \(-(2k+1)(2k^2-k+8)/4\) and the full ideal equality leave the exceptional direction \(\eta=(1,0,2)\). Its conductor trace–norm obstruction excludes descent of **every** positive power, not merely a bounded list. The exact pencil, coefficient identities, and certificates remain in that Argument. The omitted-middle projection center is fixed throughout; arbitrary \(\mathrm{PGL}_2\) changes are not permitted.

### Endpoint [4] derivative partition: direct line-singularity argument

In characteristic zero the derivative quartic in this branch lacks a \(U^2V^2\) term. A quadruple root therefore forces \(6\alpha^2\beta^2=0\), hence an endpoint root. Center-preserving reversal reduces to \(Q_2=E_0+hE_2\); the net determinant \(-h^3\) forces \(h=0\). The other pencil quadric is then, modulo \(E_0\), a combination of \(E_1\) and \(E_3-E_2\), giving a common singular line \(Y_0=Y_1=Y_2=0\). This excludes the entire \([4]\) partition under the normal genus-one model assumptions. The complete coefficient derivation and boundary coverage are in [the repeated-partition proof](../../arguments/carriers/genus_one_ribbon_partition_proofs.md#2-partition-4-both-endpoints-and-every-direction).

### Explicit trace–norm certificate for the surviving displayed [2,2] pencil

For the unique surviving displayed \([2,2]\) pencil, the [complete calculation](../../arguments/carriers/genus_one_ribbon_partition_proofs.md#5-the-sole-22-pencil-has-no-descending-power) works in the entire quadratic conductor algebra, including its trace and norm. Its conic is smooth (matrix determinant \(243/128\)); the reduced trace-square and norm have coefficient minor \(120\ne0\). Equivalently, on a two-point slice \(18t^2-1=0\), the ratio \(T^2/N=22+72t\) is nonconstant. If \(Q^n\) descended for any \(n>0\), the conjugate ratio \(r\) would satisfy \(r^n=1\), forcing \(T^2/N=2+r+r^{-1}\) to be constant. The proof is for this fixed pencil; exhaustive \([2,2]\) coverage uses the preceding ideal classification.

