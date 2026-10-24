# Independent review: the osculating conormal line and its coincidence divisor

Date: 2026-10-24. Reviewer: `osculating_normal_count`.

Status: **independently reconstructed exploratory geometry; not canonically
promoted**. The count proposed by the parent investigation is correct with the
qualifications below. No STCI obstruction or new bound on actual STCI equations
is proved.

Work over an algebraically closed field of characteristic zero, for the fixed
embedding

\[
\nu([s:t])=[s^4:s^3t:st^3:t^4],\qquad C=\nu(\mathbf P^1).
\]

The sole retained normal-bundle input is the accepted
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md):
\(E=N^*_{C/\mathbf P^3}=\mathcal O(-7)^2\), with degrees taken on
\(\mathbf P^1\). Its proof is not rerun. No quartic-carrier exclusion or
higher-contact classification is used.

## 1. The intrinsic line defined by osculation

The osculating plane at \([s:t]\) has coefficients

\[
h(s,t)=(-t^4,\ 2st^3,\ -2s^3t,\ s^4).
\]

Indeed, on \(s=1\), its pullback to \(C\) is
\((v-u)^3(v+u)\). The coefficient vector is nowhere zero, including at
the two endpoints. Because this plane contains the tangent line of \(C\),
its differential belongs to \(E(4)\). Its coefficient degree gives a
nowhere-vanishing line inclusion

\[
\mathcal O(-4)\longrightarrow E(4).
\]

Consequently the osculating conormal direction is the saturated subline

\[
L_{\rm osc}\simeq\mathcal O(-8)\subset E.
\tag{1}
\]

Equivalently, the tautological line of the degree-four osculating map
\(\mathbf P^1\to(\mathbf P^3)^\vee\) is
\(L_{\rm osc}(4)=\mathcal O(-4)\). This argument proves (1) directly,
without using a singular auxiliary surface or its normalization.

There is also an independent check using the cubic scroll

\[
R=x_0x_2^2-x_1^2x_3.
\]

On \(x_0=1\), use normal coordinates
\(v=x_2-u^3,\ w=x_3-u^4\), with \(u=x_1\). Then

\[
R=v^2+u^2(2uv-w),\qquad
\sigma_R=u^2(2uv-w).
\]

On \(x_3=1\), use \(z=x_2\),
\(v'=x_1-z^3,\ w'=x_0-z^4\). Then

\[
R=-(v')^2+z^2(w'-2zv').
\]

Thus its first normal symbol vanishes exactly to order two at each
endpoint and nowhere else. Saturating
\(\mathcal O(-12)\xrightarrow{\sigma_R}E\) removes this degree-four
divisor and again gives \(\mathcal O(-8)\). Its limiting direction at
the endpoints is the hyperosculating plane, although \(R\) itself is
singular there. One must use this saturated direction rather than call
the tangent plane of a singular surface uniquely defined.

## 2. Exact coincidence count for an individual surface

Let \(F\in I_C(d)\) have nonzero first normal symbol
\(\sigma_F\in H^0(E(4d))\). Let \(A_F\) be its zero divisor, and
let \(L_F\subset E\) be its saturated image. Then

\[
L_F=\mathcal O(\deg A_F-4d).
\]

The wedge map

\[
L_F\otimes L_{\rm osc}\longrightarrow\det E
\]

is either identically zero, in which case the two saturated line
subbundles agree, or has an effective zero divisor \(D_F^{\rm osc}\)
of degree

\[
\boxed{\deg D_F^{\rm osc}=4d-6-\deg A_F.}
\tag{2}
\]

This follows from \(\deg\det E=-14\) and (1). At a point where
\(F=0\) is smooth, the vanishing means exactly
\(T_pV(F)=H_p\). At a point of \(A_F\), the surface is singular,
so the divisor compares the **limiting saturated normal direction**
with the osculating direction; it does not assign a unique tangent
plane to the singular surface. If \(\sigma_F=0\) identically, neither
\(L_F\) nor (2) is available. If \(V(F)\) is smooth along all of
\(C\), then \(A_F=0\) and the count is \(4d-6\), unless the
directions agree identically. In the latter case degree comparison
would force \(4d=8\); the actual smooth quadric below does not have
identically osculating tangent plane.

This identity uses the actual first normal symbol. It does not assert
that every abstract line subbundle or every prescribed coincidence
divisor comes from a global homogeneous equation.

## 3. An explicit polynomial check, including both endpoints

For any homogeneous \(F\in I_C(d)\), define

\[
P_F(s,t)=\sum_{i=0}^3 F_{x_i}(\nu(s,t))\nu_i(s,-t).
\]

Its degree is \(4d\), and \(s^3t^3\) always divides it. To see this
at \(s=1\), put \(f_i(u)=F_{x_i}(1,u,u^3,u^4)\). Euler's identity
and differentiation along \(C\) give

\[
f_0+uf_1+u^3f_2+u^4f_3=0,\qquad
f_1+3u^2f_2+4u^3f_3=0.
\]

Hence

\[
P_F(1,u)=4u^3(f_2+2uf_3).
\tag{3}
\]

The reversed chart proves divisibility by \(s^3\). In the normal
coordinates above, \(\sigma_F=f_2v+f_3w\), whereas
\(L_{\rm osc}\) has primitive generator \(2uv-w\). Their wedge
is \(-f_2-2uf_3\), so (3) is precisely the local coincidence equation,
with the fixed endpoint factor separated. Thus

\[
\frac{P_F}{4s^3t^3}\in H^0(\mathcal O(4d-6))
\]

records \(A_F+D_F^{\rm osc}\) if the wedge is nonzero. The factor
\(A_F\) must be removed before interpreting zeros as coincidences of
saturated directions.

For \(q=x_0x_3-x_1x_2\), one gets
\(P_q/(4s^3t^3)=st\). Thus the quadric's tangent plane is
osculating exactly at the two endpoints, each once. For the scroll
\(R\), the polynomial is identically zero, as required.

## 4. A global counterexample test for an unscoped small bound

Take the explicit cubic

\[
F=(x_0^2x_2-x_1^3)+(x_1x_3^2-x_2^3).
\tag{4}
\]

Its first normal symbol on \(x_0=1\) is

\[
\sigma_F=(1-3u^6)v+2u^5w.
\]

The two coefficients have no simultaneous zero. The reversed chart
has the identical formula with \(u,v,w\) replaced by \(z,v',w'\).
Therefore this cubic is smooth at every point of \(C\). Moreover

\[
P_F=4s^3t^3(s^6+t^6).
\]

It has six distinct osculating tangent-plane coincidences. Thus a
universal bound of two for the osculating coincidences of an arbitrary
smooth containing surface is false. This is a statement about
individual containing surfaces; it is not an STCI construction and
does not refute any theorem with additional STCI hypotheses.

There is also a useful test for broader containing **pairs**. Let
\(L\) be a nonzero linear form, and set

\[
G=LF+q^2.
\]

Then \((F,G)=(F,q^2)\), a proper homogeneous pair. Its two nonzero
generic first normal symbols have the same saturated direction
\(L_F=\mathcal O(-12)\). In the balanced bundle
\(E(7)=\mathcal O^2\), this direction defines a map to
\(\mathbf P^1\) of degree five. This already rules out an unscoped
degree-at-most-two bound based on proper containment and common normal
direction alone.

The residual support is explicit. In Segre coordinates
\([x_0:x_1:x_2:x_3]=[ac:ad:bc:bd]\),

\[
F|_Q=(a^2-b^2)(bc^3-ad^3).
\]

Consequently \(V(F,G)_{\rm red}\) is \(C\) together with the two
trisecant ruling lines \(a=b\) and \(a=-b\). This example **fails
sole support in a visible way**. It cannot be used against a proposed
bound whose hypotheses include \(V(F,G)_{\rm red}=C\).

## 5. Computation and review boundary

The displayed formulas for (4), its reversed chart, the scroll normal
symbols, and \(P_F\) were independently expanded with SymPy 1.14.0,
using `/tmp/stci-z4-env/bin/python`, with exact polynomial comparisons.
The final command returned:

```text
PASS: cubic smooth along C, endpoint-normal checks, six osculating tangencies
D_F = 4*s**3*t**3*(s**2 + t**2)*(s**4 - s**2*t**2 + t**4)
```

The proof above is independent of that expansion. The initial test used
structural equality against a differently factored expression, which
failed; replacing it by expansion of the difference returned zero.
This was a test-harness correction, not a counterexample or change to
the mathematical formulas.

The reviewed conclusion is (1)--(3), including all endpoint and
singular-symbol qualifications, plus the explicit counterexample tests.
What remains unproved is any implication from these identities to an
STCI obstruction, or any bound on the common saturated direction of
actual sole-support equations. Such a bound would need genuinely
global input beyond the incidence geometry used here.
