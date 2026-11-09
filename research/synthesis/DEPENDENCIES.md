# Proved implications and missing bridges

This is short dependency navigation, not a new theorem or a compulsory research
program. Read each linked statement's exact hypotheses and characteristic.
The [mechanism map](../MAP.md) handles conceptual connections and the
[frontier](../FRONTIER.md) owns open questions.

| Proved implication | Required premises | Scope boundary |
| --- | --- | --- |
| Integral low-degree carrier exclusions + factor reduction → both defining degrees at least five | Fixed embedding, characteristic zero | [Quartic carrier proof](quartic_carrier_proof.md); false as a characteristic-free conclusion |
| Rank-four Gorenstein transverse algebra and symbol pencil → local surface germs → exceptional rank contradiction | Hypothetical supported quartic pair, saturated Gorenstein structure, separable symbol pencil, characteristic-zero global bound | [Quartic pair](quartic_pair_obstruction.md); independent of the full carrier theorem |
| Proper supported (5,8) pair + globally ADE quintic → contradiction | Fixed C0, characteristic zero; no reduced-symbol assumption | [Cover and symbolic-triple proof](quintic_octic_ade_cover_and_triple.md); [earlier reduced-symbol even-node proof](quintic_octic_surface_constraints.md) remains a separate argument |
| Nonnormal quintic + Gorenstein normalization + sole-supported mate → contradiction | Integral carrier, fixed C0, characteristic zero; any mate degree | [Full conductor proof](quintic_gorenstein_normalizations.md); normal quintics and non-Gorenstein normalizations are outside |
| Actual normalized section + full conductor compatibility → descended section | Specified carrier and full inverse support, including nilpotent conductor data | [Fixed-carrier criterion](../results/fixed_carrier_conductor_criterion.md); no universal carrier classification |
| Saturated actual first relation + full generic binary CI → normal flatness and arithmetic restrictions | Exact orders and generation assumptions | [Filtrations](normal_filtration_boundary_obstructions.md); other initial patterns remain outside |
| Proper actual pair + generic length → exact residual degree | Complete-intersection purity and degree | [Two surfaces](02-two-surfaces.md), [finite jets](finite_normal_jets.md); an exceptional vertical component is not a residual curve |
| Torus translates of a supported thickening → invariant full flat limits with the same support and Hilbert polynomial | Fixed C0, full Hilbert limit, closed incidence between C0 and a fixed power neighborhood | [Flat-limit argument](global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary); CI/AG structure need not survive, and limiting two forms is not the full ideal |
| Embedded finite quotient → saturated orbit-family image and exact prescribed-degree CI test | Actual u,v multiplication, finite quotient length n; degree product 4n and a proper pair in the recovered homogeneous source spaces | [Quotient descent](../arguments/torus_embedded_quotients.md); arbitrary characteristic. Abstract algebra type and endpoint lengths alone do not give the proper pair |
| Proper eigenform sextic pair → quotient length at most eight and boundary cycle degree at least four | Integer weights (0,1,3,4), both ordinary degrees six; finite quotient counts local lengths | [Sextic residual configurations](../arguments/torus_sextic_residuals.md); sharp in every characteristic, not a bound for arbitrary mixed-weight pairs |
| Frobenius-compatible exponents → actual quartic-carrier STCI | Fixed monomial curve, positive characteristic | [Construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md); does not supply characteristic-zero equations |
| Exact prescribed Chow bundle map → unique ambient pair | Algebraically closed field, any characteristic; dim V≥3 and nonnegative symmetric powers | [Full Hom identity](chow_bundle_maps.md); existence with the required determinant remains to be proved |
| Picard torsion → spectral determinant vanishing and a graded CI family | Full smooth-root, parameter-line and characteristic hypotheses | [Determinant schemes](spectral_determinant_schemes.md); the actual homogeneous source operator is an additional condition |
| Actual embedded jet filtration → finite homogeneous realization | Fixed smooth embedded curve and degree; explicit bound uses the stated quadric flag | [Global jets](global_equation_jets.md); neither a rank plateau nor graded pieces alone establish realization |

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
- A flat finite quotient family need not have images commuting with base
  change. The [length-four comparison](../arguments/torus_embedded_quotients.md#embedded-quotients-and-characteristic-dependent-endpoints)
  separates quotient collisions, endpoint algebra, postulation and actual CI.
- The [residual three-generator limit](../results/sextic_three_generator_full_limit.md)
  has the CI Hilbert series but loses its CI generators; it is not a
  sole-support boundary for the supported deformation problem.
- Partial residual absorption does not give an iteration preserving all the
  hypotheses of the next step.
- An invariant supported ideal with the right Hilbert polynomial need not
  deform to a CI while preserving support. Torus weight decompositions of
  tangent spaces do not establish integration or recovery of two generators;
  a chosen boundary family also needs coverage before supporting an exclusion.
- A computation on one carrier or a finite source chart does not quantify over
  every higher-degree pair.

Each failure is documented through an explicit control or exact missing map
in its [mathematical home](../INDEX.md). Neither analogy nor equivalence closes
an implication. Existence and obstruction use the same compatibility tests:
a construction must pass them, while a nonexistence proof must establish a
failure over its entire claimed class.
