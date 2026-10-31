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

## 3A. Generic length, residual degree, and the role of full initial equations

For a proper degree-(d,e) pair containing C, let m be the length of its generic transverse local algebra. The cycle identity is de=4m+deg(R), where R is the residual one-cycle. Consequently a lower bound on residual degree requires an *upper* bound on m for actual global equations. A bound on the product of their displayed normal orders does not suffice when leading forms share a factor: cancellation can raise m beyond that product. The full generic initial ideal, rather than two chosen leading forms, determines the generic associated-graded length. See [Chapter 2](02-two-surfaces.md) and [Higher initial ideals](../supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#explicit-cancellation-examples).

A punctual defect in the filtered equation-module comparison is a different issue: it concerns how generic initial relations extend over closed points of C. The [filtration synthesis](normal_filtration_boundary_obstructions.md#full-initial-ideals-and-the-filtered-equation-module) explains why neither such a defect nor a vertical exceptional cycle automatically supplies a positive-degree residual curve. The selected sextic calculation [R-0025](../results/ci_fixed_sextic_jet_rigidity.md) avoids this inference: it bounds m using the actual global mate source and then applies degree exhaustion. A uniform residual theorem would need a comparable bound over every admissible carrier and exceptional stratum, not only the tested sextic.

## 4. The missing bridge

The natural desired theorem would connect a **generator-independent normal invariant** (full initial ideal, Rees data, or saturated flag) to a **positive residual degree** for actual global equations. Current evidence does not supply that implication in general. In particular:

1. A horizontal common direction on the first blowup need not be a smooth global root section.
2. A vertical exceptional component is not a residual curve in projective space.
3. A local or graded algebra passing numerical tests need not be realized by homogeneous forms.
4. The existence of residual curves in selected examples does not imply all pairs have residual curves.
5. A jet-kernel rank calculation for one carrier cannot be extrapolated to arbitrary carriers.

The [filtration/boundary synthesis](normal_filtration_boundary_obstructions.md) isolates the separate punctual-comparison and one-step lifting questions. A bridge between those defects and R-0019's residual cycles still requires proof, with hypotheses on saturation, finite flatness, and properness.

## 5. Concrete next investigations

- **Residual detector:** formulate and prove one implication from a full initial-ideal or valuation invariant to positive residual degree for an actual family. Begin by separating horizontal and vertical exceptional support.
- **Family-level jet bound:** replace the single Fstar of R-0025 with a geometrically defined family and prove a uniform jet-kernel restriction. A generic rank bound alone may leave special carriers.
- **Fixed-boundary deformation:** determine which invariants of R-0023's attachment divisor remain fixed when residual nodes smooth, and whether analogous independent smoothing holds beyond the specified pencil.
- **Characteristic comparison:** isolate the exact flatness and support mechanisms of R-0021 rather than treating characteristic-two coalescence as a characteristic-zero obstruction.

## 6. Authority and evidence

The canonical records R-0001, R-0019, R-0021–R-0025 are authoritative only within their recorded scopes. Their audits and computation certificates remain linked there. The general valuation and blowup program in [formal-normal intersection](formal-normal-intersection.md) is provisional. This synthesis changes neither status nor evidence, and retires no source material.

## 7. Quantitative comparison: where residual degree enters

For a proper intersection of surfaces of degrees d and e, the fundamental cycle decomposes as

    [V(F,G)] = m_C[C] + sum_i m_i[R_i],

where the R_i are irreducible residual curves distinct from C. Consequently

    d*e = 4*m_C + sum_i m_i*deg(R_i).

This is a cycle identity, not a decomposition of defining ideals. It gives a precise target for any proposed residual detector: a universal obstruction must force m_C < d*e/4 for every actual proper pair in the class. By contrast, an exceptional component of a blowup can contribute to a local intersection calculation without producing an R_i downstairs.

Three distinct quantitative tests are available:

- **Proper residual intersection on an auxiliary surface:** Under R-0019's finite-flat curvilinear and saturated-flag hypotheses, the residual *zero-cycle* is (m-1)T + D_(m-1). Its degree is not automatically the degree of a residual *curve* in P3; the auxiliary intersection and properness hypotheses matter.
- **Actual quartic residual curves:** R-0023 constructs a (2,3) pair with a smooth degree-12 residual D and C meeting D transversely in 18 points. At the (1,1) specialization, the degree-12 residual splits into a line and a smooth degree-11 component, with five transverse nodes between them. These have residual multiplicity one along C and degree 12 in the projective cycle; they do not contradict the characteristic-zero quartic-carrier exclusion.
- **Fixed higher-degree jet source:** In R-0025 the selected sextic Fstar and degree-sixteen mates have d*e=96. The normal-branch calculation gives m_C=2n <=22, so the residual cycle has degree at least 96-4*22=8. The essential step is the degree-sixteen jet-kernel identity for this particular Fstar, not a bound valid for all sextics.

The examples show two logically independent ways of proving positive residual degree: construct and certify the residual scheme, or prove a strict upper bound on generic multiplicity for an actual global source space. A formal normal-cone picture alone supplies neither.

## 8. Fixed boundary versus residual removal

The fixed-boundary deformation theorem R-0024 is more precise than the phrase "the nodes smooth." For its specified quartic pencil, the 36-dimensional ordered source has boundary, node and combined tangent ranks 19, 5 and 24. On the Grassmannian, the projective boundary rank is 18, and the fixed-boundary fiber is smooth of dimension 14. After etale localization at the five labeled nodes its formal local ring has five independent smoothing coordinates and nine further parameters.

Thus attachment of the residual to C can be held fixed while the internal singularities of the residual change. This separates **boundary incidence**, **residual geometry**, and **residual degree**. Independent smoothing is not an operation that deletes the residual cycle. The theorem gives formal/etale-local parameters; it does not supply a polynomial coefficient arc in the original source coordinates.

## 9. From isolated calculations to an invariant exclusion

A case calculation should be retained in the synthesis only when it identifies one of the following reusable mechanisms: a saturated-flag divisor formula, a geometric residual component and its attachments, a fixed-boundary deformation invariant, or a global jet-kernel obstruction. Repeatedly searching for individual F,G pairs without extracting a condition on an invariant family does not advance an unrestricted exclusion.

For a proposed family-level extension of R-0025, first define a parameter space of carriers and the vector spaces of degree-e mates. Construct the normal jet map over the parameter space, determine a rank condition on its kernel modulo carrier multiples, and identify the locus where the rank can drop. Then analyze those exceptional strata geometrically; a generic rank calculation is insufficient to rule out all carriers. Finally translate the uniform multiplicity bound, if established, into residual degree using the cycle identity above.

For a proposed extension of R-0019, instead start with a saturated finite-flat flag and check that its residual zero-cycle formula is compatible with the actual global equations. Do not assume a vertical exceptional cycle maps to a residual curve. These are two different possible research programs, and neither currently bridges arbitrary initial ideals to a universal STCI obstruction.
