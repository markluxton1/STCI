---
id: STCI-R-0027
title: "Dual discriminant intersections and singular scheme of the marked quartic"
kind: theorem
scope:
  characteristic: "0"
  curve: "fixed marked rational quartic C0"
  hypotheses:
    - "The specified dual-coordinate discriminant and its Jacobian ideal"
statement: "The dual discriminant has the stated scheme-theoretic intersection identities; its saturated Jacobian scheme has degree 16, four minimal and two embedded associated primes, and two length-one endpoint corrections."
dependencies:
  - STCI-R-0026
evidence:
  - "research/supplements/QUARTIC_DUAL_SCHEMES.md"
  - "research/computations/verify_quartic_dual_singular_scheme_2026_10_24.m2"
independent_audits:
  - "research/supplements/QUARTIC_DUAL_SCHEMES.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Saved Macaulay2 certificates inspected, not freshly rerun"
  - "Specific marked dual discriminant only"
---
# Dual discriminant and singular scheme

## Statement
In dual coordinates A,B,C,D, put M=AD-BC, L=BC-4AD, K=AC^2+B^2D, N=AC^2-B^2D, and Delta=-4L^3-27K^2=4M(8AD+BC)^2-27N^2. The scheme intersections have ideals (Delta,K)=(K,L^3), (Delta,M)=(M,N^2), and (K,M), respectively. These identities use Cartier multiplicities, not ambient ideal powers.

Let J=Jac(Delta), h=(BC+8AD)K, and U=J+(h). Then J is saturated, J:h=(B,C,AD), and U/J is isomorphic to (S/(B,C,AD))(-5). The scheme U is unmixed, and J has four minimal associated primes and two embedded endpoint primes, each contributing length one. There is a primary decomposition U=(A,B^2) intersect (D,C^2) intersect T_O intersect P_B, with T_O primary to the osculating quartic and P_B the reduced bitangent quartic prime. The Hilbert polynomials are HP(S/J)=16n-43 and HP(S/U)=16n-45.

Away from the two marked endpoints, transverse Jacobian structures are curvilinear doubles along cusp strata and reduced along the ordinary-node bitangent stratum. These generic models alone do not imply the endpoint contributions.

## Hypotheses and quantifiers
Algebraically closed characteristic-zero field and the displayed marked dual equation.

## Proof outline
The discriminant identities are polynomial identities. The colon, saturation, associated primes, Hilbert polynomials, and decomposition follow from the exact saved Macaulay2 certificate and independent mathematical audit. Local endpoint syzygies and Hilbert-Burch calculations identify the two socle corrections; transverse cusp and node models identify generic scheme structure.

## Dependencies
R-0026 supplies the marked flag and dual-geometric setup.

## Evidence and verification
Independent audit and saved Macaulay2 source and outputs; no fresh execution during consolidation.

## Consequences
Distinguishes the unmixed singular cycle from its two embedded endpoint contributions.

## Limitations
No global STCI obstruction and no claim about other dual varieties.

## Current proof

[Dual discriminant: intersections, singular cycle and endpoint socles](../supplements/QUARTIC_DUAL_SCHEMES.md). The full proof and exact scope are retained in these mathematical homes; the independent review described there covers the inherited result.
