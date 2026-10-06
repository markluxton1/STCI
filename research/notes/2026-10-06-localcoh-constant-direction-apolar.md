# Constant directions require a prescribed common scalar divisor

Date: 2026-10-06. Status: **PROVED**, conditional on the characteristic-zero
P-010 quadratic transition class and the generic length-three reduction in
`2026-10-05-localcoh-generic-length.md`. This is a necessary second-contact
condition on quartic ancestor pairs, not a complete exclusion.

Use the balanced conormal frame \((U,V)\) of the monomial quartic and a
constant primitive first-symbol direction \(m=U+\theta V\), with
\(\ell=V\). Write the quartic symbols as \(a m,b m\), where
\(a,b\in H^0(O(9))\), and let \(D\) be their common-zero divisor.

Generic transverse multiplicity three forces their pure \(\ell^2\)
second coefficients \(f_2,g_2\) to obey \(b f_2-a g_2=0\). Hence
\(\beta=f_2/a=g_2/b\) is a rational quadratic correction to the common
surface equation. Its poles are bounded by \(D\): at any curve point the
two expressions bound the pole order by the minimum of the vanishing orders
of \(a,b\). Since the first coefficients have degree nine and second
coefficients have degree two, \(\beta\) is a meromorphic local section
of \(O(-7)\).

On chart overlaps these corrections differ by the P-010 class

\[
h_\theta=3\left(\theta^3t^{-5}-\frac12\theta^2t^{-4}
 +\frac14\theta t^{-3}-\frac18t^{-2}\right)
 \in H^1(O(-7)).
\]

Consequently this class must vanish after allowing the poles:

\[
\boxed{D\cdot h_\theta=0\quad\text{in }H^1(O(\deg D-7)).}
\]

Here multiplication by \(D\) means multiplication by a homogeneous binary
form defining that divisor. In the affine notation \(D(t)=\sum d_i t^i\),
the equation says that the coefficients of \(t^{-1},\ldots,
t^{-(6-\deg D)}\) in \(D(t)h_\theta\) vanish. This gives exact linear
conditions on its coefficients, rather than just a positive-degree bound.

For finite mixed directions \(\theta\ne0\), the multiplication maps
for divisors of degrees one and two have full column rank. A nonzero
degree-three divisor exists, and its kernel is exactly

\[
(d_0,d_1,d_2,d_3)\sim(0,2\theta,1,0).
\]

Therefore

\[
\boxed{\theta\ne0:\quad \deg D\ge3;\qquad
\deg D=3\Rightarrow D\sim st(t+2\theta s).}
\]

The boundary direction \(\theta=0\) first permits a degree-two divisor
\(D\sim t^2\). The missing direction \(m=V,\ell=U\), whose class is
\(3t^{-5}\), first permits \(D\sim s^2\). Both pure directions are
already excluded by the stronger contact theorem in
`2026-10-05-localcoh-pure-direction-audit.md`.

The exact companion `verify_localcoh_constant_direction_apolar.py` checks
the ranks using nonzero minors and the exceptional axis kernels. In
particular its degree-two mixed minor is \(-\theta^4/32\), so the proof
does not confuse generic rank with an assertion at \(\theta=0\).
It also checks that the degree-four scalar divisor of the explicit mixed
contact pair in `verify_localcoh_direction_contact_survivor.py` kills
\(h_{1/2}\). That example shows that this pole-bound condition can be
satisfied by ambient-coprime contact pairs.

The remaining obligation is target-specific: even after this formal
second-contact condition, the highest coefficient forced by
\(F\alpha=u,G\alpha=v\) must be a regular global section of \(O(7)\),
and every lower principal part must agree. The explicit mixed pair fails
that regularity condition, but no exclusion of all mixed constant directions
is claimed here.
