# Independent addendum audit: moving ideals, actual sections and the ribbon control

Date: 2026-10-27. Reviewer: discrepancy-scope subagent, independent of the
source author and the original flag-tangent reviewer. Scope: §§4–5 of
[Moving a thickening together with actual equations](2026-10-27-absorption-formal-lifting-interface.md),
with its tangent conventions reconstructed from §§2–3.

**Outcome: PASS for the mathematical statements with the explicit
\(\operatorname{Ext}^1_C\) interpretation in the ribbon paragraph.
A category/subscript clarification was requested before integration.**
These remain provisional deductions, not canonical promotion.

## 1. Tangent targets and global compatibility

For \(I^N\subset J\subset I\), the graph convention
\(j+\epsilon h\), \(h\bmod J=\xi(j)\), gives precisely

\[
\xi\in H^0\mathcal Hom_X(J/I^N,I/J).
\]

The target keeps the marked \(C\) fixed, and quotienting the source by
\(I^N\) fixes the ambient infinitesimal neighborhood. Requiring a moving
equation \(F+\epsilon\dot F\) to lie in the graph ideal gives
\(\dot F\bmod J=\xi(F)\). Its global correction necessarily belongs to
\(H^0(I(a))\), since the right side lies in \(I/J\).
The connecting map for
\(0\to J(a)\to I(a)\to(I/J)(a)\to0\)
therefore gives exactly the stated obstruction in \(H^1(J(a))\).
The independent second equation has the same calculation. Kernel and
torsor assertions follow from exactness, with no replacement by
function-field coefficients.

## 2. Small-extension statement

Let \(B'\twoheadrightarrow B\) be a small extension with kernel \(A\),
and let a flat marked \(T_{B'}\) already have been chosen. The ideal
\(J_{B'}\) is flat over \(B'\): in
\[
0\to J_{B'}\to\mathcal O_X\otimes B'\to\mathcal O_{T_{B'}}\to0
\]
the middle and right terms are flat, and the kernel is flat by the
Tor exact sequence. Base change identifies \(J_{B'}\otimes B=J_B\),
using flatness of \(\mathcal O_{T_{B'}}\) again. Since the maximal ideal
of \(B'\) kills \(A\), tensoring the ideal with \(A\) gives the
special-fiber ideal tensored over \(k\). Hence
\[
0\to J(a)\otimes_k A\to J_{B'}(a)\to J_B(a)\to0
\]
is exact. Its cohomology gives an obstruction
\(H^1(J(a))\otimes_k A\), vanishing exactly when the chosen section
lifts; lifts form a torsor under \(H^0(J(a))\otimes_k A\).

This validates §4 without assuming that the quotient itself lifts,
or that its Hilbert scheme is unobstructed. Likewise, lifting a
prescribed class in \(J/IJ\) uses the different sequence with kernel
\(IJ(a)\); the source correctly distinguishes those problems. The
large-twist comment is conditional on boundedness and the stated
cohomology/base-change neighborhood, and makes no generation or STCI
conclusion.

The flat-tensor mechanism and Hom/Ext distinction agree with the
freshly inspected primary [Stacks 0CZU](https://stacks.math.columbia.edu/tag/0CZU)
and [0CZV](https://stacks.math.columbia.edu/tag/0CZV).

## 3. Ribbon calculation and required category clarification

For the fixed characteristic-zero quartic, accepted R-0020 gives
\[
0\to K=\mathcal O_C(-8)\to E=\mathcal O_C(-7)^2
\to L=\mathcal O_C(-6)\to0,
\]
where these degrees are on \(C\simeq\mathbf P^1\).
With \(T=2C\subset Q\), \(J=(q)+I^2\), the marked ribbon Quot
problem is a quotient of the sheaf \(E\), which is killed by \(I\).
It is consequently a Quot problem **on \(C\)**. Its tangent
\(\operatorname{Hom}_C(K,L)=H^0(\mathcal O(2))\) has dimension three.
Surjections \(E\to L\) are basepoint-free pairs of binary linear
forms modulo scalar, an open subset of \(\mathbf P^3\).
This explicitly integrates all these tangent directions; local inverse
images of their kernel have ideal \((x,y^2)\).

Here \(\operatorname{Ext}^1_C(K,L)=H^1(\mathcal O(2))=0\).
The source must not confuse this with the ambient group in the
general Quot discussion:
\[
\operatorname{Ext}^1_X(i_*K,i_*L)
\simeq H^0\bigl(K^\vee\otimes L\otimes N_{C/X}\bigr)
=H^0(\mathcal O(9))^2,
\]
which has dimension twenty. The local-to-global Ext spectral sequence
gives this equality because \(H^1(\mathcal O(2))=H^2(\mathcal O(2))=0\).
Adding the subscript \(C\) to the ribbon Ext group resolves the
ambiguity without changing any construction or obstruction conclusion.

The symbol \(q\) trivializes \(K(2)\). Uniqueness of the containing
quadric makes \(H^0(I(2))=H^0(J(2))=kq\), with zero image in
\(H^0(L(2))=H^0(\mathcal O(2))\).
The nine independent quadratic restriction weights cover
\(H^0(\mathcal O_C(2))=H^0(\mathcal O(8))\), so \(H^1(I(2))=0\).
Thus the connecting map to \(H^1(J(2))\) is an isomorphism and
evaluation \(\xi\mapsto\xi(q)\) identifies the tangent with its
three-dimensional obstruction space.

For \(F=q,\ G=(x_0^2x_2-x_1^3)^2\), the pair is proper and on \(Q\)
has divisor \(2C+4\ell\). Its full marked primary component is \(2C\).
Because \(G\in I^2\), every permitted \(\xi\) kills \(G\).
Hence all nonzero ribbon motions fail to move with an actual
degree-two first carrier, while the second obstruction is zero.
This is an exact control of the proposed general lifting statement,
not a reopened low-degree STCI search.

## 4. Scope

The audit used direct algebra and exact sequences; no inherited
verifier was replayed. No higher-order integrability of arbitrary
flag tangents, algebraization of a formal parameter arc, or endpoint
existence is asserted. The sole correction requested is explicit
separation of \(\operatorname{Ext}_C\) and
\(\operatorname{Ext}_X\) in the ribbon paragraph.
