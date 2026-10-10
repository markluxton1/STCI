# Independent audit: the specified two-arm star equations

Date: 2026-10-10. Status: **PROVED conditional on the graph and contact hypotheses stated here**. This is only an audit of the graph arithmetic; it does not establish that a geometric application has this graph or contact pattern.

Let \(E^2=-3\), and let at most two arms consist of chains

\[
F_1-\cdots-F_n,\qquad F_i^2=-2,
\]

with \(F_1\) meeting \(E\) once. Distinct arms are disjoint and all adjacent graph intersections have multiplicity one. Write

\[
Z=E+\sum_{\text{arms}}\sum_{i=1}^n z_i F_i.
\]

Assume \(Z\cdot F=-C\cdot F\) for every graph prime \(F\). The central coefficient of \(Z\) is therefore fixed at one. The permitted contacts are: \(C\) meets \(E\) once transversely, or \(C\) meets exactly one arm prime \(F_j\) once transversely; it has no other graph contacts.

## Arm equations and signs

For an arm, put \(z_0=1\) and \(z_{n+1}=0\), and let \(c_i=C\cdot F_i\). The equation on \(F_i\) is

\[
z_{i-1}-2z_i+z_{i+1}=-c_i.
\]

Equivalently, with the positive \(A_n\) Cartan matrix \(A\),

\[
A(z_1,\ldots,z_n)^\mathsf T=e_1+(c_1,\ldots,c_n)^\mathsf T.
\]

The positive sign of the contact term is essential: contact increases the arm coefficients. The inverse is

\[
(A^{-1})_{ij}
=\frac{\min(i,j)(n+1-\max(i,j))}{n+1}.
\]

Without contact on the arm,

\[
z_i=\frac{n+1-i}{n+1},\qquad z_1=\frac n{n+1}<1.
\]

If \(C\) meets its \(j\)-th prime once, \(1\le j\le n\), the contact adds \((A^{-1})_{ij}\), so

\[
z_1=\frac n{n+1}+\frac{n+1-j}{n+1}
=\frac{2n+1-j}{n+1}\le\frac{2n}{n+1}<2.
\]

These formulas satisfy both endpoint equations, including the one-prime arm \(n=1\). An absent arm may be encoded as \(n=0\) with contribution zero, but there is no arm prime and no valid contact index \(j\) when \(n=0\).

## Central equation and contradictions

Let \(S\) be the sum of the first coefficients over the arms. At \(E\),

\[
Z\cdot E=-3+S=-C\cdot E,
\qquad S=3-C\cdot E.
\]

The equation at \(E\) is part of the stated hypothesis and must be justified separately in any geometric application; it does not follow from the arm equations alone.

If \(C\cdot E=1\), neither arm has contact, so \(S<2\) with at most two arms, whereas the central equation requires \(S=2\). This is impossible, including configurations with zero or one arm.

If \(C\) meets one arm prime, then \(C\cdot E=0\). The contacted arm contributes strictly less than two and the possible other arm contributes strictly less than one, so \(S<3\), whereas the central equation requires \(S=3\). This is impossible. With only the contacted arm the stronger bound \(S<2\) holds.

If the contact hypotheses are broadened to allow no graph contact at all, the central equation still requires \(S=3\), while both arms are uncontacted and \(S<2\). That additional case is also impossible. Multiple graph contacts or contact multiplicity greater than one are outside this conclusion and would change the right-hand sides.

No integrality or effectiveness restriction on the \(z_i\) is needed for these contradictions. The strict finite-arm bounds suffice. The graph is also automatically negative definite under these hypotheses: the arm blocks are negative definite, and their central Schur complement is \(-3+\sum n/(n+1)<-1\). Negative definiteness is consistent with, but not needed for, the central coefficient contradiction.
