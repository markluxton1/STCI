# A supported length-five family whose comparison defect does not specialize

**Scope and status.** This is an independently reviewed exact local calculation. It concerns the smooth affine line in a smooth affine threefold, in arbitrary characteristic. It does not construct a homogeneous projective pair for the fixed quartic, and it does not settle whether a sole-support complete intersection with generically zero comparison defect can have a nonzero punctual relative defect. Its contribution is a stronger support-only control: the relative defect is zero, although the actual closed transverse fibre has nonzero defect. The full initial ideal, the initial ideal of the product, and the actual filtered equation module are all computed below.

The governing comparison is [R-0030](../results/local_filtration_comparison_defect.md), with its full local proofs in [the equation-filtration supplement](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md). The distinction below is separate from the existing length-four control there: in that control the closed fibre also has zero field defect.

## 1. Equations, support, and a free actual algebra

Let \(k\) be any field, \(A=k[[t]]\), \(R=A[[x,y]]\), and (I=\(x,y\)). Put
\[
 f=x^2-txy+y^3,\qquad g=xy+ty^2-t^2x,\qquad J=(f,g).
\]
The same equations give an algebraic family over \(k[t]\). The calculation is valid after localizing at the origin or completing there. One can replace \(f\) by
\[
 f+tg=x^2+y^3+t^2y^2-t^3x.
\]
Define the following further actual equations:
\[
 k_3=txy^2-y^4=(t^2-y)f+(x-ty)g,
\]
\[
 k_4=xy^3=tk_3+y^2g,
 \qquad k_5=y^5=tk_4-yk_3.
\tag{1}
\]
In particular \(y^5\in J\). The equation \(f\) gives x^2 in the ideal \(y\) modulo J, so x is nilpotent once y is; hence \(\sqrt J=I\).

Here is a direct normal-form proof, including freeness rather than merely a length assertion. In \(R/J\),
\[
 xy=t^2x-ty^2,\quad
 x^2=t^3x-t^2y^2-y^3,\quad
 y^4=t^5x-t^4y^2-t^2y^3,
\tag{2}
\]
and
\[
 x^3=x^2y=xy^3=y^5=0.
\tag{3}
\]
Consequently \(R/J\) is spanned over \(A\) by
\[
 1,x,y,y^2,y^3.
\tag{4}
\]
There are no hidden coefficient relations. On the free module with basis (4), define multiplication by \(x\) and \(y\) by (2), by \(xy^2=t^4x-t^3y^2-ty^3\), and by \(xy^3=0\). The two matrices commute and satisfy \(X^2-tXY+Y^3=0\) and \(XY+tY^2-t^2X=0\). Their cyclic vector (1) generates all five basis vectors. This constructs an inverse to the proposed normal-form presentation. This argument uses integer-coefficient identities and is valid in every characteristic.

Thus \(R/J\) is free of rank five over \(A\), its sole reduced support is the marked line, and \(J\) has height two. Since the ambient ring is regular, the displayed two equations are a regular sequence. No inference from vertical components of a normal cone enters this support proof.

## 2. Full normal initial ideal

Write \(S=A[X,Y]=\operatorname{gr}_I R\). The full initial ideal is
\[
 \boxed{H=\operatorname{in}_I J
   =(t^2X,\ X^2-tXY,\ tXY^2,\ XY^3,\ Y^5).}
\tag{5}
\]
The inclusions from right to left follow from \(g,f,k_3,k_4,k_5\). To prove fullness without guessing from these symbols, compute every power of the image (N=I\(R/J\)) in the free actual algebra (4). Set
\[
 v=t^4x-t^3y^2,\qquad w=tv-t^2y^3.
\]
The exact submodules are
\[
\begin{array}{c|l}
n&N^n\\ \hline
1&A x\oplus A y\oplus A y^2\oplus A y^3\\
2&A(t^2x)\oplus A y^2\oplus A y^3\\
3&A v\oplus A y^3\\
4&A w\\
5&0.
\end{array}
\tag{6}
\]
These follow by multiplication using (2)–(3); the stated direct sums also follow by inspecting coefficients in (4). They hold in arbitrary characteristic.

For explicit verification that (5) is the full kernel, its proposed quotient has the following degree pieces:
\[
\begin{array}{c|l}
n&(S/H)_n\\ \hline
0&A\\
1&A Y\oplus (A/(t^2))X\\
2&A Y^2\oplus (A/(t^2))XY\\
3&A Y^3\oplus (A/(t))XY^2\\
4&A Y^4\\
\ge5&0.
\end{array}
\tag{7}
\]
The free-plus-torsion presentation in degree two follows from \(X^2=tXY\) and \(t^2XY=0\). In degree three it follows from \(X^2Y=tXY^2=0\). On the actual side, degree two is the quotient of (A\(t^2x\)\oplus Ay^2) by (A\(t^4x-t^3y^2\)); its torsion generator is \(xy=t^2x-ty^2\). Degree three is the quotient of \(Av\oplus Ay^3\) by (A\(tv-t^2y^3\)); its torsion generator is \(xy^2=v-ty^3\). The other degrees are immediate from (6). These maps identify each line of (7) with \(N^n/N^{n+1}\), proving (5) in all degrees. This is a complete remainder/power-filtration proof; no truncated initial-generator assumption is being used.

After passing to (K=k(\(t\))), (5) becomes
\[
 H_K=(X,Y^5),
\]
so the generic transverse algebra has length five and the generic comparison defect is zero.

## 3. Actual equation filtration and minimal initial equations

Because \(f,g\) are a regular sequence and belong to \(I\), the actual equation module
\[
 D=J/IJ=Ae_f\oplus Ae_g
\]
is free. Equations (1) give
\[
 [k_3]=t^2e_f,\quad [k_4]=t^3e_f,
 \quad [k_5]=t^4e_f.
\tag{8}
\]
The complete filtration is
\[
\begin{array}{c|l}
n&F^nD\\ \hline
1&Ae_f\oplus Ae_g\\
2&Ae_f\\
3&t^2Ae_f\\
4&t^3Ae_f\\
5&t^4Ae_f\\
6&0.
\end{array}
\tag{9}
\]
For completeness, (5) and the actual lifts \(g,f,k_3,k_4,k_5\) justify both inclusions here. Cancel the lowest normal symbol of an element of \(J\cap I^n\) with these lifts and iterate. Every positive-normal-degree multiplier vanishes in \(D\); the remaining constant multipliers come only from lifts of order at least \(n\). This is the standard filtered division argument, now justified by the all-degree kernel calculation (6)–(7). It terminates for the purpose of \(D\) because \(I^5\subset J\), hence \(I^6\subset IJ\). Applying (8) gives exactly (9).

Therefore
\[
 \operatorname{gr}_F^1D=Ae_g,\quad
 \operatorname{gr}_F^2D=A/(t^2),\quad
 \operatorname{gr}_F^3D=A/(t),\quad
 \operatorname{gr}_F^4D=A/(t),\quad
 \operatorname{gr}_F^5D=A,
\tag{10}
\]
with all other pieces zero. The last free piece is the submodule \(t^4Ae_f\), with its induced identification; no saturation of (9) has been taken.

Independently, (5) gives
\[
\begin{array}{c|l|l}
n&Q_n=(H/S_+H)_n&\text{initial generator}\\ \hline
1&A&-t^2X\\
2&A/(t^2)&X^2-tXY\\
3&A/(t)&tXY^2\\
4&A/(t)&XY^3\\
5&A&Y^5.
\end{array}
\tag{11}
\]
The comparison sends these generators to the actual classes represented by \(g,f,k_3,k_4,k_5\). Equations (8)–(10) show that every line of (11) maps isomorphically onto the corresponding line of (10). In particular all three torsion pieces survive the comparison.

It follows that
\[
 \boxed{\Delta=0,\qquad
 B=\operatorname{in}_I(IJ)=S_+H.}
\tag{12}
\]
An explicit generating set for the latter full initial ideal is
\[
 \boxed{B=(X^3,\ X^2Y-tXY^2,\ t^2X^2,\ t^2XY,
               \ tXY^3,\ XY^4,\ Y^6).}
\tag{13}
\]
Equality of the displayed ideal with \(S_+H\) follows by multiplication in (5). In particular (X^3=X\(X^2-tXY\)+tY\(X^2-tXY\)+t^2XY^2). Thus (13) is an actual calculation of \(B\), rather than an assertion based only on the number of initial equations.

## 4. The actual closed transverse fibre has a different defect

Set \(t=0\) in the actual equations. Then
\[
 J_0=(x^2+y^3,xy)\subset k[[x,y]],
\]
a sole-support, length-five complete intersection, with
\[
 H_0^{\mathrm{actual}}=(X^2,XY,Y^4).
\tag{14}
\]
Indeed (y\(x^2+y^3\)-x\(xy\)=y^4), and the quotient by the displayed initial ideal has the same length five as the actual algebra. Its initial generator space has dimensions two in degree two and one in degree four. On (D_0=J_0/\(x,y\)J_0), both actual generator classes have order two and no nonzero class has higher order, since their degree-two symbols \(X^2,XY\) are linearly independent. Thus
\[
 \Delta_0^{\mathrm{actual}}=k\text{ in degree }4,
\]
\[
 \operatorname{in}_{(x,y)}((x,y)J_0)
       =(X^3,X^2Y,XY^2,Y^4),
\]
whereas
\[
 (X,Y)H_0^{\mathrm{actual}}
       =(X^3,X^2Y,XY^2,Y^5).
\tag{15}
\]
In contrast, taking the coefficient-specialization image of the *relative* initial ideal (5) gives
\[
 \overline H=(H+(t))/(t)=(X^2,XY^3,Y^5),
\]
whose quotient has length eight. Consequently normal-cone formation does not commute with this transverse specialization, despite the actual algebra being finite free of rank five and supported on the marked curve. Moreover
\[
 \Delta\otimes_Ak=0\quad\text{but}\quad
 \Delta_0^{\mathrm{actual}}\simeq k[-4]\ne0.
\tag{16}
\]
The notation \(k[-4]\) here means a single copy in normal degree four.

This control rules out a tempting detection shortcut: finding a nonzero field-valued defect in an exceptional transverse slice does not prove a nonzero punctual relative defect on the curve. A calculation of the full relative comparison remains necessary. It also explains why a family with a special fibre having three minimal initial equations can still have zero relative comparison defect.

## 5. Remaining question and projective limit

The original existence problem remains open in this calculation: no example with \(\sqrt J=I\), \(\Delta_K=0\), and nonzero punctual \(\Delta\) has been produced, and no general vanishing theorem has been proved. This example proves vanishing for one nontrivial supported family, with the complete arithmetic valid over every field; it cannot support a universal vanishing claim.

The equations are weighted homogeneous for weights (\mathrm{wt}\(t,x,y\)=(1,3,2)), of weights six and five. This observation does not supply two ordinary homogeneous equations with sole support on the fixed projective quartic. Ordinary homogenization gives
\[
 F=zx^2-txy+y^3,\qquad G=zxy+ty^2-t^2x
\]
in \(\mathbf P^3_{[z:t:x:y]}\). Besides the marked line \(L=V(x,y)\), these contain the conic \(D=V(z,y^2-tx)\). Put \(q=y^2-tx\). At the generic point of \(D\), the coordinates \(x,y,t\) are units; \(G=0\) gives \(q=-zxy/t\), and then \(F=zx^2+yq\) reduces to \(z^2x^2y/t^2\). Thus the generic conic multiplicity is two.

The two cubics have no common surface factor: their affine equations on \(z=1\) have height two and sole line support, so any additional homogeneous common factor would have to be \(z\), which divides neither cubic. The line multiplicity is five, and degree exhaustion and complete-intersection purity therefore give the entire projective cycle
\[
 [V(F,G)]=5[L]+2[D].
\]
Its degree is nine in every characteristic. This identifies the residual degree four explicitly; the projective closure supplies no sole-support example for the fixed quartic.

## Independent review

Independent reconstruction checked the finite free actual algebra, all powers of its normal ideal, the full initial ideal, terminating filtered division for the equation module, and the comparison in every degree. All identities are integral and require no characteristic exclusions. The closed-fiber mismatch and the doubled residual conic of the projective closure were checked separately. The original existence question for a nonzero punctual relative defect under sole support remains open.
