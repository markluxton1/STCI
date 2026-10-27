# Normal jets and filtrations: first claim-level source inventory

**Status:** read-only mathematical triage of canonical records, 2026-10-27. No proof revalidation, source-note reading, deletion, or theorem promotion yet. Branch: `restructure/mathematical-consolidation`.

## Claims and primary locations

| Claim | Authority | Distinct contribution | Supporting source to inspect | Consolidation treatment |
|---|---|---|---|---|
| Conormal splitting changes in characteristic 2 | R-0020, `results/quartic_conormal_characteristic_jump.md` | N* is O(-7)^2 away from 2; O(-8)+O(-6) in char 2 | `notes/2026-10-23-quartic-characteristic-conormal.md`, geometry audit, `computations/verify_normal_bundle.py` | Foundational geometry; preserve transition argument |
| Saturated first relation implies normal flatness | R-0010, `results/saturated_first_relation_normal_flatness.md` | Projective resultant of degree zero and socle pairing, conditional on actual lci and full generic initial CI with r<s | 2026-10-19 spectral-bridge and duality notes and adversarial audits | Mechanism plus exact exclusions from scope |
| Saturated quasiprimitive residual cycle | R-0019, `results/quasiprimitive_residual_cycles.md` | Determinant length formula, residual zero-cycle and first-normal defect bound | `notes/2026-10-05-residual-cycle.md`, audit | Separate from descending residual curves; preserve distinction |
| Full conormal socle budget | R-0032, `results/full_conormal_socle_budget.md` | n(lambda d-L)=lambda(nd-2M)+2Delta with intermediate torsion | `notes/2026-10-13-evening-entirely-thick-rees-progress.md`, independent audit | Necessary numerical identity, not exclusion |
| Constant first-relation lifting obstruction | R-0033, `results/constant_first_relation_lifting.md` | Quadratic obstruction for factor directions, conditional on no new next-order relation | 2026-10-13 thick-equality geometry and audit | Boundary of constant-graded-CI argument |
| Local filtered-equation comparison | R-0030, `results/local_filtration_comparison_defect.md` | Canonical exact sequence and punctual defect supported at simultaneous singularities | 2026-10-23/24 reviews, 2026-10-26 local proof audit | Distinguish generator excess from punctual torsion; does NOT prove simultaneous singularities exist |
| Fourth normal equation in prescribed char-2 model | R-0031, `results/quartic_char2_fourth_equation_kernel.md` | Canonical O(-24) kernel, order-four generator, zero comparison defect | 2026-10-23 investigation, audit, validation README | Concrete model, not universal char-2 theorem |
| (4,4) characteristic-zero exclusion | R-0022, `results/quartic_44_filtered_exclusion.md` | Filtered-contact proof; distinct alternative K3 Picard-rank proof | 2026-10-23 proof/audit and K3 proof/audit notes | Preserve **both** proof mechanisms; no all-degree inference |
| Pointwise conductor–socle defect | R-0036, `results/pointwise_conductor_socle_defect.md` | D_n=(n-1)A-B|c under smooth Cartier normalization hypotheses | 2026-10-14 conductor and independent audit notes | Specialized global bridge; preserve hypotheses |

## Preliminary navigation assessment

- `results/INDEX.md` declares 36 ID-bearing authoritative results, whereas `results/README.md` and `results/jet_geometry.md` are legacy topic navigation. The latter records a primitive conormal modification at a degree-three divisor R, first-order quartic sources on Q, and a second-order target on 2R; its cited 2026-10-06 structural supplement has **not yet been inspected**.
- `results/entirely_thick.md` records necessary blowup/quadric inequalities and expressly says these do not exclude the entirely-thick branch. The valuation/Rees failure mode should remain visible.
- Do not collapse `R-0030` into `R-0031`: one is general local algebra; the other is an explicit characteristic-two instance.
- Do not collapse `R-0020` into `R-0022`: conormal splitting alone does not exclude a quartic pair.
- R-0022's alternative K3 proof must be retained even if the future narrative favors the filtered-contact proof.

## Next evidence pass

Read the cited proof and independent-audit notes for R-0010, R-0020, R-0022, R-0030, R-0031, R-0032 and the legacy jet supplement. Classify which notes contain unique proof steps, useful failed attempts, independent verification, or only repeated exposition. Only then propose source-file disposition.

**Not yet covered:** other canonical records, most notes, computations and validation files; the table above is not a full mathematical inventory.
