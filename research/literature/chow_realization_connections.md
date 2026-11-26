# Literature connections that change the Chow realization question

**Scope.** Focused discovery review, November 26, 2026, for the
characteristic-zero translated rational quartic. Sources were searched
by the actual questions and followed into accessible primary texts.
The transfers below are provisional pending independent mathematical
review; established external theorems retain their stated hypotheses.
No claim of an exhaustive STCI search, novelty, or unrestricted obstruction.
Use the [cycle-first account](../arguments/torus/transverse_coefficient_realization_synthesis.md)
and [Chow framework](../frameworks/chow-realization/index.md) for the
current realization problem.

## Character incidence is an existing wonderful-model problem

De Concini–Gaiffi, [Projective Wonderful Models for Toric Arrangements](https://arxiv.org/abs/1608.08746),
Theorems 7.1, 2.1 and 2.2 (checked arXiv pp. 4, 13–14), construct a
smooth projective toric refinement for a finite arrangement of torus
layers over \(\mathbf C\); the closures and boundary strata form a clean
arrangement. The wonderful blowups associated to a building set have
a simple normal-crossings boundary with incidence described by nested
sets. This is stronger than a general suggestion to use Li's theorem:
the toric refinement ensures the hypotheses for the character layers.

Apply this to \(T^m\), using the four characters \(q,\eta,u=\eta/q,
\alpha=(q\eta)^{-1}\) on each marking. Equality in any pencil and the
nonidentically true triple-concurrence equations from the
[marked account](../arguments/torus/marked_chow_configuration_boundary.md#4-base-discriminants-incidence-contact-and-collisions)
are character equalities, hence finite unions of smooth connected
cosets of subtori over \(\mathbf C\). Intersections require saturation of
the generated character lattice and all compatible torsion components;
the two solutions of \(u,\alpha\) with determinant two illustrate why
a rational hyperplane arrangement alone misses information. A
wonderful model of the complement of these base discriminants exists.
It does not have to be invented.

A useful next comparison is between two arrangements: the base
arrangement in \(T^m\), and the total one in \(T^m\times T\), obtained
by pulling back the base layers and adding \(\chi(s)=\chi(s_i)\) for
each of the four characters and each label. Forgetting the last factor
is the original projection of complements. Choose compatible toric
refinements and building sets, and determine whether the projection
extends to a relative model whose fibers give the desired marked pairs.
The theorem supplies absolute models, not flatness or the stable
relative morphism; one may close the graph for a proper comparison,
but must still analyze fibers. Start with a pair of coalescing markings
and the two sign-partner intersections, retaining both endpoint maps.
The endpoint rank-drop strata are not all character equalities. Do
not assert clean intersection for their union or that this is the
KSBA compactification of the marked surface. The strongest existing
input solves the character-incidence part only.

Moci's [Wonderful models for toric arrangements](https://arxiv.org/abs/0912.5461)
provides the preceding nested-set construction; the projective version
above is the appropriate boundary input. Schaffler–Tevelev
[arXiv:2010.03519](https://arxiv.org/abs/2010.03519), already used in the
[forgetful account](../arguments/torus/marked_arrangement_forgetful_geometry.md),
is the complementary precedent for recovering configurations from
compatible forgetful maps. Neither gives an embedded CI family.

## Multigraded incidence and the limit of projection reconstruction

Osserman–Trager, [Multigraded Cayley–Chow forms](https://arxiv.org/abs/1708.03335),
Theorem 1.1 and Remark 1.2 (arXiv pp. 2–3), treat an irreducible
\(r\)-dimensional variety in \(\prod_{j=1}^k\mathbf P^{n_j}\), not a
product with a whole unused projective factor. For incidence with
products of linear subspaces of codimensions \(\beta_j\), summing
to \(r+1\), the incidence hypersurface determines the variety iff
\(\dim p_I(X)\ge\sum_{i\in I}\beta_i\) for every proper nonempty
subset \(I\). In particular \(k\le r+1\) is required; in characteristic
zero the incidence multiplicity is one under the theorem's conditions.

Our graphs in \((\mathbf P^1)^3\) illustrate the failure of a *single*
multigraded Chow form to recover a general three-factor curve: two
point conditions omit a coordinate. For a graph in two factors with
both projections nonconstant, the theorem applies. This distinguishes
the paired projection equations from a single faithful coordinate.
The theorem is about unrestricted subvarieties, not a nonreconstruction
result for our special graph locus. Use the existing monomial transition
identities to ask when compatible two-factor incidences recover the
*same pairing* of components, with the full Chow form as a control.
No new calculation of spectral moments is required. This is the
precise dimension issue behind the
[product models](../arguments/torus/transverse_chow_product_models.md).

Pratt–Sodomaco–Sturmfels, [Multigraded Hurwitz forms](https://arxiv.org/abs/2602.19563),
Theorems 3.4 and 4.1 (checked p. 11), offer the corresponding
multigraded transversality/discriminant invariants. The generic-CI
degree formula uses generic multihomogeneous equations; our
constrained graphs and repeated schemes are not generic CI models
in these products. Use it as a comparison for the projected
discriminant on the appropriate irreducible, generically transverse
model, not a general obstruction to our realization problem.

## The actual source parameter space

Benoist, [On the birational geometry of the parameter space for
codimension 2 complete intersections](https://arxiv.org/abs/1212.4862)
(v2, January 2026, Introduction, Theorems 0.6 and 0.8,
Corollary 0.10 and §0.3, checked pp. 1–4), works over an algebraically
closed field. The proper-CI locus is an open subset of the
degree-labeled projective bundle in unequal degrees (or a
Grassmannian in equal degrees). The first contraction of the
unequal-degree ambient parameter space has an explicit common-factor
locus. The full MMP statements are confined to the indicated
degenerate cases (not general \(N=3,a,b\ge2\)). In the binary
homogeneous punctual case \(a<b\) complete curves of proper CI ideals
exist. The compactification retains all graded Hilbert pieces and
gives a useful model of movement even with constant support.

This directly strengthens our way of thinking about the
[plane-generator bundles](../arguments/torus/plane_pencil_equation_bundles.md):
the map to a moduli space of ideals is different from a global frame
of generators. The binary control has constant support but moving
ideals, and cannot be obtained by a nonconstant complete curve in
the ordered product of polynomial projective spaces avoiding the
ample resultant divisor. The degree-adapted quotient is crucial.

The [equal-degree Chow fiber comparison](../arguments/torus/chow_realization_moment_separation.md#source-parameter-space-and-equal-degree-chow-fibers)
is a small project-specific transfer: the line resultant gives a
linear system in the ample Plücker power on the Grassmannian of
pencils, so the proper-CI-to-Chow map is affine there. A nonconstant
complete family with a fixed Chow point cannot stay inside that
proper-pencil locus. This is a geometric explanation of why a
fixed-cycle Hilbert compactification needs non-CI limits; it is
not a way to force a proper invariant limit. In unequal degrees,
track the two tautological generator lines and the actual resultant
base ideal instead of assuming the same ampleness. Compare these
spaces with the existing
[common-quadric resultant graph](../arguments/equations/common_quadric_resultant_blowup.md);
Benoist's birational contractions are not automatically that graph.

A bounded useful next question is whether a known moving punctual
family in Benoist's model can be completed to the required full
plane-CI family with the endpoint piece, and what the degrees of
its minimal-generator lines then are. Use the actual non-invariant
quartic pair as a comparison; do not infer a global realization
from the punctual family alone. The problem is source descent,
not another classification of all local complete intersections.

The source argument also compares the resultant class \(\mathcal O(b,a)\)
with Benoist's explicit nef cone: for \(1<a<b\) it is outside that cone
on the compact equation bundle. This locates the exact obstruction to
transferring the equal-degree affineness proof; it is not a proof of
nonaffineness of the unequal-degree proper locus or its Chow fibers.

## Enriching Chow with a limiting discriminant

Sturmfels, [The Hurwitz Form of a Projective Variety](https://arxiv.org/abs/1410.6703),
§3 Proposition 3.4 (checked p. 7) recalls Katz's explicit calculation
for a generic pencil of plane curves \(f^n+\epsilon g\): the limiting
dual is \(n[f^\vee]\) together with the dual lines of the
\(f=g=0\) base points, each with weight \(n-1\), under the genericity
conditions. Even the fixed special scheme \(f^n=0\) does not determine
this limit. The original Katz paper
[Tangents to a Multiple Plane Curve](https://msp.org/pjm/1986/124-2/pjm-v124-n2-p05-s.pdf)
is accessible; §1 Proposition 1.2 states the smoothness,
transversality and generic dual hypotheses. Esteves–Medeiros–Sousa,
[Limits of dual curves via foliations](https://arxiv.org/abs/1909.08647),
extend ramification limits to plane Zeuthen families of higher type;
the publisher's displayed Corollary 6.2 gives the first-order
formula when the first perturbation is coprime to every multiple
component. The arXiv PDF was unavailable in this session; do not
claim verification of its full proof.

There is a particularly relevant source-side formula:
Busé–Nonkané, [Discriminants of complete intersection space curves](https://arxiv.org/abs/1702.01694),
Theorem 1 and Corollary 2, checked pp. 2–3. For two homogeneous
forms \(F,G\) with degree sum at least three, their universal
identity factors a resultant involving two Jacobian minors into
the discriminant of the pair, a directional derivative resultant,
and the discriminant of a plane section. It holds over arbitrary
commutative coefficient rings. In the current problem the same
minors already appear in the spectral–Jacobian and endpoint
residue arguments. This gives an actual source formula relating
global singularity and sectional degeneration rather than a
cycle-only differential test. At a singular or thick special fiber
both sides may vanish: use a smoothing parameter and valuations,
not division by specialized zero factors.

For reduced arrangements the normalization trace/discriminant
comparison in the [endpoint different](../arguments/torus/chow_endpoint_different.md)
already detects endpoint lengths. Do not count that budget as
a new obstruction. Also do not apply Sturmfels §4 equation (7)
literally with maximal-ideal multiplicity at the shared tangent
endpoints: a line tangent to a conic, smoothed to a cubic, gives
degrees \(2+2=4\) under that reading rather than the expected
six. The ordinary multiplicity-two description is insufficient
for a tacnode. Use the full different/ramification length or the
precise plane class formula; the discrepancy must be resolved
before using the reduced-limit formula in our high-contact case.

For a nonreduced actual pair, investigate the normalized first
nonzero coefficient of the hyperplane-section discriminant
under an explicit smoothing of the same homogeneous pair.
Use a known repeated translated-cycle control and compare two
smoothing directions, retaining the actual Jacobian and
projection corrections. Generic projection of a space curve to
a plane introduces additional nodes, so Katz's plane formula
does not simply apply to the projected cycle. The source-sensitive
question is which divisors are forced by the actual equation
ideal or its permitted deformations, versus which depend on
the arbitrary smoothing. Stop if the result merely recovers
the known endpoint index or arbitrary perturbation data.
This may supply a useful enriched Chow boundary without assuming
that the ordinary Chow form remembers a thick scheme.

## The Capelli lead and a rigorous limit on the substitute

Méo, [Chow forms and complete intersections in the projective space](https://doi.org/10.1016/j.bulsci.2024.103505),
Theorem 2 in §4.2, is the closest title to the desired direct
CI criterion. The accessible publisher preview states a rank-one
Hermitian condition on operators obtained from applying Capelli
derivatives and conjugate derivatives to \(\log|f_Z|\), in the
complex setting, for an irreducible algebraic cycle. The full
text was not accessible; searches for an arXiv/author preprint
did not locate one. In particular it remains unverified how the
article defines a complete intersection, handles singular points
of the Chow divisor, treats multiplicity, or obtains global
homogeneous equations. Do not apply the displayed condition to
\(m[C]\) or infer a proof of STCI.

An accessible algebraic comparison is Kohn,
[Coisotropic Hypersurfaces in Grassmannians](https://arxiv.org/abs/1607.05932),
Theorem 14 and §5 (checked pp. 9–13), giving the GKZ rank-one
conormal characterization of associated hypersurfaces of
irreducible projective varieties and reconstruction of the
underlying variety. This first-order rank-one condition on the
smooth locus is automatic for the Chow hypersurface of *any*
irreducible curve, including \(C\) itself. It cannot distinguish
CI realizability among the already known Chow forms. For a
power \(R_C^m\) the ordinary gradient vanishes along the support
for \(m>1\); taking the squarefree part restores the old test,
not the lost thick structure. Méo's Hermitian current condition
is different; a connection between the two requires reading
the actual proof, not identifying them by the words rank one.
This is a productive negative filter on the proposed search.

Ross, [The Hilbert-Chow morphism and the incidence divisor](https://arxiv.org/abs/1009.5898),
Theorem 1.1 (checked p. 2), constructs an incidence Cartier
divisor on the closure of the disjoint locus for complementary
cycle dimensions summing to ambient dimension minus one; it is
effective on component products with properly intersecting
universal cycles, and the associated determinant line descends
from Hilbert data. For curves and lines in \(\mathbf P^3\) this
is the incidence line already used by the Chow resultant. This
explains why a determinant known to descend in this way cannot
distinguish two Hilbert lifts with the same cycle. The relevant
new discriminant/generator comparison must retain information
*not* descending to that incidence line. This is a distinction
between functorial constructions, not a general claim that no
cycle-only realizability criterion exists.

## Research decision

The strongest immediately transferable construction is the
character-layer wonderful model; the most directly source-sensitive
new comparison is the limiting sectional discriminant and its
source factorization. The actual CI parameter-space geometry
helps separate what can be compactified from what has to leave
the proper locus. The multigraded theorem gives a principled
limit on single-projection reconstruction. These complement,
rather than replace, the existing sign-source, carrier and
whole-family realization routes. They do not prove UM1 or
resolve the repeated-cycle lifting question. The
[existing queue](../investigations/proof-audit/knowledge-gain-priorities.md#concrete-alternatives-within-and-beyond-chow)
records bounded next comparisons without imposing a new ranking.
Further synthesis should evaluate the outcomes of those actual
geometric tests, not collect more citations.
