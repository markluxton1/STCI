# Bounded recovery-audit crosswalk

Read-only pass, 2026-11-19. Main is
`9b7f30757eab14a5d4815c8682184399a35c7c32`, with H15/R-0074 merged.
No open PRs. The other branch, `codex/stci-solution-search` at
`7b1d867cac9e3395684a6f1ed8be8e67a03bec40`, changes quintic/elliptic carrier
search, not H07/H16. File inspections used the existing text snapshot plus
current-main audit and branch comparison. This is a bounded source crosswalk,
not a proof re-audit of every cited chapter or historical transcript recovery.
Historical equivalence is unverified wherever the original transcript was
not read. Paths below are repository-relative and refer to main unless noted.

| Item | Concrete current source and checked scope | Disposition |
|---|---|---|
| H01 | `research/arguments/curve/fixed_quartic_geometry.md`, opening: fixed C0 has unique smooth quadric, degree four, genus zero; characteristic zero. | Basic geometry present. Exact historical (2,4) degeneration and conormal exclusion not rechecked; do not close whole cluster. |
| H02 | Same opening explicitly fixes the unique containing quadric. | Historical generic-two-quadric construction remains rejected for this C0. No new claim to recover. |
| H03 | `research/results/normal_carriers.md` points to R-0001 and `research/arguments/carriers/quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing`. Fixed-C0 normal integral quartics excluded against arbitrary mates in characteristic zero; computations eliminate necessary supersets, not realized classifications. | Stronger current carrier exclusion is present. Historical seven types/fifteen pole strata not matched individually and should not be imported as separate established classifications. |
| H04 | Same normal-carrier owner explicitly distinguishes broader preliminary rational-singularity/resolution statements from the final fixed-C0 exclusion. | Scope corrections are retained. Exceptional-lattice and conductor claims need exact passage comparison before calling the whole historical cluster closed. |
| H05 | `research/results/entirely_thick.md` explicitly states ab>=4pq and 7ab+28pq>=16(aq+bp), for a proper sole-support pair, exact generic orders p,q>=2, balanced normal bundle; links supported-cycle proof. | Exact displayed inequalities located with hypotheses. Not a universal tangent-symbol criterion; fixed C0 balance has characteristic restrictions. |
| H06 | `research/arguments/torus/tropical_thickenings_and_endpoint_duality.md#a-reduced-tropical-model-and-the-exact-normal-map` gives t=x1/x0,u=x0²x2/x1³,v=x0³x3/x1⁴, C°=(u=v=1), rays ±(1,3,4). | Exact special-coordinate tropical model present. This is not H07's general tetrahedron. Residual-line historical wording not separately rederived in this pass. |
| H08 | Audit records the affine-two-quadrics/projective-(2,2) assertion as explicitly retracted. | Keep rejected, not a recovery candidate. Original retraction transcript not reread here. |
| H09 | `research/arguments/carriers/genus_one_uniform_projection_analysis.md#7-exact-conductor-coordinates-and-fixed-curve-fiber-condition` explicitly lists six defining quadrics of [U4:U3V:UV3:V4:U2V2] in P4. `del_pezzo_roots_and_projection.md#2-a-rational-normal-quartic-and-the-actual-coordinate-change` gives an invertible five-coordinate change. | The rational-normal-quartic and six-quadric part is not absent. The proposed THREE set-theoretic equations were not located or verified; do not infer them from this match. |
| H10 | `research/arguments/carriers/quintic_conductor_geometry.md`, opening and organization: characteristic-zero admissible nonendpoint degree-five A4 del Pezzo projections, whole conductor, full inverse-support condition including isolated extra points; links Gorenstein-normalization closure. | Substantial constrained conductor geometry present, not arbitrary quintic descent. The specific historical divisor identities 5c~4H,5ell~H,c+ell~H were not located exactly during this bounded pass. |
| H11 | `research/arguments/arithmetic/z4_intrinsic_arithmetic_mechanism.md`, opening and marked quadratic-neighborhood comparison: full embedded primitive-stage extension, dependence on integral lift, distinction from abstract normal bundle/Frobenius-lifting theories. | Substantial embedding/arithmetic correction preserved. Individual historical characteristic-two transition/valuation claims not all compared. |
| H12 | `research/arguments/arithmetic/positive_characteristic_constructions.md` distinguishes actual fixed-model positive-characteristic presentations, fixed-carrier least-degree results and the different cubic-carrier universal construction. | Actual positive-characteristic material exists. Conditional sextic lift/Q³ freedom/root-node arguments must remain separate until their exact hypotheses are compared; no blanket upgrade. |
| H13 | `research/results/supported_hilbert_full_limits.md` (R-0037): bounded projective supported Hilbert loci and both full limits, including nilpotent/embedded structure; no assumed two-generator property of limits. | Precise principal distinction is present. It does not solve equation realization. |
| H14 | `research/arguments/torus_embedded_quotients.md` (A-0003): constant finite positive-length embedded Laurent quotient with named units; endpoint descent and actual equations in separate scope. | Substantial embedded quotient material present, not merely abstract length or support. Original historical exact-equivalence comparison not performed. |
| H17 | The user supplied the question reconstruction on Nov 19; the [scoped proof owner](../../arguments/torus/boundary_reconstruction_and_defects.md) addresses precise boundary-data versions. | Context recovered, not a verbatim transcript. Bounded-degree reconstruction, finite-order counterexamples and explicit defects are proved; general enriched reconstruction/realization remains open. |

## H09 concrete formulas

With retained coordinates x0,x1,x2,x3 and omitted z, the six quadrics printed
in the source are

    x0*z-x1², x0*x2-x1*z, x0*x3-x1*x2,
    x1*x2-z², x1*x3-z*x2, z*x3-x2².

These are the six minors of the usual 2-by-4 Hankel matrix after reordering
coordinates. Their existence does not by itself provide three set-theoretic
defining equations. No attempted substitution of the projected P3 quartic
for this different P4 curve is permissible.

## Audit hygiene and next gates

The main ledger has stale sentences 'No Result has been promoted in this
audit' and 'No typed Result has been added' despite its R-0074 accounting.
Those stale ledger sentences are corrected in this integration. H07's rigorously checked simple-edge case is in
[the H07 proof](../../arguments/torus/general_coordinate_boundary.md); broader wall/fan claims remain open. [H16 is proved set-theoretically](../../arguments/equations/chow_polytope_rigidity.md#set-level-symmetric-power-fiber-h16). For the remaining M/V entries, next work should retrieve the
actual historical claims and compare exact assumptions, rather than repeat
already-covered carrier computations or count filename matches as closure.


H09 update: the [three-equation proof](../../arguments/curve/fixed_quartic_geometry.md#a-different-curve-the-rational-normal-quartic-in-p4) now resolves the mathematical set-support statement, but not identity with the inaccessible historical transcript.
