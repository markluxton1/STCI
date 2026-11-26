---
id: STCI-I-0007
type: investigation
title: Trace residues and simultaneous coordinate projections
status: complete
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0010]
    to: [STCI-I-0007]
    at: "#purpose"
---
# Trace residues and simultaneous coordinate projections

## Scope

Work over an algebraically closed field of characteristic zero. Let
\(Y=V(F_a,G_b)\) be a proper homogeneous complete intersection (CI) with
entire fundamental cycle \(\sum_i n_i[C_{u_i,v_i}]\), where
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\), (u,v
e 0), and
\(m=\sum_i n_i=ab/4\). Write coordinates \([z:x:y:w]\),
\(q_i=u_i/v_i\), and \(M_1=\sum_i n_iq_i\). Multiplicities and arbitrary
compatible scheme structures are allowed. Cycles with other components
appear as controls or in the general differential comparison.

## Question

What does the common origin of all coordinate projections in the same
two global equations imply for the first spectral moment? The bounded
probe calculates the complementary Chow restrictions, their infinitesimal
endpoint responses, and the simultaneous Jacobian data. It tests whether
the first normal neighborhood alone imposes the required residue vanishing.

## Purpose

The [Chow realization framework](../../frameworks/chow-realization/index.md)
asks whether \(M_1=0\) on the full CI realization locus (UM1). This would
exclude sole support since \(M_1(m[C_{u,v}])=mu/v\). The
[proof boundary](../../arguments/torus/universal_first_moment_proof_boundary.md)
records the established restricted cases and owns the general question.
This probe compares two projections of one source pair with the established
[first-jet residue formula](../../arguments/torus/spectral_jacobian_first_jet_bridge.md).

## Findings

The calculations below are retained at investigation scope. With the exception
of the explicit first-order congruences, the new comparisons await independent
proof review.

- [Differential trace and endpoint contacts](differential_trace.md)
  expresses the ordinary trace and the differential residue as weighted
  sums of complementary endpoint jets. The weights explain the ratio
  \(4M_1:2M_1\) for a translated cycle. An explicit CI with a nontranslated
  residual component has ordinary trace \(3\) and differential trace \(1\).
- [Complementary Chow restrictions](projection_resultants.md)
  gives the three homogeneous joining-line restrictions and identifies the
  \(1:3\) ruling degrees in the two quadratic graph-chart coefficients.
  The alternating component also has a differential-trace expression
  valid for cycles missing the projection center.
- [Endpoint-plane response](endpoint_plane_response.md) calculates both
  normal variations along the full endpoint-plane charts. The perfect
  residue pairings recover classes of the same source minors in both
  endpoint section algebras, including for nonreduced sections.
- [Jacobian sections and opposite lines](jacobian_sections.md) places all
  six minors in the reduced support's dualizing sheaf with the same
  twist. Two lower-degree sections give a nontrivial Koszul class on the
  line through the endpoints. Its annihilator fixes the restricted
  cofactor pair up to a common nonzero scalar. Their restriction on the
  complementary disjoint line measures \(M_1\).
- [First-order control](first_order_wedge_control.md) gives a proper
  quartic pair whose actual Jacobian wedge satisfies all displayed
  simultaneous congruences modulo \((z,w)^2\) and has central residue \(2\).
  This excludes an argument using just those truncated identities and
  closedness and decomposability of the wedge. The control is outside the
  full translated-cycle scope.

The probe leaves the simultaneous global compatibility question open.
Endpoint residue reciprocity follows from cycle geometry. The Koszul
restriction supplies actual polynomial cofactor data, but the calculation
does not connect it to vanishing of the central classes. A continuation
would need such a comparison or another condition using global support
beyond the tested first normal neighborhood.
