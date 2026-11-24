# Trace, residue, simultaneous projections, and toric descent

**Status:** active exploratory note, not a promoted result. Characteristic zero unless stated otherwise. Goal: calculate the trace and residue on the full CI realization locus of translated cycles, without assuming universal moment vanishing or restricting carriers.

## Governing research question (user clarification)

The primary object is the **full complete-intersection realization locus of translated cycles**, not the small diagonal and not the sole-supported quartic problem. Fix a total cycle multiplicity \(m\), and consider every \(\sigma=\sum_i n_i[C_{u_i,v_i}]\) in \(\operatorname{Sym}^m(\mathbb G_m^2)\). For every degree pair \(a,b>0\) with \(ab=4m\), consider actual proper homogeneous CI pairs \((F_a,G_b)\) with entire intersection cycle \([V(F,G)]=\sigma\). Repeated components and arbitrary compatible scheme structures are allowed; additional translated components besides the marked quartic are allowed. Nontranslated residual components are outside this locus and serve only as comparison controls.

**Task:** calculate and understand the restrictions of \(H_1,T,S,U\) to this full realization locus; in particular determine whether \(H_1,T,S\) vanish there. Do not assume vanishing, restrict to sign-eigen sources, or substitute the known small-diagonal calculation for this task. No construction of a new obstruction is required as a condition for pursuing the calculation.

With \(H_1\) denoting the positive first projection trace (the negative of the first nonleading coefficient of the monic degree-\(4m\) characteristic polynomial of \(\xi\)), the established identities on this locus are
\[
H_1=T=4M_1=2S=2\operatorname{Res}_{f,g}(ps-qr),\qquad U=0.
\]
Thus the actual calculation concerns the residue or its equivalent trace on arbitrary CI realizations of translated cycles. Special sign-invariant cases are already solved, but universal vanishing remains open. The cycle formula alone does not determine what configurations the CI condition permits.

The small diagonal is a separate, already calculated benchmark: \(H_1(m[C])=4m\ne0\) in characteristic zero. Only after understanding the full CI realization locus should one compare its values with this benchmark. Do not repeatedly redirect investigations to sole support, the existence of a thickening of \(C\), or the search for a new STCI obstruction. The twenty questions below are subordinate to this governing calculation, and remain available for exploration.

### Chow-space separation formulation (governing viewpoint)

Write \(\mathcal A_m=\operatorname{Sym}^m(\mathbb G_m^2)\) for the interior translated-cycle Chow parameter space, of dimension \(2m\). Let \(\mathcal R_{a,b}\) be the actual proper-CI Chow image of degree pair \((a,b)\) in \(\mathcal A_m\), where \(ab=4m\), and \(\mathcal R_m=\bigcup_{ab=4m}\mathcal R_{a,b}\). These are constructible loci, not assumed closed. The objective is to determine whether the regular function \(M_1:\mathcal A_m\to\mathbb A^1\) belongs to the vanishing ideal of \(\overline{\mathcal R_m}\) (closure relative to \(\mathcal A_m\)). Equivalently, is \(\mathcal R_m\subseteq V(M_1)\)? By the established identities we may calculate \(H_1,T,S\) or the first-jet residue instead.

This is a **single-equation separation problem in Chow space**, not a classification of realizability. The small diagonal \(D_m\) is disjoint from \(V(M_1)\) in characteristic zero, since \(M_1(m[(u,v)])=mu/v\). The desired hypersurface separates the full realization locus (and its relative closure) from \(D_m\); it would also certify nonrealizability of every cycle with nonzero moment. It need not distinguish all nonrealizable cycles: the zero set may strictly contain the realization locus. No claim of \(V(M_1)=\mathcal R_m\) is intended.

The known [(4,4) classification](../../arguments/torus/chow_realization_moment_separation.md) illustrates why one condition can be useful without classifying a high-codimension locus: in the eight-dimensional \(\mathcal A_4\) the realization locus has a four-dimensional component and a two-dimensional exceptional nonreduced component, both in the seven-dimensional \(V(M_1)\). General high-codimension estimates remain to be established; they are not needed for this separation question. Existing [transverse Chow moment realization](../../arguments/torus/transverse_chow_moment_realization.md) and [Chow realization and first-moment separation](../../arguments/torus/chow_realization_moment_separation.md) already formulate the separator and establish restricted cases. The current investigation seeks the unrestricted calculation, rather than inventing a new separator or re-solving the reduction.

### Reduction of the original problem

The characteristic-zero STCI nonexistence problem for the fixed rational quartic is reduced, in the sufficient-implication sense, to a single general statement:

**First-moment vanishing conjecture.** Every effective translated-quartic cycle \(Z\) realized by a proper homogeneous complete intersection of two surfaces satisfies \(H_1(Z)=0\).

By the established identities on the full CI realization locus this is equivalent to \(M_1=T=S=0\), or \(\operatorname{Res}_{f,g}(ps-qr)=0\). The condition \(U=0\) already holds for every translated cycle. The small diagonal has \(H_1(m[C])=4m\ne0\) in characteristic zero for every positive integer \(m\), so proving the conjecture excludes all sole-supported pairs at once. The general vanishing conjecture is stronger than the original non-STCI assertion; its converse is not established. The research task is to calculate the invariant on the full CI realization locus, not repeatedly to reduce the original problem or seek separate obstructions.

## Inputs and scope

For the fixed quartic \(C=[s^4:s^3t:st^3:t^4]\), write \([z:x:y:w]=[x_0:x_1:x_2:x_3]\), \(A=xy,B=zw,\xi=A/B,\eta=zy^2/(x^2w)\). A translate \(C_{u,v}=[s^4:s^3t:ust^3:vt^4]\) has \(\xi=u/v,\eta=u^2/v\). The entire translated cycle \(\sum n_i[C_{u_i,v_i}]\) has spectral polynomial \(H(A,B)=\prod(A-\xi_iB)^{n_i}\), first moment \(M_1=\sum n_i\xi_i\). For an actual proper CI \((F,G)\) with that entire cycle, \(AD_{12}=2BD_{03}\) modulo the ideal and \(\operatorname{Res}_{F,G}(D_{03})=2M_1\). First jets along the disjoint center \(L=V(z,w)\) give \(\operatorname{Res}_{f,g}(ps-qr)\). Universal vanishing is **open**, not an established CI consequence. Arbitrary residual curves invalidate the special identity.

Existing owners: [spectral-Jacobian bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md), [boundary modulus](../../arguments/torus/spectral_boundary_modulus.md), [Hilbert symplectic form](../../arguments/torus/chow_hilbert_symplectic_form.md), [ACM parity](../../results/chow_acm_parity_vanishing.md), [intrinsic pencil](../../arguments/torus/quadric_pencil_spectral_intrinsic_geometry.md), [radical recovery](../../arguments/equations/jacobian_radical_support.md), [quotient graph](../../arguments/torus/chow_quotient_fan_and_blowup_comparison.md).

## Research map (preserve all four interconnected directions)

1. **Trace and residue geometry (first).** Marked spectral divisor and first-order trivialization in \(J(\mathbb P^1,2\infty)\); higher boundary jets/moments; moving spectral divisors for arbitrary finite projections. Separate cycle-level trace and symplectic movement from actual dualizing module, CI presentation and central binary Gorenstein fiber. Compare residual contributions and discrepancy \(\mathcal E=\operatorname{Tr}(\xi)-2\operatorname{Res}(D_{03})\); characterize its vanishing and limitations. Study both invariants as functions of proper equation pairs without assuming translated support.
2. **Equation and jet compatibility.** Understand residue as alternating Macaulay pairing and Serre class on \(L\). Expand actual support identities \(H(A,B)\in(F,G)\) and \(AD_{12}-2BD_{03}\in(F,G)\) along \(L\), retaining cofactor corrections. Determine what constraints are genuinely imposed on first jets, not merely what jets compute. Compare Hilbert lifts with central binary CI/Gorenstein fiber and known parity obstruction.
3. **Simultaneous projection geometry.** For sole smooth support all six complementary Jacobian minors lie in the same socle twist \(\omega_C(2)\simeq\mathcal O_{\mathbb P^1}(6)\). Compare their relations for the same actual two equations (including Plucker and Euler relations); projection base divisors and ramification give \(\operatorname{div}W_{ij}=2B_{ij}+R_{ij}\). The complementary pair 03/12 has identical divisor \(3p_0+3p_\infty\) despite degrees 4 and 2. Seek other residue identities with appropriate exceptional corrections, not naive symmetry. Degree list for retained pairs 01,02,03,12,13,23: 1,3,4,2,3,1; base divisors: \(3p_\infty,p_\infty,0,p_0+p_\infty,p_0,3p_0\). Connect to \(J:D_{12}=\sqrt J\), actual socle and the previously used projective line.
4. **Toric realization and descent.** Blow up the four coordinate points and six strict-transformed coordinate lines: the permutohedral threefold resolves all six projections, and refines the product fan for consecutive ratios \(\alpha=x/z,\beta=y/x,\gamma=w/y\). On the product, a translate is \((\alpha,\beta,\gamma)=(r,ur^2,(v/u)r)\), a graph CI of bidegrees \((2,1,0),(1,0,1)\) (multidegrees in the three factors). The quotient characters are \(\xi=\alpha/\gamma,\eta=\beta/(\alpha\gamma)\); \(\xi\) is inverse tangent slope in the alpha-gamma plane and \(\eta\) records weighted second-order contact. Compare opposite endpoint configurations and extreme weight sections on the existing quotient graph. The permutohedral refinement alone does not separate the weighted endpoint configurations; further rays of weights \((1,2,1)\) and opposite in product coordinates are relevant. Track strict transforms, exceptional scheme structure and descent of the SAME two divisors; graph CI upstairs does not imply STCI downstairs.

## Explicit checklist of the original 20 questions

The four directions above consolidate, rather than replace, these individual investigations.

### Spectral geometry
1. Marked spectral divisor: first-order triviality at infinity.
2. Generalized Jacobians: higher boundary moduli and moments.
3. Moving spectral divisors: characteristic polynomials over the projection base for arbitrary intersections.

### Residue and first jets
4. First-jet compatibility: geometric meaning of the vanishing residue pairing.
5. Serre duality on the disjoint line: meaning of the connecting class of the jet determinant.
6. Actual equation constraints: expand the spectral and Jacobian ideal memberships along the disjoint line.

### General intersections and residual components
7. Residual contributions to the spectral trace and differential residue separately.
8. Trace–residue discrepancy: what its vanishing does and does not detect.
9. Space of equation pairs: compare trace and residue before imposing translated support.

### Finite algebras and Hilbert schemes
10. Separate the CI condition from the cycle condition for traces, symplectic forms and dualizing modules.
11. Symplectic movement: what restrictions does a global two-equation realization impose?
12. Central Gorenstein fiber: constraints on possible movements and extensions.

### Six coordinate projections
13. Common sextic geometry: all six Jacobian minors simultaneously.
14. Projection compatibility: relations among minors of the same two surfaces.
15. Ramification and base divisors: explain the coincidence for the complementary 03/12 projections.
16. Other residue identities: account for exceptional and base contributions.

### Toric blowups and product model
17. Permutohedral resolution: study all six projections on a common space.
18. Endpoint tangent configurations: spectral direction and quadratic contact in the product.
19. Opposite endpoint compatibility: compare configurations and extreme weight sections.
20. CI descent: determine what prevents the product graph CI from descending without residual support.

## First probe: projective differential trace (elementary, awaiting independent review)

Let \(Y\) be any pure curve avoiding \(L\), with cycle \(\sum n_i[Y_i]\). Work on the normalizations of the reduced components and use the finite separable maps to \(P=\mathbb P^1_{[z:w]}\). The pullback of \(\mathcal O_P(1)\) equals \(\mathcal O_{Y_i}(1)\) pulled to each normalization. The ambient twisted forms \(\theta=x\,dy-y\,dx\) and \(\theta_0=z\,dw-w\,dz\) are sections of \(\Omega^1(2)\). The first pulls back to a regular section of the normalized component's \(\omega\otimes\pi^*\mathcal O_P(2)\); the second comes from the base. Weighted field traces give
\[
 T(Y)=\sum_i n_i\operatorname{Tr}_{k(Y_i)/k(P)}(xy/(zw)),\qquad
 S(Y)=\sum_i n_i\operatorname{Tr}_{k(Y_i)/k(P)}(\theta/\theta_0).
\]
By classical finite duality / trace of regular differentials (Stacks 50.19, https://stacks.math.columbia.edu/tag/0FK6, finite smooth-curve maps are finite syntomic here), the differential trace of \(\theta\) is a global section of \(\omega_P(2)\simeq\mathcal O_P\); thus \(S(Y)\) is constant, even for non-ACM curves. Similarly the trace of \(xy\) is a section of \(\mathcal O_P(2)\), so \(T(Y)=c_{20}z/w+c_{11}+c_{02}w/z\), not generally constant. These are additive cycle invariants, with no CI or Gorenstein condition. On a translated quartic \(\theta/\theta_0=u/(2v)\), \(\xi=u/v\), projection degree four, hence \(T=4M_1,S=2M_1\) for every translated cycle. In particular even the single reduced non-CI quartic has \(S=2\).

For an actual CI missing \(L\), generic socle comparison (or the existing trace-Jacobian identity and implicit differentiation in the reduced case) identifies \(S=\operatorname{Res}_{F,G}(D_{03})\), including multiplicities. The projective construction is another packaging of the existing matrix/Hilbert differential, not a new universal vanishing theorem. It reveals that the *value* of the residue cannot detect CI structures beyond the cycle: the additional CI content is its representation by first jets, or extension of the cone family across the origin through a binary Gorenstein point.

On the dense torus chart \(z=1,w=t,x=a,y=b\), one has \(2\rho-\xi=ab\,d\log(b^2/(a^2t))/dt\), where \(\rho=\theta/\theta_0\). Thus \(T-2S\) is minus the weighted trace of \(ab\,d\log\eta/dt\). A scalar cancellation does not imply pointwise constancy of \(\eta\). Full weighted tests against the generic reduced algebra are a trace-pairing version of existing radical/Jacobian support recognition, not a new obstruction.

Classical inputs: Beauville's Hilbert symplectic form; Cattani–Dickenstein–Sturmfels, [Computing Multidimensional Residues](https://arxiv.org/abs/alg-geom/9404011), trace-Jacobian formula; Stacks trace of differentials above.

### Averaging interpretation (user observation)

Put \(U=\operatorname{Tr}_{\pi}(\alpha\beta\,d\log\eta/d\lambda)\), with the dense chart conventions above. The discrepancy identity is equivalently \(S=(T+U)/2\); that is, \(S\) is the arithmetic mean of the spectral trace and the signed weighted variation trace. If instead the variation trace is defined with a minus sign, the formula is \(S=(T-\operatorname{Tr}_{\pi}(-\alpha\beta\,d\log\eta/d\lambda))/2\). Keep the sign convention explicit: \(T-2S=-U\). This is an average of two trace values, not a trace normalized by degree. On translated support \(U=0\) componentwise; for general cycles its trace can cancel. Investigate the geometry of this averaging before assuming vanishing of either summand.

## Residual control (verified elimination; no claim of a general residual theorem)

Take \(F=x^4-z^3w+zx(zw-xy),G=y^4-zw^3+wy(zw-xy)\). The pair misses \(L\); its residue is 1 by the first jets in the binary algebra \((x^4,y^4)\). On \(zw\ne0\) put \(\alpha=x/z,\beta=y/w,\lambda=w/z,T=\alpha\beta\). Both \(\alpha,\beta\ne0\). Multiplying the equations gives \((T-1)(T^3+2T+1-\alpha-\beta)=0\). First branch is \(C\), generically reduced. Residual branch is the irreducible quadratic \(\alpha^2-(T^3+2T+1)\alpha+T=0\) with \(\lambda=\alpha^4/(1+\alpha(T-1))\) on a dense open; discriminant \((T^2+T+1)(T^4-T^3+4T^2-T+1)\) squarefree. The resultant with \(\alpha^4-\lambda(1+\alpha(T-1))\), divided by \(-\lambda\), is monic with top terms \(T^{12}+T^{11}+7T^{10}+\cdots\), squarefree generically (at \(\lambda=2\) gcd with derivative is 1). At \(T=1\) the undivided resultant is \(\lambda^2-194\lambda+1\), nonzero generically. The only points with \(zw=0\) are the two endpoints. Hence cycle \(C+R\), residual degree 12, trace \(T(Y)=4-1=3\), differential trace \(S(Y)=2-1=1\), discrepancy 1. This is a control outside the entire translated-cycle locus.

## Next bounded probe

Start with an arbitrary actual CI pair with entire translated cycle, not a prescribed small-diagonal cycle. Calculate the first projection trace and residue on this locus using the established support identities and first normal layers; determine the restrictions on their values, including whether they must be zero. Use sign-invariant realizations as known zero controls and nontranslated residual examples only as comparisons. When useful, examine the homogeneous finite-flat embedded family and central binary Gorenstein fiber, but do not replace the calculation by a sole-support extension problem. Retain both possibilities (vanishing and nonvanishing) until proved; independent correctness/generality review required before promotion.
