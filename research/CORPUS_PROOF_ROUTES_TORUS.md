# Torus proof-route inventory

**Status:** source-text route classification, not independent mathematical verification. The six files listed here were fetched and inspected for their statements, scope and proof ownership. All are already catalog-linked.

| Result or task | Direct Argument | Scope and dependency distinction |
| --- | --- | --- |
| [R-0037 full supported limits](results/supported_hilbert_full_limits.md), [R-0038 eigenvector lifting](results/torus_eigenvector_generator_lifting.md), [R-0039 moving ideal generator criterion](results/moving_ideal_generator_criterion.md) | [A-0001](arguments/torus_hilbert_boundary.md) | Distinct sections of one Argument; supported-limit and graded-generator statements apply in arbitrary characteristic with the specified torus |
| [R-0040 invariant supported CI exclusion](results/invariant_supported_ci_exclusion.md) | [A-0001, invariant CI section](arguments/torus_hilbert_boundary.md#invariant-supported-complete-intersections) | Composite consequence of R-0038 and trace theorem R-0042; **invariance of the ideal**, not merely its radical, is required; characteristic-zero nonexistence |
| [R-0043 sextic eigenpair bound](results/sextic_eigenpair_quotient_bound.md) | [A-0002, sharp bound section](arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound) | Arbitrary characteristic; proper sextic **eigenpairs** not necessarily containing the fixed curve; quotient length at most eight, sharp |
| [R-0042, R-0044 through R-0050](arguments/torus_sextic_residuals.md) | [A-0002](arguments/torus_sextic_residuals.md) | Multiple distinct sextic residual, trace, colon and full-limit arguments assembled in one coherent source; do not mistake common file ownership for proof duplication |
| [R-0051 through R-0056](arguments/torus_embedded_quotients.md) | [A-0003](arguments/torus_embedded_quotients.md) | Constant finite **embedded** transverse quotient with named units; not a theorem for arbitrary moving supported thickenings |
| [R-0070 intrinsic endpoint fibers](results/intrinsic_limits_endpoint_fibers.md) | [A-0001, endpoint fiber section](arguments/torus_hilbert_boundary.md#endpoint-fibers-in-the-two-intrinsic-limits) | Pure curve with reduced support fixed C; general moving intrinsic limits and embedded endpoint lengths; relies on constant-image controls R-0051 and R-0052 from A-0003 |

## Noninterchangeability

- **A-0001** handles Hilbert incidence, moving-ideal generation, and intrinsic limits.
- **A-0002** handles the sextic eigenpair quotient and residual-cycle geometry.
- **A-0003** handles constant embedded quotient families and their endpoint descent.
- R-0040 is not a characteristic-zero obstruction for every torus-invariant **support**; it assumes the complete-intersection **ideal** is invariant.
- R-0043 is a sharp statement about proper sextic eigenpairs, not an exclusion of all sextic STCI pairs.
- R-0070 applies to pure supported curves and compares both intrinsic limits, whereas A-0003 starts from a constant embedded quotient.

**Retrieval:** Start with the precise Result; fetch the named section of the owning Argument. Load the whole Argument only for cross-section dependencies or independent proof review. Preserve the three Arguments as distinct mechanisms; no deduplication is justified from the inspected source structure.

**Unverified:** Mathematical correctness of underlying calculations, full link/anchor validation, and actual token costs.
