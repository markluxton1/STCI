# Proved implications and missing bridges

This is short dependency navigation, not a new theorem or a compulsory research
program. Read each linked statement's exact hypotheses and characteristic.
The [mechanism map](../MAP.md) handles conceptual connections and the
[frontier](../FRONTIER.md) owns open questions.

| Proved implication | Required premises | Scope boundary |
| --- | --- | --- |
| Integral low-degree carrier exclusions + factor reduction → both defining degrees at least five | Fixed embedding, characteristic zero | [Quartic carrier proof](quartic_carrier_proof.md); false as a characteristic-free conclusion |
| Rank-four Gorenstein transverse algebra and symbol pencil → local surface germs → exceptional rank contradiction | Hypothetical supported quartic pair, saturated Gorenstein structure, separable symbol pencil, characteristic-zero global bound | [Quartic pair](quartic_pair_obstruction.md); independent of the full carrier theorem |
| Quintic symbol data + ADE surface + integral divisor relation → even-node contradiction | Exact reduced-symbol and generic-curvilinear hypotheses | [Quintic–octic proof](quintic_octic_surface_constraints.md); rank alone does not finish it |
| Actual normalized section + full conductor compatibility → descended section | Specified carrier and full inverse support, including nilpotent conductor data | [Fixed-carrier criterion](../results/fixed_carrier_conductor_criterion.md); no universal carrier classification |
| Saturated actual first relation + full generic binary CI → normal flatness and arithmetic restrictions | Exact orders and generation assumptions | [Filtrations](normal_filtration_boundary_obstructions.md); other initial patterns remain outside |
| Proper actual pair + generic length → exact residual degree | Complete-intersection purity and degree | [Two surfaces](02-two-surfaces.md), [finite jets](finite_normal_jets.md); an exceptional vertical component is not a residual curve |
| Frobenius-compatible exponents → actual quartic-carrier STCI | Fixed monomial curve, positive characteristic | [Construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md); does not supply characteristic-zero equations |

## Connections requiring an additional theorem

- A saturated graded root or a formal lift does not provide global homogeneous
  generators. Actual source images and their common higher-lift freedom matter.
- A local equation-module comparison defect is not identified with a global
  jet-rank defect or a conductor gluing defect.
- A normalized Cartier class relation does not determine full inverse support
  or descent through a nonreduced conductor.
- Componentwise polarization does not imply node gluing, and gluing does not
  by itself establish the actual projection's determinant/support condition.
- Locally CI affine endpoint contractions do not imply a homogeneous
  presentation of the chosen projective thickening.
- Partial residual absorption does not give an iteration preserving all the
  hypotheses of the next step.
- A computation on one carrier or a finite source chart does not quantify over
  every higher-degree pair.

Each failure is documented through an explicit control or exact missing map
in its [mathematical home](../INDEX.md). Neither analogy nor equivalence closes
an implication. Existence and obstruction use the same compatibility tests:
a construction must pass them, while a nonexistence proof must establish a
failure over its entire claimed class.
