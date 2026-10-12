# Genus-two bisection local fibers: independent audit and remaining structural route

Date: 2026-10-10 local time; written at 2026-10-11T01:17 UTC.
Auditor: `bisection_local_fibers`. Status of Sections 1--4:
**PROVED HERE / independent audit passed**, conditional on the explicitly
accepted second-pencil and smooth-embedded-lift reductions. Section 5 is a
separate structural proposal requiring its own audit. No canonical file
is edited, and this note asserts no universal STCI theorem.

Audited source:
[three-blowup fiber exclusion](2026-10-10-session-genus-two-bisection-three-blowup-fiber-exclusion.md),
SHA256 `f7177554d64e14a30d169daaedee7ff2ebcc51ed8b3d8435ed590369d9f24103`.
The present auditor independently checked every coefficient, center
restriction, and final contact contradiction. This is a mathematical
audit; no CAS execution or new symbolic-check count is claimed.

## 1. Precise input and verdict

Use the characteristic-zero notation of the
[second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md).
There is a smooth weak degree-four del Pezzo surface V, with connected
rational pencils f and c satisfying `-K_V=f+c` and `f.c=2`. The smooth
minimal resolution M is obtained from V by four point blowups disjoint
from the actual smooth curve c, including every infinitely near center.
For a hypothetical lambda-zero mate,

    Z_t=(k_t/2)F_t-R_t,

is an actual equality of rational divisors, with full scheme-theoretic
fiber multiplicities. The positive support of Z consists of
sigma-exceptional vertical (-2)-curves. A contacted exceptional graph
has only one transverse c-contact, and the actual pullback of a local
uniformizer supplies a positive integral anti-nef exceptional cycle
whose coefficient at that contact is one.

The three-blowup note is accepted at exactly this scope: **every fiber
with k_t=3 is impossible**. Combining it with the independently checked
[even-count exclusion](2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md)
leaves only `[1,1,1,1]`. This conclusion does not yet use conductor power
descent, the splitting of the conductor, or the fixed embedding of C0.

## 2. The fiber list includes all multiplicities

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

## 3. Independent check of the three-center histories

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

## 4. Failure shield: one blowup need not start with a reduced node

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

## 5. Proposed global route for the four-single-blowup partition

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
[unique-anticanonical-section argument](2026-10-10-session-genus-two-conductor-line-position.md)
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
horizontal contraction, should be checked explicitly before promoting
this section. A separate global Cartier-double-ribbon obstruction is
currently under independent audit and may supersede this longer route.

## 6. Independent check of the proposed ribbon alternative

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
