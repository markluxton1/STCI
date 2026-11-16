# Genus-two bisections and conductor geometry

[Carrier Framework](index.md) · [Original section addresses](quartic_proof_interfaces.md)

## 1. Genus-two bisection: global ribbon contradiction and distinct conductor algebra

In characteristic zero, the bisection second-pencil reduction gives the actual Cartier equivalence \(2c\sim2H\) on the normalization. The resulting pure Cartier double is a ribbon with nilideal \(\mathcal O_{\mathbf P^1}(-8)\). Its generically nonzero ambient conormal map would be
\[
\mathcal O_{\mathbf P^1}(-7)^{\oplus2}\longrightarrow\mathcal O_{\mathbf P^1}(-8),
\]
which is impossible. The [complete bisection proof](../../arguments/carriers/genus_two_bisection_proof.md) establishes the second pencil, purity, Hilbert-polynomial calculation, and nonzero map; the [quartic-carrier assembly](../../arguments/carriers/quartic_carrier_proof.md#61-bisection-the-global-nilideal-obstruction) uses this to exclude the entire bisection lane, without a mate-degree bound.

A **different, conditional** quadratic-descent calculation survives as a reusable conductor-power lemma: with \(w^2=\delta\) and \(Q|_D=m+w\), descent of a positive power (after excluding \(m=0\)) forces \(\delta=r^2\), \(m=\alpha r\), and \(((\alpha+1)/(\alpha-1))^n=1\), with \(\alpha\notin\{0,\pm1\}\). These are necessary conditions under the hypothetical bisection setup, not surviving STCI cases. See the [complete split-conductor argument](../../arguments/carriers/genus_two_bisection_descent.md).

## 2. Entire genus-two conductor and ambient conic model

The [entire-conductor proof](../../arguments/carriers/genus_two_entire_conductor_proof.md) establishes rational singularities without assuming a Cartier or \(\mathbf Q\)-Cartier canonical class, identifies the **actual** conductor via finite duality, and proves that its downstairs scheme is a reduced line \(\Gamma\). The whole upstairs conductor is a rank-two finite-flat algebra
\[
p_*\mathcal O_D=\mathcal O_\Gamma\oplus\mathcal O_\Gamma(-2),
\]
including singular or nonreduced fibers; its quadratic multiplication is a quartic section. These scheme-level conclusions cannot be replaced by reduced Jacobian support.

The [ambient conic-model proof](../../arguments/carriers/genus_two_ambient_conic_model_proof.md) identifies the two line equations with the complete basepoint-free adjoint pencil, proves the exact pulled-back line ideal, and constructs the integral strict transform \(T\sim4H_B-2E_B\) in the blowup along \(\Gamma\). Proper trace and crepancy make \(T\) normal Gorenstein ADE. **This does not assert** that the original normalization \(S\) is Gorenstein or that its pencil descends through horizontal contractions. The [assembly](../../arguments/carriers/quartic_carrier_proof.md#6-sectional-genus-two-conic-geometry-and-the-two-correction-strata) uses these as proved inputs.

## 3. Genus-two conductor-line positions on the fixed quartic

Under the accepted genus-two blowup and mate-stratum hypotheses, the conductor line \(\Gamma=V(t_0,t_1)\) and basepoint-free adjoint pencil satisfy \(t_i=g s_i\), with \(\operatorname{div}(g)=D_M\sim-K_M\). Hence the **scheme-theoretic** contact length is
\[
\tau=\operatorname{length}(C\cap\Gamma)=D_M\cdot c^\#=4-f\cdot c^\#.
\]
It is two in the \(\lambda=0\) stratum and three in the \(\lambda=1\) stratum, including nonreduced contact. The unique quadric \(q=x_0x_3-x_1x_2\) contains every length-three secant line. In characteristic zero, trisecant contact is either three distinct points or a triple endpoint, never \([2,1]\); no line meets \(C\) in length four. The [complete line classification, field-orbit distinctions, and exact carrier ideal](../../arguments/carriers/genus_two_trisecant_carrier_proof.md#1-all-trisecant-lines-their-actual-intersection-schemes-and-field-orbits) and the [ordinary bisecant and tangent equations](../../arguments/carriers/genus_two_trisecant_carrier_proof.md#13-ordinary-bisecants-tangent-contact-and-explicit-line-equations) are authoritative.

Three intersections of \(C\) with \(\Gamma\) do **not** imply three branch points of the residual conductor double cover: horizontal components can meet the strict curve through ADE chains and be contracted, identifying points downstairs. The all-length chain argument remains necessary. Also the adjoint-pencil argument yields \(h^0(M,-K_M)=1\), **not** \(h^0(M,-nK_M)=1\) for all \(n\); the mate correction may have fractional coefficients.

## 4. Bisection fiber counts: integral descent and the three-center obstruction

These are separate characteristic-zero, second-pencil **conditional** obstructions, not substitutes for the global ribbon proof. On the four-blowup model, with entire fibers \(F_t\), center counts \(k_t\), and relative canonical terms \(R_t\),
\[
Z_t=\frac{k_t}{2}F_t-R_t,\qquad c\cdot Z_t=k_t,\qquad \sum_t k_t=4.
\]
For positive even \(k_t\), the full exceptional correction is integral and supported on complete connected exceptional graphs. The descent of \(\mathcal O_M(c+Z_p)\) makes the smooth embedded curve Cartier at a singular downstairs point, a contradiction. This excludes partitions \([4]\), \([2,2]\), and \([2,1,1]\), including infinitely near centers and nonreduced fibers. The [bisection proof](../../arguments/carriers/genus_two_bisection_proof.md) is the primary source for the global exclusion; the even-fiber descent is a conditional refinement.

The distinct [three-center analysis](../../arguments/carriers/genus_two_bisection_three_center_proof.md) classifies all permitted original fiber types and forced exceptional graphs for \(k_t=3\): \(A_3\), \(D_4\), or \(D_n\) (\(n\ge5\)). The nonreduced \(D_n\) case satisfies the rational intersection equations, so numerical negativity alone does not exclude it. An **integral anti-nef uniformizer cycle** with contact coefficient one fails at the trivalent fork. Thus \([3,1]\) is excluded within that conditional argument, leaving \([1,1,1,1]\) at this stage. The focused proof preserves the exact center histories and coefficient calculations.

## 5. Genus-two marked section case

### Free-chain exclusion when the marked prime is absent

Under the characteristic-zero marked-section and smooth-descent hypotheses, absence of the horizontal degree-zero prime \(B=e_0-e_i-e_j\) forces free chains. The one-horizontal-line case contradicts the integral anti-nef contact coefficient bound; the two-line equality case has \(h\cdot Z=1\), contrary to \(h\cdot Z=3\). The [complete free-chain and line-budget proof](../../arguments/carriers/genus_two_marking_and_section_proof.md#8-free-chain-proof-when-the-marked-prime-is-absent) includes the proximity classification, Schur-complement inequalities, integral cycle test, equality case, and counterexamples to tempting shorter bounds. Its conclusion does not cover configurations with \(B\) present.

### Marked constraints and the case with the horizontal prime

For the genus-two section stratum \(\lambda=1\), the plane marking gives
\[
c^\#=h,\quad L=4h-2e_0-\sum_{i=1}^8e_i,\quad
f=h-e_0,\quad Z=L-h=3h-2e_0-\sum_{i=1}^8e_i,
\]
with \(Z\) effective, exceptional, \(K\cdot Z=1\), and \(Z^2=-3\). The vertical root lattice is \(D_8\). The marked blowup clusters and proximity relations are part of the geometry: they cannot be replaced by an arbitrary abstract ADE graph. A candidate horizontal degree-zero exceptional prime is \(B=e_0-e_i-e_j\); when it is present, a satellite can attach it to an **internal** vertex of an \(A\)-chain. A blanket three-arm-star classification is therefore false.

The preceding free-chain exclusion therefore implies that any surviving \(\lambda=1\) configuration must contain \(B\). The free-child and one-satellite graphs with \(B\) present are **not excluded by this marked-lattice argument alone**; neither a reduced-conductor shortcut nor the invalid universal star bound excludes them. This is a boundary of the marked-model method, **not an open case of the assembled quartic-carrier theorem**: the [actual nonendpoint](../../arguments/carriers/genus_two_nonendpoint_proof.md) and [endpoint](../../arguments/carriers/genus_two_endpoint_proof.md) equations close the section lane under the ambient conic-model hypotheses. [Marked-model derivation](../../arguments/carriers/genus_two_marking_and_section_proof.md).
