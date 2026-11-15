# Generic transverse algebras and endpoint contact

[Framework orientation](index.md) · [Original section addresses](weights_and_limits.md)

## IV. Generic algebra and endpoint extension

### Generic transverse algebra

On \(\Omega\), complete the original intersection at the generic point
of \(C\) using the chart coefficient field \(K=k(C)=k(r)\).
The actual local ideal gives the Artinian complete intersection
\[
 A_\eta=K[[U,V]]/(F|_{x_0=1},G|_{x_0=1}),\qquad
 m_C=\dim_K A_\eta.
\]
Properness ensures that this local ideal is primary to \((U,V)\).
The plane intersection multiplicity inequality gives
\(m_C\ge r_Fr_G\), with equality exactly when the first binary
symbols are coprime over \(\overline K\). The colength of the **full**
normal initial ideal computes \(m_C\) even with a common direction.
For example \((U,U+V^n)\) with \(n\ge2\) has length \(n\) and both
displayed symbols equal to \(U\). The first-order symbols therefore
measure only the first contact. [Generic length and common normal
directions](../residual-construction/two_surfaces.md#21-generic-length-and-common-normal-directions).

### Endpoint lattices and contact

For the constant case, let \(B\) be a finite positive-length quotient
of \(k[u^{\pm1},v^{\pm1}]\) with its named units, and let
\(n=\dim_k B\). Close the embedded product
\(\mathbf G_{m,r}\times\operatorname{Spec}B\) in \(\mathbf P^3\).
Its saturated ideal is the kernel of the degree-four parametrization
into \(B[s,t]\). In degree \(d\) the weight-\(w\) kernel tests
\(\sum_e c_e u^{e_2}v^{e_3}=0\) in \(B\) on the monomials of
that weight. The finite map \(\nu:\mathbf P^1_B\to Z_B\) to
that image is an isomorphism on \(\Omega\) and the two endpoint
completions are the image algebras
\[
 A_0=k[[r]][r^3u,r^4v]\subset B[[r]],\qquad
 A_\infty=k[[z]][z^3\alpha,z^4\beta]\subset B[[z]].
\]
They are finite free lattices of rank \(n\) over their indicated
parameter rings. At zero the filtration on the coefficient space \(B\)
in order \(j\) is the span of \(u^i v^l\) with \(i,l\ge0\) and
\(3i+4l\le j\), since each such monomial enters the image multiplied by
\(r^{3i+4l}\). At infinity the same recipe uses \(\alpha,\beta\) and
\(z\). Both filtrations eventually reach \(B\), since inverses of units
in a finite algebra are polynomials in those units. In an adapted
basis, each coefficient basis element entering at order \(j\) gives
a lattice generator multiplied by the \(j\)-th parameter power.
The index is the sum of these orders. [Finite image and purity](../../arguments/torus_embedded_quotients.md#finite-image-and-purity) ·
[Endpoint defects](../../arguments/torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial).

In a reduced orbit arrangement, pairwise contact at zero is the order
of the first differing graph coefficient, at order three for different
\(u\) values and at order four for equal \(u\) and distinct \(v\).
At infinity compare \(\alpha,\beta\) in the same way. For the
\(x_1\)-scaling root-of-unity arrangement this gives length four at
zero precisely when distinct labels have the same cube, length three
otherwise, and length three at infinity. These lengths describe the
embedded jets of **pairs** of branches. For a union of several
branches the full lattice records how each new branch meets the
preceding union. In the full \(\mu_8\) arrangement the pairwise contacts
over both endpoints sum to \(168\). Its total normalization defect is
\(136\).
[Pairwise contact and jet stabilizers](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#4-pairwise-endpoint-contact) ·
[Genus of the full arrangement](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#6-arithmetic-genus-and-normalization-defects).

### Conductor, torsion and descent

At an endpoint write \(A\subset \widetilde A\) for the image lattice
and its upstairs algebra. The finite torsion module
\(\widetilde A/A\) has length \(\delta\) over the parameter DVR.
The conductor \(\mathfrak c=\{b\in\widetilde A:b\widetilde A\subset A\}\)
is an ideal in both rings. The condition for a local function upstairs
to descend is that its class in \(\widetilde A/\mathfrak c\) belongs
to \(A/\mathfrak c\), or equivalently
\(A=\widetilde A\times_{\widetilde A/\mathfrak c}A/\mathfrak c\).
This uses the full finite algebras, including nilpotents. When \(A\)
is Gorenstein, as it is for a sole-supported complete intersection,
DVR lattice duality gives \(\ell(A/\mathfrak c)=\delta\) and
\(\ell(\widetilde A/\mathfrak c)=2\delta\), allowing a non-Gorenstein
upstairs algebra. For a reduced constant quotient \(B\), the finite
map \(\nu\) is the normalization.
[Full conductor boundary](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#actual-endpoint-lattices-and-the-full-conductor-boundary) ·
[Fourth-root image and conductor](../../arguments/torus_embedded_quotients.md#the-fourth-root-image-and-its-conductor).

The torsion of \(\widetilde A/A\) depends on the **embedded** quotient
and its multiplication. For \(B=k\) at \((u,v)=(1,1)\) both indices
are zero even though the ambient normal-frame cokernel has length seven
at each endpoint. The same abstract \(B\) can give different indices
in different embeddings. Torsion in the ordinary graded normal layers
of an intersection is a third object, measured by saturation of those
layers. [Distinct embeddings of the same finite algebra](../../arguments/torus_embedded_quotients.md#embedded-quotients-and-characteristic-dependent-endpoints) ·
[Normal saturation defects](../formal-normal-geometry/normal_filtration_boundaries.md).

For a proper sole-support pair, the closure \(W\) of the entire torus
restriction is finite over \(\mathbf P^1_r\) and has pushforward algebra
\(\mathcal B\), locally free of rank \(m_C\). Its finite map to the CI is
an isomorphism off the endpoints. The completed image lattices are
\(k[[r]][r^3U,r^4V]\) at zero and
\(k[[z]][z^3(\alpha-1),z^4(\beta-1)]\) at infinity, where
\(z=(u/v)r^{-1}\) is the projective parameter. Their cokernels have
lengths \(\delta_0,\delta_\infty\).
[Entire finite modification](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification) ·
[Completed lattices and conductor](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#actual-endpoint-lattices-and-the-full-conductor-boundary).

In characteristic zero, \(\deg\mathcal B>0\) by the invariant-CI
exclusion and global generation of \(\mathcal B\). The embedding can vary
even when the abstract transverse algebra stays isomorphic. The endpoint
fibers determine the pure quotients of the opposite intrinsic limits and
the embedded lengths. For a hypothetical characteristic-zero \((6,6)\)
pair, each embedded endpoint fiber \(B\) satisfies
\(D_0(B)+D_\infty(B)\ge153\), where both defects are computed for that
same fiber in the two quotient frames. It must also pass the degree-six
source test. The full endpoint algebras and moving equation
incidence remain open.
[Strict movement](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier) ·
[Endpoint comparison](../../results/intrinsic_limits_endpoint_fibers.md#statement) ·
[Sextic endpoint conditions](../../arguments/torus_hilbert_boundary.md#necessary-endpoint-conditions-for-a-sextic-pair) ·
[Remaining full-ideal comparison](../../investigations/quotient-hilbert-comparison/index.md#question).

### The characteristic-seven control in both endpoint frames

For \(F=x_1^4-x_0^3x_3,\ G=x_2^7-x_0x_1x_3^5\), the quotient on
\(\Omega/T_C\) is \((v-1,u^7-1)\). The original equations form a
proper CI in either characteristic and have no coordinate-boundary
curve, as follows directly on \(x_0=0\) and \(x_3=0\).
At zero the quotient basis \(1,u,\ldots,u^6\) enters with weights
\(0,3,\ldots,18\), giving \(D_0=63\).
At infinity \(\alpha=u^{-3},\beta=u^{-4}\). The smallest values in
the semigroup generated by \(3,4\) in the seven residue classes modulo
seven are \(0,8,9,3,4,12,6\), giving \(D_\infty=42\).
The corresponding monomials in \(u\) form a basis of
\(k[u]/(u^7-1)\) in every characteristic. The total \(105\) gives
\(28n+7-105=28n-98\),
the degree-\((4,7)\) CI polynomial.

In characteristic seven this algebra is \(k[U]/(U^7)\), the family is
constant, and \(h=0\). The two displayed equations have common linear
normal symbol \(V\), while their full local ideal contains \(U^7\).
Thus the normal orders have product one and the normal length is seven.
In characteristic zero the first symbols are independent, and the
marked length at each of the seven roots is one. The projective
intersection has seven distinct quartic components. The Frobenius
collision changes the embedded algebras and support while preserving
the same endpoint-index sum and projective CI polynomial. In
characteristic seven, \(h=0\) is compatible with the trace theorem
because seven divides the degree product. The trace proof concerns
the generic multiplicity of the full
nonreduced algebra and allows the reduced fourfold projection to be
separable. The actual two global equations hold in both fields.
[Entire finite modification and characteristic scope](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier) ·
[All reduced binomial components](../../arguments/arithmetic/positive_characteristic_constructions.md#12d-necessity-of-the-frobenius-exponent-and-all-reduced-components).

#### Higher jets of the seven branches in characteristic zero

Write \(Z=V(F,G)\) for this pair over the algebraically closed field
of characteristic zero. Its branches come from the curves
\[
C_\zeta=[s^4:s^3t:\zeta st^3:t^4],\qquad \zeta\in\mu_7.
\]
At \(p_0\) put \((r,y,w)=(x_1,x_2,x_3)/x_0\). At \(p_\infty\) put
\((z,b,a)=(x_2,x_1,x_0)/x_3\). The exact graph equations are
\[
\begin{array}{c|cc}
 & \text{order three} & \text{order four}\\ \hline
p_0 & y=\zeta r^3 & w=r^4\\
p_\infty & b=\zeta^{-3}z^3 & a=\zeta^{-4}z^4.
\end{array}
\]
The embedded jets of the individual branches agree through order two,
and every pair separates at order three at both points. In fact
\(\zeta\mapsto\zeta^{-3}\) permutes \(\mu_7\), so the difference of
the cubic graph functions generates the pairwise intersection ideal
\((r^3)\) or \((z^3)\) in the parameter ring. At order four the
coefficient at \(p_0\) is common to all branches. At \(p_\infty\) the
quartic coefficient is the inverse of the cubic coefficient and
supplies a third independent character, alongside \(1\) and the cubic
coefficient. [Embedded jet convention](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#5-intrinsic-interpretation-by-jet-stabilizers).

The completed rings of the whole intersection are
\[
A_0=k[[r,y]]/(y^7-r^{21}),\qquad
A_\infty=k[[z,a,b]]/(ab-z^7,\ a^3-b^4).
\]
At zero this follows by eliminating \(w=r^4\). At infinity the two
equations give the reductions
\[
ab\longmapsto z^7,\qquad a^3\longmapsto b^4,\qquad
b^5\longmapsto a^2z^7 .
\]
The third reduction follows from \(b^5=a^3b=a^2z^7\). Each step
decreases \(3\deg_a+2\deg_b\) on a monomial and increases its ordinary
total degree. Thus they give convergent reductions of formal series
to the span of \(1,b,a,b^2,a^2,b^3,b^4\) over \(k[[z]]\).
The seven images in the product of the branch rings have distinct
characters of \(\mu_7\), so the reduced monomials form a free basis.
At zero the corresponding basis over \(k[[r]]\) is \(1,y,\ldots,y^6\).

Identify the coefficient algebra of the normalization with
\(B=k[u]/(u^7-1)=k^{\mu_7}\), where \(u(\zeta)=\zeta\). The least
order \(d_{e,i}\) at which \(u^i\) occurs in the image at endpoint
\(p_e\) follows from these two bases.

| Endpoint | \(1\) | \(u\) | \(u^2\) | \(u^3\) | \(u^4\) | \(u^5\) | \(u^6\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(p_0\) | 0 | 3 | 6 | 9 | 12 | 15 | 18 |
| \(p_\infty\) | 0 | 6 | 12 | 4 | 3 | 9 | 8 |

At each order \(d\) the allowed coefficients are precisely the span
of the characters with \(d_{e,i}\le d\). This describes the image in
the product of the normalized branch jets at every order. The
coefficient of the parameter to power \(d\) can be prescribed
independently on every branch for \(d\ge18\) at \(p_0\) and \(d\ge12\)
at \(p_\infty\). The conductors are \(r^{18}B[[r]]\) and
\(z^{12}B[[z]]\). Indeed, multiplication by a branch idempotent isolates its
coefficient, and the character expansion
\(\frac17\sum_{i=0}^6\zeta^{-i}u^i\) of that idempotent uses all
seven characters. A proper span in the table cannot contain it.
The sums of the entry orders recover the two normalization defects
\(63\) and \(42\).

For the ordinary jets of the intersection, use \(A_e/\mathfrak m_e^{n+1}\).
With bars denoting degree-one classes, the two tangent
cones are
\[
\operatorname{gr}_{\mathfrak m_0} A_0=k[\bar r,\bar y]/(\bar y^7),
\qquad
\operatorname{gr}_{\mathfrak m_\infty} A_\infty
  =k[\bar z,\bar a,\bar b]/(\bar a\bar b,\bar a^3,\bar b^5).
\]
The degree-increasing reductions at infinity preserve the lower
bound on the total degree of any monomial in \(\mathfrak m_\infty^n\).
The reduced monomials are independent and each lies in the maximal
ideal power given by its total degree, which proves the second
tangent-cone presentation. The successive graded dimensions at
zero are \(1,2,3,4,5,6,7,\ldots\), and at infinity they are
\(1,3,5,6,7,\ldots\). Both sequences stay at \(7\) once they reach it.

