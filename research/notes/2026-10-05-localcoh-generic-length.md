# A quartic ancestor forces a curvilinear triple and a degree-four residual cycle

Date: 2026-10-05. Status: **PROVED**, conditional on the antecedent results
identified below. This note concerns the characteristic-zero monomial rational
quartic only; it does not exclude every quartic local-cohomology ancestor.

Let

\[
C_0=[s^4:s^3t:st^3:t^4],\quad I=I_{C_0},\quad
u=\frac{xz}{qB},\quad v=\frac{yw}{qB},\quad
q=xw-yz,\quad B=xz^2-y^2w.
\]

Suppose quartics \(F,G\) and \(\alpha\in H_I^2(S)_{-7}\) satisfy
\(F\alpha=u\), \(G\alpha=v\). P-037 supplies coprimality of the pair
and membership \(F,G\in I\). The note
`2026-10-05-localcoh-finite-bound.md` bounds its generic intersection
multiplicity by \(m\le3\), using the recorded characteristic-zero
degree-(4,4) exclusion. The note `2026-10-05-localcoh-degree4.md` excludes
principal-part order at most three, using P-010; therefore the ancestor has
order exactly four.

## Generic length is exactly three, rather than merely at most three

At the generic point of the curve, complete the transverse regular local
ring to \(R=K[[\xi,\eta]]\), where \(K=k(C_0)\), and write
\(E=H^2_{(\xi,\eta)}(R)\). Set

\[
J=(F,G)R,\qquad A=R/\operatorname{Ann}_R(\alpha),\qquad
\ell=\operatorname{length}_R A.
\]

The cyclic module \(R\alpha\) is isomorphic to \(A\), and its socle is
one-dimensional: it is a nonzero subspace of the one-dimensional socle
\(Ke\) of the transverse injective hull \(E\). Equivalently, \(A\) is
an Artinian Gorenstein algebra.

Since \(I^3\alpha\ne0\) and \(I^4\alpha=0\), its maximal-ideal chain
has at least four nonzero successive quotients, so \(\ell\ge4\).
Both targets are nonzero multiples of \(e\) over \(K\), hence the image
of \(J\) in \(A\) is its socle and has length one. The quotient map gives

\[
R/J\twoheadrightarrow A/JA,\qquad
m\ge\ell-1\ge3.
\]

The upper bound \(m\le3\) now forces

\[
\boxed{m=3,\qquad \ell=4,\qquad
\operatorname{Ann}_R(\alpha)\subset J.}
\]

The four nonzero terms in the maximal-ideal filtration already exhaust the
length of \(A\); its Hilbert function is \((1,1,1,1)\). Consequently
\(A\simeq K[[\tau]]/(\tau^4)\), and its socle quotient is
\(R/J\simeq K[[\tau]]/(\tau^3)\). Thus a surviving quartic pair must
define a **curvilinear triple at the generic transverse point**; its
ancestor defines the corresponding curvilinear quadruple there.

The complete intersection has degree sixteen, and \(3[C_0]\) contributes
degree twelve to its fundamental cycle. The remaining effective cycle has
degree exactly four. This is a cycle statement; it does not assert that the
residual curve is integral, reduced, smooth, or disjoint from \(C_0\).

## A further exclusion inside the constant-direction stratum

Write the proportional quartic first symbols in the balanced normal frame as
\(ar,br\), where \(r\) is a primitive basepoint-free direction of degree
\(e\), and \(a,b\in H^0(O_{\mathbf P^1}(9-e))\).

If \(a,b\) have no common projective zero, at every curve point one equation
has a nonzero linear normal term. It supplies a smooth local surface through
the curve. In that surface the second equation is locally
\(\eta^3 h(c,\eta)\), since the generic multiplicity is three. Removing
the residual factor \(h\) gives the local \(C_0\)-primary component
\((\xi,\eta^3)\). These components glue to an embedded primitive triple
with conormal quotient

\[
N_{C_0/\mathbf P^3}^*\twoheadrightarrow O_{\mathbf P^1}(e-7).
\]

For \(e=0\), this is the primitive triple of type \(O(-7)\) excluded
by P-010. Hence

\[
\boxed{e=0\quad\Longrightarrow\quad \gcd(a,b)\text{ has positive degree}}
\]

for any surviving ancestor. This excludes the open subset of the
constant-direction stratum on which the scalar factors form a basepoint-free
pencil. It leaves its scalar-basepoint boundary and every possible \(e=1,2\)
stratum unresolved.

## Failed shortcut: a top-symbol zero does not force target vanishing

It is tempting to argue that the length-four cyclic inverse system must be
Gorenstein in every transverse fiber, and therefore that its pure-cubic top
coefficient is nowhere zero. This implication is false. Over
\(D=k[[c]]\), in the finite inverse-monomial module
\(H^2_{(\xi,\eta)}(D[[\xi,\eta]])\), take

\[
\alpha=c\,\xi^{-1}\eta^{-4}+\xi^{-2}\eta^{-1},\qquad
e=\xi^{-1}\eta^{-1}.
\]

Then

\[
\xi\alpha=e,\qquad \eta^3\alpha=ce.
\]

The ideal \((\xi,\eta^3)\) has transverse length three. The cyclic module
\(D[[\xi,\eta]]\alpha\) is free of rank four over \(D\), with basis
\(\alpha,\eta\alpha,\eta^2\alpha,e\), and actions

\[
\eta:(\alpha,\eta\alpha,\eta^2\alpha,e)
\longmapsto(\eta\alpha,\eta^2\alpha,ce,0),\qquad
\xi:(\alpha,\eta\alpha,\eta^2\alpha,e)
\longmapsto(e,0,0,0).
\]

At \(c=0\), this abstract cyclic algebra has a two-dimensional socle,
spanned by the classes of \(\eta^2\alpha\) and \(e\); its injection into
the inverse-monomial module does not remain injective after passage to the
fiber. The top coefficient vanishes while \(e\) remains generated. The
exact companion `verify_localcoh_generic_length_model.py` checks these
actions, generic and special socle dimensions, and the annihilator description

\[
\operatorname{Ann}(\alpha)
=(\xi^2,\xi\eta,\eta^3-c\xi).
\]

Thus finite-flat cyclicity along the curve does not supply relative
Gorenstein fibers. Any global argument excluding top-coefficient zeros must
use extra ambient or multiplier information.

## Continuation boundary

Combine the new multiplicity-three condition with the exact pure-cubic
top-symbol lifting equations and the full multiplication tensor. The next
required information is the lower principal-part equation, which controls
whether the quartic scalar pencil can map this curvilinear quadruple to both
fixed socle targets. A primitive quadruple in the ambient space, or a pure
cubic that lifts to the 30-dimensional ancestor space, does not by itself
produce those two multiplier equations.
