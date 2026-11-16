---
id: STCI-R-0020
type: result
title: Characteristic-dependent conormal splitting of the fixed rational quartic
scope: "#scope"
statement: "#statement"
proofs:
  - name: two-chart quadric conormal transition
    at: "research/arguments/quartic_specialization_and_symbols.md#conormal-transition-p-009-characteristic-jump-in-the-normal-bundle-of-c_0"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Characteristic-dependent conormal splitting

## Scope

Let \(k\) be any field, \(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\),
\(Q=V(x_0x_3-x_1x_2)\) and \(E=\mathcal I_C/\mathcal I_C^2\).
All line bundle degrees below are on \(C\simeq\mathbf P^1_k\).

## Statement

The quadric conormal sequence is
\[
0\longrightarrow\mathcal O(-8)\longrightarrow E
 \longrightarrow\mathcal O(-6)\longrightarrow 0.
\]
In the marked two-chart frames of the proof its extension class is
represented by \(-2u^{-1}\) in \(H^1(\mathbf P^1,\mathcal O(-2))\), with
\(u=t/s\) on the first chart. In particular,
\[
E\simeq
\begin{cases}
\mathcal O(-7)^{\oplus2}, & \operatorname{char}k\ne2,\\
\mathcal O(-8)\oplus\mathcal O(-6), & \operatorname{char}k=2.
\end{cases}
\]
The split \(\mathcal O(-8)\) factor in characteristic two is the
quadric conormal line.

## Limitations

The statement concerns this fixed embedding. The
[homogeneous Euler/Jacobian argument](../arguments/quartic_specialization_and_symbols.md#an-independent-homogeneous-eulerjacobian-proof)
provides a second proof of the splitting in characteristic zero.
An exclusion of global degree-\((4,4)\) presentations requires additional
equation and intersection geometry.

## Review

The two-chart transition in A-0004 represents the extension by -2u^{-1} in H^1(O(-2)). It is nonzero when 2 is invertible, yielding the balanced splitting; in characteristic two it vanishes and the quadric conormal is a direct summand.
