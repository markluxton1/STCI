# Genus-two bisection: three-center fiber obstruction

**Scope.** Conditional characteristic-zero obstruction for a fiber with three of the four extra blowup centers, including nonreduced fibers and infinitely near centers. It assumes the second-pencil reduction and smooth embedded lift stated below. This argument alone leaves the four-single-center partition; the [global ribbon argument](genus_two_bisection_proof.md) independently excludes the entire bisection lane. The [carrier assembly](quartic_carrier_proof.md) gives the all-degree quartic-carrier conclusion.

## 1. Exact input

Use the second-pencil setup of the [global bisection proof](genus_two_bisection_proof.md).
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

Every permitted fiber and three-center history contradicts the accepted characteristic-zero \(\lambda=0\) bisection mate reduction: \(k_t=3\) is impossible. With the separate [even-count exclusion](../../frameworks/carrier-normalization/quartic_proof_interfaces.md#bisection-with-an-even-fiber-count), only \([1,1,1,1]\) remains.

The nonreduced \(D_5\) near-counterexample has effective correction and \(c\cdot Z_t=3\), but violates the **integral anti-nef uniformizer cycle of contact coefficient one** required by the smooth embedded curve. Rational divisor correction alone would not exclude it. This local calculation is not itself a global quartic-carrier exclusion; that conclusion uses the independent global ribbon argument and carrier assembly.



---

## Additional fiber-type checks and conditional four-single-center route

### Genus-two bisection local fibers: independent verification

The first four sections analyze fiber types and center histories; the proposed global route is not an established proof. The global ribbon argument independently excludes the bisection lane.

#### 1. Precise input and verdict

In characteristic zero, the [second-pencil hypotheses](#source-2026-10-10-session-genus-two-bisection-second-pencil-independent-auditmd) give a smooth weak degree-four del Pezzo \(V\), connected rational pencils \(f,c\), \(-K_V=f+c\), \(f\cdot c=2\), and \(M\to V\) consisting of four blowups disjoint from the smooth embedded \(c\), including infinitely near centers. For a hypothetical \(\lambda=0\) mate, \(Z_t=(k_t/2)F_t-R_t\) is an **actual rational-divisor equality** with full fiber multiplicities. Its positive support consists of vertical exceptional \((-2)\)-curves; a contacted graph has one transverse \(c\)-contact, with positive integral anti-nef uniformizer cycle having coefficient one there. The separate three-blowup theorem excludes every \(k_t=3\) fiber; the [even-count exclusion](../../frameworks/carrier-normalization/quartic_proof_interfaces.md#bisection-with-an-even-fiber-count) then leaves \([1,1,1,1]\). This does **not** use conductor power descent or prove a mate exclusion.

#### 2. The fiber list includes all multiplicities

The source's relative contraction argument is sufficient. Contracting a
vertical (-1)-curve E preserves anticanonical nefness: for an uncontracted
curve C, the anticanonical degree of its image increases by `E.C`.
Reverse a contraction sequence to a ruled surface. Starting from a
smooth square-zero fiber, the first blowup produces two (-1)-components.
An intermediate (-2)-component cannot be touched while anticanonical
nefness is retained. Smooth blowups at a (-1)-end extend a reduced chain;
the intersection of two adjacent (-1)-components can instead be blown
up once, creating a multiplicity-two (-1)-component with two
multiplicity-one (-2)-leaves. Subsequent smooth blowups extend the
multiplicity-two tail.

Thus the irreducible square-zero, reduced-chain, and nonreduced D-tail
fiber types exhaust the possibilities on V, including preexisting ADE
exceptional components. This argument does not assume that a degenerate
conic is reduced, and does not impose a root-rank bound.

#### 3. Independent check of the three-center histories

An original V-component of multiplicity m has no coefficient in the
relative canonical divisor R. Its strict transform therefore has Z
coefficient `3m/2>0` and must finish with square -2. Old (-2)-components
cannot be hit, old (-1)-components must be hit once, and a square-zero
component must be hit twice. At a new center, the fiber multiplicity is
the sum of the multiplicities of components through it; the relative
canonical coefficient is one plus their relative canonical coefficients.
These rules use the actual total transforms and remain valid at
intersection centers.

The irreducible case has just one possible complete history: a smooth
blowup of the old component, an intersection blowup of that component
with the new exceptional, and a smooth blowup of the next exceptional.
The positive graph is A3, with unchanged total c-contact two. The
reduced case can finish only when the two old (-1)-ends were adjacent
and were blown up together; two further smooth blowups produce D4.
Its two old ends both meet c once, in the same exceptional graph. Both
cases violate the actual smooth-lift condition.

In the nonreduced case the three centers are forced smooth successive
points starting on the unique multiplicity-two (-1)-component A. The
positive graph is D_n, with A internal on the long arm, or at its fork.
The shortest graph is D5 and its correction is

    3A+(3/2)(U+V)+2E1+E2.

This correction is effective, numerically anti-nef after adding c, and
has `c.Z_t=3`. The numerical data alone do not exclude it. If an actual
uniformizer cycle had coefficient one at A, the (-2) anti-nef inequality
would force both adjacent coefficients to be one. Propagation along the
old multiplicity-two tail reaches a trivalent vertex with coefficient
one, where `2>=1+1+1` is impossible. This verifies the required local
contradiction without using a fundamental-cycle table.

#### 4. Failure shield: one blowup need not start with a reduced node

It would be false to infer locally that k=1 forces a reduced nodal fiber.
For example, on V take a multiplicity-two (-1)-component A with two
multiplicity-one (-2)-leaves U,V. Blow up a smooth point of A disjoint
from c. On M,

    F=2A+U+V+2E,   R=E,
    Z=(1/2)F-R=A+(U+V)/2.

The new E has square -1 and zero Z coefficient; the positive graph is
A3, contacted at its middle component A. The positive integral
anti-nef cycle with all three coefficients one is compatible with the
local uniformizer condition. This is a local consistency example, not
a globally realized quartic or mate.

Consequently any exclusion of nonreduced k=1 fibers must use a global
constraint, not the three-blowup proof or a local smoothness shortcut.

#### 5. Proposed global route for the four-single-blowup partition

The following additional route is supplied to the root for a separate
audit; it is not needed for the accepted Sections 1--4.

The finite double cover `W->P1_f x P1_c` has branch equation of bidegree
(2,2), quadratic in the second coordinate. Its discriminant is a
nonzero degree-four section on the f-base. Nonzeroness follows from
the integral smooth general f-fiber. Each supported k=1 fiber must
already be degenerate on V: an irreducible square-zero component would
have positive Z coefficient after only one hit and would have square
-1 rather than -2. Four distinct supported fibers therefore require
four discriminant zeros. Degree four forces each zero to be simple.

A simple discriminant zero gives a nonzero quadratic with one double
root, and the total double-cover surface is regular at the corresponding
node. Every degeneration is thus a simple reduced nodal conic. In
particular the branch curve is smooth: a singular branch point would
give a discriminant zero of multiplicity at least two. A smooth branch
divisor of class (2,2) is connected and hence irreducible; it is a smooth
genus-one curve. The local node blowup is forced, and each of the four
nodes lies on the ramification curve of the double cover.

The ramification curve on V is the anticanonical divisor `-K_V=f+c`.
Its proper transform through the four node blowups is an effective
integral anticanonical divisor on M and remains a smooth genus-one
curve. The actual ambient conic model supplies an effective divisor
`D_M=-K_M`, pulled back from the entire conductor. The
[unique-anticanonical-section argument](../../frameworks/carrier-normalization/quartic_proof_interfaces.md#15-genus-two-conductor-line-positions-on-the-fixed-quartic)
would identify D_M with this irreducible genus-one curve. To check that
argument directly, tensor the basepoint-free f-pencil sequence by -K.
An effective section of `-K-f` would write `L=2f+T` and impose a
nonzero quadric equation on the actual quartic image via three squares.
Thus `H0(-K-f)=0`. Two independent anticanonical sections would then
give four independent products with the two f-sections, a basis of
`H0(L)`, and a Segre quadric on the image. Hence `h0(-K)=1`.

If the entire upstairs conductor has already been proved reduced split
with two rational components, its pulled-back divisor cannot be the
single irreducible genus-one curve just obtained. This would exclude
`[1,1,1,1]` and complete an alternative structural bisection exclusion.
The discriminant-to-entire-conductor identification, and any possible
horizontal contraction, should be checked explicitly before relying on
this argument. A separate global Cartier-double-ribbon obstruction is
currently under independent audit and may supersede this longer route.

#### 6. Independent check of the proposed ribbon alternative

The root also proposed a short obstruction using the actual Cartier
double `2c_S~2H`. A CM double curve with reduction a smooth P1 has a
square-zero nilradical: its square is generically zero, hence finite
support, and a CM curve has no nonzero finite-support subsheaf. The
nilradical is rank-one torsion-free on P1, so it is a line bundle.
From `chi(O_S(mH))=2m^2+m+1`, the Cartier exact sequence gives double
curve polynomial `8m-6`. Subtracting the reduced curve polynomial
`4m+1` gives nilradical `O_P1(-8)`.

For the literal curve C0, the normal bundle is `O(7) direct_sum O(7)`.
An independent hand calculation is as follows. The quadratic syzygies
of `[s^4,s^3t,st^3,t^4]` are

    (st,-s^2,0,0), (t^2,-st,0,0), (0,t^2,-s^2,0),
    (0,0,st,-s^2), (0,0,t^2,-st).

On s=1 their differential images in `Omega_P1(6)=O(4)` are
`-1,-t,-2t^2,-t^3,-t^4`, times dt. The differential map is therefore
an isomorphism on global sections in characteristic different from
two. Consequently `H0(N^*(6))=H0(N(-8))=0`, and determinant `O(14)`
forces the asserted splitting.

The morphism from the double to P3 induces a global map
`I_C0/I_C0^2 -> O(-8)`. This map is generically surjective outside
the conductor, where normalization is an isomorphism and the double
is the actual Cartier double of c. Its Hom group is nevertheless zero,
since `Hom(O(-7)^2,O(-8))=H0(O(-1))^2=0`. The construction needs no
global closed immersion of the double into P3. This corroborates the
root's proposed obstruction; its final acceptance is assigned to the
separate full auditor and is not asserted by this local-fiber record.


---

