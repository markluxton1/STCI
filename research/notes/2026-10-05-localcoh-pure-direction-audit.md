# Independent audit of pure constant quartic directions

Date: 2026-10-05. Status: **PASS**. Scope is the characteristic-zero
monomial rational quartic \(C_0=[s^4:s^3t:st^3:t^4]\), quartic multiplier
pairs, and the two pure constant directions in the balanced frame

\[
U=w-t^4-\frac32t(z-t^3),\qquad V=z-t^3.
\]

This proves an exclusion for quartic common local-cohomology ancestors
using the established order-three primitive-triple obstruction. It does
not settle the mixed constant directions or degree-one/two directions.
The exact independent companion is
`research/computations/verify_localcoh_pure_direction_audit.py`.

## 1. Exact pure-direction space and transverse coefficients

Retain

\[
q=xw-yz,\quad A=x^2z-y^3,\quad
B=xz^2-y^2w,\quad C=yw^2-z^3.
\]

The quartic symbol-image classification gives every pure-\(V\) form
uniquely as

\[
\begin{aligned}
 F={}&c_0xA+c_1yA+c_3zA+c_4wA\\
 &+c_6(zB+qyw)+c_7(wB+qz^2)
  +c_9(-zC+2qw^2)+\kappa q^2.
\end{aligned}
\]

Its first symbol is \(h_FV\), where

\[
h_F=c_0+c_1t+c_3t^3+c_4t^4+c_6t^6+c_7t^7+c_9t^9.
\]

Substituting \(x=1,y=t,z=t^3,w=t^4+U\), equivalently setting \(V=0\),
gives the exact identity

\[
 F|_{V=0}=R_FU^2+2c_9U^3,
 \qquad R_F=\kappa+c_6t-c_7t^2+3c_9t^4.
\]

In particular, \(R_F=0\) if and only if
\(\kappa=c_6=c_7=c_9=0\), and then \(F\in AS_1\). A zero first symbol
means \(F=\kappa q^2\); this boundary is included.

## 2. The contact identity has no missing coefficient strata

For two such forms, define

\[
\Delta=h_FR_G-h_GR_F.
\]

The following exhaustive algebraic statement holds:

\[
\boxed{\Delta=0\quad\Longrightarrow\quad
\text{either }F,G\text{ are scalar-proportional, or }F,G\in AS_1.}
\]

To prove it, if some \(R\) is nonzero choose the highest active coefficient
among \(c_9,c_7,c_6,\kappa\) across both forms, interchange the forms if
necessary so that it occurs in \(F\), and subtract a scalar multiple of
\(F\) from \(G\) to kill that coefficient in \(G\). This operation preserves
the contact identity. The four possible cases are:

* If \(c_9\ne0\), now \(c'_9=0\). The coefficients of \(\Delta\) in
  degrees eleven, ten, and nine successively give
  \(-4c_9c'_7=0\), \(-2c_9c'_6=0\), and \(c_9\kappa'=0\).
* If both degree-nine coefficients vanish and \(c_7\ne0\), now
  \(c'_7=0\). Degrees eight and seven successively give
  \(2c_7c'_6=0\) and \(c_7\kappa'=0\).
* If all degree-nine and degree-seven coefficients vanish and
  \(c_6\ne0\), now \(c'_6=0\). Degree six gives
  \(c_6\kappa'=0\).
* In the last case both forms have \(c_9=c_7=c_6=0\), and
  \(\kappa\ne0\). Killing \(\kappa'\) already gives \(R_G=0\).

In each case all four coefficients of \(R_G\) vanish. Since \(R_F\ne0\),
the identity then forces \(h_G=0\). Together with \(\kappa'=0\), all eight
coefficients of the adjusted \(G\) vanish, so the original \(G\) was
proportional to \(F\). This includes \(h_F=0\), since the final argument
does not divide by \(h_F\). If both \(R\)'s initially vanish, both forms
lie in \(AS_1\), as claimed.

Therefore an ambient-coprime pair has \(\Delta\ne0\). The two forms
cannot both have zero first symbol, since the first-symbol kernel is
\(kq^2\).

## 3. Generic transverse length and the ancestor implication

Let \(K=k(C_0)\). For an ambient-coprime pair the generic transverse
algebra is the finite-colength complete intersection in \(K[[U,V]]\).
At least one of \(h_F,h_G\) is nonzero; interchange the forms so that
\(h_F\ne0\). The formal implicit-function theorem eliminates \(V\):

\[
 V=-\frac{R_F}{h_F}U^2+O(U^3).
\]

Modulo \(F\), the coefficient of \(U^2\) in \(G\) is

\[
 R_G-\frac{h_G}{h_F}R_F=\frac\Delta{h_F}.
\]

Thus generic transverse length at least three is equivalent to
\(\Delta=0\), under the finite-colength hypothesis. Since a coprime pair
has \(\Delta\ne0\), its generic transverse length is exactly two. This
also covers a zero first symbol for \(G\): then
\(G=\kappa' q^2\) with \(\kappa'\ne0\), and the same coefficient is
\(\kappa'\).

Suppose now quartics obey \(F\alpha=u,G\alpha=v\), where the independent
targets lie in the first socle and \(\alpha\) has degree \(-7\). P-037
forces \(F,G\) to be coprime: a common factor would produce multipliers
of degree at most three. Generic transverse length two gives
\(I^2\subset(F,G)\) at the generic curve point. Since
\(I(F,G)\alpha=0\), it follows that \(I^3\alpha=0\) generically.

The torsion-free local inverse-monomial module propagates this
annihilation over every closed curve point. The established
\(H^0_{\mathfrak m}(H_I^2(S))=0\) then removes the possible cone-vertex
ambiguity. These are precisely the propagation arguments in
`2026-10-05-localcoh-finite-bound.md`, with \(m=2\). Hence globally

\[
\boxed{I^3\alpha=0.}
\]

The balanced normal bundle gives

\[
(\mathcal T_n/\mathcal T_{n-1})(-7)
\simeq O(7n-21)^{\oplus n},
\qquad H^0(\mathcal T_2(-7))=0.
\]

Thus a nonzero ancestor would have order exactly three, with a nonzero
constant quadratic top symbol. Multiplication by the nonzero pure first
symbol \(hV\), while the result belongs to the first socle, forces that
quadratic to be the perpendicular pure square. It is nowhere zero because
its coefficients are global constants.

As proved in the order-three argument of
`2026-10-05-localcoh-degree4.md`, this cyclic inverse system defines a
primitive triple of conormal type \(O(-7)\). Locally one may normalize it
to

\[
 \alpha=\xi^{-1}\eta^{-3}
       +c\xi^{-2}\eta^{-1}
       +d\xi^{-1}\eta^{-2}
       +e\xi^{-1}\eta^{-1},
\]

whose annihilator is \((\xi-c\eta^2,\eta^3)\). Its cyclic module has
the free basis \(\alpha,\eta\alpha,\eta^2\alpha\), so it is a primitive
triple in every transverse fiber. The annihilator ideals glue under the
unit changes in local trivialization of the twisted ancestor. P-010
excludes such a primitive triple in characteristic zero. Therefore no
pure-\(V\) quartic pair supplies a common ancestor.

## 4. The pure-\(U\) direction is included by an exact symmetry

The ambient coordinate reversal
\(\tau(x,y,z,w)=(w,z,y,x)\) preserves \(C_0\), sends the curve parameter
to its inverse, fixes \(q\), and sends \(B\) to \(-B\). In the fixed
balanced frame its quartic symbol action is exactly

\[
 \boxed{\sigma(\tau F)
 =(2t^9Q(1/t),\tfrac12t^9P(1/t)).}
\]

The independent script verifies this on an 18-element basis of
\(I_{C_0}(4)\). Consequently reversal exchanges the two pure constant
directions, preserving ambient coprimality and generic transverse length.
It also exchanges the specific local-cohomology targets by
\(\tau u=-v,\tau v=-u\). The pure-\(U\) exclusion follows with no
additional hypothesis.

The audited conclusion is an all-stage exclusion of both pure constant
directions for quartic ancestors. Its contact argument alone is about
generic multiplicity two; the essential final input is the established
order-three primitive-triple obstruction.
