---
id: STCI-R-0060
type: result
title: A degree-four initial equation invisible in the filtered equation module
scope: "#scope"
statement: "#statement"
proofs:
  - name: length-five algebra and explicit cancellation
    at: "research/arguments/filtered_equation_comparison.md#a-minimal-initial-equation-erased-by-the-comparison"
    using: [STCI-R-0030]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# A degree-four initial equation invisible in the filtered equation module

## Scope

Over a field \(k\) of characteristic zero, take \(R=k[x,y]_{(x,y)}\),
\(I=(x,y)\), and the two integral polynomial hypersurfaces with equations
\[
f=x^2+y^3,\qquad g=xy+x^3+y^3.
\]
Use the full \(I\)-initial ideals of \(J=(f,g)\) and \(IJ\), and the
comparison of [R-0030](local_filtration_comparison_defect.md). One may also
adjoin a free parameter \(t\) and mark the smooth \(t\)-axis.

## Statement

The equations form a regular sequence. The transverse quotient has
length five, with basis \(1,x,y,y^2,y^3\) and relations
\(x^2=xy=-y^3\), \(y^4=0\). With \(X,Y\) the degree-one normal variables,
\[
H=(X^2,XY,Y^4),\qquad
Q_4=kY^4=\Delta_4,\qquad
F^2(J/IJ)=k^2,\quad F^3(J/IJ)=0 .
\]
In particular \(Q_4\) is nonzero while
\(\operatorname{gr}_F^4(J/IJ)=0\). The initial equation \(Y^4\) comes from
a combination of \(f,g\) with both coefficients in \(I\). The first higher
differential in the Koszul complex with generator weights two sends the
initial syzygy \(Y e_f-X e_g\) to \(Y^4\bmod(X^2,XY)\).

After adjoining \(t\), the construction is a local complete intersection
supported on the smooth marked axis, and \(\Delta_4\) is still nonzero at
its generic point.

## Limitations

This is a local characteristic-zero counterexample. Its defect after
adjoining \(t\) has positive generic rank, so it leaves the generically
defect-free punctual question open. It gives no homogeneous global pair
for the fixed projective quartic.

## Review

The Phase 5 nonauthor reviewer accepted the local counterexample using
R-0030. The review reconstructed irreducibility and regularity, the
unit elimination and associative model, the colength argument for the
full initial ideal, and the order of the lifted Koszul syzygy. All six
checks in the finite arithmetic verifier passed on replay.

The October 23 lifting audit checked irreducibility, the regular sequence,
the associative five-dimensional quotient, the cancellation with
coefficients in \(I\), the independence of the two quadratic symbols and
the indicated filtered Koszul differential. The arithmetic check covers the
explicit identity, algebra model and filtration dimensions. The written
proof gives irreducibility and the reasoning that the initial ideal is full.
[October 23 review](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#higher-generator-counterexample) ·
[Finite arithmetic check](../computations/verify_ideal_filtration_counterexamples_2026_10_23.py)
