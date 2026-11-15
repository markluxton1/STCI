# Quintic h=2 rank incidence, ODE witnesses, and conductor-norm boundary

This is a necessary-incidence analysis for the **admissible nonendpoint genus-one quintic \(A_4\), \(h=2\) parameter open in characteristic zero**, not a classification of arbitrary quintic carriers or an STCI construction. It retains scheme-theoretic saturation, global witness gluing, and the distinction between rank incidence and actual conductor norm.

On the justified remaining nonendpoint \(A_4\) quintic \(h=2\) parameter open, write \(H=t^2+vst+ws^2\), \(Q=\sum_{i=0}^6q_is^{6-i}t^i\), \(j=\bar J\), and \(R=D_HQ\). The accepted closed-lane and intrinsic-contact results give the **unit ideal** \((q_5,q_6)=A\) on the localized candidate ring; this is not permission to invert either coefficient separately. The full quadratic and cubic rank incidence has 77 minors. Its saturation by \((q_5,q_6)\) equals the saturation of **twelve fixed generators**: eleven selected cubic minors and \(jM_{56}\), where \(M_{56}=q_5r_6-q_6r_5\). The identity uses pivot covers, works with nonreduced parameter rings, and does not divide by \(j\). The actual conductor norm product can be appended as a single necessary equation without splitting its factors.

On the same localized scheme, the cubic rank condition is equivalently the existence of uniquely determined, locally gluing witnesses \(d,u\) for
\[
h\(z\)q'\(z\)=(dz+u)q\(z\),\quad
E_i=w(i+1)q_{i+1}+(vi-u)q_i+(i-1-d)q_{i-1}=0
\quad\(0\le i\le7\).
\]
The equations imply **as ideal memberships**, not just at closed points, \((d-5)(d-6)=0\) and \(j(d-6)=0\). The \(d=5\) branch retains simple intrinsic-\(A_4\) infinity contact; \(d=6\) has no infinity root. Neither is discarded.

Geometrically, the ODE measures invariance of the zero divisor of q under the polynomial vector field `h\(z\) d/dz`, with the right-hand affine factor recording the chosen line-bundle lift and infinity weight. At a root x of q of multiplicity m, write `q=(z-x)^m r`, r\(x\)≠0. The leading term of hq′ is `m h\(x\) r\(x\)(z-x)^(m-1)`, whereas `(dz+u)q` has order at least m. In characteristic zero this forces h\(x\)=0. Thus the derivative equation encodes support at the actual root directions, rather than an unrelated coefficient rank. Repeated roots of h and the prescribed infinity support still need their exact coefficient equations; this interpretation does not replace them. In characteristic p a multiplicity divisible by p makes the displayed leading coefficient vanish, so this support argument does not extend without a separability or multiplicity hypothesis.

There is a single derived spectral polynomial on this entire scheme. Put \(\Delta=v^2-4w\), \(\eta=dv-2u\),
\[
P_6\(X\)=X\(X^2-4\Delta\)\(X^2-16\Delta\)\(X^2-36\Delta\),\qquad
P_5\(X\)=\(X^2-\Delta\)\(X^2-9\Delta\)\(X^2-25\Delta\).
\]
Then \((d-5)P_6\(\eta\)+(6-d)P_5\(\eta\)\) belongs to the same ODE ideal. The proof uses the two complementary idempotents \(d-5\) and \(6-d\) and Cayley–Hamilton on the sixth and fifth symmetric powers, without radicalizing, inverting a discriminant, or choosing roots. This is a computational compression, **not a unit-ideal certificate**. The subsequent whole-\(h=2\) global saturation prospect stopped at its memory guard and supplied no mathematical emptiness result; that resource-limit history is not part of the theorem. [Twelve generators](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit), [ODE equivalence](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-automatic-open-ode-independent-audit), [spectral identity](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit).


The **global** monic necessary incidence has seventeen equations in nine variables on the original-parameter open `delta E Delta1!=0`. It retains the inverse-map boundary `Delta K=0`. Saturating by `Delta K` treats only a smaller chart and cannot settle the global incidence. The [global monic proof](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence) states this boundary exactly. The [degree-five j=0 reduction](../../arguments/carriers/quintic_toric_center_incidence.md#quintic-h2-the-degree-five-necessary-incidence-and-its-open-boundary) remains unresolved: both proposed exclusions mistake a fixed simple A4 zero at source infinity for one at source zero, so they do not justify their pure-power specialization. The later verifier additionally divides the unreversed determinant polynomial instead of the actual source conductor. Replaying its resultants cannot repair this reduction gap. The degree-six j!=0 branch and full conductor-power descent remain open. Neither the ODE reduction nor the spectral accelerator resolves them.


