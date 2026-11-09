---
id: STCI-R-0068
type: result
title: Punctual comparison defects of arbitrary degree and length with integral carriers
scope: "#scope"
statement: "#statement"
proofs:
  - name: filtered syzygy lifting and actual fiber calculation
    at: "research/arguments/punctual_comparison_defects.md#arbitrary-punctual-degree-and-length-with-integral-carriers"
    using: [STCI-R-0030, STCI-R-0065]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---

# Punctual comparison defects of arbitrary degree and length with integral carriers

## Scope

Let \(k\) be a field of characteristic zero. The marked smooth curve is the
\(t\)-axis \(x=y=0\) in \(\mathbf A^3_k\), with marked point the origin.
Work in the polynomial local ring \(k[t,x,y]_{(t,x,y)}\) and its completion
\(R=B[[x,y]]\), where \(B=k[[t]]\) and \(I=(x,y)\).
The completed formulas below use \(B\) as coefficient ring. Their relative
initial ideals and comparison modules also hold in the polynomial local
ring with coefficient ring \(k[t]_{(t)}\). The finite free algebra and its
generic and closed fibers are taken over the completed base \(B\).

## Statement

For every pair of integers \(r\ge1\), \(m\ge2\), set \(a=t^r\) and take
\[
f=ax+x^2+y^m,\qquad
g=ay+xy+y^m+x^{m+1},\qquad J=(f,g)\subset I.
\]
The equations define distinct integral hypersurfaces in \(\mathbf A^3_k\)
and form a regular sequence in both local rings of the scope.

Write \(S=B[X,Y]=\operatorname{gr}_I R\), \(S_+=(X,Y)\),
\(h=xg-yf=xy^m-y^{m+1}+x^{m+2}\) and \(q=XY^m-Y^{m+1}\). The full normal
initial ideals are
\[
H=\operatorname{in}_I(J)=(aX,aY,q),\qquad
T=\operatorname{in}_I(IJ)=(aX^2,aXY,aY^2,q).
\]
The actual equation module \(D=J/IJ\) is free on the classes of \(f,g\).
Its conormal map \(D\to I/I^2\) is \(\operatorname{diag}(a,a)\),
so \(F^1D=D\) and \(F^nD=0\) for \(n\ge2\) in the filtration
\(F^nD=((J\cap I^n)+IJ)/IJ\). In particular the generic conormal rank is two
and the closed-point rank is zero. The module \(Q=H/S_+H\) has
\(Q_1\simeq B^2\), \(Q_{m+1}\simeq B/(t^r)\), and all other pieces zero.
The comparison defect \(\Delta=T/S_+H\) is concentrated in degree \(m+1\)
and generated there by the class of \(q\), with annihilator \((t^r)\).
It vanishes generically and has length \(r\) at the origin. Thus every
degree \(d\ge3\) and length \(r\ge1\) occur independently. Degree three
attains the lower bound for the relative comparison in
[R-0065](normal_koszul_comparison_defect.md).

The actual closed equations generate
\(J_0=(x^2+y^m,xy+y^m+x^{m+1})\subset k[[x,y]]\).
The algebra \(k[[x,y]]/J_0\) has basis \(1,x,y,\ldots,y^m\), with
\(x^2=xy=-y^m\), \(x^3=0\), and \(y^{m+1}=0\). Its full closed normal
initial ideal and comparison defect are
\[
\begin{array}{c|c|c}
 & H_0^{\rm act} & \Delta_0^{\rm act} \\ \hline
 m\ge3 & (X^2,XY,Y^{m+1}) & k\text{ in degree }m+1 \\
 m=2 & (X^2+Y^2,XY+Y^2) & 0 .
\end{array}
\]
The second ideal is a regular quadratic pair. The full actual initial
ideal of \((x,y)J_0\) is \((X^3,X^2Y,XY^2,Y^{m+1})\) for \(m\ge3\)
and \((X,Y)H_0^{\rm act}\) for \(m=2\).
The coefficient-specialization
images of both \(H\) and \(T\) in \(k[X,Y]\) are \((q)\), so
\((S/H)\otimes_B k=k[X,Y]/(q)\) has infinite length. The tensor
\(\Delta\otimes_B k\) is a copy of \(k\) in degree \(m+1\) for every
\(m\). Its natural specialization map to \(\Delta_0^{\rm act}\) is
an isomorphism for \(m\ge3\) and zero for \(m=2\).

The actual completed algebra \(M=R/J\) is finite free of rank \(m+2\)
over \(B\). Write \(K=k((t))\) and let \(\mathfrak p=(x,y)(M\otimes_B K)\)
be the marked generic maximal ideal. The localization
\((M\otimes_B K)_{\mathfrak p}\) is \(K\), as is the quotient by the two
equations in the completed marked transverse ring \(K[[x,y]]\).
The full generic algebra \(M\otimes_B K\) is the product of this
length-one marked factor and an Artinian \(K\)-algebra of dimension
\(m+1\) supported off the marked generic point. Also \(H\otimes_B K=(X,Y)\)
inside \(K[X,Y]\), so the generic normal algebra along the marked
component has length one.

[Complete proof in A-0010](../arguments/punctual_comparison_defects.md#arbitrary-punctual-degree-and-length-with-integral-carriers)

## Limitations

The residual dimension is a property of the actual finite algebra.
The example has a proper marked component and leaves open the existence
of a nonzero punctual relative defect with \(\sqrt J=I\) and
\(\Delta_K=0\). The marked line calculation concerns local equations in
characteristic zero. It gives no global equations for the fixed quartic.

## Review

The Phase 5 nonauthor reviewer `review_proofs` accepted the filtered syzygy and actual
fiber route with R-0030 and R-0065 for every \(m\ge2\) and \(r\ge1\) in
characteristic zero. They checked integrality of the polynomial carriers,
generation of all symbol syzygies over the possibly nonreduced coefficient
quotient, both full relative initial ideals, and the exact comparison.
They reconstructed the actual closed basis, both full slice initials,
the separate \(m=2\) quadratic calculation and the specialization map.
They also checked finiteness and freeness of the actual algebra and its
generic Artinian decomposition. This is a symbolic review of the
all-parameter proof. The finite replays are recorded separately in A-0010.

The October 24 independent reconstruction checked all symbol syzygies over
the nonreduced coefficient quotient, their exact lifts, the conormal rank,
the separate \(m=2\) closed fiber, and the actual finite-flat rank and
residual support. The source records a primary-agent irreducibility check
and a separate finite Rees-saturation check of the punctual family for
three thickness parameters. The October 26 local audit retained the
distinction between the residual family and the open sole-support problem.
[October 24 review](https://github.com/markluxton1/STCI/blob/737bfe4eacb93dfc1273228773695e1b55c72028/research/notes/2026-10-24-delta-singular-locus-review.md#L46) ·
[October 26 audit](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#local-filtration-audit-and-scope-boundary--2026-10-26)
