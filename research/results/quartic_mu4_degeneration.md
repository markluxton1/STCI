---
id: STCI-R-0021
type: result
title: Four-component mu4 degeneration of the explicit quartic intersection
scope: "#scope"
statement: "#statement"
proofs:
  - name: monic flatness and two-chart scheme decomposition
    at: "research/arguments/quartic_specialization_and_symbols.md#1-what-actually-coalesces"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Four-component mu4 degeneration

## Scope

Fix \(C=C_0=[s^4:s^3t:st^3:t^4]\) and the two integral equations
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3.
\]
The family is over \(\mathbf Z\) and the fiber statements concern
geometric fibers in characteristics zero and two.

## Statement

The projective intersection \(D=V(F,G)\) is flat over \(\mathbf Z\), with
complete-intersection fibers. On \(x_0\ne0\), in coordinates
\[
u=x_1/x_0,\qquad X=x_3/x_0-u^4,\qquad Y=x_2/x_0-u^3,
\]
its chart ideal is \((X,P)\) for
\[
P=Y^4+4u^3Y^3+6u^6Y^2+4u^9Y.
\]
On \(u\ne0\) this is \(\mathbf G_m\times\mu_4\), with
\(z=1+Y/u^3\), \(z^4=1\) and \(C\) given by \(z=1\).

In characteristic zero the fiber is the reduced scheme union of the four
curves \(C_\zeta=[s^4:s^3t:\zeta st^3:t^4]\) for \(\zeta^4=1\). They meet
only at \(p_0=[1:0:0:0]\) and \(p_\infty=[0:0:0:1]\). Each pair has
intersection multiplicity three at each endpoint. Each endpoint of the union
has delta invariant eighteen, so the union has arithmetic genus thirty-three.
Relative to \(C=C_1\), the sum of contacts of the three residual quartics
with \(C\) is \(9p_0+9p_\infty\).

In characteristic two the chart ideal is \((X,Y^4)\). On \(x_3\ne0\), with
\(c=x_2/x_3\), \(A=x_0/x_3-c^4\) and \(B=x_1/x_3-c^3\), it is
\((A,B^4)\). The two charts cover the fiber. Its reduced support is \(C\),
and its generic transverse algebra is \(k(C)[Y]/(Y^4)\).

## Limitations

The four components and their contacts concern the prescribed equations.
The [arithmetic ruled four-section](quartic_arithmetic_ruled_models.md)
has its own normalization and endpoint intersection lengths.

## Review

The Phase 5 independent reviewer accepted the route for the prescribed
equations. The reviewer checked flatness of the monic projective family,
purity of the complete-intersection fibers, both endpoint charts, the
geometric decomposition and contact and delta calculations in
characteristic zero, and the characteristic-two ideals. The Macaulay2
replay also passed, including the split ideal over \(\mathbf Q(i)\).

The October 23 audit checked the monic flatness argument, the decomposition,
contact and delta calculations, and the local characteristic-two ideal.
It inspected the family certificate and its recorded successful execution
without rerunning that script during the audit. [Source review](../arguments/quartic_specialization_and_symbols.md#source-review-and-verification)
