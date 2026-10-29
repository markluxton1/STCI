# Independent audit of the mixed-weight sextic contact incidence

October 29, 2026. Reviewer: `contact_theory`, a separate agent from
`mixed_contact`. Outcome: **PASS for the exact family and degree stated
below**. The independent verifier completed with its final marker.
This is review evidence for a provisional contribution, not canonical
promotion and not an unrestricted STCI theorem.

## Claim reconstructed

Over an algebraically closed field of characteristic zero, let
\[
q=x_0x_3-x_1x_2,\quad c_0=x_1^3-x_0^2x_2,\quad
c_2=x_2^3-x_1x_3^2,
\]
and let \(F=q^3+\alpha c_0^2+\beta c_2^2\), with
\(\alpha\beta\ne0\). Every member is integral. For every proper
intersection with an actual homogeneous sextic \(G\), its generic
intersection length along \(C_0\) is at most eight. Hence the required
\((6,6)\) sole-support incidence (generic length nine) is empty, and
\(\deg R=36-4\ell_C\ge4\).

The calculation controls the complete 84-dimensional ambient sextic
space; its coefficients are scalars in the base field. It does not
replace that source with arbitrary coefficients in \(k(C_0)\).

## Independent reconstruction and scope checks

The curve-preserving torus substitution
\(\tau_t=(x_0,tx_1,t^3x_2,t^4x_3)\) gives weights 4, 3, 9 for
\(q,c_0,c_2\). Choosing \(t^{12}=-\alpha/\beta\) and dividing by
\(\beta t^{18}\) puts the carrier in the form
\[
F_k=kq^3+c_2^2-c_0^2,\qquad
k=1/(\beta t^6),\qquad k^2=-1/(\alpha\beta)\ne0.
\]
A further substitution with \(t^6=-1\) sends \(F_k\) to
\(-F_{-k}\) and interchanges the two tangent branches. Thus a uniform
calculation on one branch for every nonzero \(k\) controls both branches;
there is no assumption of equal branch contact.

On \(x_0=1\), use the curve coordinate \(t=x_1\), the normal coordinate
\(q\), and \(a=c_0\). Then
\[
x_2=t^3-a,\qquad x_3=q+t x_2.
\]
For the branch whose tangent has \(c_2=a\),
\(a_1=-2t^5/(t^6+1)\). The coefficient of \(q\) in
\(\partial F_k/\partial a\) is \(4t^5\). Consequently its unique
formal solution through degree four is reconstructed recursively by
\[
a_n=-\frac{[q^{n+1}]F_k(q,a_{<n})}{4t^5},\qquad 2\le n\le4.
\]
The independent verifier uses this variable \(a\), whereas the proposal
uses \(v=-a\); their opposite correction signs agree under that change
of variable. The residual equation is checked modulo \(q^6\).

The two branches are smooth and transverse over \(k(C_0)\). In
particular their contact orders may be different. For a proper mate,
the transverse intersection length is the sum of its two branch orders.
A total at least nine would force one branch order at least five. The
certificate below proves that branch order at least five forces a
sextic to be a scalar multiple of \(F_k\), violating properness.
It therefore avoids the invalid use of a nonsplit-node bound for this
split node.

The same one-dimensional branch kernel also proves integrality. If
\(F_k\) factored, a proper factor \(H\) of degree at most five would
vanish identically on the chosen branch. Then
\(H\cdot S_{6-\deg H}\), of dimension at least four, would lie in that
kernel. This contradicts its dimension one. This argument also handles
factors whose other components avoid the generic point of \(C_0\).

## Exact family certificate

The independent script
[stci_mixed_contact_audit_2026_10_29.m2](../computations/stci_mixed_contact_audit_2026_10_29.m2)
reconstructs the formal branch from scratch. It evaluates the curve
coordinate in the two reduced finite algebras
\(\mathbf Q[k,t]/(t^{18}-s)\), for \(s=1,8\). These are sample points
of the curve coordinate, **not samples of the parameter \(k\)**.
Both \(t\) and \(t^6+1\) are invertible there, with
\[
(t^6+1)^{-1}=(t^{12}-t^6+1)/(s+1),\qquad t^{-5}=t^{13}/s.
\]
Vanishing at the generic point implies vanishing in these algebras.
Extracting coefficients of \(q^0,\ldots,q^4\) and
\(t^0,\ldots,t^{17}\) gives an exact \(90\times84\) matrix over
\(\mathbf Q[k]\) for each \(s\).

The residual \(\mu_6\) action preserves both the carrier and the chosen
branch. The source splits by
\(e_1+3e_2+4e_3\pmod6\), with column counts
\((16,13,14,14,14,13)\). A row of normal order \(j\) and curve
coefficient \(t^i\) belongs to weight \(i+4j\pmod6\). The script
computes the corresponding exact cokernel presentations.

For weights 1 through 5 at \(s=1\), all torsion is supported at
\(k=0\), so every such block is injective for every nonzero parameter.
The weight-zero block has generic kernel dimension one and residual
torsion supported at \(k=0\) or roots of a degree-seven polynomial.
The \(s=8\) block gives a second degree-seven polynomial. Their gcd is
one over \(\mathbf Q[k]\). The script checks this without relying on
hard-coded factors by saturating the sum of the two relevant Fitting
ideals by \((k)\) and asserting that it is the unit ideal. Thus no
nonzero parameter is discarded by inversion of a convenient minor.
The common kernel is exactly the known carrier vector \(F_k\).

Reproduction command:

```sh
M2 --script research/computations/stci_mixed_contact_audit_2026_10_29.m2
```

The [saved output](../computations/stci_mixed_contact_audit_2026_10_29.txt)
contains the matrix shapes, all six presentations, the second
weight-zero presentation, and final marker
`AUDIT_ALL_NONZERO_PARAMETERS_PASS`.

## Limits and frontier effect

This closes the required length-nine incidence for this entire
mixed-weight two-parameter family at mate degree six. The bound eight
is the bound established here; attainment of eight is not asserted.
The calculation does not control sextic mates of every sextic carrier,
mates of degree greater than six on these carriers, or the two-non-binomial
class in positive characteristic. No new canonical result/question file
is introduced.
