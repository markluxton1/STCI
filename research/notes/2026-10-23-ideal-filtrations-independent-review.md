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
