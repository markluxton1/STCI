# Independent audit: four-line obstruction for every mate degree

October 30, 2026. Reviewer: line_audit, independent of the proposing
root agent.

**Verdict: PASS for the entire characteristic-zero family and all positive
mate degrees.** This is independent review of a provisional contribution,
not canonical promotion and not an unrestricted STCI theorem.

The audited proposal is
[the four-line obstruction](2026-10-30-mixed-weight-line-obstruction.md).
The accepted input for this audit is the already reviewed integrality of
every member in
[the mixed-weight contact note](2026-10-29-mixed-weight-contact.md).
Its proof and jet certificate were not rerun.

## Exact claim and parameter coverage

For the fixed embedded quartic
\(C_0=[s^4:s^3t:st^3:t^4]\) over an algebraically closed characteristic-zero
field, every
\[
F_{\alpha,\beta}=q^3+\alpha c_0^2+\beta c_2^2,\qquad \alpha\beta\ne0,
\]
has no homogeneous mate of any positive degree. The mate may be reducible
or nonreduced; no restriction on its normal order is imposed.
Here \(q=x_0x_3-x_1x_2\), \(c_0=x_1^3-x_0^2x_2\), and
\(c_2=x_2^3-x_1x_3^2\).

I independently checked that the torus weights are \(4,3,9\). Choosing
\(\rho^{12}=-\alpha/\beta\), composing with
\((x_0,\rho x_1,\rho^3x_2,\rho^4x_3)\), and dividing by
\(\beta\rho^{18}\), gives
\[
F_h=hq^3+c_2^2-c_0^2,\qquad h=1/(\beta\rho^6)\ne0.
\]
Thus no nonzero parameter pair is omitted. The argument below is uniform
in \(h\); it does not invert a parameter-dependent minor.

## Independent reconstruction of the lines and their attachment

On \(x_0=1\), set \(x_1=t,x_2=w,x_3=tw+q\). Direct substitution gives
\[
F_h|_{q=0}=(w-t^3)^2(w^4-1).
\]
Hence \(L_\zeta=(x_2=\zeta x_0,\ x_3=\zeta x_1)\) is an actual line
on the surface for each \(\zeta^4=1\). It meets \(C_0\) at precisely
the three distinct nonzero parameters \(t^3=\zeta\). Its point at
infinity is \([0:1:0:\zeta]\), outside \(C_0\). These statements include
all projective points of each line.

Write \(u=w-t^3\). I independently recovered the transverse quadratic
\[
4t^{10}q^2-4t^{11}qu+(t^{12}-1)u^2
=[(t^6-1)u-2t^5q][(t^6+1)u-2t^5q].
\]
Its discriminant is \(16t^{10}\). Therefore the generic transverse node
splits over \(k(t)\) into two branches, each with residue field \(k(t)\).
In the finite normalization these give two divisorial inverse curves
\(\Gamma_+,\Gamma_-\), each of generic degree one over \(C_0\), labelled
by \(c_2=+c_0\) and \(c_2=-c_0\).

The attachment assertion needs more than the generic tangent factors.
At a line-intersection point \(t_0^3=\zeta\), the coefficient \(4t^{10}\)
of \(q^2\) is a unit. Weierstrass preparation in
\(k[[t-t_0,u]][[q]]\) produces a monic quadratic in \(q\) times a unit.
Its discriminant is \(u^2\) times a unit whose leading value is
\(t_0^{-10}\), after dividing the transverse quadratic by its leading
\(q^2\) coefficient \(4t^{10}\). The unit has a square root in this complete
characteristic-zero local ring. Thus its two factors are
\(q-f_+(t,u)\) and \(q-f_-(t,u)\), giving regular local normalization
branches with coordinates \(t-t_0,u\). The inverse curve is \(u=0\)
on each.

The exact identity on the line is
\[
c_2=-\zeta^2c_0.
\]
Its tangent direction is \(q=0\), while the two local surface tangent
directions at the intersection are distinct. Substitution of the formal
line into the two-factor equation has integral target \(k[[t-t_0]]\);
one factor vanishes identically and the other does not. The selected
factor is the one with label \(-\zeta^2\). This proves actual local
attachment to that branch, rather than only a coincidence of tangent
directions.

The strict transform of the line has no second attaching point over this
same parameter. The surface is generically smooth along the line:
\[
\left.\frac{\partial(F_h|_{q=0})}{\partial w}\right|_{w=\zeta}
=4\zeta^3(\zeta-t^3)^2\ne0
\]
away from its intersections with \(C_0\). Its strict transform is
therefore finite and birational over the smooth projective line, hence
is isomorphic to it. Equivalently, a finite integral extension inside the
same function field equals the integrally closed local rings of
\(\mathbf P^1\).

Finally \(u|_{L_\zeta}=\zeta-t^3\) has a simple zero at each attaching
point. Thus the line meets its selected inverse curve with local
intersection multiplicity one. The two values \(\zeta=\pm1\) select
one label and the two values \(\zeta=\pm i\) select the other.

## Independent reconstruction of the degree contradiction

Assume \(G_b\), \(b>0\), cuts out only \(C_0\) on \(X_h\). Let
\(\nu:S\to X_h\) be the finite normalization and
\(H=\nu^*\mathcal O_{X_h}(1)\). Since the generic node has only the two
listed inverse curves, the effective divisor of the pulled-back
nonzero section is
\[
\operatorname{div}(\nu^*G_b)=r\Gamma_++s\Gamma_-,\qquad r,s>0.
\]
No omitted divisorial component can lie over an isolated point of \(C_0\),
because a finite map preserves the dimension of an integral curve.
Possible isolated inverse points do not contribute a hidden curve to
this divisor identity. In particular they cannot repair the following
degree calculation.

At each attaching point the normal surface branch is regular, with
inverse curve parameter \(u\). The pulled-back section is exactly
\(u^r\) or \(u^s\) times a unit. Any nonunit remaining factor would have
a height-one zero in this two-dimensional regular local ring and hence
would introduce another divisor component, contrary to sole support.
Since \(u\) has order one on the line, the restriction of \(G_b\) has
order exactly \(r\), respectively \(s\), at all three of its attaching
points.

The restriction to a line cannot be identically zero, since this would
give additional intersection support downstairs. It is a section of
\(\mathcal O_{\mathbf P^1}(b)\), with no zeros off its three intersections
with \(C_0\). One line of each label therefore already gives
\[
b=3r,\qquad b=3s.
\]
On the normalization, \(H^2=6\) and
\(H\cdot\Gamma_\pm=4\), by the finite birational projection formula and
generic degree-one maps to the degree-four curve. Intersecting the
pulled-back Cartier divisor with \(H\) gives
\[
6b=4(r+s).
\]
The identities contradict each other for every \(b>0\).
This step does not assume that the two branch orders are equal;
their equality is a consequence of the two independently counted lines.
It also avoids relying on any unproved uniform contact cutoff.

## Residual consequence checked

For a proper containing pair with generic branch orders \(r,s\), the
local orders of a nonzero line restriction are at least \(r\) or \(s\).
Additional residual zeros can only increase them. If \(r+s>2b/3\),
one order exceeds \(b/3\); both lines of that label must consequently
be contained in \(V(G_b)\). They are two distinct genuine residual
components downstairs. This verifies the proposal's additional
residual-support statement without asserting a classification of the
full residual scheme.

## Exact controls and limits

The independently assembled control is
[stci_mixed_weight_lines_audit_2026_10_30.m2](../computations/stci_mixed_weight_lines_audit_2026_10_30.m2),
with [saved output](../computations/stci_mixed_weight_lines_audit_2026_10_30.txt).
It checks the quadric restriction, both normal tangent factors, the
discriminant, all four line identities, and simplicity of their
intersection parameters. Its final marker is
AUDIT_LINE_IDENTITIES_PASS. These controls substantiate the polynomial
identities; the normalization and divisor argument was independently
reconstructed above.

The result covers the stated two-parameter mixed-weight seed over an
algebraically closed characteristic-zero field, and every positive mate
degree. Integrality was taken from the already reviewed input; no
inherited proof was reopened. The boundary \(\alpha\beta=0\), other
sextics, arbitrary higher-degree carriers, and positive characteristic
are outside this audit's claim. The earlier degree-six certificate
remains valid independent evidence. No canonical record or unrestricted
STCI status is changed.
