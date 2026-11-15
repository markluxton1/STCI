# Embedded one-step lifts and arithmetic boundaries

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.11 Embedded one-step lifting and the actual homogeneous source

The [October 27 one-step investigation](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#boundary-obstruction-and-endpoint-scope-investigations) supplies a source-level theorem for a *fixed embedded lower thickening* Y with generic algebra K[y]/(y^n), n at least two. Write I=I_C, J=I_Y, and let M_Y=(J/IJ)/torsion. The first-symbol quotient is V_Y=R(-B_Y), and the saturated kernel of the first-symbol map is Ubar_Y=L^n(A_Y), where L is the torsion-free first normal quotient. The actual equation module sits in

    0 -> Ubar_Y -> M_Y -> V_Y -> 0,

with extension class e_Y in Ext^1(V_Y,Ubar_Y). These objects depend on the embedded lower scheme, not only on its graded Hilbert function.

To add a saturated next layer T=L^n(D), a necessary condition is A_Y <= D. Under that condition, extension of the prescribed power map from Ubar_Y to all of M_Y is equivalent to vanishing of the pushed-forward class in H^1(Ubar_Y tensor V_Y^vee(D-A_Y)). Maps satisfying the extension condition form a torsor; *surjectivity* is a further requirement for an actual pure embedded extension, automatic when D=A_Y. Thus an abstract cohomological repair is not itself an embedded thickening.

At the final step of a generically curvilinear Gorenstein multiple curve of length at least three, the source proves the stronger necessary conditions e_Y=0 and A_Y=D_soc. The final socle divisor has no unused repair allowance. For a fixed lower Y the source also gives a completion criterion: splitting of the equation-module extension together with all required perfect-pairing divisor equalities. This is a criterion for an embedded Gorenstein completion, not for two homogeneous carrier equations.

There is a separate exact test for the actual global equations. Suppose C has degree c, ab=(n+1)c, and F,G are actual sections of J(a),J(b) forming a proper pair. Their classes in M_Y give a determinant section theta_Y(F,G). Its vanishing is equivalent to sole reduced support C: if nonzero, the generic length is n and the residual cycle has degree c; if zero, Bezout and purity force generic length n+1 and exhaust the projective degree. For equal degrees the zero-pencils form a Grassmannian linear section of the kernel of the determinant map, restricted to proper pairs; for unequal degrees use the corresponding Segre locus. A generic-rank computation alone does not settle its exceptional decomposable kernel points.

These statements are retained as reviewed source-level deductions. Their practical contribution is to distinguish the lower embedded extension class, its boundary repair, the final Gorenstein pairing, and the actual global source map. Passing any one of these tests does not imply the next.

Next: [carrier normalization and conductor](../carrier-normalization/carrier_descent.md), which imposes a different global descent condition.



## 3.12 Boundary repair versus embedded lifting

For a **specified** obstruction \(o\in H^1(C,V)\) in a vector bundle \(V\) on a smooth curve, and an effective divisor \(D\), the exact sequence
\[
0\longrightarrow V\longrightarrow V(D)\longrightarrow V(D)/V\longrightarrow0
\]
shows that \(o\) dies in \(H^1(C,V(D))\) exactly when it lies in the image of the connecting map \(H^0(C,V(D)/V)\to H^1(C,V)\). By Serre duality this is equivalent to \(o\) annihilating \(H^0(C,V^\vee\otimes\omega_C(-D))\). This is a **principal-parts repair test for the specified class**, not a construction of an arbitrary embedded thickening.

On \(C=\mathbf P^1\), take \(V=\mathcal O(-r)\), \(r\ge2\), and \(n=r-2\). A divisor \(D\) of degree \(B\) corresponds to a nonzero \(h\in H^0(\mathcal O(B))\) up to scalar. The class \(o\) is reparable by **some** such divisor exactly when the catalecticant map
\[
H^0(\mathcal O(B))\longrightarrow H^0(\mathcal O(n-B))^\vee,\qquad
h\longmapsto (q\mapsto\langle o,hq\rangle)
\]
has a nonzero kernel. If \(B\ge\lfloor r/2\rfloor\), a kernel exists by dimension for every class, but this only allows an *arbitrarily chosen* divisor. For a direct sum of obstruction lines the **same** \(h\) must repair all components, so their catalecticant maps must be stacked. The [boundary supplement](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-weighted-initials-and-lifting) gives the complete calculation and the unproved comparison with the ambient lifting complex.

The [one-step package](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#boundary-obstruction-and-endpoint-scope-investigations) is more restrictive: it fixes an embedded lower thickening, its equation module and permissible socle boundary. One must establish that the geometric boundary actually induces the proposed modification of the **correct obstruction bundle**, rather than applying an arbitrary twist to an unrelated cohomology class. Vanishing, the final Gorenstein pairing and the existence of two **proper decomposable** elements in actual homogeneous source spaces are distinct tests. A nonzero linear kernel need not meet the decomposable locus.

The [Delta-embedding package](../../arguments/normal-geometry/rees_equation_persistence.md#the-equation-filtration-conormal-torsion-and-specialization) addresses a different local comparison defect. It is not interchangeable with the repair divisor, with the saturated first-relation defect or with a residual projective curve. See the [open sole-support question](open_normal_geometry.md#punctual-relative-defect-under-sole-support).


## 3.13 Characteristic is part of the mechanism

The fixed C0 is an STCI with a quartic carrier in **every positive characteristic**; the [complete construction and fixed-carrier degree sets](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) are the positive control beside all characteristic-zero exclusions. Every smooth nondegenerate rational quartic is also an STCI in positive characteristic, by the separate [cubic-carrier construction](../../arguments/arithmetic/rational_quartics_in_positive_characteristic.md). This family-wide claim has different carrier-degree quantifiers and is not inferred by changing the coefficients of C0.

| Mechanism | What extends to positive characteristic | Exact restriction or failure |
|---|---|---|
| Ordinary powers on a split smooth quadric | Every-degree sheaf-power/ordinary-power equality and, for integral C, symbolic equality; the proof uses binary monomial multiplication without factorials. | This parameterizes equation spaces; it does not make I two-generated or S/I^m Cohen–Macaulay. See [the full proof](../../arguments/normal-geometry/formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof). |
| Fixed embedded ribbon→triple | The canonical extension J₂/(IJ₂+I³) and its splitting obstruction work without inverting2. | For fixedC0 the class stays nonzero for p>3 and disappears at3; at2 the split O(-8)⊕O(-6) has no quotient O(-7), so the primitiveL=-7 model fails already in first order. [General proof](../../arguments/normal-geometry/formal-normal-intersection.md#the-embedded-ribbon-to-triple-obstruction), [fixed-quartic controls](../../arguments/normal-geometry/formal-normal-intersection.md#characteristic-reach-of-the-two-mechanisms). |
| Full-root Picard criterion | The finite-flat divisor sequence and unit criterion include nilpotents in arbitrary characteristic. | The repeated-component exclusion extends when \(p\nmid s\) for the descended second degree; without the prime-to-p condition Frobenius supplies counterexamples, since \(\mathcal O(-p,p)\) can be trivial on the doubled diagonal. [Spectral proof](../../arguments/spectral/moving_power_and_spectral_roots.md#2026-10-14-generalization-spectral-root-curve-relations). |
| Saturated duality/resultant | The source-level arbitrary-conormal bridge is characteristic free; resultants are integral polynomial identities. | The C0 generator arithmetic extends to odd characteristic under the same r≥2, full-generic-CI, saturated-first-relation and actual sole-support assumptions; the apolar moving-power shortcut extends in fixed total degrees at most \(s\) when \(p>s\). [Full proof](../../arguments/spectral/spectral_pushforward_powers.md#saturated-duality-root-descent-and-embedded-formal-surfaces). |
| Smooth-root formal obstruction/actual bridge | R0005 and R0006 have their explicit characteristic-free balanced-normal and smooth-full-root scopes; R0006 retains inseparable generic root primes. | These hypotheses are not a reduction of arbitrary STCI equations. Regular singular-root R0018 remains characteristic zero. |
| Actual local-cohomology source and duality | A normalized polynomial annihilator excludes an image over any ring where its identity is defined. | The audited QQ tensor, ranks, balanced frame, denominators and field units must be re-established at a prime; characteristic2 is already a different normal model. [Completed endpoint proof](../../arguments/local-cohomology/degree_fifteen_obstruction.md#complete-rational-endpoint-ancestor-exclusions). |
| Conormal comparison and Rees persistence | The exact defect and deformation/specialization sequences are characteristic free in their local algebra scope. | Individual example lengths and special-fiber formulas may use2 as a unit; the invariant alone does not force residual support. [Proof and qualification](../../arguments/normal-geometry/rees_equation_persistence.md#the-equation-filtration-conormal-torsion-and-specialization). |


## 3.14 Why finite determinacy is a uniqueness theorem

The two positivity regimes must not be conflated. Vanishing of \(H^1\) for moving pure-power first relations can **construct compatible first-relation jets**, but does not make the final ideal Gorenstein or two-generated. For a fixed finite-type family of full roots with coefficient-map degree \(\epsilon\), the bound \(\lambda>3\epsilon\) instead kills all \(H^0\) corrections. This **uniqueness** makes each obstruction stage closed in one fixed coefficient space, so Noetherian stabilization gives an existential finite stage, **not an explicit bound**. Adjacent-stage equality alone is insufficient.

The intrinsic smooth-family variant uses the degree inequality \(\nu>\max(Z_E^2,0)\), retaining uniqueness over nonreduced parameter bases; smoothness is essential to that argument. Neither formal uniqueness nor a stable locus constructs a global two-equation STCI. The prime-to-characteristic spectral-root restriction, distinct apolar shortcut, and arithmetic embedded-neighborhood counterexamples retain their separate hypotheses. See the [complete finite-determinacy and root-tower comparison](../../arguments/normal-geometry/finite_determinacy_and_root_tower_comparison.md).

