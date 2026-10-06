# Positive-characteristic literature audit, 2026-10-06

Status: primary-source literature audit and an exact audit of an unrefereed proof. No universal projective STCI theorem is asserted. This note was prepared independently of the agents working on the characteristic-zero computation frontier.

## Conclusions and scope

The search did not locate a primary-source theorem proving that every integral curve in `P^3` is an STCI either over an arbitrary algebraically closed field of positive characteristic or over `Fpbar`. A failed search is not a proof of open status. The positive results actually found have extra hypotheses or are affine. Two particularly tempting apparent shortcuts fail for precise reasons recorded below.

1. Cowsik--Nori concerns affine curves, not projective curves or their two-dimensional cones.
2. Moh concerns all projective monomial curves in characteristic `p>0`, and curves admitting a birational linear plane projection with center disjoint from the curve and only cusps in the plane image. It does not state that every projective curve admits such a projection.
3. Das's peer-reviewed theorem already proves STCI for lci surfaces in affine space over `Fpbar`; a non-CI projective space curve has a cone that is not lci at its vertex.
4. A 2025 Mandal--Zinna preprint states a broader affine result, but its displayed splitting argument fails an elementary exactness test. Its unrestricted claims should be recorded as claims with an invalid proof, not imported as established theorems.
5. Torsion in the degree-zero Picard group over `Fpbar` does not remove the Neron--Severi obstruction to a curve being STCI on a specified surface. A different literature term, the *set-theoretic complete intersection property* (SCIP), concerns cutting finite subsets on a curve and must not be confused with cutting the curve by two surfaces.

## Primary sources checked

### Cowsik--Nori and the projective special families

R. C. Cowsik and M. V. Nori, *Affine curves in characteristic p are set theoretic complete intersections*, Invent. Math. 45 (1978), 111--114. The [publisher record](https://link.springer.com/article/10.1007/BF01390268) confirms the bibliographic data; the full paper was not accessible through the browser. The theorem is affine: a pure affine curve in affine `n`-space in characteristic `p` is set-theoretically cut out by `n-1` equations. The affirmative projective conclusion does not occur in the title or in the accessible primary record.

T. T. Moh, *Set-theoretic complete intersections*, Proc. AMS 94 (1985), 217--220. The [AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/) directly states two results: projective monomial curves over a characteristic-`p` field are STCI; and a curve over an algebraically closed characteristic-`p` field is STCI if it has a birational linear plane projection, with center disjoint from the curve, whose image has only cusps. Its references include Hartshorne's *Complete intersections in characteristic p>0*, Amer. J. Math. 101 (1979), 380--383, and Ferrand's 1979 chapter. Hartshorne's [JSTOR record](https://www.jstor.org/stable/2373984) was found, but its full text was not accessible. The universal monomial-family scope is verified directly in Moh, rather than extrapolated from Hartshorne.

### Das: the established affine surface theorem

Mrinal Kanti Das, *On a conjecture of Murthy*, Adv. Math. 331 (2018), 326--338, DOI 10.1016/j.aim.2018.04.012. The [publisher abstract](https://www.sciencedirect.com/science/article/pii/S000187081830152X) explicitly gives the lci affine-surface application. The [author PDF](https://oldweb.isical.ac.in/~mrinal/Murthy_CI_v2.pdf), accessible through indexed primary-source search text, gives Theorem 4.2: an lci ideal of height `d-2` in `Fpbar[X1,...,Xd]`, `d>=4`, is STCI. Theorem 4.1 first constructs a same-support lci thickening with free conormal. For `d=4`, the proof produces a rank-two projective module and invokes Quillen--Suslin to make it free. This is affine space and requires the lci hypothesis.

### Mandal--Zinna: published and preprint statements are distinct

The separate published paper *Set-theoretic complete intersection for smooth surfaces in a smooth affine algebra*, J. Algebra 693 (2026), 36--53, DOI 10.1016/j.jalgebra.2025.12.026, has a [primary publisher abstract](https://www.sciencedirect.com/science/article/abs/pii/S0021869326000165). Its surface result is conditional: smooth affine ambient algebra over `Fpbar`, trivial conormal, and torsion class in the Grothendieck group. Several formulas in the browser's introduction extract are missing, so this audit does not claim to have verified the precise dimension inequality of every numbered theorem.

The [arXiv v1 full text](https://arxiv.org/html/2511.07589v1) of *On set-theoretic complete intersections for smooth curves in three-dimensional affine schemes* was inspected directly. Theorem 4.8 claims STCI for any height-two lci ideal in a four-dimensional affine algebra over `Fpbar`. Theorem 4.4 also claims CI for a height-two lci ideal with free conormal in any Noetherian ring of dimension at least two. Theorem 4.8 reuses the proof of Theorem 4.2. The exactness audit below invalidates that argument. This audit refutes the unrestricted Theorem 4.4; it does not by itself refute every field-restricted STCI assertion in the preprint.

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

## Continuation implications

- Preserve the affine/projective and lci-cone boundaries in the ledger.
- Replace any reliance on the broad 2025 preprint with the established affine results whose hypotheses have actually been checked.
- If the broad preprint is retained, attach this exact proof audit and distinguish its claimed results from verified theorems.
- Over `Fpbar`, a useful affirmative route would still have to construct a carrier or a homogeneous thickening satisfying the full divisor relation; degree-zero Picard torsion alone is insufficient.
- No changes to canonical research files were made by this audit agent.
