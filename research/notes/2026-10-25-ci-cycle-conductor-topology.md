# Conductor, topology, and where the genus is stored

Date: 2026-10-25. Status: exploratory contribution to the complete-intersection cycle notebook; new calculations and interpretations below are provisional, pending the package audit. This is geometry of cycles containing the fixed curve, with no STCI objective or canonical promotion.

Throughout the main discussion, the field is algebraically closed of characteristic zero; assertions about Betti numbers use the associated complex curve. Set

\[
C=[s^4:s^3t:st^3:t^4],\quad
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,
\quad Z=V(F,G).
\]

Write \(p=[1:0:0:0]\), \(q=[0:0:0:1]\). The prescribed four-component decomposition and mixed-characteristic flatness are promoted in [STCI-R-0021](../results/quartic_mu4_degeneration.md); its [source note](2026-10-23-quartic-characteristic-conormal.md), Section 1, supplies the endpoint contact calculation. These established inputs are used without rerunning their proof. The ruled cubic used for a competing example below comes from [the independently reviewed provisional cubic-scroll note](2026-10-24-cubic-scroll-normalization.md); that geometry has not been promoted canonically.

## 1. An intuitive starting point: the same genus in different places

A useful picture is that arithmetic genus is a budget. It can live in the genera of normalized components, in loops made by gluing components, or in higher-order infinitesimal gluing invisible to the underlying topology. The special curve puts a striking amount into the third account.

At \(p\), eliminating the smooth equation \(F\) gives the plane germ

\[
f(u,y)=y^4-u^{12}=0,
\]

where \(u=x_1\), \(y=x_2\). Its four branches are \(y=\zeta u^3\), \(\zeta^4=1\). A pair of branches has contact three, so

\[
\delta_p=\sum_{i<j} I_p(C_i,C_j)=6\cdot3=18.
\]

The same calculation holds at \(q\). Consequently

\[
\delta(Z)=36,\qquad
p_a(Z)=\sum_i g(C_i)+\delta(Z)-4+1=33.
\]

This number also follows from the complete-intersection formula. Its meaning here is particularly transparent: all four normalized components are rational, and all the arithmetic genus arises from the way they are attached.

Let \(D=C_{-1}\cup C_i\cup C_{-i}\) be the residual union to \(C=C_1\). At either endpoint, its three pairwise contacts contribute \(3\cdot3=9\), so \(\delta(D)=18\) and \(p_a(D)=18-3+1=16\). Meanwhile

\[
C\cap D=9p+9q,\qquad \operatorname{length}(C\cap D)=18.
\]

Thus

\[
33=p_a(C)+p_a(D)+18-1=0+16+18-1.
\]

This is a promising deformation picture: a nearby smooth residual curve of genus sixteen would trade its eighteen units of singularity defect for intrinsic genus, while the marked attachment divisor on \(C\) retains total degree eighteen. The genus is moving from gluing to handles, without changing the Hilbert polynomial.

The residual genus is **sixteen**, not seventeen. The liaison difference is
\((4+4-4)(12-4)/2=16\); the union formula above is an independent check.

## 2. The boundary is canonical, but its total degree is already forced

For a reduced Gorenstein curve \(W\) with normalization \(\nu:\widetilde W\to W\), write \(B\) for the conductor divisor upstairs. The relation

\[
\nu^*\omega_W\simeq\omega_{\widetilde W}(B)
\]

says that the conductor is exactly what turns ordinary differentials on the normalization into dualizing differentials on the singular curve. For this particular plane germ, the standard residue generator is

\[
\frac{du}{f_y}=\frac{du}{4y^3}.
\]

On a branch \(y=\zeta u^3\), it has a pole of order nine. This explains the exponent nine in differential language: each branch is separated from three others to order three, and the product of those separations vanishes to order nine.

Globally, \(\omega_Z=\mathcal O_Z(4)\). On each quartic normalization,

\[
\nu^*\omega_Z|_{C_\zeta}=\mathcal O_{\mathbf P^1}(16)
 =\omega_{\mathbf P^1}(9p+9q).
\]

The total boundary degree on the four normalizations is \(4\cdot18=72=2\delta(Z)\). This is not a mysterious extra numerical coincidence; it is the Gorenstein conductor-degree identity in this explicit example.

For any reduced \((a,b)\) complete intersection containing \(C\) as a component of multiplicity one, the same restriction calculation forces the boundary on the smooth marked branch to have degree

\[
\deg B_C=\deg(\omega_W|_C)-\deg\omega_C
 =4(a+b-4)+2=4a+4b-14.                 \tag{1}
\]

For \((4,4)\), the answer is always eighteen. Therefore the *degree* of the marked boundary cannot detect specialness within the reduced fixed-degree locus. Its distribution can: eighteen distinct simple attachments and \(9p+9q\) are very different divisors of the same degree.

There is another distinction worth preserving. On a nodal \(C\cup D\) with \(D\) smooth of genus sixteen and eighteen transverse intersections, the full conductor degree is thirty-six, not seventy-two. Its eighteen points on \(C\) are matched by eighteen points on \(D\). At \(Z\), the residual curve has its own singularities, producing the additional boundary. The marked boundary on \(C\) sees the attachment to the residual curve but does not recover the residual curve's internal singularity defect.

This makes \(B_C\) a good marked invariant and an incomplete invariant of the total curve. A proposed ordering using only \(B_C\) must expect large fibers.

## 3. The topology is much simpler than the arithmetic genus suggests

Topologically, a high-order tangency still glues the same points as an ordinary gluing. The normalization consists of four spheres, and at each endpoint four points are identified. The bipartite incidence graph has four component vertices, two singular-point vertices, and eight branch edges. Its first Betti number is \(8-6+1=3\).

The complex curve therefore has

\[
b_0(Z)=1,\quad b_1(Z)=3,\quad b_2(Z)=4,\quad\chi_{\rm top}(Z)=2.
\]

The Euler characteristic is the same as that of the smooth rational curve \(C\). This is a genuinely surprising failure of a plausible proximity statistic: Euler characteristic alone would place them together even though one has four irreducible components and three independent topological loops. Keeping the full Betti vector separates them.

The following comparison is a picture of possible fibers, not an assertion that all deformations are topologically equivalent to the second row.

| Complex curve | Normalization | Total delta | \(b_1\) | \(b_2\) | Euler characteristic |
|---|---|---:|---:|---:|---:|
| Special \(Z\) | Four copies of \(\mathbf P^1\) | 36 | 3 | 4 | 2 |
| Nodal \(C\cup D\), \(D\) smooth genus 16, 18 attachments | \(\mathbf P^1\amalg D\) | 18 | 49 | 2 | -46 |
| Smooth \((4,4)\), allowing \(C\) to disappear as a component | Smooth genus 33 curve | 0 | 66 | 1 | -64 |
| Reduced characteristic-two support of prescribed fiber | One \(\mathbf P^1\) | 0 | — | — | — |

The last row is algebraic, so complex Betti numbers are deliberately not assigned. Its underlying reduced curve is rational; the full characteristic-two scheme still has the complete-intersection Hilbert polynomial and arithmetic genus thirty-three. Reduction has forgotten that arithmetic information.

The local Milnor number at either endpoint in characteristic zero is

\[
\mu=(4-1)(12-1)=33=2\delta-r+1.
\]

Thus a full smoothing trades \(66\) units of local vanishing-cycle complexity against Euler characteristic: \(2-66=-64\). In a nodal marked deformation the eighteen remaining nodes leave Euler characteristic \(-64+18=-46\). A drawing of four highly tangent rational curves can conceal a large reservoir of vanishing cycles.

This also warns against a naive family of normalizations. Four rational normalizations do not simply deform as four disjoint rational curves into the normalization \(\mathbf P^1\amalg D\) of a nodal marked deformation. Normalization need not commute with the family. In suitable reduced families over a normal one-dimensional base, delta-constancy is tied to simultaneous normalization; see [Greuel–Pfister, *The delta invariant and fiberwise normalization*, 2022](https://www.journalofsing.org/volume25/greuel-pfister.pdf). Their precise hypotheses concern isolated non-normal singularities and the relevant flat/finite setup. They do not license applying the classical finite-delta picture to a fiber nonreduced along its entire curve.

## 4. A refined genus ledger: generalized Jacobians

For a connected reduced proper curve over an algebraically closed characteristic-zero field, the generalized Jacobian has an abelian quotient from the Jacobians of its normalized components, a torus from the gluing graph, and an additive contribution from the higher-order gluing. The normalization units sequence gives the concrete calculation here. For the general framework separating the maximal torus and the unipotent part, see [Geisser, *The affine part of the Picard scheme*, corrected version](https://arxiv.org/html/0704.0479v4), Theorems 1 and 3.

At an endpoint of \(Z\), the local unit quotient has dimension \(\delta_p=18\). Its torus dimension is \(r_p-1=3\); the remaining fifteen dimensions are unipotent. At the two endpoints these give six torus dimensions and thirty additive dimensions. Dividing by the three independent rescalings of four normalized components leaves a torus of dimension three. Since the normalized Jacobians vanish, the result is, noncanonically,

\[
\operatorname{Pic}^0(Z)\simeq\mathbf G_m^3\times\mathbf G_a^{30}.
\]

The split expression is characteristic zero only. The count \(3+30=33\) recovers the arithmetic genus.

For a nodal \(C\cup D\) as in the table,

\[
0\longrightarrow\mathbf G_m^{17}\longrightarrow
\operatorname{Pic}^0(C\cup D)\longrightarrow
\operatorname{Jac}(D)\longrightarrow0.
\]

Here the gluing graph has two vertices and eighteen edges, hence seventeen cycles. There is no additive part because the singularities are nodes. The dimensions now read \(17+16=33\).

This suggests recording a vector

\[
(\text{abelian dimension},\text{torus rank},\text{unipotent dimension})
\]

instead of a single genus. Its values in the three characteristic-zero pictures are

\[
Z:(0,3,30),\qquad C\cup D:(16,17,0),\qquad
\text{smooth CI}:(33,0,0).
\]

The first coordinate measures handles on the normalization; the second measures topological gluing loops; the third measures infinitesimal contact. This is an appealing way to articulate “exceptionally close to rational components”: almost all of \(Z\)'s genus is additive contact data. It is not yet an ordering, and none of the three coordinates should be asserted to vary monotonically in every family. Degenerations can exchange them.

## 5. A symmetry principle for the boundary, and a toric shadow

The embedded curve has the explicit torus action \(u\mapsto\lambda u\), realized by

\[
[x_0:x_1:x_2:x_3]\longmapsto
[x_0:\lambda x_1:\lambda^3x_2:\lambda^4x_3],
\]

and the endpoint-swapping coordinate reversal. These preserve the four-curve configuration. No classification of the full automorphism group is needed for the following observation: an effective degree-eighteen divisor invariant under this torus must be supported at \(p,q\), and endpoint swap then forces it to be \(9p+9q\).

Thus \(B_C\) is the unique degree-eighteen boundary invariant under these visible symmetries. This is a precise and modest extremality principle. It explains the balanced endpoint concentration without claiming that the complete intersection itself is unique among configurations having that boundary.

The reduced boundary provides another useful change of viewpoint:

\[
(\mathbf P^1,p+q)\quad\text{has}\quad K_{\mathbf P^1}+p+q\sim0.
\]

It is the standard toric compactification of \(\mathbf G_m\). On the open torus the prescribed family is \(\mathbf G_m\times\mu_4\), so the same two points are simultaneously the compactification boundary and the locus of conductor concentration. There is a toric/logarithmic shadow of the configuration.

One must retain the coefficient distinction. The actual canonical conductor is \(9p+9q\), giving \(K+B\) degree sixteen; the reduced toric boundary gives degree zero. Passing from one to the other discards contact order. A logarithmic model with only reduced boundary therefore needs additional contact data, such as decorations of order nine or the pairwise order-three separation data, to recover the original geometry.

Possible experiment: study the map from the fixed-degree parameter space to \(\operatorname{Sym}^{18}(C)\) sending a reduced marked intersection to \(B_C\), then examine the fiber over \(9p+9q\). Does the special roots-of-unity configuration occupy an isolated symmetry stratum in that fiber, or are there many different residual curves with the same concentrated boundary? The first possibility would make boundary plus symmetry more selective; the second would identify exactly what further data must be retained.

## 6. A useful competing configuration: larger delta is possible

It would be tempting to call \(\delta(Z)=36\) maximal among all \((4,4)\) intersections containing \(C\). Reducible hypersurfaces already give a reason to resist this conjecture.

Set

\[
Q=x_0x_3-x_1x_2,\qquad R=x_0x_2^2-x_1^2x_3,
\]

and choose planes

\[
\begin{aligned}
L_1&=x_0+x_1+x_2+x_3,\\
L_2&=x_0+2x_1+3x_2+5x_3,\\
L_3&=x_0+7x_1+11x_2+13x_3.
\end{aligned}
\]

Consider the actual \((4,4)\) pair

\[
W=V(Q L_1L_2,\ R L_3).
\]

The factors share no surface component. The Segre parametrization \((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\) gives

\[
R|_Q=ab(bc^3-ad^3),
\]

so \(Q\cap R\) is \(C\) plus the two ruling lines \(a=0,b=0\). The remaining components are the conic \(Q\cap L_3\), two plane cubics \(R\cap L_1,R\cap L_2\), and two lines \(L_1\cap L_3,L_2\cap L_3\).

The two cubic sections are geometrically irreducible and rational. This can be seen directly on the cubic normalization: a plane \(\alpha x_0+\beta x_1+\gamma x_2+\delta x_3=0\) pulls back to

\[
 A(\alpha v_0^2+\delta v_1^2)+B(\beta v_0+\gamma v_1)=0.
\]

For \(L_1\), the two coefficient forms are \(v_0^2+v_1^2\) and \(v_0+v_1\); for \(L_2\), they are \(v_0^2+5v_1^2\) and \(2v_0+3v_1\). Neither pair has a common projective zero, so the inverse plane section is a smooth rational section of the ruling, mapping birationally to the plane cubic. They meet the double line \(x_1=x_2=0\) at \((-1:0:0:1)\) and \((-5:0:0:1)\), respectively. At these non-pinch points their plane equations have a nondegenerate quadratic leading term, hence an ordinary node. An irreducible plane cubic has arithmetic genus one, so its normalization has genus zero. The conic is smooth: eliminating \(x_0\) with \(L_3\) gives \(-x_1x_2-7x_1x_3-11x_2x_3-13x_3^2\), whose symmetric matrix has determinant \(-16\). Thus there are eight rational normalized components, and the normalization sequence gives

\[
\delta(W)=p_a(W)+8-1=33+7=40>36.
\]

The exact finite-ideal check is preserved in [the M2 script](../computations/verify_ci_cycle_eight_component_competitor_2026_10_25.m2). Running

```sh
/opt/homebrew/bin/M2 --script research/computations/verify_ci_cycle_eight_component_competitor_2026_10_25.m2
```

returns degree sixteen, Hilbert polynomial \(16n-32\), equality to the intersection of the eight displayed component ideals, and primality of those eight ideals; their degrees are \(4,1,1,2,3,3,1,1\). This establishes the checked coordinate example. The rationality and delta interpretation use the elementary node/genus argument just given. The calculation is not a classification of any family.

The lesson is productive rather than dismissive: an extremality claim needs a chosen comparison class. Requiring integral hypersurfaces, prescribing the number/degrees of normalized components, fixing symmetry, or comparing the marked boundary could each recover a meaningful question. They are different questions and should remain separate.

## 7. Candidate invariants worth carrying forward

- **Marked boundary distribution.** Total degree is fixed by (1), but support size, endpoint weights, and multiplicity partitions can vary. Concentration is geometrically meaningful, while a numerical concentration score would need a fixed normalization and a decision about endpoint weighting. Without symmetry, a single point of multiplicity eighteen is even more concentrated than \(9p+9q\), if realizable; the latter is special as the balanced symmetric divisor.
- **Residual singularity defect.** For a reduced \(C\cup D\), \(\delta(C\cup D)=\delta(D)+\operatorname{length}(C\cap D)\) when \(C\) is smooth. This separates attachment from internal residual geometry. At \(Z\) the two summands are eighteen and eighteen. Delta is useful for specialization in suitable reduced families, but does not extend by simply reducing a generically nonreduced fiber.
- **Generalized-Jacobian signature.** The vector \((a,t,u)\) distinguishes handles, topological loops, and higher contact. The value \((0,3,30)\) is a concise description of the special arrangement. It captures more than either arithmetic genus or reduced-support topology.
- **Decorated gluing graph.** Four vertices joined at two multi-branch points, with pairwise contact three and conductor weight nine, retains the incidence and the tangency. An ordinary dual graph loses both multiplicities and three-dimensional embedding data. A metric/tropical enhancement could assign lengths from a chosen one-parameter degeneration, but those lengths depend on the degeneration and are not presently intrinsic to \(Z\).
- **Canonical boundary plus visible symmetry.** The pair \((C,9p+9q)\) is canonically meaningful relative to the embedding and has a unique invariant boundary of the forced degree under the displayed torus and swap. Whether the complete intersection is extremal within its boundary fiber remains an attractive, genuinely open experiment.

## 8. Audit and continuation boundary

This contribution separates a promoted input (the prescribed degeneration), reviewed but unpromoted ruled-surface geometry, direct numerical/topological calculations, a finite coordinate computation, and exploratory interpretations. The parent package's independent reviewer should reconstruct the genus sixteen calculation, the generalized-Jacobian ranks, the distinction between marked and full conductor boundaries, and the reduced eight-component competitor. No canonical research result, question, or STCI frontier is changed.

Promising next computations are the boundary-map image, the local marked deformation of \(y^4-u^{12}\) into nine transverse attachments while preserving the branch \(y=u^3\), and the Picard signature along such a global family. The last two require an actual family and should not be inferred solely from compatible numbers.
