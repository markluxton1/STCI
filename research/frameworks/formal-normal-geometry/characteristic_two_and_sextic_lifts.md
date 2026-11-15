# Characteristic-two tests and sextic lifting

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.10 The characteristic-two arithmetic test case

For the fixed quartic, the conormal sequence
\[
0\to\mathcal O_C(-8)\to N^*_{C/\mathbf P^3}\to\mathcal O_C(-6)\to0
\]
has extension class proportional to \(2\). Thus [R-0020](../../results/quartic_conormal_characteristic_jump.md) gives splitting \(\mathcal O(-7)^2\) away from characteristic two and \(\mathcal O(-8)\oplus\mathcal O(-6)\) in characteristic two. This changes normal-symbol directions, not by itself the existence of equations.

The prescribed integral pair \(F=x_1^4-x_0^3x_3\), \(G=x_2^4-x_0x_3^3\) is flat over \(\mathbf Z\). By [R-0021](../../results/quartic_mu4_degeneration.md), away from the endpoints its family is \(\mathbf G_m\times\mu_4\): four reduced quartic components in characteristic zero coalesce to sole reduced support \(C\) and generic transverse length four in characteristic two. Cancellation of dependent first normal symbols produces the **full** initial ideal \((X,Y^4)\); [R-0031](../../results/quartic_char2_fourth_equation_kernel.md) identifies the fourth initial-equation bundle and zero filtered comparison defect **for this pair**, not for all characteristic-two pairs.

The separate [R-0012](../../results/prescribed_z4_arithmetic_nonlifting.md) excludes a flat embedded lift of the specified supported complete intersection over \(\mathbf Z_{(2)}\) or \(\mathbf Z_2\) **with sole generic reduced support the fixed relative quartic**. Its primitive-triple obstruction lies in \(H^1(\mathbf P^1,\mathcal O(-4))\). This is compatible with flatness of the displayed family, whose characteristic-zero generic fiber has four components; neither statement excludes unrelated characteristic-zero STCI pairs or arbitrary ramified bases.

## 3.10A Characteristic-two cancellation versus embedded lifting

The prescribed characteristic-two pair has full initial ideal \((X,Y^4)\), vanishing local comparison defect, and sole reduced support \(C\), whereas its integral characteristic-zero generic fiber has four reduced components. These facts concern different notions of lifting: [R-0021](../../results/quartic_mu4_degeneration.md) and [R-0031](../../results/quartic_char2_fourth_equation_kernel.md) describe the actual family and filtered kernel; [R-0012](../../results/prescribed_z4_arithmetic_nonlifting.md) excludes the specified embedded lift **with sole generic support** over its stated two-adic bases. The characteristic jump [R-0020](../../results/quartic_conormal_characteristic_jump.md) does not turn this into a universal nonlifting theorem.

## 3.10B An explicit sextic normal-symbol image

In characteristic zero the actual degree-six order-two source has dimension \(23\), symbol image dimension \(22\), and kernel \(kq^3\), inside a \(33\)-dimensional target. Thus eleven independent leading-symbol conditions remain. For a moving quadratic root \(f\) and multiplier \(\alpha\), they are **bilinear** conditions retaining the zeros of \(\alpha\). The [exact symbol map and equations](../../arguments/spectral/rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map) give the complete linear calculation. The [cubic-jet gate](../../arguments/spectral/rank_strata_and_sextic_lifts.md#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet) is additional; neither test constructs a degree-sixteen mate or certifies sole support.

## 3.10C A failed seed and an exact cubic correction

The conditional \((6,16)\) torsion-two seed \(f_0=(z^2+4)u^2+(z^2-8)v^2\) has unique projective multiplier \(\alpha_0=z^8-8z^6+96z^4+256z^2+1024\) passing all eleven leading-symbol conditions. The exact cubic pairing \(-384\) annihilates both the seed and its free \(q^3\) lift, so **no sextic lift of this seed** exists; its independent second obstruction also fails. This does not exclude the family.

For a general quadratic \(f=au^2+buv+cv^2\), the cubic correction \(f(\ell u+mv)\) has coefficients \((a\ell,b\ell+am,c\ell+bm,cm)\). Multiplication by nonzero \(f\) is injective, so this is a rank-16 map into 40 cubic coefficients, with 24-dimensional quotient and a unique correction if one exists. These undivided identities include singular roots and coefficient zeros. The [full coefficient test](../../arguments/carriers/normalization_conductor_phase2_addendum.md#coefficient-level-cubic-obstruction-without-elimination) retains the remaining second-obstruction and mate questions.

## 3.10E A full-lift certificate beyond the failed seed

The [free cube-orbit full-lift calculation](../../arguments/carriers/normalization_conductor_phase2_addendum.md#existing-full-lift-exclusion-on-the-free-cube-orbit-chart) includes the \(\eta q^3\) direction. Its chart satisfies \(648h^4+45h^2-4=0\), whereas the cubic equations imply \(18h-324h^3=0\), with an exact polynomial unit certificate. Thus **the entire stated chart is empty**, not just the original seed. Endpoint and orbit-collision strata remain open; supported-pair applications require the [quadric-cycle norm bridge](../../arguments/carriers/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge).

## 3.10F Two-node reduction and the surviving sextic pencil

The [two-node continuation](../../arguments/carriers/normalization_conductor_phase2_addendum.md#two-node-root-strata-exact-exclusions-and-retained-pencils) excludes the generic nonzero-defect line component and its \(B=0,C=0\) boundaries, but not the generic conic component. On the distinct zero-defect stratum, a global sextic must have the form \(H_1H_2+\eta q^3\), with \(\eta\ne0\) for an actual supported pair by cubic-factor reduction. This is a **necessary** pencil, not a mate construction.

## 3.10G Actual-pair geometric obstruction

Under the conditional \((6,16)\) saturated movement-two bridge, the [geometric continuation](../../arguments/carriers/normalization_conductor_phase2_addendum.md#geometric-exceptional-locus-for-actual-pairs) forces a nonreduced full-root multiplier divisor for any actual supported pair. The normal strict-sextic singularity budget is \(144\) versus at most \(50\), and ampleness extends the argument to nodal roots. The degree-52 exceptional locus is **necessary, not sufficient**; the statement does not apply to arbitrary abstract root-incidence configurations.

