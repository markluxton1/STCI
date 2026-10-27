# 1. The problem and fixed curve

Let \(k\) be algebraically closed of characteristic zero and let
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
We seek homogeneous forms \(F,G\) such that \(V_+(F,G)_{\mathrm{red}}=C_0\). We may study integral factors separately, but must preserve the factor-reduction hypotheses when doing so.

The curve has degree four, genus zero, and unique smooth containing quadric \(Q=V(x_0x_3-x_1x_2)\). Its normal bundle is \(\mathcal O_{\mathbf P^1}(7)^{\oplus2}\). These are fixed inputs, not calculations to redo.

For a proper intersection of degrees \(d,e\) supported set-theoretically on \(C_0\), Bézout gives generic intersection length \(de/4\). More generally, when other curves occur, the cycle is \([V(F,G)]=m[C_0]+R\) and \(de=4m+\deg R\); thus \(m\) need not equal \(de/4\). If \(r,s\) are generic normal orders, their initial forms govern the first blowup but **do not in general determine** the full intersection multiplicity. See [Chapter 2](02-two-surfaces.md) and [residual intersections](residual_intersections_and_jets.md).

**Established boundary:** integral quartic carriers have no mate in characteristic zero, [STCI-R-0001](../results/quartic_carrier_exclusion.md). Together with separately audited lower-degree and factor arguments, hypothetical defining degrees are at least five. The unrestricted STCI question is still open.

Next: [simultaneous surface geometry](02-two-surfaces.md).
