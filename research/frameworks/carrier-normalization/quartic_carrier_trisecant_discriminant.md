# Trisecant carrier ideals and discriminant boundary

[Carrier Framework](index.md) · [Original section addresses](quartic_proof_interfaces.md)

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

**Boundaries of this discriminant method (not unresolved cases of the assembled theorem):** \(\Delta\equiv0\), where the residual conductor may be nonreduced; the two endpoint trisecants; and the bisecant lane. Neither the ordinary-node argument nor a three-distinct-contact condition extends automatically to these. The [nonendpoint](../../arguments/carriers/genus_two_nonendpoint_proof.md) and [endpoint](../../arguments/carriers/genus_two_endpoint_proof.md) arguments instead use the full ambient conic equations and exceptional attachments to close the genus-two section case; the bisection has its [independent ribbon obstruction](../../arguments/carriers/genus_two_bisection_proof.md). The [carrier-ideal and conditional discriminant derivation](../../arguments/carriers/genus_two_trisecant_carrier_proof.md) remains useful for its scheme-theoretic proof.


