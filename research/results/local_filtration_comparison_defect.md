---
id: STCI-R-0030
title: "Local filtered-equation comparison and punctual defect criterion"
kind: theorem
scope:
  characteristic: "arbitrary where the stated regular local hypotheses hold"
  curve: "smooth codimension-two curve in smooth threefold"
  hypotheses:
    - "J=(f,g) is a two-generator regular sequence contained in I_C"
    - "Generic finite-length and generic defect-free hypotheses are imposed only for the corresponding conclusions"
statement: "The initial-equation comparison has a canonical exact sequence; generic defect is initial-generator excess; under generic vanishing punctual defect is the torsion lost by the comparison, supported at simultaneous carrier singularities."
dependencies: []
evidence:
  - "research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md"
  - "research/supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md"
  - "research/supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md"
independent_audits:
  - "research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md"
  - "research/supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Local statements only; no global quartic twisting assertion"
  - "No existence or impossibility theorem for punctual defects under radical(J)=I"
  - "No new executable replay during consolidation"
---
# Local filtered-equation comparison

## Statement
Let I be the ideal of a smooth codimension-two curve in a smooth threefold, J=(f,g) subset I a regular sequence, S=gr_I R, H=in_I(J), B=in_I(IJ), and S_+ the positive ideal. Give D=J/IJ the filtration F^nD=(J intersect I^n+IJ)/IJ. Then S_+H subset B and, for every n, there is a canonical exact sequence

0 -> Delta_n=B_n/(S_+H)_n -> Q_n=H_n/(S_+H)_n -> gr_F^nD=H_n/B_n -> 0.

At a generic transverse field where J is a parameter ideal, dim Delta=mu(H)-2. If Delta vanishes generically along an integral smooth curve, then at each DVR stalk

length Delta_n = length tors(Q_n) - length tors(gr_F^n D).

In particular torsion-free Q implies Delta=0 under generic vanishing. If either carrier is smooth at p on C, then Delta_p=0. Thus Supp Delta is contained in C intersect Sing(F) intersect Sing(G), without asserting this intersection is nonempty.

## Hypotheses and quantifiers
The exact sequence is an algebraic initial-ideal identity. The generator-excess count assumes a generic finite-length transverse complete intersection. The DVR formula assumes generic Delta=0. The support containment assumes regular local ambient geometry and the stated two-generator complete intersection.

## Proof outline
Take initial symbols of J, IJ, and the intrinsic filtered equation module. The quotient identities give the exact sequence. At the generic transverse point, J/IJ has dimension two, so summing its graded dimensions gives the generator excess. Over a DVR the surjective comparison induces an isomorphism on equal-rank torsion-free quotients, yielding the length identity. At a smooth carrier, straighten its equation to one normal parameter; the completed-local standard-basis calculation gives in(IJ)=S_+in(J), and faithful flatness descends the vanishing.

## Dependencies
No result dependency; original reviewed local algebra is cited as evidence.

## Evidence and verification
The October 23 and 24 independent mathematical reviews checked the exact comparison, local support calculation, and torsion formula. The October 26 note independently checks the elementary quotient and DVR arguments. Saved validation scripts were not rerun during consolidation.

## Consequences
Separates generic extra initial generators from isolated torsion cancellations, and gives a necessary simultaneous-singularity condition for punctual defect.

## Limitations
Does not prove the characteristic-two O(-24) global identification or the filtered normal-Koszul spectral sequence. Does not decide whether a nonzero punctual defect exists under radical(J)=I and generic Delta=0. Counterexamples with residual support do not settle that question.

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. The consolidation incorporates reviewed corrections; the statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.

The [supported length-five specialization control](../synthesis/comparison_defect_specialization.md) computes zero relative comparison defect and nonzero actual closed-fiber comparison defect. It shows why exceptional transverse slices do not by themselves establish a punctual relative defect. This reviewed example does not change the theorem or settle its remaining sole-support existence question.
