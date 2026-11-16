---
id: STCI-R-0069
type: result
title: A supported quadruple whose equation filtration retains the torsion
scope: "#scope"
statement: "#statement"
proofs:
  - name: free supported algebra and full equation filtration
    at: "research/arguments/punctual_comparison_defects.md#a-supported-quadruple-torsion-in-q-is-not-enough"
    using: [STCI-R-0030]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---

# A supported quadruple whose equation filtration retains the torsion

## Scope

Let \(k\) be any field, \(B=k[[t]]\), \(R=B[[x,y]]\), and \(I=(x,y)\).
Use the relative comparison of [R-0030](local_filtration_comparison_defect.md)
over \(B\), with \(S=B[X,Y]\) and \(S_+=(X,Y)\).

## Statement

Put \(f=x^2\), \(g=y^2+tx\), and \(J=(f,g)\). This is a complete
intersection with \(\sqrt J=I\). Its algebra \(M=R/J\) is free over \(B\)
on \(1,x,y,xy\), with \(x^2=0\), \(y^2=-tx\), and \((I/J)^4=0\).
The same ideal is cut out by the two integral polynomial carriers
\(g,g+f\), both singular at the origin and with common first symbol \(tX\).
Their conormal map has generic rank one.

The full relative initial ideals are
\[
H=(tX,X^2,XY^2,Y^4),\qquad
T=\operatorname{in}_I(IJ)=S_+H.
\]
Write \(D=J/IJ\) and let \(e_f,e_g\) be its free equation basis.
The nonzero pieces and their comparison are
\[
\begin{array}{c|c|c|c|c}
n & F^nD & Q_n=H_n/(S_+H)_n & G_n=F^nD/F^{n+1}D &
  \text{comparison on generators}\\ \hline
1 & D & B & B & tX\mapsto [e_g]\\
2 & Be_f & B/(t) & B/(t) & X^2\mapsto [e_f]\\
3 & tBe_f & B/(t) & B/(t) & XY^2\mapsto [-t e_f]\\
4 & t^2Be_f & B & B & Y^4\mapsto [t^2e_f].
\end{array}
\]
All pieces in degrees \(n\ge5\) vanish. Each comparison is an isomorphism
and \(\Delta=0\). In particular, both torsion pieces of \(Q\) survive in
\(G\), so their contributions cancel in the DVR length formula of R-0030.

Over \(k((t))\), the actual transverse algebra is \(k((t))[y]/(y^4)\).
The actual closed ideal is \(J_0=(x^2,y^2)\) with full initial ideal
\(H_0^{\rm act}=(X^2,Y^2)\) and \(\operatorname{in}_{(x,y)}((x,y)J_0)
=(X,Y)H_0^{\rm act}\). Thus \(\Delta\otimes_B k=0\) and the actual closed
defect is also zero. The image \(\overline H\) of \(H\) in \(k[X,Y]\)
is \((X^2,XY^2,Y^4)\), giving a specialized relative normal algebra of
length six, while the actual closed normal algebra has length four.
The image of \(T\) is \((X,Y)\overline H\).

[Complete proof in A-0010](../arguments/punctual_comparison_defects.md#a-supported-quadruple-torsion-in-q-is-not-enough)

## Limitations

This is a local example along a marked line. The coexistence of torsion
in \(Q\) and sole reduced support is compatible with vanishing of
\(\Delta\). See the
[open sole-support question](../frameworks/formal-normal-geometry/open_normal_geometry.md#punctual-relative-defect-under-sole-support).

## Review

The free supported algebra and full equation filtration are retained in [A-0010](../arguments/punctual_comparison_defects.md#a-supported-quadruple-torsion-in-q-is-not-enough). Torsion in both comparison modules survives while the defect vanishes.
