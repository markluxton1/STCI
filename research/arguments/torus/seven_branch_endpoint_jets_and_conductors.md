# Exact higher jets and conductor lattices of the seven-branch control

This calculation concerns the explicit proper pair \(F=x_1^4-x_0^3x_3\), \(G=x_2^7-x_0x_1x_3^5\) **in characteristic zero**. It computes the full completed endpoint algebras, branch jets, conductor thresholds and ordinary tangent cones, rather than inferring them from pairwise contact alone.

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

