# Characteristic-only addendum for the smooth-root theorem

Date: 2026-10-15. Reviewer: `new_logarithmic_review`.

Status: **PASS for the characteristic-free formal geometric theorem,
its numerical criterion, and the finite embedded-Cartier tower under
their explicit hypotheses. The actual-CI gap conclusion remains
conditional on the actual bridge being valid in the chosen
characteristic.**

This reviews only Section 10 of the
[owner note](2026-10-15-generalization-smooth-root-formal-nonexistence.md).
The completed
[characteristic-zero geometry audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md)
is a premise; its arguments and accepted computations were not replayed.
No characteristic-zero logarithmic argument, P010 calculation, or
normal-bundle splitting of the literal repository curve is imported.

## 1. The geometric inputs permit arbitrary algebraically closed k

- [Bost, geometric Theorem 3.5 and Corollary 3.8](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27)
  are stated over a field k without a characteristic restriction.
  Their smooth formal branch, complete positive-dimensional center,
  and ample-normal hypotheses remain exactly the ones already checked.
- [Hartshorne, Section 1 and Theorem 4.1](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=3)
  explicitly work over an algebraically closed field of arbitrary
  characteristic. The neighborhood-equivalence conclusion used in
  the accepted degree argument has that scope.
- Finite-type local rings over a field are excellent in every
  characteristic. Finite normalization and its completed-branch
  decomposition retain their hypotheses; see
  [Stacks, Lemma 15.110.8](https://stacks.math.columbia.edu/tag/0C2E).
- Algebraic surface resolution is available in every characteristic:
  [Stacks, Lipman's Theorem 54.14.5](https://stacks.math.columbia.edu/tag/0BGP)
  applies to finite-type surfaces over a field, as explained in the
  [chapter introduction](https://stacks.math.columbia.edu/tag/0ADX).
  The construction uses normalized point blowups over singular points,
  so it can preserve the regular neighborhood of the selected curve;
  see [Lemma 54.6.5](https://stacks.math.columbia.edu/tag/0BFZ).
  These modifications are projective here. Since an algebraically
  closed field is perfect, the resolved regular surface is smooth.

Normality, uniqueness of the normalization lift, surface intersection,
and adjunction do not require characteristic-zero division. The
formal surface is smooth because the **full** root divisor is smooth;
no nonvanishing fiber derivative or separability of its projection
is needed for this step.

## 2. Embedded hyperplanes avoid the inseparable-linear-system issue

For an integral S in P3 over algebraically closed k of any
characteristic, [Stacks, Lemma 37.32.3](https://stacks.math.columbia.edu/tag/0G4C)
gives an irreducible general hyperplane section. The smooth locus of
S is dense, and its immersion in P3 satisfies
[smooth Bertini, Lemma 33.47.3](https://stacks.math.columbia.edu/tag/0FD4)
in arbitrary characteristic. Thus a general section is generically
reduced. Being a plane hypersurface, it has no embedded components;
it is consequently integral. No arbitrary inseparable linear system
on a separate source is being used.

General planes meet the smooth embedded C transversely in e distinct
points in every characteristic. Indeed planes containing a tangent
line to C form an incidence image of dimension at most two in the
three-dimensional dual projective space. A general plane also avoids
the finite nongeneric-multiplicity locus on C. Wild ramification or
inseparability of another map does not change this incidence argument.

If Z->C is inseparable, its total degree is still r, and

    H.Z=deg pullback(O_C(1))=e*r.

The formula uses total field degree, including inseparable degree.
Likewise, W|E>=Z gives m>=r by intersection lengths on an exceptional
fiber. Neither calculation counts distinct geometric points in a
fiber of Z->C. Plane blowup adjunction and nonnegative arithmetic
genus then give the accepted lower bound in every characteristic.
No separable Puiseux expansion or ordinary-singularity assumption
enters that calculation.

## 3. Characteristic-free formal theorem and finite cutoff

The main formal theorem therefore holds over arbitrary algebraically
closed k: for a smooth rational C of degree e>=4 with the **explicit**
balanced normal bundle O_(P1)(2e-1)^2, every smooth Z of class (2,r),
r>=2, fails to extend as an embedded Cartier divisor through all
exceptional neighborhoods. The general numerical criterion and its
quadratic consequence retain the same rational-base, smoothness,
finiteness, and numerical assumptions.

The Euler and tangent sequence degree calculation is characteristic
free, so balance, when it actually holds, gives lambda=2e-1. This does
not establish balance for any particular curve in an exceptional
characteristic, or transfer an earlier splitting calculation.

The accepted tower's cohomological and functor proofs introduce no
characteristic restriction. Their inputs are the divisor sequence
on P1 x P1, multiplication by a nonzero fiber polynomial, vector-bundle
splitting and cohomology on P1, square-zero embedded-ideal lifting,
equation units, Nakayama, and noetherian stabilization. None divides
by a degree or factorial, takes a logarithm, or assumes a separable
root polynomial. Multiplication remains injective even when the
characteristic divides r, and the relative arguments include
nonreduced roots and parameter bases.

Thus lambda>3epsilon still supplies all-order uniqueness and the fixed
finite-type closed tower in any characteristic. For epsilon=2,e>=4,
lambda>=7>6. For each fixed actual embedding and r, combining this
tower with the formal theorem gives a finite N with

    K_N intersect U_smooth = empty

as a scheme. The cutoff is existential and is not uniform as r or
the actual embedding varies.

## 4. Positive-characteristic actual-CI consequence is conditional

The existing
[actual-CI bridge audit](2026-10-14-generalization-blowup-root-curve-bridge-independent-audit.md)
is explicitly stated in characteristic zero. Its generic-root argument
uses generic separability. In characteristic p, smoothness of the
whole root does not by itself imply this: the local equation
v^p-t=0 is smooth over k but its projection to the t-line is
inseparable. The formal nonexistence theorem above needs no such
separability, but it must not silently extend that earlier bridge.

Whenever a valid bridge in the chosen characteristic supplies the
local strict ideal

    (h,u^(s-r)),

with all its other actual hypotheses, the indexing argument is purely
algebraic. It supplies every stage m<s-r. The
empty stage N therefore forces

    s-r<=N, equivalently s<=r+N.

At equality only stage N-1 is supplied. The addendum does not assert
that arbitrary positive-characteristic actual CIs satisfy this local
bridge, nor that they are excluded. A separate bridge extension may
use additional hypotheses or a direct local proof; it is outside
this characteristic-only review.

No accepted verifier, CAS calculation, first/second class computation,
commit, or memory write was performed. Singular or nonreduced roots,
unbalanced normal bundles, and unrestricted STCI remain outside this
conclusion.
