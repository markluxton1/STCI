# Sign-odd cubic factors in the two-node sextic lane

**Scope and review.** Characteristic zero, in the original fixed ambient
coordinates of the [forced-norm two-node continuation](conditional_2_12_singular_and_conductor.md#2-an-exact-cubic-defect-makes-the-forced-norm-equations-small).
The November 23, 2026 synthesis and an independent correctness reviewer
reconstructed this structural exclusion. It uses the actual cubic-source
formula, not a new torsion or obstruction-locus computation.

Retain factors
\[
 l_i=(A_i+C_i z)u+(B_i+D_i z)v.
\]
Consider the locus
\[
 A_i=D_i=0,\qquad B_iC_i\ne0,\qquad
 B_1C_2-B_2C_1\ne0.                                    \tag{ON1}
\]
Each factor has nonzero determinant \(-B_iC_i\), and the two
distinct graph components meet transversely at the two endpoint nodes.
Here \(\kappa_i=0\), and the forced multiplier is
\[
 \alpha_i=B_i^2+\tfrac12B_iC_i z^2+\tfrac14C_i^2z^4.
\]
For ambient coordinates \((x_0,x_1,x_2,x_3)\), put
\[
 q=x_0x_3-x_1x_2,\qquad
 \mathcal A=x_0^2x_2-x_1^3,\qquad
 \mathcal D=x_2^3-x_1x_3^2.
\]
The injective actual cubic symbol map identifies the unique cubic with
symbol \(\alpha_i l_i\) as
\[
 H_i=B_i^3\mathcal A+B_i^2C_i x_1q
       +\tfrac12B_iC_i^2x_2q-\tfrac18C_i^3\mathcal D.    \tag{ON2}
\]
This follows by substituting \(A_i=D_i=0\) into the actual cubic
coefficient formula in the linked continuation. Every displayed
ambient cubic is odd for
\(\tau=\operatorname{diag}(1,-1,-1,1)\), whereas \(q\) is even.
Consequently every allowed sextic in this locus is sign-even:
\[
             F_6=H_1H_2+\eta q^3,\qquad \tau F_6=F_6.    \tag{ON3}
\]
The [one-sign-eigen-generator theorem](../torus/sign_symmetry_and_actual_sources.md#1-one-sign-eigen-equation-is-sufficient)
therefore excludes a sole-support mate of **any** degree for every
such sextic. A hypothetical proper mate supported on \(C_0\)
would have nonzero first moment in characteristic zero, contrary to
that theorem. Reducible or nonreduced sextics are covered as well.

This closes the both-odd sublocus (ON1) of the zero-defect continuation.
It is distinct from the earlier [diagonal slice](conditional_2_12_singular_and_conductor.md#3-a-proper-diagonal-slice-is-exactly-excluded-already-at-first-order)
\(l_i=t_i u+zv\), whose factors correspond to the other parity.
It does not close the general zero-defect locus or the nonzero-defect
conic. Those strata retain their complete ambient, root-gluing and
actual-source conditions.
