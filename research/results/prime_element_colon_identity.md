---
id: STCI-R-0041
type: result
title: Prime-element colon identity and its exact sequence
scope: "#scope"
statement: "#statement"
proofs:
  - name: prime-cancellation
    at: "#proof"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Prime-element colon identity and its exact sequence

## Scope

Let \(R\) be a commutative integral domain, \(q\) a nonzero prime element,
\(a,b\in R\) with \(q\nmid ab\), and \(r\ge2\) an integer. Put
\(I=(q^r,bq,ab)\). No grading, field, Noetherian, or characteristic
hypothesis is needed for the identity. A numerical length calculation further
requires that the terms in the exact sequence have finite length over a
specified local ring.

## Statement

One has
\[
I:q=(q^{r-1},b),\qquad I+(q)=(q,ab),
\]
and the short exact sequence
\[
0\longrightarrow R/(q^{r-1},b)
 \xrightarrow{\,q\,}R/I
 \longrightarrow R/(q,ab)\longrightarrow0.
\]
When its terms have finite length, their lengths add. The identity therefore
applies to polynomial rings and to formal power series domains under the same
prime-element and divisibility hypotheses.

## Proof

If \(qf=q^ru+bqv+abw\), primality of \((q)\) and \(q\nmid ab\) give
\(w=qz\). Cancel the nonzero element \(q\) in the domain to obtain
\(f=q^{r-1}u+bv+abz\in(q^{r-1},b)\). Conversely multiplication by \(q\)
takes both generators \(q^{r-1},b\) into \(I\), proving the colon equality.
The sum equality is immediate. The multiplication map has kernel exactly the
colon ideal modulo which its source is taken, its image is \((I+(q))/I\),
and its cokernel is \(R/(I+(q))\). This proves exactness. Additivity of finite
module length gives the numerical assertion.

## Evidence and application

This isolates the prime-cancellation step used in
[R-0045's homogeneous divisor-cycle argument](colon_divisor_cycle.md) and its
[complete proof](../arguments/torus_sextic_residuals.md#a-colon-formula-for-divisor-cycles).
It states explicitly the general domain hypothesis actually used in that step;
the homogeneous projective cycle assertion retains its additional hypotheses.

For example, in \(k[[x,y]]\), take \(q=x\), \(a=y^2\), \(b=y^3\),
and \(r=3\). The sequence reduces the length of
\(k[[x,y]]/(x^3,xy^3,y^5)\) to the lengths of
\(k[[x,y]]/(x^2,y^3)\) and \(k[[y]]/(y^5)\), hence gives \(6+5=11\).
This is a local length statement, with no projective saturation conclusion.

## Limitations

The cancellation step requires the stated primality and nondivisibility;
an arbitrary common initial factor does not suffice. No saturation, purity,
absence of embedded points, deformation, or global two-equation realization
follows from this identity alone.

## Review

Independent reconstruction review accepted the general-domain colon proof,
the exact sequence, and the formal local application in every characteristic.
It checked the precise primality and cancellation steps and independently
counted the eleven surviving monomials in the example. This acceptance covers
the explicit scope extension; it is distinct from the source's polynomial-ring
review. No saturation or global realization assertion was accepted, and the reviewed scope does not include saturation or global realization.
