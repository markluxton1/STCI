# Independent audit: the pure constant directions in regular degree (4,6)

Date: 2026-10-05. Status: **PASS**, with a small local-intersection
clarification recorded below. Scope is exactly characteristic zero,
the smooth monomial rational quartic
\(C_0=[s^4:s^3t:st^3:t^4]\), and the regular-ratio branch. This audit
does not extend the result to arbitrary ratios, mixed constant directions,
degree-one horizontal directions, or all rational quartics.

The audited proof is
`research/notes/2026-10-05-mixed46-regular.md`, and its exact arithmetic
companion is `research/computations/verify_mixed46_regular.py`.
The conclusion is that, after globally subtracting a quadratic multiple of
the quartic from the sextic, a hypothetical set-theoretic pair cannot have
quartic first normal form \(hV\) or \(hU\) in the stated balanced frame.

## What was checked independently

The full exact script was run with

```
/private/tmp/stci-cas-venv/bin/python research/computations/verify_mixed46_regular.py
```

It passed its assertions. Before reading the complete proposed proof, the
audit independently derived the Segre residual

\[
\rho=b_0(c_0a_0^3+c_3a_0^2a_1+c_6a_0a_1^2+c_9a_1^3)
     +b_1(c_1a_0^3+c_4a_0^2a_1+c_7a_0a_1^2),
\]

where \(F|_Q=c\rho\) and \(c=a_1b_0^3-a_0b_1^3\). The eight-dimensional
pure quartic space and the formulas

\[
h=c_0+c_1z+c_3z^3+c_4z^4+c_6z^6+c_7z^7+c_9z^9,
\qquad
R=\kappa+c_6z-c_7z^2+3c_9z^4
\]

agree with the derived ideal-space calculation.

For a genuine pair, the forms have no common surface factor. Thus their
intersection is a degree-24 complete-intersection curve supported on
\(C_0\), and its generic transverse length is \(24/4=6\). This is sufficient
for the generic elimination argument; it does not assert uniform
curvilinearity at every point.

The ambient sextic reduction uses the proved symbolic-square description
from P-017/P-022:

\[
H^0(I_C^{(2)}(6))
=qH^0(I_C(4))+\langle A^2,AB,B^2,BD,D^2\rangle.
\]

Only \(D^2\) contributes to the coefficient of \(z^{10}U^2\), and its
coefficient is \(4\). Every \(qF_4\) term contributes to that coefficient
with degree at most nine. Therefore divisibility of the quadratic normal
form by \(V\) kills the \(D^2\) coefficient, and indeed makes
\(a_0\mid\sigma\) in \(G|_Q=c^2\sigma\). This is an exhaustive ambient
kernel argument, not an assumption that an arbitrary jet lifts.

## Boundary and contact-degree checks

If \(c_9=0\), the displayed residual has the factor \(a_0\). Since
\(a_0\mid\sigma\) too, the entire ruling \(a_0=0\) lies in both carriers.
It is an extra line, so this boundary is excluded without any smoothness
assumption.

If \(c_9\ne0\), let \(P=[0:0:0:1]\). In the chart \(x_3=1\), put
\((x_0,x_1,x_2)=(X,Y,W)\). At \(P\),

\[
dF=2c_9\,dX,\qquad dq=dX.
\]

Hence the two smooth surfaces \(F\) and \(Q\) have the same tangent plane.
On \(Q\), use \((a_0,b_0)=(Y,W)\), so

\[
c=W^3-Y,\qquad
\rho=c_9W+c_7Y+O((Y,W)^2).
\]

The tangent to \(C\) is the \(W\)-axis. The tangent to \(\rho\) is
\(c_9\,dW+c_7\,dY=0\), so these curves are transverse in the common
tangent plane. Consequently their local intersection multiplicity is one
on **both** \(Q\) and the smooth surface \(F\). This last observation is
the small clarification needed when passing from the intersection
calculation on \(Q\) to divisibility on \(F\); intersection multiplicity
on two unrelated containing surfaces should not be identified without
checking it.

In particular \(Y=a_0\) is a parameter on the smooth germ \(\rho\), and a
local Cartier equation \(v\) for \(C\subset F\) restricts to an element of
order one on \(\rho\). Generic order six along \(C\) implies
\(v^6\mid G\) in \(\mathcal O_{F,P}\). One can justify this by localizing
at the height-one prime \((v)\) in the regular local ring and then
contracting \((v^6)\); regularity makes this symbolic power ordinary.
Thus

\[
\operatorname{ord}_{\rho,P}(G)\ge6,
\quad
\operatorname{ord}_{\rho,P}(c)=1,
\quad
\operatorname{ord}_{\rho,P}(\sigma)\ge4.
\]

Since \(\sigma\) is a binary quartic, this forces
\(\sigma=\gamma a_0^4\), \(\gamma\ne0\). An initially considered
objection—that finite zeros of \(h\) might permit additional residual
rulings—is resolved by this local argument: the single smooth point
\(P\) already exhausts the degree-four vanishing allowance of \(\sigma\).
Support considerations alone would not have forced this concentration.

## Cubic identity and final contradiction

The residual equality gives
\(G=\gamma A^2+qF'\). Because \(G\) has normal order at least two and
\(q\) has order one generically, the quotient quartic lies in \(I_C(4)\).
Divisibility of \(G_2\) by \(V\) then forces the first normal form of
\(F'\) to be \(h'V\). No quartic quotient is omitted.

The elimination \(V=-(R/h)U^2+O(U^3)\) gives cubic coefficient
\(R'-h'R/h\). After subtracting the scalar multiple of \(F\) that removes
\(c'_9\), the coefficients in the necessary identity
\(hR'-h'R=0\) successively give

\[
[z^{11}]=-4c_9c'_7,\quad
[z^{10}]\big|_{c'_7=0}=-2c_9c'_6,\quad
[z^9]\big|_{c'_7=c'_6=0}=c_9\kappa'.
\]

Thus \(c'_7=c'_6=\kappa'=0\), then \(R'=0\), then \(h'=0\) since
\(R\ne0\). The quartic space has no further first-normal kernel beyond
\(kq^2\), already killed by \(\kappa'=0\), so \(F'\) was a scalar
multiple of \(F\). Modulo \(F\), the sextic is \(\gamma A^2\).
Since \(A=V\) on the affine chart and \(R\ne0\), its generic transverse
order is exactly four, contradicting six.

Finally the coordinate reversal can be checked directly, without importing
an orbit assertion. Put

\[
w=\frac{z^3+V}{z^4+U+\tfrac32zV},\qquad
\widetilde V=\frac z{z^4+U+\tfrac32zV}-w^3,
\]

\[
\widetilde U=\frac1{z^4+U+\tfrac32zV}-w^4-\tfrac32w\widetilde V.
\]

To first normal order,

\[
\widetilde V=2z^{-7}U,
\qquad
\widetilde U=\tfrac12z^{-7}V.
\]

Thus the reversal exchanges the two pure constant directions and preserves
the regular-ratio condition. The pure-\(U\) conclusion follows from the
fully audited pure-\(V\) case.

No counterexample or missing parameter stratum was found within the stated
scope. The productive remaining branch is the mixed constant direction,
where both coefficients are nonzero; the proof above gives no conclusion
there.
