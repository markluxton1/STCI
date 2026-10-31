# Affine/projective scope and explicit literature counterchecks

These proofs separate homogeneous projective equations from affine equations, a line-bundle condition on the curve from a divisor-class condition on a carrier, and an embedded lifting problem from a splitting claim. They preserve useful mathematical counterexamples from a bounded literature assessment. The precise preprint audit concerns **arXiv:2511.07589v1**, Theorem 4.2 Step 3 and the unrestricted Theorem 4.4 as formulated in that version; it is not a claim about an uninspected later revision. No counterexample below is asserted to settle projective STCI over an algebraically closed field.

The established affine lci and projective bundle-section constructions, with theorem-level primary sources, are integrated in [the global-equations account](../synthesis/global_equations_and_constructions.md). The fixed quartic has an [explicit quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier); that fact needs no unverified transfer from a broad affine theorem.

## What the positive-characteristic literature actually supplies

Moh's [official abstract](https://doi.org/10.1090/S0002-9939-1985-0784166-1) states affirmative results for projective monomial curves in positive characteristic and, separately, for a curve admitting a birational linear plane projection with center **disjoint from the curve** and only cusps in its image. The bounded source assessment verified the publisher's indexed abstract, not the full proof, a theorem number or a generalized meaning of cusp. In particular it supplied no theorem asserting that every projective curve admits such a projection. The internal cuspidal projection in [the rational-quartic construction](RATIONAL_QUARTICS_IN_POSITIVE_CHARACTERISTIC.md) is instead justified by its own full proof.

The earlier Barile–Morales–Thoma [2000 publisher abstract](https://doi.org/10.1006/jabr.1999.8195) states a constructive positive-characteristic STCI theorem for simplicial affine or projective toric varieties **with full parametrization**. Neither hypothesis may be discarded; the abstract-level assessment did not verify the detailed definition needed for a new application. The direct fixed-quartic application in [the construction chapter](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md) uses the independently verified 2002 article instead.
 The same 2000 abstract separately reports weaker almost-STCI results in arbitrary characteristic; those statements are not converted here into STCI assertions or results for arbitrary projective curves.

Published Mandal–Zinna papers and the audited preprint have distinct scopes. The [J. Algebra 690 (2026), 101–113 abstract](https://doi.org/10.1016/j.jalgebra.2025.10.042) concerns affine threefolds over characteristic-zero C1 fields, with trivial conormal and a torsion Grothendieck-class hypothesis. The separate [J. Algebra 693 (2026), 36–53 abstract](https://doi.org/10.1016/j.jalgebra.2025.12.026) concerns a conditional smooth-affine-surface result over the algebraic closure of a finite field, again with trivial conormal and a torsion Grothendieck-class hypothesis. These abstract-level scope assessments do not establish any projective transfer. The counterchecks below address specific displayed claims and proof steps of arXiv:2511.07589v1; they do not conflate those claims with either published conditional theorem.

Cowsik–Nori, *Affine curves in characteristic p are set theoretic complete intersections*, Invent. Math. 45 (1978), 111–114, is the classical affine statement: a pure affine curve in affine n-space in positive characteristic is set-theoretically cut out by n−1 equations. The inherited assessment verified the [publisher record](https://doi.org/10.1007/BF01390268); it did not inspect the full proof. This recorded affine scope is not a projective or homogeneous-cone theorem. Applying an affine-surface lci theorem to the two-dimensional cone over a projective curve requires lci at the cone vertex, which is exactly the failure isolated by the next proof. A same-support affine pair also need not be homogeneous or have the required support at infinity. A search that fails to locate a universal projective theorem is not itself proof of its absence.

## The lci affine-surface theorem and its missing cone hypothesis

Das, *On a conjecture of Murthy*, Adv. Math. 331 (2018), 326–338, [Theorem 4.2 in the author manuscript](https://oldweb.isical.ac.in/~mrinal/Murthy_CI_v2.pdf), proves that a height-\(d-2\) locally complete-intersection ideal in \(\overline{\mathbf F}_p[X_1,\ldots,X_d]\), \(d\ge4\), is an STCI. Theorem 4.1 first constructs a same-support lci thickening with free conormal; at \(d=4\) the proof produces a rank-two projective module and uses Quillen–Suslin to make it free. The primary statement and this proof structure were checked in the inherited source assessment. This is an affine-space theorem with an lci hypothesis, not an assertion for arbitrary projective curves or arbitrary singular cones. [Publisher record](https://doi.org/10.1016/j.aim.2018.04.012).

## Exact obstruction to applying affine surface theorems to the cone

This is proved here and needs no literature extension.

Let `S=k[x0,x1,x2,x3]`, let `m=(x0,x1,x2,x3)`, and let `I` be the homogeneous prime ideal of an integral projective curve. If `I_m` is lci, it has two minimal generators because its height is two in the regular local ring `S_m`. The minimal number of generators equals

`dim_k(I/mI)`.

This is also the number of minimal homogeneous generators of `I`. Hence `I` has two homogeneous generators, so the projective curve is already a scheme-theoretic complete intersection. Thus the affine cone of every projective curve that is not a scheme-theoretic CI fails the lci hypothesis at the vertex. Smoothness of the projective curve does not fix this failure. For example, the twisted cubic is smooth, but its cone ideal has three quadratic minimal generators.

Even an affine same-support pair need not be homogeneous. A further argument is required to supply two homogeneous equations or to control the hyperplane at infinity.

## Exact audit of arXiv:2511.07589v1, Step 3

The source location is Theorem 4.2, Step 3, displayed sequence following equation (1); in the browser HTML it is lines 343--350. The problem is the substitution of `J/(c)` for the actual tensor quotient `J/cJ`.

Test the claimed operation on a complete intersection, over any field:

```
A = k[x,y,z],       J = (x,y),       c = x,
P = A^2,
f(1) = (-y,x),      g(a,b) = ax+by.
```

The sequence `0 -> A -> P -> J -> 0` is exact. Put `B=A/(x)=k[y,z]`. The preprint's proposed sequence with last term `J/(x)` becomes

```
B -> B^2 -> (y) -> 0,
t |-> (-yt,0),       (a,b) |-> by.
```

Its middle kernel is `B(1,0)`, while the preceding image is `yB(1,0)`. The middle homology is `B/(y)`, which is nonzero. Therefore that displayed sequence is not exact, even for this simplest CI ideal.

The actual tensor quotient has an extra torsion summand:

`J/xJ = (x,y)/(x^2,xy)`,

and the class of `x` is nonzero but annihilated by `y`. The natural quotient from `J/xJ` to `J/(x)` kills this summand. If the paper's notation `J/(c)` were instead interpreted as `J/cJ`, its assertion that this module is locally free of rank one would fail in the same example. Neither interpretation repairs the splitting step.

This is an exact algebraic countercheck of the proof, not an argument from parallel agreement or from the theorem's surprising breadth.

## Independent refutation of the unrestricted CI claim

This elementary example is proved here; it is outside the user's algebraically closed-field setting and is used solely to test the preprint's explicit *arbitrary Noetherian ring* claim.

Let

`A = R[x,y,z]/(x^2+y^2+z^2-1)` and `I=(x,y,z-1)`.

The algebra is a smooth two-dimensional real affine algebra, and `I` is the maximal ideal at the north pole. It is lci of height two. In `I/I^2`, the sphere equation gives `2(z-1)=0`, so `I/I^2` has basis the classes of `x,y` and is free of rank two over `A/I=R`.

Suppose `I=(f,g)`. On the real sphere `S^2`, the smooth map `F=(f,g):S^2 -> R^2` then has exactly one zero, the north pole. Since the two generators give a basis of `I/I^2`, its derivative at this zero is invertible, so the local winding number is `+1` or `-1`.

Here is a direct contradiction without invoking an Euler-class computation. On `R^2 \ {0}`, the form

`alpha = (u dv-v du)/(u^2+v^2)`

is closed. Remove a small disk around the north pole from `S^2`; `F^*alpha` is a smooth closed form on the remaining compact surface. Stokes's theorem forces its integral on the boundary to be zero. The invertible derivative forces that same integral to be `+2*pi` or `-2*pi`. Thus `I` cannot have two generators. It is lci with free conormal but is not a CI.

This disproves the preprint's unrestricted Theorem 4.4. It does not give a counterexample to projective STCI over an algebraically closed field.

## Why finite-field torsion does not settle the projective problem

Hartshorne--Polini, *Divisor class groups of singular surfaces*, [primary arXiv full text](https://arxiv.org/html/1301.3222), Proposition 7.1: if a curve meets the singular locus of its carrier surface only finitely, it is STCI on that surface precisely when `r[C]=m[H]` in `APic(X)` for positive integers `r,m`.

An elementary fixed-carrier counterexample to an overbroad torsion inference is a ruling line `L` on a smooth quadric `Q=P^1 x P^1`, over `Fpbar` or any algebraically closed field. Here `Pic^0(Q)=0`, `Pic(Q)=Z^2`, `[H]=(1,1)`, and `[L]=(1,0)`. There are no positive `r,m` with `r(1,0)=m(1,1)`. Thus `L` is not STCI on this chosen quadric, despite complete torsion of `Pic^0(Q)`. Of course the line is STCI in the ambient `P^3` using two planes. The example isolates the gap: finding a suitable carrier with the required full divisor-class relation remains additional work.

Kollar--Lieblich--Olsson--Sawin, *The Zariski topology, linear systems, and algebraic varieties*, [authors' book PDF](https://williamsawin.com/ReconstructionBook.pdf), Definition 7.1.1 and Theorem 7.1.10, prove that over a locally finite perfect field every irreducible curve has SCIP. In that terminology SCIP means that every finite closed subset of the curve can be obtained by intersecting the curve with an ambient effective divisor. It does not mean that the curve is the intersection of two ambient surfaces. The finite-field torsion used there concerns line bundles on the curve and cutting finite subsets. This theorem therefore supplies no hidden affirmative answer to the user's projective space-curve problem.


The tensor-quotient countercheck is an exact algebraic calculation in every characteristic. The real-sphere counterexample uses real topology and tests only the arbitrary-Noetherian-ring CI assertion. The fixed-quadric Picard obstruction holds over every algebraically closed field. These scopes remain distinct from each other and from the open fixed-quartic characteristic-zero question.


## The failed unique-prime inference in arXiv:2209.04489v1

Vahap Erdoğdu, *Radically finite rings and space curves*,
<https://arxiv.org/abs/2209.04489>, v1 submitted 2022-09-09, has no later version
in the inspected arXiv history. Its abstract and Corollary 4.4 assert that space
curves are not always STCI. The full proof is directly accessible at
<https://arxiv.org/html/2209.04489>, section 4, Theorem 4.3 and Corollary 4.4.
The corollary concerns the affine polynomial ring in three variables; it is not
an explicit integral projective-curve construction.

The theorem's argument first establishes a unique maximal ideal above an ideal
generated by two elements, then tries to establish that it is the unique
**prime** ideal above that ideal. The decisive inference is that a contraction
which is a G-ideal makes the prime above it maximal. The G-ideal condition gives
the existence of a maximal ideal with that contraction; it does not identify
every prime above the contraction with that maximal ideal.

### An elementary counterexample to that exact inference — PROVED HERE

Let k be any field and

\[
R=k[x,y]_{(x,y)},\qquad A=R[T].
\]

Then R is a finite-character UFD of dimension two: it is local, with unique
maximal ideal M=(x,y). In the displayed construction in the proof choose

\[
\Pi_1=x,\quad \Pi_2=y,\quad z=1-y,\quad f=T,
\quad g=y+(1-y)T.
\]

These choices satisfy every relation used there, including \(\Pi_2+z=1\).
The element 1-y is a unit of R. Consequently

\[
P^*=(x,g)\subset A
\]

is prime, because elimination of T gives

\[
A/P^*\simeq R/(x)\simeq k[y]_{(y)},\qquad
T\longmapsto-\frac{y}{1-y}.
\]

It has height two. It is properly contained in the height-three maximal ideal

\[
M^*=(x,y,T).
\]

For example y is nonzero in the displayed quotient, so y is not in P*. Since
P* is already prime,

\[
\sqrt{(\Pi_1,g)}=P^*\ne M^*.
\]

At the same time the quotient is local, so M* **is** its unique maximal ideal;
the paper's intermediate statement about the intersection of maximal ideals
holds in this example. This isolates the exact failure: a unique maximal ideal
does not make the smaller defining prime maximal. No appeal to computation is
needed.

The contraction \(P^*\cap R=(x)\) also satisfies the existential property of a
G-ideal used in the paper: the distinct maximal ideal
\((x,yT-1)\) of A contracts to (x), with quotient k(y). That existence does not
change the nonmaximal prime P* above the same contraction.

**Scope.** This disproves a particular implication in the proof, so the
negative-resolution corollary is unsupported by that proof. It does not prove
that every affine space curve is STCI, or that the theorem's whole statement is
false under every possible interpretation of “radically finite.” Searches did
not find a correction or a refereed replacement proof.
