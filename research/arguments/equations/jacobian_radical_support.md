# One relative Jacobian recovers the radical

**Status.** The generalization and quartic corollary were independently
reconstructed during the algebraic-geometry review; a distinct correctness
reviewer independently reconstructed this written proof on November 23, 2026.
The precise scope and review are recorded in [R-0081](../../results/jacobian_radical_support.md). The Artinian complete-intersection Jacobian theorem
is the classical input; no new theorem about residues or differents is claimed.

## Radical recovery for any proper pair missing the projection center

Let \(k\) be any field of characteristic zero, put

\[
 S=k[x_0,x_1,x_2,x_3],\qquad B=k[x_0,x_3],
\]

and let homogeneous forms \(F_a,G_b\), of positive degrees \(a,b\), be a
regular sequence. Write \(J=(F,G)\) and \(Z=\operatorname{Proj}(S/J)\).
Assume

\[
 Z\cap M=\varnothing,\qquad M=V(x_0,x_3)\subset\mathbf P^3_k.
 \tag{J1}
\]

Define the relative Jacobian determinant

\[
 D=F_{x_1}G_{x_2}-F_{x_2}G_{x_1},\qquad \deg D=a+b-2.
\]

**Theorem.** Under these hypotheses, as ideals in the polynomial ring,

\[
 \boxed{J:D=\sqrt J.} \tag{J2}
\]

No smoothness, irreducibility or prescribed reduced support of \(Z\) is
assumed. In particular, residual curves are allowed.

**Proof.** Set \(R=S/J\). Condition (J1) says that the binary forms

\[
 f_0=F(0,x_1,x_2,0),\qquad g_0=G(0,x_1,x_2,0)
\]

have no common projective zero, so they are a regular sequence in
\(k[x_1,x_2]\). Thus \(R/(x_0,x_3)R\) has dimension \(ab\) over \(k\).
Homogeneous lifts of a basis generate \(R\) over \(B\) by graded Nakayama.
They freely generate: the source free module and the complete-intersection
ring \(R\) have the same Hilbert series, since

\[
 H_R(t)=\frac{(1-t^a)(1-t^b)}{(1-t)^4}
       =\frac{H_{k[x_1,x_2]/(f_0,g_0)}(t)}{(1-t)^2}.
\]

Consequently \(R\) is finite free of rank \(ab\) over \(B\), in particular
\(B\)-torsion-free. Let \(K=\operatorname{Frac}(B)\) and

\[
 A=R\otimes_B K=K[x_1,x_2]/(F,G).
\]

This is a finite Artinian complete intersection. After the faithfully flat
extension \(K\subset\overline K\), it is a product of local Artinian
complete intersections. On each factor, the image of \(D\) generates the
socle by the Artinian Jacobian theorem. The factor's residue field is
\(\overline K\), its length is nonzero in characteristic zero, and the
annihilator of its nonzero socle is its maximal ideal. Therefore

\[
 \operatorname{Ann}_A(D)=\operatorname{Nil}(A). \tag{J3}
\]

Here the Artinian input is, for example, Eisenbud--Ulrich,
[*Duality and socle generators for residual intersections*, Theorem A.5](https://www.math.purdue.edu/~bulrich/papers/published%20version%20of%20Duality%20for%20Residual%20Intersections.pdf).
Faithful flatness descends the equality from \(\overline K\) to \(K\).

Both sides of (J3) contract to their counterparts in \(R\). For the
annihilator, if \(rD=0\) after localization, some \(0\ne s\in B\) has
\(srD=0\) in \(R\), and torsion-freeness gives \(rD=0\). For nilpotence,
if \(r/1\) is nilpotent in \(A\), then \(sr^N=0\) for some \(N>0\) and
\(0\ne s\in B\); again \(r^N=0\). Thus

\[
 \operatorname{Ann}_R(D)=\operatorname{Nil}(R).
\]

Taking inverse images in \(S\) proves (J2). No saturation step is needed.
\(\square\)

**Trace interpretation.** For the perfect Grothendieck residue pairing on
\(A\), multiplication by \(D\) represents the trace functional:
\(\operatorname{Res}_{F,G}(Dh)=\operatorname{Tr}_{A/K}(h)\). Hence (J3)
also says that the radical of the trace pairing is the nilradical.
Indeed, on a local factor with residue field \(L/K\) and length \(e\),
the trace is \(e\operatorname{Tr}_{L/K}\) after reduction. Characteristic
zero makes \(e\ne0\) and \(L/K\) separable, so that pairing is nondegenerate
on the reduction. This is the same classical different/trace mechanism;
the local-socle proof above avoids choosing a residue normalization.

## Two Jacobian products recognize sole support on the fixed quartic

Keep the hypotheses of the theorem and assume additionally

\[
 F,G\in I_C,\qquad
 C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]

Use the two members of the standard quartic ideal

\[
 Q=x_0x_3-x_1x_2,\qquad U=x_0^2x_2-x_1^3.
\]

**Corollary.** There is an exact equivalence

\[
 \boxed{Z_{\mathrm{red}}=C
 \quad\Longleftrightarrow\quad QD\in J\ \text{and}\ UD\in J.} \tag{J4}
\]

Equivalently, there exist homogeneous cofactors with the indicated degrees
such that

\[
 \begin{aligned}
 QD&=A_bF+B_aG,\\
 UD&=A_{b+1}'F+B_{a+1}'G.
 \end{aligned} \tag{J5}
\]

The two identities have degrees \(a+b\) and \(a+b+1\), respectively.
If instead \(c=x_1^3-x_0^2x_2=-U\), the second condition is \(cD\in J\).
No value of the sole-support multiplicity is assumed in advance.

**Proof.** By (J2), the right side of (J4) is precisely
\(Q,U\in\sqrt J\). Set-theoretically, over every field,

\[
 V(Q,U)=C\cup L_{01},\qquad L_{01}=V(x_0,x_1). \tag{J6}
\]

For an explicit check, on \(x_0\ne0\) put \(r=x_1/x_0\). The two
equations give \(x_2/x_0=r^3\) and \(x_3/x_0=r^4\), exactly the affine
part of \(C\). On \(x_0=0\), \(U=0\) forces \(x_1=0\), giving
\(L_{01}\). This proves (J6); its residual line has multiplicity two
in the complete-intersection cycle, which is unnecessary for (J4).

The pure complete-intersection curve \(Z\) has no isolated reduced
components. Thus every component of \(Z_{\mathrm{red}}\) contained in
\(C\cup L_{01}\) is \(C\) or \(L_{01}\). The latter is impossible by
(J1), since

\[
 L_{01}\cap M=\{[0:0:1:0]\}.
\]

The assumed containment of \(C\) now gives \(Z_{\mathrm{red}}=C\).
Conversely, that equality gives \(\sqrt J=I_C\), so (J2) supplies both
products. Homogeneous ideal membership gives exactly the cofactor degrees
in (J5). \(\square\)

## Generality, meaning, and limits

The geometric input in (J2) is a finite flat projection of an actual CI;
the Jacobian detects its nilradical even at ramification points. This
extends the [sole-supported smooth-curve colon identity](../torus/contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity)
to arbitrary proper pairs satisfying (J1). For the quartic, the
[containing quadric and parametrization](../curve/fixed_quartic_geometry.md)
reduce radical recognition further to the two products (J4): the extra
line in (J6) is forbidden by the projection center. The residual line is
not the center \(M\) itself.

Unlike the [ideal-power/perfect-residue criterion](../torus/sole_support_first_jet_gate.md#full-exact-stci-jet-criterion-ideal-powers-and-the-perfect-residue-pairing),
(J4) needs only two full polynomial ideal memberships, without first
choosing the length \(m=ab/4\) or generators of \(I_C^m\). The older
criterion remains valid in arbitrary characteristic under its own
hypotheses. The present proof uses characteristic zero at the generic
Artinian Jacobian step: in characteristic \(p\), a local factor of length
divisible by \(p\), or inseparable reduced generic algebra, can destroy
radical recovery. No unrestricted positive-characteristic extension is
asserted.

These are exact support detectors, not a nonexistence theorem. Solving
(J5) still requires the same actual global equations, properness and
projection-center avoidance simultaneously. The identities do not
follow from their leading jets, from a prescribed cycle, or from an
abstract finite algebra. Nor does the Jacobian recover the full thick
scheme from its radical. No new carrier replacement or residual
absorption follows without further realization evidence.
