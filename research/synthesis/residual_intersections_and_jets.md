# Residual intersections, deformations, and global jet bounds

**Status:** thematic synthesis of scoped canonical results and open interfaces. This is not a new theorem or an independent rerun of computational certificates. Start with [the simultaneous-surface chapter](02-two-surfaces.md) and [the formal-normal intersection framework](formal-normal-intersection.md).

## 1. Setup: proper intersections are not necessarily STCI

For two surfaces meeting properly and containing the fixed quartic C, write the fundamental cycle as [V(F,G)] = m[C] + R. Then de = 4m + degree(R), so m = de/4 **only** when R vanishes. See [Chapter 2](02-two-surfaces.md) for generic normal orders and exceptional directions, and [Formal normal geometry](formal-normal-intersection.md) for the provisional full-initial-ideal/valuation framework.

The results below concern **specific residual cycles, deformation families, and global jet sources**. None makes a vertical exceptional component into a positive-degree residual curve or proves that every pair has residual support.

## 2. Four distinct results and their scopes

**A. Residual cycles from a saturated quasiprimitive flag.** [R-0019](../results/quasiprimitive_residual_cycles.md) gives a torsion-length identity and a proper residual zero-cycle formula under finite-flat curvilinear and saturated-order-flag assumptions, plus a smooth auxiliary surface with a nonzero generic first class and proper residual intersection. It also bounds the first-normal divisor by the top defect under its additional primitive-horizontal-kernel hypothesis. These are *length cycles and divisor inequalities*, not scheme/ideal equalities. Do not apply them to an unsaturated associated graded or an improper residual intersection.

**B. Explicit quartic residual configurations.** [R-0023](../results/ci_quartic_explicit_residual_geometry.md) studies specified quartic pairs in characteristic zero. One (2,3) pair has residual D smooth of degree 12 and genus 16, meeting C transversely in 18 points. A (1,1) pair has residual L union E, with L a line and E smooth of degree 11 and genus 12; their five transverse nodes coexist with 17 C-E attachments and one C-L attachment, without triple points. This demonstrates actual global residual configurations, **not** a classification of quartic pairs.

**C. Deforming the residual while fixing its attachment boundary.** [R-0024](../results/ci_quartic_fixed_boundary_smoothing.md) applies only at the (1,1) pencil of R-0023. The fixed-boundary Grassmannian fiber is smooth of dimension 14, and after splitting/labeling the five nodes its formal local coordinates include five independent node-smoothing parameters. Thus the residual nodes can be smoothed independently *while the boundary is fixed*, locally in the specified family. This is not a global polynomial coefficient arc or a universal smoothing theorem.

**D. A selected higher-degree global jet obstruction.** [R-0025](../results/ci_fixed_sextic_jet_rigidity.md) fixes one sextic Fstar and considers proper degree-sixteen mates G. Its audited order-twelve jet-kernel computation implies generic multiplicity at most 22 and residual degree at least eight. The source uses exact normal division and finite-field rank certification lifted to characteristic zero; an independent normal-division replay passed, while the Macaulay2 source was not rerun in that workflow. The conclusion is for this Fstar and this mate degree, not all sextics.

## 3. How the results fit together

- R-0019 controls **abstractly constrained local-to-global residual cycles** provided its strong saturated/finite-flat hypotheses hold. R-0023 provides **specific actual projective intersections**, but those examples alone do not establish that R-0019's hypotheses hold for them.
- R-0024 shows that residual singularities need not be rigid under a fixed attachment divisor in its particular pencil. It does **not** say the residual can be removed: smoothing nodes changes singularities, not automatically the positive residual degree in the cycle.
- R-0025 supplies a **global source-space obstruction** in a selected higher-degree setting. Its residual-degree bound comes from limiting the generic transverse multiplicity, not from an exceptional vertical cycle or the R-0019 formula.
- [R-0021](../results/quartic_mu4_degeneration.md) is a different specialization phenomenon: a prescribed flat pair has four distinct quartic components in characteristic zero but only C as reduced support in characteristic two. It is a useful warning that support and transverse multiplicity behave differently under characteristic change; it is not a universal quartic-pair decomposition.
- [R-0022](../results/quartic_44_filtered_exclusion.md), independently of the broader [R-0001](../results/quartic_carrier_exclusion.md), excludes quartic-pair STCI in characteristic zero. R-0023/R-0024 remain useful geometric laboratories **despite** the closed quartic STCI case.

## 4. The missing bridge

The desired general interface should explain actual residual geometry and its specialization from full normal and global equation data. Positive residual-degree bounds are one scoped outcome; constructive transfer of residual mass onto \(C\) is another. The current [arbitrary-degree continuation](../notes/2026-10-27-arbitrary-degree-absorption-synthesis.md) proves selected interfaces provisionally without assuming that every pair has residual support. In particular:

1. A horizontal common direction on the first blowup need not be a smooth global root section.
2. A vertical exceptional component is not a residual curve in projective space.
3. A local or graded algebra passing numerical tests need not be realized by homogeneous forms.
4. The existence of residual curves in selected examples does not imply all pairs have residual curves.
5. A jet-kernel rank calculation for one carrier cannot be extrapolated to arbitrary carriers.

The [filtration/boundary synthesis](normal_filtration_boundary_obstructions.md) isolates the separate punctual-comparison and one-step lifting questions. A bridge between those defects and R-0019's residual cycles still requires proof, with hypotheses on saturation, finite flatness, and properness.

## 5. Selecting investigations

A substantial calculation should test a general construction, criterion or competing assertion, with a stated payoff beyond its degree pair. The sextic locus is an optional control, with no reduction from arbitrary equations. The earlier scoped questions below remain available when they serve such a principle.

- **Residual interface:** compare actual attachment and transfer with full primary equation modules and valuation data. Distinguish the geometric residual, the flat closure of a generic residual, and exceptional vertical support.
- **Family-level jet bound:** replace the single Fstar of R-0025 with a geometrically defined family and prove a uniform jet-kernel restriction. A generic rank bound alone may leave special carriers.
- **Fixed-boundary deformation:** determine which invariants of R-0023's attachment divisor remain fixed when residual nodes smooth, and whether analogous independent smoothing holds beyond the specified pencil.
- **Characteristic comparison:** isolate the exact flatness and support mechanisms of R-0021 rather than treating characteristic-two coalescence as a characteristic-zero obstruction.

## 6. Authority and evidence

The canonical records R-0001, R-0019, R-0021–R-0025 are authoritative only within their recorded scopes. Their audits and computation certificates remain linked there. The general valuation and blowup program in [formal-normal intersection](formal-normal-intersection.md) is provisional. This synthesis changes neither status nor evidence, and retires no source material.

## 7. General partial absorption and the actual equation presentation

The [arbitrary-degree absorption synthesis](../notes/2026-10-27-arbitrary-degree-absorption-synthesis.md) integrates four reviewed provisional interfaces, with proofs and audits linked there:

- On a chosen smooth containing surface, linear-system interpolation constructs any finite increase \(m<n\) in marked multiplicity for sufficiently large mate degree. The residual closure specializes to \((n-m)C+D_n\), with actual global equations and Cartier gluing. This is a positive characteristic-zero operation, not a claim that every given residual deforms this way.
- For the fixed quartic, an integral carrier smooth at every point of \(C\) forces residual degree at least one third of the CI degree. The nef bundle \(3H-C\) proves this uniform capacity statement; it is not transferred to arbitrary on-curve singular carriers.
- For the full \(C\)-primary component \(T\), the actual attachment divisor is the determinant of the torsion-free equation source plus the torsion divisor of \(I_T/I_CI_T\). A determinant alone can miss attachments at non-lci points of \(T\). Full attachment \(T\cap D\) also includes marked normal nilpotent contributions.
- A flat lower witness can organize deformations of actual pairs, while the full primary component changes Hilbert polynomial at an absorption jump. Quot motion and global section lifting have distinct obstruction groups, and full primary extraction must not be assumed to commute with specialization.

These interfaces connect nef/effective cones, linkage duality, Quot deformation theory and conductor/formal-group descent. They remain proposals with independent evidence; they do not establish an unrestricted characteristic-zero construction or exclusion.
