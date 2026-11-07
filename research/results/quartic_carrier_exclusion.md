---
id: STCI-R-0001
title: Complete exclusion of integral quartic carriers of the fixed rational quartic
kind: theorem
scope:
  characteristic: "algebraically closed fields of characteristic zero"
  curve: "C0 = [s^4:s^3t:st^3:t^4] in P3, and its projective equivalents"
  hypotheses:
    - "X is an integral degree-four hypersurface in P3 containing C0"
    - "G is any homogeneous form of positive degree"
statement: "For every such X and G, the set V(X,G) is not C0."
dependencies: []
evidence:
  - "research/synthesis/quartic_carrier_proof.md"
  - "research/supplements/GENUS_TWO_AMBIENT_CONIC_MODEL_PROOF.md"
  - "research/supplements/GENUS_TWO_BISECTION_PROOF.md"
  - "research/supplements/GENUS_TWO_NONENDPOINT_PROOF.md"
  - "research/supplements/GENUS_TWO_ENDPOINT_PROOF.md"
  - "research/supplements/GENUS_TWO_ENDPOINT_LOCAL_CORRECTIONS.md"
independent_audits:
  - "research/synthesis/quartic_carrier_proof.md#9-review-state"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not settle whether C0 is an STCI using surfaces of degrees at least five."
  - "Does not apply to every smooth rational quartic embedding."
  - "Does not resolve common-quartic local-cohomology ancestor incidence."
---

# Complete quartic-carrier exclusion for the fixed C0

Over every algebraically closed field of characteristic zero, for every
integral quartic surface \(X\subset\mathbf P^3\) containing
\(C_0=[s^4:s^3t:st^3:t^4]\), and every homogeneous form \(G\) of
positive degree,
\[
V(X,G)_{\mathrm{red}}\ne C_0.
\]
The theorem is invariant under projective equivalence of this embedding.
There is no restriction on normality, normalization singularities,
conductor scheme, mate degree, or generic normal order of the mate.

The [complete current proof](../synthesis/quartic_carrier_proof.md) owns the
shared reductions, normal-case argument and exhaustive assembly. For a
nonnormal carrier, normalized sectional genus is zero, one or two; the
proof derives rationality, generic regularity and full inverse support
before using the specialized normalization geometry. Genus two has exactly
the bisection and section correction strata, and the latter has distinct-
contact or triple-contact trisecants. All degree and endpoint charts are
included. The normal case retains exact necessary graph enumerations,
whole correction-column denominators, actual ideal vanishing and the
independent low-degree inputs; it is not a consequence of a narrower
quartic-pair theorem.

The current proof links every specialized full argument and necessary exact
computation, and records the scope of reused independent review. The
original accepted assembly dates from October11; consolidation changes its
proof organization, not its quantifiers or mathematical conclusions.

## Consequences and boundaries

If \(V(F,G)_{\mathrm{red}}=C_0\), coprimality and purity imply that each
irreducible factor of either equation is itself a carrier with the other
as mate. The plane, unique-quadric and classical cubic exclusions, followed
by this theorem, force every irreducible factor to have degree at least
five. In particular both defining degrees are at least five, even for
reducible or repeated equations. The [factor argument and cubic literature
input](../synthesis/05-exclusions.md#52-factors-and-the-degree-bound) give the
precise reduction.

The unrestricted characteristic-zero existence question remains **open**.
This theorem does not cover every smooth rational quartic embedding,
compute common-quartic ancestor incidence, or exclude arbitrary higher-
degree carriers and entirely thick pairs.

In **every characteristic \(p>0\)**, the fixed \(C_0\) is an STCI using
a quartic carrier. The [actual construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
and [mechanism-by-mechanism boundary](../synthesis/quartic_carrier_proof.md#8-what-changes-in-positive-characteristic)
explain why the characteristic-zero proof cannot be transported unchanged.

## Earlier partial mechanisms

The theorem closes the earlier quartic-*mate* open labels in
[normal carriers](normal_carriers.md), [order-one structures](order_one.md),
[primitive e2 incidence](quartic_e2.md) and MF6. Their distinct normal,
conductor, primitive, local-cohomology and ancestor calculations remain
useful in their stated scopes. A no-mate theorem does not prove a separate
common-ancestor incidence empty.
