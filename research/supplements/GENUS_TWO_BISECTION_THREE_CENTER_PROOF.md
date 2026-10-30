# Genus-two bisection: three-center fiber obstruction

## Dependency guide: odd fiber obstruction and surviving cases

This conditional argument excludes a **three-blowup fiber** by analyzing irreducible, reduced, and nonreduced fiber graphs, including the stated near-counterexample. It complements rather than duplicates [the even-fiber exclusion](GENUS_TWO_BISECTION_EVEN_FIBER_PROOF.md). Both require the second-pencil reduction and the smooth embedded lift; this proof also records that the parent's adversarial audit was pending. The surviving four-single-blowup partition and other global mate questions remain open here.

---


Permanent complete proof, retaining the original conditional status and numerical nonreduced-fiber near-counterexample.

# Genus-two bisections: the three-blowup fiber is impossible

Date: 2026-10-10. Author: `k3_fiber_enumeration`, independently
assigned by `bisection_local_fibers`. Status: **PROVED HERE,
conditional on the accepted second-pencil reduction and the smooth
embedded lift; awaiting the parent's separate adversarial audit**.
No canonical frontier file was edited.

This note excludes a fiber with blowup count `k_t=3`. It includes
nonreduced fibers and preexisting ADE exceptional components. It does
not by itself exclude the surviving four-single-blowup partition.

## 1. Exact input

Use the notation of the
[second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md).
The smooth weak del Pezzo surface V is the minimal crepant resolution
of its ADE double-cover model W. The connected rational pencils f
and c on V satisfy

    -K_V=f+c,  f.c=2.

The actual curve c on M is the pullback of the corresponding smooth
member on V. All four extra point blowups `alpha:M->V` have centers
disjoint from c, including every infinitely near center. On a fixed
fiber t having three of these centers, the actual equality is

    Z_t=(3/2)F_t-R_t,

where F_t is the entire scheme-theoretic fiber on M and R_t is the
actual relative canonical divisor, a sum of total exceptional
transforms. It is not permissible to replace F_t by its reduction.

Z_t is effective. Every prime in its positive support is an
f-vertical, sigma-exceptional smooth rational `(-2)` curve. Moreover
`L=c+Z` is numerically trivial on every such prime.

The smooth embedded lift supplies two local facts. A connected
sigma-exceptional graph contacted by c meets c at just one point,
on just one prime, transversely with intersection one. Pulling back
a local uniformizer of the smooth downstairs curve gives a positive
integral anti-nef exceptional cycle on this graph whose coefficient
on that contacted prime is one. These are conditions on actual local
functions, stronger than a rational numerical correction.

## 2. All possible V-fiber graphs

The fibers of a smooth rational pencil with nef anticanonical class
have the following forms:

1. One smooth rational component of square zero and multiplicity one.
2. A reduced chain with two `(-1)` ends and any number of intervening
   `(-2)` components, all multiplicities one.
3. A nonreduced tree with a unique `(-1)` component A of multiplicity
   two. Its other components are `(-2)`. There are two multiplicity-one
   leaves meeting a fork; from the fork to A there is a possibly empty
   chain of multiplicity-two components. If that chain is empty, A
   itself meets the two leaves.

Here is the contraction argument, including its applicability to
preexisting ADE degenerations. Contract vertical `(-1)` curves until
the rational pencil is a relatively minimal ruled surface. This is
the usual relative ruled-surface reduction; a primary proof uses this
sequence explicitly in [Tanaka, *Discriminant divisors for conic
bundles*, proofs of Propositions 6.1--6.2, PDF pages 41--43](https://arxiv.org/pdf/2308.08119).
After a contraction b, for each noncontracted curve C,

    (-K_new).b(C)=(-K_old).C+E.C >= 0.

Thus the anticanonical class stays nef at every intermediate stage.
Reverse the sequence over t. The first blowup of a smooth fiber gives
two `(-1)` components. A later blowup cannot touch a `(-2)` component,
since its strict transform would have negative anticanonical degree.
Blowing up a smooth point of a `(-1)` end extends the reduced chain.
The only allowed intersection blowup is the intersection of the two
`(-1)` curves when they are adjacent. That operation produces the
unique multiplicity-two `(-1)` curve with two multiplicity-one
`(-2)` leaves. Subsequent allowed blowups occur at a smooth point of
the unique `(-1)` curve and extend its multiplicity-two tail. This
proves the list and the displayed multiplicities directly.

Adjunction, or `c=-K_V-f`, now gives c-degree two on the irreducible
fiber, c-degree one on each `(-1)` component, and c-degree zero on
every old `(-2)` component. The new centers leave these c-degrees
unchanged, because they are c-disjoint.

## 3. The coefficient constraint fixes the allowed new centers

Every strict transform of a V-fiber component of multiplicity m has
coefficient `3m/2` in Z_t: R_t has no V-component. This coefficient is
strictly positive. Hence its final self-intersection must be `-2`.
In particular:

    old (-2) component: cannot be hit;
    old (-1) component: must be hit exactly once;
    old square-zero component: must be hit exactly twice.

At the creation of a new exceptional prime E, its fiber multiplicity
is the sum of the multiplicities of the components through the
center. Its R_t coefficient is one plus the sum of their R_t
coefficients. Thus

    coefficient_E(Z_t)=(3/2) multiplicity_E(F_t)-coefficient_E(R_t).

A positive-coefficient new exceptional curve also must be hit exactly
once after its creation to finish with square `-2`. A new curve with
negative coefficient is forbidden by effectivity. These simple rules
exhaust the three-center histories below; no degree-four rank bound
is needed.

## 4. Irreducible V fiber

The first center is a smooth point of its square-zero component A.
It creates E1 with fiber multiplicity one, R coefficient one and Z
coefficient `1/2`. A now has square `-1` and must be hit once more.

If the second center is another smooth point of A, the new E2 also
has Z coefficient `1/2`; E1 and E2 are disjoint `(-1)` curves and both
need another hit. One remaining blowup cannot hit them both. A smooth
point of E1 instead would produce multiplicity one and R coefficient
two, hence negative Z coefficient `-1/2`.

The only remaining second center is `A intersect E1`. It creates E2
with multiplicity two and R coefficient two, hence Z coefficient
one. A and E1 now both have square `-2`. The third center is forced
to be a smooth point of E2, since touching either of those other
curves would make its square less than `-2`. The third exceptional
curve E3 has multiplicity two, R coefficient three and Z coefficient
zero.

The positive graph is consequently the `A3` chain

    A -- E2 -- E1,
    Z coefficients: 3/2, 1, 1/2.

The unchanged intersection `c.A=2` contradicts the single transverse
contact with a connected exceptional graph. This includes the case
of one tangential contact of intersection two.

## 5. Reduced V fiber

Write A and B for its `(-1)` ends, each of c-degree one. They must
each be hit exactly once. Old `(-2)` components cannot be touched.

If the first center is a smooth point of A, it creates E1 with Z
coefficient `1/2`. The second center cannot be a smooth point of E1
(it would create coefficient `-1/2`) or the intersection `A intersect
E1` (it would hit A twice). It must therefore be a smooth point of B.
The resulting E2 has coefficient `1/2` and is disjoint from E1. The
third center cannot turn both into `(-2)` curves. The same argument
applies with A and B exchanged.

Therefore A and B must be adjacent and the first center must be their
intersection. Its exceptional E1 has multiplicity two, R coefficient
one and Z coefficient two. The second and third centers are forced
successive smooth points of the new exceptional curves, avoiding all
already final `(-2)` curves. They produce E2 and E3 of multiplicity
two, R coefficients two and three, and Z coefficients one and zero.

The positive graph is the `D4` star with central E1 and leaves A, B,
E2, carrying Z coefficients `2,3/2,3/2,1`. The curve c meets both A
and B with intersection one. They lie in the same connected
exceptional graph, contradicting the smooth embedded lift.

## 6. Nonreduced V fiber

Let A be its unique `(-1)` component, of multiplicity two and
c-degree one. Every other old component is `(-2)` and cannot be hit.
The first center is consequently a smooth point of A away from the
old components. It creates E1 with multiplicity two, R coefficient
one and Z coefficient two; A reaches square `-2`.

The second center is forced to be a smooth point of E1, creating E2
with multiplicity two, R coefficient two and Z coefficient one.
The third center is forced to be a smooth point of E2, creating E3
with multiplicity two, R coefficient three and Z coefficient zero.
All intersections with already final `(-2)` curves are forbidden.

The positive graph is a `D_n` graph, `n>=5`: retain all the old V
components, turn A into a `(-2)`, and append the two-vertex tail
`E1--E2`. The contact component A has coefficient three in Z_t. It
lies inside the long arm (or is the fork if the old double fiber had
only three components), and at least two vertices of the long arm
remain beyond A. In the shortest example the graph is `D5` and

    Z_t=3A+(3/2)(old leaf 1+old leaf 2)+2E1+E2.

This rational correction is numerically consistent; effectivity and
intersection numbers alone do not exclude it.

The actual uniformizer cycle does. Suppose a positive integral
anti-nef cycle Y on this graph had `Y_A=1`. At an internal long-arm
vertex having coefficient one, the `(-2)` anti-nef inequality reads

    2 >= coefficient(left neighbor)+coefficient(right neighbor).

Both neighboring coefficients are positive integers, so both must
be one. Propagate toward the fork. At the fork all three neighboring
coefficients are positive integers, and anti-nefness would require

    2 >= 1+1+1,

a contradiction. If A is the fork, this contradiction is immediate.
Hence no such cycle exists, contrary to the pulled-back uniformizer
of the smooth embedded curve. This is the fundamental-cycle
obstruction proved directly, without a graph-table assertion.

## 7. Conclusion and failure shield

Every possible V-fiber and every allowed three-center history leads
to a contradiction. Therefore `k_t=3` is impossible in the accepted
lambda-zero bisection mate reduction. Together with the separate
[even-count exclusion](GENUS_TWO_BISECTION_EVEN_FIBER_PROOF.md),
the only possible blowup-count partition is

    [1,1,1,1].

The nonreduced `D5` numerical example must remain visible: its
correction is effective and has `c.Z_t=3`. It fails because the
smooth embedded curve requires an actual integral anti-nef
uniformizer cycle of contact coefficient one. Replacing that local
condition by a mere rational divisor correction would leave the
example and invalidate the exclusion.

This result is conditional on the accepted characteristic-zero
second-pencil and smooth-lift reductions. It asserts neither a
global quartic-carrier exclusion nor a universal STCI theorem.
