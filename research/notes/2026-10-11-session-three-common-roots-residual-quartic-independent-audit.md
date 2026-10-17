# Three-common-root family: independent residual-quartic support exclusion

Status: **PROVED (univariate algebra, characteristic zero).** No geometric
exclusion is asserted in this note. The proof handles every parameter in the
specified family with the stated carrier coefficient nonzero; it has no finite
exception set on that locus.

## 1. Corrected parameter family

Let the field be algebraically closed of characteristic zero and let `b != 0`.
The condition that the cubic `U` divide the quartic `V` fixes

\[
a=\frac32b^2,\qquad
g=\frac1{9b}-\frac23,\qquad
d=\frac1{54b^2}-\frac1{9b}.
\]

The initially transmitted negative sign `a=-3b^2/2` is incompatible with
`U | V`. Indeed the exact remainder for that negative sign is

\[
V\bmod U=-z^2-\frac{z}{3b}+\frac{1-6b}{27b^2}.
\]

For the corrected positive sign the quotient is

\[
V=\left(\frac32z+\frac1{6b}\right)U.
\]

Use the definitions from the parent calculation:

\[
\begin{aligned}
U&=2az^3-3bz^2-z+g,&
V&=3az^4-4bz^3-2z^2-z+d,\\
A&=az-b,&h&=az^3+z-g-1,\\
J&=AV-(Az-1)U,&
E&=J^2-(3zA-1)hJ+AUh^2.
\end{aligned}
\]

Since `U | V`, also `U | J` and `U | E`. Write `S=E/U`. The carrier
coefficient in the task is

\[
C_b=a^2g-ab-b^3=-\frac34b^3(2b+3).
\]

Thus its nonzero locus is exactly `b != 0,-3/2`.

## 2. The exact quartic

An exact expansion gives `S=-T/(432b)`, where

\[
\begin{aligned}
T={}&(324b^5+486b^4)z^4-(54b^4+405b^3)z^3\\
&+(270b^3+81b^2)z^2-(72b^3+132b^2+36b)z\\
&+48b^2+352b+12.
\end{aligned}
\]

In particular the leading coefficient of `S` is `C_b/2`; hence `S` has degree
exactly four for every allowed specialization. The degree of `U` is exactly
three because its leading coefficient is `3b^2`.

## 3. Two incompatible necessary resultants

Define

\[
R=(12b^2+116b+3)(72b^4+252b^3+1126b^2+513b+54)
\]

and

\[
\begin{aligned}
D={}&(2b+3)(2b^2+9b+15)^2\\
&\quad\cdot(9216b^6-208896b^5-2002096b^4-2800992b^3\\
&\hspace{52mm}-117672b^2+72b+45).
\end{aligned}
\]

The exact resultant identities are

\[
\operatorname{Res}_z(U,S)=-\frac{3b^5}{2048}R,
\qquad
\operatorname{Res}_z(S,S')=\frac{b^9}{8388608}D.
\]

Exact Euclidean polynomial arithmetic verifies

\[
\gcd_{\mathbf Q[b]}(R,D)=1.
\]

Now suppose every root of `S` were a root of `U`. The quartic `S` has at least
one root, so `U` and `S` would have a common root. Also a quartic whose distinct
roots lie among the at most three distinct roots of a cubic necessarily has a
repeated root. Therefore both displayed resultants would vanish. Since `b`
is nonzero, this would require `R(b)=D(b)=0`, contradicting their exact
coprimality. The argument works without assuming that `U` is squarefree.

Consequently, for **every** allowed `b`, the support of `S` is not contained in
the support of `U`. There are no exceptional parameters on `C_b != 0`.

## 4. Scope and evidence

The result excludes the univariate support condition in the corrected
`U | V` family. It does not on its own classify the other common-root strata,
prove that the displayed polynomial is the required global conductor
obstruction, or exclude a geometric STCI presentation. Those interpretations
remain the parent's responsibility.

The final source is
[verify_session_three_common_roots_residual_quartic_2026_10_11.m2](../computations/verify_session_three_common_roots_residual_quartic_2026_10_11.m2),
SHA-256 `e0762fcc2c959cbf32b87de10ced160b7913b0da5d0de6875917a9a97632727b`.
Its **eight exact assertions passed** in a captured execution. They verify
both divisibilities, exact quotient, carrier coefficient, quartic leading
coefficient, both resultant formulas and the coprimality. The negative-sign
remainder is also printed.

The fresh one-shot execution record, copied source, stdout and stderr are in
[2026-10-11-three-common-roots-quartic-support](../validation/2026-10-11-three-common-roots-quartic-support/execution-record.json).
The copied source is an execution snapshot of this one source, not a second
independent computation. Earlier development invocations of the source were
successful but were not captured as additional execution records; no count
or certificate relies on them.
