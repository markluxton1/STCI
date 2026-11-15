# Characteristic-two tests and sextic lifting

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.10 The characteristic-two arithmetic test case

For the fixed quartic the conormal sequence is

    0 -> O_C(-8) -> N_C^* -> O_C(-6) -> 0.

Its extension class is proportional to 2 in H1(P1,O(-2)). Accordingly [R-0020](../../results/quartic_conormal_characteristic_jump.md) gives N_C^*=O(-7)^2 in characteristic different from two and O(-8)+O(-6) in characteristic two. This changes the available symmetric-power directions; it does not itself exclude or construct defining equations.

The prescribed integral quartics F=x1^4-x0^3*x3 and G=x2^4-x0*x3^3 give a complementary example. By [R-0021](../../results/quartic_mu4_degeneration.md), their intersection is flat over Z and, away from the endpoints, equals G_m times mu_4. In characteristic zero it is the reduced union of four distinct quartic curves, while in characteristic two it has sole reduced support C and generic algebra K[Y]/(Y^4). This is coalescence of *actual projective components*, not merely exceptional directions.

The full initial ideal explains the jump. In characteristic zero the two generic first normal symbols are independent and the transverse multiplicity along C is one. In characteristic two they become dependent, and cancellation using the actual equations supplies the order-four generator. The special ideal is (X,Y^4), not merely the ideal of the displayed first symbols. [R-0031](../../results/quartic_char2_fourth_equation_kernel.md) identifies the fourth minimal initial-equation bundle and the filtered equation-module kernel with O(-24), with zero comparison defect, for this prescribed pair. It does not give a general theorem for arbitrary characteristic-two pairs.

Finally [R-0012](../../results/prescribed_z4_arithmetic_nonlifting.md) excludes a *flat embedded lift of this particular special complete intersection* over Z_(2) or Z_2 whose generic reduced support is the fixed relative quartic. The obstruction is a forced primitive-triple class in H1(P1,O(-4)) with a middle Laurent coefficient congruent to 2 modulo 4. The theorem neither covers arbitrary ramified mixed-characteristic DVRs nor excludes an unrelated characteristic-zero STCI. Flatness of the displayed integral family is consistent with nonlifting under the extra requirement of sole generic reduced support: its characteristic-zero generic fiber has four components.

These results separate four questions: conormal splitting, full initial equations, global reduced support, and arithmetic deformation of a prescribed embedded scheme. None may be substituted for another.



## 3.10A Characteristic-two cancellation versus embedded lifting

The prescribed characteristic-two pair has full initial ideal \((X,Y^4)\), vanishing local comparison defect, and sole reduced support \(C\), whereas its integral characteristic-zero generic fiber has four reduced components. These facts concern different notions of lifting: [R-0021](../../results/quartic_mu4_degeneration.md) and [R-0031](../../results/quartic_char2_fourth_equation_kernel.md) describe the actual family and filtered kernel; [R-0012](../../results/prescribed_z4_arithmetic_nonlifting.md) excludes the specified embedded lift **with sole generic support** over its stated two-adic bases. The characteristic jump [R-0020](../../results/quartic_conormal_characteristic_jump.md) does not turn this into a universal nonlifting theorem.

## 3.10B An explicit sextic normal-symbol image

For the fixed characteristic-zero quartic, the map from degree-six forms vanishing to order two to quadratic normal symbols has a 23-dimensional domain, a 22-dimensional image and kernel spanned by the cube of the containing quadric. The target has dimension 33, so its image has codimension eleven. The [exact symbol map](../../arguments/spectral/rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map) gives the source basis and all eleven equations.

For a moving quadratic root f with symbol multiplier alpha, these equations become eleven bilinear conditions on f and alpha, retaining the zeros of alpha. The [actual cubic-jet test](../../arguments/spectral/rank_strata_and_sextic_lifts.md#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet) adds a separate finite condition on all forty cubic coefficients. A compatible sextic still needs a proper degree-sixteen mate and a support certificate.


## 3.10C A failed seed and an exact cubic correction

The conditional (6,16) calculation has a smooth torsion-two root \(f_0=(z^2+4)u^2+(z^2-8)v^2\) with a unique projective multiplier \(\alpha_0=z^8-8z^6+96z^4+256z^2+1024\) satisfying all eleven leading-symbol image equations. The cubic comparison has nonzero pairing \(-384\) with an exact row that also annihilates the additional \(q^3\) lift direction. It therefore excludes all sextic lifts of this seed. The seed also fails the independent second obstruction under its stated hypotheses; neither test excludes the entire family.

The cubic correction is \(f(\ell u+mv)\), where \(f=au^2+buv+cv^2\) and \(\deg\ell,\deg m\le7\). For a prescribed cubic \(h=h_0u^3+h_1u^2v+h_2uv^2+h_3v^3\), compatibility means \(h_0=a\ell\), \(h_1=b\ell+am\), \(h_2=c\ell+bm\), \(h_3=cm\). Multiplication by nonzero \(f\) is injective, giving a rank-sixteen correction map into forty cubic coefficients and a twenty-four-dimensional quotient obstruction. A correction, if it exists, is unique. These undivided identities remain valid for singular roots and coefficient zeros.

The twenty-five second-obstruction pairings, full-root torsion and existence of a proper degree-sixteen mate remain separate tests. See [the full calculation](../../arguments/carriers/normalization_conductor_phase2_addendum.md#coefficient-level-cubic-obstruction-without-elimination).


## 3.10E A full-lift certificate beyond the failed seed

The historical [free cube-orbit calculation](../../arguments/carriers/normalization_conductor_phase2_addendum.md#existing-full-lift-exclusion-on-the-free-cube-orbit-chart) includes the free \(\eta q^3\) sextic lift. Its restricted chart reduces to \(p(h)=648h^4+45h^2-4=0\), while two full cubic equations satisfy \(E_4-6E_8=18h-324h^3\) and a polynomial unit certificate. Thus that entire chart is empty even after varying the lift. The endpoint and orbit-collision strata remain open. Application to supported pairs uses the [reviewed quadric-cycle norm proof](../../arguments/carriers/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge).


## 3.10F Two-node reduction and the surviving sextic pencil

The [forced-norm two-node continuation](../../arguments/carriers/normalization_conductor_phase2_addendum.md#two-node-root-strata-exact-exclusions-and-retained-pencils) excludes the generic nonzero-defect line component and its \(B=0,C=0\) boundaries by exact scoped computations. The generic conic component remains unresolved. On the distinct zero-defect stratum, the global sextic has the exact form \(H_1H_2+\eta q^3\), and an actual supported pair must have \(\eta\ne0\) by cubic factor reduction. This is a necessary pencil description, not a mate construction.


## 3.10G Actual-pair geometric obstruction

The reviewed geometric continuation of the conditional (6,16) investigation forces a nonreduced full-root multiplier divisor for an actual supported pair with the stated saturated movement-two bridge. The normal strict-sextic singularity budget gives 144 versus at most 50; ampleness of the strict mate extends the restriction to nodal roots. The resulting degree-52 exceptional locus is necessary, not sufficient, and is not a condition on arbitrary abstract root incidence points.

