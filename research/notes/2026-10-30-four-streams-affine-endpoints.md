# Two affine endpoints, actual gluing, and where the residual must appear

Date: 2026-10-30. Status: **independently reviewed provisional deductions**, with the [independent proof audit](2026-10-30-four-streams-affine-endpoints-audit.md). No canonical promotion.

## Scope and what is inherited

Let \(k\) be algebraically closed and

\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k,
\quad p_0=[1:0:0:0],\quad p_\infty=[0:0:0:1].
\]

The principal question is characteristic zero. The elementary descent and connectedness arguments below work in every characteristic. Put

\[
U_0=D_+(x_0),\quad U_\infty=D_+(x_3),\quad
U=U_0\cup U_\infty=\mathbf P^3\setminus M,
\quad M=V(x_0,x_3).
\]

Here \(M\cap C=\varnothing\), while the two omitted hyperplane divisors on \(C\) are \(4p_\infty\) and \(4p_0\). Arbitrary pairs below may define higher multiple structures; neither a fixed carrier nor a prescribed normal form is assumed.

The following are inherited, not new results:

- [P-007](../RESEARCH_RECORD.md#p-007-an-exact-affine-to-projective-boundary-criterion): a radical affine pair has STCI homogenizations exactly when its leading forms are coprime; a reduced affine generating pair cannot solve the projective quartic problem.
- [Formal-neighborhood residual visibility](2026-10-27-formal-neighborhood-residual-visibility.md), sections 2 and 5–6: connectedness detects residual attachment, and a **full globally glued fixed-twist formal pair** with uniform power containment already algebraizes and gives an STCI. There is no further algebraization gap once those exact formal data exist.
- [Coefficient valuations](2026-10-23-intrinsic-coefficient-valuations.md) and [endpoint valuations](2026-10-25-ci-cycle-endpoint-valuations.md): curve valuations, ambient valuations, scalar ideal values, and full residue ideals carry different information.

This note specializes these broad principles to the user's two hyperosculating affine charts, makes their actual transition explicit, and isolates a single-endpoint exact test for **any chosen affine radical pair**. It does not claim a new general nonexistence theorem.

## 1. Once actual split sections glue, the missing line is not an extra obstruction

**Two-chart criterion.** Fix positive integers \(a,b\). The curve \(C\) is the reduced intersection of degree-\((a,b)\) homogeneous equations if and only if there are polynomial pairs

\[
(f_0,g_0)\quad\hbox{on }U_0,\qquad
(f_\infty,g_\infty)\quad\hbox{on }U_\infty
\]

whose zero sets are respectively \(C\cap U_0\) and \(C\cap U_\infty\), and which obey the **actual section identities** on the entire overlap

\[
f_0=(x_3/x_0)^a f_\infty,\qquad
g_0=(x_3/x_0)^b g_\infty.                 \tag{1}
\]

The right sides use the usual change of affine coordinates. No restriction is placed on the generic thickness of either pair, apart from the compatibility already forced by (1).

**Proof of extension.** Write the \(U_0\) coordinates as

\[
z=x_1/x_0,\quad y=x_2/x_0,\quad D=x_3/x_0,
\]

and the \(U_\infty\) coordinates as

\[
A=x_0/x_3,\quad B=x_1/x_3,\quad W=x_2/x_3.
\]

A section identity for twist \(d\) is

\[
h_\infty(A,B,W)=A^d h_0(B/A,W/A,1/A).
\]

The monomial \(z^iy^jD^k\) contributes \(B^iW^jA^{d-i-j-k}\). Distinct triples give distinct Laurent monomials, so there is no cancellation of negative powers of \(A\). Polynomiality on both charts is exactly the condition that every monomial of \(h_0\) has total degree at most \(d\). Consequently \(x_0^d h_0\) is a unique homogeneous polynomial of degree \(d\). This directly proves extension across \(M\), without a bundle-splitting assumption or a convergence argument.

Apply this to obtain \(F_a,G_b\). They have no common surface component: a surface cannot be contained in the line \(M\), so any common surface would meet \(U\), contradicting the prescribed one-dimensional support there. Thus \(Y=V(F,G)\) is a proper projective complete-intersection curve. Every component outside \(C\) is contained in \(M\). Since \(M\cap C=\varnothing\), any such component would disconnect the support of \(Y\).

For completeness, the Koszul resolution and the intermediate cohomology vanishing for line bundles on \(\mathbf P^3\) give

\[
H^1(\mathcal I_Y)=0,\qquad H^0(\mathcal O_Y)=k.
\]

Hence \(Y\) is connected, including when it is nonreduced. No residual component exists. The converse is restriction of the homogeneous equations. The cohomology input is [Stacks, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).

**Geometric meaning.** Compatibility of two arbitrary local ideals is weaker than (1). But once the equations themselves are sections of the same split ambient bundle \(\mathcal O(a)\oplus\mathcal O(b)\), there is no independent curve-at-\(M\) problem left. The complement is codimension two, the sections extend, and a disconnected extra component is impossible for their complete intersection. This is an explicit polynomial version of the already recorded full formal-section principle.

More generally one may first glue the pairs as a section of a rank-two bundle on \(U\). If that bundle is then proved isomorphic to \(\mathcal O_U(a)\oplus\mathcal O_U(b)\), the same conclusion follows after applying that isomorphism. No assertion that arbitrary bundles on \(U\) split, or descend from the base of a ruling, is used here.

## 2. For any chosen affine radical pair, every global failure is visible at one endpoint

Let \(f,g\in k[z,y,D]\) be **any** pair with

\[
\sqrt{(f,g)}=I_{C\cap U_0},
\]

and let \(F,G\) be their ordinary homogenizations. They have no common factor: an affine common hypersurface factor contradicts the radical equality, and ordinary homogenization introduces no \(x_0\) factor. Thus \(Y=V(F,G)\) is a proper CI. Let \(m\) be its generic length along \(C\).

**Single-endpoint criterion.** The following are equivalent:

1. \(Y_{\mathrm{red}}=C\).
2. The completed ideal at \(p_\infty\) contains a power of the completed ideal of \(C\):
   \[
   I_{C,p_\infty}^{N}\widehat{\mathcal O}_{\mathbf P^3,p_\infty}
   \subset (F,G)\widehat{\mathcal O}_{\mathbf P^3,p_\infty}
   \quad\text{for some }N.
   \]
3. The Hilbert–Samuel multiplicity at the endpoint satisfies \(e_{p_\infty}(Y)=m\).

**Proof.** All residual components lie in \(H_\infty=V(x_0)\), because the affine zero set is prescribed. Their union, if nonempty, must meet \(C\) by the connectedness proved above. Since \(C\cap H_\infty=\{p_\infty\}\), some residual component passes through this endpoint. Power containment there excludes such a component; its implication in the local ring follows by faithful-flat contraction from completion. Conversely sole support gives power containment by Noetherianity.

For the multiplicity statement, associativity, smoothness of \(C\), and Cohen–Macaulay purity of the CI give

\[
e_{p_\infty}(Y)
=m+\sum_{D_j\ne C,\ p_\infty\in D_j}
 m_j e_{p_\infty}(D_j).
\]

Every summand is positive. The sum is nonempty precisely when residual components exist, by the preceding argument. One may compute the left side as the length after a sufficiently general local linear slice. The slice-length foundation is [Stacks, Lemma 42.3.2](https://stacks.math.columbia.edu/tag/02QG). This specializes the inherited all-points detector, rather than asserting a new multiplicity theorem.

**Geometric meaning.** An affine STCI pair can acquire a long or reducible residual configuration at infinity. Some components can attach through other residual components, so it is false that every one must pass through \(p_\infty\). Nevertheless the entire failure cannot hide away from that endpoint. A full local endpoint test therefore decides a chosen affine pair, without scanning the whole boundary plane.

This gives the precise scope of a valuative attack: adapt valuations and residue data to the **full endpoint ideal** and its generic thickness. A universal strict inequality \(e_{p_\infty}(Y)>m\) for every characteristic-zero affine radical pair would prove non-STCI. No such inequality has been established here. Conversely a pair achieving equality would construct an STCI. The criterion makes that target exact; it does not supply either outcome.

## 3. The two reduced affine generators do not form an invertible transition on the whole overlap

Put

\[
q=x_0x_3-x_1x_2,\quad c_0=x_1^3-x_0^2x_2,\quad
c_\infty=x_2^3-x_1x_3^2.
\]

The normalized pairs \((q/x_0^2,c_0/x_0^3)\) and \((q/x_3^2,c_\infty/x_3^3)\) generate the reduced ideals on their respective affines. Write the first pair as \((q_0,c_{0,0})=(D-zy,z^3-y)\). The exact identity

\[
x_0^2c_\infty=-x_2^2c_0-(2x_1^2x_2+x_1q)q
\]

gives on the overlap

\[
\binom{q_\infty}{c_{\infty,\infty}}
=
\begin{pmatrix}
D^{-2}&0\\
-D^{-3}(2z^2y+zq_0)&-D^{-3}y^2
\end{pmatrix}
\binom{q_0}{c_{0,0}}.                         \tag{2}
\]

This matrix has determinant \(-y^2D^{-5}\), which is not a unit on the whole overlap \(\operatorname{Spec}k[z,y,D,D^{-1}]\). It is invertible near the overlap with \(C\), where \(y\ne0\).

In fact **no** invertible matrix on that whole overlap transforms these two generating pairs into each other. To see this, set \(z=t,y=t^3,D=t^4\) on \(C\cap U_0\cap U_\infty\). Every such matrix must induce the same map on \(I_C/I_C^2\); its determinant restricts to

\[
-t^{-14}.
\]

But every unit of \(k[z,y,D,D^{-1}]\) is \(cD^n\), restricting to \(ct^{4n}\). The exponent \(-14\) is not divisible by four. This is a contradiction. The conclusion also holds after replacing either affine pair by any other two generators of the same reduced ideal: along each affine copy of \(\mathbf A^1\subset C\), the determinant of a basis change is a nonzero constant, and cannot change the exponent.

**Geometric meaning.** Two generating pairs can define exactly the same ideal on the overlap without being related by a globally invertible two-by-two matrix there. The determinant obstruction is the degree-\(14\) normal determinant of the reduced quartic, versus the multiples of four obtained by restricting ambient line bundles. It is the familiar reduced-curve adjunction obstruction in explicit endpoint coordinates, not a new obstruction to arbitrary higher multiple structures. A successful higher thickening can have different determinant data; its entire transition, including nonlinear terms, still has to be handled.

For clarity, the full graph coordinates also show the nonlinearity directly. Put

\[
u=D-z^4,\quad v=y-z^3,
\qquad u'=A-W^4,\quad v'=B-W^3.
\]

Then, with \(D=z^4+u\),

\[
W=\frac{z^3+v}{D},\qquad
u'=\frac{D^3-(z^3+v)^4}{D^4},\qquad
v'=\frac{zD^2-(z^3+v)^3}{D^3}.                \tag{3}
\]

These identities hold on the actual ambient overlap. Replacing \(D\) by \(z^4\) or retaining only their linear terms records a normal symbol, not an actual transition of equations. In particular the base-coordinate change itself has normal corrections.

## 4. What endpoint orders omit, and the exact stopping point

The hyperplane-at-infinity degree filtration is the ambient valuation at the generic point of that plane. It is distinct from the point valuation on \(k(C)\) or an ambient valuation centered at the closed endpoint. In the \(U_0\) coordinates it sends \(z,y,D\) to \(-1\). In graph coordinates its values on \(z,v,u\) are respectively \(-1,-3,-4\), but those three weights alone do not define it: the exact cancellations

\[
y=z^3+v,\qquad D=z^4+u
\]

raise both values to \(-1\). Thus termwise endpoint weights in a chosen normal frame can lose precisely the cancellations controlling homogeneous degree and actual extension. This concrete example complements the inherited warning that scalar valuation data omit residue relations.

There is no conflict with the existing formal-section theorem. **Full** fixed-twist formal gluing at all orders, together with uniform power containment, is already enough. The unresolved step is producing that data from generic normal forms, finitely many jets, or coefficient valuations. Equations (1) and (3), or the inherited full formal-section formulation, specify what must eventually be proved; there is no license to replace them by first-order determinant matching.

The contribution of this stream is therefore a sharply located route and failure analysis: simultaneous actual two-chart descent automatically handles the remote line; any chosen affine pair can be tested at its one omitted endpoint; and the naïve reduced-generator gluing fails even before bundle splitting. No higher-degree class has been excluded, no successful higher thickening has been constructed, and the characteristic-zero question remains open.

## Review and verification boundary

The displayed algebraic identities were checked by direct expansion. The proofs are uniform in the degrees and do not rely on a finite computation. No inherited certificate or classification was rerun. The independent audit reconstructed the deductions without a material correction; the inherited connectedness, formal-section, and multiplicity results retain their existing review status. No canonical record was changed.
