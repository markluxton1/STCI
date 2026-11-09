---
id: STCI-R-0046
type: result
title: A saturated ACM full torus limit with generator degrees six six ten
scope: "#scope"
statement: "#statement"
proofs:
  - name: Hilbert-Burch family and colon cycle
    at: "research/arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit"
    using: [STCI-R-0045]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# A saturated ACM full torus limit with generator degrees six six ten

## Scope

Let \(k\) be algebraically closed of any characteristic,
\(S=k[x_0,x_1,x_2,x_3]\), and \(C=[s^4:s^3t:st^3:t^4]\).
Use the integer weights \((0,1,3,4)\) and maximal-weight convention
\(f\mapsto h^{\max w(f)}f(x_0,h^{-1}x_1,h^{-3}x_2,h^{-4}x_3)\).
Define

\[
q=x_0x_3-x_1x_2,\quad A=x_0^2x_2-x_1^3,\quad
B_3=x_0x_2^2-x_1^2x_3,\quad
a_6=x_0^2x_3A,\quad b_4=x_0^3x_2,
\]

\[
F=q^3+a_6,\qquad G=q^3+x_0^2x_1B_3.
\]

Write \(L_{ij}\) for coordinate lines. The statement concerns this
specified actual pair and its full ideal, not a family of supported ideals.

## Statement

The identity \(G-F=-b_4q\) gives the proper sextic complete intersection
\(I=(F,G)=(q^3+a_6,b_4q)\). Its full torus family is exactly

\[
\mathcal I=(q^3+h^5a_6,b_4q,a_6b_4)\subset S[h].
\]

The quotient is flat over \(k[h]\), the ideal is \(h\)-saturated, and
every graded fiber is irrelevant-saturated and ACM. Its full homogeneous
initial ideal and saturated projective special fiber agree and are

\[
I_0=(q^3,b_4q,a_6b_4).
\]

This ideal has minimal generator degrees \(6,6,10\), minimal syzygy
degrees \(10,12\), and minimal resolution

\[
0\longrightarrow S(-10)\oplus S(-12)
\longrightarrow S(-6)^2\oplus S(-10)
\longrightarrow S\longrightarrow S/I_0\longrightarrow0.
\]

It is not a complete intersection. Its Hilbert series nevertheless is
\((1-z^6)^2/(1-z)^4\), with polynomial \(36n-144\).

Let \(T=V(x_2,x_0x_3^2-x_1^3)\), an irreducible plane cubic.
The original and special fundamental cycles are respectively

\[
[C]+13[L_{23}]+13[L_{13}]+2[L_{01}]+[L_{02}]+[T],
\]

\[
[C]+13[L_{23}]+14[L_{13}]+4[L_{01}]+[L_{02}].
\]

Thus both schemes have multiplicity one along \(C\) and residual degree
32, and neither has an embedded associated component. Both restrict
on the dense coordinate torus to the same reduced curve \((q,A)\);
their finite transverse quotient is \(k\).

The endpoint schemes are retained by exact chart ideals. On \(x_0=1\),
put \(t=x_1,y=x_2,z=x_3,Q_0=z-ty\); the original and special ideals are

\[
(Q_0^3+z(y-t^3),yQ_0),\qquad
(Q_0^3,yQ_0,zy(y-t^3)).
\]

On \(x_3=1\), put \(\alpha=x_0,\beta=x_1,\gamma=x_2\),
\(Q_\infty=\alpha-\beta\gamma\), \(E=\alpha^2\gamma-\beta^3\);
the corresponding ideals are

\[
(Q_\infty^3+\alpha^2E,\alpha^3\gamma Q_\infty),\qquad
(Q_\infty^3,\alpha^3\gamma Q_\infty,\alpha^5\gamma E).
\]

## Proof

The [complete determinantal proof](../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit)
exhibits the three generators as maximal minors, proves height two in
every fiber, then proves parameter regularity, flatness and saturation.
Its continuation,
[cycles and endpoint schemes](../arguments/torus_sextic_residuals.md#cycles-and-endpoint-schemes-of-the-three-generator-limit),
derives the original cycle by Cartier-divisor additivity, derives the
special cycle by R-0045, independently checks the cubic's divisor limit,
and gives the literal endpoint substitutions. That subsection is part
of the addressed determinantal section and completes the construction's proof.

## Evidence

Reconstructed from §§4–4.1 of
[sextic residuals](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md).
The finite verifier's matrix-minor, substitution and numerator checks
are auxiliary identity checks; the written Hilbert–Burch and regularity
arguments establish the geometric assertions.

## Limitations

This example has residual support of degree 32. It is not a point of a
sole-supported Hilbert incidence, and does not exclude arbitrary sextic
pairs. Initial forms of the two chosen equations alone do not generate
the full limit. No identification with the normal-cone initial ideal
along \(C\) is made. A preserved cycle, polynomial, or quotient cannot
replace the actual saturated ideal or endpoint charts.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed the height-two Hilbert–Burch proof,
parameter regularity, flatness, parameter and irrelevant saturation,
minimal resolution, both cycle calculations, and endpoint chart ideals.
A separate sparse-polynomial implementation over the integers checked the
generator change, all three matrix minors, cancellation relation, Segre
restrictions of a6 and b4, and original-cycle restriction factorizations.
Those identity checks support the geometric reduction with necessary
exact algebra; they do not replace its flatness or saturation argument.
The residual-degree-32 example remains outside sole support.

Independent reconstruction review accepts this route within its stated scope.
