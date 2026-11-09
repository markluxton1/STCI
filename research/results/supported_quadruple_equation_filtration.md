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
\(\Delta\). The existence of a nonzero punctual relative defect under sole
support and generic vanishing remains open.

## Review

The Phase 5 nonauthor reviewer `review_proofs` accepted the free supported algebra and
full equation filtration route with R-0030 over every field. They checked
the radical and free basis, both full relative initial ideals, the powers
in \(R/IJ\) and their intersections with \(J/IJ\), and the maps retaining
both torsion generators. They reconstructed the actual generic and closed
algebras and the comparison with the coefficient images of the relative
initial ideals. This review used symbolic arguments. The separate finite
replay checks the full relative initials and \(I^4\subset J\).

The October 24 review records the quadruple as a separate primary-agent
calculation from the free basis \(1,x,y,xy\), with full initial ideals
verified by Rees saturation. The review records torsion survival and
zero relative defect for this example. The normal-cone regularity audit
used this calculation as inherited evidence, and the October 26 local
audit retained its scope as a control with sole support.
[October 24 review](https://github.com/markluxton1/STCI/blob/737bfe4eacb93dfc1273228773695e1b55c72028/research/notes/2026-10-24-delta-singular-locus-review.md#L69) ·
[Normal-cone audit](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#4-next-directions-and-evidence-boundary) ·
[October 26 audit](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#local-filtration-audit-and-scope-boundary--2026-10-26)
