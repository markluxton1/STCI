# Four ruling lines obstruct every mate of the mixed-weight seed

October 30, 2026. Status: **independently reviewed provisional
all-mate-degree exclusion**, with the
[independent audit](2026-10-30-mixed-weight-line-obstruction-audit.md).
This extends the independently reviewed
[degree-six contact calculation](2026-10-29-mixed-weight-contact.md).
The earlier certificate and its audit are retained as evidence, not rerun
or replaced. No canonical result or question is changed.

## Exact proposed statement

Let \(k\) be algebraically closed of characteristic zero and
\[
C_0=[s^4:s^3t:st^3:t^4],\quad
q=x_0x_3-x_1x_2,\quad
c_0=x_1^3-x_0^2x_2,\quad c_2=x_2^3-x_1x_3^2.
\]
For every \(\alpha\beta\ne0\), the integral surface
\[
X_{\alpha,\beta}=V(q^3+\alpha c_0^2+\beta c_2^2)
\]
has **no homogeneous set-theoretic mate of any positive degree** for
\(C_0\).
Integrality of every member is an input from the reviewed degree-six
calculation. The new argument uses actual ruling lines and the degrees of
the pullback of a hypothetical global equation on the normalization.
It makes no assertion about other sextic families or arbitrary carriers.

## 1. Normalization of the parameters and four actual lines

The curve-preserving torus substitution from the
[earlier proof](2026-10-29-mixed-weight-contact.md) puts every nonzero
parameter pair, up to a projective automorphism and nonzero scalar, into
\[
F_h=hq^3+c_2^2-c_0^2,\qquad h\ne0.
\]
Work with this form. On the affine chart \(x_0=1\), write
\[
x_1=t,\qquad x_2=w,\qquad x_3=tw+q.
\]
On the target quadric \(q=0\),
\[
c_0=t^3-w,\qquad c_2=w^2(w-t^3),\qquad
F_h|_{q=0}=(w-t^3)^2(w^4-1).
\]
Consequently, for each fourth root of unity \(\zeta\), the **actual
projective line**
\[
L_\zeta=V(x_2-\zeta x_0,\ x_3-\zeta x_1)
\]
lies on \(X_h\). It is not a component of \(C_0\).
Its intersection with \(C_0\) consists of the three distinct points
\[
[1:t:t^3:t^4],\qquad t^3=\zeta.
\]
None is a parameter endpoint. The remaining point of the projective line
is \([0:1:0:\zeta]\), which is not on \(C_0\).

## 2. Which normal branch each line meets

At the generic point of \(C_0\), set \(u=w-t^3\). The quadratic transverse
initial form of \(F_h\) is
\[
(t^6u-2t^5q)^2-u^2
=[(t^6-1)u-2t^5q][(t^6+1)u-2t^5q].
\]
There are two distinct smooth formal branches over \(k(t)\), labelled
by their tangent equations \(c_2=+c_0\) and \(c_2=-c_0\). Let
\(\Gamma_+\) and \(\Gamma_-\) be the corresponding irreducible curves in
the finite normalization \(\nu:S\to X_h\). Each maps to \(C_0\) with
generic degree one. These are the only divisorial components above
\(C_0\), since the generic transverse curve has exactly these two
branches.

The same two branches remain distinct and their normalizations remain
smooth at every point \(t^3=\zeta\): the discriminant of the displayed
binary quadratic is \(16t^{10}\ne0\). More explicitly, its \(q^2\)
coefficient is a unit. The formal Weierstrass factors therefore write
each local surface branch as a smooth graph \(q=q_\pm(t,u)\), and
\(u=0\) is its local inverse curve.

On \(L_\zeta\) one has the exact identity
\[
c_2=-\zeta^2c_0.
\]
Thus its strict transform meets only the curve with label
\(-\zeta^2\) at each of the three intersection points. Its transverse
coordinate is \(u=\zeta-t^3\), which has a simple zero there. The
intersection with that inverse curve has multiplicity one at each
point. Two of the four lines attach to \(\Gamma_+\), and two attach
to \(\Gamma_-\). This is actual branch attachment, not merely a
comparison of generic tangent directions.

The line is generically in the smooth locus of \(X_h\). Indeed at
\(q=0,w=\zeta,w\ne t^3\), differentiating the displayed restriction
with respect to \(w\) gives \(4\zeta^3(\zeta-t^3)^2\ne0\).
Its strict transform therefore maps to the line birationally.

## 3. A hypothetical mate gives incompatible degree identities

Suppose a homogeneous form \(G_b\), \(b>0\), satisfied
\(V(F_h,G_b)_{\mathrm{red}}=C_0\).
It does not vanish identically on \(X_h\), and its pullback is a
nonzero section of \(bH\), where \(H=\nu^*\mathcal O_{X_h}(1)\).
Its effective divisor has the form
\[
\operatorname{div}(\nu^*G_b)=r\Gamma_++s\Gamma_-,
\qquad r,s>0.
\]
There can be no other divisor component: its image would be contained
in \(C_0\), and the two listed generic branches exhaust the divisorial
inverse image. Possible isolated inverse points do not add a divisor
component or alter the degree identity.

Near an attaching point of \(L_\zeta\), the relevant local surface
branch is regular, with inverse curve parameter \(u\). The pullback
of \(G_b\) is therefore \(u^r\) times a unit, or \(u^s\) times a unit,
according to the label. An extra zero of the remaining factor would
give another divisor component, contrary to the support assumption.
Since \(u|_{L_\zeta}\) has a simple zero, the order of \(G_b\) on the
line is exactly \(r\), respectively \(s\), at each of its three
points on \(C_0\).

The restriction \(G_b|_{L_\zeta}\) is a nonzero section of
\(\mathcal O_{\mathbf P^1}(b)\). Otherwise the line itself would be
additional intersection support. It has no zeros outside those three
points. The two labels consequently give
\[
b=3r,\qquad b=3s.
\tag{1}
\]
On the other hand, \(H^2=6\) and \(H\cdot\Gamma_\pm=4\). Intersecting
the pullback divisor with \(H\) gives
\[
6b=4(r+s).
\tag{2}
\]
Equations (1) and (2) imply \(6b=8b/3\), impossible for \(b>0\).
This proves the proposed exclusion without fixing the mate degree.

## 4. A residual consequence retaining proper intersections

For any actual proper containing pair \((F_h,G_b)\), let \(r,s\) be
its two finite generic branch orders, so \(m_C=r+s\). If
\(m_C>2b/3\), at least one branch order exceeds \(b/3\).
Both ruling lines attached to that branch must then be contained in
\(V(G_b)\): a nonzero degree-\(b\) restriction would already have more
than \(b\) zeros at its three attaching points. Those two lines are
genuine residual components downstairs.

This last argument uses a lower bound for the local zero orders; any
additional local zeros strengthen it. It does not assert that every
proper mate has high contact, or compute the full residual scheme.
It explains geometrically why a sole-support candidate is impossible.

## Verification and review boundary

The new exact polynomial control is
[stci_mixed_weight_lines_2026_10_30.m2](../computations/stci_mixed_weight_lines_2026_10_30.m2),
with its [saved output](../computations/stci_mixed_weight_lines_2026_10_30.txt).
It checks the quadric factorization, the four line identities, and the
transverse quadratic discriminant. The normalization, branch-attachment,
and divisor arguments above were independently reconstructed in the
linked audit, which also supplies a separate exact verifier. Its passing
verdict is specific to this family and all positive mate degrees; it
is not a canonical promotion.
