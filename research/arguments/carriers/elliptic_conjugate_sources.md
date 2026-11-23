# Conjugate sources and homogeneous cancellation for the elliptic octics

**Scope and review.** Work over an algebraically closed field of
characteristic zero on the smooth, basepoint-free, birational locus of
the fixed [elliptic octic family](elliptic_double_inverse_construction.md).
The November 23, 2026 reassessment and a distinct independent reviewer
reconstructed the conjugate-source comparison and the saturated
equation-source extension below. They do not exclude this family.
Retain the [contact notation and four conditional rows](elliptic_contact_and_spectral_comparison.md):
\(G=Z\cap E\), \(g=\operatorname{length}G\), \(d=6-g\), and
the vertical first-symbol divisor \(V\) of degree \(12+g\).
Write \(\mathscr S=k[x_0,x_1,x_2,x_3]\),
\(\tau=\operatorname{diag}(1,-1,-1,1)\), and let \(F\) be the
implicit octic.

## 1. The octic and its sign transform have generic contact four

The quadratic residue extension of the generic transverse node of
\(F\) is the function field of its inverse elliptic curve over
\(k(C_0)=k(t)\). The [branch calculation](elliptic_contact_and_spectral_comparison.md#4-the-fixed-marking-prevents-target-sign-symmetry)
identifies it as
\[
 k(t)(\sqrt{D(t)}),\qquad
 D(t)=t^4-6it^2-8(1-i)t+7.
\]
The corresponding extension for \(\tau F\) is
\(k(t)(\sqrt{D(-t)})\). Both polynomials are squarefree, neither
branches at infinity, and their branch divisors are disjoint: a common
root would satisfy
\(D(-t)-D(t)=16(1-i)t=0\), whereas \(D(0)=7\).
In particular the two quadratic extensions are distinct.

Each primitive quadratic normal form is irreducible over \(k(t)\),
since its horizontal root has normalization the connected double
cover \(E\). If the two quadratics shared a projective root, their
irreducibility would make them proportional and identify their residue
extensions. They are therefore coprime. Thus the actual pair
\[
                         H=(F,\tau F)                       \tag{ES1}
\]
has full generic ordinary initial CI of type \((2,2)\) along \(C_0\).
The two distinct integral octics have no common surface factor, so this
is a proper homogeneous \((8,8)\) CI. Its generic multiplicity on
\(C_0\) is four, and its residual cycle has degree
\[
                         64-4\cdot4=48.                    \tag{ES2}
\]
No classification of this residual or of its attachments is asserted.

## 2. The conjugate-pair quotient retains a length-four primary mark

Suppose \(J=(F,G_b)\) is an actual sole-supported pair. Its mate has
\(b\ge6\) and pulls back to a scalar multiple of \(e^b\), where
\(e=Q_0\) cuts \(E\). At the generic point of \(C_0\), the
[node calculation](elliptic_contact_and_spectral_comparison.md#3-four-necessary-rows-when-the-actual-first-kernel-is-saturated)
gives
\[
 G_b\in(F)+\mathfrak m^b
\]
after completion and a separable residue extension. The initial CI
in (ES1) has Hilbert function \((1,2,1)\), so
\(\mathfrak m^3\subset H\) there. Faithful flatness of completion
and of the residue extension descends the resulting ideal membership.
Consequently, for
\[
 K=J+\tau J,\qquad U=J\cap\tau J,
\]
one has \(K_{I_C}=H_{I_C}\), of length four. This is generic local
membership; it does not claim \(G_b\in H\) globally.

Define the canonical primary component
\[
                  Q_C=H_{I_C}\cap\mathscr S.                \tag{ES3}
\]
Then
\[
                  K\subset K^{\rm sat}\subset Q_C,
\]
and \(Q_C\) is the pure hull of \(K^{\rm sat}\). Indeed
\(\sqrt K=I_C\), the two ideals have the same generic localization,
and removing the projective embedded points leaves that unique
\(C\)-primary component. Equality \(K^{\rm sat}=Q_C\) is not
automatic; their difference can retain finite projective attachments.
In particular \(K^{\rm sat}\ne I_C\), since its generic length is
four. The reduced-quadric explanation for cheap saturation torsion
does not apply literally here.

The actual union sequence
\[
0\longrightarrow\mathscr S/U
\longrightarrow\mathscr S/J\oplus\mathscr S/\tau J
\longrightarrow\mathscr S/K\longrightarrow0
\]
gives the union's generic multiplicity
\[
                    (2b)+(2b)-4=4b-4.                      \tag{ES4}
\]
The [symmetrized-source theorem](../torus/sign_symmetry_and_actual_sources.md#2-symmetrizing-an-actual-acm-source)
therefore applies with this actual intersection quotient and the
nonzero moment of \((4b-4)[C_0]\). Its saturation torsion must be
nonzero, but this remains a detector rather than an exclusion.
For example \(I_C^3\subset Q_C\), by generic membership in (ES1)
and contraction. Thus \(q^3\in Q_C\) for the containing quadric
\(q\). If \(K^{\rm sat}=Q_C\) and \(b>6\), this degree-six
element already supplies a missing low-degree equation of \(K\).
The marked inclusions, finite attachments and multiplication must be
retained beyond that observation.

## 3. Saturated first symbols force a nontrivial source extension

Now impose the additional hypothesis that the actual degree-two
relation kernel itself is a line subbundle. The [contact comparison](elliptic_contact_and_spectral_comparison.md#3-four-necessary-rows-when-the-actual-first-kernel-is-saturated)
identifies it as \(R=\mathcal O_{C_0}(-20+g)\). The actual two
equation sources induce a surjection
\[
\begin{split}
0\longrightarrow\mathcal O(-12-4b-g)
\longrightarrow\mathcal O(-32)\oplus\mathcal O(-4b)
\xrightarrow{(\alpha,\beta)}\mathcal O(-20+g)
\longrightarrow0,\\
\alpha\in H^0(\mathcal O(12+g)),\qquad
\beta\in H^0(\mathcal O(4b-20+g)).                         \tag{ES5}
\end{split}
\]
All line bundles here are on the parametrizing \(C_0\simeq\mathbf P^1\).
The coefficient pair has no common zero precisely because it generates
the actual relation line everywhere. The determinant gives the displayed
kernel. For \(b\ge6\), both summands of
\(\operatorname{Hom}(R,\mathcal O(-32)\oplus\mathcal O(-4b))\)
have negative degree, so this surjection has no global splitting.

For the octic coefficient, \(\operatorname{div}(\alpha)=V\).
On \(\alpha\ne0\), the first generic cancellation uses
\[
                         G_b-(\beta/\alpha)F.
\]
The ratio is a rational section of \(\mathcal O(4(b-8))\) with
pole divisor **exactly** \(V\), since \(\alpha,\beta\) have no
common zero. A homogeneous multiplier of degree \(b-8\) restricts
to a regular section of this line bundle and cannot equal that ratio.
If \(b<8\), no nonzero multiplier of that degree exists at all.
Thus local cancellation does not provide the permitted global
homogeneous row operation. Higher cancellations must also retain
their actual source denominators.

The four rows remain compatible with these bundle degrees; (ES5)
does not contradict their existence as abstract extensions. It explains
the source issue rather than supplying a new exclusion.

Two different defects must also be distinguished. Under this saturation
hypothesis, R-0010 supplies ordinary normal flatness and generic initial
CI type \((2,b)\). Hence [R-0063](../../results/normal_flat_comparison_specialization.md)
gives zero for the [R-0030 equation-comparison defect](../../results/local_filtration_comparison_defect.md),
denoted \(\Delta_{\rm cmp}\) here. In contrast, the corrected total
normal-layer degree defect of [R-0032](../../results/full_conormal_socle_budget.md)
has \(n=2b\), Loewy index \(b\), Hilbert first moment \(b^2\),
and \(L=4b+18\). Its identity gives
\[
             \Delta_{\rm layers}=3b(b-6)>0                 \tag{ES6}
\]
in all four conditional rows. Vanishing of the equation-comparison
defect does not erase these positive normal-layer degree defects.

## 4. Upstairs section bounds do not settle the source problem

On the smooth quadric normalization, \(E\sim H\) and \(e=Q_0\)
is an actual global section of \(H\). Thus \(e^b\) already belongs
to \(H^0(S,bH)\) and has divisor \(bE\) for every \(b>0\).
Any valuation bound using only the normalization and its polarization,
and valid for all such global sections, must permit this order.

The actual mate condition is stronger:
\(e^b\) must belong to the degree-\(b\) subalgebra generated by
the four projection sections. Equivalently it must pass the full
surface-conductor descent test. This is separate from the rank-twelve
inverse-support test and from root-conductor Picard gluing. The
conjugate pair (ES1) and the extension (ES5) provide actual sources
for studying those distinctions; neither generic cancellation nor
an upstairs pole budget proves that a mate exists or is impossible.
