---
id: STCI-R-0082
type: result
title: Arrangement Hilbert strata, endpoint planarity and separate orders
scope: "#scope"
statement: "#statement"
proofs:
  - name: endpoint ranks, formal planarity and exceptional valuations
    at: "research/arguments/torus/arrangement_strata_and_orders.md#arrangement-strata-endpoint-planarity-and-separate-vanishing-orders"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Arrangement Hilbert strata, endpoint planarity and separate orders

## Scope

Distinct translates \(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\) over an
algebraically closed field of arbitrary characteristic, with reduced union.
The flat-family assertion uses reduced locally closed configuration strata;
the separate-order dictionary is fiberwise on the existing smooth separated
blowup model.

## Statement

1. On a reduced configuration stratum with constant reduced-union Hilbert
   polynomial, the finite full endpoint-rank vector is locally constant.
   Forming the union anew there gives a flat family whose ideal intersection
   commutes with every further base change.
2. If both endpoint germs of an arrangement of at least five components lie
   on smooth formal surfaces, every component lies on one common smooth
   quadric. Thus a reduced scheme-theoretic CI arrangement with at least five
   components must be nonplanar at an endpoint. For four components, reduced
   \((4,4)\) CI is equivalent to planarity at both endpoints and absence of
   a common quadric.
3. On the separated model \(g:\widehat W_Z\to\mathbf P^3\), for all
   \(n_i\ge0\),
   \[
   g_*O(-\sum_i n_i\widetilde E_i)=\bigcap_i I_{C_i}^{n_i}.
   \]
   Projection formula gives the corresponding degree-\(d\) section dictionary.

[Complete proofs](../arguments/torus/arrangement_strata_and_orders.md).

## Limitations

Constant total endpoint defect forces local constancy of every rank by
semicontinuity; a finer rank stratification is optional for this flatness
argument. This does not identify the re-formed union with restriction of
the ambient universal union, or prove Rees base change. Endpoint planarity
is intrinsic, but the quadric-generator exclusion uses reduced CI structure
and cannot be applied to arbitrary repeated cycles. The separate-order
identity concerns intersections of individual smooth-curve powers, not
powers of the singular union ideal or joint intersection lengths.

## Review

On November 23, 2026, a bounded generalizations investigator supplied the
three candidate extensions. A distinct Sol/xhigh technical reviewer
independently reconstructed them and supplied the four-component corollary;
the generalizations lead independently checked the final written account,
including that corollary. The review used the exact endpoint and separated
model proofs, without claiming a general Rees specialization theorem or
reproof of nonreduced Chow realization. No numerical computation supports
or substitutes for these arguments.
