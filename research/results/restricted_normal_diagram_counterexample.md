---
id: STCI-R-0061
type: result
title: Identical graded embedding diagrams after restriction to the reduced curve
scope: "#scope"
statement: "#statement"
proofs:
  - name: local binomial calculation
    at: "#proof"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---

# Identical graded embedding diagrams after restriction to the reduced curve

## Scope

Let \(k\) be a characteristic-zero field, \(R=k[t,u,v]_{(t,u,v)}\),
\(I=(u,v)\), \(P=\operatorname{Spec}R\), and
\(C=\operatorname{Spec}(R/I)\). Write \(D_0=R/I=k[t]_{(t)}\).
This is a local comparison along a smooth curve in a smooth threefold.

For each embedding \(W\hookrightarrow W'\) with ideal \(L\subset Q=\mathcal O(W')\),
take \(\operatorname{gr}_L Q\), based over its degree-zero ring \(Q/L\).
Restriction to \(C\) means tensoring this graded algebra over \(Q/L\) with
\(D_0\). In each chain with ideals \(L\subset M\subset Q\), the arrows
are the degree-preserving maps
\[
\operatorname{gr}_L Q \longrightarrow \operatorname{gr}_M Q
\longrightarrow \operatorname{gr}_{M/L}(Q/L)
\]
from ideal inclusion and ambient quotient. The first is taken after the
appropriate base change on degree zero when comparing over the smaller
scheme. On restriction of all objects to \(C\), these maps are maps of
graded \(D_0\)-algebras.

## Statement

Take
\[
f_0=u^2+v^5,\qquad f_1=u^2+v^3,\qquad g=v^4+u^5.
\]
For \(i=0,1\), let \(A_i=(f_i)\), \(B=(g)\), \(J_i=A_i+B\),
\(X_i=V(A_i)\), \(Y=V(B)\), and \(Z_i=V(J_i)\) in \(P\).
The hypersurfaces \(X_0,X_1,Y\) are integral, each pair \((f_i,g)\)
is a regular sequence, and both intersections have reduced scheme \(C\).
In \(R\),
\[
J_0=(u^2,v^4),\qquad J_1=(u^2+v^3,v^4).
\]
The nine graded algebras of the embeddings among \(C,Z_i,X_i,Y,P\), with
their maps, agree after restriction to \(C\). In particular, writing
\(K_i=I/J_i\), both normal graded algebras
\(\operatorname{gr}_{K_i}(R/J_i)\) are
\(D_0[U,V]/(U^2,V^4)\), where \(U,V\) are the degree-one classes of
\(u,v\). The full initial ideal \((U^2,V^4)\) in each case gives
the same minimal equation modules \(Q_2=D_0\cdot[U^2]\) and
\(Q_4=D_0\cdot[V^4]\), where brackets denote the classes in \(H/S_+H\).
The rings \(R/J_0\) and \(R/J_1\) are nevertheless
nonisomorphic as abstract rings. The first has a square-zero element outside
the square of its nilradical and the second has none.

The comparison changes if the diagram retains the original bases and
ambient degree-zero quotient maps. Over the fixed \(P\), the map
\(R\to(\operatorname{gr}_{J_i}R)_0\) then recovers the embedded ideal \(J_i\)
as its kernel. The original degree-zero base alone gives the abstract
intersection ring.

## Proof

For positive coprime \(a,b\), the binomial \(x^a+y^b\) defines an
integral hypersurface. Over an algebraic closure of \(k\), choose
\(\zeta^a=-1\) and send \(x\mapsto\zeta z^b\), \(y\mapsto z^a\).
A reduced representative modulo the monic equation in \(x\) is a sum
of terms \(c_{ij}x^iy^j\) with \(0\le i<a\). Their images have
distinct exponents \(bi+aj\), by coprimality. Thus the quotient embeds
in the polynomial ring in \(z\). Adjoining \(t\), descending to \(k\),
and localizing preserve the resulting domain assertion for each of
\(f_0,f_1,g\).

For \(f=u^2+v^r\), with \(r=5\) or \(3\),
\[
g=f(uf-2uv^r)+v^4(1+uv^{2r-4}).
\]
The parenthetical factor of \(v^4\) is a unit in \(R\). The image of
\(v\) is nonzero in the domain \(R/(f)\), as is seen from the
binomial parametrization. Hence \((f,g)\) is regular and generates
\((f,v^4)\). Reducing \(v^5\) modulo \(v^4\) gives the claimed
simplification of \(J_0\). Each simplified ideal has radical \(I\).

Both quotients have the free \(D_0\)-basis
\[
1, v, v^2, v^3, u, uv, uv^2, uv^3.
\]
Indeed the quotient of \((D_0[v]/(v^4))[u]\) by the monic quadratic
\(u^2\) or \(u^2+v^3\) has this basis. The resulting ring has nilpotent
ideal \((u,v)\) and quotient \(D_0\). Thus every polynomial inverted in
forming \(R\) already has unit image in this model, so the model is
\(R/J_i\). In either model \(K_i^n\) is spanned by the basis monomials
of total degree at least \(n\). Each such monomial is in \(K_i^n\),
and reduction of monomials of degree at least \(n\) via \(u^2=0\)
or \(u^2=-v^3\), and \(v^4=0\), never lowers degree. It follows that
\(U^2,V^4\) vanish in the graded algebra and the other basis monomials
give its degreewise bases, proving the claimed graded presentation.

### The restricted algebras and maps

Write \(S=D_0[U,V]\), \(E=D_0[T_f,T_g]\),
\(E_f=D_0[T_f]\), and \(E_g=D_0[T_g]\), with all displayed variables
of degree one. The equation variables represent the original generators
\(f_i,g\) in the relevant filtrations.

| Embedding | Ideal in the actual ambient ring | Original degree-zero ring | Algebra after restriction to \(C\) |
| --- | --- | --- | --- |
| \(X_i\hookrightarrow P\) | \(A_i\subset R\) | \(R/A_i\) | \(E_f\) |
| \(Y\hookrightarrow P\) | \(B\subset R\) | \(R/B\) | \(E_g\) |
| \(Z_i\hookrightarrow P\) | \(J_i\subset R\) | \(R/J_i\) | \(E\) |
| \(C\hookrightarrow P\) | \(I\subset R\) | \(D_0\) | \(S\) |
| \(Z_i\hookrightarrow X_i\) | \(J_i/A_i\subset R/A_i\) | \(R/J_i\) | \(E_g\) |
| \(Z_i\hookrightarrow Y\) | \(J_i/B\subset R/B\) | \(R/J_i\) | \(E_f\) |
| \(C\hookrightarrow X_i\) | \(I/A_i\subset R/A_i\) | \(D_0\) | \(S/(U^2)\) |
| \(C\hookrightarrow Y\) | \(I/B\subset R/B\) | \(D_0\) | \(S/(V^4)\) |
| \(C\hookrightarrow Z_i\) | \(K_i\subset R/J_i\) | \(D_0\) | \(S/(U^2,V^4)\) |

For the principal ideals in the first, second, fifth and sixth rows,
powers of the nonzerodivisor identify each graded piece with one copy
of the original degree-zero ring. For the third row, the two generators
of a regular sequence freely generate the associated graded algebra as
a polynomial algebra over \(R/J_i\). In this case, if a degree-\(n\)
combination of the monomials \(f_i^j g^{n-j}\) lies in \(J_i^{n+1}\),
subtract a combination with coefficients in \(J_i\) to make the
relation zero. In a zero relation the coefficient of \(g^n\) belongs
to \((f_i)\), by reduction modulo \(f_i\). Absorb that term into the
coefficient of \(f_i g^{n-1}\), changing it by a multiple of \(g\).
Dividing by \(f_i\) reduces to a degree-\((n-1)\) relation and induction
puts all the original coefficients in \(J_i\). This gives the third
row after tensoring with \(D_0\).

The graded algebra for \(I\) in \(R\) is \(S\), by the monomial
basis in each degree for the \((u,v)\)-adic filtration, with localization
inducing the coefficient ring \(D_0\). Passage to \(R/A_i\) or \(R/B\)
quotients \(S\) by the full initial ideal of the corresponding
principal ideal. Because \(S\) is a domain, the leading symbol of
each nonzero multiple is the product of the two leading symbols.
Thus the full initial ideals are \((U^2)\) and \((V^4)\), respectively.
The final row follows from the basis calculation above.

The table below lists the two maps for every strict triple in the scheme
diagram. The first column is ordered from smallest to largest scheme.
An inclusion of equation variables sends each named variable to the
same variable. A projection of equation variables kills the variable
absent from the target. A quotient map on the normal variables sends
each of \(U,V\) to its class. All maps induce the identity of \(D_0\)
in degree zero.

| Triple | Map from ideal inclusion | Map from ambient quotient |
| --- | --- | --- |
| \((Z_i,X_i,P)\) | \(E_f\to E\), inclusion | \(E\to E_g\), projection |
| \((Z_i,Y,P)\) | \(E_g\to E\), inclusion | \(E\to E_f\), projection |
| \((C,X_i,P)\) | \(E_f\to S\), kills \(T_f\) | \(S\to S/(U^2)\), quotient |
| \((C,Y,P)\) | \(E_g\to S\), kills \(T_g\) | \(S\to S/(V^4)\), quotient |
| \((C,Z_i,P)\) | \(E\to S\), kills \(T_f,T_g\) | \(S\to S/(U^2,V^4)\), quotient |
| \((C,Z_i,X_i)\) | \(E_g\to S/(U^2)\), kills \(T_g\) | \(S/(U^2)\to S/(U^2,V^4)\), quotient |
| \((C,Z_i,Y)\) | \(E_f\to S/(V^4)\), kills \(T_f\) | \(S/(V^4)\to S/(U^2,V^4)\), quotient |

The first two triples send the indicated generators to their classes in
\(J_i/J_i^2\) or in the quotient by \(A_i\) or \(B\). The other
inclusion maps kill equation variables because \(f_i,g\in I^2\), also
after passing to \(R/A_i\) or \(R/B\). Ambient quotient maps act by
passing to the indicated classes. Each algebra is generated in degree
one over its degree-zero ring, so these assignments determine the maps
in all degrees and their composites. In particular the first conormal
maps from the carrier equations to the curve's conormal are zero.
The higher leading symbols of the two original equations in \(S\)
are \(U^2\) and \(V^4\) in both examples, in normal degrees two and
four respectively.

### Abstract nonisomorphism and the original bases

In \(R/J_0\), \(u^2=0\) and \(u\notin K_0^2\). In \(R/J_1\),
a square-zero element \(h\) is in the nilradical \(K_1\).
Write \(h=\alpha u+\beta v+w\), with \(w\in K_1^2\), and let
\(\gamma\) be its \(v^2\) coefficient. In the displayed basis
the \(v^2\) coefficient of \(h^2\) is \(\beta^2\), and the \(v^3\)
coefficient is \(2\beta\gamma-\alpha^2\). Indeed a product of basis
monomials contributing to those coefficients either contains no \(u\)
or contains \(u^2\), which reduces to \(-v^3\) and vanishes when
multiplied by a positive power of \(v\). Since \(D_0\) is a domain,
\(h^2=0\) forces first \(\beta=0\) and then \(\alpha=0\).
Thus \(h\in K_1^2\). A ring isomorphism preserves square-zero elements,
the nilradical, and its square, giving the abstract distinction.

In the original diagram \((\operatorname{gr}_{J_i}R)_0=R/J_i\).
Retaining its ambient map recovers \(J_i\) as the kernel, and
restriction to \(C\) changes the degree-zero ring to \(D_0\)
and the ambient map to \(R\to D_0\) with kernel \(I\).

## Limitations

This example is local along \(C\). It makes no projective realization or
set-theoretic complete intersection claim for the fixed quartic \(C_0\).
It concerns the nine ideal-power graded algebras after degree-zero
base change to \(C\). With the original bases and ambient quotient maps
over the fixed \(P\), the full diagram determines the embedded
intersection directly in degree zero.

## Review

The Phase 5 nonauthor reviewer accepted the local binomial proof after
checking the integral presentations, the unit factors and localization,
the normal filtration of the eight-element bases, the maps for all seven
strict triples and the square-zero distinction. The review checked
recovery of the embedded ideal from the original degree-zero map.
All seven finite arithmetic checks passed on replay.

The [October 23 completeness review](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#completeness-counterexample)
checked the two local integral-hypersurface presentations, the common
normal graded algebra, all nine restricted graded objects, the intrinsic
nonisomorphism, and the distinction from the full diagram retaining
the original bases and ambient maps. The
[review assignments](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#review-assignments-and-findings)
also record separate checks of the general embedding bases and higher
graded maps in the source investigation.

The [exact arithmetic script](../computations/verify_ideal_filtration_completeness_2026_10_23.py)
checks the unit identities, eight-dimensional transverse models over
\(\mathbb Q\), normal Hilbert functions, and square coefficients. The
proof above supplies integrality, the coefficient-ring and localization
arguments, and the comparison of the full restricted diagrams.
